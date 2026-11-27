---
resumen: >-
  El costo de lo vendido es lo que costaron las mercaderías que la empresa entregó en un período; se calcula con una fórmula de valuación del inventario (PEPS o promedio ponderado bajo NIIF) y nunca deja el stock por encima de lo que se puede recuperar vendiéndolo.
estado: vigente
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIC 2 Inventarios, resumen oficial: https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/"
  - "IFRS Foundation, NIC 2, texto oficial (edición HTML 2026): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html"
  - "IFRS Foundation, NIC 2, copia de una edición anterior del volumen de normas: https://ktkt.uel.edu.vn/Resources/Docs/SubDomain/ktkt/VanBan/IAS/ias2_en.pdf"
  - "IFRS Foundation, NIC 2, Fundamentos de las conclusiones BC9 a BC20 (copia de la AASB): https://www.aasb.gov.au/admin/file/content105/c9/IAS2_BC_1-22.pdf"
  - "OpenStax, Principles of Financial Accounting (2019), 10.3 costo de lo vendido con el método permanente: https://openstax.org/books/principles-financial-accounting/pages/10-3-calculate-the-cost-of-goods-sold-and-ending-inventory-using-the-perpetual-method"
  - "OpenStax, Principles of Financial Accounting (2019), resumen del cap. 10 (vía buscador): https://openstax.org/books/principles-financial-accounting/pages/10-summary"
  - "Contabilidad/.investigacion/operaciones.md (2026-11-27)"
aliases: [costo de lo vendido, costo de ventas, costo de la mercadería vendida, CMV, cost of goods sold, COGS, valuación de inventarios, inventory valuation, PEPS, FIFO, UEPS, LIFO, promedio ponderado, weighted average cost, valor neto de realización, net realisable value, NIC 2, IAS 2]
creado: 2026-11-27
revisado: 2026-11-27
---

# Costo de lo vendido

El costo de lo vendido es lo que costaron las mercaderías que la empresa entregó en un período; se calcula con una fórmula de valuación del inventario (PEPS o promedio ponderado bajo NIIF) y nunca deja el stock por encima de lo que se puede recuperar vendiéndolo.

El costo de lo vendido y el inventario son dos caras del mismo registro: lo que sale del stock pasa a resultados como costo, y lo que queda es el activo del balance. Contar, ubicar y mover el stock es del tema Inventario y depósitos, todavía no escrito; la diferencia que aparece al contar la mide el depósito y la registra la contabilidad. Cómo se reparten los costos de fábrica entre los productos, en una empresa que produce, es de [sistemas de costeo](../Contabilidad-de-gestion/sistemas-de-costeo.md).

## Permanente o periódico

Hay dos maneras de llevar el inventario en el registro. Con el sistema permanente, cada compra suma al inventario y cada venta resta su costo en el momento: el saldo de la cuenta Inventario dice en todo momento cuánto hay. Con el periódico, las compras se acumulan aparte y el costo de lo vendido se calcula al cierre, contando lo que quedó: inventario inicial más compras menos inventario final (fórmula habitual, sin fuente leída). Según el resumen de OpenStax leído por el buscador, en el permanente el promedio se recalcula con cada cambio de unidades, y en el periódico es el total disponible dividido por las unidades disponibles.

El permanente es el que exige que cada venta tenga dos asientos, el del ingreso y el del costo (ver [operaciones](operaciones.md)). Para un sistema es el natural: cada entrada y salida es una fila, y el saldo es la suma, como en el [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md). En planilla, el mismo diseño está en [planilla de stock](../../Planillas-de-calculo/Diseno-de-planillas/planilla-de-stock.md). El periódico sigue sirviendo cuando no se puede registrar el costo de cada venta en el momento, y el conteo físico es lo que le da el costo del período. Es inferencia propia.

## PEPS, promedio ponderado y UEPS sobre las mismas compras

Si los precios de compra cambian, la misma venta puede tener costos distintos según qué unidades se suponga que salieron. La NIC 2 pide identificación específica para los ítems que no son intercambiables (por ejemplo, bienes hechos para un proyecto) y, para el resto, "first-in, first-out (FIFO) or weighted average cost formula", la misma para inventarios de naturaleza y uso parecidos. En castellano se dicen PEPS (primero entrado, primero salido) y promedio ponderado; el promedio se puede calcular por período o con cada recepción.

OpenStax 10.3 compara los métodos sobre un mes de julio con precios que suben. Inventario inicial de 150 unidades a $21; el 5 vende 120 a $36; el 10 compra 225 a $27; el 15 vende 180 a $39; el 25 compra 210 a $33. Quedan 285 unidades; el costo disponible total es $16.155 y las ventas, $11.340.

| Método | Costo de lo vendido | Inventario final | Margen bruto |
|---|---|---|---|
| PEPS | 7.200 | 8.955 | 4.140 |
| UEPS | 7.380 | 8.775 | 3.960 |
| Promedio ponderado | 7.253 | 8.902 | 4.087 |

La página aclara que no muestra los asientos. Derivados de sus cifras, la venta del 5 de julio queda así:

| Cuenta | Debe | Haber |
|---|---|---|
| Cuentas a cobrar | 4.320 | |
| Ventas | | 4.320 |
| Costo de lo vendido | 2.520 | |
| Inventario | | 2.520 |

Con PEPS, el costo de la venta del 15 de julio es $4.680: 30 unidades que quedaban a $21 y 150 de la compra del 10 a $27 (cálculo propio).

Con precios que suben, PEPS da el menor costo, el mayor margen y el mayor inventario. El método cambia el resultado y el balance; la caja es la misma con cualquiera, porque las compras y las ventas no cambian. La norma pide usar la misma fórmula para inventarios de naturaleza y uso parecidos.

## Por qué la NIC 2 prohíbe UEPS

UEPS (último entrado, primero salido) supone que las últimas unidades compradas son las primeras que se venden. OpenStax lo enseña como un método más, porque el US GAAP lo admite. La NIC 2 lo prohíbe: "The Standard does not permit the use of the last-in, first-out (LIFO) formula to measure the cost of inventories."

El por qué está en los fundamentos de la norma. El IASB dice que UEPS "is generally not a reliable representation of actual inventory flows" y que lo eliminó "because of its lack of representational faithfulness of inventory flows". Agrega que un motivo fiscal no justifica un tratamiento contable. Las dos fuentes no se contradicen: son marcos distintos, y la nota que corresponde a cada empresa está en [normas contables](../Estados-contables/normas-contables.md).

## El valor neto de realización pone un techo

El inventario no puede quedar en el balance por más de lo que se va a recuperar con él. La NIC 2 lo dice así: "Inventories shall be measured at the lower of cost and net realisable value." El valor neto de realización es el precio de venta estimado en el curso normal del negocio menos los costos de terminar el producto y venderlo. Si cae por debajo del costo, la diferencia se rebaja del inventario contra resultados.

La rebaja se hace normalmente ítem por ítem, no por una categoría entera como "productos terminados", y el valor neto de realización se vuelve a estimar en cada período.

> [!NOTE] Sin fuente todavía: un ejemplo con números de una rebaja a valor neto de realización.

Para quien construye un sistema, lo anterior pide guardar el costo de cada entrada (PEPS necesita las capas por fecha y precio; el promedio, el costo acumulado y las unidades) y poder registrar una rebaja de valor que no mueve unidades.
