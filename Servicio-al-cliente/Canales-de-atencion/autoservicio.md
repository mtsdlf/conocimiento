---
resumen: >-
  El autoservicio es la parte de la atención que el cliente resuelve sin una persona: la base de conocimiento, las preguntas frecuentes, el portal, la respuesta de voz automática y los bots. Se mide por cuántas veces el cliente encuentra lo que necesita, y el desvío (el contacto que no llegó a una persona) se cuenta mal con facilidad.
estado: borrador
estabilidad: semi
fuentes:
  - "Consortium for Service Innovation, KCS v6 Practices Guide, «The Solve Loop»: https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/030 (leída la página, no la guía completa)"
  - "Consortium for Service Innovation, «Measuring Self Service Success»: https://library.serviceinnovation.org/KCS/Measuring_Self-Service_Success (según su resumen; parte es solo para miembros)"
  - "Consortium for Service Innovation, «Understanding Success by Channel»: https://library.serviceinnovation.org/KCS/KCS_v6/Understanding_Success_by_Channel (según su resumen)"
  - "TSIA, «Self-service best practices»: https://www.tsia.com/resources/tsia-self-service-best-practices (según su resumen)"
  - "Metabase, «Deflection rate»: https://www.metabase.com/metrics/deflection-rate (como evidencia de práctica)"
  - "Gans, Koole y Mandelbaum (2003), M&SOM 5(2), 79-141, sección 2.2: https://aviman.technion.ac.il/files/References/Gans-Koole-Mandelbaum-CCReview.pdf"
  - "Dixon, Freeman y Toman (2010), «Stop Trying to Delight Your Customers», Harvard Business Review, julio-agosto, 116-122: https://beyondphilosophy.com/wp-content/uploads/2013/07/Stop-Trying-to-delight.pdf"
  - "Gartner, nota de prensa del 19 de agosto de 2024: https://www.gartner.com/en/newsroom/press-releases/2024-08-19-gartner-survey-finds-only-14-percent-of-customer-service-issues-are-fully-resolved-in-self-service (según resumen del buscador; la página dio 403)"
  - "CFPB, «Chatbots in consumer finance», junio de 2023: https://www.consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance/ (leído el resumen de la página, no el informe)"
  - "Price y Jaffe (2008), The Best Service Is No Service, Jossey-Bass/Wiley: https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0470189088,descCd-description.html (según el resumen de la editorial; el libro no se leyó)"
  - "Servicio-al-cliente/.investigacion/canales-y-niveles-de-servicio.md, sección 2"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, sección 4, mito 4"
aliases: [self-service, autoservicio, base de conocimiento, knowledge base, preguntas frecuentes, FAQ, portal de clientes, bot, chatbot, IVR, respuesta de voz interactiva, desvío, deflection, KCS, Knowledge-Centered Service]
creado: 2026-11-27
revisado:
---

# Autoservicio

El autoservicio es la parte de la atención que el cliente resuelve sin una persona: la base de conocimiento, las preguntas frecuentes, el portal, la respuesta de voz automática y los bots. Se mide por cuántas veces el cliente encuentra lo que necesita, y el desvío (el contacto que no llegó a una persona) se cuenta mal con facilidad.

Es uno de los dos lados de los [canales de atención](canales-de-atencion.md): el otro es la atención asistida. Lo que el autoservicio no resuelve entra como contacto a una persona y abre o actualiza un [caso](../Caso/caso.md). Por eso el autoservicio cambia el volumen que usa el [dimensionamiento del equipo](dimensionamiento-del-equipo.md), pero solo en la medida en que de verdad resuelve.

## De qué está hecho el autoservicio

- **La base de conocimiento**: artículos que explican cómo resolver un problema o hacer un trámite. Es la pieza que alimenta a las demás.
- **Las preguntas frecuentes**: una selección corta de esos artículos, a la vista.
- **El portal**: un lugar donde el cliente identificado consulta y opera por su cuenta. Que incluya abrir un caso y ver su estado es práctica común sin fuente leída.
- **La respuesta de voz automática** (IVR, por sus siglas en inglés): el menú telefónico que resuelve sin pasar a una persona. Gans, Koole y Mandelbaum dicen que en muchos centros bancarios «roughly 80% of customer calls are fully self-served using an IVR». Es una cifra de 2003 y de un sector, no una referencia general.
- **Los bots**: programas que conversan por chat o mensajería. No se encontró una fuente primaria y neutral sobre cuánto resuelven; lo que hay es de proveedores.

## KCS: la base de conocimiento se escribe mientras se atiende

KCS (Knowledge-Centered Service) es la metodología del Consortium for Service Innovation para mantener la base de conocimiento. Su idea central es que el artículo no lo escribe un equipo aparte después, sino quien atiende el caso, en el momento. La guía v6 lo organiza en dos ciclos.

El **ciclo de resolución** (Solve Loop) es, en sus palabras, «the request-response workflow». La página leída lo arma con cuatro prácticas:

1. **Capturar**: «capture in the workflow: while responding to the request, we capture the requestor's context».
2. **Estructurar**: «consistent structure, simple templates, and a crisp style improves KCS article readability».
3. **Reusar**: buscar un artículo que exista antes de escribir otro.
4. **Mejorar**: «reuse is review: as responders, we take responsibility for the articles we interact with».

Otra lectura del corpus v6 pone el orden reusar, mejorar, capturar, estructurar; la página leída numera como arriba. No se leyó la guía completa para resolverlo.

El **ciclo de evolución** (Evolve Loop) aprende de muchos eventos del primero: según resúmenes del corpus, los expertos escriben artículos de más valor a partir de los patrones de reuso y de uso del autoservicio. Los nombres y el orden de sus prácticas cambian según la página, y no se verificaron.

Para un sistema, KCS pide tres cosas: buscar en la base desde la pantalla del caso, crear o editar un artículo desde ahí sin cambiar de herramienta, y vincular el artículo usado al caso. Ese vínculo es el dato que después muestra qué artículos resuelven y cuáles faltan (lectura de esta base sobre la guía).

## Cómo se mide el autoservicio

El Consortium dice que medir el éxito del autoservicio es difícil y que «there is no one measure that indicates success». Define el **éxito del autoservicio** como el porcentaje de veces que el cliente encuentra lo que necesita, y la **evasión de costo** (el contacto que ya no llega a una persona) como un subconjunto de ese éxito. Propone medir con más de un indicador. La TSIA, una asociación del sector, propone definiciones estándar de éxito, desvío implícito y desvío explícito; se conocen por su resumen.

## Por qué el desvío se cuenta mal

El **desvío** (deflection) es el contacto que no llegó a una persona porque el cliente se resolvió solo. La forma fácil de contarlo es restar: todo el que entró al portal o al menú telefónico y no habló con nadie cuenta como desviado. Así, el cliente que se cansó y abandonó también suma como éxito. Según notas de proveedores, el desvío es real solo si el cliente no vuelve por otro canal con el mismo problema. Uno de ellos propone contar como resuelto solo lo que no abrió un caso en las 72 horas siguientes; es la regla de un proveedor, no un estándar.

La evidencia de que el autoservicio resuelve menos de lo que se cuenta viene de dos lados:

- Dixon, Freeman y Toman: «Fifty-seven percent of inbound calls came from customers who went to the website first». Muchas llamadas llegan después de fracasar en el autoservicio.
- Gartner, en una encuesta a 5.728 clientes: solo el 14% de los problemas se resolvió del todo en autoservicio, y el 36% aun entre los problemas «very simple». El fallo más común fue no encontrar contenido relevante, en más del 43% de los casos. Se conoce por el resumen de su nota de prensa de 2024, y es una sola fuente, de la consultora que vende el estudio.

Del otro lado, Dixon y sus coautores citan una empresa donde el autoservicio subió del 30% al 84% bajando el esfuerzo del cliente. Es un caso de la propia consultora de los autores.

Para medirlo bien, el sistema tiene que poder unir la sesión de autoservicio con lo que pasó después: si el mismo cliente abrió un caso, por qué canal y en cuánto tiempo. Sin ese vínculo, el desvío es una resta (lectura de esta base).

## Los bots y la salida a una persona

La Oficina de Protección Financiera del Consumidor de Estados Unidos (CFPB) estudió los bots de la banca en 2023. El resumen de su informe dice: «Deficient chatbots that prevent access to live, human support can lead to law violations». El término «doom loops» (el cliente que da vueltas en el bot sin salida) y la cifra de 98 millones de usuarios de bots bancarios en 2022 vienen de resúmenes de prensa y de estudios jurídicos, no de la página leída. Es evidencia sobre la banca de un país.

La lectura de esta base para el diseño: el bot y el menú telefónico necesitan una salida a una persona, y el caso tiene que llegarle a esa persona con lo que el cliente ya contó, para que no empiece de cero.

> [!NOTE] Sin fuente todavía: cuánto resuelven los bots, medido por una fuente que no los venda.

Las cifras que circulan sobre autoservicio y bots, con lo que sí dice la evidencia, están en [mitos del servicio al cliente](../Fundamentos/mitos-del-servicio-al-cliente.md).

## El autoservicio no es la causa resuelta

Un artículo que explica cómo esquivar un problema baja las llamadas, pero el problema sigue. Para la corriente de «la mejor atención es no necesitarla» (Price y Jaffe, según resúmenes de su editorial), cada contacto señala algo que falló antes y hay que atacar esa causa. El camino de los casos repetidos a la causa está en [problema y causa raíz](../Escalamiento/problema-y-causa-raiz.md). Que el autoservicio sea el «nivel 0» de los [niveles de soporte](../Escalamiento/niveles-de-soporte.md) es práctica común sin fuente neutral.
