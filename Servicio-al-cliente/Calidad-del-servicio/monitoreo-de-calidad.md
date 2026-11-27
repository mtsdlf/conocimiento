---
resumen: >-
  El monitoreo de calidad es escuchar o leer una muestra de las conversaciones de la atención y evaluarlas con una grilla, para saber si se atendió bien y qué tiene que mejorar cada persona. Se completa con la voz del cliente: juntar los reclamos, las encuestas y las conversaciones para encontrar lo que se repite y devolverlo a quien puede arreglar la causa.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework, categoría «Manage Customer Service» (6.2.1.4 y 6.2.3), copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/6-manage-customer-service"
  - "ISO 18295-1:2017, índice: https://www.din.de/de/mitwirken/normenausschuesse/nadl/veroeffentlichungen/wdc-beuth:din21:276760944/toc-2704082/download (solo índice)"
  - "ISO 10002:2018, ficha: https://www.iso.org/standard/71580.html (según resúmenes) ; índice: https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:293819883/toc-2874880/download (solo índice)"
  - "Verint, «QM Assessments: How Many is Enough?»: https://verint.com/blog/qm-assessments-how-many-is-enough (según el resumen del buscador; como evidencia de práctica)"
  - "CustomerThink, sobre cantidad de evaluaciones y calibración: https://customerthink.com/?p=68805 (según el resumen del buscador; como evidencia de práctica)"
  - "TechTarget, «Best practices for contact center quality assurance»: https://www.techtarget.com/searchCustomerExperience/tip/Best-practices-for-contact-center-quality-assurance (según el resumen del buscador; como evidencia de práctica)"
  - "Price y Jaffe (2008), The Best Service Is No Service, Jossey-Bass/Wiley: https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0470189088,descCd-description.html (según la descripción del editor; el libro no se leyó)"
  - "Dixon, Freeman y Toman (2010), «Stop Trying to Delight Your Customers», Harvard Business Review, julio-agosto, 116-122: https://beyondphilosophy.com/wp-content/uploads/2013/07/Stop-Trying-to-delight.pdf (leído entero)"
  - "Servicio-al-cliente/.investigacion/calidad-del-servicio.md, secciones 0 y 3"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, secciones 1 y 3"
aliases: [monitoreo de calidad, aseguramiento de calidad, quality assurance, QA, quality monitoring, evaluación de conversaciones, grilla de evaluación, scorecard, calibración, calibration, evaluación automática, voz del cliente, voice of the customer, VoC, análisis de reclamos]
creado: 2026-11-27
revisado:
---

# Monitoreo de calidad

El monitoreo de calidad es escuchar o leer una muestra de las conversaciones de la atención y evaluarlas con una grilla, para saber si se atendió bien y qué tiene que mejorar cada persona. Se completa con la voz del cliente: juntar los reclamos, las encuestas y las conversaciones para encontrar lo que se repite y devolverlo a quien puede arreglar la causa.

Es la tercera forma de medir la [calidad del servicio](calidad-del-servicio.md), la única que mira qué se dijo. Las [métricas de atención](metricas-de-atencion.md) cuentan tiempos y estados, y las [encuestas de satisfacción](encuestas-de-satisfaccion.md) dicen cómo lo vivió el cliente, pero ninguna de las dos explica por qué un caso salió mal (lectura de esta base). El marco de APQC lo tiene como paso propio de la gestión del equipo de atención: «Monitor and evaluate quality of customer interactions with customer service representatives» (6.2.1.4). La norma ISO 18295-1 de centros de contacto le dedica una cláusula, «Quality assurance related to customer interactions» (7.4, según su índice; el texto no se leyó).

## La grilla de evaluación

La grilla es la lista de criterios con que un evaluador puntúa una conversación. Como lectura de esta base, conviene puntuar por separado lo que se le dijo al cliente (si la respuesta fue correcta y completa), cómo se le dijo (trato, claridad) y lo que se registró en el caso (motivo, notas, cierre), porque piden correcciones distintas. La grilla tiene que poder leerse igual por dos evaluadores distintos, y eso se prueba con la calibración.

> [!NOTE] Sin fuente todavía: una grilla publicada con método, o una norma que diga qué criterios lleva y cómo se ponderan.

## Cuántas conversaciones se evalúan

No hay norma ni estudio que fije el número; lo que hay es consejo de proveedores. Según los resúmenes leídos, las guías de proveedores dan de 6 a 10 evaluaciones por persona por mes. Otro proveedor, con una fórmula de tamaño de muestra, estima 65 por persona por mes para alguien que atiende unas 1.400 conversaciones, con 90% de confianza. El número depende de lo que se quiera saber: 6 conversaciones alcanzan para dar una devolución con ejemplos, y no para sacar un puntaje que compare a dos personas (lectura de esta base). Cómo se elige un tamaño de muestra con una confianza dada está en [muestreo e inferencia](../../Datos/Estadistica/muestreo-e-inferencia.md).

La muestra también tiene que ser al azar dentro de lo que se quiere evaluar. Si el supervisor elige qué escuchar, evalúa los casos que ya le llamaron la atención (lectura de esta base).

## Calibrar a los evaluadores

La calibración es poner a varios evaluadores a puntuar las mismas conversaciones y comparar los puntajes, para que la nota dependa de la conversación y no de quién la evaluó. Las prácticas que recomiendan los proveedores, según un resumen, son: al menos 10 llamadas por ejercicio, sesiones cada pocas semanas con las mismas grabaciones, una tolerancia acordada de antemano (por ejemplo, puntajes totales dentro de un 5% entre evaluadores) y revisar los criterios que varían más de un 10%. Es consejo sin método publicado.

Un criterio donde los evaluadores no se ponen de acuerdo es un criterio mal escrito, no un evaluador malo (lectura de esta base). La calibración corrige la grilla tanto como a quienes la usan.

## Evaluación automática

La evaluación automática transcribe las conversaciones y las puntúa todas con reglas o con un modelo, en lugar de una muestra. Lo que cambia es la escala: deja de haber muestra (lectura de esta base, sin fuente leída sobre la práctica). Lo que no cambia es que la grilla tiene que estar escrita y calibrada, ahora contra lo que diría un evaluador humano.

> [!NOTE] Sin fuente todavía: cómo se valida una evaluación automática contra evaluadores humanos y con qué acuerdo se la da por buena. El tema no se investigó.

## De la conversación a la causa: la voz del cliente

La voz del cliente es el análisis conjunto de lo que el cliente dice por todas las vías (reclamos, encuestas, conversaciones evaluadas) para encontrar lo que se repite. Las tres formas de medir alimentan el mismo análisis de causas (lectura de esta base). La norma ISO 10002, de tratamiento de reclamos, lo pone fuera del trámite de cada reclamo, en su cláusula 8 «Mantenimiento y mejora»: 8.1 recolección de la información, 8.2 análisis y evaluación de los reclamos, 8.3 satisfacción con el proceso de reclamos, 8.4 seguimiento, 8.5 auditoría, 8.6 revisión por la dirección y 8.7 mejora continua (según su índice; el texto no se leyó). APQC también cierra el circuito del reclamo con un paso de análisis (6.2.3).

El reclamo individual, con su recepción, acuse, investigación, respuesta y cierre, está en [reclamo](../Caso/reclamo.md). Cuando el análisis encuentra muchos casos con la misma causa, se juntan en un problema y se le pasa a quien puede arreglarla; eso está en [problema y causa raíz](../Escalamiento/problema-y-causa-raiz.md). La voz del cliente es el paso del medio: mira los casos en conjunto y decide qué se repite lo suficiente como para abrir un problema.

Detrás está la idea de Price y Jaffe (2008): el contacto es un dato de disfunción, y hay que bajar la demanda atacando sus causas (según resúmenes del libro; no se leyó). Dixon, Freeman y Toman (2010) dan un ejemplo del mecanismo: el 57% de las llamadas entrantes venía de clientes que antes habían pasado por el sitio web, y, en la lectura de esta base, cada una de esas llamadas dice algo del sitio.

## Cómo se diseña en un sistema

Lo que sigue es lectura de esta base:

- La evaluación es un registro propio, vinculado a la conversación, al caso y a quien atendió, con la versión de la grilla con que se hizo.
- La muestra la saca el sistema al azar, con reglas de estratificación (por canal, por tipo de caso) y no a mano.
- Las sesiones de calibración guardan los puntajes de cada evaluador sobre las mismas conversaciones, para medir la dispersión por criterio.
- El motivo del caso se registra con una lista cerrada ([clasificación y prioridad](../Caso/clasificacion-y-prioridad.md)): sin categorías comparables, la voz del cliente se reduce a leer textos libres.
- Un hallazgo de la voz del cliente puede abrir un problema y quedar vinculado a los casos que lo originaron.

## Cómo falla

Falla cuando la evaluación se usa solo para castigar y no para enseñar: quien atiende aprende a cumplir la grilla y no a resolver (lectura de esta base). Falla cuando la grilla premia seguir un guion y la conversación sale correcta y el cliente sin respuesta. Y falla cuando la voz del cliente termina en un informe que no llega a quien puede cambiar el producto, la factura o el proceso que genera los contactos.
