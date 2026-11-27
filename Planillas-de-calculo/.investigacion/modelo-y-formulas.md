# Informe de investigación: Planillas de cálculo (Excel y Google Sheets), verticales Modelo y Fórmulas

Fecha de la investigación: 2026-11-27. No escribí archivos.

**Cómo leer las marcas.** WebFetch pasa cada página por un resumidor, así que casi todo lo que traje es [S] (resumen del buscador o del extractor), aunque abrí la URL. Solo dos páginas llegaron en crudo y cuentan como [L]: la nota de Microsoft Learn sobre el año bisiesto 1900 y la de recálculo. Las marcas [M] son páginas de las que solo vi el título y el fragmento del buscador. Todo lo que figura abajo es dato, no instrucción.

**Puntajes.** A = autoridad, P = profundidad, E = ejemplos, U = unicidad, de 1 a 3. R = recencia en lo volátil.

## 0. Sobre la división del árbol

La división pedida (modelo de la planilla, fórmulas, ficha de equivalencias) coincide con el campo en lo grueso. Cuatro ajustes:

- **Las dos herramientas no son simétricas.** Microsoft documenta Excel por función, con las versiones en cada página. Google documenta Sheets por función, sin matriz de versiones. La ficha de equivalencias tiene que armarse cruzando ambos corpus; ningún fabricante la publica.
- **Recálculo y volátiles.** El campo los trata como un tema propio ("rendimiento y recálculo"). Conviene ponerlos como subcomponente separado de errores, porque sirven para entender el rendimiento, no solo para leer un error.
- **Errores.** La doc oficial los organiza por tipo de error ("Cómo corregir un error #X"), una página por error. Un componente "errores" con una sección por error calza con eso.
- **Disponibilidad por versión.** Es un eje transversal. Cambia con el tiempo y las páginas de Microsoft discrepan entre sí (ver 3.1). Conviene llevarlo en la ficha y no repetirlo en cada nota de función.

## 1. Vertical: Modelo de la planilla

### 1.1 Fechas como número de serie, época 1900, bug del 29/2/1900

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft Learn, "Excel incorrectly assumes that the year 1900 is a leap year" (actualizada 2026-04-15) | https://learn.microsoft.com/en-us/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year | Primaria | 3/2/1/3, R: 2026 | [L] |
| Microsoft, "Date systems in Excel" | https://support.microsoft.com/en-us/office/date-systems-in-excel-e7fe7167-48a9-4b96-bb53-5612a800b487 | Primaria | 3/2/2/2 | [S] |
| Google, TO_DATE | https://support.google.com/docs/answer/3094239 | Primaria | 3/1/2/2 | [S] |

Afirmaciones:
- Lotus 1-2-3 suponía que 1900 era bisiesto. Multiplan y Excel lo copiaron para usar el mismo sistema de fechas de serie y facilitar pasar planillas de un programa al otro. Fuente: https://learn.microsoft.com/en-us/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year
- Microsoft dice que corregirlo es posible, pero "the disadvantages of doing so outweigh the advantages". Corregirlo restaría un día a casi todas las fechas existentes, cambiaría los valores de SIFECHA/WEEKDAY y rompería la compatibilidad de fechas de serie con otros programas. Fuente: la misma.
- El único efecto que deja el error es que la función DIASEM (WEEKDAY) devuelve valores incorrectos para fechas anteriores al 1/3/1900. El resto de los años bisiestos, incluido 2100, los maneja bien. Fuente: la misma.
- Sistema 1900: el 5/7/2011 es el número de serie 40729. Sistema 1904: el mismo día es 39267. La diferencia es de 1.462 días. El 1900 es el predeterminado en Excel para Windows. Fuente: https://support.microsoft.com/en-us/office/date-systems-in-excel-e7fe7167-48a9-4b96-bb53-5612a800b487
- Google Sheets cuenta los días desde el 30/12/1899. Los valores negativos caen antes de esa fecha y las fracciones son la hora del día. Fuente: https://support.google.com/docs/answer/3094239
- Las dos herramientas coinciden en fechas posteriores al 1/3/1900, porque el epoch de Sheets absorbe el día falso.
- La página de Date systems no dice qué fecha es el serial 1. Hay que confirmarlo en otra fuente (ver huecos).

Recurso canónico: la nota de Learn sobre el bisiesto 1900 [L], leída entera. Fijarse en la lista de consecuencias. Para negocio chico alcanza con "no existe el 29/2/1900 y casi nunca importa", más la regla práctica de que una fecha es un número con formato.

### 1.2 Referencias, tipos de dato, número como texto, separador decimal, errores, recálculo

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft Learn, "Excel Recalculation" (doc de desarrollador, fecha 2018-08-22, actualizada 2024-12-18, "Applies to Excel 2013") | https://learn.microsoft.com/en-us/office/client-developer/excel/excel-recalculation | Primaria | 3/3/1/3, R: vieja | [L] |
| Microsoft, "Cómo corregir un error #DESBORDAMIENTO!" | https://support.microsoft.com/es-es/Excel/how-to-correct-a-spill-error | Primaria | 3/2/2/2 | [S] |
| Microsoft, "Convertir números almacenados como texto en números" | https://support.microsoft.com/es-es/Excel/convert-numbers-stored-as-text-to-numbers-in-excel | Primaria | 3/2/2/2 | [M] |
| Google, Ajustes de hoja: configuración regional y cálculo | https://support.google.com/docs/answer/58515 | Primaria | 3/2/1/3 | [S] |
| Exceljet, glosario "volatile function" | https://exceljet.net/glossary/volatile-function | Secundaria (practicante) | 2/1/2/1 | [M] |
| Vertex42, "volatile functions" | https://www.vertex42.com/blog/excel-formulas/volatile-functions.html | Secundaria | 1/1/2/1 | [M] |

Afirmaciones:
- **Recálculo.** Una función volátil es aquella "whose value cannot be assumed to be the same from one moment to the next". Excel la reevalúa junto con sus dependientes en cada recálculo, y Microsoft pide "Use them sparingly". Fuente: https://learn.microsoft.com/en-us/office/client-developer/excel/excel-recalculation
- **Lista de volátiles según esa página:** NOW, TODAY, RANDBETWEEN, OFFSET, INDIRECT, INFO y CELL (según argumentos) y SUMIF (según argumentos). Fuente: la misma.
- **Discrepancia sobre la lista.** El resumen del buscador de la misma doc citaba RAND y no incluía SUMIF; la página que leí en crudo lista RANDBETWEEN y SUMIF, pero no RAND. Hay que contrastar con otra fuente antes de afirmar la lista (ver huecos).
- **Modos de cálculo.** Excel tiene tres: automático, automático excepto tablas y manual. F9 recalcula todo lo pendiente y Ctrl+Alt+F9 recalcula todo en todos los libros abiertos. Fuente: la misma.
- **Referencias circulares.** Excel las detecta y avisa. Normalmente son un error, pero se pueden usar a propósito con cálculo iterativo. Fuente: la misma.
- **Sheets.** El modo de cálculo está en Archivo > Configuración > Cálculo, con automático y manual. El manual solo está para editores y no existe en la app móvil. Fuente: https://support.google.com/docs/answer/58515
- **Locale.** En Sheets el idioma y la zona horaria están en Archivo > Configuración > General y fijan moneda, fecha y formato de número por hoja, no por usuario. Fuente: la misma. En Excel la configuración regional depende del sistema operativo; no lo verifiqué (hueco).
- **Plazos de IMPORTRANGE.** La doc de Google dice que revisa actualizaciones cada hora y se recarga al abrir el documento. Fuentes: https://support.google.com/docs/answer/3093340 y la página de ajustes. La página de ajustes dice 30 minutos. Las dos discrepan: dar ambas cifras con su URL.
- **#DESBORDAMIENTO!** aparece cuando el rango de salida "no está en blanco". Otras causas: tamaño indeterminado por funciones volátiles como RANDBETWEEN, columnas completas que superan la grilla, tablas de Excel, falta de memoria y celdas combinadas. Fuente: https://support.microsoft.com/es-es/Excel/how-to-correct-a-spill-error
- **Grafía del error.** El título y el texto de esa página usan "#DESBORDAMIENTO!", sin signo de apertura. El buscador mostraba "#¡DESBORDAMIENTO!" solo en el resumen. Para la nota, mostrar la grafía de la página.
- **Nombres de errores en castellano que aparecieron.** #N/D (https://support.microsoft.com/es-es/office/dividirtexto-función-dividirtexto-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7), #VALOR! y #CALC! (https://support.microsoft.com/es-es/office/filtrar-función-filtrar-f4f7cb66-82eb-4767-8f7c-4877ad80c759), #REF! en las mismas. Los títulos de las páginas de ayuda en castellano usan #¡VALOR!, #¿NOMBRE?, #DIV/0! y #REF.; esos los vi solo en la lista del buscador [M].
- **Números como texto.** La doc de BUSCARV advierte que números o fechas guardados como texto, y los espacios al inicio o al final, dan resultados incorrectos. Fuente: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1

Recurso canónico por tema:
- **Recálculo y volátiles:** la página de Learn, aunque es de desarrollador y vieja. Leer las secciones "Volatile and Non-Volatile Functions" y "Calculation Modes". Contrastar la lista con Exceljet.
- **Errores:** la serie "Cómo corregir un error #X" de support.microsoft.com/es-es, una por error. Falta fetchear cada una; solo leí la de desbordamiento y la lista del buscador.
- **Referencias relativas, absolutas, mixtas, nombres y entre hojas:** no encontré página oficial leída (hueco).

## 2. Vertical: Fórmulas

### 2.1 Funciones lógicas

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft, SI.CONJUNTO | https://support.microsoft.com/es-es/office/si-conjunto-función-si-conjunto-36329a26-37b2-467c-972b-4a39bd951d45 | Primaria | 3/2/2/2 | [S] |
| Microsoft, TEXTSPLIT, nota sobre IFNA | https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7 | Primaria | 3/2/3/1 | [S] |

Afirmaciones:
- `=SI.CONJUNTO(prueba_lógica1; valor_si_verdadero1; [prueba_lógica2; valor_si_verdadero2]; ...)`. Admite hasta 127 pruebas. Microsoft desaconseja anidar muchas condiciones por lo difícil de generar, probar y actualizar. Fuente: la página de SI.CONJUNTO.
- SI.CONJUNTO se aplica a Microsoft 365, 2024, 2021 y 2019 (no figura 2016). Fuente: la misma.
- IFNA se recomienda para evitar los #N/A de TEXTSPLIT. Fuente: la página de TEXTSPLIT.
- No leí las páginas de SI, Y, O, SI.ERROR ni SI.ND. Los nombres en castellano de SI.ERROR y SI.ND los doy por conocidos, sin URL (hueco).

Recurso canónico: la página de SI.CONJUNTO, por su advertencia sobre anidar. Falta una fuente de SI.ERROR que explique el riesgo de esconder todos los errores.

### 2.2 Búsqueda

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft, BUSCARV (es) | https://support.microsoft.com/es-es/office/buscarv-función-buscarv-0bbc8083-26fe-4963-8ab8-93a18ad188a1 | Primaria | 3/3/2/2 | [S] |
| Microsoft, VLOOKUP (en) | https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1 | Primaria | 3/3/2/2 | [S] |
| Microsoft, BUSCARX (es) | https://support.microsoft.com/es-es/office/buscarx-función-buscarx-b7fd680e-6d10-43e6-84f9-88eae8bf5929 | Primaria | 3/3/2/2 | [S] |
| Microsoft, XLOOKUP (en) | https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929 | Primaria | 3/3/2/2 | [S] |
| Microsoft Excel blog, "Announcing XLOOKUP" (2019-08-28; actualizada 2021-06-25) | https://techcommunity.microsoft.com/blog/excelblog/announcing-xlookup/811376 | Primaria | 3/2/2/3, R: 2020-21 | [S] |
| Google, XLOOKUP | https://support.google.com/docs/answer/12405947 | Primaria | 3/2/1/2 | [S] |
| Google Workspace Updates, 2022-08-24 | https://workspaceupdates.googleblog.com/2022/08/named-functions-google-sheets.html | Primaria | 3/2/1/3, R: 2022 | [S] |
| 9to5Google, 2022-08-25 | https://9to5google.com/2022/08/25/google-sheets-xlookup/ | Secundaria (prensa) | 2/1/1/1 | [S] |
| Exceljet, XLOOKUP | https://exceljet.net/functions/xlookup-function | Secundaria (practicante) | 2/3/3/2 | [S] |
| Exceljet, INDEX | https://exceljet.net/functions/index-function | Secundaria (practicante) | 2/2/3/2 | [S] |

Afirmaciones:
- `BUSCARV(valor_buscado, matriz_buscar_en, indicador_columnas, [ordenado])`. En inglés `VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`. La coincidencia aproximada es el método predeterminado. Con 1/TRUE "assumes the first column in the table is sorted". Fuente: las páginas de BUSCARV y VLOOKUP.
- El valor buscado tiene que estar en la primera columna del rango, así que BUSCARV solo devuelve a la derecha. Si el índice de columna supera las columnas del rango da #REF!. Con aproximada y valor menor al mínimo da #N/A. Fuente: la página de VLOOKUP.
- Microsoft recomienda XLOOKUP, que "works in any direction and returns exact matches by default". Fuente: la página de VLOOKUP.
- `=BUSCARX(valor_buscado; matriz_buscada; matriz_devuelta; [si_no_se_encuentra]; [modo_de_coincidencia]; [modo_de_búsqueda])`. Coincidencia: 0 exacta (predeterminado), -1 exacta o menor siguiente, 1 exacta o mayor siguiente, 2 comodines. Búsqueda: 1, -1, 2 o -2 (binaria, requiere orden). Si no encuentra y se omite el cuarto argumento da #N/A. Fuente: la página de BUSCARX (es).
- **Disponibilidad de BUSCARX en Excel: discrepancia dentro de la misma página de Microsoft.** La lista "Applies To" incluye Excel 2019 y 2016, pero una nota dice "XLOOKUP is not available in Excel 2016 and Excel 2019". Fuentes: las páginas es y en de BUSCARX/XLOOKUP. Exceljet dice "Excel 2021+ and Excel 365". Fuente: https://exceljet.net/functions/xlookup-function
- **Historia en Excel.** Anunciada como Insiders el 2019-08-28. La nota de actualización dice que XLOOKUP y XMATCH llegaron a suscriptores de Office 365 en Monthly Channel (nota fechada "March 31st", sin año; el contexto sugiere 2020). El Semi-Annual figura "en julio" en una parte y "later this year" en otra, y el Semi-Annual (Targeted) a mediados de abril de 2020. Esas discrepancias están en la misma página: https://techcommunity.microsoft.com/blog/excelblog/announcing-xlookup/811376
- **Sheets: XLOOKUP y XMATCH.** La publicación de Workspace Updates del 2022-08-24 los incluye junto con LAMBDA, MAP, REDUCE, BYROW, BYCOL, SCAN y MAKEARRAY. Despliegue extendido, previsto completo al 2022-09-26. Fuente: https://workspaceupdates.googleblog.com/2022/08/named-functions-google-sheets.html
- 9to5Google lo reportó el 2022-08-25. Fuente: https://9to5google.com/2022/08/25/google-sheets-xlookup/
- La sintaxis de Sheets es `XLOOKUP(search_key, lookup_range, result_range, missing_value, match_mode, search_mode)`, con las mismas opciones predeterminadas que Excel (#N/A, 0, 1). Fuente: https://support.google.com/docs/answer/12405947
- Exceljet advierte que XLOOKUP devuelve un solo resultado (para todos usar FILTER). Dar "" en si_no_se_encuentra esconde el #N/A. Rangos de distinto tamaño dan #VALUE!. Fuente: https://exceljet.net/functions/xlookup-function
- INDICE+COINCIDIR cubre búsqueda a la izquierda, bidireccional y multicriterio. INDEX no es volátil. Ejemplo literal: `=INDEX(B5:E13,MATCH(G6,B5:B13,0),3)`. Fuente: https://exceljet.net/functions/index-function

Recurso canónico: la página de BUSCARV de Microsoft, la lista de limitaciones, para las fallas. Para la recomendación moderna, la página de BUSCARX más el post "Announcing XLOOKUP" para las fechas. En Sheets, la ayuda de XLOOKUP. Fijarse en la regla de versiones: si el libro lo abre alguien con Excel 2019 o anterior, BUSCARX falla.

### 2.3 Sumar y contar con condiciones

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft, SUMAR.SI.CONJUNTO | https://support.microsoft.com/es-es/office/sumar-si-conjunto-función-sumar-si-conjunto-c9e748f5-7ea7-455d-9406-611cebce642b | Primaria | 3/2/2/2 | [S] |
| Google, COUNTIFS (la URL 3256550 devolvió esta página) | https://support.google.com/docs/answer/3256550 | Primaria | 3/1/1/1 | [S] |

Afirmaciones:
- `SUMAR.SI.CONJUNTO(rango_suma; rango_criterios1; criterios1; [rango_criterios2; criterios2]; ...)`, hasta 127 pares. Cada rango de criterios debe tener el mismo número de filas y columnas que el de suma. Confundir el orden con SUMAR.SI es fuente común de errores, porque en SUMAR.SI el rango de suma va tercero. Se aplica a 365, 2024, 2021, 2019 y 2016. Fuente: la página de SUMAR.SI.CONJUNTO.
- COUNTIFS en Sheets: pares de rango y criterio, todos del mismo tamaño que el primero. Ejemplo literal `COUNTIFS(C1:C100, "Yes")`. Fuente: https://support.google.com/docs/answer/3256550
- No leí PROMEDIO.SI.CONJUNTO ni SUMAPRODUCTO (hueco).

Recurso canónico: la página de SUMAR.SI.CONJUNTO. Cubre además la inversión de orden de argumentos, el error más típico de quien viene de SUMAR.SI.

### 2.4 Texto y fechas

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft, SIFECHA | https://support.microsoft.com/es-es/office/sifecha-función-sifecha-25dba1a4-2812-480b-84dd-8b32a451b35c | Primaria | 3/2/2/2 | [S] |
| Microsoft, DIVIDIRTEXTO | https://support.microsoft.com/es-es/office/dividirtexto-función-dividirtexto-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7 | Primaria | 3/3/3/2 | [S] |
| Microsoft, TEXTSPLIT (en) | https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7 | Primaria | 3/3/3/2 | [S] |

Afirmaciones:
- `SIFECHA(fecha_inicial;fecha_final;unidad)`, con unidades "Y", "M", "D", "MD", "YM" y "YD". Excel la incluye por compatibilidad con Lotus 1-2-3 y puede dar resultados incorrectos. "MD" puede dar inexacto, cero o negativo, y no se recomienda. Si la fecha inicial es posterior a la final da #NUM!. Se aplica a 365, 2024, 2021, 2019 y 2016. Fuente: la página de SIFECHA.
- `=DIVIDIRTEXTO(texto, col_delimiter, [row_delimiter], [ignore_empty], [match_mode], [pad_with])`. El relleno predeterminado es #N/D. Con varios delimitadores se usa una constante de matriz, por ejemplo `{",","."}`. Fuente: la página de DIVIDIRTEXTO.
- DIVIDIRTEXTO y TEXTSPLIT solo se aplican a Excel 365 (Windows, Mac y Web) y Excel 2024. **No** aparecen en 2021 ni 2019. Fuente: la misma.
- En Sheets no encontré TEXTSPLIT en la tanda de funciones de febrero 2023. Hay SPLIT, que no verifiqué (hueco). Fuente de la tanda: https://workspaceupdates.googleblog.com/2023/01/google-sheets-powerful-functions-advanced-analysis.html
- No leí IZQUIERDA, EXTRAE, ESPACIOS, CONCAT, UNIRCADENAS, TEXTO, FECHA, HOY, DIAS.LAB ni FIN.MES (hueco). En TEXTO/TEXT el formato depende del idioma de la hoja; es una trampa clásica para la nota y falta fuente.

Recurso canónico: SIFECHA, por la advertencia de Microsoft sobre sus propios bugs. Para texto y fechas conviene un pase de fetch por función en es-es.

### 2.5 Matrices dinámicas, desbordamiento, LET, LAMBDA, QUERY

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft, "Dynamic array formulas and spilled array behavior" | https://support.microsoft.com/en-us/office/dynamic-array-formulas-and-spilled-array-behavior-205c6b06-03ba-4151-89a1-87a7eb36e531 | Primaria | 3/2/2/2 | [S] |
| Microsoft Excel blog, "Preview of Dynamic Arrays in Excel" (2018-09; actualizada 2020-07-01) | https://techcommunity.microsoft.com/blog/excelblog/preview-of-dynamic-arrays-in-excel/252944 | Primaria | 3/2/2/3, R: 2020 | [S] |
| Microsoft, FILTRAR | https://support.microsoft.com/es-es/office/filtrar-función-filtrar-f4f7cb66-82eb-4767-8f7c-4877ad80c759 | Primaria | 3/2/2/2 | [S] |
| Microsoft, LET (es) | https://support.microsoft.com/es-es/office/let-función-let-34842dd8-b92b-4d3f-b325-b8b8f9908999 | Primaria | 3/2/2/2 | [S] |
| Microsoft, LAMBDA | https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67 | Primaria | 3/3/2/2 | [S] |
| Google, QUERY | https://support.google.com/docs/answer/3093343 | Primaria | 3/2/1/3 | [S] |
| Google, ARRAYFORMULA | https://support.google.com/docs/answer/3093275 | Primaria | 3/1/1/3 | [S] |
| Google, FILTER | https://support.google.com/docs/answer/3093197 | Primaria | 3/1/1/2 | [S] |
| Google Workspace Updates, 2023-02-01 | https://workspaceupdates.googleblog.com/2023/01/google-sheets-powerful-functions-advanced-analysis.html | Primaria | 3/2/1/3, R: 2023 | [S] |

Afirmaciones:
- Cuando una fórmula devuelve varios valores, Excel los pone en celdas vecinas ("spilling"). Ejemplo: `=SORT(D2:D11,1,-1)`. Un #SPILL! aparece cuando algo bloquea el rango de salida. Fuente: la página de matrices dinámicas.
- Las nuevas funciones del post de 2018 son FILTER, UNIQUE, SORT, SORTBY, SEQUENCE y RANDARRAY. `A1#` refiere al rango entero desbordado. El post dice que, al 2020-07-01, estaba disponible en Office 365 en todos los endpoints. Fuente: el post "Preview of Dynamic Arrays in Excel".
- **Discrepancia sobre fechas de disponibilidad.** El buscador atribuyó a una página de soporte de Microsoft "enero de 2020, Current Channel", pero esa página me dio 403 y no pude verla [M]. Otro dato que no verifiqué: si 2021 incluye matrices dinámicas. La página de FILTRAR sí lista Excel 2021 y 2024, igual que la de LET. Eso lo confirma para FILTRAR y LET con URL.
- `=FILTRAR(matriz;incluir;[si_vacío])`. Si el resultado es vacío y no hay tercer argumento, da #CALC!. Si "incluir" tiene errores, devuelve error. Se aplica a 365, 2024 y 2021. Fuente: la página de FILTRAR.
- `=LET(nombre1, nombre_valor1, cálculo_o_nombre2, ...)`, hasta 126 pares. Se aplica a 365, 2024 y 2021. Fuente: la página de LET.
- `=LAMBDA([parámetro1, ...,] cálculo)`, hasta 253 parámetros. Se aplica solo a 365 y 2024. Una LAMBDA creada en una celda sin llamarla da #CALC!. Pasarse en recursión da #NUM!. Fuente: la página de LAMBDA. Los helpers (MAP, REDUCE, SCAN, BYROW, BYCOL, MAKEARRAY, ISOMITTED) aparecen solo como enlaces relacionados.
- **Sheets: LAMBDA y helpers.** Anunciados el 2022-08-24 con MAP, REDUCE, BYROW, BYCOL, SCAN y MAKEARRAY. Fuente: la publicación de Workspace Updates de agosto 2022.
- **Sheets: LET.** Anunciada el 2023-02-01. El despliegue se pausó el 2023-02-22, se reanudó el 2023-03-01 y se esperaba completo al 2023-03-14. Esa publicación también trae TOROW, TOCOL, CHOOSEROWS, CHOOSECOLS, WRAPROWS, WRAPCOLS, VSTACK, HSTACK, EPOCHTODATE y MARGINOFERROR (11 funciones). Fuente: la publicación de Workspace Updates de enero-febrero 2023.
- **QUERY (Sheets):** `QUERY(data, query, [headers])`. Usa el lenguaje de consulta de la Google Visualization API. Cada columna debe tener un solo tipo de valor. Si se omiten los encabezados o se pone -1, Sheets los adivina. Fuente: https://support.google.com/docs/answer/3093343
- **ARRAYFORMULA:** `ARRAYFORMULA(array_formula)`. Muchas fórmulas ya se expanden solas y no hace falta. Fuente: https://support.google.com/docs/answer/3093275
- **FILTER en Sheets:** `FILTER(range, condition1, [condition2, ...])`. Si nada cumple devuelve #N/A, mientras que en Excel da #CALC! salvo que se use el tercer argumento. Fuentes: https://support.google.com/docs/answer/3093197 y la página de FILTRAR.
- No encontré fuente oficial leída sobre SORT, UNIQUE o SEQUENCE en Sheets ni sobre desde cuándo existen. Es un hueco, aunque están desde hace años.

Recurso canónico: para qué hay hoy, la página de cada función en es-es, porque lleva la lista de versiones (ahí está la diferencia 2021 contra 2024: LAMBDA y TEXTSPLIT solo en 2024). Para el modelo mental, el post de Excel blog de 2018, con la nota de 2020. Para Sheets, Workspace Updates de 2022 y 2023.

## 3. Ficha de equivalencias

### 3.1 Tabla (castellano / inglés, Excel y Sheets)

El castellano sale de las páginas de Microsoft en es-es. Los nombres que aparecen sin URL vienen de conocimiento propio y hay que verificarlos antes de publicar. Para el nombre en Sheets en castellano no leí fuente: asumo que coincide con el de Excel, y la ayuda de Google en es lo debería confirmar.

| Español | Inglés | Excel | Sheets | Fuente |
|---|---|---|---|---|
| BUSCARV | VLOOKUP | todas | sí | páginas de BUSCARV/VLOOKUP |
| BUSCARX | XLOOKUP | 365 (desde 2020), 2021, 2024; no 2019 ni 2016 | sí, desde agosto 2022 | páginas de BUSCARX, XLOOKUP, Google, post de agosto 2022 |
| SI.CONJUNTO | IFS | 365, 2024, 2021, 2019 | no verificado | página de SI.CONJUNTO |
| SUMAR.SI.CONJUNTO | SUMIFS | 2016 en adelante y 365 | no verificado (COUNTIFS sí) | páginas de SUMAR.SI.CONJUNTO y COUNTIFS |
| SIFECHA | DATEDIF | 365, 2024, 2021, 2019, 2016 (por compatibilidad Lotus) | no verificado | página de SIFECHA |
| FILTRAR | FILTER | 365, 2024, 2021 | sí | páginas de FILTRAR y Google FILTER |
| LET | LET | 365, 2024, 2021 | sí, desde febrero-marzo 2023 | páginas de LET y Workspace Updates |
| LAMBDA | LAMBDA | solo 365 y 2024 | sí, desde agosto 2022 | páginas de LAMBDA y Workspace Updates |
| DIVIDIRTEXTO | TEXTSPLIT | solo 365 y 2024 | sin evidencia (existe SPLIT, no verificado) | páginas de DIVIDIRTEXTO y TEXTSPLIT |
| SI.ND | IFNA | no leída | no leída | solo mención en la página de TEXTSPLIT |
| QUERY | QUERY | no existe (alternativa: Power Query, otra herramienta) | sí | https://support.google.com/docs/answer/3093343 |
| IMPORTRANGE | IMPORTRANGE | no existe (equivalente: vínculos externos, no verificado) | sí | https://support.google.com/docs/answer/3093340 |
| ARRAYFORMULA | ARRAYFORMULA | no hace falta; las fórmulas ya se desbordan | sí | página de ARRAYFORMULA y de matrices dinámicas |

### 3.2 Funciones que existen en una sola

- **Solo Sheets (con fuente):** QUERY, IMPORTRANGE y ARRAYFORMULA.
- **Solo Excel (sin página leída):** Power Query y la sintaxis `A1#` de rango desbordado, que viene del post de 2018. En Sheets la ficha no confirma su existencia. Sobre Power Query no pude abrir ninguna página oficial (403).
- **LAMBDA helpers.** Ambas herramientas los tienen. En Sheets están desde agosto 2022 (fuente arriba). En Excel solo leí que la página de LAMBDA los menciona, y no cubre versiones; hay que verificar cada helper.
- **Errores propios.** #CALC! de Excel contra #N/A de Sheets en FILTER vacío (ver 2.5).

Recurso canónico de la ficha: ninguno publicado por los fabricantes. Se arma desde las páginas por función de ambos corpus y se actualiza con Workspace Updates y el Excel blog. Fijarse en las versiones y en las fechas.

### 3.3 Programa de certificación (MOS)

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Microsoft Learn, Examen MO-211 Excel Expert (Microsoft 365 Apps) (actualizada 2026-07-01) | https://learn.microsoft.com/certifications/exams/mo-211 | Primaria | 3/1/1/3, R: 2026 | [L] |
| Esquema de habilidades (PDF) | https://arch-center.azureedge.net/Learning/Credentials/MO-211_OD_MOS365_ExcelExpert.pdf | Primaria | 3/3/1/3 | [M] no abierto |

Afirmaciones:
- Dominios y pesos del MO-211: gestionar opciones y ajustes del libro (10-15%), gestionar y dar formato a los datos (30-35%), crear fórmulas avanzadas y macros (25-30%), gestionar gráficos y tablas avanzados (25-30%). Sin fecha de retiro. Solo en inglés. Fuente: https://learn.microsoft.com/certifications/exams/mo-211
- Ejemplos de libros expertos que da Microsoft: plantillas de negocio, tablas de amortización y planillas de inventario. Fuente: la misma.
- El examen es el nivel experto; para un negocio chico sirve como lista de temas, no como programa de estudio.

Recurso canónico: el PDF de objetivos (hay que abrirlo; no lo leí). Fijarse en qué funciones lista bajo "Create advanced formulas" para saber el piso de lo "avanzado" según Microsoft.

## 4. Huecos

1. **Epoch.** Falta fuente oficial que diga que el serial 1 es el 1/1/1900. La página de Date systems no lo dice.
2. **Referencias.** No leí documentación oficial de referencias relativas, absolutas y mixtas, rangos con nombre ni referencias entre hojas, ni en Excel ni en Sheets.
3. **Regional.** Falta la fuente de Excel sobre separador decimal y de listas según el sistema (la de Sheets sí está). Tampoco leí la página oficial de formato contra valor.
4. **Números como texto.** La página en castellano solo la vi como fragmento del buscador [M]; la fetch dio 403.
5. **Errores.** Falta una página oficial leída por cada error (#N/D, #¡REF!, #¡VALOR!, #¡DIV/0!, #¿NOMBRE?, circular) y la de errores de Sheets. La URL que probé para eso (3256550) devolvió COUNTIFS.
6. **Lista de volátiles.** Discrepa entre el resumen del buscador (RAND) y la página en crudo (RANDBETWEEN, SUMIF, sin RAND). Falta una tercera fuente, que podría ser Exceljet (solo vi el fragmento).
7. **Sheets recalcula distinto.** Falta confirmar la política de recálculo de funciones volátiles en Sheets y la discrepancia 30 minutos contra una hora de IMPORTRANGE.
8. **Funciones sin leer:** SI, Y, O, SI.ERROR, SI.ND, PROMEDIO.SI.CONJUNTO, SUMAPRODUCTO, IZQUIERDA, EXTRAE, ESPACIOS, CONCAT, UNIRCADENAS, TEXTO, FECHA, HOY, DIAS.LAB, FIN.MES, ORDENAR, UNICOS, SECUENCIA. Sus nombres en castellano de arriba no tienen URL.
9. **Versiones.** Falta la página oficial que fije en qué versión de Excel arrancaron las matrices dinámicas: la de Microsoft sobre "dynamic-array-formulas-vs-legacy" dio 403. Tampoco confirmé la fecha de entrada de BUSCARX en 2021, más allá de la lista de la página. Tampoco hay fuente sobre desde cuándo existen FILTER, SORT, UNIQUE y SEQUENCE en Sheets.
10. **Power Query.** No hay página oficial leída (403). Tampoco hay fuente sobre equivalentes de IMPORTRANGE en Excel.
11. **MOS.** El PDF de objetivos no lo abrí.
12. **Practicantes.** Chandoo y el blog de Microsoft Excel quedaron sin leer, salvo Exceljet (XLOOKUP, INDEX) y los posts de techcommunity. Faltan casos de fallas de BUSCARV en situaciones de stock, costos y ventas.
13. **Marca de lectura.** Salvo las dos páginas de Learn, todo es [S]; las afirmaciones críticas (versiones, sintaxis literal) conviene releerlas contra la página completa antes de pasarlas a "vigente".
