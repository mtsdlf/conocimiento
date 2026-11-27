---
resumen: >-
  Una compra a crédito crea una cuenta a pagar al proveedor, que nace cuando la empresa recibe lo que pidió, se confirma con la factura después de cruzarla con el pedido y la recepción, y se cancela con el pago.
estado: borrador
estabilidad: semi
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 6.3 compras con inventario permanente: https://openstax.org/books/principles-financial-accounting/pages/6-3-analyze-and-record-transactions-for-merchandise-purchases-using-the-perpetual-inventory-system"
  - "Microsoft Learn, Three-way matching (documentación de un proveedor de software): https://learn.microsoft.com/en-us/training/modules/work-invoice-matching-finance/three-way-matching"
  - "Planergy, GRNI reconciliation (blog de un proveedor de software): https://planergy.com/blog/grni-reconciliation-process-benefits"
  - "Oracle, Accrual Process for Perpetual Accruals (documentación de un proveedor de software, vía buscador): https://docs.oracle.com/cd/A60725_05/html/comnls/us/po/rcvacc02.htm"
  - "Contabilidad/.investigacion/operaciones.md (2026-11-27)"
aliases: [compras, cuentas a pagar, cuentas por pagar, accounts payable, proveedores, factura de proveedor, vendor invoice, cruce de tres vías, conciliación de tres vías, three-way match, recibido no facturado, GRNI, goods received not invoiced]
creado: 2026-11-27
revisado:
---

# Compras y cuentas a pagar

Una compra a crédito crea una cuenta a pagar al proveedor, que nace cuando la empresa recibe lo que pidió, se confirma con la factura después de cruzarla con el pedido y la recepción, y se cancela con el pago.

Es el ciclo de la compra al pago visto desde el registro. El pedido al proveedor y la recepción que coincide con lo pedido son del tema Compras y abastecimiento; ejecutar el pago es de Tesorería. Ambos están todavía sin escribir. De acá son el pasivo, su asiento y su saldo por proveedor en las [cuentas corrientes](../Registro/cuentas-corrientes.md).

## La factura del proveedor y el pago

Con inventario permanente, una compra de mercadería a crédito sube el inventario y crea la deuda; el pago la cancela contra la caja. OpenStax 6.3 lo muestra con una compra del 1 de mayo de 67 tabletas a $60, con condiciones 5/10 n/30 (5 % de descuento si se paga en 10 días; si no, el total a 30):

| Cuenta | Debe | Haber |
|---|---|---|
| Inventario | 4.020 | |
| Cuentas a pagar | | 4.020 |

Si paga el 10 de mayo, dentro del plazo, el descuento de $201 baja el costo del inventario:

| Cuenta | Debe | Haber |
|---|---|---|
| Cuentas a pagar | 4.020 | |
| Inventario | | 201 |
| Caja | | 3.819 |

Si paga el 25 de mayo, sin descuento, el asiento es Cuentas a pagar 4.020 contra Caja 4.020. Una devolución al proveedor o una rebaja también reducen la deuda y el inventario. En otro ejemplo del mismo capítulo, sobre 80 impresoras a $100, la empresa devuelve 15 dañadas (Cuentas a pagar 1.500 contra Inventario 1.500), recibe una rebaja de $120 y paga $6.380 con un descuento del 5 % ($319), es decir $6.061 en caja.

Cuando lo comprado es un servicio o un gasto, la factura va contra la cuenta de gasto en lugar del inventario. Cuando es una máquina o un vehículo, contra el activo fijo, como se explica en [activos fijos y amortización](activos-fijos-y-amortizacion.md). Lo que se hace con el impuesto incluido en la factura (el crédito fiscal) es del tema Impuestos, todavía no escrito; acá solo va su cuenta.

## El cruce de tres vías, visto desde el registro

Antes de registrar una factura de proveedor, se la compara con dos documentos: el pedido (qué se pidió y a qué precio) y la recepción (qué llegó y cuánto). Si los tres coinciden dentro de una tolerancia, la factura se registra y queda lista para pagar. Si no, queda retenida hasta que alguien resuelva la diferencia. Las guías de proveedores de software lo describen como dos controles: que la diferencia de precio entre pedido y factura esté dentro de la tolerancia, y que la cantidad facturada coincida con la recibida. Sin ese cruce, según la misma documentación, el sistema podría registrar la factura con errores que afectan la contabilidad más adelante.

El límite con Compras queda así: el cruce termina en Compras cuando lo recibido coincide con lo pedido, y el pasivo nace acá. El cruce es además un control que impide pagar lo que no se pidió o no llegó; se complementa con que quien da de alta al proveedor no sea quien aprueba la factura ni quien paga ([separación de funciones](../Control-interno/separacion-de-funciones.md)) y con los niveles de aprobación de [autorizaciones](../Control-interno/autorizaciones.md).

> [!NOTE] Sin fuente todavía: una fuente primaria (libro de texto o norma de auditoría) para el cruce de tres vías y para lo recibido sin facturar. Todo lo de esta sección y la siguiente sale de documentación de proveedores de software, que cuenta como una sola fuente de práctica.

## Lo recibido sin facturar

Si la mercadería llega antes que la factura, la empresa ya debe algo aunque no tenga el papel del proveedor. Con inventario permanente, la recepción se registra contra una cuenta transitoria de pasivo, Recepciones no facturadas, que se parece a un devengamiento. Según el ejemplo de una guía de un proveedor de software de compras, una recepción de $5.000:

| Cuenta | Debe | Haber |
|---|---|---|
| Inventario | 5.000 | |
| Recepciones no facturadas | | 5.000 |

Cuando llega la factura, la cuenta transitoria se cancela contra la deuda con el proveedor (Recepciones no facturadas al debe, Cuentas a pagar al haber), según esa guía y la documentación de otro proveedor leída por el buscador. La tabla de esa misma guía muestra Inventario al haber en este paso, lo que parece un error de la fuente. Si la factura trae otro importe que el registrado al recibir, la guía revierte lo registrado y vuelve a registrar por el valor de la factura.

El saldo de Recepciones no facturadas tiene que poder explicarse partida por partida: cada línea es algo que llegó y cuya factura falta. Revisarlo al cierre muestra (explicación propia) facturas perdidas o recepciones mal cargadas, y lo trata [conciliaciones](../Control-interno/conciliaciones.md). Con inventario periódico la recepción no se registra hasta la factura o el cierre, y la cuenta no hace falta (según un glosario de proveedor, vía buscador). La diferencia entre los dos sistemas está en [costo de lo vendido](costo-de-lo-vendido.md).

Para quien construye un sistema, el asiento de recepción es la razón para que la recepción sea un documento con fecha propia: si solo existe la factura, el pasivo aparece tarde y el inventario del cierre queda corto. Este punto es inferencia a partir de las fuentes de arriba.
