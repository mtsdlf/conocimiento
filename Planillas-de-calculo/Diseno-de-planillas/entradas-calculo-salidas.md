---
resumen: >-
  Entradas, cálculo y salidas es la estructura que separa en una planilla los supuestos que alguien
  carga, las fórmulas que calculan con ellos y los resultados que se leen, para que cada dato esté en
  un solo lugar y la lógica vaya siempre de las entradas a las salidas.
estado: vigente
estabilidad: estable
fuentes:
  - "ICAEW, Financial Modelling Code (2018, ed. 2024), principios #9, #12, #14 y #15: https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx"
  - "FAST Standard Organisation, The FAST Standard (solo la página web; el PDF de reglas 02c no se leyó): https://www.fast-standard.org/the-fast-standard/"
  - "Microsoft, Overview of formulas in Excel (referencias relativas y absolutas): https://support.microsoft.com/en-us/office/overview-of-formulas-in-excel-ecfdc708-9162-49e8-b993-c311f47ca173"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
aliases: [inputs calculations outputs, entradas cálculos salidas, separar supuestos, hoja de supuestos, Financial Modelling Code, FAST Standard]
creado: 2026-11-27
revisado: 2026-11-27
---

# Entradas, cálculo y salidas

Entradas, cálculo y salidas es la estructura que separa en una planilla los supuestos que alguien carga, las fórmulas que calculan con ellos y los resultados que se leen, para que cada dato esté en un solo lugar y la lógica vaya siempre de las entradas a las salidas.

La formulación de referencia es la del *Financial Modelling Code* del ICAEW: "Segregate inputs (assumptions), calculations and outputs (results)" (principio #9), con la lógica fluyendo "from inputs to outputs". El Code está pensado para modelos financieros; acá se adapta a la planilla que más se arma en un negocio chico, la de costos y precios. La misma estructura sirve para el [plan financiero mínimo](../../Emprender/Finanzas/plan-financiero-minimo.md), que es una planilla de caja mes por mes.

## Una planilla de costos partida en tres

Un comercio que vende pan y facturas quiere saber cuánto le cuesta cada producto y a qué precio venderlo. Partida en tres, la planilla queda así:

| Hoja | Qué tiene | Quién la toca |
|---|---|---|
| Supuestos | Precio del kilo de cada insumo, margen buscado, recargo de la tarjeta, costo de la hora de trabajo | Quien sabe los precios, cada vez que cambian |
| Cálculo | La receta de cada producto (cantidad de cada insumo) y el costo que sale de multiplicar por los precios de Supuestos | Casi nadie: se arma una vez y se revisa |
| Resumen | Costo por unidad, precio sugerido y margen de cada producto | Se lee, no se escribe |

Con esa separación, cuando sube la harina se cambia una sola celda en Supuestos y todo lo demás se recalcula. Sin ella, el precio de la harina aparece escrito en diez fórmulas, alguien actualiza nueve y el costo de las medialunas queda viejo sin que nada lo avise.

El Code admite una excepción: un tablero de resultados puede tener entradas, aunque eso "contradice" la práctica de agruparlas, siempre que la entrada esté "very clearly identified". En la planilla de costos, eso sería poner el margen buscado arriba del Resumen para probar precios, con el color de entrada.

## Los cuatro principios que la sostienen

Separar en tres hojas no alcanza si adentro de cada una las fórmulas esconden datos. El Code agrega principios que hacen que la separación funcione. Estos son los que tocan a una planilla chica:

**Un solo lugar por cada valor de entrada (#15).** El Code lo llama evitar la duplicación. Si el precio del kilo de harina vive en `Supuestos!B4`, toda fórmula que lo use apunta a `Supuestos!B4`; nadie lo vuelve a tipear. Es el mismo principio que hace preferir un archivo compartido a copias por mail, como cuenta [compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md).

**Ningún número fijo adentro de una fórmula (#14).** El Code define el problema como "Fixed values embedded into a formula, such as a tax rate entered as 20% within a formula". En la planilla de costos, `=C5*1,1` para sumar el recargo de la tarjeta es exactamente eso: el 10 % no se ve, no tiene etiqueta y no cambia cuando cambia el recargo. Va en una celda de Supuestos con su nombre. El Code admite excepciones de bajo riesgo, como las 24 horas de un día, y lo prohíbe para valores que puedan cambiar durante la vida de la planilla.

**Fórmulas consistentes en todo el bloque (#12).** El texto es "Make formulas strictly consistent across formula blocks, so the formula can be copied and pasted across the block". En la hoja de Cálculo, la fórmula del costo es la misma en cada fila de producto, y la diferencia entre filas sale de las referencias, no de fórmulas escritas a mano una por una. Lo que no tiene que moverse al copiar se fija con `$` o con un nombre, como explica [celda y referencia](../Modelo-de-la-planilla/celda-y-referencia.md). Una fila con una fórmula distinta a sus vecinas es el lugar donde suele estar el error.

**Las entradas se distinguen a la vista.** El Code pide marcarlas con un color de relleno definido y no identificarlas solo con una etiqueta de texto. En la práctica: todas las celdas que se cargan a mano llevan el mismo color, y cualquier celda de ese color en la hoja de Cálculo es una alarma.

Otros dos principios del Code completan la estructura, pero son de revisión: poner controles visibles (#17) y probar la planilla cambiando entradas (#18). Están en [revisar una planilla](revisar-una-planilla.md).

## Qué cambia entre Excel y Google Sheets

La estructura es la misma en las dos aplicaciones, porque es una forma de ordenar celdas y no una función de ninguna. Cambian las herramientas para sostenerla:

- **Nombres.** Las dos permiten ponerle nombre a una celda o un rango (`RecargoTarjeta` en lugar de `Supuestos!B7`), que es la forma que el Code sugiere para que una fórmula se lea sola. El detalle está en [celda y referencia](../Modelo-de-la-planilla/celda-y-referencia.md).
- **Proteger lo que no se carga.** En Sheets se puede limitar quién edita un rango o una hoja, con la advertencia de Google de que "Protection isn't a security measure". En Excel la protección de hoja cumple el mismo papel. Las dos cosas están en [compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md).
- **Validar lo que sí se carga.** Una lista desplegable en la celda del insumo evita que alguien escriba "harina 000" en una fila y "Harina 000" en otra; las diferencias entre las dos aplicaciones están en [validación de datos](../Datos-en-la-planilla/validacion-de-datos.md).

## FAST, la otra referencia

El FAST Standard es el otro estándar de modelado que se cita junto al del ICAEW. Su nombre es la sigla de "Flexible, Appropriate, Structured & Transparent", y lo mantiene la FAST Standard Organisation. Su página pide "Rigorous consistency in layout and organisation" y "simple, clear formulas". La versión enlazada es la 02c de julio de 2019, según el nombre del archivo.

> [!NOTE] Sin fuente todavía: las reglas concretas de FAST (por ejemplo, el sentido en que fluye el cálculo dentro de una hoja) están en su PDF, que no se leyó. Esta nota no le atribuye ninguna regla más allá de lo que dice su página web.

Cómo se relacionan FAST y el Code, que se suelen presentar como complementarios, está en [fundamentos de planillas](../Fundamentos/fundamentos-de-planillas.md).

## Cómo falla la estructura

La falla más común es la planilla que nació chica y nunca se separó: los precios están en la misma fila que los cálculos y cada mes alguien pisa un número. La segunda es separar bien al principio y después "arreglar" un caso tipeando un valor arriba de una fórmula; desde ese momento la celda ya no calcula y nada lo muestra. Las dos son errores que la [revisión](revisar-una-planilla.md) encuentra si busca fórmulas inconsistentes y celdas con valores donde debería haber fórmulas.

> [!NOTE] Sin fuente todavía: el reparto en tres hojas para una planilla de costos es una adaptación propia del principio #9 del ICAEW a un negocio chico; el Code no da ese ejemplo.
