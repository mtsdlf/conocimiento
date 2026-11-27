---
tema: Activos y mantenimiento
para: entender cómo una empresa registra sus equipos, decide qué mantenimiento hacerles, organiza el trabajo con órdenes y lo lleva a la casa del cliente cuando el equipo es de él; la leen quien construye software de gestión y necesita entender el negocio que modela y, en segundo lugar, quien lo vende o lo implementa
nivel: entiende de software y de negocio en general; no se da por sabido el vocabulario de mantenimiento (preventivo, por condición, orden de trabajo, MTBF, criticidad, base instalada) ni cómo lo divide un sistema
escuela: neutral; el mantenimiento centrado en la confiabilidad (RCM), el mantenimiento productivo total (TPM) y la gestión de activos de la ISO 55000 se presentan como enfoques que conviven, cada uno con lo que sostiene
fuera:
  - el alta contable del activo, la amortización, capitalizar o gastar y la baja con su resultado — Contabilidad/Operaciones/activos-fijos-y-amortizacion.md; se enlaza
  - la compra del activo y de los repuestos (pedido, recepción, proveedor) — tema Compras y abastecimiento (Compras-y-abastecimiento/)
  - el stock de repuestos en el depósito (contar, ubicar, valuar) — tema Inventario y depósitos (Inventario-y-depositos/); acá, qué repuesto necesita una orden y cuál es crítico
  - la atención al cliente, el reclamo y el escalamiento — tema Servicio al cliente (Servicio-al-cliente/, que deriva desde Escalamiento/derivacion-al-tecnico.md); acá empieza cuando el caso deriva a un técnico
  - el presupuesto y la venta de un contrato de servicio — Relación con clientes; acá, qué cubre el contrato y qué promete
  - la programación de la planta, la calidad y la eficiencia de la línea (OEE como medida de producción) — tema Producción (Produccion/; la OEE en Produccion/Ejecucion-en-planta/eficiencia-global-del-equipo.md)
  - el legajo, las horas para liquidar y la capacitación de los técnicos — tema Administración de personal y nómina (Administracion-de-personal-y-nomina/); la capacitación, Liderazgo-y-direccion/Gestion-de-personas/desarrollo-de-personas.md
  - los proyectos de inversión para construir un activo (una planta, un edificio) — fuera de esta pasada y sin tema propio; Servicios-profesionales-y-proyectos/ trata el proyecto vendido a un cliente, no la obra propia, y el activo construido por la empresa se nombra en Procesos-de-negocio/de-la-compra-a-la-baja-del-activo.md
  - el transporte de mercadería y la flota de reparto como logística — tema Cadena de suministro y logística (Cadena-de-suministro-y-logistica/, el ruteo de camiones en Transporte/consolidacion-y-ruteo.md); acá solo el ruteo de técnicos
  - el recorrido de la compra a la baja del activo (acquire-to-retire) — Procesos-de-negocio/de-la-compra-a-la-baja-del-activo.md
  - las categorías de producto (EAM, CMMS, gestión de servicio de campo) y las piezas comunes de todo software de gestión — tema Software de gestión (Software-de-gestion/Categorias-de-producto/eam-y-cmms.md, servicio-de-campo-y-mesa-de-ayuda.md y Columnas-tecnicas/)
  - el análisis de datos de sensores y los modelos de predicción de fallas como técnica — Datos e IA; se enlazan
  - la gestión de activos de TI y de software, y la gestión de flota como negocio propio
  - productos de mantenimiento o servicio de campo, comparativas y precios — fuera de la base
fuentes: []
preguntas:
  - "Estoy diseñando el registro de equipos de una planta: ¿qué diferencia hay entre una ubicación y un equipo, cómo se arma la jerarquía y qué tiene que guardar el historial de cada uno?"
  - "¿Cuándo conviene mantenimiento preventivo por calendario, cuándo por uso, cuándo por condición y cuándo dejar que el equipo falle?"
  - "¿Qué estados tiene una orden de trabajo, qué diferencia hay entre el aviso y la orden, y qué se registra al cerrarla?"
  - "Una reparación cambia el motor de una máquina: ¿qué registra mantenimiento, qué registra Contabilidad y quién decide si se capitaliza?"
  - "Un cliente llama porque su equipo dejó de andar: ¿dónde termina la atención, qué datos necesita el técnico que va a la casa del cliente y qué decide si la visita se cobra?"
  - "¿Qué son el MTBF, el MTTR y la disponibilidad, cómo se calculan y cómo se engañan?"
aprobado:
---

# Alcance: Activos y mantenimiento

El tema cubre el dominio de negocio que lleva un sistema de mantenimiento (CMMS, EAM) y uno de servicio de campo: el registro de los equipos, la estrategia de mantenimiento, la orden de trabajo y su ciclo, el servicio técnico en casa del cliente y cómo se mide el desempeño de los activos. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), huecos (#104), límites entre dominios (#98), procesos de punta a punta (#99), verticales de Software de gestión (#100) y orden de armado (#101). Es la sesión 12 de 16 (issue #119). El árbol general y los límites los aprobó la persona en el mapa; el árbol de adentro del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió, y queda para revisar en el PR.

Es un tema agnóstico: vale para cualquier producto sin nombrar proveedores, y se sostiene sin software (una planilla de equipos, un tablero con tarjetas de trabajo y un cuaderno de historial hacen lo mismo que un sistema). Lo propio de la Argentina va en una nota aparte.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo (decisión de #98). Este tema es dueño del **activo físico como registro operativo** (qué es, dónde está, de qué está hecho, qué le pasó), del **plan de mantenimiento** y de **la orden de trabajo**, y del verbo **mantener**: conservar o devolver un equipo a la condición en que cumple su función, sea de la empresa o del cliente.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Contabilidad](../Contabilidad/contabilidad.md) | el activo fijo como valor: alta, amortización, capitalizar o gastar, baja | El mismo equipo tiene dos registros: el operativo (acá) y el contable (allá). La orden de trabajo junta el costo de una reparación; si alarga la vida útil y se capitaliza lo decide la regla de [activos fijos y amortización](../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md) |
| [Compras y abastecimiento](../Compras-y-abastecimiento/compras-y-abastecimiento.md) | comprar el activo y los repuestos | La orden pide un repuesto que no hay; la compra, allá |
| [Inventario y depósitos](../Inventario-y-depositos/inventario-y-depositos.md) | el stock de repuestos: contar, ubicar, valuar | Acá, qué repuestos lleva un equipo, cuál es crítico y la reserva contra la orden; allá, cuántos hay y dónde |
| [Servicio al cliente](../Servicio-al-cliente/servicio-al-cliente.md) | la atención, el reclamo y el escalamiento | El caso nace allá; cuando hace falta un técnico, [deriva](../Servicio-al-cliente/Escalamiento/derivacion-al-tecnico.md) una orden de servicio que es de acá. Revisar y autorizar un reclamo de garantía es del caso; qué promete el contrato, de acá. El cierre de la orden vuelve al caso |
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | el cliente como registro, el presupuesto y el pedido de venta | Un contrato de servicio se vende con un presupuesto y un pedido de allá; qué cubre y qué tiempo de respuesta promete, acá |
| [Producción](../Produccion/produccion.md) | transformar: programar la planta, calidad, eficiencia de la línea | Producción dice cuándo se puede parar la máquina; mantenimiento, qué hacerle. La OEE mide la línea y se explica en [eficiencia global del equipo](../Produccion/Ejecucion-en-planta/eficiencia-global-del-equipo.md) |
| [Administración de personal y nómina](../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) | el legajo, la asistencia y la liquidación del técnico | Las horas cargadas en una orden son costo del trabajo acá; para liquidar el sueldo, allá |
| [Cadena de suministro y logística](../Cadena-de-suministro-y-logistica/cadena-de-suministro-y-logistica.md) | mover mercadería entre lugares | Rutear técnicos a visitas es de acá; rutear camiones con carga, en [consolidación y ruteo](../Cadena-de-suministro-y-logistica/Transporte/consolidacion-y-ruteo.md) |
| [Procesos de negocio](../Procesos-de-negocio/procesos-de-negocio.md) | el recorrido de la compra a la baja del activo | La orden de mantenimiento es un paso de [de la compra a la baja del activo](../Procesos-de-negocio/de-la-compra-a-la-baja-del-activo.md); su detalle vive acá |
| [Software de gestión](../Software-de-gestion/software-de-gestion.md) | las categorías [EAM y CMMS](../Software-de-gestion/Categorias-de-producto/eam-y-cmms.md) y [gestión de servicio de campo](../Software-de-gestion/Categorias-de-producto/servicio-de-campo-y-mesa-de-ayuda.md), y las columnas técnicas ([documento y estados](../Software-de-gestion/Columnas-tecnicas/documento-y-estados.md), [datos maestros](../Software-de-gestion/Columnas-tecnicas/datos-maestros-y-partes.md)) | Acá, el saber que existe sin software; allá, cómo lo empaqueta un producto |

Cuando se escribió, los temas que todavía no existían se nombraban sin enlace; se enlazaron en la sesión 16 del mapa (#123).

## Árbol

```
Activos-y-mantenimiento/
  activos-y-mantenimiento.md         el todo: qué es mantener, las cinco partes, los vecinos; qué leer según lo que estés haciendo
  mantenimiento-obligatorio-en-argentina.md  inspecciones y servicios que exige la norma (seguridad e higiene, matafuegos, ascensores, electricidad)
  Registro-de-activos/               qué se mantiene: el equipo como registro
    registro-de-activos.md             (entrada) el activo físico frente al contable, el ciclo de vida, por qué un solo registro
    jerarquia-de-activos.md            ubicación técnica y equipo, niveles, componentes y lista de repuestos del equipo
    criticidad.md                      cuánto importa que falle cada equipo y cómo eso decide la estrategia
    historial-del-equipo.md            lo que le pasó: órdenes, fallas codificadas (modo, causa), lecturas y contadores
  Estrategia-de-mantenimiento/       qué mantenimiento hacerle a cada equipo
    estrategia-de-mantenimiento.md     (entrada) correctivo, preventivo, por condición, dejar fallar; cómo se elige
    mantenimiento-preventivo.md        el plan: tareas, frecuencia por calendario o por uso, rutas, cómo se generan las órdenes
    mantenimiento-por-condicion.md     predictivo, inspección, la curva P-F, cuándo vale la pena
    mantenimiento-centrado-en-confiabilidad.md  RCM: funciones, modos de falla, los patrones de falla y qué tarea corresponde
  Orden-de-trabajo/                  el trabajo de mantenimiento, del aviso al cierre
    orden-de-trabajo.md                (entrada) el documento, sus estados y su ciclo
    solicitud-de-trabajo.md            el aviso o pedido, la evaluación y la prioridad
    planificacion-y-programacion.md    planificar (qué, cómo, con qué) frente a programar (cuándo, quién); el pendiente
    repuestos-y-materiales.md          qué pide la orden, repuestos críticos, reserva y consumo
    cierre-de-la-orden.md              qué se registra al cerrar: trabajo hecho, falla, horas, materiales, costo
  Servicio-de-campo/                 el mantenimiento en casa del cliente
    servicio-de-campo.md               (entrada) qué cambia cuando el equipo es del cliente; el límite con Servicio al cliente
    base-instalada.md                  el equipo del cliente: número de serie, ubicación, garantía
    contrato-de-servicio.md            garantía y contrato, cobertura, tiempo de respuesta, qué se factura
    despacho-y-agenda.md               asignar la visita: habilidades, zona, ventana, ruteo
    visita-tecnica.md                  la orden en campo: repuestos del técnico, conformidad del cliente, resolver en la primera visita
  Desempeno-de-los-activos/          cómo se sabe si el mantenimiento anda y cuándo reemplazar
    desempeno-de-los-activos.md        (entrada) qué se mide y para qué decisión
    indicadores-de-mantenimiento.md    MTBF, MTTR, disponibilidad, cumplimiento del preventivo, pendiente, costo
    reparar-o-reemplazar.md            costo del ciclo de vida, vida económica, cuándo dar de baja
  Fundamentos/
    fundamentos-de-activos-y-mantenimiento.md  (entrada) historia, escuelas (RCM, TPM, ISO 55000), fuentes, mitos
    glosario-de-activos-y-mantenimiento.md     términos con su nombre en inglés
```

## Supuestos

- El árbol general y los límites vienen aprobados del mapa (#94, #98, #101, #104). El árbol del tema lo propone esta sesión sin esperar respuesta; la persona lo revisa en el PR.
- Cinco verticales. Las cuatro primeras siguen el corte del campo: qué se mantiene (el registro), qué se decide hacer (la estrategia), cómo se hace el trabajo (la orden) y cómo se mide (el desempeño); es la división de APQC 10.0 y del cuerpo de saber de SMRP, según la investigación de cada vertical. Servicio de campo es la quinta porque lo pidió el mapa (#104): es el mismo ciclo de orden de trabajo sobre un equipo que no es de la empresa.
- La orden de trabajo es una sola para el mantenimiento interno y el servicio de campo. Servicio de campo enlaza a [Orden de trabajo](Orden-de-trabajo/orden-de-trabajo.md) y explica solo lo que cambia (el cliente, el contrato, el viaje, la conformidad).
- La OEE nace en el TPM pero mide la línea: se nombra acá y se explica en Producción, en [eficiencia global del equipo](../Produccion/Ejecucion-en-planta/eficiencia-global-del-equipo.md).
- El mantenimiento predictivo con sensores y modelos se trata como estrategia (cuándo conviene); la técnica de análisis queda en Datos e IA.
- Lo de la Argentina va en una sola nota del tema, con las inspecciones y servicios que la norma vuelve obligatorios.
- **Investigación corta** (2026-11-27): el buscador web se agotó al empezar, y las normas (EN 13306, ISO 14224, ISO 55000, SAE JA1011), SMRP, Palmer y el informe de Nowlan y Heap no se pudieron leer. Lo que sale de ellos va atribuido a resúmenes secundarios, y cada nota declara sus huecos con un `[!NOTE]`. APQC 7.4 sí se leyó entero (`.investigacion/apqc-10.md`) y el servicio técnico en campo resultó estar en 6.3 «Service products after sales», no en 5.0. Conviene una pasada de `mantener` cuando haya acceso a esas fuentes.
- **Pasada de verificación** (2026-11-27, con el buscador de vuelta): se leyeron Nowlan y Heap (copia de la Wayback Machine del PDF de DTIC), la ficha oficial de SAE JA1011, las definiciones de ISO 55000 citadas por el IAM, las columnas de Palmer, la ayuda de SAP sobre estados de la orden, la guía de O&M del DOE y las normas de ascensores, matafuegos y aparatos a presión de la Ciudad y la Provincia de Buenos Aires. Siguen sin leer EN 13306, ISO 14224 (tablas), SMRP (solo para socios) e IRAM 3517-2. El detalle está en `.investigacion/verificacion-*.md`.
