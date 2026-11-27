---
resumen: >-
  El presupuesto es la oferta formal que una empresa le hace a un cliente: qué le vende, en qué cantidades, a qué precio, con qué descuentos e impuestos, en qué condiciones y hasta qué fecha vale. Es un documento con estados (borrador, enviado, aceptado, rechazado, vencido) y, si el cliente lo acepta, se convierte en pedido de venta.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 3.5.3 «Develop and manage sales proposals, bids, and quotes»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "SCOR 6.0 Quick Reference, D1.1 «Process Inquiry & Quote»: https://www2.isye.gatech.edu/~lfm/8851/Sources/SCOR/SCORv6quickref.pdf"
  - "ERPNext, Quotation (estados y validez): https://docs.frappe.io/erpnext/user/manual/en/quotation"
  - "Odoo 19, Create quotations (confirmar convierte el registro en pedido): https://www.odoo.com/documentation/19.0/applications/sales/sales/sales_quotations/create_quotations.html"
  - "SAP R/3 4.7, Sales Document Types (consulta y presupuesto como preventa): https://help.sap.com/saphelp_470/helpdata/en/dd/55fb06545a11d1a7020000e829fd11/content.htm"
  - "Relacion-con-clientes/.investigacion/presupuesto-y-pedido.md (secciones A y D)"
aliases: [cotización, quote, quotation, oferta comercial, presupuestar, cotizar]
creado: 2026-11-27
revisado:
---

# Presupuesto

El presupuesto es la oferta formal que una empresa le hace a un cliente: qué le vende, en qué cantidades, a qué precio, con qué descuentos e impuestos, en qué condiciones y hasta qué fecha vale. Es un documento con estados (borrador, enviado, aceptado, rechazado, vencido) y, si el cliente lo acepta, se convierte en pedido de venta.

Es el tercero de los cuatro objetos de [Relación con clientes](../relacion-con-clientes.md). Recibe del [registro del cliente](../Registro-del-cliente/registro-del-cliente.md) a quién se le ofrece y con qué [condiciones comerciales](../Registro-del-cliente/condiciones-comerciales.md) (lista de precios, condición de pago, moneda). Suele colgar de una [oportunidad](../Seguimiento-comercial/oportunidad.md): la oportunidad dice que hay una venta posible y cuánto podría valer; el presupuesto dice exactamente qué se ofrece y por cuánto, y una oportunidad puede tener varios. Si lo aceptan, termina en un [pedido de venta](../Pedido-de-venta/pedido-de-venta.md).

## De qué está hecho un presupuesto

Un presupuesto tiene una cabecera y renglones. La cabecera lleva el cliente, la fecha, la moneda, la condición de pago, la fecha hasta la que vale y un número propio. Cada renglón lleva un producto o servicio, la cantidad, la unidad, el precio unitario, el descuento y el impuesto que le corresponde; el total sale de sumar los renglones. Así lo modelan los sistemas abiertos y los de los proveedores grandes, y así se arma también en papel.

En el recorrido de una venta, el presupuesto llega después de una consulta. SCOR 6.0 los junta en un solo paso del proceso de entrega de producto en stock: D1.1 «Process Inquiry & Quote». APQC 7.4 le dedica el proceso 3.5.3 «Develop and manage sales proposals, bids, and quotes», con pasos como «Develop pricing and scheduling estimates» (3.5.3.9), «Conduct profitability analysis» (3.5.3.10), «Manage internal approvals» (3.5.3.12), «Submit/present bid/proposal/quote to customer» (3.5.3.13) y «Revise bid/proposal/quote» (3.5.3.14). Un ERP de un proveedor grande los agrupa como documentos de preventa, junto con la consulta.

## Los estados del presupuesto

| Estado | Qué significa |
|---|---|
| Borrador | Se está armando; se puede cambiar todo |
| Enviado (abierto) | El cliente lo tiene y la oferta está vigente |
| Aceptado | El cliente dijo que sí; de acá sale el pedido |
| Rechazado (perdido) | El cliente dijo que no; conviene registrar el motivo |
| Vencido | Pasó la fecha hasta la que valía sin respuesta |
| Anulado | Se retiró la oferta por un error o un cambio propio |

Un sistema abierto usa estos mismos estados, con «perdido» en lugar de «rechazado» y «pedido» en lugar de «aceptado», y pide anotar por qué se perdió. El motivo de pérdida del presupuesto y el de la oportunidad suelen ser el mismo dato: si la oportunidad tiene un solo presupuesto, se registra una vez.

El número del presupuesto identifica la oferta ante el cliente y permite que el pedido diga de dónde salió.

> [!NOTE] Sin fuente todavía: cómo numeran los sistemas los presupuestos y sus revisiones (series, prefijos, sufijo de versión).

## Dónde termina la propuesta y empieza el presupuesto

[La propuesta](../../Ventas/La-propuesta/la-propuesta.md) de Ventas es el documento que convence: qué problema del cliente se resuelve, con qué prueba y por qué este precio. El presupuesto es el documento que compromete: qué renglones, a qué precio y hasta cuándo. En una venta simple son el mismo papel; en una venta compleja la propuesta se presenta y el presupuesto va como anexo o se manda después.

Ningún estándar traza esta frontera así. APQC 3.5.3 mezcla pasos de propuesta, como «Perform competitive analysis» (3.5.3.4) y «Understand customer business and requirements» (3.5.3.6), con pasos de presupuesto, como los de precio y aprobación. La división es criterio de la base: Ventas se queda con lo que persuade y este tema con lo que se registra.

## Dos diseños para pasar de presupuesto a pedido

Cuando el cliente acepta, hay dos maneras de modelarlo, y quien construye software elige una:

1. **El mismo registro cambia de estado.** Al confirmarse, el presupuesto pasa a ser pedido de venta: mismo número, mismos renglones. Lo hace un sistema abierto. Es simple, pero se pierde la foto de lo que se ofreció si después se cambia el pedido, salvo que se guarde aparte.
2. **Se crea un documento nuevo que apunta al presupuesto.** El pedido copia los renglones y guarda la referencia; el presupuesto queda en estado «aceptado» o «pedido» y no se toca. Lo hacen otro sistema abierto y un ERP de un proveedor grande, que muestra la cadena de documentos (consulta, presupuesto, pedido, entrega, factura). Cuesta un documento más, pero cada uno conserva lo que dijo.

El segundo diseño es el que conviene cuando un presupuesto se acepta en partes, cuando se aceptan varias versiones o cuando hay que mostrarle al cliente lo que se le ofreció. Esto es criterio de la base; las fuentes muestran los dos diseños sin elegir.

En la Argentina el presupuesto tiene reglas propias: lo que debe contener en ciertos servicios, la oferta que obliga y la leyenda que lo distingue de una factura; están en [Relación con clientes en la Argentina](../relacion-con-clientes-en-argentina.md).

## Qué hay en Presupuesto

- [Precio y descuentos](precio-y-descuentos.md): de dónde sale el precio de cada renglón, cómo se aplica un descuento y quién lo aprueba.
- [Productos configurables](productos-configurables.md): cómo se presupuesta lo que tiene opciones, y por qué el configurador ata el precio con la fecha de entrega.
- [Vigencia y aceptación](vigencia-y-aceptacion.md): hasta cuándo vale, cómo se revisa, cómo lo acepta el cliente (firma, orden de compra, seña) y qué pasa con el precio en el paso a pedido.
