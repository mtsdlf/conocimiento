---
resumen: >-
  El trabajo en curso es la diferencia, en un momento dado, entre lo que una firma ya trabajó para un cliente y lo que ya le facturó. Existe porque reconocer el ingreso no es facturar: el ingreso sigue el avance del trabajo y la factura sigue el calendario pactado, y la NIIF 15 llama a la diferencia activo del contrato, cuenta a cobrar o pasivo del contrato.
estado: vigente
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIIF 15 Ingresos de actividades ordinarias procedentes de contratos con clientes, párrafos 35, 39-41, 105-109 y B14-B19: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html"
  - "IFRS Foundation, NIIF 15 Ejemplos ilustrativos, Ejemplo 19 y Ejemplo 42: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15-ie.html"
  - "IFRS Foundation, IFRS 15 Revenue from Contracts with Customers (qué normas reemplaza): https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage billing backlog: https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/manage-billing-backlog"
  - "Grant Thornton, Revenue from Contracts with Customers: Navigating the guidance in ASC 606 and ASC 340-40 (enero 2022), ASC 606-10-25-27, 606-10-25-31, 606-10-45-2 y 606-10-55-17 y 55-18: https://www.grantthornton.com/content/dam/grantthornton/website/assets/content-page-files/audit/pdfs/2022/revenue-from-contracts-with-customers-updated-220124.pdf"
  - "Kreston Reeves, Lock-up management in legal firms (2026): https://www.krestonreeves.com/news/lock-up-management-legal-firms/"
  - "ILFM (Institute of Legal Finance and Management), Lock-up management in law firms: why it matters: https://www.ilfm.org.uk/blog/ilfm-blog/lockup-management-in-law-firms-why-it-matters/"
  - "Odoo 19, Project profitability: https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_profitability.html"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (secciones 3.4 y 4)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 4.5)"
aliases: [trabajo en curso, WIP, work in progress, trabajo en curso sin facturar, unbilled revenue, ventas sin facturar, unbilled sales, activo del contrato, contract asset, pasivo del contrato, contract liability, ingreso diferido, deferred revenue, porcentaje de avance, percentage of completion]
creado: 2026-11-27
revisado: 2026-11-27
---

# Trabajo en curso

El trabajo en curso es la diferencia, en un momento dado, entre lo que una firma ya trabajó para un cliente y lo que ya le facturó. Existe porque reconocer el ingreso no es facturar: el ingreso sigue el avance del trabajo y la factura sigue el calendario pactado, y la NIIF 15 llama a la diferencia activo del contrato, cuenta a cobrar o pasivo del contrato.

Es la idea que une las reglas de [facturación del proyecto](facturacion-del-proyecto.md): sea por hora, por hito o por abono, al cierre de cada mes lo trabajado y lo facturado no coinciden. La NIIF 15 en sus cinco pasos está en [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md#cuándo-hay-un-ingreso-los-cinco-pasos-de-la-niif-15), y la regla de fondo de registrar en el período en que pasa, en [devengado](../../Contabilidad/Registro/devengado.md). De un servicio importa cómo se mide el avance en horas y qué nombre lleva la diferencia.

El nombre se presta a confusión. En una fábrica, el trabajo en curso es el inventario a medio hacer, medido a costo, como en [sistemas de costeo](../../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md#por-órdenes-o-por-procesos-qué-se-acumula). En una firma de servicios se usa para lo trabajado sin facturar, y el sistema de gestión de servicios leído lo guarda a precio de venta. Es lectura de esta base: el término inglés *work in progress* cubre los dos usos.

## Por qué un servicio se reconoce a medida que se trabaja

La NIIF 15 reconoce el ingreso a lo largo del tiempo si se cumple alguno de tres criterios (párrafo 35). El primero describe lo que Grant Thornton llama «typical service contracts»; que un servicio profesional sea uno de ellos es lectura de esta base. Dice que el cliente «simultaneously receives and consumes the benefits provided by the entity's performance as the entity performs». Una consultoría, una auditoría o el soporte de un sistema se consumen mientras se prestan.

Si el ingreso se reconoce a lo largo del tiempo, la firma tiene que medir el avance (párrafo 39) y elegir un solo método por obligación (párrafo 40): «An entity shall apply a single method of measuring progress for each performance obligation satisfied over time.» Los métodos posibles son de producto o de insumo (párrafo 41).

## Medir el avance: producto o insumo

| Familia | Qué mide | Ejemplos de la norma | En un servicio |
|---|---|---|---|
| Producto (B15-B17) | El valor que recibió el cliente | Encuestas del trabajo hecho, evaluaciones de resultados | Entregables aceptados, [hitos](../Proyecto-del-cliente/hitos-y-entregables.md) |
| Insumo (B18-B19) | Lo que puso la firma | «resources consumed, labour hours expended, costs incurred, time elapsed or machine hours used» | Horas aprobadas sobre horas presupuestadas |

En un servicio, el insumo natural son las horas: si el [presupuesto del proyecto](../Proyecto-del-cliente/presupuesto-del-proyecto.md) dice 400 horas y van 100 aprobadas, el avance es del 25 %. Este ejemplo es propio. El párrafo B19 pide un ajuste: si un costo no refleja avance (un error que hubo que rehacer, una compra que todavía no se usó), se saca de la medida.

El Ejemplo 19 de la norma muestra ese ajuste con números. Un contrato de CU5.000.000 tiene costos esperados de CU4.000.000, de los cuales CU1.500.000 son ascensores comprados antes de instalarse; se excluyen de la medida. Con CU500.000 de costo incurrido sin los ascensores, el avance es «20 per cent complete (ie CU500,000 ÷ CU2,500,000)», y el ingreso, «(20 per cent × CU3,500,000) + CU1,500,000», o sea CU2.200.000. Es un ejemplo de construcción; en un servicio el equivalente sería, en lectura de esta base, una licencia de software que la firma compra para el cliente y que no mide avance del trabajo.

Cómo se mide el avance como método de seguimiento, con el valor ganado, está en [medir el avance](../../Gestion-de-proyectos/Seguimiento/medir-el-avance.md#el-valor-ganado-y-la-estabilidad-del-cpi). Es el mismo dato con otro fin: allá para saber cuánto falta, acá para saber cuánto ingreso hay.

En tiempo y materiales no hace falta medir nada: el párrafo B16 deja reconocer como ingreso el monto que la firma tiene derecho a facturar, y el Ejemplo 42 lo muestra con un servicio en que el cliente paga «an hourly rate of CU25». Está en [facturación por hora](facturacion-por-hora.md#el-ingreso-es-lo-facturable).

## Activo del contrato, cuenta a cobrar y pasivo del contrato

Cuando alguna de las partes cumplió, la firma presenta el contrato como «a contract asset or a contract liability» (párrafo 105). La norma da tres nombres:

- **Pasivo del contrato** (párrafo 106): el cliente pagó, o la firma tiene derecho incondicional a cobrar, antes de que la firma trabaje. Es lo facturado de más: un anticipo, una bolsa de horas sin consumir. En la Argentina, cobrar por adelantado obliga a facturar, como dice [servicios profesionales en la Argentina](../servicios-profesionales-en-argentina.md#cuándo-nace-la-obligación-de-facturar).
- **Activo del contrato** (párrafo 107): la firma trabajó antes de que el cliente pague, y su derecho a cobrar depende de algo más que el paso del tiempo. Lectura de esta base: esa condición suele ser alcanzar el próximo hito. La norma pide además evaluar su deterioro con la NIIF 9, igual que el de un activo financiero.
- **Cuenta a cobrar** (párrafo 108): «A receivable is an entity's right to consideration that is unconditional.» Solo falta que llegue la fecha.

La norma no obliga a usar esos nombres (párrafo 109): una firma puede seguir diciendo «trabajo en curso sin facturar» o «ingreso diferido». Lectura de esta base sobre los tres párrafos:

| Situación al cierre del mes | Nombre según la NIIF 15 |
|---|---|
| Por hora: horas aprobadas, factura del mes todavía no emitida | Cuenta a cobrar, si solo falta emitir según el calendario |
| Precio cerrado: avance del 40 %, primer hito facturable al 50 % | Activo del contrato |
| Anticipo del 30 % cobrado, avance del 10 % | Pasivo del contrato por la diferencia |
| Bolsa de 40 horas pagada, 15 consumidas | Pasivo del contrato por las 25 restantes (aplicación del párrafo 106 y de B44 a la bolsa, ver [abono y bolsa de horas](abono-y-bolsa-de-horas.md)) |

Los ejemplos de la tabla son propios. La clasificación de la primera fila es la más discutible: depende de si el contrato da derecho a facturar las horas sin otra condición. Dinero y norma: lo de esta sección tiene dos fuentes, la IFRS Foundation y el ASC 606 de los Estados Unidos, leído en el texto que reproduce Grant Thornton. Los criterios de reconocimiento a lo largo del tiempo (606-10-25-27), la presentación del pasivo del contrato (606-10-45-2) y el atajo de la hora facturable (606-10-55-18) coinciden con los párrafos 35, 106 y B16.

La NIIF 15 reemplazó a la NIC 11 (contratos de construcción) y a la NIC 18 (ingresos) para los ejercicios que empiezan desde el 1 de enero de 2018. Lo que se escriba sobre «porcentaje de avance» con la terminología vieja viene de la NIC 11, cuyo texto no se leyó.

## Cómo lo llevan los sistemas

Un sistema de gestión de servicios no guarda el trabajo en curso como un saldo sino como transacciones: cada hora aprobada de una línea por tiempo y materiales crea una venta sin facturar, que se junta en una bandeja de todo lo pendiente de facturar de todos los contratos. Los hitos de precio cerrado van en otra vista. El saldo sale de sumar. Un sistema abierto muestra la rentabilidad del proyecto en tres columnas de ingreso: vendido, entregado y facturado. Entre «entregado» y «facturado» está el trabajo en curso.

Lectura de esta base sobre los dos: el trabajo en curso a precio de venta sirve para facturar y para ver cuánta plata está parada; el ingreso contable, en un precio cerrado, sale del avance y no de las horas a tarifa. Un sistema que solo tiene el primero sirve para facturar por hora, pero no para cerrar el mes de un proyecto a precio cerrado. El asiento de cierre que lleva cada mes al ingreso correcto es un [ajuste de cierre](../../Contabilidad/Estados-contables/ajustes-de-cierre.md).

## Cuánto tiempo tarda en volverse plata

Cuánto del trabajo en curso se castiga antes de facturarse y cobrarse es la [realización](../Rentabilidad-de-la-firma/realizacion.md). Cuántos días tarda en volverse plata es otra medida, que los estudios jurídicos llaman *lockup*. Según un artículo de Kreston Reeves, una firma contable del Reino Unido, el *lock-up* mide «the time taken to convert work done into cash received» y se calcula como «Lock up days = WIP days + Debtor days»: los días de trabajo en curso son el tiempo promedio entre el trabajo hecho y la factura emitida, y los días de deudores, el que va de la factura al cobro. Con cifras de ese artículo, 120 días de *lock-up* inmovilizan unas 3,2 millones de libras en trabajo en curso y deudores para una firma que factura 10 millones al año. Una página del Instituto de Finanzas y Gestión Legal (ILFM) repite la definición y el ejemplo, pero lleva la misma firma de autor, de modo que cuenta como una sola fuente. Es práctica de estudios jurídicos británicos y no un estándar.

> [!NOTE] Sin fuente todavía: otra definición independiente del *lock-up* (el Law Society de Escocia da una variante, el valor del trabajo en curso más los deudores, pero su página dio 403), cifras de referencia por rubro y la práctica de estudios para dar de baja trabajo en curso que no se va a cobrar. Ninguna guía de colegios profesionales se pudo leer.
