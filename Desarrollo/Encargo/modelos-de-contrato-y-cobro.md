---
resumen: >-
  El modelo de contrato y cobro de un encargo decide qué se fija de antemano (precio, alcance,
  tarifa, tiempo o resultado) y, con eso, quién carga el costo de que la estimación falle. Los más
  usados son precio cerrado, tiempo y materiales, sus híbridos con tope, alcance variable con precio
  fijo y abono; el cobro por resultado es minoritario, y qué cambia cuando programa un agente
  todavía es teoría.
estado: borrador
estabilidad: semi
fuentes:
  - "Arbogast, Larman y Vodde (2012), Agile Contracts Primer v5, Part 3 y secciones de pago y soporte, leídas: http://www.agilecontracts.org/agile_contracts_primer.pdf"
  - "Fowler (2004), Fixed Scope Mirage, leído: https://martinfowler.com/bliki/FixedScopeMirage.html"
  - "Fink, Lichtenstein y Wyss (2013), Ex post adaptations and hybrid contracts in software development services (abstract e introducción): https://openaccess.city.ac.uk/id/eprint/18016/"
  - "Sutherland (2008), Agile Contracts: Money for Nothing and Your Change for Free: http://jeffsutherland.com/scrum/2008/10/agile-contracts-money-for-nothing-and.html"
  - "Kelly (2014), Agile Contracts: Truth & Options: https://www.allankelly.net/static/presentations/AgileContracts2014.pdf"
  - "Boag (2024), Pricing Projects As A Freelancer Or Agency Owner, Smashing Magazine: https://smashingmagazine.com/2024/08/pricing-projects-freelancer-agency-owner/"
  - "Gaebert, estudio sobre contratos de precio fijo (según resumen del buscador): https://link.springer.com/chapter/10.1007/978-3-319-21915-8_2"
  - "Wikipedia, Agile contracts (solo para ubicar a Opelt y otros, Agile Contracts, Wiley 2013): https://en.wikipedia.org/wiki/Agile_contracts"
  - "Brynjolfsson y Petropoulos (23 ago 2026), Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives, working paper (abstract y sección 1 leídos): https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf"
  - "Gartner, informe sobre acuerdos de servicios por resultado (de pago, no abierto; cifras por resumen del buscador): https://www.gartner.com/en/documents/8201129"
  - "IDC, informe sobre contratos de servicios de IA (no abierto; cifras por resumen del buscador): https://www.idc.com/?p=123073"
  - "AlixPartners, Enterprise software outcome-based pricing (según resumen): https://www.alixpartners.com/media/javp02x3/enterprise-software-outcome-based-pricing-pdf-final.pdf"
  - "CIO.com, Your service vendors are being rebuilt around AI, leído: https://www.cio.com/article/4196348/your-service-vendors-are-being-rebuilt-around-ai.html"
  - "Desarrollo/.investigacion/encargo.md"
  - "Desarrollo/.investigacion/posicion-contraria.md"
aliases: [tipos de contrato, modelo de contrato, precio fijo, precio cerrado, tiempo y materiales, time and materials, T&M, alcance variable, cobro por resultado, outcome-based pricing, retainer, abono, contrato ágil, agile contract]
creado: 2026-11-27
revisado:
---

# Modelos de contrato y cobro

El modelo de contrato y cobro de un encargo decide qué se fija de antemano (precio, alcance, tarifa, tiempo o resultado) y, con eso, quién carga el costo de que la estimación falle. Los más usados son precio cerrado, tiempo y materiales, sus híbridos con tope, alcance variable con precio fijo y abono; el cobro por resultado es minoritario, y qué cambia cuando programa un agente todavía es teoría.

Se elige después de la [estimación](estimacion.md), que dice cuánto cuesta; el contrato decide quién paga el desvío. Cuánto se cobra de lista y cómo se arma la oferta es de [pricing y empaquetado](../../Producto/Monetizacion/pricing-y-empaquetado.md#cómo-cobra-una-consultora-o-una-agencia), y cómo se presenta el número, de [presentar el precio](../../Ventas/La-propuesta/presentar-el-precio.md). El caso del precio cerrado, con sus formas de repartir el riesgo y cómo se pierde plata, está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#formas-de-repartir-el-riesgo).

## Qué se fija y quién carga el riesgo

Lo que no se fija es lo que se mueve cuando la estimación falla. La columna de riesgo es lectura de esta base sobre las fuentes.

| Modelo | Qué se fija | Quién carga el desvío | Fuente |
|---|---|---|---|
| Precio y alcance cerrados | Precio y alcance | El proveedor | *Primer*; Fowler |
| Precio cerrado por fase | El precio de cada fase, cotizada con lo aprendido en la anterior | El proveedor, fase por fase | Boag, una sola fuente |
| Tiempo y materiales | La tarifa | El cliente | *Primer*; Fink y otros |
| Tiempo y materiales con tope | Tarifa y presupuesto máximo | El cliente hasta el tope, el proveedor arriba | Fink y otros; *Primer* |
| Precio por iteración | Un precio por iteración o por unidad de trabajo | Compartido; el proveedor suma una prima | *Primer*, una sola fuente |
| Costo objetivo | Un costo meta con ganancia y pérdida compartidas | Compartido | *Primer*, una sola fuente |
| Precio fijo con alcance variable | El total; lo nuevo reemplaza algo del mismo tamaño | Compartido | Sutherland; *Primer* |
| Por resultado | Un resultado medible | El proveedor | Brynjolfsson y Petropoulos; Gartner e IDC por resumen |
| Abono | Un pago periódico por disponibilidad o mantenimiento | El proveedor si el trabajo crece; el cliente si no lo usa | *Primer*, fase de soporte; [abono de cuidado](../../Emprender/Modelo-de-negocio/abono-de-cuidado.md) |

La regla más trasladable, según [pricing y empaquetado](../../Producto/Monetizacion/pricing-y-empaquetado.md#cómo-cobra-una-consultora-o-una-agencia), viene de la teoría de agencia: cuanto más incierto el alcance, más conviene que el precio siga al tiempo. En Argentina, la diferencia entre prometer un resultado entregable y prometer una actividad cambia lo que se debe, como cuenta [contrato de servicio](../../Emprender/Legal-e-impuestos/contrato-de-servicio.md#obra-para-armar-servicio-para-cuidar).

## Por qué fijar el alcance suele salir mal

Dos practicantes desaconsejan el precio y el alcance fijos a la vez. El *Agile Contracts Primer* dice que esos contratos «tend toward lose-lose situations for both the customer and supplier», y que las ofertas de precio fijo agregan una contingencia «as high as 50%», sin citar de dónde sale. Fowler cuenta que siempre aconsejó a sus clientes «to avoid this mirage», que hay proveedores que «deliberately low-bid the fixed price, with the explicit plan of making a profit on change requests», y concluye: «It is possible to do a FixedPrice contract in an agile manner, but it's not wise to fix the scope». Son dos fuentes independientes, ambas de practicantes y no estudios.

Lo que tiene respaldo de estudios es la causa: los proyectos se pasan de lo estimado de forma sistemática (Jørgensen, en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#por-qué-el-precio-cerrado-tiende-a-perder-plata)). Un precio cerrado le pasa ese riesgo al proveedor.

> [!IMPORTANT]
> El precio fijo con alcance variable es práctica de consultores sin respaldo empírico, y para dinero esta base pide dos fuentes independientes que no hay. La única línea de estudios es delgada: según el resumen del buscador, Gaebert encontró que los clientes confiables hacen creíbles los contratos de precio fijo y que las cláusulas sofisticadas no tienen ese efecto, una tesis de Portsmouth dice que no había todavía investigación académica sustancial sobre Scrum bajo precio fijo cerrado y otra, de práctica, que su aplicación exitosa con alcance y plazo predeterminados «has not been proven». Opelt y otros (*Agile Contracts*, 2013) proponen un precio indicativo que se vuelve vinculante después de dos a cinco sprints de verificación, según un resumen de Wikipedia; el libro no se leyó. La evaluación escéptica de Kelly sobre el contrato de Sutherland está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#formas-de-repartir-el-riesgo).

## Cómo se paga a lo largo del encargo

El *Primer* dice que el sistema de pago más popular en contratos iterativos es pagar cada iteración cuando se acepta su entregable. Es una sola fuente, pero ata el cobro a la [aceptación por partes](alcance-y-aceptacion.md#la-aceptación-por-partes) y, en criterio de esta base, reduce lo que el proveedor tiene trabajado sin cobrar. Los adelantos y los hitos que usan las agencias están en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#formas-de-repartir-el-riesgo).

Para el soporte después del proyecto, el *Primer* describe un caso con «Progressive, capped T&M»: presupuesto anual fijo, alcance variable y tope mensual, aceptable porque «a high level of trust had been established». El modelo de negocio de ese tramo es el [abono de cuidado](../../Emprender/Modelo-de-negocio/abono-de-cuidado.md#cómo-se-cobra); el paso al soporte, el [traspaso](traspaso.md).

> [!NOTE]
> Sin fuente todavía: «Agile Fixed Price» como método con nombre, leído en una fuente primaria, y el capítulo de Opelt y otros sobre alcance adaptable.

## Cobrar cuando el código lo escribe un agente

Es la parte de evidencia más débil: un marco teórico y cifras de informes que no se leyeron.

El marco es un *working paper* de Brynjolfsson y Petropoulos del 23 de agosto de 2026, sin revisión por pares a la vista. Parte de la teoría principal-agente y de dos ejes: qué tan observable es el resultado y qué tan observable es el costo de los insumos. Sostiene que la IA usada adentro del proveedor «lowers input cost observability: identical deliverables can now be produced with widely varying combinations of human time, computational spend, and unobservable orchestration effort», y que la IA desplegada en el entorno del cliente «raises outcome observability». Su tesis es que «AI tends to push consulting firms toward hybrid and asset-based structures». También pone un límite al cobro por resultado: «Attribution risk therefore sets a floor on outcome-signal informativeness that no amount of instrumentation can lower», lo que limita el cobro por resultado cuando el aporte del proveedor se confunde con lo que hace el cliente. Es una predicción, no una medición con datos de agencias de software.

Las cifras de adopción salen de resúmenes del buscador sobre informes de pago que no se abrieron. Según esos resúmenes, para Gartner solo el 19 % de los compradores de servicios y el 13 % de los acuerdos de los vendedores usan acuerdos por resultado; IDC pone en 21 % los contratos de servicios de IA por resultado; un repaso de Orb de 80 empresas de agentes (el informe no registró su enlace) encontró cobro por resultado puro en el 3,8 %; y un analista de Gartner lo llama «more buzz than reality». El marco y esas cifras coinciden en que dominan los híbridos, aunque las cifras son de segunda mano.

Según su resumen, AlixPartners nota que el código de un agente es más difícil de atar a un resultado limpio que un ticket resuelto, y CIO.com advierte que «pay for outcomes» puede ser «a risk transfer unless you can govern it». Que cobrar por hora castiga al eficiente lo dicen sobre todo agencias que venden su propio modelo por resultado, y no cuenta como evidencia.

La lectura de esta base, sin medición propia: las horas de programación pierden relación con el costo y con el valor, y el cliente las ve menos, así que el cobro por hora se vuelve difícil de defender como modelo por defecto. El precio cerrado se vuelve más viable si el alcance está bien acotado, pero el riesgo de cola sigue estando en lo que el agente no hace: definir mal, integrar y los requisitos que cambian. No hay medición de cuánto bajó el costo de un proyecto a medida por usar agentes ni de cómo cambiaron los precios de las agencias.

Para leer: el *Primer*, Part 3, libre; el texto de Fowler, de una página; y el *working paper* de Brynjolfsson y Petropoulos, sabiendo que es teórico. Fijate en qué tan observable es el resultado y qué tan atribuible es a quien lo entrega.
