---
resumen: >-
  El flujo continuo organiza el trabajo como una corriente de pedidos que entran, esperan en colas y salen terminados, y lo gobierna limitando cuánto trabajo hay en curso, achicando los lotes y ordenando por costo de demora. Sirve para el trabajo que no tiene fin y es la lente principal de este tema.
estado: borrador
estabilidad: estable
fuentes:
  - "Reinertsen (2009), The Principles of Product Development Flow, Celeritas (libro no leído; según resúmenes): https://www.slideshare.net/slideshow/the-principles-of-product-development-flow-a-summary/72489409 ; https://productdevelopment101.substack.com/p/productivity-in-product-development-4bb"
  - "Kanban University, The Kanban Guide (según resumen de la página): https://kanban.university/kanban-guide/"
  - "Agile Alliance, sobre Anderson y el origen de Kanban (según resumen del buscador): https://www.agilealliance.org/?p=8027291"
  - "Little (2011), Little's Law as Viewed on Its 50th Anniversary, Operations Research 59(3) (texto completo): https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf"
  - "PMI, Critical chain project management investigation (según resumen): https://www.pmi.org/learning/library/critical-chain-project-management-investigation-6380"
  - "Gestion-de-proyectos/.investigacion/enfoque.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [flujo, kanban, gestión del flujo, flow, continuous flow, trabajo en curso, WIP, costo de demora, cost of delay]
creado: 2026-11-27
revisado:
---

# Flujo continuo

El flujo continuo organiza el trabajo como una corriente de pedidos que entran, esperan en colas y salen terminados, y lo gobierna limitando cuánto trabajo hay en curso, achicando los lotes y ordenando por costo de demora. Sirve para el trabajo que no tiene fin y es la lente principal de este tema.

Es uno de los [enfoques](enfoque.md) entre los que se [elige](elegir-un-enfoque.md). Lo fijo no es el alcance ni el tiempo sino cuánto trabajo puede haber empezado a la vez; qué entra y cuándo varía. Encaja con un equipo de operaciones, una mesa de ayuda, el mantenimiento de una flota de sistemas o una fábrica de agentes que recibe pedidos todos los días.

## Las colas que no se ven

Según los resúmenes del libro de Reinertsen (2009), las colas invisibles son la causa de fondo del mal desempeño del desarrollo de producto. En una fábrica, el inventario se ve en el piso; en el trabajo del conocimiento, un pedido esperando revisión o una decisión pendiente no ocupa lugar. Que la mayor parte del tiempo de un pedido sea espera es una afirmación que la base trata en el [flujo de valor](../../DevOps/Cultura-y-medicion/flujo-de-valor.md) para software; las fuentes de esta nota no la miden.

La relación entre trabajo en curso, ritmo de salida y tiempo de cada pedido es una identidad de la teoría de colas, la ley de Little. Su consecuencia es directa: con el mismo ritmo de entrega, más trabajo empezado significa más tiempo por pedido. Little (2011) da ejemplos fuera del software, como clientes y botellas en una bodega, y por inferencia de la base eso haría del flujo el enfoque más portable a otros dominios, aunque no hay estudios con método fuera del software. La ley, sus supuestos y las mediciones en equipos reales están en [trabajo en curso y colas](../Seguimiento/trabajo-en-curso-y-colas.md).

## Las cuatro palancas del flujo

1. **Limitar el trabajo en curso.** Se fija cuántos pedidos puede haber empezados en cada paso y no se arranca uno nuevo hasta que salga otro. Es una de las seis prácticas de la guía de Kanban.
2. **Achicar los lotes.** Según los resúmenes de Reinertsen, el tamaño de lote óptimo sale de una curva en U entre dos costos: el de mantener trabajo esperando, que crece con el lote, y el de transacción (preparar, revisar, desplegar), que baja con él. Bajar el costo de transacción permite lotes más chicos.
3. **Ordenar por costo de demora.** El costo de demora es cuánto se pierde por cada semana que algo no está terminado. Reinertsen propone priorizar por costo de demora dividido por duración (CD3): primero lo que pierde mucho y se termina rápido.
4. **Gestionar la variabilidad por su efecto económico.** Para Reinertsen, lo que se minimiza es el impacto económico de la variabilidad, no la variabilidad. Un pedido incierto pero barato de fallar no necesita el mismo control que uno caro.

La guía de Kanban, según la página, define el trabajo en curso como "los ítems que han entrado al sistema o actividad y no han salido" y lista seis prácticas: visualizar, limitar el trabajo en curso, gestionar el flujo, hacer explícitas las políticas, tener ciclos de retroalimentación y mejorar en colaboración. Mide el tiempo de entrega desde el punto de compromiso hasta que el pedido termina. Anderson dice haber aplicado Kanban en 2004 en el área de TI de una empresa de software y definido el método en un proyecto de 2006-2007, según un resumen de Agile Alliance.

## Un caso: la mudanza de cuarenta servicios

Ejemplo inventado para ilustrar, no un caso medido.

Un equipo tiene que mudar cuarenta servicios a una plataforma nueva. Si arranca los cuarenta a la vez, a los tres meses tiene cuarenta mudanzas a medio hacer y ninguna terminada. Con un límite de cuatro en curso, el primer servicio queda andando en la primera semana y cada uno que termina enseña algo para los siguientes. Ordenar por costo de demora pone primero los que más cuesta mantener en la plataforma vieja y menos tardan en mudarse.

## Flujo y cadena crítica

Goldratt llegó a una idea vecina desde la teoría de restricciones (según la formulación habitual, que no se cotejó con su libro): el sistema rinde lo que rinde su paso más lento, y mejorar otro paso no sirve. Su cadena crítica, según una revisión del PMI, trata el síndrome del estudiante y la ley de Parkinson como fuentes de holgura oculta y junta los márgenes al final del proyecto. La misma revisión ve evidencia escasa y supuestos discutidos, como que los recursos estén dedicados. La cadena crítica se trata en [dependencias y camino crítico](../Planificacion/dependencias-y-camino-critico.md) y los márgenes, en [márgenes](../Incertidumbre-y-riesgo/margenes.md).

## Teoría firme, evidencia de campo débil

La matemática de colas es firme; lo que falta son estudios controlados de que limitar el trabajo en curso mejore los proyectos. Lo que hay son estudios de caso de una sola empresa, con resultados mixtos, y no hay un límite óptimo demostrado: el detalle está en [trabajo en curso y colas](../Seguimiento/trabajo-en-curso-y-colas.md). Reinertsen y Anderson son practicantes, y sus libros se citan acá por resúmenes. Las cifras que circulan sobre cuántas empresas miden sus colas o conocen su costo de demora salen de una presentación, no del libro, y no se usan.

> [!NOTE]
> Sin fuente todavía: críticas formales a Reinertsen y estudios con método sobre flujo fuera del software.

## Cómo falla

Inferencias de la base, sin fuente.

- **Límites que nadie respeta.** El tablero muestra el límite, pero ante un pedido urgente se arranca igual. El límite sin una política explícita para lo urgente es decoración.
- **Limitar el paso equivocado.** Se limita lo que está en ejecución mientras la cola real está en revisión o en una aprobación externa. El límite va donde está la restricción.
- **Medir ocupación en vez de flujo.** Tener a todos ocupados sube el trabajo en curso y, con él, el tiempo de cada pedido. Lo que se mide es cuánto tarda un pedido y cuántos salen, como explica [medir el avance](../Seguimiento/medir-el-avance.md).

## El flujo cuando ejecutan agentes

Inferencia de esta base: con agentes, ejecutar deja de ser el paso lento y el cuello de botella se corre a especificar y verificar. El límite de trabajo en curso tiene que ponerse sobre lo que está "listo para revisar", no sobre lo que está "en ejecución": un agente puede abrir veinte frentes en una tarde, y cada uno espera a una persona. Como producir un lote ya casi no cuesta, el costo de transacción que fija el tamaño de lote es el de revisar, no el de construir. Es el argumento de [la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md).
