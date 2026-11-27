---
resumen: >-
  Power Query es el motor de Excel para importar, limpiar y combinar datos con pasos que se graban y
  se repiten con un clic, sin fórmulas y sin tocar el archivo de origen. Google Sheets no lo tiene:
  IMPORTRANGE, QUERY y Connected Sheets cubren partes distintas de ese trabajo y no equivalen uno a uno.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, What is Power Query? (actualizada 2026-09-30): https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query"
  - "Microsoft, Power Query data sources in Excel versions: https://support.microsoft.com/en-us/excel/power-query-data-sources-in-excel-versions"
  - "Microsoft, Use Power Query in Excel for the web: https://support.microsoft.com/excel/use-power-query-in-excel-for-the-web"
  - "Microsoft Tech Community, New in Excel for the web: Power Query refresh data source (2025-07): https://techcommunity.microsoft.com/t5/excel-blog/new-in-excel-for-the-web-power-query-refresh-data-source/ba-p/4422757"
  - "Google, IMPORTRANGE: https://support.google.com/docs/answer/3093340"
  - "Google, QUERY: https://support.google.com/docs/answer/3093343"
  - "Google, Connected Sheets: https://support.google.com/docs/answer/9702507"
  - "Google Workspace Admin, ediciones de Connected Sheets: https://support.google.com/a/answer/9604541"
  - "FAST Standard Organisation, The FAST Standard: https://fast-standard.org/the-fast-standard/"
  - "Ken Puls y Miguel Escobar, M is for (Data) Monkey, Holy Macro! Books, ISBN 9781615470341"
aliases: [Power Query, Obtener y transformar, Get & Transform, Get Data, lenguaje M, M, ETL en Excel, IMPORTRANGE, QUERY, Connected Sheets, Hojas conectadas]
creado: 2026-11-27
revisado:
---

# Power Query

Power Query es el motor de Excel para importar, limpiar y combinar datos con pasos que se graban y
se repiten con un clic, sin fórmulas y sin tocar el archivo de origen. Google Sheets no lo tiene:
IMPORTRANGE, QUERY y Connected Sheets cubren partes distintas de ese trabajo y no equivalen uno a uno.

## El problema que resuelve: limpiar lo mismo todos los meses

Todos los meses llega el mismo archivo: el listado de precios del proveedor, el extracto de ventas
del sistema de facturación, el CSV de la plataforma de pagos. Cada vez hay que borrar las filas de
encabezado, partir una columna, pasar texto a número y pegarlo junto al del mes anterior. Power Query
graba esa limpieza una vez como una serie de pasos y, el mes siguiente, la repite sobre el archivo
nuevo con Refresh.

Microsoft lo define como "a data transformation and data preparation engine". Tres rasgos lo separan
de hacer lo mismo con fórmulas:

- **Pasos, no celdas.** Cada transformación queda registrada como un paso, en orden, y se puede
  revisar, cambiar o borrar.
- **El origen no se toca.** Los pasos se aplican sobre una copia; el archivo del proveedor queda
  como llegó.
- **Detrás hay un lenguaje.** Cada paso del editor genera código M, y el Advanced Editor permite
  editarlo. Para usarlo no hace falta saber M.

## Qué transformaciones hace

Además de lo básico (quitar filas y columnas, cambiar tipos, partir y unir texto), Microsoft lista
entre las avanzadas combinar (merge), anexar (append), agrupar, pivotar y despivotar. En un negocio
chico se traducen así:

| Transformación | Ejemplo |
|---|---|
| Anexar | juntar los extractos de ventas de enero, febrero y marzo en una sola lista |
| Combinar | traer a cada venta el rubro y el costo desde el catálogo de productos, por código |
| Despivotar | pasar una planilla con un mes por columna a una fila por producto y mes ([datos ordenados](datos-ordenados.md)) |
| Agrupar | total vendido por cliente antes de cargarlo |

Combinar hace el mismo trabajo que una [función de búsqueda](../Formulas/funciones-de-busqueda.md)
copiada en cada fila, pero como un solo paso. Es, por inferencia, la misma operación que un
[JOIN de SQL](../../Bases-de-datos/SQL/join.md): unir dos listas por una columna en común. El
resultado se carga a la hoja, normalmente como [tabla estructurada](tabla-estructurada.md), y de ahí
lo leen la [tabla dinámica](../Analisis/tabla-dinamica.md) y las fórmulas.

## Dónde está disponible en Excel

La disponibilidad cambia por plataforma y por versión, y las fuentes de Microsoft no coinciden del
todo. Lo que dicen al 2026-11-27:

- **Windows**: está en todas las versiones autónomas de Excel 2016 o posterior. Las ediciones
  perpetuas tienen "a large subset of features, but not all", y Microsoft 365 "contains all the
  available Power Query features".
- **Mac**: para suscriptores de Microsoft 365, por Get Data. Algunas fuentes (Text/CSV, libro de
  Excel, JSON, OData) permiten importar y actualizar; otras (SQL Server, carpeta local, tabla o
  rango) solo actualizar.
- **Web**: se pueden crear consultas desde un libro de Excel, Text/CSV, XML, JSON, SQL Server, lista
  de SharePoint Online y OData, y actualizarlas con Data > Refresh All. "Viewing and refreshing
  queries is available to all Microsoft 365 Subscribers." Otra página dice que en la web no se
  actualizan las consultas cargadas al Modelo de Datos (el almacén interno de Excel donde se cargan
  varias tablas para relacionarlas) y que el límite es de 1000 conexiones por
  usuario. Según una publicación del blog de Microsoft de julio de 2025, la actualización con
  fuentes autenticadas seleccionadas ya está disponible de forma general.
- **Android e iOS**: no está soportado.

> [!IMPORTANT]
> Discrepancia sin resolver sobre Excel para la web. La página "What is Power Query?" de Microsoft
> Learn dice, en su tabla de dónde se usa Power Query, que Excel tiene Power Query Desktop y que
> Power Query Online es "No". En otra sección de la misma página, "Excel Online" figura entre los
> productos que usan Power Query Online. Y la página de ayuda "Use Power Query in Excel for the web"
> describe cómo crear y actualizar consultas en la web. Antes de contar con Power Query en el
> navegador, conviene probarlo con la cuenta que se va a usar.

La [ficha de aplicaciones](../aplicaciones-de-planillas.md) reúne estas diferencias de versión con el
resto.

## Lo que Google Sheets tiene en su lugar

Sheets no tiene un motor de pasos grabados con interfaz gráfica. Tiene tres herramientas que cubren
pedazos distintos del trabajo de Power Query, y ninguna de ellas lo repite:

| Herramienta | Qué hace | Qué parte de Power Query cubre | Qué no cubre |
|---|---|---|---|
| IMPORTRANGE | trae un rango de otra hoja de cálculo de Google | importar | limpiar, transformar, otros formatos de archivo |
| QUERY | consulta un rango con cláusulas tipo SQL | filtrar, agrupar, pivotar | importar, pasos grabados, interfaz gráfica |
| Connected Sheets | conecta la hoja con BigQuery, el almacén de datos de Google Cloud | trabajar sobre datos grandes | no es para archivos sueltos ni para un negocio chico |

**IMPORTRANGE** tiene la sintaxis `IMPORTRANGE(spreadsheet_url, range_string)`, con coma en la
documentación en inglés; en una hoja configurada en castellano se escribe con punto y coma:
`=IMPORTRANGE("https://docs.google.com/spreadsheets/d/..."; "Ventas!A1:D500")`. La primera vez hay
que dar permiso explícito entre las dos hojas. El tope es de 10 MB por solicitud, y no admite
funciones volátiles como AHORA (NOW), ALEATORIO (RAND) y ALEATORIO.ENTRE (RANDBETWEEN), aunque HOY
(TODAY) sí. Sobre cada cuánto se actualiza, la página de la función dice que busca cambios cada hora
con el documento abierto, y otra página de ajustes de Google habla de 30 minutos.

**QUERY** corre una consulta en el lenguaje de la Google Visualization API, con cláusulas tipo SQL
(select, where, group by, pivot, order by). Por ejemplo, el total vendido por producto:
`=QUERY(Ventas!A1:D500; "select B, sum(D) group by B"; 1)`. Cada columna debería tener un solo tipo
de dato: si mezcla tipos, gana el más frecuente y el resto se trata como nulo, así que un precio
cargado como texto desaparece del total sin aviso. La función está en
[matrices dinámicas](../Formulas/matrices-dinamicas.md) junto a las otras fórmulas que devuelven
rangos.

**Connected Sheets** conecta con BigQuery, el almacén de datos de Google Cloud. Una página de
administración de Google lo limita a ciertas ediciones de Workspace (Enterprise Standard y Plus,
Education Standard y Plus, Enterprise Essentials y Essentials Plus), y una publicación de Google
Cloud de mayo de 2026, según su resumen, dice que alcanza con una cuenta de Workspace y un proyecto
de Google Cloud con facturación. Las dos descripciones difieren. En cualquier caso, supone tener los
datos en BigQuery, que no es el punto de partida de un comercio chico.

Lo que queda sin equivalente en Sheets es la combinación: pasos grabados, interfaz gráfica, combinar
listas sin fórmulas y repetir todo con un clic. En Sheets, ese trabajo se arma con fórmulas
(IMPORTRANGE más QUERY o [funciones de búsqueda](../Formulas/funciones-de-busqueda.md)) o con
[Apps Script](../Automatizar-y-compartir/apps-script.md).

> [!NOTE]
> Sin fuente todavía: si Sheets tiene una forma nativa de importar todos los archivos de una carpeta,
> como hace Power Query.

## Cuándo conviene y qué cuesta

Power Query conviene cuando la misma limpieza se repite: el archivo de cada mes, varios archivos con
la misma forma, una lista que hay que cruzar con otra cada semana. Para un cruce que se hace una vez,
una fórmula de búsqueda es más corta.

El costo es de transparencia, y es una inferencia, porque no se encontró una fuente que critique
Power Query. La lógica vive en el editor de consultas y no en la grilla: quien revisa la planilla ve
el resultado cargado, pero no los pasos, si no abre el editor. Las guías de modelado como FAST piden,
según su resumen, fórmulas "simple, clear" y transparentes para quien no las escribió; esa es la
posición a favor de las fórmulas, no una crítica a Power Query. Una planilla con consultas tiene que
decir en algún lado qué consultas hay y de dónde leen, como cuenta
[revisar una planilla](../Diseno-de-planillas/revisar-una-planilla.md).

> [!NOTE]
> Sin fuente todavía: una crítica documentada a Power Query (auditoría, reproducibilidad de los pasos)
> o una comparación con fórmulas.

Cuando las consultas empiezan a cruzar muchos archivos que cambian todos los días, la planilla está
haciendo de base de datos: ese es el momento que describe
[cuándo pasar a una base](../cuando-pasar-a-una-base.md).

## Qué leer

"What is Power Query?" de Microsoft Learn, en las secciones de transformaciones, el lenguaje M y la
tabla de dónde se usa Power Query; fijate en la fecha de actualización, porque la disponibilidad
cambia. Para saber qué hay en Windows, Mac y la web, "Power Query data sources in Excel versions",
que es la única que separa las tres. Para profundizar, *M is for (Data) Monkey*, de Ken Puls y Miguel
Escobar, escrito por practicantes; el año de edición no se confirmó. Para Sheets, las páginas de
ayuda de IMPORTRANGE y QUERY.
