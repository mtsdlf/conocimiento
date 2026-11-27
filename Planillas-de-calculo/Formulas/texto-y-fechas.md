---
resumen: >-
  Las funciones de texto parten, unen y limpian lo que hay en una celda (un código, un nombre, una
  descripción), y las de fecha arman fechas, calculan plazos y sacan el mes o el año. Juntas
  preparan los datos para que las búsquedas y los resúmenes funcionen.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft, Referencia de funciones de texto: https://support.microsoft.com/es-es/excel/text-functions-reference"
  - "Microsoft, páginas de IZQUIERDA, DERECHA, EXTRAE, LARGO, ESPACIOS, LIMPIAR, CONCAT, UNIRCADENAS, TEXTO y VALOR: https://support.microsoft.com/es-es/excel/functions/<nombre-en-inglés>-function (p. ej. https://support.microsoft.com/es-es/excel/functions/trim-function)"
  - "Microsoft, páginas de FECHA, HOY, AHORA, DIAS.LAB, FIN.MES, FECHA.MES, MES y AÑO: https://support.microsoft.com/es-es/excel/functions/<nombre-en-inglés>-function (p. ej. https://support.microsoft.com/es-es/Excel/functions/date-function)"
  - "Microsoft, Función DIVIDIRTEXTO: https://support.microsoft.com/es-es/office/dividirtexto-función-dividirtexto-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7 (según un resumen)"
  - "Microsoft, Función SIFECHA: https://support.microsoft.com/es-es/office/sifecha-función-sifecha-25dba1a4-2812-480b-84dd-8b32a451b35c (según un resumen)"
  - "Google, SPLIT: https://support.google.com/docs/answer/3094136?hl=es"
  - "Google, UNIRCADENAS: https://support.google.com/docs/answer/7013992?hl=es"
  - "Google, TEXTO: https://support.google.com/docs/answer/3094139?hl=es"
  - "Google, Lista de funciones de Hojas de cálculo de Google: https://support.google.com/docs/table/25273?hl=es"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, sección 2.4; páginas leídas el 2026-11-27"
aliases: [funciones de texto, text functions, funciones de fecha, date functions, IZQUIERDA, LEFT, EXTRAE, MID, ESPACIOS, TRIM, CONCAT, UNIRCADENAS, TEXTJOIN, TEXTO, TEXT, DIVIDIRTEXTO, TEXTSPLIT, SPLIT, FECHA, DATE, HOY, TODAY, DIAS.LAB, NETWORKDAYS, FIN.MES, EOMONTH, SIFECHA, DATEDIF]
creado: 2026-11-27
revisado: 2026-11-27
---

# Texto y fechas

Las funciones de texto parten, unen y limpian lo que hay en una celda (un código, un nombre, una
descripción), y las de fecha arman fechas, calculan plazos y sacan el mes o el año. Juntas
preparan los datos para que las búsquedas y los resúmenes funcionen.

Los datos de un negocio rara vez llegan limpios: un código de producto que trae la categoría
pegada, un nombre con espacios al final, una fecha de un sistema que entra como texto. Para una
limpieza que se repite cada mes, [Power Query](../Datos-en-la-planilla/power-query.md) la hace una
vez y la guarda; las funciones de esta nota sirven para arreglos dentro de la planilla. La
limpieza de datos en general (ordenar la tabla, faltantes, duplicados, atípicos) está en
[limpieza de datos](../../Datos/Analisis/limpieza-de-datos.md), del tema Datos.

## Partir un texto

IZQUIERDA (LEFT), DERECHA (RIGHT) y EXTRAE (MID) sacan una parte de un texto por posición, y
LARGO (LEN) cuenta sus caracteres; según Microsoft, "los espacios se cuentan como caracteres".
Sintaxis según Microsoft: `IZQUIERDA(texto; [núm_de_caracteres])`, que toma 1 si se omite el
segundo argumento, y `EXTRAE(texto; posición_inicial; núm_de_caracteres)`. Si el código de
producto es `ALM-00123`, con la categoría en las tres primeras letras:

```
=IZQUIERDA(A2; 3)          → ALM
=EXTRAE(A2; 5; 5)          → 00123
```

El resultado es texto aunque parezca número: `00123` no se encuentra en una lista donde el código
es el número 123. Para convertirlo está VALOR (VALUE), aunque Microsoft aclara que "por lo general,
no es necesario usar la función VALOR". Esa trampa se explica en
[tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md).

Cuando el texto tiene un separador (una coma, un guion), partir por posición no alcanza. Excel
tiene DIVIDIRTEXTO (TEXTSPLIT), cuya sintaxis según Microsoft es
`=DIVIDIRTEXTO(texto, col_delimiter, [row_delimiter], [ignore_empty], [match_mode], [pad_with])`;
vuelca cada parte en una celda y con varios delimitadores usa una constante como `{",","."}`.
Sheets usa SPLIT, que conserva el nombre en inglés en castellano:
`SPLIT(texto; delimitador; [dividir_por_carácter]; [quitar_texto_vacío])`. Según Google, por defecto
"cada carácter del delimitador se tiene en cuenta individualmente": con `", "` como delimitador
parte por la coma y también por el espacio. No se encontró TEXTSPLIT en la lista de funciones de
Sheets.

## Limpiar espacios y caracteres invisibles

ESPACIOS (TRIM) quita los espacios del principio, del final y los dobles: según Microsoft, "elimina
los espacios del texto, excepto el espacio normal que se deja entre palabras". Es lo primero que
se prueba cuando una búsqueda no encuentra un nombre que está a la vista. LIMPIAR (CLEAN) elimina
los caracteres que no se imprimen.

Las dos tienen límites que explican muchos "no lo encuentra":

- ESPACIOS no quita el espacio de no separación, el carácter 160, que suele venir al copiar de una
  página web o un sistema. Microsoft: "Por sí sola, la función ESPACIOS no quita los espacios de no
  separación." Hay que reemplazarlo antes con SUSTITUIR.
- LIMPIAR quita los caracteres del 0 al 31, pero no los "valores 127, 129, 141, 143, 144 y 157".

> [!NOTE]
> La página de Microsoft en es-es sobre ESPACIOS se titula "Función SUPRESP" y sus ejemplos usan
> RECORTAR, TRIM y SUPRESP; la sintaxis y la lista de funciones de Sheets dicen ESPACIOS. Qué
> nombre acepta Excel en cada configuración en castellano no se verificó.

## Unir textos

CONCAT une textos uno detrás de otro y, según Microsoft, "reemplaza la función CONCATENAR", que
sigue por compatibilidad. UNIRCADENAS (TEXTJOIN) une con un separador y puede saltear las celdas
vacías: `UNIRCADENAS(delimitador; ignorar_vacío; texto1; [texto2]; ...)`. Para armar una dirección
de envío desde tres columnas:

```
=UNIRCADENAS(", "; VERDADERO; B2; C2; D2)
```

El operador `&` hace lo mismo que CONCAT en lo simple: `=B2&" "&C2`. UNIRCADENAS existe con el
mismo nombre en Sheets.

## Dar formato de texto a un número

TEXTO (TEXT) convierte un número en texto con un formato, por ejemplo `=TEXTO(B2; "0,00")` para
un importe con dos decimales dentro de una frase. Microsoft advierte que "convierte los números en texto,
lo que puede dificultar la referencia en cálculos posteriores", y que el separador de miles
"depende de la configuración regional". Por eso TEXTO va al final, para mostrar (en una etiqueta,
en una frase), y no en el medio de un cálculo. En Sheets se llama igual y, según Google, no admite
asteriscos ni el patrón con `?` en el formato.

> [!NOTE]
> Sin fuente todavía: que los códigos de formato de TEXTO cambien según el idioma de la planilla
> (por ejemplo, "aaaa" o "yyyy" para el año), que es una trampa conocida al compartir archivos
> entre configuraciones. La página de Microsoft solo menciona la configuración regional para los
> separadores.

## Armar una fecha y calcular plazos

Como una fecha es un número de días (ver [tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md)),
sumar y restar funciona directo: `=A2+30` es el vencimiento a 30 días y `=B2-A2` los días entre dos
fechas. Las funciones cubren lo que la resta no hace:

| Función (castellano / inglés) | Qué hace, según Microsoft | Ejemplo de negocio |
|---|---|---|
| FECHA / DATE | arma la fecha desde año, mes y día: `FECHA(año; mes; día)` | juntar tres columnas de un sistema viejo |
| HOY / TODAY | la fecha actual, sin argumentos: `=HOY()` | días de atraso de una factura: `=HOY()-C2` |
| AHORA / NOW | fecha y hora actuales | marcar cuándo se actualizó un tablero |
| FIN.MES / EOMONTH | el último día del mes, N meses antes o después | el cierre del mes de una venta: `=FIN.MES(A2; 0)` |
| FECHA.MES / EDATE | la misma fecha N meses después | el vencimiento de una cuota mensual |
| DIAS.LAB / NETWORKDAYS | los días hábiles entre dos fechas, sin fines de semana ni los feriados que se le pasen | plazo de entrega en días hábiles |
| MES / MONTH y AÑO / YEAR | el número de mes (1 a 12) o el año | una columna de mes para agrupar ventas |

Microsoft recomienda escribir el año de FECHA con cuatro dígitos: los años de 0 a 1899 se toman
sumándoles 1900. DIAS.LAB acepta una lista de feriados como tercer argumento; para fines de semana
distintos del sábado y domingo está DIAS.LAB.INTL. HOY y AHORA se recalculan cada vez que la
planilla recalcula, lo que las hace volátiles: el efecto en una planilla grande está en
[errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md#el-recálculo-y-las-funciones-volátiles).
Microsoft dice de AHORA que "solo cambian cuando se realiza un cálculo en la hoja de cálculo o
cuando se ejecuta una macro… No se actualiza constantemente".

Sheets tiene HOY, FIN.MES, FECHA.MES y DIAS.LAB con los mismos nombres en castellano.

## SIFECHA calcula edades y antigüedades, con fallas conocidas

SIFECHA (DATEDIF) da la diferencia entre dos fechas en años, meses o días:
`SIFECHA(fecha_inicial; fecha_final; unidad)`, con unidades "Y", "M", "D", "MD", "YM" y "YD". Sirve
para la antigüedad de un empleado o de un cliente en años cumplidos. Microsoft la incluye "por
compatibilidad con Lotus 1-2-3" y advierte que puede dar resultados incorrectos: con "MD" puede dar
un número inexacto, cero o negativo, y no la recomienda. Si la fecha inicial es posterior a la
final, da #¡NUM!.

> [!NOTE]
> Sin fuente todavía: la página de Google de DATEDIF en Sheets, y si tiene las mismas fallas.

## Qué cambia entre Excel y Sheets

Casi todas las funciones de texto y fecha tienen el mismo nombre en castellano en las dos, según
la lista de funciones de Google: IZQUIERDA, DERECHA, EXTRAE, LARGO, ESPACIOS, LIMPIAR, VALOR,
TEXTO, UNIRCADENAS, HOY, DIAS.LAB, FIN.MES y FECHA.MES. En esa lista no se verificaron FECHA,
AHORA, MES, AÑO ni CONCAT. Las diferencias:

- Para partir texto, Excel usa DIVIDIRTEXTO y Sheets usa SPLIT, con argumentos y comportamiento
  distintos.
- DIVIDIRTEXTO y UNIRCADENAS no existen en las versiones más viejas de Excel, que todavía circulan;
  cuáles, en la [ficha de equivalencias](equivalencias-de-funciones.md).
- Sheets interpreta las fechas según la configuración regional de la hoja, y Excel según la del
  sistema de cada computadora (ver [tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md#la-configuración-regional-decide-la-coma-y-el-punto)).
