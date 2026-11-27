---
resumen: >-
  El contrato marco es el acuerdo con un proveedor que fija precio y condiciones para las compras de un período, a veces con una cantidad comprometida, sin pedir nada todavía. Las compras concretas se hacen después con órdenes que lo usan, y lo que queda por consumir se sigue contra lo acordado.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft, Dynamics 365 Supply Chain Management, Purchase agreements (práctica de un ERP grande): https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements"
  - "ERPNext, Blanket Order (práctica de un sistema abierto): https://docs.frappe.io/erpnext/user/manual/en/blanket-order"
  - "Wikipedia, Framework agreement (consultada 2026-11-27): https://en.wikipedia.org/wiki/Framework_agreement"
  - "UK Government, The Sourcing Playbook, sección 6: https://www.gov.uk/government/publications/the-sourcing-and-consultancy-playbooks/the-sourcing-playbook-html"
  - "CIPS, Kraljic Matrix: https://1prd-dxp.cips.org/intelligence-hub/supplier-relationship-management/kraljic-matrix"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.2.3 «Negotiate and establish contracts» y 4.2.2.4 «Manage contracts»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Compras-y-abastecimiento/.investigacion/abastecimiento-estrategico.md (2026-11-27), sección 8"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (2026-11-27), sección 3"
aliases: [contrato marco, acuerdo marco, framework agreement, framework contract, blanket agreement, umbrella agreement, acuerdo de compra, purchase agreement, contrato de suministro, contrato de precios, acuerdo de precios]
creado: 2026-11-27
revisado: 2026-11-27
---

# Contrato marco

El contrato marco es el acuerdo con un proveedor que fija precio y condiciones para las compras de un período, a veces con una cantidad comprometida, sin pedir nada todavía. Las compras concretas se hacen después con órdenes que lo usan, y lo que queda por consumir se sigue contra lo acordado.

Cuando algo se compra muchas veces, el contrato marco es el resultado natural de [Abastecimiento estratégico](abastecimiento-estrategico.md) (lectura de esta base): la [cotización o licitación](cotizacion-y-licitacion.md) y la [negociación](negociacion-de-compras.md) se hacen una vez, y quedan escritas en el contrato. Este tema separa el acuerdo de su uso. El contrato marco es el acuerdo y vive acá, con las reglas que lo hacen valer; la orden abierta y la orden contra contrato están en [tipos de orden](../Orden-de-compra/tipos-de-orden.md). APQC pone las dos tareas del lado del acuerdo, «Negotiate and establish contracts» (4.2.2.3) y «Manage contracts» (4.2.2.4), y deja la orden en 4.2.3.

## Decidir una vez y comprar muchas

El contrato marco separa la decisión de la ejecución. Quien pide una resma de papel o un repuesto no tiene que buscar proveedor ni discutir precio: emite una orden contra contrato y el precio ya está. CIPS asigna al cuadrante no crítico de la [matriz de Kraljic](matriz-de-kraljic.md) contratos de sistema y compras electrónicas para estandarizar; el contrato marco cumple ese papel (criterio de la base).

También sirve en lo apalancable, para fijar por un año el precio que se logró licitando, y en el cuello de botella, para asegurar que el proveedor reserve capacidad. Estos dos usos son criterio de la base, coherente con las estrategias que CIPS da a cada cuadrante (licitar lo apalancable, asegurar el abastecimiento en el cuello de botella).

## Contrato con compromiso y acuerdo sin compromiso

Wikipedia distingue dos figuras, aunque está escrita desde el derecho de las compras públicas europeas y hay que usarla con cuidado:

| Figura | Qué obliga | Cómo se fija el precio |
|---|---|---|
| Contrato marco con compromiso (framework contract) | Hay una contraprestación inicial que asegura el compromiso del proveedor | La fuente no lo dice |
| Acuerdo marco sin compromiso (framework agreement, umbrella agreement) | Sin contraprestación, no hay obligación de comprar ni de vender | Lista de precios, fórmula o una nueva competencia entre los proveedores del acuerdo |

La misma fuente define el marco como el acuerdo que fija «the terms governing contracts to be awarded during a given period», con el precio y, si corresponde, «the quantity envisaged». La base usa «contrato marco» para las dos figuras; «acuerdo marco» es el nombre de la que no tiene compromiso de cantidad o monto, y se aclara cuál es cuando importa. Lo que no se consumió depende de la figura (inferencia de la base): con compromiso es un compromiso incumplido, y sin compromiso no hay obligación de comprar.

## Lo que registra un sistema

Dos sistemas muestran la práctica. Varios sistemas llaman «blanket order» al documento que acá es el contrato marco, y Microsoft lo llama «purchase agreement»; en esta base la orden abierta es otra cosa y está en [tipos de orden](../Orden-de-compra/tipos-de-orden.md). El sistema abierto lo describe así: su blanket order «records a long-term commitment to buy or sell specified items within an agreed period» a tarifas negociadas; no mueve bienes ni dinero, solo sirve de referencia a las órdenes que vienen después. Lleva el proveedor, las fechas de vigencia y, por artículo, la cantidad total comprometida, la tarifa y la cantidad ya ordenada, que es «The quantity already referenced by submitted downstream orders».

De ahí sale el seguimiento del consumo: lo comprometido menos lo ordenado es lo que queda por liberar, y las órdenes canceladas no cuentan. Con eso se puede ver si el contrato se está usando y si va a quedar volumen sin comprar (lectura de la base). Según la misma documentación, el contrato «may not automatically close» al vencer: alguien tiene que mirar el saldo al final del período.

## Las reglas que hacen valer el contrato

La documentación de Microsoft describe el acuerdo como un contrato que compromete a comprar una cantidad o un monto con varias órdenes a lo largo del tiempo, a cambio de precios y descuentos especiales. El compromiso puede ser por la cantidad de un producto, por el monto de un producto, por el monto de una categoría o por el monto de cualquier producto. El acuerdo tiene vigencia, se activa y se cierra. Dos políticas definen qué tan firme es:

- **Tope**: el total de las órdenes no puede superar el compromiso.
- **Precio fijo**: si una orden trae otro precio o descuento, se rompe el vínculo con el acuerdo y ese renglón no cuenta para cumplir el compromiso.

También admite montos mínimo y máximo por liberación. El acuerdo se aplica al crear la orden, no después, y guarda una versión cada vez que se confirma (cómo se versionan las órdenes está en [cambios y cancelaciones de la orden](../Orden-de-compra/cambios-y-cancelaciones-de-la-orden.md)).

Para quien diseña un sistema, el contrato marco es un documento con vigencia y saldo, no una lista de precios. Una lista de precios dice cuánto cuesta algo (está en [condiciones del proveedor](../Proveedores/condiciones-del-proveedor.md)); el contrato dice además hasta cuándo, cuánto se comprometió y cuánto se usó. Es criterio de la base.

## Las órdenes que lo consumen

La orden abierta es una orden de compra por un total o un período, con entregas que se liberan de a poco. La orden contra contrato es la que toma precio y condiciones de un contrato marco; en inglés se la llama call-off o release, y en castellano también liberación. La guía de compras del gobierno británico advierte que «Call-off contracts from frameworks (and dynamic purchasing systems) need to be fully understood»: quien compra tiene que saber qué condiciones heredó cada orden. La misma guía indica comprar lo común por un marco del gobierno y lo hecho a medida por un proceso completo, partición parecida a la que hace la matriz de Kraljic entre lo rutinario y lo estratégico (lectura de esta base). Qué hereda cada orden y qué necesita está en [tipos de orden](../Orden-de-compra/tipos-de-orden.md).

Una compra que saltea el contrato marco vigente, a otro proveedor o a otro precio, es compra fuera del circuito (maverick spending; la definición completa está en [solicitud de compra](../Orden-de-compra/solicitud-de-compra.md)). Pierde el precio acordado y deja sin consumir el volumen comprometido (criterio de la base). En el [análisis del gasto](analisis-del-gasto.md) aparece como gasto sin acuerdo.

> [!NOTE] Sin fuente todavía: duración típica de un contrato marco, cláusulas habituales (precio fijo o indexado, mínimos, exclusividad, qué pasa si no se consume el volumen comprometido) y en qué se diferencia de un contrato de suministro.
