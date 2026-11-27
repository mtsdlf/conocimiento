# Verificación contra el texto completo: Resistencia

Fecha: 2026-11-27. Grupo: las siete notas de `Entrenamiento/Resistencia/`. Texto completo bajado de Europe PMC (`fullTextXML`), de pmc.ncbi.nlm.nih.gov con curl o de PDF abiertos (repositorios de Aalborg y DCU, y el sitio del laboratorio de Lenhart). Springer, IJSPP, JSCR, MSSE y BJSM no dieron texto completo; vdoto2.com devolvió 403. Donde no hubo texto completo, se miró el resumen en Europe PMC para ver si coincidía; si el propio resumen contradecía la nota, se corrigió y se marca así.

Resultados: **S** sostiene, **C** corregida, **Su** suavizada, **SA** sin acceso (queda como estaba), **CR** corregida desde el resumen (sin texto completo).

## resistencia.md

| Afirmación | Fuente | Resultado | Cita del texto completo |
|---|---|---|---|
| 17,8 lesiones/1000 h en novatos y 7,7 en recreativos; rango 2,5 a 33 | Videbæk 2015, https://pmc.ncbi.nlm.nih.gov/articles/PMC4473093 | S | "weighted injury incidence of 17.8 (95 % CI 16.7–19.1) in novice runners and 7.7 (95 % CI 6.9–8.7) in recreational runners"; "13 original articles"; "ranged from a minimum of 2.5 … to a maximum of 33.0" |
| GRONORUN 20,8 % vs 20,3 % | Buist 2008, https://research.rug.nl/en/publications/no-effect-of-a-graded-training-program-on-the-number-of-running-r/ | SA (resumen del repositorio; el PDF devolvió HTML). Lo reporta igual Damsted 2018 completo | Damsted: "a graded training program with 10% average increase in weekly volume vs. a standard training program with 24% average increase in weekly volume" |
| Concurrente: no compromete hipertrofia ni fuerza máxima; atenúa la explosiva; sin diferencia correr/pedalear | Schumann 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8891239 | S | "A total of 43 studies were included"; SMD "−0.28 … for … explosive strength"; "No significant effects were found for … type of aerobic training (cycling vs. running)"; más atenuación "within the same session" |
| FC de muñeca: −7,26 lpm pesas, −4,55 lpm ciclismo | Citada como PMC8273688 | C (atribución) | PMC8273688 es Mühlen y otros 2021, recomendaciones de método, y no trae esas cifras. Las cifras son de Zhang y otros 2020 (https://pubmed.ncbi.nlm.nih.gov/32552580/, sin texto abierto; resumen: "-0.51 bpm (-1.60 to 0.58) during treadmill activities … resistance training (-7.26 bpm …) and cycling (-4.55 bpm …)") |
| Seiler 80/20; Jamnick; Wilson 2012; Wewege 2017 | — | SA | — |

## zonas-de-intensidad.md

| Afirmación | Fuente | Resultado | Cita |
|---|---|---|---|
| VT1: la homeostasis empieza a ser desafiada; VT2: las alteraciones se aceleran | MacIntosh 2021, https://pmc.ncbi.nlm.nih.gov/articles/PMC8493117 (= fphys.2021.682233) | S | "The first threshold occurs at the metabolic rate associated with the initial challenge to physiological homeostasis"; "The second threshold represents the metabolic rate above which the disturbance to physiological homeostasis accelerates disproportionally" |
| El % del máximo tiene poco fundamento | Jamnick 2020 (sin acceso) + MacIntosh 2021 | SA (Jamnick); S como segunda fuente (MacIntosh) | MacIntosh: "percentage of maximal heart rate or of maximal oxygen uptake … does not acknowledge the individual variability of these metabolic boundaries" |
| Talk test y RPE válidos para VT y RCP; agrado más débil | Bok 2022, Sports Med (Springer bloqueó) | SA; se sumó del resumen: "RPE of 10-11 … reflective of the ventilatory threshold, while … RPE of 13-15 … respiratory compensation threshold" | — |
| r 0,71, 0,84 y 0,81 "el resumen no dice con qué" | Jeanes 2011, https://pubmed.ncbi.nlm.nih.gov/21311346/ | CR | Resumen: "Fourteen well-trained … performed 2 incremental exercise tests (to evaluate reproducibility)"; "The HR (r = 0.84), RPE (r = 0.81), and Talk Test (r = 0.71) responses during paired incremental tests were well correlated". Son correlaciones entre dos pruebas repetidas, no entre los tres métodos |
| Talk test más ligado al umbral de lactato | Quinn y Coons 2011, https://pubmed.ncbi.nlm.nih.gov/21774751/ | SA (resumen coincide; n = 15, de 18 a 35 años) | — |
| Zona 1 < 2 mM (Seiler); consenso de zona 2 (Sitko 2025) | — | SA (resúmenes coinciden) | — |
| Cinco ritmos de Daniels | https://vdoto2.com/LearnMore/TrainingDefinitions | SA (403) | — |

## distribucion-de-intensidad.md

| Afirmación | Fuente | Resultado | Cita |
|---|---|---|---|
| Stöggl y Sperlich llaman piramidal al 80:20 de la élite y reservan polarizado para poca zona 2 | Stöggl y Sperlich 2015, https://pmc.ncbi.nlm.nih.gov/articles/PMC4621419 | C | Lo contrario: el 80:20 es su cifra del polarizado. "The distribution between low and high intensity training is often quantified as 80:20%, or 75–80% with low intensity, 5% threshold intensity, and 15–20% as high intensity training"; "The majority of studies present a 'pyramidal' TID"; "Some world-class athletes appear to adopt a so-called 'polarized' TID … during certain phases of the season" |
| "El reparto de umbral no tiene definición en las fuentes" | Stöggl y Sperlich 2015; Oliveira 2024 | C | Oliveira: "In THR training, volume in Z2 is emphasized (> 35%), with the remaining volume distributed between Z1 and Z3"; "POL consists of high training volumes in Z1 (75–80%), moderate volumes in Z3 (15–20%), and a small fraction in Z2 (< 10%)" |
| Índice de polarización distingue los repartos | Treff 2019, https://pmc.ncbi.nlm.nih.gov/articles/PMC6582670 | S (+ fórmula) | "calculated as log 10 (Zone 1/Zone 2 ∗ Zone 3 ∗ 100)"; "If PI > 2.00 a.U., the TID is defined as 'polarized'"; "the percentage of Zone 3 must be higher than Zone 2 to result in a PI > 2.00" |
| Oliveira: 17 estudios, 437; superior solo en VO2pico; < 12 semanas, muy entrenados | Oliveira 2024, https://pmc.ncbi.nlm.nih.gov/articles/PMC11329428 | S (+ tamaño del efecto) | "SMD = 0.24 [95% CI 0.01, 0.48] … high certainty"; "TT (SMD = – 0.01 [95% CI -0.28, 0.25]" |
| Los dos metaanálisis "concuerdan en la dirección pero no en el alcance"; Oliveira "restringe" a Rosenblat | Oliveira 2024 | C | "Their results suggested superiority of POL compared to THR for TT improvement, which is in opposition to our findings"; Rosenblat tenía "n = 112" |
| Rosenblat: 3 estudios, ES −0,66, PEDro 4 y 5 | Rosenblat 2019 (JSCR) | SA (resumen coincide) | — |
| Ensayo en 30 recreativos, autoría no verificada | Muñoz y otros 2014, https://pubmed.ncbi.nlm.nih.gov/23752040/ | CR (autoría y duración, de los metadatos y el resumen) | Autores: Muñoz I, Seiler S, Bautista J, España J, Larumbe E, Esteve-Lanao J; "over the 10-wk intervention period" |
| Seiler 2010 | — | SA (resumen coincide) | — |

## metodos-de-resistencia.md

| Afirmación | Fuente | Resultado | Cita |
|---|---|---|---|
| "Revisión de 2019", autoría no verificada: continuo mejor para la economía en recreativos | González-Mohíno y otros 2020, https://www.doi.org/10.1007/s40279-019-01201-x | CR (identificación; Springer bloqueó el texto) | Resumen: metaanálisis, "Six studies (seven trials) … 295 participants"; "0.28 [95% CI 0.01, 0.54]"; "Continuous training seems, overall, a better strategy than interval training to reduce the oxygen cost in recreational endurance runners" |
| Buchheit y Laursen: nueve variables | Sports Med 2013 | SA (resumen coincide) | — |
| Wewege 2017 | — | SA | — |

## plan-de-carrera.md

| Afirmación | Fuente | Resultado | Cita |
|---|---|---|---|
| GRONORUN: 532 novatos, 13 vs 8 semanas, 20,8 % vs 20,3 % | Buist 2008 | SA (resumen del repositorio); detalle sumado desde Damsted completo | ver arriba |
| Nielsen 2012: "no fue posible identificar" | https://pmc.ncbi.nlm.nih.gov/articles/PMC3290924/ | S (+ detalle) | "nine retrospective cohort studies, 13 prospective cohort studies, six case-control studies, and three randomized controlled trials … mean quality score was 44.1%. Conflicting results were reported" |
| "Cohorte de Nielsen": más lesiones ligadas a la distancia, no el total; "una revisión vio evidencia moderada" | Citada como https://vbn.aau.dk/ws/files/284775170/e000333.full.pdf | C (atribución) y Su | Ese PDF es Run Clever (Ramskov 2018), no la cohorte. La cohorte es Nielsen 2014 (https://pubmed.ncbi.nlm.nih.gov/25155475/, solo resumen: 874 novatos, "hazard ratio = 1.59; 95% confidence interval: 0.96, 2.66; P = .07"). No se encontró la "evidencia moderada"; la revisión que trata el tema dice lo contrario: Damsted 2018, https://pmc.ncbi.nlm.nih.gov/articles/PMC6253751/: "Very limited evidence exists supporting that changes (increases and decreases) in training load are associated with injury development. Specifically, no evidence was found to support the use of the so-called '10% rule'" |
| Run Clever: mismo riesgo en volumen o intensidad | https://pmc.ncbi.nlm.nih.gov/articles/PMC5841490 | S (matiz) | "A similar proportion of runners sustained injuries in the two running schedules"; 447 en el período de 16 semanas; "RD 16 weeks =−14.0% (−36.9% to 8.9%)" |
| Videbæk 17,8 vs 7,7 | ver resistencia.md | S | — |
| Couch to 5K: 110, 27,3 %, 21 lesiones (19 %), sin evidencia empírica | https://pmc.ncbi.nlm.nih.gov/articles/PMC10487403/ | S (+ detalle) | "Twenty-one injuries were reported during the programme (19%)"; "Only 27.3% completed the programme"; "there is no empirical evidence to support the design of Couch-to-5k"; 90 de 110 mujeres; edad 47,1; "Previous injury increased the risk of new injury (OR 7.56" |
| ACSM 2011 "≥20 min·d on ≥3 d·wk" | MSSE | SA (resumen coincide) | — |
| Bosquet 2007: 2 semanas, 41-60 % | MSSE | SA (resumen coincide; dice "exponentially reduced") | — |
| Pfitzinger | finalsurge.com | SA (no se abrió) | — |

### Hueco: volúmenes para recreativos de 10 y 21 km

Tres búsquedas. Se encontró y leyó completo Fokkema y otros 2020, Scand J Med Sci Sports, acceso abierto: https://pmc.ncbi.nlm.nih.gov/articles/PMC7496388/. Es observacional (cuestionarios, cohorte prospectiva), no un plan. Se sumó a la nota con esa atribución.

Citas: "556 participants of a half marathon"; "They ran on average 29.9 (SD 19.4) km/wk, with a training pace of 5:45 (SD 0:45) minutes per km and a longest endurance run of 19.3 (SD 6.5) km, and finished their race on average in 2:00:05"; "In half‐marathon runners, a high training volume (>32 km/wk) (β −4.19, 95% CI: −6.52;−1.85) and a long endurance run (>21 km) (β −3.87 …) were associated with a faster finish time"; "No associations between training characteristics and RRIs were identified". Los cortes (< 20, 20 a 32, > 32 km; < 15, 15 a 21, > 21 km) los fijaron los autores. Limitaciones: datos autorreportados; 14,7 % de los "de media" corrían también la maratón.

Descartados: Knopp y otros 2024 (Sports Med Open; planes de maratón, no de 10 o 21 km); planes de federaciones o clubes (England Athletics vía marcas comerciales), que no son guías publicadas por la federación. Sigue sin fuente un plan de 10 km con ritmos y kilómetros.

## tecnica-de-carrera.md

| Afirmación | Fuente | Resultado | Cita |
|---|---|---|---|
| Heiderscheit: 45 recreativos, ±5 y ±10 %; aumentos sutiles bajan mucho la carga; 10-20 % difícil | https://pmc.ncbi.nlm.nih.gov/articles/PMC3022995 | S (matiz) | "Less mechanical energy was absorbed at the knee (p<0.01) during the +5% and +10% step rate conditions, while the hip (p<0.01) absorbed less energy during the +10% condition only"; "subtle increases in step rate can substantially reduce the loading to the hip and knee"; "a 10–20% increase … may prove challenging to adopt and compromise performance" (de la introducción, citando trabajos previos) |
| Lenhart: 110 % baja 14 % la fuerza patelofemoral | https://uwnmbl.engr.wisc.edu/pubs/msse14_lenhart.pdf | S (+ diseño) | "30 healthy adults"; "musculoskeletal model to estimate … patellofemoral joint forces"; "Increasing step rate to 110% of the preferred reduced peak patellofemoral joint force by 14%" |
| Metaanálisis 2022: evidencia insuficiente | Anderson y otros 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC9441414/ | S (+ detalle) | "Thirty-seven studies … injury (n = 2)"; "very limited evidence indicated that increasing running step rate is associated with improvements in pain … in recreational runners with patellofemoral pain"; "insufficient evidence to conclusively determine the effects … on injury and performance" |
| Revisión 2014: "siete de nueve estudios no hallaron asociación; dos asociaron cadencia baja con fracturas por estrés" | Schubert y otros 2014, https://pmc.ncbi.nlm.nih.gov/articles/PMC4000471 (= PMID 24790690) | C | Esa revisión no estudia lesiones: "Ten studies met the inclusion/exclusion criteria", todos de biomecánica; conclusión: "an increased stride rate … appears to reduce the magnitude of several key biomechanical factors associated with running injuries". La cifra 7 de 9 no está; se sacó |
| Revisión 2025 favorable | Cureus 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC12440572 | S | "evidence suggested a preventive effect on injuries such as patellofemoral pain and tibial stress fractures. Cadence retraining appears to be a low-cost, accessible, and effective strategy"; "Further high-quality prospective studies are needed" |
| Daoud 2012 | MSSE | SA (resumen coincide) | — |
| Burke 2021: 3 de 6, calidad muy baja, "sin estudios que sigan a los corredores hacia adelante" | https://doras.dcu.ie/28875/1/… | S en lo central; C en lo prospectivo | "We reviewed 13 studies"; "Three of the 6 studies looking at categorical FSP found rearfoot strikers have a significantly greater retrospective injury rate … with 1 other study noting a greater risk associated with midfoot and forefoot strike"; "Three of the 13 studies included were prospective cohort studies"; "More large-scale prospective studies are required" |
| Metaanálisis 2020 de pisada | Anderson y otros 2020 (Sports Med) | SA (resumen coincide: "changing strike pattern cannot be recommended for an uninjured RFS runner") | — |
| Nigg 2015 | BJSM | SA | — |
| Revisión posterior: evidencia limitada en los cuatro paradigmas | Agresta y otros 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8959543 | S (+ recomendación y dato sobre pronación) | "We find that evidence in support of any paradigm is generally limited … recommend footwear that is lightweight, comfortable, and has minimal pronation control technology"; "pronation was not found to be a risk factor for non-specific injuries in a large prospective study of novice runners (Nielsen et al., 2014)" |

## calzado-y-relojes.md

| Afirmación | Fuente | Resultado | Cita |
|---|---|---|---|
| Placa: 2-3 % menos de demanda metabólica, sin atribuirlo a la placa sola | Kobayashi y otros 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC12827780/ | S (+ detalle) | "Fourteen studies met the inclusion criteria"; "lowered metabolic demand by ∼2%–3% across outcomes (mean −2.75%; range −0.99% to −4.47%)"; "Certainty of evidence was moderate"; "causality cannot be attributed to the plate alone" |
| Healey y Hoogkamer 2022, "citado en la revisión de 2026": la rigidez sola no cambia la economía | misma revisión | C (atribución) | Healey no está citado. La revisión dice: "growing consensus that the metabolic benefit arises from the interaction between greater LBS … and the midsole's energy return properties, rather than any single component by itself" |
| Sin estudios en recreativos | misma revisión | Su (matiz) | Incluye "Nielsen et al. … 37 … Recreational runners" a "12.3 km·h −1" |
| Clavos con placa 2025 | Wu y otros 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC12672227 | S (+ población) | "foam-only AFT spikes improved RE … in national-level athletes. Adding a carbon plate did not guarantee a metabolic benefit and may increase energetic cost when shoe stiffness exceeds an athlete-specific optimum" |
| Respuesta individual −10 % a +14 % (2023) | sin URL | SA | — |
| FC de muñeca −7,26 / −4,55 | citada como PMC8273688 | C (atribución) | ver resistencia.md: es Zhang 2020 (resumen). PMC8273688 (Mühlen 2021) sostiene que las validaciones de laboratorio son mayormente en cinta: "Lab based protocols … usually included treadmill locomotion … or a combination of treadmill locomotion and ergometer cycling" |
| ±15 lpm, 0,98 | Sartor 2018, https://pmc.ncbi.nlm.nih.gov/articles/PMC5984393 | S (+ detalle) | "The limits of agreement … were within the range of ±15 bpm. The OHRM showed a concordance correlation coefficient of 0.98. Overall, the mean absolute error was not larger than 3 bpm"; 95 % del tiempo dentro de 10 lpm "during the most intense activity (i.e., running)"; 199 voluntarios; autores de Philips Research |
| Validaciones en cinta favorecen al reloj; trail con banda | informe | Su (marcado como lectura propia y recomendación del informe) | — |
| Estudio 2025 de exactitud moderada | sin URL | SA | — |
| Forerunner 245: 5,7 % en 23 corredores | Düking 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC9286863/ | S (+ detalle) | "Twenty-three non-competitive recreational runners"; "MAPE of 5.7% (corresponding to an error of 2.80 ml∙min −1 ∙kg −1 )"; "within the lower ˙VO 2peak category, the smartwatch tends to overestimate … whereas within the higher ˙VO 2peak category values tend to be underestimated" |
| Forerunner 265 (~18 %), Venu SQ | sin URL | SA | — |
| Garmin: aire libre con GPS "o con potenciómetro" | manual, https://www8.garmin.com/manuals/webhelp/GUID-9D99A9D4-467A-4F1A-A0EA-023184FEA3DD/EN-US/GUID-3E971364-A756-4057-B22D-C41250B2A82B.html | C | Es el manual del Forerunner 955. Para correr: frecuencia cardíaca de muñeca o banda, "Run for at least 10 minutes outdoors" con GPS; el potenciómetro figura solo para ciclismo |
| Métricas propias (tiempo de recuperación) | — | SA (hueco) | — |
