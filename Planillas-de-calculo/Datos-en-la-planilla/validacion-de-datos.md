---
resumen: >-
  La validación de datos es una regla que se le pone a una celda o rango para que solo acepte ciertos
  valores (una lista desplegable, un número en un rango, una fecha), y que rechaza o advierte lo que
  no cumple. Frena los errores de carga antes de que lleguen a las fórmulas.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Apply data validation to cells: https://support.microsoft.com/en-us/office/apply-data-validation-to-cells-29fecbcc-d1b9-42c1-9d76-eff3ce5f7249"
  - "Google, Create a drop-down list: https://support.google.com/docs/answer/186103"
  - "Karl W. Broman y Kara H. Woo, Data Organization in Spreadsheets, The American Statistician 72(1), 2018: https://kbroman.org/Paper_DataOrg/manuscript.html"
aliases: [data validation, validación, lista desplegable, drop-down list, desplegable, dropdown]
creado: 2026-11-27
revisado:
---

# Validación de datos

La validación de datos es una regla que se le pone a una celda o rango para que solo acepte ciertos
valores (una lista desplegable, un número en un rango, una fecha), y que rechaza o advierte lo que
no cumple. Frena los errores de carga antes de que lleguen a las fórmulas.

## Qué error de carga evita

Una planilla de ventas que carga a mano el nombre del producto termina con "Yerba 1kg", "yerba 1 kg"
y "Yerba x 1 kilo" como tres productos distintos. La tabla dinámica los muestra en tres filas y la
suma por producto da mal sin dar error. Una lista desplegable con los productos del catálogo obliga a
elegir uno de ellos, y el problema no aparece. Broman y Woo la recomiendan por eso, como parte de
cargar los datos de forma consistente ([datos ordenados](datos-ordenados.md)).

Los usos más comunes en un negocio chico:

- **Lista**: producto, rubro, medio de pago, sucursal. La lista sale mejor de un rango (el catálogo
  de productos) que escrita a mano, porque se actualiza en un solo lugar.
- **Número entero o decimal en un rango**: cantidad mayor que cero, descuento entre 0 y 30 %.
- **Fecha**: que la fecha de venta no sea futura ni de otro año.
- **Personalizada, con fórmula**: que el código de cliente no se repita, por ejemplo.

## Qué tipos de regla hay en Excel y en Sheets

En Excel, los tipos son Whole Number, Decimal, List, Date, Time, Text Length y Custom; la última
acepta una fórmula. Una lista escrita a mano se separa con comas. Sheets organiza la regla alrededor
de la lista desplegable y la muestra en tres estilos: Chip, Arrow o Plain text. Solo el estilo chip
permite elegir varios valores en la misma celda, y la lista se actualiza sola si cambia el rango de
origen.

## Rechazar o advertir: la diferencia que más importa

Lo que pasa cuando alguien escribe un valor fuera de la regla cambia entre las dos aplicaciones:

| | Excel | Google Sheets |
|---|---|---|
| Por defecto | rechaza (estilo Stop) | rechaza |
| Niveles | tres: Stop, Warning, Important | dos: rechazar o advertir |
| Cómo se cambia | pestaña Error Alert | "Show a warning" en las opciones avanzadas |

En Excel, Stop pide "Require users to fix the error before proceeding"; Warning pregunta y deja
elegir Yes o No; y el tercero deja seguir después de cerrar el mensaje. La página de Microsoft que se
leyó llama Important al tercer estilo.

> [!NOTE]
> Sin fuente todavía: si en la interfaz de Excel en inglés el tercer estilo figura como
> "Information" en lugar de "Important"; la página leída solo nombra Important.

Advertir sirve cuando el valor raro puede ser legítimo (un precio fuera de lo habitual) y rechazar,
cuando no hay excepción posible (un producto que no está en el catálogo).

## Dónde deja de proteger

En Excel, la validación no se puede cambiar si el libro está compartido en el modo antiguo o si la
hoja está protegida. La validación tampoco es una barrera completa: es una ayuda para quien carga.
Para que otro no toque fórmulas ni supuestos hace falta además proteger rangos, como cuenta
[compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md).

> [!NOTE]
> Sin fuente todavía: que pegar sobre una celda con validación borra o saltea la regla, que es la
> limitación práctica más conocida, y la opción de Excel para marcar con un círculo los datos que ya
> no cumplen ("Circle invalid data"). Ninguna de las dos páginas oficiales leídas los cubre.

## Qué leer

Las dos páginas oficiales son cortas. En la de Microsoft, la sección "Error Alert"; en la de Google,
"Advanced options", donde está la opción de advertir en vez de rechazar.
