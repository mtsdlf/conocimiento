---
resumen: >-
  El análisis de brechas compara lo que trae un software de gestión con lo que la empresa necesita y, para cada diferencia, decide si cambia el proceso de la empresa o cambia el software. La literatura llama desajustes a esas diferencias, y la evidencia sobre cuál de los dos caminos conviene es mixta.
estado: borrador
estabilidad: semi
fuentes:
  - "Soh, Sia y Tay-Yap (2000), Cultural fits and misfits: is ERP a universal solution?, CACM 43(4):47-51 (según resumen; la página dio 403): https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits"
  - "Brehm, Heinzl y Markus (2001), Tailoring ERP systems: a spectrum of choices and their implications, HICSS-34 (según resumen): https://doi.org/10.1109/HICSS.2001.927130"
  - "Davenport (1998), Putting the enterprise into the enterprise system, HBR 76(4):121-131 (según resumen de terceros): https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm"
  - "Gattiker y Goodhue (2005), MIS Quarterly 29(3):559-585, con su fe de erratas (según resumen): https://aisel.aisnet.org/misq/vol29/iss3/9/"
  - "Wagner y Newell (2004), 'Best' for whom?, J. of Strategic Information Systems 13(4) (abstract): https://sro.sussex.ac.uk/id/eprint/51660/"
  - "Light (2001), The maintenance implications of the customization of ERP software, J. of Software Maintenance and Evolution 13(6) (abstract): https://salford-repository.worktribe.com/output/1471899/the-maintenance-implications-of-the-customization-of-erp-software"
  - "Hong, Siau y Kim (2016), The impact of ISP, BPR, and customization on ERP performance in manufacturing SMEs of Korea (según resumen): https://doi.org/10.1108/apjie-12-2016-008"
  - "The Register, 2025-11-13, sobre una charla de Gartner (leído): https://www.theregister.com/2025/11/13/erp_disaster_gartner/"
  - "Panorama Consulting Solutions, 2017 Report on ERP Systems & Enterprise Software (leído): https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf"
  - "Material de la metodología de implementación de un proveedor grande, talleres de ajuste al estándar (según resumen): https://learning.sap.com/courses/discovering-sap-activate-implementation-tools-and-methodology/describing-the-methodology-structure"
  - "Software-de-gestion/.investigacion/implementacion.md"
  - "Software-de-gestion/.investigacion/contraria.md"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md"
aliases: [análisis de brechas, fit-gap, fit-gap analysis, gap analysis, ajuste al estándar, fit-to-standard, desajuste, misfit, misfits, adaptar el proceso o el software, mejores prácticas, best practices, vainilla, vanilla]
creado: 2026-11-27
revisado:
---

# Análisis de brechas

El análisis de brechas compara lo que trae un software de gestión con lo que la empresa necesita y, para cada diferencia, decide si cambia el proceso de la empresa o cambia el software. La literatura llama desajustes a esas diferencias, y la evidencia sobre cuál de los dos caminos conviene es mixta.

Es la decisión central de la fase de proyecto de la [implementación](implementacion.md). Arranca con lo que quedó a la vista en la demo guionada al [elegir un sistema](elegir-un-sistema.md) y termina en una lista de brechas, cada una con su resolución. Cómo se cambia el software una vez decidido (configurar con datos, extender con código aparte o modificar el producto) y lo que cuesta cada mecanismo al actualizar es de [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md). Esta nota trata la decisión anterior: si conviene cambiar el software o el proceso.

## Ajuste, brecha y desajuste

Una brecha es una necesidad de la empresa que el producto, tal como viene, no cubre. Se encuentra recorriendo los procesos de la empresa en el producto: un pedido, una devolución, un cierre de mes, como en los recorridos de [Procesos de negocio](../../Procesos-de-negocio/procesos-de-negocio.md). La metodología de un proveedor grande lo hace, según un resumen, en talleres de «ajuste al estándar» (fit-to-standard). En lectura de esta base, eso significa partir del proceso que trae el producto y discutir solo lo que no encaja, en lugar de escribir primero el proceso ideal y buscar el producto que lo copie.

Soh, Sia y Tay-Yap (2000) llamaron desajustes (misfits) a esas brechas y las clasificaron en tres tipos, según los resúmenes leídos. Su estudio es un solo caso, un hospital de Singapur, presentado como resultados tempranos de un trabajo mayor.

| Desajuste | Qué no encaja | Ejemplo |
|---|---|---|
| De datos | El formato o las relaciones del modelo de datos | El producto guarda un solo domicilio por cliente y la empresa entrega en varios |
| Funcional | Lo que se puede hacer: el acceso, los controles, el proceso | El producto pide aprobar todo pedido y la empresa aprueba solo los de cliente nuevo |
| De salida | El formato y el contenido de los reportes y documentos | La factura o el listado no sale como lo pide el cliente o el fisco |

Los ejemplos son de esta base. Según los resúmenes, los desajustes de salida fueron los más frecuentes, y hubo menos en contabilidad y finanzas, donde las normas dan algo de estandarización. Según los extractos, los de datos obligan a reestructurar tablas, un cambio costoso en el núcleo del paquete.

## Adaptar el proceso o el software

Cada brecha tiene tres salidas: se cambia el proceso de la empresa para que siga al producto, se adapta el producto, o se deja afuera y se resuelve con otra herramienta. Brehm, Heinzl y Markus (2001) llaman tailoring a las adaptaciones del software, desde configurar hasta modificar el producto, y las clasifican por la capa que tocan. Según los resúmenes, entre ellas figuran los informes ampliados, la programación de flujos y las interfaces; los resúmenes difieren en el número de tipos (siete, ocho o nueve), y no se leyó el original.

Davenport (1998) defiende que la empresa adapte sus procesos al sistema. Según un resumen de terceros, sostiene que «an enterprise system, by its very nature, imposes its own logic on a company's strategy, organization, and culture» (cita tomada del resumen, sin verificar en el original), y que la mayoría de las empresas tendrán que adaptar sus procesos. Según el mismo resumen, advierte que el sistema empuja hacia procesos genéricos aunque los propios sean una ventaja frente a la competencia.

La crítica a las «mejores prácticas» que trae el producto va por dos lados. Según un resumen, Soh y otros señalan que esas prácticas se formaron en otras condiciones culturales, económicas y normativas. Wagner y Newell (2004), en un solo caso, el de un paquete para universidades, muestran según su abstract una brecha entre la práctica que el paquete declara y la que usan quienes lo instalan.

## Lo que dice la evidencia

La evidencia sobre si conviene adaptar poco o mucho es escasa y de baja calidad. Ningún estudio fuerte prueba ni refuta la regla de no tocar el producto («vainilla»).

- Light (2001), con dos casos, concluye según su abstract que personalizar puede dar valor, pero que cada personalización se evalúa por su efecto en el mantenimiento futuro. La regla que sale es caso por caso.
- Gattiker y Goodhue (2005), con una encuesta a 111 plantas, encuentran según un resumen que el ERP encaja mejor donde las unidades dependen mucho unas de otras y se diferencian poco. Según su fe de erratas, las hipótesis sobre personalización no se sostuvieron.
- Hong, Siau y Kim (2016), con 96 respuestas de pymes manufactureras de Corea, no encuentran que el nivel de personalización influya en el desempeño del ERP, según un resumen. Es una muestra chica, de un país y autoinformada.
- Gartner, en una charla de 2025 que cuenta la prensa, nombra entre las causas de fracaso la personalización atada demasiado a los procesos existentes.
- Panorama Consulting, una consultora con interés comercial, llama «ideal» a personalizar entre 10 y 20 % en su informe de 2017 (encuesta autoseleccionada), sin método publicado.

En lectura de esta base, el criterio defendible es preguntar por cada brecha si el proceso propio es una ventaja frente a la competencia o una costumbre. Una ventaja justifica adaptar el software y pagar su mantenimiento; una costumbre, no.

## Cómo se registra y cómo falla

Cada brecha queda escrita con su resolución, quién la decidió y cuánto cuesta, porque se vuelve a discutir en cada actualización del producto. Una brecha que se resuelve adaptando el software es un cambio de alcance del proyecto y se trata como tal ([cambios de alcance](../../Desarrollo/Encargo/cambios-de-alcance.md)). En lectura de esta base, el análisis falla de tres maneras.

- Copiar el sistema viejo: los usuarios piden que el sistema nuevo haga lo que hacía el viejo, y cada pedido se vuelve una personalización.
- Forzar el estándar donde el negocio es distinto: la empresa pierde lo que la diferenciaba o lo sigue haciendo en una planilla al lado del sistema.
- Descubrir la brecha tarde: una brecha que aparece en las pruebas o en la puesta en marcha ya no se negocia: se paga.
