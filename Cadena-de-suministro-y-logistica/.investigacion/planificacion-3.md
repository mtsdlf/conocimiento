# Planificación (vertical): informe de investigación, tercera ronda (DRP)

Complementa a `planificacion.md` y `planificacion-2.md`. Alcance: la tabla por período del DRP, el neteo y cómo los pedidos planificados de un depósito pasan a ser necesidades del que lo abastece. Se hizo al escribir la nota `planificacion-de-la-distribucion.md` (2026-11-27).

Marcas: [L] texto completo o sección completa leída, [M] metadatos o abstract, [S] resumen secundario o del buscador.

## Fuentes de esta ronda

| Id | Fuente | URL | Marca |
|---|---|---|---|
| H1 | Gershwin, S. B., *Material Requirements Planning*, diapositivas del curso MIT 2.853/2.854 Introduction to Manufacturing Systems (© 2002-2006; publicado en MIT OpenCourseWare, otoño de 2016). Fuente primaria declarada: Hopp y Spearman, *Factory Physics* | https://ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/4eec617bb52d64f4ea1bed6d9905bc00_MIT2_854F16_MatrialRequire.pdf | [L] las 43 diapositivas (texto extraído con pdftotext) |
| H2 | Documentación de ayuda de un ERP comercial, versión 4.6C, «Distribution Resource Planning (DRP)» | https://help.sap.com/saphelp_46c/helpdata/en/84/f1065301f011d295a90000e81d646f/content.htm | [L] la página entera (resumen del lector con citas literales) |
| H3 | Domański, R. y Adamczak, M., *Planning of material flows in the supply chain based on algorithms of ERP systems* (diapositivas de un curso de DRP I, alojadas en la Universidad de Óbuda) | https://old2.kgk.uni-obuda.hu/sites/default/files/Planning-of-material-flows-in-the-supply-chain-based-on-algorithms-of-ERP.pdf | [S] solo el resumen del buscador: el servidor rechazó la conexión (ECONNREFUSED por https, tiempo agotado por http). El caso de dos minoristas y un mayorista y sus números NO se leyeron |

## H1: la lógica de neteo (MRP), literal

- Demanda: «... from outside the system is independent demand.» «... for components or raw material is dependent demand.» (diap. 3)
- Tiempo: «In some MRP systems, time is divided into time buckets — days, weeks, or whatever is convenient.» (diap. 6)
- Empujar y tirar: «Push system: one in which material is loaded based on planning or forecasts, not on current demand. ⋆ MRP is a push system.» «Pull system: one in which production occurs in response to the consumption of finished goods inventory by demand.» (diap. 8)
- Definiciones del plan maestro (diap. 10): «Gross requirements: What must be delivered in the future, and when.» «On-hand inventory: Finished good already available.» «Net requirements: (Gross requirements) – (On-hand inventory).»
- Ejemplo de neteo (diap. 11), semanas 1 a 8, stock inicial 30:

| Semana | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Gross requirements | 15 | 20 | 50 | 10 | 30 | 30 | 30 | 30 |
| Projected on-hand (30 al inicio) | 15 | -5 | | | | | | |
| Net requirements | 0 | 5 | 50 | 10 | 30 | 30 | 30 | 30 |

  «15 of the initial 30 units of inventory are used to satisfy Week 1 demand.» «The remaining 15 units are 5 less than required to satisfy Week 2 demand.»
- Lote (diap. 12): «Lot sizes are 75. The first arrival must occur in Week 2.» «75 units last until Week 4, so plan arrival in Week 5.» «Similarly, deliveries needed in Weeks 5 and 7.» Fila «Planned order receipts»: 30 (inicial), 0, 75, 0, 0, 75, 0, 75, 0 para las semanas 0 a 8; acumulados de necesidades 15, 35, 85, 95, 125, 155, 185, 215; acumulado de recepciones 30, 105, 105, 105, 180, 180, 255, 255.
  - Nota de lectura: la diapositiva dice en el texto que las llegadas son en las semanas 2, 5 y 7, y la fila de la tabla extraída queda corrida una columna por el valor inicial 30. Lo que es seguro: tres lotes de 75 que llegan en las semanas 2, 5 y 7.
- Desfase por plazo (diap. 14): «Lead times are 1 week. Therefore, order release must occur one week before delivery is required.» Fila «Planned release»: 75, 0, 0, 75, 0, 75, 0, 0 (semanas 1 a 8), es decir, lanzamientos en las semanas 1, 4 y 6.
- Dinámica del stock (diap. 19): «It = It−1 − Dt, as long as It−1 − Dt ≥ 0»; «It = It−1 − Dt + St, if It−1 − Dt < 0», «where St is minimal amount needed to make the inventory positive, which is consistent with lot-sizing requirements.»
- Reglas de lote (diap. 23): «Lot-for-lot: produce in a period the net requirements for that period. Maximum setups.» «Fixed order period: produce in a period the net requirements for P periods.» «Fixed order quantity: always produce the same quantity, whenever anything is produced. EOQ formula can be used to determine lot size.»
- Explosión (diap. 25): «The planned order releases for Level 0 are the gross requirements for Level 1.» «Do the same for Level 2, 3, etc.»
- Incertidumbre (diap. 26-27): «MRP is deterministic but reality is not. Therefore, the system needs safety stock and safety lead times.» «Instead of having a minimal planned inventory of zero, the (positive) safety stock is the planned minimal inventory level.»
- Nerviosismo (diap. 31, 33): «Nervousness — drastic changes in schedules due to small deviations from plans». «Solution: Freeze the early part of the schedule (ie, the near future).» «But: What price is paid for freezing?»
- Problema de fondo (diap. 34): el modelo es «deterministic» e «infinite capacity»; «it frequently produces non-optimal or infeasible schedules» y «it requires constant manual intervention to compensate for poor schedules».
- Jerarquía de planes (diap. 38, 40-42): «Higher levels deal with longer time scales and more of the system (scope).» «Higher levels use more aggregated (coarse-grained) models.» «Higher levels send production targets down to lower levels.» Largo plazo: «Range: six months to five years.» «Recalculation frequency: 1/month to 1/year.» «Detail: part family.», con pronóstico, planificación de recursos y «Aggregate planning — determines rough estimates of production, staffing, etc.» Plazo intermedio: «Demand management — converts long range forecast and actual orders into detailed forecast.», plan maestro, capacidad gruesa y CRP. Corto plazo: plan diario y control de planta. Problemas (diap. 43): «The high level and low level models sometimes don't match.»

## H2: un ERP comercial, como evidencia de cómo lo implementa un sistema

- Objetivos: «To improve customer service levels by anticipating customer demand at distribution centers», «To provide an accurate requirements plan for manufacturing.», «To optimize the distribution of available stock in the distribution network using the deployment function.»
- Neteo: «During the net requirements calculation the system compares the available stock and the planned receipts»; «If there is a material shortage (available stock is less than the quantity required), the system creates an order proposal.»
- Prerrequisitos: «Set up a distribution network, including identification of quota arrangements and lead times.» «Define MRP parameters in the material master record for all materials in the distribution network.»
- Pasos: pronóstico de necesidades para centros de distribución y plantas, que pasa a la gestión de la demanda como necesidades independientes planificadas, y la corrida del DRP las convierte en solicitudes u órdenes.
- Resultado, literal: «The DRP run in the distribution centers creates calls for stock transfer purchase requisitions in the supplying plants.» «A DRP run for the supplying plants creates planned orders for production.»
- Alcance: «The DRP process can be used for the entire supply chain including the production plants.»
- No aparece en la página: reparto justo («fair share») ni el detalle de la función de despliegue.

## H3: lo único que se tiene

- Según el resumen del buscador [S]: es un curso de DRP I de Domański y Adamczak que adapta el MRP I a redes de distribución de varios niveles; su lógica es que el programa de pedidos del eslabón de abajo se vuelve automáticamente el pronóstico de necesidades del eslabón de arriba que lo abastece. Sin citas literales ni números: no se pudo abrir.

## Qué queda para la nota

- La tabla por período y el neteo salen de H1 (MRP), que es la misma lógica; que el DRP la aplica a depósitos sale de H2 y, de forma secundaria, de H3 y del glosario del CSCMP (en `fundamentos-y-contraria-2.md`).
- El paso de pedidos planificados de un depósito a necesidades brutas del central tiene: H1 para el análogo en la lista de materiales (literal), H2 para el sistema (literal: solicitudes de traslado en la planta que abastece) y H3 [S].
- No hay un ejemplo numérico de DRP con dos depósitos y un central leído en una fuente: el de la nota es ejemplo de la base, armado con la lógica de H1.

## Huecos

- H3 completo (el caso de dos minoristas y un mayorista).
- Martin (1983), el texto de origen del DRP: sigue sin leerse.
- Reparto del stock escaso entre depósitos (reparto justo, «fair share»): sin fuente.
