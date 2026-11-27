---
resumen: >-
  Un error de fórmula es el valor que muestra una celda cuando la fórmula no puede calcular: un
  valor no encontrado, una referencia rota, una división por cero. Cada error nombra una causa
  distinta y se propaga a todo lo que depende de esa celda; las referencias circulares y el
  recálculo explican los otros dos síntomas, la planilla lenta y el valor viejo.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft, Corregir un error #N/A: https://support.microsoft.com/es-es/excel/how-to-correct-a-n-a-error"
  - "Microsoft, Cómo corregir un error #¡VALOR!: https://support.microsoft.com/es-es/excel/how-to-correct-a-value-error"
  - "Microsoft, Cómo corregir un error #¡REF!: https://support.microsoft.com/es-es/excel/how-to-correct-a-ref-error"
  - "Microsoft, Cómo corregir un error #¡DIV/0!: https://support.microsoft.com/es-es/excel/how-to-correct-a-div-0-error"
  - "Microsoft, Cómo corregir un error #¿NOMBRE?: https://support.microsoft.com/es-es/excel/how-to-correct-a-name-error"
  - "Microsoft, Cómo corregir un error #¡NUM!: https://support.microsoft.com/es-es/excel/how-to-correct-a-num-error"
  - "Microsoft, Cómo corregir un error #DESBORDAMIENTO!: https://support.microsoft.com/es-es/excel/how-to-correct-a-spill-error"
  - "Microsoft, Cómo corregir un error #CALC!: https://support.microsoft.com/es-es/excel/how-to-correct-a-calc-error"
  - "Microsoft, Quitar o permitir una referencia circular en Excel: https://support.microsoft.com/es-es/excel/remove-or-allow-a-circular-reference-in-excel"
  - "Microsoft Learn, Excel Recalculation (aplica a Excel 2013): https://learn.microsoft.com/en-us/office/client-developer/excel/excel-recalculation"
  - "Microsoft Learn, Excel performance: Improving calculation performance: https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-improving-calculation-performance"
  - "Exceljet, Volatile function: https://exceljet.net/glossary/volatile-function"
  - "Microsoft, Función HOY: https://support.microsoft.com/es-es/excel/functions/today-function"
  - "Google, TIPO.DE.ERROR (ERROR.TYPE): https://support.google.com/docs/answer/3238305?hl=es"
  - "Google, Ajustes de hoja de cálculo: https://support.google.com/docs/answer/58515"
  - "Google, IMPORTRANGE: https://support.google.com/docs/answer/3093340"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, sección 1.2; páginas leídas el 2026-11-27 a través de un resumidor"
aliases: [error de fórmula, formula error, "#N/A", "#N/D", "#¡REF!", "#REF!", "#¡VALOR!", "#VALUE!", "#¡DIV/0!", "#¿NOMBRE?", "#NAME?", referencia circular, circular reference, recálculo, recalculation, función volátil, volatile function]
creado: 2026-11-27
revisado: 2026-11-27
---

# Errores de fórmula

Un error de fórmula es el valor que muestra una celda cuando la fórmula no puede calcular: un
valor no encontrado, una referencia rota, una división por cero. Cada error nombra una causa
distinta y se propaga a todo lo que depende de esa celda; las referencias circulares y el
recálculo explican los otros dos síntomas, la planilla lenta y el valor viejo.

Un error visible es la falla barata: avisa. La falla cara es la que no da error: una fórmula que apunta
a la celda equivocada y devuelve un número creíble; de esa se ocupan
[errores en planillas](../Diseno-de-planillas/errores-en-planillas.md) y
[revisar una planilla](../Diseno-de-planillas/revisar-una-planilla.md). Leer un error empieza por
la celda donde nace: como se propaga, el total que muestra #¡REF! puede no tener la culpa, y hay
que seguir sus precedentes (las celdas de las que toma valores) hasta la primera celda con error.

## Qué dice cada error

| Error en castellano | En inglés | Qué lo causa, según Microsoft | Ejemplo de negocio |
|---|---|---|---|
| #N/A | #N/A | una búsqueda no encontró el valor: no está, el tipo de dato no coincide, hay espacios de más, o se usó coincidencia aproximada | el código del producto no está en la lista de precios |
| #¡VALOR! | #VALUE! | un argumento del tipo equivocado: espacios ocultos, números o fechas guardados como texto, caracteres especiales | sumar una celda que dice "1.500 " con un espacio |
| #¡REF! | #REF! | la celda a la que apuntaba se borró o se pegó algo encima; un índice de columna fuera del rango de BUSCARV o INDICE | se borró la columna de costos que usaba el margen |
| #¡DIV/0! | #DIV/0! | dividir por cero o por una celda "con valor 0 o en blanco" | el margen de un producto que todavía no vendió |
| #¿NOMBRE? | #NAME? | una función o un nombre mal escrito o no definido, comillas faltantes, falta el `:` de un rango | `=SUMAR(A1:A5)` en vez de SUMA, o BUSCARX en un Excel que no la tiene |
| #¡NUM! | #NUM! | un número que la función no admite, una iteración que "no puede encontrar un resultado", un resultado demasiado grande o chico | una tasa que no converge |
| #DESBORDAMIENTO! | #SPILL! | una fórmula de varias celdas no tiene lugar libre para volcar el resultado | hay un dato debajo de un FILTRAR |
| #CALC! | #CALC! | una matriz que el cálculo no admite, por ejemplo un resultado vacío | un FILTRAR sin coincidencias y sin tercer argumento |

Los de #DESBORDAMIENTO! y #CALC! son propios de las [matrices dinámicas](../Formulas/matrices-dinamicas.md).
El #N/A de una búsqueda casi siempre es un problema de [tipos de dato](tipos-de-dato.md): el código
está, pero como texto en una lista y como número en la otra.

> [!IMPORTANT]
> La grafía de los errores en castellano no es uniforme ni en las fuentes oficiales. Las páginas
> de Microsoft en es-es escriben #N/A en la de ese error, y #N/D en la de DIVIDIRTEXTO; mezclan
> #REF! con #¡REF!, #DIV/0! con #¡DIV/0! y #NUM! con #¡NUM!; y escriben #DESBORDAMIENTO! y #CALC!
> sin signo de apertura. Las páginas de Google en castellano también mezclan: #VALOR! junto a
> #NAME? y #N/D junto a #N/A. Este tema usa la forma con signo de apertura donde Microsoft la usa
> en el título (#¡VALOR!, #¡REF!, #¿NOMBRE?) y #N/A. Qué muestra en pantalla cada aplicación
> según el idioma configurado no se verificó.

En Sheets, la función TIPO.DE.ERROR (ERROR.TYPE) devuelve un número por tipo de error, del 1 al
8: #NULL!, #DIV/0!, #VALOR!, #REF!, #NAME?, #NUM!, #N/A y "todos los demás errores".

> [!NOTE]
> Sin fuente todavía: una página de Google que liste los errores de Sheets y sus causas. El error
> #ERROR! de Sheets aparece en la guía oficial de funciones personalizadas de Apps Script, como lo que
> muestra la celda cuando la función tarda más de 30 segundos ([Apps Script](../Automatizar-y-compartir/apps-script.md));
> sus otras causas no se encontraron en páginas oficiales.

## Atrapar un error no es arreglarlo

SI.ERROR y SI.ND reemplazan un error por otro valor, y están en
[funciones lógicas](../Formulas/funciones-logicas.md). Sirven para errores esperados, como el
#¡DIV/0! de un producto sin ventas o el #N/A de un cliente nuevo. Usados para tapar cualquier
error, esconden justo los que avisan de un problema: Microsoft dice, para el #¿NOMBRE?, "No use
ninguna función de control de errores, como SI.ERROR, para enmascarar el error."

## Una fórmula que depende de sí misma

Según Microsoft, "una referencia circular se produce cuando una fórmula hace referencia a sí
misma, directa o indirectamente". Lo común es que sea un error: el total de la columna incluye su
propia celda, o el precio depende del margen que depende del precio. Excel la detecta y avisa.

A veces es a propósito: un cálculo que se resuelve por aproximación, como un interés que depende
del saldo que depende del interés. Para eso Excel tiene el cálculo iterativo ("Habilitar cálculo
iterativo" en Windows, "Usar cálculo iterativo" en Mac), que se detiene, según Microsoft, "después
de 100 iteraciones" o cuando los valores cambian "en un valor inferior a 0,001". Para un negocio
chico, una circular casi siempre se resuelve reordenando el cálculo; dejar el iterativo prendido
hace que las circulares accidentales dejen de avisar (esto es inferencia).

## El recálculo y las funciones volátiles

La planilla recalcula en cadena: cuando una celda cambia, recalcula lo que depende de ella (ver
[modelo de la planilla](modelo-de-la-planilla.md)). Las funciones volátiles rompen esa economía.
Microsoft define una función volátil como aquella "whose value cannot be assumed to be the same
from one moment to the next", y Excel la recalcula, con todo lo que depende de ella, en cada
recálculo de cualquier celda. La recomendación de Microsoft es "Use them sparingly". En una
planilla de ventas con miles de filas, un DESREF (OFFSET) o un INDIRECTO (INDIRECT) en cada fila
puede hacer que cada cambio tarde segundos (inferencia, sin medición que lo respalde).

> [!IMPORTANT]
> Las fuentes no coinciden en la lista de funciones volátiles. Las tres coinciden en AHORA (NOW),
> HOY (TODAY), DESREF (OFFSET), INDIRECTO (INDIRECT), CELDA (CELL) e INFO.
>
> - **Microsoft Learn, "Excel Recalculation"** (aplica a Excel 2013): NOW, TODAY, RANDBETWEEN,
>   OFFSET, INDIRECT, INFO y CELL según sus argumentos, y SUMIF según sus argumentos. No incluye
>   RAND.
> - **Microsoft Learn, "Improving calculation performance"**: "obviously volatile: RAND(), NOW(),
>   TODAY(). Others are less obviously volatile: OFFSET(), CELL(), INDIRECT(), INFO()". No incluye
>   RANDBETWEEN ni SUMIF, y aclara que INDEX, ROWS, COLUMNS y AREAS, documentadas antes como
>   volátiles, "are not in fact volatile".
> - **Exceljet**: NOW, TODAY, RAND, RANDARRAY, RANDBETWEEN, OFFSET, INDIRECT, y CELL e INFO según
>   sus argumentos. No incluye SUMIF.

La salida práctica es reemplazar DESREF e INDIRECTO por INDICE, que no es volátil, y poner HOY en
una sola celda a la que apunten las demás, en lugar de repetirla en cada fila (lo último es
inferencia).

Excel tiene tres modos de cálculo: automático, automático excepto [tablas de datos](../Analisis/analisis-de-escenarios.md), y manual. En
manual, F9 recalcula lo pendiente y Ctrl+Alt+F9 recalcula todo en todos los libros abiertos. Una
planilla en manual muestra valores viejos hasta que alguien recalcula: si un total no cambia al
cambiar un dato, lo primero es mirar el modo. La página de HOY lo dice para su caso: si no se
actualiza, revisar que las opciones de cálculo estén en "Automático".

En Sheets, el modo está en Archivo > Configuración > Cálculo, con automático y manual; según
Google, el manual es solo para editores y no existe en la app móvil. Google nombra como volátiles
a TODAY, NOW, RAND y RANDBETWEEN. Las funciones que
traen datos de afuera se recalculan solas cada cierto tiempo, y en eso Google se contradice:

> [!IMPORTANT]
> La página de IMPORTRANGE dice que la función "automatically checks for updates every hour while
> the document is open", y que se recarga al abrir el documento. La página de ajustes de la hoja
> de cálculo dice "ImportRange: 30 minutes" (y una hora para IMPORTHTML, IMPORTFEED, IMPORTDATA e
> IMPORTXML). No se resolvió cuál vale.

> [!NOTE]
> Sin fuente todavía: las opciones de recálculo de Sheets "Al cambiar", "Al cambiar y cada minuto"
> y "Al cambiar y cada hora" no aparecen en la página de ajustes de Google que se leyó.
