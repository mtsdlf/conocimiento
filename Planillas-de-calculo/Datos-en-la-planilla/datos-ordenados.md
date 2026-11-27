---
resumen: >-
  Datos ordenados es la forma de guardar datos en una planilla donde cada fila es un registro y cada
  columna una sola variable, en un único rectángulo sin totales ni celdas combinadas. Es la condición
  para que las fórmulas, los filtros y las tablas dinámicas funcionen sin preparación.
estado: borrador
estabilidad: estable
fuentes:
  - "Karl W. Broman y Kara H. Woo, Data Organization in Spreadsheets, The American Statistician 72(1), pp. 2-10, 2018, DOI 10.1080/00031305.2017.1375989: https://kbroman.org/Paper_DataOrg/manuscript.html"
  - "Hadley Wickham, Tidy Data, Journal of Statistical Software 59(10), 2014: https://vita.had.co.nz/papers/tidy-data.html"
  - "Microsoft, Create a PivotTable to analyze worksheet data: https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576"
  - "Microsoft Learn, What is Power Query?: https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query"
aliases: [tidy data, datos tidy, formato largo, una fila un registro, data organization in spreadsheets]
creado: 2026-11-27
revisado:
---

# Datos ordenados

Datos ordenados es la forma de guardar datos en una planilla donde cada fila es un registro y cada
columna una sola variable, en un único rectángulo sin totales ni celdas combinadas. Es la condición
para que las fórmulas, los filtros y las tablas dinámicas funcionen sin preparación.

## Las dos versiones de la regla: Wickham y Broman y Woo

La regla tiene dos formulaciones que se complementan. Wickham (2014) define un modelo de datos para
analizar: "Each variable is a column, each observation is a row, and each type of observational unit
is a table." Broman y Woo (2018) dan reglas de práctica para quien carga en la planilla. La primera
dice qué forma tienen que tener los datos; la segunda, cómo no estropearlos al escribirlos.

Las prácticas de Broman y Woo que más pesan en un negocio chico:

- **Una cosa por celda.** "The cells in your spreadsheet should each contain one piece of data.
  Don't put more than one thing in a cell." "500 g" son dos datos: el número va en la celda y la
  unidad en el nombre de la columna (`peso_g`) o en un diccionario de datos aparte.
- **Un solo rectángulo.** "The best layout for your data within a spreadsheet is as a single big
  rectangle." Nada de un bloque de ventas de enero y otro de febrero separados por filas vacías.
- **Sin celdas combinadas.** "Finally, don't merge cells." Una celda combinada deja vacías las
  demás, y el filtro o la tabla dinámica las ven vacías.
- **Ser consistente**, escribir las fechas como AAAA-MM-DD y usar validación al cargar, según el
  resumen del trabajo. La consistencia es su primera regla ("be consistent"): "CABA" en una fila y
  "Capital" en otra son dos lugares para la planilla.

> [!NOTE]
> Sin fuente todavía: las partes del trabajo de Broman y Woo sobre no usar el color como dato, no
> hacer cálculos en los datos crudos y armar un diccionario de datos no se leyeron en el texto.

El tercer pedazo de la regla de Wickham, una tabla por tipo de unidad, es el mismo principio que
ordena una [base relacional](../../Bases-de-datos/Modelos-de-datos/base-relacional.md): las ventas
van en una lista y los datos fijos de cada producto (precio de lista, proveedor) en otra, unidas por
el código de producto. Así el precio de un producto se corrige en un solo lugar y las ventas lo traen
con una [función de búsqueda](../Formulas/funciones-de-busqueda.md).

## Un caso: las ventas por mes como columnas

La forma más común de romper la regla es la planilla "ancha", hecha para leer y no para calcular:

| Producto | Ene | Feb | Mar |
|---|---|---|---|
| Yerba 1 kg | 120 | 95 | 130 |
| Azúcar 1 kg | 80 | 70 | 85 |

Se lee bien, pero el mes es una variable repartida en los encabezados. Para sumar el primer
trimestre por producto hay que nombrar columnas a mano, y abril obliga a tocar todas las fórmulas.
La versión ordenada, "larga", tiene una fila por producto y mes:

| Fecha | Producto | Unidades |
|---|---|---|
| 2026-01-01 | Yerba 1 kg | 120 |
| 2026-01-01 | Azúcar 1 kg | 80 |
| 2026-02-01 | Yerba 1 kg | 95 |

Con esta forma, abril son filas nuevas y nada más. El total por mes y por producto lo arma una
[tabla dinámica](../Analisis/tabla-dinamica.md) o una suma con condiciones
([sumar y contar con condiciones](../Formulas/sumar-y-contar-con-condiciones.md)), y la vista ancha
vuelve a aparecer como salida, sin ser el lugar donde se guardan los datos. Pasar de ancho a largo es
la operación que Power Query llama despivotar (unpivot), entre sus transformaciones avanzadas
([Power Query](power-query.md)).

## Dónde se nota en Excel y en Sheets

La regla es la misma en las dos aplicaciones, porque es anterior a ellas. Lo que cambia es la ayuda
para cumplirla. En las dos, convertir el rango en una [tabla estructurada](tabla-estructurada.md)
obliga a un encabezado por columna y hace que las filas nuevas entren solas. La
[validación de datos](validacion-de-datos.md) frena la inconsistencia al cargar. Microsoft pide para
la tabla dinámica encabezados únicos y no vacíos, sin celdas combinadas ni doble fila de encabezado:
es la misma regla, escrita como requisito.

Las fechas merecen cuidado aparte, porque la planilla las guarda como un número y las muestra con
formato; eso está en [tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md).

## Qué leer de Broman y Woo

El manuscrito de los autores está abierto. Las secciones a leer son "Put just one thing in a cell",
"Make it a rectangle", "No empty cells" y "Write dates like YYYY-MM-DD". Sus ejemplos son de
laboratorio (pesos de ratones, fechas de muestras); al leerlos, conviene traducirlos a productos,
ventas y stock. Wickham 2014 sirve como lectura teórica de apoyo, no como guía de carga.
