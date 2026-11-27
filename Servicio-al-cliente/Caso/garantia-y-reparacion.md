---
resumen: >-
  Un caso de garantía y reparación es el que trata un producto que falló o que el cliente quiere devolver: se revisa si está cubierto, se autoriza o se rechaza, y se decide la resolución (reparar, cambiar, devolver la plata o compensar). Lo propio del servicio al cliente es esa decisión y el registro que une los pasos; el paquete, el taller, el stock y la nota de crédito son de otros dominios.
estado: vigente
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), Cross-Industry, 6.1.6, 6.2.4, 6.3 y 6.5.4, copia de la IFRC, leída el 2026-11-27: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "APQC, Process Classification Framework, categoría «Manage Customer Service», 6.1.6, 6.2.4, 6.3 y 6.5.4, copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/6-manage-customer-service"
  - "Shopify, «Return merchandise authorization»: https://www.shopify.com/blog/return-merchandise-authorization (según el resumen del buscador; como evidencia de práctica, junto con páginas parecidas de otros dos proveedores)"
  - "ServiceNow, recorrido de un caso RMA: https://www.servicenow.com/docs/r/order-management/rma-case-user-journey.html (como evidencia de práctica)"
  - "ERPNext, Warranty Claim: https://docs.frappe.io/erpnext/user/manual/en/warranty-claim (como evidencia de práctica)"
  - "Odoo 18.0, servicios posventa del Helpdesk: https://www.odoo.com/documentation/18.0/applications/services/helpdesk/advanced/after_sales.html (como evidencia de práctica)"
  - "Servicio-al-cliente/.investigacion/caso-y-escalamiento.md, componente 4"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, secciones 1 y 5"
aliases: [garantía, reclamo de garantía, warranty claim, RMA, return merchandise authorization, return material authorization, RGA, autorización de devolución, cambio de producto, reparación, servicio técnico, posventa]
creado: 2026-11-27
revisado: 2026-11-27
---

# Garantía y reparación

Un caso de garantía y reparación es el que trata un producto que falló o que el cliente quiere devolver: se revisa si está cubierto, se autoriza o se rechaza, y se decide la resolución (reparar, cambiar, devolver la plata o compensar). Lo propio del servicio al cliente es esa decisión y el registro que une los pasos; el paquete, el taller, el stock y la nota de crédito son de otros dominios.

Es un tipo de [caso](caso.md) que apunta a un producto y no solo a un cliente. APQC lo reparte en varios procesos de su categoría de servicio, en la versión 7.4 de su marco: la política y la oferta de garantía se definen en la estrategia (6.1.6 «Define warranty claims», con 6.1.6.4 «Define warranty related offerings for customers»); la devolución se procesa con los contactos (6.2.4 «Process returns», con 6.2.4.1 «Authorize return»); y el servicio posventa (6.3) incluye registrar productos, los reclamos de garantía con diez pasos, el recupero a proveedores y el servicio del producto, con «Execute product repair» y «Generate service order». ISO 10002 e ITIL lo dejan fuera.

## La autorización de devolución

La autorización de devolución, que el campo llama RMA (return merchandise authorization, y en logística return material authorization), es según un proveedor de comercio electrónico «a business's formal approval for the repair, replacement, or refund of a product under warranty» (según el resumen del buscador). El esquema que describen tres proveedores, que en la práctica cuentan como una sola fuente, tiene cinco pasos, según los resúmenes:

1. La empresa fija una política de devoluciones y garantía.
2. El cliente pide la devolución.
3. La empresa la verifica contra la política y emite un número de autorización.
4. El cliente envía el producto.
5. La empresa lo inspecciona, y de la inspección sale el reembolso, el cambio, el reemplazo o el servicio de garantía.

Fuera de garantía la autorización puede no aplicar, aunque el soporte puede ofrecer una reparación.

## De qué está hecho el caso de garantía

Un sistema abierto abre el reclamo de garantía con el cliente y el número de serie, y de la serie trae el artículo, su descripción y los datos de la garantía. Sus estados son abierto, en curso, cerrado («The repairs have been done») y cancelado («The Warranty Claim was invalid»). Si hace falta una visita al cliente, desde el reclamo se crea una visita.

Un sistema de un proveedor grande arma el caso de devolución por líneas. Cada línea es un producto defectuoso tomado de lo que el cliente tiene instalado, con un código de motivo y la resolución esperada. La garantía y el derecho del cliente se revisan línea por línea; el caso se acepta o se rechaza (si se rechaza, avisa y cierra), se propone una solución y, si hace falta, se crea una tarea para un especialista. Sus estados son borrador, en curso, resuelto y cerrado.

Como lectura de esta base sobre los dos, un sistema necesita en este caso el vínculo con el producto por serie, la revisión de cobertura como paso registrado, la decisión de aceptar o rechazar con su motivo y la resolución elegida por línea.

## Las resoluciones que se disparan desde el caso

Una mesa de ayuda abierta dispara desde el caso cinco resoluciones. El reembolso genera una nota de crédito y pide que la factura esté registrada. El cupón es otra forma de resolver. La devolución genera un movimiento inverso de mercadería, con la opción de cambio que genera una entrega nueva, y solo aparece si hay una entrega registrada. La reparación genera una orden de reparación que, si está en garantía, queda con precio cero. El servicio de campo genera una tarea en el lugar del cliente.

Cada resolución crea un documento en otro dominio, y el caso queda como el registro que los une. Esa división es lectura de esta base sobre dos sistemas.

## Dónde termina el caso y empieza el vecino

El reparto es lectura de esta base sobre dos sistemas; ninguna fuente lo fija.

| Paso | De quién es |
|---|---|
| Revisar la cobertura, autorizar o rechazar, elegir la resolución | Este caso |
| El paquete que vuelve, su envío y su costo en una tienda online | [Devoluciones](../../Comercio-electronico/Operaciones-del-comercio/devoluciones.md), en Comercio electrónico |
| La mercadería devuelta que entra al depósito y si vuelve a la venta | Inventario y depósitos |
| La nota de crédito, el reintegro y su impuesto | Contabilidad, Impuestos y Tesorería |
| La reparación en el taller y la visita al domicilio | Activos y mantenimiento |
| La falla repetida de un producto fabricado | Producción, a partir del [problema](../Escalamiento/problema-y-causa-raiz.md) |

La visita al domicilio se decide acá y se pasa con la [derivación al técnico](../Escalamiento/derivacion-al-tecnico.md); el caso queda abierto hasta que vuelve el resultado (lectura de esta base). Si la devolución anula parte de una venta, el pedido de origen está en [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md).

## Cómo falla

Como lectura de esta base, falla cuando el caso se cierra al autorizar la devolución y nadie sigue si llegó el producto, si se reparó o si se acreditó la plata; cuando la cobertura se decide sin el número de serie y la fecha de compra; y cuando los casos de garantía no se miran juntos, aunque APQC tiene un proceso para evaluar el desempeño de la garantía (6.5.4) que se apoya en ellos.

> [!NOTE] Sin fuente todavía: una fuente neutral (norma o libro) sobre el proceso de garantía. Todo lo de esta nota sale del marco de APQC y de la práctica de sistemas.

Lo que la ley argentina exige de la garantía y del servicio técnico está en [Servicio al cliente en la Argentina](../servicio-al-cliente-en-argentina.md).
