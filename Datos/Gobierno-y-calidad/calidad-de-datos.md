---
resumen: >-
  La calidad de datos es cuánto sirve un dato para el uso que se le quiere dar, medida en seis
  dimensiones (completitud, unicidad, consistencia, oportunidad, validez y exactitud). Un dato malo se
  detecta con tests de datos: consultas que buscan las filas que rompen una regla y fallan si
  encuentran alguna.
estado: vigente
estabilidad: semi
fuentes:
  - "UK Government, Meet the data quality dimensions (definiciones citadas literalmente): https://www.gov.uk/government/news/meet-the-data-quality-dimensions"
  - "UK Government, The Government Data Quality Framework (según su resumen): https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework"
  - "DAMA UK, The Six Primary Dimensions for Data Quality Assessment (2013), copia de tercero según el buscador: https://joelbth.codeberg.page/community-notices/dama-quality-dimensions.pdf"
  - "ISO/IEC 25012:2008, Data quality model (ficha del catálogo e índice): https://iso.org/standard/35736.html"
  - "iso25000.com, ISO/IEC 25012 (secundaria): https://iso25000.com/index.php/en/iso-25000-standards/iso-25012"
  - "dbt Docs, Data tests: https://docs.getdbt.com/docs/build/data-tests"
  - "Datos/.investigacion/gobierno-y-privacidad.md"
aliases: [data quality, calidad del dato, dimensiones de calidad, tests de datos, data tests]
creado: 2026-11-27
revisado: 2026-11-27
---

# Calidad de datos

La calidad de datos es cuánto sirve un dato para el uso que se le quiere dar, medida en seis dimensiones (completitud, unicidad, consistencia, oportunidad, validez y exactitud). Un dato malo se detecta con tests de datos: consultas que buscan las filas que rompen una regla y fallan si encuentran alguna.

Es la pieza de [Gobierno y calidad](gobierno-y-calidad.md) que el analista nota primero. La diferencia con la [limpieza de datos](../Analisis/limpieza-de-datos.md) es de quién y cuándo: la limpieza la hace el analista sobre su propia tabla, una vez, para el análisis que tiene adelante; la calidad es una regla de la organización que se comprueba cada vez que el dato se mueve, para que el próximo analista no tenga que limpiar lo mismo.

## Las seis dimensiones de un dato bueno

Las seis dimensiones vienen de un documento de 2013 del grupo de trabajo de DAMA UK. Las definiciones que siguen son las que adoptó el gobierno del Reino Unido, que las recomienda «as defined by the Data Management Association UK». Una página de IBM atribuye las mismas seis a DAMA International; el origen es el documento de DAMA UK, que solo se vio en una copia de tercero.

| Dimensión | Definición (gov.uk) | En una tabla de ventas de un comercio |
|---|---|---|
| Completitud | «all the data required for a particular use is present and available to be used» | Ventas sin medio de pago cargado |
| Unicidad | «it appears only once in a data set» | El mismo pedido dos veces porque el aviso de la tienda llegó repetido |
| Consistencia | «data values do not conflict with other values within a record or across different data sets» | Una venta de un cliente que no existe en la tabla de clientes |
| Oportunidad | «the data is available when expected and needed» | El tablero de las 9 todavía muestra las ventas de anteayer |
| Validez | «the data conforms to the expected format, type, and range» | Un precio negativo, una fecha del año 2206 |
| Exactitud | «data reflects reality» | El stock dice 4 y en el depósito hay 1 |

La definición misma ya dice algo: la completitud es «for a particular use». Un dato no es bueno o malo en abstracto; un teléfono vacío no importa para un tablero de ventas y sí para una campaña por mensajería (lectura de la base). Los ejemplos de la tercera columna son de la base.

La norma ISO/IEC 25012:2008 propone un modelo más fino, de quince características vistas desde dos puntos de vista: el inherente al dato y el que depende del sistema que lo guarda. Fue revisada y confirmada en 2025, así que la edición de 2008 sigue vigente (según el resumen del buscador sobre la ficha de ISO). Para quien empieza, las seis de DAMA UK alcanzan; la norma sirve cuando hay que auditar.

> [!NOTE]
> Sin fuente todavía: la lista completa de las quince características de ISO/IEC 25012 y su reparto entre los dos puntos de vista. Solo se leyó el índice de la norma, que es de pago.

## Cada dimensión es una pregunta que contesta una consulta

Un dato malo se encuentra preguntándole a la tabla lo que no debería pasar. Un test de datos es una consulta SQL que busca las filas que contradicen una regla. La documentación de dbt, una herramienta de transformación que lo popularizó, lo dice así: son consultas «that seek to grab "failing" records, ones that disprove your assertion», y «if the data test returns zero failing rows, it passes».

Cuatro tests cubren casi todo lo básico. La correspondencia con las dimensiones es de la base, no de la documentación:

| Test | Qué busca | Dimensión que mide |
|---|---|---|
| No nulo | Filas con la columna vacía | Completitud |
| Único | Valores repetidos en una columna que debería ser clave | Unicidad |
| Valores aceptados | Valores fuera de una lista (un estado de pedido que no existe) | Validez |
| Relación | Claves que no existen en la otra tabla (un `cliente_id` de ventas que no está en clientes) | Consistencia |

La oportunidad se mide aparte, mirando cuándo llegó el último dato de cada fuente. La exactitud es la que ningún test resuelve solo: comparar con la realidad pide una fuente externa, como un conteo de depósito o el extracto del banco. Las reglas propias del negocio («el total de la venta es la suma de sus renglones») se escriben como consultas a medida.

Un test también decide qué pasa cuando falla. Se configura como aviso o como error que frena el paso siguiente, y las filas que fallan se pueden guardar para revisarlas. Lo habitual es frenar ante lo que rompe los números (una clave duplicada) y avisar ante lo que solo los empobrece (un campo opcional vacío) (lectura de la base).

## Dónde se pone cada control

Los tests corren donde el dato cambia de manos. El lugar natural es el paso de [ETL o ELT](../Ingesta-y-transformacion/etl-y-elt.md), después de cargar y antes de que el dato llegue al tablero. Lo que se puede evitar en el origen conviene evitarlo ahí: una restricción en el [modelo relacional](../Modelado-y-almacenamiento/modelo-relacional.md) que no deja guardar un pedido sin cliente vale más que un test que lo encuentra después. En la analítica de producto el problema típico es otro: un evento que se dejó de mandar o cambió de nombre en una versión de la app, y ahí la regla vive en la [tabla de eventos](../Modelado-y-almacenamiento/tabla-de-eventos.md).

La calidad tiene un límite que conviene saber. Un test comprueba que el dato cumple una regla, no que la regla sea la correcta: una tabla de ventas puede pasar todos los tests y estar contando las devoluciones como ventas. Eso es de la [definición de métrica](../Analitica-de-producto/definicion-de-metrica.md). Y cuando un test falla, saber qué tableros quedaron afectados pide [linaje](metadatos-y-linaje.md).

## Por dónde empezar en un negocio chico

1. Elegí las dos o tres tablas que alimentan los números que se miran todas las semanas (ventas, clientes, productos).
2. A cada clave ponele un test de único y no nulo, y a cada relación entre tablas, uno de relación.
3. Sumá valores aceptados para los estados y las categorías.
4. Mirá cuándo llegó el último dato de cada fuente antes de abrir el tablero.
5. Cada vez que un número salga mal, escribí el test que lo habría encontrado.

Si todavía no hay más que planillas, las mismas preguntas se hacen con un filtro o una tabla dinámica: contar repetidos, contar vacíos, buscar valores fuera de rango. Es la parte de la [limpieza de datos](../Analisis/limpieza-de-datos.md) que conviene repetir siempre igual.
