---
resumen: >-
  Una plataforma de tiendas gana plata por dos vías: la suscripción mensual que paga cada comercio y una parte de lo que el comercio vende, sobre todo por procesar sus pagos. La segunda crece con las ventas de los comercios y en Shopify ya es tres cuartos del ingreso; se lee con GMV, take rate, MRR y penetración de pagos.
estado: borrador
estabilidad: estable
fuentes:
  - "Shopify, 10-K del ejercicio 2025 (cierre 31/12/2025), Item 1 y Item 7: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm (leído en parte, por tramos)"
  - "VTEX, 20-F del ejercicio 2025, presentado el 26/02/2026: https://www.sec.gov/Archives/edgar/data/1793663/000119312526076504/ck0001793663-20251231.htm (leído en parte, por tramos)"
  - "MercadoLibre, 10-K del ejercicio 2025: https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm (leído en parte, por tramos)"
  - "Shopify, pricing: https://www.shopify.com/pricing (leída, consultada el 2026-11-22)"
  - "Tiendanube, planes y precios: https://www.tiendanube.com/planes-y-precios (leída, consultada el 2026-11-22)"
  - "Comercio-electronico/.investigacion/plataforma-de-tiendas.md (secciones 3 y 4)"
  - "Comercio-electronico/.investigacion/huecos-plataformas.md (sección 1)"
  - "Comercio-electronico/.investigacion/vistazo.md (sección 2)"
aliases: [modelo de negocio de una plataforma de e-commerce, GMV, gross merchandise volume, volumen bruto de mercadería, take rate, tasa de captura, MRR, monthly recurring revenue, ingreso recurrente mensual, penetración de pagos, attach rate, subscription solutions, merchant solutions]
creado: 2026-11-22
revisado:
---

# El negocio de una plataforma de tiendas

Una plataforma de tiendas gana plata por dos vías: la suscripción mensual que paga cada comercio y una parte de lo que el comercio vende, sobre todo por procesar sus pagos. La segunda crece con las ventas de los comercios y en Shopify ya es tres cuartos del ingreso; se lee con GMV, take rate, MRR y penetración de pagos.

Es el modelo de una plataforma [alojada](tipos-de-plataforma.md). La autoalojada no cobra por el software, y el marketplace cobra una comisión por venta. Quiénes participan en un pago y cuánto cuesta cobrar está en [Pagos](../Pagos/pagos.md); la teoría de a qué lado cobrarle, en [mercado de dos lados](../../Producto/Plataformas/mercado-de-dos-lados.md).

## Suscripción y soluciones para comerciantes

Shopify, que cotiza en Estados Unidos, separa su ingreso en dos segmentos en su 10-K. Los nombres son suyos, y otras plataformas cortan distinto.

| Segmento | Qué incluye, según el 10-K | De qué depende |
|---|---|---|
| Subscription solutions | suscripciones, cargos variables de plataforma, POS Pro, apps, dominios y temas | de cuántos comercios pagan y en qué plan |
| Merchant solutions | sobre todo "payment processing fees and currency conversion fees" de su pasarela, más préstamos, comisiones por referidos y "the sale of shipping labels" | de cuánto venden los comercios |

El 10-K lo dice así: "Our merchant solutions revenues are directionally correlated with the level of GMV". En el ejercicio 2025, merchant solutions fue el 76% del ingreso y la suscripción el 24%. Las cifras completas están en la [ficha de Shopify](shopify.md).

VTEX cobra de otra manera. Sus planes tienen "a fixed fee component and a revenue-sharing component based on a percentage of our customers' GMV", con contratos de 12 a 36 meses, y todo eso entra como ingreso por suscripción. Así, la parte por ventas que Shopify cuenta aparte, VTEX la cuenta dentro de la suscripción. Comparar "ingresos por suscripción" entre las dos sin leer qué incluye cada una da un resultado falso (ver [la ficha de VTEX](vtex.md)).

## Por qué una plataforma gana más con los pagos que con la suscripción

La suscripción es fija por comercio; la comisión por pagos sube con cada venta. Una plataforma que procesa los pagos crece cuando sus comercios crecen, sin cobrarles un plan más caro. En Shopify, el ingreso por merchant solutions creció 35% en 2025 y el de suscripción, 17%.

Las plataformas empujan a usar su propia pasarela con el precio. Shopify y Tiendanube cobran una comisión extra por cada venta que el comercio cobra con una pasarela externa, y esa comisión es más alta en los planes baratos (los valores están en las fichas de [Shopify](shopify.md) y de [Tiendanube](tiendanube.md)). La lectura de esta base: la comisión extra abarata la pasarela propia frente a la externa, y así la plataforma se queda con el margen del pago.

El marketplace llega al mismo lugar por otro camino. En el 10-K de MercadoLibre, la línea financiera (fintech) es una de sus dos grandes líneas, y en Argentina pesa más que la de comercio (ver [la ficha de Mercado Libre](mercado-libre.md)). La lectura de esta base: en las dos clases de plataforma, mover el dinero de los comercios rinde tanto como vender el software o la vidriera, y a veces más.

## GMV: el volumen que pasa por la plataforma

El GMV (gross merchandise volume, volumen bruto de mercadería) suma el valor de todo lo vendido a través de la plataforma. Shopify lo define: "GMV is the total dollar value of orders facilitated through our platform". Y aclara: "GMV does not represent revenue earned by us."

Es el denominador para leer todo lo demás. No es ingreso de la plataforma: es la plata de los comercios que pasa por ella. Cada empresa define su propio GMV, y por eso un GMV no se compara con otro sin leer la definición.

## Take rate: cuánto se queda la plataforma de cada peso vendido

El take rate es el ingreso de la plataforma dividido por el GMV. Mide qué parte de lo vendido se queda la plataforma. Shopify no lo publica con ese nombre en lo leído de su 10-K: es una razón que se calcula.

Con las cifras del ejercicio 2025 de Shopify (US$ millones), el cálculo es de esta base:

| Razón | Cálculo | Resultado |
|---|---|---|
| Take rate de merchant solutions, 2025 | 8.804 / 378.441 | 2,33% del GMV |
| Take rate de merchant solutions, 2024 | 6.530 / 292.275 | 2,23% del GMV |
| Take rate total, 2025 | 11.556 / 378.441 | 3,05% del GMV |

Hay dos cuidados. El numerador incluye préstamos y etiquetas de envío, que no son comisión por pago, así que el take rate no es lo que paga un comercio por cobrar. Y el take rate de otra plataforma se calcula con otro numerador: con VTEX, el mismo cálculo da cerca de 1,15% del GMV, pero mezcla cargos fijos y es aproximado. Las dos cifras no miden lo mismo.

## MRR y penetración de pagos

El MRR (monthly recurring revenue, ingreso recurrente mensual) es el valor de las suscripciones de un mes. Shopify: "MRR is the aggregate value of all subscription plans, excluding variable platform fees". Según un resumen de su 10-K, la empresa lo considera la métrica más ligada al valor de largo plazo de la relación con el comerciante. Al 31 de diciembre de 2025 era de US$ 205 millones, contra 178 un año antes.

La penetración de pagos es la parte del GMV que se cobra con la pasarela de la plataforma. Shopify la publica: 65,6% en 2025, contra 61,9% en 2024. Es una proporción del volumen, no de los comercios: no dice cuántos comercios usan la pasarela, sino cuánto de lo vendido pasa por ella. Es lo más cercano publicado a lo que se suele llamar attach rate de pagos.

> [!NOTE] Sin fuente todavía: las bajas de comerciantes (churn) y el ingreso promedio por comerciante (ARPU) de una plataforma de tiendas. Son métricas del dominio, pero ninguna fuente leída las publica. Tampoco hay un GMV oficial de Tiendanube ni un take rate publicado de Mercado Libre.

## Cómo se leen estas métricas en un competidor

Cómo se lee un 10-K o un 20-F, qué hay en cada ítem y por qué los indicadores no se comparan entre empresas está en [lectura de reportes públicos](../../Estrategia-competitiva/Analisis-de-competidores/lectura-de-reportes-publicos.md). Lo propio de una plataforma de tiendas son cuatro preguntas:

1. ¿Cuánto del ingreso viene de la suscripción y cuánto de las ventas de los comercios? Dice si el negocio depende de sumar comercios o de que vendan más.
2. ¿Cómo define el GMV, y lo publica? Sin GMV no hay take rate.
3. ¿Qué parte del GMV pasa por su pasarela, y cómo cambió? Si sube, la plataforma está convirtiendo comercios en clientes de pagos.
4. ¿Qué hay en el numerador del take rate que se calcula? Préstamos, envíos y publicidad inflan la razón sin ser comisión.

Ejemplo: un SaaS que analiza si entrar a vender a comerciantes puede ver que la plataforma dominante gana tres cuartos de su ingreso con los pagos. Una funcionalidad que la plataforma regala en la suscripción no le cuesta ingreso, y le puede servir para retener comercios que pagan comisión. Con una plataforma que no cotiza, como [Tiendanube](tiendanube.md), casi todo es lo que publica la empresa o la prensa, sin auditoría.

El recurso canónico es el 10-K de Shopify del ejercicio 2025. Leer el Item 1 por las definiciones de los segmentos, de GMV y de MRR, y el Item 7, en la parte de indicadores clave, por las cifras y la penetración de pagos. Fijarse en la frase "GMV does not represent revenue". Después, el 20-F de VTEX, sección 5, para ver un cobro por suscripción con porcentaje del GMV.
