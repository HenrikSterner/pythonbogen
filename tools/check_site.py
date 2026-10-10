from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "bogen.html", "laeseproeve.html", "vygotskai.html", "laboratorier.html", "undervisere.html", "kom-i-gang.html", "om.html"]
ERRORS: list[str] = []
PAGE_IDS: dict[str, set[str]] = {}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.h1_count = 0
        self.images_without_alt = 0
        self.empty_hash_links = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            if values["id"] in self.ids:
                ERRORS.append(f"Dobbelt id #{values['id']}.")
            self.ids.add(values["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "img":
            if "alt" not in values:
                self.images_without_alt += 1
        for key in ("href", "src", "poster"):
            if values.get(key):
                self.references.append((key, values[key] or ""))
                if tag == "a" and values[key] == "#":
                    self.empty_hash_links += 1


def local_target(base: Path, url: str, current_file: Path | None = None) -> tuple[Path | None, str]:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or url.startswith(("/", "//")):
        return None, parsed.fragment
    target = (base / unquote(parsed.path)).resolve()
    if not target.is_relative_to(ROOT):
        ERRORS.append(f"Lokal sti fører uden for projektmappen: {url} i {base}.")
        return None, parsed.fragment
    if not parsed.path and current_file:
        target = current_file.resolve()
    return target, unquote(parsed.fragment)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    for page in PAGES:
        path = ROOT / page
        if not path.is_file():
            ERRORS.append(f"Mangler side: {page}")
            continue
        raw = path.read_text(encoding="utf-8")
        if "{{" in raw:
            ERRORS.append(f"Uforløst skabelonmarkør i {page}")
        parser = PageParser()
        parser.feed(raw)
        parser.close()
        PAGE_IDS[page] = parser.ids
        if parser.h1_count != 1:
            ERRORS.append(f"{page} har {parser.h1_count} hovedoverskrifter (forventede én).")
        if parser.images_without_alt:
            ERRORS.append(f"{page} har {parser.images_without_alt} billeder uden alt-attribut.")
        if parser.empty_hash_links:
            ERRORS.append(f"{page} har {parser.empty_hash_links} døde href=#-links.")
        for attribute, url in parser.references:
            target, fragment = local_target(ROOT, url, path)
            if target is None:
                continue
            if not target.is_file():
                ERRORS.append(f"Mangler lokal {attribute}: {page} → {url}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_parser = PageParser()
                target_parser.feed(target.read_text(encoding="utf-8"))
                target_parser.close()
                if fragment not in target_parser.ids:
                    ERRORS.append(f"Mangler fragment #{fragment}: {page} → {url}")

    for page in sorted((ROOT / "labs").glob("*.html")):
        if page.name != "index.html":
            raw = page.read_text(encoding="utf-8")
            parser = PageParser()
            parser.feed(raw)
            parser.close()
            if parser.images_without_alt:
                ERRORS.append(f"Laboratoriet {page.name} har billeder uden alt-attribut.")
            for attribute, url in parser.references:
                target, _ = local_target(page.parent, url, page)
                if target is not None and not target.is_file():
                    ERRORS.append(f"Mangler lokal lab-afhængighed: labs/{page.name} → {url}")

    lab_data = json.loads((ROOT / "data" / "labs.json").read_text(encoding="utf-8"))
    chapters = json.loads((ROOT / "data" / "chapters.json").read_text(encoding="utf-8"))
    if len(lab_data) != 8:
        ERRORS.append(f"Laboratoriekataloget indeholder {len(lab_data)} poster i stedet for 8.")
    if len(chapters) != 16:
        ERRORS.append(f"Kapiteloversigten indeholder {len(chapters)} kapitler i stedet for 16.")
    for entry in lab_data:
        if not (ROOT / "labs" / entry["href"]).is_file():
            ERRORS.append(f"Laboratoriets destinationsfil mangler: {entry['href']}")
    for preview in ["forord.html", "01-dit-foerste-program.html"]:
        path = ROOT / "laeseproeve" / "kapitler" / preview
        if not path.is_file():
            ERRORS.append(f"Mangler læseprøve: {preview}")
        else:
            rendered = path.read_text(encoding="utf-8")
            if "raw-typst" in rendered or "&lt;u&gt;" in rendered:
                ERRORS.append(f"Læseprøven viser kilde-layoutmarkører eller HTML-tags: {preview}")

    stylesheet = ROOT / "assets" / "css" / "site.css"
    if stylesheet.exists():
        for match in re.finditer(r"url\((?:['\"])?([^'\")]+)", stylesheet.read_text(encoding="utf-8")):
            url = match.group(1).strip()
            if url.startswith(("data:", "http:", "https:", "#")):
                continue
            target, _ = local_target(stylesheet.parent, url)
            if target is not None and not target.is_file():
                ERRORS.append(f"Mangler CSS-afhængighed: assets/css/site.css → {url}")

    if ERRORS:
        for error in ERRORS:
            print("FEJL: " + error)
        print(f"Validering afbrudt med {len(ERRORS)} fejl.")
        return 1
    print(f"Validering bestået: {len(PAGES)} sider, {len(chapters)} kapitler, {len(lab_data)} laboratorier, lokale links og prøveuddrag.")
    print("Laboratoriernes lokale scripts, styles og billeder er kontrolleret; denne kontrol starter ikke selve labværktøjerne.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
