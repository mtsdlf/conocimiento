---
resumen: >-
  Cada celda guarda un valor de un tipo (número, texto, fecha, verdadero o falso) y lo muestra con
  un formato que puede ocultar el tipo real. Una fecha es un número de días con formato de fecha, y
  un número guardado como texto se ve igual pero no suma ni se encuentra al buscarlo.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, Excel incorrectly assumes that the year 1900 is a leap year (actualizada 2026-04-15): https://learn.microsoft.com/en-us/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year"
  - "Microsoft, Date systems in Excel: https://support.microsoft.com/en-us/office/date-systems-in-excel-e7fe7167-48a9-4b96-bb53-5612a800b487 (según un resumen)"
  - "Microsoft, Función FECHA: https://support.microsoft.com/es-es/Excel/functions/date-function"
  - "Microsoft Learn, How to correct formula errors (separador de listas): https://learn.microsoft.com/en-us/office/troubleshoot/excel/formula-errors"
  - "Google, TO_DATE: https://support.google.com/docs/answer/3094239 (según un resumen)"
  - "Google, Ajustes de hoja de cálculo (configuración regional y cálculo): https://support.google.com/docs/answer/58515 (según un resumen)"
  - "Microsoft, VLOOKUP function: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1 (según un resumen)"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, secciones 1.1 y 1.2"
aliases: [tipo de dato, data type, número como texto, formato de celda, número de serie de fecha, date serial number, configuración regional, locale]
creado: 2026-11-27
revisado:
---

# Tipos de dato

Cada celda guarda un valor de un tipo (número, texto, fecha, verdadero o falso) y lo muestra con
un formato que puede ocultar el tipo real. Una fecha es un número de días con formato de fecha, y
un número guardado como texto se ve igual pero no suma ni se encuentra al buscarlo.

Muchos "números raros" de una planilla vienen de acá: una suma que da menos de lo que debería,
una búsqueda que no encuentra un código que está a la vista, una fecha que aparece como 45000. La
[celda](celda-y-referencia.md) tiene dos capas, el valor y el formato, y las fórmulas trabajan con
el valor.

## El formato cambia cómo se ve, no lo que vale

El formato de celda decide si un valor se muestra como `1500`, `$ 1.500,00`, `15 %` o con dos
decimales. No cambia el valor: una celda que muestra `$ 1.500` puede valer 1499,6, y la suma usa
1499,6. Por eso un total puede no coincidir con la suma de lo que se ve en pantalla, y la
diferencia es de redondeo de formato, no un error de la fórmula. Si el número tiene que quedar
redondeado de verdad (un precio de lista), se redondea con una función, no con el formato.

> [!NOTE]
> Sin fuente todavía: la página oficial de Microsoft o Google que explique formato contra valor y
> el redondeo de lo mostrado.

## Una fecha es un número de días

Excel y Sheets guardan cada fecha como un número de serie: la cantidad de días desde una fecha de
origen. La hora es la parte decimal: 0,5 es mediodía. Microsoft lo dice así: "Excel almacena las
fechas como números de serie secuenciales para que se puedan usar en cálculos", y "la fecha 1 de
enero de 1900 es el número de serie 1". En ese sistema de fechas 1900, el predeterminado de Excel
para Windows, el 5/7/2011 es el número 40729. Google dice que
Sheets cuenta los días desde el 30/12/1899, con valores negativos para fechas anteriores y
fracciones para la hora.

Que sea un número es lo que permite calcular: restar dos fechas da los días entre ellas, sumar 30
a una fecha da la fecha de vencimiento, y comparar con `>=` sirve para
[sumar por mes](../Formulas/sumar-y-contar-con-condiciones.md#sumar-por-mes-es-una-condición-de-dos-fechas).
Cuando una celda de fecha muestra un número como 45000, el valor está bien y le falta el formato
de fecha. Las funciones para armar y partir fechas están en
[texto y fechas](../Formulas/texto-y-fechas.md).

Hay dos detalles históricos que casi nunca importan en un negocio:

- **Excel cree que existió el 29 de febrero de 1900.** Lotus 1-2-3 suponía que 1900 era bisiesto,
  y Excel lo copió para que las planillas pasaran de un programa al otro con las mismas fechas.
  Microsoft dice que corregirlo es posible, pero "the disadvantages of doing so outweigh the
  advantages", porque correría un día casi todas las fechas guardadas. El único efecto que queda
  es que DIASEM (WEEKDAY) da valores incorrectos antes del 1/3/1900. El origen de Sheets en el
  30/12/1899 absorbe ese día falso, así que las dos herramientas coinciden desde marzo de 1900
  (esto último es inferencia de la investigación).
- **Existe un sistema 1904.** En él, el 5/7/2011 es el 39267, 1.462 días menos. Si se copian
  fechas entre libros con sistemas distintos, se corren cuatro años.

## Un número guardado como texto no es un número

Cuando un dato entra como texto (al pegar desde un sistema, al importar un CSV, al escribir un
apóstrofo adelante), la celda muestra `1500` pero guarda la palabra "1500". SUMA lo ignora, las
comparaciones fallan y las búsquedas no lo encuentran. Microsoft lo advierte en la página de
BUSCARV: números o fechas guardados como texto, y los espacios al principio o al final, dan
resultados incorrectos. Es la causa más común de un #N/A en una búsqueda que "debería andar" (ver
[funciones de búsqueda](../Formulas/funciones-de-busqueda.md)).

Las señales son un triángulo verde en la esquina de la celda en Excel, el número alineado a la
izquierda (el texto se alinea a la izquierda y los números a la derecha por defecto) o un
CONTAR que da menos que CONTARA. La conversión está en la página de Microsoft "Convertir números
almacenados como texto en números", y los espacios se quitan con ESPACIOS (ver
[texto y fechas](../Formulas/texto-y-fechas.md)). Lo mismo pasa con las fechas que entran como
texto: se ven como fecha pero no ordenan ni restan.

> [!NOTE]
> Sin fuente todavía: la página de Microsoft sobre números almacenados como texto solo se vio en
> un buscador, y las señales (triángulo verde, alineación) son conocimiento corriente sin fuente
> citada.

Para que no entren mal, la carga se controla con [validación de datos](../Datos-en-la-planilla/validacion-de-datos.md)
y las importaciones se limpian con [Power Query](../Datos-en-la-planilla/power-query.md).

## La configuración regional decide la coma y el punto

Qué es separador decimal, qué es separador de miles, cómo se escribe una fecha y con qué se
separan los argumentos de una función depende de la configuración regional. En una planilla en
castellano con coma decimal, `1,5` es un número y los argumentos van con punto y coma:
`=SUMA(A1;B1)`. En una en inglés, el decimal es el punto y el separador, la coma. Un CSV con
punto decimal abierto en una planilla con coma decimal puede convertir `1.500` en mil quinientos
o `3.10` en un texto o una fecha.

En Excel, el separador de argumentos es el "separador de listas" de la configuración regional de
Windows. Microsoft: "an error will occur if trying to use a symbol that isn't the default 'list
separator' in the Windows Regional settings", y "the comma is the default list separator for US -
English Locale". Por eso la misma fórmula se escribe con `,` en una computadora y con `;` en otra,
y una fórmula copiada de un foro en inglés da error hasta cambiar las comas. El mismo separador
decide el delimitador con que Excel lee y guarda los CSV.

En Sheets, el idioma y la zona horaria están en Archivo > Configuración > General, y según Google
fijan moneda, fecha y formato de número por hoja de cálculo, no por usuario: dos personas que
abren el mismo archivo ven el mismo formato.

> [!NOTE]
> Sin fuente todavía: que en Excel el separador de listas pase a `;` cuando el decimal es la coma
> (solo aparece en respuestas de foros), y que en Sheets el separador de argumentos cambie con la
> configuración regional de la hoja (solo aparece en sitios de terceros).
