---
resumen: >-
  Un problema es la causa, conocida o sospechada, de uno o más casos: cuando los casos se repiten, se los junta en un problema para buscar su causa raíz y arreglarla, en vez de resolver cada caso por separado. El campo tiene dos tradiciones para ese paso: la gestión de problemas de ITIL, con el error conocido y la solución provisoria, y el análisis de reclamos de la ISO 10002.
estado: borrador
estabilidad: estable
fuentes:
  - "Atlassian, «Problem management process»: https://www.atlassian.com/itsm/problem-management/process (según resúmenes del buscador; comercial)"
  - "BMC, «ITIL problem management»: https://dev.blogs.bmc.com/itil-problem-management/ (según resúmenes del buscador; comercial)"
  - "InvGate, «Problem management in an ITIL 4 world»: https://blog.invgate.com/problem-management-in-an-itil-4-world (según resúmenes del buscador)"
  - "ManageEngine, glosario de ITIL 4: https://www.manageengine.com/products/service-desk/itsm/itil-4-glossary-terms.html (según resúmenes del buscador)"
  - "Wikipedia, Known error: https://en.wikipedia.org/wiki/Known_error (según resúmenes del buscador)"
  - "Gobierno de Ontario, GO-ITS 38, Enterprise Problem Management Process: https://www.ontario.ca/document/go-its-38-enterprise-problem-management-process (no leída: 403)"
  - "ISO 10002:2018, vista previa del editor (introducción, definiciones y principios): https://cdn.standards.iteh.ai/samples/71580/6db527fdda0a42ac8f597ffd406e3509/ISO-10002-2018.pdf ; ficha: https://www.iso.org/standard/71580.html (según su resumen)"
  - "Price y Jaffe (2008), The Best Service Is No Service, Jossey-Bass/Wiley: https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0470189088,descCd-description.html (según la sinopsis del editor; el libro no se leyó)"
  - "Servicio-al-cliente/.investigacion/caso-y-escalamiento.md, componentes 3 y 8"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, escuelas y glosario"
  - "Servicio-al-cliente/.investigacion/calidad-del-servicio.md, sobre la cláusula 8 de ISO 10002"
aliases: [problema, gestión de problemas, problem management, causa raíz, root cause, análisis de causa raíz, root cause analysis, error conocido, known error, solución provisoria, workaround, base de errores conocidos, KEDB, casos repetidos]
creado: 2026-11-27
revisado:
---

# Problema y causa raíz

Un problema es la causa, conocida o sospechada, de uno o más casos: cuando los casos se repiten, se los junta en un problema para buscar su causa raíz y arreglarla, en vez de resolver cada caso por separado. El campo tiene dos tradiciones para ese paso: la gestión de problemas de ITIL, con el error conocido y la solución provisoria, y el análisis de reclamos de la ISO 10002.

Vive en [Escalamiento](escalamiento.md) porque nace cuando quien atiende ve que un caso se repite y lo pasa a quien puede arreglar la causa. Es la vuelta que describe la entrada del tema: el escalamiento le devuelve al [caso](../Caso/caso.md) la solución, o el aviso de que hay un problema de fondo.

## Caso y problema son dos registros distintos

En el vocabulario de ITIL, el caso se llama incidente y el problema es otra cosa: «A cause, or potential cause, of one or more incidents», según la definición de ITIL 4 que citan segundas fuentes (el glosario oficial es pago y no se leyó). En castellano común «problema» es cualquier dificultad; en este tema es la causa. El [glosario](../Fundamentos/glosario-de-servicio-al-cliente.md) marca la diferencia.

La consecuencia para un sistema, como lectura de esta base: el problema es un registro aparte, vinculado a muchos casos. El caso se puede cerrar con una solución provisoria mientras el problema sigue abierto, y cuando el problema se arregla, los casos vinculados tienen una respuesta de fondo.

## Error conocido y solución provisoria

La gestión de problemas de ITIL agrega dos términos, que se leyeron en fuentes comerciales y resúmenes y no en el texto de ITIL:

- **Solución provisoria** (workaround): reduce el impacto de un problema sin eliminar su causa raíz. Le permite al primer nivel resolver el caso del cliente mientras la causa sigue.
- **Error conocido** (known error): un problema que ya se analizó. Si arreglar la causa no conviene económicamente, el problema queda como error conocido y la solución provisoria se aplica cada vez que vuelven los casos, según un proveedor de software de gestión de servicios.

Los errores conocidos se registran en una base de errores conocidos (KEDB, por su sigla en inglés), que es lo que consulta el primer nivel para reconocer un caso ya visto. Según un resumen, ITIL 4 recuperó el control de problemas y el control de errores, que faltaban en ITIL v3 de 2011.

> [!IMPORTANT]
> Las fuentes leídas definen el error conocido de dos formas que no coinciden. Un proveedor lo define como «a problem that has a documented root cause and a workaround»; otro, como «a problem that has been analyzed but not resolved», que es también la redacción que un glosario atribuye a ITIL 4. La primera exige causa y solución provisoria documentadas; la segunda, solo el análisis. No se pudo verificar contra el glosario oficial.

Esta práctica sale de la gestión de servicios de TI. Llevarla a un producto físico es una analogía de esta base: el error conocido sería una falla conocida de un modelo o de un lote, y la solución provisoria, el ajuste que el técnico aplica mientras fábrica corrige el diseño. La calidad del producto fabricado es del tema Producción, todavía no armado.

## El análisis de reclamos de la ISO 10002

La otra tradición viene de la calidad. La ISO 10002, la norma de tratamiento de reclamos, pone entre sus propósitos «enhance the ability of the organization to identify trends and eliminate causes of complaints» (introducción, 0.1). Separa el tratamiento de cada reclamo (cláusula 7, que está en [reclamo](../Caso/reclamo.md)) del mantenimiento y la mejora (cláusula 8), que incluye recolectar la información (8.1), analizar y evaluar los reclamos (8.2) y la mejora continua (8.7). El principio de mejora es el 4.13. El texto de la cláusula 8 no se leyó: es pago, y la vista previa del editor trae solo su índice.

La norma también advierte que la falta de reclamos no prueba nada: «Complaints are a common indicator of low customer satisfaction but their absence does not necessarily imply high customer satisfaction» (3.4, nota 2).

Cómo se analizan los reclamos junto con las encuestas y la escucha de conversaciones para mejorar la atención está en [monitoreo de calidad](../Calidad-del-servicio/monitoreo-de-calidad.md). La diferencia con la gestión de problemas, como lectura de esta base: ITIL busca la causa técnica de un grupo de casos; la ISO 10002 busca tendencias en los reclamos para cambiar el producto, el servicio o el propio proceso de reclamos.

## La mejor atención es no necesitarla

Una escuela lleva la idea más lejos. Price y Jaffe, en *The Best Service Is No Service* (2008), tratan cada contacto como un dato de algo que falló antes y proponen bajar la demanda de atención atacando sus causas, según la sinopsis del editor; el libro no se leyó y sus cifras no se citan acá. Para esta escuela, el problema y la causa raíz no son un paso del escalamiento sino el objetivo de toda la atención. La posición y sus críticas están en [fundamentos](../Fundamentos/fundamentos-de-servicio-al-cliente.md).

## Dónde falla

Como lectura de esta base, sin fuente que lo mida:

- **Nadie junta los casos.** Sin una categoría consistente en [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md), los casos repetidos no se ven como repetidos.
- **La solución provisoria se vuelve permanente.** El primer nivel la aplica, el caso se cierra y las [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md) dan bien, mientras la causa sigue generando casos.
- **El problema no tiene dueño.** La causa está en otro equipo (desarrollo, fábrica, logística) y la atención no tiene cómo pedirle que la arregle; el acuerdo entre equipos que lo sostiene está en [acuerdos internos](../Niveles-de-servicio/acuerdos-internos.md).

> [!NOTE] Sin fuente todavía: el texto de la guía de gestión de problemas de ITIL 4 y del estándar GO-ITS 38 de Ontario, que se buscó y no se pudo leer; y la cláusula 8.2 de la ISO 10002, para saber qué categorías de análisis pide.
