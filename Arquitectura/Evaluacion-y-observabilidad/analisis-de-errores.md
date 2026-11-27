---
resumen: >-
  El análisis de errores es leer a mano trazas reales de un sistema con un modelo, anotar cada
  falla en texto libre, agruparlas en categorías y contarlas, para saber qué evaluar antes de
  elegir métricas.
estado: borrador
estabilidad: semi
fuentes:
  - https://hamel.dev/blog/posts/field-guide/
  - https://hamel.dev/blog/posts/evals/
  - https://arxiv.org/abs/2404.12272
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://huyenchip.com/2025/01/07/agents.html
aliases: [error analysis, mirar los datos, look at your data]
creado: 2026-11-27
revisado:
---

# Análisis de errores

El análisis de errores es leer a mano trazas reales de un sistema con un modelo, anotar cada falla
en texto libre, agruparlas en categorías y contarlas, para saber qué evaluar antes de elegir
métricas.

Es el puente del [bucle](evaluacion-y-observabilidad.md) entre la
[observabilidad](observabilidad-de-modelos.md), que guarda las trazas, y la [evaluación](evaluacion.md), que
necesita saber qué medir. El índice de Huyen no lo separa como sección; el campo lo trata aparte
por las notas de Husain y el trabajo de Shankar.

## El paso que más se saltea

Husain (2025) llama a saltearse el análisis de errores "el error más común" al construir productos
con modelos. El síntoma es un tablero de métricas genéricas (fidelidad, relevancia, toxicidad) que no
se mueven cuando el producto mejora o empeora, porque nadie miró qué fallaba. Huyen dice lo mismo
desde su experiencia: "staring at data for just 15 minutes usually gives me some insight that could
save me hours of headaches", y recomienda inspeccionar a mano datos de producción todos los días.

## De la traza a la categoría contada

El proceso de Husain va de abajo hacia arriba:

1. Leé conversaciones o trazas reales, completas, con los pasos intermedios.
2. Anotá cada falla en texto libre, sin categorías previas.
3. Agrupá las anotaciones en una taxonomía; un modelo puede ayudar a agrupar.
4. Contá cuántas veces aparece cada categoría y atacá las más frecuentes.

En el caso de un cliente propio que relata, tres problemas
causaban más del 60 % de las fallas, y el manejo de fechas pasó de 33 % a 95 % de acierto después de
atacarlo. Es la cifra de un solo cliente del autor, sin verificación independiente. Las categorías
contadas son las que después se vuelven evals y, si hace falta escala, criterios para un
[juez](ia-como-juez.md).

## Criteria drift: los criterios cambian al mirar

Shankar et al. (2024) estudiaron cómo las personas validan evaluadores generados por modelos y
encontraron *criteria drift*: hace falta tener criterios para calificar salidas, pero calificar
salidas cambia los criterios. Quien mira cien respuestas descubre fallas que no imaginaba y deja de
importarle otras que creía graves. Husain lo cita así: "it is impossible to completely determine
evaluation criteria prior to human judging of LLM outputs".

La consecuencia de diseño es que la rúbrica de evaluación no se escribe una vez: se reescribe cada vez
que el análisis de errores encuentra algo nuevo. Por eso el bucle vuelve siempre a las trazas.

## Cómo sale mal

- **Categorías de antemano.** Partir de una lista de fallas "típicas" en lugar de leer; se encuentra
  lo que se buscaba.
- **Mirar solo la salida final.** Sin los pasos intermedios, una respuesta mala no dice si falló la
  recuperación de [contexto](../Sistemas-con-modelos/contexto-y-rag.md), la herramienta o el modelo.
  En un [agente](../Sistemas-con-modelos/agente.md), Huyen distingue fallas de planificación, de
  herramientas y de eficiencia.
- **Delegarlo entero.** Un modelo puede agrupar anotaciones, pero las anotaciones las hace quien
  conoce el producto; Husain insiste en que la corrección se alinea con una persona.

## Qué leer para hacerlo la primera vez

Husain, ["A Field Guide to Rapidly Improving AI Products"](https://hamel.dev/blog/posts/field-guide/):
fijarse en el proceso de abajo hacia arriba y en el visor de trazas con botones de correcto e
incorrecto. Para el fundamento, Shankar et al.,
["Who Validates the Validators?"](https://arxiv.org/abs/2404.12272), leído solo en su resumen: fijarse
en criteria drift.
