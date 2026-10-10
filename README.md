# Pythonbogen

Dansk hjemmeside for *Introduktion til Python i Gymnasiet*, VygotskAI og de interaktive Python-laboratorier. Bygget bruger Python 3.10 eller nyere; selve hjemmesiden kræver kun en almindelig statisk webserver.

## Åbn hjemmesiden lokalt

Fra denne mappe kan du starte en enkel lokal webserver med Pythons standardbibliotek:

```powershell
python -m http.server 8000
```

Åbn derefter <http://127.0.0.1:8000/>. Lad serveren blive kørende, mens du bruger siden. Den lokale HTTP-adresse gør det muligt at hente boguddrag og de tilhørende JSON- og CSV-filer på almindelig vis.

## Byg efter en ændring i kildematerialet

Siderne er HTML-filer, og deres faste indhold kan rettes under `site_src/pages/`. Navigation, sidehoved og sidefod kommer fra `site_src/`. Designet ligger i `assets/css/site.css`, og browserens interaktioner ligger i `assets/js/site.js`.

Kør fra projektmappen:

```powershell
python build.py
```

Bygget kopierer bogens omslag og læseprøvens illustrationer, samler forord og kapitel 1 fra deres aktuelle Markdown-filer, bygger kapitel- og fagdatasæt og kopierer de valgte browserlaboratorier og deres lokale afhængigheder. Kildeprojekterne bliver kun læst; den publicerbare version samles i denne mappe.

Kør derefter valideringen:

```powershell
python tools/check_site.py
node --check assets/js/site.js
```

Følgende links er arbejdsområder for dette site og bør genopbygges efter ændringer i deres tilhørende kildefiler: `index.html`, `bogen.html`, `laeseproeve.html`, `vygotskai.html`, `laboratorier.html`, `undervisere.html`, `kom-i-gang.html`, `om.html`, `data/`, `labs/` samt `laeseproeve/kapitler/`.

## Offentliggørelse

Filerne kan publiceres som et statisk website. Hvis webstedet skal ligge under en sti som `/pythonbogen/`, afprøv direkte undersidelinks og relative stier på netop den værtsopsætning. Webprojektet indeholder ikke en download af VygotskAI-installeren. Bestilling og spørgsmål om bogen går til `kontakt@pythonbog.dk`.

Se [INDHOLD-OG-KILDER.md](INDHOLD-OG-KILDER.md) for datakilder, udvalgte laboratorier og afklaringer før offentlig udgivelse.
