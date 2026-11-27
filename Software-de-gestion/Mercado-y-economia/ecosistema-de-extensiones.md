---
resumen: >-
  El ecosistema de extensiones de un software de gestión son los módulos que hacen terceros para sumarle un rubro, una función o una localización, y que el proveedor publica en su tienda a cambio de una comisión. Funciona como cualquier ecosistema de plataforma, con una diferencia: la extensión escribe en los mismos registros que lleva la contabilidad.
estado: vigente
estabilidad: semi
fuentes:
  - "Blog de un proveedor grande de software de empresa, Drive growth with the most partner-focused business platform (2021-07-14): https://azure.microsoft.com/blog/drive-growth-with-the-most-partnerfocused-business-platform/ (leído)"
  - "Software-de-gestion/.investigacion/mercado-y-economia.md (2026-11-27), sección 4"
aliases: [extensiones, add-ons, agregados, apps de terceros, tienda de extensiones, marketplace de aplicaciones de empresa, ISV, desarrollador independiente de software, independent software vendor]
creado: 2026-11-27
revisado: 2026-11-27
---

# Ecosistema de extensiones

El ecosistema de extensiones de un software de gestión son los módulos que hacen terceros para sumarle un rubro, una función o una localización, y que el proveedor publica en su tienda a cambio de una comisión. Funciona como cualquier ecosistema de plataforma, con una diferencia: la extensión escribe en los mismos registros que lleva la contabilidad.

La teoría general (qué abre una plataforma, cuánto cobra, cuándo absorbe lo que hicieron otros) está en [ecosistema de terceros](../../Producto/Plataformas/ecosistema-de-terceros.md) y no se repite. Acá va lo propio del software de gestión, que tiene poca literatura propia. Quién hace las extensiones suele ser un partner del [canal](canal-de-partners.md), y cómo se suma una sin tocar el núcleo del producto es la decisión de [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md).

## Qué completan las extensiones

Un software de gestión horizontal trae los dominios comunes y deja huecos que llenan los terceros (lectura de esta base, sin estudio que lo mida):

- **Un rubro.** Lo que necesita una bodega, una clínica o una constructora y el producto no trae; es la forma más barata de volver vertical un producto horizontal ([software por rubro](../Categorias-de-producto/software-por-rubro.md)).
- **Una localización.** Los comprobantes, libros y regímenes de un país, cuando el proveedor no los mantiene ([software de gestión en la Argentina](../software-de-gestion-en-argentina.md)).
- **Una conexión.** Con un banco, una tienda online, un transportista o un sistema de planta ([integración y migración](../Columnas-tecnicas/integracion-y-migracion.md)).

## Cuánto cobra la tienda

El único dato primario hallado de una tienda de software de empresa es de un proveedor grande. Desde el 1 de julio de 2021 bajó la comisión de su mercado comercial, que incluye su tienda de aplicaciones de negocio, «from an industry-standard 20 percent to 3 percent» para las ofertas que se venden por la tienda. Su programa para desarrolladores de aplicaciones de gestión se alineó con ese 3 %. Para comparar, la tienda de apps de una plataforma de comercio cobra 15 % pasado el primer millón de dólares ([ecosistema de terceros](../../Producto/Plataformas/ecosistema-de-terceros.md#el-reparto-de-ingresos-con-los-desarrolladores)).

La lectura de esta base es que un proveedor de software de gestión puede cobrar poco por la tienda porque gana en otro lado: cada extensión que resuelve un rubro le hace más difícil al cliente irse ([costos de cambio](../../Estrategia-competitiva/Fuentes-de-ventaja/costos-de-cambio.md)) y le vende más licencias o suscripciones del producto base.

## Por qué una extensión de gestión pesa más que una app

Una app de una tienda online que falla muestra mal una página. Una extensión de un software de gestión que falla puede generar asientos mal hechos, stock que no cuadra o comprobantes fiscales con datos errados, porque escribe en el [registro de movimientos](../Columnas-tecnicas/registro-de-movimientos-y-dimensiones.md) que no se edita. Es inferencia de esta base, sin fuente que la mida.

De ahí salen dos consecuencias para quien diseña el producto. Las extensiones tienen que pasar por los mismos documentos, permisos y reglas que el núcleo, no escribir directo en las tablas. Y cada versión nueva del producto tiene que mantener los puntos de extensión, porque romperlos deja a los clientes sin actualizar ([después de la puesta en marcha](../Implementacion/despues-de-la-puesta-en-marcha.md)).

> [!NOTE] Sin fuente todavía: la comisión y los requisitos de certificación de la tienda de otros proveedores de ERP; datos de cuántos ingresos se concentran en pocas extensiones; un caso documentado de un proveedor de ERP que absorbió una extensión de terceros.
