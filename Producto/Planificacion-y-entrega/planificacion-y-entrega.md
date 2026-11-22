---
resumen: >-
  Planificación y entrega es la parte de producto que decide qué se hace primero y cómo llega a la gente: ordena lo que el descubrimiento dejó como digno de construir y lo pone en manos de los usuarios de forma controlada.
estado: borrador
estabilidad: estable
fuentes:
  - "Sean McBride, RICE: Simple prioritization for product managers (Intercom, 2018-01-05): https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/"
  - "Marty Cagan, The Alternative to Roadmaps (SVPG, 2015-09-07): https://www.svpg.com/the-alternative-to-roadmaps/"
  - "Ryan Singer, Shape Up (Basecamp), cap. 2, cap. 8 y apéndice 2: https://basecamp.com/shapeup"
  - "Pete Hodgson, Feature Toggles (martinfowler.com, 2017-10-09): https://martinfowler.com/articles/feature-toggles.html"
  - "Marty Cagan, Dual-Track Agile (SVPG, 2012-09-17): https://www.svpg.com/dual-track-agile/"
  - "Scrum Guide: https://scrumguides.org/scrum-guide.html"
  - "Pragmatic Institute Framework: https://www.pragmaticinstitute.com/framework/"
  - "Producto/.investigacion/planificacion-y-entrega.md"
  - "Producto/.investigacion/posicion-contraria.md"
aliases: [planning and delivery, planificación de producto, product planning]
creado: 2026-11-22
revisado:
---

# Planificación y entrega

Planificación y entrega es la parte de producto que decide qué se hace primero y cómo llega a la gente: ordena lo que el descubrimiento dejó como digno de construir y lo pone en manos de los usuarios de forma controlada.

En el ciclo del [producto](../producto.md) va entre dos vecinos. Recibe de [Descubrimiento](../Descubrimiento/descubrimiento.md) las ideas que pasaron las pruebas y de [Estrategia](../Estrategia/estrategia.md) los resultados que se buscan. Entrega a [Medición](../Medicion/medicion-de-producto.md) algo que ya está en producción y se puede medir. Si la medición desmiente una apuesta, el orden de lo que sigue cambia (lectura de esta base).

## Tres respuestas a la misma pregunta

Priorización, roadmap y Shape Up contestan la misma pregunta, "qué hacemos y en qué orden", cada uno con otra herramienta. Esta lectura es del informe de investigación de esta base; ninguna fuente lo plantea así.

| Respuesta | Qué produce | Qué supone | Dónde se lee |
|---|---|---|---|
| Puntaje | Una lista ordenada por una fórmula (RICE, costo de demora) | Ideas comparables entre sí y estimables | [Priorización](priorizacion.md) |
| Roadmap | Temas o resultados ubicados en el tiempo | Un horizonte de varios meses que hay que comunicar | [Roadmap](roadmap.md) |
| Apuesta con tiempo fijo | Lo que entra en el próximo ciclo de seis semanas | Que el alcance se recorta y el tiempo no | [Shape Up](shape-up.md) |

Los puntajes ordenan una cola. Intercom publicó RICE en 2018 para comparar ideas por alcance, impacto, confianza y esfuerzo. El costo de demora, que SAFe convirtió en WSJF, sirve según esta base cuando el valor depende del momento en que se entrega (síntesis del informe, no una cita). Ningún estudio con método mostró que puntuar mejore las decisiones: las críticas y las defensas son opinión de practicantes.

El roadmap pone la dirección en el tiempo, y ahí está la disputa más viva de la vertical. Cagan desconfía de él porque las fechas son "essentially just your hopes and wishes" y propone objetivos por equipo. *Product Roadmaps Relaunched* y el Pragmatic Institute lo mantienen, pero organizado por temas y resultados. Ninguna de las dos posiciones tiene estudio.

Shape Up reemplaza a las dos con apuestas. Basecamp trabaja en ciclos de seis semanas, decide en una reunión de apuestas qué entra y no mantiene backlog. El tiempo es fijo y el alcance se ajusta.

## Del código a la gente: el lanzamiento

Salir al mercado tiene una parte de producto y otra de marketing. La de producto decide qué sale, para quién y cómo se despliega: con *feature toggles* (Hodgson) el código llega a producción apagado y se enciende para un porcentaje chico de usuarios antes de abrirlo a todos. La de marketing pone el mensaje, los canales y el [posicionamiento](../../Marketing/Propuesta/posicionamiento.md). En el marco de Pragmatic Institute el lanzamiento vive en "Go-to-Market", separado del roadmap. Ninguna fuente leída fija el reparto entre product manager y product marketing; está en [Lanzamiento](lanzamiento.md).

## Cuando el cliente paga por fechas

La escuela de este tema recomienda roadmaps de resultados, sin fechas salvo excepciones. Una consultora o una agencia vende otra cosa: alcance y fecha, firmados en un contrato. Los estudios de contratos de software (precio fijo contra tiempo y materiales) no dan un ganador único y tienen muestras de un solo país; el detalle está en [pricing y empaquetado](../Monetizacion/pricing-y-empaquetado.md#como-cobra-una-consultora-o-una-agencia). Cómo se combina un roadmap de resultados con compromisos firmados está en [Roadmap](roadmap.md#el-roadmap-cuando-el-cliente-paga-por-fechas-y-alcance).

## Dónde termina producto y empieza Scrum

Scrum define un rol de dueño del backlog, no de producto entero. Según la Scrum Guide, "The Product Owner is accountable for maximizing the value of the product resulting from the work of the Scrum Team", responde por el Product Backlog y el Product Goal, y trabaja en Sprints de "one month or less". La guía no dice cómo se descubre qué poner en ese backlog.

Esa costura (lectura de esta base) es la que Cagan describió en 2012 como *dual-track*, término que atribuye a Jeff Patton ("Dual-Track Scrum"): "The Discovery track is all about quickly generating validated product backlog items" y "the Delivery track is all about generating releasable software". Después lo dejó porque "the phrase made people focus far too much on process, and not enough on the principles", y pasó a hablar de descubrimiento continuo y entrega continua. El descubrimiento tiene su nota en [Descubrimiento continuo](../Descubrimiento/descubrimiento-continuo.md).

Product owner y product manager no son lo mismo en la teoría, y en la práctica muchas empresas los funden en una persona (afirmación sin fuente en esta base). Cómo se reparten los roles está en [Roles de producto](../Organizacion/roles-de-producto.md).

> [!NOTE]
> Sin fuente todavía: una comparación con método entre el product owner de Scrum y el product manager.

## Cómo falla la planificación

La planificación falla de tres maneras que las fuentes nombran. La primera es el roadmap como lista de funcionalidades con fechas, que según Cagan "tell the team what to do" y salta el trabajo de descubrir; las escuelas que discuten entre sí coinciden en que es la peor forma. La segunda es el "scoring theater" que critican algunos blogs: el puntaje convierte un desacuerdo en aritmética y da una precisión que no tiene. La tercera es adoptar Shape Up fuera de su escala: Singer avisa que "the specific practices ... are scale-dependent", y los casos de equipos que lo dejaron son anécdotas, no estudios.

## Qué hay adentro de planificación y entrega

- [Priorización](priorizacion.md): RICE, costo de demora y WSJF, y Kano como clasificación; qué método sirve para qué.
- [Roadmap](roadmap.md): la disputa entre Cagan, *Roadmaps Relaunched* y Now-Next-Later, y el roadmap cuando el cliente paga por fechas.
- [Shape Up](shape-up.md): ciclos de seis semanas, apetito y apuestas en lugar de backlog, y de qué escala depende.
- [Lanzamiento](lanzamiento.md): feature toggles, lanzamiento gradual y el límite con product marketing.

Faltan estos componentes y se van a sumar:

- ICE y MoSCoW, dos métodos de priorización que no se investigaron todavía.
- Deuda técnica como decisión de producto: cuándo se prioriza contra funcionalidades.
- Ciclo de vida del producto: cómo cambia la planificación entre el lanzamiento, el crecimiento y el retiro.
