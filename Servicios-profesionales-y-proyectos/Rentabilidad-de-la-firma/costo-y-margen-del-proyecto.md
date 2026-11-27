---
resumen: >-
  El costo de un proyecto es la suma de sus horas imputadas, cada una por su costo de la hora, más los gastos que se le cargan; el margen del proyecto es su ingreso menos ese costo, y el del cliente, la suma de sus proyectos. El costo de la hora es un dato separado de la tarifa, y cómo se calcula decide qué margen se ve.
estado: borrador
estabilidad: semi
fuentes:
  - "FAR 52.232-7, Payments under Time-and-Materials and Labor-Hour Contracts, (a)(4) (la cita leída en la página): https://www.acquisition.gov/far/52.232-7"
  - "FAR 31.201-1, Composition of total cost (según resumen): https://www.acquisition.gov/far/31.201-1"
  - "Wikipedia, Contribution margin (según resumen): https://en.wikipedia.org/wiki/Contribution_margin"
  - "ERPNext, Timesheet y Project costing (costo y tarifa como campos separados; margen bruto del proyecto), según resumen: https://docs.frappe.io/erpnext/user/manual/en/timesheet"
  - "ERPNext, Project Profitability: https://docs.frappe.io/erpnext/user/manual/en/project-profitability"
  - "Odoo 19, Project profitability (según resumen): https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_profitability.html"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage contract values for project-based sales (qué se registra al aprobar una hora según el método): https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/manage-contract-values-project-based-sales"
  - "Servicios-profesionales-y-proyectos/.investigacion/metricas-fundamentos-y-contraria.md"
  - "Servicios-profesionales-y-proyectos/.investigacion/asignacion-y-horas.md"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md"
aliases: [costo y margen del proyecto, costo de la hora, cost rate, costo cargado, loaded cost, fully loaded cost, costo horario, margen del proyecto, project margin, rentabilidad del proyecto, project profitability, margen del cliente, client profitability]
creado: 2026-11-27
revisado:
---

# Costo y margen del proyecto

El costo de un proyecto es la suma de sus horas imputadas, cada una por su costo de la hora, más los gastos que se le cargan; el margen del proyecto es su ingreso menos ese costo, y el del cliente, la suma de sus proyectos. El costo de la hora es un dato separado de la tarifa, y cómo se calcula decide qué margen se ve.

Contablemente, cada proyecto es una orden: se costea como el trabajo de una imprenta o de una constructora, con el [costeo por órdenes](../../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md#por-órdenes-o-por-procesos-qué-se-acumula), que sigue los costos de cada trabajo hasta el final. El proyecto viaja como dimensión en cada movimiento, como explica [centros de costo](../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md#por-qué-los-centros-de-costo-van-en-dimensiones-y-no-en-el-plan-de-cuentas). Esta nota trata lo propio de una firma que vende horas: de dónde sale el costo de cada hora y qué margen conviene mirar.

## El costo de la hora y la tarifa son dos datos

Cada hora imputada lleva dos valores: lo que le cuesta a la firma y lo que se le cobra al cliente. Un sistema abierto los guarda como campos distintos, uno «the actual cost of work done» y otro la tarifa a la que se factura, y multiplica cada uno por las horas. El porqué de esa separación está en el [registro de horas](../Registro-de-horas/registro-de-horas.md); acá importa que el margen sale de la diferencia.

La norma de compras del gobierno de Estados Unidos dice de qué está hecha una tarifa horaria en sus contratos por tiempo y materiales: «The hourly rates shall include wages, indirect costs, general and administrative expense, and profit» (FAR 52.232-7, párrafo (a)(4)). Es decir, salarios, costos indirectos, gastos generales y de administración, y ganancia. Otra cláusula de la misma norma define el costo total de un contrato como la suma de los costos directos e indirectos que se le pueden asignar (FAR 31.201-1, según resumen). Las dos son reglas de un tipo de contrato público de un solo país, y es la única fuente leída sobre dinero en esta nota.

Leída al revés, que es lectura de esta base, la cláusula separa la tarifa en dos partes: un costo cargado (salarios más indirectos más gastos generales y de administración) y una ganancia. El costo de la hora que interesa para el margen es la primera parte.

## Cómo se calcula el costo cargado

> [!NOTE] Sin fuente todavía: la fórmula del costo de la hora cargado, qué entra en el numerador y sobre qué horas se divide. Lo que sigue es práctica común sin fuente leída y criterio de esta base.

La cuenta usual tiene un numerador y un denominador, y en los dos hay una decisión:

| Parte | Qué entra | La decisión |
|---|---|---|
| Sueldo y cargas | El sueldo de la persona con las contribuciones y los beneficios | Por persona o promedio por rol |
| Indirectos | Una parte de alquiler, software, administración, gerencia | Si entran o quedan para el margen de la firma |
| Horas | Las horas sobre las que se reparte | Horas pagadas, horas de capacidad o horas facturables esperadas |

El denominador mueve el número más que nada. Si se divide por las horas facturables esperadas, cada hora facturable carga también el costo del tiempo que no se factura, y el costo de la hora sube. Si se divide por las horas pagadas, el costo de la hora baja, y el tiempo no facturable aparece como un costo aparte de la firma. Kaplan y Anderson hacen el mismo argumento para el costeo por actividades: dividir por la capacidad práctica deja la capacidad ociosa a la vista en lugar de esconderla en las tarifas, como cuenta [sistemas de costeo](../../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md#time-driven-abc-dos-parámetros-en-vez-de-una-encuesta). Trasladarlo al costo de la hora es lectura de esta base.

Si el costo de la hora es directo o indirecto respecto del proyecto depende de la pregunta. Las horas de quien trabaja en el proyecto son directas; la gerencia que reparte su tiempo entre todos es indirecta, como explica [clasificación de costos](../../Contabilidad/Contabilidad-de-gestion/clasificacion-de-costos.md#directo-e-indirecto-si-se-puede-atribuir-al-producto).

## Qué margen mirar

Hay al menos dos márgenes del proyecto, y conviene no mezclarlos en el mismo informe (criterio de esta base):

- **Margen directo**: ingreso menos horas al costo de sueldo y cargas, menos gastos del proyecto. Muestra cuánto deja el proyecto para pagar la estructura.
- **Margen después de indirectos**: usa el costo cargado. Muestra si el proyecto paga su parte de la firma.

El primero se parece al [margen de contribución](../../Contabilidad/Contabilidad-de-gestion/punto-de-equilibrio.md#margen-de-contribución-lo-que-deja-cada-venta-para-pagar-los-fijos), que es el precio menos el costo variable. El parecido tiene un límite, que también es lectura de esta base: en una firma con gente asalariada, el sueldo es casi fijo en el corto plazo, así que la hora no es un costo variable en sentido estricto. Por eso elegir el margen es una decisión de método de la firma, y no una regla.

Los sistemas leídos calculan el margen así. Un sistema abierto toma el costo total del proyecto (horas por su costo, más gastos, compras y materiales) y lo compara con lo facturado. Otro separa el ingreso en vendido, entregado y facturado, y el costo en esperado, por pagar y pagado, de modo que el margen se puede ver en cada etapa.

## El margen según cómo se cobra

Lo que una hora mueve depende del modelo de cobro. En un sistema de gestión de servicios, aprobar una hora de un contrato por [tiempo y materiales](../Facturacion-del-proyecto/facturacion-por-hora.md) crea dos registros: el costo y la venta sin facturar. Aprobar una hora de un contrato a [precio cerrado](../Facturacion-del-proyecto/facturacion-por-hito.md) crea solo el costo; el ingreso llega por hito o por avance.

De ahí sale una consecuencia para leer el margen. En tiempo y materiales, el margen de cada hora es tarifa menos costo, y solo baja si la hora se castiga en la factura, lo que mide la [realización](realizacion.md). A precio cerrado, el margen del mes no dice nada sin el avance: un proyecto puede mostrar mucho costo y poco ingreso porque el hito todavía no llegó. El ingreso que corresponde al trabajo hecho está en [trabajo en curso](../Facturacion-del-proyecto/trabajo-en-curso.md), y el riesgo de pasarse en un proyecto a precio cerrado, en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md). Comparar el costo con lo que se presupuestó es tarea del [presupuesto del proyecto](../Proyecto-del-cliente/presupuesto-del-proyecto.md).

## Del proyecto al cliente

El margen del cliente es la suma de los márgenes de sus proyectos, menos lo que se gastó en él fuera de cualquier proyecto: la preventa, las reuniones de cuenta, los reclamos. Si esas horas se cargan a un [proyecto interno](../Proyecto-del-cliente/proyecto-del-cliente.md) etiquetado con el cliente, el margen del cliente las incluye; si no, el cliente parece más rentable de lo que es (criterio de esta base).

## Cómo sale mal el margen

- **Horas que no se cargan.** Si quien está pasado de presupuesto deja de imputar, el proyecto parece rentable. Es el límite de todo lo que sale de la hoja, explicado en [calidad del registro](../Registro-de-horas/calidad-del-registro.md).
- **Un costo de la hora viejo.** Si los sueldos suben y el costo de la hora no se actualiza, todos los márgenes salen inflados. Con inflación alta, el costo de la hora necesita fecha de vigencia como la tarifa (criterio de esta base).
- **Gastos que no se imputan.** Un gasto que no se traslada al cliente sigue siendo costo del proyecto; cómo se registra está en [gastos del proyecto](../Registro-de-horas/gastos-del-proyecto.md).
- **Leer un proyecto a precio cerrado sin su avance**, como en la sección anterior.
