---
resumen: >-
  Lo transversal del tema Planillas de cálculo: de dónde salen las planillas (de VisiCalc en 1979 a
  Google Sheets en 2006), los enfoques que compiten para armarlas y usarlas, las ideas que circulan y
  no se sostienen, la bibliografía y el glosario.
estado: borrador
estabilidad: estable
fuentes:
  - "Computer History Museum, Software Arts y VisiCalc (según resumen del buscador): https://www.computerhistory.org/collections/catalog/102738286"
  - "Wikipedia, Microsoft Excel (secundaria; leída en parte): https://en.wikipedia.org/wiki/Microsoft_Excel"
  - "Wikipedia, Google Sheets (secundaria): https://en.wikipedia.org/wiki/Google_Sheets"
  - "Microsoft Learn, Excel incorrectly assumes that the year 1900 is a leap year (2026-04-15): https://learn.microsoft.com/en-us/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year"
  - "Microsoft Excel blog, Announcing XLOOKUP (2019-08-28): https://techcommunity.microsoft.com/blog/excelblog/announcing-xlookup/811376"
  - "Microsoft Excel blog, Preview of Dynamic Arrays in Excel (2018-09; actualizada 2020-07-01): https://techcommunity.microsoft.com/blog/excelblog/preview-of-dynamic-arrays-in-excel/252944"
  - "Microsoft, XLOOKUP function: https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929"
  - "Google Workspace Updates, funciones con nombre, LAMBDA y XLOOKUP (2022-08-24): https://workspaceupdates.googleblog.com/2022/08/named-functions-google-sheets.html"
  - "Exceljet, INDEX function (practicante): https://exceljet.net/functions/index-function"
  - "ICAEW, Financial Modelling Code (2018, ed. 2024): https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx"
  - "FAST Standard Organisation, The FAST Standard: https://www.fast-standard.org/the-fast-standard/"
  - "Raymond R. Panko, What We Don't Know About Spreadsheet Errors Today, EuSpRIG 2015: https://arxiv.org/pdf/1602.02601"
  - "Planillas-de-calculo/.investigacion/posicion-contraria-y-fundamentos.md"
aliases: [historia de las planillas, spreadsheet history, VisiCalc, Lotus 1-2-3]
creado: 2026-11-27
revisado:
---

# Fundamentos de planillas

Lo transversal del tema Planillas de cálculo: de dónde salen las planillas (de VisiCalc en 1979 a Google Sheets en 2006), los enfoques que compiten para armarlas y usarlas, las ideas que circulan y no se sostienen, la bibliografía y el glosario.

No es una parte de la planilla, como las verticales de [planillas de cálculo](../planillas-de-calculo.md), sino lo que cruza a todas.

- [Glosario de planillas](glosario-de-planillas.md) — los términos del tema, de libro y celda a matriz dinámica y Power Query, cada uno enlazado a la nota que lo trata.
- [Fuentes de planillas](fuentes-de-planillas.md) — la bibliografía: qué leer, qué parte y en qué fijarse.

## De VisiCalc a Google Sheets

La planilla electrónica nació como programa para computadoras personales. Según el Computer History Museum (visto por resumen), Dan Bricklin y Bob Frankston fundaron Software Arts en 1979 para hacer VisiCalc, que vendió alrededor de un millón de copias en su vida. Lotus 1-2-3 dominaba el mercado hacia 1983, según Wikipedia.

Excel nació para Macintosh: Microsoft lo anunció el 2 de mayo de 1985 y lo lanzó el 30 de septiembre de 1985; Excel 2.0 para Windows salió el 19 de noviembre de 1987 (fechas de Wikipedia). De esa época viene una herencia que sigue viva: Lotus 1-2-3 suponía que 1900 era bisiesto, y Excel copió el error para poder intercambiar fechas con Lotus. Microsoft dice que corregirlo es posible, pero "the disadvantages of doing so outweigh the advantages". El efecto práctico es mínimo y está en [tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md).

Google Sheets llegó en 2006. Wikipedia da dos fechas para el lanzamiento, el 9 de marzo (en su cuadro) y una prueba limitada desde el 6 de junio, con beta abierta el 11 de octubre de 2006; el producto viene de la compra de XL2Web, de 2Web Technologies, ese año, y se llama Google Sheets desde octubre de 2012. Su diferencia de origen, vivir en el navegador, explica por qué la coautoría fue siempre natural ahí, como cuenta [compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md).

La última gran renovación de las fórmulas fue la de las matrices dinámicas. Microsoft las presentó en septiembre de 2018 y, según la actualización del mismo anuncio, al 2020-07-01 estaban en Office 365 en todas las plataformas. BUSCARX (XLOOKUP) se anunció el 2019-08-28 para quienes prueban versiones previas, y LAMBDA llegó el 3 de diciembre de 2020, según Wikipedia. Sheets sumó XLOOKUP y LAMBDA en el anuncio del 2022-08-24. Qué hacen está en [matrices dinámicas](../Formulas/matrices-dinamicas.md) y [funciones de búsqueda](../Formulas/funciones-de-busqueda.md).

> [!NOTE] Sin fuente todavía: una fuente primaria sobre VisiCalc (el sitio de Bricklin falló por certificado) y sobre Lotus 1-2-3, fuera de Wikipedia. La discrepancia entre las dos fechas de lanzamiento de Google Sheets en 2006 no se resolvió.

## Enfoques que compiten

### FAST y el Code del ICAEW se complementan

Hay dos referencias para armar planillas que duren. El *Financial Modelling Code* del ICAEW da principios (separar entradas, cálculos y salidas; no esconder números en las fórmulas; fórmulas consistentes) y, según un resumen de su presentación, "is not intended to be a tick-box compliance tool; rather it is a framework". El FAST Standard ("Flexible, Appropriate, Structured & Transparent") detalla reglas de construcción, con "Rigorous consistency in layout and organisation" y "simple, clear formulas". Las fuentes los presentan como complementarios, no rivales: ICAEW dice qué lograr y FAST cómo construirlo. Cómo se aplica el Code a una planilla de costos está en [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md).

Las reglas concretas de FAST están en su PDF, que la investigación no leyó; acá no se le atribuye ninguna. Un tercer estándar que a veces se nombra, SMART, no apareció en ninguna búsqueda.

### Fórmulas a la vista o herramientas que esconden los pasos

FAST pide fórmulas simples y transparentes, que cualquiera pueda seguir celda por celda. [Power Query](../Datos-en-la-planilla/power-query.md) y la [tabla dinámica](../Analisis/tabla-dinamica.md) hacen lo contrario: resuelven en pocos clics lo que llevaría decenas de fórmulas, pero los pasos quedan adentro de la herramienta y no en celdas que se puedan rastrear. Una tabla dinámica, además, trabaja sobre una copia de los datos que hay que actualizar a mano, y las herramientas de rastreo de Excel no la siguen, como cuenta [revisar una planilla](../Diseno-de-planillas/revisar-una-planilla.md).

> [!NOTE] Sin fuente todavía: la investigación no encontró una crítica publicada a Power Query ni a las tablas dinámicas desde el lado de la auditoría. La tensión de este apartado es inferencia propia a partir de la doctrina de FAST y de lo que documenta Microsoft.

### BUSCARX o INDICE+COINCIDIR

BUSCARX (XLOOKUP) busca en cualquier dirección y da coincidencia exacta por defecto, y Microsoft la recomienda sobre BUSCARV. El argumento a favor de INDICE+COINCIDIR (INDEX+MATCH) es la compatibilidad: según Microsoft, un libro con BUSCARX abierto en una versión vieja muestra los resultados guardados, pero si se vuelve a escribir la fórmula da `#NAME?`. La propia página de Microsoft se contradice sobre si Excel 2016 y 2019 la tienen (la lista de versiones las incluye y una nota dice que no); Exceljet la da desde Excel 2021. Google Sheets la tiene desde agosto de 2022. INDICE+COINCIDIR funciona en todas las versiones y, según Exceljet, cubre la búsqueda a la izquierda, en dos direcciones y con varios criterios. La decisión depende de quién va a abrir el archivo; el detalle está en [funciones de búsqueda](../Formulas/funciones-de-busqueda.md).

## Ideas que circulan y no se sostienen

| Lo que se dice | Lo que dicen las fuentes | Dónde está |
|---|---|---|
| «El 88 % de las planillas tiene errores» | Sin fuente rastreable. Panko da 94 % de 85 planillas auditadas, sobre muestras no aleatorias | [Errores en planillas](../Diseno-de-planillas/errores-en-planillas.md) |
| «Las planillas son la fuente de los errores; hay que sacarlas» | Panko: "spreadsheet programs are not error-prone. People are error prone." Lo que falta es probarlas | [Errores en planillas](../Diseno-de-planillas/errores-en-planillas.md) |
| «Microsoft bloquea las macros de internet desde 2022» | Solo en Office para Windows; no en Mac, móviles ni la web | [Macros](../Automatizar-y-compartir/macros.md) |
| «Google Sheets admite 10 millones de celdas» | 20 millones desde septiembre de 2026 | [Ficha de aplicaciones](../aplicaciones-de-planillas.md) |
| «Proteger una hoja en Sheets protege los datos» | Google: "Protection isn't a security measure" | [Compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md) |
| «Cuando crezcas, pasá a una base» | La evidencia es de vendedores; mudarse temprano tiene costos | [Cuándo pasar a una base](../cuando-pasar-a-una-base.md) |
