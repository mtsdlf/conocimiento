---
resumen: >-
  El code review en inglés es el género de los comentarios que se dejan sobre el código de otra
  persona y de las respuestas a esos comentarios: se comenta el código y no a quien lo escribió, se
  explica el porqué y se marca cuánto importa cada observación.
estado: vigente
estabilidad: semi
fuentes:
  - "Google Engineering Practices, How to write code review comments: https://google.github.io/eng-practices/review/reviewer/comments.html"
  - "Google Engineering Practices, How to handle reviewer comments: https://google.github.io/eng-practices/review/developer/handling-comments.html"
  - "Conventional Comments: https://conventionalcomments.org/"
  - "Gunawardena et al. (2022), Destructive criticism in software code review impacts inclusion, CSCW, vía resumen: https://research.google/pubs/destructive-criticism-in-software-code-review-impacts-inclusion/"
  - "Egelman et al. (2020), Predicting developers' negative feelings about code review, ICSE, vía resumen: https://research.google/pubs/predicting-developers-negative-feelings-about-code-review/"
  - "Ortu et al. (2015), Are bullies more productive?, MSR, vía resumen: https://bura.brunel.ac.uk/handle/2438/12369"
  - "Ortu et al. (2016), Software development: do good manners matter?, PeerJ Computer Science, vía resumen: https://peerj.com/articles/cs-73"
aliases:
  - Code review comments
  - Comentarios de code review
  - Nit
  - Conventional Comments
  - Pushback
creado: 2026-11-27
revisado: 2026-11-27
---

# Code review

El code review en inglés es el género de los comentarios que se dejan sobre el código de otra persona y de las respuestas a esos comentarios: se comenta el código y no a quien lo escribió, se explica el porqué y se marca cuánto importa cada observación.

Qué es una revisión de código y qué revisa cada uno está en [Revisión de código](../../Desarrollo/Verificacion/revision-de-codigo.md); acá va solo cómo se escribe. Es un caso particular de lo que [Registro y cortesía](../Discurso/registro-y-cortesia.md) explica sobre suavizar una crítica, y vive al lado de la descripción del cambio que se revisa ([Escritura técnica](escritura-tecnica.md#la-descripción-de-un-pull-request)).

## Comentar el código, no a la persona

La guía de code review de Google pide ser "courteous and respectful" y a la vez muy claro. Su mal ejemplo es este: "Why did you use threads here when there's obviously no benefit to be gained from concurrency?". La versión que propone habla del diseño y no de la persona: que la concurrencia agrega complejidad sin una ganancia de rendimiento que se vea. También pide explicar el porqué de cada comentario.

En inglés, el cambio se nota en el sujeto y en el modo. Algunas transformaciones típicas (ejemplos propios):

| Suena brusco | Suena a revisión |
|---|---|
| *You forgot to handle the null case.* | *This will throw if `user` is null. Should we handle that here?* |
| *This is wrong.* | *I think this returns the old value, because the cache isn't invalidated yet.* |
| *Change this to a map.* | *What do you think about using a map here? Lookups would be O(1).* |
| *Why did you do it like this?* | *Can you help me understand why this goes through the queue?* |

Para un hispanohablante, la traducción literal de un comentario corto en castellano (*esto está mal*, *cambiá esto*) suele caer en la columna de la izquierda (inferencia propia). La razón está en cómo el castellano rioplatense hace los pedidos ([Registro y cortesía](../Discurso/registro-y-cortesia.md#por-qué-el-pedido-rioplatense-suena-directo-en-inglés)).

> [!NOTE]
> La guía de Google no trae una regla explícita de preferir preguntas a órdenes; las frases de la tabla son ejemplos propios y no salen de la fuente.

## Marcar cuánto importa cada comentario

Un review con veinte comentarios del mismo peso no deja ver cuáles bloquean. Google propone prefijos de severidad, con estas definiciones literales:

- "Nit: This is a minor thing. Technically you should do it, but it won't hugely impact things."
- "Optional (or Consider): I think this may be a good idea, but it's not strictly required."
- "FYI: I don't expect you to do this in this CL, but you may find this interesting to think about for the future."

**Conventional Comments** es una convención de la comunidad que lleva la idea más lejos, con el formato `<label> [decorations]: <subject>`. Sus etiquetas son *praise, nitpick, suggestion, issue, todo, question, thought, chore* y *note*, y las decoraciones *(blocking)*, *(non-blocking)* e *(if-minor)*. Ejemplos de su sitio:

- "**question (non-blocking):** At this point, does it matter which thread has won?"
- "**suggestion:** Let's avoid using this specific function…"
- "**praise:** Beautiful test!"
- "**issue (ux,non-blocking):** These buttons should be red, but let's handle this in a follow-up."

La convención pide dejar al menos un elogio por review, y que no sea falso. Como inferencia propia, para quien escribe en segunda lengua las etiquetas hacen parte del trabajo de tono: *nit:* ya avisa que es menor, sin tener que suavizarlo con palabras.

## Responder sin ponerse a la defensiva

Para quien recibe el review, la guía de Google es directa: "Never respond in anger to code review comments." La pregunta que propone hacerse es "What is the constructive thing that the reviewer is trying to communicate to me?". Si hay desacuerdo, pide pensar "collaboratively, not combatively or defensively", y que el primer paso sea siempre buscar consenso con el revisor.

Algunas frases de respuesta (ejemplos propios): *Good catch, fixed.* / *Done.* / *I went with X because of Y, but happy to change it if you feel strongly.* / *I'd rather keep this as is, because… What do you think?* / *Let's do this in a follow-up PR.*

## Qué dice la investigación sobre el tono

La investigación respalda el daño de la crítica destructiva; el beneficio de una fórmula cortés no tiene respaldo. Gunawardena y colegas (2022) presentaron escenarios a 93 profesionales: la crítica destructiva, inespecífica y de tono duro, se percibió como menos válida y con menos chances de mejorar el código, y las mujeres quedaron menos dispuestas a seguir trabajando con quien la daba. Egelman y colegas (2020) estudiaron el *pushback* (la sensación de un conflicto interpersonal innecesario mientras se bloquea un cambio) en 1.317 desarrolladores de una empresa. Los dos trabajos se leyeron por su resumen.

> [!IMPORTANT]
> **¿Ser cortés acelera el trabajo?** No hay un resultado limpio. En datos de Jira, un estudio de Ortu y colegas (2015) halló que más cortesía se asociaba a arreglos más lentos, y otro del mismo grupo (2016), a más rápidos. Son datos de tickets, no de code review, y observacionales. Lo defendible es más acotado: daña lo inespecífico y hostil, y la claridad directa sobre el código no daña. Las frases suaves son una convención de tono de la comunidad, sin eficacia medida.
