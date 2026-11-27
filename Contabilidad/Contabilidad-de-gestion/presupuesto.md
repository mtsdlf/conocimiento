---
resumen: >-
  El presupuesto es el plan de una empresa expresado en números para un período: cuánto espera vender, gastar, cobrar y pagar, y cómo quedaría su patrimonio; después se compara contra lo real y la diferencia se explica en desvíos.
estado: borrador
estabilidad: semi
fuentes:
  - "OpenStax, Principles of Accounting, Volume 2: Managerial Accounting (2019), sección 7.1: https://openstax.org/books/principles-managerial-accounting/pages/7-1-describe-how-and-why-managers-use-budgets"
  - "OpenStax, ídem, sección 7.4: https://openstax.org/books/principles-managerial-accounting/pages/7-4-prepare-flexible-budgets"
  - "OpenStax, ídem, sección 8.2: https://openstax.org/books/principles-managerial-accounting/pages/8-2-compute-and-evaluate-materials-variances"
  - "HBS Working Knowledge, entrevista sobre Hope y Fraser, Who Needs Budgets? (HBR, febrero de 2003): https://www.library.hbs.edu/working-knowledge/why-budgeting-kills-your-company"
  - "Bjarte Bogsnes, Beyond Budgeting at 25, Beyond Budgeting Institute, marzo de 2023: https://bbrt.org/wp-content/uploads/bb-white-paper.pdf"
  - "Theresa Libby y R. Murray Lindsay (2010), Beyond budgeting or budgeting reconsidered? A survey of North-American budgeting practice, Management Accounting Research 21: 56-75: https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/8/36875/files/2016/12/Libby-Lindsay_budgeting_survey-17bvsph.pdf"
  - "Trabajo de Oxford que cita a Becker (2014), según un resumen: https://ora.ox.ac.uk/objects/uuid:35c45299-832b-4602-95c1-c12e659a8868/files/rfj236339p"
  - "Contabilidad/.investigacion/contabilidad-de-gestion.md"
  - "Contabilidad/.investigacion/posicion-contraria.md"
aliases: [presupuesto maestro, presupuesto flexible, presupuesto estático, presupuesto base cero, presupuesto móvil, análisis de desvíos, variaciones, desvío de precio, desvío de cantidad, budget, master budget, flexible budget, zero-based budgeting, rolling forecast, variance analysis, Beyond Budgeting]
creado: 2026-11-27
revisado:
---

# Presupuesto

El presupuesto es el plan de una empresa expresado en números para un período: cuánto espera vender, gastar, cobrar y pagar, y cómo quedaría su patrimonio; después se compara contra lo real y la diferencia se explica en desvíos.

Según OpenStax (sección 7.1), sirve para que la empresa llegue a sus metas estratégicas y para comunicar sus planes adentro. Se arma sobre la [clasificación de costos](clasificacion-de-costos.md) (sin separar fijos de variables no hay presupuesto flexible) y se compara contra el registro de lo real, cortado por los mismos [centros de costo](centros-de-costo.md).

## El presupuesto maestro y sus dos mitades

Según OpenStax (sección 7.1), el presupuesto maestro tiene dos partes, cada una con sus presupuestos componentes. El operativo planea ingresos y gastos y termina en un [estado de resultados](../Estados-contables/estado-de-resultados.md) proyectado. El financiero planea el uso de activos y pasivos y termina en un [balance](../Estados-contables/balance.md) proyectado. Según un resumen del mismo capítulo, el maestro y sus componentes son presupuestos estáticos: se preparan para un único nivel de actividad.

## Estático, flexible, base cero y móvil

OpenStax distingue cuatro formas (secciones 7.1 y 7.4); la columna «Lo que cuesta» de las dos primeras es inferencia de la base:

| Forma | Qué hace | Lo que cuesta |
|---|---|---|
| Estático | se prepara para un solo nivel de producción en el período | si el volumen real es otro, la comparación mezcla volumen con eficiencia |
| Flexible | ajusta el estático a cada nivel de ventas posible | hay que conocer qué costos son variables |
| Base cero | parte de cero y solo agrega lo que se justifica | justificar cada gasto, aun los obvios, lleva mucho tiempo |
| Móvil | se actualiza en forma continua, agregando períodos | quita tiempo a la dirección para otras tareas |

El ejemplo de Big Bad Bikes (OpenStax 7.4) muestra el flexible. Por unidad: materiales US$ 4, mano de obra US$ 15, carga fabril variable US$ 3, gastos variables de venta y administración US$ 3. Los fijos son US$ 29.000 de fábrica y US$ 18.000 de venta y administración en todos los escenarios.

| | 1000 unidades a US$ 70 | 1500 unidades a US$ 70 (estático) | 1500 unidades a US$ 75 |
|---|---|---|---|
| Ventas | US$ 70.000 | US$ 105.000 | US$ 112.500 |
| Costo de lo vendido | US$ 51.000 | US$ 62.000 | US$ 62.000 |
| Utilidad bruta | US$ 19.000 | US$ 43.000 | US$ 50.500 |
| Utilidad neta | −US$ 2500 | US$ 20.250 | US$ 27.750 |

La utilidad neta es la que da la fuente; con los datos de arriba no se reproduce (salen −US$ 2000, US$ 20.500 y US$ 28.000), así que incluye partidas que acá no se detallan.

Si al final del año se venden 1000 unidades, el real se compara contra la primera columna y no contra la segunda: la diferencia de volumen ya está explicada y lo que queda es eficiencia o precio (inferencia de la base).

## Desvíos: separar el efecto precio del efecto cantidad

Un desvío es la diferencia entre lo real y lo esperado, sea un presupuesto o un [costo estándar](sistemas-de-costeo.md). Este análisis es el mismo para los dos y vive acá. OpenStax (sección 8.2) da las fórmulas para materiales:

- Desvío de precio = (precio real − precio estándar) × cantidad real usada.
- Desvío de cantidad = (cantidad real usada − cantidad estándar para lo producido) × precio estándar.

En el ejemplo de Connie's Candy, el estándar es de US$ 7,00 por libra de material y 0,25 libras por caja. Se compran 20 libras a US$ 9,00 y cada caja termina usando 0,50 libras.

| Desvío | Cálculo de la fuente | Resultado |
|---|---|---|
| Precio, sobre 20 libras | (9,00 − 7,00) × 20 | US$ 40 desfavorable |
| Cantidad, por caja | (0,50 − 0,25) × 7,00 | US$ 1,75 desfavorable |
| Total, por caja | (0,50 × 9,00) − (0,25 × 7,00) = 4,50 − 1,75 | US$ 2,75 desfavorable |

Por caja, el efecto precio es (9,00 − 7,00) × 0,50 = US$ 1,00, que sumado a US$ 1,75 da los US$ 2,75 (cuenta propia, para cerrar el ejemplo). Separarlos sirve para preguntarle a cada área por lo suyo: el de precio, a quien compra; el de cantidad, a quien produce (inferencia de la base).

> [!NOTE]
> Sin fuente todavía: un ejemplo con números de desvíos del presupuesto flexible contra el real (la sección 7.4 de OpenStax trae los escenarios pero no el real, y la 7.5 no se leyó).

## Cómo el presupuesto se vuelve un contrato que se negocia

El propio libro de texto advierte el riesgo de comportamiento: según OpenStax (sección 7.1), quien se evalúa contra el presupuesto puede tentarse a fijar metas bajas para cumplirlas, y quien reporta queda entre informar lo que pasó y lo que se esperaba que pasara.

Jeremy Hope y Robin Fraser llevaron esa crítica al extremo. En la entrevista de HBS Working Knowledge sobre su artículo de 2003 (el artículo no se leyó), describen el presupuesto como un contrato implícito, lleno de distorsión y de juego, en el que quien quiere plata pide de más. Dan cifras sin verificar en el original: una empresa promedio de mil millones de dólares gasta hasta 25.000 días-persona por año en presupuestar, y algunos procesos llevan hasta seis meses. El banco sueco Svenska Handelsbanken dejó el presupuesto a principios de los años setenta.

El Beyond Budgeting Institute, que promueve la posición, dice que el modelo se desarrolló en 1998 y hoy tiene doce principios, seis de liderazgo y seis de procesos (Bogsnes, 2023). Entre los de procesos: «Set directional, ambitious and relative goals; avoid fixed and cascaded targets» y «Plan and make resources available as needed; not through detailed annual budget allocations». El mismo documento advierte que ha visto implementaciones «reduced to Rolling Forecasting exercises or just a more dynamic resource allocation».

## La disputa de Beyond Budgeting y lo que muestran las encuestas

> [!IMPORTANT]
> Hay cuatro posiciones sobre el presupuesto anual.
> - Abandonarlo, según Hope y Fraser: reemplazarlo por metas relativas a dos o tres años, pronósticos móviles y recursos asignados a medida que se necesitan. Es la posición de quienes la promueven; lo que se leyó no trae prueba independiente de sus resultados.
> - Mantenerlo y cambiar la remuneración, según Bruns en la misma entrevista de HBS.
> - Usarlo sabiendo sus costos, como lo presenta OpenStax: una herramienta de planificación y comunicación, con sesgos que hay que vigilar.
> - Adaptarlo sin abandonarlo, que es lo que hacen las empresas según Libby y Lindsay (2010). Encuestaron a organizaciones medianas y grandes de Canadá y Estados Unidos (558 respuestas). El 79 % usa el presupuesto para control, y de ese grupo el 94 % no piensa abandonarlo. Su conclusión: «While problems exist with budgets, organizations are adapting their use to account for these problems rather than abandoning budgets altogether.» La tasa de respuesta fue baja (13,6 % en la muestra canadiense y 1,5 % en la de miembros del IMA), y los autores lo señalan.
>
> Un trabajo de Oxford, según un resumen, cita a Becker (2014): algunas organizaciones que eliminaron el presupuesto anual parecen haberlo restablecido.

La lectura de la base (inferencia) es que el presupuesto se adapta más de lo que se abandona: pronósticos móviles al lado del anual y metas menos atadas a la remuneración. Para un registro contable, eso se traduce en poder guardar varias versiones del presupuesto (la original, las revisiones, el pronóstico móvil) y comparar cualquiera de ellas contra lo real con los mismos cortes por cuenta y por [centro de costo](centros-de-costo.md), sin atarse a un único ciclo anual. Cómo se guardan esos movimientos está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md).
