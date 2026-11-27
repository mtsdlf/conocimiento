---
resumen: >-
  Un hito es un punto del proyecto que se puede observar y que el cliente acepta, como la entrega de un diseño o la puesta en marcha; el entregable es lo que se entrega en ese punto. En un proyecto con cliente el hito es además un evento económico: suele disparar una factura y puede servir para medir el avance del ingreso.
estado: borrador
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIIF 15 Ingresos de actividades ordinarias procedentes de contratos con clientes, párrafos B14-B19 y B83-B86: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html"
  - "Grant Thornton, Revenue from Contracts with Customers: Navigating the guidance in ASC 606 and ASC 340-40 (enero 2022), ASC 606-10-55-17 y comentario sobre «milestones reached»: https://www.grantthornton.com/content/dam/grantthornton/website/assets/content-page-files/audit/pdfs/2022/revenue-from-contracts-with-customers-updated-220124.pdf"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage contract values for project-based sales: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/manage-contract-values-project-based-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Invoice schedules on a contract line: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/invoice-schedules-contract-line-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage billing backlog: https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/manage-billing-backlog"
  - "Odoo 19, Invoice project milestones: https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/milestone.html"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (sección 2.4)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 4.3)"
aliases: [hito, hitos, milestone, entregable, deliverable, hito de facturación, billing milestone, hito de pago]
creado: 2026-11-27
revisado:
---

# Hitos y entregables

Un hito es un punto del proyecto que se puede observar y que el cliente acepta, como la entrega de un diseño o la puesta en marcha; el entregable es lo que se entrega en ese punto. En un proyecto con cliente el hito es además un evento económico: suele disparar una factura y puede servir para medir el avance del ingreso.

Los hitos se fijan al armar el [proyecto del cliente](proyecto-del-cliente.md), con el [presupuesto del proyecto](presupuesto-del-proyecto.md), y se mueven con cada [orden de cambio](orden-de-cambio.md). Cómo se acuerda qué quiere decir «terminado» y cómo acepta el cliente cada parte está en [alcance y aceptación](../../Desarrollo/Encargo/alcance-y-aceptacion.md#la-aceptación-por-partes); acá, qué se registra del hito y qué plata mueve.

## Entregable, hito y hito de facturación

Las tres palabras se usan como si fueran una. Conviene separarlas al modelar, y la separación es criterio de esta base:

- El **entregable** es una cosa: un informe, un plano, una versión del sistema. Tiene criterios de aceptación.
- El **hito** es un momento con fecha prevista y fecha real: el entregable fue aceptado, o una etapa terminó.
- El **hito de facturación** es un renglón del calendario de cobro, con un monto, que se vuelve facturable cuando se alcanza el hito al que apunta.

Un hito puede no facturar nada (la aprobación de un borrador interno) y una factura puede no tener hito (la cuota mensual de un contrato por tiempo). Cuando coinciden, el registro tiene que guardar los dos: el hito de trabajo con su aceptación y el renglón de facturación con su monto.

## Por qué el hito tiene que ser observable

La NIIF 15 reconoce dos familias de métodos para medir cuánto se avanzó en una obligación que se cumple a lo largo del tiempo (B14): los de producto, que miden lo que el cliente recibió, y los de insumo, que miden lo que la firma puso. Según B15, los métodos de producto miden directamente el valor para el cliente, y entre sus ejemplos trae «surveys of performance completed to date, appraisals of results achieved, milestones reached, time elapsed and units produced or units delivered»: los hitos alcanzados figuran como método de producto. B17 dice su punto débil: «the outputs used to measure progress may not be directly observable».

B15 pone una condición: el producto elegido tiene que reflejar fielmente el desempeño de la firma, y no lo hace si deja sin medir bienes o servicios cuyo control ya pasó al cliente. El ASC 606 de los Estados Unidos dice lo mismo en 606-10-55-17. Grant Thornton, una firma auditora, concluye que un método de «milestones reached» no es apropiado si deja fuera del avance trabajo en curso material que el cliente ya controla. Dinero y norma: dos fuentes, la IFRS Foundation y el ASC 606 citado por Grant Thornton.

La aceptación del cliente entra en la misma discusión (B83-B86). Si la firma puede determinar objetivamente que el servicio cumple lo pactado, la aceptación es «a formality» y no cambia cuándo pasa el control (B84); si no puede, no concluye que el cliente tiene el control hasta recibir su aceptación (B85). Para el registro, eso pide un criterio de aceptación que se pueda comprobar.

De ahí sale una regla de registro, que es lectura de esta base: un hito que sirve para facturar o para medir el avance tiene que ser un hecho que alguien pueda verificar (un acta firmada, un correo de aceptación, una puesta en marcha con fecha), no una estimación de porcentaje. «Diseño al 60 %» no es un hito; «diseño aprobado por el cliente» sí.

Que el hito se use para medir el ingreso y que se use para facturar son dos decisiones separadas. La factura sigue lo pactado con el cliente; el ingreso sigue el método de avance que la firma eligió. Cuando no coinciden, la diferencia es el [trabajo en curso](../Facturacion-del-proyecto/trabajo-en-curso.md).

## Qué guarda el registro de un hito

En un sistema de gestión de servicios, un hito de facturación manual lleva nombre, fecha, monto, impuesto y estado. Los estados recorren este camino:

1. **No listo para facturar**: el hito existe en el calendario.
2. **Listo para facturar**: alguien lo marcó así, o la corrida automática lo marcó al llegar la fecha.
3. **Factura creada**: está en un borrador de factura.
4. **Factura confirmada**: salió al cliente.

Si la factura de un hito se corrige, el mismo sistema solo admite el crédito total: el hito vuelve de confirmado a listo para facturar y se emite de nuevo. Un sistema abierto, en cambio, marca el hito como alcanzado en el pedido y avisa que alcanzarlo «does not automatically create an invoice»: la factura se crea aparte, y el pedido muestra qué porcentaje ya es facturable.

Lectura de esta base sobre los dos diseños: separar «alcanzado» de «facturado» es lo que permite ver un hito cumplido que nadie facturó, que es plata parada. Al registro le hacen falta las dos fechas.

## La suma de los hitos es el precio

En el sistema leído, un contrato a precio cerrado puede facturarse de dos formas: por hitos completos, que es el valor por defecto, o por avance, facturando un porcentaje del hito. Los hitos periódicos se generan dividiendo el monto por la cantidad de períodos, y la suma de los hitos tiene que dar el valor del contrato: si no da, el sistema marca error. La regla vale sin software: si el calendario de cobro no suma el precio, alguien va a facturar de más o de menos al final.

Cómo se arma ese calendario, con anticipos y retenciones de garantía, está en [facturación por hito](../Facturacion-del-proyecto/facturacion-por-hito.md). Qué hitos de cobro usan las agencias (adelanto, diseño aprobado, entrega en prueba, lanzamiento) está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#formas-de-repartir-el-riesgo).

## Cómo falla

> [!NOTE] Sin fuente todavía: estudios o práctica documentada sobre cómo fallan los hitos de facturación. Lo que sigue es criterio de esta base, con un respaldo parcial: la advertencia de la norma sobre el trabajo que queda sin medir entre un hito y otro.

El hito falla cuando su criterio de aceptación es vago, porque el cliente puede no aceptarlo y la factura queda trabada. Falla cuando los hitos están muy separados, porque la firma financia meses de trabajo sin cobrar. Y falla cuando una orden de cambio agrega trabajo pero no agrega un hito ni mueve el monto de uno existente: el trabajo se hace y no hay renglón donde cobrarlo.
