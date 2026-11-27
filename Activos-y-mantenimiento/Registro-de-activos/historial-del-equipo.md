---
resumen: >-
  El historial del equipo es lo que le pasó a cada equipo a lo largo de su vida: las órdenes de trabajo cerradas, las fallas con su modo y su causa, los repuestos que se le cambiaron, dónde estuvo instalado y las lecturas de sus medidores. De él salen los indicadores y la decisión de seguir reparando o reemplazar, y por eso vale tanto como la calidad de lo que se cargó al cerrar cada orden.
estado: vigente
estabilidad: estable
fuentes:
  - "Wikipedia, Reliability-centered maintenance (resumen): https://en.wikipedia.org/wiki/Reliability-centered_maintenance"
  - "Wikipedia, ISO 14224 (resumen; solo remite a la página de ISO): https://en.wikipedia.org/wiki/ISO_14224"
  - "Leveraging FMMEA for Digital Twin Development: A Case Study on Intelligent Completion in Oil and Gas, Sensors 25(18), 2025, 5846, tablas 2 a 4 y secciones 2.6 a 2.8 y 3.5 a 3.8 (reproducen tablas de la ISO 14224:2016): https://doi.org/10.3390/s25185846"
  - "Hodkiewicz, Lukens, Brundage y Sexton, Rethinking Maintenance Terminology for an Industry 4.0 Future, Int. J. Prognostics and Health Management 12(1), 2021, tablas 5 a 7 (método de detección de la ISO 14224): https://doi.org/10.36001/ijphm.2021.v12i1.2932"
  - "Reliable Media (Reliamag), Maintenance and Reliability KPI Reference (resumen): https://reliamag.com/topics/guides/maintenance-reliability-kpi-reference"
  - "DOE/FEMP, O&M Best Practices Guide, cap. 5 «Types of Maintenance Programs» (Release 3.0), sec. 5.4: https://www1.eere.energy.gov/femp/pdfs/OM_5.pdf"
  - "ERPNext, Asset Repair (como evidencia de práctica, resumen): https://docs.frappe.io/erpnext/user/manual/en/asset-repair"
  - "ERPNext, Asset Maintenance (como evidencia de práctica, resumen): https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance"
  - "SAP Help 4.6C, Equipment at Functional Locations (como evidencia de práctica, resumen): https://help.sap.com/saphelp_46c/helpdata/en/01/d546244ab311d189740000e8322d00/content.htm"
  - "Activos-y-mantenimiento/.investigacion/registro-y-desempeno.md (2026-11-27), primera y segunda ronda"
  - "Activos-y-mantenimiento/.investigacion/verificacion-registro-y-desempeno.md (2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/estrategia-y-fundamentos.md (2026-11-27), componente A"
aliases: [historia del equipo, historial de mantenimiento, maintenance history, equipment history, bitácora del equipo, hoja de vida del equipo, código de falla, failure code, modo de falla, failure mode, causa de falla, failure cause, mecanismo de falla, failure mechanism, problema causa remedio, problem cause remedy, medidor, meter, contador, counter, punto de medida, measuring point, horómetro]
creado: 2026-11-27
revisado: 2026-11-27
---

# Historial del equipo

El historial del equipo es lo que le pasó a cada equipo a lo largo de su vida: las órdenes de trabajo cerradas, las fallas con su modo y su causa, los repuestos que se le cambiaron, dónde estuvo instalado y las lecturas de sus medidores. De él salen los indicadores y la decisión de seguir reparando o reemplazar, y por eso vale tanto como la calidad de lo que se cargó al cerrar cada orden.

Es la parte del [registro de activos](registro-de-activos.md) que crece. Lo escribe el [cierre de la orden](../Orden-de-trabajo/cierre-de-la-orden.md); lo leen los [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md), el análisis de [reparar o reemplazar](../Desempeno-de-los-activos/reparar-o-reemplazar.md) y quien revisa la [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md). Sin software, es la hoja de vida de la máquina: una carpeta o un cuaderno con cada intervención anotada.

## De qué está hecho el historial

El historial no es un documento propio: es la suma de hechos fechados que otros documentos dejan sobre el equipo. Como criterio de la base, son cuatro clases:

| Hecho | Qué deja | De dónde viene |
|---|---|---|
| Trabajo hecho | fecha, tipo de mantenimiento, horas, repuestos, costo, texto del técnico | cada [orden de trabajo](../Orden-de-trabajo/orden-de-trabajo.md) cerrada |
| Falla | qué dejó de hacer el equipo, de qué forma y por qué | la orden correctiva, al cerrarse |
| Movimiento | dónde estuvo instalado y entre qué fechas | la instalación y el desmontaje, en la [jerarquía de activos](jerarquia-de-activos.md) |
| Lectura | horas de marcha, kilómetros, ciclos, temperatura, vibración | un medidor, a mano o con un sensor |

Un sistema de mantenimiento de referencia, según un resumen de su ayuda, guarda cada período de instalación en una lista de uso que forma parte del historial del equipo. Un sistema abierto registra cada reparación con la fecha de falla, una descripción de la falla en texto libre, los repuestos y facturas que dan el costo, las acciones realizadas y la fecha de fin; no tiene códigos de falla estructurados.

## Cómo se codifica una falla

Para que las fallas se puedan contar hay que describirlas con códigos y no solo con texto. La ISO 14224 distingue tres cosas que el texto libre suele mezclar. Las definiciones que siguen son las que recoge un artículo revisado que usa las tablas de la norma, en su sección 2; los ejemplos son de la base:

- Modo de falla: «the manner in which failure occurs», cómo se manifiesta, lo que el operador ve. «No arranca», «pierde por el sello», «vibra».
- Mecanismo de falla: «the process that leads to failure», que puede ser físico, químico, lógico o una combinación. Desgaste, corrosión.
- Causa de falla: «the circumstances during design, manufacturing, or use that led to the failure». Montaje incorrecto, operación fuera de diseño.

La norma trae las tres listas con códigos. Los modos son por clase de equipo (tablas B.7 para equipo mecánico, B.8 para eléctrico, B.10 para submarino y B.11 para terminación de pozos), con códigos de tres letras como FTS (failure to start on demand), ELP (external leakage, process medium), ELU (external leakage, utility medium), FTO y FTC (failure to open y to close on demand). Los mecanismos son una sola lista (tabla B.2), con familias numeradas como 1 Mechanical failure (1.1 leakage, 1.2 vibration, 1.4 deformation, 1.6 sticking). Las causas son otra (tabla B.3), en cinco grupos: de diseño, de fabricación o instalación, de operación o mantenimiento, de gestión y otras. Las listas de mecanismos y de causas tienen un renglón «general» para cuando no se sabe más, y el artículo evita usarlos porque dificultan encontrar la causa. La tabla de mecanismos aclara que si el modo a nivel de equipo se codificó como fuga, conviene usar «a more causally oriented failure mechanism» y, si se codificó como vibración, registrar la causa raíz, «wherever possible».

El RCM, según su resumen en Wikipedia, pide identificar los «dominant failure modes and causes» de cada equipo y arranca con un análisis de modos de falla, efectos y criticidad (FMECA). Sin modos y causas registrados, ese análisis se hace de memoria.

Una forma más corta, que se usa al cerrar la orden, es la terna problema, causa y remedio: qué se encontró, por qué, qué se hizo. Como criterio de la base, cada uno conviene que salga de una lista cerrada que dependa de la clase de equipo, para que «no arranca» de un motor no se compare con «no arranca» de una válvula.

Un artículo sobre terminología de mantenimiento agrega que la ISO 14224 recomienda un campo «Detection Method» al crear la orden, con 11 códigos (entre ellos mantenimiento periódico e inspección), y que en la práctica ese campo «is seldom captured or is unreliably populated»: en las cinco empresas que muestra, el método de detección falta entre el 60 % y el 98 % de las órdenes en las cuatro que tienen el campo.

> [!NOTE] Sin fuente todavía: una fuente que describa la terna problema, causa y remedio como la usa un sistema de mantenimiento. Las tablas de la ISO 14224 (anexo B) se leyeron solo en los extractos de un artículo revisado, no en la norma, que es de pago; el cuidado de que la lista dependa de la clase de equipo y el uso de la terna al cerrar la orden son criterio de la base.

## Lecturas y contadores

Un medidor guarda una magnitud del equipo a lo largo del tiempo. Los hay de dos clases: los contadores, que solo suben (horas de marcha, kilómetros, ciclos, piezas producidas), y las mediciones, que suben y bajan (temperatura, presión, vibración, espesor). Como criterio de la base, los contadores alimentan el preventivo por uso y el cálculo del tiempo de operación; las mediciones alimentan el [mantenimiento por condición](../Estrategia-de-mantenimiento/mantenimiento-por-condicion.md).

Según la guía del DOE, el preventivo se dispara por calendario o por tiempo de marcha del equipo, «like calendar time or equipment run time»; para dispararlo por uso hace falta un contador con lecturas al día. La documentación leída de un sistema abierto de gestión general solo describe preventivo por calendario y no menciona medidores. Como inferencia con apoyo débil, el preventivo por uso sería capacidad del mantenimiento industrial y no del sistema de gestión general.

> [!NOTE] Sin fuente todavía: cómo modelan los sistemas de mantenimiento los puntos de medida y los contadores (vuelta del contador, reemplazo del medidor, lecturas estimadas). Las páginas probadas no devolvieron contenido (la ayuda de SAP y la de IBM son de carga dinámica), y la de Odoo 17 no menciona medidores.

## Por qué los historiales suelen no servir

El dato de falla lo carga el técnico al cerrar la orden, y lo aprovecha meses después quien analiza. Esa asimetría, que ya plantea la [entrada del tema](../activos-y-mantenimiento.md), explica muchos historiales inútiles. Como criterio de la base, los síntomas son estos:

- Todo es «otros». Si la lista de causas es larga y tiene un «otros», el técnico apurado elige «otros». Un historial con la mitad de las fallas en «otros» no dice nada.
- Texto libre sin código. «Se cambió rodamiento» en una orden y «rod. lado acople» en otra no se pueden sumar sin leerlas una por una.
- La orden se cierra tarde o en bloque. Cuando el supervisor cierra cincuenta órdenes el viernes, las horas y las causas son estimaciones.
- La falla queda en el equipo equivocado. Si la orden se carga sobre la línea entera o sobre el sistema, no sobre el equipo, el nivel donde se comparan las fallas queda vacío.
- Se confunde reparable con no reparable. Una guía de indicadores advierte que confundir el tiempo medio entre fallas (de equipos que se reparan) con el tiempo medio hasta la falla (de los que se tiran) es «one of the most common errors in maintenance reporting». El historial tiene que saber cuál es cuál.

Lo que hace útil al historial se decide al diseñar el cierre: pocos códigos, dependientes de la clase de equipo, y el equipo correcto en la orden. Está en [cierre de la orden](../Orden-de-trabajo/cierre-de-la-orden.md).
