---
resumen: >-
  Los términos del tema Relación con clientes, cada uno con su nombre en inglés, una definición corta y la nota donde vive.
estado: borrador
estabilidad: estable
fuentes:
  - "ASCM, CPIM 2019 Excerpt, con definiciones del APICS Dictionary, 15.ª ed.: https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf"
  - "APQC, Process Classification Framework 7.4, categoría 3.5: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Fowler, Analysis Patterns, capítulo Organization Structures (borrador): https://martinfowler.com/apsupp/accountability.pdf"
  - "Relacion-con-clientes/.investigacion/ (cuatro informes, 2026-11-27)"
aliases: [glosario de CRM, CRM glossary, términos de relación con clientes]
creado: 2026-11-27
revisado:
---

# Glosario de relación con clientes

Los términos del tema Relación con clientes, cada uno con su nombre en inglés, una definición corta y la nota donde vive.

No hay un glosario canónico y neutral del campo: los sistemas usan nombres distintos para lo mismo, y el corte entre interesado y oportunidad cambia de uno a otro. Estas son las palabras que usa esta base, en un sentido cada una. Los términos del método de vender (calificación, grupo de compra, tasa de cierre) están en el [glosario de ventas](../../Ventas/Fundamentos/glosario-de-ventas.md).

## Los objetos

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Cuenta | Account | El cliente como organización (o persona) a la que se le vende y se le factura | [cuenta y contacto](../Registro-del-cliente/cuenta-y-contacto.md) |
| Contacto | Contact | Una persona vinculada a una cuenta, con su rol en la compra | [cuenta y contacto](../Registro-del-cliente/cuenta-y-contacto.md) |
| Parte | Party | La persona u organización registrada una sola vez, que puede cumplir varios roles (cliente, proveedor); término de Fowler | [cuenta y contacto](../Registro-del-cliente/cuenta-y-contacto.md) |
| Comprador, pagador, destinatario | Sold-to, payer (o bill-to), ship-to | Los roles que pueden tener distintas cuentas en una misma venta: quién pide, quién paga y a dónde se entrega | [cuenta y contacto](../Registro-del-cliente/cuenta-y-contacto.md) |
| Interesado | Lead | Alguien que mostró interés y todavía no se calificó; al calificarse se convierte en cuenta, contacto u oportunidad | [interesado](../Seguimiento-comercial/interesado.md) |
| Oportunidad | Opportunity | El registro de una venta posible a una cuenta, con monto, etapa, probabilidad y fecha estimada de cierre | [oportunidad](../Seguimiento-comercial/oportunidad.md) |
| Actividad | Activity | Una acción hecha o por hacer con un cliente (llamada, visita, correo, tarea), colgada del objeto al que se refiere | [actividad](../Seguimiento-comercial/actividad.md) |
| Presupuesto, cotización | Quotation, quote | La oferta formal con renglones, precios, condiciones y fecha de vigencia | [presupuesto](../Presupuesto/presupuesto.md) |
| Pedido de venta | Sales order | El compromiso de entregar productos o servicios a un cliente, en una fecha y a un precio | [pedido de venta](../Pedido-de-venta/pedido-de-venta.md) |
| Pedido abierto, contrato marco | Blanket order, sales agreement | Un acuerdo por una cantidad o un monto a lo largo de un período, del que se liberan pedidos | [tipos de pedido](../Pedido-de-venta/tipos-de-pedido.md) |

## Los datos y los estados

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Condición de pago | Payment terms | Cuándo vence lo que el cliente debe (contado, a 30 días) | [condiciones comerciales](../Registro-del-cliente/condiciones-comerciales.md) |
| Límite de crédito | Credit limit | Cuánto puede deber el cliente; lo fija Tesorería y el pedido lo consulta | [condiciones comerciales](../Registro-del-cliente/condiciones-comerciales.md) |
| Lista de precios | Price list | El precio de cada producto para un grupo de clientes, un canal o un período | [precio y descuentos](../Presupuesto/precio-y-descuentos.md) |
| Cartera | Customer portfolio, book of business | El conjunto de cuentas asignadas a un vendedor o a un territorio | [cartera de clientes](../Registro-del-cliente/cartera-de-clientes.md) |
| Territorio | Territory | Una división (geográfica, por rubro o por tamaño) para asignar cuentas | [cartera de clientes](../Registro-del-cliente/cartera-de-clientes.md) |
| Etapa | Sales stage | En qué punto del embudo está una oportunidad; las etapas las define Ventas | [oportunidad](../Seguimiento-comercial/oportunidad.md) |
| Motivo de pérdida | Loss reason | Por qué una oportunidad no se ganó | [oportunidad](../Seguimiento-comercial/oportunidad.md) |
| Vigencia | Validity, valid until | Hasta cuándo vale un presupuesto | [vigencia y aceptación](../Presupuesto/vigencia-y-aceptacion.md) |
| Seña | Down payment, deposit | Lo que el cliente entrega al aceptar, a cuenta del precio | [vigencia y aceptación](../Presupuesto/vigencia-y-aceptacion.md) |
| Fecha prometida | Promised date, committed date | La fecha de entrega que se le compromete al cliente en el pedido | [fecha prometida](../Pedido-de-venta/fecha-prometida.md) |
| Disponible para prometer | Available-to-promise (ATP) | Según ASCM, la parte del inventario y de la producción planificada que todavía no está comprometida con pedidos | [fecha prometida](../Pedido-de-venta/fecha-prometida.md) |
| Capaz de prometer | Capable-to-promise (CTP) | Según ASCM, comprometer pedidos contra la capacidad disponible además del inventario | [fecha prometida](../Pedido-de-venta/fecha-prometida.md) |
| Pendiente de entrega | Backorder | La parte de un pedido que no se pudo entregar y queda para después | [cambios y cancelaciones](../Pedido-de-venta/cambios-y-cancelaciones.md) |

## Las siglas

| Sigla | Qué es |
|---|---|
| CRM | *Customer relationship management*: la estrategia de dirigir la empresa alrededor de los clientes, o el sistema que registra clientes y oportunidades (ver [Fundamentos](fundamentos-de-relacion-con-clientes.md)) |
| SFA | *Sales force automation*: los sistemas para equipos de ventas de los noventa, de donde vienen la oportunidad y el embudo (ver [historia del CRM](historia-del-crm.md)) |
| CPQ | *Configure, price, quote*: el término de los proveedores para presupuestar productos con opciones; la academia habla de configuración de producto (ver [productos configurables](../Presupuesto/productos-configurables.md)) |
| ATP, CTP | Ver arriba |
| ERP | *Enterprise resource planning*: el sistema de gestión de la empresa; su parte de ventas toma desde el presupuesto o el pedido |
