---
resumen: >-
  Producción es operar un sistema con un modelo adentro: las capas que se suman alrededor del
  modelo (guardrails, router y gateway, cache), el servicio de inferencia que lo corre y la
  observabilidad que registra qué le pasó a cada consulta.
estado: vigente
estabilidad: estable
fuentes:
  - https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices
aliases: [producción, operar un sistema con modelos, LLMOps, AI engineering in production, infraestructura de IA]
creado: 2026-11-27
revisado: 2026-11-27
---

# Producción

Producción es operar un sistema con un modelo adentro: las capas que se suman alrededor del
modelo (guardrails, router y gateway, cache), el servicio de inferencia que lo corre y la
observabilidad que registra qué le pasó a cada consulta.

Es la tercera de las capas del oficio que distingue Huyen, la infraestructura ("model serving,
managing data and compute, and monitoring"), como se cuenta en [IA](../ia.md). Recibe de
[Contexto](../Contexto/contexto.md) y de [Agentes](../Agentes/agentes.md) las dos capas que llenan
la ventana y actúan, y de [Evaluación](../Evaluacion/evaluacion.md) la decisión de qué capa sumar.
Le devuelve a Evaluación las trazas de lo que pasó con usuarios reales, que son el insumo del
[análisis de errores](../Evaluacion/analisis-de-errores.md). La arquitectura general sobre la que
se monta (gateways, degradación, idempotencia) está en [Arquitectura](../../Arquitectura/arquitectura.md).

## Una capa por vez, y solo si la medición la pide

La versión mínima de un sistema con modelos es una consulta que va al modelo y una respuesta que
vuelve. Huyen parte de ahí y suma una capa por vez, cada una para un problema que la anterior deja:
contexto, guardrails, router y gateway, cache, lógica y acciones, más la observabilidad y la
orquestación como piezas transversales. Su regla: "a component can be skipped if your system works
well without it". La tabla de capas, el orden y un flujo posible están en
[Sistemas con modelos](sistemas-con-modelos.md).

El resumen del capítulo agrega el precio: "Each additional component can potentially make your
system more capable, safer, or faster, but will also increase the system's complexity, exposing it
to new failure modes". Cada capa de esta vertical tiene una
falla propia que la anterior no tenía:

| Capa | Qué resuelve | Cómo falla |
|---|---|---|
| [Guardrails](guardrails.md) | Entradas y salidas dañinas o incorrectas, acciones peligrosas | Bloquea pedidos legítimos y suma latencia; contra la inyección de prompt no se conoce una defensa completa |
| [Router](router-y-gateway-de-modelos.md) | Mandar cada consulta al modelo más barato que la resuelve | Manda una consulta difícil al modelo barato y nadie lo nota |
| [Gateway](router-y-gateway-de-modelos.md) | Acceso, claves, presupuesto y fallback en un solo lugar | Es un punto único por el que pasa todo |
| [Cache semántica](cache-de-modelos.md) | Consultas parecidas que se repiten | Devuelve con seguridad la respuesta de otra pregunta |
| [Observabilidad](observabilidad-de-modelos.md) | Saber qué pasó en cada consulta | Registrar todo guarda también los datos personales |

Las fallas de la tabla salen de cada nota; juntarlas así es lectura de esta base, igual que la del
gateway como punto único.

## Costo y latencia, los dos números que mueve todo

Con un modelo adentro, el [costo y la latencia](../../Arquitectura/Caracteristicas/costo-y-latencia.md)
pasan a ser características de primera, y casi todo en esta vertical existe para moverlos. El
router manda lo simple a un modelo barato; la cache evita pagar dos veces lo mismo; la
[inferencia](inferencia.md) decide cuánto tarda y cuánto cuesta cada token. Los guardrails y la
observabilidad van en sentido contrario: suman tiempo y gasto a cambio de seguridad y de poder ver.

Lo central de la inferencia es que generar texto está limitado por la memoria y no por el cálculo:
para cada token nuevo, el acelerador vuelve a leer todos los pesos del modelo. De ahí salen las
optimizaciones (cuantizar, decodificar especulativamente, agrupar pedidos) y el canje que ofrecen
los proveedores con las APIs de batch, menos precio a cambio de esperar.

## Diseñar para cuando el modelo se equivoca

La idea que ordena el tema, que un modelo genera texto probable y no verdadero (lectura de esta
base, como en [IA](../ia.md)), en producción se vuelve una regla de diseño: el sistema tiene que
aguantar que el modelo se equivoque o sea engañado. Para la seguridad, la evidencia de que no hay
una defensa completa contra la inyección está en
[Inyección de prompt](../Contexto/inyeccion-de-prompt.md), y la misma lógica vale para la cache semántica o el router: cada capa que decide sola necesita
[evals](../Evaluacion/evals.md) que la midan y una traza que muestre cuándo falló (lectura de esta
base). Por eso la observabilidad no es una capa más sino la que cierra el bucle con Evaluación.

## Qué hay adentro de Producción

- [Sistemas con modelos](sistemas-con-modelos.md) — las capas que se suman alrededor del modelo, en
  qué orden y con qué criterio; se lee primero.
- [Guardrails](guardrails.md) — controles sobre la entrada, la salida y las acciones, el Top 10 de
  OWASP 2026 y lo que cuesta cada capa.
- [Router y gateway de modelos](router-y-gateway-de-modelos.md) — qué modelo atiende cada consulta
  y cómo se centraliza el acceso, el costo y el fallback.
- [Cache de modelos](cache-de-modelos.md) — prompt cache, cache exacta y cache semántica, y por qué
  la semántica puede devolver una respuesta equivocada.
- [Inferencia](inferencia.md) — prefill y decode, las métricas del servidor y las optimizaciones del
  modelo y del servicio.
- [Observabilidad](observabilidad-de-modelos.md) — métricas, logs y trazas de cada consulta, y el
  vocabulario común de OpenTelemetry.
- [Plataformas de IA](plataformas-de-ia.md) — ficha fechada: gateways, vector stores, orquestación
  y observabilidad, el prompt cache y el finetuning por proveedor.
- [Herramientas de guardrails](herramientas-de-guardrails.md) — ficha fechada: clasificadores,
  frameworks y APIs de moderación, con cifras de latencia.
- [APIs de batch y motores de inferencia](apis-de-batch-y-motores-de-inferencia.md) — ficha fechada:
  descuentos y límites del batch por proveedor y lo que soporta un motor de código abierto.
