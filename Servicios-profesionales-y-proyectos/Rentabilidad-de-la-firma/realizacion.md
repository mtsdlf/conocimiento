---
resumen: >-
  La realización es la parte del valor del trabajo hecho, a tarifa de lista, que la firma termina facturando y cobrando. Se pierde en tres puntos del registro: cuando se fija una tarifa menor que la de lista, cuando se castigan horas en el borrador de la factura y cuando el cliente no paga lo facturado.
estado: vigente
estabilidad: semi
fuentes:
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage a proforma invoice (tipos cobrable, no cobrable y de cortesía; qué se edita en el borrador): https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/manage-proforma-invoice"
  - "Microsoft Learn, Dynamics 365 Project Operations, Revise project invoices (la factura confirmada se corrige con crédito): https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/revise-project-invoices"
  - "Microsoft Learn, Dynamics 365 Project Operations, Sales price resolution (la tarifa sale de una lista de precios por rol): https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/pricing-costing/sales-price-resolution-sales"
  - "Thomson Reuters Institute, Law Firm Rates Report 2027 (tarifa de lista y tarifa pactada con definición; realización de facturación y de cobro del segundo trimestre de 2026; datos de 184 estudios de Estados Unidos): https://www.thomsonreuters.com/en/institute/reports/law-firm-rates-report-2027"
  - "Kreston Reeves, Lock-up management in legal firms (2026): https://www.krestonreeves.com/news/lock-up-management-legal-firms/"
  - "Thomson Reuters Institute, Q2 2026 LFFI analysis (se leyó y no define realización ni lockup): https://www.thomsonreuters.com/en/institute/articles/q2-2026-lffi-analysis-law-firm-leverage"
  - "ABA Commission on Billable Hours Report 2001-2002 (agosto de 2002; leído entero en la copia del Inns of Court): https://inns.innsofcourt.org/media/44347/march_10_2009_program_materials.pdf"
  - "Servicios-profesionales-y-proyectos/.investigacion/metricas-fundamentos-y-contraria.md (sección «Realización, tarifa efectiva, lockup»: sin fuente leída en esa pasada)"
  - "Servicios-profesionales-y-proyectos/.investigacion/verificacion-rentabilidad-y-fundamentos.md"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md"
aliases: [realización, realization, realization rate, tasa de realización, realización de facturación, billing realization, realización de cobro, collection realization, castigo, write-down, write-off, tarifa efectiva, effective rate, lockup]
creado: 2026-11-27
revisado: 2026-11-27
---

# Realización

La realización es la parte del valor del trabajo hecho, a tarifa de lista, que la firma termina facturando y cobrando. Se pierde en tres puntos del registro: cuando se fija una tarifa menor que la de lista, cuando se castigan horas en el borrador de la factura y cuando el cliente no paga lo facturado.

> [!NOTE] Sin fuente todavía: una definición con autoridad de la tarifa efectiva; el lockup tiene una sola fuente, de práctica británica (ver más abajo). Se leyó el informe de tarifas 2027 y el análisis del índice financiero del segundo trimestre de 2026 del Thomson Reuters Institute, y el informe de 2002 de la comisión de la ABA sobre la hora facturable: ninguno las define. El informe anual de un proveedor de software para estudios, el de AICPA y el de la Law Society no se pudieron abrir. Las definiciones de la tabla de abajo son criterio de esta base, armadas con el vocabulario de los estudios jurídicos y contables; las fuentes leídas las apoyan solo en parte, como dice la sección que sigue.

La [utilización](utilizacion.md) dice cuántas horas facturables se trabajaron; la realización dice cuánto de su valor llegó a la caja. Juntas explican por qué una firma ocupada puede ganar poco, que es la pregunta de la [rentabilidad de la firma](rentabilidad-de-la-firma.md). Como recoge la [economía de una firma de servicios](../../Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md#la-ecuación-de-la-rentabilidad-por-socio), una versión de la ecuación de Maister vista en una nota de prensa suma la realización como un factor más, junto a la tarifa y la utilización.

## Las definiciones que usa esta base

Todas son cocientes sobre el valor estándar: las horas trabajadas multiplicadas por la tarifa de lista de cada una. Ese denominador es una elección de esta base, y las fuentes leídas muestran que otros la toman distinta (sección «Qué dicen las fuentes leídas»).

| Medida | Cuenta | Qué pierde |
|---|---|---|
| Realización de facturación | Lo facturado / el valor estándar de las horas | Descuentos de tarifa y horas castigadas antes de facturar |
| Realización de cobro | Lo cobrado / lo facturado | Notas de crédito e incobrables |
| Realización total | Lo cobrado / el valor estándar | Las dos cosas |
| Tarifa efectiva | Lo cobrado / las horas trabajadas | Lo mismo, expresado en plata por hora |

Como en la utilización, lo que entra en el denominador decide el número. Si las horas que se van a castigar ni se cargan, la realización sale alta y el problema se muda a la [calidad del registro](../Registro-de-horas/calidad-del-registro.md).

## Qué dicen las fuentes leídas

El Thomson Reuters Institute, en su informe de tarifas 2027 (datos de 184 estudios de Estados Unidos: 50 del Am Law 100, 58 del Second Hundred y 76 medianos), define dos tarifas: la **tarifa de lista** (*standard rate*), «book or sticker price» antes de cualquier rebaja, y la **tarifa pactada** (*worked rate*), «the average amount a client and firm have agreed to as the baseline rate for a legal matter», después de los descuentos iniciales y antes de enviar la factura. De la realización dice que mide «how much of a matter's value a firm actually collects against what it originally worked» (la llama *worked-to-collected realization*) y muestra por separado la realización de facturación y la de cobro, sin definir ninguna de las dos. No aclara si el valor de partida es la tarifa de lista o la pactada. Esa diferencia importa: un descuento acordado antes de trabajar baja la realización si el denominador es la tarifa de lista, y no la toca si es la pactada.

Cifras del segundo trimestre de 2026, tal como las publica (realización de facturación / de cobro): Am Law 100, 89,4 % / 86,6 %; Am Law Second Hundred, 93,5 % / 91,4 %; estudios medianos, 94,2 % / 92,4 %. El Am Law 100 perdió cerca de 1,5 puntos de realización en el período que muestra, de 2023 a 2026. Son estudios jurídicos de un solo país, y la fórmula de cada medida no está en el informe.

La comisión de la ABA (2002) usa las mismas palabras de otro modo. Dice que la ecuación de ingresos de un estudio la mueven «rates, hours and realization» (sección «Budget Models»), que los presupuestos se arman con las horas facturables esperadas por la tarifa, menos «an amount for write-offs and uncollectible accounts» (sección «The History of Hourly Billing»), y que solo con horas registradas se puede calcular «realization rate» (sección «Why Billable Hours are So Entrenched»). Coincide con la separación de esta nota entre castigos antes de facturar e incobrables, y no da la fórmula.

## Dónde se pierde en el registro

Cada punto de pérdida es un momento distinto del recorrido de la hora a la plata, y cada uno vive en otra nota del tema:

1. **La tarifa.** El valor estándar sale de una lista de precios. En un sistema de gestión de servicios, la tarifa de una hora se resuelve primero por la lista vigente a la fecha y después por el rol, con excepciones por unidad. Una tarifa pactada con el cliente por debajo de la de lista ya es una pérdida de realización, aunque nadie castigue nada. La tarifa por rol está en [roles y habilidades](../Asignacion-de-personas/roles-y-habilidades.md).
2. **El borrador de la factura.** Es donde la firma decide cuánto cobra de lo que trabajó. En el mismo sistema, cada renglón de tiempo puede cambiar de cantidad, de precio o de tipo: cobrable, no cobrable o de cortesía, y solo lo cobrable suma al total. Pasar una hora a no cobrable es un castigo (*write-down*): la hora sigue costando al proyecto y deja de sumar a la factura. Está en [facturación del proyecto](../Facturacion-del-proyecto/facturacion-del-proyecto.md) y en [facturación por hora](../Facturacion-del-proyecto/facturacion-por-hora.md).
3. **La factura ya emitida.** Una factura confirmada no se edita: se corrige con otra que acredita la original y, si corresponde, vuelve a facturar lo que sigue pendiente. Una nota de crédito baja la realización de cobro.
4. **El cobro.** Lo facturado que el cliente no paga termina como incobrable. El reconocimiento contable y la previsión están en [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md); el cobro en sí es del tema Tesorería y finanzas de la empresa en marcha, que todavía no está escrito.

Los sistemas leídos solo ofrecen esas herramientas: cambiar el tipo, la cantidad o el precio en el borrador, y acreditar una factura. El castigo contable del trabajo en curso que nunca se va a facturar, con su baja a resultados, no aparece en ninguna fuente leída.

Para medir la realización, el registro tiene que guardar las tres cifras de cada hora: el valor a tarifa de lista, lo que se facturó y lo que se cobró. Si el borrador pisa la cantidad o el precio original sin conservarlos, la pérdida se vuelve invisible (criterio de esta base).

## La realización a precio cerrado

En un proyecto a precio cerrado, la realización compara el precio con el valor estándar de las horas que llevó. Puede pasar del 100 %: si el proyecto se terminó con menos horas de las presupuestadas, la firma cobró más que la tarifa de lista por hora. Si se pasó de horas, la realización cae aunque no se haya castigado ninguna hora en la factura (las dos cosas son criterio de esta base). Por eso, en precio cerrado, la realización baja es el mismo síntoma que un [margen del proyecto](costo-y-margen-del-proyecto.md) bajo, visto en horas.

## El lockup

El lockup es cuánto tarda la firma en convertir el trabajo en plata: los días de [trabajo en curso](../Facturacion-del-proyecto/trabajo-en-curso.md) sin facturar más los días de cuentas a cobrar. Así lo define una firma contable británica, «Lock up days = WIP days + Debtor days», con una sola fuente y como práctica de estudios jurídicos del Reino Unido; el detalle está en [trabajo en curso](../Facturacion-del-proyecto/trabajo-en-curso.md). Ni el análisis del índice financiero del Thomson Reuters Institute ni el informe de la ABA lo definen. No mide cuánto se pierde, como la realización, sino cuánto se demora; los dos suelen ir juntos, porque lo que tarda mucho en facturarse es lo que más se castiga (lectura de esta base, sin evidencia).

## Cómo falla la medida

La realización no dice de quién es la pérdida. Una hora castigada puede ser un error de quien trabajó, una mala estimación de quien vendió o un descuento comercial decidido a propósito. Como criterio de esta base, conviene que el castigo lleve un motivo en el registro, para poder separar después la pérdida por precio, la pérdida por trabajo de más y la pérdida por cliente que no paga.
