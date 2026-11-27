---
resumen: >-
  Apps Script es el lenguaje de programación de Google Workspace, basado en JavaScript, con el que
  se automatiza Google Sheets: se escriben funciones propias para usar en celdas y programas que
  corren solos cuando alguien abre o edita la planilla, o a una hora fija, dentro de cuotas de
  tiempo y de uso.
estado: vigente
estabilidad: semi
fuentes:
  - "Google, Custom Functions in Google Sheets: https://developers.google.com/apps-script/guides/sheets/functions"
  - "Google, Triggers (Apps Script): https://developers.google.com/apps-script/guides/triggers"
  - "Google, Quotas for Google Services (Apps Script): https://developers.google.com/apps-script/guides/services/quotas"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
aliases: [Google Apps Script, GAS, scripts de Google Sheets, funciones personalizadas, custom functions, disparadores, triggers]
creado: 2026-11-27
revisado: 2026-11-27
---

# Apps Script

Apps Script es el lenguaje de programación de Google Workspace, basado en JavaScript, con el que se automatiza Google Sheets: se escriben funciones propias para usar en celdas y programas que corren solos cuando alguien abre o edita la planilla, o a una hora fija, dentro de cuotas de tiempo y de uso.

Cumple en Sheets el papel que en Excel cumplen las [macros](macros.md) de VBA y los Office Scripts, con una diferencia de fondo: corre en los servidores de Google, no en la computadora de quien abre el archivo. Eso le saca el problema de las macros bloqueadas por venir de internet y le pone otro: cuotas de tiempo que cortan un programa largo. Se abre desde el menú Extensiones, Apps Script, de la propia planilla.

## Dos formas de usarlo

Apps Script sirve para dos cosas distintas en una planilla, y cada una tiene sus reglas.

**Funciones personalizadas.** Son funciones que se escriben en JavaScript, se marcan con la etiqueta `@customfunction` y después se usan en una celda como cualquier otra, por ejemplo `=PRECIOCONRECARGO(B2)`. Tienen límites estrictos, según la guía de Google:

- "A custom function call must return within 30 seconds." Si tarda más, la celda muestra `#ERROR!`.
- No pueden usar servicios que piden autorización, como leer el correo.
- No pueden modificar otras celdas: solo devuelven un valor a la celda donde están (o a las vecinas, si devuelven un arreglo).
- Cada celda que usa la función hace una llamada al servidor. Para muchas filas, Google recomienda que la función reciba un rango entero y devuelva un arreglo de dos dimensiones, en lugar de copiarla en mil celdas.

Antes de escribir una, conviene revisar si una fórmula ya lo resuelve: con LET y LAMBDA, Sheets permite nombrar cálculos sin programar, como cuenta [matrices dinámicas](../Formulas/matrices-dinamicas.md).

**Programas con disparadores.** Un disparador (*trigger*) hace que una función corra sola ante un evento. Hay dos clases:

| | Disparadores simples | Disparadores instalables |
|---|---|---|
| Cómo se crean | Con nombres reservados, como `onOpen` u `onEdit` | Se activan explícitamente |
| Eventos | Abrir o editar la planilla, entre otros | También por tiempo (cada hora, cada día), al editar o al recibir un formulario |
| Límites | No pueden correr más de 30 segundos, no usan servicios que piden autorización (como Gmail) ni abren otros archivos | Pueden usar servicios autorizados, dentro de las cuotas |
| Cuándo no se activan | Si quien abre el archivo solo puede ver o comentar | — |

Un ejemplo de negocio: un disparador por tiempo que todos los días a las 8 revisa la hoja de stock y manda un correo con los productos que quedaron por debajo del mínimo. Eso pide un disparador instalable, porque mandar correo requiere autorización.

## Las cuotas que cortan un programa

Google limita cuánto puede correr Apps Script. Copiado de la tabla de cuotas el 2026-11-27:

| Cuota | Cuenta personal | Google Workspace |
|---|---|---|
| Tiempo de ejecución de un script | 6 min por ejecución | 6 min por ejecución |
| Tiempo total de disparadores por día | 90 min | 6 h |
| Tiempo de una función personalizada | 30 s | 30 s |
| Destinatarios de correo por día | 100 | 1.500 |

La tabla de correos lleva un asterisco cuyo texto no se pudo leer. Las cuotas cambian: la [página de cuotas](https://developers.google.com/apps-script/guides/services/quotas) es la fuente viva.

Para un comercio chico, la cuota que más se nota es la de 6 minutos: un programa que recorre miles de filas de a una celda por vez se corta a la mitad. La solución es la misma que para las funciones personalizadas, leer y escribir rangos enteros de una vez.

## Cómo falla

Un script que nadie más entiende deja a la planilla dependiendo de quien lo escribió, igual que una macro (inferencia, sin fuente). Un disparador `onEdit` que reescribe celdas puede pelearse con lo que carga la gente: Google documenta que `onEdit()` encola hasta dos eventos, así que ediciones rápidas pueden quedar sin procesar. Y un script que pega valores sobre fórmulas rompe la separación de [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md) sin que nadie lo vea (también inferencia). Que quién puede editar el script dependa de los permisos del archivo es una suposición sin fuente (ver la nota de abajo); los permisos los explica [compartir y colaborar](compartir-y-colaborar.md).

> [!NOTE] Sin fuente todavía: si Sheets tiene una grabadora de macros que genera Apps Script, y la página oficial sobre quién puede ver y editar el script de una planilla compartida.
