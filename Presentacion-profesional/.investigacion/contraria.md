# Posición contraria y Fundamentos

Fecha de la investigación: 2026-11-24. Ángulo: la mejor evidencia en contra de las seis tesis (a)-(f), mitos documentados, CVs con IA generativa, historia corta del CV y fuentes de referencia del campo.

Marcas de lectura: [L] leí el fragmento relevante del texto en la fuente (vía WebFetch, que devuelve un resumen guiado por mi pregunta, no el texto completo); [M] abstract o metadatos; [S] resumen del buscador o secundario. No hay ningún [L] de texto completo: todo pasó por WebFetch o WebSearch. Puntajes 1-3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U).

Nota de método: tres rondas de búsqueda en total, compartidas entre componentes, porque varios ejes se contestan con las mismas fuentes. Los huecos están al final.

## Resumen en una línea por tesis

| Tesis | Veredicto de la evidencia contraria |
|---|---|
| (a) CV = vidriera de un material aparte | No encontré evidencia en contra; es un marco de organización, no una afirmación empírica. Hueco: nadie lo testeó. |
| (b) Cuantificar solo si es verificable | No hay experimento que pruebe que "cuantificar" mejora resultados; lo que hay es práctica (Bock). Eso apoya la cautela, no la contradice. |
| (c) "6 segundos" y "ATS que rechaza solo" son mitos/exageraciones | Confirmada en lo del 75% (origen sin metodología). Matiz: los ATS sí rechazan por reglas del empleador (preguntas filtro) y hay parsers; "ATS nunca rechaza" también es exagerado. |
| (d) Adaptar por puesto conviene | Apoyada por Galdin y Silbert (empleadores valoraban cartas a medida antes de los LLM), pero la señal se erosionó con IA. Sin experimento específico para CVs. |
| (e) Ortografía cuesta caro | Apoyada (Sterkens; Wiles et al.), con límites: escenario hipotético, y el efecto de herramientas de redacción en un solo mercado. |
| (f) Portfolio/GitHub pesa | Evidencia débil: entrevistas cualitativas pequeñas; ningún estudio mide el efecto en contrataciones. |

## 1. Mitos documentados

### 1.1 El "75% de CVs rechazados por el ATS" (origen: Preptel)

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Fortune, "How to keep your resume from getting lost in cyberspace" (2014-08-22) | https://fortune.com/2014/08/22/how-to-keep-your-resume-from-getting-lost-in-cyberspace/ | Secundaria (periodismo) | 2/1/1/3 | [L] pasaje |
| The Interview Guys, "The ATS Resume Rejection Myth" | https://blog.theinterviewguys.com/?p=1967 | Secundaria, vendedor de servicios | 1/1/1/1 | [S] |
| Rezi, Resume Genius, Davron (citados por el buscador, repiten lo mismo) | https://www.rezi.ai/posts/how-to-make-a-truly-ats-friendly-resume | Secundaria, vendedor | 1/1/1/1 | [S] (una sola fuente efectiva con las anteriores) |

Afirmaciones:
- Fortune 2014 escribe literalmente: "That 75% rejection rate your friend cited probably came from a study by a job search services firm called Preptel". Agrega que Preptel fue fundada por su CEO Jon Ciampi, "an alumnus of ATS maker SumTotal Systems". El artículo no cita a ningún experto independiente que confirme o refute la cifra, ni confirma que el estudio existiera. https://fortune.com/2014/08/22/how-to-keep-your-resume-from-getting-lost-in-cyberspace/
- Según sitios de vendedores (a verificar, son [S]): Preptel no publicó metodología, muestra ni encuesta, y cerró en 2013. Esos mismos textos tienen incentivo comercial. https://www.rezi.ai/posts/how-to-make-a-truly-ats-friendly-resume
- Mi lectura: el origen está documentado de manera débil. Lo seguro es que (1) una fuente de 2014 ya lo atribuía "probablemente" a Preptel y (2) nadie publicó el método. No encontré el estudio original de 2012 de Preptel: hueco.

Contra el mito, lo que sí es cierto (documentación oficial de un ATS):
- Lever: "artificial intelligence isn't an ATS feature that can or should make important decisions"; el filtrado sigue siendo manual por reclutadores. Pero: "Knockout questions defined by recruiters and hiring managers auto-eliminate prospects" que no cumplen requisitos básicos. https://www.lever.co/blog/applicant-tracking-system-myths-debunked [L], vendedor de ATS (practicante institucional), A/P/E/U 2/1/1/2.
- Greenhouse: según su blog, el auto-rechazo es una regla que configuran los reclutadores para criterios específicos. https://my.greenhouse.com/blogs/what-really-happens-after-you-apply-for-a-job [S, no leí la página].
- Encuesta de Enhancv (25 reclutadores de EE.UU.): 92% dice que su sistema no rechaza solo por formato o contenido. Muestra mínima y de un vendedor de CVs; la disputan otros. https://betanews.com/2025/11/10/study-debunks-viral-claim-that-ai-filters-out-most-job-applicants/ [S]. Cifra: no usarla sola.
- Discrepancia a dar completa: "el ATS no rechaza" (Lever, Enhancv) vs. el informe Hidden Workers de HBS+Accenture 2021 (ya relevado): los filtros que configura el empleador descartan candidatos calificados. No son contradictorias si se separa "el software decide por sí solo" de "el empleador configura reglas que filtran".

### 1.2 Los "6 segundos" del CV

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| TheLadders, eye-tracking 2018 (PDF) | https://www.bu.edu/com/files/2018/10/TheLadders-EyeTracking-StudyC2.pdf | Primaria, vendedor | 1/2/2/2 | [S] (PDF comprimido, no pude extraer el texto) |
| ERE, Susan Gygax, "Is the 6-second resume scan a myth?" (2020-10-20) | https://www.ere.net/articles/is-the-6-second-resume-scan-a-myth | Secundaria, practicante | 1/1/1/2 | [L] |
| HR Dive sobre el estudio 2018 | https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/ | Secundaria | 1/1/1/1 | [S] |

Afirmaciones:
- La cifra sale de un estudio de eye-tracking de TheLadders de 2012; en 2018 el promedio de la revisión inicial fue 7.4 segundos. https://www.ere.net/articles/is-the-6-second-resume-scan-a-myth [L]
- Gygax dice que el reporte 2018 "does not state how many recruiters took part, their experience, or how many times the two-stage study was repeated", que no especifica tipo de puesto ni largo de CV, y que la cifra es una "vacuum metric". Es opinión de una practicante, no una refutación revisada por pares. https://www.ere.net/articles/is-the-6-second-resume-scan-a-myth [L]
- Según HR Dive (vía buscador): los segundos miden la decisión inicial "encaja/no encaja", no la lectura completa. [S]
- Un resumen periodístico habla de 30 reclutadores en 2012; no lo pude confirmar contra el informe. [S]
- Veredicto: no es un mito inventado, es un dato de un vendedor, de una tarea acotada (primer filtro) y sin metodología publicada. Corresponde a "exageración / sacado de contexto", no a "falso".

### 1.3 "La carta de presentación ya no se lee"

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Resume Genius, estadísticas de cartas | https://resumegenius.com/blog/cover-letter-help/cover-letter-statistics | Encuesta de vendedor | 1/1/1/1 | [S] |
| ResumeLab (encuesta a decisores de EE.UU.) | https://resumelab.com/uk/cover-letter/are-cover-letters-necessary | Encuesta de vendedor | 1/1/1/1 | [S] |
| Novoresume, estadísticas | https://novoresume.com/career-blog/cover-letter-statistics | Encuesta de vendedor | 1/1/1/1 | [S] |
| The Muse, "55% of hiring managers don't read cover letters" (cita Jobvite 2015) | https://www.themuse.com/advice/55-of-hiring-managers-dont-read-cover-lettersheres-how-to-get-their-attention | Secundaria | 1/1/1/1 | [S] |

Afirmaciones (todas [S], todas de vendedores de CVs, autodeclaradas):
- Resume Genius: 83% de los hiring managers leen la mayoría de las cartas aun si no son obligatorias; 45% la leen antes que el CV. https://resumegenius.com/blog/cover-letter-help/cover-letter-statistics
- ResumeLab: 77% de decisores dicen que la leerían aunque no fuera requerida. https://resumelab.com/uk/cover-letter/are-cover-letters-necessary
- Novoresume: solo 20,8% de los postulantes cree que se leen; cerca de 60% de profesionales de RRHH dice leerlas. https://novoresume.com/career-blog/cover-letter-statistics
- Jobvite 2015 (según The Muse): 55% de los hiring managers consideran las cartas poco importantes. https://www.themuse.com/advice/55-of-hiring-managers-dont-read-cover-lettersheres-how-to-get-their-attention
- Discrepancia a dar: 83% / 77% / ~60% leen vs. 55% las considera sin importancia. Miden cosas distintas ("leer" vs. "importancia"), y es lo que dicen, no lo que hacen. Los vendedores que publican esto venden cartas.
- Evidencia seria sobre cartas: no encontré un estudio revisado por pares que mida el efecto de la carta sobre la decisión. La mejor evidencia indirecta está en 2.2: en un mercado freelance la carta a medida valía antes de los LLM.

### 1.4 Otros mitos (resultado parcial)

- Texto blanco invisible con palabras clave: ManpowerGroup dijo al New York Times que detecta texto oculto en cerca del 10% de los CVs que escanea con IA, y Greenhouse estima 1%; reclutadores "casi siempre" descartan a quien lo usa. Son declaraciones de empresas a la prensa. https://fortune.com/2024/12/05/job-applicants-white-font-hack-hr-applications/ [S]. Y en el informe Greenhouse 2026: 28% de empleadores dice haber visto texto oculto en CVs. https://www.hrdive.com/news/job-candidates-ai-usage-is-obscuring-their-viability-report-finds/875232/ [L]. Veredicto: no funciona en la práctica y es riesgoso; un caso anecdótico de éxito (Entrepreneur) no es evidencia.
- "Una página siempre": no busqué evidencia propia. ResumeGo 2018 (ya relevado, vendedor) es la única que conozco. Hueco.

## 2. CVs y cartas escritos con IA generativa (2023-2026)

### 2.1 Tabla de fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Galdin y Silbert, "Making Talk Cheap: Generative AI and Labor Market Signaling" (arXiv 2511.08785, 2025-11-11) | https://arxiv.org/abs/2511.08785 | Primaria (working paper, econ.GN) | 3/3/2/3 | [M] |
| Cui, Dias y Ye, "Signaling in the Age of AI: Evidence from Cover Letters" (arXiv 2509.25054, 2025-09) | https://arxiv.org/abs/2509.25054 | Primaria (working paper) | 3/3/2/3 | [M] |
| Wiles, van Inwegen, Munyikwa y Horton, Management Science 2024 | https://www.nber.org/papers/w30886 | Primaria | 3/3/2/3 | ya relevado; lo verifiqué solo en el buscador [S] |
| Wiles y Horton, "More, but Worse" (borrador marzo 2024; posible título posterior "Generative AI and labor market matching efficiency", R&R en Management Science) | https://emmawiles.github.io/storage/jobot.pdf | Primaria (borrador) | 3/2/1/2 | [S] |
| Greenhouse, 2026 Future of Hiring Employer Report (vía HR Dive) | https://www.hrdive.com/news/job-candidates-ai-usage-is-obscuring-their-viability-report-finds/875232/ | Encuesta de vendedor de ATS | 1/2/2/2 | [L] |
| TopResume, encuesta a 600 hiring managers de EE.UU. (vía buscador) | https://topresume.com/career-advice/ai-in-hiring-survey | Encuesta de vendedor | 1/1/1/2 | [S] |

### 2.2 Afirmaciones

Efecto sobre callbacks y contrataciones:
- Cui, Dias y Ye usan el lanzamiento (abril de 2023) de una herramienta de IA para cartas en Freelancer.com. Con diferencias en diferencias, el acceso aumentó la alineación textual entre carta y oferta y subió los callbacks. Tras la herramienta, "the correlation between cover letters' textual alignment and callbacks" cayó 51%, y los empleadores pasaron a mirar otras señales, como el historial de trabajos previos. https://arxiv.org/abs/2509.25054 [M]. Datos extra (62% de usuarios elegibles la usó, 17% de las cartas con asistencia; callback +6%) vienen de secundarias y no los confirmé. [S]
- Galdin y Silbert (Freelancer.com): construyen una medida con LLM de cuán a medida es una postulación; los empleadores valoraban las postulaciones a medida antes de los LLM, y después no. En el contrafactual donde la escritura deja de ser señal, los trabajadores del quintil superior de habilidad son contratados 19% menos y los del inferior 14% más; el mercado queda "significantly less meritocratic". Es una simulación de un modelo estructural, no una observación directa. https://arxiv.org/abs/2511.08785 [M]
- Lectura para la base: apoya (d) en su forma débil (la adaptación valía), pero advierte que su valor como señal se erosiona cuando todos adaptan con IA. Ojo: es un mercado freelance, no selección de tiempo completo; ningún estudio acá cubre CVs de empleo en relación de dependencia.
- Wiles et al. (ya relevado): ayuda algorítmica en el CV, +8% contrataciones. https://www.nber.org/papers/w30886. En cambio, en el lado del empleador (Wiles y Horton): los empleadores con asistente de IA para redactar ofertas publicaron ~20% más, escribieron ~40% más rápido, y fueron menos propensos a contratar. https://emmawiles.github.io/storage/jobot.pdf [S]
- Discrepancia a dar: la IA ayuda a quien postula (+8% contrataciones, callbacks mayores) y a la vez degrada la señal (-51% correlación). Las dos cosas son compatibles: mejora individual, empeora el sistema.

Avalancha y detección:
- Greenhouse 2026 (casi 1.350 reclutadores y hiring managers de EE.UU., Reino Unido, Irlanda, Alemania y Australia): 90% de los empleadores de EE.UU. dicen que pudieron haber rechazado candidatos reales porque la postulación parecía falsa o hecha con IA; 86% cambió su proceso; 57% sumó una entrevista humana; los candidatos preseleccionados esperan en promedio 19 días a la primera entrevista; 81% detectó intentos de evadir el filtro de IA (49% declarando habilidades que no tenían, 28% con texto oculto). https://www.hrdive.com/news/job-candidates-ai-usage-is-obscuring-their-viability-report-finds/875232/ [L]. Vendedor de ATS que vende productos para este problema: sesgo posible.
- Greenhouse (vía buscador): postulaciones por vacante +111% de 2022 a 2025. [S], verificar en el informe.
- Detección: en TopResume (600 hiring managers de EE.UU.), 33,5% eligió bien el CV hecho con IA entre cuatro, contra 25% al azar; en Resume Genius, 80% dice poder identificarlo. https://topresume.com/career-advice/ai-in-hiring-survey [S]. Dato claro: confianza declarada alta, acierto bajo. Ambos de vendedores.
- Un estudio con LLMs como filtro que prefieren CVs escritos por LLM (67%-82% de comparaciones, "Xu, Li y Jiang, 2026") apareció solo en un resumen de buscador. [S] No verificado: hueco.
- Falso positivo ya citado en mi búsqueda: el estudio de Stanford "Algorithmic Monocultures in Hiring" (4 millones de postulaciones, ~150 empleadores, datos 2018-2022, un solo proveedor, Pymetrics) NO trata sobre IA generativa en postulantes; sino sobre sesgo de filtros algorítmicos. https://hai.stanford.edu/news/ai-hiring-tools-can-yield-racial-bias-and-systemic-rejection [S]. Sirve solo como contexto de filtros compartidos, no para esta pregunta.

## 3. Evidencia en contra o matices de cada tesis

### (a) El CV es una vidriera de un material aparte
No hallé evidencia en contra ni a favor; es un modelo de organización personal. Un indicio de apoyo: Cui et al. muestran que cuando la carta pierde valor, los empleadores pasan al historial de trabajos previos, es decir, al "material" de fondo. https://arxiv.org/abs/2509.25054 [M]. Hueco: no hay estudio sobre mantener un "master CV".

### (b) Cuantificar solo si es verificable
- A favor de cuantificar: Laszlo Bock (ex-SVP de personas en Google), fórmula "Accomplished [X] as measured by [Y] by doing [Z]". Es práctica de un directivo, no estudio. https://www.inc.com/melanie-curtin/job-hunting-a-google-executive-says-to-use-this-3-part-resume-formula-to-stand-out.html [S]
- En contra / límite: no encontré ningún experimento que compare bullets con número contra bullets sin número. Mi búsqueda de "resume bullet quantification experiment" no dio nada. Todo lo que se dice de "los números mejoran el CV" es práctica o de vendedores. Esto refuerza la tesis (b): la fórmula XYZ es una buena heurística, pero su efecto en selección no está medido. Las cifras inventables también son un riesgo (el informe Greenhouse registra que 49% de los empleadores vio declaraciones de habilidades inexistentes).

### (c) "6 segundos" y "ATS que rechaza solo" son exageraciones
Ver 1.1 y 1.2. El contra-matiz honesto: existen preguntas filtro y reglas de auto-rechazo configuradas por el empleador (Lever, Greenhouse); y con avalanchas de postulaciones (111% más por vacante, [S]) los reclutadores sí aplican filtros automáticos de IA (52% ya usa entrevistas con IA, Greenhouse). Entonces "el ATS no filtra" también se queda corto en 2026.

### (d) Adaptar por puesto conviene
A favor: Galdin y Silbert (medida de alineación; los empleadores la valoraban pre-LLM). En contra / límite: la correlación entre alineación y callback cayó 51% con IA (Cui et al.); si todos adaptan con IA, adaptar solo equivale a cumplir. Sin experimento de campo que compare CV adaptado vs genérico (búsqueda sin resultados).

### (e) Los errores de ortografía cuestan caro
- A favor: Sterkens et al., PLoS ONE 2022: escenario con 445 reclutadores; con muchos errores, -18,5 pp en probabilidad de entrevista; con pocos, -7,3 pp. Cerca de la mitad de la penalidad se explica por percibir menor competencia interpersonal, responsabilidad y capacidad mental. https://pmc.ncbi.nlm.nih.gov/articles/PMC10075394/ [S] (ya relevado)
- Límites: es un experimento de escenario, no contratación real; antes se limitaba a ocupaciones de oficina y a muchos errores por CV. Wiles et al. (campo, ~medio millón de postulantes): +1 pp de tasa de error se asocia con -3% de probabilidad de contratación (asociación; por eso corrieron el experimento). https://arxiv.org/pdf/2301.08083v1.pdf [S]. Ninguna se replicó de forma independiente en las fuentes que vi.
- Contra-evidencia directa (que los errores NO importen): no la encontré. Hueco.

### (f) Portfolio y GitHub pesan en selección técnica
| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Marlow y Dabbish, CSCW 2013 | https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf | Primaria (entrevistas) | 3/2/2/3 | [S] |
| Estudio con 15 reclutadores de Brasil, Canadá y EE.UU. (2024) | https://homepages.dcc.ufmg.br/~figueiredo/publications/latam2024preprint.pdf | Primaria (exploratoria) | 2/2/2/2 | [S] |
| arXiv 2409.12544 (sesgo de LLMs al reclutar por perfil de GitHub) | https://arxiv.org/abs/2409.12544v1 | Primaria | 2/1/1/2 | [S] |

- Marlow y Dabbish: los entrevistados trataban la actividad en GitHub como más verificable que una lista estática de credenciales. Un blog de vendedor dice 13 entrevistas; no lo verifiqué. [S]
- Estudio de 2024: GitHub da "una comprensión más matizada" que métodos tradicionales; muestra de 15, exploratoria. [S]
- En contra: una tesis halló que un perfil de GitHub generado fue apenas preferido por reclutadores técnicos pese a ser incompleto, es decir, la señal es difícil de leer. [S] Y ningún estudio mide cuánto mejora la contratación.
- Veredicto: (f) está respaldada por práctica y entrevistas, no por efecto medido. Conviene afirmarlo con ese grado de confianza: "plausible, poco medido". El comentario de Miranda Nash (Jobscience) en Fortune 2014, "Expand your presentation of your work, using a medium beyond your resume", es otra práctica que apunta igual. https://fortune.com/2014/08/22/how-to-keep-your-resume-from-getting-lost-in-cyberspace/ [L]

## 4. Fundamentos: historia corta del CV

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Workable, Daniel Howden, "Die hard: the troubled history of the resume" (pub. 2016-02-04, mod. 2023-09-26) | https://resources.workable.com/stories-and-insights/history-of-the-resume | Secundaria, vendedor | 1/2/2/1 | [L] pasajes |
| Britannica Money, "curriculum vitae" | https://www.britannica.com/money/curriculum-vitae-document | Secundaria (enciclopedia) | 3/1/1/2 | [S] (403 al leer) |
| Wikipedia, Résumé | https://en.wikipedia.org/wiki/R%C3%A9sum%C3%A9 | Terciaria | 2/2/1/1 | [S] |
| Carta de Leonardo a Ludovico Sforza, Codex Atlanticus, f. 1082r | https://artsandculture.google.com/asset/letter-to-ludovico-il-moro/DAEncWvZmqoodA | Primaria (reproducción) | 2/1/1/3 | [S] |
| Leonardo-online, MPIWG Berlín (catálogo) | https://leonardo-online.mpiwg-berlin.mpg.de/en/div-classleo_title_authorleonardo-da-vincidivdiv-classleo_title_titlep-classtedesco_catalogo_titolo_dbewerbungsschreiben-an-ludovico-sforzapdivdiv-classleo_title_dateplacep-classtedesco_catalogo_dati_tec_dca-1482-pdiv | Primaria (catálogo académico) | 3/2/1/3 | [S] solo el título |

Afirmaciones:
- Leonardo 1482: hecho: existe una carta a Ludovico Sforza (Duque de Milán), conservada en el Codex Atlanticus, que enumera capacidades casi todas de ingeniería militar; Leonardo pasó unos 17 años en Milán. [S] https://artsandculture.google.com/asset/letter-to-ludovico-il-moro/DAEncWvZmqoodA
- Es mito o exageración llamarlo "el primer CV": hallé fuentes que dicen "uno de los primeros", y otra que dice "cartas de presentación", no CV. Workable: "quite clearly not a resume. It's a cover letter". https://resources.workable.com/stories-and-insights/history-of-the-resume [L]. Británica es más mesurada: "forerunner" del CV actual. [S]
- Matices que cuentan: la fecha varía entre 1482 y ~1483 según la fuente; la copia conservada es un borrador no autógrafo (según un resumen de buscador, [S]); la carta se envió con una lira (según una fuente secundaria). El catálogo del MPIWG titula el documento "Bewerbungsschreiben" (carta de postulación), c. 1482. No encontré ninguna fuente académica que lo llame CV.
- Historia moderna: según Workable, "By the 1930s a resume was almost normal"; "As recently as 1950 your age, weight and the origin of your parents were considered essential elements of the CV", con foto formal. https://resources.workable.com/stories-and-insights/history-of-the-resume [L]. Etimología: "résumé" del francés résumer "resumir"; "curriculum vitae" del latín "curso de la vida". [S] Britannica.
- Recomendación de redacción para la base: decir "una carta de 1482 de Leonardo para entrar al servicio de Ludovico Sforza se cita como antecedente; es una carta de postulación, no un CV en el sentido actual".
- Hueco: no encontré una historia académica del CV (fechas del uso moderno, divergencia CV/résumé por país), ni el OED.

## 5. Fuentes de referencia del campo, con puntaje de confianza

Confianza global (1 = baja, 3 = alta) según qué tan fuerte es como base para afirmar algo.

| Fuente | Tipo | URL | Confianza | Notas |
|---|---|---|---|---|
| Sterkens et al., PLoS ONE 2022 | Primaria, escenario | https://pmc.ncbi.nlm.nih.gov/articles/PMC10075394/ | 3 | Ya relevado; ver límites en (e) |
| Wiles, van Inwegen, Munyikwa, Horton, Management Science 2024 | Primaria, campo | https://www.nber.org/papers/w30886 | 3 | Un solo mercado (freelance) |
| Galdin y Silbert 2025 | Primaria, WP | https://arxiv.org/abs/2511.08785 | 2 | Preprint y simulación |
| Cui, Dias y Ye 2025 | Primaria, WP | https://arxiv.org/abs/2509.25054 | 2 | Preprint |
| Quillian y Lee 2018 | Meta-análisis | ya relevado | 3 | Discriminación, no formato |
| Hidden Workers, HBS+Accenture 2021 | Secundaria institucional | ya relevado | 2 | Sobre filtros del empleador |
| Kessler, Low y Sullivan, "Incentivized Resume Rating" (AER 2019, NBER w25800) | Primaria, experimento | https://nber.org/system/files/working_papers/w25800/w25800.pdf | 3 | [S]: método para medir cómo evalúan CVs; útil para matizar "callback" |
| Marlow y Dabbish 2013 | Primaria, cualitativa | https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf | 2 | 13 entrevistas (no verificado) |
| Lever (mitos del ATS) | Documentación de vendedor de ATS | https://www.lever.co/blog/applicant-tracking-system-myths-debunked | 2 | [L]; una voz con interés |
| Greenhouse, informe 2026 | Encuesta de vendedor de ATS | https://www.hrdive.com/news/job-candidates-ai-usage-is-obscuring-their-viability-report-finds/875232/ | 2 | [L] vía HR Dive |
| McDowell, *The Google Resume* (Wiley, 2011) | Libro, practicante | https://oreilly.com/library/view/the-google-resume/9780470927625 | 2 | Trabajó 3 años en Ingeniería de Google, estuvo en el comité de contratación y entrevistó a más de 120 candidatos [S] |
| Bock, *Work Rules!* (2015), fórmula XYZ | Libro, practicante | https://www.inc.com/melanie-curtin/job-hunting-a-google-executive-says-to-use-this-3-part-resume-formula-to-stand-out.html | 2 | Solo vía Inc.com [S]; sin libro leído |
| TheLadders, eye-tracking 2012/2018 | Vendedor | https://www.bu.edu/com/files/2018/10/TheLadders-EyeTracking-StudyC2.pdf | 1 | Sin n declarado en el reporte 2018 |
| Resume Genius, ResumeLab, Novoresume, Zety, TopResume | Vendedores | ver 1.3 y 2.1 | 1 | Encuestas autodeclaradas |
| Workable (historia) | Vendedor | https://resources.workable.com/stories-and-insights/history-of-the-resume | 1 | Útil para el argumento de la carta |
| Guías de career services (Harvard OCS, MIT CAPD) | Guías | sin URL verificada | sin puntuar | No las encontré en esta tanda (Harvard OCS: la búsqueda no devolvió nada). Hueco. |

## 6. Recursos canónicos propuestos

- Para el mito del ATS: Fortune 2014 (origen Preptel) + la página de Lever sobre mitos (qué sí hace un ATS: preguntas filtro). Fijarse en: que la cifra no tiene método y que el rechazo existe cuando lo configura el empleador. Falta una fuente primaria de Greenhouse o Workday: hueco.
- Para IA y señal: Cui, Dias y Ye 2025 (la caída del 51% de la correlación) más Galdin y Silbert 2025 (el modelo del efecto en meritocracia). Fijarse en qué es modelo y qué es observación, y que ambos son preprints de un mercado freelance.
- Para la avalancha: informe Greenhouse 2026, con la cautela de que es de un vendedor.
- Para la historia: Workable (mejor argumento, pero vendedor) junto a Britannica para el "precursor". No hay recurso canónico académico: hueco.
- Para (f): Marlow y Dabbish 2013 como único estudio fundacional; marcar como "plausible, poco medido".

## 7. Si el árbol no coincide con cómo divide el campo mi ángulo

- Los mitos aparecen repartidos: el ATS y los "6 segundos" son del tema "cómo se lee un CV", la carta pertenece a "documentos", y la IA a un eje transversal que el campo trata aparte (economía laboral de señales). Sugiero una nota transversal "Señales que se devalúan: qué pasa cuando todos usan IA" en vez de repartirla por componentes. No leí ALCANCE.md línea por línea para esta comparación; es una sugerencia desde el material, no desde el árbol.

## 8. Huecos (declarados)

1. El estudio original de Preptel (2012) no apareció; el origen se apoya en Fortune ("probablemente") y vendedores.
2. Ningún experimento sobre bullets con y sin números, ni sobre CV adaptado vs genérico.
3. Ninguna evidencia en contra de (e), ni estudios de largo de CV más allá de ResumeGo (vendedor).
4. Ningún estudio académico sobre el efecto de cartas de presentación; solo encuestas de vendedores.
5. Los números de Greenhouse 2026 (111% más postulaciones) y del estudio "Xu, Li y Jiang 2026" provienen de resúmenes de buscador y no los verifiqué.
6. El informe de TheLadders 2018 no se pudo extraer (PDF comprimido); sus números salen de HR Dive y de críticas.
7. Britannica y Smarthistory devolvieron 403/404; Wikipedia sobre la carta de Leonardo dio 404. La carta se apoya en secundarias.
8. Sin historia académica del CV, ni OED, ni guías de career services (Harvard OCS, MIT CAPD) en esta tanda.
9. Nada de lo que traje es [L] de texto completo: todo fue por resúmenes de herramienta.
10. No verifiqué el contenido de The Interview Guys, Rezi ni Resume Genius contra sus páginas; son [S].
