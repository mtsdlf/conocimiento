---
resumen: >-
  Una tabla dinámica es un resumen interactivo que agrupa una lista de datos por categorías y
  períodos y calcula totales, conteos o promedios, sin escribir fórmulas: se arma arrastrando campos
  a filas, columnas y valores.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Create a PivotTable to analyze worksheet data: https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576"
  - "Microsoft, Use slicers to filter data: https://support.microsoft.com/en-us/Excel/get-started/use-slicers-to-filter-data"
  - "Google, Customize a pivot table: https://support.google.com/docs/answer/7572895"
  - "OpenStax, Workplace Software and Skills, 11.4 PivotTables and Charts: https://openstax.org/books/workplace-software-skills/pages/11-4-pivottables-charts"
  - "Exceljet, How to group a pivot table by date: https://exceljet.net/videos/how-to-group-a-pivot-table-by-date"
aliases: [pivot table, PivotTable, tabla pivote, tabla dinámica de Google Sheets, segmentación de datos, slicer, timeline, escala de tiempo]
creado: 2026-11-27
revisado:
---

# Tabla dinámica

Una tabla dinámica es un resumen interactivo que agrupa una lista de datos por categorías y
períodos y calcula totales, conteos o promedios, sin escribir fórmulas: se arma arrastrando campos
a filas, columnas y valores.

## El caso: un año de ventas, ¿cuánto por mes y por producto?

Una planilla tiene una fila por venta: fecha, producto, rubro, cantidad, importe. Son miles de filas
y la pregunta es simple: cuánto se vendió de cada producto en cada mes. Con una tabla dinámica, el
producto va a filas, la fecha (agrupada por mes) a columnas y el importe a valores. El resultado es
una grilla de productos por meses con los totales, y cambiar la pregunta (por rubro en vez de por
producto, unidades en vez de importe) es arrastrar otro campo.

Es la misma operación que hace un GROUP BY en una base de datos
([agregación en SQL](../../Bases-de-datos/SQL/agregacion.md)): agrupar filas por una o más columnas y
calcular un total por grupo. La planilla la ofrece con el mouse.

## Lo que la tabla dinámica le pide a los datos

La tabla dinámica solo funciona bien sobre [datos ordenados](../Datos-en-la-planilla/datos-ordenados.md).
Microsoft lo dice como requisito: "Your data should be organized in a tabular format, and not have
any blank rows or columns." Los encabezados tienen que ser únicos y no vacíos, sin celdas combinadas
ni doble fila de encabezado. Una planilla con los meses como columnas no sirve de origen: hay que
pasarla antes a una fila por producto y mes.

Conviene que el origen sea una [tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md),
no un rango suelto: según Microsoft, así las filas nuevas entran con más facilidad. Con un rango
fijo, las ventas de la semana que se agregaron abajo quedan afuera del resumen.

## Cómo la arma Excel

Al poner campos en la tabla, Excel los ubica por defecto según su tipo: los campos no numéricos van
a filas, los de fecha y hora a columnas y los numéricos a valores. La ubicación se cambia arrastrando.

Microsoft 365 suma tablas dinámicas recomendadas, que proponen resúmenes armados; según Microsoft,
"Recommended PivotTables are available only to Microsoft 365 subscribers."

Para filtrar, Excel tiene segmentaciones (slicers), botones que filtran la tabla con un clic, y
escalas de tiempo (timelines) para las fechas. Según el resumen de la página de Microsoft: una
segmentación se conecta solo con tablas dinámicas del mismo origen de datos; combinar una escala de
tiempo y una segmentación sobre el mismo campo de fecha requiere la opción "Allow multiple filters
per field"; y Excel para la web solo crea segmentaciones locales. Un texto de OpenStax dice que los
campos calculados no se pueden usar con segmentaciones; no se confirmó con Microsoft.

## El error más común: no actualizar

La tabla dinámica de Excel no lee los datos en vivo: trabaja sobre una copia en caché (una copia guardada aparte de los datos de origen). Cuando cambia
el origen, "any PivotTables built on that data source need to be refreshed", con PivotTable Analyze >
Refresh > Refresh All. Si se corrige un precio en la lista de ventas y no se actualiza, la tabla
dinámica sigue mostrando el total viejo, sin ningún aviso. Es la diferencia de fondo con las
[fórmulas de sumar con condiciones](../Formulas/sumar-y-contar-con-condiciones.md), que se recalculan
solas.

En Sheets el riesgo aparece en los filtros: "Pivot table filter settings save the list of visible
values". Si entra un producto nuevo al origen, el filtro guardado no lo incluye hasta que se lo
actualiza.

## Qué cambia en Google Sheets

Sheets tiene tablas dinámicas con la misma lógica de filas, columnas, valores y filtros. Para ver
las ventas por mes hay que agrupar las fechas: clic derecho en una celda con formato de fecha y
"Create pivot date group"; se deshace con "Ungroup pivot items".

> [!NOTE]
> Sin fuente todavía: cómo se crea una tabla dinámica en Sheets paso a paso, sus segmentaciones
> (slicers) y sus campos calculados. La página de Google que se leyó cubre solo la personalización.

## Lo que se arma encima

Un gráfico dinámico se arma sobre la tabla dinámica y cambia cuando cambian sus campos o filtros; está
en [gráficos en la planilla](graficos-en-la-planilla.md). Si el resumen tiene que quedar en celdas que
otras fórmulas usan, conviene más
[sumar y contar con condiciones](../Formulas/sumar-y-contar-con-condiciones.md) o, en Sheets,
[QUERY](../Datos-en-la-planilla/power-query.md) con group by.

## Qué leer

La página de Microsoft sobre crear una tabla dinámica, en "Data Requirements" y en la sección de
actualización. Para Sheets, la ayuda de Google sobre personalizar tablas dinámicas, en el
agrupamiento de fechas. Exceljet tiene videos cortos con ejemplos, como el de agrupar por fecha.
