---
resumen: >-
  El HCM (gestión del capital humano) es la categoría de software de gestión que lleva el registro del personal, el tiempo trabajado y la nómina y, en las suites grandes, el talento: buscar, incorporar, evaluar y desarrollar personas. HRIS, HRMS y HCM son nombres que se solapan para la misma caja.
estado: vigente
estabilidad: estable
fuentes:
  - "Wikipedia, «Human capital management» (leída en parte; cita a Armstrong 2006): https://en.wikipedia.org/wiki/Human_capital_management"
  - "Gartner, Cloud HCM Suites for 1,000+ Employee Enterprises (resumen): https://www.gartner.com/reviews/market/cloud-hcm-suites-for-1000-employees"
  - "Gartner, documento del cuadrante de suites de HCM (resumen): https://www.gartner.com/en/documents/6933166"
  - "Lista de módulos de la aplicación de personal de un ERP de código abierto (leída): https://github.com/frappe/hrms/blob/develop/hrms/modules.txt"
  - "Documentación de aplicaciones de otro ERP de código abierto, versión 18.0 (leída): https://www.odoo.com/documentation/18.0/applications.html"
  - "APQC, Process Classification Framework Cross-Industry 7.2.1, copia de terceros (resumen): https://www.slideshare.net/AsgharAghiliDehkordi/cross-industry-v721-final"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md y taxonomias-externas-96.md (2026-11-27)"
aliases: [HCM, human capital management, gestión del capital humano, HRIS, human resources information system, HRMS, human resources management system, sistema de recursos humanos, software de RR. HH., core HR, sistema de nómina, payroll software, talent management, gestión del talento]
creado: 2026-11-27
revisado: 2026-11-27
---

# HCM

El HCM (gestión del capital humano) es la categoría de software de gestión que lleva el registro del personal, el tiempo trabajado y la nómina y, en las suites grandes, el talento: buscar, incorporar, evaluar y desarrollar personas. HRIS, HRMS y HCM son nombres que se solapan para la misma caja.

Es una de las [categorías de producto](categorias-de-producto.md). Su particularidad es que junta dos temas de esta base: la [administración de personal y nómina](../../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) (registrar y calcular) y la [gestión de personas](../../Liderazgo-y-direccion/Gestion-de-personas/gestion-de-personas.md) de Liderazgo y dirección (decidir sobre las personas). La base los separa porque son saberes distintos; el mercado los vende juntos porque leen el mismo legajo.

## Los nombres de la categoría

Wikipedia dice que HCM se usa «sometimes» como sinónimo de recursos humanos, y que en sentido estricto el capital humano es lo que cada persona sabe y aporta, según Armstrong (2006). Llama HRIS a los sistemas que guardan y recuperan los registros de los empleados. Hoy el mercado dice HCM; los [fundamentos de administración de personal](../../Administracion-de-personal-y-nomina/Fundamentos/fundamentos-de-administracion-de-personal.md) cuentan cómo la nómina fue lo primero que se automatizó y cómo esos nombres se fueron pisando.

## Qué agrupa una suite de HCM

Gartner evalúa las suites de HCM para empresas de más de 1.000 empleados en tres bloques, según el resumen de su página: el núcleo de recursos humanos con los beneficios, el talento antes y después de la contratación, y la administración de la nómina.

| Bloque | Qué lleva | Dónde está el saber |
|---|---|---|
| Núcleo de RR. HH. | El legajo, el puesto, la estructura, el ingreso y el egreso | [Legajo](../../Administracion-de-personal-y-nomina/Legajo/legajo.md) |
| Tiempo y asistencia | Jornadas, turnos, marcaciones, licencias | [Tiempo y asistencia](../../Administracion-de-personal-y-nomina/Tiempo-y-asistencia/tiempo-y-asistencia.md) |
| Nómina | La liquidación, el recibo, las cargas y las declaraciones | [Liquidación de sueldos](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-de-sueldos.md) y [cargas y declaraciones](../../Administracion-de-personal-y-nomina/Cargas-y-declaraciones/cargas-y-declaraciones.md) |
| Talento | Búsqueda, incorporación, evaluación, desarrollo, compensación | [Gestión de personas](../../Liderazgo-y-direccion/Gestion-de-personas/gestion-de-personas.md) |

La aplicación de personal de un ERP de código abierto trae diez módulos, de la búsqueda a la nómina y los impuestos sobre sueldos. Otro ERP de código abierto pone en la misma familia la flota, el almuerzo y la recepción de visitas. El borde de la categoría es tan variable como el del [ERP](erp.md).

## Dónde termina y con qué se pisa

- Con el ERP, en la nómina. La nómina se puede comprar dentro del ERP o dentro del HCM. APQC la pone dos veces en su marco de procesos, según una copia de la versión 7.2.1: en finanzas (9.5 «Process payroll») y en personas (7.5.4 «Administer payroll»). El ERP necesita el resultado para el asiento; el HCM necesita el legajo para calcularla.
- Con el talento como mercado aparte. Búsqueda, aprendizaje y evaluación también se venden como productos propios de gestión del talento, fuera de las suites. Es inferencia de esta base, sin fuente leída.
- Con el [PSA](psa.md), en las horas. La misma hora sirve para pagarle a la persona y para facturarle al cliente. Servicios profesionales separa las dos: cuántas horas trabajó una persona es de nómina; a qué proyecto se imputan, del PSA.

## Cómo se integra con el ERP

La salida de cada liquidación es un documento que deja un asiento: sueldos, cargas a pagar y retenciones. El diagrama de [administración de personal y nómina](../../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) muestra que la liquidación entrega el documento del asiento a Contabilidad, y que las cargas dejan vencimientos a Tesorería. Si HCM y ERP son cajas distintas, esa entrega es una integración, y la pregunta es qué sistema manda en el empleado como parte (el mismo empleado puede ser acreedor de un reintegro de gastos en el ERP); se trata en [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md).

La nómina es además el módulo más atado a la ley de cada país: conceptos, aportes, retenciones y libros cambian con cada norma. En la lectura de esta base, por eso una suite global de HCM suele dejar la liquidación local a otro producto, y por eso la nómina es la puerta de entrada de muchos sistemas locales.

> [!NOTE] Sin fuente todavía: no hay norma ni cuerpo de saber del HCM como software; la categoría se define por el cuadrante de Gartner, que se leyó solo por resumen. Tampoco hay fuente para la afirmación de que las suites globales dejan la liquidación local a otro producto: es inferencia.
