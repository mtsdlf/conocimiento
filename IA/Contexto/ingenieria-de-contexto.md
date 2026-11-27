---
resumen: >-
  La ingeniería de contexto es decidir, en cada paso de una tarea, qué entra en la ventana del modelo
  y qué queda afuera, porque la ventana es finita y el modelo rinde peor a medida que se llena.
  Abarca el prompt, la recuperación, la memoria, la compactación y el reparto entre agentes.
estado: borrador
estabilidad: semi
fuentes:
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://www.langchain.com/blog/context-engineering-for-agents
  - https://simonwillison.net/2025/Jun/27/context-engineering/
  - https://x.com/karpathy/status/1937902205765607626
  - https://arxiv.org/abs/2307.03172
  - https://arxiv.org/abs/2404.06654
  - https://arxiv.org/abs/2502.05167
  - https://www.trychroma.com/research/context-rot
  - https://platform.claude.com/docs/en/build-with-claude/compaction
aliases: [context engineering, ingeniería del contexto, context rot, lost in the middle, compactación, compaction]
creado: 2026-11-27
revisado:
---

# Ingeniería de contexto

La ingeniería de contexto es decidir, en cada paso de una tarea, qué entra en la ventana del modelo
y qué queda afuera, porque la ventana es finita y el modelo rinde peor a medida que se llena.
Abarca el prompt, la recuperación, la memoria, la compactación y el reparto entre agentes.

El [prompt](prompt.md) es una pieza; la ingeniería de contexto es la vista de conjunto sobre todo lo
que comparte la [ventana de contexto](../Modelos/transformer.md). En lectura de esta base, importa
poco en una consulta suelta y mucho en un [agente](../Agentes/agente.md), que en una tarea larga junta instrucciones,
resultados de herramientas, historial y notas, y tiene que decidir qué sigue mereciendo lugar.

## De dónde sale el término

El término se impuso a mediados de 2025. Según reportes secundarios, Andrej Karpathy respondió el
25 de junio de 2025 a un post de Tobi Lütke apoyando "context engineering" frente a "prompt
engineering", y se le atribuye una definición como el arte y la ciencia de llenar la ventana con la
información justa para el paso siguiente. El post original no se pudo abrir y los reportes difieren
en la redacción, así que el texto exacto no está verificado. Simon
Willison lo defendió como "a better alternative to prompt engineering", porque el sentido que la
gente infería de *prompt engineering* era el de "typing things into a chatbot".

Anthropic lo formalizó en septiembre de 2025 como "the set of strategies for curating and
maintaining the optimal set of tokens" durante la inferencia, con un objetivo: "find the smallest
set of high-signal tokens that maximize the likelihood of your desired outcome". Cognition, citada
por LangChain, lo llama "effectively the #1 job of engineers building AI agents".

## Por qué el modelo rinde peor con la ventana llena

Anthropic habla de un "attention budget": cada token que entra compite por la atención del modelo
con los demás. Cuatro estudios lo miden desde ángulos distintos:

| Estudio | Qué midió | Qué encontró |
|---|---|---|
| Lost in the Middle (Liu et al., 2023, TACL) | preguntas sobre varios documentos y recuperación de pares clave-valor | el rendimiento "is often highest when relevant information occurs at the beginning or end" y cae cuando está en el medio, "even for explicitly long-context models" |
| RULER (Hsieh et al., 2024) | 17 modelos, 13 tareas | casi todos resuelven la búsqueda simple de una aguja, pero se degradan al crecer el contexto; todos declaran 32.000 tokens o más y solo cerca de la mitad rinde bien a 32.000 (según su abstract) |
| NoLiMa (Modarressi et al., ICML 2025) | agujas sin coincidencia literal con la pregunta | a 32.000 tokens, 11 de 13 modelos caen por debajo de la mitad de su rendimiento con contexto corto; uno de los mejores de 2024 baja de 99,3% a 69,7% (según su abstract) |
| Context Rot (Chroma, 2025) | 18 modelos, incluidos varios de 2025 | "performance grows increasingly unreliable as input length grows"; un solo distractor ya baja el resultado; prompts enfocados de unos 300 tokens rinden mucho más que los de unos 113.000 |

Los cuatro miden tareas sintéticas de búsqueda, no trabajo real de varios pasos. Chroma cree que la
degradación real es mayor, pero no lo probó, y es una empresa que vende bases vectoriales, con
interés en que recuperar importe. El hallazgo que ellos mismos llaman "surprising" es que los textos
de relleno barajados al azar rinden mejor que los coherentes, en los 18 modelos, y no explican por
qué.

> [!NOTE]
> Sin fuente todavía: si la degradación persiste en los modelos de contexto largo de 2026. Todo lo
> leído llega hasta mediados de 2025.

La consecuencia práctica, en lectura de esta base: que la base de conocimiento quepa en la ventana
no es razón suficiente para mandarla entera. La discusión entre contexto largo y recuperación sigue
en [Contexto y RAG](contexto-y-rag.md).

## Las cuatro estrategias: escribir, seleccionar, comprimir, aislar

LangChain ordena el trabajo en cuatro estrategias. Cada una tiene su nota en el tema:

| Estrategia | Qué hace | Dónde se explica |
|---|---|---|
| Escribir (*write*) | guarda información fuera de la ventana para traerla después | [Memoria](memoria.md) |
| Seleccionar (*select*) | trae a la ventana solo lo relevante para este paso | [Contexto y RAG](contexto-y-rag.md), [Recuperación](recuperacion.md) |
| Comprimir (*compress*) | resume o recorta lo que ya está en la ventana | abajo, en compactación |
| Aislar (*isolate*) | reparte la tarea entre subagentes, cada uno con su propia ventana | [Patrones de flujo](../Agentes/patrones-de-flujo.md) |

Anthropic nombra las mismas técnicas con otras palabras: recuperación *just-in-time*, compactación,
notas fuera de la ventana y subagentes. Su consejo final es "do the simplest thing that works".

## Compactar la conversación

Compactar es reemplazar los turnos viejos por un resumen. Un proveedor ya lo ofrece como función de
la API, "because response quality degrades as a conversation grows": el resumen se escribe del lado
del servidor, a pedido o cuando se pasa un umbral de tokens. Hay una
variante más simple, editar el contexto por regla, que borra resultados de herramientas viejos o
bloques de pensamiento.

Anthropic llama a borrar resultados de herramientas "One of the safest lightest touch forms of
compaction": lo que una herramienta devolvió hace veinte pasos rara vez se necesita entero. En su
agente de código, el resumen conserva "architectural decisions, unresolved bugs, and implementation
details". Lo que no puede perderse al resumir no se confía al resumen: se escribe en la
[memoria](memoria.md).

## El prompt de sistema a la altura justa

Anthropic pide escribir el prompt de sistema a "the right altitude": entre la lógica rígida, que se
rompe con cada caso no previsto, y la guía vaga, que no le dice nada concreto al modelo. Para el
resto propone un modelo híbrido: una parte se carga de entrada (en su agente de código, un archivo de
instrucciones del proyecto) y otra se busca en el momento con herramientas, como `glob` y `grep`.
Ese segundo camino, la búsqueda agentiva, se compara con un índice en [Recuperación](recuperacion.md).

Dónde va cada cosa dentro del prompt también cuenta: los documentos largos arriba y la consulta al
final, como se dice en [Prompt](prompt.md).

## Qué leer sobre ingeniería de contexto

Anthropic, ["Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents),
completo: fijarse en compactación, notas fuera de la ventana y subagentes, y en el consejo de
simplicidad. Para la evidencia, el abstract de [Lost in the Middle](https://arxiv.org/abs/2307.03172)
y el informe [Context Rot](https://www.trychroma.com/research/context-rot), el más legible y con
modelos recientes. Para la taxonomía, el post de
[LangChain](https://www.langchain.com/blog/context-engineering-for-agents).
