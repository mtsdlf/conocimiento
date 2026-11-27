---
resumen: >-
  La escritura técnica es el conjunto de textos con forma fija que produce un equipo de software
  (commit messages, descripciones de pull request, bug reports, design docs y RFC, documentación).
  Cada uno tiene convenciones publicadas, y todos se escriben para un lector global que muchas veces
  tampoco es nativo.
estado: borrador
estabilidad: estable
fuentes:
  - "Google developer documentation style guide, Write for a global audience: https://developers.google.com/style/translation"
  - "Microsoft Writing Style Guide, Global communications: https://learn.microsoft.com/en-us/style-guide/global-communications/"
  - "Google Engineering Practices, Writing good CL descriptions: https://google.github.io/eng-practices/review/developer/cl-descriptions.html"
  - "Chris Beams, How to write a Git commit message: https://cbea.ms/git-commit/"
  - "Conventional Commits 1.0.0: https://www.conventionalcommits.org/en/v1.0.0/"
  - "Mozilla, Bug writing guidelines: https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html"
  - "Chromium, Bug reporting guidelines: https://www.chromium.org/for-testers/bug-reporting-guidelines/"
  - "Malte Ubl, Design docs at Google: https://www.industrialempathy.com/posts/design-docs-at-google/"
  - "Rust RFC template: https://github.com/rust-lang/rfcs/blob/master/0000-template.md"
  - "Oxide, RFD 1 Requests for Discussion: https://rfd.shared.oxide.computer/rfd/0001"
  - "Digital.gov, Plain language guide: https://digital.gov/guides/plain-language"
aliases:
  - Technical writing
  - Commit message
  - Pull request description
  - PR description
  - Bug report
  - Design doc
  - RFC
creado: 2026-11-27
revisado:
---

# Escritura técnica

La escritura técnica es el conjunto de textos con forma fija que produce un equipo de software (commit messages, descripciones de pull request, bug reports, design docs y RFC, documentación). Cada uno tiene convenciones publicadas, y todos se escriben para un lector global que muchas veces tampoco es nativo.

Se apoya en [Escritura](../Discurso/escritura.md), que trata la oración corta, el mail de trabajo y cómo revisar un texto, y en [Conectores y cohesión](../Discurso/conectores-y-cohesion.md). Los comentarios que se dejan sobre el código de otros son un género aparte: [Code review](code-review.md). El postmortem, que también es escritura técnica, está en [Incidentes](incidentes.md).

## Escribir para un público global

Microsoft parte de un supuesto: "It's usually safe to assume your content will be read in many countries and by readers whose primary language isn't English." La guía de Google para documentación técnica tiene una página entera sobre eso, y sus reglas valen para cualquier texto de un equipo internacional:

- Oraciones cortas, voz activa y dirigidas a *you*.
- Sin modismos, jerga ni humor: sus ejemplos son *ballpark figure*, *back burner* y *hang in there*.
- Sin referencias de estación: "August isn't summer in the southern hemisphere", un ejemplo que en Argentina se entiende solo.
- Un verbo simple en lugar de un phrasal verb, salvo los fijados como *set up*, *log in* o *sign in* (ver [Phrasal verbs](../Lexico/phrasal-verbs.md)).
- *Start* o *begin* en lugar de *commence*, *use* en lugar de *utilize* o *leverage*, *so* en lugar de *consequently*.
- No omitir el *that* relativo: *the rules that you previously defined* mejor que *the rules you previously defined*.
- Un solo término por concepto y la condición antes de la instrucción.

Como inferencia propia, para un hispanohablante esto tiene una ventaja: el criterio es la claridad, no la elegancia nativa. Lo que se le pide a un B2 que escribe para un equipo global es lo que ya sabe hacer bien si no traduce del castellano. La palabra latina larga (*utilize*, *commence*) es justo lo que el castellano empuja y lo que la guía saca ([Cognados y falsos amigos](../Lexico/cognados-y-falsos-amigos.md)).

## El commit message

Chris Beams, en un texto muy difundido entre desarrolladores, da siete reglas: separar el asunto del cuerpo con una línea en blanco, asunto de 50 caracteres como máximo, mayúscula inicial, sin punto final, modo imperativo, cuerpo cortado a 72 caracteres, y que el cuerpo explique "what and why vs. how". Su prueba del imperativo es la más útil: el asunto tiene que completar la frase *If applied, this commit will…*. Por eso es *Fix race condition in cache refresh* y no *Fixed…* ni *Fixes…*.

El imperativo inglés es la forma base del verbo, sin sujeto. Un error típico de quien piensa en castellano, como inferencia propia, es usar el pasado (*Added validation*) o un sustantivo (*Validation fix*), porque en castellano se describe lo que se hizo.

**Conventional Commits** es una especificación que agrega un tipo al principio: `feat(lang): add Polish language`, `docs: correct spelling of CHANGELOG`, `feat!: drop support for Node 6`. `fix` corrige un bug, `feat` agrega una función y el `!` o un pie `BREAKING CHANGE:` marca un cambio incompatible. Choca con Beams en un detalle: Conventional Commits usa minúscula después del tipo y Beams pide mayúscula. Son convenciones distintas, y manda la del repositorio.

## La descripción de un pull request

Google llama "CL description" a la descripción de un cambio y pide que la primera línea sea "a short summary of what the CL does", en imperativo y como oración completa: *Delete the FizzBuzz RPC and replace it with the new system.* Malos ejemplos de su guía: *Fix bug*, *Fix build*, *Add patch*, *Phase 1*. El cuerpo explica el porqué: el problema, por qué este enfoque, las limitaciones conocidas y el contexto que no se ve en el código. Pide poner ese contexto en el texto, porque los enlaces externos se rompen.

Una descripción de pull request de un equipo suele decir qué cambia, por qué, cómo se probó y qué tiene que mirar quien revisa (un ejemplo propio: *Reviewers: the interesting part is the retry logic in `client.py`; the rest is renaming*).

## El bug report

Mozilla dice que los pasos para reproducir son "the most important part of any bug report", y pide separar el resultado real del esperado y no mezclar hechos con especulación. El título "should explain the problem, not your suggested solution": mal, *Software crashes*; bien, *Cancelling a File Copy dialog crashes File Manager*. Un bug por reporte. Su ejemplo de resultado real: "**Actual results**: My inbox displays the message 'Your browser does not support cookies (error -91)'." Chromium suma verificar con la última versión y adjuntar un caso de prueba reducido.

Por eso un bug report en inglés suele tener secciones de pasos para reproducir, resultado esperado y resultado real, con los pasos numerados y en imperativo; la forma exacta de los títulos cambia según el proyecto (inferencia propia a partir de Mozilla y Chromium).

## Design docs y RFC

Un design doc o un RFC (*request for comments*) es el texto que propone un cambio grande para que otros lo discutan antes de construirlo. En Google, según Malte Ubl, tiene contexto y alcance, objetivos y no objetivos (*goals* y *non-goals*), el diseño, las alternativas consideradas (que el autor cuenta entre las secciones más importantes) y las preocupaciones transversales. Mide de 10 a 20 páginas en proyectos grandes y de 1 a 3 en un "mini design doc".

La plantilla de RFC de Rust ordena las secciones así: *Summary, Motivation, Guide-level explanation, Reference-level explanation, Drawbacks, Rationale and alternatives, Prior art, Unresolved questions, Future possibilities*. Trae preguntas que obligan a argumentar: "Why should we _not_ do this?" y "Why is this design the best in the space of possible designs?". En Oxide, un RFD pasa por estados (*prediscussion, ideation, discussion, published, committed, abandoned*), y como guía "3-5 business days to comment on your RFD before merging seems reasonable".

Un design doc es un argumento, así que le sirve todo lo de [Estructura del argumento](../Discurso/estructura-del-argumento.md): la recomendación arriba y las alternativas con por qué se descartan. Cómo se especifica un sistema en general, más allá del idioma, está en [Especificación](../../Desarrollo/Definicion/especificacion.md).

## Documentación

Para documentación, las guías de estilo de Google y de Microsoft son las que usa esta vertical; de ellas se leyeron la página sobre público global y la presentación de la voz de Microsoft. La administración de EE.UU. tiene además una guía de *plain language* que nace de una ley de 2010 que exige textos públicos claros. Cuáles son y qué leer de cada una está en [Recursos de inglés técnico](recursos-de-ingles-tecnico.md).

> [!NOTE]
> Sin fuente todavía: las secciones de la guía de Google sobre procedimientos y documentación de referencia, y los módulos del curso *Technical Writing One* (solo se leyó la introducción).
