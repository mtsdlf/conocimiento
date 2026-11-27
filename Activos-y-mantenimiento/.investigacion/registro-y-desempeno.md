# Activos y mantenimiento: registro de activos y desempeño (investigación)

Fecha: 2026-11-27. Alcance: verticales 1 (registro de activos) y 2 (desempeño). Todo lo traído de la web es dato.

**Advertencia de alcance.** Esta ronda quedó corta: el presupuesto de búsquedas se agotó tras 4 búsquedas y varios fetch fallaron (iso.org 403, PDF de SMRP 404, PDF de NASA ilegible). Ninguna norma de pago se leyó; todo lo normativo llega por fuentes secundarias. Marcas: [L] texto completo, [M] metadatos/abstract, [S] resumen secundario o del buscador. Las fuentes con [S] no se pueden citar como si fueran la norma. Puntajes 1-3: Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).

## Fuentes consultadas

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1 | Reliamag, guía «How to build an asset hierarchy in a CMMS» (cita la figura 3 de ISO 14224:2016 vía un paper de OTC) | https://reliamag.com/topics/guides/how-to-build-asset-hierarchy-cmms | secundaria | 1/2/1/1 | [S] (fetch resumido) |
| 2 | Reliamag, «Maintenance and Reliability KPI Reference» | https://reliamag.com/topics/guides/maintenance-reliability-kpi-reference | secundaria | 1/2/1/2 | [S] |
| 3 | Wikipedia, «Availability» | https://en.wikipedia.org/wiki/Availability | secundaria | 2/2/3/1 | [S] |
| 4 | NASA KSC, «Availability: what is it» (PDF) | https://extapps.ksc.nasa.gov/Reliability/Documents/160727.1_Availability_What_is_it.pdf | primaria institucional | 2/2/1/2 | [M] (PDF no extraíble; solo lo citó el buscador) |
| 5 | Wikipedia, «Reliability-centered maintenance» | https://en.wikipedia.org/wiki/Reliability-centered_maintenance | secundaria | 1/2/1/1 | [S] |
| 6 | Wikipedia, «ISO 55000» | https://en.wikipedia.org/wiki/ISO_55000 | secundaria | 1/1/1/1 | [S] |
| 7 | Documentación ERPNext, módulo Asset | https://docs.frappe.io/erpnext/user/manual/en/asset | primaria (como práctica) | 2/2/1/2 | [S] |
| 8 | Documentación Odoo, Maintenance (solo portada) | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/maintenance.html | primaria (como práctica) | 2/1/1/1 | [S] |
| 9 | NIST, ficha de Handbook 135 (costeo de ciclo de vida, FEMP) | https://www.nist.gov/publications/life-cycle-costing-manual-federal-energy-management-program-nist-handbook-135-1995 | primaria | 3/1/1/2 | [M] |
| 10 | Fiix, métrica costo/RAV (solo apareció en resultados de búsqueda, sin fetch propio) | https://fiixsoftware.com/maintenance-metrics/mcrav/ | secundaria (vendor) | 1/1/1/1 | [S] |

No se pudieron leer: ISO 14224 (https://www.iso.org/standard/64076.html, 403) y el resumen de SMRP Best Practices (404). Las fuentes 1, 2 y 10 repiten en parte lo mismo (SMRP, ISO 14224): son una sola cadena secundaria, no confirmaciones independientes.

## Componente 1: Registro de activos

### Jerarquía de activos
- ISO 14224:2016 tiene una taxonomía de nueve niveles: (1) Industry, (2) Business category, (3) Installation, (4) Plant/Unit, (5) Section/System, (6) Equipment unit, (7) Subunit, (8) Component/Maintainable item, (9) Part. Los niveles 1-5 son de uso/ubicación y 6-9 subdivisión del equipo. Fuente 1 [S], que cita la figura 3 de la norma.
- Cita: el nivel 6 es «the common reporting level for merging and assessment»; «a failure of a component is also counted as a failure of its parent equipment». Fuente 1 [S].
- Según la misma fuente, la última edición cubre «108 equipment classes, with 46 in focus» (cifra de un paper de OTC, no verificada contra la norma). Fuente 1 [S].
- Alcance de la norma: petróleo, gas natural y petroquímica (resultado de búsqueda, [S], sin URL propia). Para otras industrias es modelo de referencia, no requisito.
- Una guía de vendor dice que no hace falta usar los nueve niveles el primer día. Fuente 1 [S].
- **Hueco**: ubicación técnica frente a equipo (el equipo se mueve, la ubicación queda) y lista de repuestos del equipo (maintenance BOM). La fuente 1 dice explícitamente que no trata BOM ni repuestos.

### Activo físico frente a contable (frontera)
- ISO/TS 55010:2019 es la guía para alinear la gestión de activos con finanzas y contabilidad. Fuente 6 [S].
- En ERPNext el registro de activo es el objeto central: enlaza ítem y valor de compra con ubicación, plan de mantenimiento, calendario de depreciación y baja. La depreciación se configura por libro financiero: «Each Finance Book may have a different method, useful life, residual value, and posting frequency». Los cambios de ubicación van por un movimiento de activo para tener «a controlled transfer and an auditable history». Estados: Sold, Scrapped, In Maintenance, Out of Order. Fuente 7 [S].
- Lectura para el árbol: en la práctica de ERP el mismo registro lleva lo físico y lo contable; la frontera es de modelo, no de módulo. El contable es de Contabilidad.

### Marco de gestión de activos
- Serie ISO 55000: 55000:2014 (visión general, principios, terminología), 55001:2014 (requisitos), 55002:2018 (guía), ISO/TS 55010:2019. Lanzamiento el 5 de febrero de 2014 (la introducción de la misma página dice enero de 2014: discrepancia interna). Los cuatro «fundamentals» de 55002: Value, Alignment, Leadership, Assurance. Antecedente: PAS 55 (2004; versión 2008). Fuente 6 [S].
- **Hueco**: la definición literal de «asset» y de ciclo de vida de ISO 55000.

### Criticidad
- RCM (SAE JA1011), siete preguntas en orden: función y estándar de desempeño; cómo falla; qué eventos causan cada falla; qué pasa cuando ocurre; cuánto importa; qué tarea proactiva previene o reduce consecuencias; qué hacer si no hay tarea adecuada. Riesgos principales: seguridad, operaciones y presupuesto de mantenimiento; el RCM moderno suma ambiente. Funciones no críticas pueden ir a «run to failure». Fuente 5 [S].
- **Hueco**: matriz consecuencia × probabilidad y cómo la criticidad define estrategia y prioridad (la guía de criticidad de Reliamag no se alcanzó a leer).

### Historial del equipo y datos de falla
- Lo de ISO 14224 sobre modo, causa y mecanismo de falla no se leyó. Lo verificado: RCM exige identificar «dominant failure modes and causes» y arranca con un FMECA. Fuente 5 [S].
- Práctica: ERPNext tiene registro de reparación del activo y un campo «Maintenance Required» que habilita plan y bitácora (fuente 7 [S], sin detalle del repair). Odoo Maintenance tiene equipo, solicitudes, calendario y configuración (fuente 8 [S]; no se confirmó ningún campo de MTBF/MTTR).
- **Hueco**: lecturas de medidores y contadores; codificación de fallas.

## Componente 2: Desempeño de los activos

### Indicadores (fórmulas literales)
| Indicador | Fórmula | Fuente |
|---|---|---|
| MTBF | «Total operating time / number of failures (repairable assets)» | 2 [S] |
| MTTR | «Total repair time / number of repairs» | 2 [S] |
| Disponibilidad | «Uptime / (uptime + downtime), or MTBF / (MTBF + MTTR)» | 2 [S] |
| Cumplimiento del preventivo | «PM work orders completed on time / PM work orders scheduled» | 2 [S] |
| Backlog en semanas | «Total outstanding estimated work hours / weekly craft capacity hours (expressed in crew-weeks)» | 2 [S] |
| Trabajo planificado | «Planned maintenance hours / total maintenance hours» | 2 [S] |
| Costo / RAV | costo anual de mantenimiento / RAV × 100; RAV = «Cost to replace the asset base with equivalent new assets» | 2 [S], 10 [S] |

- **Discrepancia, MTBF y tiempo de reparación**: la fuente 2 usa «operating time» en el denominador, lo que sugiere excluir la reparación, pero no lo dice y remite a SMRP o EN 15341 para confirmar. Sin la norma leída queda abierto. La misma fuente avisa que confundir MTBF con MTTF es «one of the most common errors in maintenance reporting».
- Disponibilidad inherente: Ai = MTBF / (MTBF + MTTR) (reparable); Ai = MTTF / (MTTF + MTTR) (no reparable). Excluye «logistics time, waiting or administrative downtime, and preventive maintenance downtime». Fuente 3 [S]; coincide con lo que el buscador atribuye a NASA (fuente 4 [M]).
- Disponibilidad lograda: incluye «active preventive and corrective maintenance downtime» pero excluye logística y espera. Fuente 3 [S].
- **Discrepancia, disponibilidad operacional**: Wikipedia da Ao = MTBF / (MTBF + MDT), con MDT tiempo medio de parada, que incluye «logistics time, ready time, and waiting or administrative downtime» (fuente 3 [S]). El resumen del buscador sobre NASA y otras da Ao = MTBM / (MTBM + MDT), con MTBM tiempo medio entre mantenimientos (preventivos y correctivos) en lugar de MTBF (fuente 4 [M], no verificada en el texto). Hay que dar las dos.
- Ejemplo numérico (Wikipedia): MTTF de 81,5 años (713.940 h) y MTTR de 1 h dan Ai = 713.940 / 713.941 = 99,999860 %; indisponibilidad 0,000140 %; 0,01235 h de parada por año. Fuente 3 [S]. Es un ejemplo de equipamiento informático, no de planta.
- Cómo se engañan: la fuente 2 avisa que los objetivos «frequently circulate without a traceable primary source» y que una métrica con el mismo nombre en un dashboard de vendor y en EN 15341 «may be calculated slightly differently». Que el preventivo cuente solo lo hecho a tiempo, o que el backlog dependa de la capacidad del denominador, son inferencias marcadas como tales por la propia fuente. En RAV, numerador y denominador deben cubrir los mismos activos y hay que declarar qué entra (ingeniería, instalación, edificios). Fuente 10 [S].
- Benchmarks: ninguno confirmado en fuente trazable.

### Reparar o reemplazar
- Lo único verificado: el Handbook 135 de NIST/FEMP es la guía del método de costo de ciclo de vida para evaluar proyectos de energía, agua y renovables en edificios federales, basada en 10 CFR 436 subparte A. La ficha no menciona descuento ni reemplazo. Fuente 9 [M].
- **Hueco**: vida económica, costo anual equivalente, criterios de baja, IEC 60300-3-3 / ISO 15663.

## Recursos canónicos propuestos (a confirmar con lectura)
- Terminología: EN 13306 (no leída; título y edición sin verificar).
- Taxonomía y datos de falla: ISO 14224:2016, figura 3 (taxonomía) y anexos de modos, causas y mecanismos. Fijarse en el nivel 6 como unidad de reporte. Probar la vista previa del Online Browsing Platform de ISO.
- Indicadores: SMRP Best Practices Metrics (fórmula por métrica y notas de qué entra y qué no).
- Marco: ISO 55000/55001/55002 y, para la frontera con contabilidad, ISO/TS 55010.
- Criticidad y estrategia: Moubray, RCM II, o SAE JA1011.
- Costo de ciclo de vida: NIST Handbook 135, texto completo.
- Práctica de ERP: ERPNext (Asset, Asset Movement, Asset Repair) y las subpáginas de Odoo Maintenance (Equipment, Maintenance requests).

## Dónde el campo corta distinto que el árbol
- Jerarquía y criticidad suelen tratarse juntas como registro maestro del activo, y la criticidad se calcula sobre la jerarquía. Separarlas es defendible, pero hay que enlazarlas. (Hipótesis; apoyo débil en fuentes 1 y 5.)
- ISO 14224 trata taxonomía y codificación de falla en la misma norma: conviene que la codificación viva con el historial y que la taxonomía se enlace desde la jerarquía.
- En los ERP el registro físico y el contable son el mismo objeto (fuente 7); la frontera con Contabilidad hay que dejarla explícita.
- Reparar o reemplazar mezcla costo de ciclo de vida (finanzas) con confiabilidad: cae en el borde entre verticales.

## Huecos
1. Ninguna norma de pago leída (EN 13306, ISO 14224, ISO 55000/55001, IEC 60050-192, IEC 60300-3-3, ISO 15663).
2. SMRP Best Practices y Body of Knowledge: definiciones literales, benchmarks y si MTBF incluye reparación.
3. Libros (Moubray, Smith y Hinchcliffe, Campbell y Reyes-Picknell, Palmer): sin consultar.
4. IAM Anatomy, GFMAM, APQC PCF 10.0: sin consultar.
5. Ubicación técnica frente a equipo; lista de repuestos del equipo.
6. Matriz de riesgo y análisis de criticidad.
7. Modo, causa y mecanismo de falla de ISO 14224; medidores y contadores.
8. Vida económica, costo anual equivalente, criterios de baja; ejemplos numéricos de reparar o reemplazar.
9. Odoo: solo se vio la portada; ERPNext Asset Repair y Maintenance sin detalle.
10. Las búsquedas se agotaron por el tope de la sesión; hace falta otra ronda (o subir CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION).

## Segunda ronda (completar huecos)

Fecha: 2026-11-27. Advertencia: el presupuesto de WebSearch se agotó tras una búsqueda útil; el resto fueron fetch directos. WebFetch devuelve resúmenes, no el texto literal (para las páginas de SAP se negó a reproducirlas por copyright), así que **nada de esta ronda es [L] verdadero**: todo es [S] (resumen de la herramienta sobre la página). Las comillas son lo que el resumidor devolvió como literal; no se verificó contra el original. Todo lo traído de la web es dato. Puntajes A/P/E/U.

### Fuentes de esta ronda

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 11 | SAP Help (4.6C, antigua), «Equipment at Functional Locations» | https://help.sap.com/saphelp_46c/helpdata/en/01/d546244ab311d189740000e8322d00/content.htm | primaria | 3/2/1/3 | [S] |
| 12 | SAP Help (4.6C), «Installing/Dismantling Equipment from the Functional Location Master Record» | https://help.sap.com/saphelp_46c/helpdata/en/01/d546314ab311d189740000e8322d00/content.htm | primaria | 3/2/1/3 | [S] |
| 13 | SAP Help (4.6C), «Installing/Dismantling from the Equipment Master Record» | https://help.sap.com/saphelp_46c/helpdata/en/01/d546654ab311d189740000e8322d00/content.htm | primaria | 3/1/1/2 | [S] |
| 14 | SAP Help (4.6C), «Replacing Equipment» | https://help.sap.com/saphelp_46C/helpdata/EN/01/d546584ab311d189740000e8322d00/content.htm | primaria | 3/1/1/2 | [S] |
| 15 | SAP Help (4.6C), «Dismantling Equipment» | https://help.sap.com/saphelp_46C/helpdata/EN/01/d5464b4ab311d189740000e8322d00/content.htm | primaria | 3/1/1/1 | [S] (no aclara historial) |
| 16 | ERPNext, Asset Movement | https://docs.frappe.io/erpnext/user/manual/en/asset-movement | primaria (práctica) | 2/2/1/2 | [S] |
| 17 | ERPNext, Asset Repair | https://docs.frappe.io/erpnext/user/manual/en/asset-repair | primaria (práctica) | 2/2/1/2 | [S] |
| 18 | ERPNext, Asset Maintenance | https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance | primaria (práctica) | 2/2/1/1 | [S] |
| 19 | Wikipedia, «Equivalent annual cost» | https://en.wikipedia.org/wiki/Equivalent_annual_cost | secundaria | 1/2/3/2 | [S] |
| 20 | Wikipedia, «Risk matrix» | https://en.wikipedia.org/wiki/Risk_matrix | secundaria | 1/2/2/2 | [S] |
| 21 | Wikipedia, «Failure mode, effects, and criticality analysis» | https://en.wikipedia.org/wiki/Failure_mode,_effects,_and_criticality_analysis | secundaria | 1/2/2/2 | [S] |
| 22 | Wikipedia, «Whole-life cost» | https://en.wikipedia.org/wiki/Whole-life_cost | secundaria | 1/1/1/1 | [S] |
| 23 | Wikipedia, «ISO 14224» | https://en.wikipedia.org/wiki/ISO_14224 | secundaria | 1/1/1/1 | [S] (sin definiciones) |
| 24 | Buscador: foro SAP «Equipment vs function location» y KBA 3582809 (solo título y extracto) | https://answers.sap.com/questions/11268447/equipment-vs-function-location.html | secundaria (foro) | 1/1/1/1 | [S] extracto del buscador, no leído |

### 1. Ubicación técnica frente a equipo

- **Qué es cada una (SAP).** Las ubicaciones técnicas definen dónde se puede instalar un equipo. El equipo puede pasar de una ubicación a otra durante su vida, o estar sin instalar o en stock. Fuente 11 [S].
- **Dónde queda el historial (SAP).** Cada período de uso lo registra el sistema en una «usage list» (lista de uso), parte del historial del equipo. Fuente 11 [S]. El resumen del buscador dice además que la ayuda de SAP afirma que las ubicaciones técnicas no tienen historial propio y que el historial del equipo se compone de eventos (instalación, desmontaje, reemplazo = desmontaje + instalación, cambio de campo). Esa frase la vi solo en el resumen del buscador, no en una página leída [S].
- **Instalar y desmontar.**
  - Se puede hacer desde la ficha de la ubicación o desde la del equipo. Fuentes 11, 12 [S].
  - El equipo ya tiene que existir como registro maestro. Fuentes 12, 13 [S].
  - Con jerarquía de equipos, solo el equipo de más arriba se instala en una ubicación. Fuente 11 [S].
  - Una ubicación se puede configurar para admitir ningún equipo, uno o varios. Fuente 12 [S].
  - Se puede registrar con fecha y hora anteriores; vacío, usa la fecha y hora actuales. Fuentes 12, 13 [S].
  - Instalar crea, si está configurado, una entrada en la lista de uso con los datos actuales del equipo. Desmontar cierra la entrada vigente con fecha y hora de desmontaje y crea una nueva con los datos actualizados. Fuentes 12, 13 [S].
  - Reemplazar: desde la ubicación, Edit > Replace equipment; un change log muestra qué se desmontó y qué se instaló. Fuente 14 [S].
- **Discrepancia.** SAP: el historial está en el equipo (fuente 11 y resumen del buscador). Posts de LinkedIn citados por el buscador: el historial de mantenimiento queda con la ubicación aunque se reemplace el activo; el propio buscador lo calificó de convención de modelado, no regla del sistema. No verificado.
- **Problema conocido (SAP KBA 3582809, solo vía buscador, no leído):** al desmontar un equipo, la ubicación se blanquea en la lista de objetos de órdenes cerradas y en curso. Aviso de diseño: si la orden guarda solo el lugar actual, mover el equipo reescribe el pasado. https://userapps.support.sap.com/sap/support/knowledge/en/3582809 [S].
- **ERPNext.** Asset Movement registra cada transferencia, entrega y recepción como evento propio: «Asset Movement records every transfer, issue, and receipt as a separate event.» El movimiento más nuevo fija la posición o custodio actual; los anteriores se conservan como historial. Propósitos: Transfer, Issue, Receipt, Transfer and Issue. «It changes custody and location, not asset value.» Fuente 16 [S]. La ubicación es un campo del activo; no hay equivalente de la ubicación técnica.
- **Maximo (Locations vs Assets):** hueco. La URL de IBM Docs probada dio 404 y no quedó presupuesto de búsqueda.
- **Para el modelo (inferencia mía desde 11-13, no de fuente):** separar el lugar (permanente, con sus tareas planificadas) del equipo (se mueve) y guardar la relación como intervalos con inicio y fin, como la lista de uso de SAP, para reconstruir qué equipo estaba dónde en cada fecha.

### 2. Lista de repuestos del equipo (maintenance BOM)

Hueco. No se alcanzó ninguna página de «Equipment BOM» de help.sap.com ni de otro ERP.

### 3. Criticidad

- **Matriz de riesgo.** Compara categoría de probabilidad con categoría de gravedad. Cita: «a simple mechanism to increase visibility of risks and assist management decision making». Estadísticamente, el riesgo a la baja es probabilidad × gravedad. Ejemplo: cuatro niveles de gravedad (Minor, Marginal, Critical, Catastrophic) y cinco de probabilidad (Certain a Rare); Certain × Minor = High; Possible × Critical = High; Rare × Catastrophic = Medium. Fuente 20 [S].
- **Críticas a la matriz (fuente 20 [S]).** Resolución pobre (según Cox, puede dar igual calificación a riesgos muy distintos); el orden depende del diseño de la matriz (Thomas, Bratvold, Bickel); las etiquetas de probabilidad son ambiguas. Una matriz propia es una convención local: documentar escalas y definiciones.
- **FMECA y número de criticidad (fuente 21 [S]).** Cm = λp × α × β × t por modo de falla; Cr = suma de los Cm de los N modos. λp (tasa base) sale de modelos como MIL-HDBK-217; α (proporción del modo) de una base de modos o de criterio experto; β es la probabilidad condicional de que el efecto llegue a la gravedad dada. Gravedad (MIL-STD-882): I Catastrófica, II Crítica, III Marginal, IV Despreciable. Probabilidad: A Frecuente, B Probable, C Ocasional, D Remota, E Improbable. Se grafica gravedad contra probabilidad; la esquina alta se mitiga primero. Es la variante aeroespacial y de defensa, no la de plantas.
- **No leídos:** NASA RCM Guide (wbdg.org redirige a un bucket S3 que dio 403), FEMP O&M Best Practices (energy.gov 404; pnnl.gov venció por tiempo), TM 5-698, ISO 31000. No cito nada de ellos.
- **Cómo se usa para priorizar y elegir estrategia:** sin fuente leída. Lo único soportado es lo de RCM de la ronda anterior (funciones no críticas pueden ir a «run to failure», fuente 5).

### 4. Codificación de fallas y medidores

- **ISO 14224:** la página de Wikipedia no define modo, mecanismo ni causa; solo dice que el alcance es la «collection of data for the management of the maintenance of equipment, including reliability data» y que cubre metodología y detalle de los datos. Fuente 23 [S]. Tablas B.2 y B.3: hueco.
- **ERPNext Asset Repair** (fuente 17 [S]): activo, fecha de falla, descripción de la falla (texto libre), facturas de proveedor y repuestos consumidos (de ahí sale el costo), acciones realizadas, fecha de finalización; interruptor «Capitalize Repair Cost» y campo «Increase in asset life». Cita: «Routine repair is normally an expense.» Un repair pendiente puede dejar el activo Out of Order. No hay códigos de falla estructurados.
- **ERPNext Asset Maintenance** (fuente 18 [S]): un plan por activo y equipo de mantenimiento; cada tarea tiene tipo, fecha de inicio, periodicidad y responsable; al guardar se generan registros planificados. La fuente no menciona medidores ni disparo por uso: el preventivo es solo por calendario.
- **Medidores en SAP PM (measuring points/counters), Maximo (meters), horómetro:** hueco. La página de IBM Docs probada era un índice sin contenido; la de SAP probada devolvió solo el título.
- Inferencia de apoyo débil: de los ERP leídos (ERPNext, Odoo), ninguno confirmó preventivo por uso; sería capacidad del mantenimiento industrial, no del ERP general.

### 5. Costo del ciclo de vida y reparar o reemplazar

- **Definición.** «Whole-life cost»: «total cost of ownership over the life of an asset». Componentes: «planning, design, construction and acquisition, operations, maintenance», «renewal and rehabilitation, depreciation and cost of finance and replacement or disposal». Fuente 22 [S]. Incluye depreciación y costo financiero, que otras definiciones (NIST/FEMP) pueden tratar distinto; no se pudo contrastar porque el Handbook 135 (https://nvlpubs.nist.gov/nistpubs/Legacy/HB/nbshb135.pdf) dio 404.
- **Costo anual equivalente (EAC).** «the cost per year of owning and operating an asset over its entire lifespan»; compara opciones de vidas distintas (supone igual riesgo). EAC = −VAN / A(t,r), con A(t,r) = (1 − 1/(1+r)^t) / r; r = tasa anual, t = años. Fuente 19 [S].
- **Ejemplo numérico (fuente 19), tasa 5 %:**

| | Máquina A | Máquina B |
|---|---|---|
| Inversión | 50.000 | 150.000 |
| Vida | 3 años | 8 años |
| Mantenimiento anual | 13.000 | 7.500 |
| EAC | 31.360 | 30.708 |

  A: 50.000 / A(3; 5 %) + 13.000 = 31.360. B: 150.000 / A(8; 5 %) + 7.500 = 30.708. La fuente concluye invertir en B. Recalculé: A(3;5 %) = 2,7232 y A(8;5 %) = 6,4632; los resultados cierran. Compara dos compras: **no** es defensor y retador ni vida económica.
- **Vida económica (EAC mínimo), defensor/retador, criterios de baja:** hueco. Que la vida económica sea el año donde el EAC es mínimo es mi inferencia, sin fuente leída.
- **Tratamiento contable de la reparación (ERPNext, fuente 17 [S]):** se gasta salvo que cumpla la política de la organización y mejore el beneficio económico futuro; si extiende la vida útil se carga el aumento de vida y se revisa el cronograma de depreciación. Es la frontera con Contabilidad.

### 6. SMRP Best Practices Metrics

Hueco total: no se fetcheó ninguna copia pública de las definiciones. Nada nuevo sobre MTBF ni sobre «Maintenance cost as a percent of replacement asset value»; sigue lo de las fuentes 2 y 10 [S].

### Huecos que quedan tras la segunda ronda
1. Maximo (Locations vs Assets, meters), SAP measuring points/counters y Equipment BOM.
2. NASA RCM Guide, FEMP O&M, TM 5-698 (probar ntrs.nasa.gov u otra ruta).
3. ISO 14224 tablas B.2/B.3 y códigos problema/causa/remedio.
4. NIST HB 135, vida económica, defensor/retador, criterios de baja.
5. SMRP: definiciones literales.
6. Todo lo de esta ronda es [S]. Las páginas SAP son de la versión 4.6C (muy antigua); falta confirmar que valgan para la ayuda actual («Installation and Dismantling of Equipment at Functional Locations»).
