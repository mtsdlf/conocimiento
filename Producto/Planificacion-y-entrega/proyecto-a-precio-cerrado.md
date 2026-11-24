---
resumen: >-
  Un proyecto a precio cerrado es un trabajo que se cobra con un precio y un alcance fijados antes de empezar, de modo que si cuesta más de lo estimado la diferencia la paga el proveedor. Esta base ordena en cuatro pasos lo que hace falta para que no se coma el margen: estimar con un rango y no con un número, fijar el alcance por escrito, cobrar los cambios contra ese escrito y cerrar con una aceptación formal.
estado: borrador
estabilidad: semi
fuentes:
  - "Jørgensen (2004), A Review of Studies on Expert Estimation of Software Development Effort, Journal of Systems and Software 70 (versión de Simula, abstract y sección de sobreoptimismo leídos): https://cms.simula.no/sites/default/files/publications/SE.4.Joergensen.2004.c.pdf"
  - "Jørgensen, Teigen y Moløkken (2003), Better Sure Than Safe? Over-confidence in judgement based software development effort prediction intervals, Journal of Systems and Software 70 (según el abstract y resúmenes): https://www.simula.no/publications/better-sure-safe-overconfidence-judgment-based-software-development-effort-prediction"
  - "Jørgensen (2004), Top-Down and Bottom-Up Expert Estimation of Software Development Effort (Simula, extractos leídos): https://cms.simula.no/sites/default/files/publications/SE.4.Joergensen.2004.d.pdf"
  - "Moløkken y Jørgensen (2003), A Review of Surveys on Software Effort Estimation, ISESE (abstract): https://static.aminer.org/pdf/PDF/000/435/238/a_review_of_surveys_on_software_effort_estimation.pdf"
  - "Jørgensen, How to Avoid Selecting Providers with Bids Based on Over-Optimistic Cost Estimates (Simula SE.159, leído): https://web-backend.simula.no/sites/default/files/publications/Simula.SE.159.pdf"
  - "Flyvbjerg y Budzier (2011), Why Your IT Project May Be Riskier Than You Think, Harvard Business Review 89(9) (versión arXiv leída): https://arxiv.org/abs/1304.0265"
  - "Eveleens y Verhoef (2010), The Rise and Fall of the Chaos Report Figures, IEEE Software 27(1) (abstract): https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/"
  - "McConnell (2010), Software Development's Cone of Uncertainty, Construx (leído): https://www.construx.com/wp-content/uploads/2019/02/CxWhitePaper_ConeOfUncertainty.pdf"
  - "Bossavit, The Leprechauns of Software Engineering, cap. 2 (pasaje leído): https://leanpub.com/read/leprechauns/leanpub-auto-chapter-2-the-cone-of-uncertainty"
  - "Little (2006), Schedule Estimation and Uncertainty Surrounding the Cone of Uncertainty, IEEE Software 23(3) (abstract según el buscador)"
  - "PMI, PMBOK Guide 6a ed. (2017), cap. 5, Validate Scope y Control Scope (según resúmenes de preparación para el examen): https://www.projectmanagement.com/blog-post/58284/project-scope-management-part-6--control-scope"
  - "Arbogast, Larman y Vodde (2012), Agile Contracts Primer v5 (secciones de cambio, aceptación, garantía y Part 3 leídas): http://www.agilecontracts.org/agile_contracts_primer.pdf"
  - "Sutherland (2008), Agile Contracts: Money for Nothing and Your Change for Free (leído): http://jeffsutherland.com/scrum/2008/10/agile-contracts-money-for-nothing-and.html"
  - "Kelly (2014), Agile Contracts: Truth & Options (diapositivas leídas): https://www.allankelly.net/static/presentations/AgileContracts2014.pdf"
  - "Fink, Lichtenstein y Wyss (2013), Ex post adaptations and hybrid contracts in software development services, Applied Economics 45(32) (abstract e introducción): https://openaccess.city.ac.uk/id/eprint/18016/"
  - "Fowler (2004), Fixed Scope Mirage (según resumen): https://martinfowler.com/bliki/FixedScopeMirage.html"
  - "Boag (2024), Pricing Projects As A Freelancer Or Agency Owner, Smashing Magazine (leído): https://smashingmagazine.com/2024/08/pricing-projects-freelancer-agency-owner/"
  - "Torchbox (2020), Fixed price is dead. (leído): https://torchbox.com/blog/agile-contracts-vs-fixed-price-contracts/"
  - "Producto/.investigacion/proyecto-a-precio-cerrado.md"
  - "Emprender/.investigacion/plata-de-un-servicio-contraria.md"
aliases: [precio cerrado, precio fijo, fixed price, fixed bid, FPFS, presupuesto cerrado, llave en mano, change request, change order, solicitud de cambio, scope creep, aceptación]
creado: 2026-11-24
revisado:
---

# Proyecto a precio cerrado

Un proyecto a precio cerrado es un trabajo que se cobra con un precio y un alcance fijados antes de empezar, de modo que si cuesta más de lo estimado la diferencia la paga el proveedor. Esta base ordena en cuatro pasos lo que hace falta para que no se coma el margen: estimar con un rango y no con un número, fijar el alcance por escrito, cobrar los cambios contra ese escrito y cerrar con una aceptación formal.

Cuándo conviene cobrar cerrado y cuándo por tiempo y materiales está en [pricing y empaquetado](../Monetizacion/pricing-y-empaquetado.md#cómo-cobra-una-consultora-o-una-agencia): cuanto más incierto el alcance, más conviene que el precio siga al tiempo. Un [servicio productizado](../../Emprender/Modelo-de-negocio/servicio-productizado.md) achica esa incertidumbre porque repite el mismo alcance. [Shape Up](shape-up.md) resuelve el mismo problema al revés, con el tiempo fijo y el alcance variable. Cómo se combinan las fechas firmadas con un roadmap está en [roadmap](roadmap.md#el-roadmap-cuando-el-cliente-paga-por-fechas-y-alcance). Esta nota trata lo que pasa después de elegir el precio cerrado: cómo se hace para no perder plata.

## Por qué el precio cerrado tiende a perder plata

Las estimaciones de software se quedan cortas, y el error no es simétrico. En las encuestas que revisaron Moløkken y Jørgensen (2003), «Most projects (60-80%) encounter effort and/or schedule overruns», con un sobrecosto promedio del 30 % al 40 %. Las cifras del informe CHAOS de Standish, que circulan mucho más, no sirven como referencia: Eveleens y Verhoef (2010) mostraron que sus definiciones miden solo si se cumplió la estimación y que, aplicadas a 1211 proyectos, no coincidían con los resultados.

El promedio esconde la cola. Flyvbjerg y Budzier (2011) midieron 1471 proyectos de tecnología con un sobrecosto medio del 27 %, pero «Fully one in six of the projects in the sample was a Black Swan, with a cost overrun of 200%, on average». La lectura de esta base es que, en un proyecto a precio cerrado, esa cola la carga el proveedor. La muestra es de proyectos enormes (US$ 167 millones de costo promedio, 92 % del sector público), así que sirve para la forma del riesgo y no para su tamaño en un proyecto chico. No se encontraron cifras de sobrecosto de proyectos chicos de comercio electrónico.

Además, ganar una oferta a precio cerrado selecciona al optimista. En un estudio de campo de Jørgensen, 35 proveedores cotizaron a precio fijo el mismo proyecto. Los tres elegidos con foco fuerte o medio-fuerte en el precio terminaron con sobrecostos de entre el 130 % y el 174 %. El elegido sobre todo por capacidad terminó con el 15 %, y su precio era más de siete veces el del proveedor elegido por precio. Jørgensen cierra con una advertencia para el proveedor: hay que reconocer las rondas de cotización en las que solo se gana si se está muy por debajo del costo real. La lectura de esta base es que competir por precio contra muchos es la situación más peligrosa para cobrar cerrado.

## Estimar con un rango y separar la estimación de la oferta

Mezclar la estimación con lo que se quiere cobrar la empeora. Jørgensen (2004) encontró evidencia «fairly strong» de que mezclar la oferta, el esfuerzo planificado y el esfuerzo más probable baja el realismo. En la práctica, primero se estima cuánto va a costar y después, aparte, se decide el precio.

De su revisión salen cuatro guías aplicables a una cotización:

1. Estimá de arriba hacia abajo (por comparación con proyectos parecidos) y de abajo hacia arriba (sumando tareas), por separado, y compará.
2. Pedí a quien estima que justifique y critique su número.
3. Combiná la estimación de más de una persona o método.
4. Dá un intervalo, no un número.

El sobreoptimismo crece con el control que uno tiene sobre la tarea. Según la misma revisión, el único método que lo redujo fue que estime otra persona distinta de la que va a hacer el trabajo. Los intervalos también salen angostos: según el resumen de otro estudio de Jørgensen, Teigen y Moløkken (2003), los intervalos que los profesionales daban con el 90 % de confianza resultaron demasiado estrechos.

Sumar tareas no siempre mejora el número. Jørgensen recomienda la estimación de abajo hacia arriba salvo que se tengan proyectos muy parecidos para comparar. También advierte que una descomposición demasiado detallada puede empeorarla: es un estudio chico, de siete equipos. La lectura de esta base es que, para un servicio que repite el mismo tipo de proyecto, el registro de cuánto llevaron los anteriores vale más que una lista de tareas más fina.

## Cotizar después de achicar la incertidumbre

Una estimación hecha antes de conocer el proyecto es un rango muy ancho. McConnell (2010) da, en la idea inicial, errores de hasta cuatro veces para arriba o para abajo, y aconseja «avoid making commitments until the Cone has been reduced». El cono no se achica solo con el paso del tiempo: según McConnell, se achica cuando se toman decisiones que sacan variabilidad del proyecto.

> [!IMPORTANT]
> El cono de incertidumbre está discutido. Bossavit dice que es simétrico cuando los proyectos se atrasan mucho más de lo que se adelantan, y que los rangos de Boehm (1981) se determinaron «subjectively». Little (2006), con datos de una empresa, encontró que el rango de error se mantenía casi igual durante todo el proyecto (según el abstract). La lectura de esta base es que las dos posturas dejan en pie lo mismo: una estimación previa al diseño es un rango ancho.

De ahí sale la práctica de cotizar por fases. Boag (2024), desde la práctica de agencias, propone cobrar primero un descubrimiento a precio fijo, de alrededor del 10 % del presupuesto total. Después se hace un prototipo, y la construcción se cotiza a partir de él. Lo que aparece en el camino entra en la cotización de la fase siguiente. Torchbox, una agencia web, reserva el precio fijo para proyectos cortos y claros y trabaja casi todo lo demás con presupuesto tope.

## Cuánto agregar por el riesgo

No se encontró ninguna medición de cuánto margen de riesgo hay que sumar a un precio cerrado de software. Las dos cifras que se encontraron son débiles y no coinciden. El *Agile Contracts Primer* dice que las ofertas a precio fijo agregan una contingencia «as high as 50%» y que esa prima «is usually hidden in the effort estimate», sin citar de dónde sale. Un blog de agencia habla de 15 % a 25 % sobre la estimación interna, sin datos.

El PMBOK distingue dos reservas: la de contingencia, para los riesgos que se conocen, y la de gestión, para los que no (según resúmenes; el texto de PMI no se pudo abrir). Para un servicio chico, la lectura de esta base es fijar la contingencia a partir de cuánto se desviaron los proyectos anteriores del mismo tipo, y no con un porcentaje copiado.

> [!NOTE]
> Sin fuente todavía: un porcentaje de contingencia medido para proyectos de software chicos, y McConnell, *Software Estimation* (2006), sobre descomposición y márgenes, que no se leyó.

## El alcance por escrito y los cambios contra ese escrito

El precio cerrado vale para un alcance, y ese alcance tiene que estar escrito antes de empezar. Según resúmenes del PMBOK 6 (el texto de PMI no se pudo abrir), el alcance aprobado es la línea base: el proceso *Control Scope* «monitors the status of project scope and manages changes to the scope baseline». Sin esa línea base no hay contra qué medir si algo es un cambio.

Un cambio se cotiza antes de hacerlo. La práctica de agencias, sin datos que la midan, coincide en que cada cambio quede por escrito con lo que se agrega, el costo, el efecto en el plazo y la conformidad del cliente. Lo que se acuerda de palabra después es difícil de cobrar; si un pedido verbal obliga a pagar depende de la ley de cada país, y para Argentina no se investigó. El *Agile Contracts Primer* propone una alternativa que no cobra: aceptar un pedido nuevo solo si reemplaza otro del mismo esfuerzo.

El alcance crece aunque nadie lo pida mal. Capers Jones, citado en un resumen, mide cambios de requisitos de entre el 1 % y más del 3 % por mes mientras se analiza, se diseña y se programa. El *scope creep* que describen las agencias tiene causas que se repiten: requisitos mal definidos, ningún canal para pedir cambios, un cliente que participa poco y el *gold-plating*, que es entregar de más sin que nadie lo pida. Es una lista de practicantes, no una medición.

> [!IMPORTANT]
> Que el alcance se pueda fijar está discutido. Fowler (2004) sostiene que un alcance fijo «only works if the contractor truly understands the requirements, which is rare», y que algunos proveedores ofertan bajo para ganar con los cambios. El *Agile Contracts Primer* recomienda evitar los contratos de precio y alcance fijos porque tienden a que el cliente no reciba lo que necesita y el proveedor pierda plata o baje la calidad. Las dos posturas son de practicantes, sin estudios.

## Aceptar y cerrar

La aceptación es el momento en que el cliente dice que el trabajo está terminado, y conviene que dependa de criterios escritos al principio. Según los mismos resúmenes del PMBOK 6, *Validate Scope* obtiene la aceptación formal de los entregables y la separa del control de calidad: una cosa es que el trabajo esté bien hecho y otra que el cliente lo acepte. El *Agile Contracts Primer* resume las dos preguntas que el contrato tiene que contestar: «Is it done?» y «What to do if not done?». Lo ambiguo ahí es, según el Primer, «a possible source of conflict—and of litigation».

Si la entrega es por partes, la aceptación final es la suma de aceptaciones parciales. El Primer dice que así baja el riesgo de la garantía, porque cada parte ya se probó y se aceptó. La práctica de contratos que se encontró, de blogs legales del Reino Unido, separa los defectos menores (se anotan y se arreglan en la garantía sin trabar la aceptación ni el pago) de los que bloquean la entrega. Para una tienda online, cómo se separa la garantía del mantenimiento está en [abono de cuidado](../../Emprender/Modelo-de-negocio/abono-de-cuidado.md#cuándo-se-ofrece).

> [!NOTE]
> Sin fuente todavía: el contenido de *Close Project or Phase* del PMBOK, un modelo de acta de entrega para proyectos web chicos y la validez de una aceptación por correo o por silencio en Argentina.

## Formas de repartir el riesgo

Entre el precio cerrado puro y el tiempo y materiales hay formas intermedias. En 270 contratos de software de un banco internacional, Fink, Lichtenstein y Wyss (2013) encontraron precio fijo con tope a los cambios de especificación y tiempo y materiales con precio máximo. El precio fijo sin cambios aparecía cuando la incertidumbre era muy baja y la relación con el proveedor era nueva. Es un solo banco y contratos de hace más de veinte años.

| Forma | Qué se fija | Quién carga el sobrecosto (lectura de esta base) | De dónde sale la forma |
|---|---|---|---|
| Precio cerrado por fase | El precio de la fase siguiente, cotizada con lo aprendido en la anterior | El proveedor, fase por fase | Boag (2024) |
| Tiempo y materiales con tope | Un presupuesto máximo y a veces una fecha | El cliente hasta el tope; el proveedor por encima | Fink y otros (2013); Torchbox (2020) |
| Intercambio a igual esfuerzo | El tamaño total del alcance; lo nuevo reemplaza algo del mismo tamaño | El proveedor, sobre un alcance que no crece | *Agile Contracts Primer* |
| Salida anticipada pagada | El precio, con derecho del cliente a terminar antes | Compartido | Sutherland (2008) |

La última fila es el contrato «Money for nothing, change for free» de Sutherland (2008). El cliente puede terminar al final de cualquier iteración pagando el 20 % de lo que faltaba, y los cambios no se cobran mientras no crezca el alcance total. Kelly (2014) lo evalúa así: «Sounds good but… They haven't taken over the world».

Los pagos por hitos también reparten riesgo: en la lectura de esta base, achican lo que el proveedor tiene adelantado sin cobrar. La práctica de agencias pide adelantos del 25 % al 50 % y cobra el resto por hitos: aprobación del diseño, entrega en un entorno de prueba y lanzamiento. Son blogs, sin estudio. Cómo pesan esos hitos en la caja está en el [plan financiero mínimo](../../Emprender/Finanzas/plan-financiero-minimo.md).

## Cómo se pierde plata a precio cerrado

La lista junta lo que dicen las fuentes de arriba con lo que la base deduce de ellas:

- Cotizar antes de conocer el proyecto. La estimación inicial es un rango de hasta cuatro veces (McConnell); cotizar un número ahí es apostar.
- Dejar que la oferta tire la estimación para abajo. Es la mezcla de objetivos contra la que advierte Jørgensen.
- Calcular el riesgo con el promedio. El caso que hunde el margen es el de la cola (Flyvbjerg y Budzier).
- Aceptar cambios sin escribirlos. Sin línea base y sin pedido por escrito, el cambio se hace gratis.
- Aceptación sin criterios. El proyecto no termina nunca, y el último pago tampoco llega.

Para leer más, el *Agile Contracts Primer*, que es libre, tiene en su Part 3 el mapa de los tipos de contrato y qué hacer si igual se elige el precio y alcance fijos. Para el riesgo de ganar una cotización por optimismo, el texto de Jørgensen sobre cómo elegir proveedores, de doce páginas, sirve leído desde el lado del proveedor. Para estimar, el artículo de McConnell sobre el cono de incertidumbre, de ocho páginas.
