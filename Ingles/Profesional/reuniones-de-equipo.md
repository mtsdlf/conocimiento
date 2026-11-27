---
resumen: >-
  Las reuniones de un equipo de software (la daily, la planning, la retro) son eventos cortos con
  una forma esperada: un update en titulares, los bloqueos dichos temprano y el desacuerdo planteado
  sin frenar al equipo. En inglés y con colegas de otros países, lo que más cuesta es entrar a
  tiempo y decir algo incómodo sin sonar brusco.
estado: vigente
estabilidad: semi
fuentes:
  - "Schwaber y Sutherland, The Scrum Guide (noviembre de 2020): https://scrumguides.org/scrum-guide.html"
  - "Stray, Moe y Sjøberg (2020), Daily stand-up meetings: start breaking the rules, IEEE Software 37(3), 70-77, preprint (abstract): https://arxiv.org/abs/1808.07650"
  - "Jason Yip, It's not just standing up: patterns for daily standup meetings (martinfowler.com): https://www.martinfowler.com/articles/itsNotJustStandingUp.html"
  - "Atlassian Team Playbook, Retrospective: https://www.atlassian.com/team-playbook/plays/retrospective"
  - "Atlassian Team Playbook, Stand-ups, vía resumen del buscador: https://www.atlassian.com/team-playbook/plays/standups"
  - "Bezos, carta a los accionistas de 2016: https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders"
  - "Rogerson-Revell (2010), reuniones internacionales, Journal of Business Communication 47(4), vía resumen de strategy+business: https://strategy-business.com/article/re00128"
  - "OpenStack Contributor Guide, Non-native English speakers: https://docs.openstack.org/contributor-guide/non-native-english-speakers.html"
  - "McSweeney (2002), Hofstede's model of national cultural differences and their consequences, Human Relations 55(1), vía metadatos: https://pure.royalholloway.ac.uk/en/publications/hofstedes-identification-of-national-cultural-differences-and-the"
aliases:
  - Daily standup
  - Daily
  - Standup
  - Retro
  - Retrospective
  - Sprint planning
  - Disagree and commit
creado: 2026-11-27
revisado: 2026-11-27
---

# Reuniones de equipo

Las reuniones de un equipo de software (la daily, la planning, la retro) son eventos cortos con una forma esperada: un update en titulares, los bloqueos dichos temprano y el desacuerdo planteado sin frenar al equipo. En inglés y con colegas de otros países, lo que más cuesta es entrar a tiempo y decir algo incómodo sin sonar brusco.

Son la versión de trabajo de lo que [Interacción](../Discurso/interaccion.md) explica en general (turnos, ganar tiempo, reparar) y de lo que [Registro y cortesía](../Discurso/registro-y-cortesia.md) explica sobre suavizar. Muchas de estas conversaciones también pasan por escrito; qué va a una reunión y qué a un mensaje se decide en [Trabajo remoto y asincrónico](trabajo-remoto-asincronico.md).

## La daily: titulares, no la historia

La Scrum Guide de 2020 define el propósito del Daily Scrum como "to inspect progress toward the Sprint Goal": dura 15 minutos, es para los desarrolladores y ellos pueden elegir "whatever structure and techniques they want". Las tres preguntas clásicas no son obligatorias. Son una convención, que Jason Yip resume como *Yesterday, Today, Obstacles* en su artículo sobre patrones de la daily. Atlassian las formula así, según el resumen del buscador: *Since the last stand-up, I have… / Before the next stand-up, I will… / What's slowing me down is…*.

Yip da la regla que más le sirve a quien habla en segunda lengua: "Tell the headline, not the whole story". La daily es para levantar temas, "not a time for in-depth problem-solving". Un update de tres oraciones en inglés claro rinde más que uno largo con muchas subordinadas. Dos ejemplos propios:

- *Yesterday I finished the retry logic for the payments webhook. Today I'm writing the tests. No blockers.*
- *I'm still on the migration script. It's taking longer than I expected because of the old data, so I probably won't finish today.*

Stray, Moe y Sjøberg observaron 102 dailies y entrevistaron a 60 personas de 15 equipos en cinco países: muchas tenían experiencias negativas con la reunión, que bajaban la satisfacción y la confianza. Por eso proponen "romper las reglas" y adaptarla. Ese trabajo se leyó solo por su resumen.

## Decir que estás bloqueado o que no llegás

Un bloqueo dicho temprano es información; dicho tarde es un problema. El castellano rioplatense tiende a la forma directa en los pedidos ([Registro y cortesía](../Discurso/registro-y-cortesia.md)), pero para avisar un riesgo el problema suele ser el contrario: callarlo hasta tener una solución. Como inferencia propia, un aviso en inglés de equipo tiene tres partes: qué pasa, qué impacto tiene y qué necesitás. Las frases son ejemplos propios:

| Para | Frase |
|---|---|
| Bloqueo | *I'm blocked on the API keys. Could someone from the platform team help me after this?* |
| Riesgo de plazo | *Heads-up: I don't think I'll make it by Friday. The integration is more complex than we estimated.* |
| Pedir ayuda sin culpa | *I've been stuck on this for a couple of hours. Can I pair with someone for 15 minutes?* |
| Llevar un tema afuera | *Let's take this offline.* / *Can we discuss this after the standup?* |

*Let's take this offline* significa "lo hablamos fuera de la reunión", no "desconectados".

## La planning: estimar en voz alta

En la planning se decide qué entra en el ciclo y se estima. En inglés aparecen dos necesidades: dar una estimación con su incertidumbre (*My gut feeling is three days, but I'm not confident until I look at the legacy code*) y preguntar antes de comprometerse (*What does "done" mean for this one?*). Cómo se estima en sí está en [Estimación](../../Desarrollo/Encargo/estimacion.md).

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre cómo se habla en la planning y en la estimación (planning poker, story points); la Scrum Guide solo define el evento.

## La retro: mejorar sin culpar

La Scrum Guide dice que el propósito de la retrospectiva es "to plan ways to increase quality and effectiveness". El Team Playbook de Atlassian la arma en cinco pasos: tono (unos 5 minutos), recoger feedback (unos 15), convertirlo en ideas (unos 20), acciones con dueño y fecha (unos 15) y cierre (unos 5). Propone formatos como *4Ls* (*loved, loathed, learned, longed for*) y *Sad / Mad / Glad*, y una regla: "Focus on improving instead of blaming people for mistakes". Esa misma regla rige el [postmortem](incidentes.md). En inglés se nota en el sujeto: *The deploy process didn't catch the missing config* en lugar de *Juan forgot the config*.

## Discrepar y comprometerse

El desacuerdo en una reunión de trabajo en inglés suele suavizarse con lo que [Registro y cortesía](../Discurso/registro-y-cortesia.md) llama matizar: *I see your point, but I'm worried about…*, *I'm not sure that's the best option, because…*. Amazon le puso nombre a lo que viene después: *disagree and commit*. En su carta a los accionistas de 2016, Bezos escribió que se puede decir "Look, I know we disagree on this but will you gamble with me on it? Disagree and commit?", y contó un caso propio: "I disagree and commit and hope it becomes the most watched thing we've ever made."

> [!IMPORTANT]
> **¿Cuán directo hay que ser?** Libros de divulgación como *The Culture Map* de Erin Meyer ubican a cada país en escalas de comunicación, de evaluación y de desacuerdo. Sirven como heurística, pero no se halló validación empírica de esas escalas, y los modelos de cultura nacional como el de Hofstede tienen críticas académicas fuertes, entre ellas la de McSweeney (2002): la cultura de un país no predice cómo actúa cada persona. Las fuentes secundarias consultadas tampoco coinciden en qué tan directa es la crítica en EE.UU. Por eso conviene mirar al equipo concreto antes que al país.

## No nativos en la misma reunión

En las reuniones internacionales que estudió Rogerson-Revell (2010), según un resumen de strategy+business, nativos y no nativos solían dejar pasar los errores menores para seguir con el contenido. Era práctico y cortés, pero no evitaba los malentendidos ni la frustración de los no nativos. Según ese resumen, ayudaba evitar modismos, tener agendas estrictas y preparar las intervenciones. La guía de OpenStack para su comunidad le pide a los no nativos que se preparen antes. Como consejo propio, llevar escritas dos o tres oraciones sobre el punto que querés plantear baja la carga de entrar al turno en vivo.

> [!NOTE]
> Sin fuente todavía: frases modelo respaldadas por un material de inglés profesional para avisar bloqueos, plazos y desacuerdos; las que aparecen acá son ilustraciones propias.
