---
resumen: >-
  En autopartes, el comprador no elige la pieza por talle o color sino por el vehículo: marca, modelo, año, motor y posición. Vender online pide datos de compatibilidad entre cada pieza y cada vehículo del parque, que un marketplace grande resuelve con su propio catálogo y que la tienda propia del repuestero tiene que conseguir o cargar a mano.
estado: borrador
estabilidad: semi
fuentes:
  - "Mercado Libre Developers, Compatibilidades entre ítems y productos de Autopartes, actualizada el 12/11/2026: https://developers.mercadolibre.com.ar/compatibilidades-entre-items-y-productos (leída descargándola)"
  - "Centro de Atención de Tiendanube, Qué son los filtros y cómo habilitarlos: https://ayuda.tiendanube.com/es_MX/que-son-los-filtros-y-como-habilitarlos-en-mi-tienda (leída)"
  - "Shopify Help Center, Adding filters: https://help.shopify.com/en/manual/online-store/search-and-discovery/filters (leída)"
  - "Shopify App Store, reseñas de 10 apps de compatibilidad por vehículo (leídas una por una, 2026-11-22)"
  - "Comercio-electronico/.investigacion/rubros-autopartes.md y rubros-refutacion.md (2026-11-22)"
aliases: [repuestos, autopartes online, compatibilidad de autopartes, fitment, year make model, YMM, repuestero, accesorios para vehículos]
creado: 2026-11-22
revisado:
---

# Autopartes

En autopartes, el comprador no elige la pieza por talle o color sino por el vehículo: marca, modelo, año, motor y posición. Vender online pide datos de compatibilidad entre cada pieza y cada vehículo del parque, que un marketplace grande resuelve con su propio catálogo y que la tienda propia del repuestero tiene que conseguir o cargar a mano.

Es uno de los [rubros](rubros.md) con necesidades propias. Lo que rompe es el supuesto de que el [catálogo](../Operaciones-del-comercio/catalogo-y-stock.md) se describe con variantes: una pastilla de freno no tiene variantes, tiene una lista de autos en los que entra.

## Las tres piezas de una búsqueda por vehículo

Para que un comprador encuentre la pieza que le va a su auto hacen falta tres cosas, y conviene separarlas porque las resuelven actores distintos:

1. **El buscador** que pide marca, modelo y año y filtra el catálogo. Es software, y es lo que venden las apps de «year make model».
2. **El catálogo de vehículos del país**: qué modelos y motores existen en el parque. Es un dato local; el parque argentino no es el de Estados Unidos.
3. **Los datos de compatibilidad**: qué pieza entra en qué vehículo. Los producen los fabricantes de autopartes y los consolidan empresas de datos; en Estados Unidos hay estándares (ACES y PIES) y proveedores que los venden.

Sin la tercera, el buscador no sirve: «The year-make-model search is only as good as your store's fitment data», dice una reseña de una de esas apps.

## Por qué el marketplace lo resuelve y la tienda propia no

El marketplace grande de la región tiene su propio catálogo de vehículos para cada país, sugiere compatibilidades a los vendedores y puede pausar las publicaciones de autopartes que las tienen incompletas. Desde el 15/07/2026, su API solo da un resumen de las compatibilidades que pone su catálogo y no deja editarlas ni copiarlas; las que carga el vendedor siguen manejándose por API.

Las plataformas generales de tiendas no traen búsqueda por vehículo. La ayuda de una dice que «no es posible agregar filtros adicionales de forma manual»; la de otra permite filtros propios pero no encadenados (primero la marca, después el modelo), con un tope de valores y sin filtros en colecciones grandes. Las apps de terceros agregan el buscador, pero el comercio carga los datos, salvo las que traen datos de Estados Unidos.

En 77 reseñas de esas apps leídas una por una, la queja más repetida entre las negativas es justamente cargar los datos (6 de 17). Ninguna era de un comercio argentino.

## Quién tiene los datos del parque argentino

Los datos existen: una empresa de datos del sector arma el informe del parque para la cámara de fabricantes y vende catálogos y tablas de compatibilidad, y esa cámara lanzó en 2020 un catálogo unificado de sus asociados. Los dos están pensados para fabricantes y distribuidores, sin precio publicado ni conector a una tienda en lo leído. Los catálogos de cada marca son gratis pero de a una marca. Los nombres están en [rubros en Argentina](rubros-en-argentina.md#autopartes).

## Lo que no está medido

No hay dato argentino de cuántas piezas se devuelven por no entrar: las cifras de 18% a 20% que circulan son de proveedores de Estados Unidos. Tampoco hay quejas públicas de repuesteros argentinos sobre la compatibilidad: el dolor está documentado por las plataformas, no por los comercios.
