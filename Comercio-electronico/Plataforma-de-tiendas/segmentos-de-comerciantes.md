---
resumen: >-
  Una plataforma de tiendas atiende a comercios de tamaños muy distintos, del emprendedor que abre su primera tienda a la marca grande con equipo propio. Los separa con una escalera de planes: a medida que el plan sube, la suscripción aumenta, la comisión por venta baja y se suman funciones, capacidad técnica y atención.
estado: vigente
estabilidad: semi
fuentes:
  - "Shopify, pricing: https://www.shopify.com/pricing (leída, consultada el 2026-11-22)"
  - "Tiendanube, planes y precios: https://www.tiendanube.com/planes-y-precios (leída, consultada el 2026-11-22)"
  - "Shopify, 10-K del ejercicio 2025: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm (leído en parte, por tramos)"
  - "VTEX, 20-F del ejercicio 2025: https://www.sec.gov/Archives/edgar/data/1793663/000119312526076504/ck0001793663-20251231.htm (leído en parte, por tramos)"
  - "Tiendanube, API documentation, introducción: https://tiendanube.github.io/api-documentation/intro (leída)"
  - "Bloomberg Línea, Nuvemshop cresceu com foco nos pequenos negócios; marcas médias entraram na mira: https://www.bloomberglinea.com.br/startups/nuvemshop-cresceu-com-foco-nos-pequenos-negocios-marcas-medias-entraram-na-mira/ (según resumen del buscador; sin fecha visible)"
  - "Comercio-electronico/.investigacion/plataforma-de-tiendas.md (secciones 3, 4 y 5)"
  - "Comercio-electronico/.investigacion/huecos-plataformas.md (sección 3)"
aliases: [segmentos de comerciantes, merchant segments, SMB, pyme, mid-market, mediana empresa, enterprise, emprendedor, planes de una plataforma de e-commerce]
creado: 2026-11-22
revisado: 2026-11-22
---

# Segmentos de comerciantes

Una plataforma de tiendas atiende a comercios de tamaños muy distintos, del emprendedor que abre su primera tienda a la marca grande con equipo propio. Los separa con una escalera de planes: a medida que el plan sube, la suscripción aumenta, la comisión por venta baja y se suman funciones, capacidad técnica y atención.

Es la [segmentación](../../Marketing/Mercado-y-cliente/segmentacion.md) aplicada a quien compra una plataforma. Ninguna plataforma leída usa los nombres emprendedor, pyme, mediana y grande: usa nombres de planes. Los cuatro segmentos de abajo son una lectura de esta base a partir de cómo están armados esos planes.

> [!NOTE] Sin fuente todavía: una clasificación de comercios online por facturación o por empleados que usen las plataformas o el campo. Los informes no la encontraron.

## La escalera de planes: más suscripción, menos comisión

Los planes de [Shopify](shopify.md) y de [Tiendanube](tiendanube.md), tomados el mismo día, tienen la misma forma. El plan de entrada es gratis o barato y cobra la comisión más alta por cada venta hecha con una pasarela externa. Cada escalón sube la suscripción y baja esa comisión. El último escalón no tiene precio publicado o tiene solo un piso: Shopify dice que Plus "starts at" un monto mensual, y Tiendanube da el plan Evolución "a consultar". [VTEX](vtex.md) no publica planes: cobra por contrato.

Esa forma hace que el plan conveniente dependa de cuánto vende el comercio. Subir de plan conviene cuando lo que se ahorra en comisión supera lo que sube la suscripción:

> ventas del mes con pasarela externa × (comisión del plan actual − comisión del plan siguiente) > suscripción del plan siguiente − suscripción del plan actual

La fórmula es de esta base, no de las plataformas. Los valores para llenarla están en las fichas. Si el comercio usa la pasarela de la plataforma, la comparación cambia, porque entra la tasa de esa pasarela (ver [costo de cobrar en Argentina](../Pagos/costos-de-cobro-en-argentina.md)).

## Qué suma cada escalón

Lo que cada segmento necesita se lee en lo que suma cada plan. La tabla es una lectura de esta base sobre las páginas de planes del 2026-11-22: las funciones salen sobre todo de la de Tiendanube, y la de varios locales, de la de Shopify. Los nombres de plan son ejemplos y cambian.

| Segmento | Qué suma el plan | Ejemplos de plan |
|---|---|---|
| Emprendedor | una tienda sin costo fijo o con uno bajo; la comisión por venta más alta | Shopify Basic; Tiendanube Inicial y Esencial |
| Pyme | comisión más baja; canales de venta como WhatsApp; acceso al código del tema | Shopify Grow; Tiendanube Impulso |
| Mediana | estadísticas avanzadas; varios centros de distribución | Shopify Advanced; Tiendanube Escala |
| Grande | soporte prioritario, un especialista dedicado y migración asistida; varios locales con punto de venta; precio negociado y contrato | Shopify Plus; Tiendanube Evolución; VTEX |

La capacidad técnica también escala. En la API de Tiendanube, las tiendas de los planes más altos tienen un límite de uso diez veces mayor que el resto (ver [arquitectura de una plataforma](arquitectura-de-plataforma.md#límites-de-uso-el-balde-de-tiendanube)). Una marca grande integra su tienda con otros sistemas y hace muchas más llamadas que un emprendedor.

El modo headless queda arriba de la escalera, en la práctica: pide un equipo de ingeniería que solo tienen los comercios grandes. Las condiciones están en [tipos de plataforma](tipos-de-plataforma.md#cuándo-conviene-headless-o-composable).

## Pocos comercios grandes, mucho volumen

Los comercios grandes son pocos y pesan mucho en el volumen. Shopify dice en su 10-K que Plus se ofrece "at a starting rate that is several times that of our standard Shopify plans", y que parte del crecimiento de su suscripción viene de "higher priced plans, such as Plus". Según un resumen de una nota de Bloomberg Línea sin fecha visible, una minoría de clientes medianos de Nuvemshop concentra una parte del GMV mucho mayor que su peso en cantidad de tiendas.

El 10-K de Shopify pone un límite a esa concentración: "No single merchant has ever represented more than five percent of our total revenues". Ningún comercio solo sostiene a la plataforma, aunque los grandes como grupo pesen mucho.

Por eso una plataforma que nació con emprendedores busca subir de segmento, y una que nació con marcas grandes busca bajar con planes más simples. Esta es una inferencia de esta base: los informes documentan el movimiento de Nuvemshop hacia las marcas medianas, por la nota de Bloomberg Línea, pero no el movimiento inverso.

## El segmento cambia lo que dicen los conteos de tiendas

Contar tiendas mide sobre todo a los comercios chicos, que son la mayoría. Contar entre los usuarios de una herramienta que usan los comercios más grandes da otro ranking. En Argentina, según StoreLeads, Shopify es tercera en tiendas vivas, pero entre las tiendas que usan Klaviyo, una herramienta de email marketing, es la primera con amplitud, según un resumen del buscador. Las cifras y sus métodos están en [presencia en Argentina](presencia-en-argentina.md).

La lectura: una plataforma puede liderar en cantidad de tiendas y no en volumen vendido, o al revés. Sin GMV por plataforma y por país, que ninguna fuente leída publica para Argentina, el conteo de tiendas no dice quién lidera el mercado.

## Cómo se usa al analizar plataformas de tiendas

Al comparar plataformas, la escalera de planes es el mapa de a quién le venden. Para un SaaS que evalúa el mercado:

1. Tomá las páginas de planes de los competidores el mismo día y anotá suscripción y comisión con pasarela externa por escalón. La comisión muestra el incentivo a usar la pasarela propia, que es donde gana la plataforma (ver [el negocio de una plataforma](negocio-de-una-plataforma.md)).
2. Marcá en qué escalón aparece cada función. Lo que una plataforma pone en el plan alto es lo que cree que pagan los comercios grandes.
3. Ubicá el segmento que querés atender y qué escalón de cada competidor le corresponde. Comparar el plan de entrada de uno con el plan alto de otro mide segmentos distintos.

Cómo se arma una comparación de precios entre competidores, y sus límites, está en [precios de la competencia](../../Producto/Monetizacion/precios-de-la-competencia.md). Qué trabajo contrata cada segmento a la plataforma se puede formular como [jobs to be done](../../Marketing/Mercado-y-cliente/jobs-to-be-done.md).

El recurso canónico son las dos páginas de planes, la de Shopify (shopify.com/pricing) y la de Tiendanube (tiendanube.com/planes-y-precios), tomadas el mismo día. Fijarse en la comisión por usar una pasarela externa en cada plan, y en que Shopify aclara que los precios "can differ depending on where your business is based".
