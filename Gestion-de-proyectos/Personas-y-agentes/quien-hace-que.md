---
resumen: >-
  En un trabajo con personas y agentes hay cuatro papeles por cada pieza: quien decide qué se hace, quien lo ejecuta, quien verifica que esté bien y quien responde por el resultado. Un agente puede ejecutar y verificar en parte; para esta base, responder queda en una persona con nombre.
estado: borrador
estabilidad: semi
fuentes:
  - "Tomašev, Franklin y Osindero (2026), Intelligent AI Delegation, arXiv 2602.11865, preprint sin revisión por pares (abstract y resumen de la primera mitad del HTML, secciones 4.8, 5.1 y 5.2): https://arxiv.org/abs/2602.11865 y https://arxiv.org/html/2602.11865"
  - "Mitchell, Ghosh, Luccioni y Pistilli (2025), Fully Autonomous AI Agents Should Not be Developed, arXiv 2502.02649 (abstract): https://arxiv.org/abs/2502.02649"
  - "Green (2022), The flaws of policies requiring human oversight of government algorithms, Computer Law & Security Review 45 (resumen): https://arxiv.org/abs/2109.05067"
  - "RACI, visión general (resumen): https://www.wikipedia.org/wiki/RACI_matrix"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [roles en la fábrica, matriz de responsabilidades, RACI, quién responde, accountability con agentes]
creado: 2026-11-27
revisado:
---

# Quién hace qué

En un trabajo con personas y agentes hay cuatro papeles por cada pieza: quien decide qué se hace, quien lo ejecuta, quien verifica que esté bien y quien responde por el resultado. Un agente puede ejecutar y verificar en parte; para esta base, responder queda en una persona con nombre.

## Los cuatro papeles y quién puede ocuparlos

| Papel | Qué hace | Puede ser un agente |
|---|---|---|
| Decidir | Fija qué se busca, qué entra y qué se descarta | Solo decisiones chicas y reversibles, dentro de lo que se le encargó |
| Ejecutar | Produce el trabajo | Sí, cuando la tarea cae dentro de su [frontera](frontera-irregular.md) |
| Verificar | Comprueba que lo producido cumple el criterio de terminado | En parte: pruebas automáticas, otro agente que revisa; la aceptación final, no |
| Responder | Da la cara por el resultado y paga las consecuencias de un error | No, por criterio de esta base |

Los papeles se separan aunque los ocupe la misma persona. Qué papel puede ocupar un agente, en la columna de la derecha, es criterio de esta base y no sale de una fuente. En un equipo chico, quien decide suele ser quien responde. Lo que la tabla evita es que nadie ocupe un papel: un agente ejecuta, otro agente revisa, y ninguna persona sabe que el resultado es suyo.

Que verificar no lo haga el mismo agente que ejecutó es una inferencia de esta base, por analogía con la regla de "hacer y revisar" de los [patrones de trabajo](patrones-de-trabajo.md). Un agente que da por terminada una tarea sin terminarla es una falla que se trata en [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md).

## Por qué responder queda en una persona

Que la rendición de cuentas quede en una persona es criterio de esta base. Ninguna fuente lo prueba, y la más cercana no lo dice así.

Tomašev, Franklin y Osindero (2026) proponen un marco de delegación entre personas y agentes. Según el abstract, delegar incluye "transfer of authority, responsibility, accountability, clear specifications regarding roles and boundaries". En el texto, la responsabilidad es transitiva: quien delega no puede "absolve themselves of accountability by blaming subcontractors" (sección 4.8). En cadenas largas de agentes advierten un "accountability vacuum" (sección 5.2) y proponen "liability firebreaks", topes de responsabilidad pactados antes. El paper no afirma que la responsabilidad deba terminar en una persona: propone mecanismos para que sea rastreable. Solo se leyó la primera mitad del texto, y es un preprint.

La base toma de ahí dos ideas. Si la responsabilidad es transitiva, la cadena termina en alguien que puede responder, y hoy un agente no puede pagar las consecuencias de un error. Y esa persona tiene que tener control real, no solo la firma.

## El riesgo de una persona que solo absorbe la culpa

Tomašev y colegas llaman "moral crumple zone" al caso de personas que "lack meaningful control over outcomes, yet are introduced in delegation chains merely to absorb liability" (sección 5.1). Es lo que pasa cuando se nombra a un responsable que no puede ver ni cambiar lo que hacen los agentes.

Green (2022) llega a algo parecido desde otro lado. Según un resumen, revisó 41 políticas que exigen supervisión humana de algoritmos de gobierno y concluye que "la gran mayoría de la investigación sugiere que las personas no pueden supervisar algoritmos de forma confiable". Esas políticas, dice, dan falsa seguridad y reducen la rendición de cuentas de quienes deciden. El contexto es distinto (algoritmos que deciden sobre personas), así que la transferencia es por analogía.

La consecuencia práctica para un proyecto: el nombre de quien responde va junto con su forma de controlar. Eso es un [nivel de autonomía](niveles-de-autonomia.md) que le deje intervenir, un [criterio de terminado](delegar-a-un-agente.md) que pueda comprobar y una carga de revisión que su [atención](la-atencion-humana-como-restriccion.md) aguante. Mitchell y colegas lo resumen del lado del riesgo: según su abstract, "risks to people increase with the autonomy of a system".

## Lo que aporta y lo que no una matriz RACI

La forma clásica de repartir papeles es la matriz RACI: quién hace (responsible), quién responde (accountable), a quién se consulta y a quién se informa. Ordena la conversación, pero no hay evidencia comparativa de que mejore resultados. Lo más cercano que se halló es una validación de diseño en una sola organización, sin grupo de comparación. Las críticas de practicantes dicen que la matriz se desactualiza. Las otras siglas de este tipo se cuentan en [derechos de decisión](../../Liderazgo-y-direccion/Decidir/derechos-de-decision.md).

Con agentes, una RACI agrega una columna por agente y deja la "A" siempre en una persona. Es una lectura de esta base. La rendición de cuentas a nivel de empresa, con sus límites, está en [rendición de cuentas](../../Liderazgo-y-direccion/Ejecucion/rendicion-de-cuentas.md); quién aprueba y con qué tolerancias en un proyecto, en [gobierno del proyecto](../Gobierno-y-cierre/gobierno-del-proyecto.md).

> [!NOTE] Sin fuente todavía: marcos de responsabilidad de IA (NIST AI RMF, ISO 42001, la supervisión humana del reglamento europeo de IA) aplicados a proyectos; no se consultaron.

Ver también: [Personas y agentes](personas-y-agentes.md).
