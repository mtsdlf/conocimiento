---
resumen: >-
  El disponible para prometer (ATP) es el cálculo de cuántas unidades de un artículo se pueden comprometer a un pedido nuevo en cada fecha: la oferta confirmada menos la demanda ya comprometida, período por período. Se calcula por el método discreto o por el acumulado hacia adelante, y su resultado depende de qué se decide contar como oferta y como comprometido.
estado: vigente
estabilidad: estable
fuentes:
  - "ASCM/APICS, CPIM 6.1 (2019) Excerpt, módulo 1, sección F, «Calculating Available-to-Promise», p. 1-209 a 1-210 (método discreto y regla del negativo): https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf"
  - "Microsoft Learn, Inventory Visibility: on-hand change schedule y available-to-promise (ATP hacia adelante, fórmula de oferta y demanda, ejemplo numérico): https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-available-to-promise"
  - "Inventario-y-depositos/.investigacion/existencias-y-control.md (2026-11-27), sección Disponible para prometer"
aliases: [disponible para prometer, ATP, available-to-promise, available to promise, disponibilidad, cálculo de disponibilidad, ATP discreto, discrete ATP, ATP acumulado, cumulative ATP, look-ahead ATP]
creado: 2026-11-27
revisado: 2026-11-27
---

# Disponible para prometer

El disponible para prometer (ATP) es el cálculo de cuántas unidades de un artículo se pueden comprometer a un pedido nuevo en cada fecha: la oferta confirmada menos la demanda ya comprometida, período por período. Se calcula por el método discreto o por el acumulado hacia adelante, y su resultado depende de qué se decide contar como oferta y como comprometido.

El cálculo es de este tema; la fecha que se le dice al cliente es de Relación con clientes, en [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md), que trae la definición del APICS Dictionary, el primer paso del ejemplo del CPIM y el capable-to-promise para lo que se fabrica contra pedido. Lo que se suma y se resta sale de la lista de [estados del stock](estados-del-stock.md), y apartar físicamente las unidades para un pedido es otra cosa: está en [reserva](../Operacion-del-deposito/reserva.md).

## Oferta menos demanda comprometida, sin descontar dos veces

Los dos métodos hacen la misma resta y se diferencian en cómo reparten lo que sobra entre las fechas. La resta es (criterio de la base, sobre las dos fuentes):

> ATP = oferta confirmada − demanda comprometida, en un horizonte de fechas

Responde a la pregunta del vendedor: «si acepto este pedido, ¿le quito unidades a alguien a quien ya se las prometí?». Por eso cada pedido aceptado baja el ATP para el siguiente.

## Método discreto: cada entrada tiene su propio disponible

El método discreto calcula un ATP por cada período en que entra mercadería y no arrastra lo que sobra de un período al siguiente. El CPIM lo explica sobre un plan maestro con entradas de 100 unidades. El primer período sale del stock inicial menos los pedidos anteriores a la primera entrada, cuyo cálculo está en [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md). Los siguientes salen de cada entrada menos los pedidos que caen antes de la entrada que sigue:

| Semana | Entrada | Pedidos hasta la próxima entrada | ATP sin corregir | ATP corregido |
|---|---|---|---|---|
| 1 | stock inicial | los anteriores a la semana 2 | 22 (ver [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md)) | 22 |
| 2 | 100 | 66 | 34 | 15 |
| 3 | 100 | 57 + 62 | −19 | 0 |
| 5 | 100 | 30 + 0 | 70 | 70 |

En la semana 3 los pedidos superan la entrada. El CPIM agrega una regla para ese caso: «Reduce the prior ATP by the amount by which the next ATP would be negative, and then add this amount to the negative ATP field so it is no longer negative». Las 19 unidades que faltan se toman de la semana 2: «100 units MPS – 66 units of orders – 19 units = 15 units ATP», y la semana 3 queda en 0. Es la única vez que el método mira el ATP de un período anterior, porque esos pedidos ya están comprometidos y alguien tiene que cubrirlos.

El supuesto del método es que el ATP de un período se lo van a comer pedidos que todavía no llegaron, así que no se arrastra. Con el ejemplo, el vendedor puede prometer hasta 22 para entrega inmediata y, si el cliente espera una semana, hasta 15 más; para más, el cliente tiene que aceptar cinco semanas.

El ejemplo parte de un plan maestro de producción. En un depósito que no fabrica, las entradas son las recepciones programadas de compras y de transferencias (inferencia de la base).

## Método acumulado hacia adelante: el mínimo de lo que se proyecta

El CPIM nombra otros dos métodos, «cumulative with look-ahead and cumulative without look-ahead», y no los presenta. Una variante con mirada hacia adelante la documenta el ERP de un proveedor grande. Ahí el ATP de una fecha es «The minimum projected on-hand quantity that's available from the specified date through the end of the schedule period», y por eso es «the maximum quantity that can be promised on the current date».

El ejemplo de esa documentación arranca con 20 unidades en stock el 1 de febrero:

| Fecha | Oferta | Demanda | Stock proyectado | ATP |
|---|---|---|---|---|
| 1 de febrero | 20 en stock | 3 | 17 | 12 |
| 2 de febrero | | | 17 | 12 |
| 3 de febrero | 10 | | 27 | 12 |
| 4 de febrero | | 15 | 12 | 12 |
| 5 de febrero | 1 | | 13 | 13 |
| 6 de febrero | 3 | | 16 | 16 |

El 3 de febrero hay 27 proyectadas, pero solo se pueden prometer 12: con más, el 4 no alcanzaría para la demanda de 15 ya comprometida.

El mismo ejemplo muestra cómo falla. Si la entrada de 10 programada para el 3 de febrero no llega, el ATP del 4 cae a 2. Lo que ya se prometió contra esa entrada queda sin cubrir.

Que esta variante sea el método acumulado con mirada hacia adelante del CPIM es inferencia del informe de la base; solo la confirma esa documentación, no un libro.

## Los dos métodos lado a lado

| | Discreto | Acumulado hacia adelante |
|---|---|---|
| Dónde calcula | En el primer período y en cada período con una entrada | En cada fecha del horizonte |
| Qué hace con lo que sobra | No lo arrastra; supone que lo van a consumir pedidos por venir | Lo arrastra, limitado por la demanda futura |
| Qué hace con un faltante | Lo cubre con el ATP del período anterior | Ya está en el mínimo proyectado |
| Fuente | CPIM, con un plan maestro | Un ERP, con el stock y las entradas y salidas programadas de un depósito |
| Conviene (criterio de la base) | Cuando se planifica por períodos y se quiere guardar lo de cada entrada para quien pida después | Cuando se promete por fecha y lo que se proyecta es confiable |

## Qué cuenta como oferta

Las dos fuentes suman cosas distintas. El CPIM suma el stock inicial y las entradas del plan maestro. La fórmula del ERP citado suma como oferta «PhysicalInvent + OnHand + Unrestricted + QualityInspection + Inbound» y aclara que «The default ATP calculated formula is for reference»: es configurable.

Las decisiones que quedan, con la propuesta de la base:

| Candidato | ¿Suma? (criterio de la base) |
|---|---|
| Stock disponible | Sí |
| Stock en cuarentena o inspección | Solo si casi siempre se aprueba; la fórmula por defecto citada lo suma |
| Stock bloqueado | No |
| Stock de terceros | No, salvo acuerdo con el dueño |
| Entradas programadas (compras, transferencias en tránsito, producción) | Sí, en su fecha, si la fecha está confirmada |
| Pedidos a proveedor sin fecha confirmada | No |

## Qué cuenta como demanda comprometida

El CPIM resta los pedidos de clientes. El ERP citado resta la reserva física, la reserva blanda y las salidas programadas. Quien diseña decide qué más entra, y tiene que decirlo:

| Candidato | ¿Resta? (criterio de la base) |
|---|---|
| Pedidos confirmados, vencidos y por vencer | Sí |
| Reservas físicas de esos pedidos | Sí, pero en lugar del pedido, no además |
| Transferencias a otro depósito ya programadas | Sí |
| Consumo de producción programado | Sí, si la planta saca de este stock |
| Presupuestos aceptados sin pedido | Según la empresa: si se cumplen casi siempre, restarlos evita prometer dos veces |
| Pronóstico de demanda | No en el ATP; el plan lo usa para decidir las entradas |
| Stock de seguridad | No, salvo que la empresa decida no prometerlo nunca |

La trampa más común es descontar dos veces. Un pedido confirmado que ya tiene su [reserva](../Operacion-del-deposito/reserva.md) resta una vez como pedido y otra como reserva si nadie lo cruza, y el ATP da menos de lo que hay. La fórmula del ERP evita eso restando reservas y salidas, y no los pedidos; el CPIM resta pedidos porque no reserva (inferencia de la base).

## Cuándo el ATP da números falsos

- **El stock registrado no es el del estante.** El ATP hereda el error del registro, y el registro suele estar mal: está en [control del stock](../Control-del-stock/control-del-stock.md).
- **Las entradas programadas no llegan.** Como en el ejemplo del 3 de febrero, lo prometido contra una entrada que se atrasa queda sin cubrir.
- **Varios canales calculan por su cuenta.** Si cada canal descuenta de una copia del número, dos venden la misma unidad; es la sobreventa de [catálogo y stock](../../Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md).
- **Un pedido se acepta sin bajar el ATP.** El CPIM dice que, en cuanto el pedido entra al sistema, sube la demanda comprometida y baja el ATP; si el sistema lo descuenta recién al final del día, todo lo vendido en el día se promete contra el mismo número (inferencia de la base).

## Para leer el cálculo en la fuente

El recurso canónico es el excerpt del CPIM, sección F, «Calculating Available-to-Promise» (p. 1-209 y 1-210): fijarse en la regla que arrastra el negativo al período anterior. La documentación del ERP citada completa con la entrada que se atrasa y la fórmula configurable.

> [!NOTE] Sin fuente todavía: el método acumulado sin mirada hacia adelante, y una fuente de libro (APICS Dictionary o un texto de planificación) para los dos métodos acumulados.
