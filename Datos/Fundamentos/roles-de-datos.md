---
resumen: >-
  Los roles de datos se reparten el recorrido del dato: el ingeniero de datos lo trae y lo guarda,
  el analytics engineer lo deja en tablas limpias, el analista y el analista BI lo convierten en
  respuestas y tableros, y el científico de datos arma modelos sobre él.
estado: borrador
estabilidad: semi
fuentes:
  - "dbt Labs (proveedor), Analytics engineer vs data analyst: https://www.getdbt.com/blog/analytics-engineer-vs-data-analyst"
  - "dbt Labs (proveedor), What is analytics engineering: https://www.getdbt.com/blog/what-is-analytics-engineering"
  - "U.S. Bureau of Labor Statistics, Occupational Outlook Handbook, Data Scientists (modificada 2026-08-27): https://www.bls.gov/ooh/math/data-scientists.htm"
  - "Microsoft, Study guide for Exam PL-300 (skills measured as of April 20, 2026): https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300"
  - "Coursera, Google Data Analytics Professional Certificate: https://www.coursera.org/professional-certificates/google-data-analytics"
  - "Sysarmy, Resultados de la encuesta de sueldos 2026.1 (2026-03-06): https://sysarmy.com/blog/posts/resultados-de-la-encuesta-de-sueldos-2026-1/"
  - "Datos/.investigacion/fundamentos.md, secciones 2 y 5"
  - "Datos/.investigacion/vistazo.md, sección 1"
aliases: [roles en datos, data analyst, analista de datos, analytics engineer, data engineer, ingeniero de datos, data scientist, científico de datos, analista BI]
creado: 2026-11-27
revisado:
---

# Roles de datos

Los roles de datos se reparten el recorrido del dato: el ingeniero de datos lo trae y lo guarda,
el analytics engineer lo deja en tablas limpias, el analista y el analista BI lo convierten en
respuestas y tableros, y el científico de datos arma modelos sobre él.

Los nombres cambian de una empresa a otra, y en un equipo chico una persona hace varios. Sirven
para saber qué aprender, a quién pedirle qué y por qué un problema («el número del tablero no
coincide con el de la tienda») cae en un tramo y no en otro.

## Cinco roles en una cadena

Ninguna fuente leída asigna los roles a los tramos del recorrido: la columna «tramo» es
construcción de la base, apoyada en las definiciones de la columna de al lado. La guía de la
certificación de BI de Microsoft da la pista de la cadena: el analista BI trabaja con la gente de
negocio y tiene que «collaborate with analytics engineers and data engineers to identify and acquire
data».

| Rol | Qué hace, según su fuente | Tramo del recorrido (construcción de la base) |
|---|---|---|
| Ingeniero de datos | «build systems to collect and process data»; arma «the foundation for all data work» (dbt Labs) | generar, ingerir y almacenar: [Modelado y almacenamiento](../Modelado-y-almacenamiento/modelado-y-almacenamiento.md) e [Ingesta y transformación](../Ingesta-y-transformacion/ingesta-y-transformacion.md) |
| Analytics engineer | «provide clean data sets to users»; pasa el tiempo «transforming, testing, deploying, and documenting data» (dbt Labs) | transformar y modelar hasta la tabla limpia; la [capa semántica](../Visualizacion-y-BI/capa-semantica.md) |
| Analista de datos | «transform raw data into business insights»: problemas de negocio, tendencias, reportes (dbt Labs) | servir: [Análisis](../Analisis/analisis.md), [Analítica de producto](../Analitica-de-producto/analitica-de-producto.md) |
| Analista BI | «deliver actionable insights by working with available data and applying domain expertise»; prepara, modela, visualiza y asegura en una herramienta de BI (Microsoft) | servir: [Visualización y BI](../Visualizacion-y-BI/visualizacion-y-bi.md) |
| Científico de datos | «use analytical tools and techniques to extract meaningful insights from data»; limpia, construye y prueba modelos de machine learning, visualiza y recomienda (BLS) | modelos sobre el dato servido, con [Estadística](../Estadistica/estadistica.md) como base |

Gobierno y calidad no tiene un rol propio en la tabla porque, a criterio de la base, cruza a todos (ninguna fuente leída lo asigna a un rol).
El machine learning del científico de datos queda fuera de este tema.

## El analytics engineer, un rol nombrado por un proveedor

El analytics engineer es el rol más nuevo y el que más depende de una sola fuente. La historia la
cuenta dbt Labs, que vende la herramienta de transformación de la que nació el rol: hay conflicto de
interés. Según su texto, antes de 2012 una empresa contrataba primero un ingeniero de datos. Desde
2012, los almacenes en la nube, la ingesta administrada y el BI de autoservicio hicieron fácil cargar
y reportar, y aparecieron números en conflicto entre reportes. «Starting in 2018», el autor y la
comunidad Locally Optimistic empezaron a llamar analytics engineer a quien arregla eso.

La misma fuente admite que las fronteras son borrosas y que el analytics engineer a veces hace
trabajo de analista. Lo que lo distingue es la forma de trabajar más que el tramo: transforma con
control de versiones, pruebas y despliegue, como un desarrollador. Lo que produce es la tabla que
el analista usa sin volver a limpiar.

## Dónde se pisan los roles

El analista de datos y el analista BI se superponen casi enteros. El analista BI es el que se
especializa en una herramienta de tableros: la certificación de Microsoft reparte su examen en
preparar los datos (25-30 %), modelarlos (25-30 %), visualizar y analizar (25-30 %) y administrar y
asegurar la herramienta (15-20 %). Que modelar pese tanto como visualizar muestra que el analista BI
también hace parte del trabajo del analytics engineer (lectura de la base).

El científico de datos se separa por el modelo predictivo. Según la oficina de estadísticas
laborales de EE.UU. (BLS), la educación típica es una licenciatura en matemática, estadística,
computación o un campo afín. En EE.UU. la mediana salarial de 2025 fue de USD 120.230 al año, con
275.600 empleos y un crecimiento proyectado del 35 % entre 2025 y 2035. Son datos de EE.UU. y no
dicen nada del mercado argentino.

## Qué se aprende primero para analista

Los dos programas leídos empiezan por lo mismo: preguntar bien, conseguir el dato y limpiarlo. El
certificado de Google de Data Analytics usa planilla en los primeros cursos, suma SQL al preparar y
limpiar, pasa a visualización en el curso 6 y deja la programación (Python) para el curso 7 de 9;
el reparto de herramientas por curso sale de las habilidades que lista la página. La
certificación de Microsoft pide dominar el lenguaje de preparación y el de fórmulas de su herramienta
(están en la ficha [herramientas del analista](../Analisis/herramientas-del-analista.md)), y preparar datos pesa entre el 25 y el 30 % del examen.

De ahí sale un orden (lectura de la base): planilla, después [SQL](../Analisis/sql-para-analisis.md)
y [limpieza](../Analisis/limpieza-de-datos.md), después [estadística
descriptiva](../Estadistica/estadistica-descriptiva.md) y [gráficos](../Visualizacion-y-BI/elegir-un-grafico.md),
y recién al final un lenguaje de programación. Para el ingeniero de datos y el analytics engineer
pesa más el [modelado](../Modelado-y-almacenamiento/modelado-dimensional.md) y el SQL de
transformación. El orden con ejercicios está en la [ruta de Data Analytics](ruta-de-data-analytics.md).

> [!NOTE]
> Sin fuente todavía: qué piden de verdad los avisos de trabajo (no se relevaron), y una fuente
> neutral sobre roles que no sea un proveedor ni una certificación.

## El hueco del mercado argentino

No hay en la base una cifra confiable de cuánto gana ni cuántos puestos hay para cada rol de datos
en Argentina. La encuesta de sueldos de Sysarmy 2026.1, publicada el 6 de marzo de 2026, analizó
4.939 respuestas de 5.074 participantes, pero su página de resultados no desglosa los roles de
datos: remite al dataset abierto, que no se leyó. Es una encuesta voluntaria y autorreportada.

Circulan cifras por rol atribuidas a Sysarmy en notas de prensa, sin período ni estadístico
(promedio o mediana) identificables; la base no las usa. Para tener el dato hay que procesar el
dataset abierto de la encuesta filtrando por rol.
