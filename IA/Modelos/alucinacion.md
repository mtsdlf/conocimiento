---
resumen: >-
  Una alucinación es una afirmación falsa que el modelo emite con la forma y la seguridad de una
  verdadera; viene de que el modelo optimiza texto probable y no texto verdadero, y la alimentan los
  datos, el post-entrenamiento, la generación token a token y la manera en que se lo evalúa.
estado: borrador
estabilidad: estable
fuentes:
  - https://arxiv.org/abs/2509.04664
  - https://arxiv.org/abs/2305.13534
  - https://arxiv.org/abs/2405.05904
  - https://arxiv.org/abs/2207.05221
  - https://lilianweng.github.io/posts/2024-07-07-hallucination/
  - https://openai.com/index/chatgpt/
  - https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
aliases: [hallucination, alucinaciones, confabulación, confabulation, calibración, calibration]
creado: 2026-11-27
revisado:
---

# Alucinación

Una alucinación es una afirmación falsa que el modelo emite con la forma y la seguridad de una
verdadera; viene de que el modelo optimiza texto probable y no texto verdadero, y la alimentan los
datos, el post-entrenamiento, la generación token a token y la manera en que se lo evalúa.

No es un error raro que se corrige en la próxima versión. El anuncio de ChatGPT (noviembre de 2022)
ya lo declaraba como limitación: "sometimes writes plausible-sounding but incorrect or nonsensical
answers". Kalai y otros (OpenAI, 2025) la definen igual: afirmaciones plausibles pero falsas,
emitidas con seguridad. Lo que hizo falta desde entonces fue entender de dónde sale, porque cada causa
tiene un remedio en otra parte del sistema.

## De dónde sale, etapa por etapa

Cada etapa de la vertical agrega su parte:

| Etapa | Qué aporta a la alucinación | Evidencia |
|---|---|---|
| [Preentrenamiento](preentrenamiento.md) | El corpus trae datos desactualizados, faltantes o incorrectos, y el modelo los memoriza | Weng (2024) |
| [Finetuning](../Ajuste/finetuning.md) con hechos nuevos | El modelo aprende "much more slowly" los hechos que no vio antes y, una vez aprendidos, tiende más a alucinar | Gekhman y otros (EMNLP 2024) |
| [Post-entrenamiento](post-entrenamiento.md) | El ajuste por preferencias empeora la calibración: la seguridad deja de corresponderse con la probabilidad de acertar | Weng, citando a Kadavath y otros |
| Evaluación del modelo | Los benchmarks premian adivinar antes que admitir que no sabe | Kalai y otros (2025) |
| Generación token a token ([muestreo](muestreo.md)) | Un primer error compromete lo que sigue, y el modelo lo sostiene | Zhang y otros (2023) |

**Los incentivos de la evaluación.** Kalai y otros sostienen, según su abstract, que los modelos
alucinan porque el entrenamiento y la evaluación premian adivinar en lugar de reconocer la
incertidumbre (lectura de esta base: en un examen que da puntos por acertar y ninguno por decir "no
sé", conviene adivinar siempre). Las alucinaciones surgirían como errores de clasificación cuando una afirmación falsa es
difícil de distinguir de un hecho. Proponen un arreglo sociotécnico: cambiar cómo puntúan las
respuestas inciertas los benchmarks que ya existen, en lugar de sumar pruebas de alucinación. Es un
preprint.

**La bola de nieve.** Zhang y otros (2023) mostraron que un modelo que se compromete con un error al
principio después genera afirmaciones falsas que él mismo reconocería como erróneas: ChatGPT y GPT-4
identificaron como erróneas el 67 % y el 87 % de sus propias afirmaciones falsas. No todo es falta de
conocimiento; parte es que cada token condiciona al siguiente.

## Si el modelo sabe lo que no sabe

Kadavath y otros (2022) encontraron que los modelos grandes están bien calibrados en preguntas de
opción múltiple y de verdadero o falso con buen formato: la probabilidad que asignan a una respuesta
se parece a cuántas veces aciertan. También entrenaron un predictor de "sé la respuesta" que
generaliza solo en parte a tareas nuevas. Una técnica de detección usa una idea vecina: si el modelo da
respuestas distintas a la misma pregunta en varias muestras, probablemente no sabe (SelfCheckGPT, según
Weng).

> [!IMPORTANT]
> Las explicaciones no son la misma. Weng, citando a Kadavath, dice que "RLHF fine-tuning makes the
> model poorly calibrated", un efecto medido del ajuste por preferencias. Kalai y otros lo atribuyen a
> los incentivos de cómo se evalúa. Zhang y otros, a la generación autorregresiva. Las tres apuntan a
> que la alucinación no es solo falta de datos, pero por mecanismos distintos, y no se excluyen. Ninguna
> fuente leída mide cuánto pesa cada una.

## Qué se hace contra ella en cada capa

La alucinación no se elimina; se reduce y se detecta. Cada causa tiene su remedio en otra vertical:

- **Darle los hechos en vez de pedírselos.** Según Weng, la recuperación reduce la alucinación de forma
  consistente: el modelo responde desde un documento que está en su ventana y no desde lo que memorizó
  ([Contexto y RAG](../Contexto/contexto-y-rag.md), [Recuperación](../Contexto/recuperacion.md)).
- **Permitir el "no sé" y pedir citas.** La guía "Reduce hallucinations" de Anthropic (no releída para
  esta versión) recomienda dejar que el modelo diga que no sabe y exigir citas textuales del material
  ([Prompt](../Contexto/prompt.md)). Reducen, no eliminan.
- **No enseñarle hechos con finetuning.** Por el resultado de Gekhman, agregar conocimiento por ajuste
  puede empeorar las cosas; el ajuste sirve para el comportamiento ([Prompt, RAG o finetuning](../prompt-rag-o-finetuning.md)).
- **Verificar afuera.** Weng reúne métodos de detección por recuperación (FActScore, SAFE), que
  comparan cada afirmación con fuentes, y por consistencia entre muestras. En un producto eso se monta
  como [guardrails](../Produccion/guardrails.md) sobre la salida, o como un
  [juez](../Evaluacion/ia-como-juez.md) en las [evals](../Evaluacion/evals.md).
- **Medirla en la tarea propia.** Cuánto alucina un modelo depende de la tarea; se cuenta en el
  [análisis de errores](../Evaluacion/analisis-de-errores.md), no se toma de un ranking.

Las [salidas estructuradas](muestreo.md#salidas-estructuradas-restringir-lo-que-se-puede-muestrear) no
ayudan acá: aseguran que el campo `total` sea un número, no que sea el número de la factura.

## Qué leer sobre alucinación

Kalai y otros, [*Why Language Models Hallucinate*](https://arxiv.org/abs/2509.04664), la introducción
y la parte sobre post-entrenamiento y evaluación: es la explicación más reciente y unificada. Fijarse
en qué parte es causa estadística y qué parte es incentivo de los benchmarks. Para el panorama de
detección y mitigación, [Weng](https://lilianweng.github.io/posts/2024-07-07-hallucination/); para el
efecto bola de nieve, el abstract de [Zhang y otros](https://arxiv.org/abs/2305.13534).
