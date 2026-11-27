---
resumen: >-
  Ingesta y transformación es la parte de Datos que lleva el dato desde los sistemas donde nace
  hasta el almacén donde se analiza y le da la forma del modelo: traerlo, transformarlo y encadenar
  esos pasos para que corran solos.
estado: vigente
estabilidad: estable
fuentes:
  - "Joe Reis y Matt Housley, Fundamentals of Data Engineering, cap. 7 Ingestion (O'Reilly, 2022); no leído, estructura del capítulo vía buscador: https://oreilly.com/library/view/fundamentals-of-data/9781098108298"
  - "dbt Labs, Understanding ELT: Extract, Load, Transform (2023): https://www.getdbt.com/blog/extract-load-transform"
  - "Apache Airflow, Dags: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html"
  - "Datos/.investigacion/modelado-e-ingesta.md (secciones 7 a 10 y sobre la división del árbol)"
aliases: [pipeline de datos, pipelines, data pipeline, integración de datos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Ingesta y transformación

Ingesta y transformación es la parte de Datos que lleva el dato desde los sistemas donde nace
hasta el almacén donde se analiza y le da la forma del modelo: traerlo, transformarlo y encadenar
esos pasos para que corran solos.

En el recorrido del dato está entre [modelado y
almacenamiento](../Modelado-y-almacenamiento/modelado-y-almacenamiento.md), que decide dónde y con
qué forma se guarda, y el [análisis](../Analisis/analisis.md), que consume las tablas que deja
listas. [Gobierno y calidad](../Gobierno-y-calidad/gobierno-y-calidad.md) controla cada tramo: un
pipeline que corre sin errores puede igual cargar datos malos.

## Primero hay que tener varias fuentes

Si el negocio tiene una sola fuente, como la base de su tienda, no hay nada que mover: se analiza
ahí o sobre una réplica, y esta vertical espera. Aparece cuando hay que cruzar la tienda con el
sistema de pagos, la planilla de costos y los anuncios, o cuando las consultas ya molestan a la
aplicación (lectura de la base). Cuánta infraestructura conviene a un negocio chico está en la
[entrada del tema](../datos.md#cuánta-infraestructura-necesita-un-negocio-chico).

## Traer, dar forma y encadenar

La vertical tiene tres piezas con fronteras claras:

1. Traer el dato crudo, sin cambiarlo, desde cada sistema de origen hasta el almacén. Es la
   [ingesta](ingesta.md), y la decisión principal es cada cuánto: por lotes, en flujo o copiando
   los cambios de la base.
2. Darle forma de modelo: limpiar, unir y calcular hasta tener las tablas de hechos y
   dimensiones del [modelado dimensional](../Modelado-y-almacenamiento/modelado-dimensional.md).
   Si eso pasa antes o después de cargar es la diferencia entre [ETL y ELT](etl-y-elt.md).
3. Encadenar los pasos para que corran solos, en orden y con reintentos. Es la
   [orquestación](orquestacion.md).

La transformación está acá porque es un paso del pipeline, pero lo que produce es el modelo: la
forma la decide modelado y almacenamiento, y esta vertical la construye. Reis y Housley ordenan el
ciclo de la ingeniería de datos en generar, almacenar, ingerir, transformar y servir, y tratan la
orquestación como una preocupación transversal a todas las etapas; esa estructura del libro la
conoce el informe de memoria y no pudo verificarla (la tabla de contenidos dio 403).

## Cómo falla un pipeline

Falla de maneras que el tablero no muestra. Un paso se cae de madrugada y el tablero de la mañana
muestra los números de ayer como si fueran de hoy. Una fuente cambia el nombre de una columna y la
carga sigue, con esa columna vacía. Una tarea que se reintenta carga dos veces el mismo día y las
ventas se duplican. Por eso un pipeline necesita avisar cuando falla y poder correr dos veces sin
duplicar (lectura de la base). Lo primero es de la orquestación; saber de dónde salió cada número
es [metadatos y linaje](../Gobierno-y-calidad/metadatos-y-linaje.md).

## Qué hay adentro de ingesta y transformación

- [Ingesta](ingesta.md) — traer el dato crudo por lotes, en flujo o copiando los cambios de la base, y cómo elegir según la latencia que hace falta.
- [ETL y ELT](etl-y-elt.md) — transformar antes de cargar o cargar crudo y transformar adentro del almacén.
- [Orquestación](orquestacion.md) — encadenar y programar los pasos como un grafo de tareas con dependencias y reintentos.
- [Herramientas de pipeline](herramientas-de-pipeline.md) — ficha con licencia y precio de seis herramientas de ingesta, transformación y orquestación, al 2026-11-27.
