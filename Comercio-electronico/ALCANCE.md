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
  - "¿Qué distingue a un mayorista o distribuidor que vende a otros comercios de una tienda que vende al público, y qué software usa cada eslabón de la cadena?"
  - "¿Cuántas empresas venden al por mayor en Argentina, cuánto pagan por su software y de qué se quejan?"
  - "¿Qué hace un sistema de gestión de pyme que no hace una plataforma de tiendas, cómo se conecta con la tienda y con Mercado Libre, y dónde suele fallar?"
  - "Tengo un local y una tienda online en Argentina: ¿cómo comparto el stock, cobro en el mostrador y facturo, y con qué opciones y precios?"
  - "¿Quién tiene que emitir factura electrónica en Argentina, qué letra de comprobante corresponde y cómo la emite un sistema?"
  - "¿Qué rubros tienen necesidades que una tienda online general resuelve mal, cuántos comercios hay en cada uno en Argentina, quién los atiende y cuánto pagan?"
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
  Operaciones-del-comercio/          del stock a la entrega (partida el 2026-11-22)
    operaciones-del-comercio           la cadena de estados; pedido, envío y atención mientras no tengan nota
    catalogo-y-stock                   variante, SKU, estados del stock y sobreventa
    devoluciones                       lo que cuestan y lo que obliga la ley
    Sistemas-de-gestion/               el software que lleva el negocio detrás de la tienda
      sistemas-de-gestion                qué es un sistema de gestión de pyme, sus módulos y tipos, cómo se elige y cómo falla
      integracion-con-tiendas-y-marketplaces   cómo se conecta con la tienda y el marketplace, quién manda en el stock, cómo falla
      sistemas-de-gestion-en-argentina   ficha comparativa fechada: precios, integraciones y reseñas
      fichas por sistema                 Tango, Dux, Contabilium, Xubio, Colppy, Bsale y los que aparezcan
    Envios-y-logistica/                (prevista; la escribe otra tanda) transportistas, agregadores, tarifas
  Venta-en-varios-canales/           tienda propia, marketplaces, redes y local (entrada)
    Local-fisico-con-caja/             el comercio con local que también vende online
      local-fisico-con-caja              qué cambia vender con mostrador y online a la vez
      punto-de-venta                     qué hace un POS y en qué se diferencia del lector de cobro y del sistema de gestión
      retiro-en-el-local-y-stock-compartido   omnicanalidad práctica: stock por ubicación, retiro, envío desde el local, con su evidencia
      puntos-de-venta-en-argentina       ficha fechada: POS de las plataformas, lectores de cobro y sus precios
  Normativa/                         lo que regula la venta online (entrada; fichas por país)
    factura-electronica-de-arca        quién factura, qué comprobante, cómo lo emite un sistema y el controlador fiscal
  Comercio-B2B/                      (a fondo, sumada el 2026-11-22) la venta entre empresas: mayoristas, distribuidores y fabricantes que venden a comercios
    comercio-b2b.md                    entrada: qué la distingue, la cadena y los modelos de software, y cómo se conectan
    cadena-de-distribucion             fabricante, distribuidor, mayorista y minorista: qué hace cada eslabón; canal tradicional y moderno en Argentina
    precio-por-cliente                 listas por cliente, zona o canal; escalas por volumen; mínimos y bultos cerrados
    cuenta-corriente-y-credito         venta a plazo, límite de crédito, cobranza, cheque y echeq
    pedido-b2b                         reposición recurrente, catálogos grandes, pedido por chat o planilla y autoservicio del cliente
    preventa-y-autoventa               el vendedor en la calle: rutas, toma de pedido sin conexión y reparto
    factura-entre-empresas             factura A, percepciones y retenciones, factura de crédito electrónica MiPyME (Argentina)
    modelos-de-software-b2b            portal B2B, capa mayorista de una tienda, app de preventa, sistema de gestión, marketplace B2B y app del fabricante
    fichas fechadas                    software B2B en Argentina; portales B2B globales; marketplaces y apps B2B de la región; cifras del comercio B2B
  Rubros/                            (sumada el 2026-11-22) los rubros con necesidades propias que una tienda general resuelve mal
    rubros.md                          entrada: qué supuesto de la tienda general rompe cada rubro, cómo se reconoce un dolor que se paga y cómo se cuenta un rubro
    gastronomia-con-delivery           apps de delivery, canal propio y lo que le falta a la tienda general para comida
    autopartes                         la compatibilidad pieza–vehículo y quién tiene los datos
    ferreteria-y-materiales            catálogos enormes, listas de precios de proveedores y venta a gremio
    indumentaria-y-calzado             el talle y el cambio de talle
    farmacia                           la venta regulada del medicamento y la dispensa digital (a medias)
    rubros-en-argentina                ficha fechada: locales por rubro, ranking de CACE, comisiones, software y reseñas
  Fundamentos/                       qué es, historia breve, bibliografía, fuentes y cifras del mercado (ficha), glosario
```

## Supuestos

- La persona aprobó el árbol en el plan del 2026-11-22 («acepto todas las recomendaciones»): a fondo solo plataforma de tiendas, pagos y checkout; el resto, la entrada de cada parte.
- Las fichas por plataforma traen datos públicos fechados, sin opinión ni comparación: la comparación es trabajo del análisis concreto, en el repo de la empresa.
- La normativa se escribe para Argentina primero, como ficha; otros países quedan nombrados como hueco.
- La investigación de pagos separó las cuotas (financiación) de los medios locales (rieles de pago), que el árbol aprobado juntaba.
- Sumado a pedido de la persona el 2026-11-22: la vertical Comercio-B2B, a fondo. Los rasgos del B2B (precio, crédito, pedido, preventa, factura) son componentes y no una sola nota, porque cada uno se enlaza solo desde las fichas y desde el análisis de un mercado. El método de la base pone «B2B» como ejemplo de corte transversal y no de parte; acá se tomó como vertical porque, en este dominio, vender a otra empresa tiene su propia cadena, su propio software y su propia operación (precio por cliente, crédito, preventa, factura), con notas que no se repiten en las otras verticales. La factura entre empresas vive en esta vertical y no en Normativa porque es parte de cómo se vende entre empresas; Normativa la enlaza. Las fichas se agrupan por modelo de software y no por empresa, para no chocar con las fichas de sistemas de gestión que pueda tener otra vertical. El marketing a empresas sigue en [Marketing B2B](../Marketing/Canales/marketing-b2b.md) y la venta consultiva en Ventas: esta vertical trata la operación de vender a comercios, no cómo se les hace publicidad ni cómo se cierra una venta compleja.
- Sumado a pedido de la persona: las apps para comerciantes, porque uno de los ejemplos de mercado (Escalafy) es una app que vive dentro de las plataformas y no una plataforma; con fichas de Escalafy y de sus alternativas con más presencia.
- Ampliado el 2026-11-22 (tanda 1 de un mapa de oportunidades, plan aprobado por la persona): Operaciones del comercio se partió en componentes, con la subcarpeta Sistemas de gestión; Venta en varios canales suma la subcarpeta Local físico con caja; Normativa suma la factura electrónica de ARCA como nota propia, y la ficha argentina la resume y enlaza. Envíos y logística queda prevista como subcarpeta de Operaciones, sin escribir. El pedido, el envío y la atención siguen en la entrada de Operaciones hasta tener nota.
- Las notas que salieron enteras de la entrada de Operaciones (catálogo y stock, devoluciones) conservan su estado `vigente`, porque su texto es el que la persona ya confirmó; lo nuevo entra como `borrador`.
- Sumado el 2026-11-22 (tanda de un mapa de oportunidades): la vertical Rubros. Como Comercio-B2B, es un corte transversal tomado como vertical, porque cada rubro con necesidades propias tiene su propio software, su propio marketplace y su propio dolor, que no se repiten en las otras verticales. Las notas de cada rubro explican el mecanismo; los nombres, precios y conteos viven en la ficha `rubros-en-argentina`. Farmacia es `volatil` porque su contenido es casi todo regulación en disputa. Óptica, alimentos frescos, mascotas, muebles y servicios con turnos quedaron nombrados como no investigados a fondo.
