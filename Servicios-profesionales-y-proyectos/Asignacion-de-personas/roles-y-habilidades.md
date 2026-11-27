---
resumen: >-
  El rol es la categoría con que una firma de servicios pide, estima y cobra el trabajo (consultor, desarrollador, jefe de proyecto), y la habilidad, con su nivel, es lo que permite elegir qué persona con nombre lo cubre. Un proyecto se planifica primero con roles genéricos y después se baja a personas.
estado: vigente
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 5.2.2.1 «Define and manage skills taxonomy», 5.2.1.5 y 5.2.3.6 «Perform skill and capability testing»"
  - "Microsoft Learn, Project Operations, Resource management key concepts (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/resource-management-key-concepts"
  - "Microsoft Learn, Project Operations, Define roles y Define skills and proficiencies (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/define-roles"
  - "Microsoft Learn, Project Operations, Generic resource requirement fulfillment (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/generic-resource-requirement-fulfillment"
  - "Microsoft Learn, Project Operations, Sales price resolution (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/pricing-costing/sales-price-resolution-sales"
  - "ERPNext, Activity Type (como evidencia de práctica, leída en el sitio): https://docs.frappe.io/erpnext/user/manual/en/activity-type"
  - "SFIA Foundation, SFIA 9, Levels of responsibility (los siete niveles y sus atributos genéricos, leída en el sitio): https://sfia-online.org/en/sfia-9/responsibilities"
  - "SFIA Foundation, SFIA 9, skills «Resourcing» y «Workforce planning» (qué niveles define cada habilidad): https://sfia-online.org/en/sfia-9/skills/resourcing"
  - "Maister, D. (2004), The Anatomy of a Consulting Firm, capítulo 2 de The Advice Business (Pearson), leído en la página del autor: https://davidmaister.com/articles/4/2/index.html"
  - "Servicios-profesionales-y-proyectos/.investigacion/asignacion-y-horas.md (sección 1.3)"
  - "Servicios-profesionales-y-proyectos/.investigacion/verificacion-asignacion-y-horas.md"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 2)"
aliases: [rol, rol genérico, recurso genérico, generic resource, named resource, persona con nombre, habilidades, skills, taxonomía de habilidades, skills taxonomy, nivel de competencia, proficiency]
creado: 2026-11-27
revisado: 2026-11-27
---

# Roles y habilidades

El rol es la categoría con que una firma de servicios pide, estima y cobra el trabajo (consultor, desarrollador, jefe de proyecto), y la habilidad, con su nivel, es lo que permite elegir qué persona con nombre lo cubre. Un proyecto se planifica primero con roles genéricos y después se baja a personas.

Es la pieza de [asignación de personas](asignacion-de-personas.md) que da el vocabulario de los pedidos: una [reserva](reserva-de-personas.md) se pide por rol, y la [demanda](demanda-y-capacidad.md) se suma por rol para ver si alcanza la gente.

## Del rol genérico a la persona con nombre

Al vender un proyecto todavía no se sabe quién lo va a hacer. Por eso se estima con un recurso genérico (*generic resource*), que es un rol en una unidad de la firma: por ejemplo, un desarrollador senior de una oficina. Un sistema de gestión de servicios lo dice así: «Staff your project with a team of generic or named resources». El presupuesto del proyecto y la cotización se arman con genéricos, y el costo y la tarifa salen del rol.

Cuando el proyecto se confirma, cada genérico se cubre con una persona con nombre (*named resource*). Un mismo genérico puede cubrirse con varias personas: el ejemplo de ese sistema es un pedido de 120 horas de ingeniería en cinco días, que una sola persona no puede hacer. Si nadie lo cubre, el genérico queda en el equipo y el hueco se ve. El mismo sistema permite sustituir a una persona por otra.

Planificar por rol y bajar a persona después es práctica documentada de un sistema. Una fuente de la literatura de firmas de servicios la respalda en parte: Maister calcula cuánta gente necesita una consultora a partir de lo que cada proyecto pide de cada nivel (socio, medio, junior), no de quién lo va a hacer, y muestra que si la mezcla de niveles del trabajo no coincide con la de las personas, el costo cae en las dos direcciones (ver [demanda y capacidad](demanda-y-capacidad.md#de-los-proyectos-a-las-personas-por-nivel)). Que haya que planificar con genéricos antes de saber quién, porque la venta y la asignación ocurren en momentos distintos y el rol es lo único que se sabe en los dos, sigue siendo razonamiento de esta base.

## Qué guarda un rol

En la práctica leída, el rol agrupa a las personas para ponerles precio: sirve para «define their pricing based on their roles». Además puede llevar valores que pasan por defecto a cada persona que lo juega, como la [utilización](../Rentabilidad-de-la-firma/utilizacion.md) objetivo y el tipo de facturación, y las habilidades que se esperan.

El rol de un proyecto no es el puesto de la persona en la organización. Como criterio de esta base: el puesto es de la estructura y de la nómina, y cambia con un ascenso; el rol es lo que la persona hace en un proyecto, y alguien puede jugar dos roles en dos proyectos el mismo mes.

## Tarifa por rol o por persona

Los sistemas no coinciden en el eje del precio de la hora:

| Diseño | Cómo se resuelve la tarifa de una hora | Excepción |
|---|---|---|
| Por rol | Se busca la línea de la lista de precios por rol y unidad de la firma; si no hay, por rol solo | Por unidad o por otras dimensiones, en orden de prioridad |
| Por tipo de actividad | El tipo de actividad (diseño, desarrollo, reunión) trae costo y tarifa por defecto | Un costo por persona pisa el del tipo de actividad |

El primero precia por lo que la persona hace en el proyecto; el segundo, por la clase de tarea. Ninguna fuente leída dice cuál es más usual en las firmas. En los dos, el costo y la tarifa son datos separados: cómo se calcula el costo de la hora está en [costo y margen del proyecto](../Rentabilidad-de-la-firma/costo-y-margen-del-proyecto.md).

## Habilidades con nivel

APQC pone la taxonomía de habilidades dentro del plan de recursos (5.2.2.1 «Define and manage skills taxonomy») y le suma una prueba de habilidades (5.2.3.6 «Perform skill and capability testing»). Las une con la demanda en 5.2.1.5: «Determine availability of skills to deliver on current and forecast customer orders».

Un sistema guarda las habilidades con una escala configurable: un mínimo, un máximo y los niveles intermedios con nombre. Con eso compara la habilidad que pide el proyecto con la que tiene cada persona disponible, y filtra a los candidatos. La taxonomía es un dato maestro de la firma; si cada jefe de proyecto inventa sus nombres de habilidades, el filtro no encuentra a nadie (criterio de esta base).

Una firma no tiene que inventar la escala. SFIA, un marco público de habilidades nacido en tecnología pero que dice ser aplicable a otras profesiones del conocimiento, define siete niveles de responsabilidad iguales para todas sus habilidades: 1 Follow (seguir), 2 Assist (asistir), 3 Apply (aplicar), 4 Enable (habilitar), 5 Ensure, advise (asegurar, aconsejar), 6 Initiate, influence (iniciar, influir) y 7 Set strategy, inspire, mobilise (fijar la estrategia). Cada nivel se describe por atributos genéricos, como la autonomía y la influencia: el 3, por ejemplo, «performs varied tasks, sometimes complex and non-routine, using standard methods and procedures» y trabaja bajo dirección general. Cada habilidad se define solo en los niveles en que tiene sentido: «Resourcing» (conseguir y desplegar recursos) en los niveles 2 a 6 y «Workforce planning» en el 4 al 6. Es una escala de responsabilidad y no una prueba de dominio de una técnica; no dice quién fija el nivel de una persona (queda abierto, abajo).

Quién evalúa el nivel de una persona, y cómo, es de [evaluación del desempeño](../../Liderazgo-y-direccion/Gestion-de-personas/evaluacion-del-desempeno.md); cómo se sube, de [desarrollo de personas](../../Liderazgo-y-direccion/Gestion-de-personas/desarrollo-de-personas.md).

> [!NOTE]
> Sin fuente todavía: cuántas habilidades conviene registrar, cada cuánto se actualizan y si el nivel lo declara la persona o lo fija un tercero. Las fuentes leídas (APQC, SFIA y la documentación de dos sistemas) describen el registro y la escala, no la práctica ni quién evalúa el nivel.
