# Informe de investigación: de la planificación a la producción (plan-to-produce)

Sesión 13 (issue #120), 2026-11-27. Ángulo: el recorrido de punta a punta que va del pronóstico y el S&OP al producto terminado ingresado, controlado y con su orden cerrada y costeada. El detalle de cada paso ya está en Producción, Cadena de suministro, Compras, Inventario y Contabilidad; este informe busca solo lo que no es de ningún dominio: el nombre del recorrido, dónde empieza, los traspasos, las fallas del recorrido entero y sus medidas.

Marcas: [L] texto completo leído; [M] metadatos o abstract; [S] resumen del buscador o de una fuente secundaria.

## 1. Fuentes

| Fuente | Tipo | Autoridad | Profundidad | Ejemplos | Unicidad | Marca |
|---|---|---|---|---|---|---|
| APQC, PCF Cross Industry 7.4 (agosto 2024), copia IFRC: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf | primaria | 3 | 2 | 1 | 3 | [L] (copia en texto del scratchpad, secciones 4.1 a 4.3 y 9.1.2) |
| APQC, Open Standards Benchmarking Measure List, Manufacturing (impreso 10/08/2012): https://www.apqc.org/sites/default/files/files/OSB/measureLists/20120812/Measures%20List%20-%20Manufacturing.pdf | primaria | 3 | 1 | 1 | 3 | [L] (2 páginas, nombres e ID; sin la fórmula de cada código) |
| APQC, medida «Production schedule attainment during a primary products planning period»: https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/production-schedule-attainment-during | primaria | 3 | 1 | 1 | 3 | [S] (403; solo el resumen del buscador) |
| APQC, medida «Primary product manufacturing cycle time in hours»: https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/primary-product-manufacturing-cycle | primaria | 3 | 1 | 1 | 3 | [S] (403) |
| APQC, End-to-End Processes: https://www.apqc.org/expertise/end-to-end-processes | primaria | 3 | 1 | 1 | 2 | [S] (403) |
| Romney y Steinbart, *Accounting Information Systems*, cap. 12 «The Production Cycle», manual del instructor (10.ª ed., según la carpeta): https://leeds-faculty.colorado.edu/marlattj/acct45405540/Solutions/romney_ais10_im/IM_CH12.DOC | secundaria del libro (manual del docente) | 2 | 2 | 1 | 3 | [L] |
| Seeling y otros (2021), PLoS ONE 16(9): e0257572 (ya leído por Cadena) | primaria | 2 | 3 | 3 | 2 | [L] por Cadena, reusado |
| Notas de dominio de Producción, Cadena, Compras, Inventario y Contabilidad (rutas abajo) | base | — | — | — | — | [L] |
| Blogs de proveedores sobre «schedule attainment» (MachineMetrics, Shoplogix, Fabrico) | secundaria de proveedor | 1 | 1 | 2 | 1 | [S]; no se usan en la nota |
| Catálogo de procesos de un proveedor de ERP que usa el nombre «plan to produce»: https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/plan-to-produce-overview | secundaria de proveedor | 1 | 1 | 1 | 2 | [S]; se usa solo para decir que el nombre circula en catálogos de producto |

## 2. El nombre y los bordes

- APQC define los procesos de punta a punta como procesos multifuncionales que reúnen todos los pasos para lograr un resultado, y los arma con piezas del PCF; su colección nombra hire-to-retire, record-to-report, order-to-cash y procure-to-pay. No se encontró un mapa de APQC llamado «plan to produce»; según el resumen del buscador, APQC registró «produce-to-ship» como pedido de sus miembros. https://www.apqc.org/expertise/end-to-end-processes [S]
- El nombre «plan to produce» aparece en el catálogo de procesos de un proveedor de ERP, con subprocesos de estrategia, planificación, operación y control de la producción. [S] Conclusión: el nombre es de la práctica de la industria del software, no de un marco neutral. La nota lo dice sin nombrar al proveedor.
- El PCF 7.4 no tiene una categoría de producción: pone el plan en 4.1 «Plan for and align supply chain resources» (que incluye 4.1.2 «Manage demand for products», 4.1.3 «Create materials plan», 4.1.4 «Create and manage master production schedule» y 4.1.8 «Develop quality standards and procedures»), la compra en 4.2 «Procure materials and services» (4.2.3 «Order materials and services») y la fabricación en 4.3 «Produce/Assemble/Test product» (4.3.1 a 4.3.4). El costo del producto es 9.1.2.4 «Perform product costing» y la variación, 9.1.2.5 «Perform variance analysis». [L]
- 4.1.2 incluye «4.1.2.1 Develop baseline demand forecasts», «4.1.2.3 Develop demand consensus forecast» y «4.1.2.7 Measure demand forecast accuracy». El S&OP no tiene nombre propio en el PCF; Cadena ya lo ubica en 4.1.2.3 (plan-de-ventas-y-operaciones.md). [L]
- Romney y Steinbart: «The production cycle is a recurring set of business activities and related data processing operations associated with the manufacture of products.» Cuatro actividades: «(1) product design; (2) planning and scheduling; (3) production operations; and (4) cost accounting.» [L, manual del instructor]
- Romney y Steinbart, traspasos con otros ciclos: «The revenue cycle provides information on customer orders and sales forecasts for use in planning production and inventory levels. The expenditure cycle provides information about raw materials acquisitions and overhead costs. The human resources/payroll cycle provides information about labor costs and availability.» Y hacia afuera: el ciclo de ingresos recibe «finished goods available for sale», el de egresos «raw materials needs», el de personal «labor needs» y el mayor «cost of goods manufactured». [L]

### Decisión: ¿empieza en el pronóstico o en el S&OP?

- A favor de empezar en el pronóstico: APQC pone la demanda (4.1.2) dentro del mismo 4.1 que el plan de materiales y el plan maestro, y mide la exactitud del pronóstico ahí (4.1.2.7) [L]. Seeling y otros ponen el plan de demanda como paso 2 de los cinco del S&OP («data gathering, demand planning, supply planning, pre-meeting, and executive meeting») [L por Cadena]. Romney y Steinbart dicen que el pronóstico llega «desde» el ciclo de ingresos, es decir, como entrada [L].
- Decisión para la nota: el recorrido empieza con el pronóstico de demanda que entra al ciclo mensual del S&OP. El pronóstico es el primer documento y su error es una medida del recorrido entero (el plan maestro, el MRP y el stock heredan el error). El disparador, en cambio, es el ciclo del S&OP: el pronóstico solo no autoriza nada. Es lectura de la base sobre las tres fuentes.
- Termina en: el producto terminado aceptado por calidad y disponible en el depósito, con la orden cerrada y su costo pasado a productos terminados y las variaciones calculadas (cierre de la orden en orden-de-produccion.md y costo-real-de-la-orden.md). La venta del terminado es de del pedido al cobro.

## 3. Documentos y traspasos (de Romney y Steinbart y de las notas de dominio)

- «Master production schedule — specifies how much of each product is to be produced during each period and when.» «Production order — authorizes production of a specified quantity of a product.» «Materials requisition — authorizes movement of materials to the factory floor.» «Move ticket — documents transfer of parts and materials through the factory.» Mano de obra: «Historically, job time tickets were used to record the time a worker spent on each job task.» [L]
- Contable: «When production is initiated, the issuance of a materials requisition triggers a debit (increase) to work in process and a credit (decrease) to raw materials inventory. Work in process is credited and raw materials are debited for any amounts returned to inventory.» [L] Coincide con la tabla de costo-real-de-la-orden.md (OpenStax 4.7).
- Datos que todo sistema necesita de la planta: «raw materials used; labor hours expended; machine operations performed; and other manufacturing overhead costs incurred.» [L]
- La cascada plan agregado → plan maestro → MRP → solicitudes de compra y órdenes planificadas → liberación está en Produccion/Planificacion-de-la-produccion/planificacion-de-la-produccion.md [L]; la liberación con sus controles (material, capacidad, lugares, lote, versión), en orden-de-produccion.md; los siete pasos de la orden, en ejecucion-en-planta.md; la entrega de material y la declaración, en consumo-y-declaracion.md; los puntos de inspección (recepción, primera pieza, en proceso, final), en plan-de-inspeccion.md; el cierre y las variaciones, en costo-real-de-la-orden.md. [L]
- Variaciones: la de precio de material «is computed at the time of purchase and not when the material is used in production» (OpenStax, citada en costo-real-de-la-orden.md). Lectura para el recorrido: la variación de precio nace en Compras y la de uso en la planta; se juntan recién al cierre del período. [L por Producción]

## 4. Dónde se traba (fallas del recorrido entero)

- Romney y Steinbart, amenaza 2 «Over- or Under-Production»; controles: «Accurate sales forecasts and inventory data; investment in production planning; collection of production performance data; proper authorization of production orders; restricted access to production scheduling programs; validity checks on production orders.» Amenaza 6 «Inaccurate Recording and Processing of Production Activity Data». [L]
- MRP con capacidad infinita y requisitos de datos («A good schedule of what is to be made / An accurate BOM / Accurate inventory records / Accurate purchases data / Lead times that will be met»): planificacion-de-la-produccion.md, con fuentes del MIT y de un solucionario. [L por Producción]
- Liberar sin material sube la producción en proceso y, por la ley de Little, el tiempo de ciclo; declarar tarde y no cerrar la orden: ejecucion-en-planta.md, «Cómo falla la ejecución» (inferencia de Producción). [L]
- Nerviosismo del MRP y barreras de tiempo: mrp.md y plan-maestro-de-produccion.md. [L por Producción]
- Efecto látigo: Cadena, efecto-latigo.md. [L por Cadena]
- Inferencias propias para la nota (marcadas como tales): el plan del S&OP por familia no cierra con la suma de los planes maestros por artículo; la solicitud de compra que propone el MRP llega a Compras con un plazo que el proveedor no cumple y la orden se libera igual; el material en cuarentena de recepción se cuenta como disponible en el MRP; la declaración de bueno antes de la inspección final mete en el disponible algo que calidad puede rechazar.

## 5. Medidas del recorrido entero

- APQC, lista de medidas de manufactura 2012 [L]: «Average production schedule attainment during a planning period for primary products» (ID 100251, PCF 10304 = 4.3.2); «Manufacturing cycle time in hours» (100854, KPI, PCF 10304); «Finished product, first pass quality yield» (100726, KPI); «Work-in-process (WIP) inventory turn rate» (104225); «Customer order cycle time in days» (100496). Las fórmulas remiten a códigos (189.0250, 189.0230) que la lista no explica.
- APQC, página de la medida de cumplimiento del programa: según el resumen del buscador, el promedio de cumplimiento del programa en un período de planificación para los productos principales, en porcentaje; la fórmula no se pudo leer (403). [S]
- APQC, tiempo de ciclo de manufactura: según el resumen, el tiempo promedio de fabricación de los productos principales, en horas, como duración del proceso «produce product» de principio a fin; APQC define el tiempo de ciclo en general como el tiempo transcurrido total del inicio al fin, incluidas las esperas. [S]
- Producción ya marcó el cumplimiento del programa como «Sin fuente todavía» (programacion-de-planta.md, sección «Cumplimiento del programa»), con una definición por inferencia. Este informe agrega el nombre y la existencia de la medida de APQC, sin la fórmula.
- Proveedores de software (MachineMetrics, Shoplogix, Fabrico): trabajo planificado terminado a tiempo sobre trabajo planificado, por turno, día o semana; algunos topean la cantidad para que la sobreproducción no pase del 100 %. [S] No se usan como autoridad.
- Tiempo de ciclo de la orden (de la liberación al final de la ruta), con la definición de Hopp y Spearman citada por Little: ejecucion-en-planta.md. [L por Producción]
- Error de pronóstico: Cadena, error-de-pronostico.md. OEE: Producción, eficiencia-global-del-equipo.md. Variaciones: costo-real-de-la-orden.md.
- Romney y Steinbart dan una medida de rendimiento de la producción: «Throughput = Productive Capacity x Productive Processing Time x Yield», con «Yield = Good Units / Total Units». [L] Es otra acepción de throughput que la de Little; no se usa en la nota para no sumar un sentido más.

## 6. Variantes

- Fabricar para stock, ensamblar, fabricar y diseñar contra pedido: fabricar-para-stock-o-contra-pedido.md (Producción) [L]. Romney y Steinbart describen la producción «lean» en que «a customer order triggers several actions»: revisa el stock, calcula la mano de obra, pide los componentes y ajusta el plan maestro. [L]
- Por procesos: receta en lugar de lista y ruta, orden por lote con merma y subproductos (orden-de-produccion.md, ruta-de-fabricacion.md, consumo-y-declaracion.md) [L]; costeo por procesos: «assigns costs to each process or work center in the production cycle and calculates the average cost for all units produced» (Romney y Steinbart) [L].
- Subcontratación: subcontratacion.md [L].

## 7. Recursos canónicos

- Para el recorrido como ciclo de transacciones: Romney y Steinbart, capítulo «The Production Cycle» (el número cambia por edición), en particular la figura de contexto con los otros ciclos y la tabla de amenazas y controles.
- Para las piezas: el PCF 7.4, 4.1 a 4.3, y 9.1.2.4 y 9.1.2.5.

## 8. Huecos

- Las fórmulas de las medidas de APQC (cumplimiento del programa y tiempo de ciclo de manufactura): las páginas dan 403 y la lista de 2012 solo trae códigos.
- Un mapa de APQC del recorrido con ese nombre: no existe o no es público.
- SCOR Make/Transform: solo la v13 de 2020 (introducción) leída por Cadena; la versión de siete procesos con Transform, solo en fuente secundaria.
- El texto del libro de Romney y Steinbart: se leyó el manual del instructor, no el capítulo.
- Una fuente para las fallas de traspaso propias del recorrido (S&OP contra plan maestro, cuarentena contada como disponible): quedan como inferencia.

## Borrador para la nota de Argentina

No hace falta apartado. El recorrido no tiene un paso propio de la Argentina: lo que el país agrega a quien fabrica (las habilitaciones sanitarias de la planta y el registro por producto en alimentos, medicamentos, productos médicos y cosméticos, la trazabilidad obligatoria ante la ANMAT, la certificación de productos eléctricos y el tratamiento de la merma y la ociosidad en la RT 54) son requisitos de la planta y del producto, y ya están en [Producción en la Argentina](../Produccion/produccion-en-argentina.md) (ruta relativa desde `Procesos-de-negocio/`). Si la nota de la Argentina quiere una línea para este recorrido, alcanza con enlazar esa nota, y para la compra de materiales, el apartado de la compra al pago.
