---
resumen: >-
  Una orden de cambio es el registro de un cambio en el alcance o en el precio de un proyecto (o en los dos) que el cliente y la firma aprobaron; dice qué se agrega o se quita, cuánto vale y cómo mueve el presupuesto del proyecto, los hitos y lo que se factura.
estado: vigente
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIIF 15 Ingresos de actividades ordinarias procedentes de contratos con clientes, párrafos 18-21 y 56: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html"
  - "Grant Thornton, Revenue from Contracts with Customers: Navigating the guidance in ASC 606 and ASC 340-40 (enero 2022), sección 10 Modifications, ASC 606-10-25-10 a 25-13: https://www.grantthornton.com/content/dam/grantthornton/website/assets/content-page-files/audit/pdfs/2022/revenue-from-contracts-with-customers-updated-220124.pdf"
  - "AIA Contract Documents, Instructions: G701-2017, Change Order (y el formulario de muestra G701-2017): https://help.aiacontracts.com/hc/en-us/articles/1500009322061-Instructions-G701-2017-Change-Order"
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 5.3.2.4 «Identify changes» y 5.3.2.5 «Obtain approval to proceed»"
  - "Microsoft Learn, Dynamics 365 Project Operations, Revise a project cost budget: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/budget/revise-project-cost-budget"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (sección 2.5)"
aliases: [orden de cambio, change order, modificación del contrato, contract modification, pedido de cambio, change request, adenda]
creado: 2026-11-27
revisado: 2026-11-27
---

# Orden de cambio

Una orden de cambio es el registro de un cambio en el alcance o en el precio de un proyecto (o en los dos) que el cliente y la firma aprobaron; dice qué se agrega o se quita, cuánto vale y cómo mueve el presupuesto del proyecto, los hitos y lo que se factura.

Cómo se decide un cambio (quién lo aprueba, si se cotiza, se intercambia por algo del mismo tamaño o se recorta) es método, y está en dos notas vecinas: [control de cambios](../../Gestion-de-proyectos/Seguimiento/control-de-cambios.md), para cualquier proyecto, y [cambios de alcance](../../Desarrollo/Encargo/cambios-de-alcance.md#tres-reglas-para-un-pedido-nuevo), para un encargo de software. Acá importa lo que queda escrito una vez decidido: el documento con precio y su efecto en el [proyecto del cliente](proyecto-del-cliente.md).

## Alcance, precio y aprobación

La definición más precisa que se leyó es la de la NIIF 15, párrafo 18: «A contract modification is a change in the scope or price (or both) of a contract that is approved by the parties». Tiene tres partes, y cada una es un dato del registro:

- **Qué cambia**: el alcance, el precio o los dos. Una rebaja sin cambio de trabajo también es una orden de cambio: Grant Thornton lista, entre las formas comunes de modificación según el ASC 606, «Reducing the contract price without a change in goods or services promised». El párrafo 18 agrega que la modificación puede llamarse «change order, a variation or an amendment».
- **Quién aprueba**: las dos partes. Un pedido del cliente que la firma todavía no aceptó, o un cambio que la firma propone y el cliente no firmó, no es una orden de cambio todavía. La norma admite que la aprobación sea escrita, oral o «implied by customary business practices»; para el registro, criterio de esta base, conviene que quede escrita.
- **Sobre qué contrato**: la orden apunta al contrato o al pedido de origen, no flota suelta.

El párrafo 19 agrega un caso que el registro tiene que admitir: puede haber modificación aunque las partes discutan el alcance o el precio. Si el precio no está resuelto, la firma lo estima con las reglas de la contraprestación variable (la parte del precio que depende de algo que todavía no se sabe, que la NIIF 15 manda estimar), y el párrafo 56 solo deja contar como ingreso lo que sea muy probable que no haya que revertir. Para el registro eso quiere decir, en lectura de esta base, que una orden puede estar aprobada en alcance y abierta en precio, y que mientras tanto el ingreso que genera se calcula con cautela.

Dinero y norma: lo de este apartado y del siguiente tiene dos fuentes, la NIIF 15 de la IFRS Foundation y el ASC 606 de los Estados Unidos (606-10-25-10 a 25-13, leído en el texto que reproduce Grant Thornton), que dicen lo mismo sobre la definición, el cambio sin precio resuelto y los dos tratamientos.

## Los estados de una orden de cambio

APQC separa dos pasos dentro de la ejecución de un servicio: «Identify changes» (5.3.2.4) y «Obtain approval to proceed» (5.3.2.5). Entre los dos hay un estado intermedio que el registro tiene que mostrar: el cambio que se detectó y todavía no se autorizó. Sobre esa base, los estados que siguen son síntesis de esta base:

| Estado | Qué significa | Se puede trabajar |
|---|---|---|
| Identificado | Alguien registró el pedido o el desvío | No, salvo en tiempo y materiales |
| Cotizado | Tiene alcance, horas, precio y efecto en el plazo | No |
| Aprobado | Las dos partes firmaron | Sí |
| Rechazado | El cliente o la firma dijo que no | No |

La columna de la derecha es la que protege la plata. Trabajar sobre un cambio identificado y no aprobado es la deriva del alcance que describe [control de cambios](../../Gestion-de-proyectos/Seguimiento/control-de-cambios.md#cambio-aprobado-y-deriva-del-alcance). En tiempo y materiales el trabajo se cobra igual por hora, y aun así conviene escribir el cambio, porque mueve el presupuesto que el cliente tiene en la cabeza, como dice [cambios de alcance](../../Desarrollo/Encargo/cambios-de-alcance.md#tres-reglas-para-un-pedido-nuevo).

## Contrato aparte o parte del mismo

La NIIF 15 distingue dos clases de modificación, y la diferencia tiene que quedar en el registro porque cambia cómo se reconoce el ingreso:

1. **Contrato separado** (párrafo 20). Se trata como un contrato nuevo cuando agrega bienes o servicios distintos de los que ya estaban y el precio sube en lo que esos servicios valdrían vendidos solos. Ejemplo propio: a un proyecto de implementación se le suma la capacitación de un segundo equipo, a la tarifa de lista.
2. **Parte del contrato existente** (párrafo 21). Si no se cumplen esas condiciones, la modificación se contabiliza como si se terminara el contrato viejo y empezara uno nuevo, cuando lo que falta es distinto de lo ya entregado, o como parte del mismo contrato, con un ajuste acumulado del ingreso, cuando no lo es. Ejemplo propio: se amplía el alcance del mismo sistema que se está construyendo y se renegocia el precio total.

Para quien modela, eso pide un dato en la orden: si suma un servicio distinto a su precio de venta, o si cambia el alcance del mismo servicio. Cómo sigue el asiento es de [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md#cuándo-hay-un-ingreso-los-cinco-pasos-de-la-niif-15).

## Qué mueve una orden aprobada

Una orden aprobada toca tres registros del proyecto. La lista es criterio de esta base:

- **El presupuesto del proyecto.** No se edita la versión aprobada: se hace una revisión que la incluye. Un sistema de gestión de servicios solo revisa una versión aprobada y crea una versión nueva en borrador, como explica [presupuesto del proyecto](presupuesto-del-proyecto.md#aprobado-pronóstico-y-revisado).
- **Los hitos o las líneas del contrato.** En un precio cerrado, la orden agrega un [hito](hitos-y-entregables.md) o sube el monto de uno; si no, el trabajo se hace y no hay dónde facturarlo. En un contrato con varias líneas, un servicio distinto puede ser una línea nueva con su propio método de facturación.
- **La fecha.** Si el cambio corre el plazo, la fecha de los hitos posteriores se mueve con él.

## Qué datos lleva el formulario

El formulario estándar de la construcción en los Estados Unidos, el G701 del Instituto Americano de Arquitectos, da una lista de datos que sirve de contraste. Según sus instrucciones, lleva:

- una descripción detallada del cambio, con los anexos que aclaren el alcance;
- el monto original del contrato, el cambio neto de las órdenes anteriores, el monto antes de esta orden, el aumento o la baja de esta orden y el monto nuevo;
- el cambio en el plazo, en días, y la fecha nueva de terminación sustancial;
- la firma de las tres partes: el dueño, el contratista y el arquitecto.

El formulario cuenta el monto como una cuenta corriente de órdenes: cada una parte del total que dejó la anterior. Para un proyecto de servicios, el equivalente es guardar con cada orden el precio antes y después, no solo la diferencia. Es una lectura de esta base sobre un formulario de otro rubro, no una práctica documentada en servicios profesionales.

> [!NOTE] Sin fuente todavía: el procedimiento de variación de los contratos de obra del FIDIC (se buscó y solo aparecieron comentarios de terceros, no el texto) y cómo registran los sistemas de servicios el efecto de un cambio en el calendario.

## Cómo se pierde plata con los cambios

Hay proveedores que ofertan bajo un precio cerrado con el plan de ganar con los cambios, según cuenta Fowler en [modelos de contrato y cobro](../../Desarrollo/Encargo/modelos-de-contrato-y-cobro.md#por-qué-fijar-el-alcance-suele-salir-mal). Del lado de la firma, la pérdida más común es la inversa, y es lectura de esta base: los cambios chicos se hacen sin orden, cada uno parece no valer el trámite, y al final el costo del proyecto creció mientras el precio quedó igual. El remedio de registro es que todo cambio entre al menos como «identificado», aunque se decida no cobrarlo: así queda a la vista cuánto se regaló. Cómo se cobran los cambios contra el alcance escrito está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#el-alcance-por-escrito-y-los-cambios-contra-ese-escrito).
