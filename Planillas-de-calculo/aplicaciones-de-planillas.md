---
resumen: >-
  Ficha de las aplicaciones de planillas al 2026-11-27 (Excel de Microsoft 365, Excel 2024, Excel
  para la web, Google Sheets y LibreOffice Calc), con sus versiones vigentes, sus límites de tamaño,
  lo que cambia entre ellas para automatizar y colaborar, y los límites de dos herramientas
  intermedias (Airtable y Access).
estado: borrador
estabilidad: volatil
fuentes:
  - "Microsoft, Excel specifications and limits: https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3"
  - "Microsoft, Office 2024 lifecycle (según resumen): https://learn.microsoft.com/lifecycle/products/office-2024"
  - "Microsoft, Office 2024 and Office LTSC 2024 FAQ (según resumen): https://support.microsoft.com/office/office-2024-and-office-ltsc-2024-faq-1c454a7d-3d0a-4139-b1bd-c61725ea436c"
  - "Microsoft Learn, Office Scripts in Excel (2026-02-26): https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel"
  - "Microsoft Learn, Macros from the internet are blocked by default in Office (2026-07-17): https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked"
  - "Microsoft, Use Power Query in Excel for the web: https://support.microsoft.com/excel/use-power-query-in-excel-for-the-web"
  - "Google, Archivos que se pueden almacenar en Google Drive: https://support.google.com/drive/answer/37603"
  - "Google Workspace Updates, Doubled cell limits in Google Sheets now generally available (2026-09-10): https://workspaceupdates.googleblog.com/2026/09/doubled-cell-limits-in-google-sheets-now-generally-available.html"
  - "Google Workspace Updates, Ten million cells (2022-03; solo metadatos): https://workspaceupdates.googleblog.com/2022/03/ten-million-cells-google-sheets.html"
  - "Google, Apps Script quotas: https://developers.google.com/apps-script/guides/services/quotas"
  - "LibreOffice, Download LibreOffice: https://www.libreoffice.org/download/download-libreoffice/"
  - "LibreOffice, novedades 25.8 y 26.2 (según resumen): https://whatsnew.libreoffice.org/26.2/"
  - "Airtable, Airtable plans overview (sin fecha visible): https://support.airtable.com/articles/2277136852-airtable-plans-overview"
  - "Microsoft, Access specifications (según resumen): https://support.microsoft.com/en-us/access/access-specifications"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
aliases: [Excel, Microsoft Excel, Google Sheets, Hojas de cálculo de Google, LibreOffice Calc, límites de Excel, límites de Google Sheets, Excel specifications and limits]
creado: 2026-11-27
revisado:
---

# Aplicaciones de planillas

Ficha de las aplicaciones de planillas al 2026-11-27 (Excel de Microsoft 365, Excel 2024, Excel para la web, Google Sheets y LibreOffice Calc), con sus versiones vigentes, sus límites de tamaño, lo que cambia entre ellas para automatizar y colaborar, y los límites de dos herramientas intermedias (Airtable y Access).

Implementa la comparación que usan [planillas de cálculo](planillas-de-calculo.md), [cuándo pasar a una base](cuando-pasar-a-una-base.md), [macros](Automatizar-y-compartir/macros.md), [Apps Script](Automatizar-y-compartir/apps-script.md) y [compartir y colaborar](Automatizar-y-compartir/compartir-y-colaborar.md). Qué función existe en cada aplicación y versión está en la [ficha de equivalencias](Formulas/equivalencias-de-funciones.md). Copiado de las fuentes vivas el 2026-11-27.

## Versiones vigentes

| Aplicación | Qué es al 2026-11-27 | Fuente |
|---|---|---|
| Excel de Microsoft 365 | Suscripción con mejoras continuas. Según Microsoft, "Microsoft 365 already has all the features included in Office 2024 and Office LTSC 2024, plus additional collaboration, productivity, and security features." | [FAQ de Office 2024](https://support.microsoft.com/office/office-2024-and-office-ltsc-2024-faq-1c454a7d-3d0a-4139-b1bd-c61725ea436c) |
| Excel 2024 | Compra única. Incluye "only a subset of the features" de Microsoft 365. Fin de soporte: 2029-10-09. La versión de consumo sigue la Modern Lifecycle Policy; la comercial (LTSC) tiene 5 años fijos. Office 2024 en Windows 10 no tiene extensión de actualizaciones de seguridad; las apps de Microsoft 365 en Windows 10 las reciben hasta el 2028-10-10 | [Ciclo de vida de Office 2024](https://learn.microsoft.com/lifecycle/products/office-2024) |
| Excel para la web | En el navegador; corre Office Scripts y, según la página de ayuda, Power Query (ver y actualizar consultas está disponible para todos los suscriptores de Microsoft 365). Otra página de Microsoft lo contradice: la discrepancia está en [Power Query](Datos-en-la-planilla/power-query.md) | [Office Scripts](https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel), [Power Query en la web](https://support.microsoft.com/excel/use-power-query-in-excel-for-the-web) |
| Google Sheets | En la nube, sin versiones. Automatiza con Apps Script (JavaScript) | [Límites de Drive](https://support.google.com/drive/answer/37603) |
| LibreOffice Calc | Libre y gratuito. Vigente: **26.8.3** ("LibreOffice 26.8 is our latest stable release"); la página también ofrece la 26.2.7, y la 27.2.0.0 alpha1 es un prelanzamiento | [Descarga de LibreOffice](https://www.libreoffice.org/download/download-libreoffice/) |

> [!NOTE] Sin fuente todavía: qué cuentas y planes dan acceso a Excel para la web (no se verificó en lo leído).

## Límites de tamaño

| Límite | Excel | Google Sheets | LibreOffice Calc |
|---|---|---|---|
| Tamaño de la grilla | 1.048.576 filas × 16.384 columnas por hoja | 20 millones de celdas o 100 MB por archivo (creado o convertido a Sheets) | Sin verificar |
| Caracteres por celda | 32.767 | Al convertir de Excel, se eliminan las celdas con más de 50.000 caracteres | Sin verificar |
| Caracteres por fórmula | 8.192 | Sin verificar | Sin verificar |
| Precisión | 15 dígitos | Sin verificar | Sin verificar |
| Usuarios a la vez | 256 en el modo antiguo de «libro compartido» ("Allow changes by more than one user"), que no admite tablas; no es el límite de la coautoría, que no se verificó | Sin verificar | — |
| Libros abiertos, hojas | Dependen de la memoria | Sin verificar | Sin verificar |

El límite de Sheets subió de 10 a 20 millones de celdas, según el anuncio de Google del 2026-09-10, para archivos nuevos, existentes e importados (.xlsx y CSV), sin control de administrador. El despliegue empezó el 2026-09-10 en Rapid Release y el 2026-09-28 en Scheduled Release, con hasta 15 días de demora. El límite anterior, de 10 millones, regía desde marzo de 2022, según el título de un anuncio de Google de 2022 que no se leyó. Google anunció también un aumento del tamaño de archivo importado como "coming soon", sin fecha. Ninguna fuente leída menciona el máximo de columnas de Sheets.

> [!NOTE] Sin fuente todavía: los límites de filas y columnas de LibreOffice Calc y el máximo de columnas de Google Sheets.

## Automatizar y colaborar en cada una

| | Excel de escritorio | Excel para la web | Google Sheets |
|---|---|---|---|
| Programar | VBA | Office Scripts | Apps Script |
| Bloqueo de macros de internet | Sí, en Windows (desde 2022) | No aplica | No aplica |
| Coautoría | Con archivo en OneDrive o SharePoint Online y suscripción a Microsoft 365 | Sin verificar | Siempre, sin fuente: es inferencia de que el archivo vive en la nube |
| Tiempo máximo de una función propia | — | — | 30 s por llamada a función personalizada |

Si Excel para la web ejecuta VBA no está verificado. El detalle de cada fila está en [macros](Automatizar-y-compartir/macros.md), [Apps Script](Automatizar-y-compartir/apps-script.md) y [compartir y colaborar](Automatizar-y-compartir/compartir-y-colaborar.md).

## Herramientas intermedias

Herramientas con forma de planilla y funcionamiento de base, para cuando aparecen las señales de [pasar a una base](cuando-pasar-a-una-base.md).

**Airtable**, según su página de planes (sin fecha de revisión visible; los registros cuentan por base, no por tabla):

| Plan | Registros por base | Almacenamiento | Llamadas a la API por mes | Precio por usuario por mes |
|---|---|---|---|---|
| Free | 1.000 | 1 GB | 1.000 | — |
| Team | 50.000 | 20 GB | 100.000 | US$24 facturado mensual, US$20 anual |
| Business | 125.000 | 100 GB | Ilimitadas | US$54 facturado mensual, US$45 anual |

**Microsoft Access**, según sus especificaciones (vistas por resumen): base de hasta 2 GB, menos el espacio de los objetos del sistema, con la posibilidad de enlazar tablas de otras bases; hasta 32.768 objetos; Microsoft indica que no soporta más de 255 usuarios concurrentes y recomienda SQL Server para más volumen.

## Precios

Solo se incluyen los de Airtable, verificados en su página oficial. Los precios de Microsoft 365, de Excel 2024 y de Google Workspace no se verificaron en una fuente oficial y no figuran.
