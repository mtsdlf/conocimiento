---
resumen: >-
  Clasificar un caso es decir qué es (su tipo y su categoría) y priorizarlo es decir cuánto apura, cruzando el impacto con la urgencia. De las dos decisiones salen a quién se asigna, qué tiempo promete el acuerdo de nivel de servicio y cuándo se escala.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework, categoría «Manage Customer Service», 6.2.2 y 6.2.3, copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/6-manage-customer-service"
  - "ISO 10002:2018, vista previa del editor, definición 3.2: https://cdn.standards.iteh.ai/samples/71580/6db527fdda0a42ac8f597ffd406e3509/ISO-10002-2018.pdf"
  - "Gobierno de Ontario, GO-ITS 37, Enterprise Incident Management Process: https://www.ontario.ca/document/go-its-37-enterprise-incident-management-process (según el resumen del buscador; la página no se pudo leer)"
  - "BMC, «Impact, urgency and priority»: https://blogs.bmc.com/impact-urgency-priority (según el resumen del buscador; como evidencia de práctica)"
  - "ERPNext, Issue: https://docs.frappe.io/erpnext/user/manual/en/support/issue (como evidencia de práctica)"
  - "Servicio-al-cliente/.investigacion/caso-y-escalamiento.md, componente 2 y «Cómo divide el campo este ángulo»"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, secciones 1 y 5"
aliases: [clasificación del caso, tipo de caso, categoría, prioridad, impacto, urgencia, matriz de prioridad, triage, triaje, case classification, priority matrix, impact and urgency]
creado: 2026-11-27
revisado:
---

# Clasificación y prioridad

Clasificar un caso es decir qué es (su tipo y su categoría) y priorizarlo es decir cuánto apura, cruzando el impacto con la urgencia. De las dos decisiones salen a quién se asigna, qué tiempo promete el acuerdo de nivel de servicio y cuándo se escala.

Son datos del [caso](caso.md) que, como lectura de esta base, se deciden al entrar y se pueden corregir después. En el campo, clasificar y escalar son una misma práctica: ITIL los pone juntos dentro de la gestión de incidentes, con el tipo, la prioridad, los niveles de soporte y los escalamientos (según resúmenes; las guías de ITIL son pagas y no se leyeron). La base los separa para que cada uno se lea solo, pero la prioridad no se entiende sin el [escalamiento](../Escalamiento/escalamiento.md) ni sin el reloj de [tiempos de respuesta y resolución](../Niveles-de-servicio/tiempos-de-respuesta-y-resolucion.md).

## El tipo de caso: consulta, pedido, incidente o reclamo

La lista consulta, pedido de servicio, incidente y reclamo es de uso común, pero no tiene una fuente primaria leída que la fije. Lo que sí tiene fuente son tres cortes parciales:

- **APQC** separa los problemas, pedidos y consultas (6.2.2) de los reclamos (6.2.3), en una copia de su marco sin versión declarada.
- **ITIL** distingue el incidente, una interrupción o una baja de calidad de un servicio de TI, del pedido de servicio, según resúmenes de su glosario. Su incidente es más estrecho que el caso de un CRM.
- **ISO 10002** define el reclamo como una expresión de insatisfacción con respuesta esperada, explícita o implícita. Lo que hace reclamo a un contacto es esa insatisfacción expresada, no el canal ni el tema.

La norma no define consulta ni pedido: que el reclamo se distinga de ellos por la insatisfacción es lectura de esta base. Cambia el tratamiento: el [reclamo](reclamo.md) lleva acuse, investigación y comunicación de la decisión, y la consulta puede cerrarse con una respuesta. «Incidente» tiene otros sentidos (el de uso general y el aviso a un regulador, que APQC pone en 6.2.5); el [glosario](../Fundamentos/glosario-de-servicio-al-cliente.md) los separa.

## La categoría: de qué trata el caso

La categoría dice sobre qué es el caso, y cada empresa arma la suya. Una mesa de ayuda abierta trae un tipo configurable con ejemplos como funcional, técnico y hardware. La categoría sirve para enrutar el caso al equipo que sabe y, después, para juntar los casos que se repiten en un [problema](../Escalamiento/problema-y-causa-raiz.md) y para el [monitoreo de calidad](../Calidad-del-servicio/monitoreo-de-calidad.md).

## Prioridad: impacto por urgencia

La prioridad se arma con dos ejes. El estándar de gestión de incidentes del Gobierno de Ontario, adoptante de ITIL, dice que «the priority of an incident is primarily determined by the impact on the business and the urgency with which a resolution or work-around is needed» (citado por el buscador; la página no se pudo leer). Como lectura de esta base, el impacto dice a cuántos afecta (un usuario, un área, todos los clientes) y la urgencia, cuánto tarda en doler.

Un proveedor de software de gestión de servicios define la prioridad como «the intersection of impact and urgency», y dice que una matriz de cinco por cinco niveles permite más fineza (según el resumen del buscador). Los valores de cada celda los pone cada organización: no hay tabla universal.

Una mesa de ayuda abierta usa tres prioridades por defecto (baja, media y alta) y ata el acuerdo de nivel de servicio a la prioridad: el acuerdo dice a qué prioridades aplica, y cambiar la prioridad cambia el acuerdo que corre. Por eso, en esa práctica, subir la prioridad es una forma de escalar. Qué tiempos corresponden a cada prioridad está en [niveles de servicio](../Niveles-de-servicio/niveles-de-servicio.md).

## Cómo se modela en un sistema

Como lectura de esta base sobre las fuentes leídas, un sistema necesita:

1. Un tipo de caso, de una lista corta, que dispare reglas distintas (el reclamo con su acuse; la garantía con la revisión del producto).
2. Una categoría jerárquica y editable, que se usa para enrutar y para analizar.
3. El impacto y la urgencia como campos, y la prioridad calculada desde una matriz configurable, con la posibilidad de corregirla a mano y dejar registro de quién la cambió.
4. Un vínculo entre la prioridad y el acuerdo de nivel de servicio, para que el reloj cambie cuando cambia la prioridad.

## Triage

En el uso corriente, triage es la revisión inicial que clasifica, prioriza y asigna un caso recién entrado. ISO 10002 tiene un paso de evaluación inicial (7.5) dentro del tratamiento de reclamos, cuyo texto no se leyó.

> [!NOTE] Sin fuente todavía: el triage como actividad propia (quién lo hace, con qué criterios y en cuánto tiempo). No se encontró fuente que lo defina.

## Cómo falla la clasificación

Como lectura de esta base, falla de dos maneras. La primera es la prioridad inflada: si quien carga el caso, o el propio cliente, elige la prioridad sin criterio, todo termina en alta y la prioridad deja de ordenar. La matriz de impacto y urgencia existe para que la prioridad salga de dos preguntas y no de una opinión. La segunda es la categoría inservible: una lista larga o vaga donde gana «otros», y el análisis de los casos repetidos se queda sin datos.
