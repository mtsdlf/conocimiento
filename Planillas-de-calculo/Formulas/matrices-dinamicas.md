---
resumen: >-
  Una matriz dinámica es una fórmula que devuelve varios valores y los vuelca sola en las celdas
  vecinas: una lista filtrada, ordenada o sin repetidos que crece y se achica con los datos.
  FILTRAR, ORDENAR, UNICOS, LET y LAMBDA son las funciones que trabajan así.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Dynamic array formulas and spilled array behavior: https://support.microsoft.com/en-us/office/dynamic-array-formulas-and-spilled-array-behavior-205c6b06-03ba-4151-89a1-87a7eb36e531 (según un resumen)"
  - "Microsoft Excel Blog, Preview of Dynamic Arrays in Excel (2018-09, actualizada 2020-07-01): https://techcommunity.microsoft.com/blog/excelblog/preview-of-dynamic-arrays-in-excel/252944 (según un resumen)"
  - "Microsoft, Función FILTRAR: https://support.microsoft.com/es-es/office/filtrar-función-filtrar-f4f7cb66-82eb-4767-8f7c-4877ad80c759 (según un resumen)"
  - "Microsoft, Función LET: https://support.microsoft.com/es-es/office/let-función-let-34842dd8-b92b-4d3f-b325-b8b8f9908999 (según un resumen)"
  - "Microsoft, LAMBDA function: https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67 (según un resumen)"
  - "Microsoft, Cómo corregir un error #DESBORDAMIENTO!: https://support.microsoft.com/es-es/Excel/how-to-correct-a-spill-error (según un resumen)"
  - "Google, FILTER: https://support.google.com/docs/answer/3093197 (según un resumen)"
  - "Google, ARRAYFORMULA: https://support.google.com/docs/answer/3093275 (según un resumen)"
  - "Google, QUERY: https://support.google.com/docs/answer/3093343 (según un resumen)"
  - "Microsoft, Función ORDENAR: https://support.microsoft.com/es-es/excel/functions/sort-function"
  - "Microsoft, Función UNICOS: https://support.microsoft.com/es-es/excel/functions/unique-function"
  - "Microsoft, Función SECUENCIA: https://support.microsoft.com/es-es/excel/functions/sequence-function"
  - "Google, SORT: https://support.google.com/docs/answer/3093150?hl=es"
  - "Google, UNIQUE: https://support.google.com/docs/answer/10522653?hl=es"
  - "Google Workspace Updates, 2022-08-24: https://workspaceupdates.googleblog.com/2022/08/named-functions-google-sheets.html"
  - "Google Workspace Updates, 2023-02-01: https://workspaceupdates.googleblog.com/2023/01/google-sheets-powerful-functions-advanced-analysis.html"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, sección 2.5"
aliases: [matriz dinámica, dynamic arrays, desbordamiento, spill, FILTRAR, FILTER, ORDENAR, SORT, UNICOS, UNIQUE, LET, LAMBDA, ARRAYFORMULA, QUERY]
creado: 2026-11-27
revisado:
---

# Matrices dinámicas

Una matriz dinámica es una fórmula que devuelve varios valores y los vuelca sola en las celdas
vecinas: una lista filtrada, ordenada o sin repetidos que crece y se achica con los datos.
FILTRAR, ORDENAR, UNICOS, LET y LAMBDA son las funciones que trabajan así.

Antes, una fórmula daba un valor por celda y para una lista había que copiarla fila por fila.
Con las matrices dinámicas, una sola fórmula en una celda produce la lista entera de clientes de
una zona, los productos sin stock ordenados por proveedor o los meses sin repetir. Es el puente
entre las fórmulas de una celda y el resumen de una [tabla dinámica](../Analisis/tabla-dinamica.md):
el resultado queda en fórmulas, se actualiza solo y se puede seguir calculando encima.

## La fórmula se desborda hacia abajo y hacia la derecha

Cuando una fórmula devuelve varios valores, Excel los pone en las celdas vecinas, lo que
Microsoft llama "spilling" y en castellano desbordamiento. Solo la primera celda tiene la
fórmula; las demás muestran el resultado. El ejemplo de Microsoft, en inglés, ordena diez ventas
de mayor a menor:

```
=SORT(D2:D11,1,-1)
```

Para referirse al resultado entero, sin saber cuántas filas tiene, Excel usa `#` después de la
primera celda: `A1#` es todo el rango desbordado desde A1. Así, `=SUMA(F2#)` suma la lista
filtrada aunque cambie de tamaño.

El desbordamiento falla cuando algo ocupa el lugar: la fórmula da #DESBORDAMIENTO! (#SPILL!).
Según Microsoft, aparece cuando el rango de salida "no está en blanco", y también con celdas
combinadas, dentro de una [tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md) de
Excel, con columnas enteras que no entran en la grilla, por falta de memoria o cuando una función
volátil hace que el tamaño no se pueda saber. La solución usual es borrar lo que hay debajo. El
resto de los errores está en [errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md).

## Las funciones que devuelven listas

| Función (castellano / inglés) | Qué hace | Ejemplo de negocio |
|---|---|---|
| FILTRAR / FILTER | las filas que cumplen una condición | las ventas de un vendedor |
| ORDENAR / SORT | ordena un rango por una columna | precios de mayor a menor |
| ORDENARPOR / SORTBY | ordena por otro rango | productos por unidades vendidas |
| UNICOS / UNIQUE | la lista sin repetidos | los clientes que compraron este mes |
| SECUENCIA / SEQUENCE | una serie de números | los números de cuota del 1 al 12 |

Las cinco, más RANDARRAY, son las que presentó Microsoft en 2018 con las matrices dinámicas. La
sintaxis de FILTRAR en castellano es `=FILTRAR(matriz;incluir;[si_vacío])`:

```
=FILTRAR(Ventas!A2:D500; Ventas!C2:C500 = "Norte"; "Sin ventas")
```

Si nada cumple la condición y falta el tercer argumento, Excel da #CALC!. Si la condición tiene
errores, FILTRAR devuelve error. FILTRAR también resuelve lo que BUSCARX no hace: traer todas las
coincidencias de una clave, no solo la primera (ver [funciones de búsqueda](funciones-de-busqueda.md)).

Para quitar repetidos y ordenar a la vez se anidan: `=ORDENAR(UNICOS(Ventas!B2:B500))` da la
lista de clientes en orden alfabético.

Las sintaxis de Microsoft en castellano son `=ORDENAR(array;[sort_index];[sort_order];[by_col])`,
con 1 para orden ascendente (el predeterminado) y -1 para descendente, y
`=SECUENCIA(filas;[columnas];[inicio];[paso])`, donde los argumentos que faltan valen 1. La página
de UNICOS muestra la sintaxis en inglés, `=UNIQUE(array,[by_col],[exactly_once])`.

> [!NOTE]
> Sin fuente todavía: la página de ORDENARPOR (SORTBY). El ejemplo anidado es propio.

## LET pone nombre a los pasos de una fórmula larga

LET define nombres dentro de una fórmula y los usa en el cálculo final, para no repetir el mismo
pedazo y para que se lea. La sintaxis de Microsoft es
`=LET(nombre1, nombre_valor1, cálculo_o_nombre2, ...)`, con hasta 126 pares. En castellano:

```
=LET(costo; B2*C2; margen; 0,3; costo*(1+margen))
```

El costo se calcula una vez y se reusa; si el margen cambia, se toca en un lugar. Para supuestos
que usa toda la planilla, el lugar es una celda de entradas, como dice
[entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md), no un número
dentro de LET.

## LAMBDA crea funciones propias sin macros

LAMBDA arma una función con parámetros a partir de una fórmula. La sintaxis de Microsoft es
`=LAMBDA([parámetro1, ...,] cálculo)`, con hasta 253 parámetros. Se le pone un nombre con el
administrador de nombres (los nombres están en [celda y referencia](../Modelo-de-la-planilla/celda-y-referencia.md))
y después se usa como cualquier función: `=PRECIOFINAL(B2)`. Una LAMBDA escrita en una celda sin
llamarla da #CALC!, y una recursión que se pasa del límite da #¡NUM!. Con ella vienen funciones
auxiliares que recorren rangos: MAP, REDUCE, SCAN, BYROW, BYCOL y MAKEARRAY.

LAMBDA reemplaza macros chicas que solo calculan, sin el riesgo ni el permiso que pide una
[macro](../Automatizar-y-compartir/macros.md). Para un negocio chico, LET alcanza casi siempre;
LAMBDA conviene cuando la misma cuenta se repite en muchas hojas.

## Qué cambia entre Excel y Sheets

Las dos tienen FILTER, SORT, UNIQUE, SEQUENCE, LET, LAMBDA y sus auxiliares, pero difieren en
cuatro cosas:

- **Los nombres.** En la lista de funciones de Google en castellano, SORT y UNIQUE conservan el
  nombre en inglés, donde Excel dice ORDENAR y UNICOS; SECUENCIA se llama igual. El SORT de Sheets
  también cambia los argumentos: `SORT(intervalo; columna_ordenación; es_ascendente; ...)` pide
  VERDADERO o FALSO para el orden, no 1 o -1.

- **FILTER sin resultados.** En Sheets, `FILTER(range, condition1, [condition2, ...])` devuelve
  #N/A si nada cumple; en Excel da #CALC! salvo que se use el tercer argumento. Sheets no tiene
  ese tercer argumento: cada argumento extra es otra condición.
- **ARRAYFORMULA.** En Sheets, `ARRAYFORMULA(array_formula)` hace que una fórmula de una celda se
  aplique a un rango entero. Según Google, muchas fórmulas ya se expanden solas y no hace falta.
  En Excel no existe porque todas las fórmulas se desbordan.
- **QUERY.** Sheets tiene `QUERY(data, query, [headers])`, que consulta un rango con un lenguaje
  parecido a SQL (el de la Google Visualization API). Cada columna tiene que tener un solo tipo de
  valor. Excel no tiene QUERY; lo más parecido es [Power Query](../Datos-en-la-planilla/power-query.md),
  que es otra herramienta. Para quien ya sabe [SQL](../../Bases-de-datos/SQL/sql.md), QUERY hace en
  una fórmula lo que pedirían varias funciones de esta nota.

En qué versiones de Excel existe cada función, y desde cuándo en Sheets, está en la
[ficha de equivalencias](equivalencias-de-funciones.md). Lo que conviene saber de antemano: estas
funciones no existen en las versiones viejas de Excel. Qué pasa exactamente al abrir el archivo en
una de ellas solo se encontró, en un resumen, para BUSCARX (muestra el resultado guardado y da
#¿NOMBRE? al reescribir la fórmula); para FILTRAR, LAMBDA y las demás no se verificó.

> [!NOTE]
> Sin fuente todavía: si la sintaxis `A1#` funciona en Google Sheets, y desde cuándo existen
> FILTER, SORT, UNIQUE y SEQUENCE en Sheets.
