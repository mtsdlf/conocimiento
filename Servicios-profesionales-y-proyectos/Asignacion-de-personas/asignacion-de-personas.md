---
resumen: >-
  La asignación de personas es decidir, a nivel de la firma, quién trabaja en qué proyecto y en qué semanas. Se compara la demanda que viene de los proyectos vendidos y del embudo con la capacidad de las personas, se pide por rol y se reserva a personas con nombre, en firme o en tentativa.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 5.2 «Manage service delivery resources», 5.3.1.6 «Identify, select, and assign resources» y 5.3.3.4 «Release resources»"
  - "Microsoft Learn, Project Operations, Resource management key concepts (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/resource-management-key-concepts"
  - "Microsoft Learn, Project Operations, Resource management mode overview (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/resource-management-mode-overview"
  - "Microsoft Learn, Project Operations, Booking status (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/booking-status"
  - "Servicios-profesionales-y-proyectos/.investigacion/asignacion-y-horas.md (sección 1)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (secciones 1 y 2)"
aliases: [asignación de recursos, resource management, gestión de recursos, staffing, planificación de recursos, resource planning, dotación de proyectos]
creado: 2026-11-27
revisado:
---

# Asignación de personas

La asignación de personas es decidir, a nivel de la firma, quién trabaja en qué proyecto y en qué semanas. Se compara la demanda que viene de los proyectos vendidos y del embudo con la capacidad de las personas, se pide por rol y se reserva a personas con nombre, en firme o en tentativa.

Dentro de [Servicios profesionales y proyectos](../servicios-profesionales-y-proyectos.md) es la vertical que une la venta con el trabajo. Recibe del [proyecto del cliente](../Proyecto-del-cliente/proyecto-del-cliente.md) los roles, las horas y las fechas que fijó su [presupuesto](../Proyecto-del-cliente/presupuesto-del-proyecto.md). Le da al [registro de horas](../Registro-de-horas/registro-de-horas.md) el equipo de cada proyecto, que es quien después carga horas en él. Sin software es una planilla con una fila por persona, una columna por semana y, en cada celda, el proyecto y las horas.

## Dos momentos que el marco de procesos separa

APQC no tiene la asignación como proceso propio: la reparte en dos momentos y un cierre. El plan de la firma vive en 5.2 «Manage service delivery resources», antes de que exista el proyecto, con tres ramas: la demanda (5.2.1), el plan de recursos (5.2.2) y la habilitación de las personas (5.2.3). La asignación a un proyecto concreto vive en otra parte, dentro de la entrega: 5.3.1.6 «Identify, select, and assign resources», con «Establish people objectives» y «Establish engagement rules». La liberación de las personas al terminar es 5.3.3.4 «Release resources».

Esta vertical junta los tres, porque, como criterio de esta base, conviene tratarlos como un solo registro: el pedido de un rol, la reserva de una persona y su liberación se leen como etapas de una misma fila. La capacitación (5.2.3) queda afuera; seleccionar, evaluar y hacer crecer a las personas es de [Gestión de personas](../../Liderazgo-y-direccion/Gestion-de-personas/gestion-de-personas.md).

## La capacidad de la firma y la del proyecto

La capacidad se mira en tres alturas, y cada una tiene su nota en la base. Dentro de un proyecto, cuánto termina un equipo por semana y por qué cargarlo al 100 % alarga el plazo está en [capacidad y costo](../../Gestion-de-proyectos/Planificacion/capacidad-y-costo.md); cuántos proyectos corren en paralelo, en [portafolio](../../Gestion-de-proyectos/Gobierno-y-cierre/portafolio.md). Cuántos clientes entran en un equipo antes de que la espera se dispare, con la cuenta de colas, está en [capacidad de un equipo de servicio](../../Emprender/Modelo-de-negocio/capacidad-de-un-equipo-de-servicio.md).

Esta vertical trata la altura que falta: persona por persona y semana por semana, a través de todos los proyectos de la firma. Es la que responde si la persona que pide un proyecto está libre en marzo y si en tres meses van a faltar dos personas de un rol.

## Quien pide y quien administra a las personas

En la práctica de los sistemas de gestión de servicios hay dos papeles. Quien lleva el proyecto define qué necesita: un rol, unas horas, unas fechas. Quien administra a las personas de la firma busca a alguien que cumpla y lo propone. Un sistema documenta dos formas de repartirlo. En la central, el administrador de las personas cubre los pedidos y el jefe de proyecto acepta o rechaza a quien le proponen. En la híbrida, los dos pueden reservar directo. El modo es un dato del proyecto y se puede cambiar.

La reserva tiene dos intensidades. La firme consume la capacidad de la persona; la tentativa la deja en el equipo pero sin consumirla, así que puede seguir ofreciéndose a otros proyectos. El detalle de los estados está en [reserva de personas](reserva-de-personas.md).

> [!NOTE]
> Sin fuente todavía: quién decide cuando dos proyectos quieren a la misma persona en firme, y con qué criterio (margen, cliente, fecha de firma, riesgo). Las fuentes leídas describen los dos papeles y que colaboran, pero ninguna dice quién arbitra.

## Cómo falla la asignación

Falla cuando la reserva y el trabajo real se separan. Un sistema advierte que la suma de las reservas de una persona y la suma de sus tareas en el cronograma suelen coincidir, pero no lo obliga, y ofrece una vista para conciliarlas. Si nadie la mira, la planilla de la firma dice una cosa y los proyectos otra.

Como criterio de esta base, falla también por dos vicios de la reserva tentativa. Si nunca se confirma ni se cancela, la persona parece ocupada sin estarlo. Si nadie reserva en tentativa, la firma ve el hueco recién cuando el proyecto se firma. El otro error común es llenar a todos al 100 %, que las notas de capacidad enlazadas arriba explican.

## Qué hay en la asignación de personas

- [Roles y habilidades](roles-y-habilidades.md): el rol genérico con que se pide y se precia, la persona con nombre que lo cubre y la escala de habilidades con que se las empareja.
- [Reserva de personas](reserva-de-personas.md): el pedido de un rol, la propuesta, la reserva tentativa y la firme, la cancelación y los conflictos entre proyectos.
- [Demanda y capacidad](demanda-y-capacidad.md): el pronóstico de cuánta gente hace falta desde los proyectos vendidos y el embudo, el banco de personas libres y cuándo subcontratar.
