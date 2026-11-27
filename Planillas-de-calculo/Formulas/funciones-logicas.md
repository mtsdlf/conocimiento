---
resumen: >-
  Las funciones lógicas hacen que una fórmula elija entre resultados según una condición: SI para
  una condición, Y y O para combinar varias, SI.CONJUNTO para una escala de casos, y SI.ERROR y
  SI.ND para decidir qué mostrar cuando otra fórmula da error.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Función SI: https://support.microsoft.com/es-es/office/si-funci%C3%B3n-si-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2"
  - "Microsoft, Función SI: fórmulas anidadas y cómo evitar problemas: https://support.microsoft.com/es-es/office/funci%C3%B3n-si-f%C3%B3rmulas-anidadas-y-c%C3%B3mo-evitar-problemas-0b22ff44-f149-44ba-aeb5-4ef99da241c8"
  - "Microsoft, Función Y: https://support.microsoft.com/es-es/excel/functions/and-function"
  - "Microsoft, Función O: https://support.microsoft.com/es-es/excel/functions/or-function"
  - "Microsoft, Función SI.CONJUNTO: https://support.microsoft.com/es-es/office/si-conjunto-función-si-conjunto-36329a26-37b2-467c-972b-4a39bd951d45 (según un resumen)"
  - "Microsoft, Función SI.ERROR: https://support.microsoft.com/es-es/office/funci%C3%B3n-si-error-c526fd07-caeb-47b8-8bb6-63f3e417f611"
  - "Microsoft, Función SI.ND: https://support.microsoft.com/es-es/office/si-nd-funci%C3%B3n-si-nd-6626c961-a569-42fc-a49d-79b4951fd461"
  - "Microsoft, Cómo corregir un error #¿NOMBRE?: https://support.microsoft.com/es-es/excel/how-to-correct-a-name-error"
  - "Google, SI.ERROR (IFERROR): https://support.google.com/docs/answer/3093304?hl=es"
  - "Google, SI (IF): https://support.google.com/docs/answer/3093364?hl=es"
  - "Google, Y (AND): https://support.google.com/docs/answer/3093301?hl=es"
  - "Google, SI.CONJUNTO (IFS): https://support.google.com/docs/answer/7014145?hl=es"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, sección 2.1; páginas de Microsoft y Google leídas el 2026-11-27 a través de un resumidor"
aliases: [SI, IF, Y, AND, O, OR, SI.CONJUNTO, IFS, SI.ERROR, IFERROR, SI.ND, IFNA, condicional, fórmula con condición]
creado: 2026-11-27
revisado:
---

# Funciones lógicas

Las funciones lógicas hacen que una fórmula elija entre resultados según una condición: SI para
una condición, Y y O para combinar varias, SI.CONJUNTO para una escala de casos, y SI.ERROR y
SI.ND para decidir qué mostrar cuando otra fórmula da error.

Sirven para lo que en un negocio son reglas: aplicar un descuento si la compra pasa de un monto,
marcar un producto para reponer si el stock está debajo del mínimo, poner una categoría según el
total vendido. Una condición es una comparación que da VERDADERO o FALSO, como `C2<D2` o
`B2="Mayorista"`.

## SI elige entre dos resultados

SI (IF) devuelve un valor si la condición es verdadera y otro si es falsa. La sintaxis de
Microsoft es `SI(prueba_lógica; valor_si_verdadero; [valor_si_falso])`. Para marcar qué reponer:

```
=SI(C2<D2; "Reponer"; "")
```

Si el stock de C2 está debajo del mínimo de D2, escribe "Reponer"; si no, deja la celda vacía.
Los resultados pueden ser otras fórmulas: `=SI(B2>=50000; B2*0,9; B2)` aplica un 10 % de
descuento a las compras de 50.000 o más. Ese 0,9 y ese 50.000 conviene sacarlos a celdas de
entradas, como dice [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md),
para cambiarlos sin tocar la fórmula.

## Y y O combinan condiciones

Y (AND) devuelve VERDADERO si todas sus condiciones lo son; O (OR), si al menos una lo es. Las dos
aceptan hasta 255 condiciones según Microsoft, y se usan adentro de SI:

```
=SI(Y(B2="Mayorista"; C2>=50000); "Descuento"; "Lista")
=SI(O(E2="Vencido"; F2>90); "Revisar"; "")
```

La primera da descuento solo a mayoristas que compran 50.000 o más; la segunda marca un cliente
si tiene una factura vencida o más de 90 días sin pagar. Google aclara para Sheets que el número
0 cuenta como FALSO y cualquier otro número, negativos incluidos, como VERDADERO.

## Muchos SI anidados se rompen; SI.CONJUNTO los ordena

Para más de dos casos, la forma vieja es poner un SI adentro de otro. Microsoft lo desaconseja con
números: "Aunque Excel le permitirá anidar hasta 64 funciones SI diferentes, no es nada
recomendable hacerlo", y advierte que una fórmula anidada sin precisión "puede funcionar el 75 %
de las veces, pero devolver resultados inesperados el 25 % de las veces". El problema es el
mantenimiento: cambiar un tramo obliga a leer toda la cadena.

SI.CONJUNTO (IFS) prueba condiciones en orden y devuelve el valor de la primera que se cumple. La
sintaxis es `=SI.CONJUNTO(prueba_lógica1; valor_si_verdadero1; [prueba_lógica2; valor_si_verdadero2]; ...)`,
con hasta 127 pruebas. Para clasificar clientes por compra anual:

```
=SI.CONJUNTO(B2>=1000000; "A"; B2>=300000; "B"; VERDADERO; "C")
```

El `VERDADERO` del final hace de "en cualquier otro caso"; sin él, si ninguna condición se cumple
la fórmula da #N/A. Aun así, Microsoft desaconseja anidar muchas condiciones en SI.CONJUNTO por lo
difícil de probar y actualizar. Cuando los tramos son una tabla (de 0 a 300.000, categoría C; de
300.000 a 1.000.000, B), es más claro poner esa tabla en la planilla y traer la categoría con una
búsqueda aproximada, como cuenta [funciones de búsqueda](funciones-de-busqueda.md). Esto último es
inferencia, no recomendación de una fuente.

## SI.ERROR esconde todos los errores, también los que avisan

SI.ERROR (IFERROR) devuelve el resultado de una fórmula o, si da error, otro valor. La sintaxis es
`SI.ERROR(valor; valor_si_error)` y atrapa, según Microsoft, "#N/A, #¡VALOR!, #¡REF!, #¡DIV/0!,
#¡NUM!, #¿NOMBRE? o #¡NULO!". Es útil para un margen que divide por ventas que todavía son cero:

```
=SI.ERROR(C2/B2; 0)
```

El riesgo es que no distingue el error esperado del que avisa de un problema: si alguien borra la
columna B, la fórmula pasa de #¡REF! a 0 sin que nadie se entere. Microsoft lo dice para el error
de nombre mal escrito: "No use ninguna función de control de errores, como SI.ERROR, para
enmascarar el error." Qué indica cada error está en
[errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md).

SI.ND (IFNA) es la versión acotada: solo atrapa #N/A, el error de una búsqueda que no encontró el
valor, y deja ver los demás. Para búsquedas conviene SI.ND, o el argumento si_no_se_encuentra de
BUSCARX, antes que SI.ERROR:

```
=SI.ND(BUSCARV(A2; Precios!A:C; 3; FALSO); "Sin precio")
```

## Qué cambia entre Excel y Sheets

Sheets tiene las seis funciones con el mismo nombre en castellano (SI, Y, O, SI.CONJUNTO,
SI.ERROR, SI.ND) y la misma lógica. Dos diferencias de detalle, según las páginas de Google:

- En Sheets, SI.ERROR acepta un solo argumento, `SI.ERROR(valor; [valor_si_error])`, y devuelve
  un elemento en blanco si hay error. En Excel los dos argumentos son obligatorios.
- En Sheets, el tercer argumento de SI es opcional y vacío de manera predeterminada.

SI.CONJUNTO no existe en versiones viejas de Excel; cuáles, en la
[ficha de equivalencias](equivalencias-de-funciones.md).
