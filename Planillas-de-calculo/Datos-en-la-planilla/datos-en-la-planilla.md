---
resumen: >-
  Datos en la planilla es la parte que se ocupa de cómo se guardan los datos crudos (ventas, stock,
  clientes) para que las fórmulas y el análisis funcionen: una fila por registro, rangos con nombre
  que crecen solos, reglas que frenan lo mal cargado y una herramienta para importar y limpiar.
estado: borrador
estabilidad: estable
fuentes:
  - "Karl W. Broman y Kara H. Woo, Data Organization in Spreadsheets, The American Statistician 72(1), 2018: https://kbroman.org/Paper_DataOrg/manuscript.html"
  - "Hadley Wickham, Tidy Data, Journal of Statistical Software 59(10), 2014: https://vita.had.co.nz/papers/tidy-data.html"
  - "Microsoft, Create a PivotTable to analyze worksheet data: https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576"
  - "Microsoft Learn, What is Power Query?: https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query"
  - "Planillas-de-calculo/.investigacion/datos-y-analisis.md (2026-11-27)"
aliases: [datos en la planilla, data in spreadsheets, organizar datos en Excel, organizar datos en Sheets]
creado: 2026-11-27
revisado:
---

# Datos en la planilla

Datos en la planilla es la parte que se ocupa de cómo se guardan los datos crudos (ventas, stock,
clientes) para que las fórmulas y el análisis funcionen: una fila por registro, rangos con nombre
que crecen solos, reglas que frenan lo mal cargado y una herramienta para importar y limpiar.

Es la materia prima del resto del tema. Las [fórmulas](../Formulas/formulas.md) buscan y suman sobre
estos datos, y el [análisis](../Analisis/analisis-en-planillas.md) los resume en tablas dinámicas y
gráficos. El [diseño de planillas](../Diseno-de-planillas/diseno-de-planillas.md) decide en qué hoja
viven y quién los carga. Cuando los datos ya no entran o los cargan muchos a la vez, el paso
siguiente es [una base de datos](../cuando-pasar-a-una-base.md), cuyo modelo de tablas
([base relacional](../../Bases-de-datos/Modelos-de-datos/base-relacional.md)) se parece mucho a una
planilla bien ordenada.

## Por qué el orden de los datos decide todo lo demás

Una planilla acepta cualquier cosa en cualquier celda, y casi todo lo que falla después nace ahí. Un
mes escrito como texto en vez de fecha, un total metido en el medio de la lista o una celda combinada
sobre dos filas rompen la suma, el filtro y la tabla dinámica sin dar error. Microsoft lo pide como
requisito para una tabla dinámica: "Your data should be organized in a tabular format, and not have
any blank rows or columns".

La regla de fondo es la de los datos ordenados: cada fila es un registro (una venta, un producto, un
cliente) y cada columna una sola variable (fecha, producto, cantidad, precio). Broman y Woo la bajan
a prácticas de carga, como una sola cosa por celda y los datos en un único rectángulo. Con eso, las
fórmulas se escriben una vez y se copian, y la tabla dinámica agrupa sin preparar nada.

## Las cuatro defensas, de la carga a la importación

Cada componente de esta vertical ataca un momento distinto de la vida del dato:

| Momento | Qué falla si no se cuida | Componente |
|---|---|---|
| Cómo se arma la lista | meses como columnas, totales en el medio, celdas combinadas | [datos ordenados](datos-ordenados.md) |
| Cuando la lista crece | fórmulas y resúmenes que no toman las filas nuevas | [tabla estructurada](tabla-estructurada.md) |
| Cuando alguien carga | "Coca 1.5" y "coca 1,5 lt" como dos productos | [validación de datos](validacion-de-datos.md) |
| Cuando los datos vienen de afuera | limpiar a mano el mismo archivo todos los meses | [Power Query](power-query.md) |

Las tres primeras se hacen igual en Excel y en Google Sheets, con diferencias de detalle. La cuarta
no: Power Query es un motor propio de Excel, y Sheets tiene en su lugar funciones que cubren partes
distintas del mismo trabajo, sin equivalencia uno a uno.

## Una palabra, tres objetos distintos

En este tema "tabla" a secas no se usa, porque nombra cosas distintas. La
[tabla estructurada](tabla-estructurada.md) es un rango con nombre que crece solo y donde viven los
datos. La [tabla dinámica](../Analisis/tabla-dinamica.md) es un resumen que se arma a partir de esos
datos. La tabla de datos del [análisis de escenarios](../Analisis/analisis-de-escenarios.md) es una
grilla de resultados para distintos valores de una o dos entradas.

## Qué hay adentro de los datos en la planilla

- [Datos ordenados](datos-ordenados.md) — una fila por registro y una columna por variable; leer
  antes que todo lo demás.
- [Tabla estructurada](tabla-estructurada.md) — la tabla de Excel y las tablas de Sheets: rangos con
  nombre que crecen solos y se referencian por columna.
- [Validación de datos](validacion-de-datos.md) — listas desplegables y reglas que rechazan o
  advierten lo mal cargado, y en qué difieren Excel y Sheets.
- [Power Query](power-query.md) — importar, limpiar y combinar archivos con pasos grabados en Excel,
  y lo que Sheets tiene en su lugar (IMPORTRANGE, QUERY, Connected Sheets).
