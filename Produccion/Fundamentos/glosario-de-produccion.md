---
resumen: >-
  Los términos del tema Producción, cada uno con su nombre en inglés, una definición corta y la nota donde vive, agrupados por la parte del dominio a la que pertenecen.
estado: vigente
estabilidad: estable
fuentes:
  - "NIC 2 Existencias, párrafo 14, en el Reglamento (CE) 1126/2008, Diario Oficial de la UE L 320, 29.11.2008: https://www.boe.es/doue/2008/320/L00001-00481.pdf"
  - "MIL-STD-1520C, «Corrective Action and Disposition System for Nonconforming Material», 27 de junio de 1986, cancelada (PDF escaneado con OCR), 3.5 a 3.15, 4.5 y 5.2 a 5.4: https://everyspec.com/MIL-STD/MIL-STD-1500-1599/download.php?spec=MIL_STD_1520C.1489.pdf"
  - "ANSI/ISA-95.00.03-2013, vista previa (introducción, alcance, definiciones y cambios de nombres): https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf"
  - "APQC, Process Classification Framework, Cross Industry, versión 7.4 (2024), procesos 4.1 y 4.3: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Produccion/.investigacion/ (informes del 2026-11-27)"
aliases: [glosario de producción, glosario de fabricación, manufacturing glossary, production glossary, términos de producción, vocabulario de producción, vocabulario de fabricación]
creado: 2026-11-27
revisado: 2026-11-27
---

# Glosario de producción

Los términos del tema Producción, cada uno con su nombre en inglés, una definición corta y la nota donde vive, agrupados por la parte del dominio a la que pertenecen.

El campo tiene un diccionario de referencia, el de ASCM (ex APICS), que esta base no leyó salvo en citas de segunda mano; los sistemas, además, usan nombres distintos para lo mismo. Estas son las palabras que usa la base, en un sentido cada una. La definición completa y sus fuentes están en la nota de la columna «Dónde»; el contexto del campo, en [fundamentos de producción](fundamentos-de-produccion.md).

Seis palabras se usan en el campo con más de un sentido, y acá figuran una vez por sentido, con la aclaración entre paréntesis: capacidad, eficiencia, utilización, rendimiento, tiempo de ciclo y lote.

## El dominio entero

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Producción | Production, manufacturing | Lo que una empresa registra y decide para transformar materiales en productos | [Producción](../produccion.md) |
| Planificación y control de la producción | Production planning and control, PCP | El nombre clásico del dominio: planificar la fabricación y seguirla en la planta | [Producción](../produccion.md) |
| ERP | Enterprise resource planning | El sistema de gestión de la empresa; en ISA-95, el nivel 4, donde se planifica | [marcos de la producción](marcos-de-la-produccion.md#isa-95-cinco-niveles-y-la-frontera-entre-erp-y-mes) |
| MES | Manufacturing execution system | El sistema de ejecución de planta; en ISA-95, el nivel 3 | [ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md#la-frontera-entre-el-erp-y-el-mes) |
| Fabricación discreta | Discrete manufacturing | La de piezas que se cuentan por unidad y se ensamblan; usa lista de materiales y ruta | [producto y proceso](../Producto-y-proceso/producto-y-proceso.md#discreta-o-por-procesos-lista-y-ruta-o-fórmula) |
| Fabricación por procesos | Process manufacturing | La de química, alimentos y bebidas, que se cuenta en kilos, litros o lotes; usa fórmula o receta | [producto y proceso](../Producto-y-proceso/producto-y-proceso.md#discreta-o-por-procesos-lista-y-ruta-o-fórmula) |

## Producto y proceso

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Datos maestros de fabricación | Manufacturing master data | La lista de materiales y la ruta: cómo debería hacerse cada producto | [producto y proceso](../Producto-y-proceso/producto-y-proceso.md) |
| Lista de materiales | Bill of materials, BOM | Qué componentes, y en qué cantidad, hacen falta para fabricar una cantidad base de un producto | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) |
| Cantidad base | Base quantity | La cantidad de producto a la que se refieren las cantidades de la lista | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) |
| Lista explotada | Indented BOM, exploded BOM | La suma de todos los niveles y ramas del árbol del producto | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) |
| Merma del componente | Scrap factor | El porcentaje de más que se consume de un componente respecto de lo que queda en el producto; es la merma normal que entra en el estándar | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md#merma-del-componente-y-rendimiento-de-la-salida) |
| Rendimiento (de la salida) | Yield | Cuánto producto sale de lo que entra, frente a lo teórico | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md#merma-del-componente-y-rendimiento-de-la-salida) |
| Lista fantasma | Phantom BOM, blow-through | El subconjunto que se arma en la línea y entra enseguida en el producto de arriba, sin pasar por el depósito | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md#lista-fantasma-el-subconjunto-que-no-se-guarda) |
| Lista de planificación | Planning BOM | La lista que no describe un armado y sirve para calcular, con porcentajes por opción | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md#lista-de-planificación-modular-y-variantes) |
| Lista de ingeniería y lista de fabricación | EBOM, MBOM | La estructura por módulos de diseño frente a la que usa la planta | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md#lista-de-ingeniería-y-lista-de-fabricación) |
| Código de nivel más bajo | Low-level code | El nivel más profundo en que aparece un artículo en todas las listas; ordena el cálculo del MRP y del costo | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md#código-de-nivel-más-bajo) |
| Coproducto | Co-product, joint product | Una salida de valor comparable a la principal, que se lleva una parte del costo (sentido de la NIC 2) | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#subproducto-y-coproducto-la-norma-contable-y-un-glosario-no-coinciden) |
| Subproducto | By-product | Una salida secundaria de poco valor, que se mide por lo que se obtiene al venderla (sentido de la NIC 2) | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#subproducto-y-coproducto-la-norma-contable-y-un-glosario-no-coinciden) |
| Ruta de fabricación | Routing | La secuencia de operaciones por la que pasa un producto, con el centro de trabajo y los tiempos de cada una | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md) |
| Operación | Operation | Un paso de la ruta, con su centro de trabajo, su tiempo y su tamaño de lote | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#operaciones-en-secuencia) |
| Centro de trabajo | Work center, workstation | El recurso donde se hace una operación: una máquina, un grupo de máquinas, una línea o un puesto | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#el-centro-de-trabajo-dónde-se-hace-y-cuánto-puede) |
| Tiempo de preparación | Setup time | Lo que lleva dejar la máquina lista para un artículo, sea cual sea la cantidad | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#los-cuatro-tiempos-de-una-operación) |
| Tiempo de ejecución | Run time | El tiempo de corrida por unidad, que se multiplica por la cantidad | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#los-cuatro-tiempos-de-una-operación) |
| Tiempo de cola | Queue time | Lo que espera un trabajo en el centro antes de que lo preparen | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#los-cuatro-tiempos-de-una-operación) |
| Tiempo de movimiento | Move time | Lo que tarda el trabajo en pasar de una operación a la siguiente | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#los-cuatro-tiempos-de-una-operación) |
| Plazo de fabricación | Manufacturing lead time | Los días que lleva completar un producto desde sus componentes más bajos, con lo comprado ya en casa | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#los-cuatro-tiempos-de-una-operación) |
| Capacidad (de la ficha del centro) | Capacity | En los sistemas abiertos leídos, cuántos trabajos puede hacer el centro a la vez | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#el-centro-de-trabajo-dónde-se-hace-y-cuánto-puede) |
| Eficiencia (multiplicador) | Time efficiency | Parámetro del centro: cuánto más rápido o más lento trabaja que el tiempo escrito en la ruta | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#eficiencia-y-utilización-dos-acepciones-de-eficiencia) |
| Eficiencia (medida) | Efficiency | Horas estándar sobre horas trabajadas; una sola fuente, de baja confianza | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#eficiencia-y-utilización-dos-acepciones-de-eficiencia) |
| Utilización (del centro) | Utilization | Horas trabajadas sobre horas disponibles | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#eficiencia-y-utilización-dos-acepciones-de-eficiencia) |
| Capacidad nominal | Rated capacity | Tiempo disponible por utilización por eficiencia; una sola fuente, de baja confianza | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#eficiencia-y-utilización-dos-acepciones-de-eficiencia) |
| Fórmula, receta | Formula, recipe | En la fabricación por procesos, el documento que junta insumos, parámetros, salidas y procedimiento | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#fórmula-o-receta-en-la-fabricación-por-procesos) |
| Receta de control | Control recipe | La copia de la receta que se usa para un lote | [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#fórmula-o-receta-en-la-fabricación-por-procesos) |
| Cambio de ingeniería | Engineering change | La modificación controlada de la lista o la ruta, con aprobación, vigencia y decisión sobre lo que queda de la versión anterior | [cambios de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md) |
| Solicitud de cambio | Engineering change request, ECR | El pedido de un cambio, antes de que se decida | [cambios de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md#solicitud-y-orden-de-cambio) |
| Orden de cambio | Engineering change order, ECO; engineering change notice, ECN | El documento que autoriza el cambio y dice cómo implementarlo | [cambios de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md#solicitud-y-orden-de-cambio) |
| Versión | Revision, version | Cada estado de la lista o la ruta; un cambio crea una nueva y hay una sola activa por período | [cambios de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md#revisión-versión-y-una-sola-versión-activa) |
| Vigencia | Effectivity | Desde cuándo vale un cambio: por fecha, por número de serie o al agotar el stock | [cambios de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md#vigencia-por-fecha-por-número-de-serie-o-al-agotar) |
| Gestión de la configuración | Configuration management | La disciplina de la que viene el control de cambios; la ordena la ISO 10007 | [cambios de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md#de-dónde-viene-la-gestión-de-la-configuración) |

## Planificación de la producción

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Plan agregado | Aggregate plan, S&OP | Cuánto producir por familia y por mes; es de Cadena de suministro | [planificación de la producción](../Planificacion-de-la-produccion/planificacion-de-la-produccion.md#dónde-empieza-el-plan-agregado-es-de-cadena) |
| Punto de desacople del pedido | Customer order decoupling point, CODP; order penetration point | El punto de la fabricación en que el producto pasa a ser de un cliente: antes manda el pronóstico y después, el pedido | [fabricar para stock o contra pedido](../Planificacion-de-la-produccion/fabricar-para-stock-o-contra-pedido.md#el-punto-de-desacople-según-sharman) |
| Fabricar para stock | Make to stock, MTS | Fabricar contra pronóstico y vender del depósito de terminados | [fabricar para stock o contra pedido](../Planificacion-de-la-produccion/fabricar-para-stock-o-contra-pedido.md#las-cinco-posiciones) |
| Ensamblar contra pedido | Assemble to order, ATO | Tener componentes y subconjuntos, y hacer el armado final con las opciones del cliente | [fabricar para stock o contra pedido](../Planificacion-de-la-produccion/fabricar-para-stock-o-contra-pedido.md#las-cinco-posiciones) |
| Fabricar contra pedido | Make to order, MTO | Fabricar un diseño estándar recién cuando llega el pedido | [fabricar para stock o contra pedido](../Planificacion-de-la-produccion/fabricar-para-stock-o-contra-pedido.md#las-cinco-posiciones) |
| Comprar y fabricar contra pedido | Purchase and make to order, PMTO | Comprar los materiales y fabricar después del pedido; sin definición leída | [fabricar para stock o contra pedido](../Planificacion-de-la-produccion/fabricar-para-stock-o-contra-pedido.md#las-cinco-posiciones) |
| Diseñar contra pedido | Engineer to order, ETO | Diseñar, comprar y fabricar para cada cliente | [fabricar para stock o contra pedido](../Planificacion-de-la-produccion/fabricar-para-stock-o-contra-pedido.md#las-cinco-posiciones) |
| Plan maestro de producción | Master production schedule, MPS | Cuánto se va a fabricar de cada artículo final, o de cada módulo, en cada período | [plan maestro de producción](../Planificacion-de-la-produccion/plan-maestro-de-produccion.md) |
| Programador maestro | Master scheduler | El dueño del plan maestro, que aprueba los cambios cerca de la fecha | [planificación de la producción](../Planificacion-de-la-produccion/planificacion-de-la-produccion.md#quién-planifica-qué) |
| Período | Time bucket | Cada columna del plan: un día, una semana o lo que convenga | [plan maestro de producción](../Planificacion-de-la-produccion/plan-maestro-de-produccion.md#una-grilla-por-artículo-y-período) |
| Barrera de tiempo | Time fence | El límite, en días desde hoy, que divide el horizonte en tramos con reglas distintas para cambiar el plan: de demanda, de planificación y de liberación | [plan maestro de producción](../Planificacion-de-la-produccion/plan-maestro-de-produccion.md#barreras-y-zonas-de-tiempo) |
| Zona congelada, semicongelada y abierta | Frozen, slushy, liquid zone | Los tramos que dejan las barreras, según quién autoriza un cambio; el esquema de tres zonas no tiene fuente primaria leída | [plan maestro de producción](../Planificacion-de-la-produccion/plan-maestro-de-produccion.md#barreras-y-zonas-de-tiempo) |
| Consumo del pronóstico | Forecast consumption | Los pedidos que llegan descuentan del pronóstico en lugar de sumarse a él | [plan maestro de producción](../Planificacion-de-la-produccion/plan-maestro-de-produccion.md#el-pedido-consume-el-pronóstico) |
| Disponible para prometer | Available to promise, ATP | La parte del stock y de la producción planificada que no está comprometida con pedidos | [plan maestro de producción](../Planificacion-de-la-produccion/plan-maestro-de-produccion.md#el-disponible-para-prometer-del-plan-maestro) |
| Capaz de prometer | Capable to promise, CTP | Prometer mirando también la capacidad, cuando el stock no alcanza | [fabricar para stock o contra pedido](../Planificacion-de-la-produccion/fabricar-para-stock-o-contra-pedido.md#qué-se-le-promete-al-cliente) |
| Programa de ensamble final | Final assembly schedule, FAS | El programa de productos terminados para pedidos concretos, cuando el plan maestro es de módulos | [plan maestro de producción](../Planificacion-de-la-produccion/plan-maestro-de-produccion.md#el-programa-de-ensamble-final) |
| MRP | Material requirements planning | El cálculo, período por período, de cuánto hace falta de cada componente y cuándo lanzar su orden | [MRP](../Planificacion-de-la-produccion/mrp.md) |
| Demanda dependiente | Dependent demand | La de componentes y materias primas, que no se pronostica: se calcula desde el plan del producto que los usa | [MRP](../Planificacion-de-la-produccion/mrp.md#demanda-dependiente-por-qué-no-alcanza-el-punto-de-pedido) |
| Necesidades brutas y netas | Gross and net requirements | Lo que pide el plan y lo que falta después de restar el stock proyectado y lo que ya viene | [MRP](../Planificacion-de-la-produccion/mrp.md#el-neteo-lo-que-falta-después-de-usar-lo-que-hay) |
| Recepción programada | Scheduled receipt | Una orden abierta que todavía no llegó | [MRP](../Planificacion-de-la-produccion/mrp.md#el-neteo-lo-que-falta-después-de-usar-lo-que-hay) |
| Explosión | Explosion | Pasar los lanzamientos de un nivel a necesidades del nivel de abajo, por la lista de materiales | [MRP](../Planificacion-de-la-produccion/mrp.md#explosión-y-desfase-de-un-nivel-al-de-abajo) |
| Desfase | Offsetting | Correr cada orden hacia atrás por su plazo | [MRP](../Planificacion-de-la-produccion/mrp.md#explosión-y-desfase-de-un-nivel-al-de-abajo) |
| Plazo | Lead time | El tiempo fijo por artículo con que el MRP calcula cuándo lanzar | [MRP](../Planificacion-de-la-produccion/mrp.md#explosión-y-desfase-de-un-nivel-al-de-abajo) |
| Lotificación | Lot sizing | La regla que dice cuánto pedir de una vez: lote por lote, cantidad fija, período fijo, cantidad por período | [MRP](../Planificacion-de-la-produccion/mrp.md#lotificación-cuánto-pedir-de-una-vez) |
| Lote (tamaño de lote) | Lot size | La cantidad que se pide o se procesa de una vez | [MRP](../Planificacion-de-la-produccion/mrp.md#lotificación-cuánto-pedir-de-una-vez) |
| Plazo de seguridad | Safety lead time | Los días que se adelanta una orden para cubrir la incertidumbre en los tiempos | [MRP](../Planificacion-de-la-produccion/mrp.md#stock-y-plazo-de-seguridad-dentro-del-plan) |
| Orden planificada | Planned order | La propuesta del MRP, que cada corrida puede cambiar | [MRP](../Planificacion-de-la-produccion/mrp.md#órdenes-planificadas-firmes-y-mensajes-de-acción) |
| Orden firme | Firm planned order | La orden planificada que el planificador fija para que el cálculo no la mueva | [MRP](../Planificacion-de-la-produccion/mrp.md#órdenes-planificadas-firmes-y-mensajes-de-acción) |
| Mensaje de acción | Action message, exception message | La sugerencia del MRP sobre una orden que ya existe: liberar, reprogramar o avisar que está demorada | [MRP](../Planificacion-de-la-produccion/mrp.md#órdenes-planificadas-firmes-y-mensajes-de-acción) |
| Rastreo de la demanda | Pegging | El vínculo de cada orden planificada con la demanda que la originó | [MRP](../Planificacion-de-la-produccion/mrp.md#rastreo-de-la-demanda) |
| Regenerativo, de cambio neto | Regenerative, net change | Rehacer todo el plan desde el plan maestro, o recalcular solo lo que cambió | [MRP](../Planificacion-de-la-produccion/mrp.md#regenerativo-o-de-cambio-neto) |
| Nerviosismo | Nervousness | Los cambios grandes del plan por desvíos chicos, de una corrida a la otra | [MRP](../Planificacion-de-la-produccion/mrp.md#por-qué-el-mrp-es-nervioso) |
| Planificación de capacidad | Capacity planning | Comparar las horas que pide el plan con las que tiene la planta, en cada nivel de la cascada | [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md) |
| Capacidad (de la planificación) | Capacity | Horas o piezas por período que puede dar un centro de trabajo | [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md) |
| Capacidad gruesa | Rough-cut capacity planning, RCCP | El control rápido del plan maestro contra unos pocos recursos críticos | [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md#capacidad-gruesa-el-plan-maestro-contra-los-recursos-críticos) |
| Lista de recursos | Bill of resources | Las horas que lleva una unidad de producto final en cada recurso crítico, sumados sus componentes | [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md#capacidad-gruesa-el-plan-maestro-contra-los-recursos-críticos) |
| Requerimientos de capacidad | Capacity requirements planning, CRP | El control de las órdenes del MRP contra cada centro de trabajo | [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md#requerimientos-de-capacidad-las-órdenes-contra-cada-centro) |
| Carga infinita y carga finita | Infinite and finite loading | Poner el trabajo en la fecha que pide el plan, entre o no, o correrlo hasta donde haya capacidad | [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md#carga-infinita-y-carga-finita) |
| MRP de lazo cerrado | Closed-loop MRP | El MRP con controles de capacidad que devuelven el plan hacia arriba | [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md#del-mrp-de-lazo-cerrado-al-mrp-ii) |
| MRP II | Manufacturing resource planning | El MRP de lazo cerrado más otras funciones de la empresa (pedidos, facturación, compras, depósito) | [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md#del-mrp-de-lazo-cerrado-al-mrp-ii) |

## Ejecución en planta

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Ejecución en planta | Shop floor control, production activity control | Convertir una orden liberada en producto terminado: programar, entregar material, registrar y medir | [ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md) |
| Orden de producción | Production order, manufacturing order, work order; Job Order en ISA-95 | El documento que autoriza fabricar una cantidad de un artículo para una fecha, y junta lo planificado con lo real | [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) |
| Estados de la orden | Order status | Planificada y firme, de la planificación; liberada, en curso, terminada y cerrada, de la planta; detenida y anulada, en cualquier momento antes del cierre | [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md#los-estados-en-dos-sistemas-abiertos) |
| Liberar | Release | Pasar la orden a la planta, comprometiendo material y capacidad | [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md#qué-se-controla-al-liberarla) |
| Terminar y cerrar | Complete, close | Terminar es que la producción acabó; cerrar es congelar la orden para que su stock y su costo queden firmes | [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md#qué-se-registra-al-cerrarla) |
| Hoja de operación, tarjeta de trabajo | Job card | El registro de lo que pasó en cada operación de la orden: tiempos, cantidad y quién la hizo | [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md#la-hoja-de-cada-operación) |
| Entrega de material a la orden | Material issue | Sacar los componentes del depósito hacia la orden antes de producir | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#entregar-el-material-a-la-orden) |
| Consumo automático | Backflush | Descontar los componentes después, explotando la lista por la cantidad producida | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#el-consumo-automático) |
| Declaración de producción | Production reporting, production confirmation | Decir cuánto salió, de qué calidad y en qué lote; en papel, el parte de producción | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#la-declaración-de-producción) |
| Merma | Scrap, process loss | La cantidad de material o de producto que se pierde en el proceso y no sale como pieza | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#la-declaración-de-producción) |
| Rechazo | Reject | La pieza que salió y no cumple; se aparta y abre una no conformidad | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#la-declaración-de-producción) |
| Desecho | Scrap | Lo que se da de baja físicamente: el sobrante de la merma o las piezas que se dispuso desechar; puede tener valor de recupero | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#la-declaración-de-producción) |
| Producción en proceso | Work in process, WIP | Lo que está entre el principio y el final de una ruta; en el costo, la suma de las órdenes abiertas | [ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md#la-ley-de-little-ordena-la-planta) |
| Ritmo de salida | Throughput | La salida promedio de un proceso por unidad de tiempo | [ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md#la-ley-de-little-ordena-la-planta) |
| Tiempo de ciclo (de la orden) | Cycle time | Lo que tarda un trabajo desde la liberación hasta el final de su ruta | [ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md#la-ley-de-little-ordena-la-planta) |
| Ley de Little | Little's law | La identidad que liga los tres: producción en proceso igual a ritmo de salida por tiempo de ciclo; vale exacta sobre un intervalo observado | [ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md#la-ley-de-little-ordena-la-planta) |
| Programación de planta | Production scheduling, shop floor scheduling | Decidir en qué orden y en qué momento pasa cada orden por cada centro de trabajo | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md) |
| Programa detallado | Detailed production schedule; Work Schedule en ISA-95 | La salida de la programación: cada operación con su centro, su día y su lugar en la cola | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md) |
| Lista de despacho | Dispatch list; Job List en ISA-95 | La cola ordenada de trabajos de un centro de trabajo | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md) |
| Regla de despacho | Dispatching rule | El criterio que ordena la cola: primero en llegar (FCFS), menor tiempo de proceso (SPT), fecha de entrega más temprana (EDD), razón crítica | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md#cuatro-reglas-de-despacho) |
| Programar hacia adelante o hacia atrás | Forward, backward scheduling | Partir de cuando hay recursos para saber la fecha de entrega, o de la entrega para saber cuándo empezar | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md#hacia-adelante-o-hacia-atrás) |
| Cuello de botella | Bottleneck | El centro con menos capacidad de largo plazo, que marca el ritmo de la línea | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md#el-cuello-de-botella-marca-el-ritmo) |
| Tambor-amortiguador-cuerda | Drum-buffer-rope, DBR | El programa de la teoría de las restricciones: la restricción marca el paso, el material se libera a su ritmo y un amortiguador de tiempo la protege | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md#los-cinco-pasos-y-tambor-amortiguador-cuerda) |
| Kanban | Kanban | La señal, por lo general una tarjeta, con que el consumo de un proceso ordena la reposición al anterior | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md#kanban-que-el-consumo-dispare-la-producción) |
| Nivelación | Heijunka, production leveling | Mantener un volumen promedio de producción mezclando modelos | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md#kanban-que-el-consumo-dispare-la-producción) |
| Subcontratación | Subcontracting, outside processing | Mandarle material propio a un tercero para que haga una o más operaciones y lo devuelva transformado; fasón | [subcontratación](../Ejecucion-en-planta/subcontratacion.md) |
| Material en poder de terceros | Stock at subcontractor | El material propio que está en el taller del proveedor, que sigue siendo stock de la empresa | [subcontratación](../Ejecucion-en-planta/subcontratacion.md#el-material-en-poder-del-tercero) |
| Eficiencia global del equipo | Overall equipment effectiveness, OEE | Qué parte del tiempo planificado un equipo produjo piezas buenas a la velocidad ideal: disponibilidad por rendimiento por calidad | [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md) |
| Disponibilidad (factor de la OEE) | Availability | Tiempo en marcha sobre tiempo planificado | [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md#los-tres-factores) |
| Rendimiento (factor de la OEE) | Performance | La velocidad real frente a la ideal mientras el equipo anda | [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md#los-tres-factores) |
| Calidad (factor de la OEE) | Quality | Piezas buenas sobre piezas producidas | [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md#los-tres-factores) |
| Tiempo ideal de ciclo | Ideal cycle time | El tiempo por pieza más rápido que el proceso puede lograr | [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md#los-tres-factores) |
| Seis grandes pérdidas | Six big losses | Las dos pérdidas que agrupa cada factor de la OEE | [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md#las-seis-grandes-pérdidas) |
| TEEP | Total effective equipment performance | La OEE sobre todo el calendario: OEE por utilización | [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md#teep-la-oee-sobre-todo-el-calendario) |
| Utilización (de la TEEP) | Utilization, loading | Tiempo planificado sobre todo el tiempo del calendario | [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md#teep-la-oee-sobre-todo-el-calendario) |

## Costos de producción

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Costo estándar del producto | Standard cost | Lo que debería costar una unidad, sumando nivel por nivel el material de la lista y la conversión de la ruta | [costo estándar del producto](../Costos-de-produccion/costo-estandar-del-producto.md) |
| Acumulación de costos | Cost roll-up | El cálculo del costo desde el componente más bajo de la lista hacia el producto final | [costo estándar del producto](../Costos-de-produccion/costo-estandar-del-producto.md#nivel-por-nivel-de-abajo-hacia-arriba) |
| Tasa del centro de trabajo | Work center rate | Lo que cuesta una hora de máquina, de mano de obra y de carga fabril en un centro; el costo por hora de su ficha | [costo estándar del producto](../Costos-de-produccion/costo-estandar-del-producto.md#cada-renglón-cantidad-de-la-lista-o-de-la-ruta-por-un-precio) |
| Carga fabril | Factory overhead | Los costos de fabricación que no se atribuyen directo a una orden y se le aplican con una tasa | [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md#lo-que-se-le-carga-a-la-orden) |
| Costo real de la orden | Actual cost, job cost | El material consumido, las horas trabajadas y la carga fabril aplicada de una orden | [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md) |
| Hoja de costos | Job cost sheet | El registro de los costos de cada orden | [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md#lo-que-se-le-carga-a-la-orden) |
| Carga fabril sobreaplicada o subaplicada | Over- or under-applied overhead | La diferencia entre la carga fabril real del período y la aplicada a las órdenes | [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md#el-cierre-y-el-pase-a-terminado) |
| Variación | Variance | La diferencia entre lo real y el estándar para lo producido; Contabilidad la llama desvío | [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md#las-variaciones-de-la-orden-y-las-del-período) |
| Variación de uso | Usage variance | Cantidad real menos cantidad estándar de material, por el precio estándar | [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md#las-variaciones-de-la-orden-y-las-del-período) |
| Variación de eficiencia | Efficiency variance | Horas reales menos horas estándar, por la tarifa o la tasa estándar | [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md#las-variaciones-de-la-orden-y-las-del-período) |
| Variación de volumen | Volume variance | La carga fija que no se absorbe por producir menos que la capacidad normal; es del período | [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md#las-variaciones-de-la-orden-y-las-del-período) |
| Merma normal y anormal | Normal and abnormal spoilage | La pérdida esperada, que va al costo del producto, frente a la que la supera, que va a resultados del período | [costos de producción](../Costos-de-produccion/costos-de-produccion.md#mermas-rechazos-y-reproceso-normal-frente-a-anormal) |
| Nivel de actividad normal | Normal capacity | La producción que se espera alcanzar como promedio de varios períodos; base para absorber la carga fija | [costos de producción](../Costos-de-produccion/costos-de-produccion.md#mermas-rechazos-y-reproceso-normal-frente-a-anormal) |
| Ociosidad | Idle capacity | La carga fija que no se aprovecha por producir bajo el nivel de actividad normal; queda fuera del costo del producto | [costos de producción](../Costos-de-produccion/costos-de-produccion.md#mermas-rechazos-y-reproceso-normal-frente-a-anormal) |

## Calidad

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Control de la calidad | Quality control, QC | Verificar que una pieza, un lote o un proceso cumplen hoy | [calidad](../Calidad/calidad.md#control-aseguramiento-y-gestión-de-la-calidad) |
| Aseguramiento de la calidad | Quality assurance, QA | El sistema que hace que cumplan siempre, y que se pueda demostrar | [calidad](../Calidad/calidad.md#control-aseguramiento-y-gestión-de-la-calidad) |
| Gestión de la calidad | Quality management | Quién decide, cómo se planifica y cómo se mejora | [calidad](../Calidad/calidad.md#control-aseguramiento-y-gestión-de-la-calidad) |
| Trilogía de Juran | Juran trilogy | Planificar, controlar y mejorar la calidad como tres procesos | [calidad](../Calidad/calidad.md#la-trilogía-de-juran-planificar-controlar-mejorar) |
| Costo de la calidad | Cost of quality, COQ | Lo que se gasta en prevención, evaluación, fallas internas y fallas externas | [calidad](../Calidad/calidad.md#el-costo-de-la-calidad) |
| Plan de inspección | Inspection plan, control plan | Qué características se controlan, en qué punto, contra qué especificación, con qué método y cada cuánto | [plan de inspección](../Calidad/plan-de-inspeccion.md) |
| Primera pieza | First article inspection | El control de la primera unidad después de preparar la máquina, antes de seguir con el lote | [plan de inspección](../Calidad/plan-de-inspeccion.md#los-cuatro-puntos-donde-se-controla) |
| Variable y atributo | Variable, attribute | La característica que se mide con un número y la que cumple o no cumple | [plan de inspección](../Calidad/plan-de-inspeccion.md#qué-dice-cada-línea-del-plan) |
| Muestreo de aceptación | Acceptance sampling | Decidir si un lote entero se acepta o se rechaza mirando una muestra | [plan de inspección](../Calidad/plan-de-inspeccion.md#el-muestreo-de-aceptación-por-atributos) |
| AQL | Acceptable quality level; acceptance quality limit | El límite de un promedio de proceso satisfactorio para el muestreo; propiedad de la serie de lotes, no de un lote | [plan de inspección](../Calidad/plan-de-inspeccion.md#el-aql-no-es-un-permiso-para-entregar-defectos) |
| Reglas de cambio | Switching rules | Las que pasan la inspección de normal a rigurosa o a reducida según cómo vienen los lotes | [plan de inspección](../Calidad/plan-de-inspeccion.md#las-reglas-de-cambio) |
| Control estadístico de procesos | Statistical process control, SPC | Vigilar un proceso con mediciones en el tiempo para separar su variación propia de la que tiene causa | [control estadístico de procesos](../Calidad/control-estadistico-de-procesos.md) |
| Gráfico de control | Control chart | El gráfico de un estadístico en el tiempo, con línea central y límites de control | [control estadístico de procesos](../Calidad/control-estadistico-de-procesos.md#los-límites-de-control-no-son-la-especificación) |
| Causa por azar y causa asignable | Chance cause, assignable cause | La variación propia del proceso y la que tiene una causa que se puede encontrar; Deming las llama común y especial | [control estadístico de procesos](../Calidad/control-estadistico-de-procesos.md#causas-por-azar-y-causas-asignables) |
| Límites de control | Control limits | Los límites que salen de los datos del proceso; no son la especificación | [control estadístico de procesos](../Calidad/control-estadistico-de-procesos.md#los-límites-de-control-no-son-la-especificación) |
| Capacidad del proceso | Process capability, Cp, Cpk | El ancho natural del proceso comparado con el que permite la especificación; no es la capacidad de la planificación | [control estadístico de procesos](../Calidad/control-estadistico-de-procesos.md#la-capacidad-del-proceso-cp-y-cpk) |
| No conformidad | Nonconformity, nonconformance | El incumplimiento de un requisito especificado por una característica del producto | [no conformidad](../Calidad/no-conformidad.md) |
| Disposición | Disposition | La decisión sobre el material no conforme: reprocesar, reparar, usar como está, desechar o devolver al proveedor | [no conformidad](../Calidad/no-conformidad.md#las-disposiciones-posibles) |
| Reprocesar (reproceso) | Rework | Eliminar por completo la no conformidad: queda una pieza conforme | [no conformidad](../Calidad/no-conformidad.md#las-disposiciones-posibles) |
| Reparar | Repair | Reducir la no conformidad sin eliminarla: la pieza queda usable, pero sin cumplir del todo | [no conformidad](../Calidad/no-conformidad.md#las-disposiciones-posibles) |
| Usar como está | Use as is | Aceptar la pieza tal cual, con autorización | [no conformidad](../Calidad/no-conformidad.md#las-disposiciones-posibles) |
| Desechar | Scrap | Dar de baja lo que no sirve para su uso y no conviene reprocesar ni reparar | [no conformidad](../Calidad/no-conformidad.md#las-disposiciones-posibles) |
| Concesión | Concession | En ISO 9001, la autorización para aceptar algo que no cumple | [no conformidad](../Calidad/no-conformidad.md#la-concesión-en-iso-9001) |
| Comité de revisión de material | Material review board, MRB | El grupo que decide la disposición de lo que la revisión preliminar no puede resolver sola | [no conformidad](../Calidad/no-conformidad.md#quién-decide-revisión-preliminar-y-comité) |
| Contención | Containment | Apartar lo afectado para que no siga camino mientras se decide | [no conformidad](../Calidad/no-conformidad.md#registrar-y-apartar-antes-de-decidir) |
| Corrección | Correction | Arreglar lo que ya salió mal | [acción correctiva](../Calidad/accion-correctiva.md#corrección-acción-correctiva-y-acción-preventiva) |
| Acción correctiva | Corrective action | Eliminar la causa de una no conformidad para que no se repita | [acción correctiva](../Calidad/accion-correctiva.md) |
| Acción preventiva | Preventive action | Eliminar la causa de un problema que todavía no pasó; ISO 9001:2015 no le dedica una cláusula | [acción correctiva](../Calidad/accion-correctiva.md#corrección-acción-correctiva-y-acción-preventiva) |
| CAPA | Corrective and preventive action | El nombre del proceso en la regulación de dispositivos médicos de los Estados Unidos | [acción correctiva](../Calidad/accion-correctiva.md#capa-el-patrón-de-los-dispositivos-médicos) |
| Causa raíz | Root cause | La causa sobre la que hay que actuar para que el problema no vuelva | [acción correctiva](../Calidad/accion-correctiva.md) |
| 8D | Eight disciplines | El método de ocho pasos para resolver un problema en equipo, con contención, causa raíz y punto de escape | [acción correctiva](../Calidad/accion-correctiva.md#el-8d-ocho-disciplinas-para-un-problema) |
| Punto de escape | Escape point | Por qué el defecto pasó sin que la inspección lo detectara | [acción correctiva](../Calidad/accion-correctiva.md#el-8d-ocho-disciplinas-para-un-problema) |
| 5 porqués | Five whys | Preguntar «por qué» en cadena hasta una causa sobre la que se puede actuar | [acción correctiva](../Calidad/accion-correctiva.md#los-5-porqués-y-su-crítica) |
| Diagrama de Ishikawa | Fishbone diagram | El diagrama de causa y efecto que ordena las causas posibles por categorías | [acción correctiva](../Calidad/accion-correctiva.md#el-diagrama-de-ishikawa) |
| Verificación de la eficacia | Effectiveness check | Comprobar que la acción funcionó antes de cerrarla | [acción correctiva](../Calidad/accion-correctiva.md#cómo-falla-una-acción-correctiva) |
| Trazabilidad de lotes | Lot traceability | Poder seguir qué lotes de componente entraron en cada lote de producto y a qué clientes fue cada uno | [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md) |
| Lote (de fabricación) | Lot, batch | La cantidad producida que se identifica y se sigue junta; el lote como atributo del stock es de Inventario | [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md) |
| Genealogía del lote | Lot genealogy | La relación entre los lotes de componente que consumió una orden y los lotes que produjo | [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md#la-genealogía-de-qué-está-hecho-cada-lote) |
| Rastreo hacia atrás y hacia adelante | Backward, forward traceability | De un producto a sus materiales y proveedores, y de un material a los productos y clientes | [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md#hacia-atrás-y-hacia-adelante) |
| Retiro | Recall | Sacar del mercado los lotes alcanzados por un problema y avisar a quienes los recibieron | [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md#el-retiro) |

## Fundamentos

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Empujar | Push | Liberar el trabajo según el plan o el pronóstico; es lo que hace el MRP | [fundamentos de producción](fundamentos-de-produccion.md#cuatro-escuelas-sobre-cómo-liberar-el-trabajo) |
| Tirar | Pull | Liberar el trabajo según el consumo, con un límite a la producción en proceso; kanban y CONWIP | [fundamentos de producción](fundamentos-de-produccion.md#cuatro-escuelas-sobre-cómo-liberar-el-trabajo) |
| CONWIP | Constant work in process | Tirar con un solo límite de producción en proceso para toda la línea | [fundamentos de producción](fundamentos-de-produccion.md#cuatro-escuelas-sobre-cómo-liberar-el-trabajo) |
| Teoría de las restricciones | Theory of constraints, TOC | La escuela que subordina toda la planta al cuello de botella | [fundamentos de producción](fundamentos-de-produccion.md#cuatro-escuelas-sobre-cómo-liberar-el-trabajo) |
| DDMRP | Demand driven MRP | Amortiguadores de stock en puntos de desacople, recalculados con la demanda real | [fundamentos de producción](fundamentos-de-produccion.md#cuatro-escuelas-sobre-cómo-liberar-el-trabajo) |
| Justo a tiempo | Just in time, JIT | Hacer solo lo que hace falta, cuando hace falta y en la cantidad que hace falta; la idea del sistema de producción de Toyota | [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md#kanban-que-el-consumo-dispare-la-producción) |
| Lean | Lean production | El nombre que Krafcik les dio en 1988 a las prácticas que Toyota desarrolló antes | [fundamentos de producción](fundamentos-de-produccion.md#del-mrp-al-erp-y-de-toyota-a-lean) |
| PCF de APQC | Process Classification Framework | El marco de procesos que pone el plan en 4.1 y la fabricación en 4.3 | [marcos de la producción](marcos-de-la-produccion.md#el-pcf-de-apqc-de-41-a-43) |
| ISA-95 | ISA-95, IEC 62264 | La norma que ordena la empresa en cinco niveles y define la frontera entre el ERP y el MES | [marcos de la producción](marcos-de-la-produccion.md#isa-95-cinco-niveles-y-la-frontera-entre-erp-y-mes) |
| SCOR | Supply Chain Operations Reference | El marco de ASCM; su proceso Make es el de este tema | [marcos de la producción](marcos-de-la-produccion.md#scor-y-cpim-lo-poco-que-se-sabe) |
| CPIM | Certified in Planning and Inventory Management | El programa de certificación en planificación de ASCM (ex APICS) | [marcos de la producción](marcos-de-la-produccion.md#scor-y-cpim-lo-poco-que-se-sabe) |
