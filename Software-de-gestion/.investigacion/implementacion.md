# Investigación: vertical Implementación (software de gestión)

Capa cruda. Marcas: [L] texto completo leído, [M] metadatos o abstract leídos, [S] resumen secundario o del buscador (no leí la fuente). Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Búsqueda hecha el 2026-11-27. Todo lo traído de la web es dato.

Aviso de método: varios PDFs académicos estaban tras muro o login (ACM, Emerald, IEEE, ScienceDirect, un repositorio universitario). Lo que no pude leer va marcado [S] o [M], y las citas literales solo vienen de lo que sí leí.

## 0. Sobre la división del árbol

- La división del árbol (ciclo, elegir, brechas, migración, puesta en marcha, partners, después) coincide con cómo el campo reparte el tema en las metodologías públicas de implementación: fases tipo descubrir/preparar/explorar/construir/desplegar/operar [L: Microsoft; S: SAP].
- Dos desajustes menores. (1) El campo trata «elegir un sistema» como parte de la primera fase del ciclo (chartering en Markus y Tanis [S]); la nota propia está bien, pero el ciclo debe decir que la selección ocurre adentro. (2) Las «brechas» (fit-gap) en la literatura académica son un caso de «tailoring» (configurar o modificar) de Brehm et al. [S] y de «misfits» de Soh et al. [M]; ahí se solapa con `Columnas-tecnicas/configurar-o-personalizar.md`. Conviene que `analisis-de-brechas.md` trate la decisión (adaptar proceso o software) y la columna trate el mecanismo.
- La evidencia sobre «cuál puesta en marcha falla más» es mucho más débil de lo que el árbol sugiere (ver sección 5): no hay estudio comparativo sólido, solo casos y encuestas chicas.

## 1. Ciclo del proyecto

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Markus, Axline, Petrie y Tanis (2000), «Learning from adopters' experiences with ERP: problems encountered and success achieved», J. of Information Technology 15(4) | https://aisel.aisnet.org/jit/vol15/iss4/2 | primaria (abstract) | 3/2/2/3 | [M] |
| Markus y Tanis (2000), «The enterprise system experience: from adoption to success», capítulo en Zmud (ed.), *Framing the Domains of IT Research*, Pinnaflex | https://www.cambridge.org/core/books/secondwave-enterprise-resource-planning-systems/learning-from-adopters-experiences-with-erp-problems-encountered-and-success-achieved/94D8867ED89F52AAC1029598D21A39A5 (ficha de referencia); el PDF indexado (https://pro.unibz.it/Staff/Ascime/Documents/ERP%20paper.Pdf) dio 404 | primaria | 3/3/3/3 | [S] (no pude leer el texto) |
| Ross y Vitale (2000), «The ERP revolution: surviving vs. thriving», Information Systems Frontiers 2(2):233-241 | https://doi.org/10.1023/A:1026500224101 | primaria | 3/2/2/2 | [S] |
| Microsoft, «Introduction to the Success by Design framework» (actualizada 2026-11-26) | https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/success-by-design | primaria de práctica (documentación de producto; solo como evidencia de que la práctica existe) | 2/3/3/1 | [L] |
| SAP, material de aprendizaje de la metodología Activate | https://learning.sap.com/courses/discovering-sap-activate-implementation-tools-and-methodology/describing-the-methodology-structure | primaria de práctica | 2/2/2/1 | [S] (la lectura directa dio 404; descripción del buscador) |

Afirmaciones
- Las cuatro fases de Markus y Tanis son chartering, project, shakedown y onward and upward; la primera cubre el caso de negocio y las decisiones de solución; la nombran así fuentes que citan el modelo. https://www.cin.ufpe.br/~llfj/Emerald/Critical%20factors%20for%20successful%20implementation%20of%20enterprise%20systems.pdf [S]. No leí las definiciones del capítulo: hueco.
- Markus et al. (2000), estudio patrocinado por un proveedor de ERP (lo dice el abstract): «success of ERP systems depends on when it is measured» (frase atribuida por el lector del abstract, no verifiqué la cita exacta); el éxito en un momento se relaciona solo débilmente con el éxito en otro; hay problemas en todas las fases y muchos de los tardíos empiezan temprano sin ser notados; recomiendan definiciones amplias de éxito, varias medidas y detectar problemas pronto. https://aisel.aisnet.org/jit/vol15/iss4/2 [M]. Interés comercial: patrocinio de un proveedor.
- Ross y Vitale: estudian cómo las empresas generan valor del ERP, etapas, obstáculos y factores críticos. https://typeset.io/papers/the-erp-revolution-surviving-vs-thriving-4t9kukqfrw [S]. Una síntesis de la Universidad de Houston habla de cinco etapas (Approach, Dive, Resurfacing, Swimming, Jet-skiing) pero no confirmé que sean de este paper. Descartar hasta leer.
- Práctica pública de un proveedor: cinco fases «methodology-agnostic»: Discover, Initiate, Implement, Prepare, Operate; Operate = «stabilization and a shift in focus towards functionality and enhancements that are planned for the next phase». https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/success-by-design [L]. La propia página aclara que «doesn't guarantee implementation outcomes».
- SAP Activate: Discover, Prepare, Explore, Realize, Deploy, Run; el hypercare cae dentro de Deploy; Explore usa talleres «fit-to-standard». Descripción del buscador sobre materiales de SAP. https://learning.sap.com/courses/discovering-sap-activate-implementation-tools-and-methodology/describing-the-methodology-structure [S].

Recurso canónico: Markus y Tanis (2000), el marco de fases y de tres medidas de éxito (a conseguir y leer; fijarse en cómo se define éxito en cada fase) más Markus et al. (2000) como evidencia de que los problemas nacen temprano. Aviso: no confirmé el texto.

Ya escrito en el repo: `Gestion-de-proyectos/Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md` (Flyvbjerg: sobrecostos en megaproyectos; no es de ERP). Es propio del tema el ciclo de cuatro fases y su definición de éxito por fase.

## 2. Factores críticos de éxito (CSF)

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Somers y Nelson (2001), «The impact of critical success factors across the stages of ERP implementations», HICSS-34 | https://doi.org/10.1109/HICSS.2001.927129 | primaria | 3/3/2/3 | [S] |
| Holland y Light (1999), «A critical success factors model for ERP implementation», IEEE Software 16(3):30-36 | https://salford-repository.worktribe.com/output/1448129/a-critical-success-factors-model-for-erp-implementation | primaria | 3/2/2/3 | [S] |
| Finney y Corbett (2007), «ERP implementation: a compilation and analysis of critical success factors», BPMJ 13(3):329-347 | https://www.doi.org/10.1108/14637150710752272 | primaria (revisión de literatura) | 3/2/1/2 | [S] |
| Mabert, Soni y Venkataramanan (2003), «Enterprise resource planning: managing the implementation process», EJOR 146(2):302-314 | https://econpapers.repec.org/RePEc:eee:ejores:v:146:y:2003:i:2:p:302-314 | primaria | 3/3/2/3 | [M] sin abstract en esa ficha; datos de método vía buscador [S] |

Afirmaciones
- Somers y Nelson: 86 organizaciones que habían completado o estaban completando una implantación; clasifican 22 factores críticos por etapa, tomando de base el modelo de seis etapas de Cooper y Zmud (según Plant y Willcocks, que es secundaria). https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_ieee_primary_927129 [S]. No tengo la lista de los 22: hueco.
- Holland y Light: modelo con factores estratégicos y tácticos (visión de negocio, apoyo de la dirección, planes y cronograma como estratégicos; configuración técnica y gestión del proyecto como tácticos), basado en Slevin y Pinto. https://salford-repository.worktribe.com/output/1448129/a-critical-success-factors-model-for-erp-implementation [S]
- Finney y Corbett: 45 artículos seleccionados, codificación inductiva; señalan que la duplicación en el recuento de frecuencia es una limitación, y piden más investigación sobre gestión del cambio. https://www.doi.org/10.1108/14637150710752272 [S]
- Mabert et al.: dos fases, 12 casos de manufactura y luego encuesta; busca diferencias entre las empresas que terminaron en plazo o dentro del presupuesto y las que no. https://econpapers.repec.org/RePEc:eee:ejores:v:146:y:2003:i:2:p:302-314 [S]
- Una nota para el tema: los CSF son listas inducidas de encuestas y casos; no prueban causalidad. Lo dice Finney y Corbett sobre su propia limitación; hay además un artículo que cuestiona «How critical are the CSFs?» https://www.doi.org/10.1108/BPMJ-11-2012-0127 [S] (leer antes de usar).

Recurso canónico: Somers y Nelson (2001) para «qué factor pesa en qué etapa»; Finney y Corbett (2007) como mapa de la literatura. Falta leer ambos.

## 3. Elegir un sistema

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Ratkevičius et al., «ERP selection criteria: theoretical and practical views» (Ekonomika, 2012) | https://epublications.vu.lt/object/elaba:4594534/index.html | primaria (revisión) | 2/2/1/2 | [S] |
| «A Holistic ERP Selection Methodology» (SINTEF) | https://www.sintef.no/globalassets/project/smartlog/publikasjoner/2007/holistic-erp-selection-methodology.pdf | primaria | 2/2/1/2 | [S] |
| Olson, Johansson y Atem de Carvalho, capítulo sobre criterios de selección | https://dx.doi.org/10.1007/978-3-642-28827-2_5 | primaria (capítulo) | 2/2/1/2 | [S] |
| GFOA, «Which System is Truly Best?» | https://www.gfoa.org/materials/gfr-0826-erp | guía de un organismo (finanzas públicas, EE.UU.) | 2/1/1/2 | [S] |
| Panorama Consulting, «ERP software selection in the public sector» | https://www.panorama-consulting.com/erp-software-selection-in-the-public-sector/ | secundaria, consultora que vende selección (interés comercial) | 1/1/1/1 | [S] |

Afirmaciones
- No hay una clasificación estándar de criterios; se parten en relacionados con el software y relacionados con la implantación (Ratkevičius et al.). https://epublications.vu.lt/object/elaba:4594534/index.html [S]
- Los métodos de decisión se apoyan en programación matemática y teoría de decisión (AHP, ANP, DEA); otras líneas identifican CSF de la evaluación sin dar guía para hacer el proceso. https://epublications.vu.lt/object/elaba:4594534/index.html [S]
- De 16 artículos relevantes sobre selección que revisó el trabajo de SINTEF, solo cinco proponían metodologías o modelos paso a paso. https://www.sintef.no/globalassets/project/smartlog/publikasjoner/2007/holistic-erp-selection-methodology.pdf [S]
- GFOA recomienda licencias, implantación y soporte en una sola licitación (RFP). https://www.gfoa.org/materials/gfr-0826-erp [S]. Panorama dice que el sector público suele pedir tres o más referencias de tamaño y alcance similar (https://www.panorama-consulting.com/erp-software-selection-in-the-public-sector/ [S]; consultora con interés).
- No encontré guía oficial que describa la demo guionada con casos propios ni la prueba de concepto. Esa parte del árbol sale hoy de práctica de consultoras, no de estudio con método: declararlo.

Recurso canónico: ninguno claro. Propuesta provisional: una revisión de criterios (Ratkevičius et al. 2012) para la lista de criterios, más el método general (necesidades → criterios → lista corta → demo → referencias → contrato) presentado como práctica sin evidencia comparativa. Leer completos antes de confirmar.

Ya escrito en el repo: `Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion-en-el-comercio/sistemas-de-gestion-en-el-comercio.md` (errores comunes de elección según un autor que vende desarrollo; declara «Sin fuente todavía» para estudios independientes de fallas en pymes) y `Compras-y-abastecimiento/Abastecimiento-estrategico/costo-total-de-adquisicion.md`.

## 4. Análisis de brechas (fit-gap)

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Soh, Kien y Tay-Yap (2000), «Cultural fits and misfits: is ERP a universal solution?», CACM 43(4):47-51 | https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits (403 al leer) | primaria | 3/2/3/3 | [S] |
| Brehm, Heinzl y Markus (2001), «Tailoring ERP systems: a spectrum of choices and their implications», HICSS-34 | https://doi.org/10.1109/HICSS.2001.927130 | primaria | 3/3/2/3 | [S] |
| Davenport (1998), «Putting the enterprise into the enterprise system», HBR 76(4):121-131 | https://fenix.iseg.ulisboa.pt/downloadFile/281608120778205/HBR_1998_Davenport_ES.pdf (login) | primaria | 3/2/3/3 | [S] |
| Gattiker y Goodhue (2005), MIS Quarterly 29(3):559-585 | https://aisel.aisnet.org/misq/vol29/iss3/9/ | primaria | 3/3/2/3 | [S] |

Afirmaciones
- Soh et al.: los desajustes se agrupan en datos, funcionales y de salida; los de salida son los más frecuentes (según un resumen); hay menos en contabilidad y finanzas, donde normas internacionales dan algo de estandarización, y más en el sistema de atención de pacientes de un hospital en Singapur; el artículo se presenta como hallazgos tempranos de un estudio mayor. https://synapsesocial.com/papers/W1969607455 y https://cacm.acm.org/?p=6012 [S]. Es un solo caso (un hospital): decirlo.
- Brehm et al. llaman «tailoring» a configurar y a modificar; describen siete tipos de personalización por capa (un revisor suma informes ampliados, programación de flujos e interfaces), tipos exactos sin confirmar. https://researchr.org/publication/BrehmHM01 [S]
- Davenport: según una síntesis de terceros, la mayoría de las empresas tendrán que adaptar o rehacer sus procesos al sistema; cita a FoxMeyer, que decía que su sistema contribuyó a su quiebra. https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm y https://typeset.io/papers/putting-the-enterprise-into-the-enterprise-system-4loq0slhz0 [S]. Texto sin leer.
- Gattiker y Goodhue: encuesta a 111 plantas; el ERP encaja mejor con alta interdependencia y baja diferenciación; la fe de erratas (diciembre 2005) corrige que mejora de coordinación sí se sostiene, eficiencia de tareas no, y que las hipótesis sobre personalización no se sostuvieron. https://misq.umn.edu/pub/skin/frontend/default/misq/pdf/appendices/ErrataNotesGattikerGoodhue.pdf [S]. Si se cita, usar la versión corregida.
- Dato de consultora: la «personalización ideal» es 10 a 20 % (Panorama 2017). Es opinión de la consultora, presentada como «ideal», sin método publicado. https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf [L]
- Práctica de proveedor: talleres «fit-to-standard» (SAP, [S] arriba).

Recurso canónico: Soh et al. (2000) para el concepto de misfit (leer completo; 5 páginas) y Brehm et al. (2001) para la escala de personalización. Fijarse en que el primero es un caso único.

Ya escrito en el repo: la columna `Columnas-tecnicas/configurar-o-personalizar.md` (aún no existe en esta rama; el árbol la prevé) y `Desarrollo/Evolucion/migraciones-y-actualizaciones.md`. Propio de esta nota: la decisión adaptar proceso o software.

## 5. Migración de datos

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Documentación de ERPNext, «Opening balance» | https://docs.frappe.io/erpnext/user/manual/en/opening-balance | primaria de práctica | 2/2/2/1 | [L] |
| Microsoft, guía de cutover de Dynamics 365 (ms.date 2024-01-30) | https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/prepare-go-live-cutover-strategy | primaria de práctica | 2/3/2/1 | [L] |
| Wipro, «The ERP data migration conundrum» (consultora) | https://www.wipro.com/analytics/latest-thinking/solving-the-erp-data-migration-puzzle/ | secundaria con interés comercial | 1/1/1/1 | [S] |
| Panorama 2017 (datos como causa de atraso) | https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf | secundaria | 1/1/2/1 | [L] |

Afirmaciones
- ERPNext: «Obtain an approved Trial Balance and supporting schedules at the cutover date»; «The Trial Balance must balance before it is entered»; los saldos de clientes y proveedores entran como facturas abiertas «where future settlement and ageing matter»; el stock entra con una conciliación de stock de tipo apertura; hay una cuenta transitoria de apertura que debe quedar en cero al final. https://docs.frappe.io/erpnext/user/manual/en/opening-balance [L]. Evidencia de que la práctica existe en un producto abierto; no se nombra en las notas.
- Microsoft: el cutover es el paso «when you switch from your old system to the new one»; «During cutover, you can't use your old system or your new one», suele durar menos de 48 horas; hay que ensayar («mock cutover») varias veces con los mismos datos, herramientas y personas; el plan incluye dueño y suplente por tarea, verificación y plan de reversa (rollback); las condiciones de entrada incluyen estrategia de migración «ready and tested»; al final se verifica que «your data is accurate and complete in production»; decisión go/no-go con criterios. https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/prepare-go-live-cutover-strategy [L]
- Consultoras (Wipro, TechTarget) coinciden en perfilar y limpiar el origen, deduplicar maestros, mapear, conciliar con expertos del negocio y financieramente antes del go-live, y cargar maestros con saldos abiertos como enfoque más común. https://www.wipro.com/analytics/latest-thinking/solving-the-erp-data-migration-puzzle/ [S]. Son afirmaciones de práctica, sin método publicado.
- Panorama 2017: «data issues» es la segunda causa citada de atraso, con 16 % (la primera, alcance ampliado, 19 %). https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf [L]
- Dato local ya en el repo: un fabricante avisa que al migrar no se cargan datos históricos como ventas o cuentas corrientes, solo maestros y stock (`Sistemas-de-gestion-en-el-comercio/sistemas-de-gestion-en-el-comercio.md` línea 62).

Hueco principal: no encontré estudio académico con método sobre migración de datos en ERP (la búsqueda devolvió solo guías de proveedores y consultoras). Sugerencia: buscar «data conversion» en la literatura de ERP o en normas de migración de datos (ISO/IEC 25012 para calidad de datos, aún sin evaluar).

Recurso canónico: la guía de cutover de Microsoft como ejemplo público de la práctica de ensayo y conciliación, y la página de saldos de apertura de ERPNext para qué entra (maestros, saldos, abiertos). Fijarse en la cuenta transitoria que debe cerrar en cero.

Ya escrito en el repo: la frontera con `Columnas-tecnicas/integracion-y-migracion.md` (mecanismo) y `Datos/Ingesta-y-transformacion/etl-y-elt.md`; esta nota trata la actividad de proyecto.

## 6. Puesta en marcha

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| CIO.com, «Supply chain: Hershey's bittersweet lesson» (2002-11-15) | https://www.cio.com/article/2440386/supply-chain-management/supply-chain---hershey-s-bittersweet-lesson.html | secundaria (prensa) | 2/2/3/1 | [L] |
| Computerworld, «Halloween less spooky for Hershey's this year» (2001-01-05) | https://www.computerworld.com/article/1577198/halloween-less-spooky-for-hershey-s-this-year.html | secundaria (prensa) | 2/1/3/1 | [L] |
| CACM, «Managing risks in enterprise systems implementations» (caso FoxMeyer y Dow Corning) | https://cacm.acm.org/research/managing-risks-in-enterprise-systems-implementations | primaria | 3/3/3/3 | [S] (403 al leer) |
| Computer Weekly / ComputerWoche / Consultancy.uk sobre Lidl | https://www.computerweekly.com/news/252446965/Lidl-dumps-500m-SAP-project ; https://www.computerwoche.de/article/2777764/lidl-stoppt-millionenschweres-sap-projekt-fuer-warenwirtschaft.html | secundaria (prensa) | 2/1/2/1 | [S] (403 al leer) |
| Bernroider y Leseure (2005), citado por la búsqueda; Mabert et al. | ver notas | primaria | 2/2/2/2 | [S] |
| Panorama 2017 | https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf | secundaria | 1/2/2/1 | [L] |

Afirmaciones
- Hershey: sistema de 112 millones de dólares (ERP, CRM y planificación de la cadena de tres productos); en septiembre de 1999 el CEO dijo que habría problemas de pedidos y que no se entregarían unos 100 millones de dólares en caramelos para Halloween 1999; la acción cayó más de 8 % ese día. https://www.cio.com/article/2440386/supply-chain-management/supply-chain---hershey-s-bittersweet-lesson.html [L]. Ese artículo no dice si fue de una vez o por fases; la prensa lo dice en otros textos que no pude confirmar. No afirmar «big bang» en la nota sin fuente que lo diga. Las ganancias del tercer trimestre de 1999 cayeron 19 % (Computerworld, [L]). Cifras que circulan en presentaciones de estudiantes (caída de 35 % de la acción, 150 millones) discrepan y no son fuente.
- FoxMeyer: según el artículo de CACM sobre gestión de riesgos, el proyecto de SAP R/3 de 65 millones de dólares empezó en 1993 junto con una automatización de depósito muy ambiciosa; cargo de 34 millones por inventario y pedidos en 1996, quiebra en agosto de 1996, adquirida por McKesson por 80 millones en noviembre de 1996; los síndicos demandaron a la consultora y a SAP. https://cacm.acm.org/research/managing-risks-in-enterprise-systems-implementations [S] (cifras de un resumen del buscador). Las fuentes secundarias discrepan en el costo (65 vs más de 100 millones). Hay que leer el CACM antes de usarlo.
- Lidl: proyecto iniciado en 2011, detenido en julio de 2018 tras unos siete años, con retorno al sistema anterior; el costo de unos 500 millones de euros es de prensa y analistas, no confirmado por Lidl ni por SAP; causa reportada: la gestión de inventario a precio de compra. https://www.consultancy.uk/news/18243/lidl-cancels-sap-introduction-having-sunk-500-million-into-it [S]. Dos o más medios, pero todos originados en una misma fuente primaria (Lebensmittel Zeitung): cuenta como una.
- Evidencia comparativa: una búsqueda no encontró ningún estudio comparativo robusto de big bang contra por fases. Lo que hay: Mabert et al. concluyen que las firmas que pudieron usar big bang tuvieron el menor tiempo de implantación (citado por un tercero); una entrevista con 30 manufactureras halló que las chicas con big bang andaban mejor que las grandes con despliegue gradual, con el tamaño como confusor; un estudio europeo sobre presupuesto no halló influencia significativa del enfoque en el costo; Bernroider y Leseure (2005) hallan que las pymes eligen más big bang y las grandes más fases. Todo [S], vía https://core.ac.uk/download/301355122.pdf (403) y https://www.dea.univr.it:443/documenti/OccorrenzaIns/matdid/matdid965805.pdf. No leí ninguno. Hueco declarado.
- Práctica de proveedor sobre corte: ensayo, ventana de cutover, rollback, go/no-go, transición a soporte (Microsoft, [L], sección 5); revisión de preparación obligatoria («Go-live Readiness Review ... mandatory»), en la guía de Microsoft [L]. Hypercare dentro de Deploy en SAP [S].
- Panorama 2017: 56 % de los encuestados tuvo una interrupción operativa material en el go-live; el 68 % de ellos la sufrió cuatro semanas o menos. https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf [L]

Recurso canónico: la guía de cutover de Microsoft (describe la práctica de ensayar, con criterios de entrada y de salida) más el caso Hershey en una fuente leída (CIO.com) como ejemplo de falla de corte en temporada alta. No hay recurso canónico académico para big bang frente a fases: decirlo.

Ya escrito en el repo: `Arquitectura/Estilos/strangler-fig.md` (migración gradual de un sistema heredado: es la analogía técnica de la puesta en marcha por fases) y `Desarrollo/Evolucion/sistema-heredado.md`.

## 7. Partners de implementación

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Ko, Kirsch y King (2005), «Antecedents of knowledge transfer from consultants to clients in enterprise system implementations», MIS Quarterly 29(1):59-86 | https://aisel.aisnet.org/misq/vol29/iss1/5 | primaria | 3/2/2/3 | [M] (abstract leído) |
| Microsoft, Success by Design (rol del partner y del proveedor) | https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/success-by-design | práctica de proveedor | 2/2/1/1 | [L] |
| Panorama 2017 (por qué se contratan consultores) | https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf | secundaria con interés | 1/1/2/1 | [L] |

Afirmaciones
- Ko et al.: los clientes esperan que los consultores les transfieran su conocimiento para poder mantener los sistemas «independent of the consultants»; datos de pares consultor-cliente de 96 proyectos de ERP; los factores relacionados con el conocimiento, motivacionales y de comunicación influyen en la transferencia; 9 de 13 hipótesis apoyadas. https://aisel.aisnet.org/misq/vol29/iss1/5 [M]. Es la mejor evidencia que hallé sobre la relación de agencia: la transferencia no es automática.
- Microsoft: el marco se ofrece a «system integrators, independent software development companies, and customers»; «Microsoft recognizes that Success by Design doesn't guarantee implementation outcomes»; los proveedores reconocen en su propia guía el reparto entre ellos, el partner y el cliente. https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/success-by-design [L]
- Panorama 2017: motivos para contratar consultores: 27 % gestionar la implantación, 22 % gestión del cambio, 19 % una selección «sin sesgo». https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf [L]. Interés comercial: la consultora vende estos tres servicios y la muestra son visitantes de su sitio.
- Casos de litigio como evidencia de agencia: FoxMeyer demandó a la consultora y a SAP (CACM, [S]); ver sección 6.

Hueco: no hallé estudios de riesgo de agencia contra consultores ni de contratos de precio fijo frente a tiempo y materiales; tampoco metodologías públicas de implementadores independientes (solo de proveedores). Sugerencia: auditorías de organismos públicos, como informes de contralorías sobre implantaciones de ERP municipales o provinciales (p. ej. el caso Birmingham, no verificado acá).

Recurso canónico: Ko, Kirsch y King (2005) para la transferencia de conocimiento; leerlo completo y fijarse en la distinción entre transferir y aplicar el conocimiento.

Ya escrito en el repo: el tema prevé `Mercado-y-economia/canal-de-partners.md` (desde el lado del proveedor); no existe aún en esta rama. Propio de esta nota: roles y contratos desde quien compra.

## 8. Después de la puesta en marcha

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Hitt, Wu y Zhou (2002), «Investment in ERP: business impact and productivity measures», JMIS 19(1):71-98 | https://www.scheller.gatech.edu/directory/research/information-technology-management/wu/pdf/hitt_wu_zhou_jmis_2002.pdf | primaria | 3/3/2/3 | [L] |
| Gattiker y Goodhue (2005), MISQ 29(3) | https://aisel.aisnet.org/misq/vol29/iss3/9/ | primaria | 3/3/2/3 | [S] |
| Nicolaou (2004), J. of Information Systems 18(2):79-105 | https://dblp.dagstuhl.de/rec/journals/jisys/Nicolaou04a.html | primaria | 3/2/1/2 | [S] |
| Markus et al. (2000) | https://aisel.aisnet.org/jit/vol15/iss4/2 | primaria | 3/2/2/3 | [M] |
| Panorama 2017 (disrupción y beneficios) | https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf | secundaria | 1/2/2/1 | [L] |

Afirmaciones
- Hitt et al., texto leído. Abstract: «Even though there is a slowdown in business performance and productivity shortly after the implementation, financial markets consistently reward the adopters with higher market valuation (as measured by Tobin's q).» Datos: solo clientes de SAP R/3, 1986 a 1998, 24.037 observaciones firma-año, 4.069 de firmas con algún módulo SAP (unas 350 firmas distintas). Hipótesis H2b: «continued drop in performance shortly after ERP implementation». Los propios autores dicen no poder probar si la productividad se recupera, por la escasez de datos posteriores. https://www.scheller.gatech.edu/directory/research/information-technology-management/wu/pdf/hitt_wu_zhou_jmis_2002.pdf [L]. Interés: D. J. Wu figura como enlace de la alianza universitaria de SAP y ganó premios de ella (biografía del propio artículo); la muestra es de un solo producto.
- Panorama 2017: «56% of organizations experience some type of material operational disruption at go-live»; 78 % obtuvo beneficios, pero 37 % menos de la mitad de lo esperado; 48 % los obtuvo dentro de seis meses del go-live; Panorama sugiere apuntar a 18 a 24 meses; los años anteriores muestran 66 %, 41 %, 46 % y 37 % con la mitad o menos de los beneficios (2013 a 2016): la serie se mueve mucho, señal de una muestra cambiante. https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf [L]
- Nicolaou y Bajor (otra revista): los adoptantes rindieron significativamente mejor en los dos años posteriores frente a controles pareados. https://www.clutejournals.com/index.php/RBIS/article/view/4504 [S]. Choca de forma parcial con el «slowdown» de Hitt: dar las dos.
- Gattiker y Goodhue: incluye el tiempo desde la implantación como variable. [S]
- Microsoft: la fase Operate es estabilización y luego mejoras planificadas; la actualización continua de la plataforma es parte del producto en la nube («one version»). https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/success-by-design [L]. Es afirmación de proveedor.
- Ross y Vitale hablan de una etapa de recuperación (resurfacing) según una síntesis, sin confirmar. [S]

Recurso canónico: Hitt, Wu y Zhou (2002), pp. 71-98 (ya leído: abstract y hipótesis H2); fijarse en que mide cuentas de firmas públicas y que dice no ver la recuperación. Para el efecto de la caída más fina, Gattiker y Goodhue (2005) a leer.

Ya escrito en el repo: `Desarrollo/Evolucion/migraciones-y-actualizaciones.md` (actualizar sin romper) y `Contabilidad/Control-interno/controles-sobre-sistemas.md` (soporte y cambios en producción). Propio de esta nota: la caída de rendimiento y el hypercare desde la empresa.

## 9. Datos de fracaso y sobrecostos: fuente original, método e interés

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Panorama Consulting Solutions, «2017 Report on ERP Systems & Enterprise Software» | https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf | secundaria, consultora | 1/2/2/2 | [L] |
| Eveleens y Verhoef (2010), «The rise and fall of the Chaos report figures», IEEE Software 27(1):30-36 | https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/ | primaria (crítica) | 3/2/2/3 | [M] |
| Standish Group CHAOS | (no accedí al informe original; no es abierto) | secundaria/privada | 1/1/1/1 | [S] |
| Hitt et al. 2002 | ver sección 8 | primaria | 3/3/2/3 | [L] |

Afirmaciones
- Panorama 2017: encuesta puesta en el sitio web de Panorama durante doce meses (marzo de 2016 a febrero de 2017), con 342 respondientes; es una muestra autoseleccionada, sin diseño muestral declarado; la ventaja de lo reportado es el autoinforme del encuestado. Resultados de 2016 según su tabla: 74 % con sobrecosto, 59 % con atraso, duración media 16,9 meses, costo medio 1,3 millones de dólares, 37 % con la mitad o menos de beneficios, 56 % con disrupción operativa. La tabla de años previos: sobrecosto 54 % (2013), 55 % (2014), 57 % (2015), 74 % (2016); atraso 72 %, 75 %, 57 %, 59 %. Aclaran que el costo medio bajó de 3,8 a 1,3 millones «likely due to the smaller and less complex organizations in this year's sample». https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf [L]. Interés comercial: la propia consultora ofrece selección, gerenciamiento de implantación, gestión del cambio y testimonio pericial (sección «About»); sus conclusiones recomiendan gestión del cambio y análisis de negocio, que son lo que vende. Los años anteriores cambian de modo irregular (74 % en 2016 frente a 57 % en 2015): leer como muestra distinta, no como tendencia.
- Standish CHAOS: Eveleens y Verhoef muestran que las definiciones de Standish juzgan el éxito solo por exactitud de la estimación de costo, plazo y alcance, y que promedian estimaciones con sesgo desconocido; al aplicar esas definiciones a su base de 5.457 pronósticos de 1.211 proyectos, las cifras de Standish no coinciden con la realidad. https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/ [M]. Standish no es ERP en particular: no usar su cifra para ERP.
- Mito «el 70 % de los ERP fracasan»: no hallé la fuente original de esa cifra; las que circulan atribuyen a consultoras y a prensa. Sirve de insumo para `Fundamentos/mitos-del-software-de-gestion.md`. Con lo leído, lo que sí se puede decir: la tasa depende de cómo se define fracaso (Markus et al.: el éxito depende de cuándo se mide), de quién responde (Panorama: muestra voluntaria) y de si se compara con otros proyectos de TI.
- Hitt et al. dan la otra cara: las firmas con ERP rinden más en promedio en muchas medidas financieras, con un bajón posterior a la implantación (sección 8).

Recurso canónico: Eveleens y Verhoef (2010) como vacuna contra las cifras de fracaso; Panorama 2017 solo como ejemplo de encuesta de consultora, con su método (muestra autoseleccionada) a la vista.

Ya escrito en el repo: `Gestion-de-proyectos/Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md` (Flyvbjerg: nueve de cada diez megaproyectos con sobrecostos) y `problemas-y-escalamiento.md`. Conviene enlazarlos y no repetirlos.

## 10. Huecos

1. Texto de Markus y Tanis (2000): el capítulo no se pudo abrir (PDF con 404, Cambridge solo ficha). Las definiciones literales de las fases y las tres medidas de éxito quedan por leer.
2. Lista de los 22 CSF de Somers y Nelson y su asignación por etapa: [S] solamente.
3. Soh et al. (2000), Brehm et al. (2001), Davenport (1998), Holland y Light (1999): todos [S]; no hay cita literal verificada. Los siete tipos de tailoring sin confirmar.
4. Selección: no hay guía de un organismo público con demo guionada o prueba de concepto; el método general sale de práctica de consultoras.
5. Migración de datos: ningún estudio académico hallado; solo documentación de productos y consultoras.
6. Big bang frente a fases: sin estudio comparativo robusto; los citados (Mabert 2003, Bernroider y Leseure 2005, un estudio europeo de presupuesto, una entrevista a 30 firmas) son [S] y no los leí. No confirmé el enfoque de corte de Hershey en una fuente leída.
7. FoxMeyer y Lidl: lectura directa bloqueada (403). Datos de FoxMeyer de resumen de buscador; la cifra de Lidl es de prensa sin confirmación de las partes. No hay GAO ni informe oficial hallado de Hershey.
8. Partners y agencia: sin estudios de contratos (precio fijo contra tiempo y materiales) ni auditorías públicas; falta metodología independiente (no de proveedor). Revisar informes de auditorías públicas sobre ERP (p. ej. el caso Birmingham, sin verificar).
9. Hypercare como término: solo aparece en descripción de metodología de proveedor (SAP) [S]; no hallé definición neutral.
10. Después del go-live: solo Hitt et al. leído; falta Nicolaou (2004), Gattiker y Goodhue (2005), Ross y Vitale (2000) para la recuperación posterior.
11. Standish: informe original no abierto, no leído; solo la crítica.
12. Panorama: solo leí la edición 2017 completa; el resto (2015, 2016, ediciones recientes) por buscador. Para datos más nuevos hay que abrir la última edición.
13. Argentina: no se buscó nada específico de implantación local (cae en `mercado-en-argentina.md` y la nota fiscal).
