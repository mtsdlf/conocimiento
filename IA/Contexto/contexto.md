---
resumen: >-
  El contexto es todo lo que entra en la ventana del modelo en una llamada: las instrucciones, los
  ejemplos, el historial, la información recuperada, los resultados de herramientas y la memoria. Es
  la forma de adaptar un modelo sin cambiar sus pesos, y la primera que se prueba.
estado: borrador
estabilidad: estable
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://www.langchain.com/blog/context-engineering-for-agents
  - https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
  - https://www.trychroma.com/research/context-rot
creado: 2026-11-27
revisado:
---

# Contexto

El contexto es todo lo que entra en la ventana del modelo en una llamada: las instrucciones, los
ejemplos, el historial, la información recuperada, los resultados de herramientas y la memoria. Es
la forma de adaptar un modelo sin cambiar sus pesos, y la primera que se prueba.

Un modelo sabe lo que vio al entrenarse y nada más. Lo que necesita para una tarea concreta (qué
se le pide, los documentos de una empresa, lo que dijo el usuario hace tres turnos) tiene que
llegarle como texto dentro de su [ventana de contexto](../Modelos/transformer.md), que es una
propiedad del modelo y tiene un tamaño fijo. Esta vertical trata lo que se pone en esa ventana; los
límites de la ventana misma se explican en [Modelos](../Modelos/modelos.md).

Dentro del tema, Contexto es la vía más barata de las tres formas de adaptar un modelo. Las
[herramientas de un agente](../Agentes/agentes.md) le traen información nueva a mitad de la tarea,
y lo que devuelven también entra como contexto. El [ajuste](../Ajuste/ajuste.md) cambia los pesos y
se reserva para cuando el contexto no alcanza: la decisión está en
[Prompt, RAG o finetuning](../prompt-rag-o-finetuning.md). La
[evaluación](../Evaluacion/evaluacion.md) dice si un cambio de contexto mejoró algo, y en
producción el [prompt cache](../Produccion/cache-de-modelos.md) abarata mandar el mismo contexto
muchas veces.

## Qué entra en la ventana y de dónde sale

Cada pieza del contexto tiene un origen distinto y se decide en un lugar distinto:

| Pieza | Quién la escribe | Nota |
|---|---|---|
| Instrucciones de sistema, ejemplos y la consulta | quien construye el producto y el usuario | [Prompt](prompt.md) |
| Fragmentos de documentos | un recuperador, en cada consulta | [Contexto y RAG](contexto-y-rag.md), [Recuperación](recuperacion.md) |
| Historial y notas que sobreviven entre pasos y sesiones | la aplicación, a veces el propio modelo | [Memoria](memoria.md) |
| Resultados de herramientas | el mundo exterior: una API, una web, un archivo | [Uso de herramientas](../Agentes/uso-de-herramientas.md) |

Las dos últimas filas traen texto que nadie del equipo escribió. Ahí está el riesgo de la vertical:
el modelo no distingue entre instrucciones y datos dentro de su ventana, así que un documento o una
página pueden darle órdenes. Eso es la [inyección de prompt](inyeccion-de-prompt.md).

## Por qué más contexto no es mejor contexto

Que la ventana sea grande no quiere decir que conviene llenarla. Los estudios de "lost in the
middle", RULER, NoLiMa y context rot miden lo mismo con métodos distintos: el modelo rinde peor
cuando la información relevante está rodeada de mucho texto. Anthropic lo resume así: el contexto
"must be treated as a finite resource with diminishing marginal returns". Por eso el trabajo de esta
vertical es elegir: poner poco y bueno, no todo lo que cabe. La evidencia y sus límites están en
[Ingeniería de contexto](ingenieria-de-contexto.md).

Si conviene recuperar fragmentos o mandar la base entera cuando cabe en la ventana es una pregunta
abierta, con estudios que dan respuestas distintas según el modelo y la fecha. Se desarrolla en
[Contexto y RAG](contexto-y-rag.md).

## Del prompt a la ingeniería de contexto

Hasta 2024 se hablaba de *prompt engineering*: escribir bien la consulta. Con los agentes, que
encadenan decenas de llamadas, el problema pasó a ser administrar la ventana durante toda la tarea:
qué se guarda afuera, qué se trae, qué se resume y qué se deja a otro agente. LangChain parte ese
trabajo en cuatro estrategias (escribir, seleccionar, comprimir y aislar) y cada una cae en una nota
de esta vertical. Que "ingeniería de contexto" sea el paraguas de toda la vertical, y no una pieza
más al lado del prompt, es lectura de esta base a partir de esas fuentes.

Huyen no agrupa así: según el índice de *AI Engineering*, el prompt y su defensa están en el cap. 5,
el RAG en el cap. 6, y la memoria, dentro de la sección de agentes del cap. 6 (p. 300). Esta base
junta todo lo que entra en la ventana en una vertical y enlaza la memoria con
[Agente](../Agentes/agente.md), que es donde más se usa.

## El contexto como superficie de ataque

Todo texto que entra en la ventana puede cambiar lo que hace el modelo, y ninguna técnica conocida
lo impide del todo. El NCSC del Reino Unido lo dice sin rodeos: los modelos actuales "simply do not
enforce a security boundary between instructions and data inside a prompt". La defensa que funciona
es de diseño: limitar lo que el sistema puede hacer después de leer algo no confiable. Eso está en
[Inyección de prompt](inyeccion-de-prompt.md); los filtros que corren sobre la entrada y la salida
en producción, en [Guardrails](../Produccion/guardrails.md).

## Lo que hay adentro de Contexto

Leé en este orden: el prompt primero, porque todo lo demás se suma a él.

- [Prompt](prompt.md) — instrucciones, roles, ejemplos y cómo se versionan; qué perdió peso con los
  modelos más capaces.
- [Ingeniería de contexto](ingenieria-de-contexto.md) — por qué el rendimiento cae cuando la ventana
  se llena, y las estrategias para elegir qué entra en cada paso.
- [Contexto y RAG](contexto-y-rag.md) — traer información externa al prompt buscando fragmentos;
  contexto largo o RAG.
- [Recuperación](recuperacion.md) — búsqueda léxica, por embeddings e híbrida, reranking, partición en
  fragmentos, métricas y búsqueda agentiva.
- [Memoria](memoria.md) — lo que persiste entre pasos, turnos y sesiones, y cómo vuelve a la ventana.
- [Inyección de prompt](inyeccion-de-prompt.md) — el contexto como superficie de ataque y las defensas
  de diseño.
