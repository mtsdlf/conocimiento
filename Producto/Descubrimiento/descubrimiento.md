---
resumen: >-
  El descubrimiento es el trabajo con el que un equipo de producto decide qué construir antes de construirlo: habla con clientes, nombra los riesgos de cada idea y los reduce con pruebas chicas y baratas.
estado: vigente
estabilidad: estable
fuentes:
  - "Teresa Torres, Product Talk, glosario Continuous Discovery: https://www.producttalk.org/glossary-discovery-continuous-discovery/"
  - "Teresa Torres, Continuous Discovery Habits (2021), caps. 1-2 (no leído; citado a través de las páginas de la autora)"
  - "Marty Cagan, Continuous Discovery (SVPG, 2012-10-24): https://svpg.com/continuous-discovery/"
  - "Marty Cagan, Product Risk Taxonomies (SVPG, 2023-07-10): https://svpg.com/product-risk-taxonomies"
  - "Jeff Patton, Dual-track development (2017, actualizado 2023): https://www.jpattonassociates.com/dual-track-development/"
  - "Teresa Torres, Assumption testing (Product Talk, 2023): https://www.producttalk.org/2023/10/assumption-testing/"
  - "Producto/.investigacion/descubrimiento.md"
  - "Producto/.investigacion/posicion-contraria.md (afirmaciones 2 y 5)"
aliases: [product discovery, discovery, descubrimiento de producto]
creado: 2026-11-22
revisado: 2026-11-22
---

# Descubrimiento

El descubrimiento es el trabajo con el que un equipo de producto decide qué construir antes de construirlo: habla con clientes, nombra los riesgos de cada idea y los reduce con pruebas chicas y baratas.

Recibe de la [estrategia](../Estrategia/estrategia.md) el [resultado](../Estrategia/resultados-y-entregables.md) que hay que mover, y le entrega a [planificación y entrega](../Planificacion-y-entrega/planificacion-y-entrega.md) lo que vale la pena construir. La razón de ser de toda la vertical es la que cruza el tema: en muchos dominios la mayoría de las ideas no mejora la métrica que buscaba, según los experimentos a gran escala que cita la [entrada del tema](../producto.md#la-idea-que-cruza-todo-el-tema). Si construir es caro y la intuición falla seguido, conviene averiguar barato antes.

## Dónde termina: Emprender y UX

Tres prácticas se llaman parecido y no son la misma. El [descubrimiento de clientes](../../Emprender/Validacion/descubrimiento-de-clientes.md) de Blank, del tema Emprender, busca un modelo de negocio en una empresa nueva: si existe un problema por el que alguien paga. El descubrimiento de esta vertical es el hábito de un equipo dentro de un producto que ya existe, que decide todas las semanas qué construir a continuación. El límite es una lectura de esta base sobre Torres, Cagan y Patton, no una cita de ellos.

La [investigación de UX](../../UX/Investigacion/investigacion.md) aporta los métodos: la [entrevista de usuario](../../UX/Investigacion/entrevista-de-usuario.md), el [test de usabilidad](../../UX/Evaluacion/test-de-usabilidad.md) y el mapa de [qué método contesta qué pregunta](../../UX/Investigacion/metodos-de-investigacion.md). Producto los usa para decidir; UX explica cómo se hacen bien.

## Riesgos, árbol y pruebas: cómo encajan las piezas

Las cuatro piezas son de tipos distintos. Los [cuatro riesgos](cuatro-riesgos.md) son una taxonomía de qué hay que averiguar de una idea: si tiene valor, si se puede usar, si se puede construir y si le sirve al negocio. Es la pieza central: las otras se explican como formas de reducir esos riesgos.

El [árbol de oportunidades](arbol-de-oportunidades.md) es una representación. Pone arriba el resultado buscado, debajo las necesidades de los clientes que lo moverían, después las soluciones y abajo las pruebas. Sirve para que cada solución que se discute esté atada a algo que se escuchó en una entrevista.

La [prueba de supuestos](prueba-de-supuestos.md) es el método. Cada solución se desarma en los supuestos que tienen que ser ciertos para que funcione, y se prueban primero los más riesgosos, con un prototipo, una encuesta de una pregunta, datos existentes o una prueba técnica corta.

El [descubrimiento continuo](descubrimiento-continuo.md) es la cadencia que mueve todo lo anterior. Torres lo define como "weekly touch points with customers by the team building the product". El mismo equipo que construye, normalmente un trío de producto, diseño e ingeniería, hace el descubrimiento; no lo terceriza en un investigador. Patton lo dibuja como dos vías de un mismo proceso: una aprende rápido y la otra entrega con calidad.

## Lo que el descubrimiento no hace

El descubrimiento reduce riesgos antes de construir. No mide el efecto de lo que ya salió: eso es el [experimento A/B](../Medicion/experimento-ab.md), de la vertical de medición, que compara una solución construida contra la anterior. El descubrimiento es anterior y más barato, y sirve también donde no hay tráfico para un experimento controlado (síntesis de esta base).

Tampoco decide el orden de lo que se construye. Lo que sobrevive a las pruebas pasa a [priorización](../Planificacion-y-entrega/priorizacion.md) y al [roadmap](../Planificacion-y-entrega/roadmap.md).

## Cómo falla

La falla más citada es hacer el ritual sin aprender. Torres sostiene que muchos equipos dicen hacer descubrimiento continuo sin cumplir su mínimo. Un artículo de Dovetail describe equipos que hablaron con una cantidad fija de clientes por semana y aun así hicieron un producto que nadie quiso. Las dos fuentes llegaron por resumen del buscador, y son anécdotas de practicantes.

La otra falla es de contexto. Un practicante señala, según el buscador, que la práctica es difícil en un [equipo de funcionalidades](../Organizacion/equipo-empoderado.md), que recibe una lista de cosas para construir. Un equipo de consultora que construye para un cliente no siempre llega a los usuarios finales ni decide el alcance.

> [!NOTE]
> Sin fuente todavía: cuánto acceso a usuarios tienen los equipos de consultoras y cómo se adapta el descubrimiento a un contrato con alcance fijo. Tampoco hay datos de cuántas pruebas por semana hace un equipo chico.

> [!IMPORTANT]
> No hay estudios con método que muestren que el descubrimiento continuo, el árbol de oportunidades o los cuatro riesgos mejoran los resultados de un equipo. Todo es literatura de practicantes (Cagan, Torres, Patton). Lo que sí tiene evidencia experimental es la premisa: las ideas fallan seguido, y los expertos se equivocan al predecir cuáles van a funcionar (Kohavi y Thomke). La cadencia semanal es la regla de una escuela, no un umbral probado; lo prudente es descubrir con la frecuencia que el contexto permita y medir si se aprende algo, no solo si se habla con gente. La tesis opuesta, el liderazgo por visión del fundador, tampoco tiene estudio comparativo; está en [founder mode](../Organizacion/equipo-empoderado.md#founder-mode-el-fundador-en-los-detalles).

## Las piezas del descubrimiento, en orden de lectura

- [Cuatro riesgos](cuatro-riesgos.md): valor, usabilidad, factibilidad y viabilidad, de dónde salen y cómo se comparan con las taxonomías de IDEO, Bland y Torres. Se lee primero.
- [Descubrimiento continuo](descubrimiento-continuo.md): la cadencia semanal del trío, el origen del dual-track en Sy, Patton y Cagan, y cómo se degrada en teatro.
- [Árbol de oportunidades](arbol-de-oportunidades.md): del resultado buscado a las soluciones y sus pruebas, en nueve pasos, con sus errores típicos.
- [Prueba de supuestos](prueba-de-supuestos.md): cómo se eligen los supuestos más riesgosos y qué tipo de prueba sirve para cada uno, incluidos fake door, Wizard of Oz y concierge.

## Qué falta

Faltan estas notas:

- Entrevista de descubrimiento: la entrevista basada en historias que alimenta el árbol. Mientras tanto, el método general está en [Entrevista de usuario](../../UX/Investigacion/entrevista-de-usuario.md), del tema UX.
- Mapa de supuestos como técnica propia, con el procedimiento de Bland para ordenar supuestos por importancia y evidencia.
- Prototipos por fidelidad: qué se prueba con un boceto, con un prototipo navegable y con uno que usa datos reales.
