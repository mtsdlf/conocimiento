---
resumen: >-
  Las métricas de evaluación son las fórmulas que califican una salida sin una persona: si el código
  generado pasa pruebas (corrección funcional), cuánto se parece a una respuesta de referencia
  (similitud) o qué tan probable le resulta un texto al modelo (perplejidad).
estado: borrador
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://hamel.dev/blog/posts/evals-faq/
  - https://arxiv.org/abs/2107.03374
  - https://aclanthology.org/P02-1040/
  - https://aclanthology.org/W04-1013/
  - https://arxiv.org/abs/1904.09675
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/
aliases: [evaluation metrics, métricas de LLM, exact evaluation, evaluación exacta, pass@k, BLEU, ROUGE, BERTScore, perplejidad, perplexity]
creado: 2026-11-27
revisado:
---

# Métricas de evaluación

Las métricas de evaluación son las fórmulas que califican una salida sin una persona: si el código
generado pasa pruebas (corrección funcional), cuánto se parece a una respuesta de referencia
(similitud) o qué tan probable le resulta un texto al modelo (perplejidad).

Son una de las formas de calificar los [evals](evals.md), junto a las aserciones propias, el
[juez](ia-como-juez.md) y las personas. Según su índice, Huyen las reúne en el capítulo 3 del libro:
"Understanding Language Modeling Metrics" y "Exact Evaluation", que se divide en corrección funcional
y similitud contra datos de referencia. Las métricas de velocidad (tiempo al primer token, tiempo por
token) son de otra clase y están en [inferencia](../Produccion/inferencia.md) y en
[costo y latencia](../../Arquitectura/Caracteristicas/costo-y-latencia.md).

## Por qué una métrica genérica engaña

Una métrica genérica mide algo que existe en cualquier texto, no lo que falla en el producto. Husain
lo dice sin vueltas: "Generic evaluations waste time and create false confidence when you use them as
quality measures." Su orden es el inverso al del catálogo: primero el
[análisis de errores](analisis-de-errores.md) para saber qué falla, después chequeos binarios propios
para esas fallas, y las métricas genéricas, como mucho, para encontrar trazas que vale la pena leer.

Husain agrega una advertencia sobre la meta: "If you're passing 100% of your evals, you're likely not
challenging your system enough." Un puntaje perfecto dice más del conjunto de casos que del sistema.

## Corrección funcional: la única exacta que aguanta

Cuando la salida se puede ejecutar o verificar, la medida más fuerte es correrla. Chen et al. (2021,
leído en su abstract) presentan HumanEval, un conjunto para medir corrección funcional al generar
programas a partir de docstrings: el modelo de entonces resolvía 28,8 % de los problemas con una
muestra y 70,2 % con 100 muestras por problema. De ahí sale pass@k, la proporción de problemas en los
que al menos una de k muestras pasa las pruebas; la definición formal está en el cuerpo del paper,
que no se leyó.

Lo mismo vale fuera del código. Yan et al. recomiendan empezar con "unit tests (i.e., assertions)
consisting of samples of inputs and outputs from production": si la salida tiene que ser un JSON
válido, citar una fuente o no pasar de cierto largo, una aserción lo comprueba sin ambigüedad. Es el
nivel 1 de los [evals](evals.md). Por inferencia de esta base, conviene llevar a esta forma todo lo
que se pueda, porque es barata, rápida y no tiene sesgos de juez.

## Similitud con una referencia

Las métricas de similitud comparan la salida con una respuesta escrita de antemano. BLEU (Papineni et
al., 2002) nació para traducción y ROUGE (Lin, 2004) para resúmenes; las dos cuentan solapamiento de
palabras. BERTScore (Zhang et al., 2020) compara con embeddings contextuales en lugar de palabras;
según el abstract, se probó con 363 sistemas de traducción y de subtitulado de imágenes y
correlaciona mejor con juicios humanos que las métricas previas. Es una afirmación de sus autores,
sobre esas tareas y no sobre aplicaciones con modelos de lenguaje.

El límite es de fondo: una respuesta correcta puede decirse con otras palabras, y una incorrecta
puede parecerse mucho a la referencia. Husain sostiene que las métricas de similitud como BERTScore o
ROUGE "are not useful for evaluating LLM outputs in most AI applications", con una excepción: en
búsqueda y [recuperación](../Contexto/recuperacion.md), donde lo que se quiere medir es justamente
cercanía semántica.

> [!NOTE]
> Sin fuente todavía: un estudio que mida la correlación de BLEU y ROUGE con juicio humano en
> generación abierta. Las páginas de los dos papers no traían abstract.

## Perplejidad y entropía cruzada

La perplejidad y la entropía cruzada miden qué tan probable le resulta un texto a un modelo: cuanto
más bajas, mejor predice ese texto. Según el resumen de capítulo del libro, Huyen las presenta como
métricas "often confusing" y explica cómo usarlas "in evaluation and data processing". La lectura de
esta base es que sirven sobre todo a quien compara o entrena modelos y a quien prepara
[datos para ajustar](../Ajuste/datos-para-ajustar.md), no para saber si una respuesta sirve: un texto
probable no es un texto verdadero, que es el origen de la
[alucinación](../Modelos/alucinacion.md).

> [!NOTE]
> Sin fuente todavía: la definición formal de perplejidad y entropía cruzada y su uso para detectar
> contaminación o duplicados. El capítulo de Huyen no se pudo leer y el libro de texto de Jurafsky y
> Martin (SLP3, cap. 3) llegó sin texto.

## Cuánto pesan frente al juez y a las personas

> [!IMPORTANT]
> Huyen presenta la evaluación exacta, el juez y la comparación como métodos que se combinan en un
> mismo pipeline, y según el resumen de sus capítulos, ninguno es perfecto por separado. Husain es
> mucho más escéptico con todo lo genérico y lo deja para buscar trazas. No se contradicen (él admite
> la similitud en búsqueda), pero el peso que le dan a la métrica es distinto. Lectura de esta base:
> corrección funcional y aserciones donde se pueda; [juez](ia-como-juez.md) validado donde el
> criterio es un juicio; similitud solo cuando la tarea es de cercanía semántica.

## Lo que falta

> [!NOTE]
> Sin fuente todavía: las métricas de clasificación (precisión, recall, F1) aplicadas a salidas que
> son una etiqueta. Son de ML clásico, que el tema deja a [Datos](../../Datos/datos.md); la única
> mención en esta vertical es la de Husain para validar un [juez](ia-como-juez.md). Tampoco hay fuente
> sobre cómo se cortan las métricas por segmento. La evaluación de trayectorias de un agente está en
> [fallas de agentes](../Agentes/fallas-de-agentes.md).

## Qué leer sobre métricas

Huyen, *AI Engineering*, capítulo 3, secciones "Understanding Language Modeling Metrics" y "Exact
Evaluation", para el mapa (leído solo por su índice). Husain,
["Evals FAQ"](https://hamel.dev/blog/posts/evals-faq/), preguntas sobre métricas listas para usar y
sobre métricas de similitud, para la postura práctica: fijarse en qué mide cada métrica de verdad
(solapamiento, no corrección).
