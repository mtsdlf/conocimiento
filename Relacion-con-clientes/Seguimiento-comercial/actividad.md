---
resumen: >-
  La actividad es el registro de cada interacción con un cliente o un interesado, hecha o pendiente: una llamada, una visita, un correo, una reunión, una tarea. Colgadas de la cuenta, el contacto o la oportunidad, las actividades arman la historia del cliente; su punto débil es que dependen de que alguien las cargue.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, tabla Activity (ActivityPointer), actualizada 2026-09-17: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/activitypointer (como evidencia de práctica)"
  - "Microsoft Learn, tabla Lead: https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/lead (como evidencia de práctica)"
  - "ERPNext, Opportunity: https://docs.frappe.io/erpnext/user/manual/en/opportunity (como evidencia de práctica)"
  - "Nutshell, «9 Reasons Why Sales Reps Quit Their CRMs» (blog de un proveedor de CRM): https://www.nutshell.com/blog/reasons-why-sales-reps-quit-their-crms"
  - "HubSpot, «team not using CRM» (blog de un proveedor de CRM): https://blog.hubspot.com/sales/team-not-using-crm (según resumen del buscador)"
  - "HubSpot, «Why your sales reps hate CRM software» (blog de un proveedor de CRM, cita una encuesta de Introhive): https://blog.hubspot.com/sales/why-your-sales-reps-hate-crm-software (según resumen del buscador)"
  - "David Taber, «How to solve CRM data deduplication dilemmas», CIO.com, 1 de octubre de 2013: https://www.cio.com/article/2382113/how-to-solve-crm-data-deduplication-dilemmas.html"
  - "Relacion-con-clientes/.investigacion/registro-y-seguimiento.md, componente 6; fundamentos-y-contraria.md, sección 6.c"
aliases: [activity, actividad comercial, interacción, historial del cliente, línea de tiempo del cliente, timeline, tarea, próximo contacto, registro de llamadas, carga de datos en el CRM, adopción del CRM]
creado: 2026-11-27
revisado:
---

# Actividad

La actividad es el registro de cada interacción con un cliente o un interesado, hecha o pendiente: una llamada, una visita, un correo, una reunión, una tarea. Colgadas de la cuenta, el contacto o la oportunidad, las actividades arman la historia del cliente; su punto débil es que dependen de que alguien las cargue.

Es el tercer objeto del [seguimiento comercial](seguimiento-comercial.md). Va acá y no en el [registro del cliente](../Registro-del-cliente/registro-del-cliente.md) porque nace en la venta en curso, aunque se muestre en la ficha del cliente. Cuántas veces insistir y cada cuánto es método, y está en [seguimiento](../../Ventas/Prospeccion/seguimiento.md) de Ventas; acá se registra lo que se hizo y lo que falta.

## Qué es una actividad

Un CRM de un proveedor grande la define como una tarea hecha o por hacer por un usuario, y como cualquier acción que puede anotarse en un calendario. Dos rasgos de ese diseño se repiten:

- **Lo hecho y lo pendiente son el mismo objeto.** Una llamada programada para mañana y una llamada de ayer se distinguen por su estado y su fecha, no por estar en tablas distintas. Así, completar una tarea no crea un registro nuevo: cambia el que había.
- **La actividad apunta a cualquier objeto.** Tiene un campo «referido a» que puede señalar una cuenta, un contacto, una oportunidad o un interesado. Esa referencia es la que arma la línea de tiempo: la ficha del cliente muestra todas las actividades que apuntan a él y a sus oportunidades.

El mismo sistema da al interesado un vínculo rápido al cliente para ver, en un solo lugar, su cuenta, sus actividades y sus oportunidades. Un sistema abierto resuelve el seguimiento programado con dos campos en la oportunidad, la fecha del próximo contacto y quién lo hace, que agregan un evento al calendario del responsable.

> [!NOTE] Sin fuente todavía: la lista de tipos de actividad (llamada, correo, reunión, tarea, visita) como estándar; los sistemas la traen, pero no se verificó en las páginas leídas.

## Cómo se carga

Hay tres formas, de más manual a más automática: el vendedor la escribe a mano después de cada interacción; el sistema la crea a partir del correo o del calendario, si están conectados; o la crea otro sistema, como el teléfono o el chat. Cuanto más manual, más depende de la disciplina de quien vende. Esto es criterio de la base; no se encontró una fuente que compare las tres.

## Por qué los vendedores no la cargan

La actividad es la víctima más común de la falta de carga. Toda la evidencia encontrada es de proveedores de software de ventas, que tienen interés en que el problema parezca de adopción y no de diseño, y que citan estudios de terceros sin enlazarlos:

- Un blog de un proveedor de CRM atribuye a ESNA que el 79 % de los datos de oportunidades que juntan los vendedores nunca entra al sistema, a MHI Global que solo un tercio de los proyectos de CRM logra que lo use el 90 % o más del equipo de ventas, y a SuperOffice que menos del 40 % de las empresas que lo implementan lo usa a pleno.
- Otro blog de proveedor, citando a un tercer proveedor, habla de cinco horas y media por semana de carga manual por vendedor.

Las razones que repiten esos blogs son parecidas: el vendedor ve el sistema como una herramienta para que lo controlen, no le ahorra tiempo, es complicado, no se usa bien desde el teléfono, tiene datos malos que le quitan confianza y está mal integrado con el correo. Según el resumen de uno de ellos, la raíz es que el vendedor no ve un beneficio propio, y una capacitación única no alcanza.

La lectura de diseño que sale de ahí es inferencia de la base, no un resultado probado: pedir pocos campos obligatorios, cargar solo lo que alguien va a leer, crear la actividad desde el correo o el calendario cuando se pueda, y darle al vendedor algo a cambio (un recordatorio, una lista de pendientes) en lugar de solo pedirle datos. La discusión más amplia sobre por qué fracasan los CRM está en [mitos del CRM](../Fundamentos/mitos-del-crm.md).

## Cuando la historia está mal

Una historia incompleta engaña más que una vacía: quien abre la ficha cree que no se habló con el cliente desde hace meses y lo vuelve a llamar con la misma oferta. Los datos malos se alimentan solos: el blog de proveedor citado arriba pone los datos malos entre las razones por las que el vendedor deja de confiar en el sistema, y un sistema en el que nadie confía se carga menos. Taber, en una columna de práctica, pone umbrales a los duplicados (ver [cuenta y contacto](../Registro-del-cliente/cuenta-y-contacto.md)). Lo general de la calidad de un dato está en [calidad de datos](../../Datos/Gobierno-y-calidad/calidad-de-datos.md).

Las actividades guardan lo que se habló con personas, y eso es un dato personal: lo general está en [privacidad de datos personales](../../Datos/Gobierno-y-calidad/privacidad-de-datos-personales.md). El caso posterior a la venta (un reclamo, una consulta de soporte) no es una actividad comercial: es del tema Servicio al cliente, todavía no armado, aunque la ficha del cliente pueda mostrar los dos.
