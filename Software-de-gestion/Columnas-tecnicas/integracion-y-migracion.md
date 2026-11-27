---
resumen: >-
  Integrar un software de gestión es decidir cómo entra y sale cada dato (hacia la tienda, el banco, el fisco, la planta o el sistema anterior) y, antes que eso, qué sistema manda en cada dato. La carga inicial de maestros y saldos al arrancar es el mismo mecanismo usado una sola vez.
estado: vigente
estabilidad: estable
fuentes:
  - "Hohpe y Woolf, Enterprise Integration Patterns, cap. 2 Integration Styles: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html"
  - "Martin Fowler, Integration Database (2004): https://martinfowler.com/bliki/IntegrationDatabase.html"
  - "Texto de un proveedor, What is a system of record?: https://www.ibm.com/think/topics/system-of-record"
  - "Davenport (1998), Putting the Enterprise into the Enterprise System, HBR 76(4) (según resumen de terceros): https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm"
  - "Leyh (2012), Tailoring of ERP Systems, cap. 6 de Readings on Enterprise Resource Planning: https://web.eng.fiu.edu/chen/Summer%202012/EGN%205621%20Enterprise%20Systems%20Collaboration/Reading%20ERP/Readings_on_ERP_chapter06.pdf"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md y columnas-tecnicas-complemento.md (2026-11-27)"
aliases: [integración, integration, interfaces, sistema que manda, sistema de registro, system of record, SOR, fuente de verdad, source of truth, estilos de integración, integration styles, base de integración, integration database, carga inicial, carga de apertura, migración]
creado: 2026-11-27
revisado: 2026-11-27
---

# Integración y migración

Integrar un software de gestión es decidir cómo entra y sale cada dato (hacia la tienda, el banco, el fisco, la planta o el sistema anterior) y, antes que eso, qué sistema manda en cada dato. La carga inicial de maestros y saldos al arrancar es el mismo mecanismo usado una sola vez.

Un software de gestión casi nunca está solo. Según el resumen de Davenport (1998), el sistema integrado vino a reemplazar aplicaciones que no se hablaban; en la práctica sigue conviviendo con una tienda online, el banco, el fisco, un sistema de planta o el sistema que reemplaza. Los patrones que resuelven la mecánica (el outbox, la clave de idempotencia, la saga) están en Arquitectura y se enlazan abajo. Acá va lo que es propio del software de gestión.

## Qué sistema manda en cada dato

La pregunta de fondo de toda integración es cuál de los dos sistemas tiene razón cuando dicen cosas distintas. El término que se usa es sistema de registro (*system of record*): un texto de un proveedor lo define como «an authoritative source of business data», y pone al ERP entre los ejemplos junto al CRM, el HCM y el MES. Las definiciones varían entre autores, y la de DAMA no se leyó.

En esta base, **el sistema que manda** en un dato es el único donde ese dato se cambia; los demás lo reflejan. La decisión se toma por dato y no por sistema, como dice [datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md#quién-manda-en-cada-dato): el precio puede mandar desde el sistema de gestión y el email del cliente desde la tienda. Una empresa que no lo decide termina con dos sistemas que pisan el mismo dato y una diferencia que nadie sabe de dónde salió.

Dos casos de dominio:

- La tienda y el marketplace. Productos, precios y stock van del sistema de gestión a los canales; los pedidos, de los canales al sistema. El caso entero, con sus fallas, está en [integración con tiendas y marketplaces](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/integracion-con-tiendas-y-marketplaces.md).
- El banco. El extracto llega del banco, que manda en lo que se acreditó; el sistema de gestión manda en qué factura cancela cada cobro. Juntar las dos cosas es la [aplicación de cobros](../../Tesoreria/Credito-y-cobranzas/aplicacion-de-cobros.md), y comprobar que coinciden, la [conciliación](../../Contabilidad/Control-interno/conciliaciones.md).

La conexión con el fisco para emitir comprobantes es un caso aparte, porque el fisco no refleja el dato sino que lo autoriza (lectura de esta base). Lo que exige la norma argentina a un sistema para eso está en [software de gestión en la Argentina](../software-de-gestion-en-argentina.md).

## Los cuatro estilos de Hohpe y Woolf

Hohpe y Woolf reconocen cuatro estilos para que dos aplicaciones compartan datos:

| Estilo | Su definición | En un software de gestión (ejemplo de esta base) |
|---|---|---|
| Transferencia de archivos | «Have each application produce files of shared data for others to consume» | el extracto bancario, el archivo de un régimen de información |
| Base compartida | «Have the applications store the data they wish to share in a common database» | los módulos de un mismo ERP sobre una sola base |
| Invocación remota | «Have each application expose some of its procedures so that they can be invoked remotely» | consultar el stock de la tienda o pedir una autorización por API |
| Mensajería | «Have each application connect to a common messaging system» | avisar a otros sistemas que se confirmó un pedido |

Para elegir, los autores miran tres cosas: el acoplamiento («Tightly coupled applications make numerous assumptions about how the other applications work»), la frescura del dato, porque cuanto más tarda en compartirse más se desactualiza, y qué pasa cuando el otro lado no responde. Dicen que la mensajería es «often the best style» en muchos casos, y que cada estilo tiene ventajas y costos.

## Los módulos sobre una misma base

Fowler llama *integration database* a «a database which acts as the data store for multiple applications»: exige un esquema que sirva a todos, los cambios «have to be negotiated» y la base se vuelve un punto de acoplamiento. Su conclusión es que «integration databases should be avoided».

En lectura de esta base, un ERP es una base de integración con un solo dueño. La advertencia de Fowler pesa menos cuando el mismo proveedor controla todos los módulos y su esquema, y por eso la base compartida es lo que hace a un ERP: un pedido confirmado se ve en el depósito al instante, sin interfaz en el medio. Pesa más cuando un tercero lee o escribe directo las tablas del producto: cada versión nueva puede cambiar el esquema y romper esa conexión. Leyh (2012) cuenta el desarrollo de interfaces entre los tipos de adaptación de un ERP, y su costo al actualizar es el de [configurar o personalizar](configurar-o-personalizar.md). El papel del ERP en el centro de las integraciones de una empresa está en [ERP](../Categorias-de-producto/erp.md#el-erp-como-centro-de-las-integraciones).

## La mecánica que vive en Arquitectura

| Problema | Patrón |
|---|---|
| Confirmar el documento y avisar a otro sistema sin perder el aviso | [outbox](../../Arquitectura/Sistemas-distribuidos/outbox.md) |
| El mismo pedido llega dos veces y se crean dos | [clave de idempotencia](../../Arquitectura/Sistemas-distribuidos/clave-de-idempotencia.md) |
| Un paso en otro sistema falla después de confirmar | [saga](../../Arquitectura/Sistemas-distribuidos/saga.md) |
| El otro sistema no responde y las llamadas se acumulan | [circuit breaker](../../Arquitectura/Sistemas-distribuidos/circuit-breaker.md) |
| Ordenar las APIs entre sistemas, procesos y canales | [API-led connectivity](../../Arquitectura/Sistemas-distribuidos/api-led-connectivity.md) |

## La carga inicial

Arrancar un sistema nuevo es una integración que corre una sola vez: el sistema anterior le pasa los datos y deja de mandar. En lectura de esta base, el orden lo da la dependencia entre columnas. Primero los [datos maestros](datos-maestros-y-partes.md), porque todo los referencia. Después los saldos a una fecha de corte, cargados como movimientos de apertura en el [registro de movimientos](registro-de-movimientos-y-dimensiones.md): el stock por artículo y depósito, el saldo de cada cuenta corriente, el balance contable. Al final, los documentos abiertos que siguen vivos, como los pedidos sin entregar.

La fecha de corte es una [fecha de bloqueo](fechas-vigencias-y-cierre.md#la-fecha-de-bloqueo) hacia atrás: nada se registra en el sistema nuevo con fecha anterior a la apertura. Qué se migra y qué se deja, cómo se limpia, cómo se ensaya y cómo se concilia es una actividad del proyecto y está en [migración de datos](../Implementacion/migracion-de-datos.md). Cuando el sistema anterior no se apaga de una vez sino por partes, la convivencia sigue el patrón de [strangler fig](../../Arquitectura/Estilos/strangler-fig.md).

## Cómo falla la integración

- Dos sistemas que mandan. El precio se cambia en la tienda y en el sistema de gestión, y la próxima sincronización pisa uno de los dos.
- Avisos perdidos o repetidos. Una venta que no llega descuadra el stock; una que llega dos veces crea dos pedidos.
- Leer las tablas del producto por afuera. Funciona hasta la próxima versión.
- Saldos iniciales sin conciliar. Si la apertura no cuadra con el último balance del sistema anterior, la diferencia arrastra a todos los períodos que siguen.
