---
resumen: >-
  Derivar al técnico es decidir, desde un caso, que el problema necesita que alguien vaya a ver el producto, y pasarle al servicio de campo lo que hace falta para la visita. El caso decide y deriva; la visita, su orden de trabajo, el técnico y los repuestos son del servicio de campo, y el caso queda abierto hasta que vuelve el resultado.
estado: borrador
estabilidad: semi
fuentes:
  - "ERPNext, Warranty Claim: https://docs.frappe.io/erpnext/user/manual/en/warranty-claim (como evidencia de práctica)"
  - "ERPNext, Maintenance Visit: https://docs.frappe.io/erpnext/user/manual/en/maintenance-visit (como evidencia de práctica)"
  - "Odoo 18.0, Helpdesk, servicios posventa: https://www.odoo.com/documentation/18.0/applications/services/helpdesk/advanced/after_sales.html (como evidencia de práctica)"
  - "Odoo 18.0, Field Service, creación de tareas: https://www.odoo.com/documentation/18.0/applications/services/field_service/creating_tasks.html (como evidencia de práctica)"
  - "APQC, Process Classification Framework, categoría «Manage Customer Service» (6.0), 6.3.4 «Service products», copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/6-manage-customer-service"
  - "Servicio-al-cliente/.investigacion/caso-y-escalamiento.md, componentes 4 y 7"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, sección 2"
aliases: [derivar al técnico, derivación al servicio técnico, visita técnica, field service dispatch, despacho de técnico, visita de mantenimiento, maintenance visit, orden de servicio, service order]
creado: 2026-11-27
revisado:
---

# Derivación al técnico

Derivar al técnico es decidir, desde un caso, que el problema necesita que alguien vaya a ver el producto, y pasarle al servicio de campo lo que hace falta para la visita. El caso decide y deriva; la visita, su orden de trabajo, el técnico y los repuestos son del servicio de campo, y el caso queda abierto hasta que vuelve el resultado.

Es la salida del [Escalamiento](escalamiento.md) hacia afuera del tema. El servicio de campo pertenece al tema Activos y mantenimiento, todavía no armado. El caso que más seguido termina en una visita es el del producto en garantía, que está en [garantía y reparación](../Caso/garantia-y-reparacion.md).

## Dónde lo ubica el campo

APQC pone la reparación dentro del servicio al cliente: en su categoría 6.0 (copia sin versión declarada), el nodo 6.3.4 «Service products» incluye «Execute product repair» y «Generate service order». La frontera que usa esta base es otra: el caso genera el pedido, y la orden de servicio y la reparación se ejecutan en Activos y mantenimiento. Es un corte de la base, para que el técnico, su agenda y los repuestos tengan un solo dueño.

## Cuándo el caso pide una visita

Las fuentes leídas no dan un criterio. En la práctica de un sistema abierto, el reclamo de garantía permite crear la visita «If a Customer visit is required to address the issue», y la decisión queda en quien atiende.

> [!NOTE] Sin fuente todavía: criterios para decidir que un caso necesita una visita (frente a resolver a distancia, pedir que el cliente envíe el producto o cambiarlo), y quién toma esa decisión.

Como lectura de esta base, la decisión compite con las otras salidas del caso sobre un producto: la devolución, cuya logística está en [devoluciones](../../Comercio-electronico/Operaciones-del-comercio/devoluciones.md); el cambio; la reparación en taller; o la visita. Las mesas de ayuda leídas ofrecen esas salidas juntas: desde el mismo caso, un sistema abierto dispara un reembolso, una devolución, una orden de reparación o una tarea de servicio de campo.

## Qué pasa del caso a la orden de trabajo

Ninguna fuente primaria dice qué datos debe llevar una derivación. Lo que se puede reconstruir de dos sistemas abiertos:

- La visita de mantenimiento de uno de ellos registra fecha y hora, cliente, tipo (programada, no programada o por rotura), estado de finalización (parcial o completa), artículo y número de serie, descripción, trabajo hecho y, de forma opcional, la opinión del cliente. Del registro del cliente toma la dirección, el contacto, el territorio y el grupo.
- El reclamo de garantía del mismo sistema se abre con el cliente y el número de serie, y de la serie trae el artículo y los datos de la garantía.
- En otro sistema, desde el caso se agenda una tarea de servicio de campo, y el cliente que tiene acceso al portal sigue su avance.

De ahí sale, como inferencia de esta base y no como norma, lo mínimo que pasa del caso a la visita:

1. El cliente, por referencia al [registro del cliente](../../Relacion-con-clientes/Registro-del-cliente/registro-del-cliente.md), con la dirección y el contacto de la visita.
2. El producto, con su número de serie, y si está en garantía.
3. La descripción del problema y lo que ya se probó a distancia.
4. El número del caso, para que el resultado vuelva a él.

Ninguna de las páginas leídas describe cómo se guarda el vínculo entre el caso y la visita, ni qué se copia de uno a otra.

## El caso sigue abierto mientras dura la visita

En esta base, el caso no se cierra al derivar: el cliente sigue esperando la solución y el reloj del [acuerdo de nivel de servicio](../Niveles-de-servicio/niveles-de-servicio.md) sigue siendo del caso. Cómo se pausa o no ese reloj mientras se espera al técnico está en [tiempos de respuesta y resolución](../Niveles-de-servicio/tiempos-de-respuesta-y-resolucion.md). Cuando la visita termina, su resultado vuelve al caso y el caso pasa a resuelto. Un sistema abierto cierra el reclamo de garantía con el estado «The repairs have been done», lo que sugiere, como lectura de esta base, el mismo circuito.

## Dónde falla la derivación

Como lectura de esta base, sin fuente que lo documente:

- **El caso se cierra al derivar.** La mesa de ayuda da el caso por resuelto y la visita queda en otro sistema; si la visita no resuelve, el cliente vuelve y entra como caso nuevo.
- **La visita no trae lo que se sabía.** El técnico llega sin la descripción ni lo que ya se probó, y el cliente lo explica otra vez.
- **Nadie mira las visitas que se repiten.** El mismo producto pide visitas una y otra vez, y eso es un problema de fondo que va a [problema y causa raíz](problema-y-causa-raiz.md) y, si es un defecto de fabricación, a la calidad del tema Producción, todavía no armado.

> [!NOTE] Sin fuente todavía: evidencia (norma, libro o estudio) sobre los datos que debe llevar una derivación al servicio de campo y sobre cómo falla el pase entre la mesa de ayuda y el técnico.
