---
resumen: >-
  Una acción correctiva elimina la causa de una no conformidad para que no se repita, a diferencia de la corrección, que arregla lo que ya salió mal. Se abre con un problema, busca la causa raíz, cambia algo en el producto, el proceso o el sistema, y se cierra solo cuando se verificó que funcionó.
estado: borrador
estabilidad: semi
fuentes:
  - "NSAI, presentación «Overview 9001:2015» (23 de septiembre de 2015), diapositiva sobre 10.2: https://www.nsai.ie/download/certification/Overview-9001-2015-presentation-23-Sep-15-Web-Compatibility-Mode.pdf"
  - "21 CFR 820.100 «Corrective and preventive action», eCFR, versión al 2026-01-01 (leída por el lector): https://www.ecfr.gov/api/versioner/v1/full/2026-01-01/title-21.xml?part=820&section=820.100"
  - "FDA, Federal Register 2024-01709, «Medical Devices; Quality System Regulation Amendments» (2 de febrero de 2024; texto del PDF): https://www.federalregister.gov/documents/2024/02/02/2024-01709/medical-devices-quality-system-regulation-amendments"
  - "FDA, preguntas frecuentes sobre el QMSR: https://www.fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions"
  - "Quality Magazine, BSI, Advisera e ISO/TC 176 N1284 sobre la acción preventiva en ISO 9001:2015 (según el buscador): https://www.slideshare.net/slideshow/iso9001-2015-andrisk/102654266"
  - "Wikipedia, «Eight disciplines problem solving» (secundaria): https://en.wikipedia.org/wiki/Eight_disciplines_problem_solving"
  - "AllAboutLean, «The History of the Eight Disciplines Problem Solving (8D)» (secundaria): https://www.allaboutlean.com/8d-history/"
  - "Wikipedia, «Five whys» (secundaria; cita a Ohno, Toyota Production System, 1988): https://en.wikipedia.org/wiki/Five_whys"
  - "Card, A. J., «The problem with '5 whys'», BMJ Quality & Safety 2017;26(8):671-677 (solo la ficha y resúmenes): https://doi.org/10.1136/bmjqs-2016-005849"
  - "ASQ, «Fishbone» (según el buscador; la página da 403): https://asq.org/quality-resources/fishbone"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.3.3.6: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Produccion/.investigacion/calidad.md (sección 5) y calidad-2.md (secciones 2 y 6); fundamentos-y-contraria.md (Card), 2026-11-27"
aliases: [acción correctiva, corrective action, acción preventiva, preventive action, corrección, correction, CAPA, corrective and preventive action, causa raíz, root cause, análisis de causa raíz, root cause analysis, RCA, 8D, ocho disciplinas, eight disciplines, G8D, TOPS, 5 porqués, cinco porqués, five whys, 5 whys, diagrama de Ishikawa, espina de pescado, fishbone diagram, Ishikawa diagram, 6M, verificación de la eficacia, effectiveness check, contención, containment, QMSR]
creado: 2026-11-27
revisado:
---

# Acción correctiva

Una acción correctiva elimina la causa de una no conformidad para que no se repita, a diferencia de la corrección, que arregla lo que ya salió mal. Se abre con un problema, busca la causa raíz, cambia algo en el producto, el proceso o el sistema, y se cierra solo cuando se verificó que funcionó.

Es la pieza de mejora de [Calidad](calidad.md), la que según la trilogía de Juran baja el nivel crónico en lugar de apagar un pico. La alimentan la [no conformidad](no-conformidad.md) que se repite, las señales del [control estadístico de procesos](control-estadistico-de-procesos.md) y el [reclamo](../../Servicio-al-cliente/Caso/reclamo.md) que llega por [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md). APQC 7.4 la nombra en 4.3.3.6 «Perform root cause analysis».

## Corrección, acción correctiva y acción preventiva

Un sistema tiene que separar las tres:

| | Sobre qué actúa | Ejemplo de la base |
|---|---|---|
| Corrección | lo que ya salió mal | reprocesar las 200 piezas con el agujero corrido |
| Acción correctiva | la causa de un problema que ya pasó | cambiar el sujetador que deja mover la pieza y agregar un control en primera pieza |
| Acción preventiva | la causa de un problema que todavía no pasó | revisar las otras máquinas con el mismo sujetador |

**ISO 9001:2015 no tiene una cláusula de acción preventiva.** La presentación de NSAI lo dice así sobre la 10.2: «Does not include a clause on Preventive action as an emphasis on risk-based thinking throughout the standard supersedes a single clause on preventive action». Según la misma fuente, la 10.2 pide «taking action to control and correct nonconformity and address the consequences, determining if similar nonconformities exist or could happen, making changes to QMS if necessary».

Las fuentes secundarias lo leen de dos maneras. Para algunas (BSI, Advisera, Quality Magazine), la acción preventiva fue reemplazada por las acciones para abordar riesgos y oportunidades. Para un documento del comité ISO/TC 176, quedó absorbida: está incorporada cuando el sistema se basa en riesgos. El anexo A.3 de la norma, que lo explica, no se leyó.

En los dispositivos médicos la preventiva sigue separada. Según la FDA, ISO 13485:2016 «has one Clause outlining expectations regarding corrective action (Clause 8.5.2) and has another Clause outlining the expectations regarding preventive action (Clause 8.5.3)».

## CAPA: el patrón de los dispositivos médicos

CAPA (corrective and preventive action) es el nombre que la regulación de dispositivos médicos de los Estados Unidos le da al proceso. El texto de 21 CFR 820.100, en su versión al 1 de enero de 2026, según una lectura automática que falta recotejar con el eCFR, pide procedimientos que cubran siete puntos:

1. Analizar procesos, quejas, producto devuelto y otros datos de calidad, con métodos estadísticos cuando haga falta.
2. Investigar la causa.
3. Identificar la acción necesaria.
4. Verificar o validar que la acción es eficaz y no perjudica al producto terminado.
5. Implementar y registrar los cambios de métodos y procedimientos.
6. Comunicar la información a los responsables.
7. Llevarla a la revisión por la dirección.

El apartado (b) pide documentar todas las actividades y sus resultados.

**Desde el 2 de febrero de 2026 rige otra regla.** El Federal Register de 2024 dice: «This rule is effective February 2, 2026». La nueva regulación (QMSR) incorpora ISO 13485:2016 por referencia. Según la FDA, los puntos 6 y 7 de 820.100 no figuran en ISO 13485, pero su sustancia está cubierta por las cláusulas 8.2.2, 8.5.2 y 8.3.1.

> [!NOTE] Sin fuente todavía: si la sección 820.100 fue derogada o reemplazada en el CFR después del 2 de febrero de 2026. El texto leído no traía aviso de reemplazo. La lista de siete puntos sigue sirviendo como patrón abierto de un proceso de CAPA, aunque haya dejado de ser la norma.

## El 8D: ocho disciplinas para un problema

El 8D ordena la acción correctiva en pasos para un equipo. Según fuentes secundarias (Wikipedia y AllAboutLean), nació en Ford: el manual «Team Oriented Problem Solving» (TOPS) «was first published in 1987». La versión vigente en Ford se llama G8D. El manual original no se leyó.

| Disciplina | Qué se hace, según las fuentes secundarias |
|---|---|
| D0 | prepararse y tomar acciones de emergencia (agregada después del original) |
| D1 | formar un equipo con conocimiento del producto y el proceso |
| D2 | describir el problema en términos cuantificables: quién, qué, dónde, cuándo, por qué, cómo y cuántos (5W2H) |
| D3 | definir e implementar la contención, para aislar el problema de cualquier cliente |
| D4 | encontrar y verificar la causa raíz y el punto de escape: por qué el defecto pasó sin detectarse |
| D5 | elegir y verificar la solución permanente |
| D6 | implementar la acción correctiva |
| D7 | prevenir la recurrencia cambiando sistemas, prácticas y procedimientos |
| D8 | cerrar y reconocer al equipo |

Las dos fuentes nombran distinto D5 y D6. El punto de escape es lo que el 8D agrega a otros métodos: no alcanza con saber por qué se hizo mal la pieza, también por qué la inspección la dejó pasar, y eso puede cambiar el [plan de inspección](plan-de-inspeccion.md) (lectura de la base).

> [!IMPORTANT] El origen está discutido. AllAboutLean conjetura que Ford, como proveedor militar, «was probably heavily influenced» por la MIL-STD-1520C de 1986, que trata la acción correctiva con un comité de revisión. Otras fuentes secundarias lo niegan o lo vinculan con el método de Kepner-Tregoe. Lo único comprobado es que la 1520C existe y es anterior a TOPS.

## Los 5 porqués y su crítica

La técnica pregunta «por qué» en cadena hasta llegar a una causa sobre la que se puede actuar. Wikipedia cita a Ohno: el método es «the basis of Toyota's scientific approach by repeating why five times», y así «the nature of the problem as well as its solution becomes clear». La frase del libro (*Toyota Production System*, 1988) no se verificó.

La crítica más citada es de Card, en *BMJ Quality & Safety* (2017), desde la seguridad del paciente. Según Wikipedia: «The arbitrary depth of the fifth why is unlikely to correlate with the root cause». Según un fragmento del resumen, la técnica «probably owes its place in the curriculum and practice of RCA to a combination of pedigree, simplicity and pedagogy». Según otro resumen, Card concede su valor para enseñar pero la desaconseja para investigaciones reales: una cadena de porqués da una sola vía causal, y otro equipo puede armar otras cinco igual de válidas. El artículo no se leyó entero, y llevarlo a la fábrica es inferencia de la base.

Wikipedia suma otras: se queda en los síntomas, depende de quien pregunta y no da lo mismo con dos investigadores.

## El diagrama de Ishikawa

El diagrama de causa y efecto, o de espina de pescado, ordena las causas posibles de un efecto por categorías. Según ASQ (por el buscador), se llama así «because Kaoru Ishikawa developed it» e «illustrates the main causes and subcauses leading to an effect». La versión de Ishikawa usaba seis categorías, las 6M: materiales, máquinas, métodos, medición, mano de obra y medio ambiente. Es la alternativa que propone Card para no quedarse con una sola cadena.

> [!NOTE] Sin fuente todavía: el año y el libro de origen del diagrama de Ishikawa.

## Adónde llega una acción correctiva

La salida de una acción correctiva es un cambio que queda. Según dónde esté la causa:

- **En el diseño del producto o en la ruta**: un [cambio de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md) de la lista de materiales o la ruta de fabricación, con su vigencia.
- **En el control**: una línea nueva o una frecuencia distinta en el [plan de inspección](plan-de-inspeccion.md).
- **En el proveedor**: un reclamo y un dato para su [evaluación](../../Compras-y-abastecimiento/Proveedores/evaluacion-de-proveedores.md), en Compras.
- **En la máquina**: un pedido a [Activos y mantenimiento](../../Activos-y-mantenimiento/activos-y-mantenimiento.md).
- **En el sistema**: un procedimiento o una instrucción que cambia, que es lo que la 10.2 llama «making changes to QMS».

## Cómo falla una acción correctiva

- **Se cierra sin verificar la eficacia.** Se implementa el cambio y se da por cerrada. La verificación es un requisito explícito del punto 4 de 820.100; sin ella, el mismo defecto reaparece meses después con otro número de caso (lo segundo es criterio de la base).
- **Se confunde la corrección con la acción.** Se reprocesó el lote y se anota como acción correctiva. La causa sigue ahí.
- **Se salta la contención.** Se busca la causa mientras el stock afectado sigue saliendo. El 8D la pone en D3, antes de la causa; la [trazabilidad de lotes](trazabilidad-de-lotes.md) dice qué apartar.
- **La causa raíz es «error humano».** Es el final típico de una cadena de porqués corta; no dice qué cambiar en el proceso para que el error no sea posible (criterio de la base).

## Qué guarda una acción correctiva

- Número, origen (no conformidad, reclamo, auditoría, señal del proceso) y vínculo con los registros de origen.
- Descripción cuantificada: qué, dónde, cuándo, cuánto.
- Responsable y equipo.
- Corrección y contención, con fecha y alcance (qué lotes, qué stock).
- Causas candidatas, causa raíz y punto de escape, con el método usado y la evidencia.
- Acción correctiva, y preventiva si la hay, con responsable y fecha límite.
- Cambios que produjo (cambio de ingeniería, plan de inspección, procedimiento).
- Verificación de la eficacia: cómo se midió, cuándo y con qué resultado.
- Estado y cierre, con quién lo aprobó.
