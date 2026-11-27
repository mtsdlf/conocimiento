---
resumen: >-
  Demanda y capacidad es la cuenta que dice, con meses de anticipación, si a la firma le van a sobrar o faltar personas de cada rol: la demanda sale de las reservas de los proyectos vendidos y de lo que se espera vender, y la capacidad, de las horas disponibles de cada persona. Cuando no cierra, se contrata, se subcontrata o se mueve la fecha de un proyecto.
estado: vigente
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 5.2.1 «Manage service delivery resource demand» (5.2.1.1 a 5.2.1.8) y 5.2.2 «Create and manage resource plan» (5.2.2.2 a 5.2.2.6)"
  - "Microsoft Learn, Project Operations, Booking status (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/booking-status"
  - "Maister, D. (2004), The Anatomy of a Consulting Firm, capítulo 2 de The Advice Business (Pearson), adaptado de Managing the Professional Service Firm (1997), leído en la página del autor (sección «Leverage Structure»): https://davidmaister.com/articles/4/2/index.html"
  - "SFIA Foundation, SFIA 9, skill «Workforce planning» (WFPL), notas de guía, leída en el sitio: https://sfia-online.org/en/sfia-9/skills/workforce-planning"
  - "Servicios-profesionales-y-proyectos/.investigacion/asignacion-y-horas.md (sección 1.2)"
  - "Servicios-profesionales-y-proyectos/.investigacion/verificacion-asignacion-y-horas.md"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 1)"
aliases: [demanda de recursos, resource demand, plan de recursos, resource plan, pronóstico de recursos, resource forecast, capacity planning, banco, bench, personas sin asignar, subcontratar]
creado: 2026-11-27
revisado: 2026-11-27
---

# Demanda y capacidad

Demanda y capacidad es la cuenta que dice, con meses de anticipación, si a la firma le van a sobrar o faltar personas de cada rol: la demanda sale de las reservas de los proyectos vendidos y de lo que se espera vender, y la capacidad, de las horas disponibles de cada persona. Cuando no cierra, se contrata, se subcontrata o se mueve la fecha de un proyecto.

Es la mirada de la firma dentro de la [asignación de personas](asignacion-de-personas.md): suma las [reservas](reserva-de-personas.md) de todos los proyectos por [rol](roles-y-habilidades.md) y por semana. No repite dos cuentas que ya están en la base: cuántos clientes entran en un equipo y por qué no conviene llenarlo, en [capacidad de un equipo de servicio](../../Emprender/Modelo-de-negocio/capacidad-de-un-equipo-de-servicio.md#por-qué-no-conviene-trabajar-al-100-); y cuánto termina un equipo dentro de un proyecto, en [capacidad y costo](../../Gestion-de-proyectos/Planificacion/capacidad-y-costo.md).

## El pronóstico de la demanda como ciclo

APQC desglosa la demanda en ocho pasos (5.2.1), y leídos en orden forman un ciclo, no un cálculo:

1. «Monitor pipeline»: mirar el embudo de ventas.
2. «Develop baseline forecasts»: un pronóstico de base.
3. «Collaborate with customers»: confirmarlo con los clientes.
4. «Develop consensus forecast»: acordar un número de consenso.
5. «Determine availability of skills to deliver on current and forecast customer orders»: cruzar con las habilidades disponibles.
6. «Monitor activity against forecast and revise forecast»: comparar con lo que pasó y corregir.
7. «Evaluate and revise forecasting approach»: revisar el método.
8. «Measure forecast accuracy»: medir cuánto se acertó.

El marco parte de dos fuentes de demanda: los pedidos vigentes (lo vendido) y el embudo (lo que se espera vender). No dice cómo pesar el embudo. Una forma de hacerlo es multiplicar cada [oportunidad](../../Relacion-con-clientes/Seguimiento-comercial/oportunidad.md#la-probabilidad-de-la-etapa-o-de-la-persona) por su probabilidad de cierre; es lectura de esta base, no está en la fuente.

## Tres capas de demanda

Como criterio de esta base, la demanda de una semana se lee mejor en tres capas apiladas, de la más segura a la menos:

| Capa | De dónde sale | Qué tan firme es |
|---|---|---|
| Reservas firmes | Proyectos firmados con personas reservadas | Consumen capacidad |
| Reservas tentativas y pedidos sin cubrir | Proyectos por empezar o por confirmar | No consumen capacidad, pero vienen |
| Embudo | Oportunidades abiertas, pesadas por probabilidad | Pronóstico |

La separación entre las dos primeras viene de la práctica de los sistemas: una reserva firme consume la capacidad de la persona y una tentativa no. La tercera es el embudo que APQC pone al principio del ciclo. Cuando las tres capas de un rol pasan la capacidad en las semanas que vienen, falta gente de ese rol; cuando las dos primeras quedan muy por debajo, sobra.

Un pronóstico así es un número con mucha incertidumbre. Cómo se expresa como rango y por qué el plan propio sale optimista está en [pronóstico](../../Gestion-de-proyectos/Planificacion/pronostico.md).

## De los proyectos a las personas por nivel

Maister hace la cuenta para una consultora con un proyecto «típico» que pide el 50 % del tiempo de un socio, el 100 % de uno de nivel medio y el tiempo completo de tres junior. Si la firma se propone que los socios facturen el 75 % de su tiempo y los junior el 90 %, y tiene cuatro socios, sale que cabe el equivalente de tres socios de tiempo completo, o sea seis proyectos; esos seis proyectos piden el equivalente de seis personas de nivel medio y de 18 junior de tiempo completo, que a esas tasas son 8 y 20 personas. La proporción queda en un socio por cada dos de nivel medio y cada cinco junior. Es un ejemplo numérico del autor, no una medición.

Dos cosas sirven para esta nota. La demanda se pasa de proyectos a personas por nivel, no por nombre. Y el desajuste de la mezcla es un costo en las dos direcciones: si el trabajo que entra pide más junior y menos socios de los que hay, «higher-priced people will end up performing lower-value tasks» y los socios quedan subutilizados; si pide más seniors, falta gente calificada y hay riesgo de calidad. La cuenta de Maister es de una consultora con una escalera de socios, medios y junior; una firma sin esa pirámide tiene que adaptarla.

## La capacidad de cada persona

La capacidad es lo que cada persona puede trabajar en proyectos por semana. Como criterio de esta base, se calcula como su jornada menos las ausencias conocidas y menos el tiempo que la firma reserva para otras cosas (vender, administrar, formarse). El plan de recursos de APQC la cruza con la demanda en 5.2.2.3 «Match resource demand with capacity, skills, and capabilities» y la vigila en 5.2.2.6 «Monitor and manage resource capacity and availability».

Llenarla al 100 % es un error que la base ya explica dos veces: alarga los plazos y deja sin margen para lo que llega sin aviso. Qué parte de la capacidad se espera que se facture es la [utilización](../Rentabilidad-de-la-firma/utilizacion.md) objetivo, que se mide del otro lado, con las horas cargadas.

## Cuando no cierra: banco, contratar o subcontratar

Si sobra gente, la firma tiene personas sin proyecto, lo que en inglés se llama el banco (*bench*). APQC no usa el término; 5.2.2.6 lo cubre sin nombrarlo. Si falta, hay tres salidas: contratar, que es de [contratar](../../Liderazgo-y-direccion/Gestion-de-personas/contratar.md); subcontratar a otra firma o a un independiente, que APQC prevé en 5.2.2.4 «Collaborate with suppliers and partners to supplement skills and capabilities»; o, como criterio de esta base, mover la fecha de un proyecto, que es una decisión de [portafolio](../../Gestion-de-proyectos/Gobierno-y-cierre/portafolio.md). APQC también pide identificar los recursos críticos y la capacidad de los proveedores (5.2.2.5).

SFIA, el marco público de habilidades, tiene una habilidad «Workforce planning» (planificación de la dotación) y dice en sus notas que mira toda la organización y es «more strategic than tactical resource allocation to projects». Entre sus actividades están evaluar el estado actual, analizar datos de la organización «over extended time periods to discover multi-year trends» y elaborar planes para cerrar las brechas con acciones como la contratación externa, el desarrollo interno, la recapacitación y «sourcing external partners», o sea subcontratar. Es la misma lista de salidas de arriba, ahora con una fuente que no es el marco de procesos, pero no dice cuándo conviene cada una.

> [!NOTE]
> Sin fuente todavía: cuándo conviene contratar y cuándo subcontratar, cuánto banco es sano, qué se hace con las personas sin proyecto, y con cuánta anticipación se mira la demanda (SFIA habla de tendencias de varios años para el plan de la dotación de toda la organización, no del horizonte del pronóstico de una firma de servicios). De Maister se leyó solo un capítulo sobre la mezcla de niveles; su libro y el de Løwendahl no se leyeron. Se buscó también en resúmenes de la literatura académica sin dar con nada que midiera el banco o el horizonte en firmas de servicios.
