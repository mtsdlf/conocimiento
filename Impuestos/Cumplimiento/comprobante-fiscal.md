---
resumen: >-
  El comprobante fiscal es el documento que respalda cada operación frente al fisco (la factura, la nota de crédito, la nota de débito): lleva los datos que permiten calcular el impuesto y saber quién lo debe, se numera en forma correlativa y no se borra, y en cada vez más países se emite en formato electrónico, a veces con la validación previa del fisco.
estado: borrador
estabilidad: estable
fuentes:
  - "Directiva 2006/112/CE del Consejo, arts. 219, 220 y 226, texto de 2006 (copia del BOE): https://www.boe.es/doue/2006/347/L00001-00118.pdf"
  - "FMI, Tax Law Design and Drafting, vol. 1 (1996), cap. 4, sección II.D, Returns and Record Keeping (autofactura): https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch4.pdf"
  - "Barreix, A. y Zambrano, R., La Factura Electrónica en América Latina, blog del CIAT, 21/03/2018 (resumen de sus autores del libro BID-CIAT): https://www.ciat.org/la-factura-electronica-en-america-latina/"
  - "World Bank Group y PwC, Paying Taxes 2020, pp. 20-23 y 28-29 (según lo leído de esas secciones): https://archive.doingbusiness.org/content/dam/doingBusiness/pdf/db2020/PayingTaxes2020.pdf"
  - "Comisión Europea, DG TAXUD, VAT in the Digital Age (ViDA): https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en"
  - "Revenue (Irlanda), VAT in the Digital Age (ViDA): https://www.revenue.ie/en/corporate/consultations-and-submissions/modernising-vat/einvoicing/introduction/vida/digital-age-vida.aspx"
  - "Impuestos/.investigacion/cumplimiento.md (2026-11-27)"
aliases: [comprobante fiscal, factura, invoice, VAT invoice, nota de crédito, credit note, nota de débito, debit note, factura rectificativa, numeración correlativa, factura electrónica, e-invoicing, e-invoice, clearance, modelo de despeje, continuous transaction controls, CTC, reporte en tiempo real, real-time reporting, autofactura, self-billing, liquidación de compra, ViDA]
creado: 2026-11-27
revisado:
---

# Comprobante fiscal

El comprobante fiscal es el documento que respalda cada operación frente al fisco (la factura, la nota de crédito, la nota de débito): lleva los datos que permiten calcular el impuesto y saber quién lo debe, se numera en forma correlativa y no se borra, y en cada vez más países se emite en formato electrónico, a veces con la validación previa del fisco.

Es el centro del [cumplimiento](cumplimiento.md): la misma factura da el débito fiscal del vendedor y el crédito fiscal del comprador (ver [IVA](../Impuestos-al-consumo/iva.md)), y el fisco controla a uno con los datos del otro.

## Qué datos lleva una factura

El núcleo de la lista se repite entre países. En la Directiva europea del IVA (texto de 2006), el artículo 226 dice que «solamente serán obligatorias» estas menciones, además de las de casos especiales:

| Dato | Para qué sirve | Art. 226 |
|---|---|---|
| Fecha de expedición | ubica la operación en un período | punto 1 |
| «Un número secuencial, basado en una o varias series, que identifique la factura de forma única» | permite saber si falta alguna | punto 2 |
| Número de identificación fiscal del vendedor y del comprador | dice quién debe el débito y quién toma el crédito | puntos 3 y 4 |
| Nombre y dirección de los dos | identifica a las partes | punto 5 |
| Cantidad y naturaleza de lo vendido | permite ver si la alícuota es la correcta | punto 6 |
| Fecha de la entrega, si es distinta | ubica el hecho imponible | punto 7 |
| «La base de imposición para cada tipo o exoneración, el precio unitario sin el IVA, así como cualquier descuento» | separa la base de cada alícuota | punto 8 |
| La alícuota aplicada y el importe del impuesto | el cálculo | puntos 9 y 10 |
| Si está exenta o la debe el comprador, la norma que lo dice | justifica que no lleve impuesto | punto 11 |

La tabla sigue el texto de 2006, modificado después. La Directiva obliga a facturar las ventas a otros contribuyentes y a personas jurídicas (art. 220); la factura al consumidor final no es obligatoria en ese texto salvo casos especiales.

El contenido de cada renglón depende de quién vende, a quién y qué: ver [hecho imponible y base](../Obligacion-tributaria/hecho-imponible-y-base.md) y [sujetos del impuesto](../Obligacion-tributaria/sujetos-del-impuesto.md). En la Argentina, la letra de la factura (A, B, C, E) codifica esa combinación, como explica [factura electrónica de ARCA](../../Comercio-electronico/Normativa/factura-electronica-de-arca.md).

## Por qué la numeración no puede tener huecos

Cada factura lleva un número correlativo dentro de su serie (en la Argentina, de su punto de venta); la Directiva pide uno «que identifique la factura de forma única» (art. 226). Que la numeración sirva de control, porque con números seguidos una factura faltante se nota y el hueco se lee como una venta no declarada, es inferencia de la base.

La contabilidad usa el mismo mecanismo con los documentos prenumerados, para comprobar que ninguna operación se saltó la aprobación (ver [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md)); acá controla el fisco.

Un sistema asigna el número al emitir y no lo reutiliza. Una factura mal emitida conserva su número y se corrige con otro comprobante (inferencia de la base a partir de la regla).

## La factura no se borra: nota de crédito y nota de débito

Una factura emitida no se edita ni se borra: se corrige con otro comprobante que la cita.

(Los usos que siguen son descripción de la base, sin fuente leída.)

- Nota de crédito: baja el importe de la factura original, total o parcialmente. Sirve para una devolución, un descuento posterior a la venta, un error de precio o la anulación de una factura entera.
- Nota de débito: sube el importe. Sirve para un interés por pago tardío, un gasto trasladado después o un error de precio a favor del vendedor.

La Directiva europea lo dice así: «Se asimilará a una factura cualquier documento o mensaje rectificativo que modifique y haga referencia expresa e inequívoca a la factura inicial» (art. 219). La contabilidad aplica la misma regla: un asiento se compensa con otro en lugar de borrarse (ver [asiento y libros](../../Contabilidad/Registro/asiento-y-libros.md)).

La nota de crédito corrige también el impuesto: baja el débito fiscal de quien la emite y el crédito fiscal de quien la recibe, en el período de la nota. En la Argentina, solo puede emitirla quien emitió la factura original ([factura electrónica de ARCA](../../Comercio-electronico/Normativa/factura-electronica-de-arca.md)); qué cambia en una venta entre empresas está en [factura entre empresas](../../Comercio-electronico/Comercio-B2B/factura-entre-empresas.md).

## El comprobante de quien no factura

Si quien vende no factura (un productor rural, un particular, un prestador del exterior), el comprador no puede tomar el crédito fiscal ni deducir el gasto. Muchos países le permiten emitir el comprobante por cuenta del vendedor: la autofactura (self-billing) o, en varios países de América Latina, la liquidación de compra. La Directiva europea admite que la factura la emita el vendedor, el comprador o, «en su nombre y por su cuenta», un tercero (art. 220), y que la emita el comprador si hay acuerdo previo y la acepta el vendedor (art. 224); el FMI da la razón fiscal: identificar a quien cobró da «valuable information that can be used in auditing the payee».

> [!NOTE] Sin fuente todavía: una fuente comparada sobre la autofactura y la liquidación de compra en América Latina.

## Factura electrónica: de controlar después a controlar en el momento

Según Barreix y Zambrano, autores del libro del BID y el CIAT sobre el tema, las administraciones la introdujeron «como un control documental del proceso de facturación, tanto para evitar omisiones de declaraciones de venta, como para evitar que las empresas declarasen compras falsas».

Hay dos modelos, según cuándo ve el fisco la factura:

| Modelo | Cuándo ve el fisco la factura | Dónde se usa (ejemplos) |
|---|---|---|
| Control posterior (post-audit) | cuando la pide en una inspección, o en un archivo que la empresa entrega por período | el archivo SAF-T «pull» que entrega la empresa a pedido (ver [registros fiscales](registros-fiscales.md)) |
| Control en el momento (clearance o controles continuos de transacciones) | antes de que la factura tenga efecto, o apenas se emite | Chile, México, Brasil, Argentina; en Europa, Italia, España (reporte inmediato) y Hungría |

La asignación de países a cada fila es lectura de la base: los europeos son los que PwC pone en el nivel más alto, y los latinoamericanos, los que Barreix y Zambrano llaman «avanzados y maduros».

En el control en el momento, la factura no vale hasta que el fisco la valida y le da un código, o se informa en tiempo real. *Paying Taxes 2020* lo pone en el nivel III de una escala de cuatro (el IV son tecnologías como blockchain en pilotos), donde «businesses share information on underlying transactions directly with tax authorities». «Post-audit», «clearance» y «continuous transaction controls» son nombres de la práctica del sector; las fuentes leídas hablan de «clearance models» y «real-time reporting».

El informe anota entre los costos que las empresas «may need to adjust their systems to fit with tax administrations' systems». En un sistema de gestión, la factura depende de un servicio del fisco que puede caerse o rechazarla. El caso argentino (el CAE, el web service, la contingencia) está en [factura electrónica de ARCA](../../Comercio-electronico/Normativa/factura-electronica-de-arca.md).

### América Latina fue primero

Según Barreix y Zambrano: «Chile fue pionero en la introducción de la FE en 2003. A mediados de 2017 Argentina, Brasil, Ecuador, México, Perú y Uruguay ya cuentan con esquemas de FE avanzados y maduros». Corea la estableció en 2011. En México, según el Banco Mundial, «all invoices must be issued in a Government-mandated XML format» (según lo leído del informe).

### Europa converge con ViDA

Europa empezó por la factura al Estado (Dinamarca, desde 2005, según los mismos autores) y avanza hacia la factura entre empresas. El paquete «VAT in the Digital Age» (ViDA), adoptado el 11 de marzo de 2025 (Directiva (UE) 2025/516), fija este calendario según la Comisión Europea:

| Desde | Qué cambia |
|---|---|
| 14 de abril de 2025 | cada país puede exigir factura electrónica en las operaciones internas sin pedir autorización a la UE |
| 1 de julio de 2030 | factura electrónica en formato estándar y reporte digital para las ventas entre empresas de distintos países de la UE |
| 1 de enero de 2035 | los países con reporte en tiempo real propio tienen que alinearlo con el modelo europeo |

Según la administración tributaria de Irlanda, desde 2030 la factura intracomunitaria se emite dentro de los 10 días y el reporte reemplaza al resumen periódico del sistema VIES.

Para leer más: *Paying Taxes 2020*, pp. 20-23 (los cuatro niveles) y pp. 28-29 (los sistemas de factura electrónica); y «La factura electrónica en América Latina» (BID y CIAT, 2018), que recorre país por país y no se leyó entero.
