---
resumen: >-
  Licencias y precios públicos de cinco herramientas de BI (Power BI, Tableau, Looker Studio,
  Metabase y Superset), copiados el 2026-11-27 con su fuente y sus discrepancias.
estado: vigente
estabilidad: volatil
fuentes:
  - "Microsoft, Power BI pricing (según su resumen): https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing"
  - "Metabase, Pricing (según su resumen): https://www.metabase.com/pricing/"
  - "Apache Superset, README (según su resumen): https://github.com/apache/superset"
  - "Tableau, Pricing (la página dio 403; cifras de los resultados del buscador): https://www.tableau.com/pricing/cloud"
  - "Google Cloud, Looker Studio Pro subscription overview (el precio oficial no se pudo leer): https://docs.cloud.google.com/looker/docs/studio/pro-subscription-overview"
  - "Datos/.investigacion/metricas-y-visualizacion.md (sección 7)"
aliases: [herramientas de business intelligence, BI tools, Power BI, Tableau, Looker Studio, Metabase, Superset]
creado: 2026-11-27
revisado: 2026-11-27
---

# Herramientas de BI

Licencias y precios públicos de cinco herramientas de BI (Power BI, Tableau, Looker Studio,
Metabase y Superset), copiados el 2026-11-27 con su fuente y sus discrepancias.

Son las herramientas con las que se arma un [tablero](tablero.md), y cada una trae su propio
modelo para la [capa semántica](capa-semantica.md). Los precios cambian seguido: antes de usarlos,
confirmalos en la página de cada una.

Copiado el 2026-11-27. Casi todo se leyó a través de un resumen de la página, no del texto completo.
Los precios están en dólares, sin impuestos, y por usuario por mes con pago anual salvo que se diga
otra cosa.

| Herramienta | Licencia y precio público | Fuente | Cómo se leyó |
|---|---|---|---|
| Power BI | Desktop gratis ("is available as a free download"); Pro USD 14,00; Premium Per User USD 24,00. Para compartir hay que pasar a Pro o Premium | [Microsoft](https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing) | resumen de la página |
| Tableau | Standard: Creator USD 75, Explorer USD 42, Viewer USD 15. Enterprise: Creator USD 115, Explorer USD 70, Viewer USD 35. Hace falta al menos una licencia Creator por despliegue; los precios varían por región | [Tableau](https://www.tableau.com/pricing/cloud) | la página dio 403; cifras de los resultados del buscador |
| Looker Studio | Tiene una versión gratuita (no verificada en esta ronda). Pro: USD 9 por usuario por proyecto por mes según la mayoría de las fuentes, USD 7 según una | [Google Cloud](https://docs.cloud.google.com/looker/docs/studio/pro-subscription-overview) | el precio oficial no se pudo leer |
| Metabase | Open Source gratis, licencia AGPL. Starter (en la nube) USD 100 por mes o USD 1.080 por año, con 5 usuarios y USD 6 por mes por usuario extra. Pro USD 575 por mes o USD 6.210 por año, con 10 usuarios. Enterprise desde USD 20.000 por año | [Metabase](https://www.metabase.com/pricing/) | resumen de la página |
| Superset | Código abierto, licencia Apache-2.0. Se describe como "Data Visualization and Data Exploration Platform", con constructor de gráficos sin código, editor SQL y "a lightweight semantic layer". La versión y la fecha del último release no se vieron | [GitHub](https://github.com/apache/superset) | resumen del README |

> [!IMPORTANT]
> Looker Studio Pro tiene dos precios en las fuentes: USD 9 o USD 7 por usuario por proyecto por mes.
> No se pudo confirmar el oficial. Los precios de Tableau salen de resultados del buscador, porque la
> página oficial no se dejó leer.

> [!NOTE]
> Sin fuente todavía: los precios en pesos y los impuestos que se suman en Argentina, la condición de
> la versión gratuita de Looker Studio y la versión vigente de Superset.

La capa semántica fuera de la herramienta de BI, en la capa de modelado, la ofrece dbt en sus planes
Starter y Enterprise, según su documentación, que es inconsistente sobre el plan Enterprise+
([dbt Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl)).
