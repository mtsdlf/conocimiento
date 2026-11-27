---
resumen: >-
  Los modelos que ofrecían los principales proveedores al 2026-11-27, con su identificador, ventana
  de contexto, salida máxima, corte de conocimiento y, donde la fuente lo da, precio y fecha de
  retiro; solo lo verificado en la página viva de cada proveedor.
estado: vigente
estabilidad: volatil
fuentes:
  - https://platform.claude.com/docs/en/models/overview
  - https://platform.claude.com/docs/en/build-with-claude/extended-thinking
  - https://developers.openai.com/api/docs/models
  - https://aistudio.google.com/docs/models
  - https://api-docs.deepseek.com/news/news260424
creado: 2026-11-27
revisado: 2026-11-27
---

# Modelos disponibles

Los modelos que ofrecían los principales proveedores al 2026-11-27, con su identificador, ventana
de contexto, salida máxima, corte de conocimiento y, donde la fuente lo da, precio y fecha de
retiro; solo lo verificado en la página viva de cada proveedor.

Implementa el [modelo base](modelo-base.md) del lado operativo: qué modelos hay para elegir. Cómo se
elige entre ellos está en [Benchmarks y elección de modelo](../Evaluacion/benchmarks-y-eleccion-de-modelo.md),
y dónde se los consume, en [Plataformas de IA](../Produccion/plataformas-de-ia.md). Copiado de las
fuentes enlazadas en cada tabla el 2026-11-27; antes de decidir, mirá la página viva.

## Qué mirar en cada fila

- **Ventana frente a salida máxima.** La [ventana de contexto](transformer.md#la-ventana-de-contexto)
  incluye la entrada; la salida máxima es mucho menor y limita respuestas largas y
  [razonamientos](razonamiento.md) largos.
- **Corte de conocimiento.** Lo posterior no lo sabe ([Preentrenamiento](preentrenamiento.md)); hay
  que dárselo en el contexto.
- **Fecha de retiro.** Anthropic la da como "Not sooner than": el identificador no se retira antes de
  esa fecha, y al migrar hay que volver a correr los [evals](../Evaluacion/evals.md).
- **Si piensa por defecto.** Cambia el costo y la latencia de cada llamada.

## Cerrados

Anthropic, desde [Models overview](https://platform.claude.com/docs/en/models/overview):

| Modelo | ID | Precio (USD por millón de tokens, entrada / salida) | Retiro no antes de |
|---|---|---|---|
| Claude Fable 5.2 | `claude-fable-5-2` | 8 / 40 | nov 2027 |
| Claude Opus 5.5 | `claude-opus-5-5` | 4 / 20 | sep 2027 |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | 2 / 10 | sep 2027 |
| Claude Haiku 5.5 | `claude-haiku-5-5` | desde 0,10 / 0,50 | oct 2027 |

Los cuatro tienen 1 M de tokens de ventana, 128 K de salida máxima, corte de conocimiento confiable
en junio de 2026 y pensamiento adaptativo: "Adaptive (always on)" en Fable 5.2 y Opus 5.5, "Adaptive"
en Sonnet 5.5 y Haiku 5.5. Claude Mythos 5.2 tiene disponibilidad limitada. Con el tokenizador actual,
"1M tokens is roughly 555k words or 2.5M Unicode characters [...]; models before it fit about 750k
words in 1M tokens": un caso de cómo el [tokenizador](token-y-embedding.md) cambia cuánto texto entra.

Control del razonamiento en la API de Anthropic, según
[Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking): "Extended
thinking is a legacy feature"; "Claude 4.7 and later models do not support it and reject requests
that use it, returning a 400 error". El presupuesto fijo (`thinking: {type: "enabled", budget_tokens:
N}`) se reemplaza por `thinking: {type: "adaptive"}` con `output_config: {effort: ...}`. Los tokens de
pensamiento se facturan como salida y se reportan en `usage.output_tokens_details.thinking_tokens`.

OpenAI, desde su [página de modelos](https://developers.openai.com/api/docs/models), leída a través del
resumen que devolvió la herramienta de lectura y no del texto crudo: GPT-6.2 Astra
(`gpt-6.2-astra`), GPT-6.2 Sol (`gpt-6.2-sol`), GPT-6.1 Terra (`gpt-6.1-terra`) y GPT-6 Luna
(`gpt-6-luna`). Ventana de 1,05 M de tokens y salida de hasta 128 K. La página da cortes de
conocimiento del 18 de mayo y del 1 de junio de 2026, sin que lo recuperado diga cuál corresponde a
cada modelo. Lo recuperado de la página no trae precios.

Google, desde su [página de modelos de Gemini](https://aistudio.google.com/docs/models), también por el
resumen de la herramienta de lectura: Gemini 4 en
cuatro variantes (Carbon, Neon, Hydrogen y Argon; IDs del tipo `gemini-4-carbon`), con 1 M de tokens
de entrada y estado no indicado. De la línea 3.x, Gemini 3.8 Flash y 3.6 Flash están estables y 3.1
Pro en preview. Sin precios en lo recuperado.

## Abiertos

DeepSeek, desde el [anuncio de V4](https://api-docs.deepseek.com/news/news260424) del 24 de abril de
2026, titulado "Preview Release" (leído por el resumen de la herramienta de lectura):

| Modelo | ID en la API | Parámetros totales | Activos por token | Ventana |
|---|---|---|---|---|
| DeepSeek-V4-Pro | `deepseek-v4-pro` | 1,6 T | 49 B | 1 M |
| DeepSeek-V4-Flash | `deepseek-v4-flash` | 284 B | 13 B | 1 M |

Los dos son [mixture of experts](transformer.md#mixture-of-experts-muchos-parámetros-pocos-por-token),
con pesos abiertos en Hugging Face. Los nombres viejos `deepseek-chat` y `deepseek-reasoner` se
retiraban después del 24 de julio de 2026. La página oficial no nombra la licencia, y no se encontró
si hubo una versión final posterior a la preview.

> [!NOTE]
> Sin fuente todavía: los modelos de Qwen (Alibaba) y de Meta solo aparecieron en resultados de
> buscador y prensa, sin abrir la fuente primaria; quedan afuera hasta verificarlos en Hugging Face o
> en el blog de cada uno. Mistral no se investigó. Faltan los precios de OpenAI y Google.
