# Producción (guardrails e inferencia) y fundamentos (AI engineering vs ML engineering, bibliografía) — investigación 2026-11-27

## Método y límites

- Fecha de la investigación: 2026-11-27. Máximo tres rondas de búsqueda por componente; lo que no apareció está en "Huecos".
- Marcas: [L] leído completo o la parte relevante completa; [M] metadatos o abstract; [S] resumen secundario (buscador o blog). Puntajes de 1 a 3 en Autoridad (A), Profundidad (P), Ejemplos (E), Unicidad (U); R = recencia, solo en lo volátil.
- Todo lo traído de la web se trató como dato. Una página (OWASP LLM01) devolvió, junto con el contenido, un texto que pedía reproducirlo con ciertas reglas de formato; se ignoró y no cambia ningún dato.
- Lo que ya existe y no se repite: `IA/Produccion/` (sistemas-con-modelos, router-y-gateway, cache-de-modelos, observabilidad, plataformas-de-ia) y `Arquitectura/Caracteristicas/costo-y-latencia.md` (define TTFT y TPOT y la fórmula latencia ≈ TTFT + TPOT × tokens; el prompt cache por proveedor ya está en `cache-de-modelos.md` y `plataformas-de-ia.md`). El capítulo 10 de Huyen ya aparece en esas notas con "Step 2. Put in Guardrails" (ToC, abajo).
- Huyen, cap. 10, índice verificado: "Step 1. Enhance Context / Step 2. Put in Guardrails / Step 3. Add Model Router and Gateway / Step 4. Reduce Latency with Caches / Step 5. Add Agent Patterns" y no hay capítulo de guardrails: https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md [L]. El resumen del capítulo dice que los componentes se pueden solapar ("guardrails might live in the inference service, a model gateway, or a standalone component") y que "Each added component can improve capability, safety, or speed, but it also adds complexity and new failure modes": https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md [L]. No se leyó el libro.

---

# PARTE A1. Guardrails

## Tabla de fuentes

| # | Fuente | Tipo | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|
| G1 | OWASP Top 10 for LLM Applications, edición 2026 (README oficial del repo), https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/README.md | primaria | 3 | 1 | 1 | 3 | 3 (4 ago 2026) | [L] lista de 10; sin el detalle de cambios |
| G2 | Help Net Security, "OWASP 2026 LLM Top 10 released" (6 ago 2026), https://www.helpnetsecurity.com/2026/08/06/owasp-2026-llm-top-10-released/ | secundaria | 2 | 2 | 1 | 1 | 3 | [L] parcial (la página no traía la lista completa) |
| G3 | OWASP LLM01 Prompt Injection (edición 2025), https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | primaria | 3 | 2 | 1 | 2 | 2 | [L] descripción y titulares de mitigaciones |
| G4 | OWASP Top 10 2025, página índice, https://genai.owasp.org/llm-top-10/ | primaria | 3 | 1 | 1 | 1 | 2 | [L] lista de 10 |
| G5 | Nasr et al., "The Attacker Moves Second", arXiv 2510.09023 (10 oct 2025; listado en USENIX Security 2026), https://arxiv.org/abs/2510.09023 | primaria (preprint, con presentación en USENIX Security 2026 según el buscador) | 3 | 2 | 2 | 3 | 2 | [M] abstract |
| G6 | Sharma et al., "Constitutional Classifiers", arXiv 2501.18837, https://arxiv.org/abs/2501.18837 | primaria (preprint de Anthropic) | 2 | 2 | 2 | 3 | 2 | [M] abstract |
| G7 | Kumar et al., "No Free Lunch with Guardrails", arXiv 2504.00441, https://arxiv.org/abs/2504.00441 | primaria (preprint; los autores construyen un guardrail propio y compararon el suyo con los demás, así que no son neutrales; no se verificó su afiliación) | 1 | 2 | 2 | 3 | 2 | [M] abstract; las cifras de latencia son [S] del buscador |
| G8 | Inan et al., "Llama Guard", arXiv 2312.06674 (7 dic 2023), https://arxiv.org/abs/2312.06674 | primaria | 3 | 1 | 1 | 2 | 1 | [M] |
| G9 | Meta, tarjeta de Llama Guard 4 (vía buscador: https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama-guard-4/) | primaria | 3 | 1 | 1 | 2 | 2 | [S] el buscador no listó las categorías |
| G10 | Rebedea et al., "NeMo Guardrails", arXiv 2310.10501 (16 oct 2023), https://arxiv.org/abs/2310.10501 | primaria | 3 | 1 | 1 | 2 | 1 | [M] |
| G11 | Documentación de NeMo Guardrails, https://docs.nvidia.com/nemo/guardrails/latest/index.html | primaria | 3 | 1 | 1 | 2 | 2 | [L] la portada; no habla de latencia |
| G12 | Repo de Guardrails AI, https://github.com/guardrails-ai/guardrails | primaria | 3 | 1 | 1 | 2 | 3 | [L] portada |
| G13 | OpenAI, guía de moderación, https://developers.openai.com/api/docs/guides/moderation | primaria | 3 | 2 | 2 | 2 | 3 | [L] |
| G14 | Anthropic, "Mitigate jailbreaks and prompt injections", https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks | primaria | 3 | 2 | 3 | 2 | 3 | [L] |
| G15 | Beurer-Kellner et al., "Design Patterns for Securing LLM Agents against Prompt Injections", arXiv 2506.08837, https://arxiv.org/abs/2506.08837 ; Debenedetti et al. (Google DeepMind), "Defeating Prompt Injections by Design" (CaMeL), arXiv 2503.18813, https://arxiv.org/abs/2503.18813 | primarias | 3 | 2 | 2 | 2 | 2 | [S] solo vistos por buscador; no se abrió ninguno |
| G16 | Nota archivada `/home/dela/repos/personal/conocimiento-ia/Archivo/IA/guardrails.md` | de la base | n/a | | | | | [L] |

## Afirmaciones

**1. Qué es un guardrail y qué cubre la lista de OWASP.** OWASP publicó el 4 de agosto de 2026 la edición 2026 del Top 10 para aplicaciones con LLM: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Excessive Agency, LLM04 Supply Chain, LLM05 Data and Model Poisoning, LLM06 Unbounded Consumption, LLM07 Misinformation, LLM08 Hidden Context Exposure, LLM09 Vector and Embedding Weaknesses, LLM10 Improper Output Handling (G1). Según Help Net Security, Prompt Injection sigue primero y ahora cubre ataques entre modalidades (imágenes o audio), Misinformation sube dos lugares, Excessive Agency pasa al tercero, Unbounded Consumption sube cuatro, Output Handling baja del quinto al décimo, y System Prompt Leakage se rebautiza Hidden Context Exposure (G2). La edición anterior (2025) era: Prompt Injection, Sensitive Information Disclosure, Supply Chain, Data and Model Poisoning, Improper Output Handling, Excessive Agency, System Prompt Leakage, Vector and Embedding Weaknesses, Misinformation, Unbounded Consumption (G4). Fechas: el repo dice 4 de agosto de 2026; una nota del Cloud Security Alliance dice 3 de agosto y el comunicado oficial del lanzamiento con el Agent Control Standard es del 1 de septiembre de 2026 (https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/) [S]. Las dos fuentes (G1, G2) discrepan en nada de lo que importa; la lista completa sale solo de G1, y G2 confirma las posiciones nombradas. Dato de la nota: en esta base, citar "versión vigente = 2026", y el título de LLM07 y LLM08 cambió.

**2. Entrada: inyección de prompt, datos personales, fuera de alcance.** OWASP dice que la inyección ocurre cuando los prompts "alter the LLM's behavior or output in unintended ways", distingue directa e indirecta (contenido externo: webs, archivos), y que "it is unclear if there are fool-proof methods of prevention for prompt injection" (G3; la página no dice a qué edición corresponde, se asume 2025 por la lista G4). Sus mitigaciones, solo titulares leídos: restringir el comportamiento del modelo, definir y validar formatos de salida, filtrar entrada y salida, privilegio mínimo, aprobación humana para acciones de alto riesgo, separar e identificar el contenido externo, pruebas adversariales (G3). Anthropic recomienda pre-filtrar con un modelo chico y salida estructurada ("Harmlessness screens"), validar la entrada, endurecer el system prompt y, para inyección indirecta, poner el contenido no confiable solo en `tool_result`, codificarlo como JSON, limitar acceso a datos y acciones y filtrar las salidas de herramientas (G14). Datos personales: no se encontró una fuente primaria con método para el filtrado de PII en esta ronda (ver Huecos); solo que "Sensitive Information Disclosure" es LLM02 en 2025 y 2026 (G1, G4).

**3. Seguridad: dos fuentes independientes dicen que no hay defensa completa contra inyección.** OWASP (G3) y Nasr et al. (G5): los autores adaptaron descenso de gradiente, aprendizaje por refuerzo, búsqueda aleatoria y exploración guiada por humanos contra 12 defensas publicadas y reportan "attack success rates above 90% for most"; esas defensas habían reportado tasas "near-zero" (G5, abstract). Un resumen secundario habla de entre 71 % y 100 % y de 95 % a 99 % en defensas por prompting (VentureBeat vía buscador, https://venturebeat.com/security/12-ai-defenses-claimed-near-zero-attack-success-researchers-broke-all-of-them) [S]; no se verificaron las cifras por defensa. Lectura que apoyan las dos: diseñar para contener el daño (privilegio mínimo, aprobación humana), no para no ser engañado. Help Net recoge la frase de los líderes de OWASP: "Build the system around it, so that when the model is fooled, and it will be, nothing important breaks" (G2). Contrapunto con una sola fuente: Anthropic reporta, para sus Constitutional Classifiers, más de 3.000 horas estimadas de red teaming sin un jailbreak universal contra un clasificador temprano (G6); es un preprint del propio proveedor y se refiere a jailbreaks de contenido dañino, no a inyección en agentes. Diseños que evitan el problema por construcción (CaMeL, "Design Patterns") [S] (G15): propuestas académicas, no leídas.

**4. Salida: formato, valor, dominio, toxicidad.** La nota archivada ya trae la pila prompt, esquema, validación y ontología (G16), con fuentes de Anthropic, Pydantic y W3C; esta investigación no la desmiente. Lo que agrega esta ronda y la nota no tiene: (a) un cuarto tipo de control, los **clasificadores** (de entrada y de salida) y las APIs de moderación; (b) controles sobre acciones, no solo sobre texto (OWASP "Excessive Agency", G1); (c) el costo de cada capa (afirmación 6). La nota archivada separa guardrails de seguridad y de corrección en un párrafo final; con OWASP, la separación se ve borrosa: Improper Output Handling (LLM10) y Misinformation (LLM07) son de corrección y están en la lista de seguridad (G1). Sugerencia para Crear/Mantener: no heredar el nombre "ontología" como cuarta capa sin decir que es una opción para dominios con ontología; Huyen y Anthropic no la mencionan (G14, índice de G1).

**5. Herramientas y clasificadores (mención fechada, a 2026-11-27).**
- Llama Guard (Meta): modelo basado en Llama2-7b, ajustado por instrucciones, que clasifica prompts y respuestas con una taxonomía de riesgos personalizable; "matches or exceeds existing content moderation tools on the OpenAI Moderation Evaluation dataset and ToxicChat" según el abstract, diciembre 2023 (G8) [M]. La versión Llama Guard 4 (12B) se alinea con la taxonomía de peligros de MLCommons (S1 a S13) y suma S14, Code Interpreter Abuse (G9) [S].
- NeMo Guardrails (NVIDIA): "open-source toolkit" con un runtime inspirado en la gestión de diálogo, donde los rails los define el usuario, independientes del modelo (G10) [M]. Documentación: versión "Latest"; otras documentadas v0.25.0, v0.24.1, v0.24.0, v0.23.0, v0.22.0; no se halló fecha de release (G11).
- Guardrails AI: "a Python framework that helps build reliable AI applications"; hace dos cosas, correr guards de entrada y salida con validadores del Guardrails Hub y generar datos estructurados; licencia Apache-2.0; un aviso del 6 de julio de 2026 dice que los validadores pasan a paquetes PyPI estándar y que el remote inferencing alojado se discontinúa con corte previsto el 25 de agosto de 2026 (G12). Es un cambio que se vence rápido.
- Moderación de OpenAI: `omni-moderation-latest`, endpoint gratuito ("free to use"), texto e imagen, no audio; categorías de solo texto `harassment`, `harassment/threatening`, `hate`, `hate/threatening`, `illicit`, `illicit/violent`, `sexual/minors`; de texto e imagen `self-harm` (y `/intent`, `/instructions`), `sexual`, `violence`, `violence/graphic` (G13).
- Anthropic: patrón de clasificador chico con salida estructurada; aclara que el clasificador puede rechazar él mismo ("stop_reason: refusal") y que eso se trata como veredicto dañino (G14).

**6. Costo en latencia y en falsos positivos.** Una sola fuente que mide varios productos: Kumar et al. dicen que "there is no free lunch with guardrails; strengthening security often comes at the cost of usability" y probaron Azure Content Safety, Bedrock Guardrails, la API de moderación de OpenAI, Guardrails AI, NeMo Guardrails y Enkrypt AI (G7) [M]. Según el buscador, en su prueba Llama Guard promedió 1,5 s y NeMo 1,0 s, contra 0,08 s de un clasificador tipo BERT (G7) [S, no verificado en el paper]. Otras cifras, todas [S] y de menor autoridad: NVIDIA dice que sumar la primera capa agrega unos 0,5 s de latencia promedio y sube la detección de violaciones de 75 % a 83 % (https://developer.nvidia.com/blog/measuring-the-effectiveness-and-performance-of-ai-guardrails-in-generative-ai-applications/); un blog de PremAI argumenta que con cinco guardas de 90 % de precisión cada una los falsos positivos llegan a ~41 % (https://blog.premai.io/production-llm-guardrails-nemo-guardrails-ai-llama-guard-compared; es una cuenta, supone independencia). Con método y números de producción: Constitutional Classifiers: +0,38 % de rechazos absolutos en tráfico real y 23,7 % de sobrecosto de inferencia (G6) [M]. Discrepancia entre fuentes: las cifras de latencia van de décimas de segundo a 10 o 15 s según cuántas llamadas al modelo hace cada rail (arXiv 2610.09906, [S]); no hay un número general. Para la nota: dar el orden (regex y clasificadores chicos: decenas de ms a cientos; guardas con un LLM: segundos) como "orden de magnitud, depende de la configuración", con la fuente.

**7. Guardrails como capas: qué dice cada fuente.** Huyen los trata como un paso de la arquitectura que puede vivir en el servicio de inferencia, en el gateway o aparte (resumen del cap. 10, https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md) [L]. Anthropic: "Combine strategies for robust protection" con un ejemplo de pre-filtro más system prompt (G14). La nota archivada: prompt, esquema, validación, ontología (G16). Las tres se pueden unir: capas por qué atrapan (forma, valor, dominio, daño, acción), y para el último eslabón, el diseño del sistema (privilegios y aprobación) y no otro filtro (G2, G3).

## Contraste con la nota archivada

| Punto | Archivada | Esta investigación |
|---|---|---|
| Alcance | Corrección de salida; seguridad en un párrafo | Seguridad (OWASP) y corrección son un solo problema en la práctica |
| Capas | Prompt, esquema, validación, ontología | Suma clasificadores y moderación, control de acciones, y capa de entrada |
| Entrada | Ausente | Inyección directa e indirecta, PII, fuera de alcance |
| Herramientas | Anthropic, Pydantic, W3C | Llama Guard, NeMo, Guardrails AI, moderación de OpenAI |
| Costo | Ausente | Latencia y falsos positivos |
| Límite | "Reducen, no eliminan" (Anthropic, citado) | Dos fuentes: no hay defensa completa contra inyección |
| Fecha | 2026-10-03, borrador | Hay que fechar herramientas; OWASP 2026 existe |

## Recurso canónico (guardrails)

OWASP Top 10 for LLM Applications 2026 (G1) para el mapa de riesgos, leyendo LLM01, LLM02, LLM03 y LLM10, y la página de Anthropic "Mitigate jailbreaks and prompt injections" (G14) para el cómo. En qué fijarse: qué riesgos se mitigan con un filtro y cuáles con privilegio mínimo y aprobación humana; Nasr et al. (G5) como la razón de no confiar solo en filtros.

---

# PARTE A2. Inferencia

## Tabla de fuentes

| # | Fuente | Tipo | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|
| I1 | Kwon et al., "Efficient Memory Management for LLM Serving with PagedAttention", arXiv 2309.06180 (12 sep 2023; SOSP 2023), https://arxiv.org/abs/2309.06180 | primaria | 3 | 2 | 2 | 3 | 1 | [M] abstract |
| I2 | Yu et al., "Orca", OSDI '22, https://www.usenix.org/conference/osdi22/presentation/yu | primaria | 3 | 2 | 1 | 3 | 1 | [M] |
| I3 | Zhong et al., "DistServe", arXiv 2401.09670 (OSDI 2024), https://arxiv.org/abs/2401.09670 | primaria | 3 | 2 | 2 | 3 | 1 | [M] |
| I4 | Leviathan et al., "Fast Inference from Transformers via Speculative Decoding", arXiv 2211.17192 (ICML 2023), https://arxiv.org/abs/2211.17192 | primaria | 3 | 2 | 1 | 3 | 1 | [M] |
| I5 | Databricks (Agarwal et al.), "LLM Inference Performance Engineering: Best Practices", 12 oct 2023, https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices | secundaria de práctica con mediciones propias | 2 | 3 | 3 | 3 | 1 | [L] (vía extractor) |
| I6 | Lin et al., "AWQ", arXiv 2306.00978, https://arxiv.org/abs/2306.00978 | primaria | 3 | 1 | 1 | 2 | 2 (v6 abr 2026) | [M] |
| I7 | Kurtic et al., "Give Me BF16 or Give Me Death?", arXiv 2411.02355 (ACL 2025), https://arxiv.org/abs/2411.02355 | primaria | 3 | 2 | 3 | 3 | 2 (v4 may 2026) | [M] |
| I8 | Documentación de vLLM, https://docs.vllm.ai/en/latest/ | primaria | 3 | 1 | 1 | 2 | 3 (pie del 6 nov 2026) | [L] portada |
| I9 | Anthropic, Message Batches, https://platform.claude.com/docs/en/build-with-claude/batch-processing | primaria | 3 | 3 | 3 | 2 | 3 | [L] |
| I10 | OpenAI, Batch API, https://developers.openai.com/api/docs/guides/batch | primaria | 3 | 2 | 1 | 2 | 3 | [L] |
| I11 | Chowdhery et al., PaLM, arXiv 2204.02311 (MFU) , https://arxiv.org/abs/2204.02311 | primaria | 3 | 2 | 2 | 3 | 1 | [M]: el abstract no define MFU; la definición y las cifras vienen del buscador [S] |
| I12 | Huyen, resumen del cap. 9, https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | primaria (resumen del propio repo) | 3 | 1 | 1 | 1 | 2 | [L] |

## Afirmaciones

**1. Métricas (lo que la nota costo-y-latencia no dice).** TTFT y TPOT ya están definidos allá. Se agregan:
- Throughput: "The number of output tokens per second an inference server can generate across all users and requests" (I5). Es del servidor entero; TPOT es por usuario.
- Latencia y throughput se oponen: según Huyen, bajar la latencia suele subir el costo (I12). Medición de Databricks en una A100 con MPT-7B (512 tokens de entrada, 64 de salida, batching estático): 0,9 req/s con batch 1, 3,2 con 4, 5,3 con 8, 8,0 con 16, 10,5 con 32 y 12,5 con 64; llevar el batch a 64 sube la latencia unas 4 veces y el throughput unas 14 (I5).
- Goodput: DistServe lo toma como la métrica a optimizar, es decir, el trabajo que cumple los objetivos de TTFT y TPOT, no el bruto; reporta "7.4x more requests" servidos, o un objetivo de latencia 12,6 veces más estricto, con más de 90 % de las solicitudes dentro de la restricción (I3). La definición literal de goodput no figura en el abstract; es lectura del título ("Goodput-optimized") y del uso de SLO de TTFT y TPOT [M].
- Utilización. MBU: "MBU is defined as (achieved memory bandwidth) / (peak memory bandwidth)", con el ancho de banda logrado = (tamaño de parámetros + tamaño del KV cache) / TPOT (I5). MFU (model FLOPs utilization): la introduce PaLM; el cociente entre el throughput observado y el máximo teórico con 100 % de los FLOPs pico; PaLM reporta 45,7 % sin autoatención y 46,2 % con ella (I11) [S, el buscador citó el paper; no verificado en el PDF]. Huyen (cap. 9) nombra latencia, throughput y utilización como las tres medidas (I12).

**2. Por qué la decodificación está limitada por memoria.** "Generating the first token is typically compute-bound, while subsequent decoding is memory-bound operation", y con batch chico la velocidad depende de "how quickly we can load model parameters from GPU memory" (I5). Es decir, cada token nuevo obliga a leer todos los pesos (Llama-2-70B en float16 son 140 GB, I5) y el KV cache; por eso el TPOT se predice mejor con el ancho de banda que con los FLOPs pico (I5). Leviathan et al. lo dicen del lado del algoritmo: "decoding K tokens takes K serial runs of the model" (I4). Es una sola familia de fuentes (Databricks y los papers de optimización coinciden); no hay una fuente en contra.

**3. Aceleradores en una línea.** Las GPU (NVIDIA y otras) y las TPU (Google) son los aceleradores de uso común; para elegir, importan memoria y ancho de banda más que FLOPs en inferencia (por 2). Esta ronda no leyó una ficha oficial de GPU ni de TPU: hueco para una tabla comparativa fechada.

**4. Optimizaciones del modelo.**
- Cuantización. Pasar de pesos de 16 a 8 bits puede reducir a la mitad las GPU necesarias en entornos limitados por memoria, y el KV cache de Llama-2-70B a largo 1024 pasa de 5 GiB a 2,5 GiB con batch 16 (I5). Calidad: Kurtic et al., más de 500.000 evaluaciones en la familia Llama-3.1: FP8 (W8A8-FP) "effectively lossless", INT8 con 1 a 3 % de pérdida si está bien ajustado, e INT4 de solo pesos "more competitive than expected"; recomiendan W4A16 para costo en sincrónico y W8A8 para batching continuo asincrónico (I7). AWQ (MLSys 2024, premio Best Paper según el listado): "Protecting only 1% salient weights can greatly reduce quantization error" (I6). vLLM soporta FP8, INT8, INT4, GPTQ/AWQ y GGUF (I8). Cuidado: las cifras de I7 son de una familia de modelos y del año 2024; la pérdida en otros modelos o tareas puede ser otra.
- Decodificación especulativa. Un modelo chico propone varios tokens y el grande los verifica en paralelo; en T5-XXL, aceleración de 2X a 3X "with identical outputs", sin reentrenar (I4). vLLM lista métodos n-gram, suffix, EAGLE y DFlash (I8); no se leyeron esos métodos.
- KV cache y PagedAttention. El KV cache de cada solicitud es grande y de tamaño variable, y la fragmentación limita el batch; PagedAttention (inspirado en la memoria virtual) y vLLM logran "near-zero waste in KV cache memory" y 2 a 4 veces más throughput que FasterTransformer y Orca a igual latencia, con más ganancia en secuencias largas y modelos grandes (I1). El prefix caching de vLLM es el equivalente autoalojado del prompt cache (I8; ver `cache-de-modelos.md`).

**4b. Del servicio.**
- Batching continuo. Orca planifica "at the granularity of iteration (instead of request)": una solicitud que termina sale y otra entra sin esperar a todo el batch; reporta hasta 36,9 veces más throughput que FasterTransformer en GPT-3 175B a igual latencia (I2; la página mostraba "36:9×", se interpreta como 36,9). Databricks dice que el batching continuo puede dar 10 a 20 veces más throughput que el dinámico (I5); es una medición de un blog.
- Prefill y decode desagregados. DistServe corre prefill y decode en GPU distintas para eliminar la interferencia y ajusta cada fase a sus objetivos de TTFT y TPOT (I3). vLLM lista "Disaggregated serving: separate prefill, decode, and encode stages" (I8). No se encontró evidencia independiente de DistServe en producción ni la comparación de costos de la red entre nodos: hueco.
- Prompt caching de proveedores: ya cubierto; en Anthropic, el batch admite prompt caching con descuentos que se acumulan y tasas de acierto "ranging from 30 percent to 98 percent" (I9).

**5. APIs de batch con descuento (a 2026-11-27).**
- Anthropic: Message Batches, "cutting costs by 50 percent"; "most batches finishing in less than 1 hour"; un batch tiene como máximo 100.000 solicitudes o 256 MB; los batches vencen si no terminan en 24 horas; admite prompt caching (con caché de 1 hora recomendada) (I9).
- OpenAI: "50% cost discount compared to synchronous APIs"; "Each batch completes within 24 hours"; hasta 50.000 solicitudes y 200 MB por archivo (I10).
- Discrepancia en límites entre las dos: 100.000 y 256 MB contra 50.000 y 200 MB. Es volátil; fechar. No se leyó la guía de Gemini.
- Cuándo sirve: trabajo sin urgencia (evaluaciones, etiquetado, enriquecimiento). Anthropic lo dice así: "You’re running large-scale evaluations or analyses" (I9).

## Recurso canónico (inferencia)

Para el mecanismo: el artículo de Databricks sobre ingeniería de rendimiento de inferencia (I5) más el paper de vLLM (I1); en qué fijarse: la fórmula de MBU, la comparación de TTFT con TPOT y la curva de throughput contra batch. Para decidir: el capítulo 9 de Huyen (I12), no leído directamente. Para precios y límites: las documentaciones oficiales (I9, I10), fechadas.

---

# PARTE B1. AI engineering y ML engineering

## Tabla de fuentes

| # | Fuente | Tipo | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|
| F1 | Huyen y Orosz, "The AI Engineering Stack" (extracto del cap. 1 en The Pragmatic Engineer, 20 may 2025), https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack | primaria (extracto del libro) | 3 | 2 | 2 | 3 | 2 | [L] vía extractor |
| F2 | Swyx y Latent Space, "The Rise of the AI Engineer" (30 jun 2023), https://www.latent.space/p/ai-engineer | primaria (ensayo de opinión) | 2 | 2 | 2 | 3 | 1 | [L] vía extractor, por citas |
| F3 | Resumen de capítulos del libro, https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | primaria | 3 | 1 | 1 | 2 | 2 | [L] |
| F4 | Repo del libro, https://github.com/chiphuyen/aie-book | primaria | 3 | 1 | 1 | 1 | 2 | [L] |
| F5 | Huyen, "Common pitfalls when building generative AI applications" (16 ene 2025), https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html | primaria | 3 | 2 | 2 | 2 | 2 | [L] titulares |

## Afirmaciones

**1. En qué se diferencia el oficio.** Huyen (cap. 1): "AI engineering focuses less on modeling and training, and more on model adaptation", "This makes evaluation a much bigger problem in AI engineering" y "ML knowledge is no longer a must-have for building AI applications" (F1). Matiz del propio libro: "many principles from ML engineering are still applicable to AI engineering" y la pregunta que se pasa por alto es "whether you should build it" (F3). Swyx (2023): "productionizing AI APIs and OSS models", con la razón de oferta: "There are ~5000 LLM researchers in the world, but ~50m software engineers", y la predicción de que será "the highest-demand engineering job of the decade" (F2). Esa predicción de 2023, con su ratio de empleos (unos 10 de ML engineer por cada uno de AI engineer en Indeed, a invertirse en unos cinco años), no se verificó con datos posteriores: hueco, y entra en la parte contraria.

**2. De modelo-primero a producto-primero.** "With traditional ML engineering, you usually start with gathering data and training a model", mientras que ahora "it's possible to start with building the product first", y "differentiation must be gained through the application development process" (F1). En el cap. 10: "AI engineering is moving closer to product" porque el flywheel de datos y la experiencia de producto son ventaja competitiva (F3). Swyx: los prototipos con LLM permiten validar ideas antes de reunir datos para ajustar un modelo (F2). Las tres coinciden y son de la misma comunidad: es una sola corriente de opinión, no tres confirmaciones independientes (ver contraria.md).

**3. La pila en tres capas (Huyen).** "Application development involves providing a model with good prompts and necessary context"; "Model development": "This layer provides tooling for developing models"; "Infrastructure": "tooling for model serving, managing data and compute, and monitoring" (F1). Mapa con esta base: aplicación = Contexto y RAG, evaluación, interfaz; infraestructura = inferencia y observabilidad (`IA/Produccion/`); desarrollo de modelos = finetuning y datos. No se leyó el capítulo entero; las tres definiciones son citas del extracto.

**4. Matiz de Swyx contra el mito.** Swyx también escribe que prompt engineering "was both overhyped and here to stay" y que el rol puede sentirse "inferior to people with good Data Science/ML backgrounds" (F2). Útil para el lector que se prepara a un puesto: el oficio no pide ser investigador, pero sí evaluación.

## Recurso canónico

Huyen y Orosz (F1) para la definición y las tres capas, y Swyx (F2) para el origen del rol; fijarse en cómo cada uno define qué se deja de hacer (entrenar) y qué se hace más (evaluar y producto). Libro: cap. 1 completo.

---

# PARTE B2. Bibliografía corta

## Tabla de fuentes

| # | Recurso | Tipo | Qué parte | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|---|
| B1 | Huyen, *AI Engineering* (O'Reilly, 2025) | primaria (libro) | Cap. 1, 3-4, 9 y 10 | 3 | 3 | 2 | 3 | 3 | [M] índice y resúmenes; el libro no se leyó. "This is NOT a tutorial book"; "Tools become outdated quickly, but fundamentals should last longer" (F4) |
| B2 | Yan, Bischof, Frye, Husain, Liu, Shankar, "What We've Learned From A Year of Building with LLMs" (8 jun 2024), https://applied-llms.org/ | secundaria (práctica) | Tactical, Operational, Strategic | 2 | 3 | 3 | 2 | 2 | [L] parcial (106.432 caracteres, se leyeron 100.000) |
| B3 | Husain, "Your AI Product Needs Evals" (29 mar 2024), https://hamel.dev/blog/posts/evals/ | secundaria | Los tres niveles de evaluación | 2 | 2 | 3 | 2 | 2 | [L] por resumen del extractor |
| B4 | Anthropic, "Building effective agents", https://www.anthropic.com/engineering/building-effective-agents | primaria | Flujos de trabajo contra agentes | 3 | 2 | 2 | 2 | 2 | [S] por `lo-que-pierde-peso.md`; no releído acá |
| B5 | Karpathy, "Neural Networks: Zero to Hero", https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ | primaria (curso abierto) | Para entender el modelo por dentro | 3 | 3 | 3 | 3 | 2 | [S] recomendado en el resources.md de Huyen; no visto |
| B6 | Hugging Face LLM Course, https://huggingface.co/learn/llm-course/chapter1/1 | primaria (curso abierto) | Caps. 1-4 | 2 | 2 | 3 | 2 | 3 | [L] portada: gratuito, requiere Python, 6 a 8 horas por capítulo |
| B7 | Alammar, "The Illustrated Transformer" (27 jun 2018), https://jalammar.github.io/illustrated-transformer/ | secundaria | Completo | 2 | 2 | 3 | 2 | 1 | [M] |
| B8 | Huyen, resources.md del libro, https://raw.githubusercontent.com/chiphuyen/aie-book/main/resources.md | primaria (lista) | Para ampliar | 3 | 1 | 1 | 2 | 2 | [L] |
| B9 | Kwon et al. (PagedAttention) y Databricks (I1, I5) | primarias | Inferencia | 3 | 3 | 2 | 3 | 1 | ver A2 |

## Recomendación por perfil (lectura de esta investigación, no de las fuentes)

- Quien programa y sabe de APIs: Huyen cap. 1 (F1), después B2 y B3 para el oficio (evaluar y mirar datos), después cap. 10.
- Quien se prepara para un puesto: lo anterior, más cap. 3 y 4 (evaluación) y la bibliografía de la parte contraria; Karpathy (B5) para un modelo mental del interior.
- Declarado: Huyen lista a Eugene Yan, Husain y Applied LLMs (B8); son practicantes reconocidos y fuente secundaria. Que Husain sea coautor de B2 y autor de B3 y que ambos defiendan la evaluación primero hace que no sean dos fuentes independientes sobre esa tesis.

## Recurso canónico (bibliografía)

*AI Engineering* (B1) como espina y B2 como complemento de práctica; fijarse en que B1 dice de sí que no es un tutorial y que las herramientas envejecen (F4).

---

# Huecos

1. **PII y datos personales en guardrails.** No hay una fuente primaria leída (Presidio, filtros de proveedores). Una ronda no alcanzó.
2. **Categorías completas de Llama Guard 4** (S1 a S13): el buscador no las listó; falta leer la tarjeta oficial de Meta.
3. **NeMo Guardrails:** los tipos de rail y los números de latencia de la documentación oficial no están (la portada no los da); las cifras de latencia de guardrails son de un preprint con conflicto de interés y de blogs.
4. **Cifras de "No Free Lunch"** (1,5 s, 1,0 s, 0,08 s): sin verificar contra el paper.
5. **CaMeL y "Design Patterns for Securing LLM Agents":** solo vistos por buscador.
6. **OWASP 2026:** detalle de cambios y de cada ítem (la página oficial no los itemiza); no se abrió el listado de cada riesgo de 2026.
7. **MFU:** definición y cifras de PaLM vía buscador; falta el apéndice B del PDF. No se halló una definición de MFU específica para inferencia.
8. **Goodput:** no hay definición literal leída; solo el uso en DistServe.
9. **Aceleradores (GPU y TPU):** sin ficha oficial leída.
10. **Gemini batch** y otros proveedores de batch: no leídos.
11. **vLLM:** no se verificaron las afirmaciones de cada técnica en la documentación detallada ni la versión estable.
12. **Cap. 9 y 10 de Huyen:** el libro no se leyó; solo índice y resúmenes de capítulo.
13. **Las tres capas de Huyen:** solo las definiciones del extracto de F1; no el capítulo.
14. **Predicción de Swyx (ratio de empleos):** sin datos posteriores.
15. **Cursos abiertos:** Karpathy y fast.ai no se abrieron; solo se verificó el curso de Hugging Face.
