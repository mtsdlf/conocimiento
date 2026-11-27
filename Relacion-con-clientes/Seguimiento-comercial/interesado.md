---
resumen: >-
  El interesado (lead) es el registro de alguien que mostró interés en comprar pero todavía no fue calificado: un nombre, una empresa, un medio de contacto y de dónde vino. Se guarda aparte del cliente para no ensuciar la cartera con datos inciertos, y cuando se califica se convierte en cuenta, contacto y oportunidad.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, tabla Lead: https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/lead (como evidencia de práctica)"
  - "SuiteCRM, Leads: https://docs.suitecrm.com/user/sales-relationships/leads/ (como evidencia de práctica)"
  - "Odoo 18.0, «Convert leads into opportunities»: https://www.odoo.com/documentation/18.0/applications/sales/crm/acquire_leads/convert.html (como evidencia de práctica)"
  - "ERPNext, Lead: https://docs.frappe.io/erpnext/user/manual/en/lead (como evidencia de práctica)"
  - "ERPNext, Customer: https://docs.frappe.io/erpnext/user/manual/en/customer (como evidencia de práctica)"
  - "APQC, Process Classification Framework, 3.5.1.2 y 3.5.1.3, copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services"
  - "Relacion-con-clientes/.investigacion/registro-y-seguimiento.md, componente 4"
aliases: [lead, prospecto, cliente potencial, contacto comercial, conversión de lead, lead conversion, origen del lead, lead source]
creado: 2026-11-27
revisado:
---

# Interesado

El interesado (lead) es el registro de alguien que mostró interés en comprar pero todavía no fue calificado: un nombre, una empresa, un medio de contacto y de dónde vino. Se guarda aparte del cliente para no ensuciar la cartera con datos inciertos, y cuando se califica se convierte en cuenta, contacto y oportunidad.

Es el primer objeto del [seguimiento comercial](seguimiento-comercial.md) y el único que cruza a la otra vertical: al convertirse, crea registros en el [registro del cliente](../Registro-del-cliente/registro-del-cliente.md). Llega por formularios, ferias, llamadas en frío o campañas; cómo se lo consigue es [prospección](../../Ventas/Prospeccion/prospeccion.md) y cómo se lo responde, [responder lo que entra](../../Ventas/Prospeccion/responder-lo-que-entra.md).

## Qué es y qué no es

Los sistemas lo definen parecido. Un CRM de un proveedor grande lo describe como un prospecto o una posible oportunidad de venta que, si se califica, se convierte en cuenta, contacto u oportunidad, y si no, se borra o se archiva. Un CRM abierto lo llama un contacto sin calificar, que suele venir de una acción de marketing. Un sistema de gestión abierto, un cliente potencial que podría estar interesado en lo que se vende.

Un interesado no es todavía un cliente (no compró ni tiene condiciones comerciales) ni una oportunidad (no se sabe qué compraría ni por cuánto). Tampoco es un contacto de una cuenta existente: si alguien de un cliente actual pide algo nuevo, eso es una oportunidad sobre esa cuenta, no un interesado nuevo. Esto último es criterio de la base.

## Por qué se separa del cliente

Un sistema abierto lo presenta como un paso de calificación antes de crear la oportunidad, que da tiempo para evaluar antes de pasarlo a un vendedor, y que cada equipo puede apagar. La razón de fondo, que ninguna fuente leída formula como principio, es de datos: un interesado tiene información incierta (un nombre mal escrito, una empresa que puede no existir) y no compromete a nadie. Si se cargara directo como cliente, la cartera se llenaría de registros que nunca compran, y los duplicados se multiplicarían.

La separación tiene costo: dos tablas, una conversión y la posibilidad de que la misma persona esté como interesado y como contacto. Por eso un sistema la deja apagar, y otro define la oportunidad como un interesado ya calificado. Sin software, una planilla de consultas con una columna de estado hace el mismo trabajo.

## Origen y estados

El origen dice cómo llegó: sitio web, feria, boca a boca, llamada en frío, campaña. Un CRM abierto lo registra para medir qué canal trae interesados; un sistema de gestión abierto lo guarda en el interesado y también en la oportunidad, para no perderlo al convertir.

Los estados varían entre sistemas:

| Diseño | Estados | Qué pasa con un descartado |
|---|---|---|
| Un CRM de un proveedor grande | Abierto (nuevo, contactado), calificado, descalificado (perdido, no se puede contactar, ya no está interesado, cancelado) | Queda de solo lectura; se puede reactivar |
| Un CRM abierto | Nuevo, asignado, en proceso, convertido, reciclado, muerto | Puede volver a la cola como reciclado |
| Un sistema de gestión abierto | Mezcla el estado del interesado con la suerte del presupuesto: calificado al crear la oportunidad, convertido cuando hay un pedido, presupuesto perdido si se pierde | Sigue la suerte del presupuesto |

Los dos primeros separan el interesado de la venta; el tercero los ata, y eso hace que un mismo campo diga dos cosas. Para quien diseña, conviene que el estado del interesado termine en la conversión y que lo demás lo lleve la oportunidad.

## La conversión

Convertir es partir el interesado en tres registros: el contacto (quién es), la cuenta (dónde trabaja) y la oportunidad (qué podría comprar). Así lo describe un CRM abierto, que además avisa si ya hay registros parecidos. En otro, el nombre de la empresa del interesado pasa a ser el nombre de la cuenta. En un tercero, al convertir se elige el vendedor y el equipo, y se crea un cliente nuevo, se vincula uno existente o no se vincula ninguno.

El interesado no se borra al convertirse: queda con el rastro de en qué se convirtió. Un CRM grande guarda la oportunidad en la que se calificó; un sistema abierto deja al cliente vinculado a la actividad comercial anterior. Ese rastro es lo que permite medir cuántos interesados de cada origen terminan en venta.

## Duplicados

Un interesado llega muchas veces por varios canales. Un sistema abierto muestra los interesados parecidos y, al fusionar, conserva el más antiguo y le suma los datos del otro; si se fusiona un interesado con una oportunidad, queda la oportunidad. APQC pone la deduplicación dentro de la gestión de datos del cliente (ver [cuenta y contacto](../Registro-del-cliente/cuenta-y-contacto.md)).

Guardar datos de personas que no son clientes tiene reglas: lo general está en [privacidad de datos personales](../../Datos/Gobierno-y-calidad/privacidad-de-datos-personales.md) y lo argentino, en [Relación con clientes en la Argentina](../relacion-con-clientes-en-argentina.md).
