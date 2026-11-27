---
resumen: >-
  Incertidumbre y riesgo es la parte de la gestión que trata lo que puede salir distinto del plan: los riesgos que se ven venir, los supuestos que se dieron por ciertos, los márgenes para absorber desvíos y los problemas que ya ocurrieron y hay que escalar, sabiendo que los proyectos se desvían de forma sistemática y con cola gruesa.
estado: vigente
estabilidad: estable
fuentes:
  - "Flyvbjerg (2014), What You Should Know About Megaprojects and Why, Project Management Journal 45(2): https://arxiv.org/pdf/1409.0003"
  - "Flyvbjerg, Budzier, Lee, Keil, Lunn y Bester (2022), The Empirical Reality of IT Project Cost Overruns, J. Management Information Systems 39(3): https://arxiv.org/abs/2210.01573"
  - "ISO 31000:2018, noticia de publicación (según resumen): https://www.iso.org/news/ref2263.html"
  - "PRINCE2, gestión por excepción (según resúmenes): https://prince2.wiki/Manage_by_exception"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [gestión de riesgos, risk management, incertidumbre, uncertainty, gestión de la incertidumbre]
creado: 2026-11-27
revisado: 2026-11-27
---

# Incertidumbre y riesgo

Incertidumbre y riesgo es la parte de la gestión que trata lo que puede salir distinto del plan: los riesgos que se ven venir, los supuestos que se dieron por ciertos, los márgenes para absorber desvíos y los problemas que ya ocurrieron y hay que escalar, sabiendo que los proyectos se desvían de forma sistemática y con cola gruesa.

La vertical recibe de [Seguimiento](../Seguimiento/seguimiento.md) los desvíos que aparecen y de [Planificación](../Planificacion/planificacion.md) el pronóstico contra el que se miden. Lo que excede la tolerancia lo sube a [Gobierno y cierre](../Gobierno-y-cierre/gobierno-y-cierre.md), donde alguien decide seguir, cambiar o parar. Cuánta incertidumbre tiene el trabajo también decide el [enfoque](../Enfoque/elegir-un-enfoque.md): con mucha, la lectura habitual es que conviene tramos cortos que la achiquen antes de comprometer más, aunque la evidencia que hay no confirma que el enfoque ágil rinda más con más complejidad (ver [elegir un enfoque](../Enfoque/elegir-un-enfoque.md)).

## Cuatro formas de lo incierto

Lo que puede salir distinto toma cuatro formas, y cada una se trata de otra manera.

| Forma | Qué es | Ejemplo al mudar una plataforma | Se trata |
|---|---|---|---|
| [Riesgo](riesgo.md) | Algo que puede pasar y cambiaría el resultado | Que el proveedor nuevo no soporte el volumen de datos | Se identifica, se responde y se revisa |
| [Supuesto](supuestos.md) | Algo que el plan da por cierto sin haberlo comprobado | Que los usuarios no dependen de la función que se apaga | Se escribe y se prueba temprano |
| [Margen](margenes.md) | Tiempo o plata reservados para absorber lo que salga distinto | Dos semanas al final antes de la fecha comprometida | Se dimensiona y se le asigna dueño |
| [Problema](problemas-y-escalamiento.md) | Algo que ya pasó, o que el pronóstico dice que va a pasar | La migración de datos ya lleva el doble de lo previsto | Se resuelve o se escala según la tolerancia |

Las cuatro se conectan. Un supuesto que resulta falso se vuelve un problema. Un riesgo que no se puede evitar se cubre con margen. Un problema que se come el margen y sale de la tolerancia se escala.

## Por qué el promedio engaña

El desvío de los proyectos no se reparte de forma pareja alrededor del plan. Flyvbjerg sostiene, con datos de miles de proyectos, que se desvían una y otra vez hacia más costo y más plazo, y que la distribución tiene cola gruesa: unos pocos se desvían muchísimo. Las cifras, la población de cada estudio y la disputa sobre la causa están en [por qué fallan los proyectos](por-que-fallan-los-proyectos.md).

Con cola gruesa, planificar con el desvío promedio deja afuera justo los casos que hunden un proyecto. De ahí salen tres prácticas de la vertical. Se pronostica con rangos y percentiles ([pronóstico](../Planificacion/pronostico.md)). El margen se dimensiona mirando la cola. Y se escala cuando el pronóstico dice que se va a salir de la tolerancia, no cuando ya se salió.

## Qué cambia cuando ejecutan agentes

Aparece un riesgo nuevo: el agente que da por terminada una tarea que no terminó. Una taxonomía de fallas de sistemas multiagente (Cemri et al.) pone la verificación de tareas como una de sus tres categorías, como se ve en [riesgo](riesgo.md); cuánto pasa y cómo se acepta con evidencia está en [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md).

Las tolerancias pasan a definir la autonomía. Un agente puede decidir solo mientras el gasto, el plazo y la confianza en la verificación queden dentro de lo acordado, y lo que sale de ahí sube a una persona. Es una aplicación de la gestión por excepción que hace esta base, sin estudio que la evalúe: está en [problemas y escalamiento](problemas-y-escalamiento.md) y en [niveles de autonomía](../Personas-y-agentes/niveles-de-autonomia.md).

Casi todo lo que la vertical dice sobre agentes es inferencia de esta base. No hay estudios de por qué fallan los proyectos ejecutados en parte por agentes, ni de cómo se dimensionan sus márgenes.

## Qué hay adentro

- [Riesgo](riesgo.md) — identificar, responder y revisar lo que puede pasar; por qué las matrices de probabilidad e impacto engañan; el riesgo del falso terminado.
- [Supuestos](supuestos.md) — lo que el plan dio por cierto, cómo se hace visible con un premortem y cómo se prueba temprano.
- [Márgenes](margenes.md) — reservas de tiempo y plata, la ley de Parkinson, dónde va el margen y de quién es.
- [Problemas y escalamiento](problemas-y-escalamiento.md) — tolerancias, informe de excepción y cuándo un desvío sube a una persona.
- [Por qué fallan los proyectos](por-que-fallan-los-proyectos.md) — la ley de hierro de Flyvbjerg, la cola gruesa y la disputa sobre la causa.
