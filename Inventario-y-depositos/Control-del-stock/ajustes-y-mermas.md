---
resumen: >-
  Un ajuste es el movimiento que lleva la cantidad del registro a la que se contó, o que registra una salida que no fue venta (rotura, robo, vencimiento). La merma es la mercadería perdida que esos ajustes dejan a la vista; se registra como un movimiento nuevo con su motivo, nunca pisando el saldo, y lo aprueba alguien distinto de quien cuida el stock.
estado: borrador
estabilidad: semi
fuentes:
  - "ERPNext, Stock Reconciliation: https://docs.frappe.io/erpnext/user/manual/en/stock-reconciliation (según su resumen)"
  - "NRF, National Retail Security Survey 2023: https://nrf.com/research/national-retail-security-survey-2023 (según el resumen del buscador)"
  - "Loss Prevention Research Council, comunicado sobre la NRSS 2023 (26/9/2023): https://lpresearch.org/2023-nrss-release-9-26-23/ (según el resumen del buscador)"
  - "Chicago Booth Review, First Measure, Then Manage: https://www.chicagobooth.edu/review/first-measure-then-manage (según su resumen)"
  - "Wikipedia, Cycle count: https://en.wikipedia.org/wiki/Cycle_count (según su resumen)"
  - "Inventario-y-depositos/.investigacion/existencias-y-control.md (componente 2, ajustes y mermas), 2026-11-27"
aliases: [ajuste de stock, ajuste de inventario, stock adjustment, inventory adjustment, merma, shrinkage, shrink, faltante, sobrante, diferencia de inventario, rotura, robo, hurto, vencimiento, baja de stock, conciliación de stock, stock reconciliation]
creado: 2026-11-27
revisado:
---

# Ajustes y mermas

Un ajuste es el movimiento que lleva la cantidad del registro a la que se contó, o que registra una salida que no fue venta (rotura, robo, vencimiento). La merma es la mercadería perdida que esos ajustes dejan a la vista; se registra como un movimiento nuevo con su motivo, nunca pisando el saldo, y lo aprueba alguien distinto de quien cuida el stock.

Es el último paso del [Control del stock](control-del-stock.md): el [conteo cíclico](conteo-ciclico.md) encuentra la diferencia y el ajuste la registra. También entra por acá lo que se pierde sin conteo de por medio: una caja que se rompe al descargar, un lote que vence en el estante.

## El ajuste es un movimiento con motivo

Un ajuste no cambia el saldo a mano: agrega un movimiento por la diferencia, positivo si sobra y negativo si falta, que dice por qué. Así se conserva qué había antes, quién lo cambió y cuándo. Cómo queda en una base (la fila de tipo `ajuste` con el motivo escrito) está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md), y no se repite acá.

La práctica de software sigue esa forma. Según su resumen, un sistema abierto llama a su conciliación de stock «the process of counting and evaluating material/products, periodically at the year-end»: se carga la cantidad contada y, al validar, la diferencia se asienta contra una cuenta de diferencia, por defecto «Stock Adjustment», o «Temporary Opening» cuando se carga el stock inicial. Es decir, el ajuste tiene dos caras: unidades que cambian acá y un importe que va a la contabilidad.

El importe no es de este tema. Cuánto vale la unidad que se perdió, y la rebaja de valor que no mueve unidades (un stock que sigue en el estante pero vale menos), están en [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md).

## De qué está hecha la merma

La encuesta de seguridad del comercio minorista de Estados Unidos (NRSS 2023, sobre el ejercicio 2022) da la única composición con cifras que se encontró. Se leyó por el resumen del buscador del informe y de un comunicado sobre él, que no son fuentes independientes; la prensa redondea los decimales.

| Causa | Parte de la merma |
|---|---|
| Hurto externo | 36,15 % |
| Hurto interno | 28,85 % |
| Errores administrativos o de proceso | 27,29 % |
| Desconocido | 6 % |
| Otros | 1 % |

La tasa promedio de merma fue de 1,6 % de las ventas, contra 1,4 % el año anterior. Son cifras de comercio minorista, no de un depósito general, y para la Argentina no se encontró un equivalente.

Lo que la tabla muestra, leído por la base: más de un cuarto de la merma, la de errores administrativos o de proceso, es un registro mal hecho sin mercadería que falte. Una devolución que no se cargó, una recepción contada de más o un pedido preparado con otro artículo producen la misma diferencia que un robo. La divulgación del estudio de DeHoratius y Raman nombra esas causas: errores de escaneo, devoluciones y cambios mal tratados, envíos equivocados y mercadería que llega sin inspeccionar.

## Los motivos que conviene distinguir

Si el motivo es un texto libre, el ajuste registra la diferencia pero no sirve para atacar la causa. La lista de motivos es criterio de la base, armada sobre las causas de arriba:

| Motivo | Qué pasó | Cómo se confirma |
|---|---|---|
| Diferencia de conteo | El conteo no coincide con el registro y no se encontró la causa | Recuento y búsqueda en otras ubicaciones |
| Error de registro | Un movimiento anterior se cargó mal (recepción, preparación, devolución) | Se encuentra el documento equivocado |
| Rotura | La mercadería se dañó y no se puede vender | Alguien la vio y la separó |
| Vencimiento | El lote venció en el estante | La fecha del [lote](../Existencias/lote-y-serie.md) |
| Robo o hurto | Se presume que se la llevaron | Rara vez se confirma; queda como presunción |

Un error de registro se corrige mejor anulando o compensando el movimiento equivocado que con un ajuste genérico, porque el documento original queda bien: la recepción dice lo que de verdad llegó. Antes de ajustar una diferencia de conteo, se busca el artículo en sus otras ubicaciones, que es una de las causas de error del conteo que nombra la enciclopedia. Las dos reglas son criterio de la base.

## Quién aprueba un ajuste

El ajuste es la puerta por donde se esconde un faltante: quien se lleva mercadería y además puede ajustar el stock, borra el rastro. Es la combinación que la [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md) prohíbe, custodiar un bien y llevar su registro. Aplicada al stock, y como lectura de la base sobre ese principio: quien cuenta o cuida el depósito propone el ajuste, y lo aprueba alguien que no tiene la mercadería a cargo.

En una empresa chica eso no siempre es posible, y entonces entran los controles compensatorios que describe la misma nota: un supervisor que revisa después los ajustes con su motivo, un reporte de ajustes por persona y por artículo, y el rastro de quién hizo cada paso. Para eso el sistema tiene que guardar en cada ajuste quién lo propuso, quién lo aprobó, cuándo y por qué; cómo se diseñan esos permisos está en [controles sobre los sistemas](../../Contabilidad/Control-interno/controles-sobre-sistemas.md).

> [!NOTE] Sin fuente todavía: umbrales de aprobación (desde qué cantidad o importe un ajuste pide una firma más alta) y una fuente primaria sobre aprobación de ajustes de stock; ninguna de las leídas lo trata.
