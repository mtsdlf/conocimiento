---
resumen: >-
  La conversación con IA es practicar el habla con un sistema de diálogo automático; un
  metaanálisis le da un efecto medio sobre el habla, pero casi todos sus estudios son de sistemas
  anteriores a los modelos de lenguaje actuales, y lo que hay de estos son estudios chicos y
  preprints.
estado: vigente
estabilidad: semi
fuentes:
  - "Hou y Min (2026, en línea 2025-07-14), metaanálisis de CALL dialógico y habla L2, ReCALL 38(1), 40-56: https://www.cambridge.org/core/product/31847710516602398819C5E594038E7B/core-reader"
  - "Bibauw et al. (2022), Language Learning & Technology: https://scholarspace.manoa.hawaii.edu/items/2e7868cd-8f01-43ca-ac54-44425cd487a9/full"
  - "Kansizoglu y Kayhan, metaanálisis de chatbots y habla: https://dergipark.org.tr/en/download/article-file/5297158"
  - "Lyu et al. (2024), vía artículo de Springer (2025): https://link.springer.com/article/10.1007/s11528-025-01140-7"
  - "Ensayo aleatorizado de pronunciación con un modelo de lenguaje (n = 60): https://link.springer.com/article/10.1007/s44217-025-00782-2"
  - "HICSS 2025, experimento de campo con agentes de IA para inglés hablado: https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/2dbb5135-db0f-4532-8a31-803df5ec3e54/content"
  - "Preprint (sin revisión por pares), habla con un modelo de lenguaje: https://arxiv.org/pdf/2611.09898"
  - "Preprint (sin revisión por pares), voz de un modelo de lenguaje, estudio preliminar: https://arxiv.org/abs/2603.14884"
aliases:
  - AI conversation practice
  - Chatbot
  - Práctica con chatbot
creado: 2026-11-27
revisado: 2026-11-27
---

# Conversación con IA

La conversación con IA es practicar el habla con un sistema de diálogo automático; un
metaanálisis le da un efecto medio sobre el habla, pero casi todos sus estudios son de sistemas
anteriores a los modelos de lenguaje actuales, y lo que hay de estos son estudios chicos y
preprints.

Está en la rama de output de la [práctica](practica.md), separada de la
[conversación con corrección](conversacion-con-correccion.md) porque su evidencia y sus riesgos
son otros. Da cantidad de práctica: se puede hablar a cualquier hora y sin pagar por minuto.
Los informes no encontraron evidencia de que corrija con confiabilidad ni de que se parezca a una
conversación con personas.

## Lo que mide el metaanálisis y dónde se queda corto

Hou y Min (2026) reunieron 16 estudios y 89 tamaños de efecto sobre sistemas de diálogo para el
habla en segunda lengua. El efecto global fue g = 0.61 (IC 95% 0.34 a 0.89), un efecto medio.
Los sistemas orientados a una meta tuvieron efecto grande; los de solo texto, el más bajo y no significativo. El feedback correctivo, el
nivel y la duración no fueron moderadores significativos. Las muestras eran de menos de 60
alumnos y los autores mencionan posible sesgo de publicación.

El límite principal: casi todos esos sistemas estaban basados en reglas, no en IA generativa, y
los autores marcan los modelos de lenguaje como línea futura. El mejor número disponible habla de
una tecnología distinta de la que se usa hoy.

Otros metaanálisis dan cifras que van de 0.58 (Bibauw et al. 2022) a 1.035 (Kansizoglu y Kayhan,
en una revista cuya calidad no se verificó). El rango refleja criterios de inclusión distintos, y
los tres son de chatbots anteriores a los modelos actuales. Lyu et al. (2024), según un artículo
que lo cita, encontraron en 31 estudios g = 0.83 con IA generativa frente a 0.47 sin ella, pero
sobre el rendimiento en la lengua en general, no solo el habla.

## Lo que hay sobre los modelos de lenguaje

Para los modelos de lenguaje (2023-2026), los informes encontraron estudios chicos,
cuasiexperimentales o descriptivos. El único ensayo aleatorizado hallado es de pronunciación, con
60 participantes en Irán. Un experimento de campo de cuatro semanas, presentado en HICSS 2025,
reportó mejoras de habla con agentes de IA, pero la aplicación era de una empresa vinculada a los
autores.

> [!IMPORTANT]
> Varios trabajos citados en la discusión son preprints sin revisión por pares: arXiv
> 2611.09898 (habla con un modelo de lenguaje), 2603.14884 (voz, estudio preliminar), 2505.24000
> (percepciones), 2510.08227 (realidad mixta) y 2606.22225 (fluidez interaccional). Ninguno es un
> ensayo controlado con resultados de aprendizaje a largo plazo. Hay indicios de que baja la
> ansiedad y da práctica; faltan estudios con IA generativa en B2 a C1 y con pruebas diferidas.

## Cómo usarla según esa evidencia

El metaanálisis de Hou y Min sugiere dos cosas: la práctica orientada a una meta rindió más, y el
texto fue el formato con menor efecto. Todo lo demás es inferencia de esta base.

1. Hablá en vez de escribir. Usá el modo de voz: los sistemas de texto tuvieron el efecto más bajo.
2. Dale una tarea con meta, no "charlemos". Por ejemplo: *You're the hiring manager for a backend
   role. Interview me for 15 minutes, one question at a time, and push back on vague answers.*
3. Pedile corrección en forma de prompt, no de recast: *When I make a grammar mistake, don't
   correct it for me. Repeat the wrong part with a question mark and wait for me to fix it.*
4. Al final, pedile una lista de tus errores repetidos con la forma correcta, y verificá los
   dudosos en un diccionario o una gramática (precaución de esta base, sin fuente).
5. Repetí la misma tarea otro día, como en la [fluidez](fluidez.md), y compará las grabaciones
   con [grabarse y medirse](grabarse-y-medirse.md).
6. Para la pronunciación fina, buscá otra referencia (precaución de esta base, sin fuente): que un
   reconocedor de voz te entienda no equivale a que te entienda una persona.

Puede sumar horas entre sesiones con personas. Reemplazarlas no tiene respaldo: ningún estudio de
los informes lo compara con la conversación real, que trae turnos, interrupciones y malentendidos
([interacción](../Discurso/interaccion.md)).
