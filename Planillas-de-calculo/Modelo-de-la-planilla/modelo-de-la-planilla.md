---
resumen: >-
  El modelo de la planilla es cómo piensa la herramienta: una grilla de celdas que guardan un valor
  o una fórmula, fórmulas que apuntan a otras celdas por su dirección, y un motor que recalcula lo
  que depende de una celda cuando esa celda cambia. Casi todo error de una planilla se explica con
  esas tres piezas.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft Learn, Excel Recalculation: https://learn.microsoft.com/en-us/office/client-developer/excel/excel-recalculation"
  - "Google, Ajustes de hoja de cálculo (configuración regional y cálculo): https://support.google.com/docs/answer/58515 (según un resumen)"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, sección 1"
aliases: [modelo de celdas, spreadsheet model, cómo funciona una planilla]
creado: 2026-11-27
revisado: 2026-11-27
---

# Modelo de la planilla

El modelo de la planilla es cómo piensa la herramienta: una grilla de celdas que guardan un valor
o una fórmula, fórmulas que apuntan a otras celdas por su dirección, y un motor que recalcula lo
que depende de una celda cuando esa celda cambia. Casi todo error de una planilla se explica con
esas tres piezas.

Dentro de [Planillas de cálculo](../planillas-de-calculo.md) es la base de todo lo demás: las
[fórmulas](../Formulas/formulas.md) son el lenguaje que corre sobre este modelo, y el
[diseño de planillas](../Diseno-de-planillas/diseno-de-planillas.md) es cómo se lo ordena para que
no se rompa. Excel y Google Sheets comparten el modelo; cambian detalles que cada nota señala.

## Libro, hoja, celda y rango

Un archivo es un libro (workbook); adentro tiene hojas (sheets); cada hoja es una grilla de celdas
con una dirección de columna y fila, como B7. Un rango es un bloque de celdas contiguas, como
A2:D500. Cada celda tiene dos capas: lo que guarda (un número, un texto, una fecha o una fórmula
que empieza con `=`) y cómo se muestra (el formato). Las fórmulas trabajan con lo que guarda, y
la diferencia entre las dos capas está en [tipos de dato](tipos-de-dato.md).

> [!NOTE]
> Sin fuente todavía: estas definiciones son estándar y no se contrastaron con una página oficial;
> el [glosario](../Fundamentos/glosario-de-planillas.md) las reúne.

## Una fórmula apunta, no copia

Una fórmula como `=B2*C2` no guarda los valores de B2 y C2: guarda la dirección. Si B2 cambia, el
resultado cambia. Esa dirección es relativa por defecto: al copiar la fórmula una fila abajo, pasa
a `=B3*C3`. Es lo que hace que una fórmula sirva para mil filas, y también la causa del error más
típico al copiar, cuando una celda que debía quedar fija (la del tipo de cambio, la del IVA) se
corre. Las referencias relativas, absolutas y mixtas, los nombres y las referencias a otras hojas
están en [celda y referencia](celda-y-referencia.md).

## La planilla recalcula en cadena

Cada fórmula depende de las celdas a las que apunta, y esas de otras: la planilla es una red de
dependencias. Cuando una celda cambia, el motor recalcula todo lo que depende de ella, en orden.
Por eso cambiar el precio de un insumo en una celda de entradas actualiza el costo de cada
producto, el margen y el total, sin tocar nada más. Es la idea que hace útil a una planilla para
[analizar escenarios](../Analisis/analisis-de-escenarios.md).

La red falla de tres maneras, y las tres se ven en [errores de fórmula](errores-de-formula.md):

- **Una fórmula que no puede calcular** muestra un valor de error, como #N/A o #¡REF!, y el error
  se propaga a todo lo que depende de ella.
- **Una fórmula que depende de sí misma**, directa o indirectamente, es una referencia circular.
  Excel la detecta y avisa.
- **Una fórmula que recalcula de más** hace lenta la planilla. Pasa con las funciones volátiles,
  como HOY o DESREF, que se recalculan siempre aunque nada haya cambiado.

El error más caro no muestra nada: una fórmula que apunta a la celda equivocada da un número
plausible. Para eso no hay mensaje; hay [revisar una planilla](../Diseno-de-planillas/revisar-una-planilla.md).

## Qué hay adentro del modelo

- [Celda y referencia](celda-y-referencia.md) — referencias relativas, absolutas y mixtas, rangos
  con nombre y referencias a otras hojas y archivos; leerla antes de copiar fórmulas.
- [Tipos de dato](tipos-de-dato.md) — número, texto, fecha como número, formato contra valor y
  configuración regional; leerla cuando un número se ve bien pero calcula mal.
- [Errores de fórmula](errores-de-formula.md) — qué dice cada valor de error, las referencias
  circulares, y el recálculo y las funciones volátiles; leerla cuando una fórmula da error o la
  planilla se pone lenta.
