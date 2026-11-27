---
resumen: >-
  Lo que la Argentina le agrega a comprar: verificar la condición fiscal del proveedor y que no esté en la base de facturas apócrifas, saber qué factura tiene que mandar según esa condición, constatar el CAE de la que llega y, si el proveedor es una pyme y la empresa es grande, aceptar o rechazar su factura de crédito electrónica antes de que venza el plazo.
estado: borrador
estabilidad: volatil
fuentes:
  - "RG ARCA 5762/2025, Boletín Oficial 25/9/2025, aviso 331947 (PDF leído entero): https://www.boletinoficial.gob.ar/pdf/aviso/primera/331947/20250925"
  - "Resolución 219/2025 de la Secretaría de la Pequeña y Mediana Empresa, B.O. 28/10/2025: https://www.argentina.gob.ar/normativa/nacional/norma-419339/texto"
  - "argentina.gob.ar, Régimen de Factura de Crédito Electrónica MiPyMEs (FCEM), sin fecha, leída 2026-11-27: https://www.argentina.gob.ar/servicio/emitir-una-factura-de-credito-electronica-mipyme"
  - "ARCA, preguntas frecuentes del receptor de la factura de crédito electrónica: https://servicioscf.afip.gob.ar/facturadecreditoelectronica/preguntasFrecuentes/receptor-factura.asp"
  - "Tributum, sobre la Res. 424/2026 SICyP (B.O. 29/10/2026): https://tributum.news/res-424-2026-sicyp-factura-de-credito-electronica-mipymes-plazos-de-aceptacion-cancelacion-y-rechazo-prorroga-hasta-octubre-2027/ (según su resumen)"
  - "iProfesional, extienden un plazo de la factura de crédito hasta 2027: https://www.iprofesional.com/economia/467929-pymes-y-facturas-de-credito-electronicas-extienden-un-plazo-clave-hasta-2027 (según el resumen del buscador)"
  - "ST Abogados, factura de crédito electrónica MiPyME impaga: https://stabogados.com.ar/civil/empresas/cobro-de-deudas/factura-de-credito-electronica-mipyme/"
  - "ARCA, Constatación de comprobantes con CAE: https://servicioscf.afip.gob.ar/publico/comprobantes/cae.aspx"
  - "ARCA, consulta de facturas apócrifas: https://servicioscf.afip.gob.ar/Facturacion/facturasApocrifas/default.aspx"
  - "ARCA, Sistema Registral, constancia de inscripción (solo el título de la página): https://seti.afip.gob.ar/padron-puc-constancia-internet/ConsultaConstanciaAction.do"
  - "iProfesional, Empresas en factura M o base apócrifa, 5/11/2024: https://www.iprofesional.com/impuestos/416546-arca-ex-afip-empresas-en-factura-m-o-base-apocrifa"
  - "iProfesional, fallo Padic S.A. (TFN, Sala C), 27/5/2026: https://www.iprofesional.com/impuestos/455765-facturas-apocrifas-fallo-rechazo-reclamo-arca-proveedores-base-apoc"
  - "El Cronista, fallo CHS de Argentina SA c/ AFIP-DGI (CNCAF, Sala II), 26/7/2025: https://www.cronista.com/columnistas/facturas-apocrifas-fallo-clave-limita-responsabilidad-de-clientes-por-incumplimientos-de-sus-proveedores"
  - "BAE Negocios, consulta de facturas apócrifas en ARCA, 21/9/2025: https://www.baenegocios.com/economia/consultas-de-facturas-apocrifas-en-arca-20250921-0049.html"
  - "Compras-y-abastecimiento/.investigacion/argentina.md (2026-11-27)"
aliases: [factura de compra, factura del proveedor, factura recibida, base APOC, facturas apócrifas, contribuyentes no confiables, constatación de comprobantes, constatar CAE, A con leyenda, operación sujeta a retención, pago en CBU informada, factura M, factura de crédito electrónica, FCE MiPyME, FCEM, Ley 27.440, RG 5762, constancia de inscripción del proveedor]
creado: 2026-11-27
revisado:
---

# Compras y abastecimiento en la Argentina

Lo que la Argentina le agrega a comprar: verificar la condición fiscal del proveedor y que no esté en la base de facturas apócrifas, saber qué factura tiene que mandar según esa condición, constatar el CAE de la que llega y, si el proveedor es una pyme y la empresa es grande, aceptar o rechazar su factura de crédito electrónica antes de que venza el plazo.

Es ley y dinero, y cambia seguido: la nota es una copia al 27 de noviembre de 2026. La RG 5762/2025 y la Res. 219/2025 se leyeron enteras; el resto, por páginas oficiales, notas de prensa o resúmenes, y se dice en cada caso. No reemplaza a un contador ni a un abogado. Lo general del tema está en [Compras y abastecimiento](compras-y-abastecimiento.md); la factura electrónica en sí (letras, CAE, web services), en [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md), y el remito que acompaña la mercadería, en [Inventario y depósitos en la Argentina](../Inventario-y-depositos/inventario-y-depositos-en-argentina.md).

## Qué se verifica del proveedor al darlo de alta

El [alta de proveedor](Proveedores/alta-de-proveedor.md) en la Argentina suma tres consultas públicas de ARCA, todas por CUIT.

- **Constancia de inscripción.** ARCA tiene una consulta pública («Sistema Registral - Internet») que da la condición del contribuyente. Qué datos devuelve no se pudo leer. La condición frente al IVA del proveedor es la que decide qué factura tiene que mandar (ver abajo).
- **Estado de la CUIT.** La RG 5762 usa como condición tener la CUIT «con estado administrativo activo sin limitaciones, en los términos de la Resolución General N° 3.832» (art. 2). Eso muestra que una CUIT puede estar limitada; la RG 3832 no se pudo abrir, así que qué limita y dónde se consulta queda sin fuente.
- **Base de facturas apócrifas.** La consulta de ARCA pide la CUIT y devuelve, si el contribuyente está incluido, la fecha de publicación, la fecha de su condición de apócrifo y una descripción. La página dice que los datos «son meramente informativos» y «cumplen una función preventiva», y no cita norma. Es una sola fuente primaria.

Qué pasa si se le compra a alguien de esa base sale de una sola nota de un abogado: ARCA «no reconoce los créditos fiscales de las operaciones con el contribuyente incluido». Dos fallos leídos por prensa matizan la consecuencia. En Padic S.A. (Tribunal Fiscal, Sala C), la inclusión del proveedor fue posterior a las facturas y no se aplicó hacia atrás. En CHS de Argentina SA (Cámara Contencioso Administrativo Federal, Sala II), el tribunal dijo que «El Fisco no puede trasladar su responsabilidad de control a un tercero».

En los dos casos el tribunal valoró lo que la empresa podía probar: que verificó los comprobantes en la web de ARCA, consultó la base de apócrifas, registró la operación, practicó las retenciones y pagó por medios bancarios. De ahí sale un criterio de la base: consultar la base al dar de alta y antes de cada compra relevante, y guardar la constancia con su fecha, porque la diligencia se prueba con registros.

## Qué factura tiene que mandar el proveedor

La letra del comprobante depende de la condición de quien vende y de quien compra. La tabla de ARCA está en [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md). Leída desde quien compra, con la empresa responsable inscripta: un proveedor responsable inscripto le factura A; uno monotributista o exento, C. Que la C no deje computar crédito fiscal es lectura de la base sobre esa tabla, no un texto leído; el crédito fiscal es del tema Impuestos, todavía no armado. Desde el 1 de noviembre de 2026 los monotributistas facturan todos en forma electrónica (RG 5893/2026, en la misma nota), así que también sus facturas C llegan con CAE.

La factura M ya no existe. Desde el 1 de diciembre de 2025 (art. 32 de la RG 5762) la reemplaza la clase A con la leyenda «OPERACIÓN SUJETA A RETENCIÓN», y toda referencia a la M en otras normas se entiende hecha a ella (art. 31). Las M impresas «podrán utilizarse hasta los plazos de validez otorgados» (art. 27). Para el comprador, esta A no es una A común:

- El inscripto en IVA que la recibe «deberá actuar como agente de retención de los impuestos al valor agregado y a las ganancias» (art. 12).
- Retiene «el CIEN POR CIENTO (100%) de la alícuota que corresponda» de IVA y el 6% de Ganancias, sobre el importe que fija la ley del impuesto (art. 13), «en el momento en que se efectúe el pago», señas y anticipos incluidos (art. 14). Si el régimen general de la RG 830 da más, se aplica el mayor (art. 12).
- El proveedor no puede oponer certificados de exclusión de Ganancias ni de IVA (art. 19).
- Si no retiene, el comprador es responsable personal y solidario por el impuesto que omitió retener, más sanciones (art. 29).

La condición no es fija. ARCA evalúa a cada emisor en febrero, junio y octubre con la información del cuatrimestre vencido y publica las novedades en una consulta del micrositio «Facturación» (arts. 23 a 25). Un proveedor que hoy factura A común puede pasar a A con leyenda en cuatro meses. Esa consulta no se encontró por su nombre.

La misma RG regula otra leyenda, «PAGO EN CBU INFORMADA». Si el proveedor la usa, el comprador inscripto tiene que pagar lo facturado menos las retenciones por transferencia o depósito a la CBU que el vendedor informó a ARCA, consultable en el micrositio «Facturación» (art. 22). Es la única consulta de CBU con base normativa que apareció, y vale solo para quien optó por esa leyenda.

## Qué se controla cuando llega la factura

La factura electrónica sin CAE no produce efectos frente a terceros (art. 12 de la RG 4291, citada en la nota de factura electrónica). ARCA tiene una consulta pública de constatación que pide la CUIT del emisor, el CAE de 14 dígitos, la fecha, el tipo de comprobante (código 1 para la A, 6 para la B), el punto de venta y el número, el importe total y el documento del receptor (código 80 para CUIT). Que el QR de la factura lleve a esa constatación lo dice una sola fuente secundaria.

Después de la constatación viene el cruce con la orden y la recepción. La cantidad recibida se compara con la orden en [recepción contra lo pedido](Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md); el cruce de la factura con las dos, y la deuda que nace, en [compras y cuentas a pagar](../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md). El remito del proveedor no es la factura y no reemplaza ninguno de esos pasos.

## La factura de crédito electrónica MiPyME, del lado del que compra

Con la Ley 27.440, una pyme le emite factura de crédito electrónica a una empresa grande o a otra pyme adherida, y esa factura puede convertirse en título ejecutivo. Según la página oficial, la obligación rige cuando el total es «igual o superior a» $ 5.549.862, desde el 14 de abril de 2026. Es una sola fuente oficial, y una nota de prensa de 2026 daba otro monto que parece viejo. El texto de la ley no se leyó: todo llega por las resoluciones y las páginas oficiales.

El reloj corre desde que la factura llega al domicilio fiscal electrónico de la empresa, no desde que alguien la ve. Según las preguntas frecuentes de ARCA, el comprador tiene que, dentro de ese plazo, aceptarla o informar que la canceló, en el Registro de Facturas de Crédito Electrónicas MiPyME con clave fiscal o por web service. Al aceptar informa «un banco pagador y su respectiva cuenta de origen (CBU)». Si no hace nada, la factura queda «aceptada tácitamente».

| Período | Plazo para aceptar, cancelar o rechazar | Fuente |
|---|---|---|
| 1/11/2025 al 31/10/2026 | «VEINTIÚN (21) días corridos» | Res. 219/2025, leída |
| 1/11/2026 al 31/10/2027 | 21 días corridos, prorrogados | Res. 424/2026 SICyP, no leída: página oficial y dos notas de prensa |

La ley fija 30 días corridos; las resoluciones los acortaron. Según un estudio jurídico, que cita la RG 4367/2018 sin que se haya leído, la factura se considera recibida a las 24 horas del día siguiente a quedar en el domicilio fiscal electrónico.

Rechazar solo se puede dentro del plazo y por una causal del art. 8 de la ley. Según el mismo estudio, son daños en la mercadería, defectos o diferencias comprobados, divergencias de plazo o precio, falta de correspondencia con lo contratado, vicios formales y falta de entrega o prestación. Para rechazar por diferencias o falta de entrega, la empresa necesita el registro de lo que recibió, y lo necesita antes de que venza el plazo. Es inferencia de la base: en una empresa grande, el domicilio fiscal electrónico tiene que tener un responsable, y el cruce con la recepción tiene que caber en 21 días.

## Qué datos fiscales guarda la ficha del proveedor

Lo que el comprador hace con ellos (retener, computar el crédito, pagar) es de los temas Impuestos y Tesorería, todavía no armados. Acá va solo qué guardar, como lectura de la base sobre las normas citadas en la RG 5762, no de un texto que los enumere:

- CUIT y condición frente al IVA y a Ganancias.
- Si factura A con leyenda «OPERACIÓN SUJETA A RETENCIÓN», con la fecha en que se verificó: cambia el cálculo de la retención y anula los certificados de exclusión.
- Certificados de exclusión vigentes, con su vencimiento.
- Si optó por «PAGO EN CBU INFORMADA» y cuál es la CBU.
- La fecha y el resultado de la última consulta a la base de apócrifas.

Por eso la condición fiscal es un dato que se revisa, no un papel del alta: puede cambiar tres veces por año.

> [!NOTE] Sin fuente todavía: qué devuelve la constancia de inscripción y si muestra las limitaciones de la CUIT; el texto de la RG 3832; el nombre y la dirección de la consulta de proveedores con A con leyenda; el web service de constatación de comprobantes; el texto de la Ley 27.440 y de la Res. 424/2026; el criterio para ser «empresa grande» a efectos de la factura de crédito; las sentencias de Padic y CHS leídas enteras; los regímenes de retención de Ganancias (RG 830) e IVA, y los de Ingresos Brutos de cada provincia.
