# Indhold og kilder for Pythonbogen

Hjemmesidens produkttekster følger den aktuelle bog, tutorapp og de browserbaserede Python-laboratorier. Kontakt og mailforespørgsel er implementeret. En bestillingsfunktion og en verificeret appudgivelse ligger ikke i dette webprojekt.

## Kildemateriale

| Hjemmesideindhold | Kilde |
| --- | --- |
| Læseprøvens forord og hele kapitel 1 | `../PYTHONBook/content/chapters/forord.md` og `01-dit-foerste-program.md` |
| Bogtitel, omslag og illustrationer | `../PYTHONBook/main.typ`, `../PYTHONBook/assets/cover/sand-cover.jpeg`, `../PYTHONBook/assets/chapter-art/` og `../PYTHONBook/assets/images/` |
| Kapitelrækkefølge og korte hjemmesidetekster | Bogens 16 kapitelkilder i `../PYTHONBook/content/chapters/` |
| AI-niveauer | Etiketterne i `../PYTHONBook/template.typ` |
| VygotskAI-funktioner, platform og praktiske oplysninger | `../VygotskAI-Tutor/README.md`, `docs/IMPLEMENTATION.md` og `docs/INSTALLATION.md` |
| Produktbilleder | De otte aktuelle kildebuild-skærmbilleder beskrevet i `../VygotskAI-Tutor/docs/marketing/billeder.json` |
| Laboratoriernes titler, beskrivelser og kategori | `../VygotskAI-Tutor/resources/content/pylabs.json` |
| Browserlaboratorier og deres statiske afhængigheder | De udvalgte `.html`-filer og understøttende assets i `../python-i-gymnasiet/pyLab/` |
| Mål og kapitelkoblinger til læreroversigten | `../python-i-gymnasiet/data/faglige_maal_med_kapiteldaekning.csv` |

`build.py` gengiver bogens Markdown til en læsevenlig HTML-prøve. Typst-layoutanvisninger filtreres fra. Kapitelopgaver vises som udfoldelige afsnit; kodeeksempler, bogens link, output og tilgængelige illustrationer bevares. Kig efter ændringer i kildens markup, når prøvekapitler opdateres.

## Laboratorieudvalg

Kataloget viser otte browseraktiviteter, som findes både i det aktuelle tutorprojekts katalog og i den foreløbige hjemmesides browsermappe:

| Laboratorium | Kilde | Redaktionelt niveau og læringsmål |
| --- | --- | --- |
| Turtle-laboratorium | `turtle-laboratorium.html` | Begynder. Undersøg instruktioner, løkker og tegning. |
| Kryds og bolle | `kryds-og-bolle-laboratorium.html` | Begynder og videre. Undersøg regler og strategier. |
| Klassediagram | `diagram-editor.html` | Begynder og videre. Skitsér klasser, relationer og kode. |
| Blokprogrammering til Python | `blockly-python.html` | Begynder. Forbind visuelle blokke med Python-strukturer. |
| Kodevisualisering | `code-visualizer.html` | Begynder og videre. Følg variabler, kald og output i eksempler. |
| KNN-laboratorium | `knn-laboratorium.html` | Videre. Undersøg afstand, naboer og klassifikation. |
| Agentlaboratorium | `agent-simulator.html` | Videre og fordybelse. Undersøg, hvordan lokale regler skaber mønstre. |
| Robotlaboratorium | `robot-laboratorium.html` | Begynder og videre. Undersøg forholdet mellem sensorinput og valg. |

De otte browserfiler er samlet fra `python-i-gymnasiet/pyLab`. De lokale Blockly-filer, øvrige leverede vendorfiler, `styles.css` og referenced assets kopieres sammen med dem. Direkte links fra kataloget går til den valgte browserfil.

Emne- og niveaufiltre er redaktionelle metadata i `build.py`; de følger ikke automatisk laboratoriets kildekode. Kontrollér dem, hvis et værktøj ændres. Kapitelkoblinger til de individuelle laboratorier er med vilje begrænset og vises kun, når de er beskrevet på kildesiden. Øvrige kapitelforbindelser er forslag til videre udforskning, ikke officielle kortlægninger.

## Faglige koblinger og printvenlig forløbsplan

Læreroversigten læser CSV-filens faglige mål og de første 15 kapitlers markeringer. Bogens kapitel 16 findes ikke som en kolonne i dette datasæt. Statusmarkeringerne vises med tekst og farve som redaktionelle relationer. De udgør ikke en vurdering foretaget af en myndighed.

Værktøjet »Lav en undervisningsplan« er et lokalt, redigerbart udkast. Læreren vælger fag, omfang og kapitler, og browserens printfunktion kan gemme det som PDF. Formularen sender ikke sine valg til en server. Udkastet er ikke en officiel undervisningsbeskrivelse.

## Kontakt, bestilling og udgivelser

- `kontakt@pythonbog.dk` findes i bogens forord. Hjemmesiden bruger adressen til mailhenvendelser om bogen og undervisningsbrug.
- Der er ikke implementeret betaling, ordre, klassesætbestilling eller webformular, fordi en faktisk modtagertjeneste ikke findes i målprojektet.
- Priser og leveringsoplysninger fra den tidligere hjemmeside er ikke brugt som aktuelle salgsfakta.
- Den gennemgåede tutorprojektmappe indeholder ingen verificeret installer eller offlinepakke under `release/`. Hjemmesiden linker derfor ikke til en udgivelsesfil.
- De faktiske skærmbilleder kommer fra tutorens kildebygning. Brug dem som produktbilleder, men kontrollér downloads, før hjemmesiden offentliggør dem som dokumentation for en bestemt binær version.
- VygotskAI-projektets repository er `HenrikSterner/VygotskAI-Tutor`. Dets indhold og seneste udgivelsesstatus bør kontrolleres før offentlig distributionsvejledning skrives.

## Installation og laboratoriebegrænsninger

Projektets installationsvejledning beskriver Windows x64, en almindelig installation, en separat lokal model, og en komplet offlinepakke. Offlinevejledningens omtrentlige minimum er 12 GB til den udpakkede pakke og en anbefaling om 24 GB RAM; den samme vejledning angiver cirka 8,02 GB for Gemma 4 12B Q4_K_M-pakken til den almindelige installation. Installationskrav kan ændres, så hjemmesideteksten skal følges op mod den faktiske publicerede pakke.

De publicerede labfiler er browseraktiviteter fra den tidligere bogside. De kører separat fra tutorappens isolerede Python-runtime. Hvis et laboratorium, dets browserafhængighed eller skolens netværk ændres, skal den konkrete aktivitet kontrolleres igen, inklusive dens interaktion og navigation tilbage til kataloget. Denne version lover ikke, at alle labs fungerer offline.

## Kontroller udført for denne version

- Sider, kapiteluddrag, datafiler, lokale billeder og valgte labfiler samles i `pythonbogen` uden at ændre kildeprojekterne.
- Kapitel- og laboratoriekataloger genereres fra aktuelle projektfiler og de dokumenterede, redaktionelle metadata.
- Appens lokale skærmbilleder, bogomslag og kapitelillustration indgår som lokale webassets.
- Interaktioner i webkoden omfatter søgning, filtre, modal lukning med Escape, lokale kodeskridt og print af planudkast.

En interaktiv browserafprøvning og direkte afprøvning af alle otte laboratoriers faglige kontroller skal udføres i den publicerede hostingkontekst. Projektet beholder valideringsværktøjet `tools/check_site.py` til links, centrale sider og lokale afhængigheder.
