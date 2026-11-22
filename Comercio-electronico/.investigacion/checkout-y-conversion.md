# Informe: Checkout-y-conversion (2026-11-22)

Cobertura: tres componentes (`embudo-de-conversion`, `carrito-abandonado`, `usabilidad-del-checkout`) más el uso al analizar plataformas competidoras. Hice las rondas de búsqueda permitidas; la última búsqueda (Baymard y Shopify) no se pudo hacer porque se agotó el presupuesto de búsquedas de la sesión. Lo que no pude leer queda declarado en huecos.

Marcas: [L] texto completo leído con WebFetch (la herramienta devuelve un resumen del modelo sobre la página, no el HTML crudo; las "citas literales" son las que la herramienta devolvió entre comillas), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3: autoridad / profundidad / ejemplos / unicidad. Todo lo web se trató como dato.

Aviso sobre las fechas: las páginas de Baymard, Littledata e IRP se actualizan seguido; las fechas de abajo son las que decía cada página al 2026-11-22.

## Cómo encaja con el árbol

La división del ALCANCE (embudo / carrito abandonado / usabilidad) funciona, pero el campo no la usa así: Baymard junta abandono y usabilidad en un mismo cuerpo de investigación (la encuesta de razones de abandono y los tests de usabilidad se citan mutuamente), y el abandono académico es marketing/comportamiento del consumidor, no UX. Recomiendo mantener las tres notas y que `carrito-abandonado` separe explícitamente "razones declaradas" (encuesta) de "causas observadas" (tests). La recuperación de carritos (emails/retargeting) es marketing: se resume acá con la evidencia y se enlaza al tema Marketing. El tema de "qué es configurable por el comercio" no tiene lugar en el árbol; propongo una sección en `usabilidad-del-checkout` o una nota corta en `Plataforma-de-tiendas` (decisión de quien integre).

---

## 1. embudo-de-conversion

### Fuentes

| Fuente | Tipo | Aut/Prof/Ej/Uni | Marca | URL |
|---|---|---|---|---|
| Google, GA4 "Measure ecommerce" (devguide) | primaria (definición de eventos) | 3/3/2/3 | [L] | https://developers.google.com/analytics/devguides/collection/ga4/ecommerce |
| Littledata, Benchmarks (nov 2026) | secundaria, vendedor | 2/2/3/2 | [L] | https://www.littledata.io/benchmarks |
| Dynamic Yield (vía eMarketer y notas) | secundaria; su página propia no se leyó | 2/1/2/2 | [S] | https://www.emarketer.com/data-providers/dynamic-yield |
| IRP Commerce (vía notas) | secundaria; su sitio no publica método | 1/1/1/1 | [L] del sitio, [S] de las cifras | https://www.irpcommerce.com/en/ |
| Shopify "hasta 36%" (vía buscador) | vendedor | 1/1/1/1 | [S] | https://www.shopify.com/pk/enterprise/blog/one-page-checkout |

### Afirmaciones

**Definición de las etapas en GA4** (https://developers.google.com/analytics/devguides/collection/ga4/ecommerce, [L]):
- `view_item`: "send a `view_item` event whenever a user views an item's details screen".
- `add_to_cart`: "Measure an item being added to a shopping cart by sending an `add_to_cart` event".
- `begin_checkout`: "Measure the first step in a checkout process by sending a `begin_checkout` event".
- `purchase`: "Measure a purchase by sending a `purchase` event with one or more items defined with the relevant fields". Lleva `transaction_id`; los reembolsos van en un evento `refund` aparte.
- Secuencia recomendada: `view_item_list`, `select_item`, `view_item`, `add_to_cart`, `view_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info`, `purchase`.
- Consecuencia: "las etapas" son eventos que la tienda decide enviar. Que `begin_checkout` marque "el primer paso" depende de cómo el comercio o la plataforma lo implemente; dos tiendas pueden medir lo mismo con eventos distintos. Esto es inferencia mía, no lo dice Google.

**Tasa de conversión: el denominador cambia entre fuentes.**
- Littledata: "The share of sessions that included at least one purchase" (sesiones). Muestra: "449 Shopify stores that use Littledata to send their data to Google Analytics 4", con mínimo de 1.000 sesiones y 90 compras; 90 días del 17/8 al 14/11/2026; generado el 18/11/2026. Mediana 1,4%; top 20% sobre 2,8%; top 10% 3,8% o más; peor 20% bajo 0,5%. Embudo: tasa de agregado al carrito, mediana 7,1% (top 10% 18%); "checkout completion" (de las sesiones que empezaron checkout, las que compraron), mediana 46% (peor 10% 14%, mejor 10% 73%); "cart abandonment" (de las sesiones con carrito, las que no compraron), mediana 79% (mejor 10% 56%, peor 10% 94%). Mobile: mediana 66% del tráfico. (https://www.littledata.io/benchmarks, [L]). Sesgo: solo tiendas Shopify que ya usan la app de Littledata (vendedor de analítica) y que superan un umbral de volumen; excluye las tiendas chicas, o sea la cola larga.
- Dynamic Yield: eMarketer describe la fuente como estadísticas mensuales de "XP2 by Dynamic Yield" con "200+ million unique users across 300 million anonymized sessions" y avisa que "Data represents activity among Dynamic Yield clients, broader industry metrics may vary". Define la conversión de dos maneras distintas en dos páginas (sesiones con compra sobre sesiones totales; compras sobre visitantes en 12 meses) (https://www.emarketer.com/data-providers/dynamic-yield, https://www.emarketer.com/industry-kpis/conversion-rate; [S]). Cifras vistas en notas de terceros: 2,72% global (12 meses móviles, panel de retailers grandes) y 2,66% en otra actualización de junio 2026; 77,81% de abandono de carrito. Estas cifras las vi solo en artículos de vendedores, sin abrir Dynamic Yield. Conflicto: Dynamic Yield vende personalización y hoy es de Mastercard (según eMarketer); sus clientes son retailers medianos y grandes.
- IRP Commerce: las notas que lo citan lo definen como transacciones sobre sesiones, panel mayormente de comercios del Reino Unido e Irlanda, pymes y medianos "on the IRP platform" ([S]). Cifras citadas con contradicciones entre notas: 1,70% abril 2026; para junio 2026, 2,03% en una nota y 1,70% en otras; 2,26% julio 2026; 1,97% septiembre 2026 (1,68% un año antes); 1,8% para 2025. Su propio sitio (https://www.irpcommerce.com/en/, [L]) no publica tamaño de muestra, número de comercios ni definición de conversión; solo muestra ventas (variación mensual). No hay método verificable. Conflicto: IRP vende servicios a comercios.
- Shopify: "hasta 36% mejor conversión" se repite en páginas de marketing de Shopify, atribuido a un estudio externo de una consultora sin nombre cuyo método no se publica en lo que vi; el mismo blog atribuye al estudio que Shop Pay puede subir la conversión 5% y hasta 50% frente a guest checkout (https://www.shopify.com/pk/enterprise/blog/one-page-checkout, [S]). Es una afirmación de un vendedor sobre su propio producto.

**Por qué comparar tasas entre tiendas engaña** (síntesis mía a partir de lo anterior, [S]):
- Denominadores distintos: sesiones vs visitantes únicos (el segundo da una tasa mayor o menor según cuántas sesiones tiene cada visitante).
- Muestras distintas: clientes de un vendedor (Dynamic Yield: enterprise; Littledata: Shopify con GA4 y umbral; IRP: Reino Unido/Irlanda pymes). Ninguna es representativa del mercado argentino.
- Las cifras para el mismo mes difieren entre notas (IRP junio 2026: 2,03% vs 1,70%).
- La conversión depende de qué se vende (precio, compra recurrente), de la fuente de tráfico (tráfico pago vs directo) y del dispositivo.
- Una tasa más baja en una plataforma no implica que su checkout sea peor: la conversión mezcla la calidad del tráfico, el catálogo y el checkout. Para aislar el checkout conviene la tasa checkout completion (de checkout iniciado a compra), aunque también depende de cómo se definió "iniciado".

### Recurso canónico
- GA4 ecommerce devguide, sección "Measure ecommerce", para la definición de eventos y de `purchase`. Fijarse en qué eventos son "recomendados" (no obligatorios) y en la secuencia.
- Littledata Benchmarks, por tener definiciones escritas y muestra declarada (449 tiendas, 90 días). Fijarse en las definiciones por etapa y en el umbral de 1.000 sesiones.

---

## 2. carrito-abandonado

### Fuentes

| Fuente | Tipo | Aut/Prof/Ej/Uni | Marca | URL |
|---|---|---|---|---|
| Baymard, lista de tasa de abandono | primaria del método y de la encuesta, vendedor | 2/2/2/3 | [L] | https://baymard.com/lists/cart-abandonment-rate |
| Baymard, "Current state of checkout UX" | primaria, vendedor | 2/3/2/3 | [L] | https://baymard.com/blog/current-state-of-checkout-ux |
| Baymard, "Ecommerce checkout usability report and benchmark" | primaria, vendedor | 2/3/2/3 | [L] | https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark |
| Baymard, "How to reduce cart abandonment" | primaria, vendedor | 2/1/1/1 | [L] | https://baymard.com/learn/reduce-cart-abandonment |
| Rajamma, Paswan y Hossain 2009 (JPBM) | primaria, académica | 3/2/1/3 | [M] (abstract vía repositorio) | https://digitalcommons.fairfield.edu/business-facultypubs/205 |
| Kukar-Kinney y Close 2010 (JAMS) | primaria, académica | 3/3/1/3 | [S] | https://link.springer.com/article/10.1007/s11747-009-0141-5 |
| Li, Luo, Lu y Moriguchi 2021 (Journal of Marketing) | primaria, académica | 3/3/2/3 | [S] | https://journals.sagepub.com/doi/10.1177/0022242920959043 |
| Marketing Science Institute, informe 21-133 | working paper | 3/2/1/2 | [S] | https://www.msi.org/wp-content/uploads/2021/09/MSI_Report_21-133-1.pdf |
| Close, Kukar-Kinney y Benusa 2012 (capítulo) | secundaria académica | 2/1/1/2 | [M] | https://scholarship.richmond.edu/marketing-faculty-publications/17/ |

### Afirmaciones

**Tasa promedio de Baymard** (https://baymard.com/lists/cart-abandonment-rate, [L]):
- Cifra literal: "we've calculated the average cart abandonment rate of 70.22%". Cuántos estudios: 50, publicados entre 2006 y 2025. Fecha: "Last updated Oct 28, 2026". Método: "The average is the plain, unweighted mean of every study listed."
- Lectura: es el promedio simple de estudios de orígenes muy distintos (cada uno con su definición de abandono, su muestra y su fecha) y no es una medición de Baymard. Que sea un promedio sin ponderar significa que un estudio de 2006 pesa lo mismo que uno de 2025 y que un panel chico pesa lo mismo que uno grande. No es "la tasa" de nada en particular.
- Otras páginas de Baymard dan cifras distintas para lo mismo: 70,19% y 68,8% en el artículo de 2016 actualizado el 2 de febrero de 2025 (https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark, [L]). Dos fuentes de la misma empresa se contradicen.
- Contraste con el embudo medido: la mediana de abandono en las 449 tiendas Shopify de Littledata es 79% (rango 56% a 94%, 90 días a nov 2026), con otra definición (sesiones con carrito sin compra) (https://www.littledata.io/benchmarks, [L]). No son lo mismo, y eso es parte del punto.

**Razones de abandono, encuesta de Baymard** (https://baymard.com/lists/cart-abandonment-rate, [L]; muestra de EE. UU.):
- "42%" abandonó por "I was just browsing / not ready to buy". Los siguientes porcentajes dejan fuera ese segmento (la página lo dice).
- 40% "Extra costs too high (shipping, tax, fees)"; 20% "Delivery was too slow"; 19% "I didn't trust the site with my credit card information"; 18% "The site wanted me to create an account"; 17% "Too long / complicated checkout process"; 17% "Website had errors / crashed"; 13% "Returns policy wasn't satisfactory"; 12% "I couldn't see / calculate total order cost up-front"; 10% "The credit card was declined"; 9% "There weren't enough payment methods"; 7% "I don't know".
- Muestra y fecha: la página de la lista no indica tamaño ni fecha ("our latest quantitative study"). Los artículos de Baymard tampoco: ninguno da la muestra de esta encuesta (https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark, [L]; https://baymard.com/learn/reduce-cart-abandonment, [L]). Las URL citan "GC049/GC050" con "March 2026" como parámetro, sin explicación. La respuesta es de varias opciones (suman más de 100%) y de "últimos 3 meses". Los 4.384 adultos de EE. UU. (2022) que aparecen son la muestra de otro dato (24% por cuenta obligatoria) (https://baymard.com/blog/make-guest-checkout-prominent, [L]). El 24% (2022) y el 18% actual para "cuenta obligatoria" difieren; no se explica si son encuestas o definiciones distintas.
- Lo declarado no es lo causado: es lo que la gente dice, en una lista cerrada que arma Baymard.
- "17%" tardó o complicó el checkout: el artículo sobre el estado actual lo repite ("17% of surveyed shoppers (1,000+)... in the last 3 months"), con 1.000+ de muestra (https://baymard.com/blog/current-state-of-checkout-ux, [L]). Es la única vez que vi un tamaño.

**Estudios académicos**
- Rajamma, Paswan y Hossain (2009), *Journal of Product & Brand Management* 18(3), 188-197, DOI 10.1108/10610420910957816 (https://digitalcommons.fairfield.edu/business-facultypubs/205, [M]): encuesta autoadministrada por internet a quienes compraron online al menos una vez en el último año. Hallazgo literal del abstract: "perceived transaction inconvenience is the major predictor of shopping cart abandonment"; el riesgo percibido también predice abandono y el tiempo de espera percibido tiene relación negativa. No vi el tamaño de muestra.
- Kukar-Kinney y Close (2010), *Journal of the Academy of Marketing Science*, DOI 10.1007/s11747-009-0141-5. [S] (la página de Springer redirigió a login; el PDF de CORE dio 403): solo tengo lo que devolvió el buscador. Define el abandono virtual como poner artículos en el carrito sin comprar nada en esa sesión, usa la Theory of Buyer Behavior de Howard y Sheth, y propone situaciones inhibitorias nuevas; una hipótesis es que usar el carrito como entretenimiento aumenta el abandono. No tengo muestra ni hallazgos numéricos. Distinción útil: para estos autores abandonar no siempre es un fracaso del checkout; el carrito puede usarse para guardar, comparar o entretenerse. El capítulo de 2012 del mismo grupo propone tres resultados (compra, abandono sin compra, abandono para comprar en otro lado) (https://scholarship.richmond.edu/marketing-faculty-publications/17/, [M]).
- Ambos son encuestas (autodeclaración), de 2009-2010, en EE. UU.; no sé si la muestra fue de estudiantes. Eso queda como hueco.

**Recuperación de carritos (retargeting y emails)**
- Li, Luo, Lu y Moriguchi, *Journal of Marketing* 85(4), jul. 2021, 123-140 (DOI 10.1177/0022242920959043; el título varía entre "Does Retargeting Too Early Backfire?" en SAGE y "Does Too Early Retargeting Backfire?" en la AMA), [S] (SAGE dio 403; datos del buscador y comunicados de la AMA): experimentos de campo aleatorizados con más de 40.500 clientes; un anuncio temprano (30 a 60 minutos tras el abandono) bajó la probabilidad de compra frente al control; uno tardío (24 a 72 horas) tuvo efecto incremental positivo. Un segundo experimento con más de 23.900 clientes de otra empresa replicó en parte. Son anuncios de retargeting, no emails: el email es otro canal y no se midió acá (no aparece en lo que leí).
- MSI informe 21-133: otro experimento de campo con un retailer: mayor aumento en compradores que abandonaron hace poco y con carritos de una sola categoría ([S]).
- Marketing Experiments (+263% en recuperación con un segundo email con rebaja): práctica sin revisión, anecdótico. No lo adopto.
- Las cifras de recuperación de las guías de Shopify y BigCommerce son de vendedores y no son experimentos controlados ([S]).
- Hueco: no encontré un experimento aleatorizado revisado por pares sobre emails de carrito abandonado. Declaro que la evidencia sólida es sobre anuncios y es de la tienda o canal ajenos a Latinoamérica.

### Recurso canónico
- Baymard, https://baymard.com/lists/cart-abandonment-rate: la sección de razones; fijarse en la nota de que "just browsing" está excluido y en que la tasa es un promedio simple de 50 estudios.
- Rajamma et al. 2009 y Kukar-Kinney y Close 2010 como lectura académica; leer el texto completo (acceso institucional) antes de citar números.
- Li et al. 2021 (JM) para recuperación; fijarse en la ventana de tiempo.

---

## 3. usabilidad-del-checkout

### Fuentes

| Fuente | Tipo | Aut/Prof/Ej/Uni | Marca | URL |
|---|---|---|---|---|
| Baymard, "Current state of checkout UX" (pub. 13/11/2024, act. 3/11/2026) | primaria, vendedor | 2/3/2/3 | [L] | https://baymard.com/blog/current-state-of-checkout-ux |
| Baymard, informe y benchmark (pub. 21/9/2016, act. 2/2/2025) | primaria, vendedor | 2/3/2/3 | [L] | https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark |
| Baymard, "Guest checkout most prominent" (17/1/2023) | primaria, vendedor | 2/2/2/3 | [L] | https://baymard.com/blog/make-guest-checkout-prominent |
| Baymard, "One page checkouts" (Holst, 26/4/2011) | primaria, opinión | 2/2/1/3 | [L] | https://baymard.com/blog/one-page-checkout |
| Baymard, metodología (del vistazo, no releída) | primaria | 3/2/1/3 | [S] | https://baymard.com/checkout-usability/methodology |
| Stripe, guía uno vs varios pasos | vendedor | 1/1/1/1 | [S] | https://stripe.com/en-es/resources/more/one-page-checkout-vs-multistep-checkout |
| Amazon Pay blog sobre Baymard y guest checkout | vendedor, de segunda mano | 1/1/1/1 | [S] | https://pay.amazon.com/us/blog/the-baymard-report-series-how-forcing-sign-ups-drives-down-sales |

### Afirmaciones

**Lo que Baymard sostiene (literal y fechado)**
- Campos: "The average US checkout shows 23.48 form elements by default (14.88 if only form fields are counted)"; un flujo ideal tiene "about 12 elements" y muchos checkouts podrían reducir el conteo por defecto entre 20 y 60% (https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark, [L], act. 2025). Esa cifra de 23,48 es del artículo actualizado en 2025; la página de 2026 no repite el promedio.
- Calificación general: "59% of desktop and mobile sites rated 'mediocre' or worse; 2% of desktop sites and 1% of mobile sites rated 'good'"; no hay sitios de escritorio "perfect"; 15% "poor" o "very poor"; apps: 60% mediocre o peor y solo una "good". Base: "44,000+ checkout usability scores", "35,500+ worst and best practice implementation examples" (https://baymard.com/blog/current-state-of-checkout-ux, [L], act. 3/11/2026). La cantidad de sitios no se da en esa página. El vistazo anotó 244 sitios y más de 110 guías en la página de metodología, y 65% en lugar de 59% (sin releer; se contradicen entre sí).
- Mejora potencial: el rediseño del checkout podría subir la conversión del sitio grande promedio 35,26%; la cifra se basa en sitios líderes (Walmart, Amazon) y el artículo dice que la ganancia es más difícil de lograr de lo que sugiere el número (https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark, [L]).
- Invitado: "Make 'Guest Checkout' the Most Prominent Option (47% Don't)", 17/1/2023; no se da el tamaño de la muestra de esa tasa ni la fecha del benchmark (https://baymard.com/blog/make-guest-checkout-prominent, [L]). Una versión más nueva del benchmark reportada por el buscador dice 62% (no leí esa página; [S]). Otro título: "Save Account Creation for the Confirmation Step (56% Don't)" (https://baymard.com/blog/current-state-of-checkout-ux, [L]). Dato adjunto: 24% de compradores de EE. UU. abandonó carritos en el último trimestre solo por cuenta obligatoria (4.384 adultos de EE. UU., 2022) (https://baymard.com/blog/make-guest-checkout-prominent, [L]).
- Costos inesperados: 40% abandona por costos extra (encuesta, ver sección 2); es la razón principal declarada.
- Teléfono: 68% se resiste a dar su teléfono (encuesta GC049, marzo 2026); 32% saltó al menos un campo obligatorio cuando solo los opcionales estaban marcados; tipos de campo incorrectos para entradas opcionales alargaron 5-30% el tiempo de los pasos (https://baymard.com/blog/current-state-of-checkout-ux, [L]).
- Estado: Baymard dice que está "retesting and verifying all of our existing Checkout research" y que publicará la investigación revisada en el 2.º trimestre de 2027 (ídem). O sea, sus propias cifras actuales se declaran en revisión.

**Método y límites**
- Método declarado: pruebas de usabilidad moderadas 1 a 1 con "think aloud" (272 sesiones sujeto/sitio), un estudio grande de eye-tracking, dos rondas de benchmark sobre más de 850 pasos de checkout y nueve estudios cuantitativos con 11.777 participantes; más de 2.700 problemas de usabilidad condensados en 134 guías en un informe de 718 páginas (https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark, [L]).
- Límites que el propio texto muestra: no hay sección de limitaciones; la parte cualitativa es una muestra chica; la mejora de 35,26% es para "el sitio grande promedio"; el artículo dice que la tasa 0% de abandono es "unattainable". Inconsistencias internas: 68,8% vs 70,19%; 50 vs 60 sitios.
- Conflicto de interés: Baymard vende la base de datos de investigación ("200,000+ hours of UX research", pago) y su benchmark califica sitios; cada problema que reporta vende acceso. No encontré auditoría independiente (el vistazo ya lo anotaba). No es un argumento de que esté mal: es un motivo para pedir el método.
- Los tests moderados descubren problemas (qué hace tropezar a la gente), no estiman cuánto sube la conversión; el vínculo entre guía y conversión sale de promedios de sitios y de las encuestas.

**Estudios independientes que confirmen o contradigan.** No encontré ninguno revisado por pares sobre campos del checkout ni sobre invitado vs registro obligatorio (búsqueda en la ronda 3; presupuesto de búsquedas agotado después). Lo que apareció es de vendedores o sin método: Corbado "registrados 64% vs invitados 52%" cita "industry data" y compara poblaciones distintas (sesgo de selección), un artículo de UX Design cuenta un test anecdótico de +180% sin tamaño de muestra, y el blog de Amazon Pay repite cifras de Baymard (+10-30% sin cuenta obligatoria, 37% disgustado en 2017) que no pude cotejar con el original. Todo eso son [S] y no cuenta como confirmación independiente. Los estudios académicos de la sección 2 coinciden en la dirección (inconveniencia percibida y riesgo predicen el abandono: Rajamma et al. 2009), pero miden percepción con encuesta, no el efecto de un cambio concreto del checkout.

**Un solo paso vs varios** (evidencia, no opinión)
- Baymard (Holst, 26/4/2011): una página "won't necessarily perform better" que un multi-paso comparativamente optimizado; algunas pruebas A/B muestran que el de una página gana "significantly", pero comparan un multi-paso sin optimizar con una página nueva optimizada; sin tests ni cifras; la hipótesis de que dividir los mismos campos en dos páginas no cambiaría casi nada es una expectativa, no un resultado (https://baymard.com/blog/one-page-checkout, [L]). Es una opinión de 2011.
- Un test citado de segunda mano (+21,8%, detenido a las 606 transacciones, CartWhisper) no se pudo verificar ([S]); además 606 transacciones es una muestra pequeña.
- Un caso de Shopify (Stellar Eats: +3,5% tras pasar a una página) es de un solo comercio, sin grupo control descrito ([S], https://www.shopify.com/gr/case-studies/stellar-eats, URL vista en el buscador, no abierta).
- Stripe: recomienda probar con la propia audiencia; no hay un mejor diseño universal ([S]).
- Conclusión honesta: no hay estudio independiente que compare a igualdad de campos; la evidencia disponible sugiere que lo que pesa es el contenido de cada paso, no el número de páginas. Es un hueco que se declara.

### Recurso canónico
- Baymard, "Current state of checkout UX" (act. 3/11/2026): para el estado actual del benchmark y el aviso de re-testeo (Q2 2027). Fijarse en las fechas y en las cifras sin tamaño de muestra.
- Baymard, informe y benchmark (act. 2025): para el método (272 sesiones, 134 guías) y el promedio de 23,48 elementos.
- Baymard 2011 sobre una página, para la distinción conceptual, no para evidencia.

---

## 4. Cómo se usa todo esto al analizar una plataforma de tiendas competidora

Síntesis mía con apoyo en las fuentes citadas arriba; marcada [S] salvo cuando cito.

1. Qué se puede comparar sin engañarse: los eventos que cada plataforma mide (GA4 `begin_checkout`, `add_payment_info`), la cantidad de pasos y de campos por defecto (contar los elementos del formulario, como hace Baymard: 23,48 promedio vs ~12 ideal), la presencia de checkout de invitado, de costos de envío visibles antes de pagar, de billeteras y medios locales. No se debe comparar la tasa de conversión publicada entre plataformas (denominadores y muestras distintos; ver sección 1).
2. Lo que fija la plataforma y lo que configura el comercio (dos ejemplos leídos):
   - Shopify (https://shopify.dev/docs/apps/build/checkout, [L]): se personaliza con extensiones de UI (bloques colocados en el editor de checkout, campos personalizados, validación del lado del cliente, autocompletar dirección, encabezado y pie), Functions (descuentos, ocultar medios de pago, renombrar opciones de entrega, bloquear el checkout si falla una regla) y branding por la Admin API. `checkout.liquid` ya no se admite para los pasos de Información, Envío y Pago. La página no lista qué bloquea Shopify ni restricciones por plan; las fechas de retiro de script tags (28/8/2025 en Plus, 26/8/2026 en no-Plus) son lo único dicho sobre planes. No pude confirmar la lista completa de lo fijo.
   - Tiendanube (centro de ayuda, resultados del buscador, [S]; no abrí las páginas): opciones en "Configuración > Opciones del checkout" (nota del cliente, pedir teléfono y documento, Factura A con CUIT y razón social, colores de marca, mensaje de confirmación); no se puede personalizar con CSS ni HTML "porque es un proceso seguro"; no se puede quitar la dirección de envío salvo productos digitales; los códigos personalizados están solo en el plan Evolución y no permiten cambiar libremente campos, botones ni estructura; para más de dos campos propios se usan apps (las páginas de ayuda no coinciden entre sí sobre campos propios nativos). Fuentes: https://ayuda.tiendanube.com/es_AR/123367-opciones-del-checkout/como-agregar-codigos-personalizados-en-el-checkout-de-mi-tiendanube y https://ayuda.tiendanube.com/es_AR/123522-recursos-extra/como-agregar-campos-personalizados-para-que-mis-clientes-los-completen-en-mi-tiendanube.
   - Lectura: la cantidad de campos, el orden de los pasos y el diseño del checkout los fija la plataforma en ambos casos; el comercio ajusta campos extra, textos, branding y reglas. Esto importa porque la mejora de usabilidad de Baymard (campos, orden, invitado) está en lo que fija la plataforma, y no es optimizable por el comerciante individual. Es inferencia mía.
3. Cómo leer las afirmaciones de conversión de una plataforma (como "hasta 36%" de Shopify): pedir el método, la comparación (contra qué), el período y quién lo hizo; tratar como afirmación de vendedor lo que no trae método.
4. Qué falta para analizar a una plataforma competidora de verdad: auditar el checkout con la lista de guías de Baymard (de pago) o con la lista de elementos propia, en vez de usar cifras de conversión de la plataforma; y medir en el contexto argentino (Pix no aplica; cuotas, billeteras y Factura A sí; ver Pagos y Normativa).

---

## Huecos

- Kukar-Kinney y Close 2010: no pude leer el abstract ni el texto (Springer pide login, CORE dio 403, SAGE dio 403); no tengo muestra ni cifras. Rajamma et al. 2009: solo el abstract, sin tamaño de muestra.
- Baymard: no hay muestra ni fecha de la encuesta de razones de abandono; no leí la página de metodología esta vez (los datos del vistazo sobre 244 sitios, más de 110 guías, 25 rondas y 20 sujetos quedaron sin releer); el 62% de invitado no prominente salió del buscador; las cifras de 2.700 problemas, 134 guías y 718 páginas son del artículo de 2016/2025.
- Dynamic Yield: no abrí su página de benchmarks; las tasas (2,72%, 2,66%, 77,81%) son de terceros. IRP Commerce: no hay método publicado; las cifras vienen de notas que se contradicen.
- Sin estudio independiente revisado por pares sobre campos de checkout, invitado vs registro, ni uno vs varios pasos. Sin experimento aleatorizado sobre emails de carrito abandonado (solo anuncios de retargeting, EE. UU./Asia; ver Li et al. 2021).
- Sin evidencia para Argentina o Latinoamérica sobre abandono ni checkout (solo EE. UU., Europa y Reino Unido).
- El estudio externo de Shopify detrás de "hasta 36%": no se encontró el método.
- No se comparó el checkout de Shopify con el de otras plataformas en el benchmark de Baymard (la búsqueda no se pudo hacer); no abrí el centro de ayuda de Tiendanube (resultados del buscador solamente); no revisé WooCommerce ni Scalafy.
- No vi qué tan estándar es el significado de "checkout iniciado" entre plataformas; es inferencia.
