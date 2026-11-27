---
tema: Producción
para: entender qué registra y qué decide una empresa para transformar materiales en productos (de qué está hecho cada producto y cómo se fabrica, cuánto fabricar y cuándo, cómo se ordena y se sigue el trabajo en la planta, cuánto cuesta y cómo se controla que salga bien), para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: entiende de software y de negocio en general; no se da por sabido el vocabulario de la fabricación (lista de materiales, ruta, plan maestro, MRP, orden de producción, consumo automático, OEE, no conformidad, acción correctiva) ni cómo lo divide un sistema
escuela: neutral; la planificación y el control de la producción como los ordenan los cuerpos de certificación (ASCM, con CPIM) y los libros de texto de operaciones es la base; las críticas al MRP y las alternativas (justo a tiempo y kanban, teoría de las restricciones, DDMRP) aparecen donde discuten; la calidad se cuenta desde la ISO 9001 y el control estadístico
fuera:
  - el pronóstico, el plan de ventas y operaciones (S&OP) y el plan de distribución (DRP) — Cadena-de-suministro-y-logistica/Planificacion; acá empieza en el plan maestro, que baja el plan agregado a artículos
  - el stock en el depósito, sus estados (cuarentena, bloqueado), el lote y la serie en el depósito, la recepción con su inspección y la reposición por punto de pedido — Inventario-y-depositos; acá, la entrega de materiales a la orden y el ingreso del terminado como hechos de la orden, y la genealogía del lote fabricado
  - el proveedor, la orden de compra y el control de lo recibido contra lo pedido — Compras-y-abastecimiento; acá, el MRP que propone qué comprar y la subcontratación como paso de la fabricación
  - los sistemas de costeo (por órdenes o por procesos, absorción o variable, estándar, ABC), la valuación del inventario y el costo de lo vendido — Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md y Contabilidad/Operaciones/costo-de-lo-vendido.md; acá, de dónde salen los datos del costo (lista, ruta, consumos, horas) y el costo de cada orden
  - el registro del equipo, la estrategia de mantenimiento, la orden de trabajo, el MTBF y la disponibilidad — Activos-y-mantenimiento; acá, la OEE como medida de la línea y cuándo se puede parar una máquina
  - la calidad en la recepción (Inventario), la calidad de la atención (Servicio-al-cliente) y la evaluación de proveedores (Compras); acá, la calidad del producto fabricado
  - el reclamo del cliente y el caso — Servicio-al-cliente; acá, la no conformidad que abre un reclamo repetido
  - el legajo, la asistencia y la liquidación de los operarios — tema Administración de personal y nómina (todavía no armado)
  - el diseño del producto físico (ingeniería, PLM) más allá de la lista de materiales y los cambios de ingeniería — fuera del perímetro (decisión de #104)
  - el recorrido de la planificación a la producción (plan-to-produce) — tema Procesos de negocio (todavía no armado)
  - las categorías de producto (MRP, MES, gestión de la calidad) y las piezas comunes de todo software de gestión — tema Software de gestión (todavía no armado)
  - la seguridad e higiene en la planta, el ambiente y la automatización de máquinas (PLC, SCADA, niveles 0 a 2 de ISA-95); los productos de fabricación, comparativas y precios
fuentes: []
preguntas:
  - "Estoy diseñando el maestro de productos de una fábrica de muebles: ¿qué tiene que guardar la lista de materiales y la ruta, y qué cambia si fabrican contra pedido con medidas a elección?"
  - "¿Cómo pasa el plan de ventas y operaciones a órdenes concretas? ¿Qué hace el MRP paso a paso, qué necesita como entrada y por qué los planificadores dicen que es nervioso?"
  - "¿Qué estados tiene una orden de producción, qué se controla antes de liberarla y cómo se registran los consumos y lo producido sin cargar cada movimiento a mano?"
  - "¿Cómo se decide en qué orden pasan los trabajos por la máquina que es el cuello de botella, y qué cambia si la planta trabaja con kanban?"
  - "¿Qué es la OEE, cómo se calcula con un ejemplo, y por qué un 85 % no prueba que la planta sea de clase mundial?"
  - "Un cliente devuelve un lote defectuoso: ¿qué se registra como no conformidad, qué se hace con lo que queda en stock, cómo se encuentra qué otros lotes llevan el mismo componente y cómo se cierra la acción correctiva?"
  - "Tengo que diseñar el módulo de producción de un sistema para una fábrica de alimentos en la Argentina: ¿qué tengo que leer, qué pide la norma y cuánto de eso es del costo y la calidad?"
aprobado:
---

# Alcance: Producción

El tema cubre el dominio de negocio que llevan el módulo de fabricación de un ERP, un sistema de ejecución de planta (MES) y uno de gestión de la calidad: de qué está hecho cada producto y cómo se fabrica, cuánto fabricar y cuándo, cómo se ordena y se sigue el trabajo en la planta, cuánto cuesta lo fabricado y cómo se controla que salga bien. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), límites entre dominios (#98), procesos de punta a punta (#99), verticales de Software de gestión (#100), orden de armado (#101) y huecos del árbol (#104, que le dio la calidad como vertical). Es la sesión 9 de 16 (issue #116). El árbol general y los límites los aprobó la persona en el mapa; el árbol de adentro del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió, y queda para revisar en el PR.

Es un tema agnóstico: vale para cualquier producto sin nombrar proveedores, y se sostiene sin software (una ficha técnica por producto, un tablero con las órdenes de la semana y una planilla de controles hacen lo mismo que un sistema). Lo propio de la Argentina va en una nota aparte.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo (decisión de #98). Este tema es dueño de **lo que se transforma**: la definición del producto para fabricarlo (lista de materiales y ruta), el plan maestro y el MRP, la orden de producción, el costo de lo fabricado y la calidad del producto. Su verbo es **transformar**: planificar la fabricación, fabricar, costear lo fabricado y controlar que cumpla.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Cadena de suministro y logística](../Cadena-de-suministro-y-logistica/cadena-de-suministro-y-logistica.md) | el pronóstico, el plan agregado ([S&OP](../Cadena-de-suministro-y-logistica/Planificacion/plan-de-ventas-y-operaciones.md)) y el plan de distribución | El S&OP fija cuánto producir por familia y por mes; el plan maestro lo baja a artículos y semanas, y el MRP lo explota en componentes. Los dos últimos son de acá (decisión de #98) |
| [Inventario y depósitos](../Inventario-y-depositos/inventario-y-depositos.md) | la cantidad en cada lugar y estado; recibir, ubicar, reservar, contar; el [lote y la serie](../Inventario-y-depositos/Existencias/lote-y-serie.md) en el depósito; la reposición por punto de pedido | La entrega de material a la orden y el ingreso del terminado son movimientos de stock que se registran allá; acá, qué orden los pide y qué cantidad corresponde. La cuarentena es un estado de allá; la decisión de calidad que la levanta, de acá. Qué lotes de componente entraron en qué lote fabricado (la genealogía) es de acá |
| [Compras y abastecimiento](../Compras-y-abastecimiento/compras-y-abastecimiento.md) | el proveedor, la orden de compra y el control de lo recibido | El MRP propone qué comprar y para cuándo; la orden al proveedor sale de allá. La subcontratación de una operación es un paso de la fabricación de acá que termina en una orden de allá |
| [Contabilidad](../Contabilidad/contabilidad.md) | el método de costeo, la valuación del inventario y el costo de lo vendido | Acá, el costo estándar de cada producto (por la lista y la ruta), el costo real de cada orden y sus variaciones; allá, qué [sistema de costeo](../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md) se usa y cómo se registra en los libros |
| [Activos y mantenimiento](../Activos-y-mantenimiento/activos-y-mantenimiento.md) | el equipo como registro, el plan de mantenimiento, la orden de trabajo, el MTBF y la disponibilidad | Producción dice cuándo se puede parar una máquina; mantenimiento, qué hacerle. La OEE mide la línea y se explica acá; su primer factor, la disponibilidad, se mide allá |
| [Servicio al cliente](../Servicio-al-cliente/servicio-al-cliente.md) | el caso, el reclamo y su escalamiento | Un reclamo repetido sobre un producto es un dato para la calidad; la no conformidad y la acción correctiva se abren acá |
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | el pedido de venta y la [fecha prometida](../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md) | Un pedido de un producto que se fabrica contra pedido genera una orden de acá; la fecha que se promete usa la capacidad de acá |
| Administración de personal y nómina (no armado) | el legajo, la asistencia y la liquidación | Las horas cargadas a una orden son costo de la orden acá; para liquidar el sueldo, allá |
| Procesos de negocio (no armado) | el recorrido de la planificación a la producción (plan-to-produce) | Cada paso del recorrido tiene su detalle acá |
| Software de gestión (no armado) | las categorías (MRP, MES, gestión de la calidad) y las columnas técnicas (documento y estados, datos maestros, unidades) | Acá, el saber que existe sin software; allá, cómo lo empaqueta un producto |

Los temas que todavía no existen se nombran sin enlace; la sesión 16 del mapa los enlaza.

## Árbol

```
Produccion/
  produccion.md                        el todo: qué es transformar, las cinco partes, los vecinos; qué leer según lo que estés haciendo
  produccion-en-argentina.md           habilitaciones por rubro (alimentos, medicamentos, productos médicos, cosméticos), trazabilidad obligatoria, certificación de productos, registro industrial y promoción
  Producto-y-proceso/                  de qué está hecho cada producto y cómo se fabrica
    producto-y-proceso.md                (entrada) los datos maestros de fabricación y quién los mantiene
    lista-de-materiales.md               niveles, cantidad por unidad, merma, lista fantasma, de planificación, variantes; ingeniería frente a fabricación
    ruta-de-fabricacion.md               operaciones, centro de trabajo, preparación y ejecución, cola y movimiento; la fórmula en procesos
    cambios-de-ingenieria.md             solicitud y orden de cambio, revisión, vigencia y qué pasa con el stock y las órdenes abiertas
  Planificacion-de-la-produccion/      cuánto fabricar y cuándo, del plan agregado a la orden propuesta
    planificacion-de-la-produccion.md    (entrada) la jerarquía de planes desde el S&OP y quién planifica qué
    fabricar-para-stock-o-contra-pedido.md  para stock, ensamblar, fabricar o diseñar contra pedido; el punto de desacople
    plan-maestro-de-produccion.md        el MPS: horizonte, barreras de tiempo, consumo del pronóstico, disponible para prometer
    mrp.md                               neteo, explosión, desfase, lotificación, mensajes de acción, rastreo, nerviosismo
    planificacion-de-capacidad.md        capacidad gruesa y detallada, carga finita e infinita; el MRP II
  Ejecucion-en-planta/                 cómo se ordena y se sigue el trabajo en la planta
    ejecucion-en-planta.md               (entrada) de la orden propuesta al producto terminado; la frontera entre ERP y MES
    orden-de-produccion.md               el documento, sus estados, qué se controla al liberarla y al cerrarla
    consumo-y-declaracion.md             entregar material, consumo automático, declarar lo producido, merma, subproducto
    programacion-de-planta.md            secuenciar, reglas de despacho, cuello de botella, tambor-amortiguador-cuerda y kanban
    subcontratacion.md                   mandar material a un tercero para una operación: qué se registra
    eficiencia-global-del-equipo.md      la OEE: tres factores, seis grandes pérdidas, un ejemplo y cómo se engaña
  Costos-de-produccion/                cuánto cuesta lo fabricado
    costos-de-produccion.md              (entrada) qué datos de la planta alimentan el costo y dónde corta con Contabilidad
    costo-estandar-del-producto.md       la acumulación por la lista y la ruta, nivel por nivel
    costo-real-de-la-orden.md            lo que se carga a la orden, la producción en proceso, el cierre y las variaciones
  Calidad/                             que lo fabricado cumpla
    calidad.md                           (entrada) control, aseguramiento y gestión de la calidad; costo de la calidad; ISO 9001
    plan-de-inspeccion.md                qué se controla, dónde, cómo y cada cuánto; muestreo de aceptación
    control-estadistico-de-procesos.md   gráficos de control, causas comunes y especiales, capacidad del proceso
    no-conformidad.md                    registrar, segregar y decidir qué hacer con lo que no cumple
    accion-correctiva.md                 corrección frente a acción correctiva, causa raíz, 8D, verificar la eficacia
    trazabilidad-de-lotes.md             la genealogía del lote fabricado, hacia atrás y hacia adelante, y el retiro
  Fundamentos/
    fundamentos-de-produccion.md         (entrada) historia, escuelas (empujar, tirar, restricciones, DDMRP), posición contraria y fuentes
    marcos-de-la-produccion.md           el PCF de APQC (4.3), ISA-95, SCOR y CPIM: cómo cortan la producción y qué le piden a un sistema
    glosario-de-produccion.md            términos con su nombre en inglés
```

## Supuestos

- El árbol general y los límites con los vecinos vienen aprobados del mapa (#94, #98, #101, #104). El árbol del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió; la persona lo revisa en el PR.
- Cinco verticales: la definición del producto para fabricarlo (Producto y proceso), el plan (Planificación de la producción), el trabajo en la planta (Ejecución en planta), el costo (Costos de producción) y la calidad (Calidad). APQC 4.3 corta en programar, producir y probar; ISA-95 separa la planificación del negocio (nivel 4) de la gestión de operaciones de planta (nivel 3), que según resúmenes secundarios se divide en producción, mantenimiento, calidad e inventario; el temario de CPIM 2026 cierra, según un resumen del buscador, con un módulo de calidad y mejora continua. El corte de la base sigue esas divisiones y le deja a cada vecino lo suyo.
- La calidad es una vertical y no un tema (decisión de #104): la calidad del producto fabricado. La de la recepción es de Inventario, la del servicio de Servicio al cliente y la evaluación del proveedor de Compras.
- El centro de trabajo no tiene nota propia: vive en la ruta, que es donde se define y se usa; la capacidad del centro, en planificación de capacidad.
- La OEE va en Ejecución en planta porque mide la línea mientras produce; Activos y mantenimiento la nombra y enlaza acá (decisión de su alcance).
- Costos de producción tiene tres notas y no repite los sistemas de costeo de Contabilidad: explica de dónde salen los datos del costo en la planta y el costo de cada orden.
- La trazabilidad de lotes va en Calidad porque la genealogía sirve, sobre todo, para un retiro; el lote como atributo del stock sigue en Inventario.
- La nota de la Argentina es una sola, como en los otros temas del área. Lo fiscal de la fabricación (Ingresos Brutos industrial, IVA) es de Impuestos y se enlaza.
- La entrada del tema se llama `produccion.md`, igual que la de la vertical `IA/Produccion/`; las rutas no chocan y la convención de entrada (`<Tema>/<tema>.md`) pesa más que el nombre único.
