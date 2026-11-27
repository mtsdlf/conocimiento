---
resumen: >-
  Un cambio de ingeniería es la modificación controlada de la lista de materiales o la ruta de un producto: alguien la pide, se evalúa, se aprueba y entra en vigencia en una fecha o un número de serie, con una decisión sobre el stock y la producción en proceso que quedan con la versión anterior.
estado: borrador
estabilidad: semi
fuentes:
  - "ISO 10007:2017, vista previa (índice, prólogo e introducción): https://cdn.standards.iteh.ai/samples/70400/c1702ad12e3e4fe99ce2f15a60fe9ad7/ISO-10007-2017.pdf"
  - "ISO 10007:2017, página oficial (resumen del buscador): https://www.iso.org/standard/70400.html"
  - "Manual de órdenes de cambio de ingeniería de un sistema comercial (estados, vigencia, disposición): https://docs.oracle.com/cd/E18727_01/doc.121/e13687/T269960T269964.htm"
  - "Órdenes de cambio de ingeniería de un sistema abierto (v18.0), etapas, aprobadores y versiones: https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/plm/manage_changes/engineering_change_orders.html"
  - "Documentación de un sistema comercial, aprobación y activación de versiones de lista (página del 2025-07-10): https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom"
  - "Wikipedia, «Engineering change order» (baja confianza, la página avisa que le faltan citas): https://en.wikipedia.org/wiki/Engineering_change_order"
  - "Fecha de uso agotado en un sistema comercial (resumen del buscador): https://docs.oracle.com/en/cloud/saas/readiness/scm/24b/plm24b/24B-plm-wn-f32012.htm"
  - "Manual de Bill of Materials de un sistema abierto (actualizar el costo de la lista): https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials"
  - "Produccion/.investigacion/producto-y-proceso.md (2026-11-27), sección 3; costos.md, sección 1"
aliases: [cambio de ingeniería, engineering change, EC, orden de cambio de ingeniería, engineering change order, ECO, solicitud de cambio de ingeniería, engineering change request, ECR, aviso de cambio de ingeniería, engineering change notice, ECN, gestión de la configuración, configuration management, ISO 10007, revisión, revision, versión de la lista, BOM version, vigencia, effectivity, fecha de vigencia, effective date, vigencia por número de serie, serial effectivity, disposición, disposition, uso hasta agotar, use-up]
creado: 2026-11-27
revisado:
---

# Cambios de ingeniería

Un cambio de ingeniería es la modificación controlada de la lista de materiales o la ruta de un producto: alguien la pide, se evalúa, se aprueba y entra en vigencia en una fecha o un número de serie, con una decisión sobre el stock y la producción en proceso que quedan con la versión anterior.

Es la tercera pieza de [Producto y proceso](producto-y-proceso.md): la [lista de materiales](lista-de-materiales.md) y la [ruta de fabricación](ruta-de-fabricacion.md) dicen cómo es el producto hoy, y el cambio de ingeniería dice cómo y desde cuándo pasa a ser otro. Muchas veces nace en Calidad: una [no conformidad](../Calidad/no-conformidad.md) que se repite lleva a una [acción correctiva](../Calidad/accion-correctiva.md), y si la causa está en el diseño, la acción termina en un cambio de ingeniería.

## De dónde viene: la gestión de la configuración

El control de cambios viene de la gestión de la configuración, que ordena la ISO 10007:2017, una guía de la familia de calidad. En el texto de la vista previa, la norma la define como «a management activity that applies technical and administrative direction over the life cycle of a product and service, its configuration identification and status, and related product and service configuration information». Sirve para cumplir la identificación y trazabilidad de la ISO 9001:2015, cláusula 8.5.2.

El índice de la norma muestra los pasos del control de cambios (cláusula 5.4): iniciar, identificar y documentar la necesidad del cambio; evaluarlo; decidir sobre él («Disposition of change»); e implementarlo y verificarlo. La cláusula 4.2 se llama «Dispositioning authority», es decir, quién tiene autoridad para decidir. Según el buscador, la edición de 2017 fue revisada y confirmada en 2023.

> [!NOTE] Sin fuente todavía: el cuerpo de la ISO 10007 (de pago). Solo se leyeron el índice, el prólogo y la introducción; los requisitos de las cláusulas 4.2 y 5.4 no se citan.

## Solicitud y orden de cambio

En el uso corriente se habla de la solicitud de cambio (ECR), antes de que se decida, y de la orden de cambio (ECO), que lo autoriza. Wikipedia trata el aviso de cambio (ECN) como sinónimo de la orden. Wikipedia define la orden como un «document approved by the design activity that describes and authorizes the implementation of an engineering change», con este contenido mínimo: la pieza, los motivos, cómo era y cómo queda, los documentos y áreas afectados, la aprobación y las instrucciones de oportunidad: por ejemplo, tirar ya el stock actual o esperar a la próxima corrida.

Los sistemas leídos no tienen la solicitud como objeto aparte. Uno abierto maneja una sola orden que avanza por etapas; uno comercial, una orden con un estado y un estado de aprobación. Una orden agrupa artículos revisados «logically related to each other, such as a new product introduction».

> [!NOTE] Sin fuente todavía: la distinción entre solicitud y orden de cambio en una fuente primaria. La ISO 10007 no define ECR ni ECO, y Wikipedia no define la solicitud.

## Revisión, versión y una sola versión activa

Un cambio no edita la lista vigente: crea una versión nueva. En un sistema abierto, al empezar la revisión se copia la lista de producción con «The next available version number» (V2, V3). Mientras la orden está abierta, «the changes stay in the revised BoM and do not affect the production BoM». Al aplicar el cambio, la lista original se archiva y la revisada pasa a ser la de producción.

Tiene que haber una sola versión activa por período. Un sistema comercial lo controla al activar: «You receive an error message if the version that you're trying to activate conflicts with a version that is already active». El mismo sistema acota cada versión por período, cantidad, planta y otros criterios, y permite activar juntas todas las listas de un cambio «for one activation date».

La [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) guarda la versión de la lista y la ruta que usó. Por eso, cuando un lote falla, se puede saber con qué versión se fabricó y la [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md) puede separar lo fabricado antes y después del cambio.

## Vigencia: por fecha, por número de serie o al agotar

La vigencia dice desde cuándo vale el cambio. Hay tres formas en los sistemas leídos:

| Vigencia | Cómo funciona | Fuente |
|---|---|---|
| Por fecha | «lo antes posible» o una fecha fija | un sistema abierto; uno comercial pide «an effective date and model / unit number for each revised item» |
| Por número de serie o de modelo | el cambio entra a partir de cierta unidad; útil cuando cada unidad lleva [número de serie](../../Inventario-y-depositos/Existencias/lote-y-serie.md) | un sistema comercial |
| Al agotar | la fecha se calcula con el momento en que se acaba el stock proyectado del componente que sale | un sistema comercial, según el buscador |

Correr la fecha no cambia la orden: «Rescheduling does not change the ECO or revised item status, only the dates». El [MRP](../Planificacion-de-la-produccion/mrp.md) lee la vigencia para saber qué componente pedir en cada período: deja de pedir el viejo a partir de la fecha y empieza a pedir el nuevo (inferencia de la base).

## Qué pasa con el stock y la producción en proceso

Cuando un componente cambia, queda material de la versión vieja en el depósito y en las órdenes en curso, y se decide por artículo revisado y por lugar. Un sistema comercial ofrece estas opciones:

| Decisión | Qué se hace con el stock y la producción en proceso |
|---|---|
| Sin cambio | es lo que propone por defecto («No change required») |
| Desechar | se tira al implementar; en el depósito, en proceso o en los dos |
| Reprocesar | se adapta a la versión nueva; en el depósito, en proceso o en los dos |
| Usar hasta agotar | se sigue usando la versión vieja hasta que se acabe, en el depósito y en proceso o solo en proceso |
| Usar hasta un número de serie | se sigue usando hasta una unidad determinada |

Es una sola fuente de sistema. Lo que se decide acá es qué hacer; el movimiento físico (bloquear, mover a desecho, ajustar) se registra en Inventario, con sus [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md).

> [!NOTE] Sin fuente todavía: qué se hace con las órdenes de producción ya liberadas cuando entra un cambio (terminarlas con la versión vieja, volver a explotarlas o cancelarlas). Ninguna fuente primaria leída lo dice.

El costo estándar del producto no se actualiza solo con el cambio. En un sistema abierto, recalcular el costo de la lista es un acto aparte, con un botón de actualizar el costo; el recálculo está en [costo estándar del producto](../Costos-de-produccion/costo-estandar-del-producto.md).

## Quién aprueba y en qué estados pasa la orden

Ningún cambio llega a la planta sin aprobación. En un sistema abierto, las etapas de verificación son «stages that require approval before the revised changes can be applied to the production BoM», y el cambio no se aplica hasta que aceptan los aprobadores. En uno comercial, la aprobación tiene sus propios estados (sin enviar, pedida, aprobada, rechazada), y el sistema no deja implementar ni programar un cambio que no esté aprobado.

Los estados de la orden en el sistema comercial leído:

| Estado | Qué significa, según la fuente |
|---|---|
| Abierta | «The ECO is not complete; you can still make changes» |
| En espera | «The ECO cannot be implemented» |
| Liberada | la fuente la nombra sin definirla |
| Programada | la fuente la nombra sin definirla; solo se llega con la aprobación |
| Implementada | «You can no longer make changes to an implemented ECO» |
| Cancelada | «All unimplemented revised items are cancelled» |

Ninguna fuente leída exige una junta de control de cambios.

## Cómo falla el control de cambios

Inferencia de la base sobre el mecanismo descrito arriba:

- **Cambios sin vigencia.** Se corrige la lista vigente en lugar de crear una versión. Las órdenes abiertas, el MRP y el costo quedan con datos que nadie puede fechar, y no se sabe con qué versión se fabricó cada lote.
- **Listas en paralelo.** Ingeniería cambia su lista y la de fabricación no se actualiza, o la planta corrige la suya sin avisar. Cada área cree que la suya es la buena; está en [lista de ingeniería y lista de fabricación](lista-de-materiales.md#lista-de-ingeniería-y-lista-de-fabricación).
- **Sin decisión sobre el stock.** El cambio entra en vigencia y nadie decidió qué hacer con lo que ya había: queda material obsoleto en el depósito o se consume el viejo en un producto que ya debía llevar el nuevo.

## Qué guarda una orden de cambio

| Parte | Datos |
|---|---|
| Orden | identificador, motivo, origen (por ejemplo, una acción correctiva), estado, estado de aprobación, aprobadores y fechas |
| Artículo revisado | artículo o lista afectada, cómo era y cómo queda, versión nueva, vigencia (fecha, «lo antes posible», número de serie o de modelo), decisión sobre el stock y la producción en proceso |
| Resultado en el maestro | la versión nueva de la lista o la ruta con su vigencia, la anterior archivada, una sola activa por período, planta y cantidad |
