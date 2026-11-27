---
tema: Servicio al cliente
para: entender cómo atiende una empresa a sus clientes después de la venta (por dónde entra el contacto, cómo se registra el caso, cuándo y a quién se escala, qué tiempos se prometen y cómo se mide si la atención es buena), con qué datos, estados y reglas; la leen quien construye software de gestión y necesita entender el negocio que modela y, en segundo lugar, quien lo vende o lo implementa
nivel: entiende de software y de negocio en general; no se da por sabido el vocabulario de la atención (caso, primer nivel, acuerdo de nivel de servicio, resolución al primer contacto) ni cómo lo divide un sistema
escuela: neutral; se cuenta la operación como la describen las normas de tratamiento de quejas y de centros de contacto y la práctica de gestión de servicios de TI, y la crítica desde el esfuerzo del cliente y desde «la mejor atención es no necesitarla» se cita donde discute
fuera:
  - el servicio de campo (el técnico en casa del cliente, la orden de trabajo, los repuestos, el mantenimiento del equipo) — tema Activos y mantenimiento (sesión 12 del mapa, todavía no armado); acá solo se deriva al técnico
  - el registro del cliente, la oportunidad, el presupuesto y el pedido de venta — Relacion-con-clientes; se enlaza
  - la calidad del servicio como marketing (expectativas, brechas, SERVQUAL, recuperación del servicio y sus tres justicias, lealtad, NPS como predictor de crecimiento) — Marketing/Servicio-y-relacion y Marketing/Canales/boca-a-boca-y-referidos; se enlaza
  - la logística de la devolución en una tienda online y su costo — Comercio-electronico/Operaciones-del-comercio/devoluciones.md; se enlaza
  - la mercadería devuelta que vuelve al stock — tema Inventario y depósitos (todavía no armado)
  - la nota de crédito, el reintegro y su impuesto — temas Contabilidad, Impuestos y Tesorería (en armado)
  - la entrega del servicio que se vende (proyectos, horas, hitos) — tema Servicios profesionales y proyectos (todavía no armado)
  - la calidad del producto fabricado y los lotes retenidos — vertical de calidad del tema Producción (todavía no armado)
  - el análisis de clientes (retención, churn, valor de vida) — Datos y Marketing; se enlaza
  - las piezas comunes a todo software de gestión (documento y estados, permisos, auditoría) — tema Software de gestión (sesión 14, todavía no armado)
  - el recorrido de punta a punta del reclamo a la resolución — tema Procesos de negocio (sesión 13, todavía no armado)
  - productos de mesa de ayuda o de centro de contacto, comparativas y precios — fuera de la base
fuentes: []
preguntas:
  - "Un cliente escribe por correo, vuelve a reclamar por chat y después llama: ¿cómo se registra para que sea un solo caso y no tres?"
  - "¿Qué diferencia hay entre una consulta, un pedido de servicio, un incidente y un reclamo, y cambia en algo cómo se trata cada uno?"
  - "¿Qué lleva un acuerdo de nivel de servicio y cómo se cuenta el tiempo de resolución si el cliente tarda en contestar o el caso entra un viernes a la noche?"
  - "El primer nivel no puede resolver un caso de un producto en garantía que hay que revisar: ¿a quién se escala, cuándo se manda un técnico y qué se le pasa?"
  - "¿Qué métricas dicen si la atención es buena, y cuáles se pueden mejorar en el tablero empeorando la atención?"
  - "Tengo que diseñar el módulo de mesa de ayuda de un sistema para una empresa argentina: ¿qué tengo que leer y qué le exige la ley a la atención?"
aprobado:
---

# Alcance: Servicio al cliente

El tema cubre el dominio de negocio que lleva una mesa de ayuda o la parte de atención de un CRM: el contacto del cliente después de la venta, el caso que lo registra, el escalamiento, los niveles de servicio prometidos y la calidad de la atención. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), huecos (#104, que le sacó el servicio de campo y le cambió el nombre), límites entre dominios (#98), procesos de punta a punta (#99), verticales de Software de gestión (#100) y orden de armado (#101). Es la sesión 7 de 16 (issue #114). El árbol general y los límites los aprobó la persona en el mapa; el árbol de este tema lo propone esta sesión y queda para que lo revise en el PR.

Es un tema agnóstico: lo que dice vale para cualquier producto, sin nombrar proveedores, y se sostiene sin software (un cuaderno de reclamos en el mostrador y una persona que llama al proveedor hacen lo mismo que una mesa de ayuda). Lo propio de la Argentina va en una nota aparte.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo (decisión de #98). Este tema es dueño del **caso** (la consulta, el pedido o el reclamo de un cliente después de la venta) y del **acuerdo de nivel de servicio**, y del verbo **resolver**: que el cliente obtenga respuesta, dentro del tiempo prometido, y que la empresa aprenda de lo que se repite.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | el registro del cliente, la oportunidad, el presupuesto y el pedido de venta | El caso apunta al cliente y, si viene de una compra, al pedido; no los copia. Un caso que termina en una venta nueva abre una oportunidad allá |
| [Marketing/Servicio-y-relacion](../Marketing/Servicio-y-relacion/servicio-y-relacion.md) | por qué el cliente juzga la atención como la juzga, la recuperación del servicio y si conviene invertir en la lealtad | Allá, qué siente el cliente y qué conviene prometer; acá, cómo se registra, se escala, se cronometra y se mide la atención |
| Activos y mantenimiento (no armado) | el servicio de campo: la orden de trabajo, el técnico, los repuestos y el historial del equipo | El caso decide que hace falta una visita y deriva; la visita y su orden de trabajo son de allá, y el caso queda abierto hasta que vuelve el resultado |
| [Comercio-electronico/devoluciones](../Comercio-electronico/Operaciones-del-comercio/devoluciones.md) | la logística de la devolución en una tienda online | El caso autoriza la devolución o el cambio; el paquete que vuelve, allá |
| Inventario y depósitos (no armado) | la mercadería devuelta que entra al depósito | El caso dice qué vuelve y por qué; dónde queda y si vuelve a la venta, allá |
| Contabilidad, Impuestos y Tesorería (en armado) | la nota de crédito, el reintegro y su impuesto | El caso decide compensar; el comprobante y la plata, allá |
| Producción (no armado) | la calidad del producto fabricado | Un reclamo repetido sobre un producto es un dato para su calidad; la no conformidad se abre allá |
| Procesos de negocio (no armado) | el recorrido del reclamo a la resolución, que cruza este tema, Relación con clientes, Inventario y Contabilidad | Allá, el recorrido entero; acá, cada paso que es del caso |

Los temas que todavía no existen se nombran sin enlace; la sesión 16 del mapa los enlaza.

## Árbol

```
Servicio-al-cliente/
  servicio-al-cliente.md                 el todo: qué es atender después de la venta, el caso como centro y cómo se conectan las verticales
  servicio-al-cliente-en-argentina.md    trato digno, garantía legal y servicio técnico, botón de baja, plazos de respuesta, vías de reclamo externo
  Canales-de-atencion/                   por dónde entra el contacto y quién lo atiende
    canales-de-atencion.md                 (entrada) asistidos y de autoservicio, sincrónicos y asincrónicos, un solo caso aunque cambie el canal
    autoservicio.md                        base de conocimiento, preguntas frecuentes, portal y bots; KCS; el desvío y cómo se mide mal
    dimensionamiento-del-equipo.md         cuántas personas hacen falta: volumen, tiempo de atención, nivel de servicio, colas
  Caso/                                  el registro de lo que pidió el cliente
    caso.md                                (entrada) datos, estados, dueño, cierre y reapertura
    clasificacion-y-prioridad.md           tipo de caso, categoría, impacto y urgencia, triage
    reclamo.md                             la queja: recepción, acuse, investigación, respuesta y cierre
    garantia-y-reparacion.md               el caso sobre el producto: garantía, devolución autorizada, cambio, reparación
  Escalamiento/                          cuando quien atiende no puede resolver
    escalamiento.md                        (entrada) escalar por conocimiento o por autoridad, y cuándo
    niveles-de-soporte.md                  primer, segundo y tercer nivel; el enjambre como alternativa
    derivacion-al-tecnico.md               cuándo el caso pide una visita y qué se pasa al servicio de campo
    problema-y-causa-raiz.md               de los casos repetidos al problema y al error conocido
  Niveles-de-servicio/                   lo que se promete en tiempo
    niveles-de-servicio.md                 (entrada) el acuerdo de nivel de servicio: qué se promete, a quién y cómo se mide
    tiempos-de-respuesta-y-resolucion.md   primera respuesta, resolución y el reloj: horario hábil, feriados, pausas
    incumplimiento-del-acuerdo.md          alertas, vencimiento, créditos y penalidades; el tablero verde con el cliente enojado
    acuerdos-internos.md                   los acuerdos entre equipos y con terceros que sostienen el que se le da al cliente
  Calidad-del-servicio/                  si la atención es buena y cómo mejora
    calidad-del-servicio.md                (entrada) medir la operación, preguntar al cliente y escuchar las conversaciones
    metricas-de-atencion.md                resolución al primer contacto, tiempo de atención, reaperturas, pendientes, abandono
    encuestas-de-satisfaccion.md           satisfacción, esfuerzo y recomendación después de un caso; tasa de respuesta y sesgos
    monitoreo-de-calidad.md                evaluar conversaciones, calibrar evaluadores y analizar los reclamos para mejorar
  Fundamentos/
    fundamentos-de-servicio-al-cliente.md  (entrada) escuelas, cómo divide el campo la atención, fuentes
    historia-del-servicio-al-cliente.md    del mostrador al centro de contacto y la mesa de ayuda
    glosario-de-servicio-al-cliente.md     términos con su nombre en inglés y las palabras con dos sentidos
    mitos-del-servicio-al-cliente.md       las cifras sin fuente y lo que sí dice la evidencia
```

## Supuestos

- El árbol general y los límites con los vecinos vienen aprobados del mapa (#94, #98, #101, #104). El árbol del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió; la persona lo revisa en el PR.
- Cinco verticales siguen lo que pasa con un contacto: entra por un canal, se registra como caso, se escala si hace falta, se cronometra contra un acuerdo y se mide. El orden no es el de ninguna fuente: APQC 6.0 divide en estrategia, contactos, servicio posventa, retiros y evaluación; las normas de centros de contacto, en requisitos de la organización, del personal y de la interacción; ITIL, en prácticas (mesa de servicio, incidentes, problemas, niveles de servicio). El corte es de la base, para que cada vertical sea un objeto o una regla que un sistema modela.
- La vertical se llama Canales de atención y no Atención, para no chocar con la nota `atencion.md` de Psicología (los nombres de archivo son únicos en la base).
- Garantía y reparación va en Caso y no en una vertical propia: desde este tema es un tipo de caso con un paso de logística o de taller, que es de otros temas.
- Problema y causa raíz va en Escalamiento y no en Calidad: nace cuando el primer nivel ve que un caso se repite y lo pasa a quien puede arreglar la causa.
- Los retiros de producto del mercado (APQC 6.4) no tienen nota: se mencionan en la entrada como un caso masivo y quedan como hueco.
- «Nivel de servicio» tiene dos sentidos en el campo (el acuerdo con el cliente y el porcentaje de contactos atendidos dentro de un tiempo en un centro de contacto). El tema usa «acuerdo de nivel de servicio» para el primero y «nivel de servicio del centro de contacto» para el segundo, y el glosario lo aclara.
- Lo de la Argentina va en una sola nota del tema, porque toca varias verticales y es corto.
