---
tema: Inventario y depósitos
para: entender qué registra y qué hace una empresa con la mercadería que guarda (qué tiene, dónde, en qué estado, cuánto puede prometer, cómo entra, cómo se prepara para salir, cómo se cuenta y cuándo se repone), para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: entiende de software y de negocio en general; no se da por sabido el vocabulario del depósito (ubicación, picking, conteo cíclico, punto de pedido, disponible para prometer) ni cómo lo divide un sistema
escuela: neutral; la teoría clásica de inventarios (el stock como colchón contra la incertidumbre, con sus fórmulas) es la base, y la crítica de lean y justo a tiempo (el stock como desperdicio) y la de DDMRP aparecen donde discuten con ella
fuera:
  - el proveedor, la orden de compra y el control de lo recibido contra lo pedido — Compras-y-abastecimiento (Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md); acá, contar y ubicar lo que llegó
  - el cruce de la factura del proveedor con la orden y la recepción (cruce de tres vías) — Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md, con el control en Contabilidad/Control-interno
  - el despacho desde que la mercadería sale por la puerta, el transporte, la red de depósitos, el pronóstico de demanda, el plan agregado (S&OP) y la reposición planificada de quien no fabrica (DRP) — Cadena-de-suministro-y-logistica (Despacho-y-entrega/, Transporte/, Red-de-distribucion/ y Planificacion/)
  - el plan maestro, el MRP y la transformación en planta, con el inventario en proceso — Produccion (Planificacion-de-la-produccion/ y Ejecucion-en-planta/)
  - la fecha que se le promete al cliente y el pedido de venta — Relacion-con-clientes; acá, el cálculo de lo disponible y la reserva
  - la valuación del stock (PEPS, promedio ponderado), el costo de lo vendido y el valor neto de realización — Contabilidad/Operaciones/costo-de-lo-vendido.md
  - la separación de funciones y las autorizaciones como control — Contabilidad/Control-interno; acá, cómo se aplican al ajuste
  - cómo se guarda el stock en una base de datos (movimientos que no se editan, saldo calculado) — Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md; en una planilla, Planillas-de-calculo/Diseno-de-planillas/planilla-de-stock.md
  - la variante, el SKU y los estados del stock en una tienda online, la sobreventa entre canales y el fulfillment — Comercio-electronico/Operaciones-del-comercio; se enlaza como el caso del comercio
  - la logística de la devolución en una tienda — Comercio-electronico/Operaciones-del-comercio/devoluciones.md; acá, el reingreso al stock
  - las piezas de diseño comunes a todo software de gestión (datos maestros, documento y estados, unidades) — Software-de-gestion/Columnas-tecnicas
  - los recorridos de punta a punta (del pedido al cobro, de la compra al pago) — Procesos-de-negocio (del-pedido-al-cobro.md y de-la-compra-al-pago.md)
  - el diseño físico del depósito (estanterías, autoelevadores, automatización, seguridad e higiene) y los productos de WMS, comparativas y precios
fuentes: []
preguntas:
  - "Un cliente pide 30 unidades: en el sistema hay 100, pero 60 están apartadas para otros pedidos y 15 en cuarentena. ¿Cuántas se le pueden prometer y quién decide qué cuenta como comprometido?"
  - "Llega un camión con mercadería: ¿qué se hace desde que se descarga hasta que el stock está disponible para vender, y qué parte es de Compras y qué parte de este tema?"
  - "El conteo da 11 y el sistema dice 13: ¿cómo se corrige, quién lo aprueba y cómo se organiza el conteo para no cerrar el depósito una vez por año?"
  - "¿Cuándo y cuánto reponer un artículo, y cómo se calcula el stock de seguridad?"
  - "¿Cuándo hace falta llevar lote o número de serie, y qué cambia en la recepción, la preparación y la salida?"
  - "Tengo que diseñar el módulo de stock de un sistema para una empresa argentina que despacha mercadería: ¿qué tengo que leer y qué documentos pide el país para mover mercadería?"
aprobado:
---

# Alcance: Inventario y depósitos

El tema cubre el dominio de negocio que lleva el módulo de stock de un ERP y un sistema de gestión de depósitos (WMS): qué mercadería tiene la empresa, dónde y en qué estado, cuánto puede prometer, cómo entra, cómo se aparta y se prepara para salir, cómo se controla que el número sea cierto y cuándo se repone. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), huecos (#104), límites entre dominios (#98), procesos de punta a punta (#99), verticales de Software de gestión (#100) y orden de armado (#101). Es la sesión 4 de 16 (issue #111). El árbol general y los límites los aprobó la persona en el mapa; el árbol de este tema es propuesta de esta sesión y queda para que lo revise en el PR.

Es un tema agnóstico: lo que dice vale para cualquier producto, sin nombrar proveedores, y se sostiene sin software (una ficha por artículo, un galpón con las estanterías numeradas y un conteo a fin de mes hacen lo mismo que un sistema). Lo propio de la Argentina va en una nota aparte.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo (decisión de #98). Este tema es dueño de **la cantidad de cada artículo, en qué lugar y en qué estado**, y de los verbos **recibir, ubicar, reservar, preparar, contar, ajustar y reponer por política**. También es dueño del **cálculo de lo disponible**: cuánto se puede prometer; la promesa al cliente es de Relación con clientes.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Compras y abastecimiento](../Compras-y-abastecimiento/compras-y-abastecimiento.md) | el proveedor, la orden de compra y el control de lo recibido contra lo pedido | En la recepción, Compras mira si llegó lo pedido (90 de 100), en [recepción contra lo pedido](../Compras-y-abastecimiento/Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md), y este tema cuenta, inspecciona, ubica y suma el movimiento al stock. Cuándo y cuánto reponer es política de acá; a quién se le pide y en qué condiciones, de Compras |
| [Cadena de suministro y logística](../Cadena-de-suministro-y-logistica/cadena-de-suministro-y-logistica.md) | lo que pasa entre lugares y el plan agregado: pronóstico, S&OP, red, transporte, despacho, reposición planificada | Preparar el pedido (picking y embalaje) es de acá; desde que sale por la puerta, de Cadena. La reposición por punto de pedido es de acá; la planificada por períodos (DRP) en quien no fabrica, de Cadena. Una transferencia entre depósitos sale de uno y entra en otro acá; el viaje, allá |
| [Producción](../Produccion/produccion.md) | lo que transforma: lista de materiales, MRP, orden de producción | La entrega de materiales a planta y el ingreso del producto terminado son movimientos de stock de acá; el inventario en proceso y el MRP, de Producción |
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | el pedido de venta y la fecha prometida | El pedido confirmado pide la reserva; la cantidad disponible la calcula este tema y la fecha que se escribe en el pedido es de allá ([fecha prometida](../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md)) |
| [Contabilidad](../Contabilidad/contabilidad.md) | la valuación del stock, el costo de lo vendido y los controles | Este tema dice cuántas unidades hay y dónde; cuánto valen, [costo de lo vendido](../Contabilidad/Operaciones/costo-de-lo-vendido.md). La factura del proveedor y su cruce con la orden y la recepción son de allá, en [compras y cuentas a pagar](../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md). El ajuste de un conteo nace acá y se registra allá; quién puede aprobarlo lo dice [separación de funciones](../Contabilidad/Control-interno/separacion-de-funciones.md) |
| [Bases-de-datos](../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md) | cómo se guarda el stock en una base | Acá la regla de negocio (todo cambio es un movimiento; un error se corrige con otro); allá la tabla, la consulta y la transacción |
| [Comercio-electronico/Operaciones-del-comercio](../Comercio-electronico/Operaciones-del-comercio/operaciones-del-comercio.md) | la aplicación a una tienda online: variante, SKU, estados según una plataforma, sobreventa entre canales, fulfillment | Allá, cómo se ve en una tienda; acá, el concepto general que lo sostiene |
| [Software de gestión](../Software-de-gestion/software-de-gestion.md) | las columnas técnicas: datos maestros, documento y estados, cantidades y unidades | Acá qué tiene que registrar el negocio; allá cómo lo resuelve cualquier sistema, en [Columnas técnicas](../Software-de-gestion/Columnas-tecnicas/columnas-tecnicas.md) |
| [Procesos de negocio](../Procesos-de-negocio/procesos-de-negocio.md) | los recorridos que cruzan dominios | Los recorridos enteros están en [del pedido al cobro](../Procesos-de-negocio/del-pedido-al-cobro.md) y [de la compra al pago](../Procesos-de-negocio/de-la-compra-al-pago.md); acá, el tramo adentro del depósito |

Cuando se armó el tema, los vecinos que todavía no existían se nombraron sin enlace; se enlazaron en la sesión 16 del mapa (#123).

## Árbol

```
Inventario-y-depositos/
  inventario-y-depositos.md        el todo: qué registra el dominio, sus cuatro partes y los vecinos; qué leer según lo que estés haciendo
  inventario-y-depositos-en-argentina.md  remito y traslado de bienes, código de operación de traslado, trazabilidad obligatoria
  Existencias/                     qué se tiene y cuánto se puede prometer
    existencias.md                   (entrada) artículo, cantidad, lugar y estado: la fórmula del stock
    articulo.md                      el artículo como dato maestro: código, unidad de medida y conversión, qué lleva stock
    lote-y-serie.md                  trazabilidad, vencimiento, orden de salida (FIFO, FEFO)
    estados-del-stock.md             físico, disponible, comprometido, en tránsito, en cuarentena, bloqueado, de terceros
    disponible-para-prometer.md      el cálculo de lo disponible (ATP): métodos y qué cuenta como comprometido
  Operacion-del-deposito/          lo que pasa adentro, de la puerta de entrada a la de salida
    operacion-del-deposito.md        (entrada) el flujo recibir, guardar, preparar, despachar, y dónde se va el tiempo
    ubicaciones.md                   depósito, zona, ubicación; cómo se direcciona; ubicación fija o libre
    recepcion.md                     descargar, contar, inspeccionar, ubicar; cuarentena y cross-docking
    reserva.md                       apartar stock para un pedido: cuándo, de qué lote y cuándo se libera
    preparacion-de-pedidos.md        picking por pedido, por lote, por zona o por ola; embalaje y control hasta la puerta
  Control-del-stock/               que el número del sistema sea el del estante
    control-del-stock.md             (entrada) inventario permanente o periódico, exactitud de registros
    conteo-ciclico.md                del conteo anual al cíclico: frecuencia, tolerancias, causas de error
    ajustes-y-mermas.md              rotura, robo, vencimiento, diferencias; quién aprueba y cómo queda
  Reposicion/                      cuándo y cuánto reponer
    reposicion.md                    (entrada) para qué se tiene stock y qué cuesta tenerlo o no tenerlo
    punto-de-pedido.md               revisión continua y periódica, mínimo y máximo
    lote-economico.md                cuánto pedir: el EOQ y sus límites
    stock-de-seguridad.md            nivel de servicio, variabilidad de la demanda y del plazo, la fórmula
    clasificacion-abc.md             ABC (y XYZ): a qué artículos mirar más
    indicadores-de-inventario.md     rotación, días de inventario, cobertura, nivel de servicio, exactitud, obsolescencia
  Fundamentos/
    fundamentos-de-inventario-y-depositos.md  (entrada) historia, escuelas, posición contraria y fuentes
    glosario-de-inventario-y-depositos.md     términos con su nombre en inglés
```

## Supuestos

- El árbol general y los límites con los vecinos vienen aprobados del mapa (#94, #98, #101). El árbol del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió; la persona lo revisa en el PR.
- Cuatro verticales: qué se tiene (Existencias), qué se hace con la mercadería adentro (Operación del depósito), que el número sea cierto (Control del stock) y cuándo reponer (Reposición). Las fuentes no lo dividen así: APQC junta el depósito con la logística (4.4) y los cuerpos de certificación ponen el inventario con la planificación. El corte lo pone la base, como dijo la investigación de taxonomías (#96).
- La clasificación ABC va en Reposición aunque también fija la frecuencia del conteo cíclico, porque nace como política de a qué artículos mirar más; el conteo la enlaza.
- La reserva va en Operación del depósito y no en Existencias: es un verbo (apartar), aunque su resultado sea un estado del stock.
- El inventario en proceso y el de consignación en casa del cliente se nombran como estados, sin nota propia.
- Lo de la Argentina va en una sola nota del tema, porque toca la recepción, la salida y el lote, y es corto.
- Mantenido el 2026-11-27 (sesión 16 del mapa del software de gestión, #123): se enlazaron los vecinos que ya existen, y [recepción](Operacion-del-deposito/recepcion.md) dejó de decir que Compras compara contra la factura: Compras compara lo recibido con la orden, y el cruce con la factura es de Contabilidad (decisión de #98).
