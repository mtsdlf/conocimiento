---
resumen: >-
  El enfoque iterativo entrega el resultado por partes que se pueden usar o mirar, y aprende de cada una para decidir la siguiente. Lo fijo es el largo de cada vuelta y lo que varía es el alcance; no exige ningún marco ni ceremonia.
estado: vigente
estabilidad: estable
fuentes:
  - "Larman y Basili (2003), Iterative and Incremental Development: A Brief History, IEEE Computer 36(6):47-56 (texto completo): https://mosaicprojects.com.au/PDF-Gen/History_of_Iterative_and_Incremental_Development.pdf"
  - "Serrador y Pinto (2015), Does Agile work?, IJPM 33(5) (abstract): https://pure.psu.edu/en/publications/does-agile-work-a-quantitative-analysis-of-agile-project-success/"
  - "Editorial invitado, IEEE Transactions on Engineering Management, ágil fuera de TI (según resumen): https://iris.imtlucca.it/bitstream/20.500.11771/21974/1/IEEE_GuestEditorial_Agile.pdf"
  - "Cambridge IfM, ágil en proyectos de producto con hardware (según resumen): https://www.ifm.eng.cam.ac.uk/uploads/15 Agile project managemetn in non-purely software dev projects.pdf"
  - "Stray, Moe y Sjøberg, stand-ups en 15 equipos (según resumen): https://arxiv.org/pdf/1808.07650.pdf"
  - "Encuesta a 221 desarrolladores sobre stand-ups (según resumen): https://core.ac.uk/works/72981633"
  - "AMCIS 2025, stand-ups y éxito del proyecto (según resumen): https://aisel.aisnet.org/amcis2025/it_pm/it_pm/2"
  - "Gestion-de-proyectos/.investigacion/enfoque.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [desarrollo iterativo e incremental, IID, iterative and incremental development, enfoque adaptativo, ágil, agile, entregas incrementales]
creado: 2026-11-27
revisado: 2026-11-27
---

# Enfoque iterativo

El enfoque iterativo entrega el resultado por partes que se pueden usar o mirar, y aprende de cada una para decidir la siguiente. Lo fijo es el largo de cada vuelta y lo que varía es el alcance; no exige ningún marco ni ceremonia.

Es uno de los [enfoques](enfoque.md) entre los que se [elige](elegir-un-enfoque.md), y una de las tres formas en que esta vertical abre lo que el PMI llama adaptativo. Sirve cuando lo que se quiere se descubre mostrando algo: un servicio nuevo que se prueba con los primeros clientes, una plataforma que se muda por grupos de usuarios, un curso que se ajusta después de cada cohorte.

## Iterar e incrementar son cosas distintas

Iterar es rehacer y mejorar lo mismo con lo que se aprendió en la vuelta anterior. Incrementar es agregar una parte nueva que funciona sola. Una mudanza por oleadas es incremental: cada oleada pasa un grupo de usuarios y queda andando. Un primer borrador de un servicio, que se muestra, se descarta en parte y se rehace, es iterativo. Larman y Basili (2003) tratan las dos como una sola familia, "IID", y el campo suele mezclarlas. La distinción y los riesgos a los que responde cada una (iterar baja el riesgo de construir lo que no era, incrementar el de entregar todo al final) son lectura de la base, no de Larman y Basili.

## Setenta años de iterar sin marcos

Según Larman y Basili, el desarrollo iterativo e incremental se aplica desde mediados de los años 50, y la mayoría de los ejemplos son de los 70 y 80. Citan el Project Mercury de la NASA. El rasgo común era evitar el ciclo de una sola pasada, secuencial, guiado por documentos y con compuertas. Su conclusión: referentes de cada década lo recomendaron, se asoció a muchos proyectos grandes exitosos y lo recomendaron organismos de normas, y aun así algunas organizaciones siguieron promoviendo la cascada como ideal.

El ciclo de Mills y el "hacerlo dos veces" de Royce (este último está en [enfoque predictivo](enfoque-predictivo.md)) eran iterativos sin roles ni eventos con nombre. Inferencia de la base: iterar pide tres cosas: una parte que se pueda mostrar, alguien que la mire con criterio y una decisión sobre la vuelta siguiente. Los marcos de software que agregan roles y reuniones, como Scrum, se tratan en [Desarrollo](../../Desarrollo/Fundamentos/escuelas-de-desarrollo.md#ágil-xp-y-scrum-los-valores-y-los-marcos-que-salieron-de-ellos); el orden de las entregas a un cliente de software, en [plan de entregas](../../Desarrollo/Encargo/plan-de-entregas.md).

## Las ceremonias sirven con condiciones

La evidencia sobre las reuniones de los marcos iterativos es escasa y dice "sirven, con condiciones". La reunión diaria (stand-up) la usa el 87 % de quienes aplican ágil, según el resumen de una encuesta a 221 desarrolladores, y las actitudes son polarizadas. Según los resúmenes de esa encuesta y del trabajo de Stray, Moe y Sjøberg, lo que más aporta a la actitud positiva es compartir información y resolver problemas. A la negativa la empujan el reporte de estado al jefe y una frecuencia o duración que se sienten excesivas. Equipos de seis la valoran más, y la valoración cae por encima de 11 personas.

Un estudio de AMCIS 2025 no encontró vínculo directo entre stand-ups y éxito del proyecto, pero sí asociaciones positivas con la seguridad psicológica y la cohesión, según su resumen. La reunión rinde como coordinación entre quienes hacen el trabajo y no como reunión de estado; informar el estado tiene su propio canal en [informar el estado](../Seguimiento/informar-el-estado.md). Qué de esto pierde peso está en [lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md).

## Fuera del software la evidencia es por analogía

Casi toda la evidencia sobre ágil viene de software. Un editorial de IEEE Transactions on Engineering Management dice que la mayoría de los estudios empíricos son de TI y que casi no hay conocimiento de ágil en otros contextos, según un resumen. Un estudio de Cambridge sobre productos con hardware y software reporta pocos proyectos completados, y en uno de los estudios que revisa hubo tensión entre los equipos ágiles y otras áreas de la empresa en el 70 % de los proyectos (según un resumen). Serrador y Pinto (2015) señalan que ágil se extendió a proyectos no TI y que faltan estudios en otras industrias.

Llevar el enfoque iterativo a un evento, una obra o un servicio es razonable, pero se hace por analogía. El choque con áreas que planifican de forma predictiva (compras, legales, finanzas) sería, por inferencia de la base a partir del dato de Cambridge, un riesgo que conviene [tratar](../Incertidumbre-y-riesgo/riesgo.md) desde el principio.

## Cómo falla

Inferencias de la base, sin fuente.

- **Vueltas sin aprendizaje.** Se entrega cada dos semanas, pero nadie fuera del equipo mira lo entregado y la vuelta siguiente sale del plan original. Es predictivo con más reuniones.
- **Partes que no se pueden mostrar.** Si cada vuelta termina en algo a medias, no hay de qué aprender. La [descomposición](../Planificacion/descomposicion-del-trabajo.md) tiene que dar piezas que se entregan y se verifican solas.
- **Alcance que nunca cierra.** Sin un [criterio de terminado](../Encuadre/resultado-y-terminado.md), cada vuelta abre otra. La [apuesta con tiempo fijo](apuesta-con-tiempo-fijo.md) ataca este riesgo poniendo un tope antes de empezar.

## Iterar cuando ejecutan agentes

Inferencia de esta base: con agentes, las vueltas se acortan porque construir una versión cuesta poco. El límite pasa a ser la retroalimentación, sea de una persona que revisa o del mercado que responde. Si la ejecución se acelera y la revisión no, se acumula trabajo esperando a ser mirado, y el tiempo de cada parte sube aunque el agente sea rápido; el mecanismo está en [trabajo en curso y colas](../Seguimiento/trabajo-en-curso-y-colas.md). Acortar la vuelta sin ampliar la capacidad de revisar no acelera el aprendizaje. Cada parte se da por hecha [con evidencia](../Seguimiento/aceptar-con-evidencia.md), no porque el agente diga que terminó.
