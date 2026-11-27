---
resumen: >-
  Aprender de un proyecto es convertir lo que pasó en un cambio concreto en cómo se hace el próximo: una regla, una lista, una prueba, un umbral. La retrospectiva o el análisis de fallas solo sirven si terminan en ese cambio, y la investigación dice que aprender de un proyecto al siguiente se descuida seguido.
estado: borrador
estabilidad: semi
fuentes:
  - "Williams (2008), How do organizations learn lessons from projects—and do they?, IEEE Transactions on Engineering Management 55(2) 248-266, doi 10.1109/TEM.2007.912920 (según resúmenes; la página dio 403): https://eprints.soton.ac.uk/148943"
  - "Resumen de Williams (2008) en el repositorio de Hull (secundaria): https://hull-repository.worktribe.com/output/417989/how-do-organizations-learn-lessons-from-projectsand-do-they"
  - "Edmondson (1999), Psychological Safety and Learning Behavior in Work Teams, Administrative Science Quarterly 44(2) 350-383 (según resúmenes): https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f"
  - "Beyer y otros, Site Reliability Engineering (Google), cap. 15 Postmortem Culture: https://sre.google/sre-book/postmortem-culture/"
  - "PRINCE2, principio de aprender de la experiencia, resumen en Wikipedia (secundaria): https://en.wikipedia.org/wiki/PRINCE2"
  - "DIN/Beuth, índice de ISO 21502:2020 (solo el índice): https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:334145134/toc-3233385/download"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [lecciones aprendidas, lessons learned, retrospectiva, retrospective, revisión posterior al proyecto, post-project review, análisis de fallas]
creado: 2026-11-27
revisado:
---

# Aprender de un proyecto

Aprender de un proyecto es convertir lo que pasó en un cambio concreto en cómo se hace el próximo: una regla, una lista, una prueba, un umbral. La retrospectiva o el análisis de fallas solo sirven si terminan en ese cambio, y la investigación dice que aprender de un proyecto al siguiente se descuida seguido.

Es la última decisión de [gobierno y cierre](gobierno-y-cierre.md): al [cerrar o cancelar](cerrar-o-cancelar.md) un proyecto, alguien decide qué se cambia. Los marcos le dan un lugar propio. PRINCE2 tiene "aprender de la experiencia" entre sus siete principios, según el resumen de Wikipedia, e ISO 21502 tiene una práctica de lecciones aprendidas (7.18) en su índice.

## Lo que se sabe de si las organizaciones aprenden

Williams (2008) se preguntó cómo aprenden las organizaciones de sus proyectos, y si lo hacen. Según un resumen, encuestó a 522 gerentes de proyecto de Reino Unido, Estados Unidos y China. Su conclusión, según el abstract, es que aprender de un proyecto al siguiente es de importancia vital pero a menudo se descuida. Según un resumen del buscador, las actividades de lecciones aprendidas son más frecuentes en organizaciones más maduras en gestión de proyectos. En un trabajo de 2006, según el buscador, el mismo autor encontró que los proyectos a menudo no se revisan en absoluto. Un resumen de terceros agrega tres causas: falta de tiempo, falta de apoyo de la gerencia y una cultura de culpa.

> [!NOTE]
> Sin fuente todavía: la frase repetida de que las lecciones aprendidas "casi nunca se usan" no aparece en el abstract de Williams y no se cotejó con su texto. Tampoco se encontraron estudios sobre el efecto de las retrospectivas como tales.

## De un documento a un cambio

El modo más común de fallar es producir un documento de lecciones que nadie vuelve a leer. Una lección sirve si cambia algo que el próximo proyecto no puede dejar de usar. Para eso:

1. Juntá los hechos antes que las opiniones: qué se pronosticó, qué pasó, dónde se desvió y cuándo se supo.
2. Para cada desvío importante, preguntá qué del sistema lo permitió (una regla que faltaba, un criterio ambiguo, un punto de control sin opción de parar), no quién se equivocó.
3. Elegí pocos cambios, cada uno con una persona a cargo y una fecha.
4. Ponelos donde el próximo proyecto los va a encontrar sin buscarlos: en la plantilla del encargo, en la lista de verificación del punto de control, en la clase de referencia que se usa para [pronosticar](../Planificacion/pronostico.md).
5. En el cierre del próximo proyecto, revisá si el cambio se aplicó y si sirvió.

Sin el paso 4, lo aprendido queda en un documento. Esta lista es una síntesis de esta base; la de un postmortem de incidentes, que se parece, está en [postmortem sin culpa](../../DevOps/Cultura-y-medicion/postmortem-sin-culpa.md). Allí también está por qué un postmortem que nadie revisa no sirve y por qué señalar culpables hace que los problemas dejen de reportarse. Esa práctica viene de incidentes de producción y no de cierres de proyecto; que valga igual para un proyecto es una extrapolación.

## Por qué la culpa frena el aprendizaje

La idea de fondo es que un equipo aprende si sus miembros pueden decir que algo salió mal sin pagar por decirlo. Edmondson (1999) encontró, en 51 equipos de una manufacturera, que la seguridad psicológica se asocia con conductas de aprendizaje, y que esas conductas median hacia el desempeño. El detalle y la discusión sobre si la causa están en [seguridad psicológica](../../Liderazgo-y-direccion/Equipos-y-cultura/seguridad-psicologica.md).

La consecuencia para el cierre es concreta. Si la revisión del proyecto puede terminar en una sanción, quien sabe dónde se rompió probablemente calle y la lección que quede sea la que nadie discute. Es una inferencia de esta base: Google SRE lo dice de incidentes de producción, no de proyectos. La cultura de culpa aparece también entre las causas que el resumen de Williams da para que no se aprenda.

## Qué pierde peso

La retrospectiva ritual al final de cada ciclo, con el mismo formato y sin cambios que se sigan, es una de las ceremonias que esta base trata como en retirada ([lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md)). No hay evidencia que lo mida: la investigación de la posición contraria no encontró estudios sobre retrospectivas. Lo que se sostiene es el mecanismo, no el ritual: revisar hechos, cambiar el sistema y comprobar que el cambio sirvió.

## Qué cambia cuando ejecutan agentes

> [!NOTE]
> Sin fuente todavía: no se encontró una fuente sobre lecciones aprendidas en proyectos ejecutados por agentes.

Lo que sigue es inferencia de esta base. Con agentes, la lección útil casi siempre termina en un cambio del entorno donde trabajan: una instrucción nueva en el encargo, una prueba que faltaba, un límite de permisos, un criterio de terminado más estricto. Un agente no lee el documento de lecciones del proyecto anterior; ejecuta lo que el encargo y su entorno le dan. Si la lección no entra ahí, se pierde. Eso refuerza el paso 4: el lugar donde se pone el cambio es [delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md) y [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md).

También es inferencia de esta base que las fallas de un agente tienen además una ventaja para aprender: suelen dejar un registro completo de lo que hizo, paso a paso. El análisis puede partir de ese registro en vez de la memoria de la gente. Los modos de falla conocidos están en [fallas de agentes](../../IA/Agentes/fallas-de-agentes.md).
