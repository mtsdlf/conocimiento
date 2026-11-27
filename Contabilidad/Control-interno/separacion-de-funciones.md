---
resumen: >-
  La separación de funciones reparte cada operación entre varias personas (quien la autoriza, quien la registra y quien custodia el bien) para que nadie pueda cometer un error o un fraude y además esconderlo.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 8.2 y 8.3: https://openstax.org/books/principles-financial-accounting/pages/8-3-describe-internal-controls-within-an-organization"
  - "University of Missouri System, política de segregación de funciones: https://www.umsystem.edu/ums/policies/finance/segregation"
  - "COSO, Internal Control — Integrated Framework, Executive Summary (2013): https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf"
  - "ACFE, Occupational Fraud 2024: A Report to the Nations, p. 103 y sección de colusión: https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf"
  - "Indiana State Board of Accounts, cap. 14 Information Technology Controls, 14.2: https://secure.in.gov/sboa/files/CH14-Information-Technology-Controls_9-25.pdf"
  - "Contabilidad/.investigacion/control-interno.md (2026-11-27)"
aliases: [segregación de funciones, segregation of duties, SoD, separación de tareas, oposición de intereses, controles compensatorios, compensating controls]
creado: 2026-11-27
revisado:
---

# Separación de funciones

La separación de funciones reparte cada operación entre varias personas (quien la autoriza, quien la registra y quien custodia el bien) para que nadie pueda cometer un error o un fraude y además esconderlo.

Es una de las actividades de control de COSO, que la pone adentro de las demás: "Segregation of duties is typically built into the selection and development of control activities." Por eso aparece en casi todas las notas de [control interno](control-interno.md): una [autorización](autorizaciones.md) no sirve si la firma el mismo que paga, y una [conciliación](conciliaciones.md) no detecta nada si la hace quien maneja la caja.

## Autorizar, registrar y custodiar

La forma clásica de enseñarla separa tres funciones:

| Función | Qué hace | Ejemplo en una compra |
|---|---|---|
| Autorizar | Decide que la operación se haga | El responsable aprueba la orden de compra |
| Registrar | La anota en los libros | Contabilidad carga la factura del proveedor |
| Custodiar | Tiene el bien o la plata | El depósito recibe la mercadería; tesorería tiene la chequera |

OpenStax lo explica con dos ideas. La primera es separar la custodia del registro: quien controla un activo no puede llevar también sus registros contables. La segunda es que en la mayoría de las operaciones intervengan al menos dos personas. Sus ejemplos: quien pide el inventario no lo recibe, y quien prepara un cheque no lo firma.

La política de la Universidad de Missouri, una fuente institucional y no una norma general, separa cinco funciones: autorización, registro, verificación, custodia de activos y revisión gerencial. Su regla es que ninguna persona tenga a su cargo dos o más de esas funciones principales (el extracto leído también habla de un piso de no más de dos funciones por persona; no se pudo verificar cuál de las dos rige).

Muchos textos de práctica suman «conciliar» como cuarta función, separada de las otras tres. Es una lectura razonable, porque una conciliación hecha por quien custodia la caja puede tapar un faltante, pero ninguna de las fuentes leídas la pone como función aparte: Missouri trata la conciliación como un control compensatorio.

## Las combinaciones que no se permiten

El principio se aplica mirando de a pares: qué dos tareas, juntas en una persona, le permiten hacer algo y ocultarlo. Missouri da tres reglas: nadie debería poder iniciar, aprobar y revisar la misma acción; nadie autoriza su propio reintegro; y autorización, verificación y revisión gerencial no las hace la misma persona.

| Combinación incompatible | Qué permite | Fuente del ejemplo |
|---|---|---|
| Pedir la compra y recibirla | Comprar para uno y declarar que llegó | OpenStax 8.3 |
| Preparar el cheque y firmarlo | Pagar a quien uno quiera | OpenStax 8.3 |
| Custodiar el efectivo y registrarlo | Quedarse con la plata y ajustar los libros | OpenStax 8.3 |
| Contar el efectivo y preparar el depósito | Depositar menos de lo contado | OpenStax 8.3 |
| Autorizar un gasto y cobrarlo como reintegro | Aprobarse a uno mismo | Missouri |
| Abrir un préstamo sin que nadie lo revise | Dar préstamos ficticios | OpenStax 8.2 |
| Dar de alta un proveedor, aprobar su factura y pagarla | Pagarle a un proveedor inventado | práctica común; ver [autorizaciones](autorizaciones.md) |

El caso del préstamo es real: OpenStax cuenta el de un banco de Enid, Oklahoma, donde no había separación de funciones para abrir préstamos y una sola empleada abrió préstamos fraudulentos. El de la última fila es el que más le importa a quien diseña un sistema de compras y pagos ([compras y cuentas a pagar](../Operaciones/compras-y-cuentas-a-pagar.md)), y no tiene una fuente neutral que lo formule.

## Lo que se pierde cuando se ponen de acuerdo

La separación supone que dos personas no se ponen de acuerdo. Cuando lo hacen (colusión), el control se elude, y COSO la nombra entre los límites del control interno. La ACFE midió el efecto en su informe de 2024:

| Perpetradores | Pérdida mediana | Duración mediana | Pérdida por mes |
|---|---|---|---|
| Uno | USD 75,000 | 12 meses | USD 6,300 |
| Dos | USD 135,000 | 12 meses | USD 11,300 |

Con tres o más, las pérdidas fueron "more than twice as high" que con dos, y la ACFE lo atribuye a que "The higher losses associated with collusive schemes could be related to easier circumvention of controls, such as separation of duties".

La misma ACFE pone la separación primera en su lista de controles de prevención, junto con otros que la complementan: "Proper separation of duties", "Use of authorizations", "Physical safeguards", "Job rotations", "Mandatory vacations". Las vacaciones obligatorias y la rotación sirven, por inferencia de la base, porque otra persona hace la tarea un tiempo y ve lo que el titular escondía.

## Controles compensatorios cuando no alcanza la gente

En una empresa chica no hay cinco personas para cinco funciones. COSO lo prevé: "Where segregation of duties is not practical, management selects and develops alternative control activities." Missouri exige lo mismo: cuando una persona junta funciones, hay que establecer controles mitigantes o compensatorios.

Los que nombra Missouri son estos:

- Una revisión frecuente y detallada, hecha y documentada por un supervisor, cuando quien registra también verifica.
- Pistas de auditoría que muestren quién hizo cada cosa.
- Conciliaciones de lo que procesa cada sistema.
- Reportes de excepciones que mira un supervisor.
- Revisiones gerenciales periódicas.

Lo que tienen en común es que un tercero mira, después y con evidencia, lo que una persona hizo sola. La confianza en esa persona no cuenta como control. El caso de la cooperativa de Iowa que cuenta OpenStax (más de 2,7 millones de dólares en 37 años, una empleada sin vacaciones y única dueña de la contraseña) es lo que pasa cuando no hay ni separación ni compensación.

## Lo que un sistema tiene que poder impedir

En un sistema de gestión, la separación se implementa con perfiles de acceso que definen, según el manual de control del Indiana State Board of Accounts, qué datos ve cada usuario y qué funciones puede hacer, con el acceso mínimo para su trabajo y revisado cada tanto por la gerencia. Para eso (inferencia de la base) el registro tiene que poder distinguir la acción (crear, aprobar, pagar, conciliar) del objeto, y negar a un mismo usuario dos acciones incompatibles sobre la misma operación, también cuando ese usuario es administrador. Cuando la empresa decide permitir la combinación, el sistema tiene que dejar rastro para el control compensatorio: quién hizo cada paso y cuándo. Cómo se diseñan los accesos y el registro de quién hizo qué está en [controles sobre los sistemas](controles-sobre-sistemas.md); el rastro de cada cambio de saldo, en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md).

> [!NOTE] Sin fuente todavía: un catálogo neutral (de un regulador, el IIA o un texto académico) de combinaciones incompatibles por ciclo (compras, ventas, sueldos, tesorería).
