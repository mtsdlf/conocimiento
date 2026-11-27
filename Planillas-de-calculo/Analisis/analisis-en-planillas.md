---
resumen: >-
  El análisis en planillas es la parte que convierte una lista de datos en respuestas: resúmenes por
  categoría y período con tablas dinámicas, gráficos que muestran la forma de los números y
  escenarios que prueban qué pasaría si cambia un supuesto.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Create a PivotTable to analyze worksheet data: https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576"
  - "Microsoft, Introduction to What-If Analysis: https://support.microsoft.com/en-US/excel/introduction-to-what-if-analysis"
  - "Microsoft Learn, Exam MO-211: Microsoft Excel Expert (actualizada 2026-07-01): https://learn.microsoft.com/certifications/exams/mo-211"
  - "Planillas-de-calculo/.investigacion/datos-y-analisis.md (2026-11-27)"
aliases: [análisis, análisis de datos en Excel, análisis en Google Sheets, spreadsheet analysis]
creado: 2026-11-27
revisado:
---

# Análisis en planillas

El análisis en planillas es la parte que convierte una lista de datos en respuestas: resúmenes por
categoría y período con tablas dinámicas, gráficos que muestran la forma de los números y
escenarios que prueban qué pasaría si cambia un supuesto.

Recibe de [Datos en la planilla](../Datos-en-la-planilla/datos-en-la-planilla.md) la materia prima,
que tiene que estar [ordenada](../Datos-en-la-planilla/datos-ordenados.md) para que el análisis
funcione sin preparación. Las [fórmulas](../Formulas/formulas.md) son la otra forma de resumir: lo
que una tabla dinámica muestra con arrastrar campos, una suma con condiciones lo deja fijo en una
celda. Lo general del análisis (estadística, qué gráfico elegir, tableros) está en el tema
[Datos](../../Datos/datos.md); acá va lo propio de la planilla.

## Tres preguntas, tres herramientas

Cada componente contesta un tipo de pregunta distinto sobre los mismos datos:

| Pregunta | Ejemplo | Herramienta |
|---|---|---|
| ¿Cuánto, por qué categoría, en qué período? | ventas por mes y por producto | [tabla dinámica](tabla-dinamica.md) |
| ¿Qué forma tienen los números? | si las ventas crecen, caen o son estacionales | [gráficos en la planilla](graficos-en-la-planilla.md) |
| ¿Qué pasaría si...? | a qué precio se llega al margen buscado | [análisis de escenarios](analisis-de-escenarios.md) |

Las dos primeras miran datos que ya pasaron; la tercera mira un modelo hacia adelante. Por eso los
escenarios dependen más del [diseño de la planilla](../Diseno-de-planillas/diseno-de-planillas.md)
que de los datos: necesitan supuestos separados en celdas de entrada, como cuenta
[entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md).

Microsoft agrupa las dos primeras: su examen de Excel experto (MO-211) las pone en un solo dominio,
"Manage advanced charts and tables", con un peso de 25 a 30 %. El gráfico dinámico es el puente
entre ambas: un gráfico que se arma sobre una tabla dinámica y cambia con ella.

## Tabla dinámica o fórmulas

La duda más frecuente de la vertical es si resumir con una tabla dinámica o con
[sumar y contar con condiciones](../Formulas/sumar-y-contar-con-condiciones.md). La tabla dinámica
es más rápida para explorar y no necesita escribir nada, pero trabaja sobre una copia de los datos
y no se actualiza sola en Excel. Las fórmulas se recalculan solas y quedan a la vista para quien
revisa, pero hay que escribirlas para cada corte. Como criterio práctico, que es una inferencia:
tabla dinámica para mirar y preguntar; fórmulas para un informe fijo que otro va a leer todos los
meses.

## Dónde se separan Excel y Sheets

Las dos aplicaciones tienen tablas dinámicas y gráficos con las mismas ideas y detalles distintos.
La diferencia grande está en los escenarios: Excel trae Buscar objetivo, Tabla de datos,
Administrador de escenarios y el complemento Solver; Google Sheets no tiene ninguno como función
propia y depende de complementos, varios de terceros, que pueden mandar los datos fuera de la hoja.

> [!IMPORTANT]
> "Tabla" nombra tres objetos distintos en el tema: la
> [tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md), donde se guardan los datos; la
> [tabla dinámica](tabla-dinamica.md), que los resume; y la tabla de datos del
> [análisis de escenarios](analisis-de-escenarios.md), que muestra resultados para varios valores de
> una entrada. Las notas usan siempre el nombre completo.

## Qué hay adentro del análisis

- [Tabla dinámica](tabla-dinamica.md) — resumir ventas, stock o clientes por categoría y período
  arrastrando campos; cómo se actualiza y qué cambia en Sheets.
- [Gráficos en la planilla](graficos-en-la-planilla.md) — gráficos desde un rango, gráficos dinámicos
  y minigráficos dentro de una celda, en Excel y en Sheets.
- [Análisis de escenarios](analisis-de-escenarios.md) — Buscar objetivo, Tabla de datos,
  Administrador de escenarios y Solver, con sus límites, y lo que hay en Sheets.
