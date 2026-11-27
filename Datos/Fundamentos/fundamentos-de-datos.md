---
resumen: >-
  Fundamentos reúne lo que cruza todo el tema Datos sin ser una de sus partes: de dónde viene el
  campo, los dos marcos que lo dividen, los roles que se reparten el recorrido del dato, las fuentes
  del tema y las dos rutas para aprenderlo.
estado: vigente
estabilidad: estable
fuentes:
  - "Joe Reis, The Data Engineering Lifecycle and Undercurrents, 4 Years Later (2026): https://joereis.substack.com/p/the-data-engineering-lifecycle-and"
  - "Joe Reis y Matt Housley, Fundamentals of Data Engineering, cap. 2 (O'Reilly, 2022), según el resumen del buscador: https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html"
  - "DAMA International, DMBOK2R infographics: https://dama.org/dmbok2r-infographics/"
  - "DAMA International, revisión 2024 del DAMA-DMBOK 2.0: https://dama.org/dama-dmbok-revision/"
  - "DAMA International, What Is DAMA International? (2026-04-14), según el resumen del buscador: https://dama.org/2026/04/14/what-is-dama-international-a-guide-for-data-professionals/"
  - "Dawiso, glosario DAMA-DMBOK (proveedor), según el resumen del buscador: https://www.dawiso.com/glossary/dama-dmbok"
  - "DATAVERSITY, A Short History of Data Warehousing: https://www.dataversity.net/a-short-history-of-data-warehousing/"
  - "Kimball Group, ficha de The Data Warehouse Toolkit, 3.ª ed.: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/"
  - "Gupta et al., Amazon Redshift and the Case for Simpler Data Warehouses, según el resumen del buscador: https://www.cs.cmu.edu/~15721-f24/papers/Redshift.pdf"
  - "dbt Labs (proveedor), What is analytics engineering: https://www.getdbt.com/blog/what-is-analytics-engineering"
  - "First Round Review, dbt Labs' path to product-market fit, según el resumen del buscador: https://review.firstround.com/dbt-labs-path-to-product-market-fit/"
  - "Datos/.investigacion/fundamentos.md, secciones 1 y 3"
  - "Datos/.investigacion/vistazo.md, sección 1"
aliases: [fundamentos, fundamentos del tema Datos, historia de los datos, marcos de datos]
creado: 2026-11-19
revisado: 2026-11-27
---

# Fundamentos de datos

Fundamentos reúne lo que cruza todo el tema Datos sin ser una de sus partes: de dónde viene el
campo, los dos marcos que lo dividen, los roles que se reparten el recorrido del dato, las fuentes
del tema y las dos rutas para aprenderlo.

Queda fuera de las verticales de [Datos](../datos.md) porque no es un tramo del recorrido del dato:
ayuda a leer todos. Fija de dónde sale la división del tema en verticales y quién trabaja en cada
tramo.

## Del almacén de datos al analytics engineer

El campo nació de una necesidad vieja: juntar datos de varios sistemas para decidir. Según
DATAVERSITY, esa necesidad es anterior al modelo relacional y a SQL. La cronología que sigue sale
de ese único artículo, salvo donde se indica otra fuente.

| Cuándo | Qué pasó |
|---|---|
| Años 70 | Bill Inmon empieza a hablar de principios de data warehouse y acuña el término |
| 1986 | Ralph Kimball funda Red Brick Systems |
| 1988 | Un artículo del IBM Systems Journal introduce el «business data warehouse» |
| 1992 | Inmon publica *Building the Data Warehouse*; Kimball deja Red Brick |
| 1996 | Kimball publica la primera edición de *The Data Warehouse Toolkit* (la 3.ª, con Margy Ross, es de Wiley, 2013, según Kimball Group) |
| Fines de los 90 | Inmon desarrolla la Corporate Information Factory |
| 2004 | Dean y Ghemawat publican el paper de MapReduce, según el buscador; sin verificar |
| Febrero de 2013 | Sale Amazon Redshift, un almacén analítico en la nube de un gran proveedor, según un paper de sus autores leído por resumen |
| 2016 | Se funda la empresa que después hizo dbt, según First Round Review leída por resumen |
| 2018 | Empieza a usarse «analytics engineer», según dbt Labs, que vende la herramienta de la que nació el rol |
| 2022 | Reis y Housley publican *Fundamentals of Data Engineering* (O'Reilly) |

Las dos escuelas de los años 90 siguen vivas. Inmon arma un almacén corporativo de arriba hacia
abajo; Kimball, almacenes dimensionales de abajo hacia arriba, según varias secundarias que repiten
lo mismo. La disputa se explica en [modelado dimensional](../Modelado-y-almacenamiento/modelado-dimensional.md).
Según dbt Labs, desde 2012 los almacenes en la nube, la ingesta administrada y el BI de autoservicio
abarataron cargar y reportar, y con eso llegaron los números que no coincidían. Ese es el problema
que se le encarga al [analytics engineer](roles-de-datos.md#el-analytics-engineer-un-rol-nombrado-por-un-proveedor).

> [!NOTE]
> Sin fuente todavía: cuándo nacen los sistemas de soporte a decisiones y la etiqueta «business
> intelligence», y una fuente primaria para el nacimiento de Hadoop.

## Dos marcos que dividen el campo

Dos marcos dividen el campo según lo que le pasa al dato, con miradas distintas, y el árbol de
este tema toma de los dos.

El ciclo de vida de Reis y Housley es la vista de quien construye. Tiene cinco etapas en orden:
generar, almacenar, ingerir, transformar y servir. Debajo corren seis preocupaciones transversales
(*undercurrents*): seguridad, gestión de datos, DataOps, arquitectura, orquestación e ingeniería de
software. La lista la confirmó el propio Reis en 2026, cuatro años después del libro. En ese post
suma FinOps como séptima posible («not fully sold yet»), duda si la IA debería ser otra y dice que le
daría más lugar al modelado. Según el resumen del buscador del capítulo 2, el ciclo cubre solo las
etapas que controla el ingeniero de datos y termina en «servir».

La rueda de DAMA-DMBOK2 es la vista de quien gobierna. Ordena las funciones de gestión que
necesita una organización, con el gobierno de datos en el centro. La guía es de 2017, y la revisión
de 2024 es de mantenimiento: «No material changes were made to the overarching data management
framework, knowledge areas, or their definitions», según DAMA.

> [!IMPORTANT]
> **¿Once o catorce áreas?** DAMA misma dice «11 core knowledge areas» en un artículo de 2026 (leído
> por resumen). Su página de infografías enumera, en cambio, 14 diagramas de contexto: suma la ética
> en el manejo de datos, big data y ciencia de datos, y la evaluación de madurez a las once. Un
> resumen del buscador menciona otra página de DAMA que habla de diez. La lista de once por nombre
> solo apareció en una secundaria de proveedor y coincide con las 14 menos esas tres; no se cotejó
> con el libro. Hasta verificarlo, la base dice «la rueda de DAMA» sin número.

Cómo calzan las verticales del tema en cada marco (lectura de la base; ninguna fuente leída compara
los dos marcos):

| Vertical | Ciclo de Reis y Housley | Rueda de DAMA |
|---|---|---|
| [Modelado y almacenamiento](../Modelado-y-almacenamiento/modelado-y-almacenamiento.md) | generar, almacenar | arquitectura, modelado, almacenamiento |
| [Ingesta y transformación](../Ingesta-y-transformacion/ingesta-y-transformacion.md) | ingerir, transformar; orquestación | integración e interoperabilidad |
| [Gobierno y calidad](../Gobierno-y-calidad/gobierno-y-calidad.md) | gestión de datos, seguridad | el centro y casi todos los radios |
| [Análisis](../Analisis/analisis.md), [Visualización y BI](../Visualizacion-y-BI/visualizacion-y-bi.md) | después de «servir» | warehousing y BI |
| [Estadística](../Estadistica/estadistica.md) | no aparece | no aparece |
| [Analítica de producto](../Analitica-de-producto/analitica-de-producto.md) | no aparece | no aparece |

Los dos huecos de la tabla son decisiones del árbol. La estadística atraviesa el análisis y los
experimentos, y está como vertical porque se estudia por separado. La analítica de producto sale de
las herramientas de producto, no de la ingeniería ni de la gestión de datos.

Para leer el marco entero: los capítulos 1 y 2 de Reis y Housley, fijándose en el diagrama del ciclo
con los undercurrents debajo; sirve para ubicar en qué tramo está un problema («el dato llega tarde»
es ingesta; «los números no coinciden» es transformación o gestión). Para la rueda, la página de
infografías de DAMA; el libro es pago.

## Qué leer y cuándo

- [Roles de datos](roles-de-datos.md) — analista, analista BI, analytics engineer, ingeniero y
  científico de datos, qué tramo cubre cada uno y qué se aprende primero. Para elegir qué estudiar o
  a quién contratar.
- [Bibliografía de datos](bibliografia-de-datos.md) — la bibliografía por vertical, con la edición verificada y
  lo que no se pudo verificar. Para elegir la próxima lectura.
- [Ruta de Data Analytics](ruta-de-data-analytics.md) — el orden para aprender el análisis con las
  notas de la base, con ejercicios sobre una tienda online chica. Para empezar de cero.
- [Análisis de cohortes desde cero](recorrido-analisis-de-cohortes.md) — trece notas en orden que
  terminan en armar, leer y explicar una tabla de retención por cohorte. Para practicar un análisis
  entero después de la ruta.

## Qué falta en Fundamentos

No hay glosario ni nota de escuelas: las disputas de modelado (Kimball, Inmon, Data Vault) viven en
su vertical. Los términos de la base y de SQL (tabla, fila, clave, NULL, join) se definen en el
[glosario de bases de datos](../../Bases-de-datos/Fundamentos/glosario-de-bases-de-datos.md), y los
de la planilla, en el [glosario de planillas](../../Planillas-de-calculo/Fundamentos/glosario-de-planillas.md);
el grano, que no está en ninguno de los dos, en
[SQL para análisis](../Analisis/sql-para-analisis.md#el-grano-qué-es-una-fila). La cronología se apoya en una sola secundaria. La lista de áreas de DAMA no se cotejó
con el libro, y el capítulo 2 de Reis y Housley no se pudo abrir: sus etapas están confirmadas por el
autor, no por el texto. Falta también qué se pide en los avisos de trabajo en Argentina (ver
[roles de datos](roles-de-datos.md#el-hueco-del-mercado-argentino)).
