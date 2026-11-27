---
resumen: >-
  Un almacén analítico es el lugar donde se juntan los datos de varias fuentes para analizarlos:
  el data warehouse los guarda ya integrados y con estructura, el data lake los guarda crudos y en
  cualquier formato, y el lakehouse intenta dar las garantías del primero sobre el almacenamiento
  barato del segundo.
estado: borrador
estabilidad: estable
fuentes:
  - "Definición de data warehouse atribuida a Inmon, vía Springer, Encyclopedia of Database Systems (solo buscador): https://link.springer.com/referenceworkentry/10.1007/978-1-4614-8265-9_121"
  - "Definición de data warehouse atribuida a Inmon, vía arXiv 1307.3448: https://arxiv.org/pdf/1307.3448"
  - "James Dixon, Pentaho, Hadoop, and Data Lakes (14 oct. 2010): https://jamesdixon.wordpress.com/2010/10/14/pentaho-hadoop-and-data-lakes/"
  - "Martin Fowler, DataLake: https://martinfowler.com/bliki/DataLake.html"
  - "Armbrust, Ghodsi, Xin y Zaharia, Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics, CIDR 2021, introducción y sección 2: https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf"
  - "Datos/.investigacion/modelado-e-ingesta.md (sección 4)"
aliases: [data warehouse, data lake, lakehouse, almacén de datos, lago de datos, warehouse]
creado: 2026-11-27
revisado:
---

# Almacenes analíticos

Un almacén analítico es el lugar donde se juntan los datos de varias fuentes para analizarlos:
el data warehouse los guarda ya integrados y con estructura, el data lake los guarda crudos y en
cualquier formato, y el lakehouse intenta dar las garantías del primero sobre el almacenamiento
barato del segundo.

Es la copia para analizar que pide la diferencia entre [OLTP y OLAP](oltp-y-olap.md). La llena la
[ingesta](../Ingesta-y-transformacion/ingesta.md), y adentro se arman los
[modelos dimensionales](modelado-dimensional.md). Si un negocio chico necesita uno está en la
entrada de [modelado y almacenamiento](modelado-y-almacenamiento.md); casi siempre, al principio,
no.

## Tres almacenes, tres ideas de qué guardar

| | Data warehouse | Data lake | Lakehouse |
|---|---|---|---|
| Qué guarda | datos integrados, en tablas | datos crudos, en cualquier formato | datos crudos y tablas sobre el mismo almacenamiento |
| Cuándo se les da forma | antes de cargar o al cargar | al leerlos | por capas, dentro del mismo sistema |
| Para quién | analistas y tableros | quien explora o entrena modelos | los dos |
| Origen del término | Inmon, años setenta, según la [cronología](../Fundamentos/fundamentos-de-datos.md#del-almacén-de-datos-al-analytics-engineer) | Dixon, 2010 | Armbrust y otros, 2021 |

## El data warehouse: integrado e histórico

La definición más citada se atribuye a Bill Inmon: un data warehouse es «a subject-oriented,
integrated, nonvolatile, and time-variant collection of data in support of management's
decisions». Circula en dos redacciones con el mismo contenido, y ninguna de las dos fuentes leídas
es el texto de Inmon. Los cuatro atributos dicen:

- Orientado a temas: los datos de un tema (ventas, clientes) van juntos, aunque vengan de
  sistemas distintos.
- Integrado: se resuelven los conflictos de nombres y unidades entre fuentes.
- No volátil: lo cargado no se modifica ni se borra.
- Variante en el tiempo: cada registro tiene su marca de tiempo, y se ven el estado actual y la
  historia.

Un warehouse en la nube como BigQuery guarda por columnas, por la razón que explica [OLTP y
OLAP](oltp-y-olap.md#por-qué-el-almacén-analítico-guarda-por-columnas); que lo hagan todos los
warehouses actuales es lectura de la base.

## El data lake: todo crudo en un lugar

El término es de James Dixon, en una entrada de blog del 14 de octubre de 2010. Un datamart es una
parte del warehouse armada para un área (ventas, finanzas); Dixon lo compara así: si un datamart es
«a store of bottled water – cleansed and packaged and structured for easy consumption», entonces
«the data lake is a large body of water in a more natural state». Otra fuente ubica el término en
2008; la página original y la mayoría de las fuentes dicen 2010.

Martin Fowler lo define como «a single store for all of the raw data that anyone in an organization
might need to analyze». La crítica conocida es que termina siendo «a dumping ground for data of
widely varying quality, better named a data swamp», un pantano de datos. Fowler la llama «both valid
and irrelevant»: el lago no promete datos limpios, y quien lo usa tiene que saber qué está leyendo.
Qué hace confiable un dato es tema de [calidad de datos](../Gobierno-y-calidad/calidad-de-datos.md).

Para un negocio chico, un lago casi nunca es el primer almacén: guarda bien lo que todavía no tiene
forma (archivos, registros, imágenes) y sirve a quien explora o entrena modelos, pero para tableros
de ventas hace falta darle forma igual. Con datos que ya vienen en tablas, el primer paso suele ser
un warehouse o la propia base, como dice [cuándo hace falta un almacén
aparte](modelado-y-almacenamiento.md) (lectura de la base).

## El lakehouse: la tesis de unir los dos

Armbrust y otros definen el lakehouse en 2021 como «a data management system based on low-cost and
directly-accessible storage that also provides traditional analytical DBMS management and
performance features such as ACID transactions, data versioning, auditing, indexing, caching, and
query optimization». ACID son las garantías de una base transaccional: que una escritura entre
entera o no entre, y que dos escrituras a la vez no se pisen. DBMS es el sistema que administra la
base. La idea es tener los datos en archivos abiertos y baratos, como en el lago, y
encima las garantías de un warehouse.

> [!IMPORTANT]
> El paper sostiene que la arquitectura de warehouse «will wither in the coming years and be
> replaced» por el lakehouse. Los autores trabajan en Databricks, que vende esa arquitectura, y los
> resultados de rendimiento son de su propio sistema. Es una tesis de parte, no un consenso.

## Dónde se lee la versión larga

La introducción y la sección 2 del paper de Armbrust y otros cuentan las dos generaciones anteriores
(el warehouse y el lago) y por qué proponen una tercera; conviene leerlo sabiendo que es un paper que
vende una arquitectura. Para el lago, la entrada de Dixon es corta y la de Fowler suma la crítica.
Los motores concretos, con licencia y precio, están en la ficha de
[motores analíticos](motores-analiticos.md). En Azure, el lago y los reportes aparecen como una de
las [arquitecturas de referencia](../../Cloud/arquitecturas-de-referencia-en-azure.md) de Cloud.
