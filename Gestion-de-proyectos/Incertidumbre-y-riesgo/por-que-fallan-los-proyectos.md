---
resumen: >-
  Los grandes proyectos se pasan de costo y de plazo una y otra vez, y el desvío tiene cola gruesa: unos pocos se desvían muchísimo. Eso está respaldado por datos publicados en infraestructura y tecnología, aunque los propios autores admiten que su muestra probablemente no es representativa; la causa (Flyvbjerg la pone en el sesgo de optimismo y la tergiversación) está en disputa.
estado: borrador
estabilidad: semi
fuentes:
  - "Flyvbjerg (2014), What You Should Know About Megaprojects and Why: An Overview, Project Management Journal 45(2):6-19 (se leyó el borrador 9.2): https://arxiv.org/pdf/1409.0003"
  - "Flyvbjerg, Budzier, Lee, Keil, Lunn y Bester (2022), The Empirical Reality of IT Project Cost Overruns: Discovering A Power-Law Distribution, J. Management Information Systems 39(3):607-639: https://arxiv.org/abs/2210.01573"
  - "Flyvbjerg y Gardner (2023), How Big Things Get Done, cifras vía entrevista a Gardner (no se leyó el libro): https://www.mindtools.com/an0e922/how-big-things-get-done"
  - "Reseña de How Big Things Get Done, strategy+business (según resumen): https://www.strategy-business.com/article/Why-do-large-projects-go-over-budget"
  - "Love y Ahiaga-Dagbui (2018), Debunking fake news in a post-truth era, Transportation Research A 113:357-368 (según el abstract): https://econpapers.repec.org/RePEc:eee:transa:v:113:y:2018:i:c:p:357-368"
  - "Flyvbjerg, Ansar, Budzier et al. (2018), Five things you should know about cost overrun, Transportation Research A 118:174-190: https://eprints.whiterose.ac.uk/id/eprint/139423/"
  - "Cemri et al. (2025), Why Do Multi-Agent LLM Systems Fail?, arXiv 2503.13657 (según resumen): https://arxiv.org/abs/2503.13657"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
aliases: [ley de hierro de los megaproyectos, iron law of megaprojects, sobrecosto, cost overrun, cola gruesa, fat tail, sesgo de optimismo, optimism bias, tergiversación estratégica, strategic misrepresentation, fracaso de proyectos]
creado: 2026-11-27
revisado:
---

# Por qué fallan los proyectos

Los grandes proyectos se pasan de costo y de plazo una y otra vez, y el desvío tiene cola gruesa: unos pocos se desvían muchísimo. Eso está respaldado por datos publicados en infraestructura y tecnología, aunque los propios autores admiten que su muestra probablemente no es representativa; la causa (Flyvbjerg la pone en el sesgo de optimismo y la tergiversación) está en disputa.

Es la evidencia sobre la que se apoya el resto de [Incertidumbre y riesgo](incertidumbre-y-riesgo.md): por qué se pronostica con una [clase de referencia](../Planificacion/pronostico.md), por qué el [margen](margenes.md) se dimensiona mirando la cola y por qué se [escala](problemas-y-escalamiento.md) por pronóstico. Las cifras más repetidas del campo, como las del informe CHAOS, no resisten la revisión y están en [mitos](../Fundamentos/mitos-de-gestion-de-proyectos.md); las de esta nota tienen metodología publicada.

## La ley de hierro de los megaproyectos

Flyvbjerg (2014) resume lo que muestran sus datos de megaproyectos: "Nine out of ten such projects have cost overruns. Overruns of up to 50 percent in real terms are common, over 50 percent not uncommon." Los faltantes de beneficios "of up to 50 percent are also common, and above 50 percent not uncommon". Según el mismo trabajo, los sobrecostos "have stayed high and constant for the 70-year period for which comparable data exist", y los sufren todos los países con datos. Su frase para la ley es "Over budget, over time, over and over again".

Los casos que cita, como sobrecostos reales:

| Proyecto | Sobrecosto |
|---|---|
| Túnel del Canal | 80 % |
| Aeropuerto de Denver | 200 % |
| Big Dig de Boston | 220 % |
| Sistema informático del servicio de salud británico | 400-700 % |
| Ópera de Sídney | 1.400 % |

Flyvbjerg calcula además que, si uno de cada diez megaproyectos cumple el presupuesto, uno de cada diez el plazo y uno de cada diez los beneficios, "then approximately one in a thousand projects is a success"; si los números fallaran por un factor dos, serían ocho de cada mil. La cuenta multiplica tres décimas, es decir, supone que las tres cosas son independientes. Es una ilustración, no una medición. El mismo trabajo estima el gasto en megaproyectos en USD 6 a 9 billones por año, el 8 % del PIB mundial.

## La cola gruesa en proyectos de tecnología

El promedio esconde lo que importa. Flyvbjerg, Budzier, Lee, Keil, Lunn y Bester (2022) estudiaron "5,392 IT projects" terminados entre 2002 y 2014, de los cuales 4.677 tenían costo estimado y real. Los sobrecostos siguen una ley de potencia, con "a large number of projects with relatively small overruns and a fat tail".

Los parámetros del ajuste: α = 2,3 (desvío estándar 0,058) desde x0 = 2,0, con el 26,5 % de las observaciones en la cola, 495 proyectos. La x es la razón entre costo real y estimado, no un porcentaje: x0 = 2,0 es costar el doble de lo estimado. Con α entre 2 y 3 la media es finita y la varianza no está definida, así que no hay un desvío "típico" que sirva para planificar. Si se supone una distribución normal, según los autores, los sobrecostos extremos "will be grossly underestimated".

Los autores proponen un mecanismo, probado por simulación: la interdependencia entre componentes tecnológicos produce reacciones en cadena. Es una hipótesis simulada, no demostrada en los datos.

## Las cifras de 2014 y las de 2023 son de poblaciones distintas

Las dos cifras más citadas de Flyvbjerg parecen contradecirse, y no se contradicen porque miden poblaciones distintas.

| Fuente | Población | Cumple el presupuesto | Cómo se leyó |
|---|---|---|---|
| Flyvbjerg (2014) | Megaproyectos | Cerca de uno de cada diez; "nine out of ten" con sobrecosto | Borrador del artículo, leído entero |
| Flyvbjerg y Gardner (2023), *How Big Things Get Done* | Base de más de 16.000 proyectos de tamaños mixtos | "A little under half" | Entrevista a Gardner; el libro no se leyó |

Del libro de 2023 circulan dos cifras más, sin verificar en el libro. Según la entrevista, el 0,5 % cumple presupuesto, plazo y beneficios, "basically a rounding error". Según reseñas, el 8,5 % cumple presupuesto y plazo. Una reseña de strategy+business, en un resumen, da el complemento: 91,5 % pasados de presupuesto, de plazo o de ambos, en una base de 136 países desde 1910.

> [!IMPORTANT]
> La causa del desvío está en disputa.
> - **Flyvbjerg y coautores (2018)**: en su réplica sostienen que la buena práctica exige medición consistente, todos los datos válidos, reconocer que el sobrecosto tiene cola gruesa de forma sistémica, aceptar que su causa raíz es el sesgo conductual y no los cambios de alcance o la complejidad, y corregir con clase de referencia o métodos similares. Dicen que sus críticos violan los cinco puntos.
> - **Love y Ahiaga-Dagbui (2018)**: según su abstract, la división entre error y mentira es una falsa dicotomía; desacreditan afirmaciones de Flyvbjerg, Holm y Buhl (2002) y piden estimaciones basadas en evidencia. Según la réplica, calculan que la muestra óptima habría sido de 383 proyectos contra los 258 de la original.
> - **Lo que conceden los dos lados**: Flyvbjerg y coautores admiten que su muestra probablemente no es representativa y que el sesgo probablemente subestima el sobrecosto de la población, y coinciden en que muestras más grandes son deseables. Los dos lados aceptan que el sobrecosto en transporte es frecuente; discrepan en la causa y en el método.
> - **Estado**: la frecuencia del desvío está bien respaldada. Que la causa raíz sea el sesgo conductual y no el alcance o la complejidad es lo más disputado, y, a juicio de esta base, la réplica lo afirma más de lo que lo prueba. La eficacia del remedio se discute en [pronóstico](../Planificacion/pronostico.md).

## Hasta dónde se puede extrapolar

Los datos son de infraestructura grande y de proyectos de tecnología. Llevarlos a un proyecto chico, a otro dominio o a uno ejecutado en parte por agentes es una extrapolación. Lo que se traslada con más confianza, según la lectura de esta base, es la forma: el desvío va hacia más costo y más plazo, y la cola importa más que el promedio. El tamaño del desvío en un proyecto chico no se conoce.

> [!NOTE] Sin fuente todavía: sobrecosto o fracaso en proyectos chicos o de trabajo del conocimiento fuera de infraestructura y software, y un contrapeso a Flyvbjerg de otro grupo de investigación más allá de Love y Ahiaga-Dagbui.

## Proyectos con agentes

No hay estudios de por qué fallan los proyectos ejecutados en parte por agentes. Lo más cercano es una taxonomía de fallas de sistemas multiagente (Cemri et al.) que pone una de sus tres categorías en la verificación de tareas, según un resumen; está en [riesgo](riesgo.md) y en [fallas de agentes](../../IA/Agentes/fallas-de-agentes.md).

La lectura de esta base es que los agentes no eliminan las dos causas que propone Flyvbjerg y pueden sumar una. El optimismo sigue en quien pronostica, y se ve en que las personas creen que los agentes las aceleran cuando la medición no lo confirma ([frontera irregular](../Personas-y-agentes/frontera-irregular.md)). La tergiversación sigue en quien necesita que el proyecto se apruebe. Lo que se suma es el falso terminado: trabajo que figura como hecho y no lo está, y que aparece tarde.

Los recursos canónicos son Flyvbjerg (2014), en la sección "The Iron Law of Megaprojects", y Flyvbjerg et al. (2022), para el ajuste de la cola y el mecanismo. Fijarse en tres cosas: qué población mide cada número, cómo se mide el sobrecosto (real o nominal, razón o porcentaje) y que el argumento es sobre colas, no sobre promedios.
