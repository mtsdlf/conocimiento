---
resumen: >-
  Los gráficos en la planilla son las tres formas de dibujar datos dentro de Excel o Google Sheets:
  el gráfico que se arma desde un rango, el gráfico dinámico que sigue a una tabla dinámica y el
  minigráfico que entra en una sola celda.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft, Use sparklines to show data trends: https://support.microsoft.com/en-us/office/use-sparklines-to-show-data-trends-1474e169-008c-4783-926b-5c60e620f5ca"
  - "Microsoft, Create a PivotChart: https://support.microsoft.com/en-us/topic/c1b1e057-6990-4c38-b52b-8255538e7b1c"
  - "Google, SPARKLINE: https://support.google.com/docs/answer/3093289"
  - "Google, Sparkline charts: https://support.google.com/docs/answer/9146780"
  - "Google Workspace Updates, New sparkline options in Google Sheets (2014-12): https://workspaceupdates.googleblog.com/2014/12/new-sparkline-options-in-google-sheets.html"
  - "Microsoft Learn, Exam MO-211: Microsoft Excel Expert: https://learn.microsoft.com/certifications/exams/mo-211"
aliases: [gráficos, charts, gráfico dinámico, PivotChart, minigráfico, sparkline, SPARKLINE, gráficos en Excel, gráficos en Google Sheets]
creado: 2026-11-27
revisado: 2026-11-27
---

# Gráficos en la planilla

Los gráficos en la planilla son las tres formas de dibujar datos dentro de Excel o Google Sheets:
el gráfico que se arma desde un rango, el gráfico dinámico que sigue a una tabla dinámica y el
minigráfico que entra en una sola celda.

Qué gráfico conviene para cada pregunta (líneas para una tendencia, barras para comparar) es un tema
general de visualización y está en [Datos](../../Datos/datos.md). Acá va cómo se arma cada tipo
dentro de la planilla y en qué difieren las dos aplicaciones.

## Tres gráficos según de dónde salen los datos

| Tipo | Lee de | Sirve para |
|---|---|---|
| Gráfico de un rango | celdas de la hoja | un resumen fijo: ventas de los últimos 12 meses |
| Gráfico dinámico | una [tabla dinámica](tabla-dinamica.md) | explorar: cambiar de producto a rubro y que el gráfico siga |
| Minigráfico | una fila o columna de celdas | ver la tendencia de cada producto al lado de sus números |

El gráfico de un rango es el común: se seleccionan las celdas y se inserta. Conviene que lea de una
[tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md), porque así toma las filas nuevas.
Si lee de un rango fijo, el mes que se agrega abajo no aparece.

## El gráfico dinámico sigue a la tabla dinámica

Un gráfico dinámico (PivotChart) dibuja lo que muestra una tabla dinámica y cambia con ella: si se
filtra la tabla dinámica o se usa una segmentación, según Microsoft, "the chart will also be
filtered". Es la forma de tener un gráfico de ventas por mes que pasa a mostrar un solo rubro con un
clic.

Cómo se crea depende de la plataforma, según Microsoft:

- **Excel para Windows**: Insert > PivotChart, desde una celda de los datos; crea el gráfico sin
  armar antes la tabla dinámica, y los campos se eligen en el panel.
- **Excel para Mac**: "you need to create a PivotTable first, and then insert a chart". Solo
  funcionan gráficos de columnas, líneas, torta y radar: "other types of charts do not work with
  PivotTables at this time."
- **Excel para la web**: también hay que crear antes la tabla dinámica y después insertar un gráfico
  desde la pestaña Insert.

El examen de Excel experto de Microsoft (MO-211) tiene un dominio "Manage advanced charts and
tables" (25 a 30 % del examen). Solo se conocen su nombre y su peso; que incluya los gráficos
dinámicos es inferencia.

> [!NOTE]
> Sin fuente todavía: cómo se hace un gráfico que siga a una tabla dinámica en Google Sheets.

## Minigráficos: un gráfico en una celda

Un minigráfico muestra la tendencia de una fila de números en el espacio de una celda. En una lista
de productos con las ventas de cada mes, una columna de minigráficos al final deja ver de un vistazo
cuáles crecen y cuáles caen, sin un gráfico por producto.

En Excel se llaman Sparklines. Microsoft los define así: "A sparkline is a tiny chart in a worksheet
cell that provides a visual representation of data." Hay tres tipos: Line, Column y Win/Loss. Se
crean desde una celda vacía al final de la fila de datos, con Insert y el tipo de minigráfico; se
eligen las celdas de la fila y se arrastra el controlador para repetirlo en las filas de abajo.
Microsoft aconseja: "For best impact, position a sparkline near its data."

En Google Sheets el minigráfico es una función, no un objeto: `SPARKLINE(data, [options])`, que
"Creates a miniature chart contained within a single cell". Los tipos se eligen con la opción
`"charttype"`: `"line"` (por defecto), `"bar"`, `"column"` y `"winloss"`. Con las ventas de enero a
diciembre en B2:M2, `=SPARKLINE(B2:M2)` dibuja una línea en la celda. Al ser una fórmula, se copia
hacia abajo como cualquier otra y se recalcula sola.

> [!IMPORTANT]
> Google se contradice sobre los minigráficos en Sheets. La página de la función SPARKLINE la
> describe como vigente, con su sintaxis y sus tipos. La página "Sparkline charts" dice: "You can no
> longer use sparkline charts in Google Sheets", agrega que los viejos pueden mostrarse como gráfico
> de líneas y recomienda usar uno. Una lectura posible, sin confirmar, es que la segunda habla de un
> tipo de gráfico del editor de gráficos y no de la función. No está resuelto: conviene probar la
> función en una hoja antes de construir sobre ella.

> [!NOTE]
> Sin fuente todavía: cómo se escriben las opciones de SPARKLINE en una hoja configurada en
> castellano, y qué pasa con los minigráficos de Excel cuando cambian los datos o hay celdas vacías.

## Lo que se rompe al dibujar

Un gráfico de planilla falla sobre todo por los datos que lee: un rango fijo que no toma los meses
nuevos, una tabla dinámica que no se actualizó ([tabla dinámica](tabla-dinamica.md)), o fechas
guardadas como texto que el gráfico ordena alfabéticamente
([tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md)).

> [!NOTE]
> Sin fuente todavía: errores de lectura propios de los gráficos de planilla, como el eje vertical
> que no empieza en cero o la torta con muchas porciones; lo general de elegir y leer un gráfico va al
> tema [Datos](../../Datos/datos.md).

## Qué leer

Para Excel, las páginas de Microsoft "Use sparklines to show data trends" y "Create a PivotChart",
que separan Windows, Mac y web. Para Sheets, la página de la función SPARKLINE, leída con la
advertencia de la contradicción de arriba.
