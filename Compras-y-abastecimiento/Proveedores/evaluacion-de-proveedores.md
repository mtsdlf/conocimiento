---
resumen: >-
  La evaluación de proveedores mide si cada proveedor cumple, con indicadores que salen de sus entregas (a tiempo, completas, aceptadas por calidad) y de su respuesta comercial, y decide qué hacer con el que no cumple: seguir, vigilarlo o bloquearlo. Se repite cada cierto período y es la reevaluación de lo que se verificó en el alta.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.4.2 «Prepare/Analyze procurement and supplier performance» y 4.2.4.4 «Monitor quality of product delivered»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "ERPNext, Supplier Scorecard (leído por extracto; como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/buying/supplier-scorecard"
  - "NSW Government, The supplier relationship (leído por extracto): https://www.info.buy.nsw.gov.au/buyer-guidance/manage/the-supplier-relationship"
  - "DHL, glosario: On Time In Full (OTIF) (según su resumen): https://lot.dhl.com/glossary/on-time-in-full-otif/"
  - "Logistics Research Network 2021, paper de Cardiff sobre errores en el cálculo de OTIF (según su resumen): https://orca.cardiff.ac.uk/id/eprint/147303/1/LRN%202021%20Final%20Paper.pdf"
  - "ISMS.online, ISO 9001 cláusula 8.4 (según su resumen; no cita la norma literal): https://www.isms.online/iso-9001/clause-8-4-control-of-externally-provided-processes-products-services/"
  - "Compras-y-abastecimiento/.investigacion/proveedores.md (2026-11-27), sección 4"
aliases: [evaluación de proveedores, desempeño de proveedores, tablero de proveedores, supplier scorecard, vendor scorecard, supplier performance, supplier evaluation, vendor rating, reevaluación de proveedores, OTIF, on time in full, entrega a tiempo y completa]
creado: 2026-11-27
revisado:
---

# Evaluación de proveedores

La evaluación de proveedores mide si cada proveedor cumple, con indicadores que salen de sus entregas (a tiempo, completas, aceptadas por calidad) y de su respuesta comercial, y decide qué hacer con el que no cumple: seguir, vigilarlo o bloquearlo. Se repite cada cierto período y es la reevaluación de lo que se verificó en el alta.

Dentro de [Proveedores](proveedores.md), cierra el círculo que abre el [alta de proveedor](alta-de-proveedor.md): el alta verifica que el proveedor puede cumplir y la evaluación mide si cumplió. APQC 7.4 la reparte en analizar el desempeño de compras y de proveedores (4.2.4.2) y controlar la calidad de lo entregado (4.2.4.4). ISO 9001:2015, en su cláusula 8.4, pide evaluar, seleccionar, seguir y reevaluar a los proveedores externos, según el resumen de una consultora que no cita el texto de la norma.

## Los datos salen de la recepción contra lo pedido

Cada indicador se calcula con algo que registró otra parte del circuito. La fecha y la cantidad de cada entrega vienen de la [recepción contra lo pedido](../Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md); lo rechazado, de [diferencias y devoluciones](../Seguimiento-de-la-orden/diferencias-y-devoluciones.md); la fecha comprometida, de la [confirmación y el seguimiento](../Seguimiento-de-la-orden/confirmacion-y-seguimiento.md). Como inferencia de la base, sin recepción registrada contra la orden no hay dato que evaluar, y una empresa que recibe sin mirar la orden no puede medir a sus proveedores.

El tablero de evaluación de un sistema abierto usa cuatro criterios, como evidencia de práctica:

| Criterio | Cómo se calcula |
|---|---|
| Aceptación de calidad | Cantidad aceptada / cantidad recibida |
| Confiabilidad de entrega | Entregas a tiempo / entregas totales |
| Respuesta a cotizaciones | Respuestas en plazo / pedidos de cotización enviados |
| Consistencia comercial | Importe esperado frente al importe recibido |

El precio no figura entre esos criterios. Cuánto cuesta de verdad un proveedor, sumando rechazos, demoras y stock, lo trata [costo total de adquisición](../Abastecimiento-estrategico/costo-total-de-adquisicion.md).

> [!NOTE] Sin fuente todavía: el precio como indicador de desempeño (contra lista, contra mercado) y la calidad medida en partes por millón (PPM).

## A tiempo y completo depende de qué se cuente

El indicador más citado junta los dos primeros: entregas a tiempo y completas, OTIF por su sigla en inglés. El glosario de un operador logístico da el ejemplo: de 1.000 entregas, 950 llegaron a tiempo y completas, así que el OTIF es 95 %. El número cambia mucho según la unidad que se cuente. Un estudio presentado en una red de investigación en logística, según su resumen, midió a un proveedor y obtuvo 43 % contando por renglón, con una tolerancia de un día.

> [!IMPORTANT]
> Las fuentes no coinciden en qué fecha define «a tiempo». Puede ser la fecha que pidió el comprador o la que prometió el proveedor al confirmar, y el mismo estudio de logística marca la diferencia como fuente de error. Contra la fecha pedida, el indicador mide también si el comprador pidió con plazo suficiente; contra la prometida, mide solo si el proveedor cumplió su palabra (lectura de la base). Quien arme el tablero tiene que fijar cuál usa, la unidad (pedido, renglón o unidad) y la tolerancia, y decirlo junto al número.

## Del puntaje al estado del proveedor

El sistema abierto citado combina los criterios en un puntaje con pesos: «The weights should total 100». Los períodos recientes pesan más que los viejos, y el período puede ser semanal, mensual o anual. El puntaje ubica al proveedor en un estado, con estos rangos de ejemplo que cada empresa puede cambiar:

| Estado | Puntaje | Qué pasa |
|---|---|---|
| Preferido (Preferred) | 85 a 100 | Ni aviso ni bloqueo |
| Aprobado (Approved) | 70 a 84 | Ni aviso ni bloqueo |
| En observación (Watch) | 50 a 69 | Se puede configurar un aviso al comprador |
| Bloqueado (Blocked) | menos de 50 | Se pueden bloquear nuevos pedidos de cotización y órdenes |

Cada estado puede solo advertir, y el comprador sigue adelante, o bloquear. Qué es el bloqueo, qué impide y por qué no es lo mismo que inactivar está en [alta de proveedor](alta-de-proveedor.md#el-bloqueo-de-un-proveedor).

## Pocos indicadores, acordados con el proveedor

La guía de compras del gobierno de Nueva Gales del Sur pone un tope: como máximo 10 indicadores, y hasta 3 por métrica. Pide definirlos junto con el proveedor y con quienes lo usan adentro. También pide que el esfuerzo de revisión sea proporcional al que se puso en preparar el contrato, y que la frecuencia dependa del segmento del proveedor.

Ese segmento es el que fija [relación con proveedores](relacion-con-proveedores.md#segmentar-tres-niveles-según-gasto-y-criticidad): un proveedor único y crítico se revisa más seguido y con más detalle que uno de papelería. Como criterio de la base, la evaluación sirve también para elegir: cuando un artículo tiene varios proveedores en sus [condiciones](condiciones-del-proveedor.md), el puntaje es lo que el comprador mira además del precio.
