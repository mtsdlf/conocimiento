---
resumen: >-
  Gobierno y cierre es la parte de la gestión de proyectos que decide sobre el proyecto desde afuera: quién tiene autoridad y con qué tolerancias, cuántos proyectos corren a la vez y cuáles entran, cuándo se termina o se cancela, y qué se aprende para el próximo.
estado: vigente
estabilidad: estable
fuentes:
  - "PMI, The Standard for Project Management and A Guide to the PMBOK, 8.ª ed. (2025), folleto e índice: https://www.pmi.org/-/media/pmi/documents/public/pdf/publications/pmbok-guide-eighth-edition_table-of-contents.pdf"
  - "DIN/Beuth, índice de ISO 21502:2020 (solo el índice): https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:334145134/toc-3233385/download"
  - "PRINCE2, resumen de principios y tolerancias en Wikipedia (secundaria): https://en.wikipedia.org/wiki/PRINCE2"
  - "Singer, Shape Up (Basecamp), cap. 8: https://basecamp.com/shapeup/2.2-chapter-08"
  - "Anthropic, Building effective agents: https://www.anthropic.com/research/building-effective-agents"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
  - "Gestion-de-proyectos/.investigacion/fundamentos.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [gobernanza del proyecto, project governance, cierre del proyecto, project closure, dirección del proyecto]
creado: 2026-11-27
revisado: 2026-11-27
---

# Gobierno y cierre

Gobierno y cierre es la parte de la gestión de proyectos que decide sobre el proyecto desde afuera: quién tiene autoridad y con qué tolerancias, cuántos proyectos corren a la vez y cuáles entran, cuándo se termina o se cancela, y qué se aprende para el próximo.

Las demás verticales de la [gestión de proyectos](../gestion-de-proyectos.md) hacen y miden el trabajo. Esta decide sobre él. Recibe de [Incertidumbre y riesgo](../Incertidumbre-y-riesgo/incertidumbre-y-riesgo.md) lo que excede la tolerancia, y de [Seguimiento](../Seguimiento/seguimiento.md) el estado y el pronóstico. Devuelve una decisión sobre el [Encuadre](../Encuadre/encuadre.md): seguir como está, cambiar el resultado o el alcance, o parar.

## Autoridad delegada dentro de tolerancias

El mecanismo central del gobierno es delegar con límites. Quien gobierna fija cuánto se puede desviar el proyecto en plazo, costo, alcance u otra dimensión, y quien lo lleva decide solo mientras se mantenga adentro. Lo que sale de la tolerancia, o se prevé que va a salir, sube. PRINCE2 lo llama gestión por excepción y fija tolerancias en tiempo, costo, calidad, alcance, riesgo y beneficio, según el resumen de Wikipedia.

Hay una alternativa a escalar: cortar. En Shape Up, si el equipo no termina en el tiempo fijado, el proyecto no recibe prórroga por defecto, y Basecamp lo compara con un disyuntor ("circuit breaker"). Las dos formas resuelven distinto qué pasa cuando se agota el margen; la comparación está en [gobierno del proyecto](gobierno-del-proyecto.md). Cómo se fijan las tolerancias y cuándo algo sube a una persona está en [problemas y escalamiento](../Incertidumbre-y-riesgo/problemas-y-escalamiento.md), y la estructura de tramos con una decisión al final de cada uno, en [etapas y puntos de control](../Enfoque/etapas-y-puntos-de-control.md).

## Tres decisiones que toma el gobierno

El gobierno toma tres decisiones que el equipo no puede tomar por sí mismo:

| Decisión | Cuándo | Nota |
|---|---|---|
| Qué proyectos entran y cuántos van a la vez | Antes de empezar, y cada vez que algo termina o se cancela | [portafolio](portafolio.md) |
| Si el proyecto sigue, cambia o para | En cada punto de control y cuando algo excede la tolerancia | [gobierno del proyecto](gobierno-del-proyecto.md), [cerrar o cancelar](cerrar-o-cancelar.md) |
| Qué se cambia para el próximo | Al cerrar, y después de una falla grande | [aprender de un proyecto](aprender-de-un-proyecto.md) |

ISO 21502 separa en su índice la supervisión del proyecto (6.3), su dirección (6.4), el cierre o la terminación (6.8), las actividades posteriores (6.9) y las lecciones aprendidas (7.18). La 8.ª edición del PMBOK tiene la gobernanza como uno de sus siete dominios de desempeño.

## Cuánta formalidad rinde

> [!IMPORTANT]
> **La evidencia de que las prácticas formales mejoran los resultados es débil.** La investigación de PMI sobre el valor de la gestión de proyectos, según resúmenes, encontró que más madurez iba con más valor intangible pero no con más valor tangible. Un estudio de TI en Sudáfrica no halló efecto de la certificación sobre el desempeño, y otro sí lo halló, mediado por el profesionalismo. Sobre las oficinas de proyectos, una revisión de PMI dice que la literatura es "en gran parte anecdótica". Casi todas las fuentes son de PMI, que vende las certificaciones. El detalle está en [gobierno del proyecto](gobierno-del-proyecto.md).

La lectura de esta base es que el gobierno se justifica por las decisiones que permite tomar a tiempo. Los comités de seguimiento que solo reciben estado pierden peso frente a tableros que cualquiera puede leer ([lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md)).

## Qué cambia cuando ejecutan agentes

El gobierno de un agente usa el mismo mecanismo en escala chica. Anthropic describe agentes que "can then pause for human feedback at checkpoints or when encountering blockers", y recomienda condiciones de parada, "such as a maximum number of iterations", para mantener el control. Es el equivalente, según esta base, de un punto de control y de una tolerancia. Es una fuente de laboratorio, sin estudio comparativo, y no se encontraron tolerancias de dinero o de tiempo para agentes más allá del tope de iteraciones.

Lo que no cambia, según esta base, es quién responde. La responsabilidad por el resultado queda en una persona con nombre ([quién hace qué](../Personas-y-agentes/quien-hace-que.md)), y designarla no alcanza para que controle: la evidencia sobre supervisión humana de sistemas automáticos está en [niveles de autonomía](../Personas-y-agentes/niveles-de-autonomia.md).

## Qué hay adentro de gobierno y cierre

- [Gobierno del proyecto](gobierno-del-proyecto.md) — quién decide sobre el proyecto (patrocinador, quien aprueba, quien asegura), con qué tolerancias, y la disputa entre escalar y cortar; leerlo al armar un proyecto o cuando nadie sabe a quién le toca decidir.
- [Portafolio](portafolio.md) — cuántos proyectos corren a la vez, cuáles entran y por qué tener demasiados es el problema más repetido; leerlo cuando hay más trabajo que gente.
- [Cerrar o cancelar](cerrar-o-cancelar.md) — cómo se termina bien un proyecto y cómo se para a tiempo uno que no rinde, con la escalada del compromiso como trampa.
- [Aprender de un proyecto](aprender-de-un-proyecto.md) — retrospectivas y análisis de fallas que cambian algo, y por qué aprender de un proyecto al siguiente se descuida tan seguido.

El gobierno de una empresa (directorio, socios, el CEO que rinde cuentas) es otra cosa y está en [directorio y gobierno](../../Liderazgo-y-direccion/Rol-del-CEO/directorio-y-gobierno.md); cómo una organización baja la estrategia a compromisos con dueño está en [rendición de cuentas](../../Liderazgo-y-direccion/Ejecucion/rendicion-de-cuentas.md) y [OKR](../../Liderazgo-y-direccion/Ejecucion/okr.md).
