---
resumen: >-
  La comunicación en un incidente de producción tiene tres momentos con géneros distintos: la llamada
  en vivo, con roles y frases cortas que no dejan lugar a dudas; los avisos a clientes, con una
  cadencia fija; y el postmortem escrito, que busca causas sin culpar a nadie.
estado: vigente
estabilidad: estable
fuentes:
  - "Google, Site Reliability Engineering, cap. 14 Managing Incidents: https://sre.google/sre-book/managing-incidents/"
  - "Google, Site Reliability Engineering, cap. 15 Postmortem Culture: https://sre.google/sre-book/postmortem-culture/"
  - "Google, Site Reliability Engineering, apéndice D Example Postmortem: https://sre.google/sre-book/example-postmortem/"
  - "PagerDuty Incident Response, Incident Commander: https://docs.pagerduty.com/ops-guides/incident-response-guide/incident-commander"
  - "PagerDuty Incident Response, During an incident: https://docs.pagerduty.com/ops-guides/incident-response-guide/during-an-incident"
  - "PagerDuty Incident Response, External communication guidelines: https://docs.pagerduty.com/ops-guides/incident-response-guide/external-comms"
  - "Atlassian, Incident communication, vía resumen del buscador: https://www.atlassian.com/incident-management/tutorials/incident-communication"
aliases:
  - Incident communication
  - Comunicación de incidentes
  - Incident commander
  - Status page
  - On-call
creado: 2026-11-27
revisado: 2026-11-27
---

# Incidentes

La comunicación en un incidente de producción tiene tres momentos con géneros distintos: la llamada en vivo, con roles y frases cortas que no dejan lugar a dudas; los avisos a clientes, con una cadencia fija; y el postmortem escrito, que busca causas sin culpar a nadie.

Es el momento en que hablar en segunda lengua cuesta más, porque se habla bajo presión y rápido. Por eso las guías de respuesta a incidentes traen frases hechas, y aprenderlas es más útil que improvisar. Por qué el postmortem no culpa a nadie y cómo se usa está en [Postmortem sin culpa](../../DevOps/Cultura-y-medicion/postmortem-sin-culpa.md); acá va el idioma. La lógica de escribir sin culpar es la misma que la de la [retro](reuniones-de-equipo.md#la-retro-mejorar-sin-culpar).

## La llamada en vivo: roles y frases fijas

El libro de SRE de Google separa cuatro roles: quien comanda el incidente ("holds the high-level state about the incident"), quienes operan ("The operations team should be the only group modifying the system during an incident"), quien comunica ("the public face of the incident response task force") y quien planifica. PagerDuty llama *incident commander* al primero y reparte la comunicación entre un *customer liaison* (afuera) y un *internal liaison* (adentro). Conviene conocer los dos juegos de nombres.

La guía de PagerDuty para el *incident commander* es la mejor fuente de frases, porque las da literales:

| Momento | Frase de PagerDuty |
|---|---|
| Presentarse | "This is [NAME], I am the Incident Commander for this call." |
| Ver si hay quien comande | "Is there an IC on the call?" |
| Asignar una tarea | "Bob, please investigate the high latency on web app boxes. I'll come back to you for an answer in 3 minutes." |
| Confirmar | "Understood." |
| Decidir | "Are there any strong objections to this plan?" |
| Ordenar la llamada | "Ok everyone, can we all speak one at a time please." |
| Pasar el mando | "Everyone on the call, be advised, at this time I am handing over command to [X]." |
| Cerrar | "Ok everyone, we're ending the call at this time. Please continue any follow-up discussion on Slack. Thanks everyone." |

Dos reglas de esa guía van contra la cortesía de todos los días. No se dice *Can someone…?*, porque nadie se hace cargo; se nombra a una persona y se le da un plazo. Tampoco se pregunta *Does everyone agree?*: se pregunta si hay objeciones fuertes. Sus lemas son "Clear is better than concise" y "Making the 'wrong' decision is better than making no decision." En una llamada de incidente se espera que la gente hable directo, una excepción a lo que [Registro y cortesía](../Discurso/registro-y-cortesia.md) explica para el resto del trabajo.

El libro de Google muestra el traspaso con una frase que espera confirmación explícita: "You're now the incident commander, okay?". Pide además llevar un documento vivo del incidente, editable por varios a la vez y con lo más importante arriba. Sus criterios para declarar un incidente: hace falta un segundo equipo, la caída la ven los clientes o el problema sigue sin resolver tras una hora de análisis. Su prioridad: "Stop the bleeding, restore service, and preserve the evidence for root-causing."

## Los avisos a clientes: cadencia y contenido

PagerDuty fija una política para la *status page* (la página pública del estado del servicio): el primer aviso se publica "within 5 minutes of kicking off the incident call"; el segundo, dentro de los 5 minutos siguientes, con el impacto, los componentes y las regiones afectadas; y en las dos primeras horas, una actualización al menos cada 20 minutos. Cada una dice qué cambió, si empezó la recuperación y cuándo es la próxima. La última confirma la recuperación y si se perdieron datos. Hacia adentro, el *internal liaison* da un resumen a la dirección cada unos 30 minutos, y la regla es "If in doubt, post it out".

Atlassian organiza sus plantillas por estado, según el resumen del buscador: *Investigating*, *Identified* y *Monitoring*, seguidos del cierre. Un aviso con esa forma (ejemplo propio):

> **Investigating** — We're seeing elevated error rates on the checkout API in the EU region. Some payments may fail. We're investigating and will post an update within 20 minutes.

Los 20 minutos son la política de PagerDuty, no una regla del rubro. Como inferencia propia, el inglés de estos avisos usa presente continuo para lo que está pasando (*We're seeing*, *We're investigating*), *may* para el impacto posible y futuro con *will* para el compromiso.

## El postmortem escrito

El libro de SRE pide que un postmortem sin culpa "must focus on identifying the contributing causes of the incident without indicting any individual or team", con una idea de fondo: "You can't 'fix' people, but you can fix systems and processes." Su ejemplo del apéndice D tiene esta estructura: *Summary, Impact, Root Causes, Trigger, Resolution, Detection, Action Items, Lessons Learned* (con *What went well*, *What went wrong* y *Where we got lucky*), una línea de tiempo en UTC e información de apoyo.

El tono sale de sus propias frases: "Shakespeare Search down for 66 minutes during period of very high interest", "Estimated 1.21B queries lost, no revenue impact", "Cascading failure due to combination of exceptionally high load and a resource leak". Son frases nominales, sin sujeto y sin culpables (lectura propia). En inglés, sacar la culpa se logra con el sistema como sujeto o con la [pasiva](../Gramatica/pasiva-y-causativa.md): *The alert was not triggered because the threshold was set too high* describe el proceso sin señalar a quién lo configuró.

> [!NOTE]
> Sin fuente todavía: el texto literal de las plantillas de Atlassian (la página no se pudo leer) y el artículo original de Etsy sobre postmortems sin culpa (dio 403).
