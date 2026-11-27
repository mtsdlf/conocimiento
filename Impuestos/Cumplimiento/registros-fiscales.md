---
resumen: >-
  Los registros fiscales son los libros y archivos que una empresa lleva para que el fisco pueda reconstruir sus impuestos: el libro de IVA ventas y el de IVA compras, comprobante por comprobante, conservados mientras el fisco pueda revisarlos y entregados en el formato que pida, cada período o en una inspección.
estado: borrador
estabilidad: estable
fuentes:
  - "FMI, Tax Law Design and Drafting, vol. 1 (1996), cap. 4, secciones II.D.4 (Record Keeping) y II.E (Audits, acceso a registros de terceros): https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch4.pdf"
  - "Directiva 2006/112/CE del Consejo, arts. 246 y 247, texto de 2006 (copia del BOE): https://www.boe.es/doue/2006/347/L00001-00118.pdf"
  - "World Bank Group y PwC, Paying Taxes 2020, pp. 20-23 (SAF-T push y pull, leído el 2026-11-27): https://archive.doingbusiness.org/content/dam/doingBusiness/pdf/db2020/PayingTaxes2020.pdf"
  - "Skatteetaten (administración tributaria de Noruega), SAF-T Financial: https://www.skatteetaten.no/en/business-and-organisation/start-and-run/best-practices-accounting-and-cash-register-systems/saf-t-financial/"
  - "Wikipedia, SAF-T (leída el 2026-11-27; confirma mayo de 2005 y abril de 2010, pero la guía de la OCDE sigue sin abrirse): https://en.wikipedia.org/wiki/SAF-T"
  - "Impuestos/.investigacion/cumplimiento.md (2026-11-27)"
aliases: [registros fiscales, libros fiscales, libro IVA, libro de IVA ventas, libro de IVA compras, subdiario de IVA, registro de facturas, VAT ledger, sales ledger, purchase ledger, conservación de comprobantes, record keeping, SAF-T, Standard Audit File for Tax, libro digital, información de terceros, third-party information]
creado: 2026-11-27
revisado:
---

# Registros fiscales

Los registros fiscales son los libros y archivos que una empresa lleva para que el fisco pueda reconstruir sus impuestos: el libro de IVA ventas y el de IVA compras, comprobante por comprobante, conservados mientras el fisco pueda revisarlos y entregados en el formato que pida, cada período o en una inspección.

Los registros son el puente del [cumplimiento](cumplimiento.md) entre el [comprobante fiscal](comprobante-fiscal.md) y la [declaración](declaracion-y-pago.md): cada comprobante entra al registro, y la declaración suma el registro. Si el fisco quiere saber de dónde sale un número de la declaración, el registro tiene que mostrarlo.

El FMI recomienda que la ley o el reglamento especifiquen «taxpayers' obligations to keep books of account and other records necessary for determining tax liability». Qué libros pide cada país varía; los de IVA son los que casi todos piden.

## Los libros de IVA ventas y compras

El libro de IVA ventas lista cada comprobante emitido del período; el de IVA compras, cada comprobante recibido. Una fila por comprobante, con los datos que hacen falta para liquidar:

| Columna | Por qué está |
|---|---|
| Fecha y tipo de comprobante (factura, nota de crédito, nota de débito) | ubica la operación en el período y dice si suma o resta |
| Serie y número | permite ver que la numeración no tiene huecos |
| Identificación fiscal y nombre de la contraparte | permite cruzar con lo que declara la otra parte |
| Neto gravado por alícuota, exento y no gravado | separa la base de cada tratamiento |
| Impuesto por alícuota | da el débito o el crédito fiscal |
| Percepciones y otros impuestos del comprobante | se computan aparte |
| Total | cuadra con el comprobante |

La tabla es una síntesis de la base a partir de los datos de una factura (ver [comprobante fiscal](comprobante-fiscal.md)); cada país fija su diseño. El total del libro de ventas es el débito fiscal del período; el del libro de compras, el crédito fiscal. La diferencia es el punto de partida de la [liquidación del IVA](../Impuestos-al-consumo/iva.md).

## Cómo se relaciona con la contabilidad

El libro de IVA y la contabilidad registran los mismos comprobantes con dos propósitos distintos. La contabilidad los anota como asientos de partida doble, en el diario y el mayor (ver [asiento y libros](../../Contabilidad/Registro/asiento-y-libros.md)); el libro de IVA los lista con el detalle que pide el fisco. En la contabilidad, el libro de IVA funciona como un subdiario: el total del período entra al diario en un asiento resumen, con las cuentas de IVA débito fiscal e IVA crédito fiscal (inferencia de la base a partir del régimen de subdiarios; ver [libros contables en Argentina](../../Contabilidad/Registro/libros-contables-en-argentina.md), art. 327 del Código Civil y Comercial).

Por eso los dos tienen que cuadrar: el saldo de la cuenta de IVA débito fiscal del mayor tiene que ser igual al total del libro de IVA ventas. Si no cuadran, falta un comprobante en uno de los dos, o uno se registró en otro período. Es una [conciliación](../../Contabilidad/Control-interno/conciliaciones.md) que conviene hacer antes de cada declaración.

El registro del impuesto en la contabilidad (cuentas y asiento) es del tema [Contabilidad](../../Contabilidad/contabilidad.md); acá interesa qué tiene que poder mostrarle el registro al fisco.

## Cuánto tiempo se guarda

Se guarda mientras el fisco pueda revisar el período, y un poco más. El plazo lo fija cada país; la Directiva europea lo dice así: «Cada Estado miembro determinará el plazo durante el cual los sujetos pasivos deberán velar por que se conserven las facturas» (art. 247). Lo que sí fija para todos es la calidad de lo guardado: «La autenticidad del origen y la integridad del contenido de las facturas conservadas, así como su legibilidad, deberán garantizarse durante todo el período de conservación» (art. 246).

El plazo fiscal se cruza con el comercial y con la [prescripción](fiscalizacion-y-sanciones.md). En la Argentina, el Código Civil y Comercial pide diez años para libros, registros y comprobantes (art. 328, en [libros contables en Argentina](../../Contabilidad/Registro/libros-contables-en-argentina.md)). La regla práctica es guardar por el plazo más largo de los que apliquen (inferencia de la base).

Guardar en formato electrónico es válido en la mayoría de los países, con condiciones. La Directiva permite que cada país exija conservar las facturas «en la forma original, ya sea en papel o electrónica, en la que se hayan transmitido» (art. 247). Una factura electrónica no se guarda imprimiéndola: se guarda el archivo original (lectura de la base de la regla del art. 247).

## Cómo le llegan los datos al fisco

El fisco obtiene los datos de una empresa por tres caminos, de menos a más automático:

| Camino | Cómo funciona | Ejemplo |
|---|---|---|
| A pedido, en una inspección | el inspector pide los libros y los comprobantes | el modelo tradicional; el SAF-T «pull» |
| Por período, en un archivo estándar | la empresa sube cada mes el detalle de sus libros | el SAF-T «push»; los libros de IVA digitales |
| En el momento de cada operación | el fisco ve cada factura cuando se emite | la factura electrónica con control previo (ver [comprobante fiscal](comprobante-fiscal.md)) |

### El SAF-T de la OCDE

El SAF-T (Standard Audit File for Tax) es un formato estándar para que un sistema contable exporte sus datos al fisco o a un auditor. Lo propuso la OCDE: la primera versión es de mayo de 2005 y la 2.0, de abril de 2010 (según Wikipedia; la guía de la OCDE no se pudo abrir). Contiene el mayor con el plan de cuentas, los datos de clientes y proveedores y el detalle de facturas, pagos y ajustes; la versión 2.0 suma inventario y activos fijos. La OCDE no impone el formato del archivo.

PwC, en *Paying Taxes 2020*, distingue dos formas de usarlo. En el modelo «pull», la empresa lo entrega cuando el fisco lo pide; en el «push», lo envía cada período. Según el informe, estos archivos llevan información «that goes beyond pure transactional and invoice information» y permiten al fisco hacer auditorías electrónicas sobre datos estructurados. Polonia, por ejemplo, reemplaza la declaración de IVA por los datos del SAF-T.

Noruega es un caso del modelo «pull». Desde los ejercicios que empiezan el 1 de enero de 2020, las empresas con contabilidad digital tienen que poder exportarla en SAF-T, con una exención para las que facturan menos de NOK 5 millones; y la entregan solo «in the event of an audit».

### La información de terceros

El fisco no depende solo de lo que declara la empresa. Recibe información de bancos, de clientes y proveedores (que declaran sus compras y ventas), de los agentes de retención y percepción, y de la otra parte de cada factura electrónica. El FMI recomienda que la administración tenga acceso a los registros de cualquiera que tenga información financiera relevante. Con esa información el fisco puede armar declaraciones prellenadas (*Paying Taxes* cita esa práctica) y detecta diferencias (ver [fiscalización y sanciones](fiscalizacion-y-sanciones.md)).

Los libros de la empresa se comparan con los de los demás: una compra que la empresa registró y su proveedor no declaró como venta, o al revés, aparece en un cruce.

## Qué tiene que poder emitir un sistema

Un sistema de gestión tiene que poder producir para el cumplimiento (inferencia de la base; ninguna fuente leída lo enumera):

1. El libro de IVA ventas y el de IVA compras de cualquier período, con el detalle por alícuota, en el formato que pida el fisco.
2. Los comprobantes originales, en su formato electrónico, durante todo el plazo de conservación, sin poder editarlos.
3. La conciliación entre el libro de IVA y las cuentas de IVA de la contabilidad.
4. El detalle de retenciones y percepciones sufridas y practicadas, con sus certificados (ver [pagos a cuenta](../Recaudacion-en-la-fuente/pagos-a-cuenta.md) y [agente de recaudación](../Recaudacion-en-la-fuente/agente-de-recaudacion.md)).
5. Una exportación de la contabilidad en el formato estándar del país, si lo hay.
6. El rastro de cada cambio: quién emitió, anuló o corrigió cada comprobante y cuándo (ver [controles sobre sistemas](../../Contabilidad/Control-interno/controles-sobre-sistemas.md)).

Cómo se modela eso en un sistema es del tema Software de gestión (todavía no escrito). El caso argentino está en [IVA en Argentina](../Impuestos-al-consumo/iva-en-argentina.md).

Para leer más: la guía de la OCDE «Guidance on the Standard Audit File – Tax, Version 2.0» (2010), por la lista de datos que el fisco espera de un sistema contable; y la página SAF-T Financial de la administración noruega, como caso de implementación.
