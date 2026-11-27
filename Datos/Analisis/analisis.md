---
resumen: >-
  El análisis es el proceso que lleva de una pregunta de negocio a una decisión: formularla,
  conseguir y preparar los datos, limpiarlos, analizarlos, comunicar lo encontrado y actuar.
estado: vigente
estabilidad: estable
fuentes:
  - "Grow with Google, What is data analytics (21-04-2025): https://grow.google/grow-your-career/articles/what-is-data-analytics/"
  - "Coursera, Google Data Analytics Professional Certificate (página del programa, 2026): https://www.coursera.org/professional-certificates/google-data-analytics"
  - "IBM SPSS Modeler CRISP-DM Guide, v17.0, cap. 1 a 7 (reexpresa CRISP-DM 1.0): https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/17.0FP1/en/ModelerCRISPDM.pdf"
  - "CRISP-DM, Wikipedia (origen y encuestas de uso): https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining"
  - "Microsoft, Study guide for Exam PL-300 (skills measured as of April 20, 2026): https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300"
  - "Brynjolfsson, Hitt y Kim (2011), Strength in Numbers: How Does Data-Driven Decisionmaking Affect Firm Performance? (solo abstract): https://papers.ssrn.com/abstract=1819486"
  - "Datos/.investigacion/analisis.md"
  - "Datos/.investigacion/posicion-contraria.md (secciones 1 y 6)"
aliases: [análisis de datos, data analysis, proceso de análisis, ciclo de análisis, CRISP-DM]
creado: 2026-11-27
revisado: 2026-11-27
---

# Análisis

El análisis es el proceso que lleva de una pregunta de negocio a una decisión: formularla,
conseguir y preparar los datos, limpiarlos, analizarlos, comunicar lo encontrado y actuar.

Es el tramo del [recorrido del dato](../datos.md#del-hecho-registrado-a-la-decisión) donde un
número se vuelve respuesta. Recibe las tablas que dejan
[Ingesta y transformación](../Ingesta-y-transformacion/ingesta-y-transformacion.md) y
[Modelado y almacenamiento](../Modelado-y-almacenamiento/modelado-y-almacenamiento.md), o una
planilla exportada de la tienda cuando no hay nada de eso (cómo se trabaja esa planilla es el tema
[Planillas de cálculo](../../Planillas-de-calculo/planillas-de-calculo.md); SQL como lenguaje, la
vertical [SQL](../../Bases-de-datos/SQL/sql.md) de Bases de datos). Le pide a
[Estadística](../Estadistica/estadistica.md) qué se puede concluir de lo que encuentra, se aplica a
usuarios y compras en [Analítica de producto](../Analitica-de-producto/analitica-de-producto.md) y
entrega lo encontrado a [Visualización y BI](../Visualizacion-y-BI/visualizacion-y-bi.md). Se lee
primero porque las otras verticales de análisis usan este mismo proceso.

## Seis fases, de la pregunta a la acción

El certificado de Data Analytics de Google ordena el trabajo en seis pasos: «Ask, Prepare,
Process, Analyze, Share, Act», según la página de Grow with Google. Los cursos 2 a 6 del
certificado llevan esos verbos en el título; ninguno se dedica a actuar. Las definiciones finas de
cada fase salen de resúmenes de terceros, no de un texto oficial, así que la tabla usa las palabras
de esta base.

| Fase | Qué se hace | Dónde se explica |
|---|---|---|
| Preguntar | Acordar qué decisión depende de la respuesta y qué número la contesta | [Pregunta de análisis](pregunta-de-analisis.md) |
| Preparar | Conseguir los datos, entender de dónde vienen y qué es cada fila | [Ingesta](../Ingesta-y-transformacion/ingesta.md), [metadatos y linaje](../Gobierno-y-calidad/metadatos-y-linaje.md), [grano](sql-para-analisis.md#el-grano-qué-es-una-fila) |
| Limpiar | Ordenar la tabla y decidir qué hacer con faltantes, duplicados y atípicos | [Limpieza de datos](limpieza-de-datos.md) |
| Analizar | Consultar, explorar, resumir y agrupar | [SQL para análisis](sql-para-analisis.md), [análisis exploratorio](analisis-exploratorio.md), [segmentación de clientes](segmentacion-de-clientes.md) |
| Comunicar | Mostrar el hallazgo a quien decide, con el gráfico que lo deja ver | [Contar con datos](../Visualizacion-y-BI/contar-con-datos.md), [elegir un gráfico](../Visualizacion-y-BI/elegir-un-grafico.md) |
| Actuar | Tomar la decisión y, si se puede, probarla | [Experimento A/B](../../Producto/Medicion/experimento-ab.md), [incrementalidad](../../Marketing/Medicion/incrementalidad.md) |

Las fases no van en fila. Limpiar revela que la pregunta estaba mal planteada; explorar muestra que
falta una columna y hay que volver a preparar. Qué clase de respuesta se busca en cada caso (qué
pasó, por qué, qué va a pasar, qué hacer) es el vocabulario de los
[tipos de analítica](tipos-de-analitica.md).

## Dónde se parece y dónde no a CRISP-DM

CRISP-DM es el otro proceso de referencia. Nació como proyecto de un consorcio europeo de empresas
y su primera versión se presentó en 1999, según Wikipedia. Las encuestas de KDnuggets de 2002 a 2014
lo encontraron como la metodología más usada entre quienes respondieron. Sus seis fases son
Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation y Deployment. La
guía de IBM aclara el orden: «The sequence of the phases is not strict. In fact, most projects move
back and forth between phases as necessary».

Las dos listas se corresponden casi una a una. No hay una comparación publicada con método; la que
sigue es lectura de la base:

- Para qué se pensó cada una: las fases de Google son para el analista que contesta preguntas
  de negocio con tablas y gráficos, y terminan en una decisión. CRISP-DM es para proyectos de
  minería de datos y termina en desplegar un modelo.
- Preparar y limpiar: Google los separa; CRISP-DM los junta en Data Preparation, que incluye
  limpiar, construir atributos, integrar fuentes y dar formato.
- Evaluar: CRISP-DM tiene una fase para preguntar si el resultado cumple el objetivo de
  negocio. En las fases de Google esa pregunta queda repartida entre analizar y comunicar.

CRISP-DM no se actualizó: los intentos empezaron en 2006 y a 2015 no habían dado una versión
nueva, según Wikipedia. Reseñas secundarias le critican que no cubre la gestión del proyecto ni lo
que pasa después del despliegue. Un tercer corte es el de Microsoft para el examen PL-300, que no
describe un proceso sino un rol: «Prepare the data», «Model the data» y «Visualize and analyze the
data» pesan 25-30 % cada uno.

## Cómo falla un análisis

La mayoría de las fallas nacen antes de la consulta o después del gráfico, no en el cálculo.

- Empezar por los datos y no por la pregunta: sin una decisión que dependa de la respuesta, el
  análisis produce números que nadie usa. Es el error que la
  [pregunta de análisis](pregunta-de-analisis.md) previene.
- No saber qué es una fila: una tabla de ítems sumada como si fuera de ventas, o un join que
  duplica filas, infla el total sin dar error. Está en [SQL para análisis](sql-para-analisis.md).
- Limpiar sin preguntar por qué falta o por qué sobra: borrar los faltantes o los atípicos
  cambia la respuesta cuando no faltan al azar ([limpieza de datos](limpieza-de-datos.md)).
- Leer causa en un resultado descriptivo: que las ventas subieran después de una promoción no
  dice que la promoción las causó. Eso lo trabajan
  [correlación y causalidad](../Estadistica/correlacion-y-causalidad.md) y los
  [sesgos](../Estadistica/sesgos.md).
- Comunicar sin una decisión asociada: un número en un [tablero](../Visualizacion-y-BI/tablero.md)
  sin una decisión que lo use termina sin que nadie lo mire. Esto es criterio de diseño: el informe
  de posición contraria no encontró estudios con método sobre tableros que nadie mira.

> [!IMPORTANT]
> Que decidir con datos mejore los resultados tiene una evidencia acotada. Brynjolfsson, Hitt y Kim
> (2011) encontraron, en «179 large publicly traded firms», producto y productividad «5-6% higher»
> en las que deciden con datos; es una asociación medida por encuesta en grandes empresas
> (según su abstract). No hay una réplica en comercios chicos. Las cifras que circulan de
> proyectos de datos que fracasan (85 %, 80 %, 87 %) no tienen un método publicado que se haya
> podido verificar, y la base no las usa.

## Lo que hay adentro del análisis

- [Pregunta de análisis](pregunta-de-analisis.md) — cómo se pasa de un pedido vago a una pregunta que los datos pueden contestar. Va primero.
- [Tipos de analítica](tipos-de-analitica.md) — descriptiva, diagnóstica, predictiva y prescriptiva: qué pregunta contesta cada una y por qué no son una escalera.
- [Limpieza de datos](limpieza-de-datos.md) — datos ordenados, faltantes, duplicados, atípicos y formatos sobre la tabla del analista.
- [SQL para análisis](sql-para-analisis.md) — el grano y para qué usa el analista cada pieza del lenguaje (joins y fan-out, agregación, NULL, ventanas); el lenguaje está en [SQL](../../Bases-de-datos/SQL/sql.md) de Bases de datos.
- [Análisis exploratorio](analisis-exploratorio.md) — mirar los datos antes de resumirlos, para generar hipótesis.
- [Segmentación de clientes](segmentacion-de-clientes.md) — agrupar clientes por lo que compran, con RFM, y en qué se diferencia de una cohorte.
- [Herramientas del analista](herramientas-del-analista.md) — ficha con planilla, SQL y Python, con versiones a 2026-11-27.
