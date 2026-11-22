---
resumen: >-
  El encaje producto-mercado es estar en un buen mercado con un producto que lo satisface: el punto en que los clientes tiran del producto en lugar de que la empresa tenga que empujarlo. Se reconoce por la demanda y por una curva de retención que se aplana.
estado: borrador
estabilidad: estable
fuentes:
  - "Marc Andreessen, The Pmarca Guide to Startups, Part 4: The only thing that matters (2007-06-25): https://pmarchive.com/guide_to_startups_part4.html"
  - "First Round Review, How Superhuman built an engine to find product/market fit (entrevista a Rahul Vohra; cita a Sean Ellis): https://review.firstround.com/how-to-measure-product-market-fit/"
  - "CRV, Product-market fit survey: https://www.crv.com/content/product-market-fit-survey"
  - "Sequoia Data Science, Retention: https://articles.sequoiacap.com/retention"
  - "a16z, AI retention benchmarks (según resumen): https://a16z.com/ai-retention-benchmarks/"
  - "Wikipedia, Product/market fit: https://en.wikipedia.org/wiki/Product/market_fit"
  - "Giff Constable, Product-Market Fit is an Illusion (2018-11-14): https://giffconstable.com/?p=2660"
  - "Andy Rachleff, según Stanford GSB: https://www.gsb.stanford.edu/insights/andy-rachleff-democratizing-investment-business"
  - "Strategyzer, The Value Proposition Canvas: https://www.strategyzer.com/library/the-value-proposition-canvas"
  - "Emprender/.investigacion/crecimiento-y-modelo.md"
aliases: [product-market fit, product/market fit, PMF, ajuste producto-mercado, prueba de Ellis, Sean Ellis test]
creado: 2026-11-22
revisado:
---

# Encaje producto-mercado

El encaje producto-mercado es estar en un buen mercado con un producto que lo satisface: el punto en que los clientes tiran del producto en lugar de que la empresa tenga que empujarlo. Se reconoce por la demanda y por una curva de retención que se aplana.

Es la frontera entre las dos partes de la [vertical de Crecimiento](crecimiento.md): antes, la empresa busca un modelo que funcione; después, prueba cómo crecer con un [motor de crecimiento](motores-de-crecimiento.md).

## La definición de Andreessen

Marc Andreessen fijó el término en 2007: «Product/market fit means being in a good market with a product that can satisfy that market». La definición tiene dos mitades, el mercado y el producto. Andreessen atribuye la idea a Andy Rachleff, de quien toma la «Rachleff's Law of Startup Success»: lo que más mata startups es la falta de mercado.

De ahí saca su corolario: «The only thing that matters is getting to product/market fit». Rachleff, según un resumen de Stanford GSB, lo dice en los términos de las [hipótesis de salto de fe](../Validacion/hipotesis-de-salto-de-fe.md): el encaje es haber probado la hipótesis de valor, y recién después se prueba la de crecimiento.

## Cómo se siente estar con encaje y sin él

Andreessen describe las dos situaciones por lo que pasa con la demanda.

| Sin encaje | Con encaje |
|---|---|
| «The customers aren't quite getting value out of the product» | «The customers are buying the product just as fast as you can make it» |
| «word of mouth isn't spreading» | «Money from customers is piling up in your company checking account» |

A Rachleff se le atribuye una versión más corta, que dan resúmenes de entrevistas y no un texto propio: «If the customer doesn't scream, you don't have product-market fit».

## La prueba de Ellis

Sean Ellis propuso medir el encaje con una pregunta a los usuarios: «how would you feel if you could no longer use the product?». Las respuestas posibles son «very disappointed», «somewhat disappointed» y «not disappointed». Según First Round, Ellis dijo que «after benchmarking a hundred startups», «the magic number is 40%»: con al menos 40% de «very disappointed» hay encaje.

Superhuman la usó como método, según la entrevista de First Round a Rahul Vohra. Encuestó solo a quienes habían usado el producto «at least twice in the last two weeks», y tenía entre 100 y 200 usuarios para encuestar. Vohra dice que unos 40 respondientes ya dan una señal direccional.

CRV la presenta como un piso y no como una regla: «Companies struggling to grow tend to score below 40 percent, while companies gaining strong traction tend to exceed it».

> [!IMPORTANT]
> El respaldo del 40% está en disputa. A favor: Ellis lo sacó de comparar unas cien startups, según First Round, y CRV lo usa como heurística. En contra: el conjunto de datos nunca se publicó, Wikipedia marca la cifra con «citation needed», y las fuentes dicen «un centenar», «más de cien» o «cientos». No se encontró un estudio publicado que valide el umbral.

## La curva de retención que se aplana

La señal en los datos es la [curva de retención](../../Datos/Lectura-de-cohortes/curva-de-retencion.md) por cohorte. Según Sequoia, «When a product has not achieved product-market fit, the retention curve will continuously decline». Cuando hay encaje, la curva deja de caer y se aplana: «The higher the level at which the curve flattens, the higher the long-term retention and the healthier the product».

Cuánto tarda en aplanarse depende del producto. Según un resumen de los benchmarks de a16z para productos de IA, la curva «most often begins to flatten around M3», y en algunos casos aparece una curva en sonrisa, con usuarios que vuelven. Cómo se calcula la pérdida de clientes que hace caer la curva está en [churn](../../Datos/Retencion-y-churn/churn.md).

> [!NOTE]
> Sin fuente todavía: umbrales de aplanamiento para B2B o SaaS, y evidencia publicada que vincule la retención con el encaje más allá de lo que afirman los inversores.

## El encaje en las etapas de Blank

Según Wikipedia, que cita a Blank, el encaje cae entre la validación de clientes y la creación de clientes, el segundo y el tercer paso del desarrollo de clientes. La validación termina, según resúmenes del libro de Blank y Dorf (2012), cuando hay una hoja de ruta de ventas probada con clientes que pagan. Esa es la versión operativa del encaje: el cliente compra de forma repetible.

## Las críticas al encaje como meta

**No es binario.** Giff Constable (2018) sostiene que «In most cases, product-market fit is not a binary flag that gets set to 'true'». Y agrega: «It's an ephemeral thing». El encaje se puede perder, en el mercado general o en un segmento.

**Suele ser de un segmento.** Un glosario, según un resumen, sostiene que la mayoría de las empresas que dicen tener encaje lo tienen en un segmento y no en todo el mercado. Cómo se elige ese primer segmento está en [tamaño de mercado](../Validacion/tamano-de-mercado.md).

**El crecimiento pagado engaña.** Rachleff advierte, según una afirmación sin cita de Wikipedia, que el crecimiento pagado da una falsa confianza de haber llegado al encaje. Un resumen del libro de Ries pone el motor pagado después de los otros dos, porque gastar en adquisición antes es ineficiente; está en [motores de crecimiento](motores-de-crecimiento.md).

Wikipedia también afirma, sin cita, que un nivel mínimo de encaje no alcanza y hace falta un encaje extremo.

## Encaje de la propuesta no es encaje producto-mercado

La palabra «fit» también aparece en el Value Proposition Canvas de Osterwalder, con otro sentido. Ahí el encaje es la coincidencia entre el perfil del cliente (tareas, dolores, ganancias) y el mapa de valor de la oferta, y Strategyzer avisa que «Fit is a claim until customers confirm it». Ese encaje se da entre la [propuesta](../../Marketing/Propuesta/propuesta.md) y el cliente; el de Andreessen se da entre el producto y el mercado, y se ve en la demanda.

## Andreessen, Sequoia y Blank en el original

Andreessen (2007) es corto y se lee entero: fijarse en las dos mitades de la definición y en que la señal es de demanda. Sequoia, «Retention», para reconocerlo en los datos: fijarse en el nivel donde la curva se aplana. Para la versión de Blank, el capítulo Customer Validation de The Startup Owner's Manual: fijarse en el criterio de salida.
