---
resumen: >-
  La cache de modelos guarda trabajo ya hecho para no pagarlo dos veces: el prompt cache reutiliza
  el comienzo repetido de los prompts, la cache exacta devuelve la misma respuesta a la misma
  consulta y la cache semántica la devuelve a una consulta parecida, con el riesgo de equivocarse.
estado: vigente
estabilidad: estable
fuentes:
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 10 «Step 4. Reduce Latency with Caches», p. 460; cap. 9 «Inference Service Optimization», p. 440"
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://developers.openai.com/api/docs/guides/prompt-caching
  - https://aistudio.google.com/docs/caching
  - https://claude.com/resources/articles/harnessing-claudes-intelligence
  - https://arxiv.org/abs/2502.03771
  - https://www.infoq.com/articles/reducing-false-positives-retrieval-augmented-generation
  - https://dzone.com/articles/llm-semantic-caching
aliases: [prompt caching, prompt cache, semantic cache, cache semántica, cache exacta, exact cache, context caching]
creado: 2026-11-27
revisado: 2026-11-27
---

# Cache de modelos

La cache de modelos guarda trabajo ya hecho para no pagarlo dos veces: el prompt cache reutiliza
el comienzo repetido de los prompts, la cache exacta devuelve la misma respuesta a la misma
consulta y la cache semántica la devuelve a una consulta parecida, con el riesgo de equivocarse.

Es el paso 4 de la arquitectura de Huyen, "Reduce Latency with Caches": cada llamada a un modelo
cuesta y tarda, y en muchas aplicaciones una parte grande de lo que se manda se repite. Las tres
caches que distingue Huyen se parecen de nombre pero viven en lugares distintos y tienen riesgos
muy distintos.

| Cache | Qué reutiliza | Dónde vive | Puede devolver algo incorrecto |
|---|---|---|---|
| Prompt cache | El cómputo del comienzo del prompt que se repite | En el proveedor del modelo | Casi no: el modelo igual genera la respuesta |
| Exacta | La respuesta entera, para una consulta idéntica | En la aplicación o el gateway | Si la respuesta envejeció |
| Semántica | La respuesta entera, para una consulta parecida | En la aplicación o el gateway | Sí, si toma por parecidas dos consultas que no lo son |

## El prompt cache: ordenar el prompt para que el proveedor reutilice

Muchos prompts empiezan igual: las instrucciones del sistema, las definiciones de herramientas, un
documento largo, la conversación hasta acá. El prompt cache guarda el cómputo de ese comienzo y lo
reutiliza en la consulta siguiente, que se cobra más barata y tarda menos. Huyen advierte que, como
pasa con la [KV cache](../Modelos/transformer.md), "prompt cache size can be quite large and require significant
engineering effort". Hoy lo ofrecen los proveedores, y a la aplicación le toca aprovecharlo. Del
lado del servidor, el libro trata la optimización del servicio de inferencia en el cap. 9 (p. 440),
y su versión autoalojada (*prefix caching*) se cuenta en [Inferencia](inferencia.md).

Los tres grandes proveedores lo ofrecen con diseños distintos: uno exige marcar qué se cachea,
otros lo activan solos; algunos cobran la escritura en la cache además de descontar la lectura. Lo
que tienen en común define cómo se escribe el prompt:

- **El acierto exige un comienzo idéntico.** La documentación de Anthropic pide un prefijo 100%
  igual; cualquier cambio corta la cache desde ese punto.
- **Lo estable va primero y lo variable al final.** Es el consejo explícito de OpenAI y de
  Anthropic: instrucciones y herramientas arriba, la consulta del usuario abajo.
- **Cambiar herramientas o modelo invalida.** Según Anthropic, cambiar las definiciones de
  herramientas invalida toda la cache, y su guía de harness recomienda no cambiar de modelo a mitad
  de una sesión para no perder los aciertos.

Esto afecta a otras capas: un [router](router-y-gateway-de-modelos.md) que cambia de modelo en cada
turno pierde la cache, y un [agente](../Agentes/agente.md) con herramientas que cambian también. Cuánto se
descuenta, cuánto dura la cache y desde qué tamaño de prompt aplica cambia por proveedor y por
modelo, y está en [Plataformas de IA](plataformas-de-ia.md).

## La cache exacta: la de siempre, con una política de expiración

La cache exacta es la de cualquier sistema: misma entrada, misma salida guardada. Huyen la descarta
para consultas propias de un usuario o que dependen del momento, donde una respuesta guardada
queda mal. Huyen dice que tener una política de desalojo es imprescindible para controlar el tamaño de la cache y
mantener el rendimiento; que lo guardado envejezca es lectura de esta base.

## La cache semántica y por qué se equivoca

La cache semántica convierte la consulta en un embedding, busca una consulta guardada parecida y,
si la similitud pasa un umbral, devuelve su respuesta sin llamar al modelo. Acierta más seguido que
la exacta, porque la gente pregunta lo mismo con palabras distintas (inferencia de esta base), pero
su falla es devolver con
seguridad una respuesta a otra pregunta. Huyen lo dice así: "If the system mistakes the incoming
query as being similar to another query", la respuesta es errónea; y su calidad depende de
"high-quality embeddings, functional vector search, and a trustworthy similarity metric".

La evidencia sobre ese riesgo es poca y floja, pero apunta al mismo lado:

- vCache (preprint sin revisión por pares, según su resumen) encuentra que los aciertos correctos e
  incorrectos tienen puntajes de similitud muy superpuestos, así que ningún umbral global los
  separa bien; propone aprender un umbral por entrada.
- Un caso publicado en InfoQ, sobre las preguntas frecuentes de un banco (un solo caso, con tono de
  proveedor, leído por su resumen), reporta respuestas seguras pero erróneas y falsos positivos de
  hasta 99% en algunos modelos con umbral 0,7.
- Un artículo de divulgación sugiere umbrales más estrictos, embeddings del dominio, verificar la
  respuesta después, combinar clave exacta y semántica, y recuerda que la similitud no envejece: una
  entrada vieja sigue pareciendo igual de cercana.

Por inferencia de esta base: la cache semántica tiene que pasar por la misma
[evaluación](../Evaluacion/evals.md) que el modelo, con casos de consultas
parecidas que piden respuestas distintas, y no conviene en dominios donde una respuesta equivocada
cuesta caro.

> [!NOTE]
> Sin fuente todavía: un estudio con revisión por pares sobre cache semántica en producción.

El recurso canónico para las tres caches es la sección "Cache" del
[post de plataforma de Huyen](https://huyenchip.com/2024/07/25/genai-platform.html) (cap. 10,
p. 460); conviene fijarse en que el riesgo de corrección está solo en la semántica. Para el prompt
cache, la documentación del proveedor que se use: la de
[Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) es la más
completa sobre qué invalida la cache y cómo leer en la respuesta cuánto se leyó de ella.
