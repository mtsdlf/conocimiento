---
resumen: >-
  Descuento, ventana y límites de las APIs de batch de los proveedores, y las técnicas que soporta
  un motor de inferencia de código abierto, copiados el 2026-11-27.
estado: vigente
estabilidad: volatil
fuentes:
  - https://platform.claude.com/docs/en/build-with-claude/batch-processing
  - https://developers.openai.com/api/docs/guides/batch
  - https://docs.vllm.ai/en/latest/
aliases: [batch API, Message Batches, vLLM, motor de inferencia, inference engine]
creado: 2026-11-27
revisado: 2026-11-27
---

# APIs de batch y motores de inferencia

Descuento, ventana y límites de las APIs de batch de los proveedores, y las técnicas que soporta
un motor de inferencia de código abierto, copiados el 2026-11-27.

Implementa el batch y las optimizaciones del servicio de [Inferencia](inferencia.md). La fuente
viva de cada fila es la documentación enlazada.

## APIs de batch por proveedor

Copiado de las dos documentaciones el 2026-11-27.

| | Anthropic (Message Batches) | OpenAI (Batch API) | Google |
|---|---|---|---|
| Descuento | "cutting costs by 50 percent" | "50% cost discount compared to synchronous APIs" | no se leyó |
| Ventana | "most batches finishing in less than 1 hour"; vence si no termina en 24 horas | "Each batch completes within 24 hours" | — |
| Límite por lote | 100.000 pedidos o 256 MB | 50.000 pedidos y 200 MB por archivo | — |
| Prompt cache | se combina, con descuentos que se acumulan; recomienda la cache de 1 hora; aciertos "ranging from 30 percent to 98 percent" | la página no lo dice | — |
| Fuente | [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) | [batch](https://developers.openai.com/api/docs/guides/batch) | — |

## vLLM, un motor de inferencia de código abierto

Según la portada de su [documentación](https://docs.vllm.ai/en/latest/) (pie de página del
2026-11-06), vLLM soporta:

- cuantización FP8, INT8, INT4, GPTQ/AWQ y GGUF;
- decodificación especulativa con los métodos n-gram, suffix, EAGLE y DFlash (no se leyeron);
- "Disaggregated serving: separate prefill, decode, and encode stages";
- prefix caching, el equivalente autoalojado del prompt cache;
- PagedAttention, que nació con el mismo proyecto ([paper](https://arxiv.org/abs/2309.06180)).

> [!NOTE]
> Sin fuente todavía: la API de batch de Google, la versión estable de vLLM y la documentación de
> cada técnica en detalle.
