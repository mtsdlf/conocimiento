---
resumen: >-
  El control de cambios es cómo se decide qué hacer cuando cambia lo pedido a mitad de camino: quién aprueba el cambio, qué desplaza y qué se mueve de la línea base. Los estándares la prescriben (PMBOK y PRINCE2, según lo que se pudo ver) y no se encontró evidencia con método que la respalde.
estado: vigente
estabilidad: semi
fuentes:
  - "PMI, Pulse of the Profession 2018, sobre scope creep (según un resumen; encuesta autodeclarada): https://www.pmi.org/learning/library/2019/04/07/16/06/scope-creep-rising-11308"
  - "The Impact of Scope Creep on Project Success: An Empirical Investigation, IEEE Access (2020), doi 10.1109/ACCESS.2020.3007098 (abstract): https://doaj.org/article/62c59e683e0c4d9e89f04776c192895e"
  - "Encuesta sobre volatilidad de requisitos, UTS (2004) (según un resumen): https://opus.lib.uts.edu.au/bitstream/10453/2350/3/2004003534.pdf"
  - "PMI, Top five causes of scope creep (según un resumen; practicante): https://www.pmi.org/learning/library/top-five-causes-scope-creep-6675"
  - "PMI, PMBOK 7 y 8, control integrado de cambios (no leído; de pago): https://www.pmi.org/standards/pmbok"
  - "Gestion-de-proyectos/.investigacion/seguimiento.md"
aliases: [gestión de cambios del proyecto, control integrado de cambios, integrated change control, change control, scope creep, deriva del alcance, corrimiento del alcance, junta de cambios, change control board]
creado: 2026-11-27
revisado: 2026-11-27
---

# Control de cambios

El control de cambios es cómo se decide qué hacer cuando cambia lo pedido a mitad de camino: quién aprueba el cambio, qué desplaza y qué se mueve de la línea base. Los estándares la prescriben (PMBOK y PRINCE2, según lo que se pudo ver) y no se encontró evidencia con método que la respalde.

Un cambio toca lo que [Encuadre](../Encuadre/encuadre.md) dejó fijo: el [alcance](../Encuadre/alcance.md) y su línea base, a veces el [resultado](../Encuadre/resultado-y-terminado.md) mismo. El control de cambios no es el mismo asunto que la gestión del cambio en una organización (que la gente adopte una forma nueva de trabajar), que está en [gestión del cambio](../../Liderazgo-y-direccion/Ejecucion/gestion-del-cambio.md).

## Cambio aprobado y deriva del alcance

Conviene separar dos cosas que se mezclan. Un cambio aprobado es una decisión: alguien con autoridad acepta que el alcance cambie y se ajustan plazo, costo o lo que sale a cambio. La deriva del alcance (*scope creep*) es el cambio que entra sin decisión: un pedido chico por acá, una mejora "ya que estamos" por allá, hasta que el trabajo es otro y el plan sigue diciendo lo mismo.

El control de cambios existe para que lo segundo se vuelva lo primero.

## Dos formas de tratar un cambio

| | Con línea base fija | Con alcance que se reprioriza |
|---|---|---|
| Cuándo | [enfoque predictivo](../Enfoque/enfoque-predictivo.md), contratos de alcance cerrado | [enfoque iterativo](../Enfoque/enfoque-iterativo.md), [flujo continuo](../Enfoque/flujo-continuo.md) |
| Qué es un cambio | todo lo que mueve la línea base | casi nada: lo nuevo entra a la lista y compite |
| Quién decide | una autoridad de cambios fijada en el [gobierno del proyecto](../Gobierno-y-cierre/gobierno-del-proyecto.md) | quien prioriza, dentro de las tolerancias |
| Qué se ajusta | plazo, costo o las dos cosas | qué sale o qué se posterga |

El cuadro es armado por la base. Que la primera columna sea la del control integrado de cambios del PMBOK y la autoridad de cambios de PRINCE2 no se verificó: ninguno de los dos textos se leyó. La segunda es la postura de la escuela adaptativa: el cambio se espera y se gestiona repriorizando. Una [apuesta con tiempo fijo](../Enfoque/apuesta-con-tiempo-fijo.md) es el caso extremo: el plazo no se mueve y lo que no entra se recorta.

Criterio de la base: en los dos casos, el cambio que excede lo que quien lleva el proyecto puede decidir sube según las tolerancias, como dice [problemas y escalamiento](../Incertidumbre-y-riesgo/problemas-y-escalamiento.md). Un cambio fácil de deshacer pide menos ceremonia que uno que no se puede revertir; esa distinción está en [decisiones reversibles](../../Liderazgo-y-direccion/Decidir/decisiones-reversibles.md).

## Lo que se sabe del scope creep, con pocos datos

Lo que se encontró sobre scope creep son sobre todo encuestas. Según el Pulse de PMI (una encuesta a practicantes) of the Profession 2018, el 52 % de los proyectos terminados en los últimos 12 meses sufrió scope creep o cambios de alcance no controlados, contra 43 % cinco años antes. Es una encuesta autodeclarada, no una medición.

Un estudio publicado en IEEE Access en 2020 halla, según su abstract, que los factores de scope creep se asocian negativamente con el éxito de proyectos de software; no se vio la muestra. Una encuesta sobre volatilidad de requisitos afirma que no existe evidencia empírica integral sobre qué la causa (según un resumen).

> [!NOTE] Sin fuente todavía: una revisión sistemática sobre control de cambios; estudios con diseño sólido sobre causas y efectos del scope creep; evidencia de que una junta de cambios o una línea base mejore los resultados; evidencia de que repriorizar, como propone la escuela adaptativa, funcione mejor. Las dos formas de la tabla son prescripciones que ningún estudio comparó.

## Cuándo un cambio del agente es un cambio del proyecto

Con agentes aparece, por inferencia de la base, una clase de cambio que las fuentes leídas no tratan: cambia el que ejecuta y no lo pedido. Una versión nueva del modelo, otra herramienta o una instrucción reescrita pueden alterar lo que sale sin que nadie haya tocado el alcance.

> [!NOTE] Sin fuente todavía: si un cambio de especificación, de modelo o de herramientas cuenta como cambio de línea base.

Como inferencia de esta base: un cambio en cómo se ejecuta no mueve el alcance, pero sí invalida aceptaciones anteriores si el agente vuelve a tocar piezas ya hechas. Lo práctico es registrarlo como cambio, aunque lo apruebe quien lleva el proyecto sin subirlo, y volver a [aceptar con evidencia](aceptar-con-evidencia.md) lo que el cambio afecte. Que un agente amplíe por su cuenta lo que hace, más allá de la tarea, es deriva del alcance con otro autor; los límites de lo que puede hacer se fijan al [delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md).

En un encargo de software, la regla con el cliente (cotizar, cambiar por algo del mismo tamaño o recortar) está en [cambios de alcance](../../Desarrollo/Encargo/cambios-de-alcance.md). La entrada de la vertical es [Seguimiento](seguimiento.md).
