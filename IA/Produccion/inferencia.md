---
resumen: >-
  La inferencia es correr un modelo ya entrenado para que genere su salida; se mide en latencia,
  throughput y utilización del hardware, y se optimiza cambiando el modelo (cuantización,
  decodificación especulativa) o el servicio que lo atiende (batching, memoria de la KV cache,
  separar prefill y decode).
estado: borrador
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices
  - https://arxiv.org/abs/2211.17192
  - https://arxiv.org/abs/2309.06180
  - https://www.usenix.org/conference/osdi22/presentation/yu
  - https://arxiv.org/abs/2401.09670
  - https://arxiv.org/abs/2306.00978
  - https://arxiv.org/abs/2411.02355
  - https://arxiv.org/abs/2204.02311
  - https://docs.vllm.ai/en/latest/
  - https://platform.claude.com/docs/en/build-with-claude/batch-processing
  - https://developers.openai.com/api/docs/guides/batch
aliases: [inference, inference optimization, optimización de inferencia, serving, servicio de inferencia, LLM serving]
creado: 2026-11-27
revisado:
---

# Inferencia

La inferencia es correr un modelo ya entrenado para que genere su salida; se mide en latencia,
throughput y utilización del hardware, y se optimiza cambiando el modelo (cuantización,
decodificación especulativa) o el servicio que lo atiende (batching, memoria de la KV cache,
separar prefill y decode).

Quien usa un modelo por API no maneja el servidor, pero paga sus consecuencias en precio y
latencia; quien autoaloja un modelo de pesos abiertos lo maneja directamente. Huyen le dedica el cap. 9,
"Inference Optimization" (según el índice del libro), y según su resumen mide la inferencia en
latencia, throughput y utilización, y advierte que bajar la latencia suele subir el costo. La
inferencia mueve las dos características que un modelo pone al frente, el
[costo y la latencia](../../Arquitectura/Caracteristicas/costo-y-latencia.md).

## Prefill y decode: por qué generar está limitado por memoria

Generar una respuesta tiene dos fases. En el *prefill*, el modelo procesa todo el prompt de una
vez y produce el primer token; en el *decode*, genera los siguientes de a uno, cada uno a partir de
los anteriores. Databricks lo resume así: "Generating the first token is typically compute-bound,
while subsequent decoding is memory-bound operation".

La razón está en cuánto hay que leer por token. Para emitir cada token nuevo, el acelerador tiene
que traer de su memoria todos los pesos del modelo y la [KV cache](../Modelos/transformer.md) de la
conversación; con pocos pedidos a la vez, la velocidad depende de "how quickly we can load model
parameters from GPU memory". Un Llama-2-70B en float16 pesa 140 GB: esos 140 GB se leen para cada
token. Leviathan et al. lo dicen del lado del algoritmo: "decoding K tokens takes K serial runs of
the model".

Dos consecuencias. El TPOT se predice mejor con el ancho de banda de memoria que con la potencia de
cálculo del acelerador (Databricks). Y casi todas las optimizaciones de abajo atacan esa lectura
repetida: leer menos bytes (cuantización), leer una vez para varios tokens (decodificación
especulativa) o para varios usuarios (batching). Al elegir un acelerador para inferencia importan
la memoria y su ancho de banda más que los FLOPs pico, por inferencia de esta base desde lo
anterior.

> [!NOTE]
> Sin fuente todavía: una ficha fechada de aceleradores (GPU y TPU) con memoria y ancho de banda.

## Las métricas: las del usuario y las del servidor

El TTFT y el TPOT miden lo que espera un usuario y están definidos en
[Costo y latencia](../../Arquitectura/Caracteristicas/costo-y-latencia.md). Del lado del servidor
se suman tres:

- **Throughput**: "The number of output tokens per second an inference server can generate across
  all users and requests" (Databricks). Es del servidor entero; el TPOT es de cada usuario.
- **Goodput**: el trabajo que cumple los objetivos de latencia (de TTFT y de TPOT), no el bruto.
  DistServe lo toma como la métrica a optimizar; la definición es lectura de su título
  ("Goodput-optimized") y de su abstract, que no la da literal.
- **Utilización**: cuánto del hardware se aprovecha. Para el decode, Databricks usa la MBU: "MBU is
  defined as (achieved memory bandwidth) / (peak memory bandwidth)", con el ancho de banda logrado
  igual a (tamaño de los parámetros + tamaño de la KV cache) / TPOT. La MFU, que introdujo el paper
  de PaLM, compara los FLOPs usados con el máximo teórico; según resultados de buscador, PaLM
  reportó 45,7 % sin contar la autoatención y 46,2 % contándola.

Latencia y throughput tiran en sentidos opuestos. Databricks midió un modelo de 7.000 millones de
parámetros en una sola GPU, con 512 tokens de entrada, 64 de salida y batching estático:

| Pedidos por batch | 1 | 4 | 8 | 16 | 32 | 64 |
|---|---|---|---|---|---|---|
| Pedidos por segundo | 0,9 | 3,2 | 5,3 | 8,0 | 10,5 | 12,5 |

Llevar el batch de 1 a 64 multiplica el throughput unas 14 veces y la latencia unas 4. Por eso la
pregunta de un servicio no es cuán rápido puede responder, sino cuánto throughput saca sin pasarse
de un objetivo de latencia, que es lo que mide el goodput (lectura de esta base).

## Optimizar el modelo: menos bits y menos pasadas

**Cuantización.** Guardar los pesos con menos bits reduce lo que hay que leer por token. Según
Databricks, pasar de 16 a 8 bits puede reducir a la mitad las GPU necesarias cuando la memoria es
el límite, y la KV cache de Llama-2-70B (largo 1024, batch 16) baja de 5 GiB a 2,5 GiB. Sobre la
calidad, Kurtic et al. corrieron más de 500.000 evaluaciones en la familia Llama-3.1 y, según su
abstract, encontraron FP8 "effectively lossless", INT8 con 1 a 3 % de pérdida bien ajustado e INT4
de solo pesos "more competitive than expected". Recomiendan 4 bits en pesos con activaciones de 16
para costo en uso sincrónico, y 8 bits en pesos y activaciones para batching continuo asincrónico.
AWQ, un método de cuantización a 4 bits, parte de que "Protecting only 1% salient weights can
greatly reduce quantization error". Las cifras de Kurtic son de una familia de modelos: en otros
modelos o tareas la pérdida puede ser otra, y la única forma de saberlo es correr las
[evals](../Evaluacion/evals.md) propias con el modelo cuantizado.

**Decodificación especulativa.** Un modelo chico propone varios tokens y el grande los verifica
todos en una sola pasada; se aceptan los que el grande habría elegido. Leviathan et al. reportan,
en T5-XXL, una aceleración de 2X a 3X "with identical outputs", sin reentrenar. Funciona porque el
decode deja cálculo ocioso: verificar varios tokens cuesta casi lo mismo que generar uno (lectura de
esta base desde la sección de prefill y decode).

La [destilación](../Ajuste/destilacion.md) también baja el costo de inferencia, pero cambia los
pesos y se trata en Ajuste.

## Optimizar el servicio: llenar la GPU sin pasarse de latencia

**Batching continuo.** Con batching estático, un batch espera a que termine su pedido más largo.
Orca planifica "at the granularity of iteration (instead of request)": un pedido que termina sale y
otro entra sin esperar al resto. Orca reporta hasta 36,9 veces más throughput que FasterTransformer
en GPT-3 175B a igual latencia; Databricks, de 10 a 20 veces más que el batching dinámico.

**Memoria de la KV cache.** La KV cache de cada pedido es grande y de tamaño variable, y la
fragmentación de memoria limita cuántos pedidos entran en un batch. PagedAttention la administra en
bloques, como la memoria virtual de un sistema operativo, y según su abstract logra "near-zero waste
in KV cache memory" y de 2 a 4 veces más throughput que FasterTransformer y Orca a igual latencia.
Reutilizar la KV cache de un prefijo común entre pedidos (*prefix caching*) es la versión
autoalojada del prompt cache de [Cache de modelos](cache-de-modelos.md).

**Separar prefill y decode.** Como las dos fases tienen cuellos distintos, mezclarlas en la misma
GPU hace que una frene a la otra. DistServe las corre en GPU distintas y ajusta cada una a su
objetivo de TTFT o de TPOT; reporta "7.4x more requests" servidos, o un objetivo de latencia 12,6
veces más estricto, con más del 90 % de los pedidos dentro del objetivo.

> [!NOTE]
> Sin fuente todavía: evidencia independiente de prefill y decode separados en producción, y el
> costo de mover la KV cache entre máquinas.

Los motores de inferencia de código abierto reúnen estas técnicas; cuáles soporta uno de ellos está
en la ficha [APIs de batch y motores de inferencia](apis-de-batch-y-motores-de-inferencia.md).

## Batch: cambiar urgencia por precio

Los proveedores grandes ofrecen una API de batch: se manda un lote de pedidos, se devuelven en
algún momento dentro de una ventana de horas y se cobran con descuento. Es el mismo canje de
latencia por throughput de la tabla de arriba, vendido como producto (lectura de esta base). Sirve
para trabajo sin usuario esperando: correr evals, etiquetar datos, enriquecer registros. Anthropic
lo ilustra con "You're running large-scale evaluations or analyses", y en su API el batch se
combina con el prompt cache. El descuento, la ventana y los límites de cada proveedor están en la
ficha [APIs de batch y motores de inferencia](apis-de-batch-y-motores-de-inferencia.md).

## Qué leer

Para el mecanismo, el artículo de Databricks
["LLM Inference Performance Engineering: Best Practices"](https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices)
(2023): fijarse en la fórmula de la MBU, en por qué el TTFT y el TPOT se comportan distinto y en la
curva de throughput contra tamaño de batch. Después, el paper de
[PagedAttention](https://arxiv.org/abs/2309.06180), para ver por qué la memoria de la KV cache es el
límite del batch. El cap. 9 de *AI Engineering* es el canónico para decidir qué optimizar; acá se usó
solo su índice y su resumen.
