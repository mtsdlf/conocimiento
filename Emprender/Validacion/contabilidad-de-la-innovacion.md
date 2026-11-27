---
resumen: >-
  La contabilidad de la innovación es la forma de medir el avance de una empresa nueva que propone Ries: fijar una línea de base con un MVP, afinar el producto para mover esa línea hacia el ideal y decidir con el resultado si pivotar o perseverar, usando métricas accionables y no de vanidad.
estado: vigente
estabilidad: semi
fuentes:
  - "Eric Ries, The Lean Startup (2011), capítulos Measure y Experiment según resúmenes; en castellano, El método Lean Startup (Deusto)"
  - "theleanstartup.com, Principles: https://theleanstartup.com/principles"
  - "Resumen del libro de un lector: https://publish.obsidian.md/dk/Reading/Books/The+Lean+Startup"
  - "Eric Ries, prólogo a Lean Analytics (Croll y Yoskovitz), según un resumen: https://www.oreilly.com/library/view/lean-analytics/9781449335687/pr03.html"
  - "Koning, Hasan y Chatterji (2022), Experimentation and Start-up Performance: Evidence from A/B Testing, Management Science 68(9):6434-6453, DOI 10.1287/mnsc.2021.4209: https://www.nber.org/papers/w26278"
  - "Emprender/.investigacion/validacion.md"
  - "Emprender/.investigacion/posicion-contraria.md"
aliases: [innovation accounting, métricas accionables, actionable metrics, métricas de vanidad, vanity metrics, línea de base, afinar el motor]
creado: 2026-11-22
revisado: 2026-11-22
---

# Contabilidad de la innovación

La contabilidad de la innovación es la forma de medir el avance de una empresa nueva que propone Ries: fijar una línea de base con un MVP, afinar el producto para mover esa línea hacia el ideal y decidir con el resultado si pivotar o perseverar, usando métricas accionables y no de vanidad.

La página de principios del Lean Startup la presenta como «a new kind of accounting, specific to startups», para medir el progreso, fijar hitos y priorizar el trabajo. En su prólogo a *Lean Analytics*, según un resumen, Ries advierte que las métricas contables tradicionales aplicadas a la incertidumbre de la innovación son «surprisingly dangerous». Lo que mide es el [aprendizaje validado](construir-medir-aprender.md), es decir, la fase «medir» del ciclo.

## Los tres pasos: línea de base, afinar el motor, decidir

Según un resumen del libro, la contabilidad de la innovación tiene tres pasos:

1. **Fijar la línea de base.** Se usa un [producto mínimo viable](producto-minimo-viable.md) para obtener datos reales de dónde está la empresa hoy: cuántos se registran, cuántos vuelven, cuántos pagan.
2. **Afinar el motor.** Se hacen cambios al producto para mover la línea de base hacia el ideal del plan. Cada cambio es un experimento que tiene que mover una métrica concreta.
3. **Pivotar o perseverar.** Si los cambios no mueven las métricas que importan, el modelo está mal. Según el resumen: «If we are not moving the drivers of our business model, we are not making progress». La decisión está en [pivotar o perseverar](pivotar-o-perseverar.md).

En la lectura de la base, el ideal contra el que se compara la línea de base sale del [modelo de negocio](../Modelo-de-negocio/modelo-de-negocio.md): las tasas de conversión, retención y costo de adquisición que harían viable a la empresa. Si cada cliente deja más de lo que cuesta conseguirlo se mide con la [economía unitaria](../../Marketing/Medicion/economia-unitaria.md).

## Métricas accionables y métricas de vanidad

El libro, según el mismo resumen, pide que una métrica cumpla tres condiciones, las «tres A». La cita de la primera es del resumen; lo demás de la tabla es descripción de la base:

| Condición | Qué pide | Qué la viola |
|---|---|---|
| Accionable | «must demonstrate clear cause and effect»: que se sepa qué acción movió el número | Un total acumulado que sube aunque no se haga nada |
| Accesible | Que la entienda quien tiene que decidir con ella | Un tablero que solo lee quien lo armó |
| Auditable | Que los datos sean creíbles y se puedan verificar contra la fuente | Un número que nadie puede reconstruir |

Las métricas de vanidad son las que no cumplen la primera condición. En el mismo prólogo a *Lean Analytics*, según un resumen, Ries las describe como números que hacen sentir bien pero engañan, como los clientes totales o el tráfico bruto, y les opone la métrica accionable. Que crezcan solas con el tiempo o con el gasto en publicidad, sin decir si un cambio funcionó, es descripción de la base.

> [!NOTE]
> Sin fuente todavía: la definición literal de Ries de «vanity metrics» y el ejemplo de cohortes de IMVU que, según resúmenes, trae el capítulo Measure.

## La medida por cohortes

Según el resumen del libro, en lugar de mirar totales se mira por separado cada grupo de clientes, la cohorte. La lectura de la base: si los cambios funcionan, cada cohorte nueva se comporta mejor que la anterior, y en un total esa mejora queda tapada por los clientes viejos. Cómo se arma y se lee una cohorte es técnica del tema Datos y está en [análisis de cohortes](../../Datos/Analitica-de-producto/Cohortes/analisis-de-cohortes.md).

Qué métrica seguir en cada momento lo propone Lean Analytics con [una métrica que importa por etapa](../../Marketing/Medicion/metrica-que-importa.md): según esa nota, un emprendimiento recién arrancando está en la etapa de empatía (si hay un problema real y gente que paga) o en la de ingresos. La contabilidad de la innovación da el método; esa nota, qué mirar.

## La evidencia sobre experimentar

Koning, Hasan y Chatterji (2022) estudiaron startups tecnológicas que adoptaron herramientas de A/B testing (mostrar dos versiones a usuarios elegidos al azar y comparar qué hacen). Según su abstract, «although relatively few firms adopt A/B testing, among those that do, performance improves by 30%–100% after a year of use». El abstract agrega que las startups no prueban solo cambios puntuales: usan el A/B testing «as part of a broader strategy of experimentation». Eso se parece a lo que pide el paso de afinar el motor (lectura de la base).

El estudio es observacional (la adopción fue escalonada, no asignada al azar) y la muestra son empresas de alta tecnología con tráfico digital, donde experimentar es barato. Según un resumen del NBER, la herramienta además se asocia a resultados más extremos: las startups jóvenes fallan más rápido y las maduras escalan más. No se leyó el paper completo ni se conoce el tamaño de la muestra.

## El capítulo Measure

En *The Lean Startup*, los capítulos Measure y Experiment (nombres según resúmenes). Fijarse en las tres A y en el ejemplo de cohortes de IMVU, que hay que verificar en el libro.
