---
resumen: >-
  La realización es la parte del valor del trabajo hecho, a tarifa de lista, que la firma termina facturando y cobrando. Se pierde en tres puntos del registro: cuando se fija una tarifa menor que la de lista, cuando se castigan horas en el borrador de la factura y cuando el cliente no paga lo facturado.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage a proforma invoice (tipos cobrable, no cobrable y de cortesía; qué se edita en el borrador): https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/manage-proforma-invoice"
  - "Microsoft Learn, Dynamics 365 Project Operations, Revise project invoices (la factura confirmada se corrige con crédito): https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/revise-project-invoices"
  - "Microsoft Learn, Dynamics 365 Project Operations, Sales price resolution (la tarifa sale de una lista de precios por rol): https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/pricing-costing/sales-price-resolution-sales"
  - "Servicios-profesionales-y-proyectos/.investigacion/metricas-fundamentos-y-contraria.md (sección «Realización, tarifa efectiva, lockup»: sin fuente leída)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md"
aliases: [realización, realization, realization rate, tasa de realización, realización de facturación, billing realization, realización de cobro, collection realization, castigo, write-down, write-off, tarifa efectiva, effective rate, lockup]
creado: 2026-11-27
revisado:
---

# Realización

La realización es la parte del valor del trabajo hecho, a tarifa de lista, que la firma termina facturando y cobrando. Se pierde en tres puntos del registro: cuando se fija una tarifa menor que la de lista, cuando se castigan horas en el borrador de la factura y cuando el cliente no paga lo facturado.

> [!NOTE] Sin fuente todavía: ninguna definición de realización, tarifa efectiva ni lockup se leyó en una fuente. Las de esta nota son criterio de esta base, armadas con el vocabulario de los estudios jurídicos y contables, y no llevan cifras de referencia. Las fuentes a leer son el Law Firm Financial Index de Thomson Reuters Institute, el Legal Trends Report de Clio y lo que publica la ABA (American Bar Association) sobre gestión de estudios.

La [utilización](utilizacion.md) dice cuántas horas facturables se trabajaron; la realización dice cuánto de su valor llegó a la caja. Juntas explican por qué una firma ocupada puede ganar poco, que es la pregunta de la [rentabilidad de la firma](rentabilidad-de-la-firma.md). Como recoge la [economía de una firma de servicios](../../Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md#la-ecuación-de-la-rentabilidad-por-socio), una versión de la ecuación de Maister vista en una nota de prensa suma la realización como un factor más, junto a la tarifa y la utilización.

## Las definiciones que usa esta base

Todas son cocientes sobre el valor estándar: las horas trabajadas multiplicadas por la tarifa de lista de cada una.

| Medida | Cuenta | Qué pierde |
|---|---|---|
| Realización de facturación | Lo facturado / el valor estándar de las horas | Descuentos de tarifa y horas castigadas antes de facturar |
| Realización de cobro | Lo cobrado / lo facturado | Notas de crédito e incobrables |
| Realización total | Lo cobrado / el valor estándar | Las dos cosas |
| Tarifa efectiva | Lo cobrado / las horas trabajadas | Lo mismo, expresado en plata por hora |

Como en la utilización, lo que entra en el denominador decide el número. Si las horas que se van a castigar ni se cargan, la realización sale alta y el problema se muda a la [calidad del registro](../Registro-de-horas/calidad-del-registro.md).

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

El lockup es cuánto tarda la firma en convertir el trabajo en plata: los días de [trabajo en curso](../Facturacion-del-proyecto/trabajo-en-curso.md) sin facturar más los días de cuentas a cobrar. En esta base se define así, sin fuente, y el informe de investigación avisa que hay variantes según quién lo publica. No mide cuánto se pierde, como la realización, sino cuánto se demora; los dos suelen ir juntos, porque lo que tarda mucho en facturarse es lo que más se castiga (lectura de esta base, sin evidencia).

## Cómo falla la medida

La realización no dice de quién es la pérdida. Una hora castigada puede ser un error de quien trabajó, una mala estimación de quien vendió o un descuento comercial decidido a propósito. Como criterio de esta base, conviene que el castigo lleve un motivo en el registro, para poder separar después la pérdida por precio, la pérdida por trabajo de más y la pérdida por cliente que no paga.
