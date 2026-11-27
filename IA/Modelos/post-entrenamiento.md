---
resumen: >-
  El post-entrenamiento es la etapa que convierte un modelo preentrenado, que solo continúa texto,
  en uno que sigue instrucciones y conversa: primero con ajuste supervisado sobre ejemplos y después
  con ajuste por preferencias (RLHF, DPO o IA constitucional).
estado: borrador
estabilidad: estable
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://arxiv.org/abs/2203.02155
  - https://openai.com/index/chatgpt/
  - https://arxiv.org/abs/2305.18290
  - https://arxiv.org/abs/2212.08073
  - https://arxiv.org/abs/2411.15124
  - https://lilianweng.github.io/posts/2024-07-07-hallucination/
  - https://arxiv.org/abs/2207.05221
  - https://arxiv.org/abs/2501.12948
  - https://web.stanford.edu/~jurafsky/slp3/
aliases: [post-training, posentrenamiento, alineación, alignment, SFT, supervised finetuning, ajuste supervisado, ajuste por preferencias, preference finetuning, RLHF, DPO, RLAIF, constitutional AI, IA constitucional, modelo de recompensa, reward model]
creado: 2026-11-27
revisado:
---

# Post-entrenamiento

El post-entrenamiento es la etapa que convierte un modelo preentrenado, que solo continúa texto,
en uno que sigue instrucciones y conversa: primero con ajuste supervisado sobre ejemplos y después
con ajuste por preferencias (RLHF, DPO o IA constitucional).

Un modelo que salió del [preentrenamiento](preentrenamiento.md) sabe mucho, pero ante una pregunta
puede seguir con otra pregunta o con un texto cualquiera que se parezca al corpus. Según el resumen
del capítulo 2 de Huyen, el preentrenamiento sobre datos imperfectos da salidas que no coinciden con
lo que espera el usuario, y el post-entrenamiento lo corrige en dos pasos: ajuste supervisado y ajuste
por preferencias. Agrega que, como las preferencias humanas son diversas, los métodos actuales son
imperfectos.

Lo hace quien construye el modelo, a gran escala, antes de publicarlo. El ajuste que hace quien
construye una aplicación sobre un modelo ya publicado, para su tarea, es
[finetuning](../Ajuste/finetuning.md) y vive en [Ajuste](../Ajuste/ajuste.md): usa técnicas de la
misma familia, pero con otro objetivo, otros datos y otro costo.

## Ajuste supervisado: aprender de demostraciones

En el ajuste supervisado (SFT, *supervised finetuning*) el modelo se ajusta con aprendizaje supervisado
sobre ejemplos de la conducta buscada. En InstructGPT (Ouyang et al., 2022), según su abstract,
etiquetadores escribieron demostraciones de cómo responder a los prompts y GPT-3 se ajustó con ellas.
Lectura de esta base: el modelo aprende el formato de una respuesta útil, contestar lo que se pregunta
en el registro de un asistente.

## Ajuste por preferencias: aprender de comparaciones

El ajuste por preferencias usa comparaciones entre respuestas en vez de respuestas escritas, y hay tres formas principales de hacerlo:

| Método | De dónde sale la señal | Cómo se usa |
|---|---|---|
| RLHF (InstructGPT, 2022) | Personas que ordenan varias respuestas de la mejor a la peor | Se entrena un modelo de recompensa que imita esos órdenes y después se optimiza el modelo con aprendizaje por refuerzo (PPO) para que saque buen puntaje |
| DPO (Rafailov et al., 2023) | Los mismos pares de preferencias | Se ajusta el modelo directamente con una pérdida de clasificación, sin modelo de recompensa aparte ni aprendizaje por refuerzo |
| IA constitucional o RLAIF (Bai et al., 2022) | Un modelo que juzga con una lista corta de principios escritos por personas | El modelo critica y revisa sus propias respuestas según esos principios, y un modelo juez elige entre pares para entrenar la recompensa |

**RLHF.** El abstract de InstructGPT trae el resultado que lo hizo famoso: "outputs from the 1.3B
parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer
parameters". Es preferencia humana sobre los prompts de los autores, no superioridad en todo, y el
mismo abstract admite que "still makes simple mistakes". ChatGPT (noviembre de 2022) se ajustó desde
un modelo de la serie GPT-3.5 con "the same methods as InstructGPT": entrenadores humanos escribieron
conversaciones y ordenaron respuestas para entrenar el modelo de recompensa, y después se aplicó PPO.
Cómo se pasó de ahí a un producto está en [Historia de la IA generativa](../Fundamentos/historia-de-la-ia-generativa.md).

**DPO.** Rafailov et al. mostraron que el objetivo de RLHF se puede reescribir para que la política
óptima salga en forma cerrada, y el problema queda como una clasificación "with no sampling from the
language model during fine-tuning". Según su abstract, iguala o mejora a los métodos anteriores y es
más simple de ajustar. Lectura de esta base: muestra que aprender de preferencias no exige
aprendizaje por refuerzo.

**IA constitucional (Constitutional AI).** Bai et al. (Anthropic) reemplazan buena parte del juicio humano por el de un
modelo guiado por principios (la "constitución"). En la fase supervisada, el modelo revisa sus
respuestas con esos principios y se ajusta con las revisiones; en la fase de refuerzo, un modelo
juzga cuál de dos respuestas es mejor (RLAIF, *RL from AI feedback*). El resultado que reportan es un
asistente "harmless but non-evasive". Lectura de esta base: es la idea de
[IA como juez](../Evaluacion/ia-como-juez.md), usada para entrenar en vez de para medir.

## Recompensas verificables y recetas abiertas

Tulu 3 (Lambert et al., 2024) publicó una receta completa, con datos y código, que encadena SFT, DPO
y un método que llaman "Reinforcement Learning with Verifiable Rewards" (RLVR); su abstract no explica
el mecanismo. Lectura de esta base, a partir de DeepSeek-R1, que reporta su rendimiento en
"verifiable tasks": la recompensa no sale de una preferencia sino de comprobar la respuesta, como el
resultado de un problema de matemática o un código que pasa las pruebas. Los autores reportan superar
a modelos abiertos y cerrados de tamaño comparable de fines de 2024; es un preprint. DeepSeek-R1 entrenó
su razonamiento con ese tipo de recompensa ([Razonamiento](razonamiento.md)).

## El modelo de recompensa no es la verdad

Lectura de esta base: el modelo de recompensa aprendió qué respuestas prefieren los etiquetadores, no
cuáles son correctas, y el modelo que se optimiza contra él puede aprender a agradar: sonar seguro,
extenderse, darle la razón a quien pregunta.

Sobre la calibración (que la seguridad con que responde se corresponda con la probabilidad de
acertar), las fuentes leídas no coinciden. Lilian Weng, en un resumen secundario que atribuye el dato
a Kadavath et al., escribe que "RLHF fine-tuning makes the model poorly calibrated". El abstract de
Kadavath et al., leído aparte, destaca lo contrario: modelos grandes bien calibrados en preguntas de
opción múltiple con buen formato. Puede que hablen de modelos distintos (antes y después del ajuste),
pero eso no se verificó. Es uno de los caminos posibles hacia la [alucinación](alucinacion.md).

> [!NOTE]
> Sin fuente todavía: los trabajos originales de RLHF (Christiano et al., 2017; Stiennon et al.,
> 2020), que no se leyeron.

## Qué leer sobre post-entrenamiento

[InstructGPT](https://arxiv.org/abs/2203.02155), las secciones de método (SFT, modelo de recompensa,
PPO) y los resultados de preferencia: es el puente directo a ChatGPT. Para el estado actual,
[Tulu 3](https://arxiv.org/abs/2411.15124), una receta abierta de punta a punta. El abstract de
[DPO](https://arxiv.org/abs/2305.18290), para ver por qué se puede prescindir del aprendizaje por
refuerzo. Jurafsky y Martin dedican el capítulo 8 de
[*Speech and Language Processing*](https://web.stanford.edu/~jurafsky/slp3/) al post-entrenamiento
(se leyó solo el índice).
