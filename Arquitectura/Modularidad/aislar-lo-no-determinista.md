---
resumen: >-
  Aislar lo no determinista es poner el modelo de IA detrás de una interfaz propia y chica, para
  que el resto del sistema no dependa de un proveedor, de un modelo ni de salidas que cambian, y
  para poder cambiarlo, probarlo y medirlo en un solo lugar.
estado: borrador
estabilidad: semi
fuentes:
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://martinfowler.com/articles/gen-ai-patterns/
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://medium.com/@nakabonne/depth-of-module-f62dac3c2fdb
aliases: [aislar el modelo, interfaz del modelo, adaptador del modelo]
creado: 2026-11-27
revisado:
---

# Aislar lo no determinista

Aislar lo no determinista es poner el modelo de IA detrás de una interfaz propia y chica, para
que el resto del sistema no dependa de un proveedor, de un modelo ni de salidas que cambian, y
para poder cambiarlo, probarlo y medirlo en un solo lugar.

No es un concepto del canon: Richards y Ford no lo tratan, y ninguna fuente lo nombra como
principio. Es la aplicación de la [modularidad](modularidad.md) a la pieza más incierta del
sistema, armada con lo que dicen Huyen, el artículo de patrones de IA generativa del sitio de
Martin Fowler y Anthropic.

## Por qué un modelo pide su propio límite

Un [modelo de lenguaje](../../IA/llm.md) rompe dos supuestos del resto del código. El primero es el
determinismo: "With LLM-based systems, we encounter a system that no longer behaves
deterministically", y "Such a system will provide different outputs to the same inputs on repeated
requests" (Subramaniam, en el sitio de Fowler). El segundo es la estabilidad: el proveedor puede cambiar el
modelo o su API, y a veces se cae. Si cada parte del sistema llama al modelo por su
cuenta, cada uno de esos cambios se reparte por todo el código. Con un solo punto de entrada, se
arregla en un lugar.

## Lo que gana la interfaz propia

Huyen describe esa interfaz a escala de organización como el gateway de modelos: "A model gateway
is an intermediate layer that allows your organization to interface with different models". La
ganancia que nombra es la de cualquier buen módulo: "If a model API changes, you only need to update
the model gateway". Cuando un modelo se cae, el gateway "can route requests to alternative models".
El detalle de esa pieza está en
[router y gateway de modelos](../Sistemas-con-modelos/router-y-gateway-de-modelos.md).

Detrás de la misma interfaz quedan las piezas que tratan la salida incierta. Que vivan juntas ahí es
lectura de esta base: las fuentes tratan cada una por separado.


- **Los guardrails**, que filtran lo que entra al modelo y validan lo que emite antes de que llegue al resto. Según el mismo
  artículo, "Guardrails act to shield the LLM", y "guardrails don't come for free". Las capas están
  en [guardrails de LLM](../../IA/guardrails.md).
- **La evaluación**, que necesita un punto único donde mirar entradas y salidas. El artículo
  propone tratar los evals "similarly to how we work with performance testing", con umbrales en
  lugar de pasa o no pasa; ver [evaluación](../Evaluacion-y-observabilidad/evaluacion.md) y
  [fitness function](../Caracteristicas/fitness-function.md).
- **El costo y la latencia**, que se miden y se controlan donde pasan todas las llamadas; ver
  [costo y latencia](../Caracteristicas/costo-y-latencia.md).

Para los agentes, Anthropic pide cuidar la interfaz entre el modelo y sus herramientas como una
interfaz más: "Carefully craft your agent-computer interface (ACI) through thorough tool
documentation and testing", y "Tool definitions and specifications should be given just as much
prompt engineering attention as your overall prompts". Ver [agente](../Sistemas-con-modelos/agente.md).

## Interfaz chica, no abstracción opaca

Las mismas fuentes que piden una capa advierten contra las capas que esconden demasiado. Huyen
cuenta entre los errores comunes usar frameworks que "Abstract away critical details, making it
hard to understand and debug your system", y aconseja sobre los orquestadores "start building your
application without one first". Anthropic dice que los frameworks "often create extra layers of
abstraction that can obscure the underlying prompts and responses".

Las dos cosas se concilian, y la conciliación es inferencia de esta base: lo que conviene aislar es
el acceso al modelo, con una interfaz propia, chica y transparente; lo que conviene evitar es
delegar en un framework ajeno el prompt y la respuesta, que son justo lo que hay que poder leer
para depurar. La interfaz decide qué no ve el resto del sistema; no tiene que impedir que quien
depura vea el prompt exacto y la salida exacta.

> [!IMPORTANT] Hay una tensión con los [módulos profundos](modularidad.md#módulos-profundos): un
> crítico de Ousterhout sostiene que las clases profundas son más difíciles de testear (según su
> resumen). Con un modelo detrás, eso pesa: la interfaz chica tiene que dejar pasar lo necesario
> para evaluar (el prompt armado, la salida cruda, el modelo usado) aunque el resto del sistema no
> lo use.

## Qué leer

Huyen, "Building A Generative AI Platform" (2024), la sección del gateway, que es la única fuente
con la interfaz reemplazable dicha en sus palabras. Fijarse en lo que logra: cambiar de modelo,
fallback y control de costo. Para cómo se prueba lo que queda detrás, la sección de evals de
"Emerging Patterns in Building GenAI Products" (2025), en el sitio de Fowler.

> [!NOTE] Sin fuente todavía: un recurso que formule "aislar el modelo detrás de una interfaz
> propia" como principio. Puede ser un hueco del campo o del artículo de Fowler, que no se leyó
> completo.
