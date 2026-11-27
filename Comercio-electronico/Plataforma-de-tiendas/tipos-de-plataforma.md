---
resumen: >-
  Las plataformas de tiendas se dividen en tres tipos según quién opera el software y en qué sitio se vende: la alojada, que el proveedor opera y el comercio alquila; la de código abierto autoalojada, que el comercio instala y mantiene; y el marketplace, donde el comercio vende dentro del sitio de otro. Headless y composable no son un cuarto tipo: son una forma de armar la tienda que se elige con condiciones.
estado: vigente
estabilidad: estable
fuentes:
  - "WooCommerce, About: https://woocommerce.com/about/ (leída, consultada el 2026-11-22)"
  - "VTEX, 20-F del ejercicio 2025, sección 5: https://www.sec.gov/Archives/edgar/data/1793663/000119312526076504/ck0001793663-20251231.htm (leído en parte, por tramos)"
  - "MACH Alliance, Wikipedia: https://en.wikipedia.org/wiki/MACH_Alliance (según resumen del buscador)"
  - "commercetools, nota de prensa de la formación de la MACH Alliance, 2020: https://commercetools.com/press-releases/mach-alliance-forms-to-empower-enterprises-taking-advantage-of-modern-saas-technology (según resumen del buscador)"
  - "Shopify, Wikipedia: https://en.wikipedia.org/wiki/Shopify (según resumen; fecha de Hydrogen)"
  - "Ryan Breen (Fastr), The headless commerce productivity myth, 20/04/2023, actualizado 20/06/2026: https://getfastr.com/blog/the-headless-commerce-productivity-myth-why-composable-stacks (leído)"
  - "Elogic, Composable commerce vs headless, 12/05/2026, actualizado 3/11/2026: https://elogic.co/blog/composable-commerce-vs-headless/ (leído)"
  - "Jordan Jewell (VTEX), The MACH mirage, 25/03/2025: https://vtex.com/en-us/blog/mach-mirage (leído)"
  - "Comercio-electronico/.investigacion/plataforma-de-tiendas.md (sección 1)"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (A2, A7 y B1)"
  - "Comercio-electronico/.investigacion/vistazo.md (sección 2)"
aliases: [tipos de plataforma de e-commerce, SaaS commerce, hosted platform, plataforma alojada, self-hosted, código abierto autoalojado, open source commerce, headless commerce, composable commerce, MACH]
creado: 2026-11-22
revisado: 2026-11-22
---

# Tipos de plataforma

Las plataformas de tiendas se dividen en tres tipos según quién opera el software y en qué sitio se vende: la alojada, que el proveedor opera y el comercio alquila; la de código abierto autoalojada, que el comercio instala y mantiene; y el marketplace, donde el comercio vende dentro del sitio de otro. Headless y composable no son un cuarto tipo: son una forma de armar la tienda que se elige con condiciones.

El tipo decide tres cosas antes que cualquier funcionalidad: quién carga con la operación del software, cómo cobra el proveedor y de quién es la relación con el comprador. Por eso es lo primero que se fija al ubicar a un jugador de la [plataforma de tiendas](plataforma-de-tiendas.md). La distinción es de uso común en el campo; los informes no encontraron una fuente primaria que la fije, y el manual que podría hacerlo, Laudon y Traver, no se leyó.

## Alojada, autoalojada y marketplace

| | Alojada (SaaS) | Código abierto autoalojada | Marketplace |
|---|---|---|---|
| Quién aloja, actualiza y asegura el software | el proveedor | el comercio o su agencia | el marketplace |
| Qué paga el comercio | una suscripción y, casi siempre, una parte de lo que vende | nada por el núcleo; aparte, el alojamiento, las extensiones y la pasarela | una comisión por venta y servicios opcionales |
| Dónde está la tienda | en el dominio del comercio, sobre la instalación del proveedor | donde el comercio la instale | dentro del sitio del marketplace |
| De quién es el cliente | del comercio | del comercio | del marketplace |
| Ejemplos con ficha | [Shopify](shopify.md), [Tiendanube](tiendanube.md), [VTEX](vtex.md), [Empretienda](empretienda.md), [Wix](wix.md) | [WooCommerce](woocommerce.md) | [Mercado Libre](mercado-libre.md) |

La alojada es un alquiler. El comercio abre una cuenta y el proveedor corre una sola instalación para todas las tiendas, como se ve en [arquitectura de una plataforma](arquitectura-de-plataforma.md). VTEX, por ejemplo, se describe a sí misma como un SaaS en su 20-F. Lo que el proveedor cobra y por qué gana más con los pagos que con la suscripción está en [el negocio de una plataforma](negocio-de-una-plataforma.md).

La autoalojada es software que el comercio instala. WooCommerce se define como "the flexible, Open Source commerce solution built on WordPress", con el núcleo gratis. El software no cuesta, pero el trabajo de mantenerlo pasa al comercio: actualizaciones, seguridad, rendimiento y la integración de cada extensión. [Adobe Commerce](adobe-commerce.md), heredero de Magento, suele ponerse en este grupo; los informes no pudieron verificar su licencia ni sus ediciones.

El marketplace no le da al comercio una tienda propia. El comercio publica dentro del sitio de un tercero, que trae el tráfico y cobra una comisión, y el comprador es del marketplace. Si conviene vender ahí, en una tienda propia o en los dos está en [venta en varios canales](../Venta-en-varios-canales/venta-en-varios-canales.md#marketplace-o-tienda-propia-depende-de-la-etapa), con los costos de cada lado.

> [!NOTE] Sin fuente todavía: una comparación neutral del costo total de cada tipo para un mismo comercio. Los informes no la encontraron, y armarla con las fichas sería un cálculo de esta base, no un dato.

## Headless y composable: separar la vitrina y elegir cada pieza

Headless separa la vitrina, lo que ve el comprador, del motor de comercio, que guarda catálogo, carrito y pedidos; las dos partes se hablan por API. Composable va más lejos: la tienda se arma con servicios independientes, elegidos uno por uno (catálogo, búsqueda, pagos, contenido), en lugar de una plataforma que los trae juntos. Las dos definiciones son síntesis del campo, sin fuente que las fije.

Se cruzan con los tipos, no los reemplazan. Una plataforma alojada puede ofrecer el modo headless: Shopify lanzó Hydrogen, su stack para vitrinas a medida, en 2021, según Wikipedia. Eso muestra que la oferta existe, no que rinda. Qué se programa en la práctica, cuánto cuesta y quién la tiene en Argentina está en [vitrina a medida](vitrina-a-medida.md), y los motores, en [motores para vitrinas a medida](motores-para-vitrinas-a-medida.md).

La sigla que acompaña al composable es MACH: microservices, API-first, cloud-native y headless. La promueve la MACH Alliance, una organización sin fines de lucro lanzada en junio de 2020, según un resumen de Wikipedia. Su propia nota de prensa nombra como fundadores a commercetools, Contentstack, EPAM Systems y Valtech. Quienes la impulsan venden componentes de ese tipo.

## Cuándo conviene headless o composable

Headless y composable dan independencia de la vitrina y de cada servicio, a cambio de integraciones propias y un equipo que las sostenga. Es una decisión con condiciones, no una mejora. Cada integración que la plataforma ya no resuelve pasa a ser código que el comercio escribe, prueba y mantiene.

Elogic, una consultora que es partner de Adobe y de Shopify Plus, publica criterios para no ir a composable. No lo recomienda si el equipo de ingeniería tiene menos de 15 personas, si marketing depende de ingeniería para cambios rutinarios, o si el GMV anual está bajo unos US$ 20 millones con menos de 10 integraciones. Pide calcular el costo total del cambio a tres años. Son criterios de un proveedor de servicios, no una regla medida.

> [!IMPORTANT]
> Ninguna cifra sobre el costo de headless o composable tiene un estudio independiente detrás. Todas, a favor y en contra, vienen de quien vende algo.
>
> **En contra.** Fastr, que vende un producto de vitrina, y Elogic afirman que el costo total de composable supera al de un SaaS bien gestionado, sin método publicado. VTEX, que vende la alternativa unificada, escribe que "MACH principles are no longer special; they're table stakes", sin datos.
>
> **A favor.** Elogic presenta casos propios con menos costo total y más conversión después de migrar, sin verificación externa. También cita a Gartner una baja de costo para empresas con licencias de plataforma de entre US$ 500.000 y 2 millones por año, sin enlace; Gartner no se leyó.

## Cómo se usa al analizar plataformas de tiendas

El tipo ordena a los competidores antes de comparar funciones. Si un SaaS para comerciantes compara una plataforma alojada con una autoalojada, compara también quién paga la operación: en la autoalojada ese costo lo pone el comercio y no aparece en ningún precio. En el marketplace, la comparación es de canal, no de software.

Ofrecer headless dice a quién apunta una plataforma. Una vitrina separada pide un equipo propio, que tienen las marcas grandes y no el emprendedor; cómo se reparte eso por tamaño está en [segmentos de comerciantes](segmentos-de-comerciantes.md). Al leer el material de un proveedor sobre composable, la pregunta es qué vende: casi todas las fuentes del debate venden una de las dos opciones.

No hay todavía un recurso canónico confiable sobre tipos de plataforma. El sitio de la MACH Alliance (machalliance.org) sirve para la definición literal de MACH y sus principios de certificación, leído como lo que es: la voz de un grupo de proveedores. Para la distinción entre alojada y abierta, el candidato es la parte de infraestructura de Laudon y Traver, *E-commerce* (18.ª ed., 2023), sin verificar.

> [!NOTE] Sin fuente todavía: un estudio académico o de analista abierto que mida costos o fracasos de headless y composable, y una crítica independiente de MACH.
