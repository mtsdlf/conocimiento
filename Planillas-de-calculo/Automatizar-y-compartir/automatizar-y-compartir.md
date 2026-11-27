---
resumen: >-
  Automatizar y compartir reúne lo que pasa cuando una planilla deja de ser de una persona y de una
  sola vez: los programas que repiten tareas dentro de ella (macros de Excel, Apps Script de Google
  Sheets) y las reglas para que varias personas trabajen sobre el mismo archivo sin pisarse.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, Macros from the internet are blocked by default in Office (actualizada 2026-07-17): https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked"
  - "Microsoft Learn, Office Scripts in Excel (2026-02-26): https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel"
  - "Google, Custom Functions in Google Sheets: https://developers.google.com/apps-script/guides/sheets/functions"
  - "Google, Proteger rangos y hojas: https://support.google.com/docs/answer/1218656"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
aliases: [automatización de planillas, spreadsheet automation, colaboración en planillas, macros y scripts]
creado: 2026-11-27
revisado:
---

# Automatizar y compartir

Automatizar y compartir reúne lo que pasa cuando una planilla deja de ser de una persona y de una sola vez: los programas que repiten tareas dentro de ella (macros de Excel, Apps Script de Google Sheets) y las reglas para que varias personas trabajen sobre el mismo archivo sin pisarse.

Son dos cosas distintas que aparecen juntas. Automatizar es escribir o grabar un programa; compartir es una cuestión de quién puede tocar qué, y no programa nada. Están en la misma vertical porque las dos llegan cuando la planilla ya funciona y empieza a usarse más: alguien repite todos los lunes la misma limpieza del listado de ventas, o tres personas cargan pedidos en el mismo archivo. Las dos se apoyan en un [diseño](../Diseno-de-planillas/diseno-de-planillas.md) que separa entradas, cálculo y salidas: una macro que escribe en la hoja de supuestos o un compañero que edita la hoja de cálculo rompen lo mismo.

## Antes de programar, lo que la planilla ya hace sola

Muchas tareas que parecen pedir una macro se resuelven sin programar. Importar y limpiar el mismo archivo cada mes es trabajo de [Power Query](../Datos-en-la-planilla/power-query.md) en Excel, que guarda los pasos y los repite. Un resumen que se rehace a mano se resuelve con una [tabla dinámica](../Analisis/tabla-dinamica.md) o con [matrices dinámicas](../Formulas/matrices-dinamicas.md). Lo que sigue necesitando un programa es lo que mueve cosas: mandar un correo cuando el stock baja, copiar pedidos de una hoja a otra, armar un archivo por cliente.

> [!NOTE] Sin fuente todavía: el orden «primero fórmulas y Power Query, después macros» es criterio de práctica de esta base; ninguna fuente leída lo formula así.

## Excel y Sheets automatizan con lenguajes distintos

Cada aplicación tiene su lenguaje, y no se traducen entre sí:

| | Excel | Google Sheets |
|---|---|---|
| Lenguaje clásico | VBA, en el Excel de escritorio | Apps Script (JavaScript) |
| Automatización en la web | Office Scripts | Apps Script, que ya vive en la web |
| Grabar sin programar | Grabadora de macros (VBA) y grabadora de acciones (Office Scripts) | Sin dato verificado |
| Correr por un evento o un horario | Power Automate; la programación propia de Office Scripts está suspendida | Disparadores de Apps Script |
| Función propia en una celda | Sin dato en lo investigado | Funciones personalizadas con `@customfunction` |

El riesgo también es distinto. Las macros de VBA son, según Microsoft, "a common way for malicious actors to gain access to deploy malware and ransomware", y por eso Office en Windows las bloquea en los archivos que vienen de internet. Apps Script corre en los servidores de Google con cuotas de tiempo y de uso. Los detalles están en [macros](macros.md) y en [Apps Script](apps-script.md).

## Una sola copia, varias personas

Compartir bien empieza por tener un solo archivo en la nube en lugar de copias que viajan por mail: es el mismo principio del ICAEW de un solo lugar por dato, llevado al archivo entero. Después vienen los permisos (quién ve, comenta o edita), la protección de rangos para que nadie pise las fórmulas, y el historial de versiones para volver atrás. Sheets trae todo eso de fábrica (la coautoría sin condiciones es inferencia de que el archivo siempre vive en la nube, sin fuente que lo diga); Excel lo tiene con condiciones (archivo en OneDrive o SharePoint, suscripción a Microsoft 365). La comparación está en [compartir y colaborar](compartir-y-colaborar.md).

Cuando varias personas cargan los mismos registros todo el tiempo, compartir la planilla deja de alcanzar y aparecen las señales de [pasar a una base](../cuando-pasar-a-una-base.md).

## Qué hay adentro de Automatizar y compartir

- [Macros](macros.md) — VBA y la grabadora en el Excel de escritorio, el bloqueo de macros de internet y Office Scripts con Power Automate.
- [Apps Script](apps-script.md) — automatizar Google Sheets: funciones personalizadas, disparadores y cuotas.
- [Compartir y colaborar](compartir-y-colaborar.md) — coautoría en Excel, permisos y protección en Sheets, historial de versiones y por qué una sola copia.
