---
resumen: >-
  Los datos públicos de Shopify, una plataforma de tiendas alojada: sus planes en dólares, sus cifras del 10-K de 2025, su API y su presencia en Argentina, consultados el 2026-11-22.
estado: vigente
estabilidad: volatil
fuentes:
  - "Shopify, 10-K FY2025 (cierre 31-dic-2025): https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm (leído por tramos; sin leer parte del Item 1 y el último tramo)"
  - "Shopify, Pricing (página de EE.UU.): https://www.shopify.com/pricing (leído vía herramienta de resumen, 2026-11-22)"
  - "Shopify, API versioning: https://shopify.dev/docs/api/usage/versioning (leído vía herramienta de resumen)"
  - "Shopify, Liquid: https://shopify.dev/docs/api/liquid (leído vía herramienta de resumen)"
  - "Shopify Engineering, shard balancing: https://shopify.engineering/mysql-database-shard-balancing-terabyte-scale (leído vía herramienta de resumen)"
  - "Wikipedia, Shopify: https://en.wikipedia.org/wiki/Shopify (según resumen del buscador)"
  - "StoreLeads, Shopify en Argentina: https://storeleads.app/reports/shopify/AR/top-stores (leído; página actualizada 2026-11-13)"
  - "Comercio-electronico/.investigacion/plataforma-de-tiendas.md (secciones 2, 3, 4, 5 y 7)"
  - "Comercio-electronico/.investigacion/huecos-plataformas.md (sección 3)"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (A3)"
aliases: [Shopify Plus, Shopify Payments]
creado: 2026-11-22
revisado: 2026-11-22
---

# Shopify

Los datos públicos de Shopify, una plataforma de tiendas alojada: sus planes en dólares, sus cifras del 10-K de 2025, su API y su presencia en Argentina, consultados el 2026-11-22.

Es un caso de [plataforma alojada](tipos-de-plataforma.md). Sus cifras ilustran el [negocio de una plataforma](negocio-de-una-plataforma.md), y su API y sus pods, la [arquitectura](arquitectura-de-plataforma.md). Consultado el 2026-11-22. Las fuentes vivas son la [página de precios](https://www.shopify.com/pricing), el [10-K en EDGAR](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) y [shopify.dev](https://shopify.dev/docs/api/usage/versioning).

## Origen y mercados

Según Wikipedia, que el informe leyó por el buscador, Shopify nació de Snowdevil, una tienda de snowboards de 2004, y se lanzó en junio de 2006. La historia está en [historia del comercio electrónico](../Fundamentos/historia-del-comercio-electronico.md).

> [!NOTE] Sin fuente todavía: el país de origen y la sede. El informe lo dejó sin verificar.

El 10-K dice que la usan "millions of merchants from more than 175 countries". Al 31-dic-2025, la base de comerciantes se reparte así: 44% EE.UU., 31% EMEA, 16% Asia-Pacífico, Australia y China, 5% Canadá y 5% América Latina. Según el mismo 10-K, "No single merchant has ever represented more than five percent of our total revenues".

## Planes públicos en dólares

Copiado de la página de precios de EE.UU. el 2026-11-22. La página aclara que "Pricing and payment options can differ depending on where your business is based", y no mostró las tarifas de tarjeta.

| Plan | Mensual | Mensual con pago anual | Tarifa por usar un proveedor de pago externo |
|---|---|---|---|
| Basic | US$ 25 | US$ 19 | 2% |
| Grow | US$ 65 | US$ 49 | 1% |
| Advanced | US$ 399 | US$ 299 | 0,6% |
| Plus | "starts at $2,300/mo" | no figura | 0,2% |

El punto de venta POS Pro cuesta US$ 89 por mes y por local; Plus "includes 20 locations". La entrada es una prueba de 3 días y después US$ 1 por mes durante 3 meses. El 10-K describe a Plus como "offered at a starting rate that is several times that of our standard Shopify plans".

## Cifras del 10-K de 2025

Cifras en millones de dólares, al cierre del 31-dic-2025, del tramo MD&A del 10-K. Es una fuente primaria con obligación legal de exactitud, publicada por la propia empresa.

| | 2025 | 2024 | 2023 |
|---|---|---|---|
| Subscription solutions | 2.752 (+17%, 24% del total) | 2.350 (+28%, 26%) | 1.837 (26%) |
| Merchant solutions | 8.804 (+35%, 76%) | 6.530 (+25%, 74%) | 5.223 (74%) |
| Ingresos totales | 11.556 (+30%) | 8.880 (+26%) | 7.060 |
| GMV | 378.441 (+29%) | 292.275 (+24%) | sin dato leído |
| MRR al 31 de diciembre | 205 (+15%) | 178 | 144 |
| GMV vía Shopify Payments | 248,1 mil millones (+37%) | 181,0 mil millones | sin dato leído |
| Penetración de Shopify Payments | 65,6% | 61,9% | sin dato leído |

Por región, la penetración de Shopify Payments al 31-dic-2025 es 88% en Norteamérica, 89% en Asia-Pacífico y 83% en EMEA. Es una proporción del GMV, no de comerciantes.

Las definiciones son literales del 10-K. "GMV is the total dollar value of orders facilitated through our platform" y "GMV does not represent revenue earned by us". "MRR is the aggregate value of all subscription plans, excluding variable platform fees". Merchant solutions viene sobre todo de "payment processing fees and currency conversion fees", más préstamos, comisiones de referidos y "the sale of shipping labels".

En lo leído del 10-K, Shopify no publica un take rate con ese nombre. El informe lo calculó sobre estas cifras: merchant solutions sobre GMV da 2,33% en 2025 y 2,23% en 2024; los ingresos totales sobre GMV, 3,05%. El numerador incluye préstamos y etiquetas, así que no es lo que paga un comercio. Cómo se lee esa razón está en [negocio de una plataforma](negocio-de-una-plataforma.md).

> [!NOTE] Sin fuente todavía: el monto originado por Shopify Capital ("loans and merchant cash advances", según los riesgos del 10-K) y si Shopify Payments opera en Argentina.

## API, temas y tienda de apps

- **Versiones de la API**: "Shopify releases a new API version every three months at 5pm UTC on the first day of the quarter". "Each stable version is supported for a minimum of 12 months", con "at least nine months of overlap". La última estable al 2026-11-22 es 2026-10.
- **Temas**: "Liquid is a template language created by Shopify"; los temas usan una variante que "extends the open-source version of Liquid".
- **Pods**: según el blog de ingeniería, "A pod is an isolated instance of Shopify consisting of an individual MySQL database shard", y "Every pod houses a unique subset of shops on the platform". La clave de partición es `shop_id`.
- **Tienda de apps**: [apps.shopify.com](https://apps.shopify.com). El informe vio que existe y no la midió; el reparto con los desarrolladores está en [apps para comerciantes](apps-para-comerciantes.md).
- **Socios**: lo que paga y prohíbe a las agencias que arman tiendas está en [programa de socios de Shopify](programa-de-socios-de-shopify.md).

> [!NOTE] Sin fuente leída: la Admin API GraphQL, la Storefront API, Hydrogen, Functions y los webhooks figuran solo en un resumen del buscador; falta leer [shopify.dev/docs/api](https://shopify.dev/docs/api).

## Presencia en Argentina

StoreLeads cuenta 9.059 tiendas vivas en Argentina, en su página actualizada el 2026-11-13, sobre un total global mostrado de 3.298.869. Es un rastreador que detecta sitios, no un dato de la empresa. Las otras mediciones y sus métodos están en [presencia en Argentina](presencia-en-argentina.md).
