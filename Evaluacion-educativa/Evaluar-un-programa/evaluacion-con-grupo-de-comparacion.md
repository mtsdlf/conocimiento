---
resumen: >-
  Evaluar un programa con grupo de comparación es medir el mismo resultado en quienes hicieron el curso y en quienes no, para atribuirle la diferencia. Los estándares del What Works Clearinghouse ponen arriba los diseños con asignación controlada y exigen que los grupos empiecen parecidos.
estado: vigente
estabilidad: estable
fuentes:
  - "What Works Clearinghouse, Procedures and Standards Handbook v5.0: https://ies.ed.gov/ncee/wwc/Docs/referenceresources/Final_WWC-HandbookVer5.0-0-508.pdf"
  - "EEF, Teaching and Learning Toolkit (no leído): https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit"
  - "EEF (2019), Classification of the security of findings from EEF evaluations, versión 2.0 (texto completo de las secciones A a C y del apéndice 1): https://d2tic4wvo1iusb.cloudfront.net/production/documents/evaluation/peer-review-process/Classifying_the_security_of_EEF_findings_2019.pdf"
  - "EEF (2023), Teaching and Learning / Early Years Toolkit guide (texto completo, sección Evidence strength): https://d2tic4wvo1iusb.cloudfront.net/production/documents/toolkit/toolkit_guide_2025_v3.0.0.pdf"
  - "EEF, Evaluation design (página de guías para evaluadores): https://educationendowmentfoundation.org.uk/projects-and-evaluation/evaluation/evaluation-guidance-and-resources/evaluation-design"
  - "Evaluacion-educativa/.investigacion/adaptativa-calificacion-programa.md"
  - "Evaluacion-educativa/.investigacion/fuentes-evaluar-un-programa-2026-11.md"
aliases: [diseño experimental, grupo de control, ensayo aleatorizado, cuasiexperimento, What Works Clearinghouse, WWC, evaluación de impacto]
creado: 2026-11-27
revisado: 2026-11-27
---

# Evaluación con grupo de comparación

Evaluar un programa con grupo de comparación es medir el mismo resultado en quienes hicieron el curso y en quienes no, para atribuirle la diferencia. Los estándares del What Works Clearinghouse ponen arriba los diseños con asignación controlada y exigen que los grupos empiecen parecidos.

Es la tradición educativa de [evaluar un programa](evaluar-un-programa.md), y la respuesta al problema que deja abierto el [retorno de la capacitación](retorno-de-la-capacitacion.md): sin comparación no se sabe qué parte del cambio es del curso. Cómo se leen los resultados de estos estudios (tamaños de efecto, por qué los ensayos grandes dan efectos chicos) es transversal al área y está en [evidencia en educación](../../Didactica/Fundamentos/evidencia-en-educacion.md) y en [cómo leer un estudio](../../Psicologia/Fundamentos/como-leer-un-estudio.md).

## Los estándares del What Works Clearinghouse

El What Works Clearinghouse (WWC), del Institute of Education Sciences de Estados Unidos, califica estudios de programas educativos con un manual público (versión 5.0, leída):

El desgaste (*attrition*) es la proporción de participantes que se pierde antes de la medición final; si se van más de un grupo que del otro, los grupos dejan de ser comparables. La discontinuidad de regresión compara a quienes quedaron apenas por encima y apenas por debajo de un puntaje de corte que decidía quién entraba al programa: a ambos lados del corte las personas son casi iguales.

| Diseño | Calificación máxima |
|---|---|
| Experimento aleatorizado con poco desgaste, discontinuidad de regresión, diseño de caso único | «Meets WWC Standards Without Reservations» |
| Cuasiexperimento, o aleatorizado con desgaste alto | «With Reservations» |

Para los cuasiexperimentos y los aleatorizados comprometidos, el manual exige equivalencia de partida: en las variables clave, los grupos no pueden diferir en más de 0,25 [desviaciones estándar](../../Didactica/Fundamentos/glosario-de-didactica.md#leer-la-evidencia). Entre 0,05 y 0,25 hace falta ajuste estadístico; por debajo de 0,05, no.

La lógica de fondo: si los grupos empezaron distintos, la diferencia del final puede venir de ahí y no del programa.

## Los candados de la EEF

La Education Endowment Foundation (EEF), de Inglaterra, califica la solidez de la evidencia con candados (*padlocks*), de 0 a 5. Usa dos escalas distintas: una para cada evaluación que financia y otra para cada tema de su Toolkit.

**En una evaluación.** El documento de 2019 (versión 2.0) califica solo el resultado principal y mira sobre todo la validez interna. Cinco candados es «the most robust evidence that could be expected from a single study»; cero, un estudio que «adds little to the evidence base». La nota no dice si el programa funcionó: el efecto se informa al lado. Dos revisores califican con tres criterios, cada uno de 0 a 5, y la nota provisoria es la más baja de las tres:

| Candados | Diseño | Efecto mínimo detectable (MDES) | Desgaste |
|---|---|---|---|
| 5 | Aleatorizado | hasta 0,2 | 0-10 % |
| 4 | Considera algo de lo no observable (discontinuidad de regresión, diferencias en diferencias) | 0,21-0,29 | 11-20 % |
| 3 | Considera todos los factores observables relevantes (*matching*, regresión) | 0,30-0,39 | 21-30 % |
| 2 | Considera solo algunos factores relevantes | 0,40-0,49 | 31-40 % |
| 1 | No considera ningún factor relevante | 0,50-0,59 | 41-50 % |
| 0 | Sin grupo de comparación | 0,6 o más | más de 50 % |

El efecto mínimo detectable depende sobre todo del tamaño de la muestra («MDES is highly dependent upon the sample size»). Después, las amenazas a la validez interna (por ejemplo, otras intervenciones al mismo tiempo o datos faltantes) pueden bajar hasta dos candados. A diferencia del WWC, la EEF mide el desgaste total y no la diferencia entre grupos.

**En el Toolkit.** Cada tema arranca con candados según cuántos estudios cumplen los criterios de inclusión: de 11 a 39 es «Very limited evidence», y 120 o más es «Very Extensive evidence». Con menos de 11 estudios el tema recibe cero candados y no informa meses de progreso. Después pierde candados si pocos estudios son recientes, si muchos no son ensayos aleatorizados, si se hicieron en condiciones distintas de la escuela común, si no los evaluó alguien independiente o si los resultados varían sin explicación. Todos los estudios del Toolkit tienen grupo de comparación.

La EEF también publica guías para quien evalúa: análisis estadístico (2022), evaluación de implementación (2022), costos (2023) y pilotos (2023), entre otras. Solo se leyó su lista.

## Con un curso chico

Con pocas personas, un ensayo aleatorizado formal no es viable. Las opciones realistas, como inferencia del informe de esta base (ninguna fuente las valida):

1. Compará con la cohorte anterior o con una lista de espera, usando la misma prueba.
2. Medí antes y después, no solo después.
3. Usá un criterio que no sea la opinión de los participantes: una tarea, no la encuesta (ver [niveles de Kirkpatrick](niveles-de-kirkpatrick.md)).
4. Que no evalúe quien enseñó, o que corrija sin saber de qué grupo es cada trabajo.

Ninguna de estas comparaciones llega al estándar del WWC; sirven para no confundir el efecto del curso con lo que la gente ya traía.

> [!NOTE] Sin fuente todavía: el contenido de las guías de evaluación de la EEF (solo se leyó su lista).
