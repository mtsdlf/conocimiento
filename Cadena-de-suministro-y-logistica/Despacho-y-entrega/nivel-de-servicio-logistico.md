---
resumen: >-
  El nivel de servicio logístico mide si las entregas llegaron como se prometieron: a tiempo y completas (OTIF), y además sin daño y con la documentación y la factura correctas (pedido perfecto). Sus definiciones cambian según quién las fija, así que cada indicador tiene que decir contra qué fecha, con qué tolerancia y por pedido o por línea se calcula.
estado: vigente
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.4.1.4 «Develop and maintain delivery service policy», 4.4.1.6 «Define key performance measures» y 4.4.4.2 «Track carrier delivery performance»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "APQC, Perfect order performance, medida de benchmarking (solo el fragmento del buscador; la página dio 403; según el resumen): https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/perfect-order-performance"
  - "KPMG, Beyond OTIF: Why Perfect Order Performance Matters (2026), fuente secundaria que cita a APQC: https://kpmg.com/us/en/articles/2026/perfect-order-performance.html"
  - "CASRAI Dictionary, SCOR Model: Framework, Metrics and Guide, sección de RL.1.1 (fuente secundaria de calidad dudosa): https://casrai.org/guides/scor-model"
  - "CSCMP, Supply Chain Management Terms and Glossary (2013), entrada perfect order (copia no oficial): https://www.cisco-eagle.com/uploads/cscmp/cscmp-glossary.pdf"
  - "ASCM, SCOR Digital Standard, introducción (© 2020, v13), tabla 2 (métricas de nivel 1): https://www.ascm.org/globalassets/ascm_website_assets/docs/intro-and-front-matter-scor-digital-standard.pdf"
  - "Wikipedia, Order fulfillment (según el resumen): https://en.wikipedia.org/wiki/Order_fulfillment"
  - "Odoo 17.0, modelo de transferencias (scheduled_date, date_deadline, date_done): https://raw.githubusercontent.com/odoo/odoo/17.0/addons/stock/models/stock_picking.py"
  - "Cadena-de-suministro-y-logistica/.investigacion/despacho-y-entrega.md (componente nivel-de-servicio-logistico)"
  - "Cadena-de-suministro-y-logistica/.investigacion/despacho-y-entrega-2.md (componente nivel-de-servicio-logistico)"
aliases: [nivel de servicio logístico, nivel de servicio de la entrega, servicio al cliente logístico, OTIF, on time in full, a tiempo y completo, entregas a tiempo, on-time delivery, pedido perfecto, perfect order, perfect order fulfillment, perfect order performance, RL.1.1, tasa de llenado, fill rate, tasa de cumplimiento, entregas completas, tiempo de ciclo del pedido, order fulfillment cycle time]
creado: 2026-11-27
revisado: 2026-11-27
---

# Nivel de servicio logístico

El nivel de servicio logístico mide si las entregas llegaron como se prometieron: a tiempo y completas (OTIF), y además sin daño y con la documentación y la factura correctas (pedido perfecto). Sus definiciones cambian según quién las fija, así que cada indicador tiene que decir contra qué fecha, con qué tolerancia y por pedido o por línea se calcula.

Es la vuelta de control de [Despacho y entrega](despacho-y-entrega.md). Compara la [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md) del pedido de venta con lo que registró la [prueba de entrega](prueba-de-entrega.md): cuándo llegó, cuánto llegó y en qué estado. APQC no le da un proceso propio. Lo reparte entre fijar la política de servicio de la entrega (4.4.1.4 «Develop and maintain delivery service policy»), definir las medidas (4.4.1.6 «Define key performance measures») y seguir el desempeño de los transportistas (4.4.4.2 «Track carrier delivery performance»).

## No es el nivel de servicio del stock

El mismo nombre se usa para dos cosas. El nivel de servicio del stock mide si había stock cuando se lo pidió: qué parte de los ciclos de reposición terminan sin faltante, o qué parte de la demanda se atendió con lo que había en mano. Está en [indicadores de inventario](../../Inventario-y-depositos/Reposicion/indicadores-de-inventario.md#nivel-de-servicio) y se dimensiona con el [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md).

El nivel de servicio logístico mide otra cosa: si el pedido llegó a las manos del cliente cuando y como se prometió. Puede haber stock de sobra y entregar tarde porque el camión salió tarde; puede faltar stock y entregar a tiempo lo que había. Un tablero que muestra «nivel de servicio» tiene que decir de cuál habla (criterio de la base).

## OTIF, pedido perfecto y tasa de cumplimiento de la entrega

| Indicador | Qué pregunta | Lo que se encontró |
|---|---|---|
| A tiempo y completo (OTIF) | ¿llegó para la fecha y con todo? | sin definición de una fuente con autoridad |
| Pedido perfecto | ¿salió bien en todas las dimensiones a la vez? | cuatro componentes según APQC (fragmento) y SCOR (vía una fuente dudosa) |
| Tasa de cumplimiento de la entrega (fill rate) | ¿qué parte de lo pedido se entregó? | sin definición de fuente para la entrega; la tasa de cumplimiento del stock está en [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md), de Inventario |
| Tiempo de ciclo del pedido | ¿cuánto tardó de punta a punta? | «the period from order receipt to product delivery», según una fuente secundaria |

El pedido perfecto, según un fragmento del buscador de la medida de APQC, se calcula como «(% on time delivery) multiplied by (% complete orders) multiplied by (% damage free) multiplied by (% accurate documentation) then multiplied by 100». La encuesta de APQC, según el mismo fragmento, suma exactitud en la toma del pedido, asignación inmediata de stock y factura correcta.

SCOR lo tiene como RL.1.1, «Perfect Order Fulfillment», en el atributo de confiabilidad. Según CASRAI, una fuente secundaria de calidad dudosa, se arma con cuatro métricas: «RL.2.1 (Delivered in Full)», «RL.2.2 (Delivery to Commit Date)», «RL.2.3 (Documentation Accuracy)» y «RL.2.4 (Perfect Condition)». Coincide con APQC en los cuatro componentes. Del estándar solo se leyó la introducción de ASCM, que confirma la métrica de nivel 1 (está en [marcos de la cadena de suministro](../Fundamentos/marcos-de-la-cadena-de-suministro.md#los-cinco-atributos-de-desempeño)); los componentes de nivel 2 no se pudieron leer ahí. Para ellos hay dos fuentes secundarias que coinciden, no una de autoridad.

KPMG presenta el OTIF como la versión angosta del pedido perfecto: «A perfect order is achieved when every critical order dimension is right at the same time. That makes the definition broader—and the performance challenge harder—than traditional OTIF measurement». Es decir, OTIF mira dos de las dimensiones (a tiempo, completo) y el pedido perfecto todas.

> [!NOTE] Sin fuente todavía: el texto de SCOR para RL.1.1 y sus componentes (el sitio de ASCM no se pudo abrir), una definición de OTIF y de tasa de cumplimiento de la entrega de una fuente con autoridad, y las ventanas de tolerancia y penalidades que piden los minoristas grandes.

## Por qué las definiciones varían

KPMG lista las dimensiones que muchas organizaciones miran: «On time», «In full / complete», «In condition / damage-free / quality-correct», «Correctly billed / invoiced» y «Supported with complete and accurate documentation». Y agrega: «These dimensions can vary by industry and customer requirements».

Tres decisiones cambian el número, y ninguna fuente leída las fija (lectura de la base):

- Contra qué fecha: la que pidió el cliente, la que se le prometió o la que se programó para despachar. El SCOR de CASRAI dice «Commit Date», la comprometida; el glosario del CSCMP define el pedido perfecto contra la fecha pedida por el cliente («Delivered on time to customer's request date»).
- Con qué tolerancia: un día antes o después, una franja horaria, o la fecha exacta.
- Con qué grano: por pedido (llegó todo o no) o por línea (qué parte de las líneas llegó completa). Un pedido de diez líneas con una incompleta es 0 % por pedido y 90 % por línea.

Por eso, a juicio de la base, cuando un cliente mide a su proveedor con OTIF la definición la pone el cliente, y el sistema tiene que poder calcular la suya.

## Por qué el pedido perfecto da bajo

El pedido perfecto multiplica, y por eso cae rápido. KPMG da el ejemplo: «If five order dimensions each perform at 95 percent, the compounded perfect order rate falls to about 77 percent». La cuenta se verifica: 0,95 a la quinta da 0,774.

Como referencia, KPMG cita datos de APQC: «APQC benchmarking data puts median perfect order performance at roughly 90 percent [...] while top-quartile performers reach 95 percent or higher». Es una cifra de una consultora que cita a otra fuente que no se pudo abrir, sin año de los datos; sirve de orden de magnitud, no de meta.

## Qué hay que guardar para poder medirlo

Los datos salen de los componentes del pedido perfecto; el esquema es inferencia de la base, no un modelo publicado:

- Por línea del pedido: la fecha comprometida con el cliente, la cantidad pedida y la cantidad entregada.
- Por entrega: la fecha real en que el cliente recibió (la de la [prueba de entrega](prueba-de-entrega.md), no la de salida del depósito), si llegó con daño y si la documentación estaba completa.
- Por factura: si salió correcta o hubo que corregirla.
- Por transportista: las mismas marcas, para seguir su desempeño, como pide APQC 4.4.4.2.

Uno de los sistemas abiertos consultados guarda en cada documento de salida una fecha programada, una fecha límite y la fecha en que se hizo. Esas fechas alcanzan para medir si salió a tiempo, pero el sistema no guarda ahí una fecha prometida al cliente distinta de la programada. Si la promesa vive solo en el pedido de venta, el indicador tiene que ir a buscarla ahí (inferencia de la base).

## Fallas de la medición

Las tres fallas que siguen son criterio de la base.

- Se mide la salida y no la llegada. «Despachado a tiempo» no es «entregado a tiempo»; el tramo del transportista queda afuera.
- Se cambia la fecha prometida cuando se atrasa. Si la fecha comprometida se reescribe, el indicador da siempre a tiempo. La fecha original tiene que quedar guardada.
- Se mezcla el grano. Un tablero por línea y otro por pedido dan números distintos para la misma operación, y los dos son correctos.
