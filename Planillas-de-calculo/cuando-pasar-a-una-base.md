---
resumen: >-
  Pasar de una planilla a una base de datos conviene cuando la planilla dejó de ser el lugar donde se
  hacen cuentas y pasó a ser el registro del negocio, que varias personas cargan a la vez y que tiene
  que hacer cumplir reglas. Antes de eso hay límites duros de tamaño, opciones intermedias y un
  riesgo real de mudarse demasiado pronto.
estado: vigente
estabilidad: semi
fuentes:
  - "Microsoft, Excel specifications and limits: https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3"
  - "Google, Archivos que se pueden almacenar en Google Drive: https://support.google.com/drive/answer/37603"
  - "Microsoft, Access specifications (según resumen): https://support.microsoft.com/en-us/access/access-specifications"
  - "Microsoft, Migrate an Access database to SQL Server (según resumen): https://support.microsoft.com/en-us/access/migrate-an-access-database-to-sql-server"
  - "Airtable, Airtable plans overview: https://support.airtable.com/articles/2277136852-airtable-plans-overview"
  - "Raymond R. Panko, What We Don't Know About Spreadsheet Errors Today, EuSpRIG 2015: https://arxiv.org/pdf/1602.02601"
  - "Resultados del buscador de vendedores de herramientas (Retool, Airtable, Softr, Jotform, Basedash), sobre cuándo migrar; evidencia débil"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
  - "Planillas-de-calculo/.investigacion/posicion-contraria-y-fundamentos.md"
aliases: [de Excel a una base de datos, migrar de planilla a base de datos, spreadsheet to database, outgrowing spreadsheets, cuándo dejar Excel]
creado: 2026-11-27
revisado: 2026-11-27
---

# Cuándo pasar a una base

Pasar de una planilla a una base de datos conviene cuando la planilla dejó de ser el lugar donde se hacen cuentas y pasó a ser el registro del negocio, que varias personas cargan a la vez y que tiene que hacer cumplir reglas. Antes de eso hay límites duros de tamaño, opciones intermedias y un riesgo real de mudarse demasiado pronto.

Esta nota es el puente entre los dos temas. Del lado de la planilla, supone que ya se probó lo que la planilla hace bien: [datos ordenados](Datos-en-la-planilla/datos-ordenados.md), [tablas estructuradas](Datos-en-la-planilla/tabla-estructurada.md), [validación](Datos-en-la-planilla/validacion-de-datos.md) y [compartir un solo archivo](Automatizar-y-compartir/compartir-y-colaborar.md). Del otro lado está el tema [Bases de datos](../Bases-de-datos/bases-de-datos.md), que explica qué es una base y cómo se elige.

## Los límites duros

Hay un punto en que la planilla no entra más, y ese no se discute. Excel limita por filas y columnas por hoja; Google Sheets limita por celdas totales del archivo, y ese límite se duplicó en 2026. Los números de cada aplicación, con su fecha, están en la [ficha de aplicaciones](aplicaciones-de-planillas.md).

En la práctica, un comercio chico rara vez llega a esos topes con datos propios. Llega antes por otro lado: la planilla se vuelve lenta, o el problema no es cuántos datos hay sino cuántas personas los tocan y qué reglas tienen que cumplir. El caso de Public Health England en 2020, que según la prensa perdió casos al pasar el tope de filas de un formato viejo de Excel (el comunicado oficial no nombra el formato), está contado en [errores en planillas](Diseno-de-planillas/errores-en-planillas.md): el tope era real, pero el error fue usar una planilla como tubería de datos, es decir, como paso intermedio por el que los datos pasan automáticamente de un sistema a otro.

## Las señales de que la planilla ya no alcanza

> [!NOTE] Sin fuente todavía: ninguna fuente primaria lista estas señales. Son criterio de esta base, apoyado en los límites de cada herramienta, en lo que una base hace y una planilla no (tema [Bases de datos](../Bases-de-datos/bases-de-datos.md)) y en las señales que repiten, sin estudio detrás, las páginas de vendedores de herramientas.

**Varias personas escriben los mismos registros a la vez.** Una planilla compartida deja editar a muchos, pero no sabe qué hacer si dos cambian el mismo pedido al mismo tiempo: gana el último. Una base ordena esas escrituras, como explica [concurrencia](../Bases-de-datos/Transacciones/concurrencia.md). En una planilla compartida no hay nada equivalente a la escritura condicional de una base («descontá 1 solo si el stock sigue en 5»), así que dos descuentos simultáneos del mismo stock pueden pisarse; esto es inferencia, sin una fuente que lo pruebe en una planilla. Si en el local dos vendedores descuentan stock del mismo producto en la misma planilla, esta es la señal más clara.

**Los datos tienen relaciones de uno a muchos.** Un cliente tiene muchos pedidos; un pedido tiene muchos productos. En una planilla eso termina en filas repetidas con el nombre del cliente copiado, o en columnas «producto 1», «producto 2», «producto 3». Una base guarda cada cosa en su tabla y las vincula, como cuenta la [base relacional](../Bases-de-datos/Modelos-de-datos/base-relacional.md).

**Hay reglas que no se pueden romper.** «Todo pedido tiene un cliente que existe», «el precio no puede ser negativo». La [validación](Datos-en-la-planilla/validacion-de-datos.md) de una planilla ayuda, pero es una capa sobre celdas que se pueden pegar o reescribir (que pegar encima borra la regla es saber de práctica, sin fuente verificada); una base rechaza el dato que no cumple.

**Hace falta saber quién cambió qué, o que cada uno vea solo lo suyo.** El historial de versiones de una planilla permite volver atrás, pero no deja que cada vendedor vea solo sus clientes ni registra cada cambio con su autor.

**Mantener la planilla lleva más tiempo que usarla.** Es la señal que más repiten las fuentes de vendedores: la planilla pasó de ser el lugar donde se hacen cuentas a ser el lugar donde el negocio guarda su verdad, y alguien pasa horas arreglando copias y fórmulas rotas.

Una sola señal no obliga a mudarse. Dos o tres juntas, sobre los datos que mueven el negocio (pedidos, stock, clientes), sí.

## Lo que hay entre una planilla y una base

Entre una planilla y una base hecha a medida hay herramientas que se ven como planilla y funcionan como base: tienen tablas vinculadas, tipos de dato que se respetan y permisos. Las que aparecieron en la investigación:

- **Airtable**: aspecto de planilla y funcionamiento de base. Sus planes se distinguen por cuántos registros admiten por base, no por tabla.
- **Microsoft Access**: una base de escritorio. Microsoft indica que no soporta más de 255 usuarios concurrentes y recomienda SQL Server para más volumen.
- **AppSheet**, de Google: se la nombra como opción, pero no se investigó.

Los límites y precios de Airtable y los límites de Access, con su fecha, están en la [ficha de aplicaciones](aplicaciones-de-planillas.md). Cómo se elige una base propiamente dicha está en [criterios de elección](../Bases-de-datos/Elegir-una-base/criterios-de-eleccion.md).

> [!NOTE] Sin fuente todavía: AppSheet, Notion y otras herramientas sin código no se investigaron; tampoco hay una comparación neutral entre estas opciones.

## El riesgo de mudarse demasiado pronto

> [!IMPORTANT]
> La evidencia sobre cuándo migrar es la más débil de toda la investigación: casi todo lo que aparece lo escribe quien vende una alternativa a la planilla, y no hay estudios neutrales. Con esa advertencia, esas mismas fuentes señalan dos riesgos de migrar temprano. Una planilla que se entiende es más fácil de limpiar y de migrar después que una base armada a las apuradas. Y muchas migraciones fracasan después de cargar los datos, porque la gente no técnica ya no puede tocarlos y vuelve a la planilla.

Del lado de la planilla, Panko concluye que el problema de los errores no es la herramienta sino la falta de prueba: "spreadsheet programs are not error-prone. People are error prone." Una planilla con errores de diseño no se arregla mudándola a una base; se arregla con [diseño](Diseno-de-planillas/entradas-calculo-salidas.md) y [revisión](Diseno-de-planillas/revisar-una-planilla.md). La base resuelve otra cosa: escrituras simultáneas, relaciones y reglas.

Un camino que reduce el riesgo, como inferencia de lo anterior: mudar primero solo lo que muestra las señales (los pedidos, el stock) y dejar en la planilla el análisis, que es lo que la planilla hace mejor. Una planilla puede leer los datos de una base y seguir haciendo [tablas dinámicas](Analisis/tabla-dinamica.md) sobre ellos.
