---
resumen: >-
  El CRM es la categoría de software de gestión que lleva el registro del cliente y lo que pasa antes del pedido (el interesado, la oportunidad, las actividades del vendedor), y que a veces suma la atención y el marketing. Bajo esa sigla el mercado vende tres productos distintos.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, «Customer relationship management» (leída en parte; los tres componentes vienen de la literatura académica que cita, como Buttle 2004): https://en.wikipedia.org/wiki/Customer_relationship_management"
  - "Gartner, definición de CRM citada por terceros (resumen): https://www.smartsheet.com/content-center/best-practices/project-management/project-management-guide/professional-services-project-management"
  - "Gartner, Magic Quadrant for Sales Force Automation Platforms, julio de 2025 (resumen): https://www.gartner.com/en/documents/6747034"
  - "CX Today, resumen del cuadrante de automatización de ventas 2025: https://www.cxtoday.com/crm/gartner-magic-quadrant-for-sales-force-automation-platforms-sfa-2025-the-rundown/"
  - "Lista de módulos de un ERP de código abierto (leída): https://github.com/frappe/erpnext/blob/develop/erpnext/modules.txt"
  - "Documentación de aplicaciones de otro ERP de código abierto, versión 18.0 (leída): https://www.odoo.com/documentation/18.0/applications.html"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md y taxonomias-externas-96.md (2026-11-27)"
aliases: [CRM, customer relationship management, gestión de la relación con el cliente, sistema de CRM, SFA, sales force automation, automatización de la fuerza de ventas, CRM operativo, CRM analítico, CRM colaborativo]
creado: 2026-11-27
revisado:
---

# CRM

El CRM es la categoría de software de gestión que lleva el registro del cliente y lo que pasa antes del pedido (el interesado, la oportunidad, las actividades del vendedor), y que a veces suma la atención y el marketing. Bajo esa sigla el mercado vende tres productos distintos.

Es una de las [categorías de producto](categorias-de-producto.md). El dominio que lleva es [Relación con clientes](../../Relacion-con-clientes/relacion-con-clientes.md): el [registro del cliente](../../Relacion-con-clientes/Registro-del-cliente/registro-del-cliente.md), el [seguimiento comercial](../../Relacion-con-clientes/Seguimiento-comercial/seguimiento-comercial.md) y, según el producto, el presupuesto. Qué datos, estados y reglas tiene cada uno de esos objetos está allá; acá, cómo se empaquetan y dónde corta la caja.

## Estrategia o software

La sigla nombra dos cosas. Gartner, según la cita de terceros, define al CRM como «a business strategy that optimizes revenue and profitability while promoting customer satisfaction and loyalty». Quien construye o implementa software usa la sigla para el sistema que guarda clientes y oportunidades. Relación con clientes ya discute la lectura estratégica y elige la segunda; este tema usa la misma.

## Tres productos bajo una sigla

Wikipedia, apoyada en la literatura académica del CRM, distingue tres componentes: el operativo, que automatiza ventas, marketing y servicio con una vista única del cliente; el analítico, que analiza los datos de clientes; y el colaborativo, que comparte información con proveedores y distribuidores. El mercado corta de otra manera, pero también en tres. Según resúmenes, Gartner evalúa por separado las plataformas de automatización de la fuerza de ventas (julio de 2025) y las suites de centro de atención al cliente (octubre de 2025), y el marketing va por otro camino.

| Producto | Qué lleva | Dominio de esta base |
|---|---|---|
| Automatización de la fuerza de ventas | Interesados, oportunidades, actividades, embudo, previsión | [Relación con clientes](../../Relacion-con-clientes/relacion-con-clientes.md); el embudo como método, en [Ventas](../../Ventas/ventas.md) |
| Atención al cliente | El caso, su escalamiento y sus tiempos | [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md); como categoría, en [mesa de ayuda](servicio-de-campo-y-mesa-de-ayuda.md) |
| Automatización de marketing | Campañas, segmentos, envíos | [Marketing](../../Marketing/marketing.md) |

Para quien construye, la consecuencia es que «hacer un CRM» puede querer decir cualquiera de los tres, y que lo común a los tres es el registro del cliente (lectura de esta base). La lectura analítica del CRM, juntar datos de clientes para decidir, es inteligencia de negocio y está en [Visualización y BI](../../Datos/Visualizacion-y-BI/visualizacion-y-bi.md).

## Dónde termina frente al ERP: el pedido

La frontera con el [ERP](erp.md) es la pregunta de quién es dueño del pedido. La [historia del CRM](../../Relacion-con-clientes/Fundamentos/historia-del-crm.md#del-fichero-al-sistema-de-un-equipo) cuenta por qué el mismo dominio quedó partido en dos cajas: el CRM creció desde el programa de contactos del vendedor, y el presupuesto y el pedido crecieron junto al stock y la facturación. Un ERP de código abierto lo muestra en su estructura: separa el módulo de CRM (antes del pedido) del de ventas (del pedido en adelante). Otro pone CRM, ventas, punto de venta y suscripciones en una misma familia de ventas.

Hay tres cortes posibles, y cada producto elige uno (lectura de esta base):

1. El CRM llega hasta la oportunidad ganada; el presupuesto y el pedido son del ERP.
2. El CRM hace también el presupuesto; al aceptarse, el pedido nace en el ERP.
3. El CRM lleva todo hasta el pedido y el ERP recibe el pedido confirmado para reservar, despachar y facturar.

Cuanto más lejos llega el CRM, más datos del ERP necesita (lectura de esta base): la lista de precios, la condición de pago, el límite de crédito y el disponible para prometer. Esos datos están en las [condiciones comerciales](../../Relacion-con-clientes/Registro-del-cliente/condiciones-comerciales.md) y en [disponible para prometer](../../Inventario-y-depositos/Existencias/disponible-para-prometer.md), y alguien tiene que decidir dónde se mantienen.

## Con qué más se pisa

- Con la [mesa de ayuda y el servicio de campo](servicio-de-campo-y-mesa-de-ayuda.md): el caso del cliente y la orden de trabajo que sale de él. Si la atención vive en el CRM, el caso queda junto al historial comercial; si vive en otra caja, hay que conectarlos.
- Con el [PSA](psa.md): la oportunidad de una firma de servicios alimenta la demanda de personas, y un PSA completo suma su propio CRM.

## El cliente como dato maestro entre cajas

El cliente es el dato que más se duplica entre CRM y ERP. El vendedor lo da de alta en el CRM; la administración lo necesita en el ERP con su clave fiscal y su condición frente al impuesto. Que haya un solo registro de cada cliente entre los dos es el problema del [registro de oro](../../Datos/Gobierno-y-calidad/datos-maestros.md), y cómo se decide qué sistema manda en cada dato está en [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md). Por qué «un solo registro» es un buen objetivo y un mal supuesto está en [mitos del CRM](../../Relacion-con-clientes/Fundamentos/mitos-del-crm.md), junto con las cifras de fracaso de proyectos de CRM y lo que de verdad miden.
