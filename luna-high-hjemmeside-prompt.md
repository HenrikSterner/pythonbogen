# Prompt til Luna High om hjemmesiden Pythonbogen

Du er Luna High og skal designe og implementere en ny dansk hjemmeside med navnet **Pythonbogen**. Hjemmesiden skal præsentere og promovere lærebogen *Introduktion til Python i Gymnasiet* sammen med **VygotskAI**, en lokal AI-tutor og et Python-værksted, samt **Python-laboratorierne**, som gør programmering og informatiske begreber konkrete gennem eksperimenter og visualiseringer.

Byg hjemmesiden i `C:\code\pythonbogen`. Brug den eksisterende hjemmeside i `C:\code\python-i-gymnasiet` som indholdsmæssig og funktionel inspiration, og brug `C:\code\PYTHONBook` og `C:\code\VygotskAI-Tutor` til at forstå de faktiske produkter. Lever en sammenhængende, fungerende hjemmeside med dansk indhold og en tydelig visuel identitet. Arbejd frem til en lokal, afprøvet løsning, som kan gennemgås i en browser.

Den centrale fortælling er: **Læs og forstå i bogen. Undersøg og afprøv i laboratorierne. Få hjælp videre med VygotskAI.** Bogen er det faglige fundament og sidens primære produkt. Tutoren og laboratorierne skal fremstå som meningsfulde supplementer, der hjælper eleverne med at forstå og bruge det, de lærer.

## 1 Opgave og prioritering

Skab en hjemmeside, hvor en elev eller lærer inden for få sekunder kan forstå, hvad Pythonbogen tilbyder, hvem materialet er til, og hvordan man kommer i gang. Siden skal have en elegant, rolig og gennemarbejdet præsentation, som også føles interessant for unge mennesker.

Prioriter disse resultater i denne rækkefølge:

1. Besøgende forstår sammenhængen mellem bog, tutor og laboratorier.
2. Besøgende kan læse en prøve og finde en relevant aktivitet med få klik.
3. Elever får en overskuelig vej ind i programmering, også uden forkundskaber.
4. Lærere kan vurdere materialets faglige anvendelse, progression og praktiske krav.
5. Besøgende kan finde en faktisk bestillingsvej eller en ærlig vej til at spørge om bogen.
6. Besøgende kan se VygotskAI i brug og finde installationsoplysninger og eventuelle verificerede downloads.

Byg først de vigtige brugerforløb helt færdige. Sørg derefter for den visuelle finish. Et smukt element skal understøtte forståelse, orientering eller handling.

## 2 Kilder og eksisterende materiale

Læs relevante `AGENTS.md`-filer og undersøg målprojektets struktur, før du ændrer filer. Hvis `pythonbogen` allerede indeholder en hjemmeside, skal du tilpasse implementeringen til dens etablerede struktur. De tre kildemapper skal anvendes som læsegrundlag; alle nye hjemmesidefiler og nødvendige kopier af webressourcer placeres i `pythonbogen`.

Stierne nedenfor er relative til `C:\code\pythonbogen`:

| Kilde | Brug i den nye hjemmeside |
| --- | --- |
| `../python-i-gymnasiet/index.html` | Bogpræsentation, eksisterende navigation, målgruppetekster og idéer til indhold |
| `../python-i-gymnasiet/assets/css/site.css` | Forstå den tidligere visuelle løsning og dens temaer |
| `../python-i-gymnasiet/assets/js/site.js` | Undersøg eksisterende interaktioner og formularernes faktiske funktion |
| `../python-i-gymnasiet/kapitler.html` og `assets/js/reader.js` | Inspiration til læseoplevelse og kapitelnavigation |
| `../python-i-gymnasiet/fagdaekning.html` | Inspiration til lærernes overblik over kapitler og fag |
| `../python-i-gymnasiet/uvbeskrivelse.html` | Eksisterende værktøj til undervisningsbeskrivelser |
| `../python-i-gymnasiet/data/faglige_maal_med_kapiteldaekning.csv` | Eksisterende redaktionel kobling mellem faglige mål og kapitler |
| `../python-i-gymnasiet/pyLab/index.html` | Den tidligere hjemmesides laboratorieudvalg |
| `../PYTHONBook/main.typ` | Bogens titel, omslag og overordnede opsætning |
| `../PYTHONBook/content/chapters/forord.md` | Målgruppe, progression, AI-brug og forfatteroplysninger |
| `../PYTHONBook/content/chapters/` | Autoritativt grundlag for kapitelindhold og læseprøve |
| `../PYTHONBook/template.typ` | Bogens fem AI-niveauer og markeringer af opgavetyper |
| `../PYTHONBook/content/back-cover.typ` | Bogens korte præsentation og kobling til digitale supplementer |
| `../PYTHONBook/didactics/pfpl_opgavetyper.md` | Faglig uddybning til lærerindhold om arbejde med prompts |
| `../PYTHONBook/assets/cover/sand-cover.jpeg` | Det omslag, som bogens aktuelle `main.typ` refererer til |
| `../PYTHONBook/assets/chapter-art/` og `assets/images/` | Udvalgte bogillustrationer, når de understøtter indholdet |
| `../VygotskAI-Tutor/README.md` | Overblik over den aktuelle tutorapp og dens funktioner |
| `../VygotskAI-Tutor/docs/INSTALLATION.md` | Installation, platform, modelbehov og praktiske begrænsninger |
| `../VygotskAI-Tutor/docs/IMPLEMENTATION.md` | Implementerede funktioner og deres placering |
| `../VygotskAI-Tutor/docs/TELEMETRY.md` | Tutorens lokale observationer og grundlag for feedback |
| `../VygotskAI-Tutor/docs/PYLABS_MIGRATION.md` | Status og begrænsninger for laboratorier i desktopappen |
| `../VygotskAI-Tutor/resources/content/pylabs.json` | Struktureret laboratoriekatalog med titler, kategorier og kildefiler |
| `../VygotskAI-Tutor/resources/content/pylabs/index.html` | Laboratoriernes beskrivelser og eksisterende anbefalinger til læsning |
| `../VygotskAI-Tutor/resources/content/pylabs/` | Pakkede laboratorier og tilhørende webressourcer |
| `../VygotskAI-Tutor/docs/marketing/reklametekst.txt` | Konkrete produkttekster, som kan redigeres til hjemmesiden |
| `../VygotskAI-Tutor/docs/marketing/billeder.json` | Billedtitler, alt-tekster og anvendelsesforslag |
| `../VygotskAI-Tutor/docs/marketing/billeder/` | Faktiske skærmbilleder fra appen med demonstrationsdata |
| `../VygotskAI-Tutor/docs/marketing/LAES-MIG.txt` | Forbehold om forskellen mellem kildebygning og tidligere releasepakker |

Når kilder er uenige, skal den aktuelle bogtekst styre bogens indhold, mens tutorens aktuelle implementering og brugervejledning styrer appens funktioner. Den gamle hjemmeside leverer inspiration; dens salgsudsagn er ikke automatisk bekræftede produktfakta. Den oprindelige tutorspecifikation i `docs/vygotskai_tutor.md` beskriver også designintentioner og må ikke alene bruges som bevis for færdige funktioner.

Genkontrollér kilderne, når du bygger. Dette projekt kan udvikle sig efter promptens tilblivelse.

## 3 Produktfakta og redaktionelle grænser

Disse oplysninger er grundlaget for præsentationen, med kontrol mod de aktuelle filer før implementering:

- Sitets navn er **Pythonbogen**. Bogens titel er **Introduktion til Python i Gymnasiet**. Bevar forskellen mellem sitets navn og bogens titel.
- Forfatterne er **Kathrine Bohus Madsen** og **Henrik van Bedaf Sterner**. Bogens omslag bruger den kortere form Henrik Sterner. Brug fulde navne i forfatterpræsentationen, når de aktuelle kilder fortsat understøtter dem.
- Bogen begynder med grundlæggende programmering og fortsætter til blandt andet objektorientering, softwarearkitektur, dataudtræk, maskinlæring, webscraping, test og Git.
- Bogen har 16 kapitler. Den aktuelle tutorbeskrivelse angiver 358 opgaver og 240 bogafsnit. Brug eventuelle antal som vedligeholdte data, og skeln mellem bogens indhold og appens importerede kursuspakke.
- Den tidligere hjemmeside omtaler 27 laboratorier. Det gennemgåede `resources/content/pylabs.json` indeholder 31 poster. Afled det nye sites antal af det udvalg, der faktisk publiceres og virker; forskellige udgaver kan have forskellige udvalg.
- VygotskAI samler bog, opgaver, Python-editor, output, tekst og blokke samt lokal tutorhjælp i et dansk arbejdsrum.
- Den aktuelle releaseplatform er Windows x64. Tilgængelighed til andre platforme skal bekræftes særskilt.
- Den færdige desktopapp indeholder et Python-miljø. Eleven skal ikke selv installere Python til appens interne øvelser. Nogle bogopgaver kræver dog et eksternt udviklingsmiljø.
- Appen bruger lokale profiler og kræver ikke en onlinekonto til det beskrevne lokale arbejde.
- Tutorhjælp kræver en klargjort lokal model. En almindelig installer og en komplet offlinepakke har forskellige download- og installationsbehov.
- Tutorens guidede støtte følger som udgangspunkt bogens AI-niveauer. Appen har også separate indstillinger for hjælp i alle opgaver og fuld tutorhjælp. Beskriv mulighederne præcist, og undgå at love, at tutoren aldrig giver kode eller hele løsninger.
- Automatiske funktionelle tests findes til udvalgte opgaver. Elevens færdigmarkering er selvvurdering, og AI-feedback er støtte til læring.
- Lokale arbejdsobservationer kan indgå i tutorens hjælp. Beskriv det forståeligt som et grundlag for kontekstuel støtte, uden at fremstille det som måling af intelligens, sikker diagnose af forståelse eller automatisk kontrol af snyd.

Kontrollér særligt følgende før brug på den nye side:

1. Priserne 299 kr. og 199 kr., leveringstid, fragt, EAN-køb og prøveeksemplarer optræder på den gamle hjemmeside. Behandl dem som tidligere udkast, indtil aktuelle salgsoplysninger er bekræftet.
2. Den gamle hjemmesides formularhandler viser en `alert` og nulstiller formularen. Det dokumenterer ingen faktisk ordre, mail eller download.
3. Den gamle sides udtalelser, stjerner og udsagn som »Danmarks første« må kun anvendes, hvis de kan dokumenteres og er beregnet til offentlig brug.
4. `kontakt@pythonbog.dk` optræder i bogens forord, mens den gamle hjemmeside bruger et andet domæne. Saml kontaktoplysninger i konfiguration, og få den valgte adresse verificeret før offentlig udgivelse.
5. De eksisterende marketingbilleder viser en kildebygning. Et download skal matche de funktioner, som billeder og tekst lover.
6. Laboratoriernes desktopintegration har kendte forskelle fra browserudgaven. Sortering og det generelle maskinlæringslaboratorium er i migrationsbeskrivelsen nævnt med eksterne Brython-afhængigheder. Undersøg den aktuelle status før udsagn om offlinebrug.

Vis alene »gratis«, »inkluderet« eller »følger med bogen«, når adgangsvilkåret er verificeret for det konkrete materiale. Vis ingen opdigtede priser, testimonials, certificeringer, skolelogoer, købertal eller garantier for læringsresultater.

## 4 Målgrupper og konkrete behov

Skriv på naturligt dansk. Indholdet skal være let at forstå uden kendskab til AI-teknik eller programmeringssprog. Beskriv en konkret aktivitet og dens værdi, før du nævner teknologien bag.

| Målgruppe | Besøgendes spørgsmål | Hjemmesidens svar og næste handling |
| --- | --- | --- |
| Gymnasieelev med begrænset erfaring | Kan jeg finde ud af det, og hvor begynder jeg? | Vis et lille forståeligt eksempel, bogens begyndelse og knappen »Start med Python« |
| Gymnasieelev med erfaring | Hvad kan jeg bygge, og hvordan kommer jeg videre? | Vis relevante kapitler, spil, data og AI-laboratorier samt konkrete læringsmål |
| Elev i folkeskolens ældste klasser | Kan jeg prøve noget, jeg kan se med det samme? | Fremhæv blokke, Turtle og kodevisualisering samt korte introduktionsaktiviteter |
| Lærer i programmering | Hvordan får jeg progression, øvelser og faglig refleksion? | Vis kapitelstruktur, opgavetyper, AI-niveauer og et eksempel på et undervisningsforløb |
| Lærer i informatik | Hvordan kan materialet indgå i mit fag? | Vis relevante aktiviteter om data, systemer, modeller og algoritmer samt eksisterende fagkoblinger |
| Lærer i udskolingen | Hvilke dele kan mine elever starte med? | Vis et afgrænset begynderforløb med enkle forudsætninger og visuelle værktøjer |
| Lærer eller skole med ansvar for opsætning | Hvad kræver det at bruge tutoren i praksis? | Vis platform, installation, modelbehov og forskellen mellem browserlabs og desktopappen |

Gør gymnasiet til det primære faglige anker. Vis udskolingen som en tydelig indgang til udvalgte begyndervenlige dele. Undgå at love, at alle bogens avancerede kapitler er passende til alle aldersgrupper.

Lærersidens faglige stof må gerne være mere præcist. Forklar PRIMM, SOLO og andre begreber, første gang de bruges, og knyt dem til det, eleverne faktisk gør.

## 5 Visuel retning

Skab en lys, varm og redaktionelt præget hjemmeside, der forbinder en lærebogs troværdighed med lysten til at eksperimentere. Lad bogens omslag, håndtegnede illustrationer og appens faktiske arbejdsrum give siden særpræg.

Brug dette som designgrundlag:

- En varm, næsten hvid baggrund og enkelte let tonede sektioner.
- Mørk petrol til vigtige overskrifter og primære handlingsknapper, inspireret af omslagets skærmmotiv.
- Sandfarver til bogens læseunivers og afdæmpet grøn til laboratorier og tutorhjælp.
- En lille varm gul accent til markeringer og særligt vigtige detaljer.
- Store, læsbare overskrifter, tydelig typografisk rangorden og generøs luft.
- Tynde kanter, moderate hjørner og diskrete skygger, når et element skal adskilles fra baggrunden.
- En ensartet ikonstil. Brug ikoner sammen med forståelige tekstlabels.
- Varierede kompositioner: bog og tekst side om side, et stort produktbillede med forklaring, en enkel læringssekvens og et kurateret laboratorieudvalg.

Foreslåede farvetokens, som du skal justere efter kontrastkontrol:

| Token | Startværdi | Rolle |
| --- | --- | --- |
| `background` | `#FAF8F3` | Sidens hovedflade |
| `surface` | `#FFFFFF` | Indhold, læseprøve og formularflader |
| `ink` | `#17343A` | Brødtekst og overskrifter |
| `muted` | `#52656A` | Sekundær tekst |
| `primary` | `#075566` | Primære knapper og links |
| `sand` | `#E8E0D3` | Bogsektioner og varme baggrunde |
| `green` | `#315C48` | Tutor og laboratorier |
| `accent` | `#E9BE55` | Små fremhævelser med mørk tekst |
| `border` | `#D9DFD8` | Afgrænsning af felter og paneler |

Typografi: Brug en læsbar skrifttypefamilie med danske tegn. En lokal systemfont er et godt udgangspunkt. En eventuel ekstra skrifttype skal have en tydelig rolle og korrekt licens. Brug monospace til kode. Brødtekst bør typisk være 17–18 px med god linjeafstand; undgå små tekster til væsentlige forklaringer.

Hold læsetekst omkring 60–75 tegn per linje og det brede sidelayout omkring 1160–1240 px. Brug en konsekvent afstandsskala, eksempelvis 8, 12, 16, 24, 32, 48, 64 og 96 px.

Vis omslaget i dets fulde proportioner. Brug en diskret CSS-bogeffekt, hvis den forbedrer præsentationen. Omslagets titel og illustration må ikke beskæres eller erstattes af et opfundet omslag.

Brug bevægelse til kort feedback og overskuelige overgange. Undgå kontinuerligt hoppende mærkater, automatiske karruseller, store lysglimt og animationer, som konkurrerer med læsningen. Respektér brugerens valg om reduceret bevægelse.

Et mørkt tema er en valgfri forbedring efter den lyse oplevelse er færdig. Implementér i så fald temaet gennem designvariabler og kontrollér alle komponenter i begge temaer.

## 6 Navigation og sidestruktur

Byg en kompakt fælles header med navnet Pythonbogen som hjemlink. Brug højst fem primære navigationspunkter:

**Bogen · VygotskAI · Laboratorier · Til undervisere · Kom i gang**

En tydelig knap »Læs en prøve« skal være synlig i headeren. Placér køb eller kontakt i en relevant kontekst på bogsiden og til sidst på forsiden. Brug links til navigation og knapper til handlinger.

Brug en enkel mobilmenu med tydelig åbne- og lukkeknap. Aktuelt menupunkt skal fremgå, og menuen må ikke skjule nødvendig navigation på små skærme. En eventuel fast header må ikke dække ankerdestinationer eller tastaturfokus.

Implementér disse sider eller tilsvarende statiske HTML-ruter:

| Side | Hovedopgave |
| --- | --- |
| Forside | Præsentere det samlede læringsunivers og give få klare indgange |
| Bogen | Forklare indhold, progression, opgaver og adgang til prøve samt bestilling |
| Læseprøve | Give en reel, behagelig smagsprøve på bogens forord og kapitel 1 |
| VygotskAI | Vise produktet, tutorhjælp, arbejdsformer og installationsvej |
| Laboratorier | Gøre det let at finde og åbne relevante laboratorier |
| Til undervisere | Understøtte faglig vurdering og undervisningsplanlægning |
| Kom i gang | Vise begynderruter, browseradgang og eventuel installation |
| Kontakt og om | Præsentere forfatterne og verificerede kontaktmuligheder |

Brug eksisterende fungerende værktøjer til fagkoblinger og undervisningsbeskrivelser som undersider eller ressourcer under »Til undervisere«. De skal have en tydelig vej tilbage til Pythonbogen.

Vælg én konsekvent strategi for stier og hosting. Interne links, assets og browserens tilbageknap skal fungere ved direkte åbning af undersider og ved hosting under en undermappe.

## 7 Forsidens første skærmbillede

Den første skærm skal have en klar besked og et fremtrædende bogomslag. Vis også tidligt, at universet omfatter tutor og laboratorier.

Brug denne tekst som et konkret udgangspunkt:

**Lille indledning:**

»Python til undervisning og nysgerrige begyndere«

**Hovedoverskrift:**

»Lær Python. Forstå din kode. Byg noget selv.«

**Kort beskrivelse:**

»Pythonbogen samler en dansk lærebog, en lokal AI-tutor og interaktive laboratorier. Gå fra dine første kodelinjer til projekter med spil, data og kunstig intelligens — med forklaringer og øvelser undervejs.«

**Målgruppelinje:**

»Til elever og undervisere i gymnasiet — og udvalgte begynderforløb i folkeskolens ældste klasser.«

**Primær handling:** »Læs en prøve«.

**Sekundær handling:** »Udforsk laboratorierne«.

**Enkelt tekstlink:** »Se VygotskAI i brug«.

På desktop placeres teksten og bogen i en afbalanceret komposition, typisk omkring 60/40. På mobil vises overskrift, kort beskrivelse og handlinger før en tilpasset bogvisualisering. Gør omslaget synligt uden at lade det skubbe alle handlinger langt ned.

Vis under introduktionen en kort forbindende linje med tre indgange: **Bogen giver overblik · Laboratorierne gør det synligt · VygotskAI hjælper dig videre**. De må gerne være klikbare, men skal opleves som dele af ét læringsforløb.

Undgå brede salgspåstande. Tilliden skal komme fra indholdet, bogens forfattere og konkrete produktbilleder.

## 8 Forsidens øvrige indhold

Komponér forsiden i denne rækkefølge. Sektionerne skal have tydeligt forskellige opgaver og passende længde.

### Et lille eksempel på forståelse

Vis en kort, kontrolleret kodevisualisering med en klasseliste og en løkke:

```python
klasseliste = ["Sara", "Ali", "Emil", "Freja"]

for elev in klasseliste:
    print(f"Hej {elev}")
```

Lad brugeren vælge »Vis næste trin« og se det aktuelle navn, den aktive instruktion og næste outputlinje. Vis en nulstillingsknap og en tekstlig beskrivelse af hele resultatet.

Præsentér den som **»Visualisering af et Python-eksempel«**. Hvis demonstrationen bruger JavaScript til at vise kendte trin, skal brugerfladen beskrive det sådan. En generel redigerbar Python-editor må kun vises som fungerende, hvis der faktisk er en korrekt runtime. Brug ikke `eval` til at efterligne vilkårlig Python.

Knyt eksemplet til bogens kapitel 4 og kodevisualiseringslaboratoriet. Placér en kort læringspointe: »En løkke gentager den samme handling for hvert element i listen.«

### Bogen som fundament

Vis et reelt boguddrag eller en velvalgt illustration sammen med en kort beskrivelse af progressionen. Brug overskriften »Et fagligt fundament, du kan bygge videre på«. Fremhæv begyndervenlig opbygning, praktiske opgaver og arbejde med forståelse af kode. Link til bogsiden og læseprøven.

### VygotskAI i brug

Brug et stort faktisk skærmbillede af arbejdsrummet. Forklar de tre dele med korte billedtekster: »Læs opgaven«, »Afprøv din kode«, »Spørg om næste skridt«. Billedet skal kunne forstørres med tastatur og lukkes igen. Link til den fulde produktside.

### Et kurateret laboratorieudvalg

Vis seks laboratorier, som tilsammen demonstrerer både lav adgangstærskel og faglig bredde: Turtle, kodevisualisering, sortering, KNN, et diagramværktøj og agentmodeller eller robotter. Hvert element viser navn, konkret aktivitet, et læringsmål og en tydelig åbneknap. Vælg kun laboratorier, som er med i det fungerende publicerede udvalg.

### Vælg en vej ind

Giv to tydelige indgange, som ikke skjuler resten af siden:

- **Jeg er elev:** »Start med et lille program, se hvad koden gør, og prøv en aktivitet.«
- **Jeg underviser:** »Få overblik over kapitler, læringsaktiviteter og mulighederne for at bruge AI i undervisningen.«

Begge links skal føre til konkrete næste trin. Brug ikke et obligatorisk målgruppevalg ved første besøg.

### Et samlet læringsforløb

Vis sekvensen **Læs → Forudsig → Afprøv → Forklar → Arbejd videre** med korte forklaringer. Knyt den til ét eksempel med løkker, så besøgende ser sammenhængen mellem bog, laboratorium og tutorhjælp.

### Forfattere og afsluttende handling

Præsentér forfatterne med korte, kildebaserede beskrivelser. Brug faktiske billeder, hvis der findes egnede billeder beregnet til formålet. Ellers brug bogillustrationer og en typografisk præsentation.

Afslut med »Find din vej ind i Python« og knapper til læseprøve og lærerindgang. Giv en verificeret bestillingsvej, hvis den findes.

## 9 Bogsiden og kapiteloverblikket

Gør bogsiden til den mest komplette præsentation af hovedproduktet. Vis bogens præcise titel, omslag, forfattere, faglige idé og målgruppe. Forklar, at grundstoffet bygger op fra begyndelsen, og at videregående kapitler kan vælges efter behov.

Gruppér kapiteloversigten visuelt uden at ændre bogens rækkefølge:

| Gruppe | Kapitler |
| --- | --- |
| Kom i gang med Python | 1 Dit første program; 2 Variabler og deres datatyper; 3 Forgreninger og betinget udførelse; 4 Løkker og lister; 5 Funktioner |
| Forstå struktur og genbrug | 6 Rekursion; 7 Objektorienteret programmering; 8 OOP og biblioteker i praksis; 9 Regulære udtryk |
| Byg systemer og arbejd med data | 10 Arkitektur for brugerhåndtering; 11 Arkitektur for dataudtræk gennem API |
| Undersøg og udvikl videre | 12 Maskinlæring; 13 Webscraping; 14 Test og fejlfinding; 15 Samarbejde gennem Git; 16 Opgavesamling |

Kontrollér de præcise kapiteltitler i de aktuelle kildefiler. Skriv kortere labels i navigationen, hvis det gør den lettere at bruge, og bevar den fulde titel på kapitlets informationsflade.

Hvert kapitel skal kunne udvides og vise:

- To eller tre konkrete læringsmål baseret på kapitlets indhold.
- Et kort eksempel på en aktivitet eller opgave.
- Relevante laboratorier, når relationen kan forklares fagligt.
- Forudsætninger eller forslag til forudgående læsning.

Markér »Redaktionelt forslag«, hvis en laboratoriekobling er din tilføjelse. Undgå at præsentere et bredt kapitelinterval fra laboratoriets katalog som et bevis på en specifik opgavekobling.

Vis et eksempel på bogens opgavetyper og de fem AI-niveauer. Forklar dem på almindeligt dansk:

1. Ingen generativ AI: arbejd selv med bog, noter og samtale.
2. AI finder kun fejl: få hjælp til at undersøge fejl.
3. AI forklarer begreber: brug forklaringer og eksempler til forståelse.
4. AI giver kodefeedback: få feedback på egen kode og vælg forbedringer.
5. AI fremstiller kode: forstå, test og tilpas kodeforslag.

Bevar de præcise betegnelser fra `template.typ`, hvis de ændres. Forklar, at lærerens rammer og aktivitetens mål er relevante for brugen, og at appens hjælp kan indstilles lokalt.

Saml prøve, bestilling og spørgsmål om klassesæt i en enkel afsluttende sektion. Brug almindelig produktpræsentation frem for en tabel, der får bogen, tutoren og laboratorierne til at ligne abonnementstrin uden dokumenterede adgangsvilkår.

## 10 Læseprøven

Giv besøgende direkte adgang til en reel prøve med forord og kapitel 1, uden krav om registrering eller mailadresse. Brug den aktuelle bogtekst som kilde. Et eksisterende prøve-PDF kan anvendes, hvis det er til stede og korrekt; en fuld bog-PDF skal ikke omdøbes til prøvekapitel.

Hvis der ikke findes et færdigt prøve-PDF, skal du levere en læsbar HTML-prøve. Fjern eller omsæt Typst-direktiver, så læseren kun ser bogens relevante tekst, kode og illustrationer. Bevar mening, kodeindrykning, overskrifter og forfatteroplysninger.

Læseoplevelsen skal have:

- Et tydeligt hjemlink og link til bogsiden.
- Navigation mellem forord og kapitel 1.
- En rolig læsekolonne, god linjeafstand og behagelig kodevisning.
- Knapper til at kopiere kode med synlig feedback.
- En printervenlig visning uden navigation og dekorative elementer.
- En tydelig afslutning med mulighed for at læse om bogen og digitale supplementer.

Bogtekstens introduktion til VS Code og Python skal bevares i sin faglige sammenhæng. En kort separat boks kan forklare, at VygotskAI er et supplerende lokalt øvemiljø med medfølgende Python. Undgå at ændre bogens arbejdsgang til en installationsfri browseroplevelse, som kilderne ikke beskriver.

## 11 VygotskAI som produktside

Brug overskriften »Hjælp til næste skridt i din kode« eller en tilsvarende konkret formulering. Forklar produktet med et kort afsnit:

»VygotskAI samler bog, opgaver og Python i et dansk arbejdsrum. Du kan skrive kode eller arbejde med blokke, undersøge resultatet og få hjælp fra en AI-tutor, der kører lokalt på din computer.«

Vis et stort produktbillede og korte forklaringer af disse fordele:

- **Sammenhæng:** Opgave, bogtekst, kode og hjælp findes i samme arbejdsrum.
- **Forståelse:** Tutoren kan forklare begreber, bygge videre på forsøget og hjælpe med fejlfinding.
- **Flere veje ind:** Tekst og blokke gør det muligt at arbejde på forskellige måder.
- **Refleksion:** Eleven kan skrive sin egen forklaring og undersøge sit resultat.
- **Lokalt arbejde:** Profiler, kode og den lokale tutors behandling findes på computeren.
- **Praktisk kontinuitet:** Automatisk gemning og versionshistorik understøtter det daglige arbejde.

Udvælg funktioner til forsiden; den komplette liste kan stå længere nede på produktsiden. Vis tale og oplæsning som en ekstra mulighed, hvis den version, siden præsenterer, indeholder den. Undgå at love bestemt talegenkendelsespræcision eller særlige medicinske virkninger.

### Demonstration af tutorhjælp

Lav en lille interaktiv forklaring med tre valgbare situationer: »Jeg forstår ikke en løkke«, »Mit program viser en fejl« og »Jeg vil forbedre mit forsøg«. Ved valg vises situation, et kort kodeeksempel og et eksempel på guidet hjælp.

Hvis svarene er forudskrevne, mærkes komponenten tydeligt »Eksempel på en tutorsamtale«. Brug faste valg, som svarer til det viste indhold. Vis ingen fri chatboks, der lader som om den forbinder til en model. En fri chatfunktion kræver en faktisk, særskilt implementeret og dokumenteret forbindelse.

Forslag til et illustrativt eksempel:

**Elev:** »Hvorfor bliver alle navnene skrevet ud?«

**Tutor:** »Listen indeholder flere navne. Løkken tager ét navn ad gangen, og `print` skriver en hilsen til det navn. Prøv at følge de to første trin: Hvilket navn står i `elev` hver gang?«

Dette er redaktionelt demonstrationsindhold og må ikke betegnes som et faktisk modelsvar. Brug eksisterende skærmbilleder til at vise faktiske svar.

### Installation og modelvalg

Vis først en kort forklaring af de praktiske behov og derefter en detaljeret vejledning. Læreren skal kunne vurdere, om skolens computere passer, før et download starter.

Præsentér en tabel med platform, installationsform, behov for modeldownload, omtrentligt pladsbehov og dokumenterede hardwareanbefalinger. Hent værdier fra den aktuelle installationsvejledning og den konkrete release. Beskriv krav for Light og Medium særskilt, når dokumentationen understøtter det. Brug ikke Medium-pakkens anbefaling som et fælles minimum for alle varianter.

Vis en downloadknap alene, når fil eller URL er til stede, og versionsoplysningerne er kontrolleret. Indtil da bruges »Se installationsvejledningen« og en konkret tekst om downloadstatus. En downloadknap skal angive platform og eventuelt filstørrelse, når den er kendt.

Forklar den daglige lokale brug og forudsætningen om, at modellen er klar, før tutoren kan fungere uden internet. Beskriv laboratoriernes browser- og offlinebehov særskilt.

## 12 Laboratoriekataloget

Brug navnet **Python-laboratorier** i den almindelige navigation. PyLab eller pyLabs kan stå som sekundær betegnelse, hvor det passer til eksisterende værktøjer.

Kataloget skal give besøgende et hurtigt valg og plads til udforskning. Start med »Prøv et begreb. Se hvad der sker.« og en kort forklaring af, at laboratorierne forbinder kode, modeller og synlige resultater.

Vis øverst tre konkrete begynderruter: Turtle, blokprogrammering og kodevisualisering. De skal være enkle indgange for både nye gymnasieelever og udskoling.

Implementér søgning og filtre i den publicerede katalogliste:

- Søgning i titel, beskrivelse og faglige nøgleord.
- Emner som »Kom i gang«, »Spil«, »Algoritmer«, »Data og AI«, »Systemer og diagrammer« og »Simulation og robotter«.
- Et enkelt niveauvalg, eksempelvis »Begynder«, »Videre« og »Fordybelse«, med kort forklaring.
- Relevant bogkapitel, når koblingen er defineret i katalogdata.

Grupper og niveauer er redaktionelle hjælpekategorier. Kortlæg dem eksplicit fra de eksisterende katalogposter, og bevar kildekategorien i data. Brug ikke elevens alder som eneste mål for sværhedsgrad.

Hvert laboratorieelement viser:

1. En præcis titel.
2. En sætning om, hvad eleven kan gøre.
3. Et konkret læringsmål.
4. Niveau og centrale forudsætninger.
5. Relevant kapitel eller fagligt tema.
6. Knap »Åbn laboratoriet« og eventuelt »Om aktiviteten«.

Eksempler på læringsmål:

| Laboratorium | Aktivitet og læringsmål |
| --- | --- |
| Turtle | Tegn et mønster og undersøg, hvordan en løkke gentager instruktioner |
| Kodevisualisering | Følg programmets trin og se, hvordan variabler og output ændrer sig |
| Sortering | Sammenlign strategier og undersøg forskelle i antal trin |
| KNN | Flyt datapunkter og undersøg, hvordan naboer påvirker klassifikation |
| Klassediagram | Skitsér klasser og relationer og forbind modellen med kode |
| Agentlaboratorium | Undersøg, hvordan simple regler kan skabe samlede mønstre |

Der skal være resultatantal, knap »Nulstil filtre« og en venlig tomtilstand: »Ingen laboratorier matcher dine valg. Prøv et andet emne eller nulstil filtrene.« Filtre må gerne afspejles i URL'en, så et lærerlink kan deles og genåbnes.

### Åbning af laboratorier

Et almindeligt link skal åbne det konkrete laboratorium. Gem kildefilens query-parametre, eksempelvis `?diagram=class`. Et klik må ikke føre til en tilfældig indeksside, hvis handlingen lover et bestemt værktøj.

Genbrug de eksisterende laboratorier med deres nødvendige styles, biblioteker og assets. Kopiér det valgte materiale ind i målprojektets publicerbare struktur. Undgå at implementere alle simulationerne igen som en del af markedsføringshjemmesiden.

Brug en enkel tilbagevej til kataloget, enten på laboratoriet eller i en let værtsside, hvor den eksisterende funktion fortsat virker. En iframe må kun bruges efter kontrol af størrelser, tastatur, scripts og navigation. For tungere værktøjer er en egen side ofte mere praktisk.

Kontrollér både appens pakkede katalog og den tidligere hjemmesides browserfiler. Vælg en dokumenteret browserudgave til hvert værktøj. Katalogtilstedeværelse er ikke alene bevis på, at laboratoriet fungerer i den nye hostingkontekst.

Vis en kort oplysning om internetbehov, hvis et laboratorium bruger eksterne scripts. Påstå kun offlinefunktion, når den konkrete browser- eller appvariant er afprøvet offline.

## 13 Lærerindgangen

Brug en konkret overskrift som »Saml læsning, eksperimenter og refleksion i dit forløb«. Gør siden anvendelig både for læreren, der undersøger materialet, og læreren, der allerede har valgt bogen.

Start med tre handlinger: »Se bogens progression«, »Find en aktivitet« og »Se faglige koblinger«.

Vis et forslag til et kort forløb om løkker. Mærk det »Forslag til undervisningsforløb«, og angiv eksempelvis 45–60 minutter som en redaktionel plan, der kan tilpasses:

| Trin | Elevaktivitet | Materiale |
| --- | --- | --- |
| Læs | Læs en forklaring og et eksempel på en løkke | Relevant del af kapitel 4 |
| Forudsig | Skriv, hvad programmet vil vise | Et kort eksempel fra bogen eller et tydeligt redaktionelt eksempel |
| Undersøg | Følg koden trin for trin | Kodevisualisering eller Turtle |
| Afprøv | Ændr en værdi eller instruktion og sammenlign resultatet | Laboratorium eller VygotskAI |
| Forklar | Beskriv med egne ord, hvad ændringen gjorde | Elevforklaring og samtale |
| Arbejd videre | Undersøg en fejl eller stil et afgrænset spørgsmål | Tutorhjælp, når aktivitetens AI-ramme tillader det |

Knyt PRIMM til de konkrete handlinger forudsig, kør, undersøg, ændr og skab. SOLO kan omtales som en måde at arbejde med stigende dybde i forklaringer og sammenhænge. Hold den mere udførlige didaktik i uddybende indhold.

Forklar, hvordan begyndere kan starte med blokke og visualisering, mens andre elever kan arbejde med tekstkode og mere åbne opgaver. Beskriv differentiering som konkrete valg af opgave, støtte og arbejdsform.

Vis eksisterende fagkoblinger fra CSV og `fagdaekning.html`. Bevar kategorier som »Delvist« og »Slet ikke«, og vis dem også med tekst. Betegn dem som materialets redaktionelle kapitelkoblinger. De skal hjælpe lærerens vurdering og må ikke markedsføres som myndighedsgodkendelse eller garanti for fuld læreplansdækning. Hvis officielle krav beskrives som aktuelle, skal de kontrolleres mod relevante primære kilder ved implementeringen.

Hvis værktøjet til undervisningsbeskrivelser genbruges, skal kapitelvalg og faktisk eksport afprøves. En knap til PDF eller Word må kun være aktiv, når den leverer det lovede format.

Giv et kort afsnit om AI i undervisningen: bogens fem niveauer, guidet støtte, appens lokale valg og elevens ansvar for at forstå og teste kode. Appens indstillinger må ikke beskrives som centralt håndhævede lærerrettigheder, hvis de styres lokalt hos brugeren.

Lav til sidst en enkel praktisk liste om Windows, lokale modeller, eksterne bogaktiviteter og skolens vurdering af anvendelsen. Beskriv de faktiske dataveje og lokale målinger. Undgå generelle mærkater som »GDPR-godkendt« eller »ingen data registreres«.

## 14 Kom i gang og målgruppernes ruter

Vis tre overskuelige ruter med højst tre eller fire trin hver:

**Ny i Python:** Læs en prøve → undersøg et kort kodeeksempel → prøv Turtle eller blokke → læs om næste kapitel.

**Vil du bruge VygotskAI:** Se arbejdsrummet → kontrollér platform og modelbehov → følg verificeret installation → opret en lokal profil og prøv en opgave.

**Skal du undervise:** Se progressionen → vælg en aktivitet → fastlæg AI-rammen → brug et forløbsforslag og relevante lærerressourcer.

Skeln tydeligt mellem »Åbn i browseren« og »Installér på computeren«. En besøgende skal ikke tro, at desktopappen er en browserchat, eller at alle browserlabs bruger samme runtime som appens Python-miljø.

Giv en kort FAQ med svar på:

- Skal jeg have programmeret før?
- Hvad kan jeg prøve direkte på hjemmesiden?
- Hvordan hænger bogen, laboratorierne og VygotskAI sammen?
- Kan udskolingen bruge materialet?
- Skal jeg installere Python for at bruge appen?
- Hvilke computere understøttes?
- Hvornår kan tutoren bruges uden internet?
- Giver tutoren færdig kode?
- Kan alle bogens opgaver køres i appen?
- Hvordan spørger jeg om bogen eller materiale til en klasse?

Svar kort, præcist og i overensstemmelse med den aktuelle produktversion.

## 15 Billeder og konkrete visuelle beviser

Brug eksisterende billeder, som viser de faktiske produkter. Prioriter følgende tutorbilleder:

| Fil under `../VygotskAI-Tutor/docs/marketing/billeder/` | Placering |
| --- | --- |
| `01-arbejdsrum.png` | Stor produktintroduktion på lys side |
| `02-tekst-og-blokke.png` | Begynderindgang og forklaring af blokke og tekst |
| `03-ai-vurdering.png` | Uddybning af feedback på besvarelser |
| `04-data-og-grafer.png` | Tværfaglighed og arbejde med data |
| `05-bog-og-opgaver.png` | Forbindelsen mellem bogtekst og programmering |
| `06-udseende-og-tutorhjaelp.png` | Lærerindhold om valg af hjælp og udseende |
| `07-lokale-modeller.png` | Praktiske installations- og modeloplysninger |
| `08-arbejdsrum-moerkt.png` | Valgfri præsentation af mørkt tema |

Brug beskrivelserne fra `billeder.json` som grundlag for meningsfulde alt-tekster. Sørg for, at screenshottekster ikke lover funktioner i en ældre downloadpakke.

Appbilleder skal vises stort nok til at forstå deres struktur. Brug en forstørrelsesmulighed og eventuelt et markeret udsnit ved en specifik forklaring. Bevar hele produktbilledets proportioner, når det vises som helhed.

Tag om muligt billeder af de fremhævede laboratorier med kontrollerede demonstrationsdata. Brug aldrig billeder fra et andet laboratorium som dokumentation for den viste aktivitet.

Vælg billedformater og størrelser efter anvendelsen. Prioritér skarp kode og læsbar UI frem for aggressiv komprimering. Angiv dimensioner, lav passende responsive varianter, og indlæs sekundære billeder efter behov. Det centrale omslag eller hovedbillede skal indlæses tidligt.

## 16 Interaktioner og feedback

Alle synlige handlinger skal have en defineret effekt. Implementér mindst:

- Mobilmenu med korrekt åbne- og lukketilstand.
- Kapiteludfoldning med tastaturbetjening og korrekt udvidelsesstatus.
- Kodesekvensen med næste trin og nulstilling.
- Valg af de tre tutorcases med tydelig aktiv tilstand.
- Laboratoriesøgning, filtre, resultatantal og nulstilling.
- Kopiering af kode med diskret synlig og tilgængelig feedback.
- Forstørrelse af billeder med lukning via Escape og tilbageføring af fokus.
- FAQ med semantisk udfoldning.
- Fungerende links til prøven, de konkrete laboratorier og praktiske vejledninger.

Oplysninger, som er afgørende for at forstå et produkt, skal stå på siden. Brug dialoger til eksempelvis billedforstørrelse, hvor de forbedrer oplevelsen.

Hvis der genbruges tunge laboratorier, indlæses de efter en bevidst handling. Kataloget skal kunne bruges hurtigt, uden at alle simulationer og deres biblioteker starter ved sideåbning.

## 17 Bestilling og kontakt

Lav en troværdig vej fra interesse til næste skridt med udgangspunkt i de verificerede muligheder.

Hvis der findes en faktisk boghandel eller bestillingsløsning, link til den og vis de korrekte oplysninger. Hvis der alene er en kontaktvej, brug »Spørg om bogen« eller »Spørg om klassesæt«. En mailhandling skal hedde »Åbn mail« eller tilsvarende, så besøgende ved, at deres mailprogram åbnes.

Vis ikke en bekræftelse om, at en ordre eller besked er modtaget, når der ikke er en server eller en ekstern tjeneste, som har modtaget den. Tilføj ikke et fiktivt betalingsflow, nyhedsbrev, elevlogin eller lærerlogin.

En eventuel formular kræver en faktisk destination. Den skal have labels, validering, ventetilstand, korrekt fejlbesked og bekræftelse efter reel modtagelse. Bevar det indtastede indhold ved fejl.

Saml priser, kontaktadresser, købsmål, adgangsvilkår og downloads i én konfiguration. Uafklarede værdier skal håndteres med passende tekst og alternative handlinger i den lokale side. Skriv de konkrete udeståender i udviklerdokumentationen.

## 18 Mobilvisning og tilgængelighed

Design og afprøv mindst ved 360, 390, 768, 1024 og 1440 px bredde. Kontrollér også et smalt 320 px layout og 200 procent zoom.

På små skærme skal handlinger stå tydeligt og laboratoriefiltre kunne bruges uden at fylde hele visningen. Kort og indhold bliver én kolonne. Kodeblokke må scrolle internt, mens siden som helhed skal undgå vandret overflow.

Implementér:

- `lang="da"`, korrekt tegnsæt og én beskrivende hovedoverskrift per side.
- Semantiske områder for header, navigation, hovedindhold og footer.
- Et link til at springe direkte til hovedindholdet.
- Synligt tastaturfokus på alle interaktive elementer.
- Tilstrækkelig kontrast, også på sekundær tekst og knapper.
- Tekstlabels sammen med farver og ikoner.
- Klikområder omkring mindst 44 px til centrale handlinger på mobil.
- Korrekte labels og hjælpetekster ved felter.
- Meningsfulde alt-tekster og tom alt-tekst på rent dekorative billeder.
- Reduceret bevægelse og fravær af automatisk lyd.
- Fokusstyring ved menu eller dialog, hvor det er nødvendigt.
- En kort besked ved ændret filterresultat uden at oplæse hele kataloget igen.

Bevar en brugbar tekstlig forklaring ved visuelle demoer. En elev skal kunne forstå eksemplets idé uden at aflæse farver eller se animationen. Selve laboratoriernes særlige tilgængelighedsbegrænsninger skal beskrives konkret, hvis de påvirker anvendelsen.

## 19 Teknisk implementering og vedligeholdelse

Tilpas teknologien til målprojektet. Hvis der ikke findes en etableret kodebase, er et statisk website med semantisk HTML, CSS og JavaScript udgangspunktet. Brug kun en større frontendstruktur, hvis den løser et konkret behov og fortsat giver en enkel lokal og publicerbar løsning.

Hjemmesiden skal kunne hostes som statiske filer. Den må ikke være afhængig af en Python-backend, en AI-nøgle eller tutorens desktopserver for at vise sit almindelige indhold. Tilføj ikke modeldownloads eller genopbygning af desktopappen som en nødvendig del af webbygningen.

Hold indhold adskilt fra præsentation, eksempelvis:

```text
pythonbogen/
  index.html
  bogen.html
  laeseproeve.html
  vygotskai.html
  laboratorier.html
  undervisere.html
  kom-i-gang.html
  kontakt.html
  assets/
    css/
    js/
    images/
  data/
    site-config.json
    kapitler.json
    laboratorier.json
    tutor-eksempler.json
  labs/
    ... laboratoriefiler og nødvendige afhængigheder
  scripts/
    ... eventuel kontrolleret synkronisering og validering
  README.md
  INDHOLD-OG-KILDER.md
```

Strukturen er et forslag. Bevar et etableret framework, hvis det allerede bruges. Undgå dublerede headers, fodtekster eller produktfakta, som bliver svære at vedligeholde; brug en enkel buildmekanisme eller fælles komponenter, hvor det er relevant.

Laboratoriedata skal som minimum rumme stabilt id, titel, beskrivelse, kildekategori, websti med query-parametre, redaktionelle emner, niveau, forudsætninger, læringsmål, kapitelrelation og status for internetbehov. Bevar oplysninger om kilde og eventuel indholdsversion i udviklerdata.

Konfiguration for appdownloads bør omfatte URL, version, platform, filstørrelse, kontrolsum hvor den findes, og bekræftet tilgængelighed. Vis en almindelig vejledningshandling, når ingen udgivelsesfil er klar. Kopiér ikke mange gigabyte runtime eller modeller ind i webprojektet.

Hvis data hentes med `fetch`, skal README beskrive opstart via en lokal HTTP-server. Afhængigheden af en server må ikke være skjult bag en instruktion om blot at dobbeltklikke en fil.

Render tekst og metadata sikkert. Behandl bogens Markdown, katalogdata og søgetekst som indhold. Fjern nødvendige Typst-kommentarer gennem en afgrænset konvertering frem for at vise dem eller afvikle vilkårlige felter som kode. Brug ikke rå HTML-indsættelse for brugerinput.

Undgå API-nøgler, hemmeligheder og brugerdata i det publicerede output. Bevar licens- og ophavsoplysninger ved kopiering af eksisterende biblioteker og illustrationer.

## 20 Metadata og indlæsning

Sørg for beskrivende sidetitler, korte danske metabeskrivelser og relevante delingsbilleder. Sidetitlen bør kombinere sidens emne med Pythonbogen, eksempelvis »VygotskAI — Pythonbogen«.

Brug kun et kanonisk domæne, når det faktiske udgivelsesdomæne er afklaret. Undgå at indsætte det gamle hjemmesidedomæne i nye metadata som en antagelse. Et eventuelt sitemap skal bruge den verificerede baseadresse.

Vis væsentligt indhold som almindelig HTML. Hvis JavaScript fejler, skal besøgende fortsat kunne læse hovedpræsentationen og følge de vigtigste links. Vis katalogets fulde liste uden filtre eller en tydelig alternativ vej, hvis filtreringen kræver JavaScript.

Indlæs kun nødvendige scripts på hver side. Undgå at hente editorer, ML-biblioteker og alle laboratorier til forsiden. Kontrollér, at det første skærmbillede vises uden billedhop, og at skrifttyper eller billeder ikke blokerer den grundlæggende læsning.

## 21 Arbejdsrækkefølge

Udfør arbejdet i denne rækkefølge og fortsæt selvstændigt gennem almindelige reversible design- og implementeringsvalg:

1. **Undersøg materialet:** Læs projektinstruktioner, relevante kilder og målprojektets status. Udpeg faktiske aktiver, brugbare laboratorier og uafklarede salgs- eller releaseoplysninger.
2. **Fastlæg indhold:** Lav sidestruktur, kapiteldata, laboratorieudvalg og konfiguration. Beslut en konsistent visuel retning ud fra denne prompt.
3. **Byg det samlede skelet:** Opret alle centrale sider, fælles navigation og fungerende interne stier.
4. **Færdiggør hovedpræsentationen:** Byg forsiden, bogsiden, prøven og tutorpræsentationen med de faktiske aktiver.
5. **Gør aktiviteter tilgængelige:** Implementér katalog og filtre, og integrér eller link de valgte fungerende laboratorier i den publicerbare struktur.
6. **Færdiggør lærer- og begynderruter:** Tilføj faglige koblinger, forløbsforslag, installation, FAQ og ærlige kontakt- eller bestillingsveje.
7. **Afprøv og ret:** Kontrollér de konkrete brugerforløb, responsive størrelser, tastaturbetjening, billeder og links. Ret væsentlige problemer før levering.
8. **Dokumentér:** Beskriv opstart, indholdskilder, opdatering af katalog og konfiguration samt konkrete udeståender før offentlig udgivelse.

Hvis én salgsoplysning eller releasefil mangler, skal resten af sitet færdiggøres. Brug en passende informations- eller kontakthandling i den del, der mangler en destination. Afslut ikke opgaven med et designforslag alene.

## 22 Afprøvning og acceptkriterier

Kontrollér funktioner med meningsfulde brugerforløb frem for kun at se, om siden åbner. Brug browserautomatisering, hvis den findes i miljøet, og ellers den tilgængelige browser og relevante statiske kontroller. Rapportér præcist, hvilke forløb der er kørt.

| Forløb | Godkendt resultat |
| --- | --- |
| Ny elev åbner forsiden | Forstår tilbuddet og kan åbne prøven uden registrering |
| Elev vil prøve et begreb | Finder et begyndervenligt lab og åbner det konkrete fungerende værktøj |
| Elev undersøger kodeeksemplet | Kan følge trinene og nulstille; tekst og output svarer til eksemplet |
| Besøgende ser tutorhjælp | Kan skifte mellem cases og forstår, at forudskrevne svar er eksempler |
| Lærer vurderer materialet | Finder progression, en aktivitet, AI-niveauer og praktiske krav |
| Besøgende søger et laboratorium | Filtre kombineres korrekt; nulstilling og tomtilstand fungerer |
| Besøgende vil bruge appen | Ser korrekt platform og modelbehov før en eventuel verificeret download |
| Besøgende vil købe eller spørge | Når den faktiske destination og får ingen opdigtet modtagelsesbekræftelse |
| Mobilbruger besøger siderne | Menu, handlinger, læseprøve og filtre fungerer uden vandret sideoverflow |
| Tastaturbruger navigerer | Fokus er synligt, udfoldning virker, og eventuelle dialoger kan lukkes |

Kontrollér yderligere:

- Alle interne links, billedstier og laboratoriekilder findes i det publicerbare output.
- Query-parametre og relative afhængigheder bevares ved laboratorieåbning.
- Direkte undersidelinks og hosting under en undermappe virker.
- Katalogets viste antal svarer til det publicerede og validerede udvalg.
- Hvert laboratorie i kataloget åbner uden blokerende fejl, og mindst én central faglig handling afprøves i hvert publiceret værktøj. Markér ikke et uafprøvet værktøj som funktionskontrolleret.
- Prøvens tekst er læsbar, kode kan kopieres, og Typst-direktiver vises ikke.
- Appbilleder og funktionsudsagn stemmer med den version, der eventuelt downloades.
- Der er ingen døde `href="#"`-handlinger eller synlige byggepladsholdere.
- Der er ingen fejl i konsollen, som blokerer de centrale brugerforløb.
- Der er ingen udokumenterede pris-, adgangs-, eksamens- eller privatlivsløfter.
- Læseprøven kan udskrives i et forståeligt layout.

Hvis en browser- eller labkontrol ikke kan gennemføres i miljøet, dokumentér præcis hvad der mangler. Lever stadig det øvrige gennemarbejdede resultat, og undgå at betegne en uafprøvet funktion som verificeret.

## 23 Levering

Lever den færdige lokale hjemmeside i `C:\code\pythonbogen` med alle nødvendige webfiler og genbrugte assets. Skriv en kort README med præcise kommandoer eller trin til at starte og åbne siden. Beskriv, hvordan almindelige indholdsændringer og eventuelle buildtrin udføres.

Skriv `INDHOLD-OG-KILDER.md` med:

- Kilder til produktbeskrivelser, bogtekst og billeder.
- Det valgte laboratorieudvalg og eventuelle redaktionelle niveau- og kapitelkoblinger.
- Status for priser, kontakt, adgangsvilkår og downloads.
- Forskel mellem den præsenterede kildebygning og eventuelle releasepakker.
- Konkrete kontrolresultater og kendte begrænsninger.

Hvis browseren er tilgængelig, gem et lille udvalg af screenshots i målprojektet: forside på desktop, forside på mobil, laboratoriekatalog og en relevant lærer- eller tutorside.

Slut med en kort tilbagemelding om, hvad der er bygget, hvordan siden åbnes, hvilke brugerforløb der er afprøvet, og hvilke konkrete oplysninger der eventuelt skal afklares før offentlig udgivelse.

Det færdige resultat skal få besøgende til at tænke: **Jeg kan se, hvordan jeg kommer i gang, hvordan materialet hænger sammen, og hvorfor det hjælper mig med at lære eller undervise i Python.**
