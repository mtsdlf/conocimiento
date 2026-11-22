---
resumen: >-
  Los cuatro riesgos son la taxonomía de Cagan de lo que hay que averiguar de una idea antes de construirla: si tiene valor para el cliente, si se puede usar, si se puede construir y si le sirve al negocio.
estado: borrador
estabilidad: estable
fuentes:
  - "Marty Cagan, Product Risk Taxonomies (SVPG, 2023-07-10): https://svpg.com/product-risk-taxonomies"
  - "Marty Cagan, Inspired, 2.ª ed. (2017 o 2018, según la fuente), cap. 33 (no abierto; preguntas de cada riesgo según el buscador): https://www.oreilly.com/library/view/inspired-2nd-edition/9781119387503/c33.xhtml"
  - "Paweł Huryn, Product Compass, sobre el riesgo ético (vía buscador): https://www.productcompass.pm/p/product-model-first-principles-discovery-deliver"
  - "Teresa Torres, Assumption testing (Product Talk, 2023): https://www.producttalk.org/2023/10/assumption-testing/"
  - "David Bland, mapeo de supuestos (Strategyzer, vía buscador): https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter"
  - "Producto/.investigacion/descubrimiento.md"
aliases: [four big risks, los cuatro grandes riesgos, riesgos de producto, product risks, value usability feasibility viability]
creado: 2026-11-22
revisado:
---

# Cuatro riesgos

Los cuatro riesgos son la taxonomía de Cagan de lo que hay que averiguar de una idea antes de construirla: si tiene valor para el cliente, si se puede usar, si se puede construir y si le sirve al negocio.

Es la pieza central del [descubrimiento](descubrimiento.md). El [árbol de oportunidades](arbol-de-oportunidades.md) y la [prueba de supuestos](prueba-de-supuestos.md) son formas de reducir estos riesgos, y el [descubrimiento continuo](descubrimiento-continuo.md) es la cadencia con que se hace. Los riesgos se atacan antes de construir y no después de lanzar.

## Los cuatro y la pregunta de cada uno

Las preguntas de la tabla vienen de un resumen del buscador sobre el capítulo 33 de *Inspired* (2.ª ed.); no se verificaron en el texto. Según ese mismo resumen, Cagan exige evidencia para cada riesgo, no la opinión del product manager.

| Riesgo | La pregunta | En inglés |
|---|---|---|
| Valor | ¿Lo van a comprar o usar? | value |
| Usabilidad | ¿Los usuarios saben usarlo? | usability |
| Factibilidad | ¿Podemos construirlo? | feasibility |
| Viabilidad de negocio | ¿Le sirve al negocio? | business viability |

Fuentes secundarias reparten los riesgos entre los roles del trío: el product manager responde por valor y viabilidad, el diseñador por usabilidad y el líder técnico por factibilidad. Es una interpretación común que no se confirmó en Cagan. Los roles están en [roles de producto](../Organizacion/roles-de-producto.md).

La viabilidad de negocio se cruza con [Monetización](../Monetizacion/monetizacion.md), donde se decide cómo cobra el producto.

## De tres riesgos a cuatro

Cagan enseñó primero tres riesgos: valor, usabilidad y factibilidad, los de la primera edición de *Inspired* (2008). En la segunda edición (2017 o 2018, según la fuente) dividió el valor en dos: valor para el cliente y viabilidad de negocio. Así llegó a cuatro (SVPG, "Product Risk Taxonomies", 2023).

Cagan admite el costo del cambio. Para enseñar, "it really is better to have 3 items rather than 4"; pero concluye que "it's worth the extra cognitive load to have the four risk taxonomy". La lectura de esta base: separar la viabilidad obliga a preguntar por el negocio aunque el cliente esté encantado.

## Cómo se compara con IDEO, Bland y Torres

Otras escuelas cortan el mismo terreno de otra manera. La diferencia más útil de ver es dónde queda la usabilidad y dónde la ética.

| Escuela | Categorías | Dónde queda la usabilidad | Dónde queda la ética | Fuente |
|---|---|---|---|---|
| IDEO | Deseabilidad, viabilidad, factibilidad | Dentro de la deseabilidad, que junta valor y usabilidad | No aparece en lo investigado | Cagan, SVPG 2023 |
| Cagan | Valor, usabilidad, factibilidad, viabilidad de negocio | Riesgo propio | Dentro de la viabilidad de negocio; en 2024 dijo que hay un argumento para separarla | SVPG 2023; Huryn, vía buscador |
| Bland (Strategyzer) | Deseable, viable, factible (los colores del mapeo de supuestos) | No figura como categoría | No figura | Strategyzer, vía buscador |
| Torres | Desirability, viability, feasibility, usability, ethical | Categoría propia | Categoría propia: "Is there any potential harm in building this solution?" | Product Talk, "Assumption testing" |

Según Cagan, la taxonomía de IDEO encaja mejor en productos de consumo que en productos de negocio. Torres usa sus cinco categorías para generar supuestos, no para clasificarlos: importa menos en qué categoría cae un supuesto que generar supuestos de las cinco. Cómo se usan esas categorías en la práctica está en [prueba de supuestos](prueba-de-supuestos.md).

Las diferencias no son un desacuerdo de fondo. Según el resumen del buscador del artículo de SVPG, Cagan dice que cualquier taxonomía sirve para no olvidarse de nada; la frase "any taxonomy beats none" que circula es del buscador, no literal.

## La trampa de la palabra "viabilidad"

"Deseabilidad" (IDEO, Bland, Torres) y "valor" (Cagan) son casi lo mismo. "Viabilidad" en IDEO y Bland, y "viabilidad de negocio" en Cagan, también. El problema es que en inglés "viability" se usa para las dos cosas. En esta base, viabilidad es siempre la del negocio, y factibilidad la técnica.

## Cómo falla

> [!IMPORTANT]
> No hay estudio que muestre que trabajar con los cuatro riesgos reduzca los fracasos, ni una crítica con método al marco (por ejemplo, que no ayude a priorizar entre riesgos). Es un marco de practicante, no un resultado empírico. Su apoyo indirecto (lectura de esta base) es la evidencia de que las ideas fallan seguido y que los expertos se equivocan al predecir cuáles van a funcionar, citada en la [entrada del tema](../producto.md#la-idea-que-cruza-todo-el-tema).

El informe de esta base lee en Cagan que la usabilidad se prueba con prototipos funcionales y no describiendo la idea, pero no lo verificó en el texto de *Inspired*. Cómo se hace un test con personas está en [test de usabilidad](../../UX/Evaluacion/test-de-usabilidad.md), del tema UX.

## Qué leer

Primero Cagan, [Product Risk Taxonomies](https://svpg.com/product-risk-taxonomies), corto, primario y con las tres taxonomías. Después *Inspired* (2.ª ed.), la sección de descubrimiento, donde los cuatro riesgos se atacan antes de construir y se explica por qué Cagan separó la viabilidad del valor.

> [!NOTE]
> Sin fuente todavía: el texto del capítulo 33 de *Inspired*, con las preguntas literales de cada riesgo y el reparto entre roles.
