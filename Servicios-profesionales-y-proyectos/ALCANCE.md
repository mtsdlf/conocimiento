---
tema: Servicios profesionales y proyectos
para: entender qué registra y cómo se gestiona una firma que vende trabajo de personas por proyecto (el proyecto con el cliente y su presupuesto, la asignación de personas, las horas, la facturación por hora, por hito o por abono, el costo y el margen), en cualquier rubro; lo lee quien construye software de gestión y necesita entender el negocio que modela y, en segundo lugar, quien lo vende o lo implementa o dirige una firma chica de servicios
nivel: entiende de software y de negocio en general, y sabe qué es un proyecto; no se da por sabido el vocabulario de las firmas de servicios (utilización, realización, trabajo en curso, bolsa de horas, reserva tentativa) ni cómo se factura un proyecto
escuela: neutral; la economía de la firma se lee con Maister (palancas y apalancamiento), y el precio por valor y la crítica a la hora facturable aparecen como posición contraria donde discuten con esa lectura
fuera:
  - el método de llevar un proyecto (encuadre, enfoque, plan, pronóstico, valor ganado, control de cambios, riesgo, portafolio como método) — tema Gestión de proyectos; se enlaza
  - el encargo de software con un cliente (acuerdo inicial, estimación de software, plan de entregas, traspaso) y la elección del modelo de contrato con su reparto del riesgo — Desarrollo/Encargo; se enlaza
  - el riesgo del precio cerrado (contingencia, cómo se pierde plata) — Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado; se enlaza
  - la economía de la firma como modelo de negocio (la ecuación de Maister, la pirámide, las cifras de utilización de referencia), la capacidad con teoría de colas, el abono de cuidado y el servicio productizado — Emprender/Modelo-de-negocio; se enlaza
  - el presupuesto y el pedido de venta como documentos — tema Relación con clientes; se enlaza
  - el asiento, el ingreso según la NIIF 15, el costeo por órdenes y el proyecto como dimensión contable — tema Contabilidad; se enlaza
  - la asistencia, la liquidación de sueldos y el legajo — tema Administración de personal y nómina (Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md)
  - el cobro y la decisión de dar crédito — tema Tesorería (Tesoreria/Credito-y-cobranzas/credito-y-cobranzas.md)
  - la factura electrónica, las alícuotas y las retenciones como obligación recurrente — tema Impuestos (Impuestos/impuestos.md)
  - el recorrido de punta a punta del proyecto al cobro (project-to-cash) — tema Procesos de negocio (Procesos-de-negocio/del-proyecto-al-cobro.md)
  - el PSA como categoría de software — tema Software de gestión (Software-de-gestion/Categorias-de-producto/psa.md)
  - la posventa (consultas, reclamos) — tema Servicio al cliente (Servicio-al-cliente/servicio-al-cliente.md); la visita técnica y la orden de trabajo sobre un equipo — tema Activos y mantenimiento (Activos-y-mantenimiento/Servicio-de-campo/servicio-de-campo.md)
  - seleccionar, evaluar y hacer crecer a las personas — Liderazgo-y-direccion/Gestion-de-personas; se enlaza
  - productos de PSA o ERP, comparativas y precios — fuera de la base
fuentes: []
preguntas:
  - "Una consultora firma un proyecto a precio cerrado de 400 horas con tres hitos: ¿qué se registra al firmarlo, cómo se arma el presupuesto del proyecto y cuándo se factura cada hito?"
  - "Dos proyectos piden a la misma persona el mismo mes: ¿quién decide, cómo se registra una asignación tentativa frente a una firme y cómo se ve con meses de anticipación si va a faltar gente?"
  - "Diseño la carga de horas de un sistema: ¿qué datos lleva cada hora, quién la aprueba, qué pasa si se corrige después de facturada y en qué se diferencia de la asistencia que usa la nómina?"
  - "Un estudio cobra por hora con un tope de 100 horas y lleva 80 trabajadas sin facturar: ¿qué se factura, qué es el trabajo en curso y cuándo se reconoce el ingreso?"
  - "¿Cómo sé si un proyecto y la firma ganan plata, y por qué una utilización alta puede convivir con un margen bajo?"
  - "Facturo servicios en Argentina: ¿qué datos lleva la factura de un servicio, puedo ajustar la tarifa por inflación y qué retenciones me van a hacer?"
aprobado:
---

# Alcance: Servicios profesionales y proyectos

El tema cubre el dominio de negocio de una firma que vende trabajo de personas por proyecto: una consultora, un estudio contable o jurídico, una agencia, un estudio de arquitectura o de ingeniería, una software factory. Es lo que APQC llama 5.0 «Deliver Services» y lo que los productos llaman PSA (*professional services automation*). Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), huecos (#104, que lo hizo tema propio), límites entre dominios (#98), procesos de punta a punta (#99), verticales de Software de gestión (#100) y orden de armado (#101). Es la sesión 11 de 16 (issue #118). El árbol general y los límites los aprobó la persona en el mapa; el árbol de adentro del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió, y queda para revisar en el PR.

Es un tema agnóstico: lo que dice vale en cualquier producto, sin nombrar proveedores, y se sostiene sin software (una carpeta por proyecto, una planilla de horas y un talonario de facturas hacen lo mismo). Lo propio de la Argentina va en una nota aparte.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo (decisión de #98). Este tema es dueño del **proyecto como contrato con un cliente**, de **la asignación de personas a proyectos**, de **la hora imputada** y de **las reglas con que el trabajo se vuelve factura**, y del verbo **entregar y facturar el servicio vendido**.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Gestión de proyectos](../Gestion-de-proyectos/gestion-de-proyectos.md) | el método de llevar cualquier proyecto: encuadre, enfoque, plan, pronóstico, avance, riesgo, gobierno | Allá, cómo se planifica y se mide el avance; acá, qué de eso se registra con plata y con un cliente del otro lado. El valor ganado se explica allá; acá se usa el avance como base para facturar y reconocer el ingreso |
| [Desarrollo/Encargo](../Desarrollo/Encargo/encargo.md) | el ciclo con el cliente en un desarrollo de software a medida, y la elección del modelo de contrato con su reparto del riesgo | Allá, cómo se elige entre precio cerrado y tiempo y materiales; acá, qué se registra y cómo se factura con cada modelo, en cualquier rubro |
| [Emprender/Modelo-de-negocio](../Emprender/Modelo-de-negocio/modelo-de-negocio.md) | la economía de la firma como modelo de negocio (Maister), la capacidad con teoría de colas, el abono y el servicio productizado | Allá, por qué una firma gana o pierde plata y qué cifras de referencia hay; acá, cómo se miden la utilización, la realización y el margen desde el registro de la firma en marcha |
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | el presupuesto y el pedido de venta como documentos | El presupuesto aceptado o el contrato firmado abre el proyecto; de ahí en adelante es de acá |
| [Contabilidad](../Contabilidad/contabilidad.md) | el asiento, el ingreso según la NIIF 15, el costeo por órdenes, el proyecto como dimensión | Acá se calcula el avance, el trabajo en curso y lo que se factura; allá, el asiento que lo registra |
| [Administración de personal y nómina](../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) | la asistencia, el legajo y la liquidación | Allá, cuántas horas trabajó una persona; acá, a qué proyecto se imputan y cuáles se cobran |
| [Tesorería](../Tesoreria/tesoreria.md) | el cobro y el crédito | Acá se emite la factura del proyecto; allá se cobra |
| [Impuestos](../Impuestos/impuestos.md) | qué impuesto lleva la factura y qué retenciones se sufren | La nota de Argentina de acá los nombra y enlaza las [retenciones y percepciones en Argentina](../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md) |
| [Procesos de negocio](../Procesos-de-negocio/del-proyecto-al-cobro.md) | el recorrido del proyecto al cobro | El recorrido entero allá; cada paso, en su dominio |
| [Software de gestión](../Software-de-gestion/software-de-gestion.md) | el PSA como categoría de producto ([PSA](../Software-de-gestion/Categorias-de-producto/psa.md)) y las columnas técnicas | Acá el saber del dominio, que existe sin software |
| [Servicio al cliente](../Servicio-al-cliente/servicio-al-cliente.md) y [Activos y mantenimiento](../Activos-y-mantenimiento/Servicio-de-campo/servicio-de-campo.md) | la posventa y la orden de trabajo sobre un equipo | Un servicio de campo se gestiona allá aunque se facture por hora |

Cuando se armó el tema, varios vecinos no existían y se nombraban sin enlace; la sesión 16 del mapa (#123) los enlazó.

## Árbol

```
Servicios-profesionales-y-proyectos/
  servicios-profesionales-y-proyectos.md   el todo: la firma que vende horas de gente, los cinco objetos y cómo se conectan
  servicios-profesionales-en-argentina.md  factura de servicios, honorarios con arancel, ajuste por inflación, retenciones
  Proyecto-del-cliente/                    el proyecto como registro económico frente a un cliente
    proyecto-del-cliente                     (entrada) de la venta al proyecto, datos, estados, facturable o interno, cierre
    presupuesto-del-proyecto                 horas, costo y precio por fase, tarea o rol; línea base y estimación al terminar
    hitos-y-entregables                      el hito como evento de aceptación y de facturación
    orden-de-cambio                          el cambio de alcance como documento con precio y efecto en el presupuesto
  Asignacion-de-personas/                  quién trabaja en qué proyecto, a nivel de la firma
    asignacion-de-personas                   (entrada) demanda, capacidad y quién decide
    roles-y-habilidades                      rol genérico, persona con nombre, taxonomía de habilidades
    reserva-de-personas                      pedido de recurso, reserva tentativa y firme, conflictos
    demanda-y-capacidad                      pronóstico desde la cartera y el embudo, banco, subcontratar
  Registro-de-horas/                       el trabajo hecho, imputado a un proyecto
    registro-de-horas                        (entrada) la hora imputada como movimiento
    hoja-de-horas                            período, facturable o no, aprobación, correcciones, cierre
    gastos-del-proyecto                      gastos imputados y reembolsables, recargo
    calidad-del-registro                     subregistro, carga tarde, registro automático
  Facturacion-del-proyecto/                de la hora y el hito a la factura
    facturacion-del-proyecto                 (entrada) la regla de facturación según el modelo de cobro
    facturacion-por-hora                     tarifas, topes, borrador desde horas aprobadas, ajustes
    facturacion-por-hito                     calendario de facturación, anticipos, retención de garantía
    abono-y-bolsa-de-horas                   pago periódico y horas prepagas que se consumen
    trabajo-en-curso                         trabajado sin facturar, facturado sin devengar, ingreso por avance
  Rentabilidad-de-la-firma/                si el proyecto y la firma ganan plata
    rentabilidad-de-la-firma                 (entrada) del proyecto a la firma, qué medir
    costo-y-margen-del-proyecto              costo de la hora cargado, margen del proyecto y del cliente
    utilizacion                              facturable, productiva, el denominador, objetivos
    realizacion                              de la tarifa de lista a lo facturado y a lo cobrado
  Fundamentos/
    fundamentos-de-servicios-profesionales   (entrada) historia, escuelas, fuentes, mitos
    glosario-de-servicios-profesionales      términos con su nombre en inglés
```

## Supuestos

- El árbol general y los límites con los vecinos vienen aprobados del mapa (#94, #98, #101, #104). El árbol del tema lo propone esta sesión sin esperar respuesta; la persona lo revisa en el PR.
- **Gestión de proyectos se mergeó mientras se armaba este tema** (PR #128) y cubre el método. Por eso este tema no tiene verticales de planificación ni de seguimiento: el avance y el plan son de allá, y acá entran solo como dato que mueve plata (presupuesto del proyecto, hito, trabajo en curso).
- Las cinco verticales siguen a APQC 5.0 (5.2 recursos, 5.3 entrega y cierre financiero) y a los módulos que separan los productos de servicios (proyecto, planificación de recursos, horas, facturación), más la rentabilidad, que el campo mide con indicadores propios (utilización, realización).
- El nombre de la carpeta es el del tema del mapa, «Servicios profesionales y proyectos», aunque sea largo, para que no se confunda con `Gestion-de-proyectos/`.
- Lo de la Argentina va en una sola nota del tema, porque toca dos verticales y es corto; lo impositivo recurrente va al tema [Impuestos](../Impuestos/impuestos.md), que se enlazó en la sesión 16 (#123).
