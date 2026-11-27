---
resumen: >-
  El modelado dimensional ordena los datos para analizar en tablas de hechos, que guardan las
  medidas de un proceso del negocio con un grano declarado, y tablas de dimensiones, que guardan el
  contexto (quién, qué, dónde, cuándo) por el que se filtra y se agrupa.
estado: borrador
estabilidad: estable
fuentes:
  - "Kimball Group, Grain: http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/"
  - "Kimball Group, Fact table structure: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/fact-table-structure"
  - "Kimball Group, Star schemas and OLAP cubes: http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/star-schema-olap-cube/"
  - "Kimball Group, Type 2: Add new row: http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-2"
  - "Kimball Group, Differences of Opinion (2004): https://www.kimballgroup.com/2004/03/differences-of-opinion/"
  - "Kimball Group, Type 0 a Type 7 (páginas type-0, type-1, type-3, type-4-mini-dimension, type-5, type-6 y type-7, leídas enteras en Datos/.investigacion/bi-gestion-modelado.md): https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/"
  - "W. H. Inmon, Building the Data Warehouse, 4.ª ed., Wiley, 2005, cap. 1 (extracto oficial, leído entero en Datos/.investigacion/bi-gestion-modelado.md): https://media.wiley.com/product_data/excerpt/45/07645994/0764599445-18.pdf"
  - "Datos/.investigacion/bi-gestion-modelado.md (secciones 3 y 7)"
  - "Ralph Kimball y Margy Ross, The Data Warehouse Toolkit, 3ª ed., caps. 1-2 (no leído; citado por el sitio de Kimball Group)"
  - "Databricks, glosario, Data Vault: https://www.databricks.com/glossary/data-vault"
  - "dbt, Dimensional modeling (vía buscador): https://docs.getdbt.com/terms/dimensional-modeling"
  - "Perficient, The star schema is obsolete (2022), vía buscador: https://blogs.perficient.com/2022/09/13/the-star-schema-is-obsolete-reduced-cost-and-better-performance/"
  - "Hightouch, Modern Data Warehouse Modelling pt. 2 (vía buscador): https://www.hightouch.com/blog/data-warehouse-modelling-part-2"
  - "Datos/.investigacion/modelado-e-ingesta.md (sección 3)"
  - "Datos/.investigacion/posicion-contraria.md (sección 5)"
aliases: [esquema en estrella, star schema, hechos y dimensiones, Kimball, dimensional modeling, dimensión lentamente cambiante, SCD]
creado: 2026-11-27
revisado:
---

# Modelado dimensional

El modelado dimensional ordena los datos para analizar en tablas de hechos, que guardan las
medidas de un proceso del negocio con un grano declarado, y tablas de dimensiones, que guardan el
contexto (quién, qué, dónde, cuándo) por el que se filtra y se agrupa.

Lo sistematizó Ralph Kimball. Parte de las tablas del [modelo relacional](modelo-relacional.md) y
las reordena para que las preguntas de análisis se contesten con pocos *joins* (lectura de la base). La reordenación la
hace la [transformación](../Ingesta-y-transformacion/etl-y-elt.md), y el resultado vive en un
[almacén analítico](almacenes-analiticos.md).

## Hechos, dimensiones y la estrella

Una **tabla de hechos** guarda lo que se mide. Kimball: «A fact table contains the numeric measures
produced by an operational measurement event in the real world», y además siempre tiene claves
foráneas a cada una de sus dimensiones. En un comercio, la tabla de ventas guarda cantidad, precio e
importe de cada venta.

Una **tabla de dimensiones** guarda el contexto: el cliente, el producto, la sucursal, la fecha. Es
por donde se corta el número («ventas por categoría», «por mes»). El modelo divide los datos en
medidas o en contexto descriptivo, el «who, what, where, when, why, and how».

La tabla de hechos en el centro, con las dimensiones alrededor, forma un **esquema en estrella**:
«Star schemas characteristically consist of fact tables linked to associated dimension tables».

## El grano se declara antes que todo

El grano dice qué representa una fila de la tabla de hechos: una venta, una línea de pedido o el
total de un día por sucursal. Kimball lo pone primero: «Declaring the grain is the pivotal step in a
dimensional design», y se declara «before choosing dimensions or facts». Esa precedencia está en su página de grano; el orden completo (proceso del negocio, grano,
dimensiones y hechos) es el que propone el informe para el libro, que no se leyó.

Mezclar granos es el error más caro, porque suma mal sin avisar: «different grains must not be mixed
in the same fact table». Si una tabla tiene filas por pedido y por línea de pedido, el importe del
pedido se cuenta dos veces. El mismo cuidado vale para cualquier
[definición de métrica](../Analitica-de-producto/definicion-de-metrica.md): decir sobre qué fila se
cuenta.

## Cuando el contexto cambia en el tiempo

Un cliente se muda, un producto cambia de categoría. Las **dimensiones lentamente cambiantes**
deciden qué pasa con la historia. Kimball nombra cuatro tipos básicos: 0 «Retain original», 1 «Overwrite»,
2 «Add new row» y 3 «Add new attribute». El tipo 2 agrega una fila nueva con los valores cambiados y
una clave nueva, que los hechos usan «from the moment of the update». Así una venta de marzo queda
con la categoría que el producto tenía en marzo.

Los otros tres básicos, en palabras de Kimball. En el tipo 0 «the dimension attribute value never changes, so facts are always grouped by this original value», y vale para casi todos los atributos de una dimensión de fechas. En el tipo 1 el valor viejo se pisa con el nuevo, «and therefore this technique destroys history». El tipo 3 agrega un atributo para guardar el valor anterior mientras el nuevo pisa al principal, y Kimball dice que a veces se lo llama «alternate reality».

Kimball suma además cuatro tipos híbridos. El 4 separa en una minidimensión el grupo de atributos que cambia rápido (la «rapidly changing monster dimension»). El 5 suma al 4 una referencia de tipo 1 a esa minidimensión desde la dimensión base. El 6 guarda en la fila de tipo 2 también el valor actual, para agrupar por el valor de su momento o por el de hoy. El 7 pone en la tabla de hechos la clave durable y la clave sustituta, para ver los dos, «as-was and as-is». Cuándo conviene cada uno en el registro de un sistema de gestión está en [historia en el BI de gestión](../Visualizacion-y-BI/BI-sobre-software-de-gestion/historia-en-el-bi-de-gestion.md#como-era-o-como-es-hoy).

Importa cuando el costo o el precio de un producto cambia y se quiere saber cuánto dejó cada venta
con los valores de su momento, como pide la [economía
unitaria](../../Marketing/Medicion/economia-unitaria.md) (lectura de la base).

> [!IMPORTANT]
> Tres escuelas para el almacén. Kimball arma el almacén con modelos dimensionales por proceso
> del negocio y sostiene que «atomic data must be dimensionally structured», con «conformed
> dimensions» (las mismas dimensiones compartidas por todos los procesos) como columna vertebral.
> La escuela de Inmon, la fábrica de información corporativa, carga primero «a third normal form
> (3NF) relational database containing atomic data» y arma los modelos dimensionales después. Esa
> descripción es de un artículo de Kimball de 2004 sobre su rival. En su propio libro, Inmon separa
> cuatro niveles de datos (operativo, atómico o almacén, departamental o data mart, e individual) que
> forman la fábrica de información corporativa, y dice que el nivel del almacén «holds integrated,
> historical primitive data that cannot be updated»; los datos derivados van en otro nivel, porque
> los primitivos y los derivados «do not reside in the same database or even the same environment».
> El fragmento leído no habla de la tercera forma normal. Data Vault, de Dan Linstedt, reparte el almacén en *hubs* (los
> conceptos del negocio), *links* (las relaciones entre hubs) y *satellites* (los atributos y su
> historia), según el glosario de un proveedor, que lo presenta como un patrón para analítica a escala de
> empresa; que los satélites guarden la historia y que sirva a empresas con muchas fuentes que
> cambian es lectura de la base.

## La crítica de la tabla única

Una posición más reciente pregunta si hace falta separar hechos y dimensiones o conviene una tabla
ancha con todo junto (*one big table*). La documentación de una herramienta de transformación
responde que «depends on the situation» y atribuye el cambio de mirada al almacenamiento barato, a
herramientas de BI que resuelven joins, a la evolución de SQL y a analistas con más habilidad. Un blog de 2022 declara obsoleto
el esquema en estrella y cita un benchmark de un proveedor, no verificado contra el original, con
tablas anchas «25-50% faster». Otra postura es híbrida: la estrella como paso intermedio y las
tablas anchas armadas a partir de ella. Todas las fuentes son de proveedores o blogs, según sus
resúmenes.

Aunque la tabla final sea ancha, declarar el grano y separar medidas de contexto sigue siendo la
forma de pensar el modelo; la ventaja de la estrella, además de la velocidad, es que todos usen las
mismas definiciones (lectura de la base). Esa idea sigue en la [capa
semántica](../Visualizacion-y-BI/capa-semantica.md).

## Dónde se lee la versión larga

*The Data Warehouse Toolkit*, de Kimball y Ross, caps. 1 y 2 (técnicas básicas y dimensiones
lentamente cambiantes; números de capítulo sin verificar). La alternativa gratuita son las páginas
de técnicas del sitio de Kimball Group, empezando por la de grano. Conviene leerlo junto con la
página de modelado dimensional de dbt como contrapeso.

> [!NOTE]
> Sin fuente todavía: la definición literal de tabla de dimensiones según Kimball, y un texto primario
> de Linstedt.
