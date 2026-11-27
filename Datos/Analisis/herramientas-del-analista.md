---
resumen: >-
  Las herramientas con que un analista prepara, consulta y explora datos (planilla, SQL y Python
  con pandas y Jupyter), con las versiones vigentes al 2026-11-27 y los cambios que rompen
  tutoriales viejos.
estado: vigente
estabilidad: volatil
fuentes:
  - "python.org, Downloads (consultado 2026-11-27): https://www.python.org/downloads/"
  - "pandas, What's new (índice): https://pandas.pydata.org/docs/whatsnew/index.html"
  - "pandas, What's new in 3.0.0 (January 21, 2026): https://pandas.pydata.org/docs/whatsnew/v3.0.0.html"
  - "pandas 3.1.1, Working with missing data: https://pandas.pydata.org/docs/user_guide/missing_data.html"
  - "PostgreSQL 19, documentación Current: https://www.postgresql.org/docs/current/"
  - "JupyterLab, changelog 4.6.x (según resumen): https://jupyterlab.readthedocs.io/en/4.6.x/getting_started/changelog.html"
  - "Coursera, Google Data Analytics Professional Certificate: https://www.coursera.org/professional-certificates/google-data-analytics"
  - "Coursera, Ask Questions to Make Data-Driven Decisions: https://www.coursera.org/learn/ask-questions-make-decisions"
  - "Microsoft, Study guide for Exam PL-300: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300"
  - "Datos/.investigacion/analisis.md (sección 8)"
creado: 2026-11-27
revisado: 2026-11-27
---

# Herramientas del analista

Las herramientas con que un analista prepara, consulta y explora datos (planilla, SQL y Python
con pandas y Jupyter), con las versiones vigentes al 2026-11-27 y los cambios que rompen
tutoriales viejos.

Implementan las fases de preparar, limpiar y analizar del [análisis](analisis.md): la
[limpieza de datos](limpieza-de-datos.md), el [SQL para análisis](sql-para-analisis.md) y el
[análisis exploratorio](analisis-exploratorio.md). Las herramientas para mostrar resultados, como
Power BI, están en la ficha [herramientas de BI](../Visualizacion-y-BI/herramientas-de-bi.md); los motores
donde viven las tablas grandes, en [motores analíticos](../Modelado-y-almacenamiento/motores-analiticos.md).

Copiado de las páginas oficiales el 2026-11-27, salvo JupyterLab, que sale de un resumen.

## Versiones

| Herramienta | Para qué la usa el analista | Versión al 2026-11-27 | Fuente |
|---|---|---|---|
| Planilla (Excel, Google Sheets) | Tablas chicas, cuentas rápidas, compartir con quien no programa | Sin verificar | — |
| PostgreSQL | Practicar y consultar SQL sobre una base real | 19, lanzada el 2026-11-19 según el banner de su documentación | [postgresql.org](https://www.postgresql.org/docs/current/) |
| Python | Lenguaje para limpiar y analizar con código repetible | 3.15.2 (2026-10-25); 3.15 salió el 2026-10-09 | [python.org](https://www.python.org/downloads/) |
| pandas | Tablas en Python: leer, limpiar, agrupar, unir | 3.1.1 (2026-11-04); 3.1.0 del 2026-10-22 | [pandas, What's new](https://pandas.pydata.org/docs/whatsnew/index.html) |
| JupyterLab | Cuadernos que mezclan código, tablas y gráficos | 4.5.6 (2026-03-11) es la más nueva encontrada; puede haber una posterior | [changelog](https://jupyterlab.readthedocs.io/en/4.6.x/getting_started/changelog.html), baja confianza |

Soporte de Python según python.org: 3.14 y 3.15 reciben correcciones; 3.13, 3.12 y 3.11, solo
parches de seguridad; 3.10 llegó a fin de vida el 2026-10-01.

## pandas 3 rompe código de tutoriales viejos

pandas 3.0.0 salió el 2026-01-21. Los materiales grabados con pandas 1.x o 2.x, como probablemente
varios cursos de Data Analytics (lectura de la base), tienen código que ya no funciona igual:

- Texto: «a dedicated string data type is enabled by default». Las columnas de texto ya no son
  de tipo `object`.
- Copy-on-Write: la asignación encadenada («chained assignment», del estilo
  `df[df.x > 0]["y"] = 1`) «will stop working», y desaparece la advertencia
  `SettingWithCopyWarning`.
- Python mínimo: pandas 3.0.0 «supports Python 3.11 and higher».

Las notas de la versión recomiendan pasar primero por pandas 2.3 y arreglar las advertencias de
deprecación antes de subir a 3.

## Faltantes en pandas

`dropna()` borra filas o columnas con faltantes y `fillna()` los reemplaza. La comparación
`df == np.nan` no encuentra faltantes, porque un faltante no es igual a otro; se usa `isna()`. Por
qué falta un dato y qué hacer con él está en
[limpieza de datos](limpieza-de-datos.md#por-qué-falta-un-dato-importa-más-que-cuántos-faltan).

## Qué usa el certificado de Google

El certificado de Data Analytics de Google se cursa en Coursera en 9 cursos. El curso 2 dedica su
módulo 3, «Spreadsheet magic», de 7 horas, a planillas; los siguientes suman SQL, y el curso 7 es
de Python, agregado en lugar de R, que cerraba las versiones anteriores. La página dice «over 180
hours» y los cursos listados suman 151.

El examen PL-300 de Microsoft, para analistas de Power BI, mide habilidades desde el 2026-04-20 y
pide Power Query para preparar datos y DAX para calcular.

## Cuándo cada una

No hay una comparación con método publicada entre planilla, SQL y Python. El criterio que sigue
es de esta base:

- Planilla: cuando los datos entran en una hoja, el análisis se hace una vez y lo tiene que
  revisar alguien que no programa.
- SQL: cuando los datos ya están en una base, hay que unir tablas o el mismo análisis se repite
  cada semana.
- Python: cuando la limpieza tiene muchos pasos que hay que poder repetir, o hace falta
  estadística y gráficos que la planilla no da.

> [!NOTE]
> Sin fuente todavía: versiones y límites de filas de Excel y Google Sheets, la versión vigente de
> DuckDB (su página no respondió) y una comparación con método entre planilla, SQL y Python.
