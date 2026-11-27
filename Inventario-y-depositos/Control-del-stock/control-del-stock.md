---
resumen: >-
  Control del stock es la parte del dominio que se ocupa de que la cantidad del registro sea la que está en el estante: cuándo se actualiza esa cantidad, cómo se cuenta para encontrar las diferencias y cómo se corrigen sin perder el rastro. Todo lo que se calcula sobre el stock, de lo disponible al punto de pedido, depende de que esto funcione.
estado: borrador
estabilidad: estable
fuentes:
  - "DeHoratius y Raman (2008), Inventory Record Inaccuracy: An Empirical Analysis, Management Science 54(4), 627-641, abstract: https://doi.org/10.1287/mnsc.1070.0789 y https://ideas.repec.org/a/inm/ormnsc/v54y2008i4p627-641.html (según su resumen; el texto completo no se leyó)"
  - "Chicago Booth Review, First Measure, Then Manage (divulgación del mismo estudio): https://www.chicagobooth.edu/review/first-measure-then-manage (según su resumen)"
  - "Kök y Shang (2007), Inspection and Replenishment Policies for Systems with Inventory Record Inaccuracy, MSOM 9(2), 185-205: https://doi.org/10.1287/msom.1060.0136 (según su resumen)"
  - "Odoo 19, Inventory valuation, periódico frente a permanente: https://www.odoo.com/documentation/19.0/applications/finance/accounting/get_started/inventory_valuation.html (solo vía buscador)"
  - "Wikipedia, Cycle count: https://en.wikipedia.org/wiki/Cycle_count"
  - "Inventario-y-depositos/.investigacion/existencias-y-control.md (componente 2) y fundamentos-y-contraria.md (sección 4.1), 2026-11-27"
aliases: [control del stock, control de inventario, inventory control, exactitud del inventario, exactitud de registros, inventory record accuracy, IRA, inexactitud del registro, inventory record inaccuracy, inventario permanente, perpetual inventory, inventario periódico, periodic inventory]
creado: 2026-11-27
revisado:
---

# Control del stock

Control del stock es la parte del dominio que se ocupa de que la cantidad del registro sea la que está en el estante: cuándo se actualiza esa cantidad, cómo se cuenta para encontrar las diferencias y cómo se corrigen sin perder el rastro. Todo lo que se calcula sobre el stock, de lo disponible al punto de pedido, depende de que esto funcione.

Es una de las cuatro partes de [Inventario y depósitos](../inventario-y-depositos.md). [Existencias](../Existencias/existencias.md) dice qué hay, en qué lugar y en qué estado; [Operación del depósito](../Operacion-del-deposito/operacion-del-deposito.md) cambia esas cantidades con cada recepción, reserva y salida, y es ahí donde nacen casi todos los errores. Control del stock cuenta y corrige. Lo que consume sus resultados es [disponible para prometer](../Existencias/disponible-para-prometer.md), la [reserva](../Operacion-del-deposito/reserva.md) y la [Reposición](../Reposicion/reposicion.md). La exactitud del registro como indicador está en [indicadores de inventario](../Reposicion/indicadores-de-inventario.md).

## El registro está mal más seguido de lo que se cree

La inexactitud del registro es la causa raíz que este control ataca. DeHoratius y Raman (2008) revisaron casi 370.000 registros de stock en 37 tiendas de un minorista de Estados Unidos y encontraron que el 65 % no coincidía con lo que había en el estante (según el resumen del artículo). Su punto de partida: «Traditional inventory models, with a few exceptions, do not account for the existence of inventory record inaccuracy».

Según el mismo resumen, auditar reduce la inexactitud, y la complejidad del local y la estructura de distribución la aumentan. La categoría de producto explica el 26,4 % de la varianza y la tienda, el 2,7 %: el error depende más de qué artículo es que de dónde está. Una nota de divulgación del mismo estudio lista las causas: errores de escaneo en la caja, devoluciones y cambios mal tratados, envíos equivocados desde el centro de distribución, mercadería que llega sin inspeccionar, más variedad de producto y locales saturados. Los envíos directos del proveedor tuvieron registros más exactos que los que pasaban por el centro de distribución del propio minorista.

> [!IMPORTANT]
> **Las cifras discrepan entre lecturas del mismo estudio.** El resumen del artículo habla de casi 370.000 registros; la nota de divulgación, de «nearly 240,000 items across 37 stores» con diferencias y de una caída de ganancias de más del 10 %. Pueden ser universos distintos (registros revisados frente a artículos con diferencia), pero no se pudo verificar en el texto completo. En los dos casos es un solo minorista: el 65 % no se generaliza a cualquier depósito.

Kök y Shang (2007) modelan qué hacer cuando se sabe que el registro miente. Según su resumen, conviene una política que inspecciona cuando el registro cae bajo un umbral y pide hasta un nivel que depende del tiempo desde la última inspección. Un [conteo cíclico](conteo-ciclico.md) con niveles que dependen del estado rinde casi igual. El trabajo también estima cuánto vale tener datos exactos, por ejemplo con RFID.

La consecuencia, que es inferencia de la base: el disponible, la reserva y el punto de pedido heredan el error del registro. Un sistema que calcula con precisión sobre un número equivocado da números falsos con apariencia de exactos, y un faltante que el registro no ve tampoco dispara la reposición.

## Permanente o periódico: cuándo se actualiza la cantidad

Hay dos reglas para saber cuándo cambia la cantidad del registro. En el inventario permanente, cada movimiento (una recepción, una venta, una transferencia) la actualiza en el momento, y el registro dice en todo momento cuánto debería haber. En el periódico, la cantidad se conoce cuando se cuenta; entre un conteo y otro, el registro no la sigue.

La práctica de software trata esta distinción como una regla de valuación: según el resumen del buscador, la documentación de un sistema abierto dice que el periódico actualiza el valor del inventario solo al cierre y el permanente, a medida que ocurren las transacciones. Esa parte (cuánto vale el stock y cuándo se reconoce el costo) es de Contabilidad y está en [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md). Acá importa solo la cantidad.

Que un sistema de gestión lleve inventario permanente es casi automático, porque cada documento genera su movimiento; cómo se guarda está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md). El permanente no hace innecesario contar: dice cuánto debería haber, y solo el conteo dice cuánto hay. La enciclopedia, según su resumen, define el conteo cíclico justamente como una auditoría del inventario permanente.

> [!NOTE] Sin fuente todavía: la definición de «perpetual inventory» e «inventory record accuracy» del APICS Dictionary, y una meta de exactitud con fuente primaria.

## Contar, comparar y corregir

El control es un ciclo de tres pasos, que es criterio de la base armado sobre las fuentes de los componentes:

1. **Contar** una parte del stock, según un calendario que reparte el depósito a lo largo del año. Cómo se elige qué contar y cuándo está en [conteo cíclico](conteo-ciclico.md).
2. **Comparar** lo contado con lo que dice el registro en ese mismo momento. Una diferencia puede ser mercadería que está en otra ubicación o un movimiento que todavía no se cargó, y se revisa antes de corregir.
3. **Corregir** con un movimiento nuevo que lleva el registro a lo contado y dice por qué. Quién lo aprueba y cómo se clasifica el motivo está en [ajustes y mermas](ajustes-y-mermas.md).

El ajuste corrige el número, pero no la causa. Si las diferencias de un artículo vuelven a aparecer, la causa está en algún paso de la [recepción](../Operacion-del-deposito/recepcion.md), la [preparación de pedidos](../Operacion-del-deposito/preparacion-de-pedidos.md) o las devoluciones, donde están casi todas las causas que lista la divulgación del estudio de DeHoratius y Raman. Un control que solo ajusta deja el registro bien un día y mal al siguiente; esto es inferencia de la base.

## Lo que hay en Control del stock

- [Conteo cíclico](conteo-ciclico.md): del inventario anual al conteo de una parte por vez; cómo se fija la frecuencia (por clase o por ubicación) y qué errores mete el propio conteo.
- [Ajustes y mermas](ajustes-y-mermas.md): cómo se registra una diferencia, una rotura, un robo o un vencimiento, de qué está hecha la merma y quién aprueba el ajuste.
