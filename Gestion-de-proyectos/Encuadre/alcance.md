---
resumen: >-
  El alcance es la frontera del proyecto: qué entra, qué queda afuera y qué se fija como línea base, de modo que cualquier cambio posterior se vea como cambio. Se decide junto con qué se deja variar cuando falta tiempo o plata.
estado: vigente
estabilidad: estable
fuentes:
  - "PMI, The Standard for Project Management and A Guide to the PMBOK, 8.ª ed. (2025), folleto e índice: https://www.pmi.org/-/media/pmi/documents/public/pdf/publications/pmbok-guide-eighth-edition_table-of-contents.pdf"
  - "BrainBOK, PMBOK 7th vs 8th (conteo de procesos por dominio; secundaria): https://www.brainbok.com/blog/pmp/pmbok-guide-7th-vs-8th-edition-what-has-changed"
  - "DIN/Beuth, índice de ISO 21502:2020 (solo el índice): https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:334145134/toc-3233385/download"
  - "IPMA, Individual Competence Baseline 4.0, edición alemana de GPM: https://www.gpm-ipma.de/fileadmin/user_upload/ICB4_Projektmanagement.pdf"
  - "Singer, Shape Up (Basecamp), cap. 8: https://basecamp.com/shapeup/2.2-chapter-08"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
  - "Gestion-de-proyectos/.investigacion/fundamentos.md"
aliases: [scope, alcance del proyecto, línea base de alcance, scope baseline, fuera de alcance, out of scope]
creado: 2026-11-27
revisado: 2026-11-27
---

# Alcance

El alcance es la frontera del proyecto: qué entra, qué queda afuera y qué se fija como línea base, de modo que cualquier cambio posterior se vea como cambio. Se decide junto con qué se deja variar cuando falta tiempo o plata.

Dentro del [encuadre](encuadre.md), el alcance traduce el [resultado](resultado-y-terminado.md) en trabajo concreto. De él salen la [descomposición del trabajo](../Planificacion/descomposicion-del-trabajo.md), que lo parte en piezas que se entregan y se verifican, y el [control de cambios](../Seguimiento/control-de-cambios.md), que decide qué pasa cuando alguien pide algo distinto.

## Tres listas: adentro, afuera y fijo

Un alcance útil tiene tres listas. La de lo incluido dice qué se entrega. La de lo excluido dice qué no, aunque alguien pueda suponer que sí. La de lo fijo dice qué no se toca sin una decisión de quien gobierna el proyecto.

La lista de lo excluido es la que más se omite y la que más evita discusiones. En la mudanza de una oficina, "incluye el traslado de puestos y servidores" no dice nada sobre los archivos en papel ni sobre el mobiliario viejo. Si no se escribe "no incluye digitalizar el archivo ni deshacerse de los muebles", alguien lo va a pedir a mitad de camino como si siempre hubiera estado.

La línea base es una foto del alcance aprobado en un momento. No impide cambiar: hace visible el cambio. Sin línea base, según esta base, el alcance crece de a poco y nadie puede decir cuándo empezó a crecer; no hay fuente que lo mida.

## Qué se fija y qué se deja variar

Un proyecto tiene alcance, plazo, costo y calidad, y cuando algo sale distinto no pueden quedar fijos todos. El encuadre decide de antemano cuál se mueve. Hay dos posturas:

- **Alcance fijo, plazo y costo estimados.** Se define todo lo que hay que entregar y se pronostica cuánto lleva. Es la postura del [enfoque predictivo](../Enfoque/enfoque-predictivo.md), y, según la lectura de esta base, funciona cuando el resultado y el camino se conocen bien.
- **Tiempo fijo, alcance variable.** Se fija cuánto vale el trabajo en tiempo y se recorta alcance para entrar. En Shape Up, el "appetite" es "The amount of time we want to spend on a project, as opposed to an estimate", y el alcance se ajusta a ese tiempo. Es una fuente de practicante, sin estudio que la compare. Está en [apuesta con tiempo fijo](../Enfoque/apuesta-con-tiempo-fijo.md) y, como método de producto, en [Shape Up](../../Producto/Planificacion-y-entrega/shape-up.md).

La calidad casi nunca debería ser la variable: recortarla en silencio produce un entregable que cumple el alcance en el papel y falla en el uso. Esto es una lectura de esta base, sin fuente que lo mida.

## Lo que dicen los marcos

La 8.ª edición del PMBOK mantiene el alcance como uno de sus siete dominios de desempeño; según un resumen secundario, con seis de sus 40 procesos. ISO 21502 tiene una práctica de gestión del alcance (7.4) separada del control de cambios (7.10), según su índice. El ICB4 de IPMA tiene "Scope" como una de sus competencias técnicas (Practice 3). Ninguna de estas fuentes se leyó más allá del índice o la estructura.

> [!NOTE]
> Sin fuente todavía: no se encontró una fuente que defina con método la estructura de desglose del trabajo (EDT) como línea base de alcance, ni evidencia de que definir el alcance en detalle reduzca los fracasos. Las candidatas son el dominio de alcance del PMBOK y el estándar de práctica de EDT de PMI.

Cuánto detalle conviene fijar al principio depende de cuánto se sabe del resultado. Fijar en detalle un alcance que todavía no se entiende produciría, según esta base, una línea base que se va a reescribir entera; la discusión está en [elegir un enfoque](../Enfoque/elegir-un-enfoque.md). Que el cronograma detallado de todo el proyecto pierde peso frente a un plan vivo está en [lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md).

## Qué cambia cuando ejecutan agentes

> [!NOTE]
> Sin fuente todavía: no se encontró una fuente sobre el alcance de proyectos ejecutados por agentes.

Lo que sigue es inferencia de esta base. Para un agente, el alcance tiene que estar escrito como una lista de criterios de aceptación que el agente no puede reescribir, por la misma razón que el [terminado comprobable](resultado-y-terminado.md). La lista de lo excluido pesa más que con personas: una persona pregunta antes de meterse en algo dudoso, y un agente con permisos amplios puede hacerlo y reportarlo como avance. Los límites de lo que un agente puede tocar se fijan al [delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md).

Cuando el trabajo es software para un cliente, el alcance acordado y la regla para los pedidos nuevos están en [alcance y aceptación](../../Desarrollo/Encargo/alcance-y-aceptacion.md) y [cambios de alcance](../../Desarrollo/Encargo/cambios-de-alcance.md).
