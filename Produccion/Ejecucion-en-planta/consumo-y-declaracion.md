---
resumen: >-
  El consumo registra qué material, de qué lote, usó una orden de producción, y la declaración de producción registra qué salió de ella: cuánto bueno, cuánto rechazado, cuánta merma y qué subproductos. Son los dos hechos que convierten el trabajo de la planta en movimientos de stock y en costo.
estado: borrador
estabilidad: semi
fuentes:
  - "Documentación de Work Order de un sistema abierto (entrega a producción en proceso, consumo automático, devolución, desecho): https://docs.frappe.io/erpnext/user/manual/en/work-order"
  - "Documentación de Job Card del mismo sistema (pérdida de proceso): https://docs.frappe.io/erpnext/user/manual/en/job-card"
  - "Glosario de un sistema comercial que cita el APICS Dictionary, 8.ª ed., entrada backflush (según el resumen): https://erp.smcusa.com/SyteLine/Language/en-US/mergedProjects/sl_main/other/glossary/def_backflush.htm"
  - "IISE, Z94.14 Operations & Inventory Planning & Control, entradas back flush y by-product (según el resumen): https://www.iise.org/Details.aspx?id=2402"
  - "NIC 2 Existencias, párrafo 14, en el Reglamento (CE) 1126/2008, Diario Oficial de la UE L 320, 29.11.2008: https://www.boe.es/doue/2008/320/L00001-00481.pdf"
  - "IAS 2 Inventories, párrafo 14, versión consolidada de la Comisión Europea (copia en un sitio universitario): https://moodle2.units.it/pluginfile.php/305507/mod_resource/content/1/ias2_en%20%282%29.pdf"
  - "Produccion/.investigacion/ejecucion-en-planta.md (sección 2) y ejecucion-en-planta-2.md (secciones 6 y 7), 2026-11-27"
aliases: [consumo de materiales, material consumption, entrega de materiales a la orden, material issue, vale de salida, consumo automático, backflush, backflushing, back flush, declaración de producción, production reporting, production confirmation, parte de producción, merma, scrap, pérdida de proceso, process loss, rechazo, reject, desecho, subproducto, by-product, coproducto, co-product, producto conjunto, joint product]
creado: 2026-11-27
revisado:
---

# Consumo y declaración

El consumo registra qué material, de qué lote, usó una orden de producción, y la declaración de producción registra qué salió de ella: cuánto bueno, cuánto rechazado, cuánta merma y qué subproductos. Son los dos hechos que convierten el trabajo de la planta en movimientos de stock y en costo.

Pertenecen a la [orden de producción](orden-de-produccion.md), dentro de [Ejecución en planta](ejecucion-en-planta.md). Cada uno termina en un movimiento de stock, que es de Inventario: el material sale de un lugar y el terminado entra en otro, como filas del [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md). El sistema abierto leído modela la producción en proceso como un depósito propio, una [ubicación](../../Inventario-y-depositos/Operacion-del-deposito/ubicaciones.md) más, así que consumir es mover del estante a la producción. Acá se decide qué orden pide el movimiento y qué cantidad le corresponde.

## Entregar el material a la orden

La forma explícita es entregar el material antes de producir. En un sistema abierto, el material pasa del depósito de origen a uno de producción en proceso con un movimiento de transferencia para fabricar. Por cada componente, la orden lleva tres cantidades: «Required Quantity», que se calcula «automatically based on the Bill Of Materials», «Transferred Quantity» y «Consumed Quantity».

Lo que sobra vuelve: el mismo sistema tiene una acción «Return Components» que genera el movimiento inverso. También deja entregar más de lo que pide la lista, hasta un porcentaje configurable («Transfer Extra Raw Materials to WIP (%)»). En papel, la entrega es un vale de salida de depósito firmado por quien retira, y la devolución, un vale de reingreso (criterio de la base).

Entregar primero tiene una ventaja: la orden abierta muestra su costo mientras avanza. Tiene un costo: cada entrega es un registro más (inferencia de la base).

## El consumo automático

El consumo automático (backflush) descuenta los componentes después, a partir de lo producido. La definición del APICS Dictionary, 8.ª edición, citada en el glosario de un sistema comercial, es «The deduction from inventory records of the component parts used in an assembly or subassembly» «by exploding the bill of materials by the production count of assemblies produced». El glosario Z94.14 del IISE, según su resumen, empieza igual, pero la frase quedó cortada. Las dos son de la misma tradición y cuentan como una sola fuente.

En el sistema abierto se activa con una opción: «Backflush Raw Materials From Work-in-Progress Warehouse». Con ella, la declaración crea un movimiento de tipo fabricación que consume desde el depósito de origen e ingresa el terminado. Otra opción saltea la entrega: «the raw material is considered to be consumed hence the Stock Entry is skipped».

El consumo automático es tan bueno como la [lista de materiales](../Producto-y-proceso/lista-de-materiales.md). Si la lista dice cuatro tornillos y se usan cinco, el sistema descuenta cuatro y el quinto aparece como faltante en el próximo conteo, sin una orden a la que imputarlo. Tampoco se ve el costo de la orden hasta el final, como advierte [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md) (inferencia de la base en los dos casos).

Un caso de la base: una orden de 100 mesas, con cuatro patas cada una, declara 98 buenas y 2 rechazadas. Si el consumo se calcula sobre las buenas, descuenta 392 patas; si se calcula sobre las 100 producidas, 400. Las 8 patas de las mesas rechazadas salieron del estante igual, así que la primera regla deja el stock del sistema 8 patas por encima del real. La documentación del sistema abierto no dice sobre qué cantidad calcula; es una decisión de diseño que conviene escribir.

Como criterio de la base, el consumo automático conviene para componentes baratos y de mucho uso, con una lista confiable y un plazo corto entre entrega y declaración. La entrega explícita conviene para lo caro, lo que lleva lote o lo que se usa en cantidades variables.

## La declaración de producción

Declarar es decir cuánto salió, de qué calidad y en qué lote. Cada declaración ingresa lo bueno al depósito de terminados con un movimiento; el sistema abierto deja declarar una parte y seguir produciendo. En papel es el parte de producción del turno (criterio de la base).

Lo que sale de una orden se reparte en cuatro destinos:

| Salida | Qué es (criterio de la base) | Adónde va |
|---|---|---|
| Producto bueno | lo que cumple | depósito de terminados |
| Rechazo | una pieza que salió y no cumple | se aparta y se abre una [no conformidad](../Calidad/no-conformidad.md), que decide la disposición: reprocesar, reparar, usar como está con concesión, desechar o devolver al proveedor |
| Merma | material o producto que se pierde en el proceso y no sale como pieza | se registra como pérdida de la orden; el desecho con valor, a un depósito de desecho |
| Subproducto o coproducto | otra salida del mismo proceso | su propio depósito, con su cantidad |

Para el desecho, el sistema abierto pide un lugar: «If the BOM results in Scrap material, the Scrap Warehouse needs to be selected». Para la merma de una operación tiene una regla propia: la pérdida de proceso «will be calculated only when the Pending Qty is zero»; con 10 a fabricar y 6 terminadas, mientras queden 4 pendientes no la calcula, y con cero pendientes las 4 restantes «will be treated as Process Loss Qty». Es una decisión de ese sistema, no un estándar.

Merma, rechazo, desecho y reproceso tienen un sentido cada uno en todo el tema (criterio de la base). Merma es la cantidad que se pierde en el proceso. Rechazo es la pieza que salió y no cumple. Desecho es lo que se da de baja físicamente: el sobrante de la merma, como un recorte, o las piezas que la no conformidad dispuso desechar; puede tener valor de recupero. Reproceso es el trabajo que deja conforme una pieza rechazada. Desechar y reprocesar son dos de las disposiciones que define [no conformidad](../Calidad/no-conformidad.md#las-disposiciones-posibles).

La lista ya trae una merma normal por componente y un rendimiento esperado, como explica [lista de materiales](../Producto-y-proceso/lista-de-materiales.md#merma-del-componente-y-rendimiento-de-la-salida). Lo que se declara es la merma real; la diferencia entre las dos es la variación de uso de material. Dónde va el costo de la merma normal, la anormal y el reproceso lo decide [Costos de producción](../Costos-de-produccion/costos-de-produccion.md). La merma que aparece en el depósito al contar es otra cosa y es de Inventario: ver [ajustes y mermas](../../Inventario-y-depositos/Control-del-stock/ajustes-y-mermas.md).

## Subproducto y coproducto: la norma contable y un glosario no coinciden

Algunos procesos dan más de una salida. La NIC 2, en su párrafo 14, lo describe así: «El proceso de producción puede dar lugar a la fabricación simultánea de más de un producto. Es el caso, por ejemplo, de la producción conjunta o de la producción de productos principales junto a subproductos». Si el costo de cada uno no se puede identificar por separado, se reparte «utilizando bases uniformes y racionales», por ejemplo por el valor de mercado. Y agrega: «La mayoría de los subproductos, por su propia naturaleza, no poseen un valor significativo», y entonces se miden con frecuencia «por su valor realizable neto, deduciendo esa cantidad del coste del producto principal».

> [!IMPORTANT]
> Qué es un coproducto. La NIC 2 distingue productos conjuntos, que se reparten el costo, de un producto principal con subproductos de poco valor. El glosario Z94.14 del IISE define el subproducto como «A material of value produced as residual of or incidental to the production process» y da «co-product» como sinónimo. En las fuentes, «coproducto» no tiene un sentido único.

En el tema, la base sigue a la NIC 2 (criterio de la base): coproducto es una salida de valor comparable a la principal, que se lleva una parte del costo; subproducto es una salida secundaria de poco valor, que se mide por lo que se obtiene al venderla. El texto leído es el de la Unión Europea, no el de la norma argentina.

> [!NOTE] Sin fuente todavía: la norma contable argentina sobre existencias, que no se leyó. En la lista, cada salida extra es un renglón del lado de lo que sale, como cuenta [lista de materiales](../Producto-y-proceso/lista-de-materiales.md#subproducto-y-coproducto-como-datos-de-la-lista).

## El lote consumido es la base de la trazabilidad

La genealogía de un lote fabricado no se carga aparte: sale de estos registros. Cada entrega o consumo tiene que decir qué lote de componente se usó, y cada declaración, qué lote salió. Con eso, saber qué lotes de terminado llevan un componente malo es una consulta, como explica [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md). El lote como atributo del stock es de Inventario, en [lote y serie](../../Inventario-y-depositos/Existencias/lote-y-serie.md).

El consumo automático complica esto: si el sistema descuenta por la lista, tiene que elegir de qué lote descontar, y la regla que elija (el más viejo, el que vence antes) puede no ser el lote que de verdad se usó (inferencia de la base). En los artículos que se siguen por lote, el consumo tiene que confirmar el lote, a mano o leyéndolo del envase, o la regla tiene que coincidir con lo que se hace en la línea. Es el mismo criterio de [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md#qué-tiene-que-registrar-un-sistema).

## Qué guarda un sistema del consumo y la declaración

- Por componente de la orden: cantidad requerida, entregada, consumida y devuelta; lote y lugar de cada movimiento.
- La regla de consumo de cada componente (entrega explícita o automática) y sobre qué cantidad se calcula el automático.
- Por declaración: fecha, quién declaró, operación, cantidad buena, rechazada y merma, con su motivo.
- Por salida: el lote producido y su lugar de destino, incluidos subproductos, coproductos y desecho.
- El vínculo de cada rechazo con su [no conformidad](../Calidad/no-conformidad.md).

Evidencia: la documentación de la orden y de la hoja de operación de un sistema abierto; los motivos y la regla del consumo automático son criterio de la base.
