---
tema: Cadena de suministro y logística
para: entender qué registra y qué decide una empresa sobre lo que pasa entre lugares (cuánto se va a vender, cómo se acuerda un plan entre áreas, cuánto mandar a cada depósito, dónde tener depósitos, cómo se mueve la carga, cómo se despacha y se entrega, cómo se cruza una frontera), para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: entiende de software y de negocio en general; no se da por sabido el vocabulario de la planificación y la logística (pronóstico, S&OP, DRP, carga completa, cross-docking, prueba de entrega, Incoterms, despacho aduanero) ni cómo lo divide un sistema
escuela: neutral; la gestión de la cadena como la ordenan los cuerpos de certificación (ASCM, con SCOR, CSCP y CLTD) y los libros de texto de operaciones es la base; el pronóstico se cuenta desde la estadística (Hyndman y Athanasopoulos); la crítica de la planificación por pronóstico (DDMRP, «el pronóstico siempre está mal») y la discusión entre eficiencia y resiliencia aparecen donde discuten
fuera:
  - lo que pasa adentro del depósito (recibir, ubicar, reservar, preparar el pedido, contar) y la reposición artículo por artículo con punto de pedido, lote económico, stock de seguridad y ABC — Inventario-y-depositos; acá se enlaza
  - el proveedor, la orden de compra y el control de lo recibido contra lo pedido — Compras-y-abastecimiento; acá, el viaje de lo comprado y el plan que dice cuánto comprar
  - el plan maestro de producción, el MRP, la lista de materiales y la programación de planta — Produccion; acá, el plan agregado que lo alimenta
  - lo fiscal del comercio exterior en la Argentina (derechos, tasas, IVA y percepciones en la importación, reintegros) — Impuestos/comercio-exterior-en-argentina.md; acá, cómo se mueve y se documenta la mercadería
  - el pedido de venta y la fecha prometida al cliente — Relacion-con-clientes; acá, cuánto tarda el transporte
  - el envío de una tienda online (transportistas, agregadores, costo del envío, fulfillment, devoluciones) — Comercio-electronico/Operaciones-del-comercio/Envios-y-logistica; se enlaza como el caso del comercio
  - el remito y el código de operación de traslado en la Argentina — Inventario-y-depositos/inventario-y-depositos-en-argentina.md; se enlaza
  - la valuación del stock en tránsito y el costo del flete en el costo — Contabilidad; la diferencia de cambio, Contabilidad/Operaciones/moneda-extranjera.md
  - la carta de crédito y el pago al exterior — Tesoreria (el pago de una importación en la Argentina, en Tesoreria/tesoreria-en-argentina.md; la carta de crédito no tiene nota)
  - el presupuesto anual de la empresa — Contabilidad/Contabilidad-de-gestion/presupuesto.md; el S&OP lo enlaza
  - las piezas de diseño comunes a todo software de gestión (documento y estados, datos maestros, unidades y monedas) — Software-de-gestion/Columnas-tecnicas
  - el recorrido de punta a punta de la planificación a la producción y del pedido al cobro — Procesos-de-negocio (de-la-planificacion-a-la-produccion.md y del-pedido-al-cobro.md)
  - productos de planificación, de gestión de transporte (TMS) o de comercio exterior, comparativas y precios; la conducción de flotas, el mantenimiento de vehículos y la seguridad vial
fuentes: []
preguntas:
  - "Tengo que pronosticar cuánto voy a vender de cada artículo el mes que viene: ¿qué métodos hay, cómo sé si el pronóstico es bueno y qué hago con los artículos que se venden poco y de a ratos?"
  - "¿Qué es el S&OP, quién se sienta en la reunión, qué se decide ahí y en qué se diferencia del presupuesto y del plan de producción?"
  - "Una distribuidora tiene un depósito central y cinco sucursales: ¿cómo decide cuánto mandar a cada una y cuándo, y qué cambia si en vez de punto de pedido usa DRP?"
  - "¿Conviene un depósito grande o varios chicos, y qué stock se ahorra al centralizar?"
  - "Sale un camión con pedidos de varios clientes: ¿qué documento lo registra, qué estados recorre hasta la entrega, y cómo se mide si se entregó bien?"
  - "Importo mercadería por barco desde Asia: ¿qué Incoterm conviene, qué documentos viajan, quién hace el trámite en la aduana y qué parte es de este tema y qué parte de Impuestos?"
  - "Tengo que diseñar el módulo de logística de un sistema para una empresa argentina que despacha a todo el país e importa: ¿qué tengo que leer?"
aprobado:
---

# Alcance: Cadena de suministro y logística

El tema cubre el dominio de negocio que llevan el módulo de planificación de un ERP, un sistema de gestión de transporte (TMS) y uno de comercio exterior: cuánto se va a vender, cómo se acuerda un plan entre ventas, compras, operaciones y finanzas, cuánto mandar a cada lugar, dónde poner los depósitos, cómo se mueve la carga, cómo se despacha y se entrega, y qué cambia cuando la mercadería cruza una frontera. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), huecos (#104), límites entre dominios (#98), procesos de punta a punta (#99), verticales de Software de gestión (#100) y orden de armado (#101). Es la sesión 8 de 16 (issue #115). El árbol general y los límites los aprobó la persona en el mapa; el árbol de este tema es propuesta de esta sesión y queda para que lo revise en el PR.

Es un tema agnóstico: lo que dice vale para cualquier producto, sin nombrar proveedores, y se sostiene sin software (una planilla con las ventas de cada mes, una reunión mensual entre áreas y una hoja de ruta por camión hacen lo mismo que un sistema). Lo propio de la Argentina va en una nota aparte.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo (decisión de #98). Este tema es dueño de **lo que pasa entre lugares y del plan agregado**: el pronóstico, el plan de ventas y operaciones, el plan de distribución, la red, el despacho y el viaje. Sus verbos son **pronosticar, planificar, distribuir, despachar, transportar, entregar, importar y exportar**.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Inventario y depósitos](../Inventario-y-depositos/inventario-y-depositos.md) | la cantidad de cada artículo en cada lugar y estado; recibir, ubicar, reservar, preparar, contar; la reposición por punto de pedido | Preparar el pedido es de allá; desde que el bulto embalado sale por la puerta, de acá. La reposición artículo por artículo con [punto de pedido](../Inventario-y-depositos/Reposicion/punto-de-pedido.md) es de allá; la planificada por períodos para varios depósitos (DRP), de acá. Una transferencia entre depósitos sale y entra allá; el viaje es de acá |
| [Compras y abastecimiento](../Compras-y-abastecimiento/compras-y-abastecimiento.md) | el proveedor, la orden de compra, la negociación y el control de lo recibido contra lo pedido | El plan de acá dice cuánto hace falta y cuándo; a quién se le compra y a qué precio, Compras. El flete de lo comprado y el trámite de importación son de acá |
| [Producción](../Produccion/produccion.md) | el plan maestro, el MRP, la lista de materiales y la programación de planta | El plan agregado de acá, que sale del S&OP, fija cuánto producir por familia y por mes; el plan maestro y el MRP lo bajan a artículos y órdenes allá |
| [Impuestos](../Impuestos/impuestos.md) | lo fiscal: derechos, tasas, IVA y percepciones de la importación, reintegros de la exportación | Acá, qué documentos viajan, quién hace el trámite y cuánto tarda; allá, cuánto se paga y cómo se liquida |
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | el pedido de venta y la [fecha prometida](../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md) | El pedido dice a dónde y para cuándo; cuánto tarda el viaje y cómo llega, acá |
| [Contabilidad](../Contabilidad/contabilidad.md) | la valuación, el costo y el registro; el presupuesto | El S&OP usa el [presupuesto](../Contabilidad/Contabilidad-de-gestion/presupuesto.md) y lo revisa mes a mes; el costo del flete se registra allá |
| [Envíos y logística, en Comercio electrónico](../Comercio-electronico/Operaciones-del-comercio/Envios-y-logistica/envios-y-logistica.md) | la aplicación a una tienda online: transportista, agregador, etiqueta, costo del envío, fulfillment | Allá, cómo se ve en una tienda; acá, el concepto general (modos, consolidación, despacho, prueba de entrega) |
| [Software de gestión](../Software-de-gestion/Columnas-tecnicas/columnas-tecnicas.md) | las columnas técnicas: documento y estados, unidades, monedas | Acá qué tiene que registrar el negocio; allá cómo lo resuelve cualquier sistema |

Cuando se escribió, Compras, Producción, Impuestos, Tesorería, Software de gestión y Procesos de negocio no existían y se nombraban sin enlace; la sesión 16 del mapa (#123) los enlazó.

## Árbol

```
Cadena-de-suministro-y-logistica/
  cadena-de-suministro-y-logistica.md   el todo: qué es la cadena, sus cinco partes, los vecinos; qué leer según lo que estés haciendo
  cadena-de-suministro-y-logistica-en-argentina.md  transporte de cargas, despachante, aduana y sus trámites; lo fiscal va a Impuestos
  Planificacion/                       cuánto se va a vender y cuánto hace falta, por período
    planificacion.md                     (entrada) la jerarquía de planes, el horizonte y quién planifica qué
    pronostico-de-demanda.md             métodos (juicio, series de tiempo, causales), la demanda intermitente y la jerarquía
    error-de-pronostico.md               cómo se mide (sesgo, MAE, MAPE, MASE) y para qué sirve medirlo
    plan-de-ventas-y-operaciones.md      el S&OP: el ciclo mensual, quién decide, qué sale; frente al presupuesto y al plan maestro
    planificacion-de-la-distribucion.md  DRP: cuánto mandar a cada depósito y cuándo, para quien no fabrica
    efecto-latigo.md                     la amplificación de la demanda aguas arriba, sus causas y remedios (compartir datos, VMI, CPFR)
  Red-de-distribucion/                 dónde están los lugares y cómo fluye la mercadería entre ellos
    red-de-distribucion.md               (entrada) los eslabones, los flujos posibles y el costo logístico total
    diseno-de-la-red.md                  cuántos depósitos y dónde; costo de transporte contra costo de stock y plazo
    centralizacion-del-stock.md          agrupar el riesgo: qué stock se ahorra al centralizar y la ley de la raíz cuadrada
    tercerizacion-logistica.md           operador logístico (3PL, 4PL): qué se terceriza y qué se pierde
  Transporte/                          cómo se mueve la carga
    transporte.md                        (entrada) quién mueve, en qué y cuánto cuesta; las decisiones del cargador
    modos-de-transporte.md               camión, tren, barco, avión, multimodal; carga completa y consolidada
    costo-del-flete.md                   de qué se arma: peso, volumen, distancia, servicio; el peso facturable y la liquidación
    consolidacion-y-ruteo.md             juntar carga y armar recorridos: el problema de ruteo de vehículos y sus límites
  Despacho-y-entrega/                  de la puerta de salida a las manos del destinatario, y de vuelta
    despacho-y-entrega.md                (entrada) el flujo despachar, viajar, entregar, y dónde corta con Inventario
    despacho.md                          el documento del despacho: qué junta, qué estados recorre, el seguimiento
    prueba-de-entrega.md                 la conformidad del destinatario, la entrega fallida y la diferencia en destino
    nivel-de-servicio-logistico.md       a tiempo y completo (OTIF), pedido perfecto: cómo se mide la entrega
    logistica-inversa.md                 devoluciones, retornables y lo que vuelve por la cadena
  Comercio-exterior/                   lo que cambia cuando la mercadería cruza una frontera
    comercio-exterior.md                 (entrada) los actores, el flujo de una importación y una exportación, los plazos
    incoterms.md                         las once reglas: quién paga, quién asegura y dónde pasa el riesgo
    documentos-del-comercio-exterior.md  factura comercial, lista de empaque, conocimiento de embarque, certificado de origen
    aduana.md                            destinación, clasificación arancelaria, regímenes y canales de control
  Fundamentos/
    fundamentos-de-cadena-de-suministro.md  (entrada) historia, escuelas, posición contraria y fuentes
    marcos-de-la-cadena-de-suministro.md    el PCF de APQC y SCOR: qué versión se leyó, cómo se reparten sus procesos y qué le piden a un sistema
    glosario-de-cadena-de-suministro.md     términos con su nombre en inglés
```

## Supuestos

- El árbol general y los límites con los vecinos vienen aprobados del mapa (#94, #98, #101). El árbol del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió; la persona lo revisa en el PR.
- Cinco verticales: el plan (Planificación), los lugares (Red de distribución), el movimiento (Transporte), la salida y la entrega (Despacho y entrega) y la frontera (Comercio exterior). SCOR divide la cadena en procesos (planificar, pedir, abastecer, transformar, cumplir, devolver) y CLTD en módulos que juntan depósito, inventario y transporte; el corte es de la base, que le deja a Inventario lo de adentro del depósito, a Compras el abastecimiento y a Producción la transformación.
- El vistazo del paso 1 de la skill lo cubre la investigación de taxonomías (#96): los programas CSCP y CLTD 2026 y SCOR DS. No se repitió.
- El efecto látigo va en Planificación porque nace de cómo se pasa la demanda de un eslabón al siguiente, y sus remedios son de planificación; la red lo enlaza.
- La tercerización logística va en Red de distribución y no en Transporte, porque un operador logístico puede guardar, preparar y mover: es una decisión sobre quién opera la red.
- La logística inversa va en Despacho y entrega porque recorre el mismo camino al revés; el reingreso al stock es de Inventario y la devolución en una tienda, de Comercio electrónico.
- Las métricas de la cadena no tienen vertical: el error de pronóstico va en Planificación, el costo logístico total en Red de distribución y el nivel de servicio de la entrega en Despacho y entrega.
- Lo de la Argentina va en una sola nota del tema, como en Inventario y depósitos.
