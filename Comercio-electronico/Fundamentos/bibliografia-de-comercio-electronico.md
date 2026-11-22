---
resumen: >-
  Lecturas de comercio electrónico ordenadas por necesidad (entender el dominio, plataformas de tiendas, pagos, checkout y conversión, canales y operaciones, América Latina): la obra, qué parte leer y en qué fijarse, de qué tipo es y cuánto se leyó para armar la base. Ningún libro se leyó; casi todo lo leído son documentos públicos, normas y páginas de proveedores.
estado: vigente
estabilidad: semi
fuentes:
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md, secciones A4 y A8"
  - "Comercio-electronico/.investigacion/vistazo.md, secciones 1, 4 y 5"
  - "Comercio-electronico/.investigacion/plataforma-de-tiendas.md, recursos canónicos"
  - "Comercio-electronico/.investigacion/pagos.md, recursos canónicos"
  - "Comercio-electronico/.investigacion/checkout-y-conversion.md, recursos canónicos"
  - "Comercio-electronico/.investigacion/operaciones-canales-y-normativa.md, recursos canónicos"
  - "Comercio-electronico/.investigacion/huecos-pagos-y-operaciones.md, recursos canónicos"
aliases: [lecturas de comercio electrónico, bibliografía de e-commerce, e-commerce reading list, libros de comercio electrónico]
creado: 2026-11-22
revisado: 2026-11-22
---

# Bibliografía de comercio electrónico

Lecturas de comercio electrónico ordenadas por necesidad (entender el dominio, plataformas de tiendas, pagos, checkout y conversión, canales y operaciones, América Latina): la obra, qué parte leer y en qué fijarse, de qué tipo es y cuánto se leyó para armar la base. Ningún libro se leyó; casi todo lo leído son documentos públicos, normas y páginas de proveedores.

La columna "Leído" dice cuánto se leyó: texto (la página o el pasaje, a través de una herramienta que devuelve un extracto), parcial, ficha (metadatos, índice o abstract), resumen (buscador o reseña) o no. El peso de cada tipo de fuente y lo que vende cada una están en [Fuentes de comercio electrónico](fuentes-de-comercio-electronico.md).

## Orden sugerido

Recomendación de la base, no hallazgo.

1. La definición de la OCDE de 2025, sección 4.3, para saber qué cuenta como comercio electrónico.
2. Las definiciones del Item 1 y los indicadores del Item 7 del 10-K de Shopify, para entender de dónde sale la plata de una plataforma.
3. El Reglamento (UE) 2015/751, corto, para ver qué partes forman el costo de cobrar con tarjeta.
4. La lista de abandono de carrito de Baymard, para ver cómo se arma la cifra más citada del tema y sus límites.
5. La sección de la necesidad concreta, abajo.

## Entender el dominio

| Obra | Qué parte leer y en qué fijarse | Tipo | Leído |
|---|---|---|---|
| [OECD, *The 2025 OECD definition of e-commerce and guidelines for interpretation*](https://unctad.org/system/files/information-document/2025oecddefinitionofecommerce_guidelinesforinterpretation.pdf), octubre de 2025 | Sección 4.3 (intermediarios, redes sociales); la definición no cambió desde 2009, cambió la interpretación | Estándar estadístico | Texto |
| Laudon y Traver, *E-commerce 2023-2024: business. technology. society.*, 18.ª ed., Global Edition, Pearson | Los capítulos de modelos de negocio y de infraestructura. Pearson la fecha el 2 de agosto de 2024 y el ISBN impreso 9781292449722 dice "Published 2023": citar "18.ª ed., 2023/2024" | Manual | Ficha |
| Laudon y Traver, *E-commerce: negocios, tecnología, sociedad*, Pearson: 4.ª ed., México, 2009, y *E-commerce 2013*, c2014 | La última traducción al castellano encontrada es de 2014; no se halló traducción de la 18.ª | Manual | Ficha (catálogos de bibliotecas) |
| Chaffey, Hemphill y Edmundson-Bird, *Digital Business and E-commerce Management*, 8.ª ed., Pearson | Enfoque de gestión; Pearson da 2024 y 2026 y varios ISBN, así que hay que verificar la edición antes de citarla | Manual | No |
| [UNCTAD, nota de 2020 sobre el comercio electrónico mundial](https://unctad.org/news/global-E-commerce-hits-256-trillion-latest-unctad-estimates) | Qué incluye la cifra (EDI, plataformas) y la salvedad de que muchos países no publican estadísticas oficiales | Organismo | Texto |
| [US Census Bureau, e-commerce trimestral](https://www.census.gov/retail/ecommerce.html) | La participación del comercio electrónico en las ventas minoristas de Estados Unidos, desestacionalizada y sin ajustar | Estadística oficial | Texto |

## Plataformas de tiendas

Para el negocio de dos lados en general, la base ya tiene [Plataformas](../../Producto/Plataformas/plataformas.md) y su bibliografía en [Bibliografía de producto](../../Producto/Fundamentos/bibliografia-de-producto.md).

| Obra | Qué parte leer y en qué fijarse | Tipo | Leído |
|---|---|---|---|
| [Shopify, 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) | Item 1 (definiciones) e Item 7, "Key Performance Indicators"; fijarse en "GMV does not represent revenue" y en la penetración de pagos. Ver [el negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md) | Reporte público | Parcial (por tramos) |
| [VTEX, 20-F FY2025](https://www.sec.gov/Archives/edgar/data/1793663/000119312526076504/ck0001793663-20251231.htm) | El modelo de cobro: cargo fijo más un porcentaje del GMV, distinto del de Shopify | Reporte público | Parcial |
| [Shopify, versionado de la API](https://shopify.dev/docs/api/usage/versioning) | La tabla de versiones y la política de deprecación: cuántos meses hay para migrar. Ver [Arquitectura de plataforma](../Plataforma-de-tiendas/arquitectura-de-plataforma.md) | Documentación | Texto |
| [Weingarten, charla en SREcon16 Europe](https://usenix.org/conference/srecon16europe/program/presentation/weingarten) | La fuente primaria más temprana de la arquitectura de aislamiento de Shopify; ver el video, no solo el abstract | Charla técnica | Ficha |
| [Sitio de la MACH Alliance](https://machalliance.org/the-alliance) | La definición de MACH y los principios de certificación, sabiendo que la impulsan proveedores de esos componentes. Ver [Tipos de plataforma](../Plataforma-de-tiendas/tipos-de-plataforma.md) | Asociación de proveedores | Resumen |
| [Rysman, "The Economics of Two-Sided Markets"](https://www.aeaweb.org/articles?id=10.1257/jep.23.3.125), *Journal of Economic Perspectives* 23(3), 2009, pp. 125-143 | Artículo corto, puerta a la teoría; sus ejemplos incluyen las tarjetas de pago | Paper | Ficha y resumen |
| Rochet y Tirole, "Platform Competition in Two-Sided Markets", *Journal of the European Economic Association*, 2003 | La fuente primaria del campo | Paper | No |
| Evans, Hagiu y Schmalensee, *Invisible Engines*, MIT Press | La primera edición sería de 2006; el vistazo decía 2008, quizás la rústica | Libro | No |

## Pagos

| Obra | Qué parte leer y en qué fijarse | Tipo | Leído |
|---|---|---|---|
| [Reglamento (UE) 2015/751](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R0751) | Arts. 3, 4, 5, 7 y 9: los topes de interchange y los tres precios que se suman (interchange, red y margen del adquirente). Ver [Costo de cobrar](../Pagos/costo-de-cobrar.md) | Norma | Texto |
| [EBA y BCE, *2025 Report on Payment Fraud*](https://www.ecb.europa.eu/press/intro/publications/pdf/ecb.ebaecb202512.en.pdf), diciembre de 2025 | Caps. 2 (niveles), 4 (autenticación fuerte) y 5 (quién pierde); los datos son del lado del emisor y no cubren América Latina. Ver [Fraude y contracargos](../Pagos/fraude-y-contracargos.md) | Organismo | Texto |
| [Stripe, cómo funcionan las disputas](https://docs.stripe.com/disputes/how-disputes-work) | La cadena del contracargo entre emisor, red, agregador y comercio; es de una empresa que vende pagos | Documentación de proveedor | Texto |
| [BCRA, Comunicación A 6885](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6885.pdf), 30/1/2020 | Puntos 1.1.1 a 1.1.5: quién es proveedor de servicios de pago. Ver [Actores del pago](../Pagos/actores-del-pago.md) | Norma | Texto |
| [Banco Central do Brasil, *Relatório de Gestão do Pix 2023-2025*](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf) | Las estadísticas de la sección 2, Pix Automático (1.1.4) y el MED (1.2.1). Ver [Medios de pago locales](../Pagos/medios-de-pago-locales.md) | Organismo | Parcial |

> [!NOTE]
> Sin fuente todavía: un libro o un glosario primario del flujo de un pago con tarjeta (autorización, captura, compensación y liquidación). El candidato es el "Red Book" del CPMI-BIS, cuya edición vigente no se localizó.

## Checkout y conversión

| Obra | Qué parte leer y en qué fijarse | Tipo | Leído |
|---|---|---|---|
| [Google, GA4 "Measure ecommerce"](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce) | Qué eventos son recomendados y en qué secuencia. Ver [Embudo de conversión](../Checkout-y-conversion/embudo-de-conversion.md) | Documentación | Texto |
| [Littledata, Benchmarks](https://www.littledata.io/benchmarks) | Las definiciones por etapa y el umbral de 1.000 sesiones; la muestra son 449 tiendas Shopify clientes del proveedor | Benchmark de proveedor | Texto |
| [Baymard, Cart abandonment rate](https://baymard.com/lists/cart-abandonment-rate) | La sección de razones; "just browsing" queda excluido y la tasa es un promedio simple de 50 estudios. Ver [Carrito abandonado](../Checkout-y-conversion/carrito-abandonado.md) | Investigación de proveedor | Texto |
| [Baymard, "Current state of checkout UX"](https://baymard.com/blog/current-state-of-checkout-ux) | El estado del benchmark y el aviso de que re-testea su investigación hasta el 2.º trimestre de 2027. Ver [Usabilidad del checkout](../Checkout-y-conversion/usabilidad-del-checkout.md) | Investigación de proveedor | Texto |
| [Rajamma, Paswan y Hossain](https://digitalcommons.fairfield.edu/business-facultypubs/205), *Journal of Product & Brand Management* 18(3), 2009 | La inconveniencia percibida como mayor predictor del abandono | Paper | Abstract |
| [Kukar-Kinney y Close](https://link.springer.com/article/10.1007/s11747-009-0141-5), *Journal of the Academy of Marketing Science* 38, 2010 | El carrito como entretenimiento y herramienta de búsqueda | Paper | Resumen |
| [Li, Luo, Lu y Moriguchi](https://journals.sagepub.com/doi/10.1177/0022242920959043), *Journal of Marketing* 85(4), 2021 | La ventana de tiempo del retargeting tras el abandono | Paper | Resumen |

## Canales y operaciones

| Obra | Qué parte leer y en qué fijarse | Tipo | Leído |
|---|---|---|---|
| [Verhoef, Kannan e Inman, "From Multi-Channel Retailing to Omni-Channel Retailing"](https://doi.org/10.1016/j.jretai.2015.02.005), *Journal of Retailing* 91(2), 2015 | La definición de omnicanal y cómo la separan de multicanal. Ver [Venta en varios canales](../Venta-en-varios-canales/venta-en-varios-canales.md) | Paper | Ficha |
| [Sopadjieva, Dholakia y Benjamin](https://hbr.org/2017/01/a-study-of-46000-shoppers-shows-that-omnichannel-retailing-works), HBR, 3/1/2017 | La cifra de gasto y el método; los autores son de Medallia y de la Universidad de Rice | Divulgación | Solo la introducción |
| Hagiu y Wright, "Marketplace or Reseller?", *Management Science*, 2015 | Cuándo un intermediario conviene como marketplace o como revendedor, desde el lado del intermediario | Paper | Ficha |
| [Shopify, gestión de inventario](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps) | Los estados del stock por ubicación; describe el modelo de una empresa, no el del campo. Ver [Operaciones del comercio](../Operaciones-del-comercio/operaciones-del-comercio.md) | Documentación | Texto |

## América Latina y Argentina

| Obra | Qué parte leer y en qué fijarse | Tipo | Leído |
|---|---|---|---|
| [CACE, biblioteca de estudios](https://www.cace.org.ar/pages/biblioteca-de-estudios) | El resumen público del estudio anual; año de los datos, muestra de socias y pesos corrientes. El informe completo es solo para socios | Cámara | Resumen de prensa |
| AMVO, *Estudio de Venta Online 2026* | El año del título no es el de los datos (2025) | Asociación | Nota de prensa especializada |
| [Disposición 954/2025](https://www.boletinoficial.gob.ar/detalleAviso/primera/330827/20250904) | Arts. 1 a 6, 8 y 10: botón de arrepentimiento, botón de baja y atención. Ver [Normativa](../Normativa/normativa.md) | Norma | Texto |
| [Código Civil y Comercial, arts. 1105-1116](https://www.argentina.gob.ar/normativa/nacional/ley-26994-235975/texto) | El 1111 (sin información, el derecho de revocar no se extingue) y el 1116 (excepciones) | Norma | Texto |
| [BCRA, Transferencias 3.0](https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/) | Reglas y costo de los pagos con transferencia | Organismo | Texto |

Las cifras de estas fuentes están en [Cifras del mercado](cifras-del-mercado.md).
