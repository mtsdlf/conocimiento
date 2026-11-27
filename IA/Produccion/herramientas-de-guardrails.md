---
resumen: >-
  Clasificadores, frameworks y APIs de moderación para implementar guardrails, con lo que dice cada
  fuente y las cifras de latencia publicadas, copiados el 2026-11-27.
estado: borrador
estabilidad: volatil
fuentes:
  - https://arxiv.org/abs/2312.06674
  - https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama-guard-4/
  - https://arxiv.org/abs/2310.10501
  - https://docs.nvidia.com/nemo/guardrails/latest/index.html
  - https://github.com/guardrails-ai/guardrails
  - https://developers.openai.com/api/docs/guides/moderation
  - https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
  - https://arxiv.org/abs/2504.00441
  - https://developer.nvidia.com/blog/measuring-the-effectiveness-and-performance-of-ai-guardrails-in-generative-ai-applications/
aliases: [guardrail tools, Llama Guard, NeMo Guardrails, Guardrails AI, moderation API]
creado: 2026-11-27
revisado:
---

# Herramientas de guardrails

Clasificadores, frameworks y APIs de moderación para implementar guardrails, con lo que dice cada
fuente y las cifras de latencia publicadas, copiados el 2026-11-27.

Implementa las capas de clasificador y de validación de [Guardrails](guardrails.md). Son ejemplos,
no un ranking; la fuente viva de cada uno es su documentación. Las filas marcadas **[buscador]**
salen de resultados de buscador sin abrir la fuente: hay que verificarlas antes de decidir.

| Herramienta | Qué es | Fuente viva | Cómo se obtuvo |
|---|---|---|---|
| Llama Guard (Meta) | Modelo que clasifica prompts y respuestas con una taxonomía de riesgos que se puede personalizar. La primera versión (dic. 2023) partía de Llama2-7b y, según su abstract, "matches or exceeds existing content moderation tools" en OpenAI Moderation Evaluation y ToxicChat. Llama Guard 4 (12B) sigue la taxonomía de peligros de MLCommons (S1 a S13) y suma S14, Code Interpreter Abuse | [paper](https://arxiv.org/abs/2312.06674), [tarjeta de Llama Guard 4](https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama-guard-4/) | abstract; la versión 4, **[buscador]** |
| NeMo Guardrails (NVIDIA) | "Open-source toolkit" con un runtime inspirado en la gestión de diálogo; los rails los define el usuario y no dependen del modelo. La documentación lista "Latest" y versiones v0.22.0 a v0.25.0, sin fecha de release | [documentación](https://docs.nvidia.com/nemo/guardrails/latest/index.html), [paper](https://arxiv.org/abs/2310.10501) | portada de la documentación y abstract |
| Guardrails AI | "A Python framework that helps build reliable AI applications": corre guards de entrada y salida con validadores y genera datos estructurados; Apache-2.0. Un aviso del 2026-07-06 dice que los validadores pasan a paquetes estándar de PyPI y que la inferencia remota alojada se discontinúa, con corte previsto el 2026-08-25 | [repositorio](https://github.com/guardrails-ai/guardrails) | portada del repositorio |
| Moderación de OpenAI | Modelo `omni-moderation-latest`, endpoint "free to use", texto e imagen, sin audio. Categorías solo de texto: `harassment`, `harassment/threatening`, `hate`, `hate/threatening`, `illicit`, `illicit/violent`, `sexual/minors`; de texto e imagen: `self-harm` (y `/intent`, `/instructions`), `sexual`, `violence`, `violence/graphic` | [guía de moderación](https://developers.openai.com/api/docs/guides/moderation) | documentación leída |
| Patrón de Anthropic | No es un producto: un modelo chico como pre-filtro con salida estructurada; si el clasificador mismo se niega ("stop_reason: refusal"), se trata como veredicto dañino | [guía de jailbreaks](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) | documentación leída |

## Cifras de latencia publicadas

Todas dependen de la configuración y ninguna es un valor general.

| Qué se midió | Cifra | Fuente | Cómo se obtuvo |
|---|---|---|---|
| Llama Guard, NeMo Guardrails y un clasificador tipo BERT, en la prueba de "No Free Lunch" | 1,5 s, 1,0 s y 0,08 s de promedio | [Kumar et al.](https://arxiv.org/abs/2504.00441) (los autores compiten con un guardrail propio) | **[buscador]**, no verificado en el paper |
| Sumar la primera capa de NeMo Guardrails | unos 0,5 s más de latencia promedio; la detección de violaciones sube de 75 % a 83 % | [blog de NVIDIA](https://developer.nvidia.com/blog/measuring-the-effectiveness-and-performance-of-ai-guardrails-in-generative-ai-applications/) (el fabricante) | **[buscador]** |
| Rails que hacen varias llamadas al modelo | de décimas de segundo a 10 o 15 s | arXiv 2610.09906 | **[buscador]** |

Kumar et al. compararon también Azure Content Safety, Bedrock Guardrails, la moderación de OpenAI,
Guardrails AI y Enkrypt AI, según su abstract.

> [!NOTE]
> Sin fuente todavía: las categorías S1 a S13 de Llama Guard 4 leídas en la tarjeta oficial, los
> tipos de rail de NeMo en su documentación y una herramienta de detección de datos personales.
