---
resumen: >-
  El análisis del gasto es juntar, limpiar, clasificar y analizar lo que la empresa le pagó a sus proveedores, para saber en qué y a quién le compra. Su producto son las categorías de compra, que son la unidad con que se decide la estrategia de abastecimiento.
estado: vigente
estabilidad: semi
fuentes:
  - "Wikipedia, Spend analysis (consultada 2026-11-27): https://en.wikipedia.org/wiki/Spend_analysis"
  - "CIPS, Category management: https://1prd-dxp.cips.org/intelligence-hub/category-management"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.1.5 «Analyze organization's spend profile»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Wikipedia, United Nations Standard Products and Services Code (consultada 2026-11-27): https://en.wikipedia.org/wiki/United_Nations_Standard_Products_and_Services_Code"
  - "Wikipedia, Procurement (según su resumen; gasto directo e indirecto, gasto bajo gestión): https://en.wikipedia.org/wiki/Procurement"
  - "Hurkens, van der Valk y Wynstra (2006), Total Cost of Ownership in the Services Sector: A Case Study, Journal of Supply Chain Management: https://repub.eur.nl/pub/57069/57069.pdf"
  - "Compras-y-abastecimiento/.investigacion/abastecimiento-estrategico.md (2026-11-27), sección 2"
  - "Compras-y-abastecimiento/.investigacion/fundamentos-y-contraria.md (2026-11-27), sección 1.7"
aliases: [análisis del gasto, análisis de gasto, spend analysis, spend analytics, mapa del gasto, cubo de gasto, spend cube, categoría de compra, categorías de compra, purchasing category, gasto directo, gasto indirecto, direct spend, indirect spend, gasto bajo gestión, spend under management]
creado: 2026-11-27
revisado: 2026-11-27
---

# Análisis del gasto

El análisis del gasto es juntar, limpiar, clasificar y analizar lo que la empresa le pagó a sus proveedores, para saber en qué y a quién le compra. Su producto son las categorías de compra, que son la unidad con que se decide la estrategia de abastecimiento.

En el recorrido de esta base es el primer paso de [Abastecimiento estratégico](abastecimiento-estrategico.md): sin saber cuánto se gasta en cada cosa no se puede ubicar nada en la [matriz de Kraljic](matriz-de-kraljic.md) ni decidir dónde vale la pena una [licitación](cotizacion-y-licitacion.md). APQC lo tiene como proceso propio, 4.2.1.5 «Analyze organization's spend profile», dentro del gobierno del abastecimiento y la gestión de categorías.

## Los cuatro pasos: juntar, limpiar, clasificar, analizar

La definición corriente lo describe como «the process of collecting, cleansing, classifying and analyzing expenditure data». Es una fuente secundaria; no se encontró una primaria que fije los pasos. El detalle de cada uno es lectura de esta base:

1. **Juntar**: las órdenes de compra, las facturas registradas en [cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md), los gastos con tarjeta y los reintegros. Lo que se paga sin orden de compra solo aparece en la factura o en el pago.
2. **Limpiar**: el mismo proveedor cargado tres veces con nombres distintos se tiene que juntar en uno, y lo mismo el mismo artículo con descripciones distintas. Es el problema del registro único que trata [datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md).
3. **Clasificar**: asignar cada renglón de gasto a una categoría de compra.
4. **Analizar**: cuánto se gasta por categoría, con cuántos proveedores, a qué precios y bajo qué acuerdos.

Cuál es la parte más costosa del trabajo no lo mide ninguna fuente leída; la limpieza de proveedores y artículos es la candidata, según esta base.

## La categoría de compra

Una categoría de compra es un grupo de cosas que se compran a un mismo mercado de proveedores y se pueden manejar juntas: papelería, transporte, chapa de acero, servicios de limpieza. CIPS define la gestión por categorías como «the process of dividing products into categories where they can be managed together», con cada categoría tratada como una unidad de negocio con su propia estrategia. Sus cinco pasos son Define, Analyse, Engage, Develop and implement y Review and improve; en Analyse se miran los patrones de gasto y las condiciones del mercado, que es donde entra el análisis del gasto.

La categoría se arma por el mercado que la abastece, no por el área que la pide. Si tres áreas compran impresoras por separado, el análisis las junta en una sola categoría, y ahí aparece el volumen que se puede negociar. Esto es criterio de la base, coherente con la consolidación de volúmenes que CIPS propone para [negociar](negociacion-de-compras.md).

Hay dos cortes por encima de la categoría. El gasto directo es lo que entra al producto (materias primas, componentes) y el indirecto, lo que no, según un resumen secundario; los ejemplos de indirecto (servicios, insumos de oficina, mantenimiento) son de la base. El gasto bajo gestión es la parte del gasto total que Compras gestiona o en la que influye, también según esa fuente.

## Clasificaciones estándar o propias

Para clasificar se puede usar una taxonomía propia o una estándar. Una de las estándar es UNSPSC, la clasificación de productos y servicios de las Naciones Unidas: «The four primary levels of the code are: Segment, Family, Class and Commodity», con dos dígitos por nivel y dos opcionales más para la función de negocio. La desarrollaron UNDP y Dun & Bradstreet en 1998; GS1 US la administró hasta 2024, cuando volvió al UNDP. La fuente es secundaria y la describe como una taxonomía para el comercio electrónico, sin ligarla al análisis del gasto.

Para quien diseña un sistema, la consecuencia es que la categoría tiene que ser un dato del artículo o del renglón de la orden de compra, cargado cuando se compra y no adivinado después a partir de la descripción. Es una inferencia de la base: clasificar después es el paso 3 de arriba, y es caro.

## Lo que el análisis muestra

El análisis no muestra solo precios. Las compras afectan costos que no figuran en la factura (inventario, calidad, administración, pago), como muestra el caso de Hurkens, van der Valk y Wynstra (2006); por eso, según esta base, un análisis completo cruza el gasto con los rechazos y las demoras de cada proveedor, que salen de la [evaluación de proveedores](../Proveedores/evaluacion-de-proveedores.md). Cómo se convierten esos costos en dinero está en [costo total de adquisición](costo-total-de-adquisicion.md).

Qué buscar en el gasto es criterio de la base, sin fuente que lo describa: concentración (pocas categorías que se llevan casi todo el gasto), fragmentación (muchos proveedores para lo mismo) y gasto sin acuerdo, el que no pasó por un [contrato marco](contrato-marco.md). El paralelo en el stock es la [clasificación ABC](../../Inventario-y-depositos/Reposicion/clasificacion-abc.md), que ordena artículos por valor de consumo.

> [!NOTE] Sin fuente todavía: cuánto se concentra el gasto típico (la proporción 80/20 que circula no tiene fuente leída), qué se sabe de la cola de gasto (tail spend), y cómo se detecta en el análisis la compra fuera del circuito (maverick spending). La compra que saltea el circuito como práctica está en [solicitud de compra](../Orden-de-compra/solicitud-de-compra.md).
