---
resumen: >-
  Un software de gestión se cobra de dos formas: una licencia perpetua más un mantenimiento anual, o una suscripción que paga el derecho de uso por período. Dentro de cada forma, el proveedor decide la unidad de cobro: el usuario, el tipo de usuario, el módulo, la empresa o el comprobante.
estado: borrador
estabilidad: semi
fuentes:
  - "CIO.com, SAP raises software maintenance fees for new customers (2008-04-10): https://www.cio.com/article/276860/enterprise-resource-planning-sap-raises-software-maintenance-fees-for-new-customers.html (leído)"
  - "Avasant (investigación de Frank Scavo, Computer Economics), High Software Maintenance Fees and What To Do About Them (febrero de 2005): https://avasant.com/report/high-software-maintenance-fees-and-what-to-do-about-them/ (leído)"
  - "Página de precios de un ERP en la nube para pymes, consultada el 2026-11-27: https://www.microsoft.com/en-us/dynamics-365/products/business-central/pricing"
  - "Página de precios de un ERP de código abierto, consultada el 2026-11-27: https://www.odoo.com/pricing"
  - "Kinnunen y Kinnunen (ICSIM 2025), Subscription vs. Perpetual: Analysis of Cloud ERP and Traditional ERP Operational Impact on IS Life Cycle Costs (según su resumen): https://jyx.jyu.fi/jyx/Record/jyx_123456789_104922"
  - "Software-de-gestion/.investigacion/mercado-y-economia.md (2026-11-27), sección 1"
aliases: [licencia perpetua, perpetual license, mantenimiento, maintenance fee, soporte, support fee, suscripción, subscription, unidad de cobro, usuario nombrado, named user, usuario concurrente, concurrent user, usuario liviano, light user, licenciamiento de ERP, ERP licensing]
creado: 2026-11-27
revisado:
---

# Licencia y suscripción

Un software de gestión se cobra de dos formas: una licencia perpetua más un mantenimiento anual, o una suscripción que paga el derecho de uso por período. Dentro de cada forma, el proveedor decide la unidad de cobro: el usuario, el tipo de usuario, el módulo, la empresa o el comprobante.

Es el lado del precio en [Mercado y economía](mercado-y-economia.md): lo que paga el cliente. Cómo se reparte esa plata dentro del proveedor, y cuánto deja cada línea, está en [economía del proveedor](economia-del-proveedor.md). La suscripción como modelo de negocio en general (ingreso recurrente, costo de adquisición, valle de caja) está en [SaaS](../../Emprender/Modelo-de-negocio/saas.md), y la métrica de valor como idea de precio, en [pricing y empaquetado](../../Producto/Monetizacion/pricing-y-empaquetado.md#la-métrica-de-valor-por-qué-unidad-se-cobra).

## Licencia perpetua y mantenimiento

Con la licencia perpetua, el cliente paga una vez el derecho a usar una versión del software, en sus propios servidores. Aparte paga cada año el mantenimiento (también llamado soporte): el derecho a recibir correcciones, versiones nuevas y atención técnica. El mantenimiento se fija como un porcentaje de lo que costó la licencia.

Dos fuentes dan el rango, las dos viejas y ninguna con método publicado:

| Fuente | Qué dice |
|---|---|
| CIO.com (2008) | Los proveedores cobran «usually 20 percent to 25 percent of the net license price per year». Uno de los proveedores más grandes pasó a sus clientes nuevos de un soporte de 17 % a uno de 22 %; otro cobraba 22 % hacía años. Un analista que revisó lo que pagaban los compradores encontró «about 26 percent» |
| Avasant, con Computer Economics (2005) | «A few years ago, 15-18% of the software license fee was a typical benchmark»; ahora los proveedores cotizan «20% or even more» |

Es un dato de dinero con dos fuentes independientes que coinciden en el orden: alrededor de un quinto de la licencia por año. La cifra actual de cada proveedor no se verificó en su política publicada.

La consecuencia, en lectura de esta base, es que la licencia perpetua ya era un negocio recurrente antes de la nube. Con un mantenimiento de 20 % anual, en cinco años el cliente pagó otra licencia entera en soporte. Por eso el cliente que deja de pagar el mantenimiento pierde las versiones nuevas, y en un software que tiene que seguir los cambios de la norma fiscal eso lo deja fuera de la ley en poco tiempo.

## La suscripción

En la suscripción el cliente paga por mes o por año el derecho de uso, el soporte y las versiones nuevas juntos; si el software corre en la nube del proveedor, paga también la operación. No compra nada que le quede: si deja de pagar, deja de usar. El precio suele cotizarse por mes y facturarse por año, como en la página de precios de un ERP en la nube para pymes consultada el 2026-11-27, que cobra «user/month, paid yearly».

Quién termina pagando más en el ciclo completo no tiene respuesta general. El único estudio con método hallado, el de Kinnunen y Kinnunen (2025), compara cuatro empresas grandes que pasaron a la suscripción y advierte, según su resumen, que el costo total de la nube es difícil de calcular. Las comparaciones con cifras vienen de partes interesadas y están en [costo total para quien compra](costo-total-para-quien-compra.md).

## La unidad de cobro

Sea licencia o suscripción, el proveedor elige qué cuenta. No se encontró un estudio que compare unidades de cobro en software de gestión; lo que sigue es la práctica tal como se ve en las páginas de precios, más la lectura de esta base.

- El usuario. La unidad más común. El usuario nombrado es una persona con su cuenta; el usuario concurrente es una sesión abierta a la vez, que deja compartir licencias entre turnos.
- El tipo de usuario. Un software de gestión tiene muchos usuarios que miran o aprueban y pocos que cargan. Por eso existe el usuario liviano: en la página de precios citada, el usuario limitado cuesta la décima parte del completo. En la de un ERP de código abierto, los clientes y proveedores que entran al portal no cuentan como usuarios.
- El módulo o la función. Contabilidad, depósito o producción se venden aparte, o por paquetes. En la página del ERP de código abierto, llevar varias empresas o usar la API obliga al plan más caro: se cobra la [estructura de la organización](../Columnas-tecnicas/estructura-de-la-organizacion.md) y la [integración](../Columnas-tecnicas/integracion-y-migracion.md).
- El volumen de negocio. Comprobantes emitidos por mes, cuentas de canal conectadas. Es la unidad de los sistemas en la nube para pymes en la Argentina ([sistemas de gestión en el comercio](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md#instalado-o-en-la-nube)).

La elección tiene efectos. Cobrar por usuario empuja al cliente a compartir cuentas, y eso rompe la [auditoría de cambios](../Columnas-tecnicas/auditoria-de-cambios.md) y la [separación de funciones](../Columnas-tecnicas/permisos-y-separacion-de-funciones.md), que necesitan saber quién hizo qué. Cobrar por comprobante sigue al tamaño del negocio y no castiga sumar gente, pero hace caro al cliente que factura mucho con poco margen. Las dos son lecturas de esta base, sin estudio que las mida. La discusión del precio por asiento frente al uso, con la IA de por medio, está en [SaaS](../../Emprender/Modelo-de-negocio/saas.md#cómo-falla).

> [!NOTE] Sin fuente todavía: un estudio que compare unidades de cobro en software de gestión y su efecto en ingresos o en retención; la política de soporte publicada hoy por algún proveedor grande.
