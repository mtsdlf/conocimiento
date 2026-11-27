---
resumen: >-
  La clasificación de costos ordena cada costo según cómo se comporta cuando cambia la actividad (fijo, variable, mixto), según si se puede atribuir a un producto (directo o indirecto) y según cuándo pasa a resultados (de producto o del período).
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Accounting, Volume 2: Managerial Accounting (2019), sección 2.2: https://openstax.org/books/principles-managerial-accounting/pages/2-2-identify-and-apply-basic-cost-behavior-patterns"
  - "OpenStax, ídem, sección 4.2 (según un resumen del buscador; no se leyó): https://openstax.org/books/principles-managerial-accounting/pages/4-2-describe-and-identify-the-three-major-components-of-product-costs-under-job-order-costing"
  - "Robert S. Kaplan, One Cost System Isn't Enough, Harvard Business Review, enero de 1988: https://eclass.aueb.gr/modules/document/file.php/LOXR285/Harvard%20Business%20Review%20-%20One%20Cost%20System%20isn%27t%20Enough.pdf"
  - "Contabilidad/.investigacion/contabilidad-de-gestion.md"
aliases: [comportamiento de costos, costo fijo, costo variable, costo mixto, costo semivariable, costo directo, costo indirecto, costo del período, cost behavior, fixed cost, variable cost, direct cost, overhead, period cost, product cost]
creado: 2026-11-27
revisado:
---

# Clasificación de costos

La clasificación de costos ordena cada costo según cómo se comporta cuando cambia la actividad (fijo, variable, mixto), según si se puede atribuir a un producto (directo o indirecto) y según cuándo pasa a resultados (de producto o del período).

Son tres cortes independientes sobre el mismo costo. El alquiler de una fábrica es fijo, indirecto y de producto; la comisión de un vendedor es variable, directa respecto de la venta y del período. Cada corte responde una pregunta distinta, y las demás notas de [contabilidad de gestión](contabilidad-de-gestion.md) usan uno u otro: el [punto de equilibrio](punto-de-equilibrio.md) necesita el primero, los [sistemas de costeo](sistemas-de-costeo.md) el segundo y el tercero.

## Fijo, variable y mixto: cómo se mueve el costo con la actividad

Según OpenStax (sección 2.2), un costo fijo no cambia en total en el corto plazo aunque cambie la actividad, y uno variable cambia en proporción directa al nivel de actividad. Un costo mixto tiene una parte fija y una variable. Las dos definiciones valen dentro del rango relevante, que el libro define como un nivel de actividad acotado por un mínimo y un máximo: fuera de él, el costo fijo puede saltar. Todas las fórmulas del [punto de equilibrio](punto-de-equilibrio.md) dependen de esa condición. El capítulo 2 de OpenStax (*Principles of Accounting, Volume 2: Managerial Accounting*) lo desarrolla con ejercicios.

Por unidad, el costo fijo baja cuando se produce más y el variable se queda igual. Por eso un costo unitario que incluye fijos solo vale para el volumen con que se calculó.

## Un astillero, un hotel y una fábrica de remeras

Los tres ejemplos de OpenStax 2.2 muestran los tres comportamientos.

| Caso | Datos de la fuente | Resultado |
|---|---|---|
| Carolina Yachts, fijo y variable | 625 barcos por año; costos fijos de US$ 1.560.000; variables de US$ 6.875.000 | fijo promedio de US$ 2496 por barco; variable de US$ 11.000 por barco |
| Ocean Breeze, mixto | US$ 2000 por mes, se alquilen las habitaciones que se alquilen, más US$ 5 por habitación por noche | con 60 habitaciones, US$ 2300 |
| Tony's T-Shirts, escalonado | costo total = US$ 6000 + US$ 0,75 por remera | pasadas las 2000 remeras, el fijo sube de US$ 6000 a US$ 8000 |

Una cuenta propia, sobre las cifras del astillero, muestra cómo se mueve el fijo unitario: si en vez de 625 barcos se hicieran 500, los mismos US$ 1.560.000 darían US$ 3120 por barco, y el variable seguiría en US$ 11.000.

## Directo e indirecto: si se puede atribuir al producto

Un costo directo se puede atribuir a un producto, un pedido o un cliente sin repartir nada: la madera de una mesa, las horas de quien la arma. Uno indirecto sirve a varios a la vez y solo llega a cada uno por reparto: la luz de la planta, el sueldo del supervisor. En la fabricación, según un resumen del buscador sobre OpenStax (sección 4.2, no leída), el costo de un producto tiene tres componentes: materiales directos, mano de obra directa y carga fabril, que junta todos los indirectos de producción.

La carga fabril es donde nace casi toda la discusión de la vertical, porque hay que elegir con qué base repartirla. Kaplan (1988) cuenta que muchas empresas la siguen repartiendo por mano de obra directa «even though direct labor may account for less than 5% of total manufacturing costs», porque las normas financieras no piden que el reparto siga la causa. Cómo se reparte bien está en [sistemas de costeo](sistemas-de-costeo.md) (ABC) y en [centros de costo](centros-de-costo.md) (reparto entre departamentos).

## De producto o del período: cuándo pasa a resultados

Un costo de producto se incorpora al valor del inventario y recién pasa a resultados como [costo de lo vendido](../Operaciones/costo-de-lo-vendido.md) cuando el producto se vende. Un costo del período se registra como gasto cuando ocurre: según el mismo resumen de OpenStax, es el caso de los gastos de ventas y de administración.

La línea entre uno y otro la fija el método de costeo. Con costeo por absorción, el costo fijo de fábrica es de producto y espera en el inventario; con costeo variable, es del período y va a resultados en el mes. Esa sola diferencia hace que el mismo año dé dos utilidades distintas, como muestra el ejemplo de Outdoor Nation en [sistemas de costeo](sistemas-de-costeo.md).

## El mismo costo cambia de clase según la pregunta

Según un resumen de la sección 2.2 de OpenStax, un mismo costo puede clasificarse distinto según para qué se use el dato. Dos ejemplos de la base: el sueldo de un jefe de taller es indirecto respecto de cada mesa y directo respecto del taller; la energía puede tratarse como fija para un presupuesto anual y como variable para cotizar un pedido grande.

Para quien construye un sistema, se sigue (inferencia de la base) que la clase de un costo funciona mejor como un atributo que se asigna según el análisis y no como una propiedad fija de la cuenta. Lo que el registro tiene que conservar es el dato que permite clasificarlo después: a qué producto, pedido, departamento o actividad corresponde cada movimiento, como se ve en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md). La división entre producto y período sí la fija la norma contable para los estados que salen afuera (inferencia de la base, sin fuente leída).
