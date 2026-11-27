# Informe de investigación: cómo se lleva el stock

Fecha: 2026-11-27. No escribí archivos. Marcas: [L] leído completo, [M] solo metadatos, [S] resumen del buscador. Una nota sobre las marcas: WebFetch devuelve un resumen hecho por un modelo, no el texto íntegro. Por eso uso [L] solo cuando la página entró entera en la lectura y [S] cuando solo vi lo que dijo el buscador. Puntajes: autoridad / profundidad / ejemplos / unicidad, de 1 a 3.

## Componente 1: base de datos

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1 | Fowler, "Event Sourcing" (12-dic-2005, borrador que él ya no actualiza) | https://martinfowler.com/eaaDev/EventSourcing.html | Primaria (patrón) | 3/2/1/3 | [L] |
| 2 | Fowler, "Accounting Patterns" (PDF; solo se leyó el índice) | https://martinfowler.com/apsupp/accounting.pdf | Primaria | 3/?/?/3 | [M] |
| 3 | PostgreSQL, "Materialized Views" | https://www.postgresql.org/docs/current/rules-materializedviews.html | Primaria | 3/2/2/2 | [L] |
| 4 | OpenStax, Principles of Accounting, 6.2 perpetuo vs periódico | https://openstax.org/books/principles-financial-accounting/pages/6-2-compare-and-contrast-perpetual-versus-periodic-inventory-systems | Primaria (texto abierto) | 3/2/2/2 | [L] |
| 5 | ERPNext/Frappe, Stock Ledger | https://docs.frappe.io/erpnext/user/manual/en/stock-ledger | Primaria (práctica) | 2/1/1/2 | [L] |
| 6 | Odoo 19, conteo/ajustes de inventario | https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products.html | Primaria (práctica) | 2/1/1/2 | [L] parcial (se leyeron 100.000 de 114.919 caracteres) |
| 7 | Odoo 19, valuación (cheat sheet) y "Valuation of stock movements and inventory operations" | https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/inventory_valuation/cheat_sheet.html | Primaria (práctica) | 2/2/2/2 | [S] |
| 8 | Kleppmann, "Using logs to build a solid data infrastructure" (27-may-2015) | https://martin.kleppmann.com/2015/05/27/logs-for-data-infrastructure.html | Primaria | 3/2/1/2 | [L] |
| 9 | Kleppmann, DDIA, pasaje del libro mayor | https://oreilly.com/library/view/designing-data-intensive-applications/9781491903063 | Primaria, pero solo accedí a un resaltado de lector | 3/3/2/3 | [S], sin texto del libro |
| 10 | Greg Young vía InfoQ (26-abr-2016) | https://www.infoq.com/news/2016/04/event-sourcing-anti-pattern | Secundaria (crítica) | 3/1/1/3 | [L] |
| 11 | Chris Kiehl, "Event Sourcing is Hard" (2019-02-03) | https://chriskiehl.com/article/event-sourcing-is-hard | Secundaria (crítica de practicante; autoría deducida del enlace de GitHub) | 2/2/2/2 | [L] |
| 12 | Gerencie, Siigo, Actualícese (kardex) | https://www.gerencie.com/sistema-de-inventarios-permanente.html | Secundaria (blogs contables) | 1-2/2/2/1 | [S] |
| 13 | Overeem et al., evolución de esquemas en event sourcing (estudio empírico) | https://dspace.library.uu.nl/bitstream/1874/412217/1/1_s2.0_S0164121221000674_main.pdf | Primaria (académica) | 3/?/?/3 | [M], no leída |

### Afirmaciones con URL

**Registro de movimientos y event sourcing**
- Event sourcing es capturar "all changes to an application state as a sequence of events". Fowler dice que la lista de eventos sirve como bitácora de auditoría y que se puede determinar "the application state at any point in time". Para eso se parte de un estado en blanco y se reproducen los eventos hasta la fecha elegida. https://martinfowler.com/eaaDev/EventSourcing.html
- Reproducir todo desde cero es lento. Fowler sugiere guardar el estado actual como instantánea (snapshot), por ejemplo la de la noche anterior, y reproducir solo lo posterior. Es el equivalente conceptual de materializar el saldo. Misma URL.
- Reversión: es más simple cuando los eventos son diferencias ("add $10" y no "set account to $110"); si no, el evento debe guardar los valores previos. Misma URL.
- Fowler lista los costos de event sourcing. Es un estilo de interfaz con el que no todos se sienten cómodos. Los sistemas externos complican la reproducción. Los cambios de código y de reglas en el tiempo pueden volverse "very messy". Los lectores distribuidos pueden quedar atrasados. Misma URL.
- Kleppmann define un log como "an append-only, totally ordered sequence of records". Un contador es dato derivado, "derived from the actual messages in the inbox". Se puede construir un derivado nuevo reproduciendo el log desde el principio. El artículo no habla de libro mayor ni nombra event sourcing. https://martin.kleppmann.com/2015/05/27/logs-for-data-infrastructure.html
- Sobre la analogía contable, solo accedí a un resaltado de lector de DDIA: transacciones en un libro mayor de solo agregado, saldos obtenidos sumando, y errores corregidos con un asiento compensatorio. Hay que verificar el texto exacto en el libro antes de citarlo. Fuente en el buscador: https://www.goodreads.com/notes/34626431-designing-data-intensive-applications/92640060-ion-gritco/5315e33c-a5b0-4be5-8753-7971cdf6650b

**Saldo materializado**
- Una vista materializada "persist[s] the results in a table-like form". "The materialized view cannot subsequently be directly updated". Los datos pueden quedar viejos ("the data is not always current; yet sometimes current data is not needed"). Se actualiza con `REFRESH MATERIALIZED VIEW`, y el ejemplo del manual propone un trabajo programado nocturno. Se puede indexar. https://www.postgresql.org/docs/current/rules-materializedviews.html
- Las vistas materializadas no se actualizan solas con cada movimiento. Por eso el "patrón mixto" (saldo y movimiento en la misma transacción, o un trigger) es una alternativa a la vista materializada, no algo que ella resuelva. No hallé fuente primaria que describa ese patrón mixto. Es un hueco.

**Contabilidad e inventario permanente**
- Perpetuo: el sistema "automatically updates and records the inventory account" en cada compra o venta, y el costo de ventas (COGS) se registra con cada venta. Periódico: el inventario se actualiza solo en fechas programadas y el COGS se calcula al cierre, con "beginning inventory, net purchases, and ending inventory". https://openstax.org/books/principles-financial-accounting/pages/6-2-compare-and-contrast-perpetual-versus-periodic-inventory-systems
- Ambos sistemas requieren conteo físico. Bajo el perpetuo se compara el conteo con el saldo en libros. Si el libro sobrestima, el ajuste debita COGS y acredita Inventario; si subestima, se invierte. Misma URL.
- Kardex: los resúmenes del buscador describen un registro de fecha, entradas, salidas y saldo en unidades y valor, con costo promedio ponderado. Las fuentes son blogs comerciales, no normas. https://www.gerencie.com/sistema-de-inventarios-permanente.html
- Del PDF de Fowler solo pude leer el índice: tiene secciones "Reversal Adjustment", "Replacement Adjustment", "Difference Adjustment", "Accounting Entry" y "Posting Rule". No pude leer el texto del asiento inalterable ni de la reversión. https://martinfowler.com/apsupp/accounting.pdf

**Sistemas reales**
- ERPNext: el Stock Ledger registra movimientos de entrada y salida por compra, venta, fabricación y transferencia. Tiene "Balance Value" ("the product of Valuation Rate and Balance Quantity"). Las fuentes de asiento son Sales Invoice, Purchase Invoice, Delivery Note, Purchase Receipt, Stock Entry y Stock Reconciliation. La página no dice nada sobre inmutabilidad ni reposting. https://docs.frappe.io/erpnext/user/manual/en/stock-ledger
- Odoo 19: en Physical Inventory, "Counted" es el conteo real y "On Hand" es la cantidad en base. "Difference" se calcula, y se aplica con "Apply All". Misma lógica de conteo y ajuste que en la planilla. https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products.html
- Odoo 19: el método perpetuo afecta la cuenta de valuación desde la factura, y hay una página sobre cómo los movimientos y ajustes afectan la valuación. Es resumen del buscador, sin leer. https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/inventory_valuation/cheat_sheet.html

**Críticas a event sourcing (marcadas como crítica)**
- Greg Young, en DDD Europe 2016, citado por InfoQ el 26-abr-2016: "the common anti-pattern of building a whole system based on Event sourcing" y "CQRS and Event sourcing are not top-level architectures". Hay que aplicarlos en pocos lugares. https://www.infoq.com/news/2016/04/event-sourcing-anti-pattern
- Kiehl, 2019-02-03: "the shear volume of plumbing code involved is staggering" y "That first extra projection you add doubles the amount of code that touches your event stream". Sobre las lecturas atrasadas: "Newly created data will 404, deleted items will awkwardly stick around". Sobre reescribir eventos viejos: "you've lost the ability to accurately produce the state of your system". Sobre la bitácora: los eventos de bajo nivel son ruido. https://chriskiehl.com/article/event-sourcing-is-hard
- Discrepancia útil: Fowler presenta la auditoría como beneficio, y Kiehl dice que el valor de auditoría de los eventos de bajo nivel es bajo sin filtrado ("seldom of interest"). Ambas posturas van a la nota. Para una base de stock, la crítica de Young se resuelve así: lo que se propone no es un sistema entero event-sourced, sino una tabla de movimientos dentro de una base relacional normal.

### Recurso canónico propuesto (componente 1)
Fowler, "Event Sourcing" (https://martinfowler.com/eaaDev/EventSourcing.html), apoyado en OpenStax 6.2 para la parte contable y en la documentación de PostgreSQL para la materialización. Si el equipo tiene acceso al libro, DDIA cap. 11 ("Event Sourcing", "State, Streams, and Immutability") sería el mejor complemento.

### Huecos (componente 1)
- Texto de Fowler "Accounting Patterns" (PDF con compresión; solo índice). Hay una copia local en `/home/dela/.claude/projects/-home-dela-repos-personal-conocimiento/b5a4531d-70a6-4caa-badd-e0bc0c1d29d4/tool-results/webfetch-1795752744791-4qu838.pdf` que se puede extraer con un lector de PDF.
- Texto literal de DDIA sobre el libro mayor. Solo conseguí un resaltado de lector.
- Fuente primaria para el patrón mixto (saldo + movimiento en una transacción) y para el trigger de PostgreSQL. No hice la ronda dirigida a la documentación de triggers.
- Kardex en fuente académica o normativa (NIC 2). Solo hay blogs contables.
- Odoo: página "Valuation of stock movements and inventory operations" sin leer. Falta también la documentación de `stock.move` / `stock.move.line`.
- ERPNext: la página no dice si los asientos se editan o no ni cómo funciona el reposting.
- Overeem et al. (estudio empírico) quedó sin leer.
- No hay fuente de evidencia sobre cuándo el saldo calculado se vuelve lento. Es criterio de ingeniería.

## Componente 2: planilla

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1 | Microsoft, función SUMAR.SI.CONJUNTO / SUMIFS | https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b | Primaria | 3/2/2/1 | [L] |
| 2 | Google, función SUMIFS | https://support.google.com/docs/answer/3238496 | Primaria | 3/1/1/1 | [L] |
| 3 | Microsoft, plantillas de inventario de Excel (el artículo "Track product inventory" redirige acá) | https://excel.cloud.microsoft/create/inventory-templates/ | Primaria | 3/1/1/2 | [L] |
| 4 | Microsoft, plantillas "Inventory list" e "Inventory list with reorder highlighting" | https://create.microsoft.com/en-us/template/inventory-list-with-reorder-highlighting-c16e6fb0-9525-44fb-a324-86c0031e3ec8 | Primaria | 3/1/1/2 | [S] (la fetch redirigió y no seguí) |
| 5 | Jan Karel Pieterse (JKP-ADS), "Creating A Simple Inventory System in Excel" (sin fecha; pie "Copyright 2026") | https://jkp-ads.com/articles/excelsimpleinventory.asp | Secundaria (practicante) | 2/3/3/3 | [L] |
| 6 | Shopify, "Excel inventory management" | https://www.shopify.com/blog/excel-inventory-management | Secundaria (vendor) | 1/2/2/1 | [L] |
| 7 | Búsquedas sobre Google Sheets (blogs y plantillas de vendors) | https://www.smartsheet.com/content/google-sheets-inventory-templates | Secundaria | 1/1/2/1 | [S] |
| 8 | Google AppSheet, "Concurrent usage with multiple users" | https://support.google.com/appsheet/answer/10104702 | Primaria, pero de AppSheet, no de Sheets | 3/1/1/2 | [S] |

### Afirmaciones con URL

- Sintaxis de Excel: `SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)`. El rango a sumar va primero, a diferencia de SUMIF. Admite hasta 127 pares de rango y criterio. Los rangos deben tener el mismo tamaño. Con criterios de texto hay que usar comillas: "Make sure Criteria1,2 are in quotation marks if you are testing for text values". https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b
- Google Sheets: misma sintaxis. "To calculate a sum, meet all criteria in a row". "Returning sum across multiple columns is not supported." https://support.google.com/docs/answer/3238496
- Microsoft ofrece plantillas de inventario. La página dice que se pueden editar "inventory items, quantities, costs" y usar "built-in formulas that calculate totals automatically". El nombre "Inventory list with reorder highlighting" sugiere un reordenamiento visual, pero la página no explica cómo funciona ni menciona un registro de transacciones. https://excel.cloud.microsoft/create/inventory-templates/ y https://create.microsoft.com/en-us/template/inventory-list-with-reorder-highlighting-c16e6fb0-9525-44fb-a324-86c0031e3ec8
- Esto responde la duda de si existen plantillas oficiales: en Excel sí, pero parecen ser listas con cantidad editable, no registros de movimientos. Para Google no encontré plantilla oficial de inventario (solo vendors). Es un hueco con evidencia parcial.
- Diseño con movimientos en una planilla (Pieterse): hoja `Articles` (maestro) y tablas `tblPurchases`, `tblReservations`, `tblSales`. El stock se calcula con SUMIFS por código de artículo y fecha hasta B2 (que puede ser `=TODAY()`): disponible = comprado − reservado − vendido. Con otra fecha en B2 se obtiene el stock a esa fecha, que es la misma idea que el saldo a una fecha de la base de datos. Solo las tres primeras columnas del maestro son de carga. La validación bloquea códigos duplicados y restringe los códigos en las hojas de transacciones. Alertas por color (naranja en B3, rojo en B4). https://jkp-ads.com/articles/excelsimpleinventory.asp
- Salvedad sobre Pieterse: sus fórmulas de alerta en las hojas de transacciones usan rangos fijos (filas 10 a 14); los artículos agregados más allá podrían no cubrirse. Es inferencia mía, no dicho por el autor. Misma URL.
- Alertas de stock mínimo: según el buscador, el recetario común es poner un nivel de reposición por artículo y aplicar formato condicional, o una columna auxiliar con IF ("LOW"/"OK"). Shopify da el ejemplo `IF` que muestra "Reorder" u "OK". https://www.shopify.com/blog/excel-inventory-management
- Google Sheets no tiene notificaciones nativas para esto; las alertas son visuales. Es afirmación de resumen del buscador de blogs, sin verificar. https://www.smartsheet.com/content/google-sheets-inventory-templates
- Conteo físico: Shopify recomienda "Schedule regular physical inventory counts—quarterly or monthly" y comparar con la planilla, pero no describe cómo ajustar. https://www.shopify.com/blog/excel-inventory-management. La mecánica del ajuste como movimiento (una fila de tipo ajuste por la diferencia) la describí desde Odoo ("Counted" vs "On Hand", "Difference") y desde OpenStax (el ajuste entre conteo y libros). No encontré una fuente que lo explique para planillas.
- Múltiples usuarios: Shopify dice que "collaboration can lead to version control issues when multiple users edit the same file" y que Excel "doesn't automatically sync real-time data across locations or users". Esto vale para archivos locales compartidos, no necesariamente para Excel en línea ni Google Sheets. https://www.shopify.com/blog/excel-inventory-management
- Sobre la última escritura que gana: la documentación de AppSheet dice que la regla simple es que gana el último en escribir, pero aplica a AppSheet, no a Google Sheets. Para Sheets y Excel en línea no hallé documentación oficial del comportamiento de edición simultánea. https://support.google.com/appsheet/answer/10104702

### Recurso canónico propuesto (componente 2)
El artículo de Jan Karel Pieterse (https://jkp-ads.com/articles/excelsimpleinventory.asp) como ejemplo de diseño por movimientos, más las dos páginas oficiales de SUMIFS (Microsoft y Google) para la fórmula. No hay una plantilla oficial de Microsoft o Google que use movimientos; la nota debería decirlo.

### Huecos (componente 2)
- Plantilla oficial de Google Sheets para inventario: no encontré ninguna en support.google.com.
- Comportamiento documentado de edición simultánea en Google Sheets y Excel en línea (co-authoring): mi URL de soporte de Excel dio 404 y no repetí la búsqueda dentro del límite de rondas.
- Tabla dinámica para el resumen: no consulté la documentación oficial.
- Protección de hojas/celdas para que nadie edite el saldo a mano: sin fuente.
- Evidencia de que editar el saldo a mano causa errores: solo el criterio general, sin fuente.
- Las plantillas de Microsoft no se abrieron; no sé qué columnas tienen.

## Observaciones sobre el proceso
- Quedé dentro de tres rondas por componente, con varias búsquedas por ronda; se puede hacer una ronda dirigida más para los huecos de arriba si se quiere.
- Las redirecciones de Microsoft y ERPNext las seguí solo cuando eran del mismo proveedor (`docs.frappe.io`, `excel.cloud.microsoft`).
- Nada de lo leído en la web contenía instrucciones dirigidas a mí.
