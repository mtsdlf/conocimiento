---
resumen: >-
  Los datos públicos de Astroselling, una app multicanal que conecta una tienda online con Mercado Libre y otros marketplaces, y de Cenit, su app gratis de ganancia real por canal: qué hacen, cómo cobran, sus reseñas y su origen, consultados el 2026-11-22.
estado: borrador
estabilidad: volatil
fuentes:
  - "Astroselling, sitio global: https://www.astroselling.com (leído con navegador y en HTML, 2026-11-22; B2 en los planes, C4 en las cifras de la empresa)"
  - "Astroselling, página de Argentina: https://www.astroselling.com/es/ar/ (leída 2026-11-22; B2)"
  - "Astroselling, precios de órdenes: https://www.astroselling.com/es/orders-pricing/ (leída 2026-11-22; B3)"
  - "Astroselling, términos y condiciones: https://www.astroselling.com/es/terminos-condiciones (leídos 2026-11-22; B2)"
  - "Tiendanube, tienda de aplicaciones, Astroselling: https://www.tiendanube.com/tienda-aplicaciones-nube/astroselling (leída 2026-11-22; B1 en notas y reseñas, C3 en el texto del desarrollador, C4 en el resumen de opiniones hecho con IA)"
  - "Shopify App Store, Astroselling: https://apps.shopify.com/astroselling?locale=es (leída 2026-11-22; B1)"
  - "Nuvemshop, loja de aplicativos, Astroselling: https://www.nuvemshop.com.br/loja-aplicativos-nuvem/astroselling (leída vía herramienta de resumen, 2026-11-22; B2)"
  - "Tiendanube, ayuda, cómo integrar Astroselling: https://ayuda.tiendanube.com/es_ES/123518-aplicaciones-de-canales-de-venta/como-integrar-astroselling-con-mi-tienda (leída vía herramienta de resumen; sin fecha; B2)"
  - "Tiendanube, tienda de aplicaciones, Cenit: https://www.tiendanube.com/tienda-aplicaciones-nube/cenit (leída 2026-11-22; B1)"
  - "Cenit, sitio y demo pública: https://cenit.astroselling.com (leídos 2026-11-22; C3)"
  - "Apps Run The World, Astroselling: https://www.appsruntheworld.com/customers-database/customers/view/astroselling-uruguay (leída vía herramienta de resumen; D5, sin método)"
  - "Experiencia propia, noviembre de 2026, una empresa de software de comercio electrónico: codificación de las reseñas de Astroselling en Tiendanube y Shopify"
aliases: [Astroselling, Cenit, METASYNC, Astroselling LLC]
creado: 2026-11-22
revisado:
---

# Astroselling

Los datos públicos de Astroselling, una app multicanal que conecta una tienda online con Mercado Libre y otros marketplaces, y de Cenit, su app gratis de ganancia real por canal: qué hacen, cómo cobran, sus reseñas y su origen, consultados el 2026-11-22.

Es un caso de [app para comerciantes](apps-para-comerciantes.md) que resuelve lo que [venta en varios canales](../Venta-en-varios-canales/venta-en-varios-canales.md) llama multicanal: un catálogo y un stock para varios canales. Sus pares están en [apps para vendedores de marketplace](apps-para-vendedores-de-marketplace.md), y Cenit entra en [apps de rentabilidad](apps-de-rentabilidad.md). Consultado el 2026-11-22. Las fuentes vivas son [su sitio](https://www.astroselling.com), [la página de Argentina](https://www.astroselling.com/es/ar/) y sus fichas en las tiendas de apps; la escala de calificación de cada fuente está en [fuentes públicas](../../Estrategia-competitiva/Analisis-de-competidores/fuentes-publicas.md#quién-lo-dice-y-si-está-confirmado).

## Qué hace: publicar una vez y sincronizar stock y precio

Conecta una tienda ([Tiendanube](tiendanube.md), [Shopify](shopify.md), [WooCommerce](woocommerce.md) o [Wix](wix.md)) con [Mercado Libre](mercado-libre.md) y otros marketplaces. No vende tienda ni checkout. Su panel tiene cuatro módulos:

| Módulo | Qué hace, según sus páginas |
|---|---|
| Sincronización | stock y precio entre canales en «menos de 60 segundos», con «reglas de mark-up o mark-down» para vender más caro o más barato en cada canal |
| Publicación | publica en lote, con IA para título, descripción y atributos por categoría; packs, combos y kits que descuentan el stock de cada componente |
| Órdenes y logística | las ventas de todos los canales en un lugar y la descarga de etiquetas |
| Facturación | a través del sistema de gestión del comercio: Alegra, Nodum, Odoo y SAP Business One en Argentina; Siigo, Bsale y NetSuite en otros países |

Los canales que nombra son Mercado Libre, Dafiti, Rappi, Falabella, Walmart, Coppel, Liverpool, Paris, Ripley y Amazon, según el país. Al publicar en Mercado Libre deja elegir publicación Clásica o Premium, y exige el SKU cargado para sincronizar, según la ayuda de Tiendanube. Su sincronización se llama METASYNC®. Si es socio certificado del programa de Mercado Libre no quedó confirmado.

## Cobro en dólares, por plan y por órdenes

Precios en dólares por mes, copiados del sitio global y de la página de Argentina el 2026-11-22. Las marcas de cada plan salen del HTML de la tabla. La página argentina ofrece «planes anuales en pesos argentinos» por WhatsApp, sin publicarlos.

| | Starter | Pro | Business | Enterprise |
|---|---|---|---|---|
| Pago anual, por mes | US$ 22,42 | US$ 49,92 | US$ 99,92 | a medida |
| Pago mensual | no publicado | US$ 59,99 | US$ 119,99 | a medida |
| Canales | 2 | 3 | 6 | a medida |
| Productos (SKU) enlazados | 500 | 1.500 | 5.000 | a medida |
| Órdenes incluidas | 100 | 100 | 100 | 100 |
| Reglas de stock, canales premium, etiquetas | no | sí | sí | sí |
| Combos, facturación, reenvío de órdenes, API | no | no | sí | sí |

La prueba es de 7 días sin tarjeta. Los términos dicen que los pagos no se reembolsan, que los precios pueden cambiar con aviso, que cobra con Stripe y que rige la ley de Uruguay. La API puede requerir «un cargo adicional de configuración».

> [!IMPORTANT]
> El sitio publica las órdenes de más de dos maneras que no coinciden. La tabla de planes dice «cada orden adicional cuesta USD 0,10», con paquetes para bajar ese valor. La página de precios de órdenes, enlazada desde los términos, cobra por franja: de 101 a 500 órdenes, US$ 75; de 501 a 1.000, US$ 150; de 1.001 a 1.500, US$ 225; más de 1.500, US$ 500. En Shopify hay además un combo de Starter con hasta 500 órdenes por US$ 51,99 por mes, con tope de 200 publicaciones. No dice si cuenta las órdenes de todos los canales o solo las de los marketplaces.

## Cenit: la ganancia real por canal, gratis

Cenit es una app de Astroselling para ver la «ganancia real por canal, después de comisiones, envíos y costo de mercadería», por producto y en el tiempo. Es gratis y «sin planes que suben a medida que vendés más». Su ficha le habla de frente a quien viene de otra app: «Si venís de Escalafy o de otra app que cobra según la cantidad de órdenes, en Cenit no hay planes».

Es de solo lectura: actualiza cada tres horas, trae 90 días hacia atrás, lee el costo del producto de Tiendanube y marca los productos con pérdida. El comercio carga una vez la comisión de cada canal, y los costos salen de Tiendanube, de una planilla o del sistema contable. Mercado Libre se suma «conectando Astroselling» o con una planilla, así que no se sabe si sirve a quien vende solo en Mercado Libre, sin tienda. En lo leído no descuenta la publicidad, los impuestos ni el costo de las cuotas, y la comisión de la pasarela es una estimación que carga el comercio.

Su demo pública, una tienda ficticia con Mercado Libre, Shopify y Tiendanube, muestra en la portada el reparto del ingreso (ventas, comisiones, envíos, mercadería y ganancia) y el margen real de cada canal, sin configurar nada. Es nueva: la ficha de Tiendanube tiene fecha de alta 2026-09-14 en los datos de la página y una sola reseña, del 21-oct-2026, y muestra 0 instalaciones, que puede ser un campo no informado.

Su sitio afirma que «Ninguna app de rentabilidad calcula por canal», y que solo quien lee todos los canales a la vez puede hacer la cuenta. Es falso en lo medido: [Escalafy](escalafy.md) ya muestra la ganancia por canal con Mercado Libre.

## Presencia y reseñas

| Cifra | Valor | Fuente y fecha |
|---|---|---|
| Reseñas en Tiendanube | 4,2 con 167: 124 de 5 estrellas, 8 de 4, 3 de 3, 7 de 2 y 25 de 1 | ficha de Tiendanube, 2026-11-22 |
| Reseñas en Nuvemshop | 4,2 con 167, la misma cifra: las reseñas son regionales, no solo argentinas | ficha de Nuvemshop, 2026-11-22 |
| Reseñas en Shopify | 4,1 con 65: 47 de 5, 3 de 4, 5 de 2 y 10 de 1; lanzada el 10-dic-2019 | ficha de Shopify, 2026-11-22 |
| Cifras que declara | «+500.000 ventas procesadas», «+26.000.000 productos actualizados», presencia en 12 países | sitio, sin fecha ni auditoría |
| Ingresos y equipo, según un tercero | US$ 2,0 millones en 2024 y unas 15 personas | Apps Run The World, sin método (D5) |

Es la app de canales con más reseñas de la tienda de Tiendanube; las demás de la categoría tienen de 0 a 36. En la lectura de 225 reseñas, quienes la usan le pagan por no vender lo que no tienen y por no cargar dos veces el catálogo, y elogian el soporte humano (66 de 123 reseñas con texto en Tiendanube lo nombran). Les duele que la sincronización se rompa, que sea cara y que desde 2025 cobre además por orden, que el soporte no resuelva los problemas del sistema y que cueste darse de baja. Ninguna habla de ganancia, margen ni rentabilidad por canal. La codificación es propia y sin segunda revisión.

## Origen

En Shopify figura Astroselling LLC, con dirección en Montevideo, Uruguay; los términos se rigen por la ley uruguaya y el WhatsApp comercial para Argentina es un número de Uruguay. Tiene páginas por país para Argentina, Brasil, Chile, Colombia, España y México. Un trabajo de grado de la Universidad ORT describe un módulo de métricas para sus clientes, según el resumen de un buscador; el documento no se pudo leer.

> [!NOTE] Sin fuente todavía: qué tarifa de órdenes rige, qué cuenta como orden, los planes en pesos, el precio mensual del Starter, si es socio certificado de Mercado Libre, cuántos comercios usan Cenit y si el módulo «Responder» contesta preguntas de Mercado Libre o es solo una nota del blog.
