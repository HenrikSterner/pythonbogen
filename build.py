from __future__ import annotations

import csv
import html
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CODE = ROOT.parent
BOOK = CODE / "PYTHONBook"
OLD = CODE / "python-i-gymnasiet"
TUTOR = CODE / "VygotskAI-Tutor"
SOURCE = ROOT / "site_src"

PAGE_TITLES = {
    "index": ("Bog, lokal AI og PyLabs til gymnasiet og folkeskolen", "Python-undervisning til gymnasiet og folkeskolen: lærebog, 100% lokal VygotskAI Tutor og integrerede PyLabs. Læs forordet gratis eller vælg e-bogen til 149 kr."),
    "bogen": ("Lærebogen", "Se bogens 16 kapitler, opgavetyper og den faglige progression fra dit første program til større projekter."),
    "laeseproeve": ("Læs en prøve", "Læs forordet og det første kapitel fra Introduktion til Python i Gymnasiet."),
    "vygotskai": ("VygotskAI", "Se hvordan bog, Python-opgaver, kode og lokal AI-tutor mødes i VygotskAI."),
    "laboratorier": ("Python-laboratorier", "Læs om alle 41 PyLabs i VygotskAI-Tutorens katalog: spil, softwaremodellering, algoritmer, data, maskinlæring og agentbaserede modeller."),
    "undervisere": ("Til undervisere", "Se bogens faglige progression, afprøv et forløbsforslag og udforsk laboratorier og lærerstøtte."),
    "kom-i-gang": ("Kom i gang med Python", "Vælg en begynderrute med læseprøve, Python-laboratorier eller den lokale VygotskAI-app."),
    "om": ("Forfattere og kontakt", "Mød Kathrine Bohus Madsen og Henrik Sterner: undervisere med erfaring i læring, programmering og AI. Kontakt os om Pythonbogen til gymnasiet og folkeskolen."),
}

CHAPTERS = [
    ("01-dit-foerste-program.md", "Dit første program", "Sæt et udviklingsmiljø op, skriv Python, og følg vejen fra instruktion til resultat.", "Kom i gang"),
    ("02-variabler-og-deres-datatyper.md", "Variabler og deres datatyper", "Gem og undersøg tal, tekst og andre værdier.", "Kom i gang"),
    ("03-forgreninger-betinget-udfoerelse.md", "Forgreninger og betinget udførelse", "Lad et program vælge mellem forskellige handlinger.", "Kom i gang"),
    ("04-loekker-og-lister.md", "Løkker og lister", "Gentag instruktioner, og arbejd med samlinger af værdier.", "Kom i gang"),
    ("05-funktioner.md", "Funktioner", "Del programmer op i genbrugelige, navngivne opgaver.", "Kom i gang"),
    ("06-rekursion.md", "Rekursion", "Undersøg funktioner, der løser et problem gennem mindre delproblemer.", "Struktur og genbrug"),
    ("07-objektorienteret-programmering.md", "Objektorienteret programmering", "Arbejd med klasser, objekter og sammenhænge mellem kode og model.", "Struktur og genbrug"),
    ("08-oop-og-biblioteker-i-praksis.md", "OOP og biblioteker i praksis", "Saml kode i større programmer med klasser og biblioteker.", "Struktur og genbrug"),
    ("09-regulaere-udtryk.md", "Regulære udtryk", "Find mønstre i tekst og bearbejd dem med Python.", "Struktur og genbrug"),
    ("10-arkitektur-for-brugerhaandtering.md", "Arkitektur for brugerhåndtering", "Undersøg hvordan systemer opdeler data, logik og præsentation.", "Systemer og data"),
    ("11-arkitektur-for-dataudtraek-gennem-api.md", "Arkitektur for dataudtræk gennem API", "Arbejd med strukturerede data og dataudtræk gennem API'er.", "Systemer og data"),
    ("12-maskinlaering.md", "Maskinlæring", "Undersøg data, modeller og klassifikation.", "Undersøg og afprøv"),
    ("13-webscrabing.md", "Webscraping", "Find og bearbejd struktureret indhold fra websider.", "Undersøg og afprøv"),
    ("14-test-i-python.md", "Test i Python", "Afprøv kode systematisk, og brug fejl til at forbedre løsningen.", "Undersøg og afprøv"),
    ("15-samarbejde-gennem-github.md", "Samarbejde gennem GitHub", "Følg ændringer og arbejd videre med kode i samarbejde med andre.", "Undersøg og afprøv"),
    ("16-opgavesamling.md", "Opgavesamling", "Vælg flere opgaver på tværs af bogens emner.", "Undersøg og afprøv"),
]

LAB_DETAILS = {
    "turtle-laboratorium.html": dict(topics=["begynder", "visualisering"], level="Begynder", prerequisites="Ingen forudsætninger. Start med enkle instruktioner og eksempler.", goal="Undersøg hvordan en sekvens, en løkke eller en funktion kan ændre et tegnet mønster.", chapter="Kapitel 1–5", feature="🐢"),
    "kryds-og-bolle-laboratorium.html": dict(topics=["spil", "algoritmer"], level="Begynder · videre", prerequisites="Du kan begynde med spillet og gå videre med strategier og kode.", goal="Afprøv spillets regler, og undersøg hvordan en strategi vælger sit næste træk.", chapter="Kapitel 1–5", feature="✳"),
    "diagram-editor.html": dict(topics=["systemer", "diagrammer"], level="Begynder · videre", prerequisites="Ingen forudsætninger for at tegne klasser; kode kræver grundlæggende Python.", goal="Tegn klasser og relationer, og sammenhold din model med genereret kode.", chapter="Kapitel 7–8", feature="▱"),
    "blockly-python.html": dict(topics=["begynder", "visualisering"], level="Begynder", prerequisites="Ingen forkundskaber. Byg logik med blokke.", goal="Flyt og forbind blokke, og undersøg hvilken Python-struktur de beskriver.", chapter="Kapitel 1–5", feature="▦"),
    "code-visualizer.html": dict(topics=["begynder", "visualisering", "algoritmer"], level="Begynder · videre", prerequisites="Vælg et af eksemplerne, eller følg programmets trin.", goal="Følg en Python-eksekvering trin for trin, og se variabler, kald og output ændre sig.", chapter="Kapitel 1–6", feature="⌁"),
    "knn-laboratorium.html": dict(topics=["data", "ai", "maskinlæring"], level="Videre", prerequisites="Kendskab til koordinater er nyttigt, men ikke et krav for at flytte punkter.", goal="Flyt datapunkter og justér k, så du kan undersøge naboer, klassifikation og outliers.", chapter="Kapitel 12", feature="◎"),
    "agent-simulator.html": dict(topics=["simulation", "ai"], level="Videre · fordybelse", prerequisites="Start med simulatoren; udvalgte kodeprojekter kræver Python.", goal="Ændr agenternes regler, og undersøg hvilke samlede bevægelser og mønstre der opstår.", chapter="Kapitel 7–8", feature="◌"),
    "robot-laboratorium.html": dict(topics=["simulation", "algoritmer"], level="Begynder · videre", prerequisites="Start med de færdige roboteksempler og udforsk sensorerne.", goal="Sammenhold robotternes sensorinput med de beslutninger, der styrer deres bevægelser.", chapter="Programmering og informatik", feature="↗"),
}


def copy_tree(source: Path, destination: Path) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)


def render_inline(text: str) -> str:
    text = html.escape(text.replace("kontakt@pythonbog.dk", "kontakt@pythonbogen.dk"), quote=False)
    text = re.sub(r"&lt;u&gt;(.+?)&lt;/u&gt;", r"<u>\1</u>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', text)
    return text


def chapter_html(filename: str, preview_heading: str) -> str:
    raw = (BOOK / "content" / "chapters" / filename).read_text(encoding="utf-8-sig")
    raw_lines = []
    in_task_source = False
    task_start = re.compile(r'<!--raw-typst\s+#task-block\(title:\s*"([^"]+)"[^]]*\)\[\s*-->(.*)')
    task_end = re.compile(r"<!--raw-typst\s+\]\s*-->")
    for source_line in raw.splitlines():
        match = task_start.search(source_line)
        if match:
            raw_lines.append(f"### {match.group(1)}")
            remainder = match.group(2)
            end = task_end.search(remainder)
            if end:
                raw_lines.append(remainder[:end.start()].strip())
                if remainder[end.end():].strip():
                    raw_lines.append(remainder[end.end():].strip())
            else:
                in_task_source = True
                if remainder.strip():
                    raw_lines.append(remainder.strip())
            continue
        if in_task_source:
            end = task_end.search(source_line)
            if end:
                if source_line[:end.start()].strip():
                    raw_lines.append(source_line[:end.start()].strip())
                if source_line[end.end():].strip():
                    raw_lines.append(source_line[end.end():].strip())
                in_task_source = False
            else:
                raw_lines.append(source_line)
            continue
        raw_lines.append(source_line)
    output: list[str] = []
    paragraph: list[str] = []
    list_tag = ""
    fence: list[str] = []
    in_fence = False
    fence_lang = "text"
    in_typst = False
    in_task = False
    task_title = ""
    task_content: list[str] = []
    task_pattern = re.compile(r'<!--raw-typst\s+#task-block\(title:\s*"([^"]+)"[^]]*\)\[\s*-->\s*(.*)')
    task_end = re.compile(r"<!--raw-typst\s+\]\s*-->")
    output_pattern = re.compile(r'<!--raw-typst\s+#program-output\("(.*?)"\)\s*-->', re.S)
    image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

    def close_paragraph() -> None:
        if paragraph:
            output.append("<p>" + render_inline(" ".join(x.strip() for x in paragraph)) + "</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_tag
        if list_tag:
            output.append(f"</{list_tag}>")
            list_tag = ""

    for line in raw_lines:
        if in_fence:
            if line.startswith("```"):
                output.append(f'<pre class="book-code"><code class="language-{html.escape(fence_lang)}">{html.escape(chr(10).join(fence))}</code></pre>')
                fence.clear()
                in_fence = False
            else:
                fence.append(line)
            continue
        if in_typst:
            if "-->" in line:
                in_typst = False
            continue
        image = image_pattern.search(line)
        if image:
            close_paragraph()
            close_list()
            alt, reference = image.groups()
            asset_name = Path(reference).name
            output.append(f'<figure><img src="assets/book/{html.escape(asset_name, quote=True)}" alt="{html.escape(alt, quote=True)}" loading="lazy"></figure>')
            continue
        if "<!--raw-typst" in line:
            close_paragraph()
            close_list()
            if output_match := output_pattern.search(line):
                value = html.unescape(output_match.group(1)).replace("\\n", "\n").replace("\\\"", '"')
                output.append(f'<pre class="program-output"><code>{html.escape(value)}</code></pre>')
            if "-->" not in line:
                in_typst = True
            continue
        if line.startswith("```"):
            close_paragraph()
            close_list()
            fence_lang = line[3:].strip() or "text"
            in_fence = True
            continue
        if not line.strip():
            close_paragraph()
            close_list()
            continue
        if heading := re.match(r"^(#{1,4})\s+(.+)$", line):
            close_paragraph()
            close_list()
            level = min(len(heading.group(1)) + 1, 4)
            title = render_inline(heading.group(2).strip())
            if heading.group(1) == "#":
                continue
            output.append(f"<h{level}>{title}</h{level}>")
            continue
        if bullet := re.match(r"^\s*[-*+]\s+(.+)$", line):
            close_paragraph()
            if list_tag != "ul":
                close_list()
                output.append("<ul>")
                list_tag = "ul"
            output.append(f"<li>{render_inline(bullet.group(1))}</li>")
            continue
        if numbered := re.match(r"^\s*\d+[.)]\s+(.+)$", line):
            close_paragraph()
            if list_tag != "ol":
                close_list()
                output.append("<ol>")
                list_tag = "ol"
            output.append(f"<li>{render_inline(numbered.group(1))}</li>")
            continue
        paragraph.append(line.strip())
    close_paragraph()
    close_list()
    if in_fence:
        output.append(f'<pre><code>{html.escape(chr(10).join(fence))}</code></pre>')
    intro = f'<p class="sample-intro">Originaluddrag fra <em>Introduktion til Python i Gymnasiet</em>. {preview_heading}. Kapitelteksten bevarer bogens henvisninger til VS Code; VygotskAI er et supplerende arbejdsrum.</p>'
    return intro + "\n".join(output)


def main() -> None:
    page_dir = SOURCE / "pages"
    if not page_dir.exists():
        raise SystemExit("Mangler site_src/pages med sidernes indhold.")
    (ROOT / "assets" / "css").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets" / "js").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets" / "book").mkdir(parents=True, exist_ok=True)
    (ROOT / "data").mkdir(parents=True, exist_ok=True)

    (ROOT / "labs").mkdir(exist_ok=True)
    copy_tree(OLD / "pyLab" / "vendor", ROOT / "labs" / "vendor")
    # The 3D agent lab links to this alternate 2D view, so keep that route local too.
    shutil.copy2(OLD / "pyLab" / "agent-simulator-2d.html", ROOT / "labs" / "agent-simulator-2d.html")
    if (OLD / "pyLab" / "assets").is_dir():
        copy_tree(OLD / "pyLab" / "assets", ROOT / "labs" / "assets")
    shutil.copy2(OLD / "pyLab" / "styles.css", ROOT / "labs" / "styles.css")
    shutil.copy2(OLD / "data" / "faglige_maal_med_kapiteldaekning.csv", ROOT / "data" / "faglige_maal_med_kapiteldaekning.csv")

    cover = BOOK / "assets" / "cover" / "sand-cover.jpeg"
    shutil.copy2(cover, ROOT / "assets" / "images" / "bogomslag.jpeg")
    marketing = TUTOR / "docs" / "marketing"
    (ROOT / "assets" / "images" / "vygotskai").mkdir(exist_ok=True)
    for jpg in sorted((marketing / "billeder").glob("*.jpg")):
        shutil.copy2(jpg, ROOT / "assets" / "images" / "vygotskai" / jpg.name)
    for name in ["01-python-og-tutor.jpg", "03-pylabs-oversigt.jpg"]:
        shutil.copy2(marketing / "lyse-skaermbilleder" / name, ROOT / "assets" / "images" / "vygotskai" / name)

    for name in ["chapter-01-dit-foerste-program.jpg"]:
        shutil.copy2(BOOK / "assets" / "chapter-art" / name, ROOT / "assets" / "book" / name)
    for name in ["image56.png", "proces.png"]:
        source_path = BOOK / "assets" / "images" / ("kap1" if name == "proces.png" else "") / name
        if source_path.is_file():
            shutil.copy2(source_path, ROOT / "assets" / "book" / name)
    chapters_root = BOOK / "content" / "chapters"
    (ROOT / "laeseproeve" / "kapitler").mkdir(parents=True, exist_ok=True)
    (ROOT / "laeseproeve" / "kapitler" / "forord.html").write_text(
        chapter_html("forord.md", "Her begynder bogens faglige introduktion"), encoding="utf-8"
    )
    (ROOT / "laeseproeve" / "kapitler" / "01-dit-foerste-program.html").write_text(
        chapter_html("01-dit-foerste-program.md", "Læs hele kapitel 1"), encoding="utf-8"
    )
    chapter_json = [{"number": f"{index:02}", "title": title, "description": description, "group": group, "file": filename} for index, (filename, title, description, group) in enumerate(CHAPTERS, 1)]
    (ROOT / "data" / "chapters.json").write_text(json.dumps(chapter_json, ensure_ascii=False, indent=2), encoding="utf-8")

    current_catalog = json.loads((TUTOR / "resources" / "content" / "pylabs.json").read_text(encoding="utf-8"))
    labs = []
    topic_by_category = {
        "Spil og Interaktive arenaer": ["spil", "algoritmer"],
        "Software modellering": ["systemer", "visualisering"],
        "Algoritmer og Datastrukturer": ["algoritmer", "data"],
        "Maskinlæring og kunstig intelligens": ["ai", "data"],
        "Agentbaseret modellering, robotter og evolution": ["simulation", "ai"],
    }
    level_by_context = {"grundlæggende": "Begynder", "øvet": "Videre", "fordybelse": "Fordybelse"}
    for item in current_catalog["items"]:
        category = item["category"]
        context = item.get("tutor_context", {})
        source = Path(item["source"]).name
        level = level_by_context.get(context.get("level", ""), "Videre")
        topics = list(topic_by_category.get(category, ["algoritmer"]))
        if level == "Begynder":
            topics.append("begynder")
        if category == "Maskinlæring og kunstig intelligens":
            topics.append("maskinlæring")
        labs.append({
            "id": item["id"],
            "title": item.get("topic_title") or item["title"],
            "description": item["description"],
            "category": category,
            "topics": topics,
            "level": level,
            "goal": context.get("exercise", item["description"]),
            "chapter": item.get("chapter_reference", "Python i Gymnasiet").replace("Læs: ", ""),
            "feature": item.get("icon", item["id"]),
            "source": source,
            "href": source,
        })
    (ROOT / "data" / "labs.json").write_text(json.dumps(labs, ensure_ascii=False, indent=2), encoding="utf-8")

    lab_cards = []
    for lab in labs:
        topic_words = " ".join(lab["topics"])
        search_words = " ".join([lab["title"], lab["description"], lab["category"], lab["goal"], lab["chapter"]])
        lab_cards.append(
            f'<article class="lab-card" data-lab-card data-topics="{html.escape(topic_words)}" data-level="{html.escape(lab["level"])}" data-search="{html.escape(search_words, quote=True)}">'
            f'<div class="lab-card-link"><span class="lab-icon" aria-hidden="true">{html.escape(lab["feature"])}</span>'
            f'<span class="lab-card-content"><span class="lab-card-title">{html.escape(lab["title"])}</span><span class="lab-card-description">{html.escape(lab["description"])}</span>'
            f'<span class="lab-meta"><span>{html.escape(lab["level"])}</span><span>{html.escape(lab["chapter"])}</span></span>'
            f'<span class="lab-goal"><b>Fagligt fokus:</b> {html.escape(lab["goal"])}</span></span></div></article>'
        )
    lab_cards_html = "\n".join(lab_cards)
    featured_html = "\n".join(lab_cards[i] for i in [0, 4, 5, 6])

    chapter_cards = []
    for index, (filename, title, description, group) in enumerate(CHAPTERS, 1):
        number = f"{index:02}"
        chapter_cards.append(
            f'<details class="chapter-card" data-chapter-card data-search="{html.escape(title + " " + description + " " + group, quote=True)}" id="kapitel-{number}">'
            f'<summary><span class="chapter-number">{number}</span><span class="chapter-summary"><b>{html.escape(title)}</b><small>{html.escape(description)}</small></span><span class="chapter-chevron" aria-hidden="true">＋</span></summary>'
            f'<div class="chapter-detail"><span class="tag">{html.escape(group)}</span><p>{html.escape(description)}</p>'
            f'<p><b>Forslag til næste handling:</b> Læs eksemplet, forudsig hvad koden gør, og afprøv en lille ændring.</p>'
            f'<a class="text-link" href="laeseproeve.html">Åbn læseprøven med bogens introduktion →</a></div></details>'
        )
    chapter_cards_html = "\n".join(chapter_cards)

    rows = list(csv.DictReader((ROOT / "data" / "faglige_maal_med_kapiteldaekning.csv").open(encoding="utf-8-sig", newline=""), delimiter=";"))
    subject_names = list(dict.fromkeys(row.get("Fag", "").strip() for row in rows if row.get("Fag", "").strip()))
    (ROOT / "data" / "subjects.json").write_text(json.dumps({"subjects": subject_names, "count": len(rows)}, ensure_ascii=False, indent=2), encoding="utf-8")

    head = (SOURCE / "head.html").read_text(encoding="utf-8")
    header_tpl = (SOURCE / "header.html").read_text(encoding="utf-8")
    footer = (SOURCE / "footer.html").read_text(encoding="utf-8")
    frame = (SOURCE / "page.html").read_text(encoding="utf-8")
    generated = []
    for page, (title, description) in PAGE_TITLES.items():
        body_path = page_dir / f"{page}.html"
        if not body_path.is_file():
            raise SystemExit(f"Manglende sideindhold: {body_path}")
        active = "index" if page == "index" else page
        header = header_tpl.replace("{{ACTIVE}}", active)
        for section in ["bogen", "vygotskai", "laboratorier", "undervisere", "kom-i-gang", "om"]:
            marker = "{{ACTIVE_ATTR:" + section + "}}"
            header = header.replace(marker, ' aria-current="page"' if section == active else "")
        body = body_path.read_text(encoding="utf-8").replace("{{LAB_CARDS}}", lab_cards_html).replace("{{FEATURED_LABS}}", featured_html).replace("{{CHAPTER_CARDS}}", chapter_cards_html)
        if page == "laboratorier":
            body = '<style>.lab-icon{min-width:5ch;width:auto;padding-inline:.55rem;white-space:nowrap}</style>' + body
            body = re.sub(r'<div class="lab-starts">.*?</div>', "", body, count=1, flags=re.S)
            body = re.sub(r'<section class="section section-tint">.*?</section>', "", body, count=1, flags=re.S)
            body = body.replace("Udforsk med hænderne", "Udforsk PyLabs")
            body = body.replace("Flyt et datapunkt. Følg et program. Undersøg hvad der ændrer sig, når du prøver en ny idé.", "Læs her om de mange laboratorier, som er tilgængelige sammen med VygotskAI-tutoren. Du kan blandt andet skifte mellem blok- og tekstkode, tegne figurer med skildpadder samt eksperimentere med maskinlæring og kunstig intelligens.")
            body = body.replace("Vælg en aktivitet", "Læs om aktiviteterne")
            body = body.replace("Hvert laboratorium åbner direkte i browseren. Start med de færdige eksempler og læs forudsætningerne, før du går videre.", "Brug søgning og filtre til at finde det laboratorium, der passer til et emne, et niveau eller et bestemt kapitel. Hvert kort forklarer aktivitetens faglige fokus.")
            body = body.replace("Udvalget består af de otte lokale browserlaboratorier, der er samlet til denne hjemmeside.", "Udvalget består af alle 41 PyLabs fra VygotskAI-Tutorens autoritative katalog.")
            body = body.replace("8 laboratorier", "41 emner")
            body = body.replace("Du kan fortsat åbne alle de laboratorier, der er listet ovenfor.", "Kataloget viser beskrivelser af alle PyLabs, men laboratorierne er ikke tilgængelige herfra.")
            for filename in ("turtle-laboratorium.html", "blockly-python.html", "code-visualizer.html"):
                body = body.replace(f'<a href="labs/{filename}">', '<span>')
            body = body.replace("</small></a>", "</small></span>")
        rendered = frame.replace("{{HEAD}}", head).replace("{{TITLE}}", html.escape(title)).replace("{{DESCRIPTION}}", html.escape(description, quote=True)).replace("{{PAGE}}", active).replace("{{HEADER}}", header).replace("{{BODY}}", body).replace("{{FOOTER}}", footer)
        output = ROOT / ("index.html" if page == "index" else f"{page}.html")
        output.write_text(rendered, encoding="utf-8", newline="\n")
        generated.append(output.name)

    custom_lab_page = (SOURCE / "lab-index.html").read_text(encoding="utf-8").replace("{{LAB_CARDS}}", lab_cards_html.replace('href="labs/', 'href="'))
    (ROOT / "labs" / "index.html").write_text(custom_lab_page, encoding="utf-8", newline="\n")

    sources = {
        "book": "PYTHONBook/content/chapters og assets",
        "tutor": "VygotskAI-Tutor/docs/marketing/billeder og current installation documentation",
        "labs": "VygotskAI-Tutor/resources/content/pylabs.json + python-i-gymnasiet/pyLab browser files",
        "coverage": "python-i-gymnasiet/data/faglige_maal_med_kapiteldaekning.csv",
    }
    (ROOT / "data" / "sources.json").write_text(json.dumps(sources, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Byggede sider: " + ", ".join(generated))
    print(f"Publicerede laboratorier: {len(labs)} (browserfiler med fulde lokale afhængigheder)")
    print(f"Kapitelkoblinger: {len(rows)} mål på tværs af {len(subject_names)} faglige kategorier")


if __name__ == "__main__":
    main()
