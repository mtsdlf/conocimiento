---
resumen: >-
  El PSA (automatización de servicios profesionales) es la categoría de software de gestión de las firmas que venden horas de gente por proyecto: lleva el proyecto del cliente, la asignación de personas, el registro de horas y gastos, la facturación del proyecto y su rentabilidad. Se pisa con el ERP para empresas de servicios.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, «Professional services automation» (leída; cita a Melik y Melik 2002, Wiley, y a Hofferberth 2001, ChannelWeb): https://en.wikipedia.org/wiki/Professional_services_automation"
  - "Gartner, Market Guide for Professional Services Automation Platforms, 2025-10-15 (resumen; no leído): https://www.gartner.com/en/documents/7070798"
  - "Gartner, Peer Insights del mercado de plataformas de PSA (resumen): https://www.gartner.com/reviews/market/professional-services-automation-platforms"
  - "Gartner, Magic Quadrant for Cloud ERP for Service-Centric Enterprises, octubre de 2025, citado junto al de empresas de producto (resumen): https://www.gartner.com/en/documents/7058198"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md y taxonomias-externas-96.md (2026-11-27)"
aliases: [PSA, professional services automation, automatización de servicios profesionales, software de servicios profesionales, software de gestión de proyectos de clientes, ERP de servicios, service-centric ERP]
creado: 2026-11-27
revisado:
---

# PSA

El PSA (automatización de servicios profesionales) es la categoría de software de gestión de las firmas que venden horas de gente por proyecto: lleva el proyecto del cliente, la asignación de personas, el registro de horas y gastos, la facturación del proyecto y su rentabilidad. Se pisa con el ERP para empresas de servicios.

Es una de las [categorías de producto](categorias-de-producto.md) y lleva el dominio de [Servicios profesionales y proyectos](../../Servicios-profesionales-y-proyectos/servicios-profesionales-y-proyectos.md). De dónde viene el nombre (principios de los años 2000, con el libro de Melik y Melik de 2002) está en sus [fundamentos](../../Servicios-profesionales-y-proyectos/Fundamentos/fundamentos-de-servicios-profesionales.md#el-psa-como-categoría-de-software).

## Qué funciones agrupa un PSA

Wikipedia, que cita a Melik y Melik (2002), lo define como software para que profesionales como abogados, auditores y consultores gestionen los proyectos de sus clientes y sus recursos, y sigan la utilización del personal facturable. Su núcleo es la contabilidad de proyectos, la gestión de recursos, el tiempo y los gastos, y la facturación; los más completos suman CRM y gestión del conocimiento. Cada función modela una parte del dominio:

| Función del PSA | Parte del dominio |
|---|---|
| Proyectos y contabilidad de proyectos | [Proyecto del cliente](../../Servicios-profesionales-y-proyectos/Proyecto-del-cliente/proyecto-del-cliente.md) |
| Gestión de recursos | [Asignación de personas](../../Servicios-profesionales-y-proyectos/Asignacion-de-personas/asignacion-de-personas.md) |
| Tiempo y gastos | [Registro de horas](../../Servicios-profesionales-y-proyectos/Registro-de-horas/registro-de-horas.md) |
| Facturación | [Facturación del proyecto](../../Servicios-profesionales-y-proyectos/Facturacion-del-proyecto/facturacion-del-proyecto.md) |
| Reportes de utilización y margen | [Rentabilidad de la firma](../../Servicios-profesionales-y-proyectos/Rentabilidad-de-la-firma/rentabilidad-de-la-firma.md) |

Gartner no publica un cuadrante de PSA. Publica una guía de mercado de plataformas de PSA (15 de octubre de 2025) con proveedores representativos y sin ranking, y, según resúmenes, una lista de funciones obligatorias que incluye los reportes y el análisis de actividad y rentabilidad, y la gestión de contratos. Un sitio de comparación afirma que existe un cuadrante, pero otras dos fuentes lo contradicen.

## Dónde termina el PSA

- **Con el ERP para empresas de servicios.** Gartner evalúa un ERP «para empresas centradas en el servicio» desde octubre de 2025 ([ERP](erp.md#un-erp-para-empresas-de-producto-y-otro-para-empresas-de-servicios)). La mitad operativa de ese ERP es la misma que la del PSA. En la lectura de esta base, la diferencia es de dónde se parte: el PSA nace del proyecto y suma la factura; el ERP nace de la contabilidad y suma el proyecto.
- **Con el [CRM](crm.md).** La oportunidad ganada abre el proyecto, y las oportunidades abiertas son la demanda futura de personas que mira la asignación. Un PSA completo trae su propio CRM.
- **Con el [HCM](hcm.md).** La hora trabajada sirve para pagar y para facturar. Cuántas horas trabajó una persona es de la nómina; a qué proyecto se imputan y cuáles se cobran, del PSA.
- **Con la gestión de proyectos.** El método de encuadrar, planificar y seguir un proyecto es de [Gestión de proyectos](../../Gestion-de-proyectos/gestion-de-proyectos.md). El PSA registra lo que de eso tiene precio y cliente; las herramientas de tareas y planificación sin facturación no son PSA.

## Cómo se integra con el ERP

Si la firma tiene PSA y ERP separados, el PSA entrega la factura o los datos para emitirla, y el ERP lleva el comprobante fiscal, la cuenta del cliente y el asiento. La parte delicada es el [trabajo en curso](../../Servicios-profesionales-y-proyectos/Facturacion-del-proyecto/trabajo-en-curso.md): la diferencia entre lo hecho, lo facturado y el ingreso, que el PSA calcula y la contabilidad tiene que reconocer. Qué sistema manda en el cliente, en el proyecto y en la tarifa de cada rol se decide como en cualquier otra frontera entre cajas, y está en [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md).

> [!NOTE] Sin fuente todavía: el texto de Melik y Melik (2002) y la guía de mercado de Gartner de 2025, que serían la fuente canónica de la categoría. La única cifra de tamaño de mercado encontrada es de una sola consultora de estudios de mercado, citada por Wikipedia, y no se usa.
