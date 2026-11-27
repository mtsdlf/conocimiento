---
resumen: >-
  Los hechos de gestión son las tablas de hechos que salen de los procesos de un sistema de
  gestión: ventas, pedidos, compras, stock, cuentas corrientes, mayor y horas. Cada proceso da una
  tabla de transacciones, una foto periódica de saldos o una fila que sigue un recorrido, y cada
  dominio define los indicadores que se calculan encima.
estado: vigente
estabilidad: estable
fuentes:
  - "Kimball Group, Transaction Fact Tables, Periodic Snapshot Fact Tables y Accumulating Snapshot Fact Tables: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/"
  - "Bob Becker, Design Tip #167, Complementary Fact Table Types (2014): https://www.kimballgroup.com/2014/06/design-tip-167-complementary-fact-table-types/"
  - "Kimball Group, Additive, Semi-Additive, and Non-Additive Facts: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/additive-semi-additive-non-additive-fact/"
  - "Kimball Group, Header/Line Fact Tables, Allocated Facts, Degenerate Dimensions, Factless Fact Tables, Year-to-Date Facts, Profit and Loss Fact Tables Using Allocations y Consolidated Fact Tables (mismas técnicas)"
  - "Kimball Group, ficha y fe de erratas de The Data Warehouse Toolkit, 3.ª ed.: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/"
  - "Kimball y Ross, The Data Warehouse Toolkit, 3.ª ed. (Wiley, 2013), índice oficial (solo los títulos de los caps. 3 a 7 y 9): https://media.wiley.com/product_data/excerpt/02/11185308/1118530802-34.pdf"
  - "Datos/.investigacion/bi-gestion-modelado.md (2026-11-27)"
aliases: [hechos de gestión, tablas de hechos del ERP, hecho de ventas, hecho de stock, foto periódica, periodic snapshot, accumulating snapshot, transaction fact table, hecho semiaditivo, semi-additive fact]
creado: 2026-11-27
revisado: 2026-11-27
---

# Hechos de gestión

Los hechos de gestión son las tablas de hechos que salen de los procesos de un sistema de gestión: ventas, pedidos, compras, stock, cuentas corrientes, mayor y horas. Cada proceso da una tabla de transacciones, una foto periódica de saldos o una fila que sigue un recorrido, y cada dominio define los indicadores que se calculan encima.

Son parte del [BI sobre el software de gestión](bi-sobre-software-de-gestion.md). La tabla de hechos, el grano y la estrella están en [modelado dimensional](../../Modelado-y-almacenamiento/modelado-dimensional.md); sus dimensiones, en [dimensiones conformadas](dimensiones-conformadas.md).

## El sistema ya registra hechos

Un sistema de gestión guarda casi todo como movimientos que no se editan, y el saldo es su suma, según el [registro de movimientos y dimensiones](../../../Software-de-gestion/Columnas-tecnicas/registro-de-movimientos-y-dimensiones.md). En lectura de esta base, ese registro ya es casi una tabla de hechos de transacciones. Al BI le toca elegir el grano, juntar lo que el sistema reparte en varias tablas y guardar lo que falta, como el saldo de cada fin de mes.

## Tres tipos de tabla para tres preguntas

Becker (2014) asocia los tres tipos de tabla de hechos de Kimball a tres preguntas: transacciones contesta «how many?», la foto periódica «how much?» y el recorrido acumulado mide la velocidad.

| Tipo | Qué es una fila | En un sistema de gestión |
|---|---|---|
| Transacciones | «a measurement event at a point in space and time» | un renglón de factura, un movimiento de stock, un asiento, una hora imputada |
| Foto periódica | resume un período, aunque no haya habido actividad | el stock por artículo al cierre del día, el saldo por cliente o cuenta a fin de mes |
| Recorrido acumulado | sigue un proceso, con una fecha por hito; la fila «is revisited and updated» | un pedido de la toma al cobro, una orden de compra hasta el pago |

Las definiciones son de Kimball; la tercera columna, lectura de esta base. Solo el recorrido acumulado actualiza filas y sufre más los [cambios que llegan después](extraer-de-un-sistema-de-gestion.md#los-cambios-que-llegan-después). Becker: «Often the best design response is a combination of two, or even all three, fact table types».

## Los hechos de cada proceso y sus indicadores

| Proceso | Hecho y grano habitual | Tipo | Indicadores, en su dominio |
|---|---|---|---|
| Ventas | renglón de factura | transacciones | [margen de contribución](../../../Contabilidad/Contabilidad-de-gestion/punto-de-equilibrio.md#margen-de-contribución-lo-que-deja-cada-venta-para-pagar-los-fijos), sobre el [costo de lo vendido](../../../Contabilidad/Operaciones/costo-de-lo-vendido.md) |
| Pedidos | renglón de [pedido de venta](../../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md) con fechas de toma, entrega, factura y cobro | recorrido acumulado | [OTIF y pedido perfecto](../../../Cadena-de-suministro-y-logistica/Despacho-y-entrega/nivel-de-servicio-logistico.md#otif-pedido-perfecto-y-tasa-de-cumplimiento-de-la-entrega); tiempos de [del pedido al cobro](../../../Procesos-de-negocio/del-pedido-al-cobro.md#qué-se-mide-del-recorrido-entero) |
| Compras | renglón de orden de compra, con recepción y factura del proveedor | transacciones y recorrido acumulado | [a tiempo y completo del proveedor](../../../Compras-y-abastecimiento/Proveedores/evaluacion-de-proveedores.md#a-tiempo-y-completo-depende-de-qué-se-cuente); tiempos de [de la compra al pago](../../../Procesos-de-negocio/de-la-compra-al-pago.md#qué-se-mide-del-recorrido-entero) |
| Stock | movimiento por artículo y depósito, más la existencia al cierre del día | transacciones y foto periódica | [rotación y días de inventario](../../../Inventario-y-depositos/Reposicion/indicadores-de-inventario.md#rotación-y-días-de-inventario), [exactitud del registro](../../../Inventario-y-depositos/Reposicion/indicadores-de-inventario.md#exactitud-del-registro) |
| Cuentas a cobrar y a pagar | movimiento por comprobante, más el saldo por antigüedad a cada cierre | transacciones y foto periódica | [antigüedad de saldos](../../../Contabilidad/Registro/cuentas-corrientes.md#la-antigüedad-de-saldos), [DSO](../../../Tesoreria/Credito-y-cobranzas/gestion-de-la-cobranza.md#dso-dso-mejor-posible-y-días-de-atraso) (sobre ventas a crédito), [ciclo de conversión del efectivo](../../../Tesoreria/Caja-y-liquidez/capital-de-trabajo.md#el-ciclo-de-conversión-del-efectivo) |
| Mayor | renglón de asiento por cuenta, más el saldo por período | transacciones y foto periódica | [estado de resultados](../../../Contabilidad/Estados-contables/estado-de-resultados.md), [desvíos contra el presupuesto](../../../Contabilidad/Contabilidad-de-gestion/presupuesto.md#desvíos-separar-el-efecto-precio-del-efecto-cantidad), resultado por [centro de costo](../../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md) |
| Horas | renglón de [hoja de horas](../../../Servicios-profesionales-y-proyectos/Registro-de-horas/hoja-de-horas.md) aprobada, por persona, proyecto y día | transacciones | [utilización](../../../Servicios-profesionales-y-proyectos/Rentabilidad-de-la-firma/utilizacion.md#el-denominador-cambia-el-número), [realización](../../../Servicios-profesionales-y-proyectos/Rentabilidad-de-la-firma/realizacion.md) |

La tabla es lectura de esta base. Según su índice, el *Toolkit* trae secciones como «Inventory Periodic Snapshot», «Accumulating Snapshot for Order Fulfillment Pipeline», «General Ledger Periodic Snapshot» y «General Ledger Journal Transactions», y ningún capítulo de cuentas corrientes ni de horas; su texto no se leyó. La OEE y los indicadores de mantenimiento salen de sistemas de planta: [eficiencia global del equipo](../../../Produccion/Ejecucion-en-planta/eficiencia-global-del-equipo.md#qué-guarda-un-sistema-para-la-oee) e [indicadores de mantenimiento](../../../Activos-y-mantenimiento/Desempeno-de-los-activos/indicadores-de-mantenimiento.md).

Cada indicador se define una vez, en su dominio, y el BI lo calcula sin redefinirlo, desde la [capa semántica](../capa-semantica.md) común a todas las herramientas.

## Lo que no se puede sumar

Un saldo no se suma en el tiempo. Kimball: «balance amounts are common semi-additive facts because they are additive across all dimensions except time». La fe de erratas del capítulo de inventario del *Toolkit* agrega que el stock y su valuación «can't be simply summed over time periods»; el promedio divide la suma por las observaciones diarias, y treinta días sumados dan treinta veces el stock. Deudores y cuentas se suman entre clientes o cuentas, no entre meses.

Una razón, como la rotación, la utilización o el DSO, tampoco se suma. Kimball: «store the fully additive components of the non-additive measure and sum these components into the final answer set before calculating the final non-additive fact». La utilización de un equipo es la suma de horas facturables sobre la de disponibles, no el promedio de las personas (lectura de esta base).

Kimball aconseja calcular los acumulados del año en la herramienta de BI, sin guardarlos, porque el pedido se vuelve rápido «YTD at the close of the fiscal period» o «fiscal period to date».

## Cabecera, renglón y lo que se reparte

Kimball: «all the header-level dimension foreign keys and degenerate dimensions should be included on the line-level fact table». El número de factura queda como dimensión degenerada, una clave sin tabla propia.

Un flete o un descuento sobre el total se reparte entre los renglones «based on rules provided by the business»; si no, el margen por artículo omite el flete y no cuadra con lo facturado (lectura de esta base). La regla es del dominio, como la de [repartir los costos de los departamentos de servicio](../../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md#repartir-los-costos-de-los-departamentos-de-servicio). Kimball posterga la tabla de resultados con costos repartidos porque el reparto «is a politically charged step that requires high-level executive support».

## Lo que no pasó

Para lo que no ocurrió (qué clientes no compraron este mes, qué horas nadie cargó), Kimball usa una tabla de cobertura: «when the activity is subtracted from the coverage, the result is the set of events that did not happen». En las horas, la cobertura es la jornada, el denominador de la utilización (lectura de esta base).

## Real contra presupuesto

El presupuesto va por mes y por cuenta o categoría, y suele vivir fuera del sistema (lectura de esta base). Kimball ofrece el *drill across*, que consulta cada tabla aparte y alinea por una dimensión achicada como el mes, o una tabla consolidada de real y pronóstico «if they can be expressed at the same grain», que complica la carga y simplifica el análisis. El armado está en [presupuesto](../../../Contabilidad/Contabilidad-de-gestion/presupuesto.md); la planilla, en [varias fuentes de gestión](varias-fuentes-de-gestion.md).

## Cómo falla

- El grano mezclado. Las filas de factura junto a las de renglón cuentan dos veces el total ([modelado dimensional](../../Modelado-y-almacenamiento/modelado-dimensional.md#el-grano-se-declara-antes-que-todo)).
- Stock sumado en el tiempo. El stock del trimestre aparece como la suma de tres cierres.
- La razón promediada. La rotación de la empresa promedia la de los depósitos sin pesar su stock.
- El indicador redefinido. El BI calcula el DSO distinto que Tesorería, y la reunión discute el número en vez de la cobranza.
- La anulación escondida. La nota de crédito es venta negativa en un hecho y devolución en otro, y los tableros no coinciden.
