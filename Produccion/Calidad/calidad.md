---
resumen: >-
  La calidad, dentro de la producción, es la parte que controla que lo fabricado cumpla sus requisitos: decide qué se inspecciona y cómo, vigila que el proceso no se desvíe, aparta y resuelve lo que no cumple, ataca las causas y deja rastro de qué entró en cada lote. Es la calidad del producto fabricado; la de lo que llega del proveedor, la de la atención y la del proveedor mismo son de otros temas.
estado: borrador
estabilidad: semi
fuentes:
  - "ISO, comunicado de prensa del 16 de septiembre de 2026, lanzamiento de ISO 9001:2026: https://committee.iso.org/files/live/sites/isoorg/files/news/News_archive/2026/09/MediaRelease_9001-2026-en.pdf"
  - "ISO/TC 176, «ISO 9001:2026 has been released!» (entrada del 23 de septiembre de 2026; fechas de transición según el lector, sin verificar en el HTML): https://committee.iso.org/sites/tc176/home/news/content-left-area/news-and-updates/news.html"
  - "ISO, ficha de ISO 9001:2026 (estado y edición según el buscador; la página da 403): https://www.iso.org/standard/9001"
  - "NSAI, presentación «Overview 9001:2015» (23 de septiembre de 2015), diapositivas sobre 8.5.2, 8.6, 8.7 y 10.2: https://www.nsai.ie/download/certification/Overview-9001-2015-presentation-23-Sep-15-Web-Compatibility-Mode.pdf"
  - "Juran Institute, «More About the Juran Trilogy» (M. Goldman, 2019, actualizada en 2025): https://www.juran.com/blog/the-juran-trilogy/"
  - "Juran, J. M., «The Quality Trilogy», Quality Progress 19(8), agosto de 1986, pp. 19-24 (solo el resumen): https://asq.org/-/media/ASQ-Supplemental-Media-Import/E/F/7/9/D/7188.pdf"
  - "ASQ, «About: A. V. Feigenbaum» (según el buscador; la página da 403): https://asq.org/about-asq/honorary-members/feigenbaum"
  - "ASQ, «What is Cost of Quality (COQ)?» (según el buscador; la página da 403): https://asq.org/quality-resources/cost-of-quality"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.1.8, 4.3.3 y 4.3.4: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Produccion/.investigacion/calidad.md y calidad-2.md (2026-11-27); fundamentos-y-contraria.md, sección del PCF 4.3"
aliases: [calidad, calidad del producto, product quality, gestión de la calidad, quality management, control de calidad, quality control, QC, aseguramiento de la calidad, quality assurance, QA, sistema de gestión de la calidad, quality management system, QMS, ISO 9001, trilogía de Juran, Juran trilogy, costo de la calidad, cost of quality, COQ]
creado: 2026-11-27
revisado:
---

# Calidad

La calidad, dentro de la producción, es la parte que controla que lo fabricado cumpla sus requisitos: decide qué se inspecciona y cómo, vigila que el proceso no se desvíe, aparta y resuelve lo que no cumple, ataca las causas y deja rastro de qué entró en cada lote. Es la calidad del producto fabricado; la de lo que llega del proveedor, la de la atención y la del proveedor mismo son de otros temas.

Es la última de las cinco partes de [Producción](../produccion.md). Recibe de [Ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md) lo producido y lo rechazado, y le devuelve a [Producto y proceso](../Producto-y-proceso/producto-y-proceso.md) los [cambios de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md) que salen de una causa en el diseño. Lo que no es de acá se enlaza: la inspección de lo que llega está en [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md) y la cuarentena en [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md), de Inventario; la [evaluación de proveedores](../../Compras-y-abastecimiento/Proveedores/evaluacion-de-proveedores.md), de Compras; y la [calidad del servicio](../../Servicio-al-cliente/Calidad-del-servicio/calidad-del-servicio.md), de Servicio al cliente.

## Control, aseguramiento y gestión de la calidad

Las tres palabras nombran capas distintas, y un sistema suele mezclarlas. Como criterio de la base:

| Capa | Qué pregunta contesta | Dónde está en esta vertical |
|---|---|---|
| Control de la calidad | ¿Esta pieza, este lote, este proceso cumplen hoy? | [plan de inspección](plan-de-inspeccion.md), [control estadístico de procesos](control-estadistico-de-procesos.md), [no conformidad](no-conformidad.md) |
| Aseguramiento de la calidad | ¿Hay un sistema que haga que cumplan siempre, y se puede demostrar? | ISO 9001, más abajo; los registros de todas las notas |
| Gestión de la calidad | ¿Quién decide, cómo se planifica y cómo se mejora? | [acción correctiva](accion-correctiva.md), la trilogía de Juran |

El control mira el producto y el proceso; el aseguramiento mira el sistema que los produce.

> [!NOTE] Sin fuente todavía: las definiciones de control, aseguramiento y gestión de la calidad de ISO 9000:2015 (de pago, no se leyó). La tabla es corte de la base.

## La trilogía de Juran: planificar, controlar, mejorar

Juran presentó la trilogía en 1986, en «The Quality Trilogy» (Quality Progress), un artículo que según su resumen propone «a new direction in managing for quality». El Juran Institute la describe así: «organizations must use three universal processes: Quality Planning (Quality by Design); Quality Control (Process Control & Regulatory); Quality Improvement (Lean Six Sigma)». El artículo original no se leyó; lo que sigue sale de la página del instituto.

El diagrama pone el tiempo en el eje horizontal y el costo de la mala calidad en el vertical. El control sirve «to prevent things from getting worse»: apaga un pico esporádico «to restore the status quo». La mejora ataca otra cosa, el desperdicio crónico: «the chronic waste was an opportunity for improvement». Juran la llama avance, «the organized creation of beneficial change and the attainment of unprecedented levels of performance».

El [control estadístico de procesos](control-estadistico-de-procesos.md) y la [no conformidad](no-conformidad.md) devuelven el proceso a donde estaba; la [acción correctiva](accion-correctiva.md) que cambia la lista, la ruta o el método es lo que baja el nivel crónico (lectura de la base).

## El costo de la calidad

El costo de la calidad mide cuánto gasta una empresa en que el producto salga bien y en lo que sale mal, en cuatro categorías. La fuente es débil: lo que sigue sale del buscador, que cita páginas de ASQ que no se pudieron abrir.

| Categoría | Qué junta, según el resumen de ASQ |
|---|---|
| Prevención | lo que se gasta para evitar la mala calidad |
| Evaluación | lo que se gasta en evaluar el producto (inspeccionar, ensayar, medir) |
| Fallas internas | defectos que se detectan antes de entregar |
| Fallas externas | defectos que encuentra el cliente |

Según la biografía de ASQ, el texto de Feigenbaum fue el primero en caracterizar los costos de la calidad como costos de prevención, de evaluación y de fallas internas y externas. El mismo resultado de búsqueda recoge un debate: la teoría tradicional supone un nivel óptimo de esfuerzo que minimiza el costo total, y los defensores de la calidad total sostienen que la prevención y la evaluación cuestan menos, y las fallas más, de lo que supone ese modelo.

Los datos salen de otras partes del tema. Las fallas internas son las piezas rechazadas, reprocesadas o desechadas que registra la [no conformidad](no-conformidad.md); su costo sale de los registros de la orden ([costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md)), y adónde va lo dice [Costos de producción](../Costos-de-produccion/costos-de-produccion.md#mermas-rechazos-y-reproceso-normal-frente-a-anormal). Las fallas externas llegan como reclamo por [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md) (inferencia de la base).

> [!NOTE] Sin fuente todavía: la definición literal de las cuatro categorías (ASQ) y el texto de Feigenbaum (Total Quality Control, 1951).

## ISO 9001 como sistema de gestión

ISO 9001 es la norma de requisitos para un sistema de gestión de la calidad (su título es «Quality management systems – Requirements»). Pide que esté definido, controlado y registrado lo que afecta al producto, y deja a la empresa el cómo fabricar (lectura de la base).

La edición vigente es la de 2026. ISO anunció el 16 de septiembre de 2026 «the launch of ISO 9001:2026, Quality management systems – Requirements». Según el comité ISO/TC 176, en una entrada leída por el lector y no verificada en el HTML, la transición es así:

| Fecha | Qué pasa |
|---|---|
| 31 de marzo de 2027 | los organismos de acreditación tienen que estar listos para evaluar contra la 2026 |
| 31 de marzo de 2028 | las certificaciones nuevas solo se emiten contra la 2026 |
| 30 de septiembre de 2029 | vence el plazo para que las empresas certificadas en la 2015 completen la transición |

Según el comunicado de ISO, la edición nueva pone «greater emphasis on leadership, a culture of quality and ethical behaviour», aclara cómo considerar riesgos y oportunidades, suma una sección que explica la intención de los requisitos y adopta la estructura armonizada de las normas de sistemas de gestión.

Las cláusulas que tocan la producción se conocen solo de segunda mano. El texto de ISO 9001 es de pago y no se pudo leer ni en la edición 2015 ni en la 2026. Lo que sigue sale de una presentación de NSAI, el organismo de normalización de Irlanda, sobre la edición 2015:

| Cláusula (2015) | Qué dice NSAI | Dónde se trata |
|---|---|---|
| 8.5.2 Identificación y trazabilidad | «No new requirements» | [trazabilidad de lotes](trazabilidad-de-lotes.md) |
| 8.6 Liberación de productos y servicios | reemplaza al seguimiento y medición del producto; «No new requirements» | [plan de inspección](plan-de-inspeccion.md) |
| 8.7 Control de las salidas no conformes | no exige procedimiento documentado pero sí información documentada | [no conformidad](no-conformidad.md) |
| 10.2 No conformidad y acción correctiva | no tiene cláusula de acción preventiva | [acción correctiva](accion-correctiva.md) |

Ninguna fuente leída dice si la edición 2026 cambió la numeración o el texto de esas cláusulas. Las notas de esta vertical citan la numeración de 2015 y hay que verificarla en la 2026. Si certificar ISO 9001 mejora el desempeño es un debate que está en [fundamentos de producción](../Fundamentos/fundamentos-de-produccion.md).

> [!NOTE] Sin fuente todavía: el texto literal de ISO 9001:2015 (8.5.2, 8.6, 8.7, 10.2 y anexo A.3) y qué cambió en esas cláusulas en la edición 2026.

## Lo que APQC pone bajo «probar»

El marco de procesos de APQC (versión 7.4) reparte la calidad de la fabricación en tres procesos. Los de 4.3 son los que registra un sistema:

| Proceso APQC | Actividades | Nota |
|---|---|---|
| 4.1.8 «Develop quality standards and procedures» | fijar objetivos, procedimientos de ensayo y especificaciones; el desglose está en [marcos de la producción](../Fundamentos/marcos-de-la-produccion.md) | esta entrada; [plan de inspección](plan-de-inspeccion.md) |
| 4.3.3 «Perform quality testing» | calibrar el equipo de ensayo; ensayar según el procedimiento estándar; gestionar las muestras; registrar los resultados | [plan de inspección](plan-de-inspeccion.md) |
| 4.3.3 (sigue) | seguir y analizar las tendencias de no conformidad; analizar la causa raíz | [no conformidad](no-conformidad.md), [acción correctiva](accion-correctiva.md) |
| 4.3.4 «Maintain production records and manage lot traceability» | definir el sistema de numeración de lotes; definir el uso del lote | [trazabilidad de lotes](trazabilidad-de-lotes.md) |

En los procesos de 4.1 y 4.3 que se leyeron no aparece el control estadístico. La base lo trata aparte porque vigila el proceso y no el producto (inferencia de la base).

## Cómo falla la calidad en una fábrica

Como criterio de la base, a partir de lo que las fuentes de cada nota marcan:

- Se inspecciona y no se registra. El resultado queda en la cabeza del inspector; no hay historia para el gráfico de control ni para la tendencia de no conformidades.
- Lo rechazado no se aparta. La pieza mala vuelve a la línea o al depósito y se usa por error, que es lo que la cláusula 8.7 busca evitar, según fuentes secundarias.
- Se corrige y no se busca la causa. Se reprocesa el lote y el defecto vuelve en el siguiente. La [acción correctiva](accion-correctiva.md) se cierra sin verificar que funcionó.
- El consumo no dice qué lote usó. El día de un retiro no se sabe qué lotes fabricados llevan el componente malo: la [trazabilidad de lotes](trazabilidad-de-lotes.md) quedó rota en la [declaración de consumo](../Ejecucion-en-planta/consumo-y-declaracion.md).

## Qué hay en Calidad

- [Plan de inspección](plan-de-inspeccion.md): qué se controla, dónde, contra qué y cada cuánto, y el muestreo de aceptación por atributos con su tabla.
- [Control estadístico de procesos](control-estadistico-de-procesos.md): gráficos de control, causas por azar y asignables, reglas para leer el gráfico y capacidad del proceso (Cp y Cpk).
- [No conformidad](no-conformidad.md): registrar y apartar lo que no cumple, y decidir qué hacer con eso (reprocesar, reparar, usar como está con concesión, desechar, devolver al proveedor).
- [Acción correctiva](accion-correctiva.md): corrección, acción correctiva y preventiva, CAPA, 8D, 5 porqués, Ishikawa y la verificación de la eficacia.
- [Trazabilidad de lotes](trazabilidad-de-lotes.md): la genealogía del lote fabricado, el rastreo hacia atrás y hacia adelante y el retiro.
