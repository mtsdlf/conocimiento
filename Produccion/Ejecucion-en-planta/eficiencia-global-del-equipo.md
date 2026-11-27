---
resumen: >-
  La eficiencia global del equipo (OEE) mide qué parte del tiempo planificado un equipo produjo piezas buenas a la velocidad ideal. Es el producto de tres factores, disponibilidad, rendimiento y calidad, y su valor depende tanto de la planta como de qué se decidió contar como tiempo planificado y como velocidad ideal.
estado: borrador
estabilidad: semi
fuentes:
  - "oee.com, Calculating OEE (fórmulas y ejemplo; sitio de un proveedor, según el resumen): https://www.oee.com/calculating-oee/"
  - "oee.com, OEE Six Big Losses (según el resumen): https://www.oee.com/oee-six-big-losses/"
  - "oee.com, World-Class OEE (según el resumen): https://www.oee.com/world-class-oee/"
  - "oee.com, TEEP (según el resumen): https://www.oee.com/teep/"
  - "Wikipedia, Overall equipment effectiveness (según el resumen): https://en.wikipedia.org/wiki/Overall_equipment_effectiveness"
  - "ISO 22400-2:2014, KPIs for manufacturing operations management, Part 2, vista previa (cláusulas 1 a 5.2): https://cdn.standards.iteh.ai/samples/54497/10e33d2a34c144558b5e3024ee5e1cb0/ISO-22400-2-2014.pdf (ficha oficial: https://www.iso.org/standard/54497.html)"
  - "Bengtsson, Andersson y Ekström (2022), Measuring preconceived beliefs on the results of overall equipment effectiveness, Journal of Quality in Maintenance Engineering 28(2):391-410, doi 10.1108/JQME-03-2020-0016 (según el resumen): https://www.emerald.com/insight/content/doi/10.1108/JQME-03-2020-0016/full/html"
  - "Bengtsson, Andersson y Ekström, Misconceptions Within the Use of Overall Equipment Effectiveness, Advances in Transdisciplinary Engineering 13 (SPS2020):36-47, doi 10.3233/ATDE200141 (resumen): https://ebooks.iospress.nl/pdf/doi/10.3233/ATDE200141"
  - "Nakajima, Introduction to TPM: Total Productive Maintenance, Productivity Press, 1988 (no leído; citado por las fuentes de arriba)"
  - "Activos-y-mantenimiento/.investigacion/estrategia-y-fundamentos.md (Wikipedia sobre TPM Tenkai, 1982)"
  - "Produccion/.investigacion/ejecucion-en-planta.md (sección 5), ejecucion-en-planta-2.md (sección 5) y fundamentos-y-contraria.md (tabla de mitos), 2026-11-27"
aliases: [eficiencia global del equipo, eficiencia general de los equipos, efectividad global del equipo, overall equipment effectiveness, OEE, disponibilidad, availability, rendimiento, performance, calidad, quality, seis grandes pérdidas, six big losses, tiempo ideal de ciclo, ideal cycle time, TEEP, total effective equipment performance, utilización, OEE de clase mundial, world-class OEE, ISO 22400]
creado: 2026-11-27
revisado:
---

# Eficiencia global del equipo

La eficiencia global del equipo (OEE) mide qué parte del tiempo planificado un equipo produjo piezas buenas a la velocidad ideal. Es el producto de tres factores, disponibilidad, rendimiento y calidad, y su valor depende tanto de la planta como de qué se decidió contar como tiempo planificado y como velocidad ideal.

Nació en el mantenimiento productivo total (TPM), como cuenta [fundamentos de activos y mantenimiento](../../Activos-y-mantenimiento/Fundamentos/fundamentos-de-activos-y-mantenimiento.md), pero mide la línea mientras produce, y por eso está en [Ejecución en planta](ejecucion-en-planta.md). Su primer factor, la disponibilidad, se mide también desde mantenimiento con otras fórmulas, en [indicadores de mantenimiento](../../Activos-y-mantenimiento/Desempeno-de-los-activos/indicadores-de-mantenimiento.md). La meta de OEE de cada centro de trabajo es un dato de la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md). En el PCF de APQC entra en 4.3.2.6 «Assess production performance».

## Los tres factores

Las fórmulas más difundidas son las de un sitio de divulgación de un proveedor, según el resumen:

| Factor | Fórmula | Qué pierde |
|---|---|---|
| Disponibilidad | «Run Time / Planned Production Time» | el tiempo parado dentro del tiempo planificado |
| Rendimiento | «(Ideal Cycle Time × Total Count) / Run Time» | la velocidad: produce menos de lo que podría mientras anda |
| Calidad | «Good Count / Total Count» | las piezas que no salen buenas |

El tiempo ideal de ciclo es «the fastest cycle time that your process can achieve in optimal circumstances». Multiplicados, los tres factores se simplifican: la OEE es igual a piezas buenas por tiempo ideal de ciclo, sobre el tiempo planificado (cuenta de la base sobre las fórmulas). Es el tiempo que habría hecho falta para las piezas buenas, sobre el que había.

En este tema, rendimiento es el segundo factor de la OEE. No es el rendimiento de la [lista de materiales](../Producto-y-proceso/lista-de-materiales.md#merma-del-componente-y-rendimiento-de-la-salida), que mide cuánto producto sale de lo que entra.

## Un ejemplo de un turno

El ejemplo es el del mismo sitio; la base rehízo las cuentas y cierran.

| Dato | Valor |
|---|---|
| Turno | 480 minutos |
| Pausas | 60 minutos |
| Tiempo planificado | 480 − 60 = 420 minutos |
| Paradas | 47 minutos |
| Tiempo en marcha | 420 − 47 = 373 minutos |
| Tiempo ideal de ciclo | 1 segundo por pieza |
| Piezas producidas | 19.271 |
| Piezas rechazadas | 423 |
| Piezas buenas | 18.848 |

- Disponibilidad: 373 / 420 = 88,81 %.
- Rendimiento: 19.271 × 1 s / (373 × 60 s) = 19.271 / 22.380 = 86,11 %.
- Calidad: 18.848 / 19.271 = 97,80 %.
- OEE: 0,8881 × 0,8611 × 0,9780 = 74,79 %.

La cuenta corta da lo mismo: 18.848 piezas buenas × 1 s = 18.848 s, sobre 420 × 60 = 25.200 s planificados, es 74,79 % (cuenta de la base). La página de Wikipedia trae otro ejemplo, pero su producto final no coincide con los factores que calcula, así que no se usa.

## Las seis grandes pérdidas

Cada factor agrupa dos pérdidas. Los nombres son los del mismo sitio, según el resumen; Wikipedia usa una tabla con otros nombres, y el original de Nakajima no se leyó.

| Factor | Pérdida | Ejemplos, según la fuente |
|---|---|---|
| Disponibilidad | Fallas del equipo («Equipment Failure») | roturas, paradas no planificadas, falta de operarios o de material, línea «starved or blocked» |
| Disponibilidad | Preparación y ajustes («Setup and Adjustments») | cambios de formato, ajustes, limpieza, calentamiento |
| Rendimiento | Paradas menores y tiempo ocioso («Idling and Minor Stops») | detenciones cortas que no se registran como parada |
| Rendimiento | Velocidad reducida («Reduced Speed») | marchar por debajo del tiempo ideal de ciclo |
| Calidad | Defectos del proceso («Process Defects») | piezas malas en marcha normal |
| Calidad | Pérdidas al arranque («Reduced Yield») | piezas malas hasta que el proceso se estabiliza |

Las pérdidas de calidad son los rechazos de [consumo y declaración](consumo-y-declaracion.md), que se deciden como [no conformidad](../Calidad/no-conformidad.md); las fallas abren una [solicitud de trabajo](../../Activos-y-mantenimiento/Orden-de-trabajo/solicitud-de-trabajo.md) de mantenimiento.

## Los tiempos de ISO 22400-2

ISO 22400-2 (2014) define los indicadores de la gestión de operaciones de manufactura, e incluye la OEE. La vista previa pública trae los tiempos con que se calcula, no la fórmula:

| Término | Definición |
|---|---|
| Tiempo de operación planificado (POT) | «the planned time in which a work unit can be used» |
| Tiempo ocupado planificado (PBT) | «the planned operation time minus the planned downtime» |
| Tiempo de producción real (APT) | «the actual time during which a work unit is producing. It includes only the value-adding functions» |
| Tiempo de proceso real de la unidad (AUPT) | «the actual production time plus the actual unit setup time» |
| Tiempo planificado de marcha por unidad (PRI) | «the planned time for producing one quantity unit» |

Según el resumen de un buscador, la norma calcula la disponibilidad como APT sobre PBT; la cláusula no se leyó. Si es así, hay dos vocabularios para la misma idea: el tiempo en marcha y el planificado del sitio de divulgación, y el tiempo de producción real y el ocupado planificado de la norma. Un detalle cambia el número: en la norma la preparación queda fuera del tiempo de producción real (lectura de la base sobre las definiciones).

> [!NOTE] Sin fuente todavía: la cláusula 6 de ISO 22400-2, con la fórmula de la OEE y de sus factores, y el anexo B con el cálculo alternativo por pérdidas. La norma es de pago.

## TEEP: la OEE sobre todo el calendario

La OEE no mira el tiempo que no se planificó usar el equipo. La TEEP sí: según el mismo sitio, «TEEP = OEE × Utilization», con «Utilization = Planned Production Time / All Time». Su ejemplo: un equipo con 65 % de OEE, programado 80 de las 168 horas de la semana, tiene 47,62 % de utilización y 30,95 % de TEEP (la base rehízo la cuenta). Wikipedia llama a la utilización «Loading». Como inferencia de la base, la OEE dice si se aprovecha el tiempo planificado y la TEEP, si hay capacidad ociosa para sumar turnos antes de comprar otra máquina.

## El 85 % de clase mundial

La cifra circula como la OEE de una planta de clase mundial. El sitio de divulgación la atribuye a Nakajima, que habría definido los componentes «90% Availability, 95% Performance, and 99% Quality» como mínimos, y advierte que esos números «have roots in a particular place (Japan), at a particular time (1970s), and in a particular industry (automotive)». El producto da 0,90 × 0,95 × 0,99 = 84,6 %, que redondea a 85 % (cuenta de la base).

> [!IMPORTANT]
> **De quién es el 85 %.** Bengtsson, Andersson y Ekström (2022), según el resumen, dicen que Nakajima presenta condiciones ideales («availability is greater than 90%, performance is greater than 95% and quality is greater than 99%») y atribuyen la lectura del 85 % como «world-class level» a Jonsson y Lesshammar (1999). Otro proveedor, visto solo en el buscador, da 99,9 % de calidad, que con los otros dos factores da 85,4 % (cuenta de la base). La fuente académica coincide con 99 %.

El año del libro también varía según la fuente. Wikipedia dice, según el resumen leído para Activos, que el término aparece por primera vez en *TPM Tenkai*, de Nakajima, en 1982. El sitio de divulgación fecha en 1984 el libro *Introduction to TPM*, traducido al inglés y publicado en 1988. El artículo académico cita la edición de 1988. Ninguna de las tres fechas se verificó en el libro.

## Cómo se engaña la medida

La OEE sirve para mejorar un equipo contra sí mismo; las fuentes coinciden en que compararla es arriesgado. Wikipedia, según el resumen: «OEE (as a number) is NOT suitable for comparing machines or benchmarking» y «OEE cannot be used to measure employee performance». Bengtsson y otros (2020) cuentan entre los malentendidos «the view on and hunt for world class levels» y «the issue of comparison of OEE results», y señalan que los factores «are not weighted» y que «no financial issues are taken into consideration».

Los estudios con datos encuentran niveles reales mucho más bajos que el 85 %, y Koch (2003) lo explica por «different ways of setting the OEE definitions», según el resumen del artículo de 2022. El mismo artículo concluye que la OEE «does not consider compliance with the production plan»: un equipo puede tener buena OEE fabricando lo que no se pidió, como discute [programación de planta](programacion-de-planta.md#cumplimiento-del-programa).

Por construcción, el número sube sin que la planta mejore (lectura de la base sobre las fórmulas):

- **Un tiempo ideal de ciclo flojo.** Si se toma el tiempo habitual en lugar del más rápido posible, el rendimiento sube.
- **Paradas pasadas a planificadas.** Lo que sale del tiempo planificado ya no resta disponibilidad: en el ejemplo, la pausa de 60 minutos no cuenta.
- **Preparaciones fuera del tiempo planificado.** Con la definición de ISO, el tiempo de preparación puede quedar afuera según cómo se cargue.
- **Rechazos recuperados.** Si lo reprocesado vuelve como bueno, la calidad no muestra el reproceso.

La defensa es guardar la definición junto al número: qué entra en el tiempo planificado, de dónde sale el tiempo ideal de ciclo y cómo se cuentan los reprocesos (criterio de la base, en línea con [fundamentos de producción](../Fundamentos/fundamentos-de-produccion.md#lo-que-las-escuelas-le-piden-a-un-sistema)).

## Qué guarda un sistema para la OEE

- Por equipo y turno: tiempo planificado, pausas y paradas planificadas, y cada parada con su inicio, fin y causa, codificada por las seis pérdidas.
- Por producto y equipo: el tiempo ideal de ciclo, con su fuente y vigencia.
- Por turno: piezas producidas, buenas y rechazadas, que salen de la [declaración de producción](consumo-y-declaracion.md#la-declaración-de-producción).
- La definición usada, para que dos números se puedan comparar.

Los sistemas abiertos leídos no calculan la OEE: la hoja de cada operación guarda tiempos y cantidades, y uno guarda la meta de OEE del centro. En papel alcanza una planilla por turno con las paradas al minuto y el conteo de piezas.
