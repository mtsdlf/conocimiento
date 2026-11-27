---
resumen: >-
  Los gastos del proyecto son los viajes, materiales y otros costos que la firma paga para un proyecto y le imputa. Algunos se trasladan al cliente y otros no; los que se trasladan se cobran a costo, con un recargo sobre el costo o con un precio por unidad, según lo que diga el contrato.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Project Operations, Set up cost and sales rates for expenses (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/pricing-costing/set-up-cost-sales-rates-expenses"
  - "Microsoft Learn, Project Operations, Sales price resolution (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/pricing-costing/sales-price-resolution-sales"
  - "Microsoft Learn, Project Operations, Manage contract values for project-based sales (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/manage-contract-values-project-based-sales"
  - "FAR 31.201-2 Determining allowability (según resumen): https://www.acquisition.gov/far/31.201-2"
  - "FAR 31.205-26 Material costs (según resumen): https://www.acquisition.gov/far/31.205-26"
  - "FAR 52.232-7 Payments under Time-and-Materials and Labor-Hour Contracts (según resumen): https://www.acquisition.gov/far/52.232-7"
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 9.6.2.3 y 9.6.2.4 (reembolsos y anticipos)"
  - "Servicios-profesionales-y-proyectos/.investigacion/asignacion-y-horas.md (sección 2.4)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 4.7)"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (sección 3.1)"
aliases: [gastos del proyecto, gastos reembolsables, reimbursable expenses, project expenses, gastos refacturables, recargo, markup, refacturar gastos, rebilling]
creado: 2026-11-27
revisado:
---

# Gastos del proyecto

Los gastos del proyecto son los viajes, materiales y otros costos que la firma paga para un proyecto y le imputa. Algunos se trasladan al cliente y otros no; los que se trasladan se cobran a costo, con un recargo sobre el costo o con un precio por unidad, según lo que diga el contrato.

Son la otra mitad del [registro de horas](registro-de-horas.md): un gasto imputado sigue el mismo recorrido que una hora (se carga, se aprueba, suma costo al proyecto y, si se cobra, pasa a la [facturación del proyecto](../Facturacion-del-proyecto/facturacion-del-proyecto.md)).

## Dos registros del mismo gasto

Un pasaje que paga una consultora para ir a lo del cliente aparece en dos lugares. Como gasto de la empresa, con su comprobante, su pago y, si lo adelantó una persona, su reintegro: eso es de [gastos y rendiciones](../../Contabilidad/Operaciones/gastos-y-rendiciones.md), en Contabilidad. Como gasto del proyecto, imputado a un proyecto y a veces a una tarea, con la marca de si se cobra: eso es de acá.

APQC solo tiene los reembolsos a empleados, en finanzas (9.6.2.3 «Approve reimbursements and advances» y 9.6.2.4 «Process reimbursements and advances»), sin vínculo con los proyectos. Como criterio de esta base, la imputación al proyecto se hace al aprobar el gasto y no al reintegrarlo, porque el costo del proyecto no puede esperar a que la persona rinda.

## Qué gasto se traslada al cliente

En ese sistema, un gasto entra a la factura solo si el contrato lo prevé. En un sistema de gestión de servicios, cada línea del contrato dice qué clases de transacción incluye (tiempo, gasto, material, honorario), y los gastos solo se facturan si la línea los incluye y si están marcados como cobrables.

Para decidir si un gasto se puede trasladar, el caso más exigente documentado es el de los contratos públicos de los Estados Unidos. Según el resumen de la FAR 31.201-2, un costo es admisible solo si es razonable, imputable a ese contrato, conforme a los términos del contrato, a los límites de la norma y a los estándares de costos aplicables (CAS) o, si no hay, a los principios contables generalmente aceptados, y el contratista tiene que guardar respaldo «adequate to demonstrate that costs claimed have been incurred»; si no, el funcionario puede rechazarlo. Es una norma de un tipo de contrato, no una regla para firmas privadas, pero sirve de lista de preguntas: ¿es razonable?, ¿es de este proyecto?, ¿lo permite el contrato?, ¿hay comprobante?

## A costo, con recargo o por tarifa

Un sistema documenta tres formas de poner el precio de venta de una categoría de gasto:

| Método | Precio al cliente | Ejemplo |
|---|---|---|
| A costo | El costo real del gasto | Un hotel se refactura por lo que costó |
| Recargo sobre el costo | Costo más un porcentaje | «the airfare sales rate should be marked up 10 percent over the cost of the incurred airfare expense» |
| Precio por unidad | Una tarifa fija por unidad | Un monto por kilómetro recorrido |

En ese sistema, en la estimación los métodos a costo y con recargo dan cero por defecto, porque solo se aplican al gasto real; y si falta la línea de precio de una categoría, el precio de venta es cero.

El contrato público estadounidense va al otro extremo con los materiales: según el resumen de la FAR 52.232-7 (una sola fuente, leída por resumen), «the Government will not pay profit or fee to the prime Contractor on materials», salvo las excepciones de la FAR 31.205-26. Y según el resumen de esa sección, al costo de los materiales se le restan los descuentos, reintegros y bonificaciones que la firma obtuvo: se traslada el costo neto.

> [!IMPORTANT]
> Es plata y hay una sola fuente de cada lado: el recargo está documentado por un sistema de gestión y la prohibición del recargo por una norma de contratos públicos de los Estados Unidos. No se leyó ninguna fuente sobre cuánto recargan las firmas privadas ni sobre las reglas de los colegios profesionales; la opinión formal de la asociación de abogados estadounidense sobre cargos de gastos al cliente no se pudo abrir. Lo que se cobra lo fija el contrato con cada cliente.

Qué factura y qué impuesto lleva un gasto refacturado en la Argentina está en [Servicios profesionales en la Argentina](../servicios-profesionales-en-argentina.md), y lo impositivo recurrente, en el tema Impuestos, que todavía no está escrito.

## Cuando el gasto no se cobra

Un gasto que no se traslada sigue siendo costo del proyecto y baja su margen. En un proyecto a precio cerrado, los gastos suelen estar dentro del precio y ninguno se refactura (criterio de esta base: depende de lo que diga el contrato). Cómo pesan en el margen está en [costo y margen del proyecto](../Rentabilidad-de-la-firma/costo-y-margen-del-proyecto.md).

Corregir un gasto aprobado sigue la misma regla que una hora: en el sistema documentado, el retiro de un gasto aprobado lo deja rechazado para que la persona lo corrija, y uno ya facturado necesita una factura correctiva antes. El detalle está en [hoja de horas](hoja-de-horas.md#corregir-una-hora-aprobada-o-facturada).
