# Investigación: verticales Caso y Escalamiento

Fecha de lectura: 2026-11-27. Capa cruda del tema Servicio al cliente. Marcas: [L] leído el texto completo (o la parte accesible), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).

Aviso general: ITIL 4 y KCS/swarming se leen casi todo de segunda mano o de páginas del propio Consorcio. Las guías de ITIL son pagas y no se leyeron. Donde digo "[S]" la afirmación no está verificada en el texto primario.

## Tabla de fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1 | ISO 10002:2018, vista previa (12 págs.: portada, índice, introducción, alcance, definiciones, principios 4.1-4.15) | https://cdn.standards.iteh.ai/samples/71580/6db527fdda0a42ac8f597ffd406e3509/ISO-10002-2018.pdf | primaria (muestra del editor iTeh) | 3/2/1/3 | [L] de lo que trae la muestra; no incluye los pasos 7.x, solo su índice |
| 2 | Ficha ISO 10002 (resumen del buscador sobre alcance y estado) | https://www.iso.org/standard/71580.html | primaria (ficha) | 3/1/1/2 | [S] (la OBP dio 403) |
| 3 | Consortium for Service Innovation, «Intelligent Swarming 101» | https://www.serviceinnovation.org/intelligent-swarming-101/ | primaria (del autor del modelo, parte interesada) | 2/2/1/3 | [L] |
| 4 | Consortium, Practices Guide, introducción | https://library.serviceinnovation.org/Intelligent_Swarming/Practices_Guide | primaria | 2/1/1/3 | [L] (solo índice y presentación) |
| 5 | Consortium, caso Akamai (2022) | https://library.serviceinnovation.org/Case_Studies/Intelligent_Swarming_Case_Studies/05_2022_Akamai | primaria, autoinformada | 1/2/3/2 | [L] |
| 6 | Consortium, casos Ping Identity (2024), Autodesk (2018), Cisco (2013) | https://library.serviceinnovation.org/Case_Studies/Intelligent_Swarming_Case_Studies | primaria, autoinformada | 1/1/2/1 | [S] (solo los resúmenes del buscador) |
| 7 | PagerDuty y Salesforce, «what is case swarming» | https://www.salesforce.com/blog/what-is-case-swarming/ | secundaria, comercial | 1/1/1/1 | [S]; cuentan como una sola familia con la 3 |
| 8 | Gobierno de Ontario, GO-ITS 37 (gestión de incidentes) | https://www.ontario.ca/document/go-its-37-enterprise-incident-management-process | primaria de un adoptante de ITIL | 2/3/2/2 | [S] (403 al leer; solo citas del buscador) |
| 9 | Gobierno de Ontario, GO-ITS 38 (gestión de problemas) | https://www.ontario.ca/document/go-its-38-enterprise-problem-management-process | ídem | 2/3/2/2 | [S] (403; solo aparece en resultados) |
| 10 | Atlassian y BMC sobre problema, error conocido, solución provisoria | https://www.atlassian.com/itsm/problem-management/process , https://dev.blogs.bmc.com/itil-problem-management/ | secundaria, comercial | 1/2/1/1 | [S] |
| 11 | Wikipedia y glosarios sobre problema y error conocido (citan ITIL 4) | https://en.wikipedia.org/wiki/Known_error | secundaria | 1/1/1/1 | [S] |
| 12 | BMC, matriz impacto-urgencia | https://blogs.bmc.com/impact-urgency-priority | secundaria, comercial | 1/2/1/1 | [S] (404 al leer; solo extracto del buscador) |
| 13 | Shopify, Lenovo, Lightspeed sobre RMA | https://www.shopify.com/blog/return-merchandise-authorization | secundaria, comercial | 1/2/2/1 | [S] |
| 14 | ERPNext (Frappe), Issue | https://docs.frappe.io/erpnext/user/manual/en/support/issue | documentación de producto | 2/3/3/2 | [L] |
| 15 | ERPNext, Warranty Claim | https://docs.frappe.io/erpnext/user/manual/en/warranty-claim | ídem | 2/2/3/2 | [L] |
| 16 | ERPNext, Maintenance Visit | https://docs.frappe.io/erpnext/user/manual/en/maintenance-visit | ídem | 2/2/3/2 | [L] |
| 17 | Odoo, Helpdesk (etapas, fusión) | https://www.odoo.com/documentation/18.0/applications/services/helpdesk.html | ídem | 2/2/3/2 | [L] |
| 18 | Odoo, servicios posventa del Helpdesk | https://www.odoo.com/documentation/18.0/applications/services/helpdesk/advanced/after_sales.html | ídem | 2/2/3/2 | [L] (hasta el carácter 100000 de 102736) |
| 19 | Odoo, Field Service, creación de tareas | https://www.odoo.com/documentation/18.0/applications/services/field_service/creating_tasks.html | ídem | 2/1/2/1 | [L] |
| 20 | ServiceNow, recorrido de un caso RMA | https://www.servicenow.com/docs/r/order-management/rma-case-user-journey.html | ídem | 2/3/3/2 | [L] |

Las fuentes 14 a 20 son evidencia de que la práctica existe; en las notas no se nombran productos.

## 1. El caso como registro

Qué es: lo que el campo llama ticket, caso o issue. No hay norma que lo defina como objeto de datos; sale de la práctica.

- Un "Issue" es "an incoming query from a Customer", normalmente por correo o por la web, creado solo o a mano. Fuente 14.
- Estados en una práctica: Open (sin respuesta; si el cliente responde vuelve a Open), Replied, Hold (pausado), Resolved (el equipo cree que está resuelto, el cliente no confirmó) y Closed (el cliente confirmó). Se cierra a mano o solo si el cliente no responde en 7 días. Fuente 14.
- Datos que esa práctica guarda: asunto, quién lo planteó, descripción, cliente (se vincula solo si el remitente coincide con uno guardado), prioridad (Low, Medium, High por defecto), tipo, apertura, tiempo hasta la primera respuesta, fecha y detalle de resolución, tiempo de resolución. Fuente 14.
- Separa el tiempo de resolución total del "User Resolution Time", que excluye la espera del cliente, y reinicia las métricas si el caso se reabre o se divide. Fuente 14.
- Asignación manual o por regla; comentarios internos visibles solo para el equipo; el número del caso va en el asunto de los correos para que las respuestas caigan en el mismo hilo. Fuente 14.
- Fusión de duplicados: otra práctica permite combinar tickets duplicados mostrando un puntaje de similitud antes de confirmar; la asignación automática puede balancear por cantidad total o por abiertos y salta a quien está de licencia. Fuente 17.
- Las etapas son por equipo y configurables ("each team has its own pipeline, organized into customizable stages"). Fuente 17. Los estados no son universales; lo universal es la distinción entre abierto, en espera, resuelto (propuesto) y cerrado (confirmado). Esto último es lectura mía de 14 y 17.
- Un caso de garantía se vincula al producto por número de serie: de ahí salen artículo, descripción y datos de garantía. Fuente 15.

Hueco: no hay norma ni fuente neutral sobre reglas de reapertura (cuánto tiempo puede reabrirse un caso cerrado, cuándo abrir uno nuevo vinculado).

Recurso canónico: no hay uno único. Para el modelo de datos, la página de Issue de ERPNext (14), la más completa que se pudo leer. Para el ciclo de vida normado, ISO 10002 cláusulas 7.2 a 7.9 (solo en el índice de la muestra; texto pago).

## 2. Clasificación y prioridad

- La lista cerrada consulta / pedido de servicio / incidente / reclamo no tiene fuente primaria leída. La práctica de producto usa un "Issue Type" configurable (ejemplos: Functional, Technical, Hardware). Fuente 14. No pude leer la guía ITIL 4 para confirmar la distinción incidente vs pedido de servicio.
- Prioridad = impacto × urgencia. Según el estándar de Ontario, "The priority of an incident is primarily determined by the impact on the business and the urgency with which a resolution or work-around is needed". Fuente 8 [S]. BMC: prioridad es "the intersection of impact and urgency"; una matriz de cinco por cinco niveles permite más fineza. Fuente 12 [S]. Los valores de cada celda varían por organización; no hay tabla universal.
- Cambiar la prioridad de un caso, en una práctica de producto, lo escala respecto del SLA: el acuerdo debe definir a qué prioridades aplica. Fuente 14.
- Triage como actividad propia: no encontré fuente que lo defina. Hueco.

Recurso canónico: la guía de gestión de incidentes de Ontario (8), por su detalle de prioridades y niveles. Fijarse en categorización y prioridad. No pude leerla (403).

## 3. Reclamo (ISO 10002)

Todo de la fuente 1 [L], salvo lo marcado.

- Definición 3.2: complaint es "expression of dissatisfaction made to an organization, related to its product or service, or the complaints-handling process itself, where a response or resolution is explicitly or implicitly expected". Nota 2: puede hacerse "directly or indirectly to the organization".
- La diferencia con consulta y pedido está en esa definición: lo que hace reclamo a un contacto es la insatisfacción expresada con respuesta esperada. La norma no define "consulta" ni "pedido"; la distinción es inferencia mía.
- Alcance (1): guía para el proceso de tratamiento de quejas sobre productos y servicios dentro de una organización, de cualquier tipo o tamaño; el Anexo B es para pequeños negocios. Excluye "disputes referred for resolution outside the organization or for employment-related disputes".
- Principios (4.2 a 4.15): compromiso, capacidad, transparencia, accesibilidad, capacidad de respuesta, objetividad, cargos ("Access to the complaints-handling process should be free of charge to the complainant"), integridad de la información, confidencialidad, enfoque centrado en el cliente, responsabilidad, mejora, competencia, oportunidad ("as expeditiously as feasible given the nature of the complaint and of the process used").
- Pasos de operación (cláusula 7), solo títulos del índice: comunicación, recepción, seguimiento, acuse, evaluación inicial, investigación, respuesta, comunicación de la decisión, cierre. Luego mantenimiento y mejora (8): recolección de información, análisis y evaluación, satisfacción con el proceso, monitoreo, auditoría, revisión por la dirección, mejora continua. No se pudo leer el texto de los pasos.
- Anexos informativos: formulario del reclamante (C), seguimiento (F), respuestas (G), flujograma de escalamiento (H).
- 3.4 nota 2: "Complaints are a common indicator of low customer satisfaction but their absence does not necessarily imply high customer satisfaction". Sirve para el mito "sin reclamos hay satisfacción".
- Familia: ISO 10001 (códigos de conducta), 10003 (disputas fuera de la organización, cuando no se resolvió adentro), 10004 (medición de satisfacción). 10002 es compatible con 9001 y 9004 y puede usarse sola (0.2 y 0.3).
- La edición vigente es la tercera, julio de 2018, confirmada en 2023 [S]. Fuente 2.
- El reclamo alimenta la mejora: "enhance the ability of the organization to identify trends and eliminate causes of complaints" (0.1). Es el puente con problema y causa raíz.

Recurso canónico: ISO 10002:2018. Leer introducción, 3.2, cláusula 4 y el flujograma del Anexo E (no accesible en la muestra). Para citar el texto completo hay que comprar la norma o usar la plataforma OBP.

## 4. Garantía y reparación

Dinero y ley: la garantía legal es de alto riesgo y va en la nota argentina aparte. Acá solo el proceso.

- RMA: "a business's formal approval for the repair, replacement, or refund of a product under warranty" (Shopify). Fuente 13 [S]. Otros nombres: RGA, y en logística "return material authorization".
- Pasos típicos: fijar política; el cliente pide y la empresa verifica contra la política y emite un número de autorización; el cliente envía; se inspecciona, y de la inspección sale reembolso, cambio, reemplazo o servicio de garantía. Fuente 13 [S]. Son sitios comerciales que describen el mismo esquema: una sola fuente en la práctica.
- Fuera de garantía el RMA puede no aplicar, aunque soporte puede ofrecer reparación. Fuente 13 [S].
- Cómo se ve en un sistema: un caso RMA con estados Draft, Work In Progress, Resolved y Closed; líneas con los productos defectuosos tomados de lo instalado; código de motivo y resolución esperada por línea; revisión de garantía y derecho por línea; aceptar o rechazar (si rechaza, avisa y cierra); propuesta de solución; tarea a un especialista si hace falta. Fuente 20 [L]. La página no describe vínculo con orden de devolución ni con reemplazo.
- Otra práctica: el reclamo de garantía se abre con cliente y número de serie; trae artículo y datos de garantía; estados Open, Work In Progress, Closed ("The repairs have been done") y Cancelled ("The Warranty Claim was invalid"); y "If a Customer visit is required to address the issue, you can create a new Maintenance Visit record from this". Fuente 15 [L].
- Desde el caso de la mesa de ayuda se puede disparar: reembolso (nota de crédito; requiere factura posteada), cupón, devolución (transferencia inversa, con opción de cambio que genera entrega; el botón aparece solo si hay entrega registrada), reparación (orden de reparación, opcionalmente en garantía, lo que deja el precio en cero) y servicio de campo (tarea in situ). Fuente 18 [L].
- Frontera: la logística física de la devolución es de Comercio-electronico/Operaciones-del-comercio/devoluciones.md; el reembolso es de finanzas; la reparación en taller y la visita son de Activos y mantenimiento. Lo propio del servicio es la decisión (autorizar, rechazar, qué resolución) y el registro que lo une todo. Esto último es lectura mía de 18 y 20.

Recurso canónico: Warranty Claim de ERPNext (15) por campos y estados; el recorrido RMA de ServiceNow (20) por mostrar la revisión de derecho y el aceptar o rechazar. Hueco: no hay fuente neutral (norma o libro) sobre el proceso de garantía.

## 5. Escalamiento funcional y jerárquico

Todo [S], fuente 8 (el estándar de Ontario y un resumen de ITIL), salvo lo marcado.

- Funcional: "the SDA assigns the incident to a group with more specialized skills. (This is known as functional escalation)".
- Jerárquico: "hierarchical escalation engages appropriate levels of management" (resumen de ITIL de Flevy, no el texto ITIL).
- Cada nivel puede tener un tiempo asignado, pasado el cual se escala funcionalmente: "Each support tier may be allocated a certain amount of time to resolve the incident".
- En una práctica de producto, escalar es cambiar la prioridad, que cambia el SLA aplicado. Fuente 14 [L].
- ISO 10002 trae un flujograma de escalamiento (Anexo H). Fuente 1, solo el índice.

Hueco: no hallé el texto ITIL 4 que define los dos tipos; las definiciones salen de adoptantes. Marcarlas "según la práctica de ITIL".

## 6. Niveles de soporte y swarming

Modelo por niveles: el Consorcio lo describe, desde su lado, como "static, linear, hierarchy-based model" basado en escalamiento. Fuente 3 [L]. No encontré fuente neutral que defina nivel 0, 1, 2 y 3 (el 0 sería el autoservicio); la definición de cada nivel es práctica común sin fuente y debe marcarse así.

Swarming:
- Intelligent Swarming es un modelo desarrollado por miembros del Consorcio, "dynamic, fluid, adaptive organization based on an unbounded network", con interacciones "emergent based on the work to be accomplished". Fuente 3 [L]. Es marca de servicio del Consorcio. Fuente 7 [S].
- Críticas a los niveles (del Consorcio, no independientes): procesos de escalamiento lineales que "treat every issue the same"; equipos que optimizan su silo "almost always to the detriment of the customer"; "rework, inefficiency, and frustration". Fuente 3 [L].
- No es solo para lo difícil: "difficult is in the eye of the beholder"; y hacen falta límites para que "the work is getting done". Fuente 3 [L]. Un resumen dice que rinde más con problemas nuevos y complejos y que no sirve en todos los entornos. Fuente 6 [S].
- La guía se organiza en Connect (perfiles de personas y de trabajo, modelo de clasificación), Collaborate y Recognize (reputación). Fuente 4 [L]. Akamai ya usaba KCS desde 2017. Fuente 5 [L].
- Visión equilibrada (PagerDuty): los niveles "can be highly effective for handling less severe issues and one-off questions". Fuente 7 [S], comercial.

Evidencia (toda autoinformada; ninguna independiente ni con control de complejidad):
- Akamai, a menos de dos trimestres: 20 % menos de nivel de esfuerzo en casos swarmed frente a escalados a nivel 2; 7 % de reducción de transiciones a Ingeniería de Producto; 68 % dice aprender de los posts; 75 % mira para ofrecer ayuda; respuesta promedio a un pedido de ayuda 16 minutos frente a casi 2 horas de aceptación de un pedido de escalamiento. Fuente 5 [L]. Límites: sin tamaños de muestra, "esfuerzo" sin definir, y se comparan dos medidas distintas.
- Ping Identity, primeras 10 semanas: tiempo medio de cierre -15 %, cumplimiento de SLA +13 %, backlog -25 %, primera respuesta -75 %, resolución de los casos más complejos -81 %. Fuente 6 [S] (texto primario no leído).
- Para los niveles no hay estudio a favor; su respaldo es la ubicuidad y la afirmación de PagerDuty (7). Hueco: ningún estudio académico que compare ambos modelos.

Para la nota: niveles como modelo por defecto; swarming como alternativa con evidencia de casos de empresas de tecnología, no concluyente, para soporte de producto complejo.

Recurso canónico: Swarming 101 (3) para la definición, y el caso Akamai (5) para ver evidencia con sus límites. Fijarse en que los números son de dos trimestres y sin control.

## 7. Derivación al técnico

- Desde un reclamo de garantía se crea una visita de mantenimiento "if a Customer visit is required". Fuente 15 [L].
- La visita registra: fecha y hora, cliente, tipo (Scheduled, Unscheduled, Breakdown), estado de finalización (Partially o Fully Completed), artículo y serie, descripción, trabajo hecho, opinión del cliente (opcional). Del cliente toma dirección, contacto, territorio y grupo. Fuente 16 [L]. La página no describe qué se copia del reclamo a la visita ni vincula la visita con el reclamo.
- En otra práctica, desde el ticket se agenda una tarea de servicio de campo y el cliente con portal sigue el avance. Fuente 18 [L]. Cómo se guarda el vínculo no está en la página. Fuente 19 [L].
- Lo mínimo que la evidencia sugiere que pasa: cliente, producto y serie, descripción del problema, dirección y contacto. Es inferencia de 15, 16 y 18, no norma.

Frontera: orden de trabajo, repuestos y agenda son de Activos y mantenimiento. Hueco: ninguna fuente primaria sobre qué datos debe traer una derivación ni cuándo un caso pide visita.

Recurso canónico: ERPNext, Warranty Claim y Maintenance Visit leídas juntas (15 y 16).

## 8. Problema y causa raíz

Todo [S].

- ITIL 4: un problema es "A cause, or potential cause, of one or more incidents". Fuentes 10 y 11 (citas de segundas fuentes, no el glosario oficial).
- Error conocido, dos redacciones que discrepan: "a problem that has a documented root cause and a workaround" (Atlassian) y "a problem that has been analyzed but not resolved" (BMC). Fuente 10.
- Solución provisoria (workaround): reduce el impacto sin eliminar la causa; si arreglar no conviene económicamente, el problema queda como error conocido y se aplica el workaround cuando vuelve a haber incidentes. Fuente 10 (BMC).
- Los errores conocidos se registran en una base de errores conocidos (KEDB). Fuente 10.
- ITIL 4 recuperó el control de problemas y el control de errores que faltaban en ITIL v3/2011. Fuente 11.
- Casos repetidos: ISO 10002 pide analizar quejas para "identify trends and eliminate causes of complaints" (0.1 y 8.2). Fuente 1 [L] para la cita. La práctica de problemas sale del mundo de TI; trasladarla a productos físicos es analogía mía (el equivalente sería un defecto de lote).

Recurso canónico: GO-ITS 38 de Ontario (9), pública y de un adoptante; no pude leerla. Alternativa: Atlassian (10), comercial.

## Cómo divide el campo este ángulo

El árbol propuesto coincide en lo grueso. Ajustes:
1. En el campo, clasificar y escalar suelen ir juntos en "gestión de incidentes" (ITIL): tipo, prioridad, niveles y escalamientos son una sola práctica. Separar Caso de Escalamiento sirve al lector, pero la nota de prioridad debe enlazar a escalamiento y al reloj del SLA.
2. El salto de casos repetidos a causa tiene dos tradiciones: gestión de problemas (TI) y análisis de quejas (calidad, ISO 10002). La nota debería decirlo.
3. El reclamo es, para el campo, un tipo de contacto; que tenga nota propia se justifica por ISO 10002, que lo trata como proceso normado.

## Huecos

- Texto de los pasos 7.2 a 7.9 de ISO 10002 y de los anexos (flujogramas E y H): la muestra pública no los trae; la OBP dio 403.
- Guías ITIL 4 (service desk, incident, problem): pagas; todo lo de ITIL es secundario. Sin verificar contra el glosario oficial: incidente, pedido de servicio, error conocido, escalamiento funcional y jerárquico.
- Estándares de Ontario (8 y 9): 403 al leerlos; solo citas del buscador.
- Nivel 0/1/2/3 y triage: sin fuente neutral.
- Fusión, reapertura y plazos para reabrir: solo evidencia de producto.
- Estudio independiente que compare niveles y swarming: ninguno; el respaldo del swarming es autoinformado. Los casos Ping Identity, Autodesk y Cisco no se leyeron.
- Qué datos debe pasar una derivación al técnico y criterios para decidirla: solo inferencia.
- Garantía legal y plazos: fuera de este ángulo; requiere dos fuentes independientes y va en la nota argentina.
- Odoo Repairs: 404; Field Service: la página no dice cómo se vincula el ticket.
