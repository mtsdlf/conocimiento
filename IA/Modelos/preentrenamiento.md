---
resumen: >-
  El preentrenamiento es la primera etapa de un modelo base: entrenarlo a predecir el próximo token
  sobre un corpus enorme y sin etiquetas, que es donde adquiere la mayor parte de su conocimiento
  factual.
estado: borrador
estabilidad: estable
fuentes:
  - https://arxiv.org/abs/2001.08361
  - https://arxiv.org/abs/2203.15556
  - https://arxiv.org/abs/2211.04325
  - https://arxiv.org/abs/2305.16264
  - https://arxiv.org/abs/2405.05904
  - https://lilianweng.github.io/posts/2024-07-07-hallucination/
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - http://cs336.stanford.edu/spring2025/
aliases: [pretraining, pre-training, preentrenar, leyes de escala, scaling laws, Chinchilla, datos de entrenamiento, corte de conocimiento, knowledge cutoff]
creado: 2026-11-27
revisado:
---

# Preentrenamiento

El preentrenamiento es la primera etapa de un modelo base: entrenarlo a predecir el próximo token
sobre un corpus enorme y sin etiquetas, que es donde adquiere la mayor parte de su conocimiento
factual.

Quien construye un producto no preentrena, pero hereda todo lo que esta etapa decidió: qué sabe el
modelo, hasta qué fecha, en qué idiomas y dominios rinde, y cuánto cuesta usarlo. Lo que sale de acá
es un **modelo preentrenado**, que el [post-entrenamiento](post-entrenamiento.md) ajusta para que siga
instrucciones.

## El texto es su propia etiqueta

En cada posición de un texto, la respuesta correcta es el [token](token-y-embedding.md) que sigue. No
hace falta que nadie etiquete nada: cualquier texto sirve como dato de entrenamiento. Huyen, según el
resumen público del capítulo 1, ubica ahí el paso de los modelos de lenguaje a los LLM, "enabled by
self-supervision".

Gekhman et al. (EMNLP 2024) encontraron que un modelo aprende "much more slowly" los hechos nuevos
que aparecen recién en el ajuste, y concluyen que el conocimiento factual se adquiere sobre todo en el
preentrenamiento. Qué implica eso para elegir entre darle el conocimiento en el contexto o ajustarlo
está en [Finetuning](../Ajuste/finetuning.md#lo-que-el-finetuning-enseña-y-lo-que-no). Lectura de
esta base: por la misma razón, el modelo no sabe nada posterior a la fecha de sus datos (el corte de conocimiento de cada modelo está en la ficha de
[Modelos disponibles](modelos-disponibles.md)).

## Qué datos entran y qué deja afuera eso

Según el resumen del capítulo 2 de Huyen, la calidad del modelo depende mucho de sus datos, y los
proveedores suelen usar "whatever data is available"; para idiomas con pocos recursos y para dominios
especializados hace falta curar datos. La [tokenización](token-y-embedding.md#el-mismo-texto-cuesta-distinto-según-el-idioma)
agrega su propio sesgo de idioma. Según Lilian Weng, los datos de preentrenamiento desactualizados,
faltantes o incorrectos, que el modelo memoriza, son una de las causas de la [alucinación](alucinacion.md).

## Leyes de escala: cuánto modelo y cuántos datos

La escala de un modelo se mide en tres números: parámetros, tokens de entrenamiento y FLOPs de
entrenamiento (Huyen, resumen del cap. 2). Las leyes de escala relacionan esos números con la
pérdida, que es cuánto se equivoca el modelo al predecir el próximo token.

Kaplan et al. (enero de 2020) encontraron que "the loss scales as a power-law with model
size, dataset size, and the amount of compute used for training", con tendencias de "more than seven
orders of magnitude", y que detalles como el ancho o la profundidad de la red tienen "minimal effects
within a wide range". Su receta para un presupuesto dado: "training very large models on a relatively
modest amount of data and stopping significantly before convergence".

Hoffmann et al. (marzo de 2022) entrenaron más de 400 modelos de 70 millones a más de 16
mil millones de parámetros y concluyeron otra cosa: "We find that current large language models are
significantly undertrained". El tamaño del modelo y los tokens tienen que crecer en la misma
proporción. Su modelo Chinchilla, de 70.000 millones de parámetros, entrenado con unas 4 veces más
datos que Gopher (280.000 millones) y el mismo cómputo, superó a Gopher, GPT-3, Jurassic-1 y
Megatron-Turing NLG, con 67,5 % de promedio en MMLU.

> [!IMPORTANT]
> Las dos leyes dan recetas distintas para el mismo presupuesto. Kaplan (2020): un modelo muy grande
> con relativamente pocos datos. Chinchilla (2022): crecer modelo y datos por igual, porque los modelos
> de la época estaban subentrenados. Chinchilla es la posterior y la que mejor resultado mostró con su
> propio modelo, pero ninguna de las dos es "la" ley de escala. Las razones metodológicas de la
> diferencia se discuten en los papers completos, que no se leyeron.

Lectura de esta base: "óptimo" en las dos quiere decir la menor pérdida para un presupuesto de
entrenamiento, no el menor costo de servir el modelo. Un modelo que se va a usar millones de veces
puede convenir más chico y entrenado con más datos de los que la receta pide, porque cada respuesta
cuesta según su tamaño ([Costo y latencia](../../Arquitectura/Caracteristicas/costo-y-latencia.md)).

## El texto humano se puede acabar

Villalobos et al. proyectaron en 2022 (revisado en 2024) que los conjuntos de entrenamiento podrían
alcanzar el stock de texto humano público "between 2026 and 2032" si la tendencia sigue, y antes si se
sobreentrena. Es una proyección, no una medición, y su ventana ya empezó. Las salidas que proponen son
[datos sintéticos](../Ajuste/datos-sinteticos.md), transferir desde dominios con más datos y aprender
más de cada dato.

Repetir datos ayuda hasta cierto punto. Muennighoff et al. (2023), con 400 corridas y modelos de
hasta 9.000 millones de parámetros, encontraron que hasta unas 4 pasadas por los mismos datos casi no
cambian la pérdida frente a datos nuevos, y que más allá el cómputo extra rinde cada vez menos. Sumar
código o aflojar los filtros de calidad son otras formas de estirar los datos.

## Qué leer sobre preentrenamiento

Los abstracts de [Chinchilla](https://arxiv.org/abs/2203.15556) y de
[Kaplan et al.](https://arxiv.org/abs/2001.08361), uno al lado del otro, con el gráfico de
asignación óptima de Chinchilla: fijarse en qué optimiza cada uno. Para el detalle técnico,
[CS336](http://cs336.stanford.edu/spring2025/) de Stanford, clases 9 y 11 (escala) y 13 y 14 (datos);
se leyó solo la página del curso.
