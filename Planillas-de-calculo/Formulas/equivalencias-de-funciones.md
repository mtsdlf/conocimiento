---
resumen: >-
  Tabla de las funciones de este tema con su nombre en castellano y en inglés, las versiones de
  Excel en que Microsoft dice que existen y su nombre y fecha de llegada en Google Sheets, copiada
  de las páginas de soporte el 2026-11-27.
estado: borrador
estabilidad: volatil
fuentes:
  - "Microsoft, páginas de soporte de cada función en es-es (lista «Se aplica a»): https://support.microsoft.com/es-es/excel/functions/<nombre-en-inglés>-function"
  - "Microsoft, XLOOKUP function: https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929"
  - "Microsoft, Función SI.CONJUNTO: https://support.microsoft.com/es-es/office/si-conjunto-función-si-conjunto-36329a26-37b2-467c-972b-4a39bd951d45 (según un resumen)"
  - "Microsoft, Función SUMAR.SI.CONJUNTO: https://support.microsoft.com/es-es/office/sumar-si-conjunto-función-sumar-si-conjunto-c9e748f5-7ea7-455d-9406-611cebce642b (según un resumen)"
  - "Microsoft, Función SIFECHA: https://support.microsoft.com/es-es/office/sifecha-función-sifecha-25dba1a4-2812-480b-84dd-8b32a451b35c (según un resumen)"
  - "Microsoft, Función DIVIDIRTEXTO: https://support.microsoft.com/es-es/office/dividirtexto-función-dividirtexto-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7 (según un resumen)"
  - "Microsoft, Función FILTRAR: https://support.microsoft.com/es-es/office/filtrar-función-filtrar-f4f7cb66-82eb-4767-8f7c-4877ad80c759 (según un resumen)"
  - "Microsoft, Función LET: https://support.microsoft.com/es-es/office/let-función-let-34842dd8-b92b-4d3f-b325-b8b8f9908999 (según un resumen)"
  - "Microsoft, LAMBDA function: https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67 (según un resumen)"
  - "Exceljet, XLOOKUP function: https://exceljet.net/functions/xlookup-function (según un resumen)"
  - "Google, Lista de funciones de Hojas de cálculo de Google: https://support.google.com/docs/table/25273?hl=es"
  - "Google Workspace Updates, 2022-08-24: https://workspaceupdates.googleblog.com/2022/08/named-functions-google-sheets.html"
  - "Google Workspace Updates, 2023-02-01: https://workspaceupdates.googleblog.com/2023/01/google-sheets-powerful-functions-advanced-analysis.html"
  - "Google, QUERY: https://support.google.com/docs/answer/3093343; IMPORTRANGE: https://support.google.com/docs/answer/3093340; ARRAYFORMULA: https://support.google.com/docs/answer/3093275"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, sección 3"
aliases: [equivalencias de funciones, nombres de funciones en inglés, function names Spanish English, compatibilidad de funciones]
creado: 2026-11-27
revisado:
---

# Equivalencias de funciones

Tabla de las funciones de este tema con su nombre en castellano y en inglés, las versiones de
Excel en que Microsoft dice que existen y su nombre y fecha de llegada en Google Sheets, copiada
de las páginas de soporte el 2026-11-27.

Sirve a todas las notas de [Fórmulas](formulas.md), y en
especial a [funciones de búsqueda](funciones-de-busqueda.md) y [matrices dinámicas](matrices-dinamicas.md),
donde la versión decide qué función usar.

Ningún fabricante publica esta tabla: se arma desde la página de cada función. La fuente viva de
Excel es la lista «Se aplica a» al pie de cada página de soporte de Microsoft; la de Sheets, la
[lista de funciones de Google](https://support.google.com/docs/table/25273?hl=es) y los anuncios
de [Google Workspace Updates](https://workspaceupdates.googleblog.com/). Al actualizarla, mirá esas
dos y las fechas.

## Cómo leer la columna de Excel

- **Todas** quiere decir que la página lista la lista completa, copiada así: "Excel para Microsoft
  365, Excel para Microsoft 365 para Mac, Excel para la Web, Excel 2024, Excel 2024 para Mac,
  Excel 2021, Excel 2021 para Mac, Excel 2019, Excel 2016". Es la versión más vieja que figura en
  las páginas; no dice que la función no exista antes.
- Cuando dice **desde 2019** o **desde 2021**, las versiones anteriores no figuran en la página:
  un archivo con esa función abierto en una versión vieja da #¿NOMBRE? al recalcular.
- Las celdas con "(resumen)" salen de un resumen de la página y no de su texto.

## Tabla

| Castellano | Inglés | Excel | Nombre en Sheets (castellano) | En Sheets desde |
|---|---|---|---|---|
| SI | IF | todas | SI | — |
| Y | AND | todas | Y | — |
| O | OR | todas | O | — |
| SI.CONJUNTO | IFS | desde 2019 (resumen) | SI.CONJUNTO | — |
| SI.ERROR | IFERROR | todas | SI.ERROR (segundo argumento opcional) | — |
| SI.ND | IFNA | todas | SI.ND | — |
| BUSCARV | VLOOKUP | todas (resumen) | sin verificar | — |
| INDICE / COINCIDIR | INDEX / MATCH | sin verificar | sin verificar | — |
| BUSCARX | XLOOKUP | discrepancia (ver abajo) | sin verificar | anuncio del 2022-08-24 |
| SUMAR.SI.CONJUNTO | SUMIFS | todas (resumen) | sin verificar | — |
| CONTAR.SI.CONJUNTO | COUNTIFS | todas | CONTAR.SI.CONJUNTO | — |
| IZQUIERDA, DERECHA, EXTRAE, LARGO | LEFT, RIGHT, MID, LEN | todas | iguales | — |
| ESPACIOS | TRIM | todas | ESPACIOS | — |
| LIMPIAR | CLEAN | todas | LIMPIAR | — |
| CONCAT | CONCAT | discrepancia (ver abajo) | sin verificar | — |
| UNIRCADENAS | TEXTJOIN | desde 2019 | UNIRCADENAS | — |
| TEXTO | TEXT | todas | TEXTO | — |
| VALOR | VALUE | todas | VALOR | — |
| DIVIDIRTEXTO | TEXTSPLIT | solo Microsoft 365 y 2024 (resumen) | no figura; Sheets usa SPLIT | — |
| FECHA | DATE | todas | sin verificar | — |
| HOY | TODAY | todas | HOY | — |
| AHORA | NOW | todas | sin verificar | — |
| DIAS.LAB | NETWORKDAYS | todas | DIAS.LAB | — |
| FIN.MES | EOMONTH | todas | FIN.MES | — |
| FECHA.MES | EDATE | todas | FECHA.MES | — |
| MES, AÑO | MONTH, YEAR | todas | sin verificar | — |
| SIFECHA | DATEDIF | todas (resumen), por compatibilidad con Lotus 1-2-3 | sin verificar | — |
| FILTRAR | FILTER | desde 2021 (resumen) | sin verificar | sin fuente |
| ORDENAR | SORT | desde 2021 | SORT (otros argumentos) | sin fuente |
| UNICOS | UNIQUE | desde 2021 | UNIQUE | sin fuente |
| SECUENCIA | SEQUENCE | desde 2021 | SECUENCIA | sin fuente |
| LET | LET | desde 2021 (resumen) | sin verificar | anuncio del 2023-02-01, despliegue previsto completo al 2023-03-14 |
| LAMBDA (y MAP, REDUCE, SCAN, BYROW, BYCOL, MAKEARRAY) | LAMBDA | solo Microsoft 365 y 2024 (resumen); auxiliares sin verificar | sin verificar | anuncio del 2022-08-24 |
| — | QUERY | no existe; lo más parecido es Power Query | QUERY | sin fuente |
| — | IMPORTRANGE | no existe; Excel usa vínculos a otro libro | IMPORTRANGE | sin fuente |
| — | ARRAYFORMULA | no hace falta: las fórmulas se desbordan solas | ARRAYFORMULA | sin fuente |

La llegada de XLOOKUP y LAMBDA a Sheets sale del anuncio de Google Workspace del 2022-08-24, con un
despliegue extendido previsto completo al 2022-09-26. Las funciones que Sheets tuvo desde siempre
llevan "—".

## Las dos discrepancias de Microsoft

> [!IMPORTANT]
> **BUSCARX (XLOOKUP).** La lista "Applies to" de la página de Microsoft incluye "Excel 2019 Excel
> 2016", y la misma página dice: "XLOOKUP is not available in Excel 2016 and Excel 2019. However,
> you may come across a situation of using a workbook in Excel 2016 or Excel 2019 with the XLOOKUP
> function in it, if it was created by someone else using a newer version of Excel." Exceljet la
> da para "Excel 2021+ and Excel 365". La nota es la que describe el comportamiento; la lista
> parece incluir esas versiones porque el archivo se puede abrir en ellas (esto es inferencia).
> En la práctica: BUSCARX desde Excel 2021 y en Microsoft 365.
>
> **CONCAT.** La página la lista desde Excel 2016, pero su nota dice que está "disponible en
> Windows o Mac si tiene Office 2019 o si tiene una suscripción a Office 365".

## Volátiles, con sus nombres

Las funciones volátiles se recalculan siempre (ver
[errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md#el-recálculo-y-las-funciones-volátiles),
donde están las tres listas que no coinciden). Sus nombres:

| Castellano | Inglés |
|---|---|
| AHORA | NOW |
| HOY | TODAY |
| DESREF | OFFSET |
| INDIRECTO | INDIRECT |
| CELDA | CELL |
| INFO | INFO |
| ALEATORIO | RAND |
| ALEATORIO.ENTRE | RANDBETWEEN |

> [!NOTE]
> Sin fuente todavía: los nombres en castellano de DESREF, INDIRECTO, CELDA, ALEATORIO y
> ALEATORIO.ENTRE, de BUSCARV, INDICE y COINCIDIR en Sheets, y la página de Microsoft de INDICE y
> COINCIDIR con sus versiones. Tampoco se verificó desde cuándo existen FILTER, SORT, UNIQUE,
> SEQUENCE, QUERY, IMPORTRANGE y ARRAYFORMULA en Sheets.
