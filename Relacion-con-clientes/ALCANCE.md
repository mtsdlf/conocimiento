---
tema: Relación con clientes
para: entender qué registra una empresa sobre sus clientes y sus ventas en curso (el cliente, el interesado, la oportunidad, el presupuesto y el pedido de venta), con qué datos, qué estados y qué reglas; la leen quien construye software de gestión y necesita entender el negocio que modela y, en segundo lugar, quien lo vende o lo implementa
nivel: entiende de software y de negocio en general; no se da por sabido el vocabulario comercial (cuenta, oportunidad, pedido abierto, fecha prometida) ni cómo lo divide un sistema
escuela: neutral; el CRM se cuenta como registro del negocio, y la visión del CRM como estrategia (Payne y Frow) se cita donde discute con esa lectura
fuera:
  - el método de vender (prospección, calificación, embudo comercial como método, la propuesta persuasiva, negociación) — tema Ventas; se enlaza
  - el marketing de relaciones, la lealtad y la calidad de servicio — Marketing/Servicio-y-relacion; se enlaza
  - el caso posterior a la venta (consulta, reclamo, escalamiento) — tema Servicio al cliente (sesión 7 del mapa, todavía no armado)
  - la reserva y la preparación de la mercadería — tema Inventario y depósitos (todavía no armado)
  - el despacho y el transporte — tema Cadena de suministro y logística (todavía no armado); el envío de una tienda, en Comercio-electronico
  - la factura y el comprobante — temas Contabilidad e Impuestos (en armado); la factura electrónica de ARCA, en Comercio-electronico/Normativa
  - la decisión de dar crédito y la cobranza — tema Tesorería (todavía no armado); la cuenta corriente entre empresas, en Comercio-electronico/Comercio-B2B
  - el análisis de clientes (valor de vida, RFM, retención, churn) — Datos y Marketing; se enlaza
  - el registro de oro y la gestión de datos maestros en general — Datos/Gobierno-y-calidad/datos-maestros; se enlaza
  - las piezas de diseño comunes a todo software de gestión (documento y estados, datos maestros, permisos) — tema Software de gestión (sesión 14, todavía no armado)
  - el recorrido de punta a punta del pedido al cobro — tema Procesos de negocio (sesión 13, todavía no armado)
  - productos de CRM o ERP, comparativas y precios — fuera de la base
fuentes: []
preguntas:
  - "Un mismo cliente compra en una sucursal, paga desde la casa matriz y recibe en un depósito: ¿cómo se registra sin duplicarlo?"
  - "¿Qué diferencia hay entre un interesado, un contacto, un cliente y una oportunidad, y cuándo pasa uno a ser el otro?"
  - "¿Qué datos lleva una oportunidad y qué dice del embudo de ventas, sin redefinirlo?"
  - "¿Qué estados tiene un presupuesto, cuánto vale y qué pasa si cambia el precio antes de que lo acepten?"
  - "Un cliente acepta un presupuesto: ¿qué se convierte en pedido, qué fecha se le promete y quién se entera?"
  - "Tengo que diseñar el módulo de pedidos de un sistema para una empresa argentina: ¿qué tengo que leer y qué datos del cliente me pide el país?"
aprobado:
---

# Alcance: Relación con clientes

El tema cubre el dominio de negocio que lleva un CRM y la parte de ventas de un ERP: el registro del cliente, del interesado, de la oportunidad, del presupuesto y del pedido de venta. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), huecos (#104), límites entre dominios (#98), procesos de punta a punta (#99), verticales de Software de gestión (#100) y orden de armado (#101). Es la sesión 6 de 16 (issue #113). El árbol general y los límites los aprobó la persona en el mapa; el árbol de este tema es propuesta de esta sesión y queda para que lo revise en el PR.

Es un tema agnóstico: lo que dice vale para cualquier producto, sin nombrar proveedores, y se sostiene sin software (una libreta de clientes, un presupuesto en papel y una nota de pedido hacen lo mismo que un sistema). Lo propio de la Argentina va en una nota aparte.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo (decisión de #98). Este tema es dueño del **cliente como registro**, de **la oportunidad**, del **presupuesto** y del **pedido de venta**, y del verbo **comprometer**: qué se le vende a quién, a qué precio y para cuándo.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Ventas](../Ventas/ventas.md) | el método de vender: prospectar, calificar, proponer, negociar; define el embudo comercial | Ventas dice qué etapas tiene el embudo y cómo se pasa de una a otra; este tema, qué se registra en cada oportunidad. La propuesta persuasiva es de Ventas; el presupuesto como documento con renglones, precios y validez, de acá |
| [Marketing/Servicio-y-relacion](../Marketing/Servicio-y-relacion/servicio-y-relacion.md) | la calidad del servicio, las expectativas y si conviene invertir en la lealtad | Marketing decide cuánto invertir en retener; este tema registra al cliente y su historia |
| Servicio al cliente (no armado) | el caso posterior a la venta | Un reclamo abre un caso allá; el historial del cliente lo muestra desde acá |
| Inventario y depósitos (no armado) | la reserva y la preparación | El pedido confirmado pide la reserva; la cantidad disponible la calcula Inventario, la fecha que se le promete al cliente es de acá |
| Cadena de suministro y logística (no armado) | el despacho y el transporte | El pedido dice a dónde y para cuándo; cómo llega, allá |
| Contabilidad e Impuestos (en armado) | la factura, la cuenta del cliente en el mayor y el impuesto | El pedido dice qué facturar; el comprobante y su impuesto, allá |
| Tesorería (no armado) | la decisión de dar crédito y la cobranza | El límite de crédito es un dato del cliente; quién lo fija y cómo se cobra, allá |
| [Comercio-electronico/Comercio-B2B](../Comercio-electronico/Comercio-B2B/comercio-b2b.md) | la aplicación a la venta mayorista: pedido B2B, precio por cliente, cuenta corriente | Allá, cómo se ve en un mayorista y en la Argentina; acá, el concepto general que lo sostiene |
| [Datos/Gobierno-y-calidad](../Datos/Gobierno-y-calidad/datos-maestros.md) | el registro de oro entre sistemas | Allá, cómo se logra un solo registro entre sistemas; acá, qué tiene adentro el registro del cliente |

Los temas que todavía no existen se nombran sin enlace; la sesión 16 del mapa los enlaza.

## Árbol

```
Relacion-con-clientes/
  relacion-con-clientes.md         el todo: qué registra el dominio, sus cuatro objetos y cómo se conectan con los vecinos
  relacion-con-clientes-en-argentina.md  datos fiscales del cliente, presupuesto y oferta en la ley, leyendas, datos personales
  Registro-del-cliente/            quién es el cliente y en qué condiciones se le vende
    registro-del-cliente.md          (entrada) cuenta, contacto y por qué un solo registro
    cuenta-y-contacto.md             la parte con roles, jerarquías, comprador/pagador/destinatario, duplicados
    condiciones-comerciales.md       lista de precios, condición de pago, límite de crédito, vendedor, moneda
    cartera-de-clientes.md           asignar cuentas y territorios, clasificar, quién es dueño de la cuenta
  Seguimiento-comercial/           las ventas posibles antes del pedido
    seguimiento-comercial.md         (entrada) del interesado a la oportunidad, y la historia que queda
    interesado.md                    el lead: origen, conversión, por qué se separa del cliente
    oportunidad.md                   el registro de una venta posible: monto, etapa, probabilidad, motivo de pérdida
    actividad.md                     llamadas, visitas, correos y tareas; por qué no se cargan
  Presupuesto/                     la oferta formal con precio
    presupuesto.md                   (entrada) el documento, sus estados y su diferencia con la propuesta
    precio-y-descuentos.md           de dónde sale el precio de cada renglón y quién aprueba el descuento
    productos-configurables.md       configurar, poner precio y presupuestar lo que tiene opciones
    vigencia-y-aceptacion.md         cuánto vale, cómo se revisa y cómo se acepta (firma, orden de compra, seña); el paso a pedido
  Pedido-de-venta/                 el compromiso de entregar
    pedido-de-venta.md               (entrada) el documento, sus estados y lo que dispara aguas abajo
    fecha-prometida.md               disponibilidad, available-to-promise y quién promete qué
    tipos-de-pedido.md               contado, a plazo, abierto o marco, recurrente
    cambios-y-cancelaciones.md       modificar, entregar en partes, pendientes, cancelar, bloquear
  Fundamentos/
    fundamentos-de-relacion-con-clientes.md  (entrada) escuelas, fuentes
    historia-del-crm.md              del fichero al CRM
    glosario-de-relacion-con-clientes.md     términos con su nombre en inglés
    mitos-del-crm.md                 las cifras de fracaso y lo que sí dice la evidencia
```

## Supuestos

- El árbol general y los límites con los vecinos vienen aprobados del mapa (#94, #98, #101). El árbol del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió; la persona lo revisa en el PR.
- Cuatro verticales siguen los cuatro objetos del dominio en el orden en que aparecen: cliente, oportunidad, presupuesto, pedido. Las fuentes no dividen así el tema (APQC no tiene categoría de relación con clientes; los analistas parten el CRM en ventas, atención y marketing; un ERP abierto separa CRM de Selling): el corte es de la base, como dijo la investigación de taxonomías (#96).
- La actividad (el historial de interacciones) va en Seguimiento comercial y no en Registro del cliente: nace en la venta en curso, aunque se muestra en la ficha del cliente.
- Vigencia, versiones y aceptación del presupuesto van en una sola nota: las fuentes casi no tratan las versiones, y separadas quedaban dos notas flacas.
- Lo de la Argentina va en una sola nota del tema, porque toca las cuatro verticales y es corto.
- El análisis de la cartera (valor de vida, RFM) no entra: se enlaza a Datos y Marketing.
