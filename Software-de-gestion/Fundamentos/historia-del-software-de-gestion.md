---
resumen: >-
  El software de gestión empezó en la fábrica con el MRP de los años sesenta, creció al MRP II en los ochenta y pasó a llamarse ERP en los noventa, cuando el término de Gartner lo extendió a toda la empresa; el año 2000 empujó el reemplazo de sistemas viejos, y después llegaron la nube y una serie de etiquetas de analista (ERP II, postmoderno, componible). Casi todo el tramo descansa en fuentes secundarias.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, Material requirements planning (secundaria; cita a Orlicky 1975, Karmarkar 1989 y Gray 1986): https://en.wikipedia.org/wiki/Material_requirements_planning"
  - "Wikipedia, Enterprise resource planning (secundaria; historia, Y2K, ERP II, nube): https://en.wikipedia.org/wiki/Enterprise_resource_planning"
  - "Jacobs y Weston (2007), Enterprise resource planning (ERP): A brief history, Journal of Operations Management 25(2): 357-363 (solo la cita; no leído): https://doi.org/10.1016/j.jom.2006.11.005"
  - "Bond, Genovese, Miklovic, Wood, Zrimsek y Rayner (2000), ERP Is Dead: Long Live ERP II, GartnerGroup (según catálogo y resúmenes): https://bibsonomy.org/bibtex/10a564a8b9b226a7f96ea0e6148f4c3e6/stefan.strecker"
  - "Accountancy Age, Gartner predictions: ERP II is served (2000): https://accountancyage.com/2000/11/19/gartner-predictions-erp-ii-is-served/?amp=1"
  - "Møller (2005), ERP II: a conceptual framework for next-generation enterprise systems?, Journal of Enterprise Information Management (según el buscador): https://dx.doi.org/10.1108/17410390510609626"
  - "Gartner, nota de prensa del 2014-01-29 sobre el ERP postmoderno (título confirmado; la página dio 403): https://www.gartner.com/en/newsroom/press-releases/2014-01-29-gartner-says-by-2016-the-impact-of-cloud-and-emergence-of-postmodern-erp-will-relegate-highly-customized-erp-systems-to-legacy-status"
  - "TechTarget, Postmodern ERP countered by continued appeal of single suite: https://www.techtarget.com/enterprise-software/feature/Postmodern-ERP-countered-by-continued-appeal-of-single-suite"
  - "TechTarget, Composable ERP strategy (según el resumen): https://www.techtarget.com/enterprise-software/feature/Composable-ERP-strategy-Key-benefits-and-steps-for-success"
  - "Gartner, documentos sobre ERP componible (según resúmenes): https://www.gartner.com/en/documents/5494395 y https://www.gartner.com/en/documents/6206787"
  - "Davenport (1998), Putting the Enterprise into the Enterprise System, HBR 76(4): 121-131 (según un resumen): https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm"
  - "Guía de implantación de un proveedor grande, Success by Design (fase Operate): https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/success-by-design"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md, sección 2.1 (2026-11-27)"
aliases: [historia del ERP, ERP history, historia de MRP, MRP II, manufacturing resource planning, ERP II, postmodern ERP, ERP postmoderno, composable ERP, ERP componible, Y2K, problema del año 2000, cloud ERP, ERP en la nube]
creado: 2026-11-27
revisado:
---

# Historia del software de gestión

El software de gestión empezó en la fábrica con el MRP de los años sesenta, creció al MRP II en los ochenta y pasó a llamarse ERP en los noventa, cuando el término de Gartner lo extendió a toda la empresa; el año 2000 empujó el reemplazo de sistemas viejos, y después llegaron la nube y una serie de etiquetas de analista (ERP II, postmoderno, componible). Casi todo el tramo descansa en fuentes secundarias.

La historia escrita desde el campo es Jacobs y Weston (2007), en el *Journal of Operations Management*, y esta base no la leyó: solo vio la cita. Lo que sigue sale de Wikipedia, de catálogos y de la prensa del sector, y cada fila dice de dónde. Sirve para fechar hechos; no alcanza para explicar por qué pasaron.

## Del cálculo de materiales a la fábrica entera

| Momento | Qué pasó | Fuente |
|---|---|---|
| Comienzos de los cincuenta | Dos fabricantes grandes computarizan el cálculo de materiales sin venderlo como producto | Wikipedia, secundaria |
| 1964 | Joseph Orlicky desarrolla el MRP; un fabricante de herramientas aparece como primer usuario | Wikipedia, secundaria |
| 1975 | Unas 700 empresas lo habían implantado; Orlicky publica *Material Requirements Planning* | Wikipedia, secundaria |
| 1981 | Unas 8.000 empresas lo tenían | Wikipedia, secundaria |
| 1983 | Oliver Wight desarrolla el MRP II a partir del MRP | Wikipedia, secundaria |
| Hacia 1989 | Un tercio de la industria del software era MRP II, 1.200 millones de dólares | Wikipedia, secundaria |

Las fechas del MRP no coinciden entre fuentes: otros textos lo ubican a fines de los cincuenta o en los sesenta con otras empresas. Qué calcula un MRP, y el libro de Orlicky con sus ediciones, está en [MRP](../../Produccion/Planificacion-de-la-produccion/mrp.md), del tema Producción. Para este tema importa otra cosa: el primer software de gestión vendido como producto fue un cálculo de planta, y por eso los ERP grandes conservan hasta hoy un corazón de manufactura (lectura de esta base).

## ERP: un término de analista

Según Wikipedia, «Gartner is credited with first using the acronym ERP in the 1990s»; otros textos dicen 1990, y esta base no encontró el documento de Gartner que lo acuñó. El término extendía el MRP y el MRP II a «a larger whole that reflected the evolution of application integration beyond manufacturing». Los primeros paquetes se armaron alrededor de finanzas, mantenimiento y personal, y a mediados de los noventa cubrían todas las funciones centrales.

Davenport (1998), según un resumen, describió el sistema empresarial como una base central que alimenta aplicaciones modulares, y advirtió que imponía su propia lógica a la empresa. Ese artículo abre la discusión sobre adoptar o adaptar que sigue en [fundamentos](fundamentos-de-software-de-gestion.md#cuatro-posiciones-en-disputa).

## El año 2000 como motor de reemplazo

Según Wikipedia, «The year 2000 problem led many companies to replace old systems with ERP». En lectura de esta base, cambiar el sistema viejo por un paquete resolvía la fecha y prometía la integración en el mismo proyecto. Los casos de puesta en marcha que más se citan como fracaso son de esos años, y están en [puesta en marcha](../Implementacion/puesta-en-marcha.md).

## ERP II, postmoderno y componible

Desde el año 2000, Gartner propuso tres etiquetas para lo que venía después del ERP. Las tres se conocen por resúmenes y por la prensa: los documentos originales están detrás de un muro.

| Etiqueta | Año | Qué proponía | Fuente |
|---|---|---|---|
| ERP II | 2000 | «ERP Is Dead: Long Live ERP II» (Bond y otros): aplicaciones por industria que optimizan procesos dentro de la empresa y entre empresas. Daba 80 % de probabilidad de que en 2005 fuera el habilitador principal de esa eficiencia | Catálogo y resúmenes |
| ERP postmoderno | 2013 o 2014 | Reemplazar la suite de un proveedor por un ERP federado y débilmente acoplado, con piezas de dos o más proveedores. Gartner esperaba que pasara de cerca del 15 % de las empresas a más del 40 % hacia 2020 | Prensa del sector, citando a una analista de Gartner |
| ERP componible | Años veinte | Una estrategia que «automates and links administrative and operational business capabilities», con bloques unidos por interfaces | Resúmenes |

La fecha del ERP postmoderno discrepa: el concepto se fecha en 2013 y la nota de prensa que lo hizo conocido es del 29 de enero de 2014. No se encontró si el pronóstico para 2020 se cumplió. Møller (2005) publicó una crítica académica de ERP II que esta base solo vio en un buscador.

Las tres etiquetas repiten el mismo debate: [suite o lo mejor de cada clase](fundamentos-de-software-de-gestion.md#cuatro-posiciones-en-disputa), que Light y otros ya planteaban en 2000. En lectura de esta base, son posiciones de analista sobre cómo armar el software, no cambios medidos en lo que compran las empresas.

## La nube

Según Wikipedia, los primeros productos de gestión que corrían solo en la nube aparecieron en 1999, y la adopción se aceleró a comienzos de los 2010. El CRM hizo el mismo camino en esos años, como cuenta [historia del CRM](../../Relacion-con-clientes/Fundamentos/historia-del-crm.md#qué-cambió-con-la-nube-y-qué-no). Lo que cambió con la nube fue sobre todo cómo se cobra y quién actualiza: la licencia perpetua con mantenimiento dio paso a la suscripción, y la guía de implantación de un proveedor grande presenta la actualización continua de la plataforma como parte del producto. Eso es del [mercado](../Mercado-y-economia/licencia-y-suscripcion.md) y de [después de la puesta en marcha](../Implementacion/despues-de-la-puesta-en-marcha.md).

## Lo que no cambió

Del MRP a la nube cambiaron las etiquetas, el alcance y la forma de cobrar. Las piezas de adentro siguieron siendo las mismas: el maestro de artículos, el documento que pasa por estados, el registro de movimientos que no se edita, el cierre de período. Esa continuidad es lo que este tema llama [columnas técnicas](../Columnas-tecnicas/columnas-tecnicas.md) (lectura de esta base, sin una fuente histórica que la estudie).

> [!NOTE] Sin fuente todavía: Jacobs y Weston (2007) leído entero; el documento de Gartner donde aparece la sigla ERP y su año exacto; el texto de «ERP Is Dead: Long Live ERP II»; una historia del software de gestión para pymes y de su llegada a la Argentina.
