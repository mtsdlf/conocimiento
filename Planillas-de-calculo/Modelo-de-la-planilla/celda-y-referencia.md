---
resumen: >-
  Una referencia es la dirección con la que una fórmula apunta a otra celda, como B4. Puede ser
  relativa (se corre al copiar la fórmula), absoluta ($B$4, queda fija) o mixta, y también puede
  ser un nombre, otra hoja u otro archivo.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft, Cambiar entre referencias relativas, absolutas y mixtas: https://support.microsoft.com/es-es/office/cambiar-entre-referencias-relativas-absolutas-y-mixtas-dfec08cd-ae65-4f56-839e-5f0d8d0baca9"
  - "Microsoft, Información general sobre fórmulas en Excel: https://support.microsoft.com/es-ES/Excel/get-started/overview-of-formulas-in-excel"
  - "Microsoft, Crear o cambiar una referencia de celda: https://support.microsoft.com/es-es/Excel/create-or-change-a-cell-reference"
  - "Microsoft, Definir y usar nombres en fórmulas: https://support.microsoft.com/es-es/Excel/get-started/define-and-use-names-in-formulas"
  - "Microsoft, Cómo corregir un error #¡REF!: https://support.microsoft.com/es-es/excel/how-to-correct-a-ref-error"
  - "Google, Name a range: https://support.google.com/docs/answer/63175"
  - "Google, Reference data from other sheets: https://support.google.com/docs/answer/75943"
  - "Google, IMPORTRANGE: https://support.google.com/docs/answer/3093340"
  - "Páginas de Microsoft y Google leídas el 2026-11-27 a través de un resumidor"
aliases: [referencia de celda, cell reference, referencia relativa, referencia absoluta, referencia mixta, rango con nombre, named range, nombre definido, defined name, referencia a otra hoja]
creado: 2026-11-27
revisado: 2026-11-27
---

# Celda y referencia

Una referencia es la dirección con la que una fórmula apunta a otra celda, como B4. Puede ser
relativa (se corre al copiar la fórmula), absoluta ($B$4, queda fija) o mixta, y también puede
ser un nombre, otra hoja u otro archivo.

Elegir bien el tipo de referencia es lo que permite escribir una fórmula una vez y copiarla a mil
filas. Elegirlo mal es el error más común al copiar: la fórmula sigue dando un número, solo que
calculado con la celda equivocada, y nada lo marca. Por eso conviene entender este mecanismo
antes que cualquier [función](../Formulas/formulas.md).

## Relativa, absoluta y mixta

Por defecto, según Microsoft, "una referencia de celda es una referencia relativa": guarda la
posición en relación con la celda de la fórmula. Si D4 tiene `=B4*C4` y se copia a D5, pasa a ser
`=B5*C5`. Es lo que se quiere para multiplicar cantidad por precio en cada fila.

Una referencia absoluta lleva `$` delante de la columna y de la fila, y no cambia al copiar:
`$B$1` apunta siempre a B1. Es lo que se quiere para una celda única que usan todas las filas,
como el tipo de cambio o la alícuota de IVA:

```
=C4*$B$1
```

Copiada hacia abajo, pasa a `=C5*$B$1`, `=C6*$B$1`: el precio se corre, el tipo de cambio no.

Una referencia mixta fija solo una parte: `$B4` fija la columna y deja correr la fila; `C$4` fija
la fila. Sirve para tablas de doble entrada, como precios por producto (filas) y por lista de
precios (columnas). La tabla de Microsoft muestra qué pasa al copiar una referencia a A1 dos
celdas abajo y dos a la derecha:

| Referencia original | Al copiarla | Tipo |
|---|---|---|
| `$A$1` | `$A$1` | absoluta |
| `A$1` | `C$1` | mixta |
| `$A1` | `$A3` | mixta |
| `A1` | `C3` | relativa |

En Excel, al seleccionar la referencia en la barra de fórmulas y apretar F4, se pasa por los
cuatro tipos. Sheets usa el mismo `$` con el mismo significado, según su página de la función
DIRECCION (ADDRESS).

> [!NOTE]
> Sin fuente todavía: Google no tiene una página propia sobre referencias relativas y absolutas;
> que F4 haga lo mismo en Sheets no se verificó.

## Un nombre dice qué es la celda

Un nombre reemplaza una dirección por una palabra: en vez de `$B$1`, `TipoDeCambio`. Microsoft
dice que se puede definir un nombre "para un rango de celdas, una función, una constante o una
tabla" y que "si utiliza nombres, sus fórmulas serán mucho más fáciles de entender y mantener".

```
=C4*TipoDeCambio
```

Un nombre es absoluto: no se corre al copiar. Google da el ejemplo de `=SUM(A1:B2, D4:E6)`
convertido en `=SUM(budget_total, quarter2)`; en Sheets los nombres admiten solo letras, números y
guiones bajos, de 1 a 250 caracteres, y no pueden parecerse a una referencia como A1. Los nombres
son una de las prácticas de [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md):
cada supuesto en una celda de entradas, con nombre. También son la forma de guardar una función
propia hecha con LAMBDA (ver [matrices dinámicas](../Formulas/matrices-dinamicas.md)).

Según un resumen del buscador de una página de Microsoft que no se pudo abrir, en Excel un nombre
vale para todo el libro o solo para una hoja, y el predeterminado es el libro.

Una [tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md) da nombre automático a
cada columna y crece sola, lo que evita tanto los rangos fijos como los nombres a mano.

## Otra hoja, otro archivo

Para apuntar a otra hoja del mismo libro se escribe el nombre de la hoja, un signo de exclamación
y la celda: `=Precios!B2`. Si el nombre tiene espacios u otros caracteres, va entre comillas
simples: `='Ingresos enero'!A1`. Es igual en Excel y en Sheets. Excel además acepta referencias
3D que recorren varias hojas: `=SUMA(Hoja2:Hoja13!B5)` suma B5 de doce hojas, por ejemplo una por
mes.

Para apuntar a otro archivo las dos herramientas difieren:

- **Excel** usa vínculos a otro libro, que Microsoft ahora llama "workbook link (previously called
  an external reference)", con el nombre del archivo entre corchetes, como
  `='C:\Reports\[SourceWorkbook.xlsx]Sheet1'!$A$1`. Esto sale de resúmenes del buscador: las
  páginas dieron error al abrirlas.
- **Sheets** no acepta la referencia directa: según Google, para otra hoja de cálculo "you must
  use the IMPORTRANGE function", con la sintaxis `IMPORTRANGE(spreadsheet_url, range_string)`. La
  primera vez pide permiso para conectar los dos archivos. Cada cuánto se actualiza está en
  [errores de fórmula](errores-de-formula.md#el-recálculo-y-las-funciones-volátiles).

Un vínculo entre archivos es frágil: si el archivo de origen se mueve, cambia de nombre o se
borra, la referencia se rompe. Cuando varias planillas dependen de los mismos datos, eso suele
ser señal de que los datos piden otro lugar, como cuenta
[cuándo pasar a una base](../cuando-pasar-a-una-base.md). Esto último es inferencia.

## Cómo se rompe una referencia

- **Borrar lo que apunta.** Si se borra la fila, columna u hoja a la que apunta una fórmula, la
  referencia se pierde y la fórmula da #¡REF!; Microsoft da como causa las celdas que "se
  eliminan o se pegan encima".
- **Copiar con la referencia equivocada.** Una celda que debía ser absoluta queda relativa y se
  corre; el resultado da un número plausible y equivocado.
- **Rangos que no crecen.** `=SUMA(D2:D100)` no suma la fila 101 cuando se agrega una venta. Una
  tabla estructurada o una columna entera (`D:D`) lo evita.
- **Apuntar a sí misma.** Una fórmula que termina dependiendo de su propia celda es una
  referencia circular.

Los mensajes de error están en [errores de fórmula](errores-de-formula.md), y cómo encontrar
referencias mal puestas que no dan error, en [revisar una planilla](../Diseno-de-planillas/revisar-una-planilla.md).
