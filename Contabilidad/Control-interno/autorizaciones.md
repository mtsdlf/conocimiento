---
resumen: >-
  Las autorizaciones definen quién puede aprobar cada tipo de operación y hasta qué monto, y los documentos numerados en forma correlativa permiten comprobar después que ninguna operación se hizo sin pasar por esa aprobación.
estado: borrador
estabilidad: semi
fuentes:
  - "COSO, Internal Control — Integrated Framework, Executive Summary (2013): https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf"
  - "OpenStax, Principles of Financial Accounting (2019), 8.3 Describe Internal Controls within an Organization: https://openstax.org/books/principles-financial-accounting/pages/8-3-describe-internal-controls-within-an-organization"
  - "Cornell University, Proper Authorization: https://finance.cornell.edu/node/904269"
  - "University of Missouri System, política de segregación de funciones: https://www.umsystem.edu/ums/policies/finance/segregation"
  - "ACFE, Occupational Fraud 2024: A Report to the Nations, esquemas y p. 103: https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf"
  - "Contabilidad/.investigacion/control-interno.md (2026-11-27)"
aliases: [autorización, aprobaciones, niveles de aprobación, matriz de autorizaciones, delegación de autoridad, delegation of authority, approval matrix, numeración correlativa, formularios prenumerados, prenumbered documents]
creado: 2026-11-27
revisado:
---

# Autorizaciones

Las autorizaciones definen quién puede aprobar cada tipo de operación y hasta qué monto, y los documentos numerados en forma correlativa permiten comprobar después que ninguna operación se hizo sin pasar por esa aprobación.

COSO pone las autorizaciones primeras en su lista de actividades de control ("authorizations and approvals, verifications, reconciliations"), y la ACFE las incluye entre los controles de prevención del fraude ("Use of authorizations"). Son un control preventivo en el sentido de que actúan antes de que la operación exista (clasificación de la base; ninguna fuente leída define el término). El marco general está en [control interno](control-interno.md).

Las fuentes abiertas sobre este tema son pocas y flacas. COSO y la ACFE nombran la autorización sin desarrollarla; lo demás sale de un libro de texto y de las políticas internas de dos universidades de Estados Unidos, que muestran cómo lo resuelve una institución pero no son una norma general.

## Niveles de aprobación y la matriz de autorizaciones

Una empresa que crece no puede hacer que el dueño apruebe cada compra, así que reparte la facultad de aprobar según el tipo de operación y el monto. La política de Cornell lo dice así: la autorización correcta la determina el plan de delegación de cada unidad y depende del tipo de transacción y del monto en dólares. La tabla que junta esas reglas se llama matriz de autorizaciones (delegation of authority, en inglés).

La estructura de una matriz se ve así. Los cargos y los tramos son ilustrativos: ninguna fuente leída da una matriz con montos.

| Tipo de operación | Tramo bajo | Tramo medio | Tramo alto |
|---|---|---|---|
| Orden de compra | Responsable del área | Gerente | Directorio o dueño |
| Alta o cambio de un proveedor | Compras propone, administración aprueba | igual | igual |
| Pago a proveedor | Tesorería, con la factura ya aprobada | Gerente de administración | Dos firmas |
| Reintegro de gastos | El superior de quien gastó | igual | igual |

Hay una regla que no depende del tramo: nadie aprueba lo propio. La política de Missouri lo dice para los reintegros (un empleado no puede autorizar su propio reintegro), y lo mismo vale para el superior que gasta y no puede aprobarse la rendición. Los reintegros y el fondo fijo están en [gastos y rendiciones](../Operaciones/gastos-y-rendiciones.md).

> [!NOTE] Sin fuente todavía: una guía neutral de delegación de autoridad (del IIA, de un regulador o de un manual del sector público) con tramos y criterios para fijarlos.

## La aprobación de pagos y el alta de proveedores

El pago a proveedores es un punto de riesgo. En el informe de la ACFE de 2024, la facturación ficticia apareció en el 22% de los casos, con una pérdida mediana de USD 100,000. La ACFE la define como "a fraudulent disbursement scheme in which a person causes their employer to issue a payment by submitting invoices for fictitious goods or services, inflated invoices, or invoices for personal purchases". La manipulación de cheques y pagos tuvo la pérdida mediana más alta entre los esquemas de apropiación de activos: USD 155,000.

El control que se recomienda junta autorización y [separación de funciones](separacion-de-funciones.md): quien crea o modifica un proveedor (su nombre, su cuenta bancaria) no aprueba sus facturas ni libera los pagos. Si una misma persona puede dar de alta un proveedor inventado, aprobar su factura y pagarla, el circuito entero de [compras y cuentas a pagar](../Operaciones/compras-y-cuentas-a-pagar.md) queda en sus manos. Esta recomendación sale solo de guías de empresas que venden software de pagos, sin autoridad independiente; las mismas guías piden que cada cambio en los datos de un proveedor guarde el valor viejo, el valor nuevo, el usuario y la hora.

Para quien construye el sistema, eso se traduce en tres capacidades: la aprobación es un paso registrado (quién, cuándo, sobre qué versión del documento), un pago sin factura aprobada no se puede emitir, y el cambio de la cuenta bancaria de un proveedor vuelve a pedir aprobación. Es una lectura propia de las fuentes de arriba. Cómo se guarda el rastro está en [controles sobre los sistemas](controles-sobre-sistemas.md).

## Numeración correlativa y formularios prenumerados

La numeración correlativa sirve, por inferencia de la base, para ver que la autorización no se salteó: OpenStax solo recomienda los formularios prenumerados. Si las órdenes de compra, los recibos o los cheques llevan un número que el sistema o la imprenta asigna en orden, cualquier número que falte o se repita se ve. OpenStax recomienda formularios prenumerados completados en tinta, para que no puedan alterarse, y copias de respaldo guardadas fuera del lugar. Esa es la única fuente encontrada sobre el tema.

El mismo capítulo de OpenStax liga la documentación con la responsabilidad: un sistema bien diseñado asigna cada rol a una persona, y si una sola persona tiene acceso a la caja, cualquier sobrante o faltante es suyo. Su ejemplo es la caja de un turno: si se registraron USD 800 de ventas, el efectivo, los cheques y los comprobantes de tarjeta tienen que sumar 800, y dos personas cuentan por separado. Los dos recuentos tienen que dar igual.

En un sistema, la numeración la asigna el registro y no el usuario, y un número no se reusa: un comprobante que se anula queda anulado con su número, y el siguiente sigue la serie. Es inferencia a partir de la regla de OpenStax, no una cita. Lo que exige la ley para la numeración de las facturas va al tema Impuestos, todavía no escrito.

> [!NOTE] Sin fuente todavía: un tratamiento propio de la numeración correlativa y el control de documentos fuera de la línea de OpenStax.
