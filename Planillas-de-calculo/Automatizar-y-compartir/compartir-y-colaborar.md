---
resumen: >-
  Compartir y colaborar es trabajar varias personas sobre la misma planilla: un solo archivo en la
  nube que todos editan a la vez, con permisos que dicen quién ve, comenta o edita, rangos protegidos
  para que nadie pise las fórmulas y un historial de versiones para volver atrás.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft, Collaborate on Excel workbooks at the same time with co-authoring (según resumen; la URL con ID dio 403): https://support.microsoft.com/en-us/excel/get-started/collaborate-on-excel-workbooks-at-the-same-time-with-co-authoring"
  - "Microsoft, Excel specifications and limits: https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3"
  - "Google, Proteger rangos y hojas: https://support.google.com/docs/answer/1218656"
  - "Google, Ver el historial de versiones (según resumen): https://support.google.com/docs/answer/190843"
  - "ICAEW, Financial Modelling Code (2018, ed. 2024), principio #15: https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
aliases: [coautoría, co-authoring, colaboración en tiempo real, compartir una planilla, proteger rangos, protected ranges, historial de versiones, version history, permisos]
creado: 2026-11-27
revisado:
---

# Compartir y colaborar

Compartir y colaborar es trabajar varias personas sobre la misma planilla: un solo archivo en la nube que todos editan a la vez, con permisos que dicen quién ve, comenta o edita, rangos protegidos para que nadie pise las fórmulas y un historial de versiones para volver atrás.

No es automatización: no programa nada. Es una cuestión de quién puede tocar qué, y por eso se apoya en el [diseño](../Diseno-de-planillas/diseno-de-planillas.md): si la planilla separa [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md), se sabe qué hoja abrir a la edición y qué hoja proteger.

## Una sola copia en la nube, no copias por mail

La forma más común de compartir una planilla en un negocio chico es la peor: mandarla por mail. Cada adjunto es una copia nueva. La encargada carga las ventas del sábado en la suya, el dueño corrige un precio en la propia, y el lunes hay dos versiones de la verdad que alguien tiene que juntar a mano.

El argumento contra las copias es el principio #15 del ICAEW, un solo lugar por cada dato, llevado al archivo entero. También es lo que exige la coautoría de Excel, que solo funciona sobre un archivo guardado en la nube, y es la forma en que trabaja Sheets, donde el archivo siempre vive en la nube. Las copias por mail tienen además un costo concreto en Excel: un archivo con macros recibido como adjunto llega bloqueado en Windows, como explica [macros](macros.md).

> [!NOTE] Sin fuente todavía: ninguna fuente oficial cuantifica el riesgo de trabajar con copias por mail. Es un argumento de práctica, apoyado en el principio #15 del ICAEW y en cómo funciona la coautoría, no un dato medido.

## Coautoría en Excel: sí, con condiciones

En Excel varias personas pueden editar el mismo libro a la vez, pero no en cualquier archivo. Según la página de coautoría de Microsoft (vista por resumen), hace falta todo esto:

- El archivo guardado en OneDrive, OneDrive para la Empresa o una biblioteca de SharePoint Online. SharePoint local no la admite.
- Cada persona con una suscripción a Microsoft 365 y la última versión de Excel.
- Formato `.xlsx`, `.xlsm` o `.xlsb`. El formato Strict Open XML no la admite.
- AutoSave activado, para que todos vean los cambios y las selecciones de los demás en color.
- Que el archivo no esté protegido con IRM o RMS.

Editar macros durante la coautoría puede interrumpir a los demás. La ficha de límites de Excel da 256 usuarios a la vez en un libro compartido; las cifras de cada aplicación están en la [ficha de aplicaciones](../aplicaciones-de-planillas.md).

En Google Sheets la coautoría no tiene condiciones: el archivo vive en la nube y cualquiera con permiso de edición edita a la vez.

## Permisos y protección en Google Sheets

Sheets reparte el acceso en tres niveles: ver, comentar y editar. Los visores y los comentaristas no pueden cambiar la planilla.

> [!NOTE] Sin fuente todavía: la página oficial de compartir de Google respondió 404. Los tres niveles se deducen de la página de protección, que menciona editores, visores y comentaristas.

Dentro de los editores, se puede proteger un rango o una hoja entera para que solo la edite uno mismo, un dominio o una lista de personas. En la planilla de costos, la hoja de Cálculo y el Resumen quedan protegidos, y la de Supuestos abierta a quien carga los precios. Hay también una opción que solo muestra una advertencia al editar, sin bloquear.

Google es explícito sobre el alcance: "Protection isn't a security measure". Quien tiene acceso puede imprimir, copiar y pegar, importar y exportar copias, y los visores pueden hacer una copia propia. No hay contraseña. La protección sirve para evitar un error de buena fe, como pisar una fórmula, no para esconder datos: lo que no puede ver alguien no se comparte con esa persona.

En Excel cumplen ese papel la protección de hoja y de libro.

> [!NOTE] Sin fuente todavía: cómo funcionan en Excel la protección de hoja y de libro y su contraseña, y en qué se diferencian de la protección de Sheets.

## El historial de versiones

El historial de versiones permite ver cómo estaba la planilla antes y volver a una versión anterior. En Sheets, solo propietarios y editores lo ven y lo pueden restaurar. Restaurar una versión borra el historial celda por celda anterior a esa restauración; si hace falta conservarlo, Google sugiere hacer una copia antes. Es la red de seguridad cuando alguien borró una columna entera, y también una herramienta para [revisar una planilla](../Diseno-de-planillas/revisar-una-planilla.md).

En Excel, para comparar dos versiones de un libro celda por celda está Spreadsheet Inquire, solo en Excel para Windows y en algunas ediciones de Microsoft 365.

> [!NOTE] Sin fuente todavía: el historial de versiones de Excel en OneDrive y SharePoint.

## Cuando compartir deja de alcanzar

Compartir resuelve que varias personas miren y carguen la misma planilla. No resuelve que dos personas modifiquen el mismo registro a la vez, ni que cada vendedor vea solo sus clientes, ni dejar constancia de quién cambió cada dato. Cuando eso es lo que hace falta, la planilla dejó de ser la herramienta: las señales están en [cuándo pasar a una base](../cuando-pasar-a-una-base.md).
