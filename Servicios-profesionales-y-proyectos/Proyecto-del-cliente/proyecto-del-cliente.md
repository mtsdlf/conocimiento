---
resumen: >-
  El proyecto del cliente es el registro económico de un trabajo vendido a un cliente: nace de un presupuesto aceptado o de un contrato firmado, fija la regla con que se va a cobrar, lleva un presupuesto en horas, costo y precio, y junta las horas, los gastos, los hitos y las facturas hasta el cierre financiero.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), categoría 5.3 «Deliver service to customer» (5.3.1.1, 5.3.1.3, 5.3.1.6, 5.3.3.2 a 5.3.3.7)"
  - "Odoo 18, Time and materials invoicing (confirmar el pedido crea el proyecto y la tarea): https://www.odoo.com/documentation/18.0/applications/sales/sales/invoicing/time_materials.html"
  - "ERPNext, Project Profitability (el proyecto como campo de los documentos de compra y venta): https://docs.frappe.io/erpnext/user/manual/en/project-profitability"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage contract values for project-based sales (líneas de contrato con método de facturación): https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/manage-contract-values-project-based-sales"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (secciones 0 y 2)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 4.1)"
aliases: [proyecto del cliente, proyecto facturable, client project, billable project, engagement, encargo, proyecto con cliente]
creado: 2026-11-27
revisado:
---

# Proyecto del cliente

El proyecto del cliente es el registro económico de un trabajo vendido a un cliente: nace de un presupuesto aceptado o de un contrato firmado, fija la regla con que se va a cobrar, lleva un presupuesto en horas, costo y precio, y junta las horas, los gastos, los hitos y las facturas hasta el cierre financiero.

Es la primera de las cinco partes de [Servicios profesionales y proyectos](../servicios-profesionales-y-proyectos.md) y la que ordena a las demás. Le pide a [Asignación de personas](../Asignacion-de-personas/asignacion-de-personas.md) los roles y las fechas, habilita la carga en [Registro de horas](../Registro-de-horas/registro-de-horas.md) y le fija a [Facturación del proyecto](../Facturacion-del-proyecto/facturacion-del-proyecto.md) la regla de cobro y los hitos. Cómo se planifica y se sigue el trabajo como método está en [Gestión de proyectos](../../Gestion-de-proyectos/gestion-de-proyectos.md); acá entra lo que de eso se registra con un precio y un cliente del otro lado.

## De la venta aceptada al proyecto

El proyecto empieza cuando el cliente dice que sí. El [presupuesto](../../Relacion-con-clientes/Presupuesto/presupuesto.md) aceptado, el [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md) o el contrato firmado son de Relación con clientes; cómo se acepta y qué precio rige si cambió en el medio está en [vigencia y aceptación](../../Relacion-con-clientes/Presupuesto/vigencia-y-aceptacion.md). De ahí en adelante el trabajo es de este tema.

Lo primero que se hace con el proyecto es leer lo que se firmó. APQC pone ese paso al principio de la entrega de un servicio: «Review contract and agreed terms» (5.3.1.1), antes de aprobar el plan (5.3.1.3) y de asignar personas (5.3.1.6). Los términos de cobro gobiernan el registro entero: si el contrato es por hora, cada hora aprobada es plata a facturar; si es a precio cerrado, la hora es costo y lo que dispara la factura es el hito. Cómo se elige entre esos modelos, y quién carga el riesgo con cada uno, está en [modelos de contrato y cobro](../../Desarrollo/Encargo/modelos-de-contrato-y-cobro.md#qué-se-fija-y-quién-carga-el-riesgo).

Los sistemas leídos atan el proyecto a la venta de dos maneras:

1. **El proyecto nace del pedido.** En un sistema abierto, confirmar el pedido de venta crea el proyecto y su tarea, y las horas cargadas vuelven al pedido como cantidad entregada. La línea del pedido es el ancla que une proyecto, horas y factura.
2. **El proyecto es una etiqueta.** En otro sistema abierto, el proyecto es un campo que llevan las órdenes de compra, las facturas de proveedor, los pedidos, las facturas de venta y los cobros; la rentabilidad sale de sumar los ingresos y los gastos que tienen esa etiqueta. Es el proyecto como dimensión de cada movimiento, el mismo diseño que [centros de costo](../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md#por-qué-los-centros-de-costo-van-en-dimensiones-y-no-en-el-plan-de-cuentas) explica para la contabilidad.

El primero sirve para facturar; el segundo, para medir. Lectura de esta base: un proyecto con cliente necesita los dos, el vínculo con la venta para saber qué se cobra y la dimensión para saber cuánto costó.

## Qué guarda el registro del proyecto

Un proyecto del cliente guarda, como mínimo, el cliente, el documento de venta del que salió, quién lo dirige, la moneda, las [tarifas](../Facturacion-del-proyecto/facturacion-por-hora.md) que se le aplican, el [presupuesto del proyecto](presupuesto-del-proyecto.md), sus [hitos](hitos-y-entregables.md) y la regla de facturación. La lista es criterio de esta base, armada sobre lo que traen los sistemas leídos.

La regla de facturación puede no ser una sola. Un sistema de gestión de servicios divide el contrato en líneas, y cada línea tiene su método («Fixed Price» o «Time and Material»), apunta al proyecto entero o a algunas tareas, y dice qué clases de movimiento incluye: tiempo, gastos, materiales u honorarios. Así un mismo proyecto puede tener el diseño a precio cerrado y el soporte posterior por hora. El mismo sistema no deja que un proyecto y una clase de movimiento caigan en dos líneas a la vez, salvo que cada línea tome tareas distintas: una hora tiene que saber con qué regla se cobra.

## Los estados del proyecto

> [!NOTE] Sin fuente todavía: ningún estándar leído define los estados de un proyecto con cliente. APQC solo da el ciclo de iniciar (5.3.1), ejecutar (5.3.2) y completar (5.3.3).

La tabla que sigue es síntesis de esta base, no un estándar. Sirve como punto de partida para modelar:

| Estado | Qué permite |
|---|---|
| Borrador | Armar el presupuesto y los hitos; no se cargan horas |
| Activo | Cargar horas y gastos, reservar personas, facturar |
| En pausa | Se conservan las reservas firmes o se liberan; no se cargan horas nuevas |
| Cerrado a cargos | No entran horas ni gastos; se emite lo que falta facturar |
| Cerrado | Cierre financiero hecho; solo lectura |

El estado que más cuesta modelar es «cerrado a cargos». Separa el fin del trabajo del fin de la plata: el equipo terminó, pero quedan horas por aprobar, una última factura y quizás un saldo prepago por devolver.

## Facturable o interno

No todo proyecto tiene un cliente que pague. La preventa, la capacitación, un desarrollo propio o la administración de la firma también reciben horas. Registrarlos como proyectos internos, con la misma carga de horas y sin regla de facturación, deja ver cuánto tiempo se va en trabajo que nadie paga, que es la diferencia entre las horas facturables y la capacidad con que se calcula la [utilización](../Rentabilidad-de-la-firma/utilizacion.md#el-denominador-cambia-el-número).

> [!NOTE] Sin fuente todavía: cómo distinguen los sistemas un proyecto interno de uno facturable, y si la marca es del proyecto, de la tarea o de cada hora. Lo que se leyó de la hora facturable está en [hoja de horas](../Registro-de-horas/hoja-de-horas.md).

## El cierre financiero

APQC separa el cierre financiero de la entrega: «Complete/finalize financial management activities» (5.3.3.2) y «Confirm delivery according to contract terms» (5.3.3.3), seguidos de liberar a las personas (5.3.3.4) y archivar los registros (5.3.3.7). El marco da los nombres pero no el contenido.

> [!NOTE] Sin fuente todavía: qué incluye el cierre financiero de un proyecto. Lectura de esta base: aprobar las últimas horas, facturar el remanente, liberar las retenciones de garantía, devolver o dar por consumido el saldo prepago, dejar en cero el [trabajo en curso](../Facturacion-del-proyecto/trabajo-en-curso.md) y cerrar el proyecto a nuevos cargos.

La aceptación del cliente que habilita ese cierre está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#aceptar-y-cerrar); el cierre como método, en [Gestión de proyectos](../../Gestion-de-proyectos/gestion-de-proyectos.md).

## Qué hay adentro del proyecto del cliente

- [Presupuesto del proyecto](presupuesto-del-proyecto.md) — la foto aprobada de horas, costo y precio por fase, tarea o rol, y el pronóstico que se mueve contra ella.
- [Hitos y entregables](hitos-y-entregables.md) — el hito como evento observable de aceptación y, a menudo, de facturación.
- [Orden de cambio](orden-de-cambio.md) — el cambio de alcance o de precio aprobado por las dos partes, con su efecto en el presupuesto y en lo que se factura.
