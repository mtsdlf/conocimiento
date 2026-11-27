---
resumen: >-
  La reserva de personas es el registro de que una persona va a trabajar en un proyecto unas horas en unas fechas. Nace de un pedido del proyecto, pasa por una propuesta de quien administra a las personas y queda tentativa, que no consume la capacidad de la persona, o firme, que sí.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Project Operations, Booking status (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/booking-status"
  - "Microsoft Learn, Project Operations, Resource management mode overview (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/resource-management-mode-overview"
  - "Microsoft Learn, Project Operations, Submit a resource request (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/submit-resource-request-po"
  - "Microsoft Learn, Project Operations, Bookings and assignments (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/booking-vs-assignment"
  - "Odoo 19, Planning (como evidencia de práctica, leída en el sitio): https://www.odoo.com/documentation/19.0/applications/services/planning.html"
  - "Nesheim, T. (2021), Exploring the resource manager role in a project-based organization, International Journal of Managing Projects in Business, https://doi.org/10.1108/ijmpb-12-2020-0389 (solo el resumen)"
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 5.3.1.6 «Identify, select, and assign resources» y 5.3.3.4 «Release resources»"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 1)"
  - "Servicios-profesionales-y-proyectos/.investigacion/asignacion-y-horas.md (sección 1.4)"
  - "Servicios-profesionales-y-proyectos/.investigacion/verificacion-asignacion-y-horas.md"
aliases: [reserva, booking, reserva tentativa, soft booking, reserva firme, hard booking, pedido de recurso, resource request, staffing request, asignación tentativa, asignación firme]
creado: 2026-11-27
revisado:
---

# Reserva de personas

La reserva de personas es el registro de que una persona va a trabajar en un proyecto unas horas en unas fechas. Nace de un pedido del proyecto, pasa por una propuesta de quien administra a las personas y queda tentativa, que no consume la capacidad de la persona, o firme, que sí.

Es el registro central de la [asignación de personas](asignacion-de-personas.md). Se pide con un [rol](roles-y-habilidades.md), y la suma de las reservas de todos los proyectos es lo que se compara con la capacidad en [demanda y capacidad](demanda-y-capacidad.md). Lo de reserva firme y tentativa sale de un solo sistema de gestión de servicios; no hay una segunda fuente independiente (se buscó una de la literatura o una guía profesional y no apareció), y un sistema abierto usa un esquema distinto (al final).

## Del pedido a la reserva

El recorrido tiene tres pasos, y cada uno lo hace un papel distinto:

1. **Pedido.** Quien lleva el proyecto define un recurso genérico con su requerimiento (rol, horas, fechas, habilidades) y lo envía. El pedido queda enviado.
2. **Propuesta.** Quien administra a las personas busca a alguien y lo propone. El pedido pasa a revisión.
3. **Aceptación.** Quien lleva el proyecto acepta o rechaza. Si se reserva, la persona con nombre reemplaza al genérico en el equipo; si no se cubre, el genérico queda y el hueco se ve.

En ese sistema toda reserva cuelga de un requerimiento: «you must always make bookings against a resource requirement». Si el proyecto no tiene un pedido específico, se reserva contra un requerimiento general que se crea con el proyecto. Como criterio de esta base, esa regla es la que permite saber después por qué alguien está en un proyecto y qué pedido cubre.

## Tentativa, firme, propuesta y cancelada

El sistema documentado tiene cuatro estados de reserva, y lo que los distingue es si consumen la capacidad de la persona:

| Estado | Para qué se usa | Consume capacidad | La persona entra al equipo |
|---|---|---|---|
| Firme (*hard*) | Asignar y reservar a alguien con certeza | Sí | Sí |
| Tentativa (*soft*) | Reservar a alguien sin quitárselo a otros proyectos «until you make a final decision» | No | Sí |
| Propuesta (*proposed*) | Quien administra a las personas ofrece a alguien ante un pedido | No | No, hasta que se decide |
| Cancelada (*canceled*) | Dejar sin efecto una reserva | Libera la que tenía | Sigue figurando en el equipo |

Las transiciones dicen qué evento del proyecto mueve la reserva. De tentativa a firme se consume la capacidad, y el caso típico es un proyecto que esperaba empezar y se confirma. De firme a cancelada se libera, por ejemplo cuando se suspende una tarea. De propuesta a cancelada no cambia nada.

La consecuencia más útil es que dos proyectos pueden tener reserva tentativa sobre la misma persona al mismo tiempo. La tentativa sirve para ver que viene trabajo; la firme, para saber quién está ocupado.

## Quién puede reservar

El mismo sistema ofrece dos modos, configurables por proyecto. En el central, quien administra a las personas cubre los pedidos y quien lleva el proyecto solo acepta o rechaza. En el híbrido, los dos pueden reservar directo. El primero centraliza la decisión; el segundo es más rápido y deja más conflictos para después (lectura de esta base).

Las ausencias entran al mismo tablero: las vacaciones o licencias pendientes aparecen como «Out» para que quien administra a las personas planifique alrededor. Cargar y aprobar esas licencias no es de acá: es de la asistencia, del tema Administración de personal y nómina.

## Conflictos entre proyectos

Las fuentes dicen solo que la reserva firme consume capacidad y la tentativa no. Ninguna página leída describe un bloqueo por sobreasignación, cómo se detecta un choque ni quién lo resuelve. Lo único con método que se leyó es un estudio de caso en una organización con estructura de matriz, donde el responsable de recursos es un jefe de línea que asigna personas y cuyo desafío principal es la relación con los jefes de proyecto (Nesheim, 2021, según el resumen). Dice que existe ese papel y que es tenso, no cómo se resuelve un choque.

> [!NOTE]
> Sin fuente todavía: cómo se resuelve que dos proyectos pidan a la misma persona en firme el mismo mes, quién decide (quien administra a las personas, un comité, la dirección) y con qué criterio. Tampoco hay fuente para el vencimiento de una reserva tentativa. No se pudo leer la guía del PMI sobre recursos en organizaciones matriciales (de pago) ni el artículo de Engwall y Jerbrant (2003) sobre la asignación de recursos entre proyectos (sin acceso al texto).

Como criterio de esta base, lo mínimo que un registro tiene que dar para que alguien decida es la suma de horas firmes por persona y por semana contra su capacidad, y la lista de tentativas que se superponen. La decisión de qué proyecto entra antes es de [portafolio](../../Gestion-de-proyectos/Gobierno-y-cierre/portafolio.md#cuáles-entran), no del registro.

## Reserva y tarea del cronograma

La reserva dice que una persona está en un proyecto; la asignación de tareas dice qué hace dentro de él. El sistema documentado las separa: la reserva es una asignación firme o tentativa al proyecto, y la tarea es el compromiso con una línea del cronograma. «Typically, the sum of the bookings for a resource equals the sum of the resource's assignments», pero el sistema no lo obliga y ofrece una vista de conciliación para quien lleva el proyecto. Cómo se reparte el trabajo dentro del proyecto es de [descomposición del trabajo](../../Gestion-de-proyectos/Planificacion/descomposicion-del-trabajo.md).

## Liberar al terminar

APQC cierra el ciclo con 5.3.3.4 «Release resources», en la categoría 5.3.3 (completar la entrega). Como criterio de esta base, en el registro liberar es cancelar o acortar las reservas firmes que quedan, para que la capacidad vuelva a estar disponible. En el sistema documentado, una reserva cancelada libera capacidad pero deja a la persona en la lista del equipo.

## Turnos en vez de reservas

Un sistema abierto resuelve la planificación con otro esquema, según su documentación: turnos con persona o abiertos (sin persona), que quedan en borrador, con rayas diagonales en el calendario, hasta que se publican, y recién entonces le llegan a cada uno. Las personas tienen roles y los turnos abiertos solo se asignan a quien tiene el rol. Distingue borrador de publicado, no tentativo de firme sobre un proyecto. Sin software, el equivalente de cualquiera de los dos es una columna «firme o tentativa» en la planilla de asignación.
