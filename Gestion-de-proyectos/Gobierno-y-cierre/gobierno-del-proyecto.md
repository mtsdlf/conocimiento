---
resumen: >-
  El gobierno del proyecto es quién tiene autoridad sobre un proyecto y cómo la delega: quién lo patrocina, quién aprueba seguir en cada punto de control, dentro de qué tolerancias decide solo quien lo lleva y qué pasa cuando se excede el margen.
estado: borrador
estabilidad: semi
fuentes:
  - "DIN/Beuth, índice de ISO 21502:2020 (solo el índice): https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:334145134/toc-3233385/download"
  - "PMI, The Standard for Project Management and A Guide to the PMBOK, 8.ª ed. (2025), folleto e índice: https://www.pmi.org/-/media/pmi/documents/public/pdf/publications/pmbok-guide-eighth-edition_table-of-contents.pdf"
  - "PRINCE2, gestión por excepción y tolerancias, resumen en Wikipedia (secundaria; el manual no se leyó): https://en.wikipedia.org/wiki/PRINCE2"
  - "Singer, Shape Up (Basecamp), cap. 8: https://basecamp.com/shapeup/2.2-chapter-08"
  - "Anthropic, Building effective agents: https://www.anthropic.com/research/building-effective-agents"
  - "Thomas y Mullaly (2008), Researching the Value of Project Management, PMI (según resúmenes): https://www.pmi.org/shop/p-/book/researching-the-value-of-project-management/00101065301"
  - "Joseph y Marnewick (2018), Investing in project management certification, Information Technology and Management 19(1) 51-74 (abstract): https://ideas.repec.org/a/spr/infotm/v19y2018i1d10.1007_s10799-017-0275-y.html"
  - "Aslam y Bilal (2021), certificación y desempeño (según un resumen; sin URL verificada)"
  - "Hobbs y Aubry, tipos y funciones de las PMO, PMI (según resúmenes): https://www.pmi.org/learning/library/project-management-offices-types-functions-2376"
  - "Estudio de dos años sobre PMO en 200 grandes organizaciones, biblioteca de PMI (según resúmenes): https://www.pmi.org/learning/library/project-management-office-strategic-goals-4122"
  - "PMI, revisión sobre el papel de la PMO en el éxito (según resúmenes): https://www.pmi.org/learning/library/role-pmo-achieving-project-success-1002"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
  - "Gestion-de-proyectos/.investigacion/fundamentos.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [gobernanza del proyecto, project governance, patrocinador, sponsor, junta del proyecto, project board, gestión por excepción, manage by exception, tolerancias, PMO, oficina de proyectos]
creado: 2026-11-27
revisado:
---

# Gobierno del proyecto

El gobierno del proyecto es quién tiene autoridad sobre un proyecto y cómo la delega: quién lo patrocina, quién aprueba seguir en cada punto de control, dentro de qué tolerancias decide solo quien lo lleva y qué pasa cuando se excede el margen.

Es la pieza de [gobierno y cierre](gobierno-y-cierre.md) que dice quién decide. Las otras dicen sobre qué: cuántos proyectos entran ([portafolio](portafolio.md)), si este sigue ([cerrar o cancelar](cerrar-o-cancelar.md)) y qué se cambia después ([aprender de un proyecto](aprender-de-un-proyecto.md)).

## Los roles que reparten la autoridad

Un proyecto necesita, como mínimo, alguien que lo pida y responda por su justificación, alguien que lo lleve día a día y alguien que pueda decir que no a los dos. ISO 21502 lista en su índice los roles de la organización del proyecto: la organización patrocinante, la junta del proyecto ("project board"), el patrocinador ("sponsor"), el aseguramiento ("assurance"), el gerente, la oficina de proyectos, quien lidera cada paquete de trabajo, el equipo y los interesados. Lo que sigue es síntesis de esta base: el índice de ISO 21502 solo lista los nombres de los roles, no lo que decide cada uno. No hace falta una persona por rol: en un proyecto chico, el patrocinador y la junta pueden ser la misma persona.

| Rol | Qué decide | Ejemplo en el lanzamiento de un servicio |
|---|---|---|
| Patrocinador | Si el proyecto vale la pena y si sigue en cada punto de control; responde por la [justificación](../Encuadre/justificacion.md) | La dirección del área que va a usar el servicio |
| Quien lleva el proyecto | Todo lo que cabe dentro de las tolerancias | La persona a cargo del lanzamiento |
| Aseguramiento | Nada: mira por separado si lo que se informa es cierto | Alguien de otra área que revisa la evidencia |
| Interesados con poder de veto | Lo suyo: aprobar, financiar, regular | Legal, quien opera los sistemas |

El aseguramiento sería, según esta base y sin fuente, el rol que más se omite y el que más falta hace cuando el estado se informa con optimismo. Por qué los reportes salen sesgados hacia arriba está en [informar el estado](../Seguimiento/informar-el-estado.md).

Quién decide qué en una organización en general, con quién opina antes y quién veta, está en [derechos de decisión](../../Liderazgo-y-direccion/Decidir/derechos-de-decision.md), y qué decisiones conviene tomar rápido porque se pueden deshacer, en [decisiones reversibles](../../Liderazgo-y-direccion/Decidir/decisiones-reversibles.md).

## Decidir por excepción

La gestión por excepción separa lo que se decide abajo de lo que sube. Quien gobierna fija tolerancias, y quien lleva el proyecto decide solo mientras el proyecto se mantenga adentro. Según el resumen de PRINCE2 en Wikipedia, las tolerancias se fijan en tiempo, costo, calidad, alcance, riesgo y beneficio, y si se superan o se prevé que se van a superar, se sube un informe de excepción. La fuente no se cotejó con el manual.

Un ejemplo: la tolerancia de una mudanza de plataforma es de dos semanas de plazo y 10 % de costo. Si a mitad de camino el pronóstico dice tres semanas de atraso, quien lleva el proyecto no decide solo si recorta alcance o pide más plazo: lo sube con opciones. Cómo se fijan las tolerancias, cómo se escala y qué lleva un informe de excepción está en [problemas y escalamiento](../Incertidumbre-y-riesgo/problemas-y-escalamiento.md). Los tramos con una decisión al final, que son donde el patrocinador decide aunque no haya excepción, están en [etapas y puntos de control](../Enfoque/etapas-y-puntos-de-control.md).

## Escalar o cortar cuando se agota el margen

> [!IMPORTANT]
> **Dos modelos de control resuelven distinto el margen agotado.** En PRINCE2, salir de la tolerancia, o prever que se va a salir, dispara una escalada: un informe de excepción sube a quien gobierna, que decide. En Shape Up, el tiempo fijado es un tope: "If they don't finish, by default the project doesn't get an extension", y Basecamp lo piensa "like a `circuit breaker` that ensures one project doesn't overload the system". Basecamp da el motivo del disyuntor; el de la escalada de PRINCE2 no lo da ninguna fuente leída: que proteja proyectos que valen aunque cuesten más es inferencia de esta base. Ninguna de las dos tiene un estudio comparativo; Shape Up es una fuente de practicante, y lo de PRINCE2 sale de un resumen.

La lectura de esta base es que el disyuntor sirve cuando el valor del trabajo se puede expresar en tiempo (cuánto vale esto, como máximo) y la escalada, cuando hay un compromiso externo que no se puede dejar a medias, como una obra o una migración con fecha de apagado. Cortar sin prórroga tiene su propia nota en [apuesta con tiempo fijo](../Enfoque/apuesta-con-tiempo-fijo.md).

## Lo que se sabe de juntas, oficinas y certificaciones

> [!NOTE]
> Sin fuente todavía: no se encontró evidencia con método sobre el efecto de las juntas de proyecto, los patrocinadores o las puertas de decisión en los resultados; solo descripciones de marcos y de practicantes.

> [!IMPORTANT]
> **Las prácticas formales tienen evidencia débil y mixta.** A favor: Aslam y Bilal (2021), según un resumen, hallan un vínculo entre certificación y desempeño mediado por el profesionalismo. En contra o neutro:
> - Thomas y Mullaly (2008) estudiaron el valor de la gestión de proyectos para PMI entre mayo de 2005 y junio de 2008. Un trabajo posterior de los mismos autores (2010) reportó, según el buscador, que más madurez iba con más valor intangible pero no con valor tangible.
> - Joseph y Marnewick (2018), según su abstract: el desempeño de proyectos de TI sudafricanos "no está influido" por la certificación en gestión de proyectos. Es un solo contexto.
> - Hobbs y Aubry encuestaron 500 oficinas de proyectos y documentaron una gran variedad de formas que cambian seguido; la ficha no dice que prueben un efecto sobre el éxito, y el texto no se leyó.
> - Un estudio de dos años con 200 grandes organizaciones halló, según un resumen, que las que más usaban oficinas de proyectos tenían costos de TI más altos y no entregaban proyectos de mayor retorno.
> - Una revisión de PMI dice que la literatura sobre el efecto de la oficina de proyectos en el éxito "es en gran parte anecdótica".
>
> Casi todas estas fuentes son de PMI o de revistas cercanas, que vende las certificaciones. Que publique resultados poco favorables les da peso, pero ninguna es independiente.

Con esa evidencia, la base trata la formalidad como un costo que se justifica caso por caso. Un gobierno liviano (un patrocinador con nombre, tolerancias escritas, puntos de control con fecha) se puede sostener por su lógica; una oficina de proyectos o un comité, solo por las decisiones que destraban. Las reuniones de comité que solo reciben estado pierden peso ([lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md)).

## Qué cambia cuando ejecutan agentes

Con agentes, según una lectura de esta base, el mismo mecanismo baja un nivel: la persona que lleva el proyecto le da a cada agente una autoridad acotada, y el agente sube lo que excede. Anthropic describe agentes que "can then pause for human feedback at checkpoints or when encountering blockers", y dice que "it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control". Es el análogo de un punto de control y de una tolerancia. Es una fuente de laboratorio, sin estudio comparativo.

> [!NOTE]
> Sin fuente todavía: no se encontraron tolerancias de dinero o de tiempo para agentes más allá del tope de iteraciones.

Cuánto decide un agente solo, y por qué poner a una persona a aprobar no garantiza que controle, está en [niveles de autonomía](../Personas-y-agentes/niveles-de-autonomia.md). Que la responsabilidad por el resultado quede en una persona con nombre, aunque ejecute un agente, está en [quién hace qué](../Personas-y-agentes/quien-hace-que.md); la práctica de un responsable con nombre por compromiso, a nivel de organización, en [rendición de cuentas](../../Liderazgo-y-direccion/Ejecucion/rendicion-de-cuentas.md).
