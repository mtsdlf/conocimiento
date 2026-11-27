---
resumen: >-
  Un agente de recaudación es la persona o empresa que la ley o el fisco designan para retener o percibir un impuesto de terceros en cada pago o cobro, depositarlo e informarlo; si no lo hace, responde por ese impuesto con su propio patrimonio.
estado: vigente
estabilidad: estable
fuentes:
  - "IMF, Tax Law Design and Drafting, vol. 2, cap. 14 «Individual Income Tax» (Burns y Krever, 1998), sección de terminología: https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch14.pdf"
  - "Ley 11.683 de Procedimiento Tributario (t.o. 1998), arts. 6, 8 y 48, como ejemplo de un país: https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/18771/texact.htm"
  - "Impuestos/.investigacion/recaudacion-en-la-fuente.md (2026-11-27)"
aliases: [agente de retención, agente de percepción, agente de recaudación, withholding agent, collection agent, responsable sustituto, designación como agente]
creado: 2026-11-27
revisado: 2026-11-27
---

# Agente de recaudación

Un agente de recaudación es la persona o empresa que la ley o el fisco designan para retener o percibir un impuesto de terceros en cada pago o cobro, depositarlo e informarlo; si no lo hace, responde por ese impuesto con su propio patrimonio.

Es una de las caras de la [recaudación en la fuente](recaudacion-en-la-fuente.md); la otra, la de quien la sufre, está en [pagos a cuenta](pagos-a-cuenta.md). Entre los [sujetos del impuesto](../Obligacion-tributaria/sujetos-del-impuesto.md), el agente no es contribuyente: es un responsable por deuda ajena. El FMI recomienda que la ley lo nombre así, como «withholding agent», y no como *taxpayer*.

## Cómo una empresa llega a ser agente

Nadie se ofrece a ser agente: se lo designan. Las formas habituales son tres, y un mismo país suele usar varias a la vez (esta clasificación y los ejemplos son inferencia de esta base; ninguna fuente leída la hace, salvo el caso argentino de la nómina y de los bancos).

| Cómo se designa | Ejemplo |
|---|---|
| Por la ley, a todo el que hace cierto pago | todo empleador retiene el impuesto a la renta de sus empleados |
| Por características objetivas: tamaño, actividad, tipo de entidad | los bancos retienen sobre las acreditaciones en cuenta; los organismos públicos retienen IVA a sus proveedores |
| Por nómina: el fisco notifica a cada empresa y publica la lista | las empresas de una lista que el fisco notifica y publica |

Una empresa puede pasar a ser agente por una notificación, con una fecha desde la que tiene que empezar a retener. Ser agente de un impuesto no la hace agente de otro, y puede serlo de retención y no de percepción, o al revés. Cómo funciona en la Argentina está en [retenciones y percepciones en Argentina](retenciones-y-percepciones-en-argentina.md).

## Lo que hace el agente en cada operación

Cada pago (si retiene) o cada cobro (si percibe) pasa por los mismos pasos:

1. Ver si la operación está alcanzada. Cada régimen dice qué conceptos entran (compras de bienes, servicios, alquileres, honorarios) y cuáles no.
2. Ver la condición de la contraparte. El agente consulta cómo está inscripta la otra parte, en qué categoría la puso el fisco, si figura en un padrón con alícuota propia y si tiene un certificado de exclusión o de reducción vigente. En Argentina, si el beneficiario no entrega la constancia de inscripción en Ganancias, el agente lo trata como no inscripto (RG 830, art. 22), y en IVA se retiene el 100 % según la categoría del proveedor (RG 2854, art. 9); que sea una regla general de todos los regímenes no está en las fuentes.
3. Calcular. La base la fija el régimen (el monto bruto, el neto sin impuestos o el impuesto mismo de la factura), y se le aplica la alícuota que corresponde. Si el régimen tiene un mínimo no sujeto, debajo de ese importe no se retiene, o se retiene solo sobre el excedente, según cómo esté escrito.
4. Retener o percibir. En la retención, el agente paga menos. En la percepción, suma el importe a la factura, detallado aparte.
5. Documentar. En la retención, el agente le entrega al retenido un certificado con los datos de los dos, el impuesto, el régimen, el comprobante que originó la retención, el importe y la fecha. En la percepción, en Argentina el comprobante puede ser la documentación habitual del agente si trae los datos exigidos (RG 2233, art. 8, inc. b).

Y después, en cada período:

6. Depositar lo recaudado en el plazo del régimen, que suele ser más corto que el de los impuestos propios (quincenal o decenal, no mensual).
7. Informar al fisco, una por una, las retenciones o percepciones del período, con el número de identificación tributaria de cada sujeto. Así el fisco cruza lo que el agente informó contra lo que el retenido computa.

## Por qué una retención no hecha se vuelve deuda propia

El agente responde por lo que no retuvo y por lo que retuvo y no depositó. En Argentina la ley lo hace responder con sus propios bienes (art. 8 de la Ley 11.683, abajo); que otros países lo hagan igual no se verificó.

El ejemplo argentino: la Ley 11.683 pone a los agentes entre los responsables por deuda ajena (art. 6) y los hace responder con sus bienes propios «por el tributo que omitieron retener, una vez vencido el plazo de quince (15) días» si no prueban que el contribuyente lo pagó (art. 8). Lo retenido y no depositado es más grave: el artículo 48 lo pena con una multa «de dos (2) hasta seis (6) veces el tributo retenido o percibido». Las cifras salen del texto de la ley en InfoLEG, leído el 2026-11-27.

La asimetría pesa en el diseño del proceso. Retener de más genera un reclamo del proveedor; retener de menos, una deuda de la empresa con el fisco. Por eso, ante la duda, el agente tendería a aplicar la alícuota más alta (inferencia de esta base, sin fuente).

## Datos que tiene que guardar un sistema

Un agente que procesa cientos de pagos no puede consultar a mano cada contraparte. Sin importar la herramienta, tiene que guardar lo siguiente:

| Dato | Por qué |
|---|---|
| De qué regímenes es agente la empresa, y desde cuándo | la designación tiene fecha de inicio y a veces de fin |
| Por contraparte: su condición frente a cada impuesto y su jurisdicción | decide si se retiene y con qué alícuota |
| Por contraparte: la alícuota del padrón, con el período al que corresponde | los padrones se publican cada mes y cambian |
| Por contraparte: los certificados de exclusión o reducción, con su vigencia | vencen y hay que verificarlos en la fuente oficial |
| Por régimen: conceptos alcanzados, base, alícuotas y mínimos, con vigencia | el fisco los modifica por resolución |
| Por operación: la base, la alícuota aplicada, el importe y el comprobante que la originó | es lo que va al certificado y a la declaración informativa |
| La numeración de los certificados emitidos | suele exigirse correlativa |
| El acumulado por contraparte y por período, si el régimen lo pide | algunos regímenes calculan el mínimo o la escala sobre lo pagado en el mes |

El modelo de datos de un software es del tema Software de gestión (todavía no escrito). Lo retenido se registra como deuda con el fisco hasta depositarlo; el asiento es de [Contabilidad](../../Contabilidad/contabilidad.md).

## Cómo falla

> [!NOTE] Esta lista y la tabla de arriba sobre qué guardar son inferencia de esta base sobre cómo opera un agente; ninguna fuente leída las enumera.

- Padrón viejo. Se aplica la alícuota del mes anterior. El error se descubre cuando el proveedor reclama o cuando el fisco cruza.
- Certificado de exclusión no verificado. Se deja de retener a alguien cuyo certificado venció. La deuda es del agente.
- Retención sobre la base equivocada, por ejemplo sobre el total con impuestos cuando el régimen dice sobre el neto.
- Lo retenido se usa como caja. La plata retenida está en la cuenta de la empresa, pero no es suya. En Argentina, mantener lo retenido después del vencimiento tiene multa de dos a seis veces el tributo (art. 48).
- Lo informado no coincide con lo emitido. Si el certificado dice una cosa y la declaración informativa otra, el retenido no puede computarlo y reclama.

Ver también: [cumplimiento](../Cumplimiento/cumplimiento.md), donde la declaración del agente entra en el calendario del mes.
