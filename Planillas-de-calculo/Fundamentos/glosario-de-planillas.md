---
resumen: >-
  Glosario de los términos del tema Planillas de cálculo, del libro y la celda a la matriz dinámica
  y Power Query, con el nombre en inglés y Excel y Google Sheets a la par, cada uno enlazado a la
  nota que lo trata.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft, Overview of formulas in Excel: https://support.microsoft.com/en-us/office/overview-of-formulas-in-excel-ecfdc708-9162-49e8-b993-c311f47ca173"
  - "Microsoft, Overview of Excel tables: https://support.microsoft.com/en-us/office/overview-of-excel-tables-7ab0bb7d-3a9e-4b56-a3c9-6c94334e492c"
  - "Microsoft, Dynamic array formulas and spilled array behavior (según resumen): https://support.microsoft.com/en-us/office/dynamic-array-formulas-and-spilled-array-behavior-205c6b06-03ba-4151-89a1-87a7eb36e531"
  - "Microsoft Learn, Excel Recalculation: https://learn.microsoft.com/en-us/office/client-developer/excel/excel-recalculation"
  - "Microsoft Learn, What is Power Query? (2026-09-30): https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query"
  - "Microsoft, Create a PivotTable to analyze worksheet data: https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576"
  - "Microsoft, Quick start: Create a macro: https://support.microsoft.com/en-us/office/quick-start-create-a-macro-741130ca-080d-49f5-9471-1e5fb3d581a8"
  - "Google Workspace Updates, Tables in Google Sheets (2024-05-08): https://workspaceupdates.googleblog.com/2024/05/tables-in-google-sheets.html"
  - "Google, ARRAYFORMULA (según resumen): https://support.google.com/docs/answer/3093275"
  - "Google, TO_DATE (según resumen): https://support.google.com/docs/answer/3094239"
  - "Planillas-de-calculo/.investigacion/posicion-contraria-y-fundamentos.md"
aliases: [glosario de Excel, glosario de Google Sheets, spreadsheet glossary, vocabulario de planillas]
creado: 2026-11-27
revisado: 2026-11-27
---

# Glosario de planillas

Glosario de los términos del tema Planillas de cálculo, del libro y la celda a la matriz dinámica y Power Query, con el nombre en inglés y Excel y Google Sheets a la par, cada uno enlazado a la nota que lo trata.

Las definiciones se apoyan en la documentación de Microsoft y de Google cuando define el término; Microsoft, por ejemplo, define la referencia y la constante pero no el libro ni la hoja. Donde ninguna documentación leída da una definición, la de acá es la de uso corriente y lo dice.

## La planilla y sus partes

| Término | Inglés | Qué es | Dónde se trata |
|---|---|---|---|
| Libro | workbook | El archivo de planilla, que contiene una o más hojas. En Sheets se le dice «hoja de cálculo» al archivo entero | [Modelo de la planilla](../Modelo-de-la-planilla/modelo-de-la-planilla.md) |
| Hoja | worksheet, sheet | Cada grilla de celdas dentro de un libro, con su pestaña | [Modelo de la planilla](../Modelo-de-la-planilla/modelo-de-la-planilla.md) |
| Celda | cell | El cruce de una fila y una columna; guarda un valor o una fórmula | [Celda y referencia](../Modelo-de-la-planilla/celda-y-referencia.md) |
| Rango | range | Un conjunto de celdas, casi siempre contiguas, como `A10:A20` | [Celda y referencia](../Modelo-de-la-planilla/celda-y-referencia.md) |
| Referencia | reference | Según Microsoft, "A reference identifies a cell or a range of cells on a worksheet" | [Celda y referencia](../Modelo-de-la-planilla/celda-y-referencia.md) |
| Referencia relativa | relative reference | La que cambia al copiar la fórmula: `A1` "is based on the relative position of the cell that contains the formula" | [Celda y referencia](../Modelo-de-la-planilla/celda-y-referencia.md) |
| Referencia absoluta | absolute reference | La que no cambia al copiar: `$A$1` "always refers to a cell in a specific location" | [Celda y referencia](../Modelo-de-la-planilla/celda-y-referencia.md) |
| Rango con nombre | named range, defined name | Un nombre (`RecargoTarjeta`) que reemplaza una referencia y hace legible la fórmula | [Celda y referencia](../Modelo-de-la-planilla/celda-y-referencia.md) |
| Valor y formato | value, format | Lo que la celda guarda y cómo se muestra; una fecha es un número con formato de fecha | [Tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md) |
| Número de serie de fecha | date serial number | El número con que la planilla guarda una fecha. Sheets cuenta los días desde el 30/12/1899 | [Tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md) |

## Fórmulas y cálculo

| Término | Inglés | Qué es | Dónde se trata |
|---|---|---|---|
| Fórmula | formula | Lo que se escribe en una celda empezando con `=`. Según Microsoft, puede contener "functions, references, operators, and constants" | [Fórmulas](../Formulas/formulas.md) |
| Función | function | Un cálculo con nombre que se usa dentro de una fórmula, como SUMA (SUM) o BUSCARX (XLOOKUP) | [Fórmulas](../Formulas/formulas.md) |
| Constante | constant | Según Microsoft, "a value that isn't calculated and always stays the same". Escrita adentro de una fórmula, es un número fijo que el ICAEW pide evitar | [Entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md) |
| Error de fórmula | formula error | El valor que muestra una celda cuando la fórmula no puede calcular: en castellano `#N/A`, `#¡REF!`, `#¡VALOR!` (en inglés, `#N/A`, `#REF!`, `#VALUE!`; algunas páginas escriben `#N/D`, como explica la nota de errores) | [Errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md) |
| Referencia circular | circular reference | Una fórmula que termina dependiendo de su propia celda | [Errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md) |
| Recálculo | recalculation | Volver a calcular las fórmulas cuando cambia algo. Excel tiene modo automático, automático excepto [tablas de datos](../Analisis/analisis-de-escenarios.md) y manual | [Errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md) |
| Función volátil | volatile function | Según Microsoft, una función "whose value cannot be assumed to be the same from one moment to the next", que se recalcula siempre; HOY (TODAY) y AHORA (NOW) son volátiles | [Errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md) |
| Matriz dinámica | dynamic array | Una fórmula que devuelve varios valores y los vuelca en las celdas vecinas, como FILTRAR (FILTER) u ORDENAR (SORT) | [Matrices dinámicas](../Formulas/matrices-dinamicas.md) |
| Desbordamiento | spill | El volcado de los resultados de una matriz dinámica. Si algo ocupa ese lugar, Excel muestra `#DESBORDAMIENTO!` (`#SPILL!`); `A1#` refiere al rango desbordado entero | [Matrices dinámicas](../Formulas/matrices-dinamicas.md) |
| ARRAYFORMULA | ARRAYFORMULA | Función de Sheets que aplica una fórmula a un rango entero; según Google, muchas fórmulas ya se expanden solas sin ella | [Matrices dinámicas](../Formulas/matrices-dinamicas.md) |
| Separador de argumentos | argument separator | El signo entre los argumentos de una función. En Excel es el "list separator" de la configuración regional de Windows, que en inglés de EE. UU. es la coma; que con coma decimal sea `;` es lo habitual pero no tiene fuente oficial (ver [tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md)). Los ejemplos de este tema usan `;` | [Fórmulas](../Formulas/formulas.md) |

## Datos y análisis

| Término | Inglés | Qué es | Dónde se trata |
|---|---|---|---|
| Datos ordenados | tidy data | Una fila por registro y una columna por variable, sin celdas combinadas | [Datos ordenados](../Datos-en-la-planilla/datos-ordenados.md); la regla general de Wickham, en [limpieza de datos](../../Datos/Analisis/limpieza-de-datos.md#datos-ordenados-una-variable-una-columna) |
| Tabla estructurada | table, Excel table | En el tema no se dice "tabla" a secas, porque nombra tres cosas distintas ([datos en la planilla](../Datos-en-la-planilla/datos-en-la-planilla.md)). En Excel, un rango con nombre y encabezados que crece solo y admite columnas calculadas; en Sheets existen desde 2024 (Formato, Convertir en tabla). No es una tabla dinámica | [Tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md) |
| Referencia estructurada | structured reference | La forma de nombrar una columna de una tabla en una fórmula, como `Ventas[Importe]` | [Tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md) |
| Validación de datos | data validation | Reglas que limitan qué se puede cargar en una celda, como una lista desplegable | [Validación de datos](../Datos-en-la-planilla/validacion-de-datos.md) |
| Power Query | Power Query | Según Microsoft, "a data transformation and data preparation engine" de Excel: importa, limpia y combina datos guardando los pasos, sin tocar el origen | [Power Query](../Datos-en-la-planilla/power-query.md) |
| M | M | El lenguaje en que Power Query guarda cada paso | [Power Query](../Datos-en-la-planilla/power-query.md) |
| Tabla dinámica | PivotTable, pivot table | Un resumen interactivo que agrupa y totaliza filas por categorías sin escribir fórmulas; en Excel trabaja sobre una copia en caché que hay que actualizar | [Tabla dinámica](../Analisis/tabla-dinamica.md) |
| Segmentación de datos | slicer | Botones que filtran una o varias tablas dinámicas | [Tabla dinámica](../Analisis/tabla-dinamica.md) |
| Análisis de hipótesis | what-if analysis | Probar qué pasa con un resultado si cambian las entradas: escenarios, tablas de datos y buscar objetivo | [Análisis de escenarios](../Analisis/analisis-de-escenarios.md) |
| Tabla de datos | data table | Una grilla de resultados de una fórmula para distintos valores de una o dos entradas; no es una tabla estructurada ni una dinámica | [Análisis de escenarios](../Analisis/analisis-de-escenarios.md) |
| Buscar objetivo | Goal Seek | Encontrar el valor de una entrada que lleva una fórmula a un resultado buscado; trabaja con una sola variable | [Análisis de escenarios](../Analisis/analisis-de-escenarios.md) |
| Solver | Solver | Complemento de Excel que optimiza un resultado cambiando varias celdas bajo restricciones | [Análisis de escenarios](../Analisis/analisis-de-escenarios.md) |
| Minigráfico | sparkline | Un gráfico chico dentro de una celda | [Gráficos en la planilla](../Analisis/graficos-en-la-planilla.md) |

## Diseño, automatización y trabajo compartido

| Término | Inglés | Qué es | Dónde se trata |
|---|---|---|---|
| Entradas, cálculo y salidas | inputs, calculations, outputs | La separación entre supuestos, fórmulas y resultados que pide el ICAEW | [Entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md) |
| Tasa de error por celda | cell error rate (CER) | La proporción de celdas con fórmula que tienen un error | [Errores en planillas](../Diseno-de-planillas/errores-en-planillas.md) |
| Rastrear precedentes y dependientes | trace precedents, trace dependents | Flechas de Excel que muestran de qué celdas sale una fórmula y qué celdas la usan | [Revisar una planilla](../Diseno-de-planillas/revisar-una-planilla.md) |
| Macro | macro | Un programa guardado en el libro que repite acciones; al grabarla, según Microsoft, "you are recording your mouse clicks and keystrokes" | [Macros](../Automatizar-y-compartir/macros.md) |
| VBA | Visual Basic for Applications | El lenguaje de las macros del Excel de escritorio | [Macros](../Automatizar-y-compartir/macros.md) |
| Office Scripts | Office Scripts | La automatización de Excel que funciona en la web, con grabadora y editor | [Macros](../Automatizar-y-compartir/macros.md) |
| Apps Script | Google Apps Script | El lenguaje de automatización de Google Sheets, basado en JavaScript | [Apps Script](../Automatizar-y-compartir/apps-script.md) |
| Función personalizada | custom function | Una función propia escrita en Apps Script que se usa en una celda | [Apps Script](../Automatizar-y-compartir/apps-script.md) |
| Disparador | trigger | Lo que hace que un script corra solo, al abrir, al editar o a una hora | [Apps Script](../Automatizar-y-compartir/apps-script.md) |
| Coautoría | co-authoring | Varias personas editando el mismo libro a la vez | [Compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md) |
| Rango protegido | protected range | Un rango o una hoja que solo ciertas personas pueden editar; en Sheets "isn't a security measure" | [Compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md) |
| Historial de versiones | version history | Las versiones anteriores del archivo, que se pueden ver y restaurar | [Compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md) |

> [!NOTE] Sin fuente todavía: libro, hoja, celda, rango, función, segmentación y minigráfico (en Excel) no tienen definición en las páginas leídas de Microsoft ni de Google; sus definiciones son las de uso corriente. Los nombres en castellano de la interfaz de Excel (por ejemplo, «Segmentación de datos») tampoco se verificaron contra la interfaz.
