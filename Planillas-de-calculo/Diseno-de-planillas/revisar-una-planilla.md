---
resumen: >-
  Revisar una planilla es recorrer sus fórmulas y probar sus resultados antes de confiar en ellos:
  seguir de dónde sale cada número, poner controles que avisen cuando algo no cuadra, cambiar
  entradas para ver si las salidas se mueven como se espera y, sobre todo, que otra persona la lea
  celda por celda.
estado: vigente
estabilidad: semi
fuentes:
  - "ICAEW, Financial Modelling Code (2018, ed. 2024), principios #17 y #18: https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx"
  - "Raymond R. Panko, Spreadsheet Errors: What We Know. What We Think We Can Do, EuSpRIG 2000: https://arxiv.org/pdf/0802.3457"
  - "Raymond R. Panko, What We Don't Know About Spreadsheet Errors Today, EuSpRIG 2015: https://arxiv.org/pdf/1602.02601"
  - "Microsoft, Display the relationships between formulas and cells (según resumen): https://support.microsoft.com/en-us/office/display-the-relationships-between-formulas-and-cells-a59bef2b-3701-46bf-8ff1-d3518771d507"
  - "Microsoft, Remove or allow a circular reference (según resumen): https://support.microsoft.com/en-us/office/remove-or-allow-a-circular-reference-8540bd0f-6e97-4483-bcf7-1b49cd50d123"
  - "Microsoft, Analyze a workbook with Spreadsheet Inquire (según resumen): https://support.microsoft.com/en-us/office/analyze-a-workbook-with-spreadsheet-inquire-5991e8fa-f1c1-401a-ae3f-469384ae3e3b"
  - "Google, Ver el historial de versiones (según resumen): https://support.google.com/docs/answer/190843"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
aliases: [auditar una planilla, spreadsheet review, auditoría de fórmulas, formula auditing, rastrear precedentes, trace precedents, revisión por pares, Spreadsheet Inquire]
creado: 2026-11-27
revisado: 2026-11-27
---

# Revisar una planilla

Revisar una planilla es recorrer sus fórmulas y probar sus resultados antes de confiar en ellos: seguir de dónde sale cada número, poner controles que avisen cuando algo no cuadra, cambiar entradas para ver si las salidas se mueven como se espera y, sobre todo, que otra persona la lea celda por celda.

Hace falta porque quien arma una planilla subestima sus propios errores: en un experimento con estudiantes que cita Panko (Panko y Featherman 1999), quienes las habían hecho estimaron una probabilidad de error mediana de 10 %, y el 86 % había cometido alguno. Las cifras y los tipos de error están en [errores en planillas](errores-en-planillas.md). Revisar es más fácil si la planilla separa [entradas, cálculo y salidas](entradas-calculo-salidas.md): los supuestos se miran una vez y las fórmulas se leen en una sola dirección.

## Lo único que mostró resultados: leer celda por celda entre varios

Panko escribió en 2000 que "only one technique, cell-by-cell code inspection, has been demonstrated to be effective". Es la misma técnica que se usa para revisar código: alguien que no armó la planilla mira cada fórmula y pregunta qué hace y si debería hacer eso. Ni así se encuentra todo. Según Panko (2000), un revisor solo encuentra "about half" de los errores; la detección se acerca al 90 % solo para errores mecánicos en fórmulas cortas, y para errores lógicos, fórmulas largas y omisiones es "far lower". En 2015 da 60 % de promedio en nueve experimentos, y en uno propio, 63 % para individuos y 83 % para equipos de tres: por eso conviene que revisen varios.

Trabajar de a varios también reduce errores al armar. En un experimento de laboratorio de Panko y Halverson, con una tarea chica, la tasa de error por celda fue 5,6 % para quienes trabajaron solos, 3,8 % en parejas y 1,9 % en grupos de cuatro. Es otra cifra que el 3,9 % de [errores en planillas](errores-en-planillas.md), que promedia 14 experimentos de personas trabajando solas.

> [!IMPORTANT]
> Esas cifras salen de experimentos con estudiantes sobre planillas de 25 a 50 celdas. Panko las presenta así, y Powell, Baker y Lawson (2008) advierten que trasladar tasas de laboratorio a planillas reales pide cuidado. Lo que sí se sostiene es la dirección: una segunda persona encuentra errores que quien la hizo no ve.

En un negocio chico, una revisión por pares se arma así:

1. Elegí a alguien que no haya armado la planilla y que entienda el negocio (sabe cuánto debería dar el costo de una docena de facturas).
2. Revisen juntos primero la hoja de supuestos: ¿cada valor está una sola vez y está al día?
3. Recorran las fórmulas de la hoja de cálculo fila por fila. Una fila con una fórmula distinta a sus vecinas se mira dos veces.
4. Busquen celdas con un número tipeado donde debería haber una fórmula.
5. Preguntá qué falta: los errores de omisión no tienen una celda donde mirar.

## Controles que viven adentro de la planilla

El ICAEW pide en el principio #17 "Include checks": indicadores visibles que se activan cuando una entrada o una salida cae fuera de lo esperado. En una planilla de ventas por mes, un control típico es una celda que compara la suma de las ventas por producto con la suma de las ventas por mes; si no dan lo mismo, muestra "NO CUADRA" en rojo. En la de stock, una celda que avisa si algún producto quedó con stock negativo.

La diferencia con la revisión por pares es que el control queda: avisa cada vez que alguien cambia algo, no solo el día que se revisó.

## Probar cambiando entradas

El principio #18 del ICAEW es "Review and test your models": cambiar entradas y comparar salidas. En la planilla de costos, se duplica el precio de un insumo y se mira si el costo de los productos que lo usan sube en la proporción esperada, y si los que no lo usan quedan igual. Un producto que no se mueve cuando debería es una fórmula que no apunta a Supuestos.

> [!NOTE] Sin fuente todavía: fuera de los principios #17 y #18 del ICAEW, no se encontró una fuente específica sobre pruebas de cuadre en planillas.

## Las herramientas de Excel

Excel trae herramientas para recorrer una planilla en la pestaña Fórmulas, grupo Auditoría. Ayudan a encontrar dónde mirar; no deciden si una fórmula está bien pensada.

- **Rastrear precedentes y rastrear dependientes.** Dibujan flechas desde las celdas que alimentan una fórmula, o hacia las que usan esa celda. Según Microsoft, las flechas son azules si no hay error y rojas si señalan una celda que causa un error. No rastrean cuadros de texto, gráficos incrustados, imágenes, tablas dinámicas ni constantes con nombre.
- **Comprobación de errores y referencias circulares.** Desde Fórmulas, Comprobación de errores, se recorren las celdas con error y se ubican las referencias circulares, las fórmulas que terminan dependiendo de sí mismas. Qué significa cada error está en [errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md).
- **Spreadsheet Inquire.** Es un complemento solo para Excel en Windows, en Microsoft 365 Apps para empresas y ediciones equivalentes; se habilita en Opciones, Complementos, Complementos COM. Trae un análisis del libro, diagramas de relaciones entre hojas y libros, y Compare Files, que compara dos versiones de un libro celda por celda, cambios de VBA incluidos. Es la herramienta para saber qué cambió entre la planilla del mes pasado y la de este.

> [!NOTE] Sin fuente todavía: las páginas oficiales de Mostrar fórmulas y Evaluar fórmula, que permiten ver todas las fórmulas a la vez y calcular una fórmula paso por paso.

## Qué hay en Google Sheets

Sheets no tiene, en lo que se investigó, un equivalente documentado de rastrear precedentes ni de Spreadsheet Inquire. Lo que sí trae es el historial de versiones: propietarios y editores pueden ver las versiones anteriores de la planilla y restaurar una. Restaurar borra el historial celda por celda previo a esa restauración, y Google sugiere hacer una copia si se necesita conservarlo. El detalle está en [compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md).

> [!NOTE] Sin fuente todavía: qué herramientas de auditoría de fórmulas trae Google Sheets (mostrar fórmulas, ver qué celdas usa una fórmula). La investigación no encontró la página oficial.

Los controles del ICAEW (#17) y las pruebas cambiando entradas (#18) funcionan igual en las dos aplicaciones, porque son fórmulas y hábitos, no funciones de una herramienta. En Sheets son la principal forma de revisión.
