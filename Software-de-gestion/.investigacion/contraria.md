# Investigación, ángulo contrario: software de gestión (ERP)

Fecha de la búsqueda: 2026-11-27. Capa cruda. Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3 en autoridad / profundidad / ejemplos / unicidad.

Tesis del ángulo: lo que la base va a afirmar (que implantar un ERP es riesgoso, que mejora el desempeño, que conviene adoptar las mejores prácticas, que la suite integrada es lo normal, que la nube reemplaza al instalado, que una pyme termina necesitando un sistema) tiene respaldo, pero casi todas las cifras populares no resisten el rastreo, y varias afirmaciones tienen evidencia en contra o mixta.

## Qué ya está escrito en el repo (para no repetir)

- `Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md`: definición de parte (vendedores) de ERP frente a facturador, contable y sistema de gestión; deja en una nota «Sin fuente todavía» los «estudios independientes sobre cómo fallan las implementaciones en pymes». Este informe llena parte de ese hueco, pero con evidencia de grandes proyectos de TI, no de pymes.
- `Planillas-de-calculo/cuando-pasar-a-una-base.md` y `Planillas-de-calculo/.investigacion/posicion-contraria-y-fundamentos.md`: señales para dejar la planilla (criterio propio, sin estudio), riesgo de mudarse demasiado pronto, Panko sobre errores. No tratan ERP ni pymes frente a ERP.
- `Software-de-gestion/` está vacío salvo `.investigacion/`: no hay notas propias todavía. Lo de abajo es propio del tema; la nota `mitos-del-software-de-gestion.md` del árbol es el destino natural de las secciones 1 y 2.
- No encontré en el repo ninguna nota sobre REA ni sobre Standish. Chequeo por búsqueda de texto, no exhaustivo.

## 1. Cuánto fallan de verdad las implantaciones de ERP

### Fuentes

| Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|
| Eveleens y Verhoef, «The Rise and Fall of the Chaos Report Figures», IEEE Software 27(1), 2010, pp. 30-36 | https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/ (DOI 10.1109/MS.2009.154) | primaria (crítica metodológica) | 3/2/2/3 | [M] abstract; lo leí vía repositorio de la universidad, no el cuerpo |
| Glass, «IT Failure Rates—70 Percent or 10–15 Percent?», IEEE Software 22(3), 2005, DOI 10.1109/MS.2005.66 | https://cacm.acm.org/?p=1819 (columna posterior de Glass en CACM que la cita) | primaria/secundaria | 2/1/1/2 | [S] no pude abrir el texto |
| Flyvbjerg y Budzier, «Why Your IT Project May Be Riskier Than You Think», HBR, sept. 2011 (89(9), pp. 23-25) | https://arxiv.org/abs/1304.0265 (versión de arXiv); https://papers.ssrn.com/abstract=2229735 | primaria | 3/2/2/3 | [M] abstract |
| McKinsey y Universidad de Oxford, «Delivering large-scale IT projects on time, on budget, and on value» | https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value | secundaria con interés (consultora) | 2/1/1/2 | [S] el sitio dio timeout; cifras por el buscador |
| Gartner, página «What IT leaders must do to avoid disappointing ERP initiatives» | https://www.gartner.com/en/information-technology/insights/what-it-leaders-must-do-to-avoid-disappointing-erp-initiatives | primaria del analista, tras muro | 2/1/1/2 | [S] la página devolvió 403; cifras por el buscador |
| The Register, 2025-11-13, sobre charla de una directora senior de estrategia de ERP de Gartner en Barcelona | https://www.theregister.com/2025/11/13/erp_disaster_gartner/ | secundaria (prensa) | 2/2/1/2 | [L] |
| Panorama Consulting, *The 2024 ERP Report* | https://qt9software.com/hubfs/2024-erp-report-panorama-consulting-group.pdf (copia alojada por un tercero) | secundaria con interés (consultora que vende evaluaciones tecnológicas) | 1/2/2/2 | [L] parcial: texto sí, gráficos de porcentajes no extraíbles |
| Sikich, nota sobre el origen de la cifra «75 %» | https://www.sikich.com/?p=12282 | secundaria con interés (consultora) | 1/1/1/1 | [S] |
| Hitt, Wu y Zhou (2002), nota al pie 4: «at least 90 percent of ERP implementations end up late or over budget [29]» | ver sección 2 | primaria que repite una cita | 3/1/1/2 | [L] |

### Afirmaciones

**1.1 La cifra «el 70 % / 75 % de los ERP fracasan» no tiene un estudio detrás que yo haya podido encontrar.**
- Gartner, según su propia página, afirma «más de 70 %» de las iniciativas de ERP recientes que no cumplirán del todo sus objetivos originales y hasta 25 % con fracaso catastrófico (https://www.gartner.com/en/information-technology/insights/what-it-leaders-must-do-to-avoid-disappointing-erp-initiatives) [S]. La Register lo confirma en boca de una analista de Gartner: «70 % of ERP initiatives fail to fully meet their original business use case goals», «25 % fail catastrophically», y anota que el artículo «no explica cómo Gartner llegó a los porcentajes» (tamaño de muestra o método) (https://www.theregister.com/2025/11/13/erp_disaster_gartner/) [L]. Son una sola fuente (la afirmación de Gartner), vista por dos canales.
- La definición de fracaso es «no cumplir del todo los objetivos originales»: eso no es lo que la gente entiende por «fracasa» (cancelar, abandonar). Gartner la presenta como pronóstico («will fail»), no como medición.
- El 75 % de la página de Gartner es otra cosa: el 75 % de las estrategias de ERP no está bien alineada con la estrategia de negocio (según el buscador, que resume la página) (https://www.gartner.com/en/information-technology/insights/what-it-leaders-must-do-to-avoid-disappointing-erp-initiatives) [S]. La Register da un 73 % de una encuesta de 2023 a 251 líderes tecnológicos, sin decir que la hizo Gartner. Dos fuentes dan cifras distintas (75 % y 73 %) para algo parecido: darlas las dos.
- Sikich dice que «75 % fracasan» empezó a circular en 2017 por un artículo de LinkedIn, y que otros autores dan un rango de 55 % a 75 % (https://www.sikich.com/?p=12282) [S]. Consultoras citan «55-75 %» a Gartner sin estudio (el buscador devolvió Rand Group y un documento de Scribd con el mismo rango sin fuente primaria). No encontré un informe de Gartner que lo sustente; no puedo afirmar que no exista, solo que no lo hallé.
- Cifra aún más vieja: Hitt, Wu y Zhou (2002) escriben «It is estimated that at least 90 percent of ERP implementations end up late or over budget [29]» (nota 4 de https://www.scheller.gatech.edu/directory/research/information-technology-management/wu/pdf/hitt_wu_zhou_jmis_2002.pdf) [L], con la referencia a una cita de prensa. Sirve de ejemplo de una cifra que circula desde fines de los 90.

**1.2 Standish CHAOS: la base de casi todas las cifras de «fracaso de proyectos de software» está desacreditada, y ERP hereda el problema.**
- Eveleens y Verhoef (2010) sostienen que las definiciones de Standish tienen cuatro problemas: se basan solo en la exactitud de la estimación de costo, plazo y funcionalidad; miden esa exactitud de forma unilateral (infla el éxito); incentivan manipular estimaciones; y promedian números con sesgo desconocido. Probaron las definiciones con 5.457 pronósticos de 1.211 proyectos reales (cientos de millones de euros) y concluyeron que las cifras de Standish no reflejan sus casos. Cita el 16 % de éxito del informe de 1994 (https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/) [M].
- Glass (2005) sostiene que las citas de la «crisis del software» se reducen a una fuente primaria, los informes de Standish, y que la encuesta (a ejecutivos de TI a quienes se les pedía contar fracasos) puede sesgar hacia el fracaso, aunque no sabemos cuánto (https://cacm.acm.org/?p=1819) [S].
- Cifras de Standish que circulan: 1994, 16,2 % éxito, 52,7 % «challenged», 31,1 % cancelados; 2015, 29 % éxito, 52 % challenged, 19 % fallidos (el 29 % sale por resta); cambió la definición de éxito entre ediciones (https://wiki.sj.ifsc.edu.br/images/3/3b/CHAOSReport2015_rev.pdf; resumen del buscador) [S]. Dato importante para la base: el informe de Standish trata de proyectos de software en general, no de ERP.
- Hueco de esta fuente: no verifiqué que Standish se niegue a compartir sus datos; el buscador no lo confirmó. Una columna de CACM dice que los datos no son públicos y que no hay réplicas (resumen del buscador de https://cacm.acm.org/?p=50417) [S].

**1.3 Lo que sí está medido: el riesgo de TI grande está en la cola, no en el promedio.**
- Flyvbjerg y Budzier (HBR 2011), con 1.471 proyectos de TI: sobrecosto promedio de 27 %, pero «Fully one in six of the projects in the sample was a Black Swan» (cerca de 1 de cada 6, 17 %), con sobrecosto de 200 % en promedio y casi 70 % de sobreplazo (https://arxiv.org/abs/1304.0265) [M]. La cifra de 1.471 y «una de cada seis» las confirmé en el abstract. La muestra es de TI en general, no de ERP.
- McKinsey y Oxford: más de 5.400 proyectos de TI grandes (precio inicial sobre 15 millones de dólares) promedian 45 % sobre presupuesto, 7 % sobre plazo, 56 % menos valor que lo previsto; «black swans» con más de 200 % de sobrecosto (https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value) [S]. Otra muestra posterior (más de 6.000 proyectos, 2001 a 2017) da 75 % de sobrecosto, 46 % de sobreplazo y 39 % menos valor: muestras distintas, no mezclar (mismo resumen) [S]. McKinsey vende servicios de este tipo.
- Lectura para la base: la afirmación defendible es «los proyectos de TI grandes tienen una cola gruesa de sobrecostos» y no «la mayoría de los ERP fracasan».

**1.4 Panorama Consulting da números que contradicen el 70 %, y tiene interés comercial.**
- *The 2024 ERP Report*: 131 respondientes, de agosto de 2022 a diciembre de 2023; mediana de ingresos anuales 200,5 millones de dólares; mediana de 750,5 empleados; 96,9 % con al menos una fase en vivo durante un año o más (https://qt9software.com/hubfs/2024-erp-report-panorama-consulting-group.pdf) [L parcial]. Textual: «More than half of organizations in our study stayed within their expected budget. The median project cost was $450,000», y lo mismo con el plazo («More than half ... completed their project within their...», la frase se corta en el extracto) [L].
- Para 2023, el buscador da: 47 % se pasó de presupuesto, mediana de costo 625.000 dólares, 183 respondientes (resumen secundario; otra fuente lo contradice con 131 respondientes, que según el PDF son de la edición 2024). Dos fuentes discrepan en el tamaño de muestra de la edición 2023: no la usaría sin leer el PDF de 2023 [S].
- Sesgos a decir: muestra de quienes responden una encuesta de una consultora; sin definición operativa de «éxito» visible en el texto que pude extraer; la consultora aconseja que las empresas contraten una evaluación tecnológica («Of those who significantly went over budget, only 33.3% said they used technology assessment services»), es decir, el informe empuja su propio servicio. Interés comercial: vende selección e implantación de ERP.

### Recurso canónico

Eveleens y Verhoef (2010) para entender por qué las cifras de «fracaso» no sirven, y Flyvbjerg y Budzier (2011) para qué decir en cambio. En qué fijarse: de Eveleens, las cuatro críticas a la definición; de Flyvbjerg, que el riesgo está en la cola. Qué no es: ninguno de los dos mide ERP.

## 2. ¿Mejora el desempeño un ERP?

### Fuentes

| Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|
| Hitt, Wu y Zhou, «Investment in Enterprise Resource Planning: Business Impact and Productivity Measures», JMIS 19(1), 2002, pp. 71-98 | https://www.scheller.gatech.edu/directory/research/information-technology-management/wu/pdf/hitt_wu_zhou_jmis_2002.pdf | primaria | 3/3/2/3 | [L] texto del PDF extraído con pdftotext |
| Poston y Grabski, «Financial impacts of enterprise resource planning implementations», Int. J. of Accounting Information Systems 2(4), 2001, pp. 271-294 | https://doi.org/10.1016/S1467-0895(01)00024-0 | primaria | 3/2/1/2 | [S] solo descripciones de terceros |
| Hendricks, Singhal y Stratman, J. of Operations Management 25(1), 2007 | (no abrí el texto; referencia vía buscador) | primaria | 3/2/1/3 | [S] |
| Aral, Brynjolfsson y Wu, «Which Came First, IT or Productivity?», ICIS 2006 / NBER 2007 | https://aisel.aisnet.org/icis2006/110 | primaria | 3/2/1/3 | [S] |

### Afirmaciones

- Hitt, Wu y Zhou encuentran que las empresas que invierten en ERP «tend to show higher performance across a wide variety of financial metrics», y también «a slowdown in business performance and productivity shortly after the implementation», mientras «financial markets consistently reward the adopters with higher market valuation (Tobin's q)». Reconocen que por falta de datos de mediano y largo plazo no pueden decir cuál es el efecto a largo plazo (abstract, PDF) [L].
- Números (todos del PDF) [L]: datos de 1986 a 1998, 24.037 observaciones empresa-año, 4.069 de empresas que implantaron módulos de un solo producto (unas 350 empresas); todos los adoptantes de un único producto (SAP R/3), y se analizó a partir de la base comercial que lo vendía. Productividad entre 2,3 % y 4,2 % más alta en adoptantes sin controlar por uso de TI, 2,7 % y 1,7 % controlando; valor de mercado (Tobin's q) cerca de 13 % mayor. Durante la implantación hay ganancia de productividad (3,6 %) seguida de pérdida posterior (4,7 %), neto de -1,1 % sin significancia estadística (con valor agregado como variable); con producción como variable, 2,4 % de ganancia y 1,7 % de pérdida.
- Cuidados: los autores mismos dicen que «not all projects will be successful» y que leen sus resultados como promedio con varianza grande entre empresas; que el efecto puede ser selección («if 'good' firms tend to adopt ERP systems for nonproductive reasons, that will still appear as positive benefits»). La muestra es de empresas públicas grandes de EE. UU. y de un solo producto de los 90: no se generaliza sin más a pymes ni a productos actuales. Los autores incluyen a uno que trabajó de enlace de SAP con universidades (nota biográfica del propio PDF): declararlo.
- Costo y plazo citados en el mismo artículo: instalación entre 1 y 3 años (21 meses de promedio), beneficios que empiezan a llegar en promedio a los 31 meses, costo típico de unos 15 millones de dólares y hasta 2 o 3 % de los ingresos; cerca de 60 % del costo es instalación y personalización, no licencia (PDF, citando a terceros) [L].
- Poston y Grabski (2001), según resúmenes: los adoptantes no mostraron mejora previa-posterior, mientras los no adoptantes empeoraron; otro trabajo lo lee como «no hubo mejora». Dos lecturas distintas del mismo estudio: darlas las dos. Estudios con ventana corta pueden perder efectos que llegan tarde (https://doi.org/10.1016/S1467-0895(01)00024-0) [S].
- Hendricks, Singhal y Stratman (2007): resultados «no uniformemente positivos» entre ERP, SCM y CRM, y no hallaron evidencia persistente de efecto negativo (resumen del buscador; no pude verificar el hallazgo exacto sobre rentabilidad) [S].
- Aral, Brynjolfsson y Wu: con 623 empresas grandes de EE. UU., de 1998 a 2005, los eventos de compra del ERP no se correlacionan con el desempeño y los de puesta en marcha sí; concluyen que el uso causa la mejora y no al revés (https://aisel.aisnet.org/icis2006/110) [S]. Los datos salen de la base de ventas de un solo proveedor.

### Recurso canónico

Hitt, Wu y Zhou (2002), secciones de resultados y de implantación (curva de «ganancia durante, pérdida después»). En qué fijarse: el efecto es promedio, de empresas grandes, con selección posible, y con un bache posterior a la puesta en marcha que los propios autores no pueden seguir más allá de la muestra.

## 3. Crítica a «adoptar las mejores prácticas del software»

### Fuentes

| Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|
| Davenport, «Putting the Enterprise into the Enterprise System», HBR 76(4), jul.-ago. 1998, pp. 121-131 | https://fenix.iseg.ulisboa.pt/downloadFile/281608120778205/HBR_1998_Davenport_ES.pdf (pide login; no pude leerlo) | primaria | 3/2/3/3 | [S] resumen de un sitio de resúmenes (https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm) |
| Soh, Kien y Tay-Yap, «Cultural fits and misfits: Is ERP a universal solution?», CACM 43(4), abril 2000, pp. 47-51 | https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits (403 al leerlo) | primaria | 3/2/3/3 | [S] resumen del buscador |
| Wagner y Newell, «'Best' for whom?...», J. of Strategic Information Systems 13(4), 2004, pp. 305-328 | https://sro.sussex.ac.uk/id/eprint/51660/ (texto no público) | primaria | 3/2/2/3 | [M] abstract |

### Afirmaciones

- Davenport: «An enterprise system, by its very nature, imposes its own logic on a company's strategy, organization, and culture»; el sistema empuja hacia procesos genéricos aun cuando los procesos propios sean fuente de ventaja competitiva; la complejidad hace impracticables las modificaciones grandes; cita el caso de una distribuidora de medicamentos que dijo que su sistema contribuyó a llevarla a la quiebra (resumen citado en el buscador, https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm) [S]. La cita textual la dio el buscador; no la verifiqué en el original. No encontré la palabra «straitjacket» en nada que pude ver.
- Soh y otros: ERP trae «mejores prácticas» incrustadas, pero los procedimientos locales se formaron en otras condiciones culturales, económicas y regulatorias. Hallazgo sobre hospitales de Singapur: tipología de desajustes, de datos (formato o modelo) y funcionales (de acceso, de control y de salida); los de salida (presentación y contenido de los reportes) fueron los más comunes (resumen del buscador) [S]. Sirve para la nota de análisis de brechas.
- Wagner y Newell (2004): el caso es una alianza entre un proveedor multinacional y una universidad para diseñar un paquete «de mejores prácticas» para educación superior; señalan una brecha entre la teoría declarada de la solución «best practice» y la teoría en uso de quienes la instalan (abstract del repositorio) [M]. Es un solo caso y trata de una universidad; el argumento de «best practice como construcción» lo desarrollan en trabajos posteriores del mismo grupo (2006, *Information and Organization*; 2010, ECIS) que no leí.
- La propia Gartner (2025) enumera como causas de fracaso la «customización atada demasiado a los procesos existentes» (https://www.theregister.com/2025/11/13/erp_disaster_gartner/) [L]: es decir, también la posición «adaptá el proceso» es la del analista, y la contraria («adaptá el software») aparece como causa de fracaso en el mismo discurso. Mostrar las dos.

### Recurso canónico

Davenport (1998) para la tesis; Soh y otros (2000) para los tipos de desajuste. Parte: el apartado sobre que el sistema impone su lógica; la tipología de desajustes. Marca [S] para ambos hasta leer el original.

## 4. Suite integrada frente a lo mejor de cada clase; «composable ERP»

### Fuentes

| Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|
| Light, Holland y Wills, «ERP and best of breed: a comparative analysis», Business Process Management J. 7(3), 2001, pp. 216-224 (DOI 10.1108/14637150110392683) | https://salford-repository.worktribe.com/output/1448144/erp-and-best-of-breed-a-comparative-analysis | primaria (estudio de caso) | 2/2/2/3 | [M] abstract |
| TechTarget, «Postmodern ERP countered by continued appeal of single suite» | https://www.techtarget.com/enterprise-software/feature/Postmodern-ERP-countered-by-continued-appeal-of-single-suite | secundaria (prensa de industria) | 1/2/2/2 | [S] |
| NetSuite, nota sobre la definición de «postmodern ERP» de Gartner | https://www.netsuite.com/portal/resource/articles/erp/how-does-netsuite-fit-gartners-definition-of-postmodern-erp.shtml | secundaria con interés (vendedor de suite) | 1/1/1/1 | [S] |

### Afirmaciones

- Light, Holland y Wills describen al ERP como plataforma dominante criticada por inflexible y presentan lo mejor de cada clase como alternativa que combina paquetes estándar o desarrollo a medida; comparan complejidad de implantación, funcionalidad, alineación con los procesos y mantenimiento (abstract del repositorio) [M]. Es un caso de un solo proyecto de lo mejor de cada clase contra una alternativa de proveedor único. No es evidencia general.
- Gartner introdujo «postmodern ERP» en 2013 (otra fuente dice 2014: dos fuentes discrepan en la fecha) y luego «composable ERP» (según el buscador; no encontré el informe primario de Gartner en ninguna versión) (https://www.techtarget.com/enterprise-software/feature/Postmodern-ERP-countered-by-continued-appeal-of-single-suite) [S]. Un pronóstico de Gartner: entre 15 % y más de 40 % de las empresas con estrategia «postmoderna» gobernada hacia 2020; no encontré si se cumplió [S].
- Escépticos citados: un analista de Forrester (integración limitada entre los productos del propio proveedor); uno de Constellation Research (las empresas siguen con un solo proveedor, los pronósticos de Gartner «no se estaban cumpliendo»); un directivo de un vendedor de suite (las empresas grandes siempre fueron «posmodernas»; la integración sigue siendo compleja aun en la nube); un exanalista de Gartner, ahora de un vendedor, cuenta que clientes que querían reemplazar el módulo de finanzas lo hallaron atado a compras y a pagos (todo por el mismo artículo de TechTarget) [S]. Casi todos con interés comercial. No encontré estudio empírico independiente que mida si la suite o lo mejor de cada clase rinde más.

### Recurso canónico

No hay uno independiente. Para la nota: Light, Holland y Wills (2001) como estudio de caso de la alternativa, y decir que el «composable ERP» es discurso de analista y de proveedores sin evidencia medida.

## 5. Personalizar o no

### Fuentes

| Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|
| Light, «The maintenance implications of the customization of ERP software», J. of Software Maintenance and Evolution 13(6), 2001, pp. 415-429 (DOI 10.1002/smr.240) | https://salford-repository.worktribe.com/output/1471899/the-maintenance-implications-of-the-customization-of-erp-software | primaria (dos casos) | 2/2/2/3 | [M] |
| Estudio de personalización de ERP en pymes de Corea y China (Lee y otros, 2011) | https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........1140063eeba193f0de1228ba0a428ae9 | primaria | 1/1/1/2 | [S] |
| Hong, Siau y Kim (2016), Asia Pacific J. of Innovation and Entrepreneurship, «The impact of ISP, BPR, and customization on ERP performance in manufacturing SMEs of Korea» | https://doi.org/10.1108/apjie-12-2016-008 | primaria | 2/2/1/2 | [S] |

### Afirmaciones

- Light (2001): personalizar puede dar valor a la organización, pero cada personalización debe evaluarse por su efecto en el mantenimiento futuro (dos casos; abstract resumido) [M]. Es decir, la regla «vainilla siempre» no sale de este estudio: sale «caso por caso».
- Un estudio coreano afirma que la preferencia por agregados (add-ons) frente a modificar se apoya sobre todo en casos con poca evidencia empírica; no halló efecto significativo del nivel general de personalización sobre satisfacción ni desempeño, pero sí del nivel de desarrollo de agregados [S]. Hong, Siau y Kim (96 respuestas, pymes manufactureras coreanas): los costos de consultoría y personalización tienen impacto positivo en el desempeño del ERP; el nivel de personalización no influye [S]. Muestras chicas, un solo país, autoinformadas.
- Un caso de agregado en un fabricante de memorias halló un ajuste y desempeño solo marginal (resumen del buscador, estudio de Ng, 2007) [S].
- Conclusión honesta: evidencia mixta y de baja calidad; no hay estudio fuerte que pruebe ni que refute «vainilla».

### Recurso canónico

Light (2001) por el criterio de evaluar cada personalización por costo de mantenimiento. [M] hasta leer.

## 6. REA frente a partida doble: por qué REA no prosperó en los productos

### Fuentes

| Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|
| Informe técnico ITU TR-2006-92 (IT-Universitetet, Copenhague) sobre REA y ERP | https://en.itu.dk/-/media/EN/Research/About-ITU-Research/Technical-Reports/2006/ITU-TR-2006-92-pdf.pdf | primaria | 2/2/1/2 | [S] solo vía buscador |
| Polovina y Fallon, REA y SAP | https://shura.shu.ac.uk/7439/1/Polovina%20REA%20analysis%20of%20sap.pdf; https://mpra.ub.uni-muenchen.de/34766/1/MPRA_paper_34766.pdf | primaria | 2/2/2/2 | [S] |
| Wikipedia, «Resources, Events, Agents» | https://wikipedia.com/wiki/Resources,_Events,_Agents | terciaria | 1/1/1/1 | [S] |

### Afirmaciones

- El informe ITU dice que los modelos contables de datos como REA «no han sido adoptados en los ERP actuales» y que los ERP siguen usando la partida doble como modelo contable que alimenta a otras aplicaciones; que REA ampliado se apoya en orientación a objetos, técnica que el diseño de datos de los ERP no adoptó; y que algunos conceptos de REA requieren más desarrollo antes de servir de base de un ERP (resumen del buscador) [S].
- Un trabajo sobre SAP sostiene que los ERP actuales están construidos alrededor de procedimientos de partida doble y que aplicar REA ahí choca con problemas (MPRA 34766) [S].
- Wikipedia: REA es popular en la enseñanza de sistemas de información contables y raro en la práctica; el estándar competidor XBRL GL imita la partida doble [S] (terciaria; sirve solo de pista).
- A favor de REA: Fallon y Polovina (2013) lo defienden como herramienta para entender implantaciones de ERP actuales (resumen del buscador) [S].
- No encontré fuente primaria que documente por qué los proveedores no lo adoptaron; lo anterior son explicaciones de académicos, no decisiones de proveedores.

### Recurso canónico

No puedo proponer uno confiable todavía. Candidato: McCarthy (1982), «The REA accounting model», *The Accounting Review* 57(3): no lo abrí. El informe ITU es el mejor para «por qué no prosperó»; leerlo entero antes de usarlo.

## 7. La nube: costos de SaaS frente a instalado y quienes vuelven

### Fuentes

| Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|
| Kinnunen y Kinnunen, TCO de ERP en SaaS e IaaS, ICSIM 2025 (cuatro casos de empresas grandes) | https://jyx.jyu.fi/jyx/Record/jyx_123456789_104922 | primaria | 2/2/2/3 | [S] |
| Nucleus Research, comisionado por Oracle (TCO 2,1 veces mayor en instalado) | https://oracle.com/webfolder/s/delivery_production/docs/FY16h1/doc26/550265-Guidebook-Oracle-ERP-Cloud.pdf | secundaria con interés (vendedor) | 1/1/1/1 | [S] |
| Hurwitz & Associates, citado por NetSuite (nube 50 % más barata en 4 años para 100 empleados) | https://netsuite.com.au/portal/au/resource/articles/on-premise-cloud-erp.shtml | secundaria con interés (vendedor) | 1/1/1/1 | [S] |
| a16z, «The Cost of Cloud, a Trillion Dollar Paradox», 2021-05-27 | https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/ | secundaria con interés (fondo de inversión, de infraestructura, no de ERP) | 2/2/1/2 | [S] |
| Encuestas de repatriación (Foundry 2026, OpenText 2025, Cloudian, VMware) | https://www.cio.com/article/4245967/cloud-repatriation-on-the-rise-but-tricky-questions-remain.html; https://www.opentext.com/en/media/guide/the-cloud-repatriation-shift-what-the-data-tells-us-guide-en.pdf | secundarias (encuestas de proveedores) | 1/1/1/1 | [S] |

### Afirmaciones

- No encontré un estudio revisado por pares con TCO controlado de varios años a escala de muchas empresas. Lo mejor académico es un estudio de cuatro casos: SaaS tiene ventaja de costo en casos específicos y la infraestructura como servicio (IaaS) podría dar más valor a empresas grandes por eficiencia de costo y control sobre el proveedor; el TCO de ERP en la nube es especialmente difícil de calcular (https://jyx.jyu.fi/jyx/Record/jyx_123456789_104922) [S].
- Las cifras a favor de la nube vienen de vendedores: 2,1 veces más caro el instalado (Nucleus Research para Oracle); 50 % menos en 4 años para 100 empleados (Hurwitz para NetSuite); y un modelo de un portal en el que en el año 5 el SaaS casi iguala al costo del instalado (licencia más infraestructura propia) (https://www.manufacturing.net/software/article/13240699/onpremise-vs-saas-erp-software-costs) [S]. Una comparación de IDC en alemán dice que el instalado trae costos ocultos que SaaS reduce o incluye (https://www.cio.de/article/3665781/kostenvergleich-lizenz-vs-saas-erp-systeme.html) [S].
- Repatriación: todo lo hallado es de infraestructura de nube, no de ERP en SaaS. Foundry 2026: dos tercios movieron o planean mover cargas fuera de la nube pública, 22 % promedio ya movido; OpenText 2025: 67 % repatrió algo y solo 14 % salió por completo; Cloudian: cerca de tres cuartos movió algo en 24 meses, y casi 30 % de ellos también amplió su nube (resúmenes del buscador; encuestas de proveedores, muestras no comparables) [S]. a16z supone 50 % de ahorro por repatriar sobre cifras de «expertos», con Dropbox (margen bruto de 33 % a 67 %, ahorro de unos 75 millones en dos años según un resumen) como ejemplo, y fue discutido por críticos que piden mirar el retorno y no solo el costo [S]. Las encuestas hablan de repatriación selectiva, no de éxodo.
- Hueco importante: no hay evidencia hallada de empresas que dejen un ERP en SaaS para volver a uno instalado. Para un ERP, el equivalente es cambiar de producto, y eso entra en costos de cambio.
- Cuidado con otra cifra de la nota de Panorama: según su informe 2024, la necesidad inesperada de tecnología adicional fue la causa más común de sobrecostos, y la consultora la vincula con la popularidad de la nube («cloud complexity», integraciones extra) (https://qt9software.com/hubfs/2024-erp-report-panorama-consulting-group.pdf) [L]. Es una hipótesis de la consultora, no un hallazgo.

### Recurso canónico

Ninguno bueno. Para TCO, el estudio de casos de Kinnunen y Kinnunen (2025), leyéndolo entero; para repatriación, aclarar que es de infraestructura.

## 8. En pymes: ¿la planilla es el sistema real?

### Fuentes

| Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|
| Tesis de Lund sobre uso de planillas en presupuestos con ERP y BI disponibles | https://lup.lub.lu.se/search/files/5929854/3050012.pdf | primaria (tesis) | 1/2/2/2 | [S] |
| Newman, propuesta doctoral sobre «feral systems» (planillas junto a un ERP en pymes de Israel) | https://arxiv.org/pdf/1503.02997 | primaria (propuesta, sin hallazgos) | 1/1/1/2 | [S] |
| Aberdeen (2010), 579 pymes, citada por CIO | https://www.cio.com/article/282843/enterprise-software-erp-rollouts-why-smbs-say-no.html | secundaria (consultora) | 1/2/1/2 | [S] |
| BPM Partners, citado por PYMNTS (84 % de profesionales de finanzas complementan el ERP con planillas) | https://www.pymnts.com/innovation/2017/why-smbs-should-use-spreadsheets/ | secundaria con interés | 1/1/1/1 | [S] |

### Afirmaciones

- Aberdeen (2010): cerca de 70 % de 579 pymes aún no invirtió en un ERP; la razón más citada fue «somos demasiado chicos» (39 %); el autor del artículo aclara que las razones declaradas no dicen nada sobre la funcionalidad de planilla frente a ERP (https://www.cio.com/article/282843/enterprise-software-erp-rollouts-why-smbs-say-no.html) [S]. Dato viejo.
- Planillas conviven con el ERP aun en empresas que lo tienen: 84 % según BPM Partners (cifra de una consultora de software de gestión del desempeño, no verificada en su origen) [S]; la tesis de Lund concluye que el uso de planillas en presupuestos es significativo pese al ERP y al BI, por falta de integración entre contabilidad financiera y de gestión y por flexibilidad [S].
- Figura de «feral system» (sistema salvaje: planilla que crece al lado del sistema oficial) como categoría de estudio en pymes (propuesta de Newman; sin resultados) [S].
- No encontré encuesta revisada por pares que mida pymes con solo planilla frente a pymes con sistema, ni evidencia de que «una pyme no necesita un ERP». Lo que sí hay es evidencia de que muchas no lo adoptan y de que las que lo adoptan siguen usando planillas.
- Evidencia contra la planilla: en el repo, `Planillas-de-calculo/cuando-pasar-a-una-base.md` cita a Panko sobre errores en planillas (https://arxiv.org/pdf/1602.02601). En Argentina, una pyme que factura debe usar comprobante electrónico: ese límite es normativo, no de preferencia (tema aparte; no investigado en este ángulo).

### Recurso canónico

Ninguno para la pregunta exacta. Para los hechos de coexistencia planilla y ERP: la tesis de Lund, leída entera.

## ¿La división del árbol coincide con la del campo?

- Casi toda la literatura académica que encontré (Hitt, Davenport, Soh, Light) trata ERP como una sola cosa: «implantación y desempeño», no «columnas técnicas» ni «categorías». El material contrario cae en `Implementacion/` y `Fundamentos/mitos`. La sección de la suite frente a lo mejor de cada clase, en `Categorias-de-producto/`, tiene poca evidencia: es sobre todo discurso de analistas.
- El árbol pone la nube («nube frente a instalado») en `Mercado-y-economia/mercado-en-argentina.md` y `licencia-y-suscripcion.md`. La evidencia hallada sobre TCO y repatriación es de dos tipos (vendedores de ERP e infraestructura general): no hay base para una nota de repatriación de ERP.

## Huecos

1. Cifra exacta y origen de «75 %» y «70 %»: no hallé estudio que las sustente; no encontré el informe primario de Gartner (la página devolvió 403). Falta leer el original de Gartner.
2. Davenport (1998), Soh y otros (2000), Wagner y Newell (2004), Poston y Grabski (2001), Hendricks y otros (2007), Light (2001): sin texto completo. Las afirmaciones son [S] o [M]. Hay que leerlos antes de citarlos como primarias.
3. Panorama 2023: no abrí el PDF; muestra discrepante (183 frente a 131). El 2024 lo leí solo en texto; sin los gráficos no tengo el porcentaje exacto de proyectos fuera de presupuesto de 2024 (solo «más de la mitad dentro de presupuesto»).
4. McKinsey y Oxford: el sitio dio timeout; cifras por el buscador. Tampoco abrí el artículo de Budzier y Flyvbjerg de 2013 (arXiv 1304.4525).
5. Glass (2005): sin texto; no confirmé la afirmación de que Standish no comparte sus datos.
6. Evidencia empírica independiente de suite frente a lo mejor de cada clase: no la hallé.
7. Evidencia sólida sobre personalizar: solo estudios chicos asiáticos y dos casos de Light.
8. REA: sin fuente primaria sobre decisiones de producto; McCarthy 1982 sin abrir.
9. Nube: no hay TCO independiente a escala ni repatriación de ERP; solo infraestructura y encuestas de proveedores.
10. Pymes: sin encuesta con método que compare planilla y ERP; nada específico de Argentina.
11. Nada sobre fracaso en pymes ni en Latinoamérica; ni estudios del bache posterior a la puesta en marcha posteriores a 2007.
