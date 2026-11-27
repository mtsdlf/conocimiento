---
resumen: >-
  El plan de ventas y operaciones (S&OP) es el proceso, normalmente mensual, en que ventas, operaciones y finanzas acuerdan un único plan de demanda y de abastecimiento por familia y por período. Su salida es el plan agregado que después se baja al plan maestro de producción y al plan de distribución.
estado: borrador
estabilidad: semi
fuentes:
  - "CSCMP, Supply Chain Management Terms and Glossary (2013), entrada S&OP (copia no oficial): https://www.cisco-eagle.com/uploads/cscmp/cscmp-glossary.pdf"
  - "Seeling, Kreuter, Scavarda, Thomé y Hellingrath (2021), Global sales and operations planning: A multinational manufacturing company perspective, PLoS ONE 16(9): e0257572: https://pmc.ncbi.nlm.nih.gov/articles/PMC8454961 (según el resumen del lector; no leído entero)"
  - "Wikipedia, Sales and operations planning (secundaria): https://en.wikipedia.org/wiki/Sales_and_operations_planning"
  - "Thomé, Scavarda, Fernandez y Scavarda (2012), Sales and operations planning: A research synthesis, International Journal of Production Economics 138(1):1-13, abstract: https://ideas.repec.org/a/eee/proeco/v138y2012i1p1-13.html (según el resumen)"
  - "Tavares Thomé, Scavarda, Fernandez y Scavarda (2012), Sales and operations planning and the firm performance, IJPPM 61(4):359-381, abstract: https://doi.org/10.1108/17410401211212643 (según el resumen)"
  - "Thomé, Sousa y do Carmo (2014), Complexity as contingency in sales and operations planning, IMDS 114(5):678-695, abstract: https://doi.org/10.1108/imds-10-2013-0448 (según el resumen)"
  - "Grimson y Pyke (2007), IJLM 18(3):322-346, abstract: https://doi.org/10.1108/09574090710835093 (según el resumen)"
  - "APQC, Process Classification Framework 7.4 (2024), 4.1.2.3 «Develop demand consensus forecast»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Campos de Sales Forecast y Master Production Schedule de un ERP abierto (rama develop): https://github.com/frappe/erpnext/tree/develop/erpnext/manufacturing/doctype"
  - "Documentación de otro ERP abierto, Master production schedule (rama 19.0): https://github.com/odoo/documentation/blob/19.0/content/applications/inventory_and_mrp/manufacturing/workflows/use_mps.rst"
  - "Cadena-de-suministro-y-logistica/.investigacion/planificacion-2.md (sección 1), fundamentos-y-contraria-2.md (secciones 6.2 y 10) y fundamentos-y-contraria.md (sección 1)"
aliases: [plan de ventas y operaciones, planificación de ventas y operaciones, S&OP, sales and operations planning, S&OP planning, planificación integrada del negocio, integrated business planning, IBP, plan agregado, aggregate planning, plan agregado de producción, reunión ejecutiva de S&OP, plan de consenso]
creado: 2026-11-27
revisado:
---

# Plan de ventas y operaciones

El plan de ventas y operaciones (S&OP) es el proceso, normalmente mensual, en que ventas, operaciones y finanzas acuerdan un único plan de demanda y de abastecimiento por familia y por período. Su salida es el plan agregado que después se baja al plan maestro de producción y al plan de distribución.

El glosario del CSCMP lo define como «A strategic planning process that reconciles conflicting business objectives and plans future supply chain actions», en el que distintas áreas, «such as sales, operations and finance», acuerdan «a single plan/forecast that can be used to drive the entire business». Es el nivel de arriba de la jerarquía de [Planificación](planificacion.md): toma el [pronóstico de demanda](pronostico-de-demanda.md) y lo convierte en un compromiso.

## Una práctica, no un proceso del marco

El S&OP viene de los cuerpos de certificación y de la consultoría, no de los marcos de procesos. APQC 7.4 no tiene un proceso con ese nombre: lo más cercano es 4.1.2.3, «Develop demand consensus forecast». Una fuente secundaria atribuye el término a Richard Ling, consultor de Oliver Wight, en los años ochenta.

> [!NOTE] Sin fuente todavía: el ciclo de S&OP en un texto de referencia (Wallace, *Sales & Operations Planning: The How-To Handbook*, o Oliver Wight). Lo que sigue sale de un solo estudio de caso.

## El ciclo mensual en cinco pasos

La única fuente leída que describe el ciclo paso a paso es un estudio de caso de una multinacional manufacturera, publicado en PLoS ONE en 2021 (Seeling y otros). Ese artículo atribuye los cinco pasos a Wallace y a Stahl: «data gathering, demand planning, supply planning, pre-meeting, and executive meeting». Así corren en la empresa del caso, que lo hace «usually once a month»:

| Paso | Cuándo, en el caso | Quién | Qué sale |
|---|---|---|---|
| 1. Recolección de datos | automática y diaria; no es paso formal | el sistema | historia de ventas, stock y capacidad |
| 2. Plan de demanda | primera semana | ventas y marketing | un plan de demanda sin restricciones, agregado y por artículo |
| 3. Plan de abastecimiento | segunda semana | el director de la cadena de suministro | un plan con restricciones de capacidad y opciones para cubrir las brechas |
| 4. Reunión previa | tercera semana, no siempre formal | «representatives from different functional business areas (e.g., sales, marketing, and operations)», y finanzas | una propuesta con los dilemas sin resolver y su análisis financiero |
| 5. Reunión ejecutiva | última semana | el gerente general y los directores: «Company's senior managers and executives take part» | el plan aprobado |

En el caso, la reunión ejecutiva es el punto de decisión. Las medidas para cubrir una brecha que exceden la autoridad de los gerentes de área pueden quedar para finanzas. Todo esto describe una empresa; no es una norma.

La diferencia entre el paso 2 y el 3 es el corazón del proceso (lectura de la base). Ventas dice cuánto podría vender sin límites; operaciones dice cuánto puede hacer o conseguir. La reunión decide qué hacer con la diferencia: subir capacidad, adelantar stock, resignar ventas o cambiar precios.

## Horizonte y nivel de detalle

En el caso de PLoS ONE, el plan cubre un «18-month horizon». La revisión de la literatura de ese artículo agrega que el horizonte «is extended and tends to merge with the multi-year strategic plan». Una fuente secundaria repite los 18 meses «at the product family level (or SKU)». Es una sola cifra, de un caso: los rangos de 18 a 24 meses que circulan no tienen fuente leída.

El plan se arma por familia de productos y por mes, no por artículo y semana. Bajarlo a artículos es trabajo del plan maestro, en Producción, y de la [planificación de la distribución](planificacion-de-la-distribucion.md).

## Perseguir la demanda o nivelar

El plan agregado de producción tiene dos estrategias opuestas, según una fuente secundaria: planes «which try to chase demand» y planes que nivelan, con una producción pareja. Perseguir mueve la capacidad (turnos, horas extra, tercerizar) y deja poco stock; nivelar mantiene la capacidad y usa el stock de anticipación como colchón (lectura de la base). El stock de anticipación es una de las funciones del stock que lista [reposición](../../Inventario-y-depositos/Reposicion/reposicion.md#para-qué-se-tiene-stock).

> [!NOTE] Sin fuente todavía: las estrategias de plan agregado en un libro de texto, y la estrategia mixta, que no apareció en ninguna fuente leída.

## Frente al presupuesto y al plan maestro

| | [Presupuesto](../../Contabilidad/Contabilidad-de-gestion/presupuesto.md) | S&OP | Plan maestro de producción |
|---|---|---|---|
| Qué es | el plan en plata de toda la empresa | el plan en unidades de demanda y abastecimiento | qué artículo producir en qué semana |
| Cada cuánto | anual, con revisiones | mensual | semanal o más seguido |
| Detalle | cuentas y centros de costo | familia y mes | artículo y semana |
| Dueño | finanzas | la dirección, con ventas, operaciones y finanzas | producción |

La tabla es síntesis de la base: ninguna fuente leída define las diferencias. Lo que sí dice el caso de PLoS ONE es que el plan de S&OP «is compared to the budget with a risk analysis» antes de aprobarse, y que ventas y abastecimiento buscan cumplir el presupuesto comprometido. El presupuesto fija la meta del año; el S&OP revisa cada mes si el plan llega y qué hacer si no. Los pronósticos móviles que algunos proponen al lado del presupuesto anual están en la nota de presupuesto, de Contabilidad.

El plan maestro y el MRP son de Producción, todavía no armado. El caso de PLoS ONE no los trata más que para decir que su «production master plan» alimenta el MRP.

## Qué dice la evidencia sobre su efecto

La evidencia de que el S&OP mejora el desempeño existe, pero es parcial:

- Thomé y otros (2012, IJPE) revisaron 271 trabajos. Según su resumen, el resultado más esperado es «a cross-functional integration of plans, although few studies report on the integration of finance plans into S&OP», y falta «unifying frameworks for maturity models, measurement of S&OP, and constructs related to the firm's performance».
- Los mismos autores, en otra revisión de 2012 (IJPPM), encontraron que «relatively few of the 55 papers reviewed estimate the effect of S&OP on firm performance» y ofrecen «partial evidence of the effect of S&OP on firm performance».
- Thomé, Sousa y do Carmo (2014), con «725 manufacturing plants from 21 countries», hallaron que las prácticas de S&OP «impact positively on manufacturing operational dimensions of quality, delivery and flexibility», y más cuanto más complejo el proceso. Mide plantas y dimensiones operativas, no rentabilidad.
- Grimson y Pyke (2007) propusieron un marco de madurez de cinco etapas con 15 entrevistas; encontraron que los procesos de negocio habilitan la integración del plan, «but that information technology is not clearly so».

Resumen de la base: hay evidencia parcial de que el S&OP mejora el desempeño operativo y falta evidencia sólida sobre el resultado económico. En lo leído no hay un estudio que muestre que no mejora. El último punto importa a quien vende software: según ese estudio, la herramienta no es lo que hace funcionar el proceso.

## Lo que un sistema registra del S&OP, y lo que no

Los ERP abiertos consultados registran el pronóstico de ventas y el plan maestro, encadenados, pero no tienen un objeto para el ciclo de S&OP: ni la reunión, ni las versiones del plan, ni las decisiones. El sistema guarda el número; el acuerdo queda en planillas y actas (inferencia de la base). El plan maestro de uno de ellos es una grilla por producto y período, un nivel más abajo que el plan por familia.

Lo que haría falta para sostener el ciclo, por las salidas que nombra el caso de PLoS ONE:

- **El ciclo**, con su mes y sus fechas de paso.
- **Las versiones del plan**: demanda sin restricciones, abastecimiento con restricciones, propuesta y plan aprobado, cada una por familia y mes.
- **Las brechas** entre demanda y capacidad, con las opciones evaluadas.
- **Las decisiones** de la reunión ejecutiva, con responsable y fecha.
- **El plan aprobado contra el presupuesto** y contra lo real, mes a mes.

Las prácticas que miden los estudios («organizational management, technological integration, measurement systems and integration of plans», según Thomé, Sousa y do Carmo) sugieren además guardar las métricas de cada área.

Para leer más: el artículo de PLoS ONE (Seeling y otros, 2021), abierto, en las secciones sobre los bloques del S&OP y los pasos locales y globales; y el resumen de Thomé y otros (2012) para el estado de la evidencia.
