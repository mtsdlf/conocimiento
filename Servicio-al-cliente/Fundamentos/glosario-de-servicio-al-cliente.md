---
resumen: >-
  Los términos del tema Servicio al cliente, cada uno con su nombre en inglés, una definición corta y la nota donde vive, y las palabras que el campo usa con más de un sentido.
estado: borrador
estabilidad: estable
fuentes:
  - "ISO 10002:2018, vista previa del editor (definiciones 3.2 y 3.4), leída: https://cdn.standards.iteh.ai/samples/71580/6db527fdda0a42ac8f597ffd406e3509/ISO-10002-2018.pdf"
  - "Gans, Koole y Mandelbaum (2003), M&SOM 5(2), 79-141, §2.3, §3 y §4 leídos: https://aviman.technion.ac.il/files/References/Gans-Koole-Mandelbaum-CCReview.pdf"
  - "Glosario de ITIL 4, según resúmenes de terceros: https://www.manageengine.com/products/service-desk/itsm/itil-4-glossary-terms.html y https://blog.invgate.com/problem-management-in-an-itil-4-world"
  - "BMC, definición de acuerdo de nivel de servicio citando ITIL 4, según el resumen del buscador: https://www.bmc.com/blogs/ola/"
  - "Gobierno de Ontario, GO-ITS 37, escalamiento funcional, según el resumen del buscador: https://www.ontario.ca/document/go-its-37-enterprise-incident-management-process"
  - "Consortium for Service Innovation, KCS v6, «The Solve Loop», leída la página: https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/030"
  - "Dixon, Freeman y Toman (2010), Harvard Business Review, julio-agosto, 116-122, leído entero: https://beyondphilosophy.com/wp-content/uploads/2013/07/Stop-Trying-to-delight.pdf"
  - "Rae, «Watertight not watermelon service level agreements», HDI SupportWorld, 2020, leído en parte: https://www.thinkhdi.com/library/supportworld/2020/watertight-not-watermelon-service-level-agreements"
  - "Servicio-al-cliente/.investigacion/ (fundamentos-y-contraria.md sección 5, caso-y-escalamiento.md, canales-y-niveles-de-servicio.md, calidad-del-servicio.md)"
aliases: [glosario de atención al cliente, customer service glossary, términos de servicio al cliente, vocabulario de mesa de ayuda]
creado: 2026-11-27
revisado:
---

# Glosario de servicio al cliente

Los términos del tema Servicio al cliente, cada uno con su nombre en inglés, una definición corta y la nota donde vive, y las palabras que el campo usa con más de un sentido.

No hay un glosario canónico y abierto del campo: el de ITIL es pago y se leyó por resúmenes, y la norma ISO 10002 se leyó solo en su vista previa. Estas son las palabras que usa esta base, en un sentido cada una. Las marcadas con † tienen más de un sentido en el campo y se explican al final. Los tipos de caso (consulta, pedido, incidente) y sus estados son lectura de esta base sobre prácticas de productos: ninguna norma los fija.

## El caso y su recorrido

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Contacto | Contact, interaction | Cada vez que el cliente escribe, llama o se presenta; varios contactos pueden ser un mismo caso | [canales de atención](../Canales-de-atencion/canales-de-atencion.md) |
| Caso † | Case, ticket, issue | El registro de lo que pidió el cliente, con sus datos, su estado y su dueño, desde que entra hasta que se cierra | [caso](../Caso/caso.md) |
| Consulta | Inquiry | Un caso en que el cliente pregunta algo | [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md) |
| Pedido de servicio | Service request | Un caso en que el cliente pide algo previsto (un cambio de datos, un acceso, un duplicado) | [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md) |
| Incidente † | Incident | En ITIL, una interrupción o baja de calidad de un servicio; en este tema, un tipo de caso | [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md) |
| Reclamo, queja † | Complaint | Según ISO 10002, una expresión de insatisfacción con un producto, un servicio o el propio tratamiento de reclamos, cuando se espera una respuesta o una solución | [reclamo](../Caso/reclamo.md) |
| Acuse de recibo | Acknowledgement | El aviso al cliente de que su reclamo entró; es un paso de la cláusula 7 de ISO 10002 | [reclamo](../Caso/reclamo.md) |
| Impacto, urgencia, prioridad | Impact, urgency, priority | La prioridad sale de cruzar cuánto afecta (impacto) con cuánto apura (urgencia), según el estándar de Ontario y BMC por resúmenes; la tabla la fija cada organización | [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md) |
| Triage | Triage | La primera mirada que clasifica y prioriza un caso; no se encontró una definición con fuente | [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md) |
| Resuelto | Resolved | Quien atiende cree que el caso está resuelto y el cliente todavía no lo confirmó | [caso](../Caso/caso.md) |
| Cerrado | Closed | El cliente confirmó, o pasó el plazo sin que contestara | [caso](../Caso/caso.md) |
| Reapertura | Reopen | El caso cerrado vuelve a abrirse porque el cliente dice que no se resolvió | [caso](../Caso/caso.md) |
| Garantía | Warranty | El compromiso de reparar, cambiar o devolver un producto que falla dentro de un plazo; lo legal está en la nota de la Argentina | [garantía y reparación](../Caso/garantia-y-reparacion.md) |
| Autorización de devolución | Return merchandise authorization (RMA) | La aprobación formal para que el cliente devuelva un producto a reparar, cambiar o reintegrar | [garantía y reparación](../Caso/garantia-y-reparacion.md) |

## El escalamiento

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Escalar, escalamiento † | Escalate, escalation | Pasar un caso a quien sabe más (funcional) o a quien puede decidir más (jerárquico) | [escalamiento](../Escalamiento/escalamiento.md) |
| Primer, segundo y tercer nivel † | Tier 1, 2, 3 (L1, L2, L3) | Las capas del soporte por especialidad: el primer nivel recibe, los siguientes saben más; algunos llaman nivel 0 al autoservicio. La definición de cada nivel es práctica común, sin fuente neutral | [niveles de soporte](../Escalamiento/niveles-de-soporte.md) |
| Enjambre | Swarming, Intelligent Swarming | Organizar el soporte sin niveles fijos: quien puede ayudar se suma al caso; *Intelligent Swarming* es marca del Consortium for Service Innovation | [niveles de soporte](../Escalamiento/niveles-de-soporte.md) |
| Derivar al técnico | Dispatch, field service request | Decidir desde el caso que hace falta una visita y pasar los datos al servicio de campo, que es de otro tema | [derivación al técnico](../Escalamiento/derivacion-al-tecnico.md) |
| Problema † | Problem | En ITIL, «a cause, or potential cause, of one or more incidents»: la causa detrás de casos repetidos | [problema y causa raíz](../Escalamiento/problema-y-causa-raiz.md) |
| Error conocido | Known error | Un problema analizado y todavía no resuelto; las redacciones de ITIL que circulan discrepan en si exige causa y solución provisoria documentadas | [problema y causa raíz](../Escalamiento/problema-y-causa-raiz.md) |
| Solución provisoria | Workaround | Lo que reduce el impacto de un problema sin eliminar su causa | [problema y causa raíz](../Escalamiento/problema-y-causa-raiz.md) |

## Los tiempos y los acuerdos

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Acuerdo de nivel de servicio † | Service level agreement (SLA) | Según ITIL 4, vía terceros, un acuerdo documentado entre quien presta el servicio y el cliente que fija los servicios y el nivel esperado | [niveles de servicio](../Niveles-de-servicio/niveles-de-servicio.md) |
| Acuerdo de nivel operativo | Operational level agreement (OLA) | El acuerdo entre equipos de la misma organización que sostiene el que se le da al cliente; ITIL 4 puede haber dejado de nombrarlo | [acuerdos internos](../Niveles-de-servicio/acuerdos-internos.md) |
| Contrato de respaldo | Underpinning contract (UC) | El contrato con un proveedor externo que sostiene el acuerdo con el cliente | [acuerdos internos](../Niveles-de-servicio/acuerdos-internos.md) |
| Tiempo de primera respuesta | First response time | Lo que tarda el cliente en recibir la primera respuesta a su caso | [tiempos de respuesta y resolución](../Niveles-de-servicio/tiempos-de-respuesta-y-resolucion.md) |
| Tiempo de resolución | Resolution time | Lo que tarda el caso en resolverse, contado en el reloj del acuerdo (horario hábil, feriados, pausas) | [tiempos de respuesta y resolución](../Niveles-de-servicio/tiempos-de-respuesta-y-resolucion.md) |
| Horario hábil | Business hours, support hours | Las franjas en que corre el reloj del acuerdo | [tiempos de respuesta y resolución](../Niveles-de-servicio/tiempos-de-respuesta-y-resolucion.md) |
| Pausa | On hold, SLA pause | El estado en que el reloj se detiene, por ejemplo mientras se espera al cliente | [tiempos de respuesta y resolución](../Niveles-de-servicio/tiempos-de-respuesta-y-resolucion.md) |
| Incumplimiento | SLA breach | Pasar el tiempo prometido sin responder o sin resolver | [incumplimiento del acuerdo](../Niveles-de-servicio/incumplimiento-del-acuerdo.md) |
| Acuerdo sandía | Watermelon SLA | El acuerdo que da verde en el reporte mientras la experiencia del cliente es roja; imagen difundida por Barclay Rae (HDI) | [incumplimiento del acuerdo](../Niveles-de-servicio/incumplimiento-del-acuerdo.md) |

## Los canales y el centro de contacto

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Centro de contacto | Contact centre, customer contact centre (CCC) | El centro de llamadas al que se suman correo, chat y otros canales; ISO 18295-1 usa el término inglés | [canales de atención](../Canales-de-atencion/canales-de-atencion.md) |
| Omnicanal | Omnichannel | Un solo caso con una sola historia aunque el cliente cambie de canal; frente a multicanal, canales en paralelo sin historia común. Definición de práctica, sin norma | [canales de atención](../Canales-de-atencion/canales-de-atencion.md) |
| Autoservicio | Self-service | Lo que el cliente resuelve sin una persona: base de conocimiento, preguntas frecuentes, portal, bots, menú de voz | [autoservicio](../Canales-de-atencion/autoservicio.md) |
| Base de conocimiento | Knowledge base | Los artículos que usan quienes atienden y, publicados, los clientes | [autoservicio](../Canales-de-atencion/autoservicio.md) |
| KCS | Knowledge-Centered Service | Práctica del Consortium for Service Innovation que escribe y mejora los artículos mientras se atienden los casos | [autoservicio](../Canales-de-atencion/autoservicio.md) |
| Desvío | Deflection | El contacto que no llega a una persona porque el cliente se resolvió solo; se suele contar de más | [autoservicio](../Canales-de-atencion/autoservicio.md) |
| Nivel de servicio del centro de contacto † | Service level, telephone service factor (TSF) | Según Gans y otros, la fracción de llamadas que esperan menos que un objetivo, «typically» 20 o 30 segundos; el «80/20» es convención de práctica | [dimensionamiento del equipo](../Canales-de-atencion/dimensionamiento-del-equipo.md) |
| Velocidad media de respuesta | Average speed of answer (ASA) | Lo que esperan las llamadas antes de ser atendidas; no cuenta a las abandonadas, así que se mira junto con el abandono | [dimensionamiento del equipo](../Canales-de-atencion/dimensionamiento-del-equipo.md) |
| Abandono | Abandonment | El cliente que corta o se va antes de que lo atiendan | [dimensionamiento del equipo](../Canales-de-atencion/dimensionamiento-del-equipo.md) |
| Ocupación | Occupancy | El tiempo atendiendo sobre el tiempo disponible | [dimensionamiento del equipo](../Canales-de-atencion/dimensionamiento-del-equipo.md) |
| Erlang C, Erlang A | Erlang C, Erlang A | Modelos de colas para calcular cuántas personas hacen falta; el C ignora el abandono y el A lo incluye | [dimensionamiento del equipo](../Canales-de-atencion/dimensionamiento-del-equipo.md) |

## Las métricas y las encuestas

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Resolución al primer contacto | First contact resolution (FCR) | La fracción de casos resueltos sin que el cliente vuelva; depende de qué se cuenta como el mismo problema y en qué plazo | [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md) |
| Tiempo medio de atención | Average handle time (AHT) | El tiempo de conversación más el trabajo posterior de cada contacto; no es el tiempo de resolución del caso | [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md) |
| Pendientes † | Backlog | Los casos abiertos sin resolver en un momento | [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md) |
| Satisfacción | Customer satisfaction (CSAT) | La pregunta al cliente, después de un caso, por cuán conforme quedó | [encuestas de satisfacción](../Calidad-del-servicio/encuestas-de-satisfaccion.md) |
| Esfuerzo del cliente | Customer effort score (CES) | La pregunta por cuánto le costó resolver; Dixon y otros la propusieron con una escala de 1 a 5, donde 5 es esfuerzo muy alto, y se dice que versiones posteriores cambiaron la escala (sin verificar) | [encuestas de satisfacción](../Calidad-del-servicio/encuestas-de-satisfaccion.md) |
| Recomendación | Net Promoter Score (NPS) | La pregunta por cuán probable es que recomiende; su valor como predictor se discute en [boca a boca y referidos](../../Marketing/Canales/boca-a-boca-y-referidos.md#cómo-se-mide-y-qué-pasa-con-el-nps) | [encuestas de satisfacción](../Calidad-del-servicio/encuestas-de-satisfaccion.md) |
| Monitoreo de calidad | Quality assurance, quality monitoring | Evaluar conversaciones con una pauta | [monitoreo de calidad](../Calidad-del-servicio/monitoreo-de-calidad.md) |
| Calibración | Calibration | Que varios evaluadores puntúen las mismas conversaciones para alinear criterios | [monitoreo de calidad](../Calidad-del-servicio/monitoreo-de-calidad.md) |

## Las palabras con más de un sentido

- **Nivel** tiene tres sentidos. El *nivel de soporte* (primer, segundo, tercer nivel) dice quién atiende. El *nivel de servicio del centro de contacto* es el porcentaje de contactos atendidos dentro de un tiempo, como el 80 % en 20 segundos. El *acuerdo de nivel de servicio* es lo que se le promete al cliente. Un centro puede cumplir su 80/20 y no cumplir el acuerdo, y al revés. El tema dice siempre la forma larga.
- **Caso, ticket, incidencia, incidente.** «Caso» es habitual en los CRM, «ticket» en las mesas de ayuda e *issue* en el seguimiento de trabajo: casi lo mismo con tres nombres. El incidente de ITIL es más estrecho, porque es la interrupción de un servicio. El tema dice «caso» para el registro e «incidente» solo como tipo de caso. En APQC, «incident» también es lo que se informa a un regulador (6.2.5), que queda fuera del tema.
- **Problema.** En el habla común es cualquier dificultad; en ITIL es la causa de uno o más incidentes. El tema lo usa solo en el segundo sentido y dice «lo que pide el cliente» para el primero.
- **Backlog.** En atención son los casos abiertos; en desarrollo de software, la lista de trabajo por hacer. El tema dice «pendientes».
- **Escalamiento** junta dos movimientos: el funcional, hacia quien sabe más, y el jerárquico, hacia quien puede decidir más. Lectura de esta base: un sistema los modela distinto, porque el primero cambia el equipo asignado y el segundo avisa a un responsable. En una práctica de producto, además, cambiar la prioridad de un caso lo escala respecto del acuerdo, que debe definir a qué prioridades aplica.
- **Reclamo y queja** se usan como sinónimos en castellano, y este tema hace lo mismo con la definición de ISO 10002. En el derecho del consumidor argentino tienen consecuencias propias, que están en [Servicio al cliente en la Argentina](../servicio-al-cliente-en-argentina.md). La ausencia de reclamos tampoco es satisfacción: la misma norma dice que «their absence does not necessarily imply high customer satisfaction».

Las razones del vocabulario elegido y las divisiones del campo están en [Fundamentos](fundamentos-de-servicio-al-cliente.md).
