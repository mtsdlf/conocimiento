---
resumen: >-
  La estrategia de mantenimiento es la decisión de qué mantenimiento se le hace a cada equipo: repararlo cuando falla, intervenirlo a intervalos fijos de tiempo o de uso, vigilar su condición e intervenir cuando avisa, o dejarlo fallar a propósito. Se decide equipo por equipo, y a veces modo de falla por modo de falla, según cuánto importa que falle y cómo falla.
estado: borrador
estabilidad: estable
fuentes:
  - "DOE/FEMP, O&M Best Practices Guide, Release 3.0, cap. 5 «Types of Maintenance Programs»: https://www1.eere.energy.gov/femp/pdfs/OM_5.pdf"
  - "NASA, Reliability Centered Maintenance Guide for Facilities and Collateral Equipment, copia de febrero de 2000, fig. 1-1 y sec. 1.2: https://everyspec.com/NASA/NASA-General/download.php?spec=NASA_RCM_GUIDE_2000.030306.pdf"
  - "Wikipedia, Corrective maintenance (cita NF EN 13306; según su resumen): https://en.wikipedia.org/wiki/Corrective_maintenance"
  - "Wikipedia, Preventive maintenance (según su resumen): https://en.wikipedia.org/wiki/Preventive_maintenance"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.1 «Plan asset maintenance» y 10.3.3 «Perform asset maintenance»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/estrategia-y-fundamentos.md (componente A, mitos y segunda ronda, 2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/apqc-10.md (2026-11-27)"
aliases: [estrategia de mantenimiento, maintenance strategy, tipos de mantenimiento, types of maintenance, política de mantenimiento, maintenance policy, programa de mantenimiento, maintenance program]
creado: 2026-11-27
revisado:
---

# Estrategia de mantenimiento

La estrategia de mantenimiento es la decisión de qué mantenimiento se le hace a cada equipo: repararlo cuando falla, intervenirlo a intervalos fijos de tiempo o de uso, vigilar su condición e intervenir cuando avisa, o dejarlo fallar a propósito. Se decide equipo por equipo, y a veces modo de falla por modo de falla, según cuánto importa que falle y cómo falla.

Es la segunda vertical de [Activos y mantenimiento](../activos-y-mantenimiento.md). Toma del [registro de activos](../Registro-de-activos/registro-de-activos.md) qué equipos hay y su [criticidad](../Registro-de-activos/criticidad.md), y devuelve un plan que genera [órdenes de trabajo](../Orden-de-trabajo/orden-de-trabajo.md). El [historial del equipo](../Registro-de-activos/historial-del-equipo.md) y los [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md) dicen después si la decisión fue buena. APQC 7.4 la pone en 10.3.1.1 «Develop maintenance strategies» y 10.3.1.3 «Specify maintenance policies», antes de crear los planes de trabajo.

## Los tipos de mantenimiento, por qué dispara la intervención

El campo usa dos taxonomías que se solapan. La norteamericana (la guía del DOE y la de la NASA) habla de reactivo, preventivo, predictivo y proactivo. La europea, la norma EN 13306, distingue entre otras cosas el correctivo inmediato y el diferido; esta base no la leyó y toma esas dos definiciones de un resumen de Wikipedia, sin poder verificar el resto de la norma. Las dos taxonomías ordenan lo mismo: qué hace que alguien intervenga el equipo (lectura de la base).

- **Correctivo inmediato.** Se repara después de detectar la falla y se empieza enseguida. Según el resumen de Wikipedia, EN 13306 define el correctivo como «maintenance which is carried out after failure detection», y el inmediato como el que «starts immediately after a failure».
- **Correctivo diferido.** La falla ya ocurrió, pero la reparación se demora según reglas fijadas de antemano («delayed in conformance to a given set of maintenance rules»). El caso típico es un equipo que sigue andando a medias o tiene respaldo, y la orden entra al pendiente (ejemplo de la base).
- **Preventivo por calendario.** Se interviene cada cierto tiempo, haya o no síntomas: la inspección mensual o el cambio de una correa cada seis meses.
- **Preventivo por uso.** Se interviene cada cierta cantidad de uso: horas de marcha, kilómetros, ciclos. El DOE define el preventivo como acciones «on a time- or machine-run-based schedule», y su ejemplo es cambiar el aceite cada 3.000 a 5.000 millas.
- **Por condición (predictivo).** Se mide el estado del equipo y se interviene cuando muestra que va a fallar. El DOE lo distingue del preventivo por basarse «on the actual condition of the machine rather than on some preset schedule»: analizar el aceite permite estirar el cambio hasta 10.000 millas.
- **Dejar fallar.** Se decide no hacer nada hasta que falle, porque prevenir cuesta más que la falla. El DOE llama reactivo al modo «run it till it breaks»; dejar fallar es ese mismo modo cuando se elige, no cuando pasa por descuido (esta distinción es criterio de la base).

La guía del DOE titula su sección «Predictive Maintenance (Condition-Based Maintenance)» y trata los dos nombres como uno. Wikipedia, en cambio, presenta el predictivo como una forma del mantenimiento por condición que usa sensores y tendencias. Esta base usa **mantenimiento por condición** y deja predictivo como sinónimo; el detalle está en [mantenimiento por condición](mantenimiento-por-condicion.md).

> [!NOTE] Sin fuente todavía: la búsqueda de fallas ocultas (probar periódicamente una protección que solo actúa cuando otra cosa falla, como una alarma o una válvula de alivio) es una tarea que propone el RCM, no un tipo normativo. Falta una fuente leída que la defina; Nowlan y Heap y Moubray no se abrieron. Tampoco se confirmaron «mejorativo» ni «detectivo» como tipos de ninguna norma.

## Qué tipo conviene a qué equipo

| Tipo | Dispara la intervención | Conviene cuando | Riesgo propio |
|---|---|---|---|
| Correctivo inmediato | La falla | No hay manera razonable de anticiparla y la falla para algo que importa | Paradas imprevistas, urgencias, horas extra |
| Correctivo diferido | La falla, con reglas para demorar | El equipo sigue funcionando a medias o hay respaldo | Que el pendiente crezca y la falla empeore |
| Preventivo por calendario | Una fecha | El desgaste depende del tiempo (corrosión, vencimientos, inspecciones obligatorias) | Intervenir equipos sanos |
| Preventivo por uso | Un contador | El desgaste depende de cuánto se usa (horas, kilómetros, ciclos) | Depende de que alguien cargue las lecturas |
| Por condición | Una medición que muestra falla en camino | La falla avisa con tiempo para actuar | Inversión en instrumentos y en gente que sepa leerlos |
| Dejar fallar | Nada hasta la falla | La falla es barata, sin consecuencias de seguridad y fácil de reparar | Elegirlo por omisión para equipos que sí importan |

La columna «conviene cuando» sigue la figura 1-1 de la guía de la NASA. Para la NASA, el reactivo sirve para elementos chicos, no críticos, sin consecuencia, improbables de fallar o redundantes. El preventivo sirve para lo sujeto a desgaste, los consumibles y lo que tiene un patrón de falla conocido. El predictivo sirve para fallas aleatorias, sin desgaste, o inducidas por el propio preventivo. La NASA suma un cuarto, el proactivo, que usa análisis de causa raíz, exploración de edad y FMEA. El reparto entre calendario y uso, y los riesgos de cada fila, son lectura de la base sobre lo que dicen el DOE y la NASA.

## Cómo se elige: criticidad primero, modo de falla después

La primera pregunta es cuánto importa que el equipo falle. Eso lo responde la [criticidad](../Registro-de-activos/criticidad.md), que ordena los equipos por consecuencia y probabilidad de falla. Un equipo de criticidad baja, con respaldo y falla barata, pasa a dejar fallar sin más análisis; uno de criticidad alta merece mirar cómo falla. Usar la criticidad como filtro para decidir dónde gastar el análisis es criterio de la base, coherente con lo que la NASA reserva para el reactivo.

La segunda pregunta es cómo falla. Un equipo no falla de una sola manera: un motor puede quemar un bobinado, gastar un rodamiento o soltar una conexión, y cada modo pide una tarea distinta. El método que hace esa pregunta de forma ordenada es el **mantenimiento centrado en la confiabilidad** (RCM). No es un tipo más de la tabla: es el procedimiento que elige entre ellos. La NASA lo dice así: el RCM «includes reactive, preventive, predictive, and proactive maintenance». Está en [mantenimiento centrado en la confiabilidad](mantenimiento-centrado-en-confiabilidad.md).

Para no elegir el preventivo por calendario por defecto hay una razón de la NASA: según su guía, los estudios de la aviación de fines de los sesenta mostraron que «the basic premise of time based maintenance was false for the majority of equipment». El mantenimiento productivo total (TPM) y la gestión de activos de la ISO 55000 son otros enfoques, en otro plano; están en [fundamentos de activos y mantenimiento](../Fundamentos/fundamentos-de-activos-y-mantenimiento.md).

## Las cifras de ahorro que circulan y por qué no sirven de dato

Varias cifras que se repiten sobre cada tipo vienen de la guía del DOE, y casi ninguna trae fuente. La guía dice que el preventivo ahorra un «Estimated 12% to 18%» sobre el reactivo y que un predictivo que funciona ahorra «8% to 12%» sobre el preventivo solo, sin citar estudios. Atribuye a «independent surveys» un retorno de la inversión de «10 times», una reducción de costos de mantenimiento de «25% to 30%», una eliminación de roturas de «70% to 75%», una reducción de paradas de «35% to 45%» y un aumento de producción de «20% to 25%». La lista de referencias del capítulo trae solo la guía de la NASA y un artículo de revista comercial sobre bombas.

La misma guía dice que una instalación promedio hace «>55% Reactive, 31% Preventive, 12% Predictive, 2% Other», según «Studies as recent as the winter of 2000», también sin citar cuáles. Una encuesta de NIST de 2020 a fábricas de EE.UU. dio otro promedio de mantenimiento reactivo, 45,7 % (ver [fundamentos](../Fundamentos/fundamentos-de-activos-y-mantenimiento.md)). Como criterio de la base, estas cifras no sirven para justificar una inversión, y quien las use en una propuesta tiene que decir de dónde salen y que no tienen estudio detrás.

## Qué hay en Estrategia de mantenimiento

- [Mantenimiento preventivo](mantenimiento-preventivo.md) — el plan con sus tareas y frecuencias, por calendario o por contador, cómo genera órdenes y el riesgo de sobremantener.
- [Mantenimiento por condición](mantenimiento-por-condicion.md) — inspección y monitoreo, la curva P-F y cuándo vale la pena vigilar en lugar de cambiar.
- [Mantenimiento centrado en la confiabilidad](mantenimiento-centrado-en-confiabilidad.md) — el método RCM, las siete preguntas, los seis patrones de falla de Nowlan y Heap, el FMEA y las cautelas sobre sus cifras.
