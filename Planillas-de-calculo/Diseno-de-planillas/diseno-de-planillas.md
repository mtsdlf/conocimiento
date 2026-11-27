---
resumen: >-
  El diseño de una planilla es la forma en que se reparten los datos, los supuestos, los cálculos y
  los resultados entre hojas y celdas, para que otra persona pueda usarla y cambiarla sin romperla.
  Abarca la estructura, cómo y cuánto fallan las planillas, y cómo se revisan antes de confiar en
  ellas.
estado: borrador
estabilidad: estable
fuentes:
  - "ICAEW, Financial Modelling Code (2018, ed. 2024): https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx"
  - "Raymond R. Panko, What We Don't Know About Spreadsheet Errors Today, EuSpRIG 2015: https://arxiv.org/pdf/1602.02601"
  - "Raymond R. Panko, Spreadsheet Errors: What We Know. What We Think We Can Do, EuSpRIG 2000: https://arxiv.org/pdf/0802.3457"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
aliases: [spreadsheet design, diseño de modelos, modelado en planillas, buenas prácticas de planillas]
creado: 2026-11-27
revisado:
---

# Diseño de planillas

El diseño de una planilla es la forma en que se reparten los datos, los supuestos, los cálculos y los resultados entre hojas y celdas, para que otra persona pueda usarla y cambiarla sin romperla. Abarca la estructura, cómo y cuánto fallan las planillas, y cómo se revisan antes de confiar en ellas.

Las otras verticales dan las piezas y esta decide dónde va cada una. Ordena dónde se guardan los [datos en la planilla](../Datos-en-la-planilla/datos-en-la-planilla.md) y dónde se escriben las [fórmulas](../Formulas/formulas.md), y se apoya en el [modelo de la planilla](../Modelo-de-la-planilla/modelo-de-la-planilla.md) para las referencias que no se corren al copiar. Cuando la planilla la usan varias personas, el diseño se cruza con [compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md).

## Por qué una planilla necesita diseño

Una celda acepta cualquier cosa y ninguna fórmula avisa si apunta a la fila equivocada. Por eso el error en una planilla no se ve: el número sale igual, con formato de moneda y dos decimales. Panko, que reunió las auditorías y los experimentos sobre el tema, lo resume en que los errores son raros celda por celda, pero en una planilla grande es muy probable que al menos un resultado final esté mal. Las cifras, con lo que mide cada una, están en [errores en planillas](errores-en-planillas.md).

El diseño ataca ese problema por dos lados. Primero, hace que los errores sean menos probables: cada supuesto en un solo lugar, ninguna cifra escondida en una fórmula, la misma fórmula en toda la fila. Segundo, hace que los errores que igual aparecen se puedan encontrar: los cálculos se leen de las entradas a las salidas, y hay controles que se ponen en rojo cuando algo no cuadra.

## Las tres decisiones que más pesan

La referencia profesional es el *Financial Modelling Code* del ICAEW, el instituto de contadores de Inglaterra y Gales. Está escrito para modelos financieros, pero sus principios valen para una planilla de costos o de stock. Las tres decisiones que más cambian el resultado son estas:

| Decisión | Qué dice el ICAEW | En una planilla de costos |
|---|---|---|
| Separar entradas, cálculos y salidas | Principio #9: "Segregate inputs (assumptions), calculations and outputs (results)" | Una hoja con precios de insumos y márgenes; otra con el costo por producto; otra con el resumen |
| Un solo lugar por dato | Principio #15: evitar la duplicación | El precio del kilo de harina se carga una vez y todo lo demás lo referencia |
| Sin números fijos en fórmulas | Principio #14: nada de valores como una tasa "entered as 20% within a formula" | El recargo de la tarjeta va en una celda de supuestos, no adentro de `=B4*1,1` |

El detalle de cada principio, con la forma de aplicarlo en Excel y en Google Sheets, está en [entradas, cálculo y salidas](entradas-calculo-salidas.md).

## Cómo se atrapa un error antes de que cueste

Panko encontró que una sola técnica mostró resultados en los estudios: la inspección celda por celda, y mejor si la hacen varias personas. Las herramientas de las aplicaciones (rastrear precedentes, comprobación de errores) ayudan a recorrer la planilla, pero no reemplazan esa lectura. El ICAEW suma dos prácticas: poner controles visibles dentro de la planilla (#17) y probarla cambiando entradas para ver si las salidas se mueven como se espera (#18). Todo eso está en [revisar una planilla](revisar-una-planilla.md).

Un error de diseño también puede ser que la herramienta ya no alcance. Cuando varias personas cargan los mismos registros a la vez o la planilla pasó a ser el registro del negocio, el problema deja de ser de fórmulas y la salida es [pasar a una base](../cuando-pasar-a-una-base.md).

## Qué hay adentro de Diseño de planillas

- [Entradas, cálculo y salidas](entradas-calculo-salidas.md) — la estructura que separa supuestos de cálculos, con los principios del ICAEW aplicados a una planilla de costos.
- [Errores en planillas](errores-en-planillas.md) — cuánto fallan de verdad, qué mide cada cifra que circula, los tipos de error y los casos públicos.
- [Revisar una planilla](revisar-una-planilla.md) — rastrear precedentes, controles, pruebas y revisión por pares, en Excel y en Sheets.
