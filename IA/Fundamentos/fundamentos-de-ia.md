---
resumen: >-
  Fundamentos reúne lo que cruza todo el tema IA sin ser una parte del sistema: de dónde viene la
  IA generativa, en qué se diferencia el oficio de AI engineering del de ML engineering, con qué
  sesgo hablan sus voces de referencia y qué leer para ir más hondo.
estado: vigente
estabilidad: estable
fuentes:
  - https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack
  - https://github.com/chiphuyen/aie-book
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/resources.md
  - https://www.latent.space/p/ai-engineer
  - https://arxiv.org/abs/2604.16304
aliases: [fundamentos de AI engineering, AI engineering foundations]
creado: 2026-11-27
revisado: 2026-11-27
---

# Fundamentos de IA

Fundamentos reúne lo que cruza todo el tema IA sin ser una parte del sistema: de dónde viene la
IA generativa, en qué se diferencia el oficio de AI engineering del de ML engineering, con qué
sesgo hablan sus voces de referencia y qué leer para ir más hondo.

No es una vertical. Las verticales de [IA](../ia.md) son las partes de un sistema con un modelo
adentro ([Modelos](../Modelos/modelos.md), [Contexto](../Contexto/contexto.md),
[Agentes](../Agentes/agentes.md), [Ajuste](../Ajuste/ajuste.md),
[Evaluación](../Evaluacion/evaluacion.md) y [Producción](../Produccion/produccion.md)); acá va lo
que sirve para leerlas a todas con criterio.

## Tres ideas que ordenan la lectura del tema

**El orden del trabajo se invirtió.** En ML tradicional se empezaba por juntar datos y entrenar un
modelo; con los modelos base se puede empezar por el producto. Huyen lo dice así en el capítulo 1
de *AI Engineering*: "it's possible to start with building the product first". Por eso la evaluación es "a much
bigger problem", y este tema, como decisión propia, pone a [Evaluación](../Evaluacion/evaluacion.md)
como la vertical que decide qué adaptar. La historia de cómo se llegó a ese punto está en
[historia de la IA generativa](historia-de-la-ia-generativa.md), y la diferencia entre los dos
oficios, en [AI engineering y ML engineering](ai-engineering-y-ml-engineering.md).

**Las voces del campo son una sola comunidad.** La lista de recursos del libro de Huyen recomienda
a Eugene Yan, a Hamel Husain y a *What We've Learned From A Year of Building with LLMs*, y Husain y
Yan son coautores de ese ensayo. Cuando coinciden, cuentan como una corriente de opinión,
no como confirmaciones independientes. El tema hereda ese sesgo (pro-evaluación y pro-producto) y
lo declara; cómo se lee el campo con eso en mente está en
[AI engineering y ML engineering](ai-engineering-y-ml-engineering.md#el-sesgo-de-comunidad-de-las-voces-del-campo).

**Lo que dura son los mecanismos, no las herramientas.** El repositorio del libro de Huyen lo
pone como premisa: "Tools become outdated quickly, but fundamentals should last longer". La base
sigue la misma regla: los nombres de modelos, precios y plataformas viven solo en fichas fechadas
(como [modelos disponibles](../Modelos/modelos-disponibles.md) y
[plataformas de IA](../Produccion/plataformas-de-ia.md)), y las notas de arriba explican lo que no
cambia cuando sale un modelo nuevo.

## Qué hay en Fundamentos

- [Historia de la IA generativa](historia-de-la-ia-generativa.md) — de los modelos de lenguaje
  estadísticos y las redes recurrentes al Transformer (2017), GPT-3 (2020), ChatGPT (2022), los
  modelos base multimodales y los modelos de razonamiento, con las fechas de cada paper.
- [AI engineering y ML engineering](ai-engineering-y-ml-engineering.md) — qué se deja de hacer y
  qué se hace más, la pila en tres capas, de dónde sale el rol y el sesgo de comunidad del campo.
- [Bibliografía de IA](bibliografia-de-ia.md) — libros, cursos abiertos, ensayos y papers, cada uno
  con qué parte leer y en qué fijarse, y la evidencia en contra para leer al lado.

El mercado laboral del oficio (qué roles piden los avisos y cómo se leen) no está acá: vive en
[Presentación profesional](../../Presentacion-profesional/Posicionamiento/caso-roles-de-ai-engineering.md).
Lo que pierde peso en la arquitectura de sistemas con modelos (entrenar desde cero, frameworks de
agentes pesados) está en [lo que pierde peso](../../Arquitectura/Fundamentos/lo-que-pierde-peso.md).

El tema no tiene glosario aparte: cada término se define en la nota de su componente
([token y embedding](../Modelos/token-y-embedding.md), [ventana de contexto](../Modelos/transformer.md),
[inferencia](../Produccion/inferencia.md)), y su nombre en inglés va en los `aliases` de esa nota.
