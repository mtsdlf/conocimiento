---
resumen: >-
  Una fórmula es una expresión que empieza con `=` y calcula un resultado a partir de valores,
  referencias a otras celdas y funciones. Esta vertical reúne las familias de funciones que usa un
  negocio: lógicas, de búsqueda, de suma y conteo con condiciones, de texto y fecha, y las que
  devuelven listas enteras.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Información general sobre fórmulas en Excel: https://support.microsoft.com/es-ES/Excel/get-started/overview-of-formulas-in-excel"
  - "Microsoft Learn, How to correct formula errors (separador de listas): https://learn.microsoft.com/en-us/office/troubleshoot/excel/formula-errors"
  - "Google, Lista de funciones de Hojas de cálculo de Google: https://support.google.com/docs/table/25273?hl=es"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, sección 2"
aliases: [fórmula, formula, función, function, funciones de Excel, funciones de Sheets]
creado: 2026-11-27
revisado:
---

# Fórmulas

Una fórmula es una expresión que empieza con `=` y calcula un resultado a partir de valores,
referencias a otras celdas y funciones. Esta vertical reúne las familias de funciones que usa un
negocio: lógicas, de búsqueda, de suma y conteo con condiciones, de texto y fecha, y las que
devuelven listas enteras.

Las fórmulas corren sobre el [modelo de la planilla](../Modelo-de-la-planilla/modelo-de-la-planilla.md):
apuntan a celdas con [referencias](../Modelo-de-la-planilla/celda-y-referencia.md), trabajan con
el valor y no con el formato ([tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md)) y, cuando
no pueden calcular, muestran un [error](../Modelo-de-la-planilla/errores-de-formula.md). Su materia
prima son los [datos en la planilla](../Datos-en-la-planilla/datos-en-la-planilla.md): con una fila
por registro, una fórmula sirve para todas las filas; con datos armados como un cuadro, cada
fórmula es un caso especial. Lo que calculan alimenta el [análisis](../Analisis/analisis-en-planillas.md).

## Una fórmula es valores, referencias, operadores y funciones

`=C2*(1+$B$1)` multiplica el costo de C2 por uno más el margen de B1: tiene referencias, una
constante, operadores (`*`, `+`) y paréntesis. Una función es una pieza con nombre que hace un
cálculo que con operadores sería largo o imposible: `=SUMA(D2:D500)`, `=BUSCARX(...)`. Recibe
argumentos entre paréntesis y devuelve un resultado, que puede entrar en otra función.

En una planilla en castellano los nombres de las funciones están traducidos: SUMA es SUM, SI es
IF, BUSCARX es XLOOKUP. Los foros y buena parte de la documentación están en inglés, así que cada
nota da los dos nombres, y la [ficha de equivalencias](equivalencias-de-funciones.md) los junta.

El separador de argumentos depende de la configuración regional. En Excel es el "separador de
listas" de Windows, que en inglés de Estados Unidos es la coma; en las planillas en castellano con
coma decimal se usa el punto y coma, y así se escriben los ejemplos de este tema:
`=SI(C2<D2; "Reponer"; "")`. Una fórmula copiada de un foro en inglés hay que pasarla de `,` a `;`.
Por qué, en [tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md#la-configuración-regional-decide-la-coma-y-el-punto).

## Las familias que resuelven el trabajo de un negocio

Cinco familias cubren casi todo lo que se calcula en un comercio:

| Familia | Qué resuelve | Pregunta típica |
|---|---|---|
| [Lógicas](funciones-logicas.md) | elegir un resultado según una condición | ¿hay que reponer este producto? |
| [Búsqueda](funciones-de-busqueda.md) | traer un dato de otra tabla por una clave | ¿cuál es el precio de este código? |
| [Sumar y contar con condiciones](sumar-y-contar-con-condiciones.md) | totales parciales | ¿cuánto vendí de este producto en marzo? |
| [Texto y fechas](texto-y-fechas.md) | partir, limpiar y unir texto; plazos y períodos | ¿cuántos días hábiles faltan para la entrega? |
| [Matrices dinámicas](matrices-dinamicas.md) | listas enteras que crecen solas | ¿qué clientes compraron este mes? |

Se combinan: una búsqueda adentro de un SI.ND, una suma condicional con fechas armadas con
FIN.MES, un FILTRAR que reemplaza a varias búsquedas.

## Las fórmulas fallan por diseño antes que por función

Las fallas más caras no son de sintaxis, que la planilla marca, sino de diseño:

- **Números escritos dentro de la fórmula.** `=B2*1,21` funciona hasta que cambia la alícuota, y
  entonces hay que encontrar cada fórmula que la tiene. Los supuestos van en celdas de entradas,
  como dice [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md).
- **Fórmulas largas y anidadas.** Microsoft desaconseja anidar muchos SI por lo difícil de probar
  y mantener (ver [funciones lógicas](funciones-logicas.md)). Partir el cálculo en columnas
  auxiliares, o nombrar los pasos con LET, hace que otro pueda revisarlo.
- **Errores tapados.** Un SI.ERROR que cubre todo esconde las referencias rotas.
- **Funciones que no existen en la versión del que abre el archivo.** BUSCARX, FILTRAR o LAMBDA
  dan #¿NOMBRE? en versiones viejas de Excel.

Cuánto fallan las fórmulas en planillas reales está en
[errores en planillas](../Diseno-de-planillas/errores-en-planillas.md).

## Qué cambia entre Excel y Sheets

Las dos comparten la mayoría de las funciones y casi todos sus nombres en castellano. Las
diferencias que más pesan:

- **Versiones.** Sheets es una sola versión para todos. En Excel, una función nueva puede existir
  en Microsoft 365 y no en una versión comprada hace años.
- **Funciones propias.** Sheets tiene QUERY, IMPORTRANGE y ARRAYFORMULA; Excel tiene la referencia
  `A1#` a un rango desbordado y Power Query como herramienta aparte.
- **Detalles de comportamiento.** El mismo nombre puede tener otros argumentos o devolver otro
  error, como FILTER sin resultados (#CALC! en Excel, #N/A en Sheets) o SORT, que en Sheets ordena
  con VERDADERO o FALSO.

## Qué hay adentro de Fórmulas

- [Funciones lógicas](funciones-logicas.md) — SI, Y, O, SI.CONJUNTO, SI.ERROR y SI.ND; leerla para
  reglas de negocio y para tratar errores esperados.
- [Funciones de búsqueda](funciones-de-busqueda.md) — BUSCARV, INDICE con COINCIDIR y BUSCARX, y el
  debate entre las dos últimas; leerla antes de cruzar dos listas.
- [Sumar y contar con condiciones](sumar-y-contar-con-condiciones.md) — SUMAR.SI.CONJUNTO y
  CONTAR.SI.CONJUNTO, con ventas por mes; leerla cuando un resumen tiene que quedar en fórmulas.
- [Texto y fechas](texto-y-fechas.md) — partir, limpiar y unir texto, armar fechas y calcular
  plazos; leerla cuando los datos llegan sucios o hay que calcular vencimientos.
- [Matrices dinámicas](matrices-dinamicas.md) — FILTRAR, ORDENAR, UNICOS, LET, LAMBDA y lo propio
  de Sheets (ARRAYFORMULA, QUERY); leerla para listas que se actualizan solas.
- [Equivalencias de funciones](equivalencias-de-funciones.md) — ficha con nombres en castellano e
  inglés y en qué versiones de Excel y desde cuándo en Sheets existe cada función, al 2026-11-27.
