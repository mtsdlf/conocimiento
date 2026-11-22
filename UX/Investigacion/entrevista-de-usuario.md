---
resumen: >-
  La entrevista de usuario es un método generativo y actitudinal: una conversación guiada con una persona para entender su contexto, sus tareas y sus motivos. Captura lo que la persona dice de su conducta, no lo que hace, y por eso se completa con observación o datos de uso.
estado: borrador
estabilidad: semi
fuentes:
  - "NN/g, User Interviews 101: https://www.nngroup.com/articles/user-interviews/ (leída a través del resumen de una herramienta)"
  - "NN/g, How Many Participants for a UX Interview?: https://www.nngroup.com/articles/interview-sample-size/ (leída a través del resumen de una herramienta)"
  - "Guest, Bunce y Johnson (2006), Field Methods 18(1):59-82, doi 10.1177/1525822X05279903 (leído a través de NN/g y del buscador, no el paper)"
  - "NN/g, Jakob Nielsen (2001), First Rule of Usability? Don't Listen to Users: https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/"
  - "Steve Portigal, Interviewing Users, 2.ª ed. (2023), Rosenfeld Media: https://rosenfeldmedia.com/books/interviewing-users-second-edition/ (solo metadatos)"
  - "Rob Fitzpatrick, The Mom Test (2013), según el resumen https://www.shortform.com/blog/what-is-the-mom-test/ (libro no leído)"
  - "UX/.investigacion/investigacion-y-evaluacion.md y UX/.investigacion/posicion-contraria.md"
aliases: [entrevista a usuarios, user interview, entrevista de investigación, entrevista semiestructurada]
creado: 2026-11-22
revisado:
---

# Entrevista de usuario

La entrevista de usuario es un método generativo y actitudinal: una conversación guiada con una persona para entender su contexto, sus tareas y sus motivos. Captura lo que la persona dice de su conducta, no lo que hace, y por eso se completa con observación o datos de uso.

NN/g la ubica en la fase generativa (Strategize) del [mapa de métodos](metodos-de-investigacion.md), dentro de la [investigación generativa](investigacion.md). Por ser un método cualitativo (clasificación de esta base), contesta por qué y cómo, y no cuántos.

## Lo que la entrevista no puede ver

NN/g enumera los límites del autorreporte: el recuerdo es imperfecto, la persona omite cosas y tiende a responder lo que queda bien (deseabilidad social). Para conocer la conducta real hay que observar o usar datos de comportamiento.

> [!IMPORTANT]
> Las fuentes leídas dan una sola medida de cuánto se aleja lo que la gente dice de lo que hace.
> Nielsen (2001) sostiene que "self-reported data is typically 3 steps removed from the truth" y cita correlaciones de 0,44 entre desempeño medido y preferencia declarada en aplicaciones de PC, y de 0,53 en sitios web. Según esa lectura, gustar predice cerca de un cuarto de lo bien que funciona un diseño. Es un artículo de opinión de 2001, sin tabla de método a la vista.
>
> Ninguna fuente leída compara lo declarado con lo observado en un diseño publicado, y las dos correlaciones son del propio Nielsen. El mismo artículo recomienda observar tareas reales y preguntar preferencias después del uso.

## Cómo se conduce

Según NN/g, la guía lleva pocas preguntas abiertas. Su ejemplo literal es "Walk me through a typical day for you." Conviene preguntar por eventos concretos, no por procesos generales, y sondear con frases como "Tell me more about that" o "Why is that important to you?".

Cuatro cuidados protegen la validez:

1. No hacer preguntas que inducen la respuesta.
2. No interrumpir ni apurar a la persona.
3. No cambiar los objetivos del estudio a mitad de camino.
4. Probar la guía con un piloto antes de usarla.

Quien valida una idea de producto, sin hacer investigación de UX, puede mirar The Mom Test. Según un resumen secundario, el libro da tres reglas: hablar de la vida de la otra persona y no de la idea propia, preguntar por hechos concretos del pasado y no por opiniones genéricas sobre el futuro, y hablar menos para escuchar más. Es un libro de fundadores y el propio libro no se leyó. Ver [Emprender](../../Emprender/emprender.md) para el contexto de validación.

## Cuántas entrevistas hacer

Con un grupo homogéneo y una guía semiestructurada, un estudio de saturación alcanzó la estabilidad hacia las 12 entrevistas. Guest, Bunce y Johnson (2006) entrevistaron a 60 mujeres en África sobre salud sexual y analizaron por tandas de 6. Según NN/g, de 36 códigos frecuentes, 34 aparecieron tras 6 transcripciones y 35 tras 12. Para metatemas generales alcanzaron 6. El paper original no se leyó: las cifras vienen de la lectura de NN/g.

NN/g suma otras cifras como contexto: tesis con entrevistas cualitativas, de 1 a 95 (mediana 31), recomendaciones publicadas de 5 a 50, y Griffin y Hauser (1993), según los cuales 20 a 30 entrevistas descubren entre 90 y 95% de las necesidades de clientes. La práctica sugerida es empezar con 5 o 6, analizar sobre la marcha y sumar participantes solo mientras aparezcan temas nuevos.

> [!IMPORTANT]
> La saturación en 12 está discutida. Según el buscador (sin verificar), Hennink y colaboradores sostienen que las guías de saturación son vagas y sin evidencia, y Hagaman y Wutich encontraron menos de 16 entrevistas por sitio en estudios transculturales. La cifra de Guest se midió en un grupo homogéneo.

NN/g aclara que la regla de cinco usuarios del [test de usabilidad](../Evaluacion/test-de-usabilidad.md) no se traslada a las entrevistas.

## Qué leer para aprender el oficio

Para el oficio, Steve Portigal, Interviewing Users (2.ª ed., 2023). Su primer capítulo se titula "Interviewing Addresses a Business Need". La nota no pudo confirmar el contenido capítulo por capítulo. Como resumen gratuito y citable, NN/g, [User Interviews 101](https://www.nngroup.com/articles/user-interviews/): conviene mirar las pautas de preguntas y los errores de sesgo. Para el número de participantes, [How Many Participants for a UX Interview?](https://www.nngroup.com/articles/interview-sample-size/), que reúne a Guest y sus límites.

> [!NOTE]
> Sin fuente todavía: evidencia empírica sobre el sesgo del entrevistador y sobre qué preguntas sesgan más; la fuente sobre el libro de Portigal es solo de metadatos. Las cifras y citas de NN/g salen de un resumen que una herramienta hizo de cada página: conviene cotejarlas en el original antes de entrecomillarlas.

Qué trabajo quiere resolver la persona, para armar la guía, se piensa con [jobs to be done](../../Marketing/Mercado-y-cliente/jobs-to-be-done.md).
