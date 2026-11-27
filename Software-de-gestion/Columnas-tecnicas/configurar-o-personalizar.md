---
resumen: >-
  Un software de gestión se adapta a una empresa de tres maneras: configurándolo con datos (tipos, reglas, parámetros), extendiéndolo con código por puntos que el producto prevé, o modificando su código. Cuanto más adentro del producto se toca, más cuesta cada actualización.
estado: borrador
estabilidad: semi
fuentes:
  - "Martin Fowler, Organization Structures, borrador del segundo volumen de Analysis Patterns (Knowledge Level): https://martinfowler.com/apsupp/accountability.pdf"
  - "Leyh (2012), Tailoring of ERP Systems, cap. 6 de Readings on Enterprise Resource Planning (secundaria; reproduce el esquema de Brehm, Heinzl y Markus): https://web.eng.fiu.edu/chen/Summer%202012/EGN%205621%20Enterprise%20Systems%20Collaboration/Reading%20ERP/Readings_on_ERP_chapter06.pdf"
  - "Brehm, Heinzl y Markus (2001), Tailoring ERP systems: a spectrum of choices and their implications, HICSS-34 (no leído): https://doi.org/10.1109/HICSS.2001.927130"
  - "The Evolution of Original ERP Customization, revisión sistemática, ICEIS 2024: https://scitepress.org/publishedPapers/2024/123055/pdf/index.html"
  - "Dittrich y Vaucouleur (2008), Customization and Upgrade of ERP Systems: An Empirical Perspective, ITU TR-2008-105: https://en.itu.dk/-/media/EN/Research/About-ITU-Research/Technical-Reports/2008/ITU-TR-2008-105-pdf.pdf"
  - "Gool y Seymour (2018), Managing ERP System Customisation Post-Implementation: The Case of an African Petroleum Organisation, ICEIS: https://scitepress.org/Papers/2018/66764/pdf/index.html"
  - "Documentación de un ERP de un proveedor grande, Extensibility home page: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/extensibility/extensibility-home-page"
  - "Documentación de un ERP de código abierto, Customize Form: https://docs.frappe.io/erpnext/user/manual/en/customize-form"
  - "Light (2001), The maintenance implications of the customization of ERP software, J. of Software Maintenance and Evolution 13(6) (abstract): https://salford-repository.worktribe.com/output/1471899/the-maintenance-implications-of-the-customization-of-erp-software"
  - "Hong, Siau y Kim (2016), The impact of ISP, BPR, and customization on ERP performance in manufacturing SMEs of Korea (según resumen): https://doi.org/10.1108/apjie-12-2016-008"
  - "Davenport (1998), Putting the Enterprise into the Enterprise System, HBR 76(4) (según resumen de terceros): https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md, columnas-tecnicas-complemento.md y contraria.md (2026-11-27)"
aliases: [configurar, configuración, configuration, personalizar, personalización, customization, customisation, tailoring, adaptación, extensión, extensibility, user exit, modificación del código, overlayering, nivel de conocimiento, knowledge level, costo de actualizar, upgrade]
creado: 2026-11-27
revisado:
---

# Configurar o personalizar

Un software de gestión se adapta a una empresa de tres maneras: configurándolo con datos (tipos, reglas, parámetros), extendiéndolo con código por puntos que el producto prevé, o modificando su código. Cuanto más adentro del producto se toca, más cuesta cada actualización.

Esta nota trata el mecanismo: qué permite configurar sin programar, qué tipos de adaptación hay y qué se rompe en cada uno al actualizar. La decisión en un proyecto, si conviene cambiar el proceso de la empresa o cambiar el software, es del [análisis de brechas](../Implementacion/analisis-de-brechas.md).

## El nivel de conocimiento: comportamiento guardado como datos

Fowler llama *Knowledge Level* a un conjunto de objetos cuyas instancias gobiernan el comportamiento de los objetos operativos. Cambiar esas instancias cambia el sistema «without programming», y lo resume así: «This choosing and wiring together of objects is how the system is configured». Es el fundamento de diseño de la configuración.

Un software de gestión configurable guarda como datos lo que otro tendría escrito en el código (ejemplos de esta base):

- Los tipos de documento, sus series de numeración y sus estados ([documento y estados](documento-y-estados.md)).
- Las reglas de contabilización que dicen qué asiento deja cada documento ([registro de movimientos y dimensiones](registro-de-movimientos-y-dimensiones.md)).
- Las reglas de una lista de precios, por período y cantidad ([precio y descuentos](../../Relacion-con-clientes/Presupuesto/precio-y-descuentos.md)).
- Los [conceptos de liquidación](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/conceptos-de-liquidacion.md) de la nómina, cada uno con su regla, su base y su orden.
- Los umbrales de aprobación y las incompatibilidades entre roles ([permisos y separación de funciones](permisos-y-separacion-de-funciones.md)).

Cuanto más de esto es dato, más empresas distintas sirve el mismo código. El costo aparece del otro lado. Leyh (2012) escribe que en los productos grandes las tablas de configuración son tantas que «it is almost impossible for "normal" employees ... to get an overview of all configuration parameters and their interdependencies». Agrega que las opciones varían mucho entre productos y que algunos sistemas chicos casi no traen configuración.

## De configurar a modificar el código

Brehm, Heinzl y Markus (2001) propusieron una tipología de las formas de adaptar un ERP, de la menos a la más invasiva. El texto original no está abierto, y las fuentes secundarias que lo resumen no coinciden en cuántos tipos son: una revisión de 2024 dice siete, otros resúmenes dicen ocho o nueve. Leyh (2012) reproduce el esquema con nueve tipos agrupados en dos bloques, y lo que es de Leyh y lo que es de Brehm no se puede separar sin el original:

| Bloque | Tipos, de menos a más invasivo (Leyh 2012) |
|---|---|
| Modificación, sin tocar el código fuente | configuración, ajuste de pantallas, ajuste de reportes, complementos de terceros (*bolt-ons*), programación de flujos de trabajo |
| Desarrollo | desarrollo de interfaces, programación en el lenguaje del producto, puntos de extensión que da el proveedor (*user exits*), modificación del código del paquete |

En este tema se usan tres palabras: **configurar** es cambiar datos del nivel de conocimiento; **extender** es agregar código propio por un punto que el producto prevé; **modificar** es cambiar el código del producto.

## Qué se rompe al actualizar

Leyh explica el costo por tipo. Un punto de extensión lo define el proveedor y «is usually not removed in later versions or releases», por eso no amenaza seriamente el mantenimiento. Modificar el código del paquete es «the most dangerous form of adjustment»: es caro de mantener porque los cambios pueden quedar rotos o pisados por la versión nueva, y algunos proveedores lo prohíben o retiran el soporte.

Dittrich y Vaucouleur (2008) lo estudiaron con entrevistas a tres consultores y una encuesta con 42 respuestas, con un proveedor de ERP como socio. La estrategia más común al actualizar es «go standard»: repasar con el cliente cada personalización y decidir si se mantiene, y «one strategy for upgrading customizations in many cases is to get rid of them». Lo más difícil es la personalización sin documentar y la escrita «directly into the standard functionality instead of developing an independent object». Si cambia el modelo de datos del que depende una función a medida, hay que rediseñarla entera.

Un caso de 2018, una petrolera africana, llega a lo mismo. Gool y Seymour concluyen que «ERP modifications need to be reapplied and tested with each upgrade», y la empresa tuvo que reducir sus objetos a medida antes de la siguiente actualización.

Los productos empujan en esa dirección. La documentación de un ERP de un proveedor grande cuenta que reemplazó la modificación por capas con extensiones, porque las actualizaciones frecuentes piden «a less intrusive customization model», y hoy dice «Overlayering isn't supported». Un ERP de código abierto permite agregar campos y propiedades desde una pantalla, sin tocar el tipo de documento base, con un botón para deshacer todas las personalizaciones.

> [!NOTE]
> Sin fuente todavía: una medición independiente de cuánto encarece cada actualización una personalización. Las cifras que circulan (un porcentaje del costo de la implantación por cada actualización) salen de consultoras y vendedores, sin estudio primario leído, y no se usan.

## Lo que no se sabe sobre personalizar

> [!IMPORTANT]
> **«No personalizar» no tiene la evidencia que parece.** Según el resumen de Davenport (1998), el sistema impone su lógica a la empresa y la complejidad vuelve impracticables las modificaciones grandes. Light (2001), por su abstract, no concluye «nunca», sino que cada personalización se evalúe por su efecto en el mantenimiento. Según un resumen, Hong, Siau y Kim (2016), con 96 pymes manufactureras de Corea, no encontraron efecto del nivel de personalización sobre el desempeño del ERP. Las muestras son chicas, de un país, y autoinformadas. Cómo se usa esto para decidir está en [análisis de brechas](../Implementacion/analisis-de-brechas.md).

## Cómo falla

- **Configuración que nadie entiende.** Un parámetro cambiado hace años explica un comportamiento que nadie recuerda. La [auditoría de cambios](auditoria-de-cambios.md) tiene que cubrir la configuración, no solo los datos.
- **Extender por donde no hay punto de extensión.** Leer o escribir tablas del producto por afuera es una modificación disfrazada ([integración y migración](integracion-y-migracion.md)).
- **Personalizaciones sin dueño.** La que escribió otra consultora y nadie documentó es, según Dittrich y Vaucouleur, la más crítica al actualizar.

En un software vendido como servicio, todos los clientes corren la misma versión, y la configuración por cliente es la única adaptación que no frena la actualización de los demás (lectura de esta base sobre [multi-tenancy](../../Arquitectura/Sistemas-distribuidos/multi-tenancy.md)).
