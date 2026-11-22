---
resumen: >-
  La activación es el momento en que un usuario nuevo llega por primera vez al valor del producto, y la métrica de activación es la acción o el umbral que lo marca. Se busca comparando qué hicieron al principio los usuarios que se quedaron y los que se fueron, y se confirma probando si provocar ese comportamiento retiene más.
estado: vigente
estabilidad: semi
fuentes:
  - "Andrew Chen, My Quora answer to: How do you find insights like Facebook's 7 friends in 10 days: https://andrewchen.com/my-quora-answer-to-how-do-you-find-insights-like-facebooks-7-friends-in-10-days-to-grow-your-product-faster/"
  - "25iq, A dozen lessons on growth (resumen de la charla de Chamath Palihapitiya; vía buscador): https://25iq.com/2017/02/10/a-dozen-lessons-on-growth"
  - "Growth Talent, Naomi Gleit on Meta's early growth playbook (vía buscador): https://www.growthtalent.org/insights/naomi-gleit-on-meta-s-early-growth-playbook-and-the-power-of-disagre"
  - "Caroline Frost, Facebook's 7 friends metric is dead (2021; vía buscador): https://carolinefrost.github.io/2021/11/16/facebooks-7-friends-metric-is-dead"
  - "Producto/.investigacion/medicion-y-monetizacion.md"
aliases: [activation, métrica de activación, activation metric, aha moment, momento ajá]
creado: 2026-11-22
revisado: 2026-11-22
---

# Activación

La activación es el momento en que un usuario nuevo llega por primera vez al valor del producto, y la métrica de activación es la acción o el umbral que lo marca. Se busca comparando qué hicieron al principio los usuarios que se quedaron y los que se fueron, y se confirma probando si provocar ese comportamiento retiene más.

Es la segunda letra del embudo AARRR, entre la adquisición, que es de Marketing, y la retención (ver [Medición](medicion-de-producto.md#heart-y-aarrr-dos-mapas-para-elegir-metricas)). Dentro de la medición, la [North Star](north-star.md) dice si el producto entrega valor en conjunto; la activación dice si los que recién llegan alcanzan ese valor. Por eso la métrica de activación se elige y se valida contra la [retención](../../Datos/Retencion-y-churn/retencion.md).

## Cómo se encuentra una métrica de activación

Andrew Chen describe el método en una respuesta abierta y breve. Son cuatro pasos:

1. Definí la métrica de éxito (para la base, lo habitual es si el usuario sigue usando el producto tiempo después; Chen, en lo que se leyó, no lo precisa).
2. Buscá qué comportamientos tempranos se correlacionan con ese éxito. Comparar grupos de usuarios por una acción que hicieron es una [cohorte de comportamiento](../../Datos/Cohortes/cohorte-de-comportamiento.md), que se arma con la técnica de Datos.
3. Formulá una hipótesis: si más usuarios hacen esa acción al principio, más se van a quedar.
4. Probala con un [experimento A/B](experimento-ab.md): empujá a una parte de los usuarios hacia esa acción y compará la retención con la del grupo de control.

Chen advierte sobre la causalidad: "fire engines correlate with house fires, but that doesn't mean that fire engines CAUSE house fires". Que los usuarios retenidos hayan hecho algo al principio no prueba que hacerlo los retenga (lectura de la base: puede que ya fueran los más interesados). Solo el experimento separa la causa de la coincidencia.

Chen agrega que el número exacto importa menos que tener una meta memorable para el equipo: "10 friends in 12 days" serviría igual. Para él, la métrica es una meta que orienta al equipo.

## El mito de "7 amigos en 10 días"

"7 amigos en 10 días" es la métrica de activación más citada del campo, y no tiene un origen verificable. El relato, según el resumen de una charla de Chamath Palihapitiya, es que el equipo de crecimiento de Facebook comparó a los usuarios que se engancharon con los que no, y encontró que los comprometidos habían llegado a 7 amigos en 10 días.

No hay un documento primario de Facebook que lo sostenga. Los relatos difieren: según una fuente secundaria, Naomi Gleit dudó entre "7 friends in 10 days" y "10 friends in 14 days". La cifra circula como si fuera un hallazgo, pero lo que se conoce de ella es una anécdota contada en charlas.

> [!WARNING]
> La cifra es una correlación, no una causa. Que los usuarios que se quedaron tuvieran 7 amigos a los 10 días no prueba que conseguirles 7 amigos los retenga. Críticas de blogs, leídas por el buscador, agregan que el umbral es arbitrario y que duplicar de 7 a 14 conexiones difícilmente duplica el valor. Copiar el número a otro producto no tiene sostén, porque ni siquiera en el original está probado como causa. El mito está también en [Mitos de producto](../Fundamentos/mitos-de-producto.md).

## Dónde termina la activación

La activación mide si el usuario llegó al valor; no diseña el camino. Que el onboarding se pueda usar sin trabas lo resuelve y lo evalúa [UX](../../UX/Evaluacion/evaluacion.md). Cómo se arman y leen las cohortes de retención es de [Datos](../../Datos/Retencion-y-churn/retencion-y-churn.md). Si el producto resuelve un problema por el que el mercado paga es el [encaje producto-mercado](../../Emprender/Crecimiento/encaje-producto-mercado.md), de Emprender: sin ese encaje, ninguna métrica de activación lo compensa.

En un producto con prueba gratuita o freemium, Wes Bush sostiene, según resúmenes de su blog, que importa sobre todo si el usuario llega al valor. Esa relación está en [freemium y prueba gratuita](../Monetizacion/freemium-y-prueba-gratuita.md).

> [!NOTE]
> Sin fuente todavía: el "aha moment" y el modelo setup, aha y hábito de Reforge, y el capítulo de onboarding de Wes Bush en *Product-Led Growth* (2019). No se abrieron, y por eso la nota no los desarrolla.

## Leer a Chen

La [respuesta de Andrew Chen](https://andrewchen.com/my-quora-answer-to-how-do-you-find-insights-like-facebooks-7-friends-in-10-days-to-grow-your-product-faster/) es corta y abierta. Conviene fijarse en el orden de los pasos y en la advertencia sobre causalidad, que se pierden cuando se repite la cifra de Facebook. Es la opinión de un practicante, no un estudio.
