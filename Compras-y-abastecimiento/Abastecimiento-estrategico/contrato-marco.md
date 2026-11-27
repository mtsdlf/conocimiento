---
resumen: >-
  El contrato marco es el acuerdo con un proveedor que fija precio y condiciones para las compras de un período, a veces con una cantidad comprometida, sin pedir nada todavía. Las compras concretas se hacen después con órdenes que lo usan, y lo que queda por consumir se sigue contra lo acordado.
estado: borrador
estabilidad: estable
fuentes:
  - "ERPNext, Blanket Order (práctica de un sistema abierto): https://docs.frappe.io/erpnext/user/manual/en/blanket-order"
  - "Wikipedia, Framework agreement (consultada 2026-11-27): https://en.wikipedia.org/wiki/Framework_agreement"
  - "UK Government, The Sourcing Playbook, sección 6: https://www.gov.uk/government/publications/the-sourcing-and-consultancy-playbooks/the-sourcing-playbook-html"
  - "CIPS, Kraljic Matrix: https://1prd-dxp.cips.org/intelligence-hub/supplier-relationship-management/kraljic-matrix"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.2.3 «Negotiate and establish contracts» y 4.2.2.4 «Manage contracts»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Compras-y-abastecimiento/.investigacion/abastecimiento-estrategico.md (2026-11-27), sección 8"
aliases: [contrato marco, acuerdo marco, framework agreement, framework contract, blanket agreement, umbrella agreement, acuerdo de compra, purchase agreement, contrato de suministro, contrato de precios, acuerdo de precios]
creado: 2026-11-27
revisado:
---

# Contrato marco

El contrato marco es el acuerdo con un proveedor que fija precio y condiciones para las compras de un período, a veces con una cantidad comprometida, sin pedir nada todavía. Las compras concretas se hacen después con órdenes que lo usan, y lo que queda por consumir se sigue contra lo acordado.

Es el resultado típico de [Abastecimiento estratégico](abastecimiento-estrategico.md) cuando algo se compra muchas veces: la [cotización o licitación](cotizacion-y-licitacion.md) y la [negociación](negociacion-de-compras.md) se hacen una vez, y quedan escritas en el contrato. Este tema separa el acuerdo de su uso. El contrato marco es el acuerdo y vive acá; la orden abierta y la orden contra contrato, que son las órdenes que lo consumen, están en [tipos de orden](../Orden-de-compra/tipos-de-orden.md). APQC pone las dos tareas del lado del acuerdo, «Negotiate and establish contracts» (4.2.2.3) y «Manage contracts» (4.2.2.4), y deja la orden en 4.2.3.

## Decidir una vez y comprar muchas

El contrato marco separa la decisión de la ejecución. Quien pide una resma de papel o un repuesto no tiene que buscar proveedor ni discutir precio: emite una orden contra contrato y el precio ya está. Es la estrategia que CIPS asigna al cuadrante no crítico de la [matriz de Kraljic](matriz-de-kraljic.md), con «contratos de sistema» y compras electrónicas para estandarizar y bajar el costo de cada compra.

También sirve en lo apalancable, para fijar por un año el precio que se logró licitando, y en el cuello de botella, para asegurar que el proveedor reserve capacidad. Estos dos usos son criterio de la base, coherente con las estrategias de cada cuadrante.

## Contrato con compromiso y acuerdo sin compromiso

La fuente leída distingue dos figuras, aunque está escrita desde el derecho de las compras públicas europeas y hay que usarla con cuidado:

| Figura | Qué obliga | Cómo se fija el precio |
|---|---|---|
| Contrato marco con compromiso (framework contract) | Hay una contraprestación inicial que asegura el compromiso del proveedor | En el contrato |
| Acuerdo marco sin compromiso (framework agreement, umbrella agreement) | Sin contraprestación, no hay obligación de comprar ni de vender | Lista de precios, fórmula o una nueva competencia entre los proveedores del acuerdo |

La misma fuente define el marco como el acuerdo que fija «the terms governing contracts to be awarded during a given period», con el precio y, si corresponde, «the quantity envisaged». La base usa «contrato marco» para las dos figuras y aclara cuál cuando importa: la diferencia decide si el proveedor puede reclamar por lo que no se compró.

## Lo que registra un sistema

Un sistema abierto muestra la práctica. Su contrato marco «records a long-term commitment to buy or sell specified items within an agreed period» a tarifas negociadas; no mueve bienes ni dinero, solo sirve de referencia a las órdenes que vienen después. Lleva el proveedor, las fechas de vigencia y, por artículo, la cantidad total comprometida, la tarifa y la cantidad ya ordenada, que es «The quantity already referenced by submitted downstream orders».

De ahí sale el seguimiento del consumo: lo comprometido menos lo ordenado es lo que queda por liberar, y las órdenes canceladas no cuentan. Con eso se responde si el contrato se está usando, si se va a consumir antes de vencer o si va a quedar volumen sin comprar. Qué pasa con lo que no se consumió lo decide el contrato, no el sistema.

Para quien diseña un sistema, el contrato marco es un documento con vigencia y saldo, no una lista de precios. Una lista de precios dice cuánto cuesta algo (está en [condiciones del proveedor](../Proveedores/condiciones-del-proveedor.md)); el contrato dice además hasta cuándo, cuánto se comprometió y cuánto se usó. Es criterio de la base.

## Las órdenes que lo consumen

Las compras contra el contrato se llaman call-off en inglés. La guía de compras del gobierno británico advierte que «Call-off contracts from frameworks (and dynamic purchasing systems) need to be fully understood»: quien compra tiene que saber qué condiciones heredó cada orden. La misma guía manda comprar lo común por un marco existente y lo hecho a medida por un proceso completo, que es la misma partición que hace la matriz de Kraljic entre lo rutinario y lo estratégico. Cómo es cada orden, la abierta y la que se emite contra el contrato, está en [tipos de orden](../Orden-de-compra/tipos-de-orden.md).

Una compra que se hace fuera del contrato vigente, a otro proveedor o a otro precio, es compra fuera del circuito (maverick spending): pierde el precio acordado y deja sin consumir el volumen comprometido (criterio de la base). Cómo se la detecta está en [análisis del gasto](analisis-del-gasto.md) y cómo se la evita al pedir, en [solicitud de compra](../Orden-de-compra/solicitud-de-compra.md).

> [!NOTE] Sin fuente todavía: duración típica de un contrato marco, cláusulas habituales (precio fijo o indexado, mínimos, exclusividad, qué pasa si no se consume el volumen comprometido) y en qué se diferencia de un contrato de suministro.
