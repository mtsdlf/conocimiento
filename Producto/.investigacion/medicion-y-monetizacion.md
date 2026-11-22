# Investigación: Medición y Monetización (Producto)

Marcas: [L] texto completo abierto, [M] metadatos/abstract, [S] resumen secundario o del buscador. Puntajes 1-3: Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Las páginas web se abrieron con una herramienta que devuelve un resumen de la página; los PDF del paper de Google y de Kohavi no se pudieron leer (binario comprimido), por eso van como [M]/[S]. No se encontró primaria abierta para varias afirmaciones: están declaradas en Huecos.

## Observación sobre la división del árbol

- Medición/ (north-star, activacion, experimento-ab) se sostiene. HEART y AARRR son marcos de métricas: conviene una nota breve de "marcos de métricas" dentro de Medición (o una sección en north-star), no notas propias. AARRR además se solapa con Marketing (embudo) y con Emprender (Lean Analytics); HEART se solapa con UX. En Medición van como mapas para elegir métricas, con enlace afuera.
- Monetizacion/ queda bien con dos notas, pero "métrica de valor" (por asiento, uso, resultado) es el nudo de pricing-y-empaquetado, y los datos de usage-based están sesgados a SaaS B2B de venture capital (ver abajo). Los límites: take rate de plataforma -> Plataformas/; PLG como canal -> Marketing; economía unitaria -> Marketing; cohortes/churn -> Datos; incrementalidad -> Marketing.

## 1. north-star

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Amplitude, "North Star Playbook" https://amplitude.com/books/north-star/about-north-star-framework | secundaria (vendor de analítica) | 2/2/2/2 | [M] (solo la introducción; los capítulos no se abrieron) |
| Amplitude, "What Makes a Good vs Bad North Star Metric" https://www.amplitude.com/blog/good-bad-north-star-metric | secundaria | 2/2/2/1 | [L] |
| Amplitude, "North Star, inputs, flywheels" https://amplitude.com/resources/north-star-inputs-flywheels | secundaria | 2/1/1/1 | [S] |

Afirmaciones
- Criterios de una buena North Star según Amplitude: "A good North Star Metric represents what customers value about your product"; "Your North Star should be something you can influence or change"; debe ser indicador adelantado de ingresos. https://www.amplitude.com/blog/good-bad-north-star-metric
- Mala North Star: indicadores rezagados ("MRR or ARPU") y métricas de vanidad, que "look great on the surface but don't translate to meaningful business outcomes"; ejemplos que Amplitude da como malos: DAU, usuarios registrados, páginas vistas, impresiones, tiempo en página. https://www.amplitude.com/blog/good-bad-north-star-metric
- Cita de John Cutler: "If you can move your North Star directly, it's probably not a good North Star". https://www.amplitude.com/blog/good-bad-north-star-metric
- El playbook trata las métricas de entrada (inputs) como parte central, "often overlooked", y dependientes del negocio. https://amplitude.com/resources/north-star-inputs-flywheels [S]
- Aviso del propio playbook: "there are no silver bullets to success". https://amplitude.com/books/north-star/about-north-star-framework
- Contradicción a anotar: Amplitude descarta DAU, pero en muchos productos de consumo es la métrica que otros usan como North Star; la lista de "malas" es posición del vendor, no consenso.
- Crítica (Goodhart, "cuando una medida se vuelve objetivo deja de ser buena medida"): no encontré fuente primaria abierta; hueco.

Recurso canónico propuesto: el North Star Playbook de Amplitude, capítulos sobre definición e inputs (contiene el ejemplo de inputs y el cuándo cambiar la métrica). Fijarse en: la separación entre la métrica y los inputs que el equipo sí mueve. Es de un vendor.

## 2. activacion

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Andrew Chen, respuesta en Quora sobre cómo se encuentra algo como "7 friends in 10 days" https://andrewchen.com/my-quora-answer-to-how-do-you-find-insights-like-facebooks-7-friends-in-10-days-to-grow-your-product-faster/ | secundaria (practicante) | 2/2/2/2 | [L] |
| 25iq, "A dozen lessons on growth" (resumen de la charla de Chamath) https://25iq.com/2017/02/10/a-dozen-lessons-on-growth | secundaria | 1/1/2/1 | [S] |
| Caroline Frost, "Facebook's 7 friends metric is dead" https://carolinefrost.github.io/2021/11/16/facebooks-7-friends-metric-is-dead | secundaria (blog) | 1/1/1/1 | [S] |
| Reforge (setup/aha/habit) y Bush, Product-Led Growth (onboarding) | — | — | no abiertas; hueco |

Afirmaciones
- Origen de "7 amigos en 10 días": según los relatos de Chamath, el equipo de crecimiento comparó usuarios que se engancharon con los que no, y los comprometidos habían llegado a 7 amigos en 10 días. https://25iq.com/2017/02/10/a-dozen-lessons-on-growth [S]
- No encontré documento primario de Facebook; los relatos difieren (una fuente dice que Naomi Gleit dudó entre "7 friends in 10 days" y "10 friends in 14 days"). https://www.growthtalent.org/insights/naomi-gleit-on-meta-s-early-growth-playbook-and-the-power-of-disagre [S] -> cifra famosa sin origen verificable.
- Método y límite según Chen: definir la métrica de éxito, ver qué comportamientos correlacionan, formular una hipótesis y probarla con un A/B; advierte "fire engines correlate with house fires, but that doesn't mean that fire engines CAUSE house fires". Dice además que el número exacto importa menos que tener una meta memorable ("10 friends in 12 days" serviría). https://andrewchen.com/my-quora-answer-to-how-do-you-find-insights-like-facebooks-7-friends-in-10-days-to-grow-your-product-faster/
- Críticas (blogs [S]): el umbral es arbitrario y correlacional; duplicar de 7 a 14 conexiones difícilmente duplica el valor. https://carolinefrost.github.io/2021/11/16/facebooks-7-friends-metric-is-dead

Recurso canónico propuesto: el texto de Chen (breve, abierto) para el método y su advertencia sobre causalidad; y el capítulo de onboarding de Wes Bush, Product-Led Growth (2019) -- no verificado, ver huecos. Límite: usabilidad del onboarding -> UX; cohortes de retención -> Datos; encaje producto-mercado -> Emprender.

## 3. experimento-ab

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Kohavi, Tang, Xu, Trustworthy Online Controlled Experiments (Cambridge UP, 2020), ficha y extracto https://assets.cambridge.org/97811087/24265/frontmatter/9781108724265_frontmatter.pdf | primaria (libro) | 3/3/3/3 | [M] (portada e índice; el cuerpo no se pudo leer) |
| Cambridge, cap. 3 "Twyman's Law and Experimentation Trustworthiness" https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/twymans-law-and-experimentation-trustworthiness/886425EC1B92BD23A0DC5E6817785190 | primaria | 3/3/2/2 | [M] |
| Kohavi et al., "Power Analysis is Essential" (arXiv, 2025) https://arxiv.org/pdf/2512.24521 | primaria (paper) | 3/2/2/2 | [S] (solo fragmentos del buscador) |

Afirmaciones
- El libro se basa en experiencia de empresas que corren más de 20.000 experimentos controlados cada una (según el frontmatter, vía buscador). https://assets.cambridge.org/97811087/24265/frontmatter/9781108724265_frontmatter.pdf [S]
- El índice lista guardrail metrics (ejemplos: tasa de escritura de cookies, latencia) y poder estadístico. https://assets.cambridge.org/97811087/24265/index/9781108724265_index.pdf [S]
- Ley de Twyman: cualquier cifra que parezca interesante o distinta suele estar mal; mirar el p-valor repetidamente (peeking) es prueba de hipótesis múltiple y sube el error tipo I. https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/twymans-law-and-experimentation-trustworthiness/886425EC1B92BD23A0DC5E6817785190 [S, parafraseado por el buscador]
- Kohavi cuenta en un documento propio que "probably 9 out of 10 times we found an issue that invalidated the result" ante resultados sorprendentes. https://docs.google.com/document/d/1IDcLEr58QoQU2VJPc-TefLMLegdQMnh3/mobilebasic [S, no es el libro]
- Para efectos chicos, la mayoría de las organizaciones no tiene poder estadístico suficiente (según el resumen del buscador de un paper de 2025 de Kohavi y coautores). https://arxiv.org/pdf/2512.24521 [S]
- Límite con Marketing: el A/B de producto compara variantes de una experiencia; la incrementalidad (efecto causal de un canal o campaña) vive en Marketing y se enlaza, no se explica acá.
- Tráfico mínimo concreto y "cuándo no sirve" (B2B chico, consultora con pocos usuarios): no se verificó en el libro; hueco. Alternativa lógica a nombrar sin cifra: pruebas de supuestos de Descubrimiento y entrevistas, que ya están en el árbol.

Recurso canónico propuesto: Kohavi, Tang y Xu, Parte I (cap. 1 a 3, introducción, vocabulario, Twyman) y los capítulos de poder y de métricas guardrail. Fijarse en la distinción métrica de objetivo / guardrail / de calidad de datos y en el chequeo SRM. Es el único texto con método de esta vertical.

## 4. Marcos de métricas (HEART, AARRR)

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Rodden, Hutchinson, Fu, "Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications", CHI 2010, pp. 2395-2398, DOI 10.1145/1753326.1753687 https://research.google/pubs/pub36299/ | primaria (paper) | 3/2/2/3 | [M] |
| McClure, "Startup Metrics for Pirates: AARRR!", Ignite Seattle 4 https://webarchive.library.unt.edu/dentonfracking/20141206040342/http://igniteshow.com/videos/startup-metrics-pirates-aarrr | primaria (charla; solo ficha) | 2/1/1/3 | [M] |
| Amplitude, "AARRR: Come Aboard the Pirate Metrics Framework" https://www.amplitude.com/blog/pirate-metrics-framework.md | secundaria | 1/2/2/1 | [S] |

Afirmaciones
- HEART = Happiness, Engagement, Adoption, Retention, Task success; el paper incluye un proceso para pasar de metas a métricas y ejemplos de equipos de Google; los autores esperan que otras organizaciones puedan reusarlo. https://research.google/pubs/pub36299/ [M]
- AARRR: adquisición, activación, retención, referencia, ingresos; presentado en Ignite Seattle 4 en 2007 según una fuente; otra dice que el modelo es de principios de los 2000, así que la fecha es discutida. https://builtin.com/growth-hacking/aarrr [S]; https://www.shopify.com/blog/aarrr-metrics [S]
- Pertenencia: HEART mide experiencia de usuario con métricas de producto (cruce con UX); AARRR es embudo de crecimiento (cruce con Marketing y Emprender). Propuesta: ambos en Medición como una nota de "marcos de métricas", con aclaración de a quién sirve cada uno.

Recurso canónico propuesto: el paper de HEART (4 páginas; mirar la tabla de metas, señales y métricas, y la advertencia de que no todas las letras aplican a todo producto -- no verificada en el texto).

## 5. pricing-y-empaquetado

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Ramanujam y Tacke, Monetizing Innovation (Wiley, 2016), TOC https://ebooks.mpdl.mpg.de/ebooks/Record/EB001935873/TOC | primaria (libro de practicantes, posición de escuela) | 2/3/3/3 | [M] |
| First Round Review, entrevista a Ramanujam "It's price before product, period" https://review.firstround.com/its-price-before-product-period.md | secundaria (entrevista al autor) | 2/2/3/2 | [L] |
| OpenView/Poyar, "State of Usage-Based Pricing" https://openviewpartners.com/blog/state-of-usage-based-pricing/ y cobertura de TechCrunch https://techcrunch.com/2023/02/02/usage-based-pricing-is-rising-but-not-replacing-other-models/ | secundaria (encuesta de un fondo) | 1/2/2/2 | [S] |
| Van Westendorp's Price Sensitivity Meter (Wikipedia, con referencias) https://en.wikipedia.org/wiki/Van_Westendorp%27s_Price_Sensitivity_Meter | secundaria | 1/2/1/1 | [S] |

Afirmaciones
- Tesis: "Most companies postpone pricing decisions until after the product is developed"; el libro propone diseñar el producto alrededor del precio. https://review.firstround.com/its-price-before-product-period.md
- Disposición a pagar: preguntarla al inicio ("Ask at the onset whether or not people would pay for the product you intend to develop"), con tres preguntas (precio aceptable, caro, prohibitivamente caro); existen "price cliffs" donde la demanda cae de golpe. https://review.firstround.com/its-price-before-product-period.md
- Cifra: "72% of these innovations did not meet their revenue or profit targets, or even failed completely" (estudio de Simon-Kucher de 2014 citado en la entrevista). https://review.firstround.com/its-price-before-product-period.md. Otras fuentes dicen "nearly three-quarters" o "about 75%", así que la cifra varía según quién la repite. https://www.getabstract.com/fr/resume/monetizing-innovation/28430 [S]
- Métrica de valor, ejemplo literal: cobrar a flotas por "the mileage they drove their Michelin tires, not by the number of tires bought". La entrevista no usa el término "value metric" ni "good-better-best"; recomienda empezar con 3-4 segmentos y expandir: "Start with 3-4 segments, then expand gradually". https://review.firstround.com/its-price-before-product-period.md
- Van Westendorp (1976): cuatro preguntas (demasiado barato, barato, caro, demasiado caro); críticas de sesgo hipotético y sensibilidad al rango testeado, pero de fuentes débiles (blog y un documento de patente); la extensión de intención de compra es de Newton, Miller y Smith (1993). https://en.wikipedia.org/wiki/Van_Westendorp%27s_Price_Sensitivity_Meter [S]
- Pricing por uso: la encuesta de OpenView de 2023 (600 empresas SaaS) dice que cerca de 61% usa alguna forma de precio por uso (45% en 2021, 34% en 2020), y que muchas lo combinan con suscripción en lugar de reemplazarla. https://techcrunch.com/2023/02/02/usage-based-pricing-is-rising-but-not-replacing-other-models/ [S]. Sesgo: muestra de SaaS de un fondo de inversión, no de pymes ni de servicios; la página original no se pudo abrir (redirige a la home).
- Take rate de plataforma: no investigado, límite con Plataformas/.

Recurso canónico propuesto: Ramanujam y Tacke, Monetizing Innovation, partes sobre disposición a pagar, y sobre modelo de precios y empaquetado. Fijarse en que es posición de escuela y que su dato central (72%) es de una consultora que vende pricing. Complemento abierto: la entrevista de First Round.

## 6. freemium-y-prueba-gratuita

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Rachitsky y Poyar, "What is a good free-to-paid conversion rate?" https://lennysnewsletter.com/p/what-is-a-good-free-to-paid-conversion | secundaria (newsletter, encuesta propia) | 2/2/2/3 | [S] (parte pública; el resto es de pago) |
| Kumar, "Making 'Freemium' Work", HBR, mayo 2014, vol. 92 n.º 5, pp. 27-29 https://hbr.org/2014/05/making-freemium-work | primaria (HBR) | 3/1/2/2 | [M] (solo la entrada; no se abrió el texto) |
| ProductLed (Bush), "Free trial vs freemium" https://productled.com/blog/free-trial-vs-freemium | secundaria (marketing del autor) | 1/2/2/2 | [S] |
| Bush, Product-Led Growth (2019) | primaria (libro) | — | no abierto |
| Freemium como estrategia para firmas dominantes (Marketing Science) https://pubsonline.informs.org/doi/references/10.1287/mksc.2018.1109 | primaria (paper) | 3/-/-/3 | [M] (solo referencias) |

Afirmaciones
- Benchmarks de Rachitsky y Poyar (1.000+ productos, "focused on B2B SaaS"): freemium autoservicio "3%-5% is a GOOD conversion rate... and 6%-8% is GREAT"; prueba gratuita 8-12% buena, 15-25% muy buena; con ventas asistidas, 5-7% buena y 10-15% muy buena. Definición: porcentaje de cuentas nuevas que pagan en los primeros 6 meses. https://lennysnewsletter.com/p/what-is-a-good-free-to-paid-conversion
- Sesgos y límites declarados: pocas empresas publican sus tasas; ventana de seis meses; cuentas más grandes convierten menos; las de desarrolladores tienen mediana de 5%, la mitad que el resto. https://lennysnewsletter.com/p/what-is-a-good-free-to-paid-conversion
- Discrepancia: otra fuente (CrazyEgg citando FirstPageSage) invierte los rangos (trial 3-5%, freemium 8-12%). Es secundaria y contradice la fuente directa; se da la de Rachitsky y se anota la otra. https://www.crazyegg.com/blog/free-to-paid-conversion-rate/
- Kumar (HBR 2014): el equilibrio entre pocas y demasiadas funciones gratis; una fuente secundaria le atribuye ~5% de conversión óptima, no verificado contra el artículo. https://hbr.org/2014/05/making-freemium-work [M]; https://builtin.com/articles/freemium [S]
- Bush y el modelo MOAT: según resúmenes, Market strategy, Ocean, Audience, Time to value, para decidir entre prueba gratuita, freemium o demo; parte del detalle está en cursos pagos. En su artículo más reciente sostiene que importa menos elegir modelo que qué se incluye gratis y si el usuario llega a valor; un artículo anterior defendía la ventaja del freemium. Dos posiciones del mismo autor. https://productled.com/blog/free-trial-vs-freemium [S]; https://productled.com/blog/freemium-vs-free-trial [S]
- Límite con Marketing: PLG como canal de adquisición no se desarrolla acá; en esta nota solo la decisión de producto/modelo de oferta (qué se da gratis).

Recurso canónico propuesto: el artículo de Rachitsky y Poyar (benchmarks, leyendo los caveats) y Kumar en HBR (3 páginas) para el mecanismo; Bush, Product-Led Growth, capítulo del modelo de crecimiento, como posición de escuela.

## Huecos

- Capítulos del North Star Playbook (definición, inputs, cuándo cambiar): solo introducción abierta; el resto por buscador.
- Goodhart/métricas de vanidad: sin fuente primaria (Strathern/Goodhart); Ries sobre vanidad vive en Emprender.
- Activación: no se abrieron Reforge ni Bush; "aha moment" y setup/aha/habit sin fuente verificada. La cifra "7 amigos en 10 días" no tiene documento primario.
- Kohavi et al.: el cuerpo del libro no se pudo leer (PDF binario); faltan tráfico mínimo, poder, peeking y guardrails citados literalmente; tampoco su aplicabilidad a B2B chico.
- Paper HEART: solo abstract; definiciones literales de cada letra sin leer. McClure: ficha, no las diapositivas.
- Pricing: Van Westendorp sin fuente primaria; "good-better-best" y "value metric" sin fuente de Ramanujam o de Simon-Kucher; reporte de OpenView sin abrir en origen. Evidencia sobre pricing para pymes, agencias o consultoras: no encontrada (todo es SaaS de venture capital).
- Freemium: texto de Kumar y de Bush sin abrir; no hay estudios sobre freemium en comercio electrónico ni ecosistemas de apps.
