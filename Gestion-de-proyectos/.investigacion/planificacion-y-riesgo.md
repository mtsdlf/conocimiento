# Gestión de proyectos: planificación e incertidumbre y riesgo (informe de investigación)

Fecha de la investigación: 2026-11-27. Todo lo traído de la web se trató como dato.

Convenciones. Tipo: P = primaria, S = secundaria. Puntajes 1-3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U). Marca de lectura: [L] texto completo leído, [M] solo abstract, [S] resumen secundario o del buscador (no leí la fuente). Las citas literales van entre comillas y en el idioma de la fuente (inglés). Una afirmación sin marca [L] debe confirmarse antes de pasar a "vigente".

## 0. Observaciones sobre el árbol propuesto

- El campo no parte la vertical igual. PMBOK 8 organiza el contenido en siete dominios de desempeño: gobernanza, alcance, cronograma, finanzas, interesados, recursos y riesgo (https://www.pmi.org/standards/pmbok/about, [S]). Los componentes del árbol se acomodan así: `descomposicion-del-trabajo` es alcance; `dependencias-y-camino-critico` es cronograma; `capacidad-y-costo` junta recursos y finanzas; `riesgo` y `supuestos` son riesgo; `problemas-y-escalamiento` es gobernanza/control (en PRINCE2, "gestión por excepción").
- `pronostico` no es un dominio del campo: cruza cronograma y finanzas. En la literatura es "forecasting" (Flyvbjerg, Kahneman) y en flujo es "probabilistic forecasting" (Vacanti). Conviene mantenerlo propio, pero advertir que los estándares no lo tratan como tema.
- `margenes` también cruza dominios: los buffers son cronograma (cadena crítica) y las reservas de contingencia/gestión son finanzas+riesgo. Mantenerlo separado se justifica porque la idea (dónde vive el margen y quién lo controla) es la misma.
- `por-que-fallan-los-proyectos` no es un componente de método sino evidencia que sostiene a todos los demás. Funciona mejor como la nota de fundamento a la que enlazan los otros.
- PMBOK 7 abandonó el catálogo de procesos como eje; PMBOK 8 los reintroduce como "focus areas" ([S]). Para lo que no pierde vigencia conviene el vocabulario de ISO 21502 / PRINCE2 y la evidencia, no los nombres de procesos de una edición.

## A1. descomposicion-del-trabajo

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| PMI, Practice Standard for Work Breakdown Structures (2.ª y 3.ª ed.), vía resúmenes: https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063 | P (estándar) | 3/2/1/3 | [S] (no accedí al texto) |
| PMI, Work Breakdown Structures Third Edition: https://www.pmi.org/fr-fr/pmiheadless/home/standards/work-breakdown-structures-third-edition | P | 3/1/1/2 | [S] |
| PMI blog sobre WBS: https://www.pmi.org/blog/work-breakdown-structure | S | 2/1/2/1 | [S] |
| Wikipedia, Work breakdown structure: https://en.wikipedia.org/wiki/Work_breakdown_structure | S | 1/1/1/1 | [S] |

### Afirmaciones

- La regla del 100 %: el EDT captura todo el trabajo del alcance, incluida la gestión del proyecto, y nada fuera de él; se aplica en cada nivel: "the sum of the work at the 'child' level must equal 100% of the work represented by the 'parent'". La 2.ª edición del Practice Standard la trata en su sección 2.4 (https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063, [S]).
- Paquete de trabajo, definición de PMI: "lowest level of the work breakdown structure for which cost and duration are estimated and managed". Tiene identificador único y un solo responsable (https://www.pmi.org/blog/work-breakdown-structure, [S]).
- Los elementos se definen por resultado (entregable), no por acción; demasiadas acciones hacen que un padre exceda el 100 % (mismo resumen, [S]).
- La 3.ª edición aplica el EDT a ciclos predictivos, iterativos, incrementales y ágiles (https://www.pmi.org/fr-fr/pmiheadless/home/standards/work-breakdown-structures-third-edition, [S]).

### Con agentes de IA
Sin fuente verificada para esta vertical. Hipótesis a marcar como tal: un paquete de trabajo ejecutable por un agente necesita criterio de aceptación verificable externamente (ver B1 sobre agentes que "cierran" algo falso). Hueco: ninguna fuente sobre tamaño óptimo de tarea delegable a agentes más allá de METR (ver A3).

### Recurso canónico
PMI, Practice Standard for Work Breakdown Structures, 3.ª ed.: leer la definición de paquete de trabajo y la regla del 100 %. Fijarse en que descomponer por entregable (no por fase ni por actividad) es lo que permite verificar cada pieza.

### Huecos
- No hay estudio con método sobre si descomponer más mejora la predicción o el resultado.
- Texto completo del estándar no leído.

## A2. dependencias-y-camino-critico

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| MacCrimmon y Ryavec 1964, "An Analytical Study of the PERT Assumptions", Operations Research 12(1):16-37: https://pubsonline.informs.org/doi/fpi/10.1287/opre.12.1.16 | P (revista) | 3/2/1/3 | [S] |
| PMI library, "Project network models past, present, and future": https://www.pmi.org/learning/library/project-network-models-past-present-future-5685 | S | 2/2/1/1 | [S] |
| Raz, Barnes y Dvir 2003, "A critical look at critical chain project management", Project Management Journal 34(4):24-32: https://cris.bgu.ac.il/en/publications/a-critical-look-at-critical-chain-project-management-2/ | P (revista PMJ) | 3/2/2/3 | [S] (solo registro) |
| Revisión de CCPM, Mirzaei y Mabin 2018, Int. J. Project Organisation and Management 10(3):242-267: https://ideas.repec.org/a/ids/ijpoma/v10y2018i3p242-267.html | S (revisión) | 2/2/1/2 | [S] |
| Revisión sistemática CCPM multiproyecto, Applied Sciences 2025: https://www.mdpi.com/2076-3417/15/15/8147 | S | 2/1/1/2 | [S] |
| Goldratt, *Critical Chain* (1997), practicante | P (libro) | 2/3/3/3 | no accedido; hueco |

### Afirmaciones

- PERT/CPM calculan duración sobre la ruta de mayor suma de duraciones esperadas. MacCrimmon y Ryavec cuestionan la distribución beta y las hipótesis de PERT; el resumen de PMI dice que produce resultados "overly optimistic" al basar la duración en esa única ruta (https://www.pmi.org/learning/library/project-network-models-past-present-future-5685, [S]). Razón estructural (inferencia estándar, sin cita verificada): cuando varias rutas casi críticas convergen, la duración esperada del proyecto es mayor que la de la ruta más larga.
- Cadena crítica (Goldratt, practicante): extiende la teoría de restricciones al proyecto, saca el margen de cada tarea y lo junta en buffers. Raz et al. 2003 es la crítica en revista con revisión; el registro solo muestra que pide examinar los conceptos de cuello de botella y buffer de material y los costos de adoptarla (https://cris.bgu.ac.il/en/publications/a-critical-look-at-critical-chain-project-management-2/, [S]).
- Evidencia: las revisiones concluyen que CCPM sigue "under investigation" (Grant y Gergely 2012, citado por https://www.mdpi.com/2076-3417/15/15/8147, [S]) y la de 2025 dice que faltan validaciones empíricas en organizaciones reales. Un estudio de 10 casos encontró que el supuesto de una cadena dependiente más larga como restricción vale solo en algunos casos: con equipo dedicado, el recurso más restringido pasa a ser el límite (https://ir.wgtn.ac.nz/handle/123456789/29888, [S], resumen del buscador).
- No traje cifras de mejora atribuidas a Goldratt porque no accedí al libro; no hay metaanálisis ni ensayo verificado que las confirme.

### Con agentes de IA
Sin fuente. Hipótesis a marcar: con agentes el cuello de botella suele ser la revisión humana, no la ejecución (coherente con la lente de restricciones; sin evidencia citable aún).

### Recurso canónico
Para vocabulario: ISO 21502 y PMBOK (cronograma). Para la crítica: Raz, Barnes y Dvir 2003 (PMJ); leer qué supuestos de CCPM se rompen. Fijarse en que el camino crítico es una herramienta de lectura de dependencias, no una garantía de plazo.

### Huecos
- Goldratt 1997 sin acceso; Rand 2000 (IJPM) no hallado; texto completo de MacCrimmon-Ryavec no leído.

## A3. pronostico

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Buehler, Griffin y Ross 1994, JPSP 67(3):366-381: https://bear.warrington.ufl.edu/brenner/mar7588/Papers/buehler-et-al-1994.pdf | P (revista) | 3/3/3/3 | [L] |
| Kahneman y Lovallo 1993, "Timid choices and bold forecasts", Management Science 39(1):17-31: https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.39.1.17 | P (revista) | 3/2/1/3 | [M] |
| Flyvbjerg 2008, "Curbing optimism bias...", European Planning Studies 16(1):3-21: https://ideas.repec.org/a/taf/eurpls/v16y2008i1p3-21.html | P (revista) | 3/2/2/3 | [S] (abstract parcial) |
| Vacanti, *When Will It Be Done?* (2018), practicante: https://leanpub.com/whenwillitbedone | P (libro, practicante) | 2/2/2/3 | [S] (descripción y títulos de capítulos) |
| Notas de practicantes sobre Monte Carlo: https://www.industriallogic.com/blog/reckoning-with-reality-with-probabilistic-forecasting/ y https://resources.scrumalliance.org/Article/achieving-predictable-delivery | S | 1/1/2/1 | [S] |
| Origen de #NoEstimates: https://developers.slashdot.org/story/15/09/24/2211234/the-noestimates-debate-an-unbiased-look-at-origins-arguments-and-leaders | S | 1/1/1/2 | [S] |
| Kwa et al. (METR) 2025: https://arxiv.org/abs/2503.14499 | P (arXiv, sin revisión por pares en la versión consultada) | 2/3/2/3 | [M] |
| Becker et al. (METR) 2025: https://arxiv.org/abs/2507.09089 | P (arXiv, ensayo aleatorizado) | 2/3/3/3 | [M] |

### Afirmaciones

- Falacia de la planificación, estudio 1 (tesis de grado): los estudiantes predijeron en promedio 33,9 días y tardaron 55,5; "Fewer than one third of the respondents (29.7%) finished in the time they reported as their most accurate prediction". Con el escenario pesimista solo 48,7 % terminó a tiempo; con el optimista (21,4 días) solo 10,8 % (https://bear.warrington.ufl.edu/brenner/mar7588/Papers/buehler-et-al-1994.pdf, [L]).
- Mecanismo y remedio, abstract del mismo paper: los sujetos "focused primarily on future scenarios", y en el estudio 4 "the optimistic bias was eliminated for Ss instructed to connect relevant past experiences with their predictions"; los observadores sobrestiman los tiempos de otros (estudio 5) (misma URL, [L]). Los autores citan casos históricos: Ópera de Sídney, estimada en 1957 en US$7 millones y para principios de 1963, inaugurada en 1973 en US$102 millones (misma URL, [L]).
- Visión interna y externa: Kahneman y Lovallo 1993 atribuyen el sesgo optimista a tratar cada decisión como un caso único y desatender las estadísticas del pasado (resumen del abstract, https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.39.1.17, [M/S]). Lovallo dice haber acuñado "inside view" y "outside view" hacia 1993 (https://www.mckinsey.com/business-functions/strategy-and-corporate-finance/our-insights/how-to-take-the-outside-view, [S]).
- Pronóstico por clase de referencia: basa la proyección en el desempeño real de un conjunto de acciones comparables; Flyvbjerg 2008 reporta la primera aplicación práctica a costos de transporte del Reino Unido (Edinburgh Tram, Crossrail de £15.000 millones) (https://ideas.repec.org/a/taf/eurpls/v16y2008i1p3-21.html, [S]). Flyvbjerg 2014 lo menciona como remedio institucional (https://arxiv.org/pdf/1409.0003, [L]).
- Evidencia de que reduce el error: lo verificado es la propuesta y su aplicación, no una evaluación comparativa con grupo de control. Hueco.
- Monte Carlo sobre datos de rendimiento (Vacanti, practicante): usa solo rendimiento histórico (ítems terminados por período); los títulos de capítulo "Never Communicate a Forecast in Terms of an Average" y "Percentiles Are Forecasts!" resumen la postura (https://leanpub.com/whenwillitbedone, [S]). Una guía de practicantes dice que bastan 10 a 20 mediciones para empezar (https://resources.scrumalliance.org/Article/achieving-predictable-delivery, [S]) y otra advierte que la simulación se degrada si el rendimiento es casi siempre cero (https://medium.com/nationwide-technology/story-pointless-part-2-of-3-57db27a48a58, [S]). Ningún estudio con revisión por pares verificado valida el método frente a alternativas. Marcar como postura de practicantes.
- #NoEstimates: el primer tuit registrado con la etiqueta es de Woody Zuill, 10 de diciembre de 2012; Zuill, Vasco Duarte y Neil Killick son los iniciadores; Zuill propone dejar de estimar del todo, Duarte y Killick una versión gradual (https://developers.slashdot.org/story/15/09/24/2211234/the-noestimates-debate-an-unbiased-look-at-origins-arguments-and-leaders, [S]). Postura de practicantes sin evidencia controlada.

### Con agentes de IA
- Sin horas-persona no hay base humana para estimar. Lo más cercano verificado: METR mide el "50%-task-completion time horizon", el tiempo humano de las tareas que un modelo completa con 50 % de éxito; para Claude 3.7 Sonnet, "around 50 minutes", con duplicación "approximately every seven months since 2019" (https://arxiv.org/abs/2503.14499, [M]; v1 del 18 de marzo de 2025, v4 revisada el 10 de julio de 2026). Medida sobre tareas de software, con validez externa limitada según los propios autores.
- La intuición sobre agentes también sufre sesgo: en un ensayo aleatorizado con 16 desarrolladores y 246 tareas, permitir IA "increased task completion time by 19%", mientras los desarrolladores esperaban una reducción de 24 % antes y estimaron 20 % después; economistas predijeron 39 % y expertos en ML 38 % (https://arxiv.org/abs/2507.09089, [M]; julio de 2025, herramientas de principios de 2025, muestra chica). Es dato fuerte sobre pronóstico propio, no sobre el costo de una fábrica de agentes.
- Consecuencia práctica (inferencia, marcar como tal): pronosticar con datos del propio sistema (rendimiento histórico, tasa de retrabajo) y no con intuición.

### Recurso canónico
Buehler, Griffin y Ross 1994: leer el estudio 1 (tabla 1) y el estudio 4. Fijarse en que la mejora viene de forzar la conexión con experiencias pasadas, es decir, de la visión externa. Para el método de flujo, Vacanti (practicante), capítulos sobre percentiles y Monte Carlo.

### Huecos
- Sin evaluación empírica de la clase de referencia frente a controles.
- Sin validación revisada por pares de Monte Carlo sobre rendimiento.
- Kahneman y Lovallo solo [M].
- Sin evidencia sobre #NoEstimates más allá de relatos.

## A4. capacidad-y-costo

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Kapoor et al. 2024, "AI Agents That Matter": https://arxiv.org/abs/2407.01502 | P (arXiv sin revisión) | 2/2/2/3 | [M] |
| PMBOK 8, dominios finanzas y recursos: https://www.pmi.org/standards/pmbok/about | P (estándar) | 3/1/1/2 | [S] |
| Reinertsen, *Principles of Product Development Flow* (2009), practicante; resúmenes: https://www.informit.com/articles/article.aspx?p=2928185&seqNum=6 | S del libro | 2/2/2/2 | [S] |

### Afirmaciones

- Kapoor et al. (1 de julio de 2024) proponen medir costo además de exactitud en la evaluación de agentes: "Our focus on cost in addition to accuracy motivates the new goal of jointly optimizing the two metrics" (https://arxiv.org/abs/2407.01502, [M]). Implica que el costo por tarea de un agente es una variable y no una constante, y que la exactitud sola engaña.
- Reinertsen (practicante): según resúmenes, el costo de las colas (trabajo esperando) supera al de recursos ociosos, operar cerca del 100 % de utilización es mala economía y conviene limitar el trabajo en curso (https://www.informit.com/articles/article.aspx?p=2928185&seqNum=6, [S]). Es la base de la lente de flujo para capacidad.
- Precios por token: no traje fuente verificada. Cambian y no pasan el criterio "no pierde vigencia"; lo duradero es la estructura (costo variable por token y por reintento, topes por tarea y por período). Hueco.
- Topes de gasto como práctica: sin fuente verificada. Hueco.

### Con agentes de IA
Diferencia estructural (inferencia, sin fuente específica): el costo de una persona es capacidad fija por período, el de un agente es variable con el uso y los reintentos; la capacidad se acota por presupuesto y por supervisión humana. Hipótesis hasta hallar fuente.

### Recurso canónico
Kapoor et al. 2024 para evaluar costo junto con exactitud; Reinertsen para la economía de colas. Fijarse en que una tarea "barata" que necesita varias rondas de revisión humana puede costar más que hacerla a mano.

### Huecos
- Sin lectura directa de los estándares sobre presupuesto y reservas.
- Sin estudio revisado por pares sobre costo de agentes frente a horas-persona.
- Sin fuente de topes de gasto.

## B1. riesgo

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| ISO 31000:2018: https://www.iso.org/news/ref2263.html (la página del estándar https://www.iso.org/standard/65694.html dio 403) | P (estándar) | 3/2/1/3 | [S] |
| Cox 2008, "What's wrong with risk matrices?", Risk Analysis 28(2):497-512: https://econpapers.repec.org/RePEc:wly:riskan:v:28:y:2008:i:2:p:497-512 | P (revista) | 3/3/2/3 | [M] (abstract, parafraseado por la herramienta) |
| Bakker, Boonstra y Wortmann 2010, "Does risk management contribute to IT project success? A meta-analysis of empirical evidence", IJPM 28(5):493-503, DOI 10.1016/j.ijproman.2009.07.002: https://www.pmi.org/learning/library/risk-management-contribute-project-success-6856 | P (metaanálisis, revista) | 3/3/2/3 | no leído |
| Flyvbjerg y Budzier 2011, HBR 89(9): https://papers.ssrn.com/abstract=2229735 | P | 2/1/2/2 | [S] |
| Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (MAST): https://arxiv.org/abs/2503.13657 | P (arXiv; póster NeurIPS 2025 según el buscador) | 2/2/2/3 | [S] |

### Afirmaciones

- ISO 31000:2018 (2.ª edición, febrero de 2018) da principios, marco y proceso; es guía, no requisitos, y no es certificable; esta revisión pone más foco en crear y proteger valor y en la naturaleza iterativa (https://www.iso.org/news/ref2263.html, [S]). Según el buscador, ISO la confirmó en 2023. El proceso: identificar, analizar, evaluar, tratar, monitorear y comunicar (resumen del buscador, [S]).
- Crítica de matrices (Cox 2008), del abstract: las matrices se usan en terrorismo, construcción y riesgo empresarial; hay poca investigación que muestre que mejoran las decisiones; cuatro límites: resolución pobre (comparan de forma fiable una fracción pequeña de pares de riesgos), errores (pueden dar mayor calificación cualitativa a riesgos cuantitativamente menores y, con frecuencia y severidad negativamente correlacionadas, decidir peor que al azar), asignación subóptima de recursos y entradas y salidas ambiguas. Concluye que deben usarse con cuidado y explicando los juicios que contienen (https://econpapers.repec.org/RePEc:wly:riskan:v:28:y:2008:i:2:p:497-512, [M]).
- Evidencia de que la gestión de riesgos mejora resultados: existe un metaanálisis en IJPM (Bakker et al. 2010) cuyo abstract califica las conclusiones de "remarkable" según el buscador, pero no pude leer qué concluye. Un estudio posterior en *Journal of Project Management* (2024, sector TI) informa que algunos componentes se asocian con éxito pero que la gestión de riesgos no influye en el éxito del proyecto (resumen del buscador, https://doaj.org/article/31ecb8864b4a49bfb3de03aca3648687, [S]). Dirección del efecto sin verificar: no afirmar en la nota que mejora resultados hasta leer el metaanálisis.
- Cifras de HBR 2011 ("uno de cada seis", 200 % de costo, 70 % de plazo): no verificadas. Un resumen de InfoQ da otra (400 % más de gasto y 25 % de beneficios) (https://www.infoq.com/news/2011/10/risky-it-projects, [S]). Dos fuentes discrepan y ninguna leída: no usar.

### Con agentes de IA
Riesgo nuevo: el agente que cierra una tarea con un falso éxito. MAST taxonomiza 14 modos de falla de sistemas multiagente en 3 categorías (diseño del sistema, desalineación entre agentes y verificación de tareas); en ésta figuran "Premature Termination", "No or Incomplete Verification" e "Incorrect Verification"; acuerdo entre anotadores kappa = 0,88 (https://arxiv.org/abs/2503.13657, [S]). No obtuve porcentajes por modo ni evidencia de falso éxito en el sentido de afirmar haber hecho lo que no se hizo. Gestión sugerida (inferencia): verificación independiente del entregable y criterio de aceptación escrito antes.

### Recurso canónico
ISO 31000:2018 para el proceso (vocabulario); Cox 2008 para saber qué no hacer con las matrices. Fijarse en que la crítica ataca las escalas ordinales, no la idea de gestionar riesgos.

### Huecos
- Resultado del metaanálisis de Bakker et al. sin leer (PMI y otros sitios bloquearon el acceso). Es la afirmación de más peso para este componente.
- ISO 31000 sin texto.
- Sin fuente sobre matrices frente a alternativas cuantitativas más allá de Cox.

## B2. supuestos

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Klein 2007, "Performing a Project Premortem", HBR 85(9):18-19: https://comprobo24.github.io/assignments/performing_a_project_premortem.pdf | P (HBR, investigador-practicante) | 2/2/2/3 | [L] |
| Mitchell, Russo y Pennington 1989, J. Behavioral Decision Making 2(1):25-38, DOI 10.1002/bdm.3960020103: https://colab.ws/articles/10.1002%2Fbdm.3960020103 | P (revista) | 3/2/1/3 | [M] (resumen del abstract) |
| Veinott, Klein y Wiggins 2010, vía Psychology Today: https://www.psychologytoday.com/ie/blog/seeing-what-others-dont/202101/the-pre-mortem-method | S | 1/1/1/1 | [S] |

### Afirmaciones

- Qué es: el equipo imagina que el proyecto fracasó y escribe por qué; el líder pide a cada miembro, empezando por el director del proyecto, que lea una razón de su lista hasta agotarlas (https://comprobo24.github.io/assignments/performing_a_project_premortem.pdf, [L]).
- Evidencia citada por Klein: "Research conducted in 1989 by Deborah J. Mitchell, of the Wharton School; Jay Russo, of Cornell; and Nancy Pennington, of the University of Colorado, found that prospective hindsight—imagining that an event has already occurred—increases the ability to correctly identify reasons for future outcomes by 30%" (misma URL, [L]).
- Discrepancia: el resumen del abstract original (https://colab.ws/articles/10.1002%2Fbdm.3960020103, [M]) dice que en el experimento 1 el marco temporal (futuro o pasado) tuvo poco efecto y que lo que más pesó fue la certeza del resultado. No encontré el 30 % en ese abstract. Tratar el 30 % como cifra atribuida por Klein, no verificada en el original.
- Veinott et al. 2010: imaginar que el plan ya falló redujo la confianza en él más que los métodos de pros y contras; solo resumen secundario (https://www.psychologytoday.com/ie/blog/seeing-what-others-dont/202101/the-pre-mortem-method, [S]).
- Registro de supuestos y probar supuestos temprano: sin fuente verificada con método. Hueco.

### Con agentes de IA
Sin fuente. Hipótesis: los supuestos implícitos del encargo son lo primero que un agente rellena en silencio; conviene pedirle que liste los que usó (inferencia).

### Recurso canónico
Klein 2007 (dos páginas): los pasos del ejercicio. Fijarse en que la cifra de 30 % no se pudo verificar en el original.

### Huecos
- Sin estudio con método que mida el premortem sobre resultados de proyecto.
- Registro de supuestos sin fuente.

## B3. margenes

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Gutierrez y Kouvelis 1991, "Parkinson's law and its implications for project management", Management Science 37(8):990-1001: https://econpapers.repec.org/RePEc:inm:ormnsc:v:37:y:1991:i:8:p:990-1001 | P (revista, modelo) | 3/2/1/3 | [S] |
| Brannon, Hershberger y Brock 1999, Psychonomic Bulletin & Review: https://link.springer.com/article/10.3758/BF03210823 | P (revista) | 3/2/1/3 | [S] |
| Simulación del "student syndrome": https://dlib.si/stream/URN:NBN:SI:DOC-28JY2A81/d0c0e633-e141-448f-aa1b-db656cc989df/PDF | P (simulación) | 1/1/1/2 | [S] |
| Raz et al. 2003 (ver A2) | P | 3/2/2/3 | [S] |

### Afirmaciones

- Gutierrez y Kouvelis modelan la ley de Parkinson: PERT/CPM no incorporan los efectos de comportamiento de la fuerza de trabajo sobre la duración esperada. Es modelo teórico, no experimento (https://econpapers.repec.org/RePEc:inm:ormnsc:v:37:y:1991:i:8:p:990-1001, [S]).
- Brannon et al. 1999 afirman, según el buscador, que la ley "has survived without an artifact-free demonstration at the individual level" (https://link.springer.com/article/10.3758/BF03210823, [S]; no confirmé el hallazgo). Es decir, evidencia experimental débil o discutida sobre Parkinson.
- Síndrome del estudiante: solo simulación; reporta que eliminarlo acorta el proyecto hasta 35 % frente a cuando ocurre (https://dlib.si/stream/URN:NBN:SI:DOC-28JY2A81/d0c0e633-e141-448f-aa1b-db656cc989df/PDF, [S]). No es dato de campo.
- Buffers de cadena crítica: mismo estado de evidencia que en A2 (propuesta de practicante, evidencia empírica escasa según las revisiones).
- Reservas de contingencia y de gestión: sin fuente verificada. Hueco.

### Con agentes de IA
Sin fuente. Inferencia a marcar: los agentes no tienen síndrome del estudiante, pero el margen que importa es el de verificación y retrabajo humano.

### Recurso canónico
Ninguno suficientemente verificado. Candidato: Raz et al. 2003 (PMJ) para el balance crítico de buffers; completar con Goldratt como fuente de practicante.

### Huecos
- Sin evidencia de campo ni experimental firme de Parkinson y síndrome del estudiante.
- Sin fuente de reservas de contingencia y de gestión.

## B4. problemas-y-escalamiento

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| PRINCE2 7 (AXELOS/PeopleCert), manual oficial | P (estándar) | 3/-/-/3 | no accedido (la página de AXELOS no dio contenido útil) |
| Manage by exception: https://prince2.wiki/Manage_by_exception | S | 1/1/1/1 | [S] |
| Exception management: https://knowledgetrain.co.uk/project-management/exception-management | S | 1/1/1/1 | [S] |
| Guía de estudio: https://open-exam-prep.com/study-guides/prince2-7-foundation/prince2-7-principles/manage-by-exception | S | 1/1/1/1 | [S] |

Las tres secundarias resumen un mismo estándar: cuentan como una sola fuente.

### Afirmaciones

- Definición, según resúmenes: "A PRINCE2 project has defined tolerances for each project objective to establish limits of delegated authority" (https://prince2.wiki/Manage_by_exception, [S]).
- Tolerancias: tiempo, costo, calidad, alcance, riesgo y beneficio; PRINCE2 7 añade sostenibilidad según una guía de estudio (https://open-exam-prep.com/study-guides/prince2-7-foundation/prince2-7-principles/manage-by-exception, [S]). Discrepancia entre fuentes secundarias (seis o siete): verificar en el manual oficial.
- Cuándo sube: no hay escalamiento mientras los pronósticos estén dentro de tolerancia; se levanta una excepción cuando se pronostica una violación, no cuando ya ocurrió. Hay tolerancias de proyecto (las fija el nivel superior) y de etapa (las fija el comité del proyecto) (https://knowledgetrain.co.uk/project-management/exception-management, [S]).
- Informe de excepción: pronóstico, causa, impacto en cada objetivo y al menos dos opciones con recomendación; el comité puede aceptar mayor tolerancia, reducir alcance o pedir un plan de excepción que rebase la etapa (misma fuente, [S]).

### Con agentes de IA
Sin fuente. Aplicación directa (inferencia): las tolerancias definen el margen de autonomía del agente, y la excepción sube a una persona cuando el pronóstico (gasto, plazo, confianza en la verificación) sale del margen.

### Recurso canónico
PRINCE2 7, principio de gestión por excepción y tema de progreso (manual oficial, no accedido). Fijarse en que se escala por pronóstico de violación, no por violación ocurrida.

### Huecos
- Manual oficial sin acceso; todo es [S].
- Sin estudio con método sobre si la gestión por excepción mejora resultados.

## B5. por-que-fallan-los-proyectos

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Flyvbjerg 2014, "What You Should Know About Megaprojects and Why: An Overview", PMJ 45(2):6-19, DOI 10.1002/pmj.21409; preprint "Draft 9.2": https://arxiv.org/pdf/1409.0003 | P (revista; leí el borrador) | 3/3/3/3 | [L] |
| Flyvbjerg, Budzier, Lee, Keil, Lunn y Bester 2022, "The Empirical Reality of IT Project Cost Overruns: Discovering A Power-Law Distribution", J. Management Information Systems 39(3):607-639; arXiv 2210.01573 (30 de septiembre de 2022): https://arxiv.org/abs/2210.01573 | P (revista; leí el PDF de la versión publicada que sirve arXiv) | 3/3/3/3 | [L] |
| Flyvbjerg y Gardner 2023, *How Big Things Get Done*; cifras vía entrevista a Gardner: https://www.mindtools.com/an0e922/how-big-things-get-done | S (entrevista; libro de divulgación) | 2/1/2/2 | [S] |
| Reseña del libro: https://www.independent.org/tir/2023-fall/how-big-things-get-done/ | S | 1/1/1/1 | [S] |

### Afirmaciones

- Ley de hierro, literal: "Nine out of ten such projects have cost overruns. Overruns of up to 50 percent in real terms are common, over 50 percent not uncommon." Sobrecostos reales: túnel del Canal 80 %, aeropuerto de Denver 200 %, Big Dig de Boston 220 %, sistema informático del NHS 400-700 %, Ópera de Sídney 1.400 %. Los sobrecostos "have stayed high and constant for the 70-year period for which comparable data exist" y todos los países con datos los sufren. Faltantes de beneficios "of up to 50 percent are also common, and above 50 percent not uncommon" (https://arxiv.org/pdf/1409.0003, [L]).
- Éxito: "approximately one out of ten megaprojects is on budget, one out of ten is on schedule, and one out of ten is on benefits, then approximately one in a thousand projects is a success"; si los números fallaran por un factor dos, serían ocho de mil. La frase de la ley: "Over budget, over time, over and over again" (misma URL, [L]). El "uno en mil" multiplica tres décimas, es decir, supone independencia; Flyvbjerg lo presenta como ilustración, no como medición.
- Gasto global de megaproyectos: USD 6-9 billones por año, 8 % del PIB mundial (abstract, misma URL, [L]).
- Colas gruesas en TI: muestra de "5,392 IT projects" completados entre 2002 y 2014, 4.677 con costo estimado y real; los sobrecostos siguen una ley de potencia, con "a large number of projects with relatively small overruns and a fat tail"; α = 2,3 (sd 0,058) para x0 = 2,0, con 26,5 % de las observaciones en la cola (495); con 2 < α < 3 la media es finita y la varianza indefinida; bootstrap: α medio 2,35 (sd 0,20). Si se supone normalidad, los sobrecostos extremos "will be grossly underestimated" (https://arxiv.org/abs/2210.01573 y PDF, [L]). La x del ajuste es razón costo real / estimado, no porcentaje: x0 = 2,0 es costo doble del estimado.
- Mecanismo propuesto, por simulación: la interdependencia entre componentes tecnológicos produce reacciones en cadena (mismo paper, [L]). Hipótesis simulada, no demostrada.
- Cifras del libro de 2023 (base de más de 16.000 proyectos): "a little under half" dentro del presupuesto; 8,5 % cumple presupuesto y plazo; 0,5 % cumple presupuesto, plazo y beneficios, "basically a rounding error" (https://www.mindtools.com/an0e922/how-big-things-get-done, [S]: la herramienta de lectura confirmó "más de 16.000", "poco menos de la mitad" y 0,5 % en la entrevista; el 8,5 % viene de reseñas del buscador).
- Discrepancia a presentar: el paper de 2014 dice que cerca de uno de cada diez megaproyectos cumple presupuesto (nueve de diez con sobrecosto); la entrevista del libro dice que "a little under half" de los proyectos de la base cumplen presupuesto. No es la misma población (megaproyectos frente a la base completa de más de 16.000 proyectos de tamaños mixtos). Citar cada una con su población. No pude verificar en el libro las cifras 8,5 % y 0,5 %.

### Con agentes de IA
No hay estudio de por qué fallan proyectos con agentes. Lo más cercano: MAST (B1) ubica una de tres categorías de falla en la verificación de tareas (https://arxiv.org/abs/2503.13657, [S]).

### Recurso canónico
Flyvbjerg 2014 (sección "The Iron Law of Megaprojects") y Flyvbjerg et al. 2022 (ajuste de la cola y mecanismo). Fijarse en: qué población, cómo se mide el sobrecosto (real frente a nominal, razón frente a porcentaje) y que el argumento es sobre colas, no promedios.

### Huecos
- Libro de 2023 sin leer; cifras de segunda mano.
- Flyvbjerg es la fuente central de este apartado y de A3; su evidencia es de megaproyectos y TI, no de proyectos pequeños ni de otros dominios. Falta un contrapeso de otro grupo (no buscado).
- HBR 2011 sin verificar.

## Resumen de recursos canónicos por componente

| Componente | Recurso | Dónde fijarse |
|---|---|---|
| descomposicion-del-trabajo | PMI, Practice Standard for WBS, 3.ª ed. | regla del 100 %, definición de paquete de trabajo |
| dependencias-y-camino-critico | Raz, Barnes y Dvir 2003 (PMJ) y vocabulario de ISO 21502 | supuestos de CCPM que se rompen |
| pronostico | Buehler, Griffin y Ross 1994 (JPSP) | estudio 1 (tabla 1) y estudio 4 |
| capacidad-y-costo | Kapoor et al. 2024 (arXiv) y Reinertsen | costo junto con exactitud; colas |
| riesgo | ISO 31000:2018 y Cox 2008 | proceso; límites de las matrices |
| supuestos | Klein 2007 (HBR) | pasos del premortem; el 30 % sin verificar |
| margenes | sin canónico verificado | hueco |
| problemas-y-escalamiento | PRINCE2 7 (manual oficial) | escalamiento por pronóstico de violación |
| por-que-fallan-los-proyectos | Flyvbjerg 2014 y Flyvbjerg et al. 2022 | población, medida, colas |

## Huecos consolidados

1. Resultado del metaanálisis Bakker et al. 2010 (¿mejora la gestión de riesgos los resultados?): no leído; es la afirmación de más peso para `riesgo`.
2. Goldratt (*Critical Chain*, 1997) y Rand 2000: sin acceso; sin cifras de mejora del método.
3. Evaluación empírica del pronóstico por clase de referencia y de Monte Carlo sobre rendimiento: solo propuesta y práctica.
4. Reservas de contingencia y de gestión, registro de supuestos y topes de gasto: sin fuente.
5. Costo de agentes frente a horas-persona: sin estudio; solo Kapoor et al. (principio) y METR (horizonte y sesgo de pronóstico). Precios por token excluidos por volátiles.
6. ISO 31000, ISO 21502, PRINCE2 7, PMBOK 7/8 y PMI WBS: solo resúmenes. Leer el texto antes de pasar a "vigente".
7. Las cifras del libro de 2023 (8,5 %, 0,5 %, "poco menos de la mitad") vienen de entrevista y reseñas; verificar en el libro.
8. Sin fuentes sobre proyectos fuera de software, infraestructura y megaproyectos, aunque el usuario trabaja en cualquier dominio.
9. Dieron 403 o bloqueo anti-bot: pmi.org/learning/library (cadena crítica, metaanálisis), iso.org/standard, axelos.com, mediatum.ub.tum.de, econbiz.de.
10. Todos los efectos de los agentes sobre cada componente son inferencias, salvo METR, Kapoor y MAST, que son arXiv sin revisión por pares verificada.
11. Mitchell, Russo y Pennington: el 30 % de prospective hindsight no está verificado en el original (ver B2).
