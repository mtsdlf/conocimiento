---
resumen: >-
  La cuenta es el registro de la empresa o la persona a la que se le vende, y el contacto es cada persona con la que se habla dentro de ella. Detrás de los dos está la idea de la parte con roles: una misma persona u organización puede ser cliente, proveedor o las dos cosas, y en una empresa grande quien compra, quien paga y quien recibe pueden ser registros distintos.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, Analysis Patterns, cap. «Organization Structures» (Party, Organization Hierarchy, Accountability), borrador: https://martinfowler.com/apsupp/accountability.pdf (leído en parte)"
  - "Martin Fowler, «Dealing with Roles» (borrador, 20 de julio de 1997): https://martinfowler.com/apsupp/roles.pdf (leído en parte)"
  - "Len Silverston, The Data Model Resource Book, vol. 1, listado de figuras del editor: https://books.wiley.com/authors/len-silverston/models (solo metadatos)"
  - "SAP Library 4.70, «Partner Functions»: https://help.sap.com/saphelp_470/helpdata/en/7f/f6341aac6111d2b44c006094b9ea37/content.htm"
  - "Microsoft Learn, tabla Account: https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account (como evidencia de práctica)"
  - "Salesforce Trailhead, «Understand Account and Contact Relationships»: https://trailhead.salesforce.com/content/learn/modules/accounts_contacts_lightning_experience/understand-account-and-contact-relationships-lightning (como evidencia de práctica)"
  - "Odoo 19.0, Contactos: https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html (como evidencia de práctica)"
  - "ERPNext, Customer: https://docs.frappe.io/erpnext/user/manual/en/customer (como evidencia de práctica)"
  - "David Taber, «How to solve CRM data deduplication dilemmas», CIO.com, 1 de octubre de 2013: https://www.cio.com/article/2382113/how-to-solve-crm-data-deduplication-dilemmas.html"
  - "Relacion-con-clientes/.investigacion/registro-y-seguimiento.md, componente 1"
aliases: [cuenta, contacto, account, contact, party, parte, sold-to, ship-to, bill-to, payer, comprador, pagador, destinatario, jerarquía de cuentas, cuenta matriz, duplicados de clientes]
creado: 2026-11-27
revisado: 2026-11-27
---

# Cuenta y contacto

La cuenta es el registro de la empresa o la persona a la que se le vende, y el contacto es cada persona con la que se habla dentro de ella. Detrás de los dos está la idea de la parte con roles: una misma persona u organización puede ser cliente, proveedor o las dos cosas, y en una empresa grande quien compra, quien paga y quien recibe pueden ser registros distintos.

Es el componente central del [registro del cliente](registro-del-cliente.md). Las [condiciones comerciales](condiciones-comerciales.md) cuelgan de la cuenta, y la [cartera de clientes](cartera-de-clientes.md) reparte las cuentas entre vendedores.

## La parte: persona u organización con roles

Fowler llama parte (party) a la abstracción de las personas y las unidades de una organización, con la persona y la organización como subtipos. Su ejemplo es una empresa de servicios cuyos clientes pueden ser individuos o empresas: lo que se hace igual con los dos se trata en la parte, y lo que difiere, en el subtipo. El problema que resuelve se ve en una libreta de direcciones con personas y empresas por separado, cada una con su domicilio y su teléfono: la duplicación molesta. Fowler dice que el nombre varía entre modelos (persona u organización, entidad legal) y que «parte» se volvió el más común.

Cliente, en este modelo, no es una clase sino un rol. Fowler pone ejemplos de una misma parte con dos roles a la vez, como un agente que también es cliente, y por eso descarta resolverlo con herencia simple. Propone cinco formas de modelar roles; una de ellas pone lo común en un objeto anfitrión y un objeto aparte por cada rol. El listado de figuras del libro de Silverston va en la misma dirección: trae figuras de Party, Party roles y Party relationships, y ninguna se llama Customer (es inferencia desde el índice; el libro no se leyó).

La consecuencia práctica, como criterio de la base: una empresa que es a la vez cliente y proveedor se registra una vez, con dos roles, y no dos veces con dos códigos.

En esta base, **cliente** es una cuenta con el rol de cliente. Cuándo nace ese rol depende del sistema y las fuentes difieren: en unos, al convertir un [interesado](../Seguimiento-comercial/interesado.md) calificado; en otros, con el primer pedido (un sistema abierto marca al interesado como convertido recién cuando hay un pedido de venta).

## Cuenta y contacto, en una tabla o en dos

Los sistemas resuelven la relación entre la empresa y sus personas de dos maneras:

| Diseño | Cómo se ve | Cuándo conviene (criterio de la base) |
|---|---|---|
| Dos tablas | La cuenta es la empresa a la que se le factura; el contacto es una persona que pertenece a una cuenta principal y puede vincularse a otras con un rol | Venta entre empresas, donde se habla con varias personas de cada cliente |
| Una tabla | Un mismo registro de contacto puede ser persona o empresa, y las personas se vinculan a una empresa | Venta a personas o mezcla de los dos, con un modelo más chico |

El primero es el de un CRM de un proveedor grande y su contraparte de otro proveedor; el segundo, el de un sistema abierto que es la idea de la parte hecha producto. Otro sistema abierto distingue el tipo de cliente (empresa, individuo, sociedad) y deja las direcciones y los contactos como registros independientes vinculados al cliente. Para el cliente persona, un CRM de un proveedor grande tiene, según un resumen, una variante de cuenta personal; no se verificó en su documentación.

Los roles del contacto dentro de la compra son un campo de la relación entre contacto y cuenta. Cómo se averiguan es método de ventas y está en [grupo de compra](../../Ventas/Descubrimiento-y-calificacion/grupo-de-compra.md).

## Jerarquías: la casa matriz y sus sucursales

Una cuenta puede tener una cuenta madre: la casa matriz de una cadena y cada local, o un grupo y sus empresas. La jerarquía sirve para ver la matriz y sus hijas en los reportes y, en algunos sistemas, para dibujar el árbol de la cuenta. Fowler aconseja modelarla solo cuando la estructura de la empresa afecta lo que hace el software: si no tenerla no duele, mantener los vínculos no vale lo que cuesta. Una regla que no puede faltar es que no haya ciclos.

Los sistemas leídos permiten una sola cuenta madre por cuenta. Fowler admite varias jerarquías a la vez, o vínculos con tipo, y para eso propone su patrón de responsabilidades (accountability), que él mismo describe como la forma más potente y más compleja de modelar organizaciones.

## Comprador, pagador y destinatario

En una venta a una empresa grande, cuatro papeles pueden recaer en registros distintos. Son las funciones estándar de SAP, con sus nombres en inglés: sold-to (el comprador, quien hace el pedido), ship-to (el destinatario, a dónde se entrega), bill-to (a quién se emite la factura) y payer (el pagador, quien paga). Su documentación los trata como roles que un interlocutor cumple en el proceso; las cuatro funciones son obligatorias por defecto y, en el caso simple, el mismo cliente cumple las cuatro. La definición de cada una, como está arriba, sale de foros y de un resumen del buscador, no de la página oficial leída.

Hay dos niveles de detalle. El completo hace de cada rol un vínculo a otro registro; según foros y resúmenes, el caso común es un pagador central distinto del que compra. El chico guarda direcciones de factura y de entrega dentro de la misma cuenta, sin pagador propio.

El depósito donde el cliente recibe se registra distinto en cada uno: en el modelo chico es una dirección de entrega de la misma cuenta; en el de cuatro roles es un destinatario con registro propio, vinculado al comprador. El chico alcanza mientras el que paga sea el que compra; cuando no, las [condiciones comerciales](condiciones-comerciales.md) y el límite de crédito tienen que leerse del pagador y no del comprador.

## Duplicados y fusión

APQC tiene pasos propios para juntar la información del cliente, interna y de terceros, y para sacar los duplicados (3.5.2.5.1 y 3.5.2.5.2). Taber, en una columna de práctica, enumera de dónde salen: nadie busca antes de crear, las importaciones no detectan duplicados, los formularios y portales insertan sin chequear, y los errores de administración o del propio software. Según él, pasado un 5 % de duplicados los usuarios empiezan a quejarse, y con un 25 % el problema puede poner en riesgo carreras. Son umbrales de un practicante, no una medición.

Como criterio de la base, fusionar dos cuentas no es borrar una: los presupuestos, pedidos y actividades de las dos tienen que quedar colgando de la que sobrevive. Cómo se decide cuál es el [registro de oro](../../Datos/Gobierno-y-calidad/datos-maestros.md) entre sistemas está en [datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md).

> [!NOTE] Sin fuente todavía: una regla general para elegir qué datos se conservan al fusionar dos cuentas.
