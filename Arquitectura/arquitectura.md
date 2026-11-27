---
resumen: >-
  La arquitectura de software son las decisiones de estructura que cuestan caro cambiar: qué
  características tiene que cumplir el sistema, cómo se parte en módulos, con qué estilo se
  arma y cómo se verifica que sigue funcionando, también cuando una de sus piezas es un modelo
  de IA que no responde siempre lo mismo.
estado: vigente
estabilidad: semi
fuentes:
  - https://nealford.com/books/SAF2e.html
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
aliases: [arquitectura de software, software architecture]
creado: 2026-10-03
revisado: 2026-11-27
---

# Arquitectura

La arquitectura de software son las decisiones de estructura que cuestan caro cambiar: qué
características tiene que cumplir el sistema, cómo se parte en módulos, con qué estilo se arma y
cómo se verifica que sigue funcionando, también cuando una de sus piezas es un modelo de IA que no
responde siempre lo mismo.

La definición de "cuestan caro cambiar" es de trabajo de esta base. El tema se escribe desde dos referencias que se complementan. Richards y Ford (*Fundamentals of
Software Architecture*, 2ª ed., 2025) ordenan el canon: características, modularidad, estilos y
decisiones. Chip Huyen (*AI Engineering*, 2025) agrega lo que el canon no tenía: un sistema con un
modelo adentro se arma de a una pieza por vez, y la evaluación decide cuándo hace falta la
siguiente. Según Huyen, "a component can be skipped if your system works well without it". El cruce
entre los dos índices es de esta base: ninguna de las dos fuentes lo hace.

Cómo se construye un sistema con un modelo de IA adentro (el modelo, su contexto, los agentes, la
evaluación y la operación en producción) está en [IA](../IA/ia.md); este tema da la base de
arquitectura sobre la que se monta. Las herramientas de quien escribe el código están en
[Desarrollo](../Desarrollo/desarrollo.md), y cómo una plataforma interna expone sus capacidades, en
[Platform Engineering](../Platform-Engineering/platform-engineering.md).

## De qué está hecha una arquitectura

Las características dicen qué tiene que cumplir el sistema; la modularidad y el estilo dicen cómo se
arma para cumplirlo, las fitness functions miden si lo cumple, y las decisiones dejan escrito por
qué se eligió cada cosa. Cuando una pieza es un modelo, su arquitectura propia (contexto, router,
cache, agente) y su evaluación viven en [IA](../IA/ia.md) y se montan sobre esta base.

```mermaid
flowchart LR
  C[Características] -->|priorizan| E[Estilos]
  M[Modularidad] -->|delimita las piezas de| E
  E -->|se distribuye con| D[Sistemas distribuidos]
  M -->|aísla detrás de una interfaz| IA[Sistemas con modelos, en IA]
  DE[Decisiones] -->|registran y revisan| E
  C -->|se miden y dan evidencia a| DE
```

- [Características](Caracteristicas/caracteristicas.md) — las "-ilities" que el sistema tiene que
  cumplir, cómo se eligen y cómo se miden; con un modelo adentro, el costo por consulta y la latencia
  pasan al frente.
- [Modularidad](Modularidad/modularidad.md) — dónde se pone un límite entre piezas y por qué el
  modelo va detrás de una interfaz propia.
- [Estilos](Estilos/estilos.md) — las formas de armar el sistema (monolito modular, capas, eventos,
  servicios, microservicios) y cómo se elige entre ellas.
- [Sistemas distribuidos](Sistemas-distribuidos/sistemas-distribuidos.md) — los patrones para cuando
  el sistema se reparte entre servicios que se llaman por la red: fallas, consistencia y bordes.
- [Decisiones](Decisiones/decisiones.md) — cómo se decide, se registra y se dibuja una arquitectura,
  empezando por lo más simple.
- [Fundamentos](Fundamentos/fundamentos-de-arquitectura.md) — las escuelas, lo que pierde peso y por
  qué, y la bibliografía.

## Empezar simple y medir antes de sumar

La idea que ordena el tema es de esta base, apoyada en Huyen y en Anthropic: cada pieza tiene un costo y entra
cuando hay evidencia de que hace falta. En estilos, una forma es partir de un
[monolito modular](Estilos/monolito-modular.md) y no de microservicios (postura de Fowler, disputada). En un sistema con modelos, es
arrancar con el prompt y sumar contexto, fine-tuning o un agente según la falla que muestre la evaluación
([Prompt, RAG o fine-tuning](../IA/prompt-rag-o-finetuning.md) explica ese diagnóstico);
Huyen cuenta entre los errores comunes "use an agentic framework when direct API calls work". Lo que
decide si una pieza entra es la [evaluación](../IA/Evaluacion/evals.md), y la regla
completa está en [Empezar simple](Decisiones/empezar-simple.md).

## Lo que cambia cuando una pieza no es determinista

Una prueba unitaria fija qué tiene que devolver una función. Con un modelo, la misma entrada puede dar
salidas distintas, y "correcto" pasa a ser una proporción sobre un conjunto de casos. Por eso la
evaluación ocupa dos capítulos del libro de Huyen antes de prompting, RAG y fine-tuning, y por eso en
[IA](../IA/ia.md) tiene vertical propia. Tres cosas del canon ganan peso con eso: medir características con
números ([fitness function](Caracteristicas/fitness-function.md)), aislar la pieza incierta detrás de
una interfaz ([aislar lo no determinista](Modularidad/aislar-lo-no-determinista.md)) y registrar por
qué se eligió cada modelo y cada umbral ([ADR](Decisiones/adr.md)).

## Catálogo de patrones

Cada patrón vive en la vertical de su problema; esta tabla los junta.

| Problema | Patrón | Nota |
|---|---|---|
| Una dependencia viene fallando y arrastra al resto | Circuit breaker | [Circuit breaker](Sistemas-distribuidos/circuit-breaker.md) |
| Qué responder cuando una dependencia no contesta | Degradación controlada | [Degradación controlada](Sistemas-distribuidos/degradacion-controlada.md) |
| Una operación toca varios servicios con base propia | Saga | [Saga](Sistemas-distribuidos/saga.md) |
| Un reintento no debe repetir el efecto | Clave de idempotencia | [Clave de idempotencia](Sistemas-distribuidos/clave-de-idempotencia.md) |
| Guardar un cambio y publicar su evento sin perder ninguno | Outbox | [Outbox](Sistemas-distribuidos/outbox.md) |
| Lecturas y escrituras con necesidades muy distintas | CQRS | [CQRS](Sistemas-distribuidos/cqrs.md) |
| Varios clientes (web, móvil) frente a muchos servicios | API gateway y BFF | [API gateway y BFF](Sistemas-distribuidos/api-gateway-y-bff.md) |
| En qué capa va cada API | API-led connectivity | [API-led connectivity](Sistemas-distribuidos/api-led-connectivity.md) |
| Varios clientes en una instancia sin mezclar datos | Multi-tenancy | [Multi-tenancy](Sistemas-distribuidos/multi-tenancy.md) |
| Reemplazar un sistema viejo sin apagarlo | Strangler fig | [Strangler fig](Estilos/strangler-fig.md) |
| El modelo no sabe lo que necesita para responder | RAG | [Contexto y RAG](../IA/Contexto/contexto-y-rag.md) |
| Cada consulta necesita un modelo distinto, o hay que centralizar el acceso | Router y gateway | [Router y gateway de modelos](../IA/Produccion/router-y-gateway-de-modelos.md) |
| Consultas repetidas cuestan y tardan | Cache de modelos | [Cache de modelos](../IA/Produccion/cache-de-modelos.md) |
| La salida del modelo puede ser incorrecta o dañina | Guardrails | [Guardrails de LLM](../IA/Produccion/guardrails.md) |
| La tarea pide varios pasos y herramientas | Agente | [Agente](../IA/Agentes/agente.md) |
| Evaluar a escala sin personas | IA como juez | [IA como juez](../IA/Evaluacion/ia-como-juez.md) |

## Qué leer según lo que estés construyendo

- Si arrancás un producto con un LLM adentro: [Sistemas con modelos](../IA/Produccion/sistemas-con-modelos.md),
  [Empezar simple](Decisiones/empezar-simple.md), [Aislar lo no determinista](Modularidad/aislar-lo-no-determinista.md),
  [Evaluación](../IA/Evaluacion/evals.md) y, desde el primer día, los registros de
  [Observabilidad de modelos](../IA/Produccion/observabilidad-de-modelos.md).
- Si el sistema además actúa (abre un ticket, manda un mail, cobra): [Agente](../IA/Agentes/agente.md),
  que explica cuándo alcanza un workflow fijo, y [Clave de idempotencia](Sistemas-distribuidos/clave-de-idempotencia.md),
  para que un reintento no repita la acción.
- Si tenés que elegir cómo armar un sistema nuevo: [Características arquitectónicas](Caracteristicas/caracteristicas-arquitectonicas.md),
  [Elegir un estilo](Estilos/elegir-un-estilo.md) y [Monolito modular](Estilos/monolito-modular.md).
- Si dudás entre monolito y microservicios: [Monolito modular](Estilos/monolito-modular.md),
  [Microservicios](Estilos/microservicios.md) y, en [Lo que pierde peso](Fundamentos/lo-que-pierde-peso.md),
  la disputa sobre microservicios por defecto.
- Si tenés que probar algo cuya salida cambia: [Evaluación](../IA/Evaluacion/evals.md),
  [Análisis de errores](../IA/Evaluacion/analisis-de-errores.md) e [IA como juez](../IA/Evaluacion/ia-como-juez.md).
- Si dudás entre mejorar el prompt, sumar RAG o hacer fine-tuning: [Prompt, RAG o fine-tuning](../IA/prompt-rag-o-finetuning.md).
- Si tenés que dejar escrita una decisión: [ADR](Decisiones/adr.md) y [Diagramas](Decisiones/diagramas.md).
- Si migrás un sistema viejo: [Strangler fig](Estilos/strangler-fig.md).
- Si un servicio llama a otros por la red: [Sistemas distribuidos](Sistemas-distribuidos/sistemas-distribuidos.md).
- Si querés saber qué no conviene estudiar primero: [Lo que pierde peso](Fundamentos/lo-que-pierde-peso.md).

## Del canon al sistema con modelos

Para aprender el tema, leé en este orden: [Características](Caracteristicas/caracteristicas.md),
[Modularidad](Modularidad/modularidad.md), [Estilos](Estilos/estilos.md) y
[Decisiones](Decisiones/decisiones.md) dan el canon. Después, si el sistema tiene un modelo adentro, el tema
[IA](../IA/ia.md), empezando por su [evaluación](../IA/Evaluacion/evaluacion.md), porque cada
pieza alrededor del modelo se justifica con una medición. [Sistemas distribuidos](Sistemas-distribuidos/sistemas-distribuidos.md)
se lee cuando el sistema se reparte entre servicios.
