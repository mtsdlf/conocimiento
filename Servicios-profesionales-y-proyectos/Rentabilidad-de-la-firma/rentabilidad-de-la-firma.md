---
resumen: >-
  La rentabilidad de la firma es si cada proyecto, cada cliente y la firma entera ganan plata, medida desde el registro de la firma en marcha. Se arma con cuatro datos: el costo de la hora, el margen del proyecto, la utilización y la realización.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 9.5.1.5 «Analyze and report employee utilization»"
  - "Wikipedia, Utilization rate (según resumen): https://en.wikipedia.org/wiki/Utilization_rate"
  - "Servicios-profesionales-y-proyectos/.investigacion/metricas-fundamentos-y-contraria.md"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md"
aliases: [rentabilidad de la firma, rentabilidad de un servicio profesional, firm profitability, métricas de servicios profesionales, professional services KPIs, indicadores de una consultora]
creado: 2026-11-27
revisado:
---

# Rentabilidad de la firma

La rentabilidad de la firma es si cada proyecto, cada cliente y la firma entera ganan plata, medida desde el registro de la firma en marcha. Se arma con cuatro datos: el costo de la hora, el margen del proyecto, la utilización y la realización.

Es la quinta parte de [Servicios profesionales y proyectos](../servicios-profesionales-y-proyectos.md), y la última del recorrido. Recibe del [registro de horas](../Registro-de-horas/registro-de-horas.md) las horas imputadas, con su costo, y de la [facturación del proyecto](../Facturacion-del-proyecto/facturacion-del-proyecto.md) el ingreso. Le devuelve al [proyecto del cliente](../Proyecto-del-cliente/proyecto-del-cliente.md) lo que aprende: qué tarifas y qué presupuestos dejan plata. Por qué una firma de servicios gana o pierde plata como modelo de negocio, con la ecuación de Maister y la pirámide, está en la [economía de una firma de servicios](../../Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md); acá está cómo se mide cada palanca con los datos que ya se cargan.

## De la hora disponible a la ganancia

Las cuatro medidas son eslabones de la misma cadena. Cada uno pierde una parte de lo que trae el anterior:

```mermaid
flowchart LR
  C[Horas de capacidad] -->|utilización| F[Horas facturables]
  F -->|por la tarifa de lista| V[Valor estándar]
  V -->|realización| I[Lo facturado y cobrado]
  I -->|menos el costo de las horas y los gastos| M[Margen]
```

La cadena es criterio de esta base, armado con las definiciones de las notas de abajo. Es la misma cuenta que la ecuación de Maister abre a nivel de firma, con la tarifa, la utilización y la realización como factores; la diferencia es que acá se calcula por persona, por proyecto y por cliente, desde cada hora imputada.

APQC no trata la rentabilidad como parte de la entrega del servicio: pone la utilización en finanzas, en 9.5.1.5 «Analyze and report employee utilization». Esta base la junta con las otras medidas porque las cuatro salen de la misma hora imputada.

## Qué se mide en cada nivel

| Nivel | Qué se mira | Con qué dato |
|---|---|---|
| Persona y rol | Utilización contra el objetivo del rol | Horas facturables sobre capacidad |
| Proyecto | Margen, y desvío contra el presupuesto | Costo de las horas y gastos contra el ingreso |
| Cliente | Margen sumado de sus proyectos, más lo gastado fuera de ellos | Los proyectos y los proyectos internos del cliente |
| Firma | Utilización media, realización, margen total | Todo lo anterior, más la estructura que no cae en ningún proyecto |

Que la firma pueda medir el cliente y la persona depende de que cada hora lleve proyecto, persona, rol y el atributo facturable, que es lo que guarda la [hoja de horas](../Registro-de-horas/hoja-de-horas.md).

## Por qué una utilización alta puede convivir con un margen bajo

La gente puede estar llena de horas facturables y la firma ganar poco. Cada eslabón de la cadena puede romperse aunque el anterior esté bien. Los casos que siguen son criterio de esta base:

- **La realización es baja.** Las horas se trabajan y se cargan como facturables, pero se castigan en el borrador de la factura o el cliente no las paga. La [utilización](utilizacion.md) cuenta la hora; la [realización](realizacion.md) muestra que no se cobró.
- **El proyecto a precio cerrado se pasó.** Las horas cuentan como facturables para la utilización, pero el precio no se mueve: más horas son solo más costo.
- **La tarifa no cubre el costo cargado.** Si la tarifa se fijó sin mirar el [costo de la hora](costo-y-margen-del-proyecto.md), o el costo subió y la tarifa no, cada hora facturable pierde plata.
- **El denominador está inflado.** Si la utilización se calcula sobre las horas registradas y el trabajo interno no se carga, el número sube sin que se facture más.
- **La mezcla de personas no es la del trabajo.** Si las horas facturables las hacen los más caros en tareas que podría hacer alguien con menos experiencia, la utilización es alta y el margen es chico. Es el problema del apalancamiento, explicado en [cómo envejece un servicio](../../Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md#cómo-envejece-un-servicio).

## Las medidas como meta

Las cuatro medidas sirven para ver dónde se pierde plata, y se deforman cuando se convierten en metas personales. La utilización es la más expuesta, porque la carga la misma persona a la que se evalúa: la ley de Goodhart aplicada a la utilización está en [utilización](utilizacion.md#cuando-la-utilización-se-vuelve-meta), y la crítica de los estudios jurídicos a la hora facturable, en [Fundamentos](../Fundamentos/fundamentos-de-servicios-profesionales.md). Cómo se atan bonos e incentivos a estas medidas es de [compensación e incentivos](../../Liderazgo-y-direccion/Gestion-de-personas/compensacion-e-incentivos.md).

> [!NOTE] Sin fuente todavía: cifras de referencia con método de realización, lockup, margen por proyecto e ingreso por persona. Las de utilización están en la [economía de una firma de servicios](../../Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md#cifras-de-utilización-de-referencia).

## Qué hay en la rentabilidad de la firma

- [Costo y margen del proyecto](costo-y-margen-del-proyecto.md): el costo de la hora cargado, separado de la tarifa; el margen del proyecto y del cliente, y cómo cambia según el modelo de cobro. Leelo para saber si un proyecto deja plata.
- [Utilización](utilizacion.md): horas facturables sobre horas de referencia, el denominador que cambia el número y por qué es mala meta. Leelo para medir cuánto de la capacidad se factura.
- [Realización](realizacion.md): de la tarifa de lista a lo facturado y a lo cobrado, los castigos y el lockup. Leelo para saber cuánto del trabajo hecho llega a la caja.
