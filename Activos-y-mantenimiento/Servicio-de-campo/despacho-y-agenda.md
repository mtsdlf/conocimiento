---
resumen: >-
  El despacho es asignar cada orden de servicio a un técnico y a un horario, y la agenda es el resultado: las visitas de cada técnico en el día, con su ruta. Se decide por ubicación, disponibilidad, habilidades y prioridad, dentro de la ventana que el cliente o el contrato aceptan, a mano, con un asistente o con un motor de optimización.
estado: vigente
estabilidad: semi
fuentes:
  - "Microsoft Learn, Overview of Dynamics 365 Field Service, 2026-11-23: https://learn.microsoft.com/en-us/dynamics365/field-service/overview"
  - "Microsoft Learn, Work order lifecycle and system statuses, 2026-08-10: https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status"
  - "Microsoft Learn, Set up customer agreements to generate work orders, 2026-03-02: https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-agreements-work-orders"
  - "Microsoft Learn, Customer agreements overview, 2026-08-28: https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-customer-agreements"
  - "Microsoft Learn, Resource Scheduling Optimization overview, 2026-10-29: https://learn.microsoft.com/en-us/dynamics365/field-service/rso-overview"
  - "Microsoft Learn, Schedule assistant overview: https://learn.microsoft.com/en-us/dynamics365/field-service/schedule-assistant"
  - "Microsoft Learn, Manually schedule from the schedule board: https://learn.microsoft.com/en-us/dynamics365/field-service/schedule-board-manual-scheduling"
  - "Paraskevopoulos, Laporte, Repoussis y Tarantilis, Resource constrained routing and scheduling: Review and research prospects, European Journal of Operational Research 263(3), 2017, 737-754 (manuscrito aceptado, leído en parte: resumen, introducción y sección 2): https://openaccess.city.ac.uk/id/eprint/19845"
  - "Castillo-Salazar, Landa-Silva y Qu, Workforce scheduling and routing problems: literature survey and computational study, Annals of Operations Research, 2014 (solo ficha bibliográfica): https://doi.org/10.1007/s10479-014-1687-2"
  - "Wikipedia, Vehicle routing problem: https://en.wikipedia.org/wiki/Vehicle_routing_problem"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 6.3.4.2 y 6.3.4.3.1: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/servicio-de-campo.md (rondas 1 y 2)"
aliases: [despacho, agenda, despacho y agenda, dispatch, dispatching, scheduling, programación de técnicos, field service scheduling, tablero de programación, schedule board, reserva, booking, ventana horaria, time window, ruteo de técnicos, technician routing, despachante, dispatcher, autoasignación]
creado: 2026-11-27
revisado: 2026-11-27
---

# Despacho y agenda

El despacho es asignar cada orden de servicio a un técnico y a un horario, y la agenda es el resultado: las visitas de cada técnico en el día, con su ruta. Se decide por ubicación, disponibilidad, habilidades y prioridad, dentro de la ventana que el cliente o el contrato aceptan, a mano, con un asistente o con un motor de optimización.

Es el paso entre crear la orden y hacer el trabajo dentro de [Servicio de campo](servicio-de-campo.md). Las órdenes le llegan del caso, cuando deriva a un técnico, o del [contrato de servicio](contrato-de-servicio.md), que las genera solas; lo que sale es una [visita técnica](visita-tecnica.md) con técnico, día y hora. Cumple el papel de la programación de [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md), con una diferencia que la cambia entera: entre una visita y la siguiente hay un viaje. La atención, el caso, el reclamo y el escalamiento son del tema [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md); el despacho empieza cuando el caso deriva a un técnico. APQC lo pone en 6.3.4.2 «Identify and schedule resources to meet service requirements» y 6.3.4.3.1 «Organize daily service order fulfillment schedule».

## La orden de servicio y la visita son dos objetos

El despacho no le pone fecha a la orden: crea una visita que la atiende. Un sistema de servicio de campo de referencia lo dice así: «Work orders and bookings have independent lifecycles». La orden es el trabajo pedido; la visita (en ese sistema, la reserva) es la cita concreta de un técnico, y cada una tiene sus estados:

| Objeto | Estados en el sistema de referencia |
|---|---|
| Orden de servicio | sin programar, programada, en curso, terminada, contabilizada, cancelada |
| Visita | programada, en viaje, en curso, en descanso, terminada, cancelada |

Una orden puede tener varias visitas. Si el técnico no termina, cierra su visita y la orden vuelve a quedar sin programar, esperando la siguiente; eso está en [visita técnica](visita-tecnica.md#cerrar-la-visita-sin-terminar-la-orden). Modelar la orden y la visita como un solo registro obliga a borrar la primera cita para cargar la segunda, y se pierde cuántas veces hubo que ir; esa consecuencia es inferencia de la base.

## Con qué criterios se elige al técnico

El mismo sistema describe un tablero donde los despachantes asignan las órdenes «to the best resources based on location, availability, skill set, priority, and more». Son cuatro preguntas distintas:

- **Ubicación**: qué técnico está cerca, o en qué zona trabaja; el asistente del sistema filtra también por territorio.
- **Disponibilidad**: quién tiene horas libres en la ventana pedida, según su horario de trabajo.
- **Habilidades**: quién sabe hacer este trabajo sobre este equipo; el sistema también habla de características («characteristics») del recurso.
- **Prioridad**: qué orden pasa primero cuando no alcanzan las horas; la prioridad se fija antes, en la [solicitud de trabajo](../Orden-de-trabajo/solicitud-de-trabajo.md) o en el caso.

El recurso que se agenda no es siempre una persona. El tablero muestra «each resource - whether an employee, contractor, or equipment»: un técnico propio, un contratista o un equipo que hay que reservar. Las horas y la capacitación del técnico como empleado son del tema Administración de personal y nómina, todavía no armado.

## La ventana que acepta el cliente

En el sistema de referencia, la visita se promete dentro de una ventana: el contrato pasa a cada orden una ventana de fechas y una franja horaria, con el ejemplo de 8 a 12. Las visitas del contrato tienen además una flexibilidad: el día 8 con ±7 días da una ventana del 1 al 15, como se explica en [contrato de servicio](contrato-de-servicio.md#el-contrato-genera-las-visitas-preventivas).

Por criterio de la base, la ventana limita el orden de las visitas del día. Un ejemplo: un técnico con dos visitas de 8 a 12 en puntas opuestas de la ciudad no llega a las dos, y eso es lo que el ruteo tiene que resolver.

## Manual, asistido u optimizado

El sistema de referencia ofrece tres maneras de despachar:

| Modo | Qué hace | Qué controla |
|---|---|---|
| Manual | El despachante arrastra la orden al técnico en el tablero | Nada: «Manual bookings don't validate constraints like availability, characteristics, or location» |
| Asistido | Un asistente «recommends resources that match criteria like availability, skills, and location» y estima el viaje de cada uno | Solo dentro de lo que recomienda; fuera de esos turnos, capacidad, horario y ventanas «aren't verified or enforced» |
| Optimizado | Un motor programa muchas órdenes a la vez y «maximizes resource use and minimizes travel time» | Habilidades, territorio y «promised time windows», con objetivos ordenados por importancia |

El manual sirve para urgencias, casos simples y excepciones, según la misma documentación. El motor corre en varios modos: nocturno, para un solo recurso, como simulación, intradía (cada 30 minutos) y de emergencia. Los objetivos van rankeados porque implican compensaciones entre sí.

## El técnico acepta o se asigna

El despacho no termina cuando el despachante elige. En el sistema de referencia, el técnico recibe un aviso y «may review and accept/decline the work order»: por inferencia de la base, la visita queda firme cuando la acepta. Qué pasa con un rechazo la fuente no lo detalla; que vuelva al despachante es lo esperable y es inferencia de la base.

El mismo sistema admite dos maneras de programar las órdenes no planificadas: «By field agent or centralized scheduling». En el despacho centralizado, una persona o un motor arma la agenda de todos; en la autoasignación, el técnico toma la orden. Ninguna fuente leída las compara.

> [!NOTE] Sin fuente todavía: cuándo conviene el despacho centralizado y cuándo la autoasignación del técnico, y qué pasa con la carga y la prioridad en cada caso.

## El ruteo es un problema de ruteo de vehículos

Armar la agenda de varios técnicos que salen de un punto, visitan clientes y vuelven es, por inferencia de la base, una forma del problema de ruteo de vehículos. Una de sus variantes incluye ventanas horarias: «The delivery locations have time windows within which the deliveries (or visits) must be made». El motor de optimización del sistema de referencia dice atacar una variante del problema del viajante.

El ruteo de técnicos agrega algo que el problema clásico no tiene: no cualquier técnico sirve para cualquier visita. La enciclopedia leída no menciona técnicos ni habilidades, pero un survey de la investigación operativa sí: en el problema de ruteo de vehículos con habilidades, cada cliente requiere un conjunto de habilidades y los técnicos tienen las suyas, y el objetivo es minimizar el costo de ruteo sin violar esas restricciones (Paraskevopoulos y otros, 2017). El ruteo de camiones con mercadería es del tema Cadena de suministro y logística, todavía no armado; acá solo el de técnicos.

Ese survey (revisión de la literatura) lo llama problema de ruteo y programación de recursos con restricciones y lo describe así: asignar recursos escasos, como técnicos calificados, que deben visitar distintos clientes; lo clasifica por calificaciones del recurso, requisitos del servicio y objetivos, e identifica los algoritmos exactos y heurísticos más eficaces. Las ventanas horarias son frecuentes, duras o blandas. Otro survey anterior sobre programación y ruteo de personal (Castillo-Salazar, Landa-Silva y Qu, Annals of Operations Research) solo se conoce por la cita del primero y por su ficha bibliográfica; su resumen no se leyó.

## Las visitas del contrato no miran la agenda

Las visitas que genera un contrato entran a la agenda sin preguntar si hay lugar. El sistema de referencia lo advierte: «Agreements create bookings according to recurrence without considering any other factors, including if the resource is active or their working hours». Un contrato que fija siempre al mismo técnico puede agendarle una visita fuera de su horario o cuando ya no está activo.

El mismo sistema deja elegir: el contrato bloquea técnico y horario, o deja la reserva al motor de optimización, que sí mira la disponibilidad. Por criterio de la base, fijar al técnico da continuidad con el cliente y dejarlo al motor da una agenda que se cumple. Elegir entre las dos es una decisión de diseño del contrato, y revisar a mano las visitas generadas cuando el técnico está fijo es criterio de la base.
