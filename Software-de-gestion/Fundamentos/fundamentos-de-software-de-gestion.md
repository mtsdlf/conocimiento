---
resumen: >-
  Lo transversal del software de gestión: un nombre sin definición acordada, una historia que va de la planificación de materiales a la empresa entera, cuatro posiciones en disputa (suite o lo mejor de cada clase, adoptar las prácticas del paquete o adaptarlo, partida doble o REA, si un ERP mejora el desempeño) y cómo leer la evidencia de un campo donde casi todas las cifras vienen de quien vende.
estado: borrador
estabilidad: estable
fuentes:
  - "Klaus, Rosemann y Gable (2000), What is ERP?, Information Systems Frontiers 2(2): 141-162 (abstract): https://ideas.repec.org/a/spr/infosf/v2y2000i2d10.1023_a1026543906354.html"
  - "Davenport (1998), Putting the Enterprise into the Enterprise System, HBR 76(4): 121-131 (según un resumen): https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm"
  - "Gartner, glosario Enterprise Resource Planning (según el resumen del buscador; la página dio 403): https://www.gartner.com/en/information-technology/glossary/enterprise-resource-planning-erp"
  - "Light, Holland, Kelly y Willis (2000), Best of Breed IT Strategy: An Alternative to ERP Systems, ECIS 2000 (abstract): https://aisel.aisnet.org/ecis2000/180"
  - "TechTarget, Postmodern ERP countered by continued appeal of single suite: https://www.techtarget.com/enterprise-software/feature/Postmodern-ERP-countered-by-continued-appeal-of-single-suite"
  - "Soh, Sia y Tay-Yap (2000), Cultural fits and misfits: is ERP a universal solution?, CACM 43(4): 47-51 (según resúmenes): https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits"
  - "Wagner y Newell (2004), 'Best' for whom?, Journal of Strategic Information Systems 13(4): 305-328 (abstract): https://sro.sussex.ac.uk/id/eprint/51660/"
  - "The Register, ERP carnage continues as orgs jump in unprepared (2025-11-13): https://www.theregister.com/2025/11/13/erp_disaster_gartner/"
  - "Informe técnico ITU TR-2006-92 sobre REA y ERP (según el resumen del buscador): https://en.itu.dk/-/media/EN/Research/About-ITU-Research/Technical-Reports/2006/ITU-TR-2006-92-pdf.pdf"
  - "Hitt, Wu y Zhou (2002), Investment in Enterprise Resource Planning: Business Impact and Productivity Measures, JMIS 19(1): 71-98: https://www.scheller.gatech.edu/directory/research/information-technology-management/wu/pdf/hitt_wu_zhou_jmis_2002.pdf"
  - "Poston y Grabski (2001), Financial impacts of enterprise resource planning implementations, IJAIS 2(4): 271-294 (según resúmenes de terceros): https://doi.org/10.1016/S1467-0895(01)00024-0"
  - "Aral, Brynjolfsson y Wu (2006), Which Came First, IT or Productivity?, ICIS 2006 (según el resumen): https://aisel.aisnet.org/icis2006/110"
  - "Panorama Consulting, 2017 Report on ERP Systems & Enterprise Software: https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf"
  - "Eveleens y Verhoef (2010), The Rise and Fall of the Chaos Report Figures, IEEE Software 27(1): 30-36 (abstract): https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md y contraria.md (2026-11-27)"
aliases: [fundamentos del software de gestión, fundamentos de ERP, qué es un ERP, definición de ERP, suite o best-of-breed, best of breed, mejores prácticas del ERP, best practices, REA y ERP, ERP y desempeño]
creado: 2026-11-27
revisado:
---

# Fundamentos de software de gestión

Lo transversal del software de gestión: un nombre sin definición acordada, una historia que va de la planificación de materiales a la empresa entera, cuatro posiciones en disputa (suite o lo mejor de cada clase, adoptar las prácticas del paquete o adaptarlo, partida doble o REA, si un ERP mejora el desempeño) y cómo leer la evidencia de un campo donde casi todas las cifras vienen de quien vende.

Rodea a las cuatro verticales del [software de gestión](../software-de-gestion.md) sin ser una de ellas. Los términos están en el [glosario](glosario-de-software-de-gestion.md) y lo que se repite sin evidencia, en los [mitos](mitos-del-software-de-gestion.md).

## Un nombre que el campo no logró definir

ERP no tiene una definición acordada, y el propio campo lo comprobó. Klaus, Rosemann y Gable (2000) cruzaron la historia, la literatura de sistemas de información y una encuesta a académicos. Según su abstract, concluyeron que «it is unlikely that at this stage a broadly agreed definition of ERP can be achieved».

Las definiciones que circulan coinciden en el núcleo y discrepan en el borde. Davenport (1998), según un resumen, describe una base central que alimenta aplicaciones modulares para casi toda la actividad de la empresa. Gartner, según el resumen de su glosario, dice que el ERP «is neither defined as a single integrated suite, nor is it a specific set of modules». En lectura de esta base, el desacuerdo está en si el CRM o la nómina entran y en si hace falta un solo proveedor.

Por eso este tema trata al ERP como una forma de empaquetar software y clasifica por el dominio que lleva cada [categoría de producto](../Categorias-de-producto/categorias-de-producto.md). El saber de cada dominio está en su tema; acá queda lo que es del software.

## De la planificación de materiales a la empresa entera

El software de gestión nació en la fábrica. El MRP calculaba qué materiales pedir y cuándo, y Oliver Wight lo amplió en MRP II. El ERP, un término de analista de los noventa, lo llevó a finanzas, personal y el resto de la empresa. Después vinieron el problema del año 2000, que según Wikipedia llevó a muchas empresas a reemplazar sus sistemas, la nube y las etiquetas de analista (ERP II, postmoderno, componible). Las fechas y sus fuentes, casi todas secundarias, están en [historia del software de gestión](historia-del-software-de-gestion.md).

## Cuatro posiciones en disputa

> [!IMPORTANT]
> **Suite de un proveedor o lo mejor de cada clase.** Light, Holland, Kelly y Willis (2000), según su abstract, sostienen que los paquetes de un solo proveedor «often fail to fit specific organizational and industry needs» y que combinar piezas de varios ajusta mejor; es un estudio de un caso. Gartner propuso en 2013 o 2014 (las fuentes discrepan) el ERP «postmoderno», federado y con piezas «likely from two or more vendors», pero su analista pedía no personalizar lo común: «finance is finance, and general ledger is general ledger». Un analista de otra firma, citado por la prensa del sector, dijo que las empresas seguían con un solo proveedor y que los pronósticos de Gartner no se cumplían. No se encontró un estudio independiente que mida cuál rinde más. En lectura de esta base, la pregunta de fondo es dónde poner el costo de integrar: lo trata [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md).

> [!IMPORTANT]
> **Adoptar las prácticas del paquete o adaptar el software.** Davenport (1998), según un resumen, sostiene que un sistema empresarial «imposes its own logic on a company's strategy, organization, and culture» y empuja a procesos genéricos aunque los propios den ventaja. Soh, Sia y Tay-Yap (2000) estudiaron un hospital de Singapur y, según resúmenes, clasificaron los desajustes entre el paquete y la organización en de datos, funcionales y de salida. Wagner y Newell (2004), según su abstract, estudiaron un solo caso, un paquete de «mejores prácticas» para una universidad, y señalan una brecha entre la teoría declarada de la solución y la teoría en uso de quienes la instalan. La propia Gartner contó en 2025 entre las causas de fracaso la personalización atada a los procesos existentes (según The Register). La decisión de proyecto está en [análisis de brechas](../Implementacion/analisis-de-brechas.md) y el mecanismo en [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md).

> [!IMPORTANT]
> **Partida doble o REA.** REA, de McCarthy (1982), registra recursos, eventos y agentes y deriva el asiento de ellos; la explicación está en [fundamentos de contabilidad](../../Contabilidad/Fundamentos/fundamentos-de-contabilidad.md#rea-registrar-los-hechos-y-no-los-asientos). Para el software importa su adopción. Un informe técnico de la IT-Universitetet de Copenhague, según su resumen, dice que los ERP no lo adoptaron: siguen usando la partida doble como modelo que alimenta a las otras aplicaciones, y su diseño de datos no tomó la orientación a objetos en la que se apoya REA. Ninguna fuente leída documenta por qué lo decidieron los proveedores. Cómo modela los movimientos un sistema, con las dos lecturas, está en [registro de movimientos y dimensiones](../Columnas-tecnicas/registro-de-movimientos-y-dimensiones.md).

> [!IMPORTANT]
> **Si un ERP mejora el desempeño.** El estudio leído entero es Hitt, Wu y Zhou (2002): con 24.037 observaciones empresa-año de 1986 a 1998, los adoptantes tienen productividad entre 2,3 % y 4,2 % más alta sin controlar por uso de TI, y un valor de mercado cerca de 13 % mayor. También hallan «a slowdown in business performance and productivity shortly after the implementation», y no pueden decir si se recupera. La muestra son empresas públicas grandes, clientes de un solo producto, y los autores admiten que el efecto puede ser selección. Poston y Grabski (2001) tienen dos lecturas en las fuentes secundarias: según una, los adoptantes no mejoraron frente a su situación previa mientras los no adoptantes empeoraron; según otra, no hubo mejora. Aral, Brynjolfsson y Wu (2006), según su resumen, hallan que la compra no se correlaciona con el desempeño y la puesta en marcha sí. Lo que pasa después del arranque está en [después de la puesta en marcha](../Implementacion/despues-de-la-puesta-en-marcha.md).

## Cómo leer la evidencia de este campo

Casi todo lo que se cita sobre software de gestión sale de tres clases de fuente, y cada una tiene su sesgo.

| Fuente | Qué da | Qué cuidar |
|---|---|---|
| Consultoras que venden selección e implantación | Encuestas anuales de costo, plazo y beneficio | Muestra autoseleccionada y conclusiones que recomiendan lo que venden |
| Analistas (Gartner y otros) | Definiciones, categorías de mercado y pronósticos | El texto está tras un muro: se cita por la prensa y no se ve el método |
| Estudios académicos con método | Muestras grandes o casos estudiados a fondo | Son pocos, muchos de los años noventa y dos mil, y varios de un solo producto |

El informe de 2017 de una consultora de selección es un buen ejemplo. Su encuesta estuvo doce meses en el sitio de la consultora y juntó 342 respuestas, sin diseño muestral declarado. Da 74 % de proyectos con sobrecosto en 2016 y 57 % en 2015. En lectura de esta base, ese salto indica una muestra distinta y no una tendencia. La propia consultora vende gestión del cambio y selección, que es lo que sus conclusiones recomiendan.

Antes de repetir una cifra conviene contestar cinco preguntas: quién la dice y qué vende, qué mide (abandono, sobrecosto o «no cumplir del todo los objetivos»), de qué muestra sale, si es una medición o un pronóstico, y si es de ERP o de proyectos de TI en general. El informe CHAOS es un ejemplo de cifra que no pasa esas preguntas. Eveleens y Verhoef (2010) probaron sus definiciones con 5.457 pronósticos de 1.211 proyectos reales y, según su abstract, hallaron que las cifras de Standish no reflejan esos casos. Además, el informe no trata de ERP. El recorrido completo de las cifras de fracaso está en [mitos del software de gestión](mitos-del-software-de-gestion.md).

> [!NOTE] Sin fuente todavía: el texto completo de Davenport (1998), de Klaus, Rosemann y Gable (2000) y de los documentos de Gartner que acuñaron cada etiqueta; un estudio independiente que compare suite y lo mejor de cada clase.

## Lo que hay en Fundamentos

- [Historia del software de gestión](historia-del-software-de-gestion.md): de MRP a MRP II, el ERP como término de Gartner, el año 2000, ERP II, el ERP postmoderno y componible, y la nube. Para fechar y para no atribuir a la nube lo que es más viejo.
- [Glosario de software de gestión](glosario-de-software-de-gestion.md): los términos del tema con su nombre en inglés y la nota donde vive cada uno, agrupados por vertical.
- [Fuentes de software de gestión](fuentes-de-software-de-gestion.md): qué leer para cada vertical, qué parte, en qué fijarse y si esta base lo leyó.
- [Mitos del software de gestión](mitos-del-software-de-gestion.md): el «70 % de los ERP fracasan», el CHAOS, las mejores prácticas, la vainilla, la nube más barata y la pyme que necesita un ERP, con lo que dice la evidencia.
