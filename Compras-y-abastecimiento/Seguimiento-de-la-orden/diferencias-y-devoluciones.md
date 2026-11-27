---
resumen: >-
  Una diferencia es lo que separa lo recibido de lo pedido: un faltante, un sobrante o algo que llegó y no sirve. Compras decide qué se le pide al proveedor por cada una (esperar el resto, reponer, cambiar o acreditar), y la devolución al proveedor es el documento con que lo rechazado vuelve a él.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Create vendor returns (Dynamics 365 Supply Chain Management): https://learn.microsoft.com/en-us/training/modules/process-purchase-orders-dyn365-supply-chain-mgmt/7-create-vendor-returns"
  - "Oracle, Understanding the RTV Business Process, PeopleSoft Purchasing 9.2 (solo resultados de búsqueda): https://docs.oracle.com/en/applications/peoplesoft/financials-and-supply-chain-management/9.2.056/peoplesoft-purchasing/understanding-rtv-business-process.html"
  - "ERPNext, Purchase Receipt (rechazados; según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt"
  - "ERPNext, Supplier Scorecard (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/supplier-scorecard"
  - "OpenStax, Principles of Financial Accounting (2019), 6.3 (vía Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md): https://openstax.org/books/principles-financial-accounting/pages/6-3-analyze-and-record-transactions-for-merchandise-purchases-using-the-perpetual-inventory-system"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.3.7 y 4.4.2.4: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (2026-11-27), sección 8"
aliases: [diferencias de recepción, faltante, sobrante, rechazo, mercadería rechazada, devolución al proveedor, return to vendor, RTV, vendor return, purchase return, autorización de devolución, RMA, return material authorization, reclamo al proveedor, nota de débito, debit memo, nota de crédito del proveedor, vendor credit note, order exceptions]
creado: 2026-11-27
revisado:
---

# Diferencias y devoluciones

Una diferencia es lo que separa lo recibido de lo pedido: un faltante, un sobrante o algo que llegó y no sirve. Compras decide qué se le pide al proveedor por cada una (esperar el resto, reponer, cambiar o acreditar), y la devolución al proveedor es el documento con que lo rechazado vuelve a él.

Es el último paso de [Seguimiento de la orden](seguimiento-de-la-orden.md): empieza donde la [recepción contra lo pedido](recepcion-contra-lo-pedido.md) encuentra algo que la tolerancia no absorbe. El paso de APQC 7.4 que más se le parece es 4.2.3.7 «Research/Resolve order exceptions» (lectura de esta base); el flujo de lo devuelto está en 4.4.2.4 «Manage flow of returned products».

## Tres diferencias, tres decisiones

| Diferencia | Qué deja en la orden | Qué decide Compras |
|---|---|---|
| Faltante | Un saldo pendiente en el renglón | Esperar el resto o cerrar el renglón |
| Sobrante | Nada, si entra en la tolerancia; si no, se rechaza al recibir | Aceptar el exceso (y ampliar la orden) o devolverlo |
| Rechazo por daño, error o calidad | Unidades recibidas que no cuentan como aceptadas; no bajan el saldo, y si se pide reposición el saldo sube | Pedir reposición, cambio o crédito |

El faltante y el sobrante los resuelven el saldo y la tolerancia, que están en [recepción contra lo pedido](recepcion-contra-lo-pedido.md). Ampliar la orden por un sobrante es un cambio de la orden y pasa por [cambios y cancelaciones](../Orden-de-compra/cambios-y-cancelaciones-de-la-orden.md). La tabla junta las fuentes de esas dos notas; el reparto en tres es criterio de la base.

## Lo que Inventario aparta y lo que Compras reclama

El rechazo se ve primero en el depósito. En un ERP abierto, según su resumen, la cantidad rechazada se carga en el mismo recibo y va a un depósito separado: «Keeping rejected stock separate prevents damaged units from appearing as usable stock». La devolución se crea después, desde ese recibo. Apartar es de Inventario y depósitos, en [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md) y [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md); decidir qué se le pide al proveedor es de acá.

Rechazar no es devolver. En un sistema de compras de un proveedor grande (según resultados de búsqueda), los bienes rechazados al recibir no generan por sí mismos una devolución ni una nota de débito: alguien tiene que crearlas. Si nadie lo hace, las unidades quedan apartadas en el depósito y la deuda con el proveedor no baja (inferencia de la base).

## La devolución al proveedor

Una devolución al proveedor (return to vendor, RTV) saca del stock lo que se le devuelve y reduce lo que se le debe. La documentación de un ERP grande lista los motivos típicos: tamaño o color equivocado, vencimiento, daño en el transporte y mal manejo. La misma fuente da tres maneras de registrarla:

1. Una orden de devolución propia, con su número de autorización y su acción de devolución.
2. Un renglón con cantidad negativa en una orden.
3. Copiar los renglones de la factura original, lo que impide devolver más de lo recibido y usa el precio original.

La autorización de devolución (RMA, return material authorization) es una preautorización que da el proveedor. Según la misma fuente, «most vendors require you to include their Return Material Authorization (RMA) number». Si el artículo se controla por [lote o serie](../../Inventario-y-depositos/Existencias/lote-y-serie.md), hay que decir cuáles unidades se devuelven.

## Qué se le pide a cambio

Según resultados de búsqueda sobre otro sistema grande, la devolución puede ser por crédito, por cambio o por reposición. La devolución por crédito puede generar sola la nota de débito, y en esa nota entran los costos de reposición que cobre el proveedor (restocking fees). Si el proveedor manda un reemplazo en lugar de un crédito, el reemplazo se recibe y su nota se registra contra la orden de devolución.

Los nombres de las notas se cruzan según quién emite. El comprador emite la nota de débito, que baja su deuda con el proveedor; el proveedor responde con una nota de crédito. El asiento es de Contabilidad y está en [compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md).

> [!NOTE] Sin fuente todavía: los plazos de un reclamo al proveedor y quién paga el flete de vuelta. Tampoco hay fuente todavía para las notas de débito y de crédito en la Argentina.

## Cada diferencia es un dato del proveedor

Las diferencias son la materia prima de la [evaluación de proveedores](../Proveedores/evaluacion-de-proveedores.md). Un tablero de un ERP abierto, según su resumen, mide la calidad como cantidad aceptada sobre cantidad recibida, y el cumplimiento como entregas a tiempo sobre entregas totales. Con el ejemplo de la vertical, 88 aceptadas sobre 90 recibidas dan un 97,8 % de calidad en esa entrega (cálculo de la base). Sin la recepción registrada contra la orden, con el rechazo cargado, ese dato no existe (inferencia de la base).
