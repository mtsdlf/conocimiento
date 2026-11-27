---
resumen: >-
  El acuerdo de nivel de servicio fija, para cada prioridad, dos tiempos: el de primera respuesta y el de resolución. El reloj que los mide corre solo dentro del horario de atención, se detiene los feriados y se pausa mientras el caso espera algo del cliente.
estado: borrador
estabilidad: semi
fuentes:
  - "ERPNext, Service Level Agreement: https://docs.frappe.io/erpnext/user/manual/en/service-level-agreement (como evidencia de práctica; leída en un resumen del lector)"
  - "Odoo 19.0, Helpdesk, SLA: https://www.odoo.com/documentation/19.0/applications/services/helpdesk/overview/sla.html (como evidencia de práctica, según resumen del buscador; la página dio 404)"
  - "Servicio-al-cliente/.investigacion/canales-y-niveles-de-servicio.md, sección 5"
aliases: [tiempo de primera respuesta, first response time, FRT, tiempo de resolución, resolution time, reloj del SLA, SLA clock, horario de atención, business hours, horario hábil, pausa del SLA, SLA pause, vencimiento]
creado: 2026-11-27
revisado:
---

# Tiempos de respuesta y resolución

El acuerdo de nivel de servicio fija, para cada prioridad, dos tiempos: el de primera respuesta y el de resolución. El reloj que los mide corre solo dentro del horario de atención, se detiene los feriados y se pausa mientras el caso espera algo del cliente.

Es el componente operativo de los [niveles de servicio](niveles-de-servicio.md): el acuerdo dice qué se promete y esta nota, cómo se cuenta. La prioridad que elige los tiempos viene de la [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md) del caso, y los estados que pausan el reloj son estados del [caso](../Caso/caso.md). Cuando el reloj llega a cero, empieza el [incumplimiento del acuerdo](incumplimiento-del-acuerdo.md).

## Primera respuesta y resolución

Los dos tiempos miden cosas distintas. La **primera respuesta** es cuánto tarda el cliente en saber que alguien tomó su caso. La **resolución** es cuánto tarda en tener lo que pidió. Un caso puede cumplir la primera y vencer la segunda.

En un sistema abierto, cada prioridad del acuerdo tiene su tiempo para responder y su tiempo para resolver, en horas y minutos, y una de ellas es la prioridad por defecto: «Default Priority selected in Priorities table that will be applied in the Service Level Agreement». Otro sistema, independiente del primero, arma el acuerdo como una etapa objetivo del caso y un tiempo asignado para llegar a ella. Las dos formas son equivalentes: el objetivo es un evento del caso (la primera respuesta, el paso a resuelto) y un plazo para que ocurra.

Qué evento para el reloj de resolución depende de cómo el [caso](../Caso/caso.md) separe resuelto de cerrado. Si para al pasar a resuelto, mide el trabajo de quien atiende; si para al cierre, suma el tiempo que el cliente tarda en confirmar. La elección se escribe en el acuerdo (lectura de esta base).

## Las tres piezas del reloj

Dos productos independientes resuelven el reloj con las mismas tres piezas. La lectura de esta base es que son parte del dominio, no de un producto; es evidencia de práctica y no una definición normativa.

1. **El horario de atención.** Se definen días con hora de inicio y fin, y el reloj corre solo dentro de esas ventanas. En el otro sistema, el horario viene por defecto del de la empresa.
2. **Los feriados.** El sistema abierto lo dice así: «Service Level Agreement won't be applied in the days mentioned in the Holiday List».
3. **Las pausas por estado.** Se eligen estados del caso que detienen el reloj, típicamente los de espera de una respuesta del cliente. En el sistema abierto, mientras el caso está en uno de esos estados los vencimientos se limpian; al salir, se registra el tiempo en espera y «The Response and Resolution time will be recalculated by adding the hold time». En el otro, el tiempo en las etapas excluidas no cuenta para el vencimiento.

## Un caso que entra un viernes a la noche

Un ejemplo de esta base, aplicando las tres piezas: el acuerdo da 4 horas hábiles para la primera respuesta y 16 para la resolución, con horario de lunes a viernes de 9 a 18. Un caso entra el viernes a las 21. El reloj no corre hasta el lunes a las 9, así que la primera respuesta vence el lunes a las 13. Si el lunes es feriado, todo se corre al martes.

Si el martes a las 11, con 2 horas consumidas, quien atiende le pide al cliente una foto y pasa el caso a «esperando al cliente», el reloj se detiene. El cliente contesta el jueves a las 10: el reloj sigue desde las 2 horas consumidas, y al vencimiento se le suma el tiempo en espera. Sin la pausa, el caso habría vencido mientras la empresa esperaba al cliente.

## Varios acuerdos sobre un mismo caso

Un caso puede cumplir las condiciones de más de un acuerdo: uno por el cliente, otro por el tipo de caso. Uno de los sistemas leídos, en ese caso, muestra el vencimiento más próximo. Es una regla de un producto; la otra opción razonable es que el acuerdo más específico gane (lectura de esta base). La regla tiene que estar escrita, porque decide qué plazo ve quien atiende.

Cuando la prioridad cambia a mitad del caso, cambian los objetivos que le tocan. Cómo y por qué cambia la prioridad está en [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md).

## Qué guarda el sistema por caso

Para que el reloj se pueda auditar, el caso guarda el acuerdo que le tocó, la fecha de creación, la de primera respuesta, la de resolución, el tiempo total en pausa y los vencimientos calculados de respuesta y de resolución (lectura de esta base sobre los dos productos). Con esos datos se reconstruye por qué un caso venció o no, y se arman las [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md).

## Dónde falla el reloj

Falla en la reapertura: ninguna de las páginas leídas explica qué pasa con el reloj cuando un caso cerrado se reabre, si sigue el que había o empieza uno nuevo.

> [!NOTE] Sin fuente todavía: cómo se trata el reloj al reabrir un caso.

Falla cuando los estados de pausa se usan para frenar el reloj sin que el caso espere de verdad al cliente: el acuerdo se cumple en el reporte y no en la realidad, que es una forma del efecto descrito en [incumplimiento del acuerdo](incumplimiento-del-acuerdo.md) (lectura de esta base). Y falla cuando el calendario del acuerdo no es el de quien atiende: si el acuerdo promete horas corridas y el equipo trabaja en horario de oficina, los casos de la noche vencen solos.

Los plazos de respuesta que fija la ley argentina están en [Servicio al cliente en la Argentina](../servicio-al-cliente-en-argentina.md).
