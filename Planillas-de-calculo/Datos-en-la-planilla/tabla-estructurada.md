---
resumen: >-
  Una tabla estructurada es un rango de datos convertido en objeto con nombre, que crece solo cuando
  se agregan filas y se referencia por el nombre de sus columnas. Es la "tabla de Excel" y las
  "tablas" de Google Sheets; no es una tabla dinámica.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Overview of Excel tables: https://support.microsoft.com/en-us/office/overview-of-excel-tables-7ab0bb7d-3a9e-4b56-a3c9-6c94334e492c"
  - "Exceljet, Excel tables: https://exceljet.net/articles/excel-tables"
  - "Google Workspace Updates, Tables in Google Sheets (2024-05-08): https://workspaceupdates.googleblog.com/2024/05/tables-in-google-sheets.html"
  - "Google Workspace Updates, Table reference improvements in Google Sheets (2024-11): https://workspaceupdates.googleblog.com/2024/11/table-reference-improvements-in-google-sheets.html"
  - "Microsoft, Create a PivotTable to analyze worksheet data: https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576"
aliases: [tabla de Excel, Excel table, Format as Table, dar formato como tabla, tablas de Google Sheets, Tables in Google Sheets, convertir en tabla, referencia estructurada, structured reference]
creado: 2026-11-27
revisado:
---

# Tabla estructurada

Una tabla estructurada es un rango de datos convertido en objeto con nombre, que crece solo cuando
se agregan filas y se referencia por el nombre de sus columnas. Es la "tabla de Excel" y las
"tablas" de Google Sheets; no es una tabla dinámica.

## Tabla estructurada no es tabla dinámica

Las dos se llaman "tabla" en la interfaz y hacen cosas opuestas. La tabla estructurada es donde se
guardan los datos crudos, fila por fila: la lista de ventas, el catálogo de productos. La
[tabla dinámica](../Analisis/tabla-dinamica.md) lee esos datos y muestra un resumen (ventas por mes y
por producto) que no se edita a mano. Lo normal es usarlas juntas: la tabla estructurada como origen
y la dinámica como salida. Microsoft lo recomienda así, porque si el origen es una tabla de Excel las
filas nuevas entran con más facilidad en la tabla dinámica.

## Por qué conviene: crece sola

Un rango común termina donde termina. Si la suma de ventas dice `=SUMA(D2:D500)` (SUM), la venta
de la fila 501 no cuenta, y nada avisa. Una tabla estructurada se estira cuando se escribe debajo de
su última fila, y todo lo que la referencia (fórmulas, tablas dinámicas, gráficos, validaciones)
toma la fila nueva. Exceljet llama a ese crecimiento "the single biggest benefit of tables".

El crecimiento viene con otras tres piezas en Excel, según Microsoft:

- **Referencias estructuradas.** La fórmula nombra la columna y no las celdas: `=SUMA(Ventas[Importe])`
  suma la columna Importe de la tabla Ventas, tenga 50 filas o 5000. El ejemplo de Exceljet en
  inglés es `=SUM(Orders[Amount])`.
- **Columna calculada.** Una fórmula escrita en una celda de la columna "is instantly applied to all
  other cells in that table column". Con eso todas las filas calculan igual (por ejemplo, un
  Importe que es Cantidad por Precio), que es la regla de fórmulas consistentes de
  [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md).
- **Fila de totales.** Las funciones que se eligen ahí se convierten en SUBTOTALES (SUBTOTAL), que
  ignoran las filas ocultas por un filtro: al filtrar un proveedor, el total muestra solo lo suyo.

## Cómo se arma en Excel y en Sheets

En Excel: Home > Format as Table, y marcar "My table has headers" si el rango tiene encabezado. Antes
conviene que el rango esté [ordenado](datos-ordenados.md): Exceljet pide quitar las filas en blanco y
dar un nombre único a cada columna. Después se le pone a la tabla un nombre que diga qué guarda
(Ventas, Productos), porque ese nombre aparece en cada fórmula.

En Google Sheets: Format > Convert to table. Google la anunció el 8 de mayo de 2024, para todas las
ediciones de Workspace y las cuentas personales. Las referencias usan el mismo formato que Excel
(`Task_tracker[Priority]` en el ejemplo de Google), y en noviembre de 2024 se mejoraron.

## Qué cambia entre las dos

| | Excel | Google Sheets |
|---|---|---|
| Referencias por columna | sí, `Tabla[Columna]` | sí, `Tabla[Columna]`, mejoradas en noviembre de 2024 |
| Tipos de columna | las fuentes leídas no los mencionan | fecha, moneda, desplegable; si el dato no coincide aparece una advertencia, no un bloqueo |
| Extras | columna calculada, fila de totales con SUBTOTALES | vista agrupada y plantillas (por ejemplo, inventario) |

Los tipos de columna de Sheets se parecen a la [validación de datos](validacion-de-datos.md), pero
advierten sin rechazar. Si una columna tiene que impedir valores fuera de lista, hace falta la
validación.

> [!NOTE]
> Sin fuente todavía: Google no tiene un artículo de ayuda detallado sobre las tablas de Sheets
> (solo los anuncios de 2024), así que sus límites de tamaño y el comportamiento de las fórmulas con
> rangos de tabla no están documentados acá.

## Qué leer

Para Excel, el artículo de Exceljet sobre tablas, en las secciones de referencias estructuradas y de
crecimiento automático; sus advertencias de versión están fechadas y cambian. Para Sheets, el anuncio
de Google de mayo de 2024, que es la única fuente con fechas y alcance.
