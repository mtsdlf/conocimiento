---
resumen: >-
  Con un modelo de lenguaje adentro, el costo por consulta y la latencia pasan a ser características
  de primera: el costo crece con las consultas y los tokens de entrada y salida, y la latencia se
  parte en el tiempo hasta el primer token (TTFT) y el tiempo por token de salida (TPOT).
estado: vigente
estabilidad: semi
fuentes:
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://thenewstack.io/pg-99-conf-2026-inference-costs/
aliases: [TTFT, TPOT, time to first token, time per output token, costo por consulta, latencia de inferencia]
creado: 2026-11-27
revisado: 2026-11-27
---

# Costo y latencia

Con un modelo de lenguaje adentro, el costo por consulta y la latencia pasan a ser características
de primera: el costo crece con las consultas y los tokens de entrada y salida, y la latencia se
parte en el tiempo hasta el primer token (TTFT) y el tiempo por token de salida (TPOT).

## Por qué un modelo los sube al frente

La explicación es de esta base. En un servicio sin modelos, el costo de una consulta más es casi cero y la latencia depende de la
base de datos y la red. Un [modelo de lenguaje](../../IA/Modelos/modelo-base.md) genera la respuesta token por token
y se paga por los tokens que lee y escribe, así que cada consulta tiene un costo propio y una
latencia que crece con el largo de la respuesta. Richards y Ford tratan el rendimiento como una
[característica](caracteristicas-arquitectonicas.md) más; esta nota es la aplicación de Huyen, que
mide las dos como métricas propias.

## TTFT y TPOT

Huyen separa la latencia en dos métricas:

- **TTFT** (time to first token): "The time it takes for the first token to be generated". Es lo
  que el usuario espera antes de ver algo.
- **TPOT** (time per output token): "The time it takes to generate each output token". Es la
  velocidad a la que se va escribiendo la respuesta.

De las dos definiciones se deduce (cuenta de esta base) que la latencia total de una respuesta es, aproximadamente, el
TTFT más el TPOT por la cantidad de tokens de salida. Una respuesta larga con buen TTFT puede
tardar mucho igual; acortar la salida baja latencia y costo a la vez. Según un resumen secundario
de una charla de Huyen, en los modelos de razonamiento "The first generated token might not be the
same as the first visible token": el modelo genera tokens que el usuario no ve antes de empezar a
responder.

## Costo por consulta

Para el costo, Huyen mide "the number of queries and the volume of input and output tokens", y
agrega que "Length-related metrics are also important for tracking latency and costs". El costo por
consulta sale de esas tres cantidades y del precio de cada token del modelo elegido. Los precios
cambian seguido y viven en la ficha de [plataformas de IA](../../IA/Produccion/plataformas-de-ia.md),
no acá.

## Las piezas que los controlan

Cada pieza de la arquitectura de Huyen mueve alguna de las dos. Las dos últimas filas son lectura de esta base:

| Pieza | Qué mueve |
|---|---|
| [Router y gateway](../../IA/Produccion/router-y-gateway-de-modelos.md) | El router manda las consultas simples a modelos más baratos; el gateway concentra el control de costo ("A model gateway is access control and cost management") |
| [Cache de modelos](../../IA/Produccion/cache-de-modelos.md) | Huyen la agrega en el paso "Reduce Latency with Cache" (prompt, exacta y semántica) |
| [Contexto y RAG](../../IA/Contexto/contexto-y-rag.md) | Cada fragmento de contexto que se agrega suma tokens de entrada |
| [Agente](../../IA/Agentes/agente.md) | Cada paso es otra llamada al modelo: multiplica costo y latencia |

Según el mismo resumen de la charla, al comparar servicios de inferencia se miran costo, latencia y
calidad juntos. Bajar costo con un modelo más chico solo vale si la
[evaluación](../../IA/Evaluacion/evals.md) muestra que la calidad aguanta, y la
[observabilidad](../../IA/Produccion/observabilidad-de-modelos.md) es la que registra los tres en
producción.

## Qué leer

El post de Huyen "Building A Generative AI Platform" (2024), sección Observability, define las
métricas y es de acceso libre. El canónico declarado es el capítulo 9 de *AI Engineering*,
"Inference Optimization".

> [!NOTE] Sin fuente todavía: el contenido del capítulo 9 de *AI Engineering* (no se pudo leer) y
> valores de referencia de TTFT o TPOT aceptables para una interfaz de chat.
