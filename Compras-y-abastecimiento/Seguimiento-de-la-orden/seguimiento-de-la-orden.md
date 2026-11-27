---
resumen: >-
  El seguimiento de la orden es lo que hace Compras desde que emite una orden de compra hasta que lo recibido coincide con lo pedido: obtener la confirmación del proveedor, perseguir las entregas, comparar cada recepción con la orden y decidir qué hacer con la diferencia. Ahí termina el trabajo de Compras, aunque la orden siga abierta hasta que llegue la factura.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.3.5 a 4.2.3.7 y 4.4.2: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "CIPS, The thirteen steps of the procurement process, pasos 9 a 11 (según su resumen): https://1prd-dxp.cips.org/intelligence-hub/procurement/procurement-process"
  - "ERPNext, Purchase Receipt (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt"
  - "ERPNext, Purchase Order (estados; según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-order"
  - "Microsoft Learn, Approve and confirm purchase orders (Dynamics 365 Supply Chain Management): https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (2026-11-27), secciones 5 a 8"
  - "Compras-y-abastecimiento/.investigacion/apqc-4-2.md (2026-11-27)"
aliases: [seguimiento de la orden, seguimiento de órdenes de compra, purchase order follow-up, order tracking, PO reconciliation]
creado: 2026-11-27
revisado:
---

# Seguimiento de la orden

El seguimiento de la orden es lo que hace Compras desde que emite una orden de compra hasta que lo recibido coincide con lo pedido: obtener la confirmación del proveedor, perseguir las entregas, comparar cada recepción con la orden y decidir qué hacer con la diferencia. Ahí termina el trabajo de Compras, aunque la orden siga abierta hasta que llegue la factura.

Es la última vertical de [Compras y abastecimiento](../compras-y-abastecimiento.md). Recibe una orden ya aprobada y emitida de [Orden de compra](../Orden-de-compra/orden-de-compra.md), donde están el documento y sus estados; acá no se repiten. Lo que pasa en esta vertical (entregas a tiempo, completas, rechazos) es el dato con que [Proveedores](../Proveedores/proveedores.md) evalúa a cada proveedor.

## De la orden emitida a lo recibido

APQC 7.4 pone tres pasos dentro de «Order materials and services» (4.2.3) después de emitir la orden: 4.2.3.5 «Expedite orders and satisfy inquiries», 4.2.3.6 «Reconcile purchase orders» y 4.2.3.7 «Research/Resolve order exceptions». En otra categoría, 4.4.2 «Plan and manage inbound material flow», están vigilar el cumplimiento de las entregas (4.4.2.3) y el flujo de lo que se devuelve (4.4.2.4). CIPS, según su resumen, salta del paso 9 (adjudicar el contrato) al 10 (depósito, logística y recepción) sin un paso propio de seguimiento.

En la práctica la secuencia es esta:

1. **El proveedor confirma** la orden, con o sin cambios de precio o fecha.
2. **Compras persigue la entrega** hasta que llega, y a veces el proveedor avisa antes qué despacha.
3. **El depósito recibe**: cuenta, inspecciona y ubica. Eso es de Inventario y depósitos, en [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md).
4. **Compras compara** ese conteo con la orden, renglón por renglón, dentro de una tolerancia.
5. **Compras decide qué hacer con la diferencia**: esperar el saldo pendiente, cerrar el renglón, rechazar o devolver.
6. **Contabilidad cruza la factura** con la orden y la recepción. La deuda con el proveedor la registra ella: al recibir, como recibido sin facturar, y se confirma con la factura ([compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md#lo-recibido-sin-facturar)).

Los pasos 1 y 2 están en [confirmación y seguimiento](confirmacion-y-seguimiento.md); el 4, en [recepción contra lo pedido](recepcion-contra-lo-pedido.md); el 5, en [diferencias y devoluciones](diferencias-y-devoluciones.md).

## Dónde termina Compras y dónde sigue la orden

El trabajo de Compras termina cuando lo recibido coincide con lo pedido, o cuando alguien decide que el saldo no va a llegar. Ese es el corte de la base, que separa dominios por objeto y verbo. Los sistemas cortan en otro lado. En un ERP abierto, según su resumen, la orden queda «Completed» recién cuando está todo recibido y todo facturado. En uno grande el renglón pasa a recibido al llegar lo pedido, y la orden se finaliza cuando se cierra en lo financiero. En esta base, cerrar es dejar de esperar el saldo pendiente de una orden, y finalizar es el cierre administrativo o financiero de una orden ya completa.

No hay contradicción: los dos cortes responden preguntas distintas. La orden como documento sigue viva hasta la factura, porque Contabilidad la necesita para el [cruce de tres vías](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md#el-cruce-de-tres-vías-visto-desde-el-registro). El trabajo de Compras sobre ella, en cambio, ya terminó.

## Pedimos 100, llegaron 90 y dos están rotas

El mismo camión deja un registro distinto en cada dominio. El reparto de la tabla sigue las fuentes de cada nota enlazada; el orden y las cifras del caso son un ejemplo de la base.

| Dominio | Qué registra | Qué decide |
|---|---|---|
| Inventario y depósitos | Entraron 90 unidades al edificio: 88 pasan a disponibles y 2 quedan apartadas, sin poder venderse ([estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md)) | Dónde se guardan las 88 y dónde quedan las 2 |
| Compras | El renglón de la orden tiene 90 recibidas (88 aceptadas y 2 rechazadas) y un saldo pendiente de 10 | Si espera las 10 o cierra el renglón; si pide reposición o crédito por las 2 |
| Contabilidad | Lo recibido sin facturar; cuando llega la factura, la cruza con la orden y la recepción | Si la factura viene por 100, la retiene hasta que Compras resuelva la diferencia |

Si Compras no decide, la orden queda abierta por 10, con 2 rechazadas sin resolver, y las 10 quizá nunca lleguen. La evaluación del proveedor tampoco registra el faltante ni el rechazo (inferencia de la base).

## Qué hay en Seguimiento de la orden

- [Confirmación y seguimiento](confirmacion-y-seguimiento.md): el acuse del proveedor, la fecha que confirma, el aviso de despacho y el seguimiento de entregas.
- [Recepción contra lo pedido](recepcion-contra-lo-pedido.md): comparar lo recibido con la orden, las tolerancias, las entregas parciales, el saldo pendiente y el cierre del renglón.
- [Diferencias y devoluciones](diferencias-y-devoluciones.md): faltantes, sobrantes y rechazos; la devolución al proveedor y qué se le pide a cambio.
