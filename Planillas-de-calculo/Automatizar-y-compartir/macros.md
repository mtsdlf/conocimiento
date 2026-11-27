---
resumen: >-
  Una macro es un programa guardado dentro de un libro de Excel que repite una serie de acciones.
  En el Excel de escritorio se escriben en VBA o se graban; en Excel para la web el equivalente son
  los Office Scripts, que se pueden encadenar con Power Automate.
estado: vigente
estabilidad: semi
fuentes:
  - "Microsoft, Quick start: Create a macro: https://support.microsoft.com/en-us/office/quick-start-create-a-macro-741130ca-080d-49f5-9471-1e5fb3d581a8"
  - "Microsoft Learn, Macros from the internet are blocked by default in Office (actualizada 2026-07-17): https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked"
  - "Microsoft Learn, Office Scripts in Excel (2026-02-26): https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
aliases: [macro, VBA, Visual Basic for Applications, grabadora de macros, macro recorder, Office Scripts, Power Automate, macros de Excel]
creado: 2026-11-27
revisado: 2026-11-27
---

# Macros

Una macro es un programa guardado dentro de un libro de Excel que repite una serie de acciones. En el Excel de escritorio se escriben en VBA o se graban; en Excel para la web el equivalente son los Office Scripts, que se pueden encadenar con Power Automate.

Sirve para lo que una fórmula no hace: mover y copiar datos, dar formato, crear hojas o archivos. En un comercio, el caso típico es el lunes a la mañana: bajar el listado de ventas del sistema, borrar las columnas que sobran, ordenar por producto y pegarlo en la hoja de ventas. Si esa limpieza es siempre igual, antes de una macro conviene probar [Power Query](../Datos-en-la-planilla/power-query.md), que guarda los pasos sin programar y no tiene los problemas de seguridad de abajo. El equivalente en Google Sheets es [Apps Script](apps-script.md).

## Grabar una macro y después leerla

La forma de empezar es la grabadora. Según Microsoft, "Macros and VBA tools can be found on the Developer tab, which is hidden by default", así que primero hay que mostrar la pestaña Programador (Developer). Después, en Windows:

1. En la pestaña Programador, grupo Código, elegí Grabar macro.
2. Poné un nombre y, si querés, un atajo de teclado y una descripción.
3. Hacé las acciones que querés repetir.
4. Elegí Detener grabación, en la misma pestaña.

En Mac, la pestaña se muestra desde las preferencias de Cinta y barra de herramientas, y el resto es igual. Lo que se graba es literal: "When you create a macro, you are recording your mouse clicks and keystrokes." Para ver o cambiar el código, se elige Macros en el grupo Código, se selecciona la macro y Modificar, que "starts the Visual Basic Editor".

La grabadora graba clics, no intenciones. Si al grabar se seleccionó el rango `A1:F230`, la macro va a usar siempre `A1:F230`, aunque la semana siguiente el listado tenga 260 filas. Por eso una macro grabada casi siempre se edita después: es la forma de aprender VBA a partir de algo que ya funciona.

> [!NOTE] Sin fuente todavía: el formato de archivo en que hay que guardar un libro con macros (la página leída no lo dice; la página de coautoría menciona `.xlsm` entre los formatos admitidos) y si Excel para la web ejecuta VBA (la investigación no encontró una afirmación directa).

## Por qué una macro de internet no corre

Microsoft cambió el comportamiento por defecto de Office para bloquear las macros de los archivos que vienen de internet, porque "VBA macros are a common way for malicious actors to gain access to deploy malware and ransomware". El cambio se desplegó por etapas:

| Canal | Versión | Fecha |
|---|---|---|
| Current Channel (Preview) | 2203 | 2022-04-12 |
| Current Channel | 2206 | 2022-07-27 |
| Semi-Annual Enterprise Channel | — | 2023-01-10 |

El alcance es más chico de lo que se suele decir. Solo afecta a Office en Windows: "The change doesn't affect Office on a Mac, Office on Android or iOS devices, or Office on the web." Las versiones perpetuas como Office LTSC 2021 u Office 2019 conservan el paso previo para documentos de confianza. Y las políticas que permiten a un administrador cambiar este comportamiento existen en Microsoft 365 Apps for enterprise, no en Apps for business.

El mecanismo es la marca de la web (*Mark of the Web*), que Windows le pone a un archivo descargado o recibido como adjunto. Al abrirlo, aparece una barra de riesgo de seguridad sin el botón de habilitar contenido. Un archivo abierto con «Abrir en la aplicación de escritorio» desde OneDrive o SharePoint no lleva esa marca.

Si te mandaron por mail una planilla con macros y confiás en quien la mandó:

1. Guardá el archivo en tu computadora.
2. Hacé clic derecho, Propiedades, pestaña General, y marcá Desbloquear.
3. Abrilo de nuevo.

En PowerShell, el mismo paso es `Unblock-File`. La mejor alternativa es no mandar planillas con macros por mail: compartir un solo archivo en OneDrive o SharePoint evita la marca y las copias, como explica [compartir y colaborar](compartir-y-colaborar.md).

## Office Scripts, las macros de Excel en la web

Office Scripts es la automatización de Excel que funciona en la web. Según Microsoft Learn, tiene una grabadora de acciones y un editor de código; los scripts se guardan en OneDrive, se comparten asociándolos a un libro y se les puede poner un botón en la hoja.

Para correrlos solos, la programación está en pausa: "Script scheduling is temporarily disabled within Office Scripts. Existing scheduled scripts will continue to run". Mientras tanto, Microsoft recomienda armar un flujo en Power Automate, que conecta un script con un evento, por ejemplo la llegada de un correo.

> [!NOTE] Sin fuente todavía: el lenguaje de Office Scripts (TypeScript, según conocimiento general, no confirmado en la página leída), qué licencias y plataformas lo admiten, y los precios y límites de Power Automate.

## Cómo falla una macro

Una macro que escribe en la planilla la puede romper igual que una persona, pero más rápido y sin que nadie mire. Las fallas más comunes son tres. Rangos fijos que no crecen con los datos, que se evitan con [tablas estructuradas](../Datos-en-la-planilla/tabla-estructurada.md). Macros que nadie más sabe leer, que dejan al negocio dependiendo de una persona. Y macros que pegan valores encima de fórmulas, que borran la separación de [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md). Editar macros mientras otros coeditan el libro, además, puede interrumpir a los demás, según la página de coautoría de Microsoft.
