---
resumen: >-
  El MES (sistema de ejecución de manufactura) es la categoría de software de gestión que supervisa, sigue y sincroniza en la planta los pasos que convierten materiales en producto terminado: despacha las órdenes, registra lo consumido y lo producido y deja la trazabilidad de cada lote. Según ISA-95 vive en el nivel 3, debajo del ERP.
estado: borrador
estabilidad: estable
fuentes:
  - "ISA, página «ISA-95 Standard» (leída): https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard"
  - "Un proveedor de automatización, «ISA-95 framework layers» (leída; cita la norma): https://www.siemens.com/en-gb/technology/isa-95-framework-layers/"
  - "Gartner, glosario «MES manufacturing execution system» y Market Guide de 2016 (resúmenes del buscador): https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/mes-manufacturing-execution-system"
  - "Gartner, Market Guide for Manufacturing Execution Systems, mayo de 2025 (resumen): https://www.gartner.com/en/documents/6420807"
  - "Otro proveedor de automatización, «What is MES», febrero de 2025 (resumen; lista las 11 funciones de MESA): https://plex.rockwellautomation.com/content/dam/plex/documents/pdf/mes/WhatIsMES_Feb2025.pdf"
  - "Wikipedia, «Manufacturing execution system» (resumen): https://www.wikipedia.org/wiki/Manufacturing_execution_system"
  - "Documentación de aplicaciones de un ERP de código abierto, versión 18.0 (leída): https://www.odoo.com/documentation/18.0/applications.html"
  - "Lista de módulos de otro ERP de código abierto (leída): https://github.com/frappe/erpnext/blob/develop/erpnext/modules.txt"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md y taxonomias-externas-96.md (2026-11-27)"
aliases: [MES, manufacturing execution system, sistema de ejecución de manufactura, sistema de ejecución de la producción, MOM, manufacturing operations management, gestión de operaciones de manufactura, QMS, quality management system, sistema de gestión de la calidad, software de calidad, MESA]
creado: 2026-11-27
revisado:
---

# MES

El MES (sistema de ejecución de manufactura) es la categoría de software de gestión que supervisa, sigue y sincroniza en la planta los pasos que convierten materiales en producto terminado: despacha las órdenes, registra lo consumido y lo producido y deja la trazabilidad de cada lote. Según ISA-95 vive en el nivel 3, debajo del ERP.

Es una de las [categorías de producto](categorias-de-producto.md) y lleva la [ejecución en planta](../../Produccion/Ejecucion-en-planta/ejecucion-en-planta.md) y la [calidad](../../Produccion/Calidad/calidad.md) del tema Producción. Es la única categoría con una norma que dice dónde termina: ISA-95, también IEC 62264.

## La frontera con el ERP la pone ISA-95

ISA-95 ordena la empresa en niveles; según la página de ISA, el nivel 3 «describes manufacturing execution systems (MES)», el 4 «all the activities related to running a business», y la norma «primarily deals with the interface between levels 3 and 4». Los cinco niveles, las ocho partes y el vocabulario de 2013 están en [marcos de la producción](../../Produccion/Fundamentos/marcos-de-la-produccion.md#isa-95-cinco-niveles-y-la-frontera-entre-erp-y-mes). Qué baja del nivel 4 al 3 (la orden, la versión de la lista y la ruta) y qué sube (lo producido, lo consumido, las horas) está en la tabla de [ejecución en planta](../../Produccion/Ejecucion-en-planta/ejecucion-en-planta.md#la-frontera-entre-el-erp-y-el-mes).

Lo que agrega este tema es la consecuencia para el producto. La frontera de ISA-95 es entre funciones, no entre cajas de software: un mismo producto puede cubrir los dos niveles, y una empresa sin MES deja que su ERP reciba las declaraciones de planta. Según el resumen de la guía de mercado de 2025, Gartner describe al MES como el que despacha trabajo según las instrucciones del ERP o del programador de producción. El [ERP](erp.md) planifica y registra; el MES ejecuta.

## Qué funciones agrupa un MES

Gartner, según resúmenes de su glosario, define al MES como el sistema que supervisa, sigue y sincroniza los pasos físicos de la fabricación, coordina las órdenes con la programación y con los sistemas de la empresa, y lleva la trazabilidad y la genealogía. Deja afuera la capa de automatización (los controladores, las pantallas de operación, el control supervisor). La guía de mercado de 2016 dice, según su resumen, que el MES tiene casi tantas definiciones como proveedores.

La lista más citada de funciones es la de MESA, de 1997, según la reproduce un proveedor de automatización: programación detallada, control de documentos, despacho de unidades de producción, recolección de datos, gestión de procesos, asignación y estado de recursos, gestión de la mano de obra, gestión de calidad, seguimiento y genealogía del producto, gestión de mantenimiento y análisis de desempeño. Según Wikipedia, ISA-95 fusionó en 2000 ese modelo con el modelo de referencia de Purdue. El orden de la lista cambia entre fuentes.

Un proveedor de automatización que cita la Parte 3 de la norma parte el nivel 3 en cuatro categorías: producción, mantenimiento, calidad e inventario. Cada una tiene un dueño en la base, como cuenta [marcos de la producción](../../Produccion/Fundamentos/marcos-de-la-produccion.md#cuatro-categorías-de-operaciones-en-el-nivel-3). Para el software, eso quiere decir que el MES se pisa con tres categorías vecinas:

- Con el [EAM y el CMMS](eam-y-cmms.md), por el mantenimiento de las máquinas de la planta.
- Con el [WMS](scm-wms-y-tms.md), por el inventario de planta: el material entregado a la orden y el producto en proceso.
- Con el software de calidad, que se trata abajo.

## La gestión de calidad (QMS)

El software de gestión de la calidad lleva el registro de lo que no cumple y lo que se hace al respecto. El saber está en [Calidad](../../Produccion/Calidad/calidad.md): el [plan de inspección](../../Produccion/Calidad/plan-de-inspeccion.md), la [no conformidad](../../Produccion/Calidad/no-conformidad.md), la [acción correctiva](../../Produccion/Calidad/accion-correctiva.md), el [control estadístico](../../Produccion/Calidad/control-estadistico-de-procesos.md) y la [trazabilidad de lotes](../../Produccion/Calidad/trazabilidad-de-lotes.md). No se encontró una definición de Gartner para el QMS como categoría.

Va como apartado del MES porque ISA-95 pone la calidad entre las cuatro operaciones del nivel 3 y MESA la lista entre las funciones del MES. Pero el QMS también se compra fuera de la planta: la norma de sistemas de gestión de la calidad, ISO 9001, se aplica a organizaciones de servicios, y un QMS lleva entonces reclamos, auditorías y documentos sin ninguna orden de producción (lectura de esta base; la norma no se leyó). Los dos ERP de código abierto consultados traen un módulo de calidad propio, separado de producción.

En la lectura de esta base, lo que el software agrega sobre el saber de Calidad es poco y concreto: un registro de no conformidades con estados, un flujo de acción correctiva con responsables y plazos, el control de versiones de los documentos (procedimientos, especificaciones) y el vínculo entre el resultado de un ensayo y el lote que lo produjo. Todo eso usa piezas comunes a cualquier software de gestión: el documento con estados y la auditoría de cambios.

## Cómo se integra con el ERP

La integración ERP-MES es la que la norma intenta estandarizar: la Parte 5 de ISA-95 trata las transacciones entre el negocio y la manufactura en los niveles 3 y 4, según la página de ISA. En la práctica, el ERP baja las órdenes liberadas y sus versiones de lista y ruta, y el MES sube las declaraciones de consumo y producción, que en el ERP se vuelven movimientos de stock y costo de la orden. Cómo se conecta, con qué frecuencia y quién es fuente de verdad del lote está en [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md).

> [!NOTE] Sin fuente todavía: cuándo conviene un MES aparte y cuándo alcanza con el ERP (ninguna fuente leída lo responde con método); el texto de ISA-95 (de pago, solo la página de ISA y fuentes de proveedores) y de ISO 9001; una definición primaria del QMS como categoría de software.
