---
resumen: >-
  Los datos públicos de Escalafy, una app de analítica de rentabilidad que se conecta a plataformas de tiendas y a un marketplace: qué hace, dónde se instala, cómo cobra y sus cifras, con las discrepancias entre sus propias páginas, consultados el 2026-11-22.
estado: vigente
estabilidad: volatil
fuentes:
  - "Escalafy, sitio en inglés: https://www.escalafy.com/en (leído vía herramienta de resumen, 2026-11-22; fuente de la empresa, con interés comercial)"
  - "Escalafy, sitio en español: https://www.escalafy.com/ (leído vía herramienta de resumen, 2026-11-22)"
  - "Escalafy, precios de Analítica: https://www.escalafy.com/en/pricing (leído con navegador moviendo el deslizador, 2026-11-22; B2)"
  - "Escalafy, precios del Pixel: https://www.escalafy.com/en/pricing/pixel (leído con navegador, 2026-11-22; B2)"
  - "Escalafy, integraciones: https://www.escalafy.com/en/integrations (leído 2026-11-22; C3)"
  - "Escalafy, stock multicanal y comisiones de Mercado Libre: https://www.escalafy.com/en/product/multichannel-inventory y https://www.escalafy.com/en/product/mercado-libre-fees (leídos 2026-11-22; C3, lo que dice que hace)"
  - "Escalafy, MCP y API: https://www.escalafy.com/en/product/mcp-api (leído 2026-11-22; C3)"
  - "Escalafy, comparaciones: https://www.escalafy.com/en/compare (leído 2026-11-22; C4, los precios de los rivales los verifica la propia empresa)"
  - "Escalafy, informe del Cyber Week 2026 de Argentina: https://www.escalafy.com/en/benchmarks/cybermonday-2026 (leída la parte abierta, 2026-11-22; C4)"
  - "Experiencia propia, noviembre de 2026, una empresa de software de comercio electrónico: codificación de 263 reseñas de Escalafy en Shopify y Tiendanube, y lectura del HTML de dos tiendas con su pixel"
  - "Shopify App Store, Escalafy: https://apps.shopify.com/escalafy (leído vía herramienta de resumen, 2026-11-22)"
  - "Tiendanube, tienda de aplicaciones, Escalafy: https://www.tiendanube.com/mx/tienda-aplicaciones-nube/escalafy (leído vía herramienta de resumen, 2026-11-22)"
  - "Capterra, Escalafy: https://www.capterra.com/p/10034658/Escalafy/ (según resumen del buscador)"
  - "Comercio-electronico/.investigacion/huecos-plataformas.md (sección 4a)"
  - "Comercio-electronico/.investigacion/plataforma-de-tiendas.md (sección 6)"
aliases: [Escalafy Analytics, Escalafy Pixel]
creado: 2026-11-22
revisado: 2026-11-22
---

# Escalafy

Los datos públicos de Escalafy, una app de analítica de rentabilidad que se conecta a plataformas de tiendas y a un marketplace: qué hace, dónde se instala, cómo cobra y sus cifras, con las discrepancias entre sus propias páginas, consultados el 2026-11-22.

Es un caso de [app para comerciantes](apps-para-comerciantes.md): no es una plataforma de tiendas, vive en las tiendas de apps de dos de ellas. Sus alternativas están en [apps de rentabilidad](apps-de-rentabilidad.md). Consultado el 2026-11-22. Las fuentes vivas son [su sitio](https://www.escalafy.com/en), [sus precios](https://www.escalafy.com/en/pricing) y sus fichas en la [tienda de apps de Shopify](https://apps.shopify.com/escalafy) y en la de [Tiendanube](https://www.tiendanube.com/mx/tienda-aplicaciones-nube/escalafy). Todas son de la empresa o de las plataformas que la venden, con interés comercial. La escala de calificación de las fuentes está en [fuentes públicas](../../Estrategia-competitiva/Analisis-de-competidores/fuentes-publicas.md#quién-lo-dice-y-si-está-confirmado).

## Qué hace y dónde se conecta

Se presenta como "Data intelligence for e-commerce brands" y, en español, como "la plataforma de inteligencia de datos para marcas de e-commerce que quieren escalar". Junta ventas, costos y gasto en publicidad para mostrar la ganancia por canal, producto y pedido, y rastrea qué anuncio origina cada venta.

Tiene dos productos que se contratan por separado. Analytics da la ganancia real por día, pedido, canal, producto y variante, el ROAS real por campaña, las comisiones de Mercado Libre desarmadas por venta, el valor de vida del cliente y cohortes. Pixel manda eventos del lado del servidor a Meta, Google y TikTok e identifica visitantes para Klaviyo y Perfit. El sitio en inglés lista los módulos Analytics, Pixel, Ads, Products, Inventory, Lifetime Value y MCP/API.

Para Mercado Libre dice leer de la API el cargo por categoría de cada venta («it doesn't estimate them») y desarmar «50 different ways» de cobrar: cargo por categoría, publicación Oro o Clásica, Full, cuotas, percepciones de Ingresos Brutos y retenciones. Su página de stock multicanal dice sincronizar el stock entre Tiendanube, Shopify y Mercado Libre «in seconds», con variantes y combos; no se vio que publique ni que fije precio por canal, y la escritura no se probó con una cuenta. Su servidor MCP funciona con Claude, ChatGPT, Gemini y Grok, y es de solo lectura salvo para cargar costos y tablas de envío. La ficha de Tiendanube dice que con el MCP «subes anuncios a Meta desde Claude o ChatGPT», y la página del MCP dice que «doesn't touch your campaigns»: no coinciden.

| Se conecta con | Cuáles, según sus páginas |
|---|---|
| Plataformas de venta | [Shopify](shopify.md), [Tiendanube](tiendanube.md) y [Mercado Libre](mercado-libre.md), con una página de producto "Mercado Libre fees" |
| Publicidad y email | Meta, Google, TikTok, Klaviyo y Perfit |
| Pagos | Mercado Pago, que toma comisiones y cuotas «sin conectar nada»; aparecen además el campo "Comisiones de pago" y el valor de ejemplo "shopify_payments" |
| IA | cuatro asistentes por MCP: Claude, ChatGPT, Gemini y Grok |
| Envíos y costos | sin proveedores nombrados; los costos de producto se cargan una vez a mano («cargas tus costos de producto una vez») |

La página de integraciones lista 13: 2 tiendas, 1 marketplace (con Mercado Ads y Full), 3 de publicidad, 2 de email, 1 de pagos y 4 de IA, con un formulario para pedir más. En Shopify corre como bloque embebido del tema con un proxy de la app; en Tiendanube agrega al formulario de compra campos `extra[esc_*]` con identificadores de visitante, cookies de Meta, TikTok, Google y Microsoft y las UTM, que viajan con el pedido (observado en el HTML de tiendas con la app, 2026-11-22).

## Cobro por pedidos del mes

Es una suscripción mensual que sube con la cantidad de pedidos: "The price follows your orders for the month. Sell less, pay less." No pide contrato anual y el alta cuesta US$ 0. Analítica tiene 7 días de prueba y Pixel 14, más 30 días de garantía; el pie del inicio dice «Start 14 days free», que no coincide con los 7 días de Analítica.

Precios en dólares por mes, leídos moviendo el deslizador de las dos páginas de precios el 2026-11-22:

| Pedidos del mes | Analítica Base | Analítica Advanced | Pixel |
|---|---|---|---|
| hasta 50 | gratis | — («From 300 orders») | — |
| hasta 300 | 19 | 30 | — |
| hasta 900 | 49 | 75 | 99 |
| hasta 2.500 | 99 | 150 | 149 |
| hasta 5.000 | 149 | 225 | 199 |
| hasta 10.000 | 199 | 300 | 279 |
| hasta 25.000 | 299 | 450 | 399 |
| hasta 50.000 | 399 | 600 | a medida en el sitio; «desde 499» en la ficha de Tiendanube |
| hasta 100.000 | 549 | 825 | a medida |
| más de 100.000 | a medida, por WhatsApp | a medida | a medida |

Advanced suma la API y el MCP. Una marca de 2.500 pedidos con Advanced y Pixel paga US$ 299 por mes (cálculo de esta base). Sus páginas de comparación lo ponen contra Polar (US$ 750), Triple Whale (US$ 129) y Northbeam (US$ 1.500), con precios que verifica la propia empresa.

| Otras páginas | Planes y precios |
|---|---|
| Ficha de Shopify | Free (hasta 50 pedidos), Pro Analytics US$ 19/mes (prueba de 7 días), Pro Pixel US$ 99/mes (prueba de 14 días) |
| Ficha de Tiendanube | Analítica gratis hasta 50 órdenes/mes, Base US$ 19, Advanced US$ 30; Pixel desde US$ 99/mes |
| Capterra, según el buscador | Growth US$ 19, Scale US$ 49, Pro US$ 99, más uno gratis |

> [!IMPORTANT]
> La ficha de Shopify no muestra el plan Advanced de US$ 30, y Capterra, según el buscador, da otros nombres de planes y un precio de US$ 49 que no aparece en ninguna página de la empresa. Arriba de 25.000 pedidos, el Pixel es «a medida» en el sitio y «desde 499» en la ficha de Tiendanube.

## Cifras públicas

| Cifra | Valor | Fuente y fecha |
|---|---|---|
| Lanzamiento en la tienda de apps de Shopify | 6-oct-2025 | ficha de Shopify |
| Idiomas | español, portugués (Brasil) e inglés | ficha de Shopify |
| Marcas conectadas | 9.260, sin definir qué es "conectada"; «+8.000 marcas de Tiendanube y Shopify en LATAM, Estados Unidos y Europa» en la ficha de Tiendanube | sitio y ficha de Tiendanube, 2026-11-22 |
| Facturación analizada | «$140M in revenue analysed per month» | sitio, 2026-11-22 |
| País de las reseñas de Shopify | de 102: 90 de Argentina, 10 de Uruguay, 1 de España y 1 de Austria | ficha de Shopify, 2026-11-22 |
| Reseñas en Shopify | 5,0 con 102 reseñas | ficha de Shopify, 2026-11-22 |
| Reseñas en Tiendanube | 5,0 con 163 reseñas, todas de 5 estrellas | ficha de Tiendanube, 2026-11-22 |
| Reseñas que declara el sitio | "318 reseñas verificadas" con 5,0, que desglosa como 163 y 155 | sitio, 2026-11-22 |

> [!IMPORTANT]
> Las cifras de la empresa no cierran entre sí. La ficha de Shopify decía "+3.000 marcas en LatAm" según un resumen del buscador; el sitio en inglés daba 9.099 marcas conectadas según el mismo tipo de resumen, y 9.260 al leerlo el 2026-11-22. Las reseñas de Shopify y Tiendanube suman 265, no las 318 del sitio: el sitio le atribuye 155 a Shopify, cuya ficha muestra 102.

De las 263 reseñas codificadas, 262 son de 5 estrellas y 1 de 4: el 5,0 no separa a Escalafy de nada. Más de la mitad de las de Shopify se escribieron en el primer mes, cerca del fin de la prueba. Lo que valoran es la ganancia real con los costos argentinos (cuotas, comisiones de Mercado Libre, impuestos); la atribución aparece en unas 31. Ninguna se queja. La codificación es propia, sin segunda revisión.

Publica una comparación contra un rival casi por semana y un informe propio de benchmarks con los pedidos de sus clientes. En el del CyberMonday 2026 de Argentina, la tienda típica creció 42% y se quedó con US$ 20,9 de cada 100 vendidos (dato de la empresa, sin tamaño de muestra en la parte abierta; C4). En la tienda de Tiendanube aparecen como apps parecidas Dash Analytics, Estadísticas Nube, Detrics, Master Metrics, Dashbo y DataCrack; las que tienen datos están en [apps de rentabilidad](apps-de-rentabilidad.md).

## Origen

El sitio no declara país de origen. Su pie de página dice "Escalafy LLC, 5830 E 2nd St, Casper, WY 82604", en Wyoming, EE.UU., y la ficha de Shopify da una dirección en Casper. La ficha de Shopify dice «Ubicadas en Argentina», pero se refiere a las tiendas donde la app es popular, no a la empresa. En Tiendanube el desarrollador figuraba como "be-flowing" y ahora figura como "Escalafy". Una reseña nombra a uno de los fundadores, que atiende el soporte por WhatsApp.

> [!NOTE] Sin fuente todavía: rondas de inversión, empleados, ingresos, instalaciones (ninguna tienda de apps las muestra en lo leído), cuántas de las marcas conectadas pagan, si la sincronización de stock escribe de verdad en Mercado Libre, y una medición independiente de los resultados del Pixel. Su informe separa tiendas de más de US$ 150 mil por mes y de menos de US$ 5 mil, así que tiene clientes en las dos puntas.
