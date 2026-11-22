---
resumen: >-
  En comercio electrónico, las definiciones y las estadísticas oficiales (OCDE, UNCTAD, oficinas de censos, bancos centrales) y los reportes que las empresas presentan ante reguladores pesan más que las cámaras, y estas más que los proveedores, que producen casi todas las cifras sobre conversión, abandono, cuotas y arquitecturas. Casi cada cifra de proveedor mide algo que el mismo proveedor vende.
estado: borrador
estabilidad: semi
fuentes:
  - "Baymard Institute, Cart abandonment rate: https://baymard.com/lists/cart-abandonment-rate (leído)"
  - "Marketplace Pulse, Amazon takes a 50% cut of sellers' revenue (13/02/2023): https://www.marketplacepulse.com/articles/amazon-takes-a-50-cut-of-sellers-revenue (leído)"
  - "The Good, Ecommerce benchmarks: https://thegood.com/insights/ecommerce-benchmarks/ (leído)"
  - "Growth Suite, The problem with benchmarking your store against industry averages (21/05/2026): https://www.growthsuite.net/blog/the-problem-with-benchmarking-your-store-against-industry-averages (leído)"
  - "EBANX, Beyond Borders 2026, cuotas: https://www.ebanx.com/en/beyond-borders-2026/section-recurring-payments/chapter-installments-and-subscription (leído)"
  - "Elogic, Composable commerce vs headless: https://elogic.co/blog/composable-commerce-vs-headless/ (leído)"
  - "Fastr, The headless commerce productivity myth: https://getfastr.com/blog/the-headless-commerce-productivity-myth-why-composable-stacks (leído)"
  - "VTEX, The MACH mirage (25/03/2025): https://vtex.com/en-us/blog/mach-mirage (leído)"
  - "Littledata, Benchmarks: https://www.littledata.io/benchmarks (leído)"
  - "NRF y Happy Returns, 2024 Consumer Returns in the Retail Industry (nota de prensa): https://nrf.com/media-center/press-releases/nrf-and-happy-returns-report-2024-retail-returns-total-890-billion (leída la nota, no el informe)"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md, secciones A5 y B; Comercio-electronico/.investigacion/vistazo.md, sección 4; Comercio-electronico/.investigacion/checkout-y-conversion.md; Comercio-electronico/.investigacion/pagos.md, sección 4; Comercio-electronico/.investigacion/huecos-pagos-y-operaciones.md, sección 5"
aliases: [peso de las fuentes de e-commerce, fuentes del comercio electrónico, conflicto de interés en e-commerce, e-commerce sources]
creado: 2026-11-22
revisado:
---

# Fuentes de comercio electrónico

En comercio electrónico, las definiciones y las estadísticas oficiales (OCDE, UNCTAD, oficinas de censos, bancos centrales) y los reportes que las empresas presentan ante reguladores pesan más que las cámaras, y estas más que los proveedores, que producen casi todas las cifras sobre conversión, abandono, cuotas y arquitecturas. Casi cada cifra de proveedor mide algo que el mismo proveedor vende.

El dominio tiene un desbalance. Lo que más se discute para diseñar un producto (cuánto convierte un checkout, cuánto suben las ventas con cuotas, si conviene una arquitectura composable) casi no tiene estudios independientes. Lo que tiene fuentes oficiales (el tamaño del mercado, el fraude con tarjetas en Europa, el uso de Pix) sirve para dimensionar, no para decidir un diseño.

## Cómo se pesa una fuente

Los pesos son de esta base, sobre los puntajes del informe de fundamentos (autoridad, profundidad, ejemplos y unicidad, de 1 a 3). Ninguna fuente leída propone pesos por tipo.

| Tipo | Ejemplos | Sirve para | Peso | Por qué |
|---|---|---|---|---|
| Estándares y estadísticas oficiales | Definición de la OCDE de 2025; estimaciones de UNCTAD; e-commerce trimestral de la oficina de censos de Estados Unidos | Qué cuenta como comercio electrónico y cuánto pesa | Alto | Método publicado; UNCTAD cubre pocas economías y su estimación es "relatively uncertain", según un resumen |
| Bancos centrales y reguladores | BCRA, Banco Central do Brasil, EBA y BCE, Reserva Federal, Reglamento (UE) 2015/751 | Reglas, costos regulados y fraude | Alto | Primarias; casi nunca cubren a América Latina en cifras de fraude |
| Reportes ante reguladores | 10-K de Shopify, 20-F de VTEX | El negocio de una plataforma y sus definiciones | Alto en lo que reportan | Auditados, pero la empresa elige qué indicadores mostrar |
| Papers con método | Kukar-Kinney y Close (2010), Rajamma et al. (2009), Li et al. (2021), Hagiu y Wright (2015) | Por qué se abandona, cuándo conviene un marketplace | Alto en su tema | Casi todos se conocen por abstract o resumen; son de Estados Unidos o Asia |
| Cámaras y asociaciones | CACE (Argentina), AMVO (México), ABComm, hoy ABIACOM (Brasil) | El tamaño del mercado local | Medio | Miden a sus socios o a un panel; el informe completo suele ser pago |
| Investigación de proveedores con método declarado | Baymard (usabilidad del checkout), Littledata (embudo), Marketplace Pulse | Orden de magnitud y problemas de diseño | Medio en método, bajo en independencia | Venden la base de datos o el servicio que la cifra justifica |
| Estudios comerciales y pronósticos | eMarketer, Statista | Pronósticos regionales | Medio-bajo | Pronósticos propios, detrás de un muro de pago; eMarketer dio 403 |
| Blogs de proveedores | Plataformas de tiendas, proveedores de pagos, consultoras de composable | Lo reciente y los argumentos | Bajo | Cada uno vende lo que recomienda |
| Wikipedia | Historia del comercio electrónico y de las plataformas | Fechar | Bajo | Terciaria; hay que ir a sus fuentes |

## Quién vende qué

Saber qué vende cada fuente no invalida lo que dice, pero cambia cómo se lee la cifra.

| Fuente | Qué vende | Cómo leerla |
|---|---|---|
| Baymard Institute | La suscripción a su base de investigación de usabilidad | Su 70,22% de abandono es la media simple de 50 estudios de terceros, varios de proveedores de recuperación de carritos; su potencial de mejora es una estimación propia. Ver [Carrito abandonado](../Checkout-y-conversion/carrito-abandonado.md) |
| Littledata | Analítica para tiendas Shopify | Muestra de 449 tiendas clientes que superan 1.000 sesiones; deja afuera a las chicas |
| Dynamic Yield, IRP Commerce | Personalización; servicios a comercios | Paneles de sus clientes; IRP no publica método. Ver [Embudo de conversión](../Checkout-y-conversion/embudo-de-conversion.md) |
| EBANX, dLocal, Stripe | Procesamiento de pagos, incluidas las cuotas | EBANX dice que las cuotas pueden "double the average order value (AOV) in Brazil" con "EBANX internal data", sin muestra ni método. Ver [Cuotas](../Pagos/cuotas.md) |
| Elogic, Fastr, VTEX, MACH Alliance | Servicios de composable, vitrinas, una plataforma unificada; componentes MACH | Elogic y Fastr dan sobrecostos de composable sin método; VTEX critica MACH sin datos y vende la alternativa. Ver [Tipos de plataforma](../Plataforma-de-tiendas/tipos-de-plataforma.md) |
| Blog de una plataforma de tiendas | Tiendas propias | Sus notas contra vender en marketplace citan charlas sin método. Ver [Venta en varios canales](../Venta-en-varios-canales/venta-en-varios-canales.md) |
| Marketplace Pulse | Investigación y medios sobre marketplaces | Datos de P&L de vendedores de Amazon, con muestra sin tamaño publicado |
| The Good, Growth Suite | Optimización de conversión; una app de analítica | Sus argumentos contra los benchmarks son razonables; Growth Suite no cita primarias y sus cifras no se pueden verificar |
| Medallia (estudio de HBR de 2017) | Software de experiencia del cliente | 46.000 clientes de un solo minorista, según un white paper de la empresa citado por el buscador |
| NRF y Happy Returns | Happy Returns es de UPS y vende servicios de devoluciones | Su 16,9% de devoluciones es una estimación de minoristas de Estados Unidos |

## Reglas para leer una cifra

1. Buscá el año de los datos, que no es el del título. El estudio de AMVO "2026" trae datos de 2025.
2. Buscá quién mide y con qué muestra: socios de una cámara, un panel de compradores, los clientes de un proveedor.
3. Buscá la definición. La tasa de conversión cambia según se divida por sesiones o por visitantes; el comercio electrónico de UNCTAD incluye EDI entre empresas y el de las cámaras suele ser solo venta a consumidores.
4. Si la fuente vende algo relacionado, escribí "afirmación de proveedor" junto a la cifra.
5. Contá las fuentes de verdad. Tres comunicados de EBANX con la base de PCMI son una sola fuente, y lo mismo ABComm y ABIACOM, que es la misma asociación con otro nombre.
6. Si es dinero en pesos argentinos, separá el crecimiento nominal del real.

## Lo que no se puede leer gratis

El informe completo de CACE es solo para socios; eMarketer y Statista están detrás de un muro de pago; de AMVO se leyó una nota especializada, no el estudio. Los papers de abandono y de omnicanalidad tienen acceso restringido y se conocen por abstract o resumen. Lo que sí se lee entero y gratis: la definición de la OCDE, las notas de UNCTAD, la oficina de censos, los 10-K y 20-F, las normas y la documentación para desarrolladores de las plataformas.

> [!NOTE]
> Sin fuente todavía: un estudio independiente (académico o de un analista abierto) sobre los costos de headless y composable, sobre la rentabilidad de vender en marketplace o en tienda propia, sobre la rentabilidad neta de la omnicanalidad y sobre el efecto de las cuotas sin interés en las ventas en Argentina, Brasil o México. Ninguno apareció en la investigación.
