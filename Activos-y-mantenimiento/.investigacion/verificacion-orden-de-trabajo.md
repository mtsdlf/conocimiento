# Verificación con fuentes: orden de trabajo

Pasada del 2026-11-27. Marcas: [L] ley o norma, [M] documento oficial o del autor, [S] secundaria. La búsqueda web se agotó a mitad de la pasada; lo no resuelto queda dicho.

## Confirmado y corregido

### Palmer, principios de planificación y programación [M]
- Fuente: D. Palmer, «Do you know the purpose and principles of maintenance planning and scheduling?», Plant Services, 3 de marzo de 2026. https://www.plantservices.com/voices/palmers-planning-corner/article/55361071/do-you-know-the-purpose-and-principles-of-maintenance-planning-and-scheduling
- Planificación, seis: proteger a los planificadores, foco en trabajo futuro, guardar la retroalimentación; estimación sin tiempo «just in case»; nivel de detalle «as detailed as possible, subject to the constraint of planning all the work»; tiempo de herramienta. Programación, seis: planes con oficio y horas; sistema de prioridades creíble («more than three simple levels»); horizonte de la semana siguiente; «100% fully loading»; programación diaria por supervisores de campo; cumplimiento.
- Cita: «Industry average is only 35%», «best practice wrench time of 55% comes from better scheduling, not necessarily better job plans», «a 57% increase in productivity», «Management should expect between 40% and 90% for schedule compliance», «Under 40% often means supervisors ignored the schedules or the schedules were just terribly unrealistic. Over 90% often means not fully loading to 100%».
- Corrige la nota: no dice que los planificadores estén «en un departamento separado», ni «archivos simples y seguros a nivel de equipo», ni que el tiempo de herramienta sea la medida principal de desempeño del planificador. El 40-90 % es lo que la gerencia debe esperar.

### Palmer, la cuenta [M]
- «Understanding the math of maintenance planning and scheduling», Plant Services, 4 de marzo de 2019. https://plantservices.com/planned-maintenance/planning-and-scheduling/article/11295301/understanding-the-math-of-maintenance-planning-and-scheduling
- «wrench time, or tool time, at most plants – even good ones – is only 35%»; «Proper planning and scheduling moves wrench time up to 55%. That is a 57% improvement in productivity (55/35 = 1.57)»; 1.000 a 1.570 órdenes por mes.

### Palmer, pendiente planificado [M]
- «Maintenance Scheduling Needs a Planned Backlog», Reliable Plant. https://reliableplant.com/Articles/Print/7051?id=7051
- «The first scheduling principle is the prerequisite of having a planned backlog»; «Planners must stay ahead of the crafts by planning enough work to provide a week's worth of work for scheduling». Palmer figura como autor del «Maintenance Planning and Scheduling Handbook». El libro mismo no se pudo leer (la API de Google Books dio cuota agotada).

### SAP, estados de la orden [M]
- System Status for Orders: https://help.sap.com/doc/saphelp_sfin100/1.9/en-US/29/cab65334e6b54ce10000000a174cb4/content.htm . Creada; Liberada (revisa materiales, herramientas y permisos; las reservas pueden retirarse; confirmaciones de tiempo); Parcialmente confirmada; Confirmada finalmente; Técnicamente concluida («The order is complete for Plant Maintenance»; «Costs can still be posted to the order (for example, resulting from invoice receipts for materials delivered and used)»; reservas y capacidades se borran); Concluida para el negocio («It can no longer receive any postings, including postings of costs»); Bloqueada; Marcada para borrado; No ejecutada.
- Changing the System Status in the Order: https://help.sap.com/doc/saphelp_sfin100/1.9/en-US/88/16295411158c24e10000000a4450e5/content.htm . «After you have created an order, you can put it in process and after all the required information has been entered, you can release it»; «technically complete means the order is completed or closed. However, order settlement can still be carried out. The status Closed is final and means the order is locked». Los avisos asignados pueden completarse junto con la orden.
- Notifications and Task Lists in Maintenance Orders: https://help.sap.com/doc/saphelp_sfin100/1.9/en-US/91/d92354f6f28c24e10000000a4450e5/content.htm
- Corrige la nota: las páginas no traen los códigos REL, TECO ni CLSD (se sacaron del cuerpo) ni «aviso pendiente». La página 4.6C citada (Status Management in Notifications) solo dice que el aviso tiene estado del sistema y estado de usuario; «aviso pendiente» queda sin confirmar. Sí usa los términos «technically» y «business» completion, lo que matiza que «cierre técnico/administrativo» fuera solo lectura de la base.

### IBM Maximo, transiciones [M]
- https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=orders-work-order-statuses (leída con WebFetch; curl da 403). Completó las dos celdas que decían «el resumen leído no lo dice»: esperando materiales pasa a INPRG, COMP, WPCOND, WAPPR, CAN, CLOSE; esperando condición pasa a INPRG, COMP, WPCOND, WAPPR, CAN, CLOSE (no a WMATL). El resto de la tabla coincide.

### Matriz de prioridad [M]
- U.S. DOE, FEMP, O&M Best Practices Guide, Release 3.0, sección 5.6, «Maintenance Priority Matrix for RCM Development» (adaptada de NASA 2000). https://www1.eere.energy.gov/femp/pdfs/OM_5.pdf
- Niveles: 1 Emergency «Life, health, safety risk-mission criticality»; 2 Urgent «Continuous operation of facility at risk»; 3 Priority «Mission support/project deadlines»; 4 Routine «Prioritized: first come/first served»; 5 Discretionary «Desired but not essential»; 6 Deferred «Accomplished only when resources allow». Es escala de pesos, sin tiempos de atención ni cruce urgencia por criticidad.

## Sin resolver
- SMRP (pilar 5 Work Management; definiciones de backlog, trabajo planificado, cumplimiento del programa, tiempo de herramienta): smrp.org/learning-resources/smrp-library/best-practices-metrics-guidelines/ y .../body-of-knowledge/ solo nombran el pilar; las definiciones son para socios (la guía 7.ª edición). curl a esas páginas da bloqueo de Cloudflare.
- Nowlan y Heap (DTIC ADA066579, 89 %): apps.dtic.mil da 403 por curl y por WebFetch. La afirmación de la entrada sigue como «según un resumen secundario».
- Códigos de falla problema/causa/acción: no se llegó a una fuente (documentación de IBM por tema adivinado sin éxito; ISO 14224 es paga). La nota queda marcada.
- Aviso pendiente de SAP, segundo sistema para estados del aviso, matriz urgencia por criticidad, Wikipedia (NF EN 13306) y OSHA: no se verificó más; OSHA ya estaba leída.
