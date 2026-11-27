---
resumen: >-
  La facturación del proyecto es la regla con que el trabajo hecho para un cliente se vuelve factura: por hora, por hito o por abono y bolsa de horas, según el modelo de cobro que se vendió. Cada modelo decide qué registro dispara la factura, y en todos la factura sigue un calendario distinto del ingreso, que sigue el trabajo hecho.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage contract values for project-based sales: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/manage-contract-values-project-based-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage billing backlog: https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/manage-billing-backlog"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage a proforma project invoice: https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/manage-proforma-invoice"
  - "Odoo 18, Time and materials invoicing: https://www.odoo.com/documentation/18.0/applications/sales/sales/invoicing/time_materials.html"
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 9.2.2 «Invoice customer» y 5.3"
  - "IFRS Foundation, NIIF 15 Ingresos de actividades ordinarias procedentes de contratos con clientes, párrafos 35 y 105-109: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html"
  - "Grant Thornton, Revenue from Contracts with Customers: Navigating the guidance in ASC 606 and ASC 340-40 (enero 2022), ASC 606-10-25-27 y 606-10-45-2: https://www.grantthornton.com/content/dam/grantthornton/website/assets/content-page-files/audit/pdfs/2022/revenue-from-contracts-with-customers-updated-220124.pdf"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (sección 3)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 4)"
aliases: [facturación del proyecto, project billing, project invoicing, facturación de servicios, regla de facturación, billing rule, billing method]
creado: 2026-11-27
revisado: 2026-11-27
---

# Facturación del proyecto

La facturación del proyecto es la regla con que el trabajo hecho para un cliente se vuelve factura: por hora, por hito o por abono y bolsa de horas, según el modelo de cobro que se vendió. Cada modelo decide qué registro dispara la factura, y en todos la factura sigue un calendario distinto del ingreso, que sigue el trabajo hecho.

Es la cuarta parte de [Servicios profesionales y proyectos](../servicios-profesionales-y-proyectos.md). Recibe del [proyecto del cliente](../Proyecto-del-cliente/proyecto-del-cliente.md) la regla de cobro y los [hitos](../Proyecto-del-cliente/hitos-y-entregables.md), y del [registro de horas](../Registro-de-horas/registro-de-horas.md) las horas y los gastos aprobados. Le da a [Rentabilidad de la firma](../Rentabilidad-de-la-firma/rentabilidad-de-la-firma.md) el ingreso, y a la contabilidad lo que [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md) registra. Cómo se elige el modelo de cobro y quién carga el riesgo con cada uno no es de acá: está en [modelos de contrato y cobro](../../Desarrollo/Encargo/modelos-de-contrato-y-cobro.md#qué-se-fija-y-quién-carga-el-riesgo).

APQC no pone la facturación de un servicio dentro de la entrega (5.0) sino en finanzas: «Invoice customer» (9.2.2), con pasos para generar los datos de facturación y transmitirlos. Este tema la trata acá porque la regla que decide qué se factura vive en el proyecto.

## Qué dispara la factura en cada modelo

El modelo de cobro decide qué registro importa. La línea del contrato, o línea de venta, es el renglón del contrato o del pedido que fija qué se vende, con qué método de facturación y sobre qué tareas. En un sistema de gestión de servicios, aprobar una hora de una línea por tiempo y materiales crea dos movimientos, el costo y la venta sin facturar; aprobar una hora de una línea a precio cerrado crea solo el costo. La hora a precio cerrado no genera venta: el ingreso llega por el hito o por el avance.

| Modelo | Qué genera la hora aprobada | Qué dispara la factura | Nota |
|---|---|---|---|
| Tiempo y materiales | Costo y venta sin facturar | La fecha de corte del período | [facturación por hora](facturacion-por-hora.md) |
| Precio cerrado | Solo costo | El hito alcanzado o el avance pactado | [facturación por hito](facturacion-por-hito.md) |
| Abono | Costo; la venta es la cuota | El período | [abono y bolsa de horas](abono-y-bolsa-de-horas.md) |
| Bolsa de horas | Costo y consumo del saldo | La compra de la bolsa, por adelantado | [abono y bolsa de horas](abono-y-bolsa-de-horas.md) |

Las filas de abono y bolsa son síntesis de esta base; las de tiempo y materiales y precio cerrado salen del sistema leído. Un mismo proyecto puede tener líneas de distintos modelos, como explica [proyecto del cliente](../Proyecto-del-cliente/proyecto-del-cliente.md#qué-guarda-el-registro-del-proyecto).

## Del trabajo aprobado al borrador de factura

En los sistemas leídos, la factura de un proyecto pasa por un borrador antes de salir. Un sistema abierto lleva las horas a la línea del pedido como cantidad entregada y desde ahí crea un borrador de factura que alguien revisa antes de confirmar. Un sistema de gestión de servicios junta en una bandeja todas las ventas sin facturar de todos los contratos, y los hitos de precio cerrado en otra vista; desde ahí se marca cada renglón como listo para facturar o no. Lo que no está listo no entra en el borrador.

El borrador es donde la firma decide cuánto cobra de lo que trabajó. En el mismo sistema, cada renglón de tiempo puede cambiar de cantidad, de precio o de tipo (cobrable, no cobrable o de cortesía), y solo lo cobrable suma al total. Esa decisión es lo que mide la [realización](../Rentabilidad-de-la-firma/realizacion.md). Una factura confirmada ya no se edita: se corrige con otra, que acredita la original. El detalle está en [facturación por hora](facturacion-por-hora.md#la-factura-confirmada-se-corrige-con-otra).

Lectura de esta base sobre los dos sistemas: el documento que se factura es la línea de venta o del contrato, no la hoja de horas. La [hoja de horas](../Registro-de-horas/hoja-de-horas.md) alimenta la línea, y la línea es la que sabe la tarifa, el tope y lo que ya se facturó.

## Reconocer el ingreso no es facturar

La factura sigue el calendario pactado con el cliente; el ingreso sigue el trabajo hecho. La NIIF 15 reconoce el ingreso de un servicio a lo largo del tiempo cuando, entre otros casos, el cliente «simultaneously receives and consumes the benefits» a medida que la firma trabaja (párrafo 35). Grant Thornton, sobre el ASC 606, dice que en «typical service contracts» el cliente recibe y consume el resultado a medida que la firma trabaja y, por eso, la obligación se cumple a lo largo del tiempo; que un servicio profesional sea uno de esos casos es lectura de esta base. Por eso, al cierre de cada mes, casi todo proyecto tiene una diferencia entre lo trabajado y lo facturado:

- Trabajado y no facturado: un activo del contrato o una cuenta a cobrar.
- Facturado y no trabajado: un pasivo del contrato.

Esa diferencia, con sus nombres según la norma, está en [trabajo en curso](trabajo-en-curso.md). Lo que se cobra antes de entregar, del lado contable, está en [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md#cobrar-antes-de-entregar-anticipos-e-ingresos-diferidos). Dinero y norma: lo de la NIIF 15 tiene dos fuentes, la IFRS Foundation y el ASC 606 de los Estados Unidos según Grant Thornton (606-10-25-27 y 606-10-45-2).

## Lo que sigue a la factura

La factura emitida pasa a otros dominios. La factura electrónica, el impuesto que lleva y las retenciones que sufre la firma son del tema Impuestos; el cobro y el crédito al cliente, de Tesorería y finanzas de la empresa en marcha; ninguno de los dos está escrito todavía. Lo propio de facturar servicios en la Argentina está en [servicios profesionales en la Argentina](../servicios-profesionales-en-argentina.md).

## Qué hay adentro de la facturación del proyecto

- [Facturación por hora](facturacion-por-hora.md): tiempo y materiales: la tarifa, el tope, el borrador desde horas aprobadas, los ajustes y la corrección de una factura.
- [Facturación por hito](facturacion-por-hito.md): precio cerrado: el calendario de facturación, los anticipos, la retención de garantía y el costo financiero de cobrar tarde.
- [Abono y bolsa de horas](abono-y-bolsa-de-horas.md): el pago periódico por disponibilidad, las horas prepagas que se consumen y el anticipo periódico que se concilia contra las horas.
- [Trabajo en curso](trabajo-en-curso.md): lo trabajado sin facturar y lo facturado sin trabajar: activo del contrato, cuenta a cobrar y pasivo del contrato, y cómo se mide el avance.
