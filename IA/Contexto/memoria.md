---
resumen: >-
  La memoria de un sistema con modelos es lo que se guarda fuera de la ventana de contexto y vuelve a
  entrar cuando hace falta: entre los pasos de un agente, entre turnos y entre sesiones. El modelo no
  recuerda nada entre llamadas; la memoria es un archivo o una base que controla la aplicación.
estado: borrador
estabilidad: semi
fuentes:
  - https://arxiv.org/abs/2005.11401
  - https://arxiv.org/abs/2310.08560
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
  - https://platform.claude.com/docs/en/build-with-claude/compaction
  - https://www.langchain.com/blog/context-engineering-for-agents
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 6, «Agents», sección «Memory», p. 300 (solo índice)"
aliases: [memory, memoria de agentes, agent memory, memoria a largo plazo, long-term memory, memoria persistente]
creado: 2026-11-27
revisado:
---

# Memoria

La memoria de un sistema con modelos es lo que se guarda fuera de la ventana de contexto y vuelve a
entrar cuando hace falta: entre los pasos de un agente, entre turnos y entre sesiones. El modelo no
recuerda nada entre llamadas; la memoria es un archivo o una base que controla la aplicación.

Lewis et al. (2020), al proponer el RAG, distinguieron dos memorias; en su abstract, "the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of
Wikipedia". La memoria de esta nota es de la
segunda clase, pero escrita durante el uso: no son documentos que alguien cargó, sino lo que el
sistema fue aprendiendo de la tarea o del usuario. En la taxonomía de LangChain es la estrategia de
"escribir" de la [ingeniería de contexto](ingenieria-de-contexto.md); traerla de vuelta es
"seleccionar", con las mismas técnicas de la [recuperación](recuperacion.md).

Huyen la trata dentro de la sección de agentes (cap. 6, "Memory", p. 300, según el índice; el texto
no se leyó), y la documentación de Anthropic también la presenta como una herramienta de agente.
Vive en Contexto porque lo que hace es decidir qué vuelve a la ventana; se usa sobre todo en un
[agente](../Agentes/agente.md).

## Tres horizontes: el paso, la conversación y la sesión

Lo que hay que recordar depende de cuánto dura lo que se recuerda. Esta división en tres horizontes
es de esta base, armada con los mecanismos que describen las fuentes; la literatura de agentes habla
de memoria de corto y de largo plazo, términos que las páginas de producto no usan.

| Horizonte | Qué se guarda | Mecanismo |
|---|---|---|
| Entre pasos de una tarea | resultados intermedios, el plan, lo que ya se probó | notas del agente fuera de la ventana; el historial de la propia tarea |
| Entre turnos de una conversación | lo que se dijo antes | el historial, que se reenvía en cada llamada y se compacta cuando crece |
| Entre sesiones | preferencias del usuario, decisiones, el progreso de un trabajo largo | archivos o una base que la aplicación guarda y el modelo lee al empezar |

La [compactación](ingenieria-de-contexto.md) y la memoria son piezas distintas. Según Anthropic, la
compactación resume el historial, y la memoria "preserves the information that must survive
summarization". Recomienda usar las dos en agentes que trabajan mucho tiempo.

## La idea de MemGPT: memoria como en un sistema operativo

MemGPT (Packer et al., 2023) tomó la idea de la memoria jerárquica de los sistemas operativos: según
su abstract, el sistema mueve datos entre una memoria rápida y chica (la ventana) y una lenta y
grande (afuera), y lo llama "virtual context management". Lo evaluaron en análisis de documentos que
no caben en la ventana y en chat de varias sesiones.

## La memoria como archivos que el agente lee y escribe

La forma más concreta que se encontró es dar la memoria como una herramienta: el modelo pide leer y
escribir archivos en un directorio de memorias, y la aplicación ejecuta esas operaciones con su
propio almacenamiento. La documentación de Anthropic lo explica así: "Rather than loading all
relevant information up front, an agent records what it learns in memory files and reads them back
on demand". Las operaciones concretas y cómo se configura están en la ficha
[Herramientas de memoria](herramientas-de-memoria.md).

Para trabajos que cruzan varias sesiones, la misma documentación propone un patrón:

1. La primera sesión arma un registro de progreso y la lista de lo que hay que construir.
2. Cada sesión siguiente lee esos archivos al arrancar.
3. Al cerrar, los actualiza, y marca algo como terminado solo después de verificarlo: "Mark a feature
   complete only after end-to-end verification".

Es el mismo patrón que [Agente](../Agentes/agente.md) describe dentro del harness, con un archivo
de progreso que sostiene el trabajo entre sesiones.

## Resumir y recuperar en lugar de mandar todo

Otra familia de sistemas extrae hechos de la conversación, los resume y los recupera por similitud.
Los únicos números encontrados son de los autores de un producto, en un preprint sin revisión por
pares y medidos con un [juez](../Evaluacion/ia-como-juez.md): sirven como señal de que resumir puede
rendir, no como comparación neutral. Las cifras están en la ficha
[Herramientas de memoria](herramientas-de-memoria.md).

Los asistentes de chat comerciales ya tienen memoria entre sesiones, con diseños distintos y sin una
taxonomía común ni un estudio que los compare; cómo funciona cada uno, también en la ficha.

## Qué decidir: qué se escribe, quién lo borra, cuándo vence

La memoria es estado que el sistema escribe solo, y eso trae decisiones que no tiene un prompt. La
documentación de la herramienta de memoria de Anthropic nombra cuatro riesgos:

- **Rutas**: validar que el modelo no salga del directorio de memorias, por ejemplo con
  `/memories/../../secrets.env`.
- **Tamaño**: limitar cuánto puede crecer cada archivo.
- **Vencimiento**: borrar memorias viejas que ya no valen.
- **Datos sensibles**: el modelo "usually refuses" a guardarlos, pero si hace falta una garantía,
  la validación va en el código.

Hay un quinto, en lectura de esta base: lo que se guarda en memoria lo escribió el modelo a partir de
entradas que pueden venir de un atacante. Una instrucción plantada en un documento puede terminar en
la memoria y volver en cada sesión. Lo que se lee de la memoria se trata como contenido no confiable,
igual que en [Inyección de prompt](inyeccion-de-prompt.md).

> [!NOTE]
> Sin fuente todavía: un estudio que compare estrategias de memoria (ventana deslizante, resumen,
> recuperación) en una misma aplicación, y uno sobre envenenamiento de memorias.

## Qué leer sobre memoria

Para la idea, el abstract de [MemGPT](https://arxiv.org/abs/2310.08560). Para hacerlo, la
[documentación de la herramienta de memoria](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
de Anthropic, la única fuente leída con API, errores y seguridad: fijarse en el patrón de varias
sesiones y en la lista de riesgos. Huyen, cap. 6, "Memory" (p. 300), por el marco dentro de agentes
(leído solo por su título en el índice).
