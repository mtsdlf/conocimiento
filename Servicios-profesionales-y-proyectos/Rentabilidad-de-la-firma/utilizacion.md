---
resumen: >-
  La utilización es la parte del tiempo de una persona o de la firma que se va en trabajo facturable: horas facturables sobre unas horas de referencia. El número depende de cuál es ese denominador, y si se calcula sobre las horas registradas sube solo cuando la gente deja de cargar el trabajo que no se cobra.
estado: borrador
estabilidad: semi
fuentes:
  - "Wikipedia, Utilization rate (según resumen; su única fuente es el blog de un proveedor de software de servicios): https://en.wikipedia.org/wiki/Utilization_rate"
  - "Wikipedia, Billable hours (según resumen; cita a McKenna y Maister, First Among Equals, 2012): https://en.wikipedia.org/wiki/Billable_hours"
  - "Strathern (1997), 'Improving ratings': audit in the British University system, European Review 5(3), 305-321, p. 308 (leída en el PDF, copia en https://www.Gwern.net/doc/statistics/decision/1997-strathern.pdf): https://www.cambridge.org/core/journals/european-review/article/improving-ratings-audit-inthe-british-university-system/FC2EE640C0C44E3DB87C29FB666E9AAB"
  - "Wikipedia, Goodhart's law (según resumen; solo para el enunciado de Goodhart de 1975, capítulo en Courakis (ed.), Inflation, Depression, and Economic Policy in the West, 1975, p. 116, que no se pudo abrir): https://en.wikipedia.org/wiki/Goodhart%27s_law"
  - "SPI Research, Professional Services Benchmarks (definición de utilización facturable y cifras del PS Maturity Benchmark 2026; no da la fórmula de la encuesta): https://spiresearch.com/professional-services-benchmarks/"
  - "SPI Research, Professional Services Maturity Benchmark 2026 (comunicado, 2026-02-24; da 66,4 % para 2025): https://www.einpresswire.com/article/894826291/"
  - "ABA Commission on Billable Hours Report 2001-2002 (agosto de 2002; leído entero en la copia del Inns of Court): https://inns.innsofcourt.org/media/44347/march_10_2009_program_materials.pdf"
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 9.5.1.5 «Analyze and report employee utilization»"
  - "Microsoft Learn, Dynamics 365 Project Operations, Define roles (el rol lleva una utilización objetivo): https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/define-roles"
  - "Servicios-profesionales-y-proyectos/.investigacion/metricas-fundamentos-y-contraria.md"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md"
aliases: [utilización, utilization, utilization rate, tasa de utilización, utilización facturable, billable utilization, chargeability, utilización productiva, productive utilization, horas disponibles]
creado: 2026-11-27
revisado:
---

# Utilización

La utilización es la parte del tiempo de una persona o de la firma que se va en trabajo facturable: horas facturables sobre unas horas de referencia. El número depende de cuál es ese denominador, y si se calcula sobre las horas registradas sube solo cuando la gente deja de cargar el trabajo que no se cobra.

Es una de las palancas de la [economía de una firma de servicios](../../Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md#la-ecuación-de-la-rentabilidad-por-socio): la productividad de cada persona es su tarifa por su utilización. Allá está por qué importa y cuáles son las [cifras de referencia](../../Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md#cifras-de-utilización-de-referencia); acá, cómo se calcula desde el [registro de horas](../Registro-de-horas/registro-de-horas.md) de la firma en marcha. APQC la pone en finanzas, en 9.5.1.5 «Analyze and report employee utilization», y no en la entrega del servicio. Las agencias de marketing suelen llamarla *chargeability* en lugar de hablar de hora facturable, según la entrada de enciclopedia sobre la hora facturable.

## El denominador cambia el número

El numerador casi no se discute: las horas imputadas a trabajo que se cobra. El denominador sí, y hay dos formas de tomarlo, según el resumen de la entrada de enciclopedia sobre la utilización:

| Denominador | Cuenta | Ejemplo de la fuente | Qué pasa en el borde |
|---|---|---|---|
| Horas registradas | Facturables sobre todas las horas que la persona cargó | 30 de 40 = 75 % | Si el trabajo no facturable no se carga, da siempre 100 % |
| Horas fijas | Facturables sobre una jornada de referencia, por ejemplo la semanal | 32 de 40 = 80 % | Puede pasar del 100 %: 50 de 40 = 125 % |

La misma fuente dice que las licencias y las enfermedades suelen sacarse del denominador. Su única referencia es el blog de un proveedor de software, así que no alcanza para afirmar una definición estándar.

Con horas registradas, la métrica se infla sin que nadie trabaje más. Basta con que la gente deje de cargar la preventa, la capacitación o la administración. La fuente lo dice así: «it's easy to see how this utilization rate can be gamed». Con horas fijas, el número no depende de lo que se carga en lo interno, pero esconde las horas extra: como criterio de esta base, una persona al 110 % no está bien utilizada, está trabajando de más.

Como criterio de esta base, el denominador que menos se deforma es la capacidad de cada persona: su jornada de contrato menos las licencias y los feriados, que es la misma que usa la [demanda y capacidad](../Asignacion-de-personas/demanda-y-capacidad.md) para planificar. Así, lo que se planifica y lo que se mide tienen la misma base.

## Facturable, productiva y la que se cobra

Las palabras se mezclan, y cada una mide otra cosa:

- **Utilización facturable**: horas imputadas a trabajo que se cobra al cliente.
- **Utilización productiva**: suma el trabajo que no se cobra pero que la firma considera útil, como desarrollar un producto propio. Según la misma entrada, aparece en firmas que además venden producto; la fuente lo afirma sin cita.
- **Carga**: todo el trabajo que llega sobre la capacidad, que es la medida de la teoría de colas. Está explicada en [capacidad de un equipo de servicio](../../Emprender/Modelo-de-negocio/capacidad-de-un-equipo-de-servicio.md#dos-utilizaciones-que-no-son-la-misma), y no es lo mismo que la facturable.

Que una hora sea facturable no quiere decir que se cobre. La hora se carga como facturable, y después alguien puede pasarla a no cobrable o de cortesía en el borrador de la factura. La utilización mide la primera parte; cuánto de eso llega a la factura y al cobro es la [realización](realizacion.md). Usar las horas facturadas como numerador mezcla las dos medidas (criterio de esta base).

## Qué tiene que guardar el registro

Para calcular la utilización sin trampas, el registro necesita tres cosas, y las tres viven en otras notas del tema (criterio de esta base sobre lo que dicen esas notas):

1. **Todas las horas, también las que nadie paga.** Por eso el trabajo interno se registra como [proyecto interno](../Proyecto-del-cliente/proyecto-del-cliente.md), con la misma [hoja de horas](../Registro-de-horas/hoja-de-horas.md) que lo facturable. Si la preventa no tiene dónde cargarse, el denominador registrado queda corto.
2. **El atributo facturable en cada hora imputada**, decidido por el proyecto o por quien aprueba. En un sistema de gestión de servicios, el aprobador puede cambiar la cantidad facturable y el tipo de facturación al aprobar de nuevo; cómo se decide está en el [registro de horas](../Registro-de-horas/registro-de-horas.md).
3. **La capacidad de cada persona por período**, que sale de la [demanda y capacidad](../Asignacion-de-personas/demanda-y-capacidad.md).

Una hora imputada a un proyecto a precio cerrado plantea una duda: ¿es facturable? El cliente no la paga una por una, pero es trabajo para un cliente. Como criterio de esta base, conviene contarla como facturable para la utilización y dejar que el [margen del proyecto](costo-y-margen-del-proyecto.md) y la realización muestren si se excedió.

## Objetivos por rol

Un sistema de gestión de servicios permite que el [rol](../Asignacion-de-personas/roles-y-habilidades.md) lleve una utilización objetivo, que pasa por defecto a cada persona que lo juega. La práctica responde a que no todos los niveles facturan lo mismo: quien dirige vende y coordina, y quien recién entra hace el trabajo de producción. Los objetivos por nivel que da Maister en su ejemplo están en las [cifras de referencia](../../Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md#cifras-de-utilización-de-referencia); no se repiten acá.

## Una definición con encuesta detrás

SPI Research, una consultora que publica un benchmark anual de firmas de servicios profesionales, define: «Billable utilization is billable hours divided by available hours». Usa una jornada fija de 2.000 horas al año como horas disponibles: quien factura 1.500 horas está al 75 %, y lo que falta (vacaciones, capacitación, apoyo a ventas, trabajo interno) queda dentro del denominador. Es el caso de las horas fijas de la tabla de arriba, y no coincide con que las licencias salgan siempre del denominador. La página no dice cómo define las horas disponibles la encuesta en sí.

Con esa encuesta (otoño de 2025, 509 firmas con más de 245.000 empleados), el benchmark 2026 da una utilización facturable promedio del 67,6 % en 2025 (68,9 % en 2024), del 75,0 % en el 20 % de firmas de mejor madurez y del 64,9 % en el resto. El 75 % es además la meta que SPI propone, no un resultado de la encuesta. Es una sola fuente, de firmas de servicios en general, con el método descripto en una página y el informe completo pago. La misma edición da otra cifra en otro lugar: el comunicado de SPI del 24 de febrero de 2026 dice que la utilización facturable bajó al 66,4 %, la más baja en los 19 años del benchmark, y es la que repiten Deltek y Certinia y la que usa la [economía de una firma de servicios](../../Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md#cifras-de-utilización-de-referencia). No es otra edición: las dos son del benchmark 2026 y del año 2025. Tampoco se ve que sean dos medidas distintas, porque la tabla de la página la llama «employee billable utilization» y el comunicado «billable utilization», sin definir ninguna de las dos aparte. Ninguna fuente leída explica la diferencia; hasta leer el informe, que es pago, valen las dos como cifras de SPI.

> [!NOTE] Sin fuente todavía: la utilización productiva, qué se saca del denominador según un colegio profesional y los objetivos por nivel con encuesta. Se buscó en el benchmark de SPI y en el informe de la ABA, que no los tratan; el sitio de AICPA no se pudo leer.

## Cuando la utilización se vuelve meta

La utilización es un buen dato y una mala meta. Strathern (1997, p. 308) escribió: «When a measure becomes a target, it ceases to be a good measure», y agrega que Hoskin lo describe como la «ley de Goodhart», por una observación de Goodhart sobre instrumentos de control monetario. La frase es de Strathern y no de Goodhart. El enunciado de Goodhart (1975) sería «Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes», según una entrada de enciclopedia que cita su capítulo de 1975; el original no se pudo leer. Aplicar la ley a la utilización es lectura de esta base.

La aplicación es directa. Si el bono depende de la utilización, la hora interna deja de cargarse y la facturable se estira. Según la entrada de enciclopedia sobre la hora facturable, los libros de gestión de estudios jurídicos critican la hora facturable porque mide cantidad y no calidad, y las horas «expand to fill the time requirement». La comisión de la ABA sobre la hora facturable (2002) coincide: «The billable hour is fundamentally about quantity over quality, repetition over creativity» (prefacio), y señala que las horas registradas pasan a ser «a proxy for quality of work and competence of the lawyer» (sección «Why Billable Hours are So Entrenched»). La crítica entera está en [Fundamentos](../Fundamentos/fundamentos-de-servicios-profesionales.md), y los efectos sobre el dato, en [calidad del registro](../Registro-de-horas/calidad-del-registro.md). La misma idea aplicada al avance de un proyecto está en [medir el avance](../../Gestion-de-proyectos/Seguimiento/medir-el-avance.md#lo-que-se-mide-se-deforma).

Como lectura de esta base, la utilización sirve para ver capacidad ociosa y para planificar contrataciones, y rinde mal como meta individual. Mirada junto con la realización y el margen, deja ver si las horas cargadas se convierten en plata, que es lo que explica la [rentabilidad de la firma](rentabilidad-de-la-firma.md).
