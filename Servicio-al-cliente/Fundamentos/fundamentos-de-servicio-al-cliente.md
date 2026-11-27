---
resumen: >-
  Lo transversal del tema Servicio al cliente: las escuelas que explican la atención de formas distintas, cómo dividen el campo las normas y los marcos (APQC, ISO 10002, ISO 18295-1, ITIL), qué cortes son de esta base y dónde se produce el saber del campo.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework, categoría «Manage Customer Service» (6.0), copia de un tercero sin versión declarada, leída entera: https://capechamber.co.za/enterprise/improve-your-business-processes/6-manage-customer-service"
  - "ISO 10002:2018, índice (copia del DIN), leído solo el índice: https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:293819883/toc-2874880/download"
  - "ISO 18295-1:2017, índice (copia del DIN), leído solo el índice: https://www.din.de/de/mitwirken/normenausschuesse/nadl/veroeffentlichungen/wdc-beuth:din21:276760944/toc-2704082/download"
  - "ITIL 4, lista de las 34 prácticas, según el resumen del buscador: https://itsm.tools/34-itil-4-management-practices/"
  - "Gans, Koole y Mandelbaum (2003), «Telephone call centers: tutorial, review, and research prospects», M&SOM 5(2), 79-141, leído en parte (índice, §2.1, §2.5, §3.2, §4.2): https://aviman.technion.ac.il/files/References/Gans-Koole-Mandelbaum-CCReview.pdf"
  - "Cleveland, Call Center Management on Fast Forward, 4.ª ed., ICMI, 2019, solo el extracto del capítulo 2: https://www.bradcleveland.com/wp-content/uploads/2023/05/Ch-2-Customer-Access-Strategy-book-excerpt.pdf"
  - "Dixon, Freeman y Toman (2010), «Stop Trying to Delight Your Customers», Harvard Business Review, julio-agosto, 116-122, leído entero: https://beyondphilosophy.com/wp-content/uploads/2013/07/Stop-Trying-to-delight.pdf"
  - "Price y Jaffe, The Best Service Is No Service, Jossey-Bass/Wiley, 2008, según la sinopsis del editor: https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0470189088,descCd-description.html"
  - "Consortium for Service Innovation, «Intelligent Swarming 101», leído entero (fuente con interés): https://www.serviceinnovation.org/intelligent-swarming-101/"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md (secciones 1, 3 y 7)"
aliases: [fundamentos de servicio al cliente, escuelas de servicio al cliente, customer service fundamentals, taxonomía de la atención]
creado: 2026-11-27
revisado:
---

# Fundamentos de servicio al cliente

Lo transversal del tema Servicio al cliente: las escuelas que explican la atención de formas distintas, cómo dividen el campo las normas y los marcos (APQC, ISO 10002, ISO 18295-1, ITIL), qué cortes son de esta base y dónde se produce el saber del campo.

## Cinco maneras de entender la atención

El campo no tiene una teoría común. Cada escuela nació en un lugar distinto (la mesa de ayuda de sistemas, el centro de llamadas, el marketing) y mira una parte distinta del mismo contacto.

| Escuela | Qué es la atención | Quién la sostiene | Qué mira |
|---|---|---|---|
| Gestión de servicios de TI | Un conjunto de prácticas con registro y escalamiento: incidente, pedido, problema, nivel de servicio | ITIL (nacida en la agencia británica CCTA, hoy ITIL 4), HDI, y el Consortium for Service Innovation con KCS y el enjambre | El caso, su estado, quién lo tiene y contra qué acuerdo corre |
| Centro de contacto | Un sistema de colas: llegan contactos, esperan y los atienden personas | Gans, Koole y Mandelbaum (2003); Cleveland, *Call Center Management on Fast Forward* | Pronóstico, dotación, nivel de servicio del centro de contacto, ocupación |
| Experiencia del cliente | Un punto de contacto dentro del recorrido completo del cliente | ISO 18295-1 (cláusulas 4.3 y 5.2 hablan de *customer experience*); la cuarta edición de Cleveland | Qué vive el cliente de punta a punta, no solo en la llamada |
| Crítica del esfuerzo | No hay que deleitar al cliente sino ahorrarle esfuerzo | Dixon, Freeman y Toman (2010), en la *Harvard Business Review* | Rellamadas, cambios de canal, repetir los datos |
| «La mejor atención es no necesitarla» | Cada contacto es la señal de algo que falló antes | Price y Jaffe, *The Best Service Is No Service* (2008), según la sinopsis del editor | Bajar la demanda atacando sus causas |

Las escuelas chocan en las métricas. La resolución al primer contacto es una medida de la escuela del centro de contacto, y Dixon y otros la usan y la discuten a la vez: según su artículo, «22% of repeat calls involve downstream issues related to the problem that prompted the original call, even if that problem itself was adequately addressed the first time». La métrica da bien mientras el cliente vuelve a llamar. Cómo se mide sin engañarse está en [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md).

Las dos críticas tienen límites propios. El estudio de Dixon se hizo dentro de una sola consultora, sin revisión externa de pares, y hay críticos que dicen que el titular es demasiado amplio. El libro de Price y Jaffe no se leyó: lo que se dice de él sale de reseñas y de la sinopsis. La escuela de TI discute adentro los niveles frente al enjambre (ver [niveles de soporte](../Escalamiento/niveles-de-soporte.md)).

Esta base escribe la operación desde las dos primeras escuelas, porque son las que dan objetos y reglas a un sistema, y cita a las otras tres donde discuten. Por qué el cliente juzga la atención como la juzga es de [Servicio y relación](../../Marketing/Servicio-y-relacion/servicio-y-relacion.md), en Marketing, con el [modelo de las brechas](../../Marketing/Servicio-y-relacion/modelo-de-las-brechas.md) y las [expectativas y la zona de tolerancia](../../Marketing/Servicio-y-relacion/expectativas-y-zona-de-tolerancia.md).

## Cómo se divide el campo a sí mismo

Cuatro divisiones pesan, y ninguna coincide con otra.

- **APQC**, en su Process Classification Framework, tiene una categoría «Manage Customer Service» con cinco partes: estrategia (6.1), gestión de los contactos (6.2), servicio de productos después de la venta (6.3), retiros de productos y auditorías de reguladores (6.4) y evaluación de la operación y la satisfacción (6.5). Dentro de 6.2 separa los problemas, pedidos y consultas (6.2.2) de los reclamos (6.2.3) y de las devoluciones (6.2.4). La copia leída es de un tercero y no dice la versión; en la versión 6.0.0 de julio de 2012 la misma categoría tenía el número 5.0, así que quien cite «6.0» tiene que decir de qué versión.
- **ISO 10002:2018** trata solo el reclamo: su cláusula 7 lo opera en pasos, de la recepción y el acuse al cierre, y su cláusula 8 lo convierte en mejora.
- **ISO 18295-1:2017** trata el centro de contacto y lo parte en requisitos de la relación con el cliente, del liderazgo, del personal, de los procesos y de la infraestructura, más una relación aparte con quien contrata al centro cuando la atención está tercerizada.
- **ITIL 4**, según resúmenes, reparte la gestión de servicios en 34 prácticas; tocan este tema la mesa de servicio y la gestión de incidentes, de pedidos de servicio, de problemas y de niveles de servicio.
- **Gans, Koole y Mandelbaum**, desde la investigación operativa, dividen el centro de llamadas en operación, planeamiento de la capacidad y enrutamiento por habilidades; Cleveland, según su editor, en nivel de servicio, pronósticos, dotación, métricas, calidad, presupuesto y estrategia.

### Las cinco verticales contra esas divisiones

| Vertical del tema | APQC | ISO 18295-1 e ISO 10002 | ITIL 4 | Gans y Cleveland |
|---|---|---|---|---|
| [Canales de atención](../Canales-de-atencion/canales-de-atencion.md) | 6.1.3, estrategia de canales; 6.2.1, fuerza de trabajo | 18295-1 8.2, manejo de las interacciones; 7.3, planificación de la dotación | Mesa de servicio como punto único de contacto | Estrategia de acceso del cliente (Cleveland); colas y capacidad (Gans) |
| [Caso](../Caso/caso.md) | 6.2.2 consultas y pedidos; 6.2.3 reclamos; 6.2.4 devoluciones; 6.3 garantía y reparación | 10002 entera para el reclamo; 18295-1 4.4 | Incidentes y pedidos de servicio | Cómo se atiende una llamada (Gans §2.2) |
| [Escalamiento](../Escalamiento/escalamiento.md) | No es categoría: solo «Route» dentro del reclamo (6.2.3.2) | No es cláusula | Un paso dentro de la gestión de incidentes; problemas, práctica aparte | Enrutamiento por habilidades (Gans §5) |
| [Niveles de servicio](../Niveles-de-servicio/niveles-de-servicio.md) | 6.1.5, nivel de servicio objetivo por segmento | 18295-1, relación con el cliente contratante (anexo B) | Gestión de niveles de servicio, práctica propia | Nivel de servicio como fracción atendida en un plazo (Gans §2.3) |
| [Calidad del servicio](../Calidad-del-servicio/calidad-del-servicio.md) | 6.5 evaluación; 6.2.1.4 monitoreo de las interacciones | 18295-1 4.3, 7.4 y anexo A de métricas; 10002 cláusula 8 | No figura como práctica | Calidad del servicio (Gans §2.5) |

### Qué cortes son de esta base

El corte coincide en lo grueso con APQC 6.2 y 6.5 y con la separación de ITIL entre mesa de servicio, incidentes, problemas y niveles de servicio. Cinco decisiones son de la base y no del campo (lectura de esta base sobre las divisiones de arriba):

1. **Escalamiento es vertical propia** aunque ninguna división lo trata como categoría de primer nivel. Se justifica por el lector: quien modela el software necesita estados, dueño y niveles, y esas piezas no caben en el caso.
2. **Problema y causa raíz va en Escalamiento**, y junta dos tradiciones: la gestión de problemas de ITIL y el análisis de reclamos de ISO 10002, que pide «identify trends and eliminate causes of complaints».
3. **Garantía y devolución cuelgan del Caso.** Coincide con APQC (6.2.4 y 6.3); ISO e ITIL las dejan fuera.
4. **El nivel de servicio del centro de contacto vive en el [dimensionamiento del equipo](../Canales-de-atencion/dimensionamiento-del-equipo.md)**, y Niveles de servicio trata solo el acuerdo con el cliente y los acuerdos internos. El campo usa la misma palabra para las dos cosas; el [glosario](glosario-de-servicio-al-cliente.md) las separa.
5. **Los retiros de productos (APQC 6.4) y los avisos a reguladores (6.2.5) quedan fuera del tema.** Se acercan más a la calidad del producto (tema Producción) y al cumplimiento que a la atención de un cliente.

## Dónde se produce el saber del campo

- **Normas ISO**: la familia del reclamo (10001 códigos de conducta, 10002 tratamiento, 10003 disputas fuera de la organización, 10004 medición de la satisfacción) y la 18295 de centros de contacto. Son pagas: para este tema se leyeron sus índices y la vista previa de la 10002, no el texto.
- **Marcos de procesos y de práctica**: el Process Classification Framework de APQC; ITIL, cuyas guías y glosario son pagos y se leyeron por resúmenes; KCS y el enjambre del Consortium for Service Innovation, que publica sus guías abiertas y promueve sus propios modelos.
- **Investigación operativa**: los modelos de colas (Erlang C, Erlang A) y la revisión de Gans, Koole y Mandelbaum (2003), la mejor lectura abierta sobre cómo funciona un centro de llamadas, con la salvedad de que trata casi solo el teléfono.
- **Revistas de marketing y servicios**: la *Harvard Business Review* para la crítica del esfuerzo y la recuperación del servicio; el *Journal of Services Marketing* y otras para la tercerización y la satisfacción.
- **Organismos públicos**: la CFPB de Estados Unidos estudió los bots en la banca (2023). Lo que exige la ley argentina está en [Servicio al cliente en la Argentina](../servicio-al-cliente-en-argentina.md).
- **Consultoras y proveedores**: Gartner, HDI y los fabricantes de mesas de ayuda publican la mayoría de las cifras que circulan. Casi ninguna trae método a la vista, y quien la publica suele vender la solución. La documentación de los sistemas abiertos sirve para ver cómo se modela un caso o un reloj, como evidencia de práctica y no como norma.

> [!NOTE] Sin fuente todavía: el texto de las normas ISO 10002 y 18295-1 (definiciones, pasos y anexo de métricas), la versión vigente del marco de APQC, las guías oficiales de ITIL 4 y el índice completo de Cleveland. Un sitio reporta una versión 5 de ITIL anunciada en enero de 2026; no se verificó.

## Lo que hay en Fundamentos

- [Historia del servicio al cliente](historia-del-servicio-al-cliente.md): del mostrador al centro de llamadas, la mesa de ayuda de sistemas y el autoservicio, con las fechas que discrepan.
- [Mitos del servicio al cliente](mitos-del-servicio-al-cliente.md): el «cinco veces más caro», bajar el tiempo de atención, el desvío y los bots, el acuerdo cumplido, los niveles frente al enjambre y la tercerización, con lo que dice la evidencia.
- [Glosario de servicio al cliente](glosario-de-servicio-al-cliente.md): los términos del tema con su nombre en inglés, la nota donde viven y las palabras con más de un sentido.
