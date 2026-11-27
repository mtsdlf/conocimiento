# Calidad del servicio, mirada desde la operación: informe crudo

Fecha de lectura: 2026-11-27. Marcas: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3: Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).

Advertencia general: esta ronda tuvo mucho bloqueo. Las páginas de iso.org, el visor OBP, la vista previa de ANSI, el artículo de HBR (capítulo en O'Reilly), PubMed Central y la nota de Telus devolvieron 403 o captcha al leerlas. Casi todo lo normativo está en [M] o [S]. Ninguna norma ISO se leyó entera. Lo que dicen las normas se afirma solo hasta donde lo muestran sus fichas oficiales o tablas de contenido de terceros.

## 0. Cómo divide el campo este ángulo

El árbol propuesto (métricas / encuestas / monitoreo) coincide con cómo lo parte la práctica, con dos matices:

- La norma ISO 18295-1 mete las métricas dentro de los requisitos del centro de contacto (Anexo A informativo sobre métricas), no en una norma aparte de medición. COPC también las trata como parte del estándar operativo. Ver sección 1.
- «Voz del cliente» (analizar reclamos para mejorar) en la práctica es el cierre del ciclo de las tres: encuestas, monitoreo y reclamos alimentan el mismo análisis de causas. ISO 10002 lo ubica en su cláusula 8 («Mantenimiento y mejora»), no en el tratamiento del reclamo individual. Conviene que la nota de voz del cliente enlace a Caso/reclamo y a Escalamiento/problema y causa raíz, y no se quede en Calidad.

## 1. Métricas de la operación

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| ISO 18295-1:2017, ficha oficial (ISO) | https://www.iso.org/standard/64739.html | primaria | 3/1/1/3 | [S] (403 al leer; datos vistos en el resultado del buscador) |
| Vista previa ANSI de ISO 18295-1 | https://webstore.ansi.org/preview-pages/ISO/preview_ISO+18295-1-2017.pdf | primaria | 3/2/1/3 | no leída (403) |
| Tabla de contenido de ISO 18295-1 (DIN) | https://www.din.de/de/mitwirken/normenausschuesse/nadl/veroeffentlichungen/wdc-beuth:din21:276760944/toc-2704082/download | secundaria (copia de ficha) | 2/1/1/2 | no legible (PDF comprimido; guardado como binario) |
| COPC, páginas del estándar CX (R8.0) | https://www.copc.com/copc-standards/for-csps/ | primaria (el dueño del estándar) | 3/1/1/3 | [S] |
| COPC, benchmarking: eficiencia y costo | https://cx.copc.com/hubfs/COPC.com%20PDF%20and%20Docs/GBS%202022/10.%20Global%20Benchmarking%20Series%202022_Contact%20Center%20Efficiency%20and%20Cost%20Management%20vs%201.0.pdf | primaria | 2/2/2/2 | [S] |
| Wikipedia, «First call resolution» | https://en.wikipedia.org/wiki/First_call_resolution | secundaria (cita a SQM, ContactBabel, blogs) | 1/1/1/1 | [L] |
| Gartner, resumen sobre FCR (2024) | https://www.gartner.com/en/documents/5232563 | secundaria (abstract de pago) | 2/1/1/2 | [M] |
| Atlassian, FCR | https://www.atlassian.com/itsm/service-request-management/first-call-resolution | secundaria (proveedor) | 1/1/2/1 | [S] |
| Gallup, estudio de caso de un banco | https://news.gallup.com/businessjournal/185963/banking-analysis-better-service-doesn-increase-costs.aspx | primaria (artículo del propio estudio) | 2/1/2/2 | [L] |
| Telus International, FCR | https://www.telusinternational.com/articles/first-call-resolution-difficult-to-measure-dangerous-to-ignore/ | secundaria (proveedor) | 1/1/1/1 | [S] (403; vía buscador) |

### Afirmaciones

FCR (resolución al primer contacto)
- Definición corriente: «a metric that measures a call center's performance for resolving customer interactions on the first call or contact» (Wikipedia, que cita a SQM Group). https://en.wikipedia.org/wiki/First_call_resolution
- Hay dos maneras de medirla y no dan lo mismo. Interna: se cuenta como resuelto si no hay llamada repetida en una ventana; Wikipedia, citando a un blog de proveedor, dice que la ventana va de «1 to 30 days» y que esto «can overstate the FCR rate by 10% to 20% higher than the external FCR measurement». Externa: encuesta posterior al contacto. Wikipedia: «The call center industry average for FCR using the external FCR measurement method of a post-call survey is 70%», sin cita. Las cifras vienen de blogs de proveedores: una sola fuente débil, no dos. https://en.wikipedia.org/wiki/First_call_resolution
- No hay estándar interno único de FCR (Wikipedia, mismo enlace) y hay debate sobre qué es «resuelto» (ídem).
- Alcance por canal: según el resumen de Gartner, la mayoría mide FCR solo dentro de un canal atendido, mientras el cliente cuenta su primer intento en cualquier canal (leído del buscador, abstract de https://www.gartner.com/en/documents/5232563; el texto completo es de pago).
- Ventana de reapertura recomendada por Atlassian: 24 a 48 horas antes de contar un caso resuelto, y combinar FCR con reaperturas y satisfacción como control cruzado (resultado del buscador de https://www.atlassian.com/itsm/service-request-management/first-call-resolution; [S]).
- Definiciones que compiten, para la nota: (a) interna por ventana sin repetición; (b) por encuesta («¿se resolvió en el primer contacto?»); (c) por agente («lo resolví»); (d) multicanal desde el cliente. Las cuatro salen de las fuentes de arriba; ninguna fuente primaria las compara.

AHT (tiempo medio de atención)
- COPC lo incluye, con utilización y ocupación, entre las métricas de eficiencia que exige su estándar CX (reporte de benchmarking de COPC citado arriba; [S]).
- Evidencia sobre «bajarlo empeora la atención»: no encontré estudio académico. Lo que hay es opinión de proveedores (apurar al cliente sube las llamadas repetidas) y un caso de Gallup. Gallup, un banco de México, primer trimestre de 2015: los grupos de trabajo con el 30% superior en puntajes de servicio tuvieron un tiempo medio por llamada 2,4% menor y una FCR 6,1% mayor; el grupo «élite» (alto en FCR y en servicio) tuvo una duración de llamada 6,1% menor y una FCR casi 13% mayor. El artículo no da tamaño de muestra, definiciones ni significación. Es una correlación en una sola organización. https://news.gallup.com/businessjournal/185963/banking-analysis-better-service-doesn-increase-costs.aspx
- Nota: el buscador resumió esas cifras con los números cruzados (duración 6,1% y FCR 13%); prevalece la lectura del artículo, pero la ambigüedad está en el original. Verificar antes de citar.

Reapertura, pendientes, abandono
- Reapertura: solo la menciona Atlassian como control del FCR ([S]). No hallé definición normativa.
- Pendientes (backlog) y antigüedad, abandono: no encontré fuente que los defina con método dentro de lo leído. Hueco.

ISO 18295-1/2 y COPC
- ISO 18295-1:2017, «Customer contact centres, Part 1: Requirements for customer contact centres»: fija requisitos de servicio y, donde hace falta, métricas; aplica a centros propios o tercerizados; tabla de contenido: relación con el cliente, comunicación de información al cliente, infraestructura de prestación (atención de interacciones, datos, entorno de trabajo, continuidad), relación con el cliente contratante; Anexo A informativo con directrices de métricas. Revisada y confirmada en 2023; hay un proyecto de segunda edición en elaboración (ISO/AWI 18295-1). Precio de referencia CHF 98 a 100. Todo desde fichas y buscador, no del texto. https://www.iso.org/standard/64739.html
- ISO 18295-2 es para organizaciones que usan los servicios de centros de contacto (cliente contratante). Mismo origen, no leída.
- COPC: la versión vigente que se ve es la Release 8.0 («Operational Playbook for CX»); desde la R8 la organización puede elegir métricas que cumplan la intención definida; la R7 trajo métricas «mejoradas y simplificadas»; el estándar incluye métricas operativas que afectan la experiencia, no solo de CX. Las definiciones están en el PDF del estándar, que no se leyó. https://www.copc.com/copc-standards/for-csps/

### Recurso canónico propuesto
- Para qué medir y con qué definiciones: ISO 18295-1, Anexo A (de pago; vista previa de ANSI), leído junto con el documento del estándar COPC. Fijarse en cómo cada métrica define su numerador, denominador y ventana. Mientras no se lean, la nota debe decir que las definiciones de FCR compiten y mostrar las cuatro.
- Para el cálculo de pendientes y ocupación: Gans, Koole y Mandelbaum 2003 (ver brief; no consultado por mí en esta ronda).

## 2. Encuestas transaccionales

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Dixon, Freeman y Toman 2010, HBR 88(7/8): 116-122 | https://hbr.org/2010/07/stop-trying-to-delight-your-customers | primaria | 3/3/2/3 | [M] (pared de pago; solo resumen) |
| Great Brook, «Effortless Experience: Weak & Flawed Research Model» | https://greatbrook.com/effortless-experience-weak-flawed-research-model/ | secundaria, crítica de consultora | 1/2/2/2 | [L] |
| Great Brook, diseño del cuestionario | https://greatbrook.com/effortless-experience-questionnaire-design-survey-administration-issues/ | secundaria | 1/2/1/2 | [S] |
| Call Centre Helper, «Debunking the Customer Effort Score» | https://www.callcentrehelper.com/debunking-the-customer-effort-score-28652.htm | secundaria | 1/1/1/2 | [S] |
| MeasuringU, lealtad y satisfacción | https://measuringu.com/?p=561 | secundaria | 1/1/1/1 | [S] |
| Mittal y Kamakura (satisfacción y recompra, 100.040 compradores de autos) | https://core.ac.uk/download/77512107.pdf (posible; no confirmé que sea este el artículo) | primaria | 3/3/3/3 | [S], no leído |
| Johnson et al. 2005, Journal of Marketing 69 (satisfacción, compromiso y retención) | https://ecommons.cornell.edu/bitstream/1813/71434/1/Johnson5_The_effects_of_customer_satisfaction_relationship_commitment.pdf | primaria | 3/3/2/2 | [S] |
| Cooil et al. 2007, Journal of Marketing 71 (satisfacción y participación en el gasto, longitudinal) | https://typeset.io/pdf/a-longitudinal-analysis-of-customer-satisfaction-and-share-2de8qsyl7q.pdf | primaria | 3/3/2/2 | [S] |
| Patient satisfaction y tasa de respuesta, Health Services Research 2002 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1464019 | primaria | 3/3/2/2 | [S] (captcha) |
| Ocal y Babin 2016, tasa de respuesta y sesgo en investigación de marketing | https://link.springer.com/chapter/10.1007/978-3-319-24184-5_174 | primaria | 2/2/1/2 | [S] |
| ISO 10004:2018, ficha | https://www.iso.org/standard/71582.html | primaria | 3/1/1/3 | [S] (403) |
| ANSI blog sobre ISO 10004 | https://blog.ansi.org/ansi/iso-10004-2018-qms-customer-satisfaction/ | secundaria | 1/1/1/1 | no leída (403) |

### Afirmaciones

CES (Customer Effort Score)
- Origen: Dixon, Freeman y Toman, «Stop Trying to Delight Your Customers», HBR, julio-agosto 2010, pp. 116-122. Tesis del resumen: «Delighting customers does not build loyalty. Reducing customers' effort does.» (resumen en el buscador; la página de HBR solo dice que la idea del deleite está tan arraigada que los gerentes rara vez la examinan). https://hbr.org/2010/07/stop-trying-to-delight-your-customers
- Cifras que circulan: una encuesta de CEB a 97.000 clientes, con 9% de desleales entre los de bajo esfuerzo (resumen secundario, vía buscador). Páginas de proveedores repiten «94% de intención de recompra y 88% de aumentar el gasto» entre quienes tuvieron buen CES. No pude rastrear esas cifras al artículo ni al informe de CEB; en las notas, no citarlas como hechos hasta verlas en el original. El 94% y el 9% pueden ser complementarios, pero no lo verifiqué.
- Crítica de método (Great Brook, sobre el libro de 2013 «The Effortless Experience», [L]): (1) mide lealtad intencionada, no conducta futura: «never compare scores from service transactions today to actual future customer loyalty behaviors»; (2) compara CES con preguntas de actitud en la misma encuesta; (3) el estudio se limitó «intentionally» a transacciones de centro de servicio (p. 12 del libro), lo que puede inflar la importancia del esfuerzo; (4) el libro dice «mitigate disloyalty by reducing customer effort» (p. 130); la crítica cita una cifra de un blog, de 22% al pasar de 1 a 5 y 2% de 5 a 7, que es un dato no verificado de tercera mano. Es una crítica de consultora competidora (con interés), no una réplica. https://greatbrook.com/effortless-experience-weak-flawed-research-model/
- Otra lectura [S]: la redacción de la pregunta cambió entre versiones, lo que dificulta comparar (https://greatbrook.com/effortless-experience-questionnaire-design-survey-administration-issues/); la pregunta oficial solo se puede hacer a quien contactó a la empresa, así que no dice nada de la lealtad del resto de los clientes (resumen de HBR vía buscador, https://tagteam.harvard.edu/hub_feeds/924/feed_items/25252); en otro análisis el esfuerzo es un factor entre otros, no el predictor más fuerte (https://www.callcentrehelper.com/debunking-the-customer-effort-score-28652.htm; https://measuringu.com/?p=561).
- Estado: no encontré réplica académica revisada por pares a favor o en contra. La evidencia a favor es del propio CEB (la fuente que vende la métrica) y la crítica es de consultoras. Declararlo como evidencia débil por ambos lados.

CSAT y recompra (evidencia con conducta, no con intención)
- Mittal y Kamakura (100.040 compradores de autos): la forma de la relación difiere según se mida intención o conducta; con intención hay rendimientos decrecientes y con conducta «monotonically increasing returns»; en algunos grupos el sesgo de respuesta es tan fuerte que la satisfacción declarada no tiene correlación con la recompra (r = 0). Resumen del buscador; no leí el artículo ni confirmé revista ni año. Este es el hallazgo más útil para decir «CSAT alto no garantiza recompra», pero hay que leerlo antes de citarlo. Ver URL arriba.
- Johnson et al. 2005 (J. of Marketing 69) usa clientes de telefonía con encuesta más retención posterior; Cooil et al. 2007 (J. of Marketing 71) mide satisfacción y participación en el gasto en el tiempo y dice que el trabajo previo era casi todo transversal. Solo por los resúmenes del buscador. Los dos sirven de base del método (datos de encuesta cruzados con conducta posterior).

Tasa de respuesta, sesgo de no respuesta
- Estudio en pacientes (Health Services Research, 2002): asociación positiva entre satisfacción media y tasa de respuesta; las simulaciones sugieren que la no respuesta puede inflar la satisfacción global, más en los proveedores con pacientes menos satisfechos (resumen del buscador; PMC dio captcha). https://pmc.ncbi.nlm.nih.gov/articles/PMC1464019 Es de salud, no de servicio al cliente; se usa como evidencia de mecanismo.
- Ocal y Babin 2016: tácticas para subir la respuesta (recordatorios, preaviso, incentivos) pueden añadir sesgo (resumen). https://link.springer.com/chapter/10.1007/978-3-319-24184-5_174
- Sesgo de quien responde y escala: no encontré fuente directa que compare, por ejemplo, escala de 5 contra 7 puntos en encuestas de servicio. Hueco.

ISO 10004
- ISO 10004:2018 «Quality management, Customer satisfaction, Guidelines for monitoring and measuring», edición 2, julio de 2018; reemplaza a la de 2012; revisada y confirmada en 2023; unas 35 páginas; precio visto CHF 159. Alcance, según resúmenes de organismos nacionales: guía para definir e implementar procesos de seguimiento y medición de la satisfacción, para cualquier organización. Estructura (tabla de contenido de DIN, no legible esta vez): marco de seguimiento y medición, examen de la información y evaluación de la eficacia de las acciones. Se declara compatible con ISO 9001 y 9004 y alineada con 10001/10002/10003 (resumen de un tercero). Todo [S]. https://www.iso.org/standard/71582.html
- NPS transaccional frente a relacional: no hallé fuente específica en esta ronda; la disputa del NPS como predictor está en otra nota (solo enlazar).

### Recurso canónico propuesto
- CES: el artículo de HBR (2010) para el planteo, y la reseña de Great Brook para lo que el estudio no puede decir (lealtad declarada, no conducta). Fijarse en qué se midió contra qué.
- Satisfacción y conducta: Mittal y Kamakura (si se confirma la referencia) y Johnson et al. 2005.
- Seguimiento de la satisfacción: ISO 10004 (las cláusulas sobre examinar la información y evaluar eficacia).

## 3. Monitoreo de calidad y voz del cliente

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Verint, «QM Assessments: How Many is Enough?» | https://verint.com/blog/qm-assessments-how-many-is-enough | secundaria (proveedor) | 1/2/2/2 | [S] |
| TechTarget, buenas prácticas de QA | https://www.techtarget.com/searchCustomerExperience/tip/Best-practices-for-contact-center-quality-assurance | secundaria | 1/1/1/1 | [S] |
| CustomerThink, nota sobre cantidad de evaluaciones | https://customerthink.com/?p=68805 | secundaria | 1/1/1/1 | [S] |
| ISO 10002:2018, ficha | https://www.iso.org/standard/71580.html | primaria | 3/1/1/3 | [S] (403) |
| Tabla de contenido de ISO 10002 (DIN) | https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:293819883/toc-2874880/download | secundaria | 2/2/1/2 | no leída directamente; el buscador la resumió |

### Afirmaciones
- Cantidad de evaluaciones por agente: las guías de proveedores dan de 6 a 10 por mes; Verint, con una fórmula de tamaño de muestra, estima 65 por agente por mes para un agente de unas 1.400 conversaciones, a confianza de 90%. El número depende de supuestos propios. Es consejo de proveedor, no norma. https://verint.com/blog/qm-assessments-how-many-is-enough
- Calibración entre evaluadores: prácticas recomendadas por proveedores (mínimo de 10 llamadas por ejercicio, sesiones cada pocas semanas con las mismas grabaciones, tolerancia previa como puntajes totales dentro de 5% y revisión de criterios que varían más de 10%). Todo consejo, sin método publicado. https://customerthink.com/?p=68805 [S]
- Evaluación automática: no se investigó a fondo en esta ronda; hueco.
- ISO 10002:2018, edición 3, julio de 2018, revisada y confirmada en 2023. Su resumen oficial incluye analizar los reclamos para mejorar la calidad del producto y del servicio y auditar y revisar la eficacia y la eficiencia del proceso. Tabla de contenido (DIN, por el buscador): cláusula 8 «Maintenance and improvement» con 8.1 recopilación de información, 8.2 análisis y evaluación de los reclamos, y luego evaluación de satisfacción, seguimiento, auditoría, revisión por la dirección y 8.7 mejora continua; Anexo I sobre seguimiento continuo; principio rector 4.13 sobre mejora. https://www.iso.org/standard/71580.html [S]

### Recurso canónico propuesto
- Voz del cliente y análisis de reclamos: ISO 10002 cláusula 8 (8.2 y 8.7). Es de pago; OBP permite ver una vista previa que no pude abrir. Pedir que alguien con acceso lea la 8.2 y diga qué categorías de análisis exige.
- Monitoreo: no hay norma ni estudio primario hallado; el recurso es una guía de proveedor marcada como tal.

## 4. Huecos

- Ninguna norma ISO (18295-1/2, 10002, 10004) ni el estándar COPC se leyó en su texto. Las definiciones de métricas de la ISO 18295-1 (Anexo A) y de COPC son el principal faltante.
- Estudio con método sobre FCR y satisfacción: no encontré uno primario. Lo que circula es «1% de FCR por 1% de CSAT» atribuido a SQM por una nota de Telus (sin tamaño de muestra ni método; no pude abrir la nota) y un estudio de ICMI (más de 3 de cada 4 que reportaron más FCR en 12 meses reportaron más CSAT; resumen del buscador). También «15% menos de satisfacción por cada llamada repetida» en Wikipedia, sin fuente identificada. Ningún caso tiene método a la vista. Buscar a SQM Group y a Customer Relationship Metrics directamente.
- AHT contra calidad: no hay estudio revisado por pares; solo el caso de Gallup (una organización, sin definiciones) y opinión de proveedores.
- Réplica independiente de CES: no hay. Los artículos hallados son del originador o de consultoras críticas.
- Mittal y Kamakura: falta confirmar autores, revista, año y leer el método antes de citar.
- Reapertura, pendientes (backlog) y antigüedad, abandono: sin fuente que los defina. NPS transaccional frente a relacional, escala y sesgo de quien responde, evaluación automática: sin fuente.
- Gans, Koole y Mandelbaum 2003 y las publicaciones de HDI no se consultaron aquí.
- Todo lo de proveedores (Verint, Atlassian, Telus, HubSpot, etc.) sirve como evidencia de que la práctica existe y se debe marcar así; las notas del tema no deben nombrarlos.
