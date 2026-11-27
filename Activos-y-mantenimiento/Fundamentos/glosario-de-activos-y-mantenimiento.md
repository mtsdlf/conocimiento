---
resumen: >-
  Los términos del tema Activos y mantenimiento, cada uno con su nombre en inglés, una definición corta y la nota donde vive, agrupados por la parte del dominio a la que pertenecen.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, Corrective maintenance (cita NF EN 13306; según su resumen): https://en.wikipedia.org/wiki/Corrective_maintenance"
  - "NASA, Reliability Centered Maintenance Guide for Facilities and Collateral Equipment, copia de febrero de 2000, glosario: https://everyspec.com/NASA/NASA-General/download.php?spec=NASA_RCM_GUIDE_2000.030306.pdf"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), categorías 10.0 y 6.3: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/ (informes del 2026-11-27)"
aliases: [glosario de mantenimiento, maintenance glossary, términos de mantenimiento, vocabulario de mantenimiento]
creado: 2026-11-27
revisado:
---

# Glosario de activos y mantenimiento

Los términos del tema Activos y mantenimiento, cada uno con su nombre en inglés, una definición corta y la nota donde vive, agrupados por la parte del dominio a la que pertenecen.

El campo tiene una norma de terminología, la EN 13306, que esta base no leyó; los sistemas, además, usan nombres distintos para lo mismo (aviso, solicitud, pedido). Estas son las palabras que usa la base, en un sentido cada una. La definición completa y sus fuentes están en la nota de la columna «Dónde»; el contexto del campo, en [fundamentos de activos y mantenimiento](fundamentos-de-activos-y-mantenimiento.md).

## El dominio entero

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Mantener | Maintain | Conservar un equipo en la condición en que cumple su función, o devolverlo a ella cuando la pierde | [activos y mantenimiento](../activos-y-mantenimiento.md) |
| Activo | Asset | Según la ISO 55000, algo con valor potencial o real para una organización; en este tema, el activo físico que se mantiene | [fundamentos](fundamentos-de-activos-y-mantenimiento.md) |
| Gestión de activos | Asset management | Sistema de gestión de los activos a lo largo de su vida, del que el mantenimiento es una parte; lo norma la serie ISO 55000 | [fundamentos](fundamentos-de-activos-y-mantenimiento.md) |
| Sistema de mantenimiento | CMMS, EAM | El software que lleva equipos, planes y órdenes; sus categorías (CMMS, EAM) son del tema Software de gestión, todavía no armado | [activos y mantenimiento](../activos-y-mantenimiento.md) |

## Registro de activos

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Registro de activos | Asset register, equipment master | Lo que se guarda de cada equipo: qué es, dónde está, de qué está hecho, cuánto importa y qué le pasó | [registro de activos](../Registro-de-activos/registro-de-activos.md) |
| Equipo | Equipment | El objeto físico mantenible, con su número de serie, que puede cambiar de lugar | [jerarquía de activos](../Registro-de-activos/jerarquia-de-activos.md) |
| Ubicación técnica | Functional location | El lugar donde se instala un equipo, que conserva su historia aunque el equipo cambie | [jerarquía de activos](../Registro-de-activos/jerarquia-de-activos.md) |
| Jerarquía de activos | Asset hierarchy | El árbol de niveles (planta, sistema, equipo, componente); la ISO 14224 propone nueve | [jerarquía de activos](../Registro-de-activos/jerarquia-de-activos.md) |
| Componente mantenible | Maintainable item | La parte de un equipo que se repara o se cambia como unidad | [jerarquía de activos](../Registro-de-activos/jerarquia-de-activos.md) |
| Lista de repuestos del equipo | Maintenance BOM, equipment BOM | Los repuestos que lleva un equipo, para pedirlos sin buscarlos en cada orden | [jerarquía de activos](../Registro-de-activos/jerarquia-de-activos.md) |
| Criticidad | Criticality | Cuánto importa que falle un equipo, por consecuencia y probabilidad | [criticidad](../Registro-de-activos/criticidad.md) |
| Matriz de riesgo | Risk matrix, criticality matrix | La tabla de consecuencia por probabilidad que califica la criticidad | [criticidad](../Registro-de-activos/criticidad.md) |
| Historial del equipo | Equipment history, maintenance history | Lo que le pasó al equipo: órdenes cerradas, fallas codificadas, lecturas | [historial del equipo](../Registro-de-activos/historial-del-equipo.md) |
| Modo de falla | Failure mode | Cómo se manifiesta una falla: «no arranca», «pierde por el sello» | [historial del equipo](../Registro-de-activos/historial-del-equipo.md) |
| Mecanismo de falla | Failure mechanism | El proceso físico que la produjo: desgaste, corrosión, fatiga | [historial del equipo](../Registro-de-activos/historial-del-equipo.md) |
| Causa de falla | Failure cause | Por qué ocurrió el mecanismo: lubricación insuficiente, mal montaje | [historial del equipo](../Registro-de-activos/historial-del-equipo.md) |
| Problema, causa y remedio | Problem, cause, remedy | La terna corta que se carga al cerrar una orden | [historial del equipo](../Registro-de-activos/historial-del-equipo.md) |
| Medidor, contador | Meter, counter | Una magnitud del equipo registrada en el tiempo; el contador solo sube (horas, kilómetros, ciclos) | [historial del equipo](../Registro-de-activos/historial-del-equipo.md) |
| Horómetro | Hour meter | El contador de horas de marcha, con el que vence el preventivo por uso | [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) |

## Estrategia de mantenimiento

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Estrategia de mantenimiento | Maintenance strategy | La decisión de qué mantenimiento se le hace a cada equipo | [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) |
| Correctivo | Corrective maintenance | El que se hace después de detectar la falla; inmediato o diferido | [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) |
| Correctivo diferido | Deferred corrective maintenance | El correctivo que se demora según reglas fijadas de antemano | [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) |
| Reactivo | Reactive maintenance | El modo «run it till it breaks» de la guía del DOE: se interviene cuando el equipo falla | [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) |
| Dejar fallar | Run to failure | No intervenir hasta la falla, por decisión, porque prevenir cuesta más | [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) |
| Proactivo | Proactive maintenance | En la NASA, el que usa análisis de causa raíz, exploración de edad y FMEA | [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) |
| Mantenimiento preventivo | Preventive maintenance (PM) | El que se hace a intervalos fijados de antemano, sin esperar síntomas | [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) |
| Preventivo por calendario | Time-based maintenance | El preventivo que vence en una fecha | [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) |
| Preventivo por uso | Usage-based, meter-based maintenance | El preventivo que vence cuando un contador llega a un valor | [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) |
| Plan de mantenimiento | Maintenance plan | Las tareas de un equipo con su frecuencia; genera las órdenes al vencer | [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) |
| Ruta | Route | Tareas cortas de muchos equipos agrupadas en un solo recorrido; definición de la base, sin fuente leída | [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) |
| Mantenimiento por condición | Condition-based maintenance (CBM), predictive maintenance (PdM) | Medir el estado del equipo e intervenir cuando muestra que va a fallar; en esta base, predictivo es sinónimo | [mantenimiento por condición](../Estrategia-de-mantenimiento/mantenimiento-por-condicion.md) |
| Monitoreo de condición | Condition monitoring | Medir la condición de forma continua o casi continua, con sensores fijos que avisan cuando una lectura pasa un umbral | [mantenimiento por condición](../Estrategia-de-mantenimiento/mantenimiento-por-condicion.md) |
| Falla potencial (P) | Potential failure | Según la NASA, «An identifiable condition that indicates a failure is imminent» | [mantenimiento por condición](../Estrategia-de-mantenimiento/mantenimiento-por-condicion.md) |
| Falla funcional (F) | Functional failure | El equipo dejó de cumplir su función | [mantenimiento por condición](../Estrategia-de-mantenimiento/mantenimiento-por-condicion.md) |
| Intervalo P-F | P-F interval | El tiempo entre detectar la falla potencial y la falla funcional | [mantenimiento por condición](../Estrategia-de-mantenimiento/mantenimiento-por-condicion.md) |
| Mantenimiento centrado en la confiabilidad | Reliability-centered maintenance (RCM) | El método que elige la tarea para cada modo de falla a partir de la función | [mantenimiento centrado en la confiabilidad](../Estrategia-de-mantenimiento/mantenimiento-centrado-en-confiabilidad.md) |
| Patrones de falla | Failure patterns | Las seis curvas de probabilidad de falla según la edad, de Nowlan y Heap | [mantenimiento centrado en la confiabilidad](../Estrategia-de-mantenimiento/mantenimiento-centrado-en-confiabilidad.md) |
| Curva de la bañera | Bathtub curve | El patrón con mortalidad infantil, tramo plano y desgaste; uno de los seis | [mantenimiento centrado en la confiabilidad](../Estrategia-de-mantenimiento/mantenimiento-centrado-en-confiabilidad.md) |
| Análisis de modos y efectos de falla | FMEA (AMEF); con criticidad, FMECA | La tabla de funciones, modos de falla, causas, efectos y consecuencias | [mantenimiento centrado en la confiabilidad](../Estrategia-de-mantenimiento/mantenimiento-centrado-en-confiabilidad.md) |
| Búsqueda de fallas ocultas | Failure-finding task | Probar una protección que solo actúa cuando otra cosa falla; tarea del RCM, sin fuente leída todavía | [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) |

## Orden de trabajo

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Orden de trabajo | Work order (WO); OT | El documento que lleva un trabajo de mantenimiento del alta al cierre | [orden de trabajo](../Orden-de-trabajo/orden-de-trabajo.md) |
| Solicitud de trabajo | Work request, maintenance notification; aviso, pedido de trabajo | El pedido de que alguien mire un equipo, antes de decidir hacer el trabajo | [solicitud de trabajo](../Orden-de-trabajo/solicitud-de-trabajo.md) |
| Prioridad | Priority | La urgencia de una orden, que combina la criticidad del equipo con la de la falla | [solicitud de trabajo](../Orden-de-trabajo/solicitud-de-trabajo.md) |
| Planificar | Planning | Decidir qué se hace, cómo y con qué, antes de que el trabajo esté listo | [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md) |
| Programar | Scheduling | Decidir cuándo y quién hace cada trabajo listo | [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md) |
| Pendiente | Backlog | El trabajo aprobado que todavía no se hizo | [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md) |
| Trabajo listo | Ready backlog | El pendiente ya planificado, con repuestos y acuerdo para parar el equipo, que se puede programar | [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md) |
| Tiempo de herramienta | Wrench time | La parte de la jornada del técnico que se pasa trabajando sobre el equipo | [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md) |
| Cumplimiento del programa | Schedule compliance | La parte del programa de la semana que se hizo; definición de la base, la de SMRP no se leyó | [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md) |
| Repuestos y materiales | Spare parts, MRO materials | Lo que el trabajo consume además de horas: piezas, insumos, consumibles | [repuestos y materiales](../Orden-de-trabajo/repuestos-y-materiales.md) |
| Repuesto crítico | Critical spare | El repuesto que se tiene en stock aunque rote poco, porque su falta deja parado un equipo importante | [repuestos y materiales](../Orden-de-trabajo/repuestos-y-materiales.md) |
| Reserva | Material reservation | Apartar el stock para una orden antes de usarlo | [repuestos y materiales](../Orden-de-trabajo/repuestos-y-materiales.md) |
| Esperando materiales | Waiting for materials | El estado de la orden que no puede empezar porque falta un repuesto | [repuestos y materiales](../Orden-de-trabajo/repuestos-y-materiales.md) |
| Cierre técnico, cierre administrativo | Technical completion, close | El trabajo terminado, primero; la orden cerrada con sus costos, después | [cierre de la orden](../Orden-de-trabajo/cierre-de-la-orden.md) |
| Código de falla | Failure code | El valor de una lista cerrada que se carga al cerrar la orden | [cierre de la orden](../Orden-de-trabajo/cierre-de-la-orden.md) |
| Bloqueo y etiquetado | Lockout/tagout (LOTO) | Aislar las energías de un equipo antes de trabajar sobre él | [orden de trabajo](../Orden-de-trabajo/orden-de-trabajo.md) |

## Servicio de campo

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Servicio de campo | Field service; FSM, field service management | El mantenimiento sobre equipos de los clientes, en el lugar donde están | [servicio de campo](../Servicio-de-campo/servicio-de-campo.md) |
| Orden de servicio | Service order, work order | La orden de trabajo sobre un equipo del cliente: el trabajo pedido | [servicio de campo](../Servicio-de-campo/servicio-de-campo.md) |
| Base instalada | Installed base | El registro de cada equipo vendido o instalado que está en manos de un cliente | [base instalada](../Servicio-de-campo/base-instalada.md) |
| Número de serie | Serial number | El identificador de una unidad; de él se lee la cobertura | [base instalada](../Servicio-de-campo/base-instalada.md) |
| Contrato de servicio | Service contract, service agreement; AMC | El acuerdo que fija cobertura, precio y visitas de un equipo del cliente | [contrato de servicio](../Servicio-de-campo/contrato-de-servicio.md) |
| Garantía | Warranty | La promesa del vendedor sobre el producto, que da cobertura sin cargo por un plazo | [contrato de servicio](../Servicio-de-campo/contrato-de-servicio.md) |
| Cobertura | Entitlement | Qué del servicio no se le cobra al cliente, por garantía o contrato | [contrato de servicio](../Servicio-de-campo/contrato-de-servicio.md) |
| Acuerdo de nivel de servicio | Service level agreement (SLA) | La promesa de tiempos de respuesta o de resolución | [contrato de servicio](../Servicio-de-campo/contrato-de-servicio.md) |
| Despacho | Dispatch | Asignar una orden a un técnico y a una ventana de tiempo | [despacho y agenda](../Servicio-de-campo/despacho-y-agenda.md) |
| Ruteo | Routing | Ordenar las visitas de un técnico para reducir el viaje | [despacho y agenda](../Servicio-de-campo/despacho-y-agenda.md) |
| Visita | Visit, service appointment | La cita concreta de un técnico en casa del cliente; una orden puede tener varias | [visita técnica](../Servicio-de-campo/visita-tecnica.md) |
| Resolver en la primera visita | First-time fix | Terminar el trabajo en la primera visita, sin volver ni pedir otro repuesto | [visita técnica](../Servicio-de-campo/visita-tecnica.md) |

## Desempeño de los activos

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Tiempo medio entre fallas | Mean time between failures (MTBF) | Cuánto anda en promedio un equipo reparable entre una falla y la siguiente | [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md) |
| Tiempo medio hasta la falla | Mean time to failure (MTTF) | El equivalente para lo que no se repara | [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md) |
| Tiempo medio de reparación | Mean time to repair (MTTR) | Cuánto tarda en promedio un equipo en volver a funcionar | [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md) |
| Disponibilidad | Availability | La parte del tiempo en que el equipo está en condiciones de funcionar | [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md) |
| Cumplimiento del preventivo | PM compliance | La parte de las órdenes preventivas que se hizo en su ventana | [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md) |
| Costo sobre valor de reposición | Maintenance cost as % of replacement asset value (RAV) | Lo que cuesta mantener, comparado con lo que costaría reponer | [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md) |
| Costo del ciclo de vida | Life cycle cost (LCC) | Todo lo que cuesta un equipo desde que se compra hasta que se da de baja | [reparar o reemplazar](../Desempeno-de-los-activos/reparar-o-reemplazar.md) |
| Costo anual equivalente | Equivalent annual cost (EAC) | El costo del ciclo de vida repartido en cuotas anuales iguales, para comparar opciones | [reparar o reemplazar](../Desempeno-de-los-activos/reparar-o-reemplazar.md) |
| Vida económica | Economic life | La edad en que el costo anual equivalente es mínimo y conviene reemplazar | [reparar o reemplazar](../Desempeno-de-los-activos/reparar-o-reemplazar.md) |
| Eficiencia global del equipo | Overall equipment effectiveness (OEE) | Disponibilidad por rendimiento por calidad; mide la línea y es del tema Producción, todavía no armado | [desempeño de los activos](../Desempeno-de-los-activos/desempeno-de-los-activos.md) |

## Las siglas

| Sigla | Qué es |
|---|---|
| CMMS | *Computerized maintenance management system*: el sistema de mantenimiento |
| EAM | *Enterprise asset management*: el sistema de gestión de activos de toda la empresa |
| FSM | *Field service management*: el sistema de servicio de campo |
| RCM | *Reliability-centered maintenance*: [mantenimiento centrado en la confiabilidad](../Estrategia-de-mantenimiento/mantenimiento-centrado-en-confiabilidad.md) |
| TPM | *Total productive maintenance*: el mantenimiento productivo total, la escuela japonesa (ver [fundamentos](fundamentos-de-activos-y-mantenimiento.md)) |
| ISO 55000 | La serie de normas de gestión de activos, de 2014 (ver [fundamentos](fundamentos-de-activos-y-mantenimiento.md)) |
| ISO 14224 | La norma de taxonomía de equipos y datos de falla (ver [jerarquía de activos](../Registro-de-activos/jerarquia-de-activos.md)) |
| EN 13306 | La norma europea de terminología de mantenimiento, no leída |
| SAE JA1011 | La norma que fija qué puede llamarse RCM |
| SMRP | Society for Maintenance & Reliability Professionals, la sociedad de practicantes de mantenimiento |
| IAM, GFMAM | El Institute of Asset Management y el foro global que agrupa sociedades de gestión de activos |
