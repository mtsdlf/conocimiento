---
resumen: >-
  La justificación es la razón escrita por la que un trabajo vale lo que cuesta, comparado con no hacerlo o con hacer otra cosa, y la condición bajo la cual deja de valer. Se escribe al empezar y se vuelve a mirar en cada punto de control.
estado: borrador
estabilidad: semi
fuentes:
  - "PRINCE2, principio de justificación continua, resumen en Wikipedia (secundaria; el manual PRINCE2 7 no se leyó): https://en.wikipedia.org/wiki/PRINCE2"
  - "DIN/Beuth, índice de ISO 21502:2020 (solo el índice): https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:334145134/toc-3233385/download"
  - "Flyvbjerg (2014), What You Should Know About Megaprojects and Why, Project Management Journal 45(2): https://arxiv.org/abs/1409.0003"
  - "Serra y Kunc (2015), IJPM 33(1) 53-66, doi 10.1016/j.ijproman.2014.03.011 (no se leyó; dos resúmenes): https://wrap.warwick.ac.uk/id/eprint/60436"
  - "APM, resumen de investigación sobre realización de beneficios (resumen secundario): https://www.apm.org.uk/media/30end0au/research-summary-akt12183-benefits-realisation-lr.pdf"
  - "Universidad de Kent, trabajo que relee a Serra y Kunc (resumen secundario): https://kar.kent.ac.uk/id/document/58128"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
  - "Gestion-de-proyectos/.investigacion/fundamentos.md"
aliases: [caso de negocio, business case, justificación continua, continued business justification, justificación del proyecto, gestión de beneficios, benefits realisation]
creado: 2026-11-27
revisado:
---

# Justificación

La justificación es la razón escrita por la que un trabajo vale lo que cuesta, comparado con no hacerlo o con hacer otra cosa, y la condición bajo la cual deja de valer. Se escribe al empezar y se vuelve a mirar en cada punto de control.

Es la primera pieza del [encuadre](encuadre.md). Las otras dicen qué se va a lograr ([resultado y terminado](resultado-y-terminado.md)) y qué entra ([alcance](alcance.md)); la justificación dice por qué conviene gastar en eso. Sin ella, el [gobierno del proyecto](../Gobierno-y-cierre/gobierno-del-proyecto.md) no tiene contra qué decidir si sigue o para.

## Lo que lleva un caso de negocio

Un caso de negocio sirve si permite que otra persona decida. Para eso tiene cuatro cosas: el costo total esperado, en rangos; el beneficio esperado y cuándo llega; la comparación con las alternativas, incluida la de no hacer nada; y el umbral que lo vuelve falso ("si el costo pasa de tanto, o si el beneficio no aparece para tal fecha, deja de convenir"). Esta lista es una síntesis de esta base; los marcos usan nombres parecidos sin fijar un formato único.

Un ejemplo fuera del software: una organización quiere mudar su atención al público a un canal digital. El caso dice cuánto cuesta la mudanza, cuántas consultas por mes espera atender por el canal nuevo y a qué costo cada una, qué pasa si se queda como está, y que si a los seis meses el canal nuevo atiende menos de la mitad de lo previsto, se revisa. Ese último dato es el que después usa el gobierno.

## Justificación continua: el caso se vuelve a leer

PRINCE2 convirtió esta idea en principio: el proyecto tiene que seguir justificado durante toda su vida, y si el caso de negocio deja de tener sentido, se cambia o se detiene. La fuente es un resumen de Wikipedia; no se cotejó con el manual de la 7.ª edición. ISO 21502 tiene la misma estructura en su índice: un caso de negocio dentro del gobierno del proyecto (4.3.2), una "initial project justification" al iniciar (6.5) y una "progressive justification" mientras se controla el proyecto (6.6). Suma una práctica aparte de gestión de beneficios (7.3).

El lugar donde se relee el caso es el [punto de control](../Enfoque/etapas-y-puntos-de-control.md) entre tramos. Si al releerlo ya no se sostiene, la decisión que sigue es la de [cerrar o cancelar](../Gobierno-y-cierre/cerrar-o-cancelar.md), que es el mismo mecanismo visto desde el final.

## Por qué los casos de negocio prometen de más

Según Flyvbjerg, los casos de negocio y los análisis de costo y beneficio de los megaproyectos se apoyan en costos subestimados y beneficios sobreestimados. En ferrocarriles encontró un sobrecosto medio de 44,7 % junto con una demanda 51,4 % menor a la prevista; en rutas, un sobrecosto medio de 20,4 %. Los datos son de infraestructura grande; la frecuencia de los desvíos y la disputa sobre sus causas están en [por qué fallan los proyectos](../Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md).

La consecuencia práctica es que un caso de negocio sin corrección por optimismo no es confiable. La corrección que proponen Flyvbjerg y sus coautores es pronosticar mirando proyectos parecidos ya terminados, la [clase de referencia](../Planificacion/pronostico.md); su eficacia y la causa del sesgo siguen en disputa. Flyvbjerg nombra como causas el sesgo de optimismo y la tergiversación estratégica; que el optimismo sea una forma de [sobreconfianza](../../Psicologia/Juicio-y-decision/sobreconfianza.md) es una lectura de esta base.

## Si medir los beneficios mejora el resultado

> [!IMPORTANT]
> **Esta base trata como moderada la evidencia de que gestionar beneficios ayude, y se lee de dos maneras.** Serra y Kunc (2015) encuestaron organizaciones de Brasil, Reino Unido y Estados Unidos para ver si las prácticas de realización de beneficios se asocian con el éxito percibido. Un resumen de APM las llama "one of the earliest academic evidences" de su relevancia. Un trabajo posterior de la Universidad de Kent lee el mismo resultado como una relación débil y mixta. Las dos lecturas vienen de resúmenes; el artículo no se leyó.

Aunque la evidencia sea moderada, y como lectura de esta base, escribir el beneficio esperado tiene un uso que no depende de ella: sin un beneficio escrito, nadie puede decir en la mitad del proyecto que dejó de valer la pena.

## Por qué este y no otro

Justificar un proyecto solo no alcanza cuando compite con otros por las mismas personas. La comparación entre proyectos, cuántos entran y en qué orden, está en [portafolio](../Gobierno-y-cierre/portafolio.md). Para ordenar trabajo dentro de un producto, el costo de demora y otros puntajes están en [priorización](../../Producto/Planificacion-y-entrega/priorizacion.md).

## Qué cambia cuando ejecutan agentes

> [!NOTE]
> Sin fuente todavía: ninguna fuente encontrada trata la justificación de proyectos con agentes de IA.

Lo que sigue es inferencia de esta base. Si un agente ejecuta, el costo de producir baja, pero el de especificar, revisar y aceptar no baja en la misma proporción. Un caso de negocio que solo cuente lo que cuesta producir subestima el proyecto: tiene que incluir las horas de las personas que encargan y verifican, que suelen ser el recurso escaso ([la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md)). Cómo se estima ese costo está en [capacidad y costo](../Planificacion/capacidad-y-costo.md).

Tampoco se da por supuesto que el agente rinda más: las mediciones con desarrolladores dieron resultados de signo distinto, y están en [frontera irregular](../Personas-y-agentes/frontera-irregular.md). Un caso de negocio que dependa de esa ganancia la trata como un supuesto a probar temprano ([supuestos](../Incertidumbre-y-riesgo/supuestos.md)).
