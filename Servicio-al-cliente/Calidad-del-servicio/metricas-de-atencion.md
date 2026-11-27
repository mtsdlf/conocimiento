---
resumen: >-
  Las métricas de atención son los números que la operación saca de sus propios registros, sin preguntarle nada al cliente: la resolución al primer contacto, el tiempo medio de atención, las reaperturas, los casos pendientes y el abandono. Cada una depende de una definición (qué se cuenta, sobre qué total y en qué ventana), y casi todas se pueden mejorar en el tablero empeorando la atención.
estado: borrador
estabilidad: semi
fuentes:
  - "Dixon, Freeman y Toman (2010), «Stop Trying to Delight Your Customers», Harvard Business Review, julio-agosto, 116-122, copia del artículo: https://beyondphilosophy.com/wp-content/uploads/2013/07/Stop-Trying-to-delight.pdf (leído entero)"
  - "Gans, Koole y Mandelbaum (2003), «Telephone call centers: tutorial, review, and research prospects», M&SOM 5(2), 79-141, §1, §2.3 y §3.2: https://aviman.technion.ac.il/files/References/Gans-Koole-Mandelbaum-CCReview.pdf (leído en parte)"
  - "Wikipedia, «First call resolution»: https://en.wikipedia.org/wiki/First_call_resolution (leída; cita blogs de proveedores)"
  - "Gartner, documento sobre resolución al primer contacto (2024): https://www.gartner.com/en/documents/5232563 (según su resumen; el texto es de pago)"
  - "Atlassian, «First call resolution»: https://www.atlassian.com/itsm/service-request-management/first-call-resolution (según el resumen del buscador; como evidencia de práctica)"
  - "Gallup, «Banking Analysis: Better Service Doesn't Increase Costs»: https://news.gallup.com/businessjournal/185963/banking-analysis-better-service-doesn-increase-costs.aspx (leído)"
  - "COPC, estándar CX R8.0: https://www.copc.com/copc-standards/for-csps/ y reporte de benchmarking de eficiencia y costo 2022 (según resúmenes; el estándar no se leyó)"
  - "ISO 18295-1:2017, ficha: https://www.iso.org/standard/64739.html ; índice: https://www.din.de/de/mitwirken/normenausschuesse/nadl/veroeffentlichungen/wdc-beuth:din21:276760944/toc-2704082/download (solo índice y ficha)"
  - "CX Today, «Why does call duration or talk time matter in the CX world?»: https://www.cxtoday.com/contact-center/why-does-call-duration-or-talk-time-matter-in-the-cx-world/ (según el resumen del buscador; los estudios que cita no se leyeron)"
  - "Servicio-al-cliente/.investigacion/calidad-del-servicio.md, sección 1"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, secciones 4 (mito 3) y 5"
aliases: [métricas de la atención, indicadores de atención, KPI de servicio al cliente, resolución al primer contacto, first contact resolution, first call resolution, FCR, tiempo medio de atención, average handle time, AHT, reapertura, reopen rate, pendientes, backlog, abandono, abandonment rate, velocidad media de respuesta, ASA]
creado: 2026-11-27
revisado:
---

# Métricas de atención

Las métricas de atención son los números que la operación saca de sus propios registros, sin preguntarle nada al cliente: la resolución al primer contacto, el tiempo medio de atención, las reaperturas, los casos pendientes y el abandono. Cada una depende de una definición (qué se cuenta, sobre qué total y en qué ventana), y casi todas se pueden mejorar en el tablero empeorando la atención.

Son una de las tres formas de medir la [calidad del servicio](calidad-del-servicio.md). Salen de los estados y las fechas del [caso](../Caso/caso.md) y de los contactos que lo abren, así que una métrica solo es tan buena como lo que el sistema registra. Las otras dos formas, preguntar con [encuestas de satisfacción](encuestas-de-satisfaccion.md) y escuchar con el [monitoreo de calidad](monitoreo-de-calidad.md), sirven de control a estas.

Dos métricas de tiempo no están acá. El nivel de servicio del centro de contacto (el porcentaje de contactos atendidos dentro de un tiempo, como 80% en 20 segundos) es una meta de dotación y vive en el [dimensionamiento del equipo](../Canales-de-atencion/dimensionamiento-del-equipo.md). El tiempo de primera respuesta y el de resolución, medidos contra lo prometido, son del [acuerdo de nivel de servicio](../Niveles-de-servicio/tiempos-de-respuesta-y-resolucion.md).

## Qué fijan las normas y qué dejan abierto

La norma ISO 18295-1:2017, de centros de contacto, trae un Anexo A informativo con directrices de métricas (según su índice). El estándar COPC incluye el tiempo medio de atención, la utilización y la ocupación entre sus métricas de eficiencia, y desde su versión 8 deja que cada organización elija métricas que cumplan la intención que define (según resúmenes). Ninguno de los dos textos se leyó, así que las definiciones de abajo salen de la práctica. Cómo se escribe la receta de una métrica para que dos tableros den el mismo número está en [definición de métrica](../../Datos/Analitica-de-producto/definicion-de-metrica.md).

> [!NOTE] Sin fuente todavía: las definiciones del Anexo A de ISO 18295-1 y del estándar COPC, con su numerador, su denominador y su ventana.

## Resolución al primer contacto y sus cuatro definiciones

La resolución al primer contacto mide qué parte de los casos se resolvió sin que el cliente tuviera que volver. La definición corriente, según la Wikipedia que cita a una consultora del rubro, es la capacidad de resolver las interacciones «on the first call or contact». No hay un estándar interno único y se discute qué cuenta como resuelto.

Compiten cuatro definiciones, y ninguna fuente primaria las compara:

1. **Interna, por ventana sin repetición.** Se cuenta como resuelto el caso sin otro contacto del mismo cliente por lo mismo dentro de una ventana. Según la Wikipedia, que cita un blog de proveedor, la ventana va de «1 to 30 days», y este método «can overstate the FCR rate by 10% to 20%» frente al externo. Una mesa de ayuda recomienda esperar de 24 a 48 horas antes de contar un caso como resuelto (según un resumen).
2. **Externa, por encuesta.** Se le pregunta al cliente si el problema se resolvió en el primer contacto. La Wikipedia da un promedio de la industria de 70% con este método, sin cita.
3. **Por quien atiende.** Quien atiende marca «lo resolví» al cerrar. Es la más fácil de registrar y la que menos dice del cliente (lectura de esta base).
4. **Desde el cliente, en todos los canales.** Según el resumen de un documento de Gartner, la mayoría mide la resolución solo dentro de un canal atendido, mientras el cliente cuenta como primer intento el que hizo en cualquier canal, incluido el autoservicio.

Las cifras de las dos primeras salen de blogs de proveedores que repite una sola fuente secundaria: sirven para saber que la diferencia existe, no su tamaño.

La cuarta importa porque, según Dixon, Freeman y Toman (2010), el 57% de las llamadas entrantes venía de clientes que antes habían pasado por el sitio web: lo que el teléfono cuenta como primer contacto pudo ser el segundo intento. Cómo se juntan los contactos de varios canales en un caso está en [canales de atención](../Canales-de-atencion/canales-de-atencion.md).

Los mismos autores muestran el límite de cualquier definición: «22% of repeat calls involve downstream issues related to the problem that prompted the original call, even if that problem itself was adequately addressed the first time». La métrica puede dar resuelto y el cliente volver por lo que el primer arreglo dejó suelto.

## El tiempo medio de atención es capacidad, no calidad

El tiempo medio de atención es lo que dura, en promedio, atender un contacto: la conversación más el trabajo posterior de quien atiende (según un resumen). No es el tiempo de resolución, que se mide en el calendario del caso desde que entra hasta que se resuelve. En el modelo de colas de Gans, Koole y Mandelbaum (2003) es un parámetro del servicio: con el volumen y la meta de espera, da cuántas personas hacen falta. Ese uso está en el [dimensionamiento del equipo](../Canales-de-atencion/dimensionamiento-del-equipo.md).

Usarlo como meta de calidad es otra cosa. Dixon y otros encontraron que los centros rara vez miden el esfuerzo del cliente a lo largo de varios contactos, «generally because they're overly focused on managing call time», y que la causa más grande de esfuerzo es tener que volver a llamar. Quien atiende con un reloj encima corta antes y el cliente vuelve (lectura de esta base).

La evidencia en la otra dirección es débil. Gallup estudió un banco de México en el primer trimestre de 2015: los grupos con el 30% superior en puntajes de servicio tuvieron un tiempo medio por llamada 2,4% menor y una resolución al primer contacto 6,1% mayor. Es una correlación en una sola organización, sin tamaño de muestra ni definiciones publicadas. Dos estudios que cita un medio del rubro no se leyeron: según su resumen, uno halla que los agentes con llamadas más largas resuelven más en un solo contacto, y otro no halla efecto de la duración sobre la satisfacción.

La lectura de esta base es que el tiempo medio de atención sirve para dimensionar y para encontrar casos que tardan por una falla del proceso, y no como meta para quien atiende. El mito y sus cifras están en [mitos del servicio al cliente](../Fundamentos/mitos-del-servicio-al-cliente.md).

## Reaperturas, pendientes y abandono

**Reapertura.** Es el caso que vuelve a abrirse después de marcado como resuelto porque el cliente dice que no se resolvió. Una mesa de ayuda la propone como control de la resolución al primer contacto (según un resumen). Solo se mide si el sistema reabre el mismo caso en lugar de crear otro; la regla está en [caso](../Caso/caso.md).

**Pendientes.** Son los casos abiertos sin resolver en un momento dado, y su antigüedad dice cuánto llevan esperando. En el desarrollo de software «backlog» nombra otra cosa, la lista de trabajo por hacer, y el [glosario](../Fundamentos/glosario-de-servicio-al-cliente.md) lo separa.

**Abandono.** Es el contacto que se corta en la cola antes de que lo atiendan. Gans y otros advierten que la velocidad media de respuesta no incluye a los que abandonaron, así que se mira junto con el porcentaje de abandono: un centro puede bajar la espera promedio porque los que esperaban mucho se fueron. Como referencia, describen un centro de alto rendimiento con abandono de «1%–2%» y utilización promedio de entre 90% y 95%.

> [!NOTE] Sin fuente todavía: una definición con método de la reapertura, de los pendientes y su antigüedad, y del abandono (por ejemplo, desde cuántos segundos de espera se cuenta).

## Cómo se mejora el tablero empeorando la atención

Cada métrica tiene una forma de subir sin que el cliente esté mejor, y una métrica hermana que la delata. Las formas de inflarlas son lectura de esta base, salvo donde se cita; las fuentes solo proponen los controles que llevan atribución.

| Métrica | Cómo se mejora sin mejorar | Con qué se controla |
|---|---|---|
| Resolución al primer contacto (interna) | Acortar la ventana, cerrar rápido y dejar que el cliente vuelva por otro canal como caso nuevo | Reaperturas y satisfacción (una mesa de ayuda); la definición multicanal |
| Tiempo medio de atención | Cortar la conversación, transferir o pedir que vuelva a escribir | Resolución al primer contacto y rellamadas (lectura de esta base a partir de Dixon y otros) |
| Reaperturas | Abrir un caso nuevo en lugar de reabrir el que se cerró | Contactos del mismo cliente por el mismo motivo dentro de la ventana |
| Pendientes | Cerrar sin resolver o pasar casos a «esperando al cliente» | Reaperturas y antigüedad de los casos en espera |
| Abandono y velocidad de respuesta | Mirar una sin la otra | Las dos juntas (Gans y otros) |

El mismo patrón, a nivel del acuerdo con el cliente, es el tablero verde con el cliente enojado, que está en [incumplimiento del acuerdo](../Niveles-de-servicio/incumplimiento-del-acuerdo.md).

## Qué tiene que registrar el sistema

Para calcular estas métricas sin depender de lo que marque quien atiende, el sistema tiene que guardar (lectura de esta base):

- cada contacto con su canal, su hora y el caso al que se vinculó, para la resolución multicanal y las rellamadas;
- cada cambio de estado del caso con su hora, incluida la reapertura como evento y no como caso nuevo;
- el motivo del caso, para saber si un contacto nuevo es por lo mismo ([clasificación y prioridad](../Caso/clasificacion-y-prioridad.md));
- el tiempo de conversación y el de trabajo posterior por separado;
- los contactos que entraron a la cola y se cortaron, con cuánto esperaron.

La definición de cada métrica (ventana, estados, canales) conviene guardarla versionada, porque cambiarla corta la serie histórica.

> [!NOTE] Sin fuente todavía: un estudio con método sobre la relación entre resolución al primer contacto y satisfacción; las cifras que circulan no tienen método a la vista.
