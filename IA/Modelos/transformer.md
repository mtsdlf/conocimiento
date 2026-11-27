---
resumen: >-
  El transformer es la arquitectura de red sobre la que se construyen los LLM: en cada capa, cada
  token mira a los demás tokens de la ventana de contexto con un mecanismo de atención y decide
  cuánto pesa cada uno para predecir el próximo.
estado: borrador
estabilidad: estable
fuentes:
  - https://arxiv.org/abs/1706.03762
  - https://jalammar.github.io/illustrated-transformer/
  - https://arxiv.org/abs/2309.06180
  - https://arxiv.org/abs/2307.03172
  - https://arxiv.org/abs/1701.06538
  - https://arxiv.org/abs/2101.03961
  - https://arxiv.org/abs/2401.04088
  - https://web.stanford.edu/~jurafsky/slp3/
aliases: [Transformer, atención, attention, self-attention, autoatención, ventana de contexto, context window, KV cache, mixture of experts, MoE, mezcla de expertos]
creado: 2026-11-27
revisado:
---

# Transformer

El transformer es la arquitectura de red sobre la que se construyen los LLM: en cada capa, cada
token mira a los demás tokens de la ventana de contexto con un mecanismo de atención y decide
cuánto pesa cada uno para predecir el próximo.

Vaswani y otros (2017) la presentaron como una arquitectura "based solely on attention mechanisms,
dispensing with recurrence and convolutions entirely". Era un modelo de traducción: logró 28,4 BLEU
en inglés-alemán y 41,8 en inglés-francés (WMT 2014), y entrenaba mucho más rápido que las redes
recurrentes de la época, porque procesa todos los tokens de un texto en paralelo. Esa velocidad es lo
que permitió el [preentrenamiento](preentrenamiento.md) sobre corpus enormes. Qué reemplazó y cómo
siguió la historia está en [Historia de la IA generativa](../Fundamentos/historia-de-la-ia-generativa.md).

## Cómo decide la atención qué token importa

La atención resuelve el problema de que el significado de una palabra depende de las otras: en "el
banco estaba cerrado", "banco" se lee distinto si antes se habló de plata o de una plaza. Según *The
Illustrated Transformer* de Jay Alammar, funciona así:

1. Cada token, a partir de su [embedding](token-y-embedding.md), genera tres vectores: una
   **consulta** (qué busca), una **clave** (qué ofrece) y un **valor** (qué aporta).
2. La consulta de un token se compara con la clave de cada otro token por producto punto. Los
   puntajes se escalan y se pasan por softmax, que los vuelve pesos que suman uno.
3. El nuevo vector del token es la suma de los valores de todos, ponderada por esos pesos.

Varias **cabezas** de atención corren en paralelo, cada una con sus propias consultas, claves y
valores (ocho en el paper original), y pueden fijarse en relaciones distintas. Como la atención por sí
sola no sabe en qué orden vienen los tokens, se le suma a cada uno un vector de posición. Un modelo
apila muchas capas de atención, cada una seguida de un bloque que transforma cada token por
separado (el bloque *feed-forward*).

El transformer original tenía un codificador y un decodificador. BERT usa la parte codificadora; los
modelos generativos predicen de izquierda a derecha, como un decodificador
([Modelo base](modelo-base.md#codificadores-y-decodificadores)).

## La ventana de contexto

La ventana de contexto es la cantidad máxima de tokens que el modelo puede tener en cuenta en una
llamada: el prompt, todo lo que se le agregó y la respuesta que va generando. Lo que no entra en la
ventana no existe para el modelo. Los tamaños de cada modelo cambian seguido y están en la ficha de
[Modelos disponibles](modelos-disponibles.md).

Que algo entre en la ventana no quiere decir que el modelo lo use bien. Liu y otros ("Lost in the
Middle", 2023) encontraron que el rendimiento cae cuando la información relevante está en el medio de
una entrada larga, incluso en modelos de contexto largo (según su abstract). Qué poner en la ventana y
cómo se degrada con contextos largos es el tema de [Ingeniería de contexto](../Contexto/ingenieria-de-contexto.md).

> [!NOTE]
> Sin fuente todavía: que el costo de la atención crece con el cuadrado del largo del contexto. Es una
> afirmación corriente del campo que no se verificó en las fuentes leídas.

## Por qué generar reutiliza la KV cache

El modelo genera un token por vez, y cada token nuevo necesita las claves y los valores de todos los
anteriores. En lugar de recalcularlos en cada paso, se guardan en memoria: eso es la **KV cache**
(*key-value cache*). Kwon y otros (2023), los autores de vLLM, la describen así: "the key-value cache
(KV cache) memory for each request is huge and grows and shrinks dynamically". Esa memoria, y no solo
el cómputo, es lo que hace caro atender muchos pedidos con contextos largos.

Lectura de esta base: el *prompt caching* de los proveedores guarda el estado de un comienzo de
prompt repetido para no procesarlo de nuevo, y por eso un prefijo largo y fijo sale más barato
([Cache de modelos](../Produccion/cache-de-modelos.md)). Cómo se administra la KV cache al servir un
modelo (PagedAttention, lotes) está en [Inferencia](../Produccion/inferencia.md).

## Mixture of experts: muchos parámetros, pocos por token

En un transformer denso, cada token pasa por todos los parámetros: duplicar el modelo duplica el
cómputo de cada respuesta. Una capa **mixture of experts** (MoE) reemplaza el bloque *feed-forward* por
varios bloques paralelos, los **expertos**, y agrega un **router** entrenable que mira cada token y
elige cuáles lo procesan. Los demás expertos no se calculan para ese token. La idea de la activación
dispersa viene de Shazeer y otros (2017), que la llamaron *sparsely-gated*.

| Modelo | Expertos por token | Qué reporta |
|---|---|---|
| Switch Transformer (Fedus y otros, 2021) | Uno solo, para simplificar el router | Hasta 7 veces menos tiempo de preentrenamiento con el mismo cómputo que T5-Base y T5-Large; modelos de un billón de parámetros con 4 veces de aceleración sobre T5-XXL |
| Mixtral 8x7B (Jiang y otros, 2024) | Dos de ocho por capa | 47 mil millones de parámetros en total y 13 mil millones activos por token (alrededor del 28 %); según su abstract, "matches or outperforms Llama 2 70B and GPT-3.5" en los benchmarks evaluados; licencia Apache 2.0 |

Lectura de esta base: los 47 mil millones de Mixtral no son 8 × 7 = 56 porque solo se multiplican los
bloques de expertos, y la atención es compartida. Los modelos abiertos grandes de la ficha de
[Modelos disponibles](modelos-disponibles.md) también son MoE, con sus parámetros totales y activos.

Lectura de esta base sobre lo que MoE no resuelve: todos los expertos tienen que estar cargados en
memoria aunque cada token use pocos, así que el costo de servir no baja en la misma proporción que el
cómputo. Tampoco es un ensamble (varios modelos completos que votan) ni un sistema de
[agentes](../Agentes/agente.md) especializados: los expertos no tienen especialidades con nombre, y lo
que aprende cada uno sale del entrenamiento.

## Qué leer sobre el transformer

Vaswani y otros, [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762), secciones 3.1 a 3.3
(arquitectura, atención y atención multicabeza), leído junto a
[*The Illustrated Transformer*](https://jalammar.github.io/illustrated-transformer/) para tener el
dibujo. Para MoE, los abstracts de [Switch Transformers](https://arxiv.org/abs/2101.03961) y
[Mixtral](https://arxiv.org/abs/2401.04088). Jurafsky y Martin, capítulo 7 ("Transformers and
Pretraining") de [*Speech and Language Processing*](https://web.stanford.edu/~jurafsky/slp3/), da la
versión de libro de texto (se leyó solo el índice).
