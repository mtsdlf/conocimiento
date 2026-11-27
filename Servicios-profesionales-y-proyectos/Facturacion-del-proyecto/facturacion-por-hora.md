---
resumen: >-
  Facturar por hora, en tiempo y materiales, es cobrarle al cliente las horas aprobadas por la tarifa que corresponde a cada una, más los gastos reembolsables; el registro tiene que resolver qué tarifa vale para cada hora, cuánto falta para el tope pactado, qué se ajusta en el borrador y cómo se corrige una factura ya emitida.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Dynamics 365 Project Operations, Price list setup: https://learn.microsoft.com/en-us/dynamics365/project-operations/pricing-costing/price-list-setup"
  - "Microsoft Learn, Dynamics 365 Project Operations, Sales price resolution: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/pricing-costing/sales-price-resolution-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage not-to-exceed status and validations: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/proforma-invoicing/manage-nte-status-validations-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Invoice schedules on a contract line: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/invoice-schedules-contract-line-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage a proforma project invoice: https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/manage-proforma-invoice"
  - "Microsoft Learn, Dynamics 365 Project Operations, Revise project invoices: https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/revise-project-invoices"
  - "Microsoft Learn, Dynamics 365 Project Operations, Recall and cancel approvals: https://learn.microsoft.com/en-us/dynamics365/project-operations/approvals/recall-cancel"
  - "ERPNext, Activity Type y Activity Cost (según resumen): https://docs.frappe.io/erpnext/user/manual/en/activity-type"
  - "Odoo 18, Time and materials invoicing: https://www.odoo.com/documentation/18.0/applications/sales/sales/invoicing/time_materials.html"
  - "FAR 52.232-7 Payments under Time-and-Materials and Labor-Hour Contracts (según resumen): https://www.acquisition.gov/far/52.232-7"
  - "Wikipedia, Time and materials (según resumen): https://en.wikipedia.org/wiki/Time_and_materials"
  - "IFRS Foundation, NIIF 15, párrafo B16: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html"
  - "IFRS Foundation, NIIF 15 Ejemplos ilustrativos, Ejemplo 42 (IE213-IE214): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15-ie.html"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (secciones 2, 4.2, 4.3, 4.6)"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (sección 3.1)"
aliases: [facturación por hora, tiempo y materiales, time and materials, T&M, hourly billing, tarifa horaria, billing rate, tope, not-to-exceed, NTE, precio máximo]
creado: 2026-11-27
revisado:
---

# Facturación por hora

Facturar por hora, en tiempo y materiales, es cobrarle al cliente las horas aprobadas por la tarifa que corresponde a cada una, más los gastos reembolsables; el registro tiene que resolver qué tarifa vale para cada hora, cuánto falta para el tope pactado, qué se ajusta en el borrador y cómo se corrige una factura ya emitida.

Es el modelo en que el cliente paga el tiempo que lleve el trabajo; según una definición secundaria, sirve cuando el tamaño no se puede estimar con precisión o los requisitos van a cambiar. Por qué conviene y quién carga el riesgo está en [modelos de contrato y cobro](../../Desarrollo/Encargo/modelos-de-contrato-y-cobro.md#qué-se-fija-y-quién-carga-el-riesgo). Es una de las reglas de [facturación del proyecto](facturacion-del-proyecto.md), y la que depende más de la [hoja de horas](../Registro-de-horas/hoja-de-horas.md): acá la hora aprobada es la factura.

## Qué tarifa vale para cada hora

La tarifa sale de una lista de precios. En un sistema de gestión de servicios, una lista es «a catalog of rates» con contexto de costo, de venta o de compra, una moneda y una vigencia con fecha de inicio y de fin. Las listas de venta se pueden pegar a un cliente, a una cotización o a un contrato; así un cliente puede tener tarifas propias sin tocar las generales. Las de costo dan el [costo de la hora](../Rentabilidad-de-la-firma/costo-y-margen-del-proyecto.md) con la misma mecánica.

Para cada hora, el sistema busca la lista por fecha de la hora y por moneda, y dentro de ella la línea del rol y de la unidad que presta a la persona. Si no hay, toma la línea del rol sin unidad. La tarifa queda por rol, con excepción por unidad, y no por persona.

Otro sistema abierto precia por otro eje: el tipo de actividad (análisis, desarrollo, reunión) tiene costo y tarifa por defecto, y una tabla por empleado los pisa. Son dos diseños distintos y ninguna fuente leída dice cuál es más común en firmas reales. Lectura de esta base: el precio por rol es el que el cliente entiende y el que se pone en una cotización; el precio por persona aparece cuando alguien vale más que su rol. Los roles están en [roles y habilidades](../Asignacion-de-personas/roles-y-habilidades.md).

> [!NOTE] Sin fuente todavía: si la tarifa que se factura es la vigente cuando se trabajó la hora o cuando se emite la factura. El sistema leído resuelve por fecha de la hora; no se encontró una regla general. El ajuste de tarifas por inflación está en [servicios profesionales en la Argentina](../servicios-profesionales-en-argentina.md).

## El tope

Un tiempo y materiales con tope (*not-to-exceed*) fija un monto máximo; hasta ahí paga el cliente y arriba carga la firma. En el sistema leído el tope existe solo en líneas por tiempo y materiales y se puede poner en cuatro niveles: la línea para un cliente, la línea, el cliente y el contrato. Se controla dos veces:

1. Al enviar la hora, contra el tope menos lo comprometido.
2. Al aprobarla, contra el tope menos lo comprometido y lo facturado.

La venta sin facturar que no entra en el tope no se puede marcar como lista para facturar. Quien dirige el proyecto puede liberar horas comprometidas para darle prioridad a otro trabajo, y reevaluar todo cuando se renegocia el tope. Las horas no cobrables o de cortesía no cuentan para el tope.

Una cláusula de contratos públicos de los Estados Unidos agrega una práctica: el proveedor avisa con una estimación revisada cuando el costo llega al 85 % del tope, y el comprador no paga nada por encima de él. Es una sola fuente, leída por resumen, y vale para ese tipo de contrato; para dinero, esta base pide una segunda fuente que no hay. En criterio de esta base, el aviso temprano es lo que hace útil el tope: sin él, la firma descubre que trabajó gratis cuando arma la factura.

## El borrador desde las horas aprobadas

En el sistema leído, la facturación por tiempo y materiales corre por calendario: cada línea tiene una frecuencia y una fecha de corrida, y la fecha de corte de las horas es el día anterior a la corrida. Un sistema abierto hace lo mismo a mano: las horas vuelven a la línea del pedido como entregadas, se crea un borrador de factura y se revisa antes de confirmar.

En el borrador, cada renglón de tiempo puede cambiar de cantidad, de precio, de descripción y de tipo: cobrable, no cobrable o de cortesía. Los dos últimos no suman al total, y la hora sigue costándole al proyecto. Es la forma en que un sistema castiga horas antes de facturar: no se borran, se reclasifican. Si llegan horas aprobadas después de armar el borrador, se pueden sumar. Cuánto se castiga entre la tarifa de lista y lo facturado es la [realización](../Rentabilidad-de-la-firma/realizacion.md).

> [!NOTE] Sin fuente todavía: la práctica de estudios para castigar horas antes de facturar y para dar de baja trabajo en curso que no se va a cobrar. Los sistemas leídos solo ofrecen reclasificar el tipo, bajar cantidad o precio, o acreditar la factura.

Los gastos reembolsables entran a la misma factura si la línea los incluye; a costo, con recargo o con precio por unidad, según [gastos del proyecto](../Registro-de-horas/gastos-del-proyecto.md).

## La factura confirmada se corrige con otra

Una factura confirmada no se edita. En el sistema leído se «revisa»: se crea un borrador nuevo con cantidades en cero, que supone crédito total, y si el crédito es parcial se carga lo que sigue facturándose. Al confirmar, el sistema revierte la venta facturada y crea una venta sin facturar nueva por lo que quedó pendiente. La hora vuelve a estar disponible para facturar.

Lo mismo vale al revés: quien cargó una hora ya facturada no puede retirarla. El sistema no deja pedir el retiro de una hora que «the system already invoiced to the customer» hasta que una factura correctiva acredite la original entera. La corrección de horas aprobadas está en [hoja de horas](../Registro-de-horas/hoja-de-horas.md); el patrón de fondo, un error que se corrige con otro movimiento y no editando, en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md#un-error-se-corrige-con-otro-movimiento).

## El ingreso es lo facturable

En tiempo y materiales no hace falta estimar cuánto se avanzó. La NIIF 15 (párrafo B16) da un atajo: si la firma tiene derecho a cobrar un monto que corresponde directamente al valor de lo que entregó hasta la fecha, puede reconocer como ingreso lo que tiene derecho a facturar. El Ejemplo 42 de la norma lo muestra con un servicio de limpieza a «CU25 per hour»: el ingreso es horas por tarifa. Lectura de esta base: con un tope, el atajo sigue valiendo mientras lo trabajado esté debajo; lo que pasa del tope no se factura y no es ingreso. Las horas trabajadas y no facturadas al cierre son [trabajo en curso](trabajo-en-curso.md). Dinero y norma: una sola fuente, la IFRS Foundation.
