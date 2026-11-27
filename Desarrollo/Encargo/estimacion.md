---
resumen: >-
  Estimar en un encargo es decir cuánto va a llevar un trabajo y con cuánta incertidumbre, para
  que el cliente y el proveedor puedan decidir. Se estima con rangos, comparando con proyectos
  parecidos, fijando un apetito en lugar de un número o pronosticando a partir del ritmo medido;
  que construya un agente no elimina el sesgo de optimismo y todavía no hay datos de cuánto cambia.
estado: borrador
estabilidad: semi
fuentes:
  - "Fowler, The Purpose of Estimation, leído: https://martinfowler.com/bliki/PurposeOfEstimation.html"
  - "Singer, Shape Up, cap. 3, Set Boundaries, leído: https://basecamp.com/shapeup/1.2-chapter-03"
  - "Singer, Shape Up, glosario: https://basecamp.com/shapeup/4.5-appendix-06"
  - "Flyvbjerg, informe para el Edinburgh Tram Inquiry, pasos de la previsión por clase de referencia (según resumen del buscador): https://arxiv.org/pdf/1805.12106"
  - "Flyvbjerg, From Nobel Prize to Project Management: Getting Risks Right (metadatos): https://arxiv.org/pdf/1302.3642"
  - "Entrevista a Vasco Duarte sobre NoEstimates, InfoQ, leída: https://www.infoq.com/articles/book-review-noestimates"
  - "Jeffries, The #NoEstimates Movement (según resumen del buscador): https://ronjeffries.com/xprog/articles/the-noestimates-movement/"
  - "Reaktor, forecasting method (según resumen): https://www.reaktor.com/insights-and-events/forecasting-method"
  - "Expedia Group Tech, Monte Carlo forecasting in software delivery (según resumen): https://medium.com/expedia-group-tech/monte-carlo-forecasting-in-software-delivery-474bb49cb3f9"
  - "Pronóstico Monte Carlo con takt time, actas de conferencia 2021 (según abstract por buscador): https://core.ac.uk/download/334528317.pdf"
  - "Thoughtworks Technology Radar, Velocity as productivity (Hold, ene 2015): https://www.thoughtworks.com/radar/techniques/velocity-as-productivity"
  - "METR (2025), Measuring AI Ability to Complete Long Tasks (según su resumen): https://arxiv.org/abs/2503.14499"
  - "Preprints sobre modelos de lenguaje que estiman puntos de historia (según resumen): https://arxiv.org/pdf/2403.08430 ; https://arxiv.org/pdf/2603.06276 ; https://arxiv.org/pdf/2604.03443"
  - "Desarrollo/.investigacion/encargo.md"
  - "Desarrollo/.investigacion/posicion-contraria.md"
aliases: [estimar, estimate, estimación de software, software estimation, previsión, forecasting, pronóstico, apetito, appetite, NoEstimates, reference class forecasting, previsión por clase de referencia, Monte Carlo]
creado: 2026-11-27
revisado:
---

# Estimación

Estimar en un encargo es decir cuánto va a llevar un trabajo y con cuánta incertidumbre, para que el cliente y el proveedor puedan decidir. Se estima con rangos, comparando con proyectos parecidos, fijando un apetito en lugar de un número o pronosticando a partir del ritmo medido; que construya un agente no elimina el sesgo de optimismo y todavía no hay datos de cuánto cambia.

Estimar y cobrar son dos decisiones distintas, y esta base las separa: la estimación dice cuánto cuesta hacer algo, y [modelos de contrato y cobro](modelos-de-contrato-y-cobro.md) decide quién carga el error de esa estimación. Mezclarlas empeora la estimación. Esa advertencia de Jørgensen, junto con los sobrecostos medidos, la cola de proyectos que se disparan, el cono de incertidumbre con su discusión y las cuatro guías para estimar con rango, está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#estimar-con-un-rango-y-separar-la-estimación-de-la-oferta) y no se repite acá.

## Para qué se estima

Fowler dice que la estimación vale «when it helps you make a significant decision»: asignar recursos, coordinar con otros o seguir el avance contra un plan. Según el mismo texto, los equipos que no estiman funcionan cuando el cliente y el equipo acuerdan que las estimaciones no van a manejar decisiones importantes y trabajan por prioridad en unidades chicas. En un encargo hay al menos una decisión que no se puede evitar: el cliente necesita saber cuánto y cuándo antes de firmar.

## Cuatro formas de estimar

| Forma | Qué responde | Qué necesita | Evidencia |
|---|---|---|---|
| Rango por juicio experto | Cuánto cuesta este alcance, con un mínimo y un máximo | Un diseño, aunque sea grueso | Estudios de Jørgensen, en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#estimar-con-un-rango-y-separar-la-estimación-de-la-oferta) |
| Clase de referencia | Cuánto llevaron proyectos parecidos | Un registro de proyectos terminados | Probada en infraestructura; sin valores para software chico |
| Apetito | Cuánto tiempo vale el problema | Un cliente dispuesto a recortar alcance | Método de Basecamp, sin estudios |
| Previsión por ritmo | Cuándo se terminan N ítems, o cuántos llegan a una fecha | Semanas de datos de ítems terminados | Blogs de empresas y un estudio chico |

### Comparar con proyectos parecidos

La previsión por clase de referencia toma la vista de afuera. Según el resumen del informe de Flyvbjerg, «The outside view does not try to forecast the specific uncertain events that will affect the particular project, but instead places the project in a statistical distribution of outcomes from this class of reference projects». El último paso ajusta el número según si el proyecto es más o menos riesgoso que su clase. Viene de Kahneman y Tversky y Flyvbjerg lo probó en transporte; no se encontraron valores de ajuste para proyectos de software.

Para un equipo chico, el equivalente práctico es su propio registro: cuánto llevaron los encargos anteriores del mismo tipo, contra cuánto se había estimado. Es la misma conclusión a la que llega [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#estimar-con-un-rango-y-separar-la-estimación-de-la-oferta), y en criterio de esta base es lo primero que conviene empezar a anotar.

### Fijar el apetito

Shape Up da vuelta la pregunta: «Estimates start with a design and end with a number. Appetites start with a number and end with a design». El principio es «fixed time, variable scope». Si el trabajo no entra, se recorta (*scope hammering*), y si no termina en el ciclo, se cancela por defecto en lugar de extenderse (*circuit breaker*). La explicación completa está en [Shape Up](../../Producto/Planificacion-y-entrega/shape-up.md#apetito-en-lugar-de-estimación).

Shape Up describe un equipo con producto propio, no un proveedor con contrato. Fijar el apetito con el cliente y acordar que lo que se recorta es alcance es una lectura de esta base; el contrato que eso pide es el de alcance variable, en [modelos de contrato y cobro](modelos-de-contrato-y-cobro.md).

### Pronosticar por ritmo

La previsión probabilística toma los ítems terminados por semana, simula miles de veces y muestra una distribución de fechas. Según resúmenes de blogs de empresas, una guía sugiere usar 12 a 16 semanas de datos y otra más de 10.000 simulaciones, y el método supone un tablero llevado con rigor: límite de trabajo en curso y todos los ítems registrados. Según el abstract de unas actas de 2021, los pronósticos de fecha con Monte Carlo sobre takt time tuvieron un error relativo medio del 32 % en una serie de diez corridas. Es un estudio chico y no hay una comparación con proyectos a medida.

El ritmo solo existe después de empezar, así que esta forma no sirve para cotizar. Sirve para el [seguimiento](seguimiento-con-el-cliente.md): mostrar cuándo es probable terminar sin hablar de porcentajes.

> [!IMPORTANT]
> #NoEstimates está en disputa. Duarte propone decidir por valor, planificar con «a budget, not an estimate», contar ítems entregados contra lo que queda y tratar el momento en que lo que queda excede la capacidad como disparador de decisiones («I never assume that scope is fixed, or the backlog is complete»). Su evidencia es anecdótica: la entrevista habla de «accuracy levels near 100%» sin datos. Según el resumen del buscador, Zuill propone dejar de estimar y Duarte, empezar y pronosticar después de unos sprints; Jeffries y McConnell lo discuten, y un crítico dice que ninguno de los dos bandos muestra casos reales. No hay estudio de proyectos sin estimaciones. Para un encargo con precio, queda en pie la parte de pronóstico por ritmo; la de no estimar choca con que el cliente pregunta antes de firmar.

## Lo que pierde peso, y con qué respaldo

La velocidad del equipo como medida de productividad tiene respaldo para dejarse: el Radar de Thoughtworks la puso en Hold en 2015, porque se usa para jugar la métrica en lugar de entregar software. La misma entrada admite la velocidad como estimación interna de capacidad.

Estimar en horas cada tarea técnica y sumar no tiene ese respaldo. Lo que hay es evidencia de que la estimación detallada se queda corta de forma sistemática, no de que haya que abandonarla, y nada de lo encontrado compara estimar tarea por tarea contra estimar en grueso. Que pierde peso es criterio de esta base, y se dice así en [lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-desarrollo.md).

## Estimar cuando construye un agente

No hay estudio sobre estimar trabajo que hace un agente; el informe de posición contraria lo marca como el hueco más grande de esta nota. Lo que hay es indirecto y se lee con cuidado:

- Que un modelo de lenguaje estime da resultados dispares. Según los resúmenes de tres preprints, en cero ejemplos rinde peor que los promedios de base, con pocos ejemplos mejora, y todos miden puntos de historia y no tiempo; los autores piden evaluarlo antes de reemplazar la estimación del equipo.
- METR mide el horizonte de tareas que un agente completa la mitad de las veces y, según su resumen, encontró que se duplicó cada siete meses aproximadamente desde 2019. METR advierte que no se lee como que la IA haga todo el trabajo de esa duración. En criterio de esta base, sirve para decidir qué porción darle a un agente, no para estimar el proyecto.
- Cuánto acelera un agente a quien programa tiene evidencia en las dos direcciones, como cuenta [agente de código](../Construccion/agente-de-codigo.md).

La lectura de esta base es que la parte que el agente abarata (escribir el código) nunca fue la que más se desviaba. Lo que dispara los proyectos sigue ahí: definir mal, integrar, requisitos que cambian. Y nada indica que el sesgo de optimismo desaparezca porque estime o construya un agente; tampoco se encontró evidencia en contra.

Para leer: el capítulo 3 de Shape Up, «Set Boundaries», se lee en media hora; el texto de Fowler sobre el propósito de estimar es de una página. Fijate en qué decisión va a tomar alguien con el número antes de darlo.
