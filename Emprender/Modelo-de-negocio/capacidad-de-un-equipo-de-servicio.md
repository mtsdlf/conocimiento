---
resumen: >-
  La capacidad de un equipo de servicio es cuánto trabajo puede tomar sin que los tiempos de respuesta se disparen. Se calcula con dos cuentas de la teoría de colas: cuántos clientes hay a la vez (ingresos por mes por meses que dura cada uno) y cuánto esperan según qué tan cargado está el equipo, que crece muy rápido cerca del 100 %.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, Kingman's formula (fórmula y definiciones; cita a Kingman 1961): https://en.wikipedia.org/wiki/Kingman%27s_formula"
  - "John D. C. Little (2011), Little's Law as Viewed on Its 50th Anniversary, Operations Research 59(3), 536-549 (primeras secciones leídas): https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf"
  - "Harchol-Balter y Scully, preguntas frecuentes sobre colas (CMU), según resumen: https://www.cs.cmu.edu/~harchol/Papers/tmp/TeaPACS21.pdf"
  - "David Maister, The Psychology of Waiting Lines (leído; el texto extraído tiene huecos): https://davidmaister.com/articles/1/52/index.html"
  - "David Maister, The Laws of Service Businesses (leído): https://davidmaister.com/articles/1/56/index.html"
  - "David Maister, The Anatomy of a Consulting Firm (prosa leída, figuras no): https://davidmaister.com/articles/16/2/"
  - "Fitzsimmons, Fitzsimmons y Bordoloi, Service Management, 9.ª ed. (McGraw-Hill), caps. 11 a 13 (solo los títulos, vistos en un fragmento del buscador)"
  - "Deltek, Professional services billable utilization (sobre SPI Research 2025): https://www.deltek.com/resources/articles/professional-services-billable-utilization-historic-low/"
  - "Bartolucci y Vivo (2026), Queue & AI: When Faster Tasks Slow Down the Workflow, arXiv 2605.27202, preprint (abstract, modelo y secciones elegidas): https://arxiv.org/pdf/2605.27202"
  - "Emprender/.investigacion/economia-de-una-firma-de-servicios.md"
  - "Emprender/.investigacion/plata-de-un-servicio-contraria.md"
aliases: [capacidad, capacity planning, planificación de capacidad, utilización, ley de Little, Little's law, fórmula de Kingman, teoría de colas, cuántos clientes]
creado: 2026-11-24
revisado:
---

# Capacidad de un equipo de servicio

La capacidad de un equipo de servicio es cuánto trabajo puede tomar sin que los tiempos de respuesta se disparen. Se calcula con dos cuentas de la teoría de colas: cuántos clientes hay a la vez (ingresos por mes por meses que dura cada uno) y cuánto esperan según qué tan cargado está el equipo, que crece muy rápido cerca del 100 %.

Es el techo físico de la [economía de una firma de servicios](economia-de-una-firma-de-servicios.md): la ecuación de Maister dice cuánto gana cada socio, y la capacidad dice cuántos clientes puede atender. Le pone un límite a cuántos [abonos de cuidado](abono-de-cuidado.md) entran antes de tener que contratar, automatizar o subir el precio, que se decide como explica [pricing y empaquetado](../../Producto/Monetizacion/pricing-y-empaquetado.md). Y es un supuesto del [plan financiero mínimo](../Finanzas/plan-financiero-minimo.md): los ingresos proyectados no pueden pasar lo que el equipo puede entregar.

## Cuántos clientes hay a la vez

La ley de Little dice que la cantidad media de ítems en un sistema es la tasa a la que llegan por el tiempo que se quedan: L = λW (Little, 1961; repasada en Little, 2011). No hace falta suponer cómo se distribuyen las llegadas. Aplicada a clientes, que es una analogía de esta base:

- Con 2 proyectos nuevos por mes que duran 1,5 meses cada uno, hay en promedio 3 proyectos en curso.
- Con 3 altas de abono por mes y una permanencia media de 20 meses, el equipo termina sosteniendo unos 60 abonos.

La segunda cuenta dice algo que no se ve mes a mes: un abono que se vende bien se acumula. La permanencia media es la inversa de la tasa de bajas; cómo se mide está en [retención y churn](../../Datos/Retencion-y-churn/retencion-y-churn.md). Si el equipo puede atender 40 abonos y entran 3 por mes con una permanencia de 20 meses, se llena antes de los dos años, aunque ningún mes parezca cargado.

No se encontró una cifra con fuente de cuántos clientes de abono atiende una persona en este tipo de servicio. Se arma con la cuenta de arriba, las horas que lleva cada cliente por mes y la utilización objetivo de la sección siguiente.

## Por qué no conviene trabajar al 100 %

Cuanto más cargado está un equipo, más esperan los pedidos, y la espera crece mucho más rápido que la carga. La aproximación de Kingman da la espera media en la cola como:

espera ≈ (ρ / (1 − ρ)) × ((cₐ² + cₛ²) / 2) × τ

donde ρ es la utilización (trabajo que llega sobre capacidad), cₐ y cₛ miden cuánto varían las llegadas y la duración de cada tarea, y τ es la duración media de una tarea. Wikipedia la describe como «generally very accurate, especially for a system operating close to saturation».

Con llegadas y duraciones irregulares típicas (cₐ = cₛ = 1), la espera vale ρ/(1 − ρ) veces lo que dura una tarea. La tabla es una cuenta de esta base con esa fórmula:

| Utilización | Espera en la cola, en duraciones de tarea |
|---|---|
| 50 % | 1 |
| 70 % | 2,3 |
| 80 % | 4 |
| 90 % | 9 |
| 95 % | 19 |

Si un pedido de un cliente de abono lleva dos horas, con el equipo al 90 % espera en promedio dieciocho horas de trabajo antes de que alguien lo empiece. Si el trabajo llega tan rápido como el equipo lo procesa, la cola crece sin límite.

La variabilidad pesa tanto como la carga. Según el resumen de Harchol-Balter y Scully, con tareas muy desparejas la espera puede ser larga aun con poca utilización. Para un servicio, eso se traduce en dos palancas además de contratar: emparejar las tareas (paquetes de cambios de tamaño parecido, ventanas fijas) y emparejar las llegadas (pedidos que se juntan y se atienden en días fijos). Es lectura de esta base sobre la fórmula; no se encontró un estudio que fije un umbral de utilización para trabajo intelectual.

## Dos utilizaciones que no son la misma

La palabra utilización se usa para dos cosas, y confundirlas lleva a llenar el equipo sin darse cuenta:

| | Utilización facturable | Carga |
|---|---|---|
| Qué cuenta | Horas que se cobran sobre horas trabajadas | Todo el trabajo que llega sobre la capacidad del equipo |
| Quién la usa | Maister, los benchmarks de servicios profesionales | La teoría de colas (Kingman, Little) |
| Para qué sirve | Saber cuánto factura cada persona | Saber cuánto esperan los pedidos |

Un equipo puede estar al 66 % facturable y al 95 % de carga, porque vender, administrar y atender urgencias también ocupa horas (lectura del informe de investigación de esta base). El benchmark de SPI Research da un 66,4 % de utilización facturable promedio en 2025 y un 75 % para las firmas de mejor desempeño; Maister usa 75 % para seniors y mandos medios y 90 % para juniors en su ejemplo. Son cifras de utilización facturable, no de carga. La ficha de esas cifras está en [economía de una firma de servicios](economia-de-una-firma-de-servicios.md#cifras-de-utilización-de-referencia).

## Nivelar la demanda o perseguirla

Ante una demanda que sube y baja, los textos de operaciones de servicios describen dos estrategias. Una es mantener la capacidad fija y gestionar la demanda. La otra es mover la capacidad detrás de la demanda: gente part-time, y programar para la temporada baja lo que puede esperar. Las dos salen de resúmenes; los capítulos 11 a 13 de Fitzsimmons y otros, *Service Management*, que son el canónico de la materia, no se leyeron.

En un servicio que mezcla proyectos y abonos, la lectura de esta base es que el abono es la carga de base y los proyectos son lo que sube y baja: la capacidad comprometida con abonos es la que no se puede mover.

## Cuánto se nota la espera

La espera que el cliente siente no es la espera real. Maister, en «The Psychology of Waiting Lines», da proposiciones como «Uncertain waits are longer than known, finite waits» y «Unexplained waits are longer than explained waits». Para un abono, avisar cuándo se va a resolver un pedido y explicar una demora cuesta menos que bajar la espera, y cambia cómo se juzga el servicio. En «The Laws of Service Businesses» suma un riesgo de capacidad que no está en las fórmulas: el desgaste de quien atiende.

## Qué cambia cuando parte del trabajo lo hacen agentes

Que un agente haga una tarea más rápido no garantiza que el equipo atienda más. Bartolucci y Vivo (2026), en un preprint sin revisión de pares, modelan un equipo donde la IA hace el trabajo y las personas lo revisan. El cuello de botella pasa a ser la atención humana de revisión. La IA puede bajar el tiempo medio de una tarea y aun así alargar las esperas si suma variabilidad: errores que pasan la revisión y vuelven como retrabajo. En su ejemplo calibrado, la tarea baja de 1 hora a 0,85 de media, pero el cuadrado de su coeficiente de variación pasa de 0,10 a 1,25: el coeficiente queda unas 3,5 veces más alto.

Leído con la fórmula de Kingman, que es lectura de esta base, la capacidad de un equipo con agentes depende de cuánto tiempo de revisión pide cada tarea y de cuán pareja sale. No se encontró ningún dato de campo sobre equipos chicos de servicios que trabajen así.

> [!NOTE]
> Sin fuente todavía: Fitzsimmons y otros, *Service Management* (9.ª ed.), caps. 11 a 13; Kingman (1961) en el original; una cifra de clientes de abono por persona en servicios de tiendas online o de sitios web.

Para leer más, el artículo de Little por los 50 años de su ley, en sus dos primeras secciones, explica la cuenta sin matemática pesada; conviene fijarse en que vale con cualquier distribución. La entrada de Wikipedia sobre la fórmula de Kingman alcanza para entender por qué la espera depende de la carga, de la variabilidad y de la duración media.
