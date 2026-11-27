---
resumen: >-
  Los canales de atención son las vías por las que el contacto del cliente llega a la empresa (mostrador, teléfono, correo, chat, mensajería, portal) y lo que lo atiende en cada una: una persona o el autoservicio. La vertical decide también cuántas personas hacen falta para atender a tiempo.
estado: borrador
estabilidad: estable
fuentes:
  - "Gans, Koole y Mandelbaum (2003), «Telephone call centers: tutorial, review, and research prospects», M&SOM 5(2), 79-141: https://aviman.technion.ac.il/files/References/Gans-Koole-Mandelbaum-CCReview.pdf (leído en parte: secciones 1, 2, 4.1, 4.2 y partes de 5)"
  - "ISO 18295-1:2017, ficha: https://www.iso.org/standard/64739.html (según resúmenes del buscador de ISO, BSI y ANSI; la ficha dio 403)"
  - "ISO 18295-1:2017, índice: https://www.din.de/de/mitwirken/normenausschuesse/nadl/veroeffentlichungen/wdc-beuth:din21:276760944/toc-2704082/download (solo el índice)"
  - "ISO 18295-1, proyecto de segunda edición: https://www.iso.org/standard/94393.html (según resumen del buscador)"
  - "APQC, Process Classification Framework, categoría «Manage Customer Service» (6.0), copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/6-manage-customer-service"
  - "Dixon, Freeman y Toman (2010), «Stop Trying to Delight Your Customers», Harvard Business Review, julio-agosto, 116-122: https://beyondphilosophy.com/wp-content/uploads/2013/07/Stop-Trying-to-delight.pdf"
  - "Servicio-al-cliente/.investigacion/canales-y-niveles-de-servicio.md, sección 1"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, secciones 1 y 4"
aliases: [canales de atención, canales de contacto, customer service channels, contact channels, centro de contacto, contact center, call center, omnicanal, omnichannel, multicanal, multichannel]
creado: 2026-11-27
revisado:
---

# Canales de atención

Los canales de atención son las vías por las que el contacto del cliente llega a la empresa (mostrador, teléfono, correo, chat, mensajería, portal) y lo que lo atiende en cada una: una persona o el autoservicio. La vertical decide también cuántas personas hacen falta para atender a tiempo.

Dentro de [Servicio al cliente](../servicio-al-cliente.md), los canales abren y actualizan el [caso](../Caso/caso.md): cada llamada, correo o mensaje es un contacto, y el caso junta los contactos que tratan lo mismo. Quien atiende en el canal es el primer nivel de los [niveles de soporte](../Escalamiento/niveles-de-soporte.md), y lo que no resuelve se [escala](../Escalamiento/escalamiento.md). [Calidad del servicio](../Calidad-del-servicio/calidad-del-servicio.md) mide lo que pasa en cada canal y devuelve correcciones: qué canal se abre, qué guion se cambia, qué artículo falta en la base de conocimiento.

## Asistidos o de autoservicio, sincrónicos o asincrónicos

La base ordena los canales en dos ejes. El primero es quién atiende: una persona (canal asistido) o el propio cliente con lo que la empresa le deja preparado ([autoservicio](autoservicio.md)). El segundo es si el cliente espera en línea la respuesta (canal sincrónico) o la recibe más tarde (asincrónico). El orden es de esta base; ninguna fuente leída lo fija como clasificación.

| | Sincrónico | Asincrónico |
|---|---|---|
| Asistido | mostrador, teléfono, chat | correo, formulario web, mensajería |
| Autoservicio | respuesta de voz automática, bot | base de conocimiento, preguntas frecuentes, portal |

La mensajería cae en un lado u otro según cómo se use: si se contesta en minutos funciona como un chat, y si se contesta en horas, como un correo (lectura de esta base).

El eje que más pesa para el sistema es el segundo. Gans, Koole y Mandelbaum describen el centro de contacto como «a call center in which agents and IVRs are complemented by services in other media, such as e-mail, fax, webpages, or chat (in that order of prevalence)». Agregan que los pedidos por correo o fax «can be "stored" for later response» y que, bien estandarizados, pueden costar bastante menos que el teléfono. Un canal que se puede guardar para después se atiende con un objetivo de horas; uno que no, con un objetivo de segundos. Esa diferencia cambia la cuenta de cuántas personas hacen falta, que está en [dimensionamiento del equipo](dimensionamiento-del-equipo.md).

Según el mismo trabajo, la ampliación de canales vino de dos lados: «customer demand for channel variety, as well as by the potential for efficiency gains». El paper es de 2003 y trata casi solo el teléfono; dice que en ese momento «no analytical model has yet been dedicated to truly multimedia contact centers».

## Un solo caso aunque el cliente cambie de canal

El cliente que escribe por correo, vuelve a reclamar por chat y después llama hizo tres contactos sobre un mismo asunto. Si cada canal guarda los suyos por separado, la empresa ve tres casos, cada persona que atiende empieza de cero y el cliente repite la historia. La práctica llama **omnicanal** a la atención que junta los contactos de cualquier canal en un solo caso con una historia común, y **multicanal** a la que ofrece varios canales en paralelo, cada uno con su historia. Es una definición de práctica: no se encontró una definición normativa, y según lo que se pudo ver de ISO 18295-1, la norma no usa ninguno de los dos términos.

El cambio de canal es frecuente. Dixon, Freeman y Toman encontraron que «Fifty-seven percent of inbound calls came from customers who went to the website first». Muchas llamadas, entonces, llegan después de un intento en otro canal, y el caso debería mostrar ese intento (lectura de esta base).

Para un sistema, la decisión de diseño es separar dos registros: el **contacto** (cada interacción, con su canal, su hora y quién atendió) y el **caso** (el asunto, con su estado y su dueño). Cada contacto que entra se identifica contra el [registro del cliente](../../Relacion-con-clientes/Registro-del-cliente/cuenta-y-contacto.md) y se agrega a un caso abierto o abre uno nuevo. Qué datos lleva el caso y cómo se fusionan dos casos duplicados está en [caso](../Caso/caso.md).

> [!NOTE] Sin fuente todavía: una regla general para decidir si un contacto nuevo pertenece a un caso abierto o abre otro (por cliente, por tema, por ventana de tiempo).

## Qué pide la norma de centros de contacto

ISO 18295-1:2017 fija requisitos para centros de contacto con el cliente, propios o tercerizados. Según el resumen de su ficha, se aplica a «in-house (captive) and outsourced (third party operator) CCCs of all sizes», de todos los sectores y en «all interaction channels», entrantes y salientes. Especifica indicadores «as and where required». Según su índice, trata la comunicación de información al cliente, la medición de la experiencia, la protección del cliente, el aseguramiento de calidad de las interacciones y el manejo de las interacciones y los datos del cliente.

Según resúmenes del buscador, la norma se revisó y se confirmó en 2023, y hay un proyecto de segunda edición que la va a reemplazar: conviene revisar su estado antes de citarla. El texto es pago; lo de arriba sale de resúmenes de la ficha y del índice. Que un centro de contacto tercerizado tenga una relación aparte con la empresa que lo contrata (cláusula 9 y Anexo B de la norma) se trata en [acuerdos internos](../Niveles-de-servicio/acuerdos-internos.md).

## Por qué canales y dimensionamiento van en la misma vertical

El campo los separa. La copia consultada del marco de APQC pone la estrategia de canales en la estrategia de servicio (6.1.3 «Define and manage customer service channel strategy») y la dotación en la operación (6.2.1 «Plan and manage customer service work force», con pronóstico de volumen, turnos y seguimiento de la utilización). ISO 18295-1 los separa en 7.3 «Workforce planning» y 8.2 «Handling customer interactions».

La base los junta porque el lector que construye software los ve juntos: el canal define qué objetivo de espera tiene sentido, y ese objetivo define cuántas personas hacen falta. El cálculo, con su teoría de colas, queda en una nota propia para que esta entrada no cargue con él.

## Dónde fallan los canales

Fallan cuando un canal no comparte la historia con los demás y el cliente tiene que contar todo de nuevo (lectura de esta base). Fallan cuando el autoservicio no resuelve y el cliente vuelve por el teléfono, contado igual como un contacto evitado: está en [autoservicio](autoservicio.md). Y fallan cuando se abre un canal sincrónico (un chat, un teléfono) sin la dotación para contestarlo en segundos, que es el problema de [dimensionamiento del equipo](dimensionamiento-del-equipo.md).

Lo que la ley argentina pide de los canales (las vías de reclamo, el botón de baja, el trato digno) está en [Servicio al cliente en la Argentina](../servicio-al-cliente-en-argentina.md).

## Qué hay en los canales de atención

- [Autoservicio](autoservicio.md) — base de conocimiento, preguntas frecuentes, portal y bots; la metodología KCS y por qué el desvío se cuenta mal.
- [Dimensionamiento del equipo](dimensionamiento-del-equipo.md) — cuántas personas hacen falta: el nivel de servicio del centro de contacto, Erlang C y A, la ocupación y el caso del correo.
