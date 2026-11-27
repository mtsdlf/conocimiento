---
resumen: >-
  La implementación es el proyecto que lleva un software de gestión a una empresa que ya trabaja de otra manera: se elige el producto, se decide qué se adapta, se migran los datos, se pone en marcha y se estabiliza. Es donde se juega casi todo el costo y el riesgo de un sistema, y las cifras de fracaso que circulan dependen de cómo se define fracaso y de quién las mide.
estado: borrador
estabilidad: semi
fuentes:
  - "Markus y Tanis (2000), The enterprise system experience: from adoption to success, en Zmud (ed.), Framing the Domains of IT Research; fases nombradas según una fuente que cita el modelo (no se leyó el capítulo): https://www.cin.ufpe.br/~llfj/Emerald/Critical%20factors%20for%20successful%20implementation%20of%20enterprise%20systems.pdf"
  - "Markus, Axline, Petrie y Tanis (2000), Learning from adopters' experiences with ERP, J. of Information Technology 15(4) (abstract): https://aisel.aisnet.org/jit/vol15/iss4/2"
  - "Guía de implementación de un proveedor grande, Success by Design (leída): https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/success-by-design"
  - "Material de la metodología de implementación de otro proveedor grande (según resumen del buscador): https://learning.sap.com/courses/discovering-sap-activate-implementation-tools-and-methodology/describing-the-methodology-structure"
  - "Somers y Nelson (2001), The impact of critical success factors across the stages of ERP implementations, HICSS-34 (según resumen): https://doi.org/10.1109/HICSS.2001.927129"
  - "Holland y Light (1999), A critical success factors model for ERP implementation, IEEE Software 16(3) (según resumen): https://salford-repository.worktribe.com/output/1448129/a-critical-success-factors-model-for-erp-implementation"
  - "Finney y Corbett (2007), ERP implementation: a compilation and analysis of critical success factors, BPMJ 13(3) (según resumen): https://www.doi.org/10.1108/14637150710752272"
  - "Panorama Consulting Solutions, 2017 Report on ERP Systems & Enterprise Software (leído): https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf"
  - "Panorama Consulting Group, The 2024 ERP Report (texto leído, gráficos no): https://qt9software.com/hubfs/2024-erp-report-panorama-consulting-group.pdf"
  - "The Register, 2025-11-13, sobre una charla de Gartner (leído): https://www.theregister.com/2025/11/13/erp_disaster_gartner/"
  - "Gartner, What IT leaders must do to avoid disappointing ERP initiatives (según resumen; la página dio 403): https://www.gartner.com/en/information-technology/insights/what-it-leaders-must-do-to-avoid-disappointing-erp-initiatives"
  - "Flyvbjerg y Budzier (2011), Why Your IT Project May Be Riskier Than You Think, HBR 89(9) (abstract): https://arxiv.org/abs/1304.0265"
  - "Eveleens y Verhoef (2010), The rise and fall of the Chaos report figures, IEEE Software 27(1) (abstract): https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/"
  - "Hitt, Wu y Zhou (2002), Investment in Enterprise Resource Planning, JMIS 19(1), nota 4 (leído): https://www.scheller.gatech.edu/directory/research/information-technology-management/wu/pdf/hitt_wu_zhou_jmis_2002.pdf"
  - "Software-de-gestion/.investigacion/implementacion.md"
  - "Software-de-gestion/.investigacion/contraria.md"
aliases: [implementación, implantación, implementación de ERP, ERP implementation, enterprise system implementation, proyecto de ERP, ciclo de implantación, enterprise system experience cycle, factores críticos de éxito, critical success factors, CSF]
creado: 2026-11-27
revisado:
---

# Implementación

La implementación es el proyecto que lleva un software de gestión a una empresa que ya trabaja de otra manera: se elige el producto, se decide qué se adapta, se migran los datos, se pone en marcha y se estabiliza. Es donde se juega casi todo el costo y el riesgo de un sistema, y las cifras de fracaso que circulan dependen de cómo se define fracaso y de quién las mide.

El campo dice implementación o implantación; las dos palabras nombran lo mismo. Esta vertical recibe un producto de [Categorías de producto](../Categorias-de-producto/categorias-de-producto.md) y lo choca con los procesos de la empresa, que viven en [Procesos de negocio](../../Procesos-de-negocio/procesos-de-negocio.md). Las [columnas técnicas](../Columnas-tecnicas/columnas-tecnicas.md) ponen el límite a lo que se puede adaptar sin romper el producto, y [Mercado y economía](../Mercado-y-economia/mercado-y-economia.md) decide quién implanta y cuánto se paga. Cómo se lleva un proyecto en general (alcance, riesgo, etapas) es de [Gestión de proyectos](../../Gestion-de-proyectos/gestion-de-proyectos.md); acá va lo propio de implantar un sistema.

## Las cuatro fases de Markus y Tanis

El marco académico de referencia es el de Markus y Tanis (2000), que parte la experiencia de una empresa con un sistema en cuatro fases. Los nombres vienen de una fuente que cita el modelo; el capítulo original no se leyó.

| Fase | Nombre en el modelo | Qué pasa | Nota de esta vertical |
|---|---|---|---|
| 1 | Chartering | El caso de negocio y las decisiones de solución: se elige el producto y quién lo implanta | [elegir un sistema](elegir-un-sistema.md), [partners de implementación](partners-de-implementacion.md) |
| 2 | Project | Se configura, se adapta, se migran los datos y se pone en marcha | [análisis de brechas](analisis-de-brechas.md), [migración de datos](migracion-de-datos.md), [puesta en marcha](puesta-en-marcha.md) |
| 3 | Shakedown | La estabilización: de la puesta en marcha a la operación normal | [después de la puesta en marcha](despues-de-la-puesta-en-marcha.md) |
| 4 | Onward and upward | La operación y la mejora, hasta la próxima decisión grande | [después de la puesta en marcha](despues-de-la-puesta-en-marcha.md) |

Lo que el modelo agrega a un plan de proyecto común es que la elección del sistema ya es parte del ciclo, y que el proyecto no termina el día de la puesta en marcha. Markus, Axline, Petrie y Tanis (2000), en un estudio que según su abstract patrocinó un proveedor de ERP, sostienen que el éxito depende de cuándo se mide: el de una fase se relaciona poco con el de la siguiente. Encontraron problemas en todas las fases, y muchos de los tardíos habían empezado temprano sin que nadie los notara.

Las metodologías públicas de los proveedores cortan parecido. La guía de un proveedor grande propone cinco fases que llama «methodology-agnostic» (descubrir, iniciar, implementar, preparar y operar), y la de otro, según un resumen, seis, con talleres de ajuste al estándar en la fase de exploración. La primera guía aclara que su marco «doesn't guarantee implementation outcomes».

## Quién participa

En una implantación trabajan tres partes con intereses distintos. La empresa pone a la dirección que patrocina, a los usuarios clave que conocen cada proceso y al equipo que va a operar el sistema. El proveedor del software pone el producto y su metodología. Un partner o integrador, o la propia empresa, hace el trabajo de configurar, migrar y capacitar; quién lo hace y con qué contrato está en [partners de implementación](partners-de-implementacion.md). La guía leída de un proveedor se dirige a esas tres partes: «system integrators, independent software development companies, and customers».

Cómo se identifica a los que ganan, pierden o pueden frenar el proyecto es de [interesados](../../Gestion-de-proyectos/Encuadre/interesados.md). Llevar a la gente de la forma de trabajar vieja a la nueva es [gestión del cambio](../../Liderazgo-y-direccion/Ejecucion/gestion-del-cambio.md), un campo cuyos modelos completos no se pusieron a prueba.

## Factores críticos de éxito

La literatura de implantación produjo listas de factores críticos de éxito. Holland y Light (1999) separan, según un resumen, factores estratégicos (visión de negocio, apoyo de la dirección, plan y cronograma) y tácticos (configuración técnica, gestión del proyecto). Somers y Nelson (2001), con 86 organizaciones, ordenan 22 factores según la etapa en que pesan; la lista no se leyó.

Las listas salen de encuestas y casos, y no prueban causa. Finney y Corbett (2007) revisaron 45 artículos y señalan, según un resumen, que contar cuántas veces aparece un factor duplica recuentos. En lectura de esta base, sirven como lista de control y no como receta.

## Cuánto fallan, según quién lo mide

Las cifras de fracaso de ERP que circulan cambian según la definición, la muestra y el interés de quien las publica. Ninguna fuente leída mide el fracaso de ERP con una muestra representativa.

| Quién | Qué dice | Método | Interés |
|---|---|---|---|
| Gartner (2025) | «70 % of ERP initiatives fail to fully meet their original business use case goals» y 25 % «fail catastrophically» | No publicado: la nota de prensa que lo cuenta aclara que no explica cómo se llegó a los porcentajes. Es un pronóstico, no una medición | Analista que vende asesoramiento a quien compra |
| Panorama Consulting (2017) | 74 % con sobrecosto, 59 % con atraso, duración media de 16,9 meses, 56 % con una interrupción operativa material en la puesta en marcha | Encuesta en su sitio web de marzo de 2016 a febrero de 2017, 342 respuestas, muestra autoseleccionada | Consultora que vende selección, gestión de la implantación y gestión del cambio |
| Panorama Consulting (2024) | «More than half of organizations in our study stayed within their expected budget», con un costo mediano de USD 450.000 | Encuesta de agosto de 2022 a diciembre de 2023, 131 respuestas | La misma |
| Flyvbjerg y Budzier (2011) | Sobre 1.471 proyectos de TI, sobrecosto promedio de 27 %, y uno de cada seis con un sobrecosto promedio de 200 % | Base de proyectos con costo estimado y real; proyectos de TI en general, no de ERP | Académico |

Las dos ediciones de Panorama no muestran una tendencia: la propia consultora atribuye la caída del costo medio de 2017 a una muestra de empresas más chicas. Lo que las fuentes con método sostienen es que el riesgo de un proyecto de TI está en la cola, no en el promedio, como desarrolla [por qué fallan los proyectos](../../Gestion-de-proyectos/Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md#la-cola-gruesa-en-proyectos-de-tecnología). El informe CHAOS de Standish, de donde salen muchas cifras de «fracaso del software», trata proyectos de software en general, y Eveleens y Verhoef (2010) mostraron que sus definiciones no reflejan proyectos reales ([el informe CHAOS](../../Gestion-de-proyectos/Fundamentos/mitos-de-gestion-de-proyectos.md#el-informe-chaos)).

La frase «el 70 % de los ERP fracasa» y de dónde sale están en [mitos del software de gestión](../Fundamentos/mitos-del-software-de-gestion.md). La cifra es vieja: Hitt, Wu y Zhou (2002) ya escribían que «at least 90 percent of ERP implementations end up late or over budget», citando a la prensa.

## Dónde falla una implantación

Las fuentes leídas ubican la falla en cuatro lugares, que corresponden a las notas de esta vertical. La primera causa de atraso en la encuesta de Panorama de 2017 fue el alcance que se amplió (19 %) y la segunda, los problemas de datos (16 %).

- **Elegir con la demo del vendedor** y no con los casos propios ([elegir un sistema](elegir-un-sistema.md)).
- **Adaptar de más o de menos**: personalizar para copiar el proceso viejo, o forzar un proceso que el negocio necesita distinto ([análisis de brechas](analisis-de-brechas.md)).
- **Migrar sin ensayar ni conciliar** ([migración de datos](migracion-de-datos.md)).
- **Cortar sin plan de vuelta atrás** o en temporada alta ([puesta en marcha](puesta-en-marcha.md)).

## Qué hay adentro de Implementación

- [Elegir un sistema](elegir-un-sistema.md) — el método general para elegir sin quedar atado a la demo: necesidades, criterios, lista corta, demo guionada, referencias y contrato.
- [Análisis de brechas](analisis-de-brechas.md) — comparar lo que trae el producto con lo que la empresa necesita y decidir, brecha por brecha, si se adapta el proceso o el software.
- [Migración de datos](migracion-de-datos.md) — qué se pasa del sistema viejo (maestros, saldos, documentos abiertos, historia), cómo se limpia y cómo se comprueba que llegó bien.
- [Puesta en marcha](puesta-en-marcha.md) — de una vez, por fases o en paralelo; el corte, su ensayo y el hipercuidado.
- [Partners de implementación](partners-de-implementacion.md) — quién implanta (el proveedor, un partner o la propia empresa), con qué contrato y qué conocimiento queda.
- [Después de la puesta en marcha](despues-de-la-puesta-en-marcha.md) — la estabilización, el bache de desempeño, el soporte y las actualizaciones.
