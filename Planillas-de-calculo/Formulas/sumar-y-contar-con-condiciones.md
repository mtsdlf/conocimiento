---
resumen: >-
  SUMAR.SI.CONJUNTO y CONTAR.SI.CONJUNTO suman o cuentan solo las filas que cumplen una o varias
  condiciones, como las ventas de un producto en un mes o los clientes de una zona. Son la forma
  de dejar en fórmulas un resumen que también podría dar una tabla dinámica.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft, Función SUMAR.SI.CONJUNTO: https://support.microsoft.com/es-es/office/sumar-si-conjunto-función-sumar-si-conjunto-c9e748f5-7ea7-455d-9406-611cebce642b (según un resumen)"
  - "Google, COUNTIFS: https://support.google.com/docs/answer/3256550 (según un resumen)"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, sección 2.3"
aliases: [SUMAR.SI.CONJUNTO, SUMIFS, CONTAR.SI.CONJUNTO, COUNTIFS, SUMAR.SI, SUMIF, CONTAR.SI, COUNTIF, suma condicional]
creado: 2026-11-27
revisado: 2026-11-27
---

# Sumar y contar con condiciones

SUMAR.SI.CONJUNTO y CONTAR.SI.CONJUNTO suman o cuentan solo las filas que cumplen una o varias
condiciones, como las ventas de un producto en un mes o los clientes de una zona. Son la forma
de dejar en fórmulas un resumen que también podría dar una tabla dinámica.

Funcionan sobre una lista de [datos ordenados](../Datos-en-la-planilla/datos-ordenados.md): una
fila por venta, con columnas de fecha, producto, cliente e importe. Si los datos están armados como
un cuadro (un mes por columna, totales intercalados), estas funciones no tienen de dónde sumar.

## SUMAR.SI.CONJUNTO empieza por lo que se suma

La sintaxis de Microsoft en castellano es:

```
SUMAR.SI.CONJUNTO(rango_suma; rango_criterios1; criterios1; [rango_criterios2; criterios2]; ...)
```

Admite hasta 127 pares de rango y criterio, y cada rango de criterios tiene que tener el mismo
número de filas y columnas que el rango de suma. Las ventas del producto de G2 en la zona Norte:

```
=SUMAR.SI.CONJUNTO(Ventas!D:D; Ventas!B:B; G2; Ventas!C:C; "Norte")
```

Todas las condiciones se cumplen a la vez (es un "y"). Las condiciones pueden ser un valor, una
celda o una comparación entre comillas, como `">=1000"`; para comparar contra una celda se une el
signo con la celda: `">="&H1`.

El error más común lo señala la propia Microsoft: confundir el orden con SUMAR.SI (SUMIF), la
versión de una sola condición, donde el rango de suma va tercero y no primero. Una fórmula
copiada de una a otra suma la columna equivocada sin dar error.

## Sumar por mes es una condición de dos fechas

Como una fecha es un número (ver [tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md)), las
ventas de un mes son las de fecha mayor o igual al día 1 y menor o igual al último día:

```
=SUMAR.SI.CONJUNTO(Ventas!D:D; Ventas!A:A; ">="&H1; Ventas!A:A; "<="&FIN.MES(H1; 0))
```

H1 tiene el primer día del mes y FIN.MES da el último (ver [texto y fechas](texto-y-fechas.md)).
Armando una columna con los meses y copiando la fórmula, queda la tabla de ventas por mes en
fórmulas. Si el resumen es para mirar y cambiar de corte seguido, la
[tabla dinámica](../Analisis/tabla-dinamica.md) lo hace sin fórmulas; si tiene que alimentar otros
cálculos o un informe fijo, conviene en fórmulas.

## CONTAR.SI.CONJUNTO cuenta filas con la misma lógica

CONTAR.SI.CONJUNTO (COUNTIFS) recibe solo pares de rango y criterio, todos del mismo tamaño que el
primero, y cuenta las filas que cumplen todos. El ejemplo de Google, en inglés, es
`COUNTIFS(C1:C100, "Yes")`. En castellano, cuántas ventas pasaron de 1000 en la zona Norte:

```
=CONTAR.SI.CONJUNTO(Ventas!C:C; "Norte"; Ventas!D:D; ">1000")
```

La misma familia tiene PROMEDIO.SI.CONJUNTO (AVERAGEIFS) para promedios.

> [!NOTE]
> Sin fuente todavía: las páginas de Microsoft de CONTAR.SI.CONJUNTO, PROMEDIO.SI.CONJUNTO y
> SUMAPRODUCTO (SUMPRODUCT), la alternativa para condiciones "o" o cálculos fila por fila antes
> de sumar.

## Qué cambia entre Excel y Sheets

Sheets tiene SUMIFS y COUNTIFS con la misma lógica de pares de rango y criterio. En Excel, la
página de Microsoft lista SUMAR.SI.CONJUNTO desde Excel 2016 (el detalle,
en la [ficha de equivalencias](equivalencias-de-funciones.md)), así que no tiene el problema de
versiones de [BUSCARX](funciones-de-busqueda.md). En Sheets, además,
[QUERY](matrices-dinamicas.md#qué-cambia-entre-excel-y-sheets) arma la tabla entera de totales por
categoría en una sola fórmula, como un `GROUP BY` de [SQL](../../Bases-de-datos/SQL/agregacion.md).
