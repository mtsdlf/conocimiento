---
resumen: >-
  Cerrar un proyecto es darlo por terminado con el resultado comprobado y el trabajo traspasado a quien lo va a usar; cancelarlo es pararlo antes porque dejó de justificarse. Las dos son decisiones de gobierno, y la segunda choca con la escalada del compromiso: la tendencia a seguir invirtiendo en lo que no rinde.
estado: borrador
estabilidad: semi
fuentes:
  - "Staw (1976), Organizational Behavior and Human Performance 16, 27-44, doi 10.1016/0030-5073(76)90005-2 (según resúmenes)"
  - "FORRT, atlas de réplicas, ficha de Staw 1976: https://forrt.org/flora-replication-atlas/doi/10.1016/0030-5073(76)90005-2/"
  - "Sleesman, Conlon, McNamara y Miles (2012), metaanálisis de la escalada del compromiso, Academy of Management Journal 55(3) 541-562, doi 10.5465/amj.2010.0696 (solo abstract y catálogos)"
  - "Keil y Robey (1999), Journal of Management Information Systems 15(4) 63-87 (según resúmenes): https://researchr.org/publication/KeilR99/bibtex"
  - "Singer, Shape Up (Basecamp), cap. 8: https://basecamp.com/shapeup/2.2-chapter-08"
  - "Resumen de Shape Up de un tercero (secundaria): https://juststeveking.com/articles/shape-up/"
  - "DIN/Beuth, índice de ISO 21502:2020 (solo el índice): https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:334145134/toc-3233385/download"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
aliases: [cierre del proyecto, project closure, cancelar un proyecto, matar un proyecto, kill a project, escalada del compromiso, escalation of commitment, falacia del costo hundido, sunk cost]
creado: 2026-11-27
revisado:
---

# Cerrar o cancelar

Cerrar un proyecto es darlo por terminado con el resultado comprobado y el trabajo traspasado a quien lo va a usar; cancelarlo es pararlo antes porque dejó de justificarse. Las dos son decisiones de gobierno, y la segunda choca con la escalada del compromiso: la tendencia a seguir invirtiendo en lo que no rinde.

Dentro de [gobierno y cierre](gobierno-y-cierre.md), es la decisión final que el [gobierno del proyecto](gobierno-del-proyecto.md) puede tomar en cualquier punto de control. Cancelar es el mismo mecanismo que la [justificación continua](../Encuadre/justificacion.md), visto desde el final: el caso de negocio se relee, y si ya no se sostiene, el proyecto se cambia o se para.

## Qué hace falta para cerrar bien

Un proyecto está cerrado, según esta base (síntesis propia, no de un estándar), cuando pasan cuatro cosas, y no cuando se termina la última tarea:

1. El resultado está comprobado contra el criterio que se escribió al encuadrar ([resultado y terminado](../Encuadre/resultado-y-terminado.md)), con la evidencia que dice [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md).
2. Lo entregado pasó a quien lo va a operar o usar, con lo necesario para hacerlo sin el equipo del proyecto.
3. Los recursos se liberaron: la gente vuelve al [portafolio](portafolio.md), las cuentas y los contratos se cierran.
4. Quedó decidido qué se aprende y qué se cambia para el próximo ([aprender de un proyecto](aprender-de-un-proyecto.md)).

ISO 21502 distingue en su índice el cierre o la terminación del proyecto (6.8) de las actividades posteriores (6.9); el índice no dice qué incluyen. Que el beneficio llegue después del cierre y que alguien tenga que quedar a cargo de mirarlo es lectura de esta base. En software para un cliente, el paso 2 es el [traspaso](../../Desarrollo/Encargo/traspaso.md).

## La escalada del compromiso

La escalada del compromiso es seguir invirtiendo en un curso de acción que viene fallando, para justificar lo que ya se invirtió. Staw (1976) es citado como su primera descripción: en una simulación de una decisión de inversión, la explicó como autojustificación.

> [!IMPORTANT]
> **El efecto original no se replica de forma pareja.** El atlas de réplicas de FORRT registra dos réplicas directas del estudio de Staw: una con resultado mixto y una fallida. Białek y otros (2021), según su abstract: "No evidence for escalation of commitment amongst the participants was found (N = 365)". Schultze y Schulz-Hardt (2022), con resultado mixto: "In the first of two experiments, we did not find evidence of temporal stability". El respaldo más amplio es el metaanálisis de Sleesman y otros (2012), que reúne los determinantes de la escalada y compara las explicaciones teóricas; esta base solo vio su abstract y no tiene sus resultados cuantitativos. La escalada está bien descrita, pero no conviene presentarla como un efecto universal.

Keil y Robey (1999) estudiaron cómo se sale de la escalada con 42 auditores de sistemas. Según los resúmenes, escalar y desescalar siguen patrones distintos, y ningún factor rescata siempre a un proyecto. La lectura práctica es que la salida no se deja a la voluntad de quien decide en el momento: se diseña antes.

## Diseñar la cancelación antes de necesitarla

Si la escalada es tan frecuente como se la describe, la decisión de parar es difícil de tomar en caliente (inferencia de esta base), y conviene fijarla cuando el proyecto empieza. Tres formas:

- **Un umbral escrito en la justificación.** "Si a los seis meses el canal nuevo atiende menos de la mitad de lo previsto, se revisa." Quien decide después no tiene que inventar el criterio, solo aplicarlo ([justificación](../Encuadre/justificacion.md)).
- **Puntos de control con la opción de parar a la vista.** Al final de cada tramo, seguir es una decisión y no un supuesto ([etapas y puntos de control](../Enfoque/etapas-y-puntos-de-control.md)).
- **Un tope sin prórroga.** En Shape Up, si el equipo no termina en el tiempo fijado, "by default the project doesn't get an extension": funciona como disyuntor. Según un resumen de terceros, el proyecto solo vuelve si se reformula y se apuesta de nuevo. Es una fuente de practicante ([apuesta con tiempo fijo](../Enfoque/apuesta-con-tiempo-fijo.md)).

Cancelar a tiempo vale más cuando los desvíos tienen cola gruesa: si unos pocos proyectos se desvían muchísimo, el costo de seguir con uno que ya se desvió puede no tener techo. Es una inferencia de esta base a partir de los datos de Flyvbjerg, que están en [por qué fallan los proyectos](../Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md).

Cancelar es una de las salidas previstas del gobierno. Un proyecto cancelado a tiempo libera gente para el [portafolio](portafolio.md); uno que sigue por inercia la ocupa sin devolver nada.

## Qué cambia cuando ejecutan agentes

> [!NOTE]
> Sin fuente todavía: no se encontró una fuente sobre la escalada del compromiso o la cancelación en proyectos con agentes.

Lo que sigue es inferencia de esta base. Si ejecutar con agentes cuesta poco, el costo hundido en ejecución pesa menos: tirar lo que hizo un agente y volver a empezar con otro encargo puede ser más barato que corregirlo. Lo que no baja es el tiempo que las personas ya pusieron en encargar y revisar, y ese es el costo hundido que puede empujar a la escalada. También aparece una forma nueva: seguir reintentando con el agente una tarea que cae fuera de lo que hace bien, porque cada intento parece barato. Qué tareas caen de qué lado está en [frontera irregular](../Personas-y-agentes/frontera-irregular.md), y el tope de intentos como condición de parada, en [gobierno del proyecto](gobierno-del-proyecto.md).
