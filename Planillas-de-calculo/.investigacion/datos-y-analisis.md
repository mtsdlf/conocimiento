# Informe de investigación: Planillas de cálculo (Excel y Google Sheets), verticales "Datos en la planilla" y "Análisis"

Fecha de la investigación: 2026-11-27.

**Cómo leer las marcas.**
- [L] significa que abrí la URL con WebFetch. Esa herramienta devuelve un resumen hecho por un modelo, no el texto íntegro. Las citas literales son las que ese resumen transcribió y conviene recotejarlas antes de escribir la nota.
- [S] significa que solo vi el resumen del buscador.
- [M] significa solo metadatos.
- Puntajes de 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).
- Tipo: P es primaria, S es secundaria.

## 0. Sobre la división del árbol

- **"Datos en la planilla" sale bien como vertical.** Los tres componentes (datos ordenados, tabla estructurada, validación) son prácticas de Excel y Sheets a la par. Power Query es de otra naturaleza y no se parece a los otros tres, porque es un motor de ETL (extraer, transformar, cargar). En Excel es un componente separado con su propio lenguaje (M). Sheets no lo tiene como producto, solo equivalentes parciales.
  - Propuesta: ponerlo como componente propio, "Importar y limpiar (Power Query y sus equivalentes)", y no mezclarlo con "tabla estructurada".
  - Los equivalentes de Sheets (IMPORTRANGE, QUERY, Connected Sheets) hacen cosas distintas entre sí. QUERY es un lenguaje de consulta sobre un rango. IMPORTRANGE solo trae datos. Connected Sheets conecta con BigQuery.
  - No hay una relación uno a uno con Power Query. Conviene decirlo en la nota y no presentar una tabla de equivalencias falsa.
- **"Análisis" sale bien.** El campo (Microsoft, MOS) agrupa tabla dinámica y gráficos dinámicos, y por separado "análisis de hipótesis".
  - El examen MO-211 pone tablas y gráficos avanzados en un solo dominio ("Manage advanced charts and tables", 25–30%).
  - Solver no está dentro de "What-If Analysis" en el menú de Excel. Está en la pestaña Datos, como complemento aparte. Conviene tratarlo como subcomponente de escenarios, aclarando que es otra herramienta.
- **Dato clave para el árbol: el campo no usa la misma jerarquía en las dos plataformas.** En Excel, "tabla" y "tabla dinámica" son objetos distintos. En Sheets 2024 se sumó "Tablas" (convertir a tabla), que se parece a la tabla de Excel pero es más liviana. Hay que evitar que "tabla" a secas sea ambiguo en las notas.

## 1. Vertical "Datos en la planilla"

### 1.1 Datos ordenados (tidy data)

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Broman & Woo 2018, manuscrito de los autores | https://kbroman.org/Paper_DataOrg/manuscript.html | P | 3/3/3/3 | [L] parcial: leí hasta el carácter 200000 de 223679 |
| Broman & Woo 2018, ficha de la revista (*The American Statistician* 72(1), pp. 2–10, DOI 10.1080/00031305.2017.1375989) | https://www.tandfonline.com/doi/full/10.1080/00031305.2017.1375989 | P | 3/3/1/1 | [M]: el sitio devolvió 403. Datos de ficha vistos vía https://econpapers.repec.org/RePEc:taf:amstat:v:72:y:2018:i:1:p:2-10 [S] |
| Wickham 2014, "Tidy Data" | https://vita.had.co.nz/papers/tidy-data.html | P | 3/3/2/3 | [L], pero el resumen no trajo la lista de problemas típicos |
| Preprint de PeerJ | https://peerj.com/preprints/3183/ | P | 3/3/3/1 | no leído (403) |

**Afirmaciones**

- **Datos de la ficha.** Karl W. Broman y Kara H. Woo, "Data Organization in Spreadsheets", *The American Statistician* 72(1), pp. 2–10 (2018). (https://econpapers.repec.org/RePEc:taf:amstat:v:72:y:2018:i:1:p:2-10) [S]
- **Principios que enuncia el paper.** Ser consistente, escribir las fechas como YYYY-MM-DD, usar validación de datos para evitar errores de carga y guardar en texto plano. La primera regla es "be consistent". (resultado del buscador sobre https://kbroman.org/Paper_DataOrg/) [S]
- **Una cosa por celda.** "The cells in your spreadsheet should each contain one piece of data. Don't put more than one thing in a cell." (https://kbroman.org/Paper_DataOrg/manuscript.html) [L]
- **Celdas combinadas.** "Finally, don't merge cells." La misma fuente [L].
- **Unidades.** Es mejor dejar la columna como `body_weight` y poner la unidad en un diccionario de datos aparte. La misma fuente [L].
- **Forma del conjunto.** "The best layout for your data within a spreadsheet is as a single big rectangle." La misma fuente [L].
- **Fechas.** El software guarda las fechas como un número interno, con convenciones distintas en Windows y Mac. (resultado del buscador sobre https://kbroman.org/Paper_DataOrg/) [S]
- **Reglas de Wickham.** "Each variable is a column, each observation is a row, and each type of observational unit is a table." Publicado en *Journal of Statistical Software* 59(10), 2014. (https://vita.had.co.nz/papers/tidy-data.html) [L]

**Qué no pude verificar.** Las secciones sobre cálculos en los datos crudos, color o resaltado como dato, y diccionario de datos. Están en el paper y en mi memoria, pero no las vi en el texto leído. Hay que citarlas del paper y no de este informe.

Hay una diferencia de enfoque entre las dos fuentes, y la nota debería darla. Wickham define un modelo de datos (qué es una variable y qué es una observación), y Broman y Woo dan reglas de carga en la planilla. Las "tres reglas" de Wickham son para el análisis. Las de Broman y Woo son de práctica en la hoja.

**Recurso canónico:** Broman & Woo 2018, en el manuscrito de los autores (https://kbroman.org/Paper_DataOrg/manuscript.html). Las secciones a leer son "Put just one thing in a cell", "Make it a rectangle", "No empty cells" y "Write dates like YYYY-MM-DD". Hay que fijarse en que sus ejemplos son de laboratorio, no de negocio, y que habrá que traducirlos a costos y stock. Wickham 2014 va como lectura teórica de apoyo (las tres reglas), no como guía práctica.

### 1.2 Tabla estructurada

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft, "Overview of Excel tables" | https://support.microsoft.com/en-us/office/overview-of-excel-tables-7ab0bb7d-3a9e-4b56-a3c9-6c94334e492c | P | 3/2/2/2 | [L] |
| Exceljet, "Excel tables" (practicante) | https://exceljet.net/articles/excel-tables | S | 2/3/3/2 | [L] |
| Google Workspace Updates, "Tables in Google Sheets" (2024-05-08) | https://workspaceupdates.googleblog.com/2024/05/tables-in-google-sheets.html | P | 3/2/1/3 | [L] |
| Google Workspace Updates, mejoras en referencias de tabla (2024-11) | https://workspaceupdates.googleblog.com/2024/11/table-reference-improvements-in-google-sheets.html | P | 3/1/1/3 | [S] |

**Afirmaciones**

- **Excel, crear una tabla.** Home > Format as Table, y marcar "My table has headers" si hay encabezado. (https://support.microsoft.com/en-us/office/overview-of-excel-tables-7ab0bb7d-3a9e-4b56-a3c9-6c94334e492c) [L]
- **Excel, columna calculada.** La fórmula "is instantly applied to all other cells in that table column". La misma fuente [L].
- **Excel, fila de totales.** Las funciones elegidas se convierten a SUBTOTAL, así que ignoran las filas filtradas. La misma fuente [L].
- **Excel, referencias estructuradas.** Ejemplo: `=SUM(Orders[Amount])`. (https://exceljet.net/articles/excel-tables) [L]
- **Excel, crecimiento automático.** Exceljet lo llama "the single biggest benefit of tables". Antes de crear la tabla hay que quitar filas en blanco y dar nombre único a cada columna. La misma fuente [L].
- **Dato fechado.** Exceljet dice que nombrar la tabla desde el cuadro de creación solo está en el canal Beta de Excel 365 "as of September 2026". La misma fuente [L]. Hay que cotejarlo antes de afirmarlo, porque cambia con el tiempo.
- **Sheets, fecha y alcance.** El anuncio es del 8 de mayo de 2024. El menú es Format > Convert to table. (https://workspaceupdates.googleblog.com/2024/05/tables-in-google-sheets.html) [L]
  - Hay tipos de columna (fecha, moneda, desplegable). Si el dato no coincide con el tipo, aparece una advertencia y no se bloquea.
  - Hay vista agrupada y plantillas prediseñadas (por ejemplo, inventario).
  - Las referencias usan el formato `Task_tracker[Priority]`.
  - Está disponible para todas las ediciones de Workspace y las cuentas personales.
  - Despliegue en dominios de Rapid Release desde el 8 de mayo hasta el 13 de junio de 2024. En dominios de Scheduled Release, desde el 13 de junio de 2024.
  - Los administradores no tienen control sobre la función.
- **Sheets, ampliaciones.** En noviembre de 2024 se agregó la sugerencia "Convert to table". El 19 de noviembre de 2024 se mejoraron las referencias de tabla. (resultado del buscador sobre https://workspaceupdates.googleblog.com/2024/11/table-reference-improvements-in-google-sheets.html) [S]

**Recurso canónico.** Para Excel, el artículo de Exceljet sobre tablas. Hay que leer las secciones de referencias estructuradas y de crecimiento automático, y fijarse en que las advertencias de versión están fechadas. Para Sheets, el anuncio de Google de mayo de 2024. Es la única fuente con fechas y alcance, pero no tiene un artículo de ayuda detallado. Ese artículo es un hueco (ver sección final).

### 1.3 Validación de datos

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft, "Apply data validation to cells" | https://support.microsoft.com/en-us/office/apply-data-validation-to-cells-29fecbcc-d1b9-42c1-9d76-eff3ce5f7249 | P | 3/2/2/2 | [L] |
| Google, "Create a drop-down list" | https://support.google.com/docs/answer/186103 | P | 3/2/2/2 | [L] |

**Afirmaciones**

- **Excel, tipos.** Whole Number, Decimal, List, Date, Time, Text Length y Custom (esta última con fórmula). Las listas se escriben separadas por comas. (https://support.microsoft.com/en-us/office/apply-data-validation-to-cells-29fecbcc-d1b9-42c1-9d76-eff3ce5f7249) [L]
- **Excel, avisos de error.** Tres estilos: Stop ("Require users to fix the error before proceeding"), Warning (hay que elegir Yes o No) e Important (se puede seguir después de cerrar el mensaje). La página no menciona un estilo "Information". La misma fuente [L]. Ojo: en Excel en inglés el tercer estilo suele figurar como "Information". Conviene verificarlo en la interfaz antes de escribirlo.
- **Excel, limitación.** No se puede cambiar la validación si el libro está compartido (modo antiguo) o la hoja está protegida. La misma fuente [L].
- **Sheets, comportamiento por defecto.** Por defecto se rechazan las entradas que no coinciden con la lista. Para permitirlas, hay que poner "Show a warning" en las opciones avanzadas. (https://support.google.com/docs/answer/186103) [L]
- **Sheets, estilos.** Chip, Arrow o Plain text. Hay selección múltiple, solo en el formato chip. La lista se actualiza sola si cambia el rango de origen. La misma fuente [L].

**Discrepancia entre plataformas que la nota debería marcar.** En Excel hay tres niveles de aviso (Stop, Warning, Important). Sheets solo ofrece rechazar o advertir. En Excel el "Stop" por defecto rechaza.

Ninguna de las dos páginas cubre el pegado. Es la limitación práctica más conocida (pegar encima de una celda con validación borra la regla). La nota debe decir que la validación se puede saltar pegando, y eso hay que buscarlo en una fuente. Es un hueco.

**Recurso canónico.** Para cada plataforma, la página oficial correspondiente. Ambas son cortas. En Excel, la sección "Error Alert". En Sheets, "Advanced options". Broman y Woo (1.1) justifican el porqué de la validación.

### 1.4 Importar y limpiar: Power Query y equivalentes en Sheets

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft Learn, "What is Power Query?" (actualizada 2026-09-30) | https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query | P | 3/3/2/3 | [L] |
| Microsoft, "Power Query data sources in Excel versions" | https://support.microsoft.com/en-us/excel/power-query-data-sources-in-excel-versions | P | 3/3/2/3 | [L] |
| Microsoft, "Use Power Query in Excel for the web" | https://support.microsoft.com/excel/use-power-query-in-excel-for-the-web | P | 3/2/2/3 | [L] |
| Google, IMPORTRANGE | https://support.google.com/docs/answer/3093340 | P | 3/3/2/2 | [L] |
| Google, QUERY | https://support.google.com/docs/answer/3093343 | P | 3/2/3/2 | [L] |
| Connected Sheets (BigQuery) | https://support.google.com/docs/answer/9702507 | P | 3/2/1/3 | [S] |
| Ken Puls y Miguel Escobar, *M is for (Data) Monkey* (Holy Macro! Books, ISBN 9781615470341, 212 pp.) | https://www.allbookstores.com/Data-Monkey-Guide-Language-Excel/9781615470341 | S, practicantes | 2/3/3/3 | [M]. El año no se confirmó. |

**Afirmaciones**

- **Qué es.** "Power Query is a data transformation and data preparation engine". Registra las transformaciones como pasos y no modifica los datos de origen. (https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query) [L]
- **Transformaciones.** Entre las avanzadas están combinar (merge), anexar (append), agrupar, pivotar y despivotar. La misma fuente [L].
- **M.** Cada paso que se crea en el editor genera código M. El Advanced Editor permite editarlo. La misma fuente [L].
- **Dónde está.** Esa página dice que Excel para Windows y Excel para Mac tienen Power Query Desktop, y que Power Query Online es "No" para ambos. La misma fuente [L].
- **Discrepancia dentro de la misma página.** En otra sección de esa página, "Excel Online" figura entre los productos que usan Power Query Online. Hay que dar las dos y no resolverla por cuenta propia.
- **Windows.** Disponible en todas las versiones autónomas de Excel 2016 o posterior. Las ediciones perpetuas tienen "a large subset of features, but not all". Microsoft 365 "contains all the available Power Query features". (https://support.microsoft.com/en-us/excel/power-query-data-sources-in-excel-versions) [L]
- **Mac.** Disponible para suscriptores de Microsoft 365 mediante Get Data. Algunas fuentes (Text/CSV, libro de Excel, JSON, OData) permiten importar y actualizar. Otras (SQL Server, carpeta local, tabla o rango) solo actualizar. La misma fuente [L].
- **Web.** En la web se pueden crear consultas desde un libro de Excel, Text/CSV, XML, JSON, SQL Server, lista de SharePoint Online y OData. Se actualizan con Data > Refresh All. "Viewing and refreshing queries is available to all Microsoft 365 Subscribers." (https://support.microsoft.com/excel/use-power-query-in-excel-for-the-web) [L]
  - Otra página dice que en la web no se actualizan las consultas cargadas al Modelo de Datos y que el límite es de 1000 conexiones por usuario. (https://support.microsoft.com/en-us/excel/power-query-data-sources-in-excel-versions) [L]
  - Una publicación de julio de 2025 en el blog de Microsoft dice que la actualización con fuentes autenticadas seleccionadas ya está disponible de forma general. (resultado del buscador, https://techcommunity.microsoft.com/t5/excel-blog/new-in-excel-for-the-web-power-query-refresh-data-source/ba-p/4422757) [S]
- **Android e iOS.** No está soportado. La misma fuente (data-sources) [L].
- **IMPORTRANGE.** Sintaxis `IMPORTRANGE(spreadsheet_url, range_string)`. Hay que dar permiso explícito entre hojas. Tope de 10 MB por solicitud, y busca actualizaciones cada hora con el documento abierto. No admite funciones volátiles como NOW, RAND y RANDBETWEEN, y TODAY sí. (https://support.google.com/docs/answer/3093340) [L]
- **QUERY.** Corre una consulta en Google Visualization API Query Language, con cláusulas tipo SQL (select, where, group by, pivot, order by). Cada columna debería tener un solo tipo de dato. Si mezcla tipos, gana el más frecuente y el resto se trata como nulo. (https://support.google.com/docs/answer/3093343) [L]
- **Connected Sheets.** Es con BigQuery. Una página de administración lista las ediciones admitidas (Enterprise Standard y Plus, Education Standard y Plus, Enterprise Essentials y Essentials Plus). Una publicación de blog de Google Cloud de mayo de 2026 dice que alcanza con una cuenta de Workspace y un proyecto de Google Cloud con facturación. (resultado del buscador, https://support.google.com/a/answer/9604541) [S]. Las dos descripciones difieren. No son para un negocio chico, y la nota debería decirlo.

**Lo que Sheets no tiene.** Ninguna de las tres herramientas de Sheets repite el modelo de Power Query: pasos grabados, interfaz gráfica, importar carpetas o la web, y combinar sin fórmulas. No confirmé en las fuentes si Sheets tiene "importar carpeta". Hay que declarar la diferencia y no inventar un equivalente.

**Recurso canónico.**
- Para Excel: "What is Power Query?" de Microsoft Learn. Hay que leer las secciones de transformaciones, el lenguaje M y la tabla de "Where can you use Power Query?", y fijarse en la fecha de actualización (2026-09-30).
- Para disponibilidad: "Power Query data sources in Excel versions", porque es la única que separa web, Mac y Windows.
- Para profundizar: *M is for (Data) Monkey*, marcada como fuente de practicantes.
- Para Sheets: las páginas de ayuda de IMPORTRANGE y QUERY.

## 2. Vertical "Análisis"

### 2.1 Tabla dinámica

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft, "Create a PivotTable to analyze worksheet data" | https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576 | P | 3/2/2/2 | [L] |
| Google, "Customize a pivot table" | https://support.google.com/docs/answer/7572895 | P | 3/2/2/2 | [L] |
| Microsoft, slicers y timelines | https://support.microsoft.com/en-us/Excel/get-started/use-slicers-to-filter-data | P | 3/2/2/2 | [S] |
| Exceljet, videos de tablas dinámicas | https://exceljet.net/videos/how-to-group-a-pivot-table-by-date | S | 2/2/3/2 | [S] |

**Afirmaciones**

- **Excel, datos de origen.** "Your data should be organized in a tabular format, and not have any blank rows or columns." Los encabezados deben ser únicos y no vacíos, sin celdas combinadas ni doble fila de encabezado. Si el origen es una tabla de Excel, las filas nuevas entran con más facilidad. (https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576) [L]
- **Excel, áreas por defecto.** Filas para campos no numéricos, columnas para fecha y hora, y valores para campos numéricos. La misma fuente [L].
- **Excel, actualización.** La tabla dinámica trabaja sobre una copia en caché. Cuando cambia el origen "any PivotTables built on that data source need to be refreshed" (PivotTable Analyze > Refresh > Refresh All). La misma fuente [L]. Este es el error más frecuente de principiante y va en la nota.
- **Excel, tablas dinámicas recomendadas.** "Recommended PivotTables are available only to Microsoft 365 subscribers." La misma fuente [L].
- **Sheets, agrupar fechas.** Clic derecho en una celda con formato de fecha y "Create pivot date group". Se deshace con "Ungroup pivot items". (https://support.google.com/docs/answer/7572895) [L]
- **Sheets, filtros.** "Pivot table filter settings save the list of visible values", así que puede hacer falta actualizar el filtro si cambia el origen. La misma fuente [L].
- **Slicers y timelines en Excel.** Los slicers se conectan solo con tablas dinámicas del mismo origen de datos. Un timeline combinado con un slicer sobre el mismo campo de fecha requiere "Allow multiple filters per field". Excel para la web solo crea slicers locales. (resultado del buscador, https://support.microsoft.com/en-us/Excel/get-started/use-slicers-to-filter-data) [S]
- **Campos calculados con slicers.** Un texto de OpenStax dice que las columnas de campo calculado no se pueden usar con slicers. (https://openstax.org/books/workplace-software-skills/pages/11-4-pivottables-charts) [S]. Lo traigo como no verificado y secundario. No lo confirmé con Microsoft.

**Hueco declarado.** No encontré fuente primaria leída sobre estos puntos de Sheets: slicers, campos calculados y la creación completa ("Create & use pivot tables"). La página que abrí (7572895) cubre solo la personalización y se declara ella misma insuficiente. La nota de Sheets sobre slicers y campos calculados queda sin respaldo.

**Recurso canónico.** Para Excel, la página de Microsoft sobre crear una tabla dinámica. Hay que leer "Data Requirements" y la sección de actualización, y fijarse en que el origen debe ser ordenado, lo que enlaza con la vertical 1. Para Sheets, la ayuda de pivot tables de Google. Hay que fijarse en el agrupamiento de fechas. Exceljet es secundario y sirve para los ejemplos.

### 2.2 Gráficos en la planilla

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Google, "Sparkline charts" (página de ayuda) | https://support.google.com/docs/answer/9146780 | P | 3/1/1/2 | [L] |
| Google, función SPARKLINE | https://support.google.com/docs/answer/3093289 | P | 3/2/3/2 | [L] |
| Google Workspace Updates, 2014: nuevas opciones de sparkline | https://workspaceupdates.googleblog.com/2014/12/new-sparkline-options-in-google-sheets.html | P | 3/1/1/1 | [S] |

**Afirmaciones y discrepancia**

- **La función SPARKLINE.** La página de la función dice "Creates a miniature chart contained within a single cell". La sintaxis es `SPARKLINE(data, [options])`. Los tipos de `"charttype"` son `"line"` (por defecto), `"bar"`, `"column"` y `"winloss"`. (https://support.google.com/docs/answer/3093289) [L]
- **Discrepancia entre las dos páginas.** La página "Sparkline charts" dice: "You can no longer use sparkline charts in Google Sheets." Agrega que los sparklines viejos pueden mostrarse como gráfico de líneas y recomienda un gráfico de líneas. (https://support.google.com/docs/answer/9146780) [L]. Las dos páginas son de Google y se contradicen. Mi lectura, sin confirmar, es que la segunda describe un tipo de gráfico del editor de gráficos y que la función SPARKLINE sigue vigente. Hay que probarlo en una hoja real antes de escribir, y declarar la discrepancia en la nota.
- **Minigráficos en Excel (Sparklines).** No obtuve una fuente de Microsoft para esto. Está declarado como hueco.
- **Qué gráfico para qué en una planilla, ejes truncados y tortas con muchas porciones.** No obtuve una fuente de planilla para estos puntos. La teoría general está en otro tema. Hueco.
- **Gráficos dinámicos (PivotChart).** Aparecen en el examen MO-211 dentro del dominio "Manage advanced charts and tables", pero no leí el detalle del PDF. Hueco.

**Recurso canónico provisional.** Para sparklines en Sheets, la página de la función SPARKLINE, con la advertencia de la discrepancia. Para el resto del componente no hay un recurso canónico validado.

### 2.3 Análisis de escenarios y Solver

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft, "Introduction to What-If Analysis" | https://support.microsoft.com/en-US/excel/introduction-to-what-if-analysis | P | 3/2/2/3 | [L] |
| Microsoft, "Define and solve a problem by using Solver" | https://support.microsoft.com/en-us/office/define-and-solve-a-problem-by-using-solver-5d1a388f-079d-43ac-a7eb-f63e45925040 | P | 3/3/2/3 | [L] |
| Google Workspace Updates, 2019-10-09: complemento Goal Seek | https://workspaceupdates.googleblog.com/2019/10/goal-seek-addon-sheets9.html | P | 3/1/1/3 | [S] |
| Marketplace: SolveSheet, Optimization Solver, OpenSolver | https://workspace.google.com/marketplace/app/solvesheet/678357015177 | tercero (comercial) | 1/1/1/2 | [S] |
| MO-211, objetivos del examen | https://learn.microsoft.com/certifications/exams/mo-211 | P | 3/2/1/3 | [L] |

**Afirmaciones**

- **Escenarios.** "A Scenario can have multiple variables, but it can only accommodate up to 32 values." (https://support.microsoft.com/en-US/excel/introduction-to-what-if-analysis) [L]
- **Tabla de datos.** "A Data Table cannot accommodate more than two variables." La misma fuente [L].
- **Buscar objetivo (Goal Seek).** "Goal Seek works with only one variable input value." La misma fuente [L].
- **Resumen de escenarios.** Una guía de terceros advierte que tras editar escenarios el reporte no se actualiza solo. (resultado del buscador) [S]. No confirmado con Microsoft.
- **Solver, instalación.** Es un complemento que hay que activar. En Excel para la web, según la página, no hay complementos, así que hace falta la versión de escritorio. (https://support.microsoft.com/en-us/office/define-and-solve-a-problem-by-using-solver-5d1a388f-079d-43ac-a7eb-f63e45925040) [L]
- **Solver, límites.** "You can specify up to 200 variable cells". La celda objetivo debe contener una fórmula. La misma fuente [L].
- **Solver, restricciones.** Admite <=, =, >=, int, bin y dif. Las tres últimas solo sobre celdas de variables de decisión. La misma fuente [L].
- **Solver, métodos.** GRG Nonlinear ("smooth nonlinear"), Simplex LP ("linear") y Evolutionary ("non-smooth"). La misma fuente [L].
- **Sheets, Goal Seek.** Llegó como complemento, no como función nativa. Anuncio del 9 de octubre de 2019. (https://workspaceupdates.googleblog.com/2019/10/goal-seek-addon-sheets9.html) [S] No hallé evidencia de una versión nativa de Google. Hay varios complementos de terceros en el Marketplace.
- **Sheets, Solver.** No hay un Solver de Google. Hay complementos de terceros con límites distintos (https://workspace.google.com/marketplace/app/solvesheet/678357015177) [S]:
  - SolveSheet tiene niveles y su solver no lineal en la nube cuesta (un precio listado de USD 12.99 por mes, sujeto a cambio). Envía el modelo a un servicio externo, lo que importa si los datos son sensibles.
  - Optimization Solver admite hasta 50 variables de decisión.
  - OpenSolver tiene reseñas negativas sobre confiabilidad, que son afirmaciones de usuarios y no están verificadas.
  - Los datos del negocio pueden salir de la hoja al usar estos complementos. La nota debe decirlo.
- **Examen.** MO-211 (Microsoft Excel Expert, Microsoft 365 Apps). Dominios: Manage workbook options and settings (10–15%), Manage and format data (30–35%), Create advanced formulas and macros (25–30%), Manage advanced charts and tables (25–30%). Sin fecha de retiro. Página actualizada el 2026-07-01. Es el dato más fiable que traje sobre el examen. (https://learn.microsoft.com/certifications/exams/mo-211) [L]

**Hueco.** El PDF de objetivos (https://arch-center.azureedge.net/Learning/Credentials/MO-211_OD_MOS365_ExcelExpert.pdf) devolvió 404 en mi fetch. No pude leer qué punto del examen cubre escenarios, tablas dinámicas, Power Query o validación. No afirmo nada de esos puntos.

**Recurso canónico.** "Introduction to What-If Analysis" de Microsoft. Hay que fijarse en los tres límites numéricos (32 valores, dos variables, una variable) porque dicen cuándo usar cada herramienta. Para Solver, la página de Microsoft, mirando los tres métodos y el tope de 200 variables. Para Sheets, no hay recurso canónico de Google, y la nota debe decirlo.

## 3. Huecos y límites del trabajo

1. **Tabla de Sheets.** No hay página de ayuda detallada de Google. Solo el anuncio de 2024 y una nota resumida de noviembre de 2024 vista en el buscador [S]. Tampoco hay detalle de límites (tamaño, fórmulas con rangos de tabla).
2. **Validación.** Ninguna fuente leída cubre el pegado sobre celdas validadas ni "Circle invalid data" en Excel.
3. **Power Query.**
   - Discrepancia sin resolver sobre Excel para la web: la tabla de Learn dice "No" en Power Query Online, y el texto de la misma página incluye Excel Online.
   - No leí documentación de M a fondo, ni Combine (merge y append) en detalle, ni importar carpetas.
   - No verifiqué el año de *M is for (Data) Monkey*. Una búsqueda adicional en el sitio de la editorial lo resolvería.
   - No confirmé si Sheets tiene equivalente de "importar carpeta".
4. **Tabla dinámica en Sheets.** Sin fuente primaria leída para slicers, campos calculados y creación inicial.
5. **Tabla dinámica en Excel.** No leí la página de campos calculados ni las limitaciones. El dato de OpenStax es secundario.
6. **Gráficos.** Sin fuente sobre qué gráfico usar y para qué, gráficos dinámicos, minigráficos de Excel, ejes truncados ni tortas con muchas porciones. La discrepancia sobre sparklines en Sheets está sin resolver.
7. **Escenarios.** No leí el Administrador de escenarios en detalle ni la Tabla de datos con ejemplos. Para Sheets no verifiqué si existe un Goal Seek nativo posterior a 2019.
8. **Examen MO-211.** El PDF de objetivos no se pudo abrir. Solo sé los dominios y las ponderaciones.
9. **Wickham 2014.** El resumen de la herramienta no trajo los cinco problemas típicos. Hay que leerlo directo.
10. **Alcance de mi lectura.** El 403 de Taylor & Francis y de PeerJ me dejó sin la ficha de la revista, y Broman & Woo quedó leído en un 90% del manuscrito.
11. **Todo [L] es lectura vía resumen.** Antes de poner una cita literal en una nota, hay que recotejarla en la página.
