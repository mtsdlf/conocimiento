---
resumen: >-
  Elegir un sistema de gestión es comparar productos contra las necesidades propias de la empresa, en este orden: necesidades, criterios, lista corta, demo guionada con casos propios, referencias y contrato. El orden es una propuesta de esta base sobre la práctica de consultoras, sin estudios que comparen un método con otro.
estado: borrador
estabilidad: semi
fuentes:
  - "Ratkevičius et al. (2012), ERP selection criteria: theoretical and practical views, Ekonomika (según resumen): https://epublications.vu.lt/object/elaba:4594534/index.html"
  - "SINTEF (2007), A Holistic ERP Selection Methodology (según resumen): https://www.sintef.no/globalassets/project/smartlog/publikasjoner/2007/holistic-erp-selection-methodology.pdf"
  - "Olson, Johansson y Atem de Carvalho, capítulo sobre criterios de selección de ERP (según resumen): https://dx.doi.org/10.1007/978-3-642-28827-2_5"
  - "GFOA, Which System is Truly Best? (según resumen): https://www.gfoa.org/materials/gfr-0826-erp"
  - "Panorama Consulting, ERP software selection in the public sector (según resumen; consultora que vende selección): https://www.panorama-consulting.com/erp-software-selection-in-the-public-sector/"
  - "Panorama Consulting Solutions, 2017 Report on ERP Systems & Enterprise Software (leído): https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf"
  - "Hitt, Wu y Zhou (2002), Investment in Enterprise Resource Planning, JMIS 19(1), costo de instalación citando a terceros (leído): https://www.scheller.gatech.edu/directory/research/information-technology-management/wu/pdf/hitt_wu_zhou_jmis_2002.pdf"
  - "Software-de-gestion/.investigacion/implementacion.md"
aliases: [elegir un ERP, selección de ERP, ERP selection, software selection, selección de software, evaluación de proveedores de software, demo guionada, scripted demo, prueba de concepto, proof of concept, lista corta, shortlist]
creado: 2026-11-27
revisado:
---

# Elegir un sistema

Elegir un sistema de gestión es comparar productos contra las necesidades propias de la empresa, en este orden: necesidades, criterios, lista corta, demo guionada con casos propios, referencias y contrato. El orden es una propuesta de esta base sobre la práctica de consultoras, sin estudios que comparen un método con otro.

Es la primera fase del ciclo de [implementación](implementacion.md): en el modelo de Markus y Tanis, según las fuentes que lo citan, la elección cae dentro de la primera fase, la del caso de negocio, antes del proyecto. Comparte la forma de cualquier compra compleja, que se cuenta en [cotización y licitación](../../Compras-y-abastecimiento/Abastecimiento-estrategico/cotizacion-y-licitacion.md): un pedido de propuesta a varios oferentes, criterios fijados antes de ver las ofertas y un contrato al final. En lectura de esta base, lo propio de un software es que la oferta no se puede inspeccionar como una muestra: el producto se ve funcionando recién cuando ya está implantado.

## Lo que dice la literatura sobre cómo se elige

La literatura académica sobre selección es chica y no da un método probado. Según un resumen, Ratkevičius y otros (2012) encuentran que no hay una clasificación estándar de criterios, y que se suelen partir en criterios del software y criterios de la implantación. Según el mismo resumen, los métodos de decisión se apoyan en programación matemática y teoría de decisión (AHP, ANP, DEA), y otras líneas identifican factores críticos de la evaluación sin dar una guía para hacer el proceso.

El trabajo de SINTEF revisó 16 artículos sobre selección de ERP y, según su resumen, solo cinco proponían un método paso a paso. Lo que sigue es un método general armado por esta base con la práctica de consultoras; ninguna fuente leída lo describe en estos seis pasos.

> [!NOTE] Sin fuente todavía: una guía de un organismo o un estudio con método que describa la demo guionada y la prueba de concepto. El paso sale de práctica de consultoras.

## Del inventario de necesidades al contrato

1. Escribí las necesidades antes de mirar productos. Partí de los recorridos que el sistema tiene que llevar, como [del pedido al cobro](../../Procesos-de-negocio/del-pedido-al-cobro.md) o [de la compra al pago](../../Procesos-de-negocio/de-la-compra-al-pago.md), y de lo que la norma le exige (en la Argentina, [lo que la normativa le pide a un sistema](../software-de-gestion-en-argentina.md)). Marcá qué es obligatorio y qué es deseable.
2. Fijá los criterios y su peso antes de pedir ofertas. Van los del software (qué dominios cubre, cómo se configura, cómo se integra) y los de la implantación (quién la hace, en cuánto tiempo, con qué riesgo). El costo se compara como [costo total para quien compra](../Mercado-y-economia/costo-total-para-quien-compra.md), no como precio de licencia.
3. Armá una lista corta. Un pedido de información sirve para descartar a quien no cubre lo obligatorio; la categoría y el escalón por tamaño ya filtran mucho ([categorías de producto](../Categorias-de-producto/categorias-de-producto.md), [escalones por tamaño](../Categorias-de-producto/escalones-por-tamano.md)).
4. Pedí una demo guionada con tus casos. El oferente recibe por adelantado un guion con documentos reales de la empresa (un pedido con descuento por volumen, una devolución parcial, un cierre de mes) y los tiene que correr en el producto. Lo que el guion no pide, el vendedor lo elige.
5. Hablá con referencias de tamaño y rubro parecidos. Preguntá por la puesta en marcha, el soporte y lo que tuvieron que personalizar, no por el producto en general.
6. Firmá un contrato que diga qué se entrega. El alcance, la aceptación y quién paga el desvío van escritos; cómo se reparte ese riesgo está en [partners de implementación](partners-de-implementacion.md).

En lectura de esta base, la demo guionada es la defensa contra la demo del vendedor, que muestra lo que el producto hace bien con datos armados para eso, y el guion obliga a mostrar la brecha antes de firmar, que es cuando todavía se puede negociar; después pasa a ser un pedido de cambio en el [análisis de brechas](analisis-de-brechas.md).

## Licitar el software y la implantación juntos o por separado

Software e implantación se pueden pedir en una sola oferta o en dos. La GFOA, una organización de responsables de finanzas públicas de Estados Unidos, recomienda, según un resumen, licencias, implantación y soporte en una sola licitación. En lectura de esta base, la razón es que el producto y quien lo implanta fallan juntos: el mejor producto con un implantador que no lo conoce rinde menos que uno peor bien implantado.

Panorama Consulting dice que el sector público suele pedir tres referencias o más, de tamaño y alcance parecidos; es una consultora que vende el servicio de selección. En su encuesta de 2017, autoseleccionada, el 19 % mencionó como motivo para contratar consultores una selección «sin sesgo», con la misma salvedad de interés.

## Cómo falla la elección

En lectura de esta base, la elección falla de cuatro maneras.

- Elegir por la demo: el producto se ve en el mejor caso del vendedor y no en el caso raro de la empresa, que es donde aparece la brecha.
- Elegir por la licencia: la licencia es solo una parte del costo, y según Hitt, Wu y Zhou (2002), citando a terceros, cerca de 60 % del costo de un ERP es instalación y personalización. El detalle está en [costo total para quien compra](../Mercado-y-economia/costo-total-para-quien-compra.md).
- Elegir con un solo criterio o una sola área: en el comercio, una fuente de parte nombra como errores comunes elegir solo por precio y decidir solo con el criterio del contador ([sistemas de gestión en el comercio](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md#cómo-se-elige-y-cómo-falla)).
- Elegir sin pensar en cómo se sale: cambiar de sistema después tiene [costos de cambio](../../Estrategia-competitiva/Fuentes-de-ventaja/costos-de-cambio.md): los datos, la capacitación y las personalizaciones quedan atados al producto.
