---
resumen: >-
  Los datos sintéticos son ejemplos de entrenamiento generados por un modelo en lugar de escritos o
  recolectados por personas; abaratan y escalan los datos para ajustar, pero hay que verificarlos
  como cualquier dato, y entrenar con ellos en exceso puede degradar al modelo.
estado: borrador
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://arxiv.org/abs/2212.10560
  - https://arxiv.org/abs/2304.12244
  - https://arxiv.org/abs/2212.08073
  - https://arxiv.org/abs/2306.11644
  - https://arxiv.org/abs/2501.12948
  - https://hamel.dev/blog/posts/evals/
  - https://www.nature.com/articles/s41586-024-07566-y
  - https://arxiv.org/abs/2305.17493
  - https://arxiv.org/abs/2404.01413
  - https://arxiv.org/abs/2211.04325
aliases: [synthetic data, datos generados, data synthesis, síntesis de datos, Self-Instruct, colapso de modelos, model collapse]
creado: 2026-11-27
revisado:
---

# Datos sintéticos

Los datos sintéticos son ejemplos de entrenamiento generados por un modelo en lugar de escritos o
recolectados por personas; abaratan y escalan los datos para ajustar, pero hay que verificarlos
como cualquier dato, y entrenar con ellos en exceso puede degradar al modelo.

Resuelven el cuello de botella de [datos para ajustar](datos-para-ajustar.md): juntar ejemplos
reales buenos es lo caro del [finetuning](finetuning.md). La [destilación](destilacion.md) por datos
es un caso particular, en el que el generador es un modelo más grande que el que se entrena. A escala
de laboratorio pesa además otra razón: una proyección de 2022, revisada en 2024, estima que los
conjuntos de entrenamiento podrían alcanzar el stock de texto humano público "between 2026 and
2032", y propone los datos sintéticos entre las salidas.

## Generar es fácil; verificar es lo difícil

El resumen del cap. 8 de Huyen lo plantea en dos frases: "Just like real data, synthetic data must
be evaluated to ensure its quality before being used to train models", y "It's hard to automate
data generation, but it's even harder to automate verifying it". La síntesis se volvió práctica,
según ese resumen, cuando los modelos pudieron generar datos realistas y complejos.

## Cuatro formas de generar datos con un modelo

| Método | Qué hace | Resultado que reporta |
|---|---|---|
| Self-Instruct (Wang et al., 2022) | el modelo genera sus propias instrucciones, entradas y salidas; se filtran las inválidas o repetidas y se ajusta con el resto | con GPT-3 base, "a 33% absolute improvement" en un benchmark de instrucciones, y "a 5% absolute gap" por detrás de InstructGPT-001 en evaluación con personas |
| Evol-Instruct (Xu et al., 2023) | un modelo reescribe instrucciones semilla "step by step into more complex instructions" | según su abstract, las personas prefirieron las instrucciones evolucionadas a las escritas a mano |
| IA constitucional (Constitutional AI; Bai et al., 2022) | el modelo critica y revisa sus propias respuestas según principios escritos, y genera las preferencias para el refuerzo | según su abstract, "a harmless but non-evasive AI assistant", con muchas menos etiquetas humanas |
| Libros de texto sintéticos, phi-1 (Gunasekar et al., 2023) | un modelo grande escribe explicaciones y ejercicios para entrenar a uno chico | según su abstract, un modelo de 1.300 millones de parámetros entrenado con unos 6.000 millones de tokens de web filtrada por su calidad de libro de texto y unos 1.000 millones de tokens sintéticos llegó a 50,6 % en HumanEval |

Los dos primeros generan datos para enseñar a seguir instrucciones; la IA constitucional, para alinear
el comportamiento, y es una pieza del [post-entrenamiento](../Modelos/post-entrenamiento.md); phi-1,
para enseñar una capacidad. Todas las cifras son de sus autores, leídas en los abstracts.

## Cómo se verifica un ejemplo generado

Ninguno de los papers leídos trata la verificación como un componente aparte, aunque Self-Instruct
filtra de forma explícita entre generación y entrenamiento. Lo que la hace posible, en lectura de
esta base, es tener un verificador más barato que el generador:

- **Un resultado comprobable**: en matemática y código se puede chequear la respuesta o correr los
  tests. Que DeepSeek-R1 sirva de ejemplo es lectura de esta base: según su abstract, rinde fuerte
  en "verifiable tasks in mathematics, coding competitions, and STEM fields".
- **Los evals del propio sistema**: Husain reutiliza los tests y las aserciones de los
  [evals](../Evaluacion/evals.md) para descartar ejemplos sintéticos que fallan.
- **Un modelo que califica**: un [juez](../Evaluacion/ia-como-juez.md) filtra lo que no se puede
  comprobar a mano, con sus propios sesgos.

Después del filtro, los datos sintéticos pasan por la misma inspección, deduplicación y separación
de los evals que los reales (ver [Datos para ajustar](datos-para-ajustar.md#duplicados-y-contaminación-con-los-casos-de-evaluación)).

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre verificación y filtrado de datos sintéticos, y un
> trabajo reciente (2025-2026) sobre síntesis a gran escala.

## El colapso de modelos

> [!IMPORTANT]
> **Si entrenar con datos generados degrada a los modelos.** Shumailov et al. (*Nature* 631, 2024)
> describen un proceso degenerativo: los modelos entrenados con contenido generado por modelos
> "forget the true underlying data distribution". Se pierden primero las colas raras de la
> distribución y después las salidas convergen a una varianza muy chica; lo observan en modelos
> simples y en modelos de lenguaje. La página de *Nature* no cargó: la cita sale del texto del
> artículo de *Nature* recuperado por buscador. La versión previa en arXiv se tituló "The Curse of
> Recursion" (2023), y el artículo tiene una corrección de los autores que no se leyó.
>
> Gerstgrasser et al. (2024) acotan el resultado. Según su abstract, reemplazar los datos reales por
> los sintéticos de cada generación lleva al colapso, pero acumular los sintéticos junto a los
> reales lo evita, con distintos tamaños, arquitecturas e hiperparámetros; en un modelo lineal
> simplificado demuestran que el error queda acotado al acumular y crece al reemplazar.
>
> Los dos resultados no se contradicen: parten de supuestos distintos, reemplazar o acumular. Qué tan
> fuerte es el efecto en modelos de lenguaje grandes sigue discutido, y todas las lecturas de esta
> base son de abstracts. Hay una crítica de terceros a Shumailov et al. que no se leyó.

Para un equipo que ajusta un modelo una vez, la lectura práctica es mezclar los sintéticos con datos
reales en vez de reemplazarlos y medir con evals hechos con casos reales, no generados (lectura de
esta base). El colapso que describe Shumailov es sobre generaciones sucesivas de modelos entrenados
con salidas de los anteriores; que eso sea más el problema de los laboratorios que el de un ajuste
puntual también es lectura de esta base.

## Qué leer sobre datos sintéticos

Huyen, *AI Engineering*, cap. 8, "Data Augmentation and Synthesis" (pp. 380-396), como mapa. El
paper de [Self-Instruct](https://arxiv.org/abs/2212.10560), en el proceso de generación y filtrado,
como mecanismo mínimo. [Shumailov et al.](https://arxiv.org/abs/2305.17493) y
[Gerstgrasser et al.](https://arxiv.org/abs/2404.01413) leídos como par: fijarse en qué miden como
colapso (la pérdida de las colas de la distribución) y bajo qué supuesto (reemplazar o acumular).
