---
resumen: >-
  El registro de activos es lo que una empresa guarda de cada equipo que mantiene: qué es, dónde está instalado, de qué está hecho, cuánto importa que falle y qué le pasó. Es el dato maestro del dominio: cada plan de mantenimiento y cada orden de trabajo se abren sobre un equipo de este registro, y al cerrarse le escriben el historial.
estado: vigente
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), categoría 10.0 «Acquire, Construct, and Manage Assets», pp. 27-28: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Institute of Asset Management, What is asset management (cita ISO 55000:2014, 3.2.1 y 3.3.1): https://theiam.org/what-is-asset-management/"
  - "Wikipedia, ISO 55000 (resumen secundario, para ISO/TS 55010): https://en.wikipedia.org/wiki/ISO_55000"
  - "Wikipedia, Asset management (resumen secundario): https://en.wikipedia.org/wiki/Asset_management"
  - "ERPNext, Asset (como evidencia de práctica, resumen): https://docs.frappe.io/erpnext/user/manual/en/asset"
  - "ERPNext, Asset Movement (como evidencia de práctica, resumen): https://docs.frappe.io/erpnext/user/manual/en/asset-movement"
  - "Activos-y-mantenimiento/.investigacion/registro-y-desempeno.md (2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/apqc-10.md (2026-11-27)"
aliases: [registro de equipos, maestro de equipos, equipment master, asset register, asset registry, inventario de activos, activo físico, physical asset, ficha del equipo]
creado: 2026-11-27
revisado: 2026-11-27
---

# Registro de activos

El registro de activos es lo que una empresa guarda de cada equipo que mantiene: qué es, dónde está instalado, de qué está hecho, cuánto importa que falle y qué le pasó. Es el dato maestro del dominio: cada plan de mantenimiento y cada orden de trabajo se abren sobre un equipo de este registro, y al cerrarse le escriben el historial.

Dentro de [Activos y mantenimiento](../activos-y-mantenimiento.md) es la vertical que dice qué se mantiene. Le da a la [Estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) la criticidad de cada equipo, a la [Orden de trabajo](../Orden-de-trabajo/orden-de-trabajo.md) el objeto sobre el que se trabaja, y a [Desempeño de los activos](../Desempeno-de-los-activos/desempeno-de-los-activos.md) el historial que se mide. Sin software, es la planilla de equipos con una hoja por máquina; con software, es la tabla que leen todos los módulos.

## El activo físico frente al contable

Un mismo equipo tiene dos registros con dueños distintos, como criterio de la base. El físico dice qué es, dónde está y qué le pasó, y es de este tema. El contable dice cuánto costó, cuánto se amortizó y cuánto vale en libros, y es de [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md). La ISO 55000:2014 (3.2.1), citada por el Institute of Asset Management, define activo como «an item, thing or entity that has potential or actual value to an organisation»; la edición 2024, que la reemplazó, no se leyó. Según su resumen en Wikipedia, la serie tiene una guía aparte, la ISO/TS 55010:2019, para alinear la gestión de activos con finanzas y contabilidad.

Como criterio de la base, los dos registros no se superponen del todo: un repuesto rotativo o un equipo alquilado se mantienen sin ser bienes de uso, y un terreno es un bien de uso que nadie mantiene. El equipo de un cliente, en el servicio de campo, está solo del lado físico: es la [base instalada](../Servicio-de-campo/base-instalada.md).

En la práctica de los sistemas de gestión, la frontera es de modelo y no de módulo. Un sistema abierto guarda en el mismo registro de activo la ubicación, el plan de mantenimiento, el calendario de amortización y la baja, y mueve la ubicación con un documento propio que, según su documentación, «changes custody and location, not asset value». Como criterio de la base, conviene que el modelo deje claro qué campos son del físico y cuáles del contable, aunque vivan en la misma tabla.

## El ciclo de vida del activo

APQC, en su marco de procesos 7.4 (2024), parte la vida del activo propio en cuatro grupos: 10.1 «Plan and acquire assets», 10.2 «Design and construct assets», 10.3 «Maintain assets» y 10.4 «Manage asset end-of-life». El registro nace al construir el activo (10.2.4.3 «Create work and asset records»), se actualiza con cada trabajo (10.3.2.4 «Update work and asset records») y termina en el fin de vida, donde APQC pone 10.4.1.1 «Monitor useful life of assets» y 10.4.1.2 «Perform cost vs. benefit analysis for replacement».

El marco no tiene un proceso llamado registro o inventario de activos: el registro aparece como el efecto de los otros procesos. Comprar y construir el activo quedan fuera de este tema; la decisión de reemplazar está en [reparar o reemplazar](../Desempeno-de-los-activos/reparar-o-reemplazar.md). Como criterio de la base, dar de baja un equipo en el registro físico no da de baja el bien de uso: son dos hechos que se registran en dos lugares.

## Por qué un solo registro

Como criterio de la base, conviene un solo registro. El equipo aparece en el plan preventivo, en cada solicitud y orden de trabajo, en la reserva de repuestos, en el contrato de servicio y en los indicadores. Si cada uno guardara su propia descripción del equipo, la historia de una bomba quedaría repartida en cinco nombres distintos y no se podría medir. Por eso el equipo se registra una vez y los documentos lo referencian, como cualquier [dato maestro](../../Datos/Gobierno-y-calidad/datos-maestros.md).

## Dónde falla el registro

Como criterio de la base, el registro falla de tres maneras, y las tres se notan recién cuando se quiere medir:

- Duplicados. La misma máquina cargada dos veces, por ejemplo una vez por su número de serie y otra por su código de planta. Las órdenes se reparten entre los dos y ninguno tiene la historia completa.
- Equipos sin ubicación o con la ubicación vieja. Un equipo que se movió y nadie registró el traslado. El técnico no lo encuentra, y las órdenes viejas quedan asociadas a un lugar donde ya no está. La forma de evitarlo es registrar cada movimiento como un hecho fechado, que está en [jerarquía de activos](jerarquia-de-activos.md).
- Descripciones libres. «Bomba», «bba. agua», «electrobomba 2»: sin una clase de equipo cerrada, no se pueden comparar equipos parecidos ni sumar sus fallas.

Lo general de la calidad de un dato (completitud, unicidad, vigencia) está en [calidad de datos](../../Datos/Gobierno-y-calidad/calidad-de-datos.md).

> [!NOTE] Sin fuente todavía: un estudio o una guía que describa cómo fallan los registros de activos en la práctica y con qué frecuencia. Lo de arriba es criterio de la base.

## Qué hay en el registro de activos

- [Jerarquía de activos](jerarquia-de-activos.md) — la ubicación técnica frente al equipo, los niveles de la taxonomía de la ISO 14224, los componentes y la lista de repuestos de cada equipo.
- [Criticidad](criticidad.md) — cuánto importa que falle cada equipo, la matriz de consecuencia por probabilidad y cómo eso orienta la estrategia y la prioridad.
- [Historial del equipo](historial-del-equipo.md) — lo que le pasó: órdenes cerradas, fallas codificadas, lecturas y contadores, y por qué los historiales suelen no servir.
