---
resumen: >-
  Lo que pierde peso en desarrollo son las prácticas del proceso que este tema dejó fuera o puso en
  segundo plano (el documento de requisitos gigante y congelado, story points como productividad,
  Scrum con todas sus ceremonias, Gitflow, la cobertura como objetivo, la estimación en horas de cada
  tarea y la revisión línea por línea como único control), cada una con quién lo dice, la evidencia
  en contra y un veredicto.
estado: borrador
estabilidad: semi
fuentes:
  - https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
  - https://www.thoughtworks.com/radar/techniques/spec-driven-development
  - https://arxiv.org/abs/1609.04886
  - https://www.thoughtworks.com/radar/techniques/velocity-as-productivity
  - https://www.thoughtworks.com/en-us/radar/techniques/four-key-metrics
  - https://solar.cs.ucl.ac.uk/pdf/tawosi2022esem.pdf
  - https://iris.polito.it/retrieve/handle/11583/2722515/224876
  - https://unpaywall.org/10.1007%2F978-3-031-78386-9_21
  - "Vincent Driessen, A successful Git branching model (nota del 5 de marzo de 2020): https://nvie.com/posts/a-successful-git-branching-model/"
  - https://cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf
  - https://research.google/pubs/code-coverage-at-google/
  - https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code
  - https://www.simula.no/research/review-studies-expert-estimation-software-development-effort
  - https://web-backend.simula.no/sites/default/files/publications/Jorgensen.2007.2.pdf
  - https://microsoft.com/en-us/research/?p=164195
  - https://research.google/pubs/modern-code-review-a-case-study-at-google/
  - https://arxiv.org/abs/2211.03622
  - https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
  - https://ieeexplore.ieee.org/document/5232804
  - https://leanpub.com/read/leprechauns/leanpub-auto-chapter-7-whos-afraid-of-the-big-bad-waterfall
  - https://www.sei.cmu.edu/blog/programmer-moneyball-challenging-the-myth-of-individual-programmer-productivity
  - https://cacm.acm.org/blogcacm/in-search-of-the-shortest-possible-schedule
  - https://link.springer.com/content/pdf/10.1007/978-3-642-02032-2_24.pdf
aliases: [posición contraria en desarrollo, lo que ya no conviene aprender primero del proceso, prácticas en desuso]
creado: 2026-11-27
revisado:
---

# Lo que pierde peso en desarrollo

Lo que pierde peso en desarrollo son las prácticas del proceso que este tema dejó fuera o puso en segundo plano (el documento de requisitos gigante y congelado, story points como productividad, Scrum con todas sus ceremonias, Gitflow, la cobertura como objetivo, la estimación en horas de cada tarea y la revisión línea por línea como único control), cada una con quién lo dice, la evidencia en contra y un veredicto.

"Pierde peso" quiere decir que conviene aprenderlo después, no que esté muerto. El respaldo es desigual: story points como productividad y cobertura como objetivo tienen estudios o una entrada del Radar de Thoughtworks; Scrum ceremonial y estimación en horas son criterio de esta base, sin estudio que lo zanje. Lo que pierde peso en la estructura del sistema y en los sistemas con modelos está en [lo que pierde peso en Arquitectura](../../Arquitectura/Fundamentos/lo-que-pierde-peso.md) y no se repite.

## Resumen por ítem

| Ítem | Quién lo dice | Evidencia en contra | Veredicto |
|---|---|---|---|
| Documento de requisitos gigante y congelado | Böckeler; Menzies, indirecto | Ningún estudio compara; las normas siguen describiendo documentos | Pierde peso el documento único; gana la especificación por tramos. Criterio de la base |
| Story points y velocity como productividad | Radar (Hold, 2015); Tawosi et al. | Sirven como planificación interna | Pierde peso como medida de productividad |
| Scrum con todas sus ceremonias | Criterio de la base | Tampoco hay evidencia de que dañe | Sin evidencia en ninguna dirección |
| Gitflow | Driessen, 2020 | Sirve para software con varias versiones | Pierde peso con entrega continua |
| Cobertura como objetivo | Inozemtseva y Holmes, 2014 | Google la usa como señal en cada cambio | Pierde peso como objetivo, no como señal |
| Estimación en horas de cada tarea | Criterio de la base | Hay prácticas de estimación con evidencia a favor | Sin estudio que lo zanje |
| Revisión línea por línea como único control | Bacchelli y Bird; Sadowski et al. | La revisión cumple funciones que las pruebas no | Pierde peso como único control |

## El documento de requisitos gigante y congelado

Böckeler, después de probar herramientas de desarrollo guiado por especificaciones: "I'm very skeptical that lots of up-front spec design is a good idea", y "The past has shown that the best way for us to stay in control of what we're building are small, iterative steps". Menzies et al. analizaron 171 proyectos de 2006 a 2014 y no encontraron evidencia consistente de que arreglar un defecto más tarde cueste mucho más, según su resumen. Eso debilita la curva de costo del cambio que justificaba especificar todo antes, pero los datos son de un solo grupo de proyectos y no tratan el documento de requisitos.

En contra, no hay estudio que compare el documento grande con los requisitos iterativos, y las normas siguen describiéndolo. El desarrollo guiado por especificaciones vuelve a poner la especificación escrita antes del código, y el Radar lo tiene en Assess (noviembre de 2025). La tensión se resuelve así, como criterio de esta base: pierde peso el documento único, completo y congelado antes de empezar, y gana la [especificación](../Definicion/especificacion.md) por tramos chicos, escrita justo antes de construir cada parte.

## Story points y velocity como medida de productividad

El Radar puso "Velocity as productivity" en Hold en enero de 2015: la métrica se termina jugando en vez de entregar software andando. La misma página admite la velocity como estimación de capacidad interna del equipo, y el Radar tiene las cuatro métricas de DORA en Adopt como alternativa. Tawosi et al. (2022) encontraron que la estimación en story points "is often not consistent throughout the project", según su resumen. A favor de los puntos, Vetro et al. reportan que cambiar el proceso de estimación llevó la precisión de 10 % a 45 % en un proyecto, un estudio chico. Veredicto: pierde peso como medida de productividad y se mantiene como ayuda para planificar. No hay fuente sobre si los story points sirven cuando el código lo escribe un agente. Las alternativas están en [estimación](../Encargo/estimacion.md) y [métricas DORA](../../DevOps/Cultura-y-medicion/metricas-dora.md).

## Scrum con todas sus ceremonias

Según Rytkönen et al. (2024), hay "far less empirical evidence on agile benefits than the method's popularity would suggest" (según el resumen del buscador). Eso tampoco prueba que Scrum dañe: no hay entrada del Radar en su contra ni meta-análisis que aísle la daily, la retrospectiva o la planificación. Es criterio de esta base: el tema contrasta un proceso con eventos predefinidos contra la entrega continua medida con DORA, sin afirmar que uno esté probado mejor que otro. El marco está en [escuelas de desarrollo](escuelas-de-desarrollo.md).

## Gitflow

Driessen, que lo publicó en 2010, aclaró en 2020 que para equipos con entrega continua recomienda algo más simple y lo reserva para software con varias versiones soportadas a la vez. El detalle está en [Gitflow](../../DevOps/Ramas-y-versiones/gitflow.md) y la alternativa, en [trunk-based development](../../DevOps/Ramas-y-versiones/trunk-based-development.md).

## La cobertura de pruebas como objetivo

Inozemtseva y Holmes (ICSE 2014) observaron una correlación de baja a moderada entre cobertura y efectividad de la suite al controlar por la cantidad de pruebas, y concluyen que la cobertura sirve para encontrar código poco probado pero no como objetivo de calidad (según su resumen). En Google se calcula la cobertura en cada cambio, para mil millones de líneas por día (Ivanković et al., 2019): se la usa como señal. Un agente puede inflarla con pruebas triviales; no hay estudio sobre eso, y el Radar pide reforzar TDD y análisis estático frente a la complacencia con el código generado. La forma de medir si las pruebas detectan fallas está en [verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md).

## La estimación en horas de cada tarea

Jørgensen (2004) concluye que la estimación por juicio experto es la más usada y que no hay evidencia sustancial a favor de los modelos formales. En su revisión de 2007, citando a Moløkken-Østvold y Jørgensen, los proyectos gastan "roughly 30–40% more effort than estimated", y la exactitud no mejoró con los años (según el resumen del buscador). Eso muestra un desvío sistemático, no que haya que dejar de estimar, y la misma literatura trae prácticas con evidencia a favor, como combinar estimaciones de varios. Nada compara estimar tarea por tarea con estimar en grueso, y no hay datos sobre tareas que hace un agente. Es criterio de esta base; la alternativa por rangos y apetito está en [estimación](../Encargo/estimacion.md).

## La revisión línea por línea como único control

Bacchelli y Bird (Microsoft, 2013) encontraron que la revisión de código es "less about defects than expected" y rinde sobre todo conocimiento compartido y soluciones alternativas; Sadowski et al. (Google, 2018) la describen como herramienta educativa y de claridad (según sus resúmenes). Ya antes de los agentes no era un buen único control de defectos. En contra, Perry et al. (2023) vieron que quienes usaban un asistente escribían código menos seguro y creían lo contrario, y eso pide más control humano. Veredicto: la revisión sigue; pierde peso como único control frente a pruebas, análisis estático y verificación automática. El reparto está en [revisión de código](../Verificacion/revision-de-codigo.md).

## Que escribir código sea el cuello de botella

DORA 2025 dice que la aceleración "can expose weaknesses downstream" y que, sin "strong automated testing, mature version control practices, and fast feedback loops", más volumen de cambio trae inestabilidad. Pierde peso organizar el proceso alrededor de tipear más rápido; gana el trabajo de [Definición](../Definicion/definicion.md) y [Verificación](../Verificacion/verificacion.md). Son correlaciones de encuesta.

## Creencias que no hay que repetir

- "Royce propuso la cascada." Criticó la pasada única; el detalle está en [escuelas de desarrollo](escuelas-de-desarrollo.md#la-cascada-y-el-malentendido-de-royce).
- "El CHAOS report prueba que la mayoría de los proyectos fracasa." Eveleens y Verhoef (2010) mostraron que sus cifras agregadas mezclan estimaciones de procesos distintos y no coincidían con los casos que examinaron; los datos no son públicos (según su resumen).
- "El programador 10x está probado." Viene de Sackman et al. (1968), con 12 programadores; Bossavit critica que compara el mejor caso de uno con el peor de otro. McConnell sostiene que hay evidencia de 10:1 y el SEI ve evidencia en contra. Hay variabilidad grande; la cifra no está bien sostenida, y vuelve con la IA como "un desarrollador con un agente rinde 10x", sin fuente.
- "La ley de Brooks es una ley." Aplica a sumar gente a un proyecto ya atrasado; McConnell (1999) discute su alcance y Capiluppi y Adams (2009) la encuentran entre los desarrolladores centrales de KDE (según resúmenes). No hay estudio que compare sumar agentes con sumar personas.
