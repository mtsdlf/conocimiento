---
tema: Comercio electrónico
para: entender cómo funciona el comercio electrónico y las plataformas de tiendas online, para poder analizar ese mercado y a sus jugadores antes de diseñar un producto propio; la leen Matias, Fer y los agentes, y la usan después los repos de cada empresa, que enlazan las notas de acá
nivel: entiende de negocio y de software pero no conoce el dominio del comercio electrónico; no se da por sabido su vocabulario (pasarela, adquirente, contracargo, GMV, take rate)
escuela: neutral; el método de investigación de usabilidad de Baymard como referencia para checkout, con sus límites
fuera:
  - cómo se analiza a un competidor (tema Estrategia-competitiva; se enlaza)
  - plataformas de dos lados, efecto de red y competir con la plataforma (tema Producto/Plataformas; se enlaza)
  - marketing para tiendas: canales, SEO, ads, email (tema Marketing; se enlaza)
  - usabilidad y formularios en general (tema UX; se enlaza)
  - pagos como sistema distribuido: sagas, idempotencia (tema Arquitectura; se enlaza)
  - impuestos en detalle y lo legal de una empresa (tema Emprender/Legal-e-impuestos; se enlaza)
  - el análisis de un mercado o de competidores concretos (repo de la empresa que decide)
fuentes: []
preguntas:
  - "¿Qué diferencia hay entre una plataforma de tiendas alojada, una de código abierto y un marketplace, y cómo gana plata cada una?"
  - "¿Quién participa en un pago con tarjeta en una tienda online y quién se queda con qué parte?"
  - "¿Por qué la gente abandona el carrito y qué se sabe con evidencia sobre cómo mejorar un checkout?"
  - "¿Qué números públicos de una plataforma de tiendas sirven para compararla con otra, y cómo se leen?"
  - "¿Qué cambia vender online en Argentina y América Latina: cuotas, medios de pago, normativa?"
aprobado: 2026-11-22
---

# Alcance: Comercio electrónico

El tema es el dominio de la industria para el plan de análisis de competencia (issue #24): lo que hay que saber del comercio electrónico para evaluar con criterio a las plataformas de tiendas online. El pedido sale de la conversación del 2026-11-22, con Tiendanube, Shopify y Escalafy como ejemplos de mercado (la persona escribió «Scalafy» y confirmó que era Escalafy, una app de rentabilidad para tiendas). Es el primer tema del área Industrias: para otro mercado, el proceso se repite con otro tema de dominio y reusa Estrategia-competitiva.

## Árbol

```
Comercio-electronico/
  comercio-electronico.md            el todo: modelos de comercio y las partes de vender online, y cómo se conectan
  Plataforma-de-tiendas/             (a fondo) el software con el que un comercio vende online
    tipos-de-plataforma                alojada, de código abierto, marketplace; headless y composable
    arquitectura-de-plataforma         una instalación para muchas tiendas, temas, tienda de apps, APIs
    negocio-de-una-plataforma          suscripción más ingresos por pagos; GMV, take rate, MRR, bajas
    segmentos-de-comerciantes          emprendedor, pyme, mediana, grande: qué necesita cada uno
    apps-para-comerciantes             las apps que viven en la tienda de apps de una plataforma: tipos, cómo cobran, qué se queda la plataforma
    fichas fechadas                    una por plataforma y una por app de referencia (Escalafy y sus alternativas), con datos públicos
  Pagos/                             (a fondo) cómo cobra una tienda online
    actores-del-pago                   pasarela, adquirente, procesador, agregador, emisor y redes
    costo-de-cobrar                    tasas, plazos de acreditación y conciliación
    fraude-y-contracargos              quién pierde cuando un pago se desconoce
    cuotas                             pagar en cuotas: quién financia y cuánto cuesta
    medios-de-pago-locales             transferencias instantáneas, QR y billeteras
  Checkout-y-conversion/             (a fondo) del carrito al pago
    embudo-de-conversion               las etapas y cómo se mide cada una
    carrito-abandonado                 por qué se abandona, con las cifras y su método
    usabilidad-del-checkout            lo que la investigación de Baymard sostiene y sus límites
  Operaciones-del-comercio/          catálogo, stock, pedidos, envío y última milla, devoluciones (entrada)
  Venta-en-varios-canales/           tienda física, marketplaces y redes (entrada)
  Normativa/                         lo que regula la venta online (entrada; fichas por país)
  Fundamentos/                       qué es, historia breve, bibliografía, fuentes y cifras del mercado (ficha), glosario
```

## Supuestos

- La persona aprobó el árbol en el plan del 2026-11-22 («acepto todas las recomendaciones»): a fondo solo plataforma de tiendas, pagos y checkout; el resto, la entrada de cada parte.
- Las fichas por plataforma traen datos públicos fechados, sin opinión ni comparación: la comparación es trabajo del análisis concreto, en el repo de la empresa.
- La normativa se escribe para Argentina primero, como ficha; otros países quedan nombrados como hueco.
- La investigación de pagos separó las cuotas (financiación) de los medios locales (rieles de pago), que el árbol aprobado juntaba.
- Sumado a pedido de la persona: las apps para comerciantes, porque uno de los ejemplos de mercado (Escalafy) es una app que vive dentro de las plataformas y no una plataforma; con fichas de Escalafy y de sus alternativas con más presencia.
