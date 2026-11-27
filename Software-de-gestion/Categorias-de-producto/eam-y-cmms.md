---
resumen: >-
  El CMMS (sistema computarizado de gestión del mantenimiento) y el EAM (gestión de activos de la empresa) son las categorías de software que llevan el registro de los equipos y su mantenimiento. El CMMS se centra en ejecutar el mantenimiento con órdenes de trabajo; el EAM, que nació de él, abarca toda la vida del activo, de la compra a la baja.
estado: vigente
estabilidad: estable
fuentes:
  - "TechTarget, definición de enterprise asset management, que cita a Gartner (resumen): https://www.techtarget.com/searcherp/definition/enterprise-asset-management-EAM"
  - "Gartner, Research Report G00122453 (2004), alojado por un proveedor (resumen; no leído): https://public.dhe.ibm.com/software/emea/de/tivoli/Gartner-Research-Report_G00122453.pdf"
  - "Un sitio de reseñas de software, glosario de EAM (resumen): https://www.g2.com/glossary/enterprise-asset-management-definition"
  - "Un proveedor de mantenimiento, glosario de EAM (resumen): https://tractian.com/en/glossary/eam-enterprise-asset-management"
  - "Documentación de aplicaciones de un ERP de código abierto, versión 18.0 (leída): https://www.odoo.com/documentation/18.0/applications.html"
  - "Lista de módulos de otro ERP de código abierto (leída): https://github.com/frappe/erpnext/blob/develop/erpnext/modules.txt"
  - "Un proveedor de automatización, «ISA-95 framework layers» (leída; cita la norma): https://www.siemens.com/en-gb/technology/isa-95-framework-layers/"
  - "Otro proveedor de automatización, «What is MES», febrero de 2025 (resumen; lista las 11 funciones de MESA): https://plex.rockwellautomation.com/content/dam/plex/documents/pdf/mes/WhatIsMES_Feb2025.pdf"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md y taxonomias-externas-96.md (2026-11-27)"
aliases: [EAM, enterprise asset management, gestión de activos de la empresa, CMMS, computerized maintenance management system, sistema de gestión de mantenimiento asistido por computadora, GMAO, sistema de mantenimiento, software de mantenimiento]
creado: 2026-11-27
revisado: 2026-11-27
---

# EAM y CMMS

El CMMS (sistema computarizado de gestión del mantenimiento) y el EAM (gestión de activos de la empresa) son las categorías de software que llevan el registro de los equipos y su mantenimiento. El CMMS se centra en ejecutar el mantenimiento con órdenes de trabajo; el EAM, que nació de él, abarca toda la vida del activo, de la compra a la baja.

Son parte de las [categorías de producto](categorias-de-producto.md) y llevan el dominio de [Activos y mantenimiento](../../Activos-y-mantenimiento/activos-y-mantenimiento.md): el [registro de activos](../../Activos-y-mantenimiento/Registro-de-activos/registro-de-activos.md), la [estrategia de mantenimiento](../../Activos-y-mantenimiento/Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md), la [orden de trabajo](../../Activos-y-mantenimiento/Orden-de-trabajo/orden-de-trabajo.md) y el [desempeño de los activos](../../Activos-y-mantenimiento/Desempeno-de-los-activos/desempeno-de-los-activos.md). El saber está allá; acá, cómo se reparte entre las dos cajas y sus vecinas.

## Del CMMS al EAM

Las dos categorías son una misma línea. Un informe de Gartner de 2004 dice, según su resumen, que el EAM evolucionó unos diez años antes desde los sistemas de mantenimiento computarizados. Gartner, citado por la prensa del sector, llama «core EAM» a las capacidades básicas de llevar un registro exacto y detallado de los activos.

La diferencia que dan los proveedores y los sitios de reseñas es de alcance: el EAM cubre todo el ciclo de vida del activo (adquisición, instalación, operación, mantenimiento y baja), y el CMMS, la ejecución del mantenimiento. El vocabulario del ciclo de vida lo fija la ISO 55000, de la que los [fundamentos de activos y mantenimiento](../../Activos-y-mantenimiento/Fundamentos/fundamentos-de-activos-y-mantenimiento.md) leyeron la ficha y las definiciones que cita el IAM, no el texto. En la lectura de esta base, la gestión de activos es un sistema del que el mantenimiento es una parte. La tabla baja la diferencia de alcance a ejes concretos (lectura de esta base).

| | CMMS | EAM |
|---|---|---|
| Centro | La orden de trabajo y el plan preventivo | El activo a lo largo de su vida |
| Qué suma | Repuestos de la orden, historial del equipo | Compra, costo del ciclo de vida, decisión de reemplazar, a veces varias plantas |
| Comprador típico (lectura de esta base) | Un área de mantenimiento | Una empresa con muchos activos caros o regulados |

## Dónde termina y con qué se pisa

- Con el [ERP](erp.md), en el activo y el repuesto. El activo tiene dos registros con dueños distintos: el operativo, que es de mantenimiento, y el contable, que es de [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md). El ERP lleva el bien de uso y el EAM el equipo; un repuesto rotativo o un equipo alquilado está solo en el segundo. Los repuestos son además stock del ERP. Un ERP de código abierto trae mantenimiento en su familia de cadena de suministro; otro tiene módulos separados de activos y de mantenimiento.
- Con el [MES](mes.md), en la planta. ISA-95 pone el mantenimiento entre las cuatro operaciones del nivel 3, según un proveedor de automatización que cita la norma, y MESA lo lista entre las funciones del MES. Una fábrica puede llevar el mantenimiento de sus máquinas en el MES, en un CMMS o en el ERP.
- Con el [servicio de campo](servicio-de-campo-y-mesa-de-ayuda.md), en el equipo del cliente. El ciclo de la orden de trabajo es el mismo; cambia de quién es el equipo, quién paga y quién da la conformidad. Esta base pone los dos en el mismo dominio por esa razón, y el mercado los vende en cajas distintas.

## Cómo se integra con el ERP

Las conexiones con el ERP son tres, en la lectura de esta base: los [repuestos y materiales](../../Activos-y-mantenimiento/Orden-de-trabajo/repuestos-y-materiales.md) que la orden reserva y consume del stock, las compras que dispara cuando falta un repuesto, y el costo de la orden que la contabilidad imputa o capitaliza. El alta y la baja de un equipo tocan los dos registros del activo, y alguien tiene que decidir cuál manda en cada dato: el número de serie y la ubicación en el EAM, el valor y la amortización en el ERP. Esa decisión está en [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md).

La cifra de que el 80 % de las implantaciones de CMMS fracasa no tiene un estudio detrás; su rastreo está en los [fundamentos de activos y mantenimiento](../../Activos-y-mantenimiento/Fundamentos/fundamentos-de-activos-y-mantenimiento.md).

> [!NOTE] Sin fuente todavía: una definición primaria del CMMS y del EAM (las leídas son de la prensa del sector, de un sitio de reseñas y de un proveedor; el informe de Gartner de 2004 se vio solo por resumen) y el texto de la ISO 55000 sobre el ciclo de vida.
