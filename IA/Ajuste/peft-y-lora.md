---
resumen: >-
  PEFT es la familia de técnicas que ajustan un modelo entrenando una fracción chica de parámetros
  con el resto congelado; LoRA, la más usada, aprende la actualización como dos matrices chicas, y
  QLoRA suma guardar el modelo congelado en 4 bits para ajustar modelos grandes en una sola GPU.
estado: borrador
estabilidad: estable
fuentes:
  - https://huggingface.co/docs/peft/index
  - https://huggingface.co/docs/peft/main/en/conceptual_guides/lora
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://arxiv.org/abs/1902.00751
  - https://arxiv.org/abs/2104.08691
  - https://arxiv.org/abs/2106.09685
  - https://arxiv.org/abs/2305.14314
  - https://arxiv.org/abs/2405.09673
  - https://arxiv.org/abs/2311.03285
  - https://arxiv.org/abs/2310.18547
  - https://arxiv.org/abs/2212.04089
  - https://arxiv.org/abs/2408.07666
  - https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms
aliases: [PEFT, parameter-efficient finetuning, ajuste eficiente en parámetros, LoRA, low-rank adaptation, QLoRA, adapters, adaptadores, prompt tuning, soft prompts, fusión de modelos, model merging]
creado: 2026-11-27
revisado:
---

# PEFT y LoRA

PEFT es la familia de técnicas que ajustan un modelo entrenando una fracción chica de parámetros
con el resto congelado; LoRA, la más usada, aprende la actualización como dos matrices chicas, y
QLoRA suma guardar el modelo congelado en 4 bits para ajustar modelos grandes en una sola GPU.

Existe por la cuenta de memoria de [Finetuning](finetuning.md): cada parámetro entrenable carga
gradientes y estados del optimizador que pesan varias veces más que el parámetro. El resumen del
libro de Huyen lo dice así: "PEFT reduces finetuning's memory requirements by reducing the number of
trainable parameters". La documentación de la librería PEFT de Hugging Face agrega la promesa de la
familia: entrenar "a small number of (extra) model parameters" con "performance comparable to a
fully fine-tuned model".

## La familia, de los adapters a LoRA

| Técnica | Qué se entrena | Fuente |
|---|---|---|
| Adapters (Houlsby et al., 2019) | módulos chicos insertados entre las capas, con los pesos originales congelados | según su abstract, en BERT quedan a 0,4 % del rendimiento del finetuning completo, con 3,6 % de parámetros por tarea |
| Prompt tuning (Lester et al., 2021) | vectores que se anteponen a la entrada, aprendidos por retropropagación | según su abstract, gana con el tamaño del modelo y pasados los mil millones de parámetros casi iguala al finetuning completo |
| LoRA (Hu et al., 2021) | dos matrices chicas por capa que representan el cambio de los pesos | ver abajo |

Un soft prompt, lo que aprende el prompt tuning, no es un [prompt](../Contexto/prompt.md) en texto:
es una secuencia de números que no se puede leer ni editar. El parecido del nombre confunde a quien
viene de las APIs.

## Cómo funciona LoRA

LoRA deja la matriz de pesos original congelada y aprende su cambio como el producto de dos matrices
chicas (una descomposición de bajo rango). La guía conceptual de PEFT lo describe así: "The original
weight matrix remains frozen and doesn't receive any further adjustments". El parámetro `r` es el
rango de esas matrices: "Lower rank results in smaller update matrices with fewer trainable
parameters". Otro parámetro, `lora_alpha`, escala la actualización por `lora_alpha/r`.

Según el abstract de Hu et al., frente a GPT-3 de 175.000 millones de parámetros ajustado entero,
LoRA reduce los parámetros entrenables "10,000 times" y la memoria de GPU "3 times".

Al terminar, la actualización se puede sumar a los pesos originales: según PEFT, "the weights can
actually be merged into a new weight matrix that is identical". El modelo fusionado se sirve sin
latencia extra. Si no se fusiona, el modelo de partida se comparte y cada tarea es un adaptador chico:
"multiple lightweight and portable LoRA models for various downstream tasks built on top of them".

### Cuánto rango y en qué capas

No hay regla firme. En el experimento de Raschka (un modelo, un conjunto de datos), el mejor
resultado salió con r=256; alpha igual al doble del rango fue un "sweet spot" con r=8; y aplicar
LoRA a todas las capas subió los parámetros entrenables de 4.194.304 a 20.277.248 y la memoria de
14,18 GB a 16,62 GB. El propio artículo da dos valores distintos para el mejor alpha con r=256 (128
en un experimento, 512 en su lista final), así que la cifra vale como orden y no como receta.

## LoRA aprende menos y olvida menos

Entrenar menos parámetros no es gratis. Biderman et al. (TMLR 2024) compararon LoRA con el finetuning
completo en programación y matemática; según un resumen secundario de su
abstract, con rangos estándar LoRA "substantially underperforms full finetuning", pero "forgets
less" lo que el modelo sabía fuera del dominio y da salidas más diversas. El
finetuning completo aprende cambios de rango 10 a 100 veces mayor. LoRA conviene cuando la tarea es
acotada y lo que el modelo ya hace bien importa; para cambiar mucho el comportamiento en un dominio
difícil, el finetuning completo aprende más (lectura de esta base). El olvido se explica en
[Finetuning](finetuning.md#olvido-catastrófico-lo-que-el-modelo-pierde-al-ajustarse).

## QLoRA: el modelo congelado en 4 bits

QLoRA (Dettmers et al., 2023) combina LoRA con cuantización: el modelo congelado se guarda en 4
bits y se retropropaga a través de él hacia los adaptadores. Según su abstract, permite ajustar un
modelo de 65.000 millones de parámetros en una sola GPU de 48 GB sin perder rendimiento frente al
finetuning en 16 bits. Sus trucos son un tipo de 4 bits pensado para pesos (NF4, 4-bit NormalFloat), una
doble cuantización y optimizadores paginados.

Los 4 bits describen cómo se guardan los pesos congelados; los adaptadores se entrenan en mayor
precisión. Es lectura de esta base a partir del abstract ("backpropagates through a frozen, 4-bit
quantized model into low-rank adapters"), sin cotejar en el texto. En el experimento de Raschka,
QLoRA bajó la memoria de 21,33 GB a 14,18 GB y subió el tiempo de entrenamiento de 1,85 h a 2,79 h,
con poco efecto en el resultado: se cambia memoria por tiempo.

Esta cuantización es la que pide el ajuste. La que se usa para servir un modelo más barato o más
rápido es otra decisión y está en [Inferencia](../Produccion/inferencia.md).

## Servir muchos adaptadores sobre un mismo modelo

Como los adaptadores son chicos y comparten el modelo de partida, un mismo servidor puede atender muchas
tareas o muchos clientes, cada uno con su LoRA. Dos papers de 2023 lo atacan como problema de
sistemas, con cifras de sus autores, no replicadas:

- S-LoRA (Sheng et al.) guarda todos los adaptadores en memoria principal y pasa a la GPU solo los
  de las consultas en curso; según su abstract, sirve miles de adaptadores con hasta 4 veces más
  rendimiento que las implementaciones de referencia.
- Punica (Chen et al.) agrupa en un solo kernel las operaciones de distintos LoRA sobre una copia
  del modelo de partida; según su abstract, hasta 12 veces más rendimiento, con unos 2 ms de latencia extra
  por token.

Elegir qué adaptador atiende cada consulta es un caso de [ruteo](../Produccion/router-y-gateway-de-modelos.md)
(lectura de esta base).

## Fusionar modelos ajustados

La fusión de modelos combina varios modelos ajustados "into one model that works better than these
models separately", según el resumen del libro de Huyen, que la trata junto al ajuste multitarea. El
mecanismo más simple es la aritmética de tareas (Ilharco et al., 2022): según su abstract, la
diferencia entre los pesos ajustados y los originales es un "vector de tarea", y sumar o restar
vectores cambia el comportamiento; lo llaman "a simple, efficient and effective way of editing
models". Un survey de Yang et al., revisado hasta fines de 2025, ordena los métodos.

> [!NOTE]
> Sin fuente todavía: los métodos concretos de fusión (promedio de pesos, TIES, DARE, SLERP), el
> ajuste multitarea y prefix tuning, que solo aparece citado por Lester et al.

## Qué leer sobre LoRA

El paper de [LoRA](https://arxiv.org/abs/2106.09685), la introducción y el método, para ver dónde
se inserta la actualización de bajo rango y por qué no agrega latencia; la
[guía conceptual de LoRA](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora) de PEFT,
para fusionar y combinar adaptadores; y el abstract de [QLoRA](https://arxiv.org/abs/2305.14314)
para el truco de memoria. Fijarse en que LoRA no entrena menos capacidad sino menos parámetros, y
que lo paga aprendiendo menos y olvidando menos.
