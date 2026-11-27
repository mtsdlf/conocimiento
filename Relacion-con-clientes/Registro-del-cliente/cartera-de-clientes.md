---
resumen: >-
  La cartera de clientes es el conjunto de clientes de una empresa visto como algo que se reparte y se ordena: a qué vendedor le toca cada cuenta, en qué territorio está y en qué grupo o clase cae. Registra quién es dueño de cada cliente; el análisis de cuánto vale cada uno es de Datos y de Marketing.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework, 3.5.2 y 3.3.5, copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services"
  - "Microsoft Learn, tabla Account: https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account (como evidencia de práctica)"
  - "ERPNext, Customer: https://docs.frappe.io/erpnext/user/manual/en/customer (como evidencia de práctica)"
  - "Mastering Salesforce CRM, O'Reilly, cap. 3: https://oreilly.com/library/view/mastering-salesforce-crm/9781786463180/ch03s02.html (según resumen del buscador)"
  - "Salesforce Trailhead, Enterprise Territory Management: https://trailhead.salesforce.com/content/learn/modules/advanced-territory-management/get-tips-and-tricks-for-enterprise-territory-management (según resumen del buscador)"
  - "IMD, «Getting ABC classifications right»: https://www.imd.org/research-knowledge/supply-chain/articles/getting-abc-classifications-right/ (según resumen del buscador)"
  - "Relacion-con-clientes/.investigacion/registro-y-seguimiento.md, componente 3"
aliases: [cartera, customer portfolio, territorio, territorio de ventas, sales territory, dueño de la cuenta, account owner, clasificación ABC de clientes, grupo de clientes, customer group]
creado: 2026-11-27
revisado:
---

# Cartera de clientes

La cartera de clientes es el conjunto de clientes de una empresa visto como algo que se reparte y se ordena: a qué vendedor le toca cada cuenta, en qué territorio está y en qué grupo o clase cae. Registra quién es dueño de cada cliente; el análisis de cuánto vale cada uno es de Datos y de Marketing.

Es el componente del [registro del cliente](registro-del-cliente.md) que mira a todos los clientes juntos. El vendedor y la zona de cada cliente son [condiciones comerciales](condiciones-comerciales.md); acá se ve cómo se organizan esos campos para que cada cuenta tenga a alguien a cargo. Según una copia del marco de APQC de versión no declarada, lo ubica en el mismo proceso que el registro de cuentas: elegir los clientes clave, armar el plan de cada cuenta y gestionar la relación (3.5.2.1, 3.5.2.2 y 3.5.2.4).

## Quién es dueño de una cuenta

Dos diseños conviven en los sistemas:

- **Un dueño único.** Un CRM de un proveedor grande guarda un propietario por cuenta, que puede ser una persona o un equipo, y lo actualiza cada vez que la cuenta se reasigna. Otro proveedor grande, según un resumen, también da un solo dueño por cuenta, que puede estar además en varios territorios.
- **Un reparto.** Un sistema abierto asigna un vendedor o un equipo de venta al cliente, con porcentajes de participación que tienen que sumar 100 %.

Como interpretación de la base, el primero responde a quién se llama por este cliente y el segundo, a quién le corresponde la comisión. Una empresa con un vendedor por cliente no nota la diferencia; una con equipos que comparten cuentas grandes, sí.

Cuando un vendedor se va, la cartera se reasigna. El registro tiene que permitir mover todas sus cuentas de una vez y que la historia (las [actividades](../Seguimiento-comercial/actividad.md), las [oportunidades](../Seguimiento-comercial/oportunidad.md) abiertas) siga colgando de la cuenta y no del vendedor. Esto es criterio de la base.

## Territorios

El territorio agrupa cuentas por zona, por rubro o por tamaño, para repartirlas y para analizar. En un sistema abierto es un árbol (país, región, zona) donde se ubica cada cliente; en un CRM grande es una lista que carga la empresa y se usa para segmentar. Según un resumen de un proveedor, los sistemas que tienen las dos cosas separan la jerarquía de roles, que dice quién le reporta a quién, de la jerarquía de territorios, que dice quién ve qué cuentas por asignación.

La venta por ruta, en la que cada vendedor recorre siempre los mismos comercios, es un caso extremo de territorio fijo: está en [preventa y autoventa](../../Comercio-electronico/Comercio-B2B/preventa-y-autoventa.md).

## Clasificar a los clientes

Un sistema abierto tiene grupos de clientes que sirven a la vez para cuatro cosas: valores por defecto, reportes, permisos y precios. Esa mezcla conviene advertirla; como interpretación de la base, si el grupo decide la lista de precios y también el informe, cambiar a un cliente de grupo para un reporte le cambiaría el precio.

La clasificación ABC ordena a los clientes por lo que facturan y los corta en clases. Es una técnica de inventario aplicada a clientes, que se apoya en Pareto: la idea de que el 20 % de los clientes trae el 80 % del ingreso es una aproximación, no una ley. Según un resumen, los cortes se fijan sobre el porcentaje de ingreso y no sobre la cantidad de clientes, la base (ingreso, unidades o margen) se discute, y la clasificación envejece si no se recalcula.

> [!NOTE] Sin fuente todavía: una definición de cliente activo e inactivo, o de cliente con potencial. Cada negocio fija cuánto tiempo sin comprar hace a un cliente inactivo.

## Dónde termina: el análisis de la cartera

Cuánto vale un cliente a lo largo del tiempo, cuántos se van y cómo se agrupan por comportamiento de compra no se registra acá: se calcula sobre estos registros. La misma copia de APQC pone el valor de vida del cliente y el análisis de bajas y retención en otra parte del proceso (3.3.5.1 y 3.3.5.3). En la base, la retención y la baja están en [retención y churn](../../Datos/Analitica-de-producto/Retencion-y-churn/retencion-y-churn.md), cómo se divide un mercado en [segmentación](../../Marketing/Mercado-y-cliente/segmentacion.md), y si conviene invertir en retener a un cliente, en [marketing de relaciones y lealtad](../../Marketing/Servicio-y-relacion/marketing-de-relaciones-y-lealtad.md).
