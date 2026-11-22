# Informe crudo: evaluación competitiva, entrevista de cambio y análisis de reseñas

Investigación del 2026-11-22 para ampliar UX (issue #24 de mtsdlf/conocimiento). Tres componentes: `Evaluacion/evaluacion-competitiva`, `Investigacion/entrevista-de-cambio`, `Investigacion/analisis-de-resenas`. Marcas: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o de buscador. Lo leído vía WebFetch pasa por el resumen de una herramienta: las citas entre comillas son las que la herramienta devolvió como literales; conviene cotejarlas en el original. Se agotó el presupuesto de búsquedas web a mitad de la ronda; lo que quedó sin buscar está en huecos.

## Mapa de fuentes

- Método de UX: NN/g (artículos de práctica), MeasuringU (Sauro y Lewis; estadística aplicada a UX), Journal of Usability Studies.
- JTBD: el sitio de Moesta y Spiek (jobstobedone.org, The Re-Wired Group), su libro, guías de práctica (thoughtbot).
- Reseñas: economía y sistemas de información (CACM, Management Science), ingeniería de requisitos (IEEE RE), análisis cualitativo (Braun y Clarke; NN/g).

## 1. Evaluación competitiva

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Tim Neusesser, NN/g, Competitive Usability Evaluations (5-ene-2024): https://www.nngroup.com/articles/competitive-usability-evaluations/ | primaria de práctica | 3/2/2/3 | [L] vía herramienta |
| Kate Moran, NN/g, 7 Steps to Benchmark Your Product's UX (3-may-2020): https://www.nngroup.com/articles/benchmarking-ux/ | primaria de práctica | 3/2/2/2 | [L] vía herramienta |
| MeasuringU, Competitive & Benchmark UX Evaluation: https://measuringu.com/?p=8464 | página de servicio de un proveedor | 2/1/1/2 | [L] vía herramienta |
| MeasuringU, SUPR-Q: https://measuringu.com/suprq/ | página del instrumento (proveedor y autor) | 2/2/1/3 | [L] vía herramienta |
| Sauro (2015), SUPR-Q: A Comprehensive Measure of the Quality of the Website User Experience, Journal of Usability Studies, pp. 68-86: https://uxpajournal.org/?p=2506 | primaria revisada | 3/3/2/3 | [S] (la página no tiene PDF; abstract según buscador) |
| Lewis y Sauro, Sample Sizes for Comparing UX-Lite Scores (11-feb-2026): https://measuringu.com/sample-sizes-for-comparison-of-ux-lite-scores/ | primaria de práctica | 3/3/2/3 | [L] vía herramienta |
| Lewis y Sauro, Sample Sizes for Comparing SUS to a Benchmark (1-mar-2022): https://measuringu.com/sample-sizes-for-SUS-benchmark-tests | primaria de práctica | 3/3/2/2 | [L] vía herramienta |
| Sauro y Lewis, Quantifying the User Experience, 2.ª ed. (2016), cap. 5 "Is There a Statistical Difference between Designs?": https://www.oreilly.com/library/view/quantifying-the-user/9780128025482/B9780128023082000059/B9780128023082000059_1.xhtml | libro de texto | 3/3/3/3 | [S] (403; índice y abstract según buscador) |
| Jakob Nielsen, NN/g, Jakob's Law of Internet User Experience (video, 18-ago-2017): https://www.nngroup.com/videos/jakobs-law-internet-ux/ | primaria de práctica | 3/1/1/2 | [S] (resumen de la página) |
| Jakob Nielsen, NN/g, Do Interface Standards Stifle Design Creativity? (21-ago-1999): https://www.nngroup.com/articles/do-interface-standards-stifle-design-creativity/ | primaria de práctica | 3/2/1/2 | [L] vía herramienta |

Afirmaciones:

- NN/g define la evaluación competitiva como "Comparing your product against several competing designs" y distingue dos métodos: revisión competitiva (un experto examina productos relacionados para encontrar fortalezas, debilidades, tendencias y patrones) y test competitivo (un experto corre un test de usabilidad sobre el diseño propio y los de competidores). https://www.nngroup.com/articles/competitive-usability-evaluations/ [L]
- Típicamente "focuses on 2 to 4 competitors' sites". Con muchos competidores, una revisión inicial elige los de contenido parecido, buena UX, diseño innovador o más superposición de clientes; sugiere mirar más allá de los rivales directos (empresas chicas, rubros vecinos). Misma URL [L].
- En el test competitivo cada participante usa dos o tres sitios; "Testing more than 3 sites with any given participant can overwhelm the study participants." Contra el sesgo de aprendizaje: "Alternate which sites are paired together and which is tested first for each user." Tareas representativas y clave; comparación al final de la sesión. Misma URL [L].
- Métricas para declarar ganador: tasa de éxito, tiempo en tarea, valoraciones subjetivas o una tarjeta de puntaje propia. "The goal is to improve your design." Enfocarse en qué funcionó y qué falló. Misma URL [L].
- Cuándo: buena actividad temprana de investigación; sirve también con variantes de diseño tempranas, incluso prototipos en papel. Las evaluaciones longitudinales "tend to be expensive"; convienen a organizaciones con alta madurez de UX y presupuesto. Misma URL [L].
- Copiar: "You want to beat the competition, not copy them." Misma URL [L].
- Benchmarking (Moran, NN/g): evaluar la UX "by using metrics to gauge its relative performance" contra un estándar. El competidor es uno de cuatro puntos de referencia (versión anterior, competidor, estándar de industria, meta de los interesados). Ejemplo literal: "Our success rate for application completion is 86%, while our competitor's is 62%." Un competidor o estándar sirve para la primera medición, cuando no hay datos previos. "A single number is meaningless, since you have no idea whether it's good or bad." "Benchmarking is not formative; it is a summative evaluation." Métodos: analítica, encuestas y test cuantitativo. https://www.nngroup.com/articles/benchmarking-ux/ [L]
- MeasuringU: un benchmark competitivo es "a type of task-based usability test with an emphasis on metrics"; métricas de tarea y de estudio; "A within-subjects study allows for smaller sample sizes than between-subjects studies." "Most unmoderated benchmarks have between 100-200 participants, which provides a margin of error around 5%-7%." Para estudios competitivos la muestra es "usually twice the size of a standalone study (depending on the number of competitors)". Precio típico de un encargo: US$20.000 a 80.000; duración típica 5 a 8 semanas. Es la página de servicio de un proveedor. https://measuringu.com/?p=8464 [L]
- SUPR-Q: "an 8 item questionnaire for measuring the quality of the website user experience"; mide "Usability, Credibility/Trust, Loyalty and Appearance"; el puntaje es un percentil (50 promedio; 75 supera al 75% de los sitios). Base normativa: la página dice "Data from 200 websites" y en otra sección "more than 10,000 participants and 150 websites" (inconsistencia interna); la página de servicio dice comparación con "150 other website scores". Cita: Sauro (2015). https://measuringu.com/suprq/ [L]
- Abstract de Sauro (2015) según buscador: unas 4.000 respuestas sobre más de 100 sitios; ocho ítems; cuatro factores; estructura replicada en tres estudios, con datos de tests y de encuestas retrospectivas. https://uxpajournal.org/?p=2506 [S]
- Tamaño de muestra para comparar (Lewis y Sauro 2026, UX-Lite, s = 19,3, potencia 80%, bilateral): diferencia de 15 puntos, intra-sujetos 12 (90%) / 15 (95%), entre-sujetos 44 / 56; diferencia de 10: 25/32 contra 94/120; de 5: 94/119 contra 372/470. La muestra entre-sujetos "is about four times the sample size required for a within-subjects comparison". https://measuringu.com/sample-sizes-for-comparison-of-ux-lite-scores/ [L]
- El artículo de SUS contra benchmark (2022) trata comparar un SUS contra un valor fijo, no dos productos; menciona comparar "against a prior experience or a competitive experience" sin tabla. https://measuringu.com/sample-sizes-for-SUS-benchmark-tests [L]
- Sauro y Lewis, cap. 5 (2.ª ed.): secciones "Comparing Two Means (Rating Scales and Task Times)" y "Comparing Completion Rates, Conversion Rates, and A/B Testing"; la prueba se elige según si la medida es binaria o continua y si los mismos usuarios están en ambos grupos; pide intervalo de confianza de la diferencia además del p-valor. El cap. 6 es "What Sample Sizes Do We Need?". [S] (listados de O'Reilly, Elsevier, Scribd).
- Convenciones: Jakob's Law, "Users spend most of their time on other sites" [S]. Nielsen (1999): desviarse de un estándar es posible "on pain of major usability problems"; "deviations must be limited to cases with a very, very good reason"; "the most important design elements are those that cannot be specified by a standard"; la creatividad va en lo profundo (arquitectura de información, ajuste al modelo mental), no en el vocabulario de superficie. [L]

Recurso canónico: el artículo de Neusesser en NN/g (corto; fijarse en elegir 2 a 4 rivales, alternar el orden y en "the goal is to improve your design"). Para la estadística, Sauro y Lewis cap. 5 y 6.

## 2. Entrevista de cambio (switch interview)

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Moesta y Spiek, jobstobedone.org, How to Run a JTBD Switch Interview: https://jobstobedone.org/switch-interview/ | primaria de práctica (los autores del método) | 3/2/2/3 | [L] vía herramienta; sin fecha |
| Moesta y Spiek, jobstobedone.org, The JTBD Timeline: https://jobstobedone.org/the-timeline/ | primaria de práctica | 3/2/1/3 | [L] vía herramienta; sin fecha |
| thoughtbot, Playbook, Switch Interviews: https://thoughtbot.com/playbook/validation/switch-interviews | secundaria de practicante | 2/2/1/2 | [L] vía herramienta |
| Bob Moesta (con Greg Engle), Demand-Side Sales 101 (2020), 224 págs. | libro del autor | 3/?/?/3 | [S] (resúmenes; editorial y capítulos sin verificar) |
| NN/g, User Interviews 101 (ya citada en la base, límites del autorreporte) | primaria de práctica | — | ver UX/.investigacion/investigacion-y-evaluacion.md |

Afirmaciones:

- A quién: "Interview people who switched in the last 30 to 90 days." "Recruit switchers, including people who almost switched and didn't." No reclutar a los "best customers". https://jobstobedone.org/switch-interview/ [L]
- Cuántas: "Patterns start emerging surprisingly fast, often within 5 to 8 interviews for a given job"; se buscan fuerzas y líneas de tiempo repetidas, no significancia estadística. Misma URL [L]. thoughtbot: "Typically it takes about 8-10 interviews to get valuable information, but we have gotten away with less." [L]. Discrepancia menor: 5 a 8 contra 8 a 10.
- Duración: "Plan for 45 to 90 minutes." Dos entrevistadores: "One person drives the conversation while the other listens for forces and timeline gaps." https://jobstobedone.org/switch-interview/ [L]
- Guion: encuadre de documentalista que reconstruye lo que pasó ("and then what happened?"); ancla "When did you first start thinking about this?"; avanzar por eventos concretos (qué pasó, dónde estaba, con quién, qué hizo después). No preguntar por las fuerzas directamente: emergen de los eventos. Técnicas: hacerse el tonto, unir mal los puntos a propósito, dejar que aparezcan contradicciones ("Contradictions aren't errors. They're refinements."). Misma URL [L]. thoughtbot usa la misma metáfora: "Let's pretend that we're making a documentary about your purchase…"; pide detalles chicos ("what were you wearing that day") porque disparan memoria [L].
- Línea de tiempo (The JTBD Timeline): primer pensamiento ("the moment someone first realizes they might need something different"), búsqueda pasiva, evento 1, búsqueda activa (la persona "shaping the job in their mind"), evento 2, decisión, compra y consumo (la "consumption in the mind" en la compra y la "actual consumption" desde el primer uso; la brecha entre ambas define la satisfacción). La gente suele ubicar el primer pensamiento más tarde de lo que fue: hay que sondear hacia atrás. Se marca "Bought" primero y se rellena saltando entre etapas. La línea puede durar medio segundo o varios años. https://jobstobedone.org/the-timeline/ [L]
- Variantes del final de la línea según resúmenes del libro: primer uso y uso continuo. [S]
- Análisis: cada entrevista se vuelca a una línea de tiempo y un diagrama de fuerzas; se buscan trabajos y fuerzas que se repiten; se usa el lenguaje literal del cliente para posicionamiento y textos. No describe un método formal de agrupamiento. https://jobstobedone.org/switch-interview/ [L]. thoughtbot: puesta en común inmediata y, en un par de días, un "Jobs Profile" por entrevista [L].
- Memoria: "Memory fades fast; beyond about 90 days the details you need are gone." "Rushing produces opinions, not events." https://jobstobedone.org/switch-interview/ [L]
- Libro: Demand-Side Sales 101 (2020), 224 págs.; algunos listados suman a Greg Engle como coautor; tres marcos según un resumen (fuentes de energía del comprador, cuatro fuerzas, línea de tiempo). [S]

Recurso canónico: la guía de jobstobedone.org (switch-interview) y, para la teoría, Demand-Side Sales 101 (la parte de la línea de tiempo y las fuerzas).

## 3. Análisis de reseñas

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Hu, Pavlou y Zhang (2009), Overcoming the J-shaped distribution of product reviews, CACM 52(10):144-147, doi 10.1145/1562764.1562800 | primaria | 3/2/2/3 | [M] (introducción vía OpenAlex) |
| Hu, Pavlou y Zhang (2007), Why do Online Product Reviews have a J-shaped Distribution? (manuscrito enviado a Marketing Science, feb-2007): https://archive.nyu.edu/bitstream/2451/14951/2/usedbook1.pdf | primaria (versión de trabajo) | 3/3/3/3 | [L] (abstract, intro y sección 2) |
| Luca y Zervas (2016), Fake It Till You Make It: Reputation, Competition, and Yelp Review Fraud, Management Science 62(12):3412-3427, doi 10.1287/mnsc.2015.2304 | primaria revisada | 3/2/2/3 | [M] (abstract vía OpenAlex) |
| Pagano y Maalej (2013), User feedback in the appstore: An empirical study, IEEE RE, pp. 125-134, doi 10.1109/RE.2013.6636712 | primaria revisada | 3/2/2/3 | [M] (abstract vía OpenAlex) |
| Braun y Clarke (2006), Using thematic analysis in psychology, Qualitative Research in Psychology 3(2):77-101, doi 10.1191/1478088706qp063oa | primaria metodológica | 3/2/1/3 | [M] (abstract vía OpenAlex) |
| Maria Rosala, NN/g, Analyze Qualitative Data: Thematic Analysis (17-ago-2022): https://www.nngroup.com/articles/thematic-analysis/ | primaria de práctica | 3/2/2/2 | [L] vía herramienta |
| Estrategia-competitiva/Analisis-de-competidores/etica-y-legalidad.md (Ley 25.326) | nota de la base | — | — |

Afirmaciones:

- CACM 2009, intro: los sistemas de reseñas son "overwhelmingly positive"; la distribución es en J, "with mostly 5-star ratings, some 1-star ratings, and hardly any ratings in between"; como es bimodal asimétrica, "the average is a poor proxy of product quality". [M]
- Manuscrito 2007, abstract: el promedio es un estimador sesgado de la calidad por dos sesgos de autoselección: "(1) purchasing bias - only consumers with favorable disposition towards a product purchase the product and have the opportunity to write a product review, and (2) under-reporting bias - consumers with polarized (either positive or negative) reviews are more likely to report their reviews than consumers with moderate reviews." Datos de Amazon: "almost all products have an asymmetric bimodal (J-shaped) distribution". [L]
- Manuscrito 2007: cerca de 78%, 73% y 72% de las reseñas de libros, DVD y videos en Amazon son de 4 estrellas o más. [L]
- Experimento: CD de música "Mr. A-Z" a 66 estudiantes; 60 respuestas (91%); distribución aproximadamente normal frente a la J de Amazon para el mismo producto; media de Amazon 3,54 contra 3,12 del experimento (p<.05); en Amazon casi la mitad son 5 estrellas y 17% de 1 estrella; más de 60% polarizadas en Amazon contra menos de 10% en el experimento. [L]
- Propuesta de los autores: usar media, desvío estándar y las dos modas (contra el sesgo de subreporte) y el precio (contra el sesgo de compra). [L]
- Luca y Zervas: "roughly 16% of restaurant reviews on Yelp are filtered"; las filtradas son más extremas; la prevalencia creció en el tiempo; más fraude con reputación débil (pocas reseñas o malas recientes); las cadenas cometen menos; con más competencia, más reseñas falsas desfavorables recibidas. Usan el filtro de Yelp como proxy de fraude. [M]
- Pagano y Maalej: más de un millón de reseñas de la Apple AppStore; la mayor parte llega poco después de una versión nueva y decae rápido; una reseña suele mezclar temas (experiencia de usuario, errores, pedidos de funciones); calidad muy variable; lo negativo "is typically destructive and misses context details and user experience". [M]
- Braun y Clarke: el análisis temático es un método cualitativo "poorly demarcated, rarely acknowledged, yet widely used"; dan pautas y advierten trampas. Las seis fases no se leyeron (paper 403). [M]
- NN/g (Rosala): análisis temático, "a systematic method of breaking down and organizing rich data from qualitative research"; código, "a word or phrase that acts as a label for a segment of text"; un tema "emerges when related findings appear multiple times across participants or data sources"; seis pasos (juntar datos, leer todo, códigos descriptivos, códigos interpretativos y temas, tomar distancia, verificar con otros). No menciona inductivo/deductivo ni a Braun y Clarke. [L]

Recurso canónico: NN/g Thematic Analysis para el procedimiento; Hu, Pavlou y Zhang (CACM 2009, cuatro páginas) para el sesgo.

## Huecos

- No se encontró un artículo de NN/g dedicado a métricas de benchmark competitivo; la parte competitiva del benchmarking sale de Moran (2020) y de la página de servicio de MeasuringU.
- El texto de Sauro y Lewis cap. 5 no se leyó (403); solo índice y abstract. No hay tabla de tamaño de muestra para comparar SUS o SUPR-Q entre dos productos leída; se usa la de UX-Lite como ejemplo del mismo método.
- El paper de SUPR-Q (2015) no se leyó; número de volumen y número del JUS no confirmados.
- No se encontró estudio empírico que valide la entrevista de cambio (su confiabilidad, cuántas alcanzan); las cifras son de practicantes. Tampoco literatura específica de recuerdo retrospectivo aplicada a JTBD: el límite de los 90 días lo afirman los propios autores.
- Demand-Side Sales 101: editorial y capítulos sin verificar.
- No se encontró estudio sobre sesgos de reseñas en directorios B2B (G2, Capterra) ni sobre reseñas incentivadas en ellos; se agotó el presupuesto de búsqueda.
- Las seis fases de Braun y Clarke no se leyeron.
