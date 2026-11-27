# Vistazo: cómo se divide el tema Datos (2026-11-27)

Informe del subagente de vistazo (paso 1 de `documentar`), ocho búsquedas y lecturas. Marcas: [L] leído completo, [M] metadatos o abstract, [S] resumen del buscador.

## 1. Cómo se divide el dominio a sí mismo

### DAMA-DMBOK2: 11 áreas de conocimiento

Gobierno de datos en el centro de la rueda; las otras diez son los radios. Nombres tomados de DATAVERSITY (secundario), no de la guía de DAMA: cotejar con el libro antes de citarlos como exactos.

1. Data Governance
2. Data Architecture
3. Data Modeling & Design
4. Data Storage & Operations
5. Data Security
6. Data Integration & Interoperability
7. Documents & Content
8. Reference & Master Data
9. Data Warehousing & Business Intelligence
10. Metadata
11. Data Quality

- [L, secundario] https://www.dataversity.net/articles/what-is-the-data-management-body-of-knowledge-dmbok/
- [S] https://atlan.com/dama-dmbok-framework/ (blog de proveedor)
- [S] https://www.snowflake.com/en/fundamentals/data-governance/framework/dama-dmbok/ (blog de proveedor)
- Los buscadores dicen que DAMA lanzó en 2025 el proyecto DMBOK 3.0, previsto para 2027 (sin verificar en dama.org).

### Reis y Housley, Fundamentals of Data Engineering (O'Reilly, junio de 2022)

- Ciclo de vida, 5 etapas: generation, storage, ingestion, transformation, serving.
- Undercurrents, 6: security, data management, DataOps, data architecture, orchestration, software engineering.
- [S] https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html (403; la lista sale del resumen del buscador)
- [S] https://greyskullanalytics.substack.com/p/book-review-fundamentals-of-data
- Aviso: [S] https://xebia.com/blog/fundamentals-of-data-engineering/ cuenta 4 etapas y omite serving; error del blog.

### Google Data Analytics Professional Certificate

- Fases ask, prepare, process, analyze, share, act: los cursos 2 a 6 llevan esos verbos en el título. No se leyó una fuente que las enumere como lista.
- Cursos (9 según Coursera): Foundations: Data, Data, Everywhere; Ask Questions to Make Data-Driven Decisions; Prepare Data for Exploration; Process Data from Dirty to Clean; Analyze Data to Answer Questions; Share Data Through the Art of Visualization; Introduction to Data Analysis Using Python; Google Data Analytics Capstone: Complete a Case Study; Accelerate Your Job Search with AI.
- [L] https://www.coursera.org/professional-certificates/google-data-analytics
- Discrepancia: grow.google decía 8 cursos y 240 horas; Credly, 187 horas.

### Microsoft PL-300 (Power BI Data Analyst), skills measured as of April 20, 2026

| Dominio | Peso |
|---|---|
| Prepare the data | 25–30% |
| Model the data | 25–30% |
| Visualize and analyze the data | 25–30% |
| Manage and secure Power BI | 15–20% |

- [L] https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300
- La guía dice que el analista colabora con analytics engineers y data engineers para identificar y adquirir datos.

### CRISP-DM

- Fases: business understanding, data understanding, data preparation, modeling, evaluation, deployment; iterativo. Guía 1.0 de 1999 (NCR, SPSS, DaimlerChrysler).
- [S] https://s2.smu.edu/tfomby/eco5385_eco6380/data/SPSS/CRISPWP-0800%20Data%20Mining%20Standards.pdf ; [S] https://en.wikipedia.com/wiki/CRISP-DM

### Tipos de analítica

- Preguntas atribuidas a Gartner: qué está pasando, por qué pasó, qué va a pasar, cómo hacemos que pase. [S] https://www.gartner.com/en/newsroom/press-releases/2015-02-16-are-you-an-analytic-business-or-just-using-business-analytics
- "Analytic Ascendancy Model": origen sin verificar. [S] https://pub.towardsai.net/the-analytics-maturity-model-how-to-know-where-your-data-team-actually-stands-24953688f57d

### Roles (dbt Labs)

| Rol | Definición de dbt | Tramo |
|---|---|---|
| Data engineer | "build systems to collect and process data" | ingesta, pipelines, infraestructura |
| Analytics engineer | "provide clean data sets to users" | limpiar, transformar, documentar |
| Data analyst | "transform raw data into business insights" | reportes y dashboards |

- [L] https://www.getdbt.com/blog/analytics-engineer-vs-data-analyst-vs-data-engineer (proveedor)
- [S] https://www.ibm.com/think/topics/data-engineer-data-vs-data-scientist-vs-analytics-engineer

## 2. Escuelas (sin búsqueda; citar a la fuente primaria al escribir)

Kimball (dimensional, bottom-up); Inmon (warehouse corporativo normalizado); Data Vault (Linstedt); ETL vs ELT; data mesh (Dehghani) vs plataforma central; frecuentista vs bayesiano; warehouse vs lake vs lakehouse; schema-on-write vs schema-on-read.

## 3. Mapa de fuentes (recomendación sin verificar)

DAMA-DMBOK2; Reis y Housley; Kimball y Ross; Kleppmann; documentación oficial de cada herramienta; ISLR; Kohavi, Tang y Xu; Cleveland, Tufte, Few; CRISP-DM; Google DA y PL-300; dbt (proveedor).

## 4. Propuesta

Un solo tema "Datos": gestión/ingeniería y análisis comparten el flujo dato crudo → modelo → decisión, y los roles de dbt van de un extremo al otro. Partir si la ingeniería crece y tiene otros lectores. Roles como nota transversal, no vertical.

## Huecos

Listas del DMBOK2 y de Reis y Housley sin verificar en primarias; escuelas y mapa sin búsqueda; faltan fuentes para data scientist y BI developer.
