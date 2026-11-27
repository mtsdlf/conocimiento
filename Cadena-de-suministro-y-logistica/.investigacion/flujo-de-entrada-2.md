# APQC PCF 8.0, proceso 4.4.2: intento de lectura (2026-11-27)

## Conclusión

**No se pudo leer el contenido de la 8.0.** No se puede decir si 4.4.2.3 cambió de número o de nombre, ni si cambiaron 4.4.3.2 y 4.2.3.5 a 4.2.3.7. No hay texto literal de 4.4 ni de 4.4.2 en la 8.0. Lo único literal sobre 4.4.2.x viene de una página de medidas de APQC que rotula la **versión 7.1.0**, no la 8.0 (ver abajo).

## Lo que sí se confirmó de la 8.0 [M]

- [M] PDF Cross-Industry 8.0, "Published On: February 27, 2026", "Authored By: APQC", "Public Content: View Now" (snapshot de Wayback del 2026-06-19): https://web.archive.org/web/20260619203749/https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-cross-industry-pdf-13
- [M] Existe la versión Excel 8.0 (misma página, enlace "Download the Cross-Industry PCF", https://www.apqc.org/pcf-excel) y el PDF en https://www.apqc.org/pcf-pdf (URL del buscador; ambas dan 403 directo).
- [M] La FAQ de APQC dice: "The latest version of the PCF is version 8.0. It can be found in our Resource Library in PDF and Excel format." (snapshot 2026-10-03): https://web.archive.org/web/20261003220533/https://www.apqc.org/process-frameworks/pcf-faqs
- [M] Colección "PCF Version 8.0 Process Definitions and Key Measures Collection" (24-mar-2026), con un documento por categoría, incluida "4.0 Manage Supply Chain for Physical Products Definitions and Key Measures PCF version 8.0 Mar 24, 2026" (snapshot 2026-07-05): https://web.archive.org/web/20260705134719/https://www.apqc.org/resource-library/resource-collection/pcf-version-80-process-definitions-and-key-measures-collection
- [M] APQC publicó también PCF 8.0 de industria (Banking, Utilities, Consumer Products, Consumer Electronics), según la FAQ citada arriba. No son lo pedido.

## Lo que no se pudo ver

- La ficha de la categoría 4.0 en la 8.0 (slug `.../resource-listing/40-manage-supply-chain-physical-products-definitions-and-key`): el único snapshot de Wayback (2025-08-10) es de antes de la 8.0 y dice "PCF version 7.4" ("Published On: August 21, 2024"): https://web.archive.org/web/20250810154628/https://www.apqc.org/resource-library/resource-listing/40-manage-supply-chain-physical-products-definitions-and-key . No hay snapshot de 2026 de ese slug (CDX vacío).
- El archivo que está detrás de "View Now" (`/resource-library/free-content/nojs?nid=604812` para el PDF 8.0): Wayback devuelve 404. El del nid=550871 (4.0 en 7.4) se archivó como página de plantilla sin el documento.
- Notas de versión («what's new in 8.0»): no se encontró ninguna página. La FAQ y la ficha del PDF no listan cambios.

## Lo literal de 4.4.2 que sí hay, y por qué no vale como 8.0 [P]

[P] Página de medidas de APQC (snapshot 2025-04-27), sección "Measure Scope", rotulada "Cross Industry (7.1.0)": https://web.archive.org/web/20250427002053/https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/number-ftes-perform-process-plan-and

> 4.4.2.1 - Plan inbound material receipts (10349) - Managing the receipts of inbound materials. Create a plan accounting for the materials procured from the source of supply and the materials delivered to the distribution center or the warehouse.
> 4.4.2.2 - Manage inbound material flow (10350) - Managing all the internal activities related to the flow/transfer of materials. Manage materials being delivered to distribution center or warehouse. Gauge the time taken for delivery and if the delivery process is on time.
> 4.4.2.3 - Monitor inbound delivery performance (10351) - Overseeing the performance of an inbound delivery system. Check the present delivery system's efficiency, cost effectiveness, and adherence to a delivery schedule.
> 4.4.2.4 - Manage flow of returned products (10352) - Tracking and taking care of the products that have been internally returned either because of their deficiency or in cases of incorrect delivery.
> 4.4.2.5 - Control quality of returned parts (12708) - Implement a checks and balances system to verify that returned parts meet acceptable quality standards to determine appropriate disposition activity.

Es 7.1.0 (versión rotulada por la página), no 7.4 ni 8.0. Esta versión tiene 4.4.2.5 como "Control quality of returned parts (12708)", distinto del "Manage disposition of returned products 20109" que el pedido da para la 7.4. Eso confirma que la lista de hijos de 4.4.2 cambió entre 7.1 y 7.4, y deja abierto si cambió otra vez en la 8.0.

## [S] Resumen del buscador, sin verificar

- [S] La búsqueda web (modo extendido) devolvió un resumen que afirmaba que la 8.0 incluye "Plan and manage inbound material flow (ID 20936)" con 4.4.2.1 a 4.4.2.3 (10349, 10350, 10351) "in version 8.0". Su única fuente eran las páginas de medidas de arriba, que rotulan 7.1.0, y 20936 no apareció en ningún texto que yo leyera. No usar como dato de la 8.0.
- [S] Copia en Scribd "K016809 - APQC Process Classification Framework (PCF) - Cross-Industry - PDF Version 8.0": https://www.scribd.com/document/1028980479/K016809-APQC-Process-Classification-Framework-PCF-Cross-Industry-PDF-Version-8-0 . Solo vi el título en el buscador. Un curl devolvió una página de desafío de JavaScript ("Client Challenge") sin contenido.

## Vías probadas y qué devolvió cada una

Ronda 1
- WebSearch "APQC PCF Cross Industry version 8.0 PDF": devolvió las fichas oficiales (pcf-pdf, pcf-excel, resource-listing pdf-13 y excel-12) y las páginas de noticias, solo con metadatos [S].
- WebFetch de la ficha oficial del PDF 8.0: HTTP 403.
- WebFetch de web.archive.org: bloqueado por la herramienta ("unable to fetch").
- curl con User-Agent de navegador a apqc.org/pcf-pdf, /pcf-excel, la ficha pdf-13 y /about-apqc/news?page=20: 403 con página de Cloudflare ("Just a moment...").
- curl a web.archive.org con `/web/2026/` sobre pcf-pdf: 200, pero redirigió a un snapshot de 2024-08 de la ficha pdf-12 (7.4). La API `archive.org/wayback/available` para pcf-pdf: sin snapshots.

Ronda 2
- CDX de Wayback de la ficha pdf-13: tres snapshots (2026-03-01, 2026-03-26, 2026-06-19). El del 2026-06-19 se leyó (metadatos, arriba). No contiene el PDF; "View Now" apunta a `free-content/nojs?nid=604812`, que da 404 en Wayback.
- CDX de `/sites/default/files/*` y `/sites/default/files/2026*`: vacío una vez y "Temporarily Offline" la otra.
- WebSearch con "4.4.2" + "inbound material flow": devolvió medidas de APQC y la copia de Scribd (ver [S]).
- Ficha Excel 12 (snapshot 2026-07-05): 200, solo metadatos.

Ronda 3
- Colección 8.0 de definiciones (snapshot 2026-07-05): 200; lista la 4.0 pero enlaza al slug cuyo único snapshot es 7.4.
- FAQ del PCF (snapshot 2026-10-03): 200; confirma 8.0 como última versión, sin notas de cambios.
- Páginas de medidas de 4.4.2 por Wayback: la de `number-ftes-perform-process-plan-and` da 200 (7.1.0, ver arriba); `total-cost-perform-process-plan-and-0` y `systems-cost-perform-process-plan-and` dan 404.
- Scribd por curl: página de desafío de JavaScript.
- Un segundo WebSearch (notas de versión de la 8.0): no se hizo; el presupuesto de búsquedas de la sesión estaba agotado.

## Para cerrar el hueco

Lo más corto es que una persona con acceso abra https://www.apqc.org/pcf-pdf en un navegador (es contenido público, solo bloquea a las herramientas) y copie 4.4 y 4.4.2 con sus IDs, y las filas 4.2.3.5 a 4.2.3.7 y 4.4.3.2. Otra vía es bajar el Excel 8.0 y filtrar por esos IDs.
