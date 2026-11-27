---
tema: Compras y abastecimiento
para: entender qué registra y qué hace una empresa para conseguir lo que necesita de afuera (a quién comprarle y en qué condiciones, cómo se pide, cómo se aprueba, cómo se le ordena al proveedor y cómo se controla que llegó lo pedido), para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: entiende de software y de negocio en general; no se da por sabido el vocabulario de compras (solicitud de compra, orden de compra, contrato marco, homologación, matriz de Kraljic, tolerancia de recepción) ni cómo lo divide un sistema
escuela: neutral; la línea de compras como función estratégica (Kraljic, el ciclo de compras y abastecimiento de CIPS, los libros de texto de van Weele y de Monczka) es la base, y la crítica a esa línea (los límites de la matriz de Kraljic, el ahorro de precio contra el costo total) aparece donde discute con ella
fuera:
  - contar, inspeccionar y ubicar lo que llega, y la política de cuándo y cuánto reponer por punto de pedido — Inventario-y-depositos (Operacion-del-deposito/recepcion.md y Reposicion/); acá, si llegó lo pedido
  - el pronóstico de demanda, el plan agregado (S&OP), la reposición planificada de quien no fabrica (DRP), el transporte y el comercio exterior — tema Cadena de suministro y logística (sesión 8, se arma en paralelo, todavía no está en la base)
  - el MRP, que calcula qué materiales pedir a partir del plan de producción, y la subcontratación como paso de la fabricación — tema Producción (sesión 9, todavía no armado); acá, la orden al proveedor que resulta
  - el cruce de tres vías como control, la matriz de autorizaciones y la separación de funciones — Contabilidad/Control-interno; acá, dónde se aplican en el circuito de compras
  - la cuenta a pagar, su asiento y lo recibido sin facturar — Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md
  - el pago al proveedor y la decisión de cuándo pagar — tema Tesorería (sesión 3, todavía no armado)
  - el crédito fiscal y las retenciones a proveedores — tema Impuestos (sesión 2, todavía no armado); acá, solo qué datos del proveedor hacen falta
  - la compra de un activo fijo y su vida útil — tema Activos y mantenimiento (sesión 12, todavía no armado) y Contabilidad/Operaciones/activos-fijos-y-amortizacion.md; acá, la orden de compra que lo trae
  - la negociación como método general — Ventas/Objeciones-y-negociacion; acá, lo propio del lado del comprador
  - el poder de negociación de los proveedores como fuerza de la industria — Estrategia-competitiva/Analisis-de-industria/cinco-fuerzas.md
  - el registro de oro entre sistemas — Datos/Gobierno-y-calidad/datos-maestros.md; acá, qué tiene adentro el registro del proveedor
  - las piezas de diseño comunes a todo software de gestión (datos maestros, documento y estados, permisos, auditoría) — tema Software de gestión (sesión 14, todavía no armado)
  - el recorrido de punta a punta de la compra al pago — tema Procesos de negocio (sesión 13, todavía no armado)
  - las compras del Estado (contrataciones públicas, licitación pública como régimen legal), los productos de compras electrónicas (e-procurement), sus comparativas y precios
fuentes: []
preguntas:
  - "Un área necesita 50 sillas: ¿qué pasa desde que alguien lo pide hasta que hay una orden de compra emitida, y quién aprueba qué?"
  - "¿Cómo se elige y se da de alta a un proveedor nuevo, y qué se controla antes de comprarle por primera vez?"
  - "Pedimos 100 y llegaron 90, dos de ellas rotas: ¿qué se registra, la orden queda abierta o se cierra, y qué parte es de Compras, de Inventario y de Contabilidad?"
  - "¿Cuándo conviene pedir cotización a varios proveedores, cuándo firmar un contrato marco y cuándo comprar directo?"
  - "¿Cómo se mide si un proveedor cumple y qué se hace con uno que no cumple?"
  - "Tengo que diseñar el módulo de compras de un sistema para una empresa argentina: ¿qué tengo que leer y qué pide el país para registrar a un proveedor y recibir su factura?"
aprobado:
---

# Alcance: Compras y abastecimiento

El tema cubre el dominio de negocio que lleva el módulo de compras de un ERP y un sistema de compras: el proveedor como registro, la decisión de a quién comprarle y en qué condiciones, la solicitud interna, la orden de compra y su seguimiento hasta que lo recibido coincide con lo pedido. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), huecos (#104), límites entre dominios (#98), procesos de punta a punta (#99), verticales de Software de gestión (#100) y orden de armado (#101). Es la sesión 5 de 16 (issue #112). El árbol general y los límites los aprobó la persona en el mapa; el árbol de este tema es propuesta de esta sesión y queda para que lo revise en el PR.

Es un tema agnóstico: lo que dice vale para cualquier producto, sin nombrar proveedores de software, y se sostiene sin software (una carpeta de proveedores, un talonario de órdenes de compra y un remito firmado hacen lo mismo que un sistema). Lo propio de la Argentina va en una nota aparte.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo (decisión de #98). Este tema es dueño del **proveedor como registro**, de **la solicitud de compra**, de **la orden de compra** y del **acuerdo con el proveedor** (cotización, contrato marco), y de los verbos **elegir, negociar, pedir, ordenar y controlar que llegó lo pedido**. Termina cuando lo recibido coincide con lo pedido.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Inventario y depósitos](../Inventario-y-depositos/inventario-y-depositos.md) | la cantidad de cada artículo, dónde está y en qué estado; recibir, ubicar, contar; cuándo y cuánto reponer por política | En la recepción, Inventario cuenta, inspecciona y ubica ([recepción](../Inventario-y-depositos/Operacion-del-deposito/recepcion.md)); Compras compara ese conteo con la orden y decide qué hacer con la diferencia. El [punto de pedido](../Inventario-y-depositos/Reposicion/punto-de-pedido.md) dice cuándo y cuánto; a quién se le pide y en qué condiciones, de acá |
| Cadena de suministro y logística (en armado en paralelo) | el pronóstico, el plan agregado, la reposición planificada, el transporte y el comercio exterior | Cadena dice qué hace falta y cuándo, en un plan; Compras convierte esa necesidad en una orden a un proveedor y negocia con él. La importación (aduana, despachante, flete internacional) es de Cadena; la orden al proveedor del exterior, de acá |
| Producción (no armado) | lo que transforma: lista de materiales, MRP, orden de producción | El MRP propone qué materiales comprar; la orden al proveedor sale de acá |
| [Contabilidad](../Contabilidad/contabilidad.md) | la cuenta a pagar, el asiento y los controles | El cruce de tres vías, la matriz de autorizaciones y la separación de funciones están en [Control interno](../Contabilidad/Control-interno/control-interno.md); acá se dice en qué paso del circuito se aplican. La deuda con el proveedor nace en [compras y cuentas a pagar](../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md) |
| Tesorería (no armado) | el pago y cuándo pagar | La condición de pago se negocia y se registra acá; el pago se ejecuta allá |
| Impuestos (no armado) | el crédito fiscal y las retenciones | Acá, la condición fiscal del proveedor como dato; allá, qué se hace con ella |
| Activos y mantenimiento (no armado) | la vida del activo | La orden que compra una máquina es de acá; su alta, su mantenimiento y su baja, de allá |
| [Ventas](../Ventas/ventas.md) | el método de vender, con la negociación vista del lado del vendedor | La negociación general está en [objeciones y negociación](../Ventas/Objeciones-y-negociacion/objeciones-y-negociacion.md); acá, lo que cambia cuando se negocia como comprador |
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | el pedido de venta | Es el espejo: la orden de compra de una empresa es el pedido de venta de su proveedor. Los objetos se parecen, pero cada empresa registra los suyos |
| [Datos/Gobierno-y-calidad](../Datos/Gobierno-y-calidad/datos-maestros.md) | el registro de oro entre sistemas | Allá, cómo se logra un solo registro; acá, qué tiene adentro el registro del proveedor |
| Software de gestión (no armado) | las columnas técnicas | Acá qué tiene que registrar el negocio; allá cómo lo resuelve cualquier sistema |

Los temas que todavía no existen se nombran sin enlace; la sesión 16 del mapa los enlaza.

## Árbol

```
Compras-y-abastecimiento/
  compras-y-abastecimiento.md      el todo: qué registra el dominio, sus cuatro partes y los vecinos; qué leer según lo que estés haciendo
  compras-y-abastecimiento-en-argentina.md  verificar al proveedor (constancia, facturas apócrifas), la factura que se recibe según su condición, la factura de crédito electrónica
  Proveedores/                     a quién se le compra y en qué condiciones
    proveedores.md                   (entrada) el proveedor como registro y por qué uno solo
    alta-de-proveedor.md             datos maestros, verificación y homologación antes de la primera compra
    condiciones-del-proveedor.md     lista de precios, plazo de entrega, mínimos y condición de pago; el registro artículo-proveedor
    evaluacion-de-proveedores.md     entregas a tiempo y completas, calidad, precio; la revisión periódica
    relacion-con-proveedores.md      segmentar, desarrollar y depender: proveedor único y riesgo de proveedor
  Abastecimiento-estrategico/      cómo se decide a quién comprarle y en qué términos
    abastecimiento-estrategico.md    (entrada) del gasto al acuerdo: el ciclo de compras y abastecimiento
    analisis-del-gasto.md            en qué y con quién se gasta; las categorías de compra
    matriz-de-kraljic.md             posicionar cada categoría por impacto y riesgo, y qué hacer en cada cuadrante
    hacer-o-comprar.md               producir adentro o comprar afuera
    cotizacion-y-licitacion.md       pedido de información, de cotización y de propuesta; comparar ofertas
    negociacion-de-compras.md        negociar como comprador
    costo-total-de-adquisicion.md    lo que cuesta una compra más allá del precio
    contrato-marco.md                precio y condiciones acordados por un período; órdenes contra el contrato
  Orden-de-compra/                 el pedido interno y el compromiso con el proveedor
    orden-de-compra.md               (entrada) el documento, sus estados y lo que dispara
    solicitud-de-compra.md           quién pide, quién aprueba, y las compras que saltean el circuito
    tipos-de-orden.md                puntual, abierta, contra contrato, de servicios, en consignación
    cambios-y-cancelaciones-de-la-orden.md  modificar, cancelar y volver a aprobar una orden emitida
  Seguimiento-de-la-orden/         de la orden emitida a lo recibido que coincide con lo pedido
    seguimiento-de-la-orden.md       (entrada) los estados después de emitir y dónde termina Compras
    confirmacion-y-seguimiento.md    el acuse del proveedor, la fecha confirmada y el seguimiento de entregas
    recepcion-contra-lo-pedido.md    tolerancias, entregas parciales, saldo pendiente y cierre de la orden
    diferencias-y-devoluciones.md    faltantes, sobrantes y rechazos; la devolución y el reclamo al proveedor
  Fundamentos/
    fundamentos-de-compras-y-abastecimiento.md  (entrada) historia, escuelas, posición contraria y fuentes
    glosario-de-compras-y-abastecimiento.md     términos con su nombre en inglés
```

## Supuestos

- El árbol general y los límites con los vecinos vienen aprobados del mapa (#94, #98, #101). El árbol del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió; la persona lo revisa en el PR.
- Cuatro verticales: a quién se le compra (Proveedores), cómo se decide a quién y en qué términos (Abastecimiento estratégico), el pedido y el compromiso (Orden de compra) y lo que pasa hasta que llega lo pedido (Seguimiento de la orden). Sigue la división clásica entre la parte estratégica de la función (sourcing) y la transaccional (procure-to-pay) que hacen CIPS y los libros de texto, con el proveedor aparte porque es el dato maestro que usan las dos.
- Abastecimiento estratégico va como vertical aunque buena parte se haga sin software: la base mide los temas por el saber, no por el módulo (#95).
- El contrato marco vive en Abastecimiento estratégico, porque es un acuerdo; la orden abierta y la orden contra contrato, que son su uso, en Orden de compra.
- La recepción contra lo pedido es de acá y la recepción física es de Inventario: el corte lo fijó #98 y el tema de Inventario ya lo usa.
- Lo de la Argentina va en una sola nota del tema, porque toca el alta del proveedor y la recepción de su factura, y es corto.
