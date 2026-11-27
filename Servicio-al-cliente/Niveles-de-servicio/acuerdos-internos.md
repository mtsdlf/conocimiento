---
resumen: >-
  Los acuerdos internos son los que sostienen el acuerdo de nivel de servicio que se le da al cliente: el acuerdo de nivel operativo (OLA), entre equipos de la misma organización, y el contrato de respaldo (UC), con un proveedor externo. El vocabulario viene de ITIL v3, y ITIL 4 lo cambió.
estado: borrador
estabilidad: semi
fuentes:
  - "Advisera, «SLAs, OLAs and UCs in ITIL and ISO 20000»: https://advisera.com/20000academy/knowledgebase/slas-olas-ucs-itil-iso-20000 (según su resumen)"
  - "BMC, «OLA»: https://www.bmc.com/blogs/ola/ (según su resumen)"
  - "InvGate, «Service level management in an ITIL 4 world»: https://blog.invgate.com/service-level-management-in-an-itil-4-world (según su resumen)"
  - "it-processmaps, Service Level Management: https://wiki.en.it-processmaps.com/index.php/Service_Level_Management (según su resumen)"
  - "ISO 18295-1:2017, índice (cláusula 9 y Anexo B): https://www.din.de/de/mitwirken/normenausschuesse/nadl/veroeffentlichungen/wdc-beuth:din21:276760944/toc-2704082/download (solo el índice)"
  - "Feinberg, Xu y Hokama (2012), Journal of Applied Marketing Theory; Whitaker, Krishnan, Fornell y Morgeson (2019), Journal of Computer Information Systems; Sharma et al. (2009 y 2012), Journal of Services Marketing: https://www.emeraldinsight.com/insight/content/doi/10.1108/08876041211245272/full/html y https://doaj.org/article/8c048bea09054c78841da740a8fc58e3 (abstracts, según resumen del buscador)"
  - "Servicio-al-cliente/.investigacion/canales-y-niveles-de-servicio.md, sección 4"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, secciones 4 (mito 7) y 5"
aliases: [acuerdo de nivel operativo, OLA, operational level agreement, contrato de respaldo, contrato de soporte, UC, underpinning contract, acuerdo entre equipos, acuerdo con proveedores]
creado: 2026-11-27
revisado:
---

# Acuerdos internos

Los acuerdos internos son los que sostienen el acuerdo de nivel de servicio que se le da al cliente: el acuerdo de nivel operativo (OLA), entre equipos de la misma organización, y el contrato de respaldo (UC), con un proveedor externo. El vocabulario viene de ITIL v3, y ITIL 4 lo cambió.

Completan los [niveles de servicio](niveles-de-servicio.md). El acuerdo con el cliente promete un tiempo de resolución; los acuerdos internos reparten ese tiempo entre quienes trabajan en el caso: el primer nivel que atiende, el segundo nivel o el área a la que se [escala](../Escalamiento/escalamiento.md), y el proveedor que repara o repone.

## El acuerdo de nivel operativo y el contrato de respaldo

En el material de ITIL v3, según resúmenes de guías secundarias:

- El **acuerdo de nivel operativo** (OLA, operational level agreement) es un acuerdo con otra parte de la misma organización. Un glosario universitario lo resume como «same as Service Level Agreements, but between service providers».
- El **contrato de respaldo** (UC, underpinning contract) es un contrato con un proveedor externo que aporta algo que el servicio necesita.

La distinción entre los tres acuerdos es de destinatario: el de nivel de servicio, con el cliente; el operativo, adentro; el de respaldo, con un proveedor.

> [!IMPORTANT]
> Las fuentes discrepan sobre el lugar de estos acuerdos en ITIL 4. Según InvGate, en ITIL 4 ya no hay OLA ni UC como tipos de acuerdo con nombre propio; otra guía los describe vigentes, con el contrato de respaldo administrado por la práctica de gestión de proveedores. No se leyó el texto oficial de ITIL 4, que es pago. Los conceptos siguen siendo útiles para modelar la atención aunque el vocabulario de la versión vigente haya cambiado.

## Por qué el acuerdo con el cliente depende de los de adentro

La lectura de esta base es que el tiempo prometido al cliente es la suma de los tiempos de todos los que tocan el caso. Si el acuerdo promete resolver en 16 horas hábiles y el caso puede pasar por el primer nivel, el segundo nivel y un proveedor, cada uno necesita su propio plazo, y la suma tiene que entrar en las 16 horas con margen. Si el segundo nivel no tiene plazo comprometido, el primer nivel promete algo que no controla.

Un ejemplo de esta base: una empresa que vende equipos promete al cliente resolver una falla en garantía en 5 días hábiles. Para eso, el taller propio se compromete a diagnosticar en 2 días (un acuerdo operativo) y el proveedor del repuesto a entregarlo en 2 días (un contrato de respaldo). Si el proveedor tarda 10, el acuerdo con el cliente se vence aunque todos los de adentro cumplan. Cómo se decide y se pasa la visita de un técnico está en [derivación al técnico](../Escalamiento/derivacion-al-tecnico.md).

## La atención tercerizada

Cuando la atención misma la da un tercero, un centro de contacto contratado, el acuerdo entre la empresa y ese centro es un contrato de respaldo para la empresa y un acuerdo de nivel de servicio para el centro. ISO 18295-1 trata esta relación aparte: su cláusula 9 («Client relationship») y su Anexo B («Client/CCC relationship») tratan la relación entre el centro de contacto y la empresa que lo contrata. En el índice, «client» es esa empresa y «customer» el cliente final (lectura de esta base sobre el índice; el texto de la norma es pago).

Si tercerizar la atención baja la satisfacción del cliente final, la evidencia es mixta. Feinberg, Xu y Hokama (2012), en dos experimentos, encuentran que los consumidores esperan menos de una llamada atendida en el exterior, pero que cuando se mide lo que importa (la velocidad de respuesta y la resolución) no hay efecto. Whitaker y sus coautores (2019), con datos de 150 empresas, asocian la tercerización de la atención con menos satisfacción, sin significación estadística en las empresas de servicios. Se conocen por sus abstracts. Lo que sí sale de la norma es que la relación se escribe como contrato, con sus objetivos.

## Cómo lo modela un sistema

En un sistema, un acuerdo interno se modela igual que uno con el cliente: objetivos de tiempo, un calendario y estados que pausan, pero aplicado a un tramo del caso y no al caso entero. El tramo empieza cuando el caso se asigna a un equipo o se le pide algo a un proveedor, y termina cuando vuelve. Así se ve en qué tramo se fue el tiempo cuando el acuerdo con el cliente vence (lectura de esta base).

Tres datos hacen falta para eso: a quién está asignado el caso en cada momento, desde cuándo y con qué acuerdo interno. Si el proveedor trabaja con su propio sistema, el caso guarda la referencia del pedido en el sistema del proveedor y la fecha en que se lo pidió.

> [!NOTE] Sin fuente todavía: una fuente primaria que describa cómo se encadenan los tiempos de los acuerdos internos dentro del acuerdo con el cliente.

## Dónde fallan los acuerdos internos

Fallan cuando no existen: el primer nivel promete y el resto trabaja sin plazo. Fallan cuando suman más que el acuerdo con el cliente, y el vencimiento está decidido desde que se firma. Y fallan como falla cualquier acuerdo: cada equipo cumple su tramo y el cliente igual espera, porque nadie mide el tiempo entre tramos, cuando el caso está en la cola de un equipo sin asignar (lectura de esta base). Es la versión interna del efecto descrito en [incumplimiento del acuerdo](incumplimiento-del-acuerdo.md).
