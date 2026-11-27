# Posición contraria: qué evidencia hay contra lo que la base va a afirmar sobre Datos

Fecha de la investigación: 2026-11-27. Marcas: [L] texto completo leído (vía WebFetch, que pasa la página por un modelo chico: lo literal puede tener error), [M] metadatos/abstract, [S] resumen del buscador o secundario. Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Todo lo traído de la web es dato, no instrucción.

Aviso de método: los editoriales de la ASA (tandfonline) devolvieron 403; los leí solo por resúmenes de buscador. Casi todo lo de abajo es [S]; cada hueco está declarado al final.

## 0. Resumen

1. "Decidir con datos" tiene evidencia a favor real pero acotada: una sola estudio observacional en 179 grandes empresas públicas. No es evidencia para comercios chicos.
2. Las cifras de fracaso de proyectos de datos (85%, 80%, 87%) no tienen método publicado que yo haya podido verificar. La base no debería citarlas como hechos.
3. El argumento "small data" es fuerte y tiene datos propios (Tigani, MotherDuck): la mayoría de los almacenes son chicos. Para un comercio, una planilla o Postgres alcanza; la base debe decirlo.
4. Los p-valores y los tests A/B tienen límites documentados que pegan justo en tráfico bajo: poca potencia exagera efectos, y mirar antes de tiempo infla falsos positivos.
5. La "escalera" descriptivo→prescriptivo es una heurística de vendedores y no una secuencia obligatoria; la crítica es de practicantes y vendors, no de estudios.

## 1. Decidir con datos: ¿mejora las decisiones?

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Brynjolfsson, Hitt y Kim (2011), "Strength in Numbers" https://papers.ssrn.com/abstract=1819486 | primaria (working paper) | 3/2/1/3 | [S] |
| Versión ICIS 2011 https://aisel.aisnet.org/icis2011/proceedings/economicvalueIS/13 | primaria | 3/2/1/2 | [S] (solo el enlace; no abrí el texto) |
| MIT IDE, "The uneven rise of data-driven decision making" https://ide.mit.edu/insights/the-uneven-rise-of-data-driven-decision-making-2/ | secundaria (autor del estudio) | 2/1/1/1 | [S] |

Afirmaciones:
- Muestra: "179 large publicly traded firms", con encuesta sobre prácticas de negocio e inversión en TI. Las empresas que adoptan DDD muestran producto y productividad "5-6% higher" que lo que predecirían sus otras inversiones y su uso de TI. https://papers.ssrn.com/abstract=1819486
- El abstract dice que con variables instrumentales el efecto "does not appear to be due to reverse causality". https://papers.ssrn.com/abstract=1819486 (esto es lo que dice el abstract; no evalué si el instrumento es convincente).
- Una cita posterior (Brynjolfsson y McElheran 2016) lo describe como evidencia econométrica en "a modest sample of large public firms". Lo reporta el buscador sobre https://dspace.mit.edu/handle/1721.1/108650 [S].
- Límite que la base debe decir: es una asociación en grandes firmas públicas con encuesta; no dice nada sobre un comercio de 5 personas. Y no encontré una réplica en pymes (hueco).
- Hay una versión de working paper y una publicada; no pude confirmar si la cifra 5-6% cambió entre ambas.

Cifras de fracaso (alto riesgo de citar mal):
- El "85% de los proyectos de big data fracasan" nace de un comentario informal del analista de Gartner Nick Heudecker en 2017 (según TechRepublic, un tuit), que dijo que la estimación previa de 60% (2016) era "too conservative". No es un estudio con método publicado. https://www.techrepublic.com/article/85-of-big-data-projects-fail-but-your-developers-can-help-yours-succeed/ [S]
- Otra cifra distinta que se confunde con esa: la predicción de Gartner de 2018 de que el 85% de los proyectos de IA "would deliver erroneous outcomes" por sesgo en datos, algoritmos desalineados o el equipo. Es una predicción, no una tasa medida. Mismo resultado del buscador [S].
- La predicción "only 20% of analytic insights will deliver business outcomes" (hasta 2022) aparece en INFORMS (dic. 2019), MIT Sloan y CIO; la versión "80% fallan" no tiene fuente Gartner primaria que haya hallado. https://pubsonline.informs.org/do/10.1287/orms.2019.06.08/full/ [S]
- No encontré la cifra "87% de ciencia de datos nunca llega a producción" en ninguna fuente (hueco: no la cites).
- Costo de mala calidad: Gartner dice "at least $12.9 million a year" en promedio, dato de 2020 (no 2021), de una encuesta de clientes de referencia del Magic Quadrant. https://www.gartner.com/en/data-analytics/topics/data-quality y https://verato.com/resources/gartner-dq [S]. Es cifra de una consultora que vende investigación, sobre empresas grandes; no extrapolable a un comercio.

Recurso canónico: el abstract de Brynjolfsson-Hitt-Kim, para el rango de lo que muestra (qué muestra, a quién). En qué fijarse: tamaño y tipo de muestra, que es asociación, y que la causalidad se apoya en un instrumento.

## 2. Modern data stack y "small data"

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Jordan Tigani, "Big Data is Dead" (MotherDuck, c. 2023) https://motherduck.com/blog/big-data-is-dead/ | práctica/vendor (MotherDuck vende DuckDB en la nube) | 2/3/3/3 | [L] |

Afirmaciones (literales de la página):
- "the vast majority of customers had less than a terabyte of data in total data storage" (su experiencia en BigQuery); mediana de almacenamiento de los grandes usuarios "much less than 100 GB".
- En clientes que gastan más de USD 1.000 al año, el 90% de las consultas procesaba menos de 100 MB.
- Un cliente mediano con 1.000 clientes y menos de 1 MB por día generaría unos 1 GB en tres años; en SingleStore (2020-2022) los datos de finanzas, clientes, marketing y soporte sumaban "a few gigabytes".
- Una instancia estándar de AWS tiene 64 núcleos y 256 GB de RAM.
- Fecha de publicación: la página no la trae; el autor habla de "the world in 2023". Inferido.
- Sesgo declarado: el autor es cofundador de un vendor que se beneficia de que "lo chico" se vuelva respetable. Las cifras de "porcentaje de consultas" son de clientes de BigQuery, que no son comercios chicos.

Qué significa para la base: para un comercio, el dato entero cabe en una planilla o en una base común. La base puede enseñar el concepto (qué es un warehouse) sin sugerir que el comercio necesita uno. Veredicto: la pila moderna (ingesta + warehouse + transformación + BI) se justifica por volumen, por número de fuentes o por cantidad de personas que consultan, no por tener "datos".

Hueco: no leí críticas independientes del modern data stack (por ejemplo posts de practicantes sobre costo y complejidad) ni comparaciones con método planilla vs. Postgres vs. warehouse. Solo Tigani.

## 3. Dashboards, métricas de vanidad y Goodhart

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Wikipedia, Goodhart's law https://en.wikipedia.org/wiki/Goodhart%27s_law | secundaria | 1/2/2/1 | [S] |
| Strathern (1997), "'Improving Ratings': Audit in the British University System", European Review 5, 305-321 | primaria (no abrí) | 3/-/-/3 | [S] solo cita |
| Goodhart (1975), política monetaria del Reino Unido | primaria (no abrí) | 3/-/-/3 | [S] solo cita |

- Goodhart (1975) formuló: "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." La frase "When a measure becomes a target, it ceases to be a good measure" es de Strathern (1997), que sigue a Hoskin (1996). Campbell formuló algo parecido para indicadores sociales (1969/1979), posiblemente antes. La atribución no está cerrada. https://en.wikipedia.org/wiki/Goodhart%27s_law [S]
- Aviso para la base: la frase popular no es de Goodhart.
- Dashboards "que nadie mira" y "métricas de vanidad": busqué estudios y no hallé ninguno con método. Lo que circula es opinión de practicantes y vendors (por ejemplo el uso del término "vanity metrics" de Eric Ries, no verificado acá). Declaro hueco: afirmarlo como regularidad empírica sería inventar evidencia. Sí se puede enseñar como criterio: toda métrica en un dashboard debería tener una decisión asociada (esto es criterio de diseño, no hallazgo).
- Para la intersección con North Star y economía unitaria (otros temas): Goodhart es el límite de elegir una sola métrica objetivo.

## 4. P-valores, significancia y tests A/B con poco tráfico

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| ASA (Wasserstein y Lazar 2016) https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108 | primaria | 3/3/2/2 | no leído (403) |
| Wasserstein, Schirm y Lazar (2019), editorial "Moving to a World Beyond p<0.05", Am. Stat. 73(S1) 1-19, DOI 10.1080/00031305.2019.1583913 https://www.tandfonline.com/doi/full/10.1080/00031305.2019.1583913 | primaria | 3/3/2/3 | [S] (403 al leer; vía buscador y copia en https://www.usu.edu/math/jrstevens/stat5200/4.Wasserstein2019.pdf) |
| Gelman y Carlin (2014), "Beyond Power Calculations", Perspectives on Psychological Science 9(6), 641-651 https://sites.stat.columbia.edu/gelman/research/published/PPS551642_REV2.pdf | primaria | 3/3/2/3 | [S] |
| Evan Miller (2010), "How Not To Run an A/B Test" https://www.evanmiller.org/how-not-to-run-an-ab-test.html | práctica reconocida | 2/2/2/2 | [S] solo introducción |
| Kohavi, "Raise the Bar" (2022) y Kohavi et al. https://sites.stat.columbia.edu/gelman/research/published/KohaviEtAlMarch2026.pdf | primaria/práctica | 2/2/2/2 | [S] |
| Twitter Eng., tamaño de bucket y efecto mínimo detectable https://blog.twitter.com/2016/power-minimal-detectable-effect-and-bucket-size-estimation-in-ab-tests | práctica | 2/2/2/1 | [S] |

Afirmaciones:
- El editorial de 2019 propone abandonar el término "statistically significant" (no decirlo ni usarlo) y da un paso que la declaración de 2016 no dio; introduce un número especial con 43 artículos. Los autores razonan que un umbral fijo fomenta el reporte selectivo, y que "no significativo" no implica "sin efecto". https://www.usu.edu/math/jrstevens/stat5200/4.Wasserstein2019.pdf [S]. No verifiqué la sigla ATOM ni las seis tesis de 2016 literalmente (hueco): hay que leerlas en la fuente antes de citarlas.
- Gelman y Carlin: error Tipo S = probabilidad de que una estimación significativa tenga el signo equivocado; Tipo M = sobreestimación esperada de un efecto que sale significativo. Ejemplo del paper vía secundaria: potencia 13%, error M 3,11, error S 2%. https://sites.stat.columbia.edu/gelman/research/published/PPS551642_REV2.pdf [S]. (El ejemplo numérico lo tomé de un resumen; confirmarlo en el paper.)
- Consecuencia para un comercio chico: con poco tráfico, un test que "da ganador" tiende a exagerar el efecto; solo se pueden detectar efectos grandes. Twitter Eng.: dado el tamaño muestral y la varianza se puede calcular el menor efecto real detectable con 80% de potencia. https://blog.twitter.com/2016/power-minimal-detectable-effect-and-bucket-size-estimation-in-ab-tests [S]
- Optimizely recomienda, con poco tráfico, no probar muchas variantes a la vez porque tardan más en llegar a significancia. https://support.optimizely.com/hc/en-us/articles/4410283325325 [S] (fuente de un vendor).
- Mirar antes de tiempo ("peeking"): Miller escribe que "The best way to avoid repeated significance testing errors is to not test significance repeatedly... no peeking!". https://www.evanmiller.org/how-not-to-run-an-ab-test.html [S]. La cifra 26,1% de falsos positivos con revisión repetida la vi solo en una nota secundaria (towardsdatascience), no la confirmé en la página de Miller: no la cites sin verificar.
- Disputa: Miller sostiene que un diseño bayesiano permite parar cuando se quiera; un análisis de 2015 (R-bloggers) y un post de 2025 dicen que el bayesiano tampoco es inmune al peeking. https://www.r-bloggers.com/2015/08/is-bayesian-ab-testing-immune-to-peeking-not-exactly/ y https://www.alexmolas.com/2025/10/30/bayesian-ab-test-peeking.html [S]. Dos posturas; la base las da ambas.
- "Garden of forking paths" (Gelman y Loken): los falsos positivos aparecen aun sin pescar, por decisiones de análisis tomadas después de ver los datos. Simmons et al. (2011): la flexibilidad en recolección, análisis y reporte "dramatically increases actual false-positive rates". Dissenso: Rubin (2023) y Murayama et al. (2013) dicen que la inflación está exagerada. https://philarchive.org/archive/RUBTIE y https://confidence.spotify.com/glossary/garden-of-forking-paths [S].
- Sobre el libro de Kohavi, Tang y Xu: no encontré su texto sobre tráfico mínimo (hueco). No existe una regla universal de tráfico mínimo (nota de un practicante, https://dataanalysis.substack.com/p/how-to-run-an-ab-testing-on-low-traffic [S], opinión).

Recurso canónico: Gelman y Carlin 2014 (secciones sobre Tipo S y M y sobre diseño con efectos realistas) para tráfico bajo; el editorial de 2019 para el vocabulario. Intersección: experimento A/B (Producto) debería enlazar acá para "cuándo no conviene testear".

## 5. Modelado: Kimball, Inmon, "one big table"

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| dbt Docs, dimensional modeling https://docs.getdbt.com/terms/dimensional-modeling | práctica/vendor | 2/1/1/1 | [S] |
| Hightouch, Modern Data Warehouse Modelling pt. 2 https://www.hightouch.com/blog/data-warehouse-modelling-part-2 | práctica/vendor | 1/2/2/1 | [S] |
| Perficient (2022), "The star schema is obsolete" https://blogs.perficient.com/2022/09/13/the-star-schema-is-obsolete-reduced-cost-and-better-performance/ | opinión | 1/1/1/1 | [S] |

- dbt: la pregunta es si mantener hechos y dimensiones separados o crear tablas anchas; la respuesta "depends on the situation". Nota que el almacenamiento barato, las herramientas de BI que manejan joins, la evolución de SQL y analistas con más habilidad cambiaron la mirada sobre los esquemas en estrella. https://docs.getdbt.com/terms/dimensional-modeling [S]
- Perficient afirma que las razones de Kimball "no longer hold true" y cita un benchmark de Fivetran: tablas anchas "25-50% faster" en Redshift, Snowflake y BigQuery. Es benchmark de vendor citado por un blog; no lo verifiqué contra el original. https://blogs.perficient.com/2022/09/13/the-star-schema-is-obsolete-reduced-cost-and-better-performance/ [S]
- Hightouch propone híbrido: estrella como paso intermedio y tablas anchas materializadas a partir de ella. Una tesis (dspace.ut.ee) halló mejor legibilidad con tabla ancha pero problemas de rendimiento, con la oración cortada en el resultado [S]. Dos fuentes discrepan y se dan las dos.
- Lo que no apareció: posición actual de Kimball Group (ni libro ni sitio). Hueco importante: el argumento a favor del modelado dimensional no es solo rendimiento, es semántica compartida (definiciones consistentes de hechos y dimensiones, granularidad declarada); eso lo sostiene el libro, que no leí acá. La base debería enseñar granularidad y dimensiones como forma de pensar aunque la tabla final sea ancha (esto es una recomendación mía, no una fuente).

Recurso canónico propuesto: Kimball y Ross, The Data Warehouse Toolkit, capítulo 1-2 (granularidad y proceso de modelado en cuatro pasos), leído junto con la página de dbt como contrapeso. No verifiqué los números de capítulo.

## 6. Escalera de madurez descriptivo → prescriptivo

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Playfair Data, "3 Reasons the Analytics Maturity Framework Is Broken" https://playfairdata.com/3-reasons-the-analytics-maturity-framework-is-broken-and-whats-better/ | práctica (consultor) | 2/2/2/2 | [S] |
| Motio, "Rethinking the analytics maturity model" https://motio.com/rethinking-the-analytics-maturity-model/ | vendor | 1/2/1/2 | [S] |
| Towards AI, "The Analytics Maturity Model..." https://pub.towardsai.net/the-analytics-maturity-model-how-to-know-where-your-data-team-actually-stands-24953688f57d | blog | 1/1/1/1 | [S] |

- Origen que se le atribuye: el "Analytic Ascendancy Model" de Gartner, con filosofía tomada del Capability Maturity Model de ingeniería de software; etapas: descriptivo, diagnóstico, predictivo y prescriptivo. No hallé el documento primario de Gartner con las etapas (el único Gartner que apareció es de marketing, sin detalle), así que la atribución es de fuentes secundarias.
- Crítica principal: no es una secuencia por la que se "sube". Playfair: la causa del malentendido es suponer que uno pasa de un tipo de análisis a otro. Motio: la escalera asumió progresión lineal y la realidad dio madurez asimétrica; las organizaciones llegan a lo predictivo antes de tener gobierno que lo sostenga.
- Contra-postura: las etapas se apilan, y un caso prescriptivo requiere casos de los niveles de abajo; conviene no sobreinvertir en predictivo y prescriptivo antes de que lo básico sea sólido. Ambas posturas, citadas del mismo resultado del buscador.
- Cifras "74% descriptivo, 34% diagnóstico, 11% predictivo, 1% prescriptivo" (Gartner 2017) vienen de una fuente secundaria y no pude verificarlas: no citar.
- Todas las críticas son de consultores y vendors con interés en un modelo alternativo. No hay estudio con método que pruebe ni refute que la escalera describe el desarrollo real de las organizaciones.
- Para un comercio: lo útil es el orden de preguntas (qué pasó, por qué, qué pasará, qué hacer), no la idea de que hay que llegar al final.

## 7. Concepciones erróneas de quien aprende

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Anscombe (1973), "Graphs in Statistical Analysis", The American Statistician 27, 17-21 | primaria (no abrí) | 3/2/3/3 | [S] vía https://en.wikipedia.com/wiki/Anscombe%27s_quartet |
| Bickel, Hammel y O'Connell (1975), Science (Berkeley) | primaria (no abrí) | 3/2/3/3 | [S] vía https://en.wikipedia.org/wiki/Simpson%27s_paradox |
| Navarro, Learning Statistics with R, "The Cautionary Tale of Simpson's Paradox" https://stats.libretexts.org/Bookshelves/Applied_Statistics/Learning_Statistics_with_R_-_A_tutorial_for_Psychology_Students_and_other_Beginners_(Navarro)/01%3A_Why_Do_We_Learn_Statistics/1.02%3A_The_Cautionary_Tale_of_Simpsons_Paradox | texto abierto | 2/2/3/2 | [S] |

- Promedio como representativo: el cuarteto de Anscombe (1973) tiene cuatro conjuntos con estadísticos descriptivos casi idénticos y gráficos muy distintos; Anscombe temía que sus colegas perdieran de vista el valor de visualizar. https://en.wikipedia.org/wiki/Anscombe%27s_quartet [S]. (Para mediana vs. media en distribuciones sesgadas, como ventas por cliente, no hallé una fuente en esta ronda: hueco.)
- Agregar esconde la verdad (paradoja de Simpson): en los datos de admisión de Berkeley de 1973 el agregado sugería sesgo contra mujeres, y por departamento la relación cambiaba; el análisis corregido halló un "small but statistically significant bias in favor of women". Una fuente secundaria da cifras totales distintas de otra; verificar en el paper. https://en.wikipedia.org/wiki/Simpson%27s_paradox [S]. Atribución del nombre en disputa: Simpson publicó en 1951 y Blyth le puso el nombre en 1972 según Wikipedia.
- Correlación no es causa y "más datos siempre es mejor": no encontré fuente primaria aceptable para estas dos en esta ronda (hueco). Para lo segundo, la evidencia relacionada está en esta misma nota: Tigani (más volumen no mejora las consultas típicas) y Gelman-Carlin (más datos sin diseño no corrigen sesgos de selección; esto último es mi lectura, no cita literal). Sí aporta que más datos no arregla el sesgo: un conjunto grande y mal diseñado sigue sesgado.
- "p < 0.05 prueba que el efecto es real/importante": cubierto en sección 4 (ASA 2016 y 2019).

Recurso canónico: Anscombe 1973 (4 páginas) para promedios y gráficos; Bickel et al. 1975 para Simpson. En qué fijarse: que lo único que cambia entre caso y caso es mirar un nivel más desagregado o graficar.

## 8. Dónde no coincide la división del árbol

- "Estadística" y "Análisis" se solapan en la práctica: el bloque de p-valores, potencia y sesgos de la sección 4 vive en Estadística, pero lo usan Analítica-de-producto (experimentos) y Visualización (qué mostrar). Conviene una nota de "límites de la inferencia" enlazada desde las tres.
- "Gobierno-y-calidad" como panorama está bien, pero el único número que traje (USD 12,9 M, Gartner) es de grandes empresas; mejor enseñar calidad con ejemplos de comercio.
- La crítica al modern data stack no tiene un lugar natural: propongo que Modelado-y-almacenamiento abra con "cuándo no hace falta" (planilla/Postgres).

## 9. Huecos principales

- Los dos editoriales de la ASA (2016 y 2019) no se leyeron (403): citas y las seis tesis sin verificar literal.
- Sin método verificable para las cifras de fracaso (85%, 80%, 87%); solo el origen informal del 85%.
- Sin evidencia sobre pymes y comercios chicos para DDD, dashboards o BI (el estudio de 2011 es de grandes firmas).
- Sin estudios (ni críticas independientes) sobre dashboards que nadie mira ni métricas de vanidad; solo la ley de Goodhart, y su atribución es disputada.
- Sin la posición actual de Kimball Group ni benchmark independiente tabla ancha vs. estrella (solo benchmark de vendor de segunda mano).
- No leí a Kohavi, Tang y Xu sobre tráfico bajo; no encontré fuente para "correlación no es causa", "más datos siempre mejor" ni media vs. mediana.
- Sin documento primario de Gartner sobre la escalera de madurez ni sobre la cifra 74/34/11/1.
