---
resumen: >-
  Después de la puesta en marcha viene la estabilización, en la que según el estudio más grande leído el desempeño cae antes de mejorar, y después la operación con soporte, actualizaciones del producto y mejoras. Los beneficios tardan meses o años, y ese estudio no pudo medir si la caída se recupera.
estado: borrador
estabilidad: semi
fuentes:
  - "Hitt, Wu y Zhou (2002), Investment in Enterprise Resource Planning: Business Impact and Productivity Measures, JMIS 19(1):71-98 (leído): https://www.scheller.gatech.edu/directory/research/information-technology-management/wu/pdf/hitt_wu_zhou_jmis_2002.pdf"
  - "Markus, Axline, Petrie y Tanis (2000), Learning from adopters' experiences with ERP, J. of Information Technology 15(4) (abstract): https://aisel.aisnet.org/jit/vol15/iss4/2"
  - "Nicolaou y Bajor, comparación de adoptantes con controles pareados, Review of Business Information Systems (según resumen): https://www.clutejournals.com/index.php/RBIS/article/view/4504"
  - "Poston y Grabski (2001), Financial impacts of enterprise resource planning implementations, IJAIS 2(4) (según resúmenes): https://doi.org/10.1016/S1467-0895(01)00024-0"
  - "Aral, Brynjolfsson y Wu (2006), Which Came First, IT or Productivity?, ICIS (según resumen): https://aisel.aisnet.org/icis2006/110"
  - "Panorama Consulting Solutions, 2017 Report on ERP Systems & Enterprise Software (leído): https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf"
  - "Guía de implementación de un proveedor grande, Success by Design, fase de operación (leída): https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/success-by-design"
  - "Light (2001), The maintenance implications of the customization of ERP software (abstract): https://salford-repository.worktribe.com/output/1471899/the-maintenance-implications-of-the-customization-of-erp-software"
  - "Software-de-gestion/.investigacion/implementacion.md"
  - "Software-de-gestion/.investigacion/contraria.md"
aliases: [después de la puesta en marcha, post go-live, estabilización, shakedown, bache de desempeño, caída de productividad, soporte, soporte posterior, actualizaciones, upgrades, mejora continua, onward and upward]
creado: 2026-11-27
revisado:
---

# Después de la puesta en marcha

Después de la puesta en marcha viene la estabilización, en la que según el estudio más grande leído el desempeño cae antes de mejorar, y después la operación con soporte, actualizaciones del producto y mejoras. Los beneficios tardan meses o años, y ese estudio no pudo medir si la caída se recupera.

Son las dos últimas fases del ciclo de [implementación](implementacion.md) en el modelo de Markus y Tanis: la estabilización (shakedown), que empieza con la [puesta en marcha](puesta-en-marcha.md) y su hipercuidado, y la operación y mejora (onward and upward), que dura hasta la próxima decisión grande. Markus y otros (2000) sostienen, según su abstract, que el éxito depende de cuándo se mide: el éxito en un momento se relaciona solo débilmente con el éxito en otro.

## El bache de desempeño

Hitt, Wu y Zhou (2002) es el estudio más grande leído por esta base sobre qué le pasa a una empresa después de implantar un ERP. Su abstract lo resume: «Even though there is a slowdown in business performance and productivity shortly after the implementation, financial markets consistently reward the adopters with higher market valuation (as measured by Tobin's q).»

Los números salen de 24.037 observaciones de empresa y año entre 1986 y 1998, de las cuales 4.069 son de unas 350 empresas que implantaron módulos del producto. Encuentran productividad más alta en los adoptantes y un valor de mercado cerca de 13 % mayor. La curva de la implantación es la que da nombre al bache: medida con valor agregado, una ganancia de productividad de 3,6 % durante la implantación seguida de una pérdida de 4,7 % después, con un neto de -1,1 % sin significancia estadística.

El estudio tiene tres límites, y los autores declaran el tercero:

- Un solo producto: todos los adoptantes usan el ERP de un mismo proveedor grande de los años noventa, y los datos salen de la base comercial de ese proveedor. Uno de los autores figura en la biografía del artículo como enlace de la alianza universitaria de ese proveedor.
- Empresas públicas grandes de Estados Unidos: no se traslada sin más a pymes ni a productos actuales.
- Sin seguimiento largo: por falta de datos posteriores, los autores dicen no poder probar si la productividad se recupera, y advierten que el efecto puede ser de selección: empresas buenas que adoptan por otras razones.

Otros estudios, leídos solo por resumen, no coinciden del todo. Nicolaou y Bajor encuentran que los adoptantes rinden mejor en los dos años posteriores que empresas parecidas que no adoptaron. Poston y Grabski (2001) se leen de dos maneras: que los adoptantes no mejoraron, o que no empeoraron mientras los no adoptantes sí. Aral, Brynjolfsson y Wu, con 623 empresas grandes de Estados Unidos y datos de un solo proveedor, hallan que el desempeño se correlaciona con la puesta en marcha y no con la compra, y lo leen como que el uso causa la mejora.

## Cuánto tardan los beneficios

Los beneficios tardan. Hitt, Wu y Zhou citan a terceros: la instalación lleva entre uno y tres años (21 meses de promedio) y los beneficios empiezan a llegar, en promedio, a los 31 meses.

En la encuesta de Panorama Consulting de 2017 (342 respuestas en su sitio, muestra autoseleccionada, consultora con interés comercial), el 78 % obtuvo beneficios, pero el 37 % menos de la mitad de lo esperado; el 48 % los obtuvo dentro de los seis meses de la puesta en marcha. La consultora sugiere apuntar a 18 a 24 meses. Su serie de años anteriores salta de 66 % a 41 % con la mitad o menos de los beneficios; en lectura de esta base, eso indica una muestra que cambia más que una tendencia.

En lectura de esta base, la consecuencia práctica es medir el proyecto en dos momentos: al cerrar la estabilización, contra el plan del proyecto, y al año o dos, contra el caso de negocio que lo justificó.

## La estabilización

En lectura de esta base, la estabilización es el período en que la empresa aprende a operar con el sistema y el sistema se corrige hasta que la operación vuelve a la normalidad. Empieza con el hipercuidado y termina cuando los errores que frenan la operación dejan de aparecer y el cierre de mes sale en el plazo de antes.

En lectura de esta base, en esas semanas aparecen las planillas al lado del sistema: lo que el sistema no hace todavía, o no hace como antes, se resuelve afuera. Cada una es una brecha que el [análisis de brechas](analisis-de-brechas.md) no vio o decidió no cubrir, y conviene registrarla como tal antes de que se vuelva permanente.

## Soporte y actualizaciones

Terminado el proyecto, el sistema pasa a soporte: quién atiende los errores, quién hace los cambios y con qué contrato. Cuando lo implantó un tercero, el paso se arregla en el [traspaso](../../Desarrollo/Encargo/traspaso.md), y el soporte puede seguir como abono ([modelos de contrato y cobro](../../Desarrollo/Encargo/modelos-de-contrato-y-cobro.md)). Los cambios en producción tienen que pasar por los controles que un auditor va a mirar, en [controles sobre los sistemas](../../Contabilidad/Control-interno/controles-sobre-sistemas.md).

El producto sigue cambiando después de la implantación. La guía de un proveedor grande describe la fase de operación como «stabilization and a shift in focus towards functionality and enhancements that are planned for the next phase», y, según la misma guía, la actualización continua de la plataforma es parte de su producto en la nube. Es una afirmación del proveedor. En lectura de esta base, una empresa con un producto instalado decide cuándo actualizar, y una en la nube, en general, no.

Cada actualización vuelve a poner sobre la mesa las personalizaciones. Light (2001) sostiene, según su abstract, que cada personalización se evalúa por su efecto en el mantenimiento futuro; el mecanismo, y por qué una modificación al producto cuesta más al actualizar que una extensión aparte, es de [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md). Cómo se actualiza sin romper, y por qué saltear actualizaciones agranda la siguiente, está en [migraciones y actualizaciones](../../Desarrollo/Evolucion/migraciones-y-actualizaciones.md).

## Cuando el sistema implantado se vuelve heredado

Un sistema muy personalizado, sin pruebas y que nadie de la empresa entiende se vuelve un [sistema heredado](../../Desarrollo/Evolucion/sistema-heredado.md): código que hay que cambiar sin saber si el cambio lo rompe. En lectura de esta base, es el destino de las implantaciones que copiaron el sistema viejo con personalizaciones y perdieron al partner que las escribió. Desde ahí, la salida es otra elección y otra implantación, con los [costos de cambio](../../Estrategia-competitiva/Fuentes-de-ventaja/costos-de-cambio.md) que eso arrastra, o reemplazar el sistema de a partes, como propone [strangler fig](../../Arquitectura/Estilos/strangler-fig.md).
