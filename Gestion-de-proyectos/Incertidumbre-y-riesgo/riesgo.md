---
resumen: >-
  Un riesgo es algo incierto que, si pasa, cambia el resultado del proyecto; gestionarlo es identificarlo, analizarlo, decidir qué hacer con él y revisarlo mientras dura el trabajo, sin confiar en que una matriz de colores lo haya medido.
estado: borrador
estabilidad: semi
fuentes:
  - "ISO 31000:2018, noticia de publicación (según resumen; la página del estándar no se pudo leer): https://www.iso.org/news/ref2263.html"
  - "Cox (2008), What's wrong with risk matrices?, Risk Analysis 28(2):497-512 (según el abstract): https://econpapers.repec.org/RePEc:wly:riskan:v:28:y:2008:i:2:p:497-512"
  - "Estudio sobre gestión de riesgos y éxito en proyectos de TI, Journal of Project Management (2024) (según resumen del buscador): https://doaj.org/article/31ecb8864b4a49bfb3de03aca3648687"
  - "Cemri et al. (2025), Why Do Multi-Agent LLM Systems Fail?, arXiv 2503.13657 (según resumen): https://arxiv.org/abs/2503.13657"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
aliases: [gestión de riesgos, risk, risk management, registro de riesgos, risk register, matriz de riesgos, risk matrix, ISO 31000]
creado: 2026-11-27
revisado:
---

# Riesgo

Un riesgo es algo incierto que, si pasa, cambia el resultado del proyecto; gestionarlo es identificarlo, analizarlo, decidir qué hacer con él y revisarlo mientras dura el trabajo, sin confiar en que una matriz de colores lo haya medido.

Es una de las cuatro formas de lo incierto que trata [Incertidumbre y riesgo](incertidumbre-y-riesgo.md). Se distingue de un [supuesto](supuestos.md), que el plan da por cierto sin decirlo, y de un [problema](problemas-y-escalamiento.md), que ya ocurrió. Lo que no se puede evitar se cubre con [margen](margenes.md).

## El proceso de ISO 31000

La norma de referencia es ISO 31000:2018, de la que esta base leyó solo resúmenes. Según la noticia de su publicación, en febrero de 2018, da principios, un marco y un proceso; es una guía y no un conjunto de requisitos, y no es certificable. Esa revisión puso más foco en crear y proteger valor y en la naturaleza iterativa del proceso. Según resúmenes del buscador, el proceso es identificar, analizar, evaluar, tratar, monitorear y comunicar, e ISO confirmó la norma en 2023.

En un proyecto, el proceso se vuelve un ciclo corto. Al lanzar un servicio se listan los riesgos al encuadrar, se decide qué hacer con los que importan y se vuelve a mirar la lista en cada punto de control ([etapas y puntos de control](../Enfoque/etapas-y-puntos-de-control.md)). Las respuestas habituales en los marcos, que esta base no cotejó con su texto, son evitar el riesgo cambiando el plan, reducir su probabilidad o su efecto, pasárselo a otro o aceptarlo con un margen. Quién responde por cada riesgo se fija como cualquier otra responsabilidad, en [quién hace qué](../Personas-y-agentes/quien-hace-que.md).

## Lo que la matriz de riesgos no mide

La herramienta más usada para analizar riesgos es la matriz de probabilidad por impacto, con casilleros de colores. Cox (2008) la critica, según el abstract de su artículo: hay poca investigación que muestre que las matrices mejoren las decisiones, y tienen cuatro límites.

1. **Resolución pobre**: comparan de forma confiable solo una fracción chica de los pares de riesgos.
2. **Errores**: pueden darle una calificación más alta a un riesgo cuantitativamente menor y, cuando frecuencia y severidad van en sentidos opuestos, decidir peor que al azar.
3. **Asignación subóptima**: llevan a repartir mal los recursos para tratar los riesgos.
4. **Entradas y salidas ambiguas**: los datos de entrada y los resultados son ambiguos.

Cox concluye que se usen con cuidado y explicando los juicios que esconden. La crítica ataca las escalas ordinales, no la idea de gestionar riesgos. Una razón más, que es lectura de esta base y no de Cox: la matriz trata cada riesgo como un punto, y los desvíos de los proyectos tienen [cola gruesa](por-que-fallan-los-proyectos.md). Un riesgo de probabilidad "baja" y efecto "alto" puede ser el que se come el proyecto.

## Si gestionar riesgos mejora los resultados

No quedó establecido en lo que esta base leyó. Según un resumen del buscador, un estudio de 2024 en proyectos de TI encontró que algunos componentes de la gestión de riesgos se asocian con el éxito, pero que la gestión de riesgos como un todo no influye en él.

> [!NOTE] Sin fuente todavía: evidencia leída de que gestionar riesgos mejore el resultado de los proyectos. Hay un metaanálisis de 2010 sobre proyectos de TI (Bakker, Boonstra y Wortmann) que esta base no pudo leer; hasta leerlo no se afirma en ningún sentido.

## El riesgo del falso terminado

Cuando ejecutan agentes aparece un riesgo: que el agente dé por terminada una tarea que no terminó. Cemri et al. clasificaron 14 modos de falla de sistemas multiagente en 3 categorías, según un resumen; una es la verificación de tareas, con modos como "Premature Termination", "No or Incomplete Verification" e "Incorrect Verification". La taxonomía y cómo se evalúa un agente están en [fallas de agentes](../../IA/Agentes/fallas-de-agentes.md).

Ese riesgo se trata, según la lectura de esta base, con dos respuestas que se fijan antes de delegar. El criterio de aceptación se escribe antes de que el agente empiece, y la verificación la hace alguien o algo distinto del agente que ejecutó. Cuánto pasa el falso terminado y cómo se acepta con evidencia está en [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md). Para el código de un agente, el detalle está en [verificar lo que hizo un agente](../../Desarrollo/Verificacion/verificar-lo-que-hizo-un-agente.md).

El otro riesgo de trabajar con agentes es de las personas: confiar de más en lo que la automatización entrega. Está en [niveles de autonomía](../Personas-y-agentes/niveles-de-autonomia.md).

Los recursos canónicos son ISO 31000:2018, para el vocabulario del proceso, y Cox (2008), para saber qué no hacer con las matrices.
