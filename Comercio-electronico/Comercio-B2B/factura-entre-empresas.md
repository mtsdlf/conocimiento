---
resumen: >-
  En Argentina, una venta entre empresas se documenta con una factura que discrimina el IVA para que el comprador lo descuente, suma las percepciones que el vendedor esté obligado a cobrar y, cuando una pyme le vende a una empresa grande por encima de un monto, tiene que ser una factura de crédito electrónica que se acepta y se puede negociar. Lo que en una tienda al público es un comprobante, acá es parte del precio y del cobro.
estado: borrador
estabilidad: volatil
fuentes:
  - "Argentina.gob.ar, Emitir una Factura de Crédito Electrónica MiPyME: https://www.argentina.gob.ar/servicio/emitir-una-factura-de-credito-electronica-mipyme (leído)"
  - "iProfesional, prórroga del plazo de aceptación de la FCE (2/11/2026), citando la Resolución 424/2026: https://www.iprofesional.com/economia/467929-pymes-y-facturas-de-credito-electronicas-extienden-un-plazo-clave-hasta-2027.amp (leído)"
  - "ARCA, Régimen de Transparencia Fiscal al Consumidor: https://servicioscf.afip.gob.ar/publico/sitio/contenido/novedad/ver.aspx?id=4709 (leído)"
  - "iProfesional, IVA en facturas, claves del régimen (29/3/2025): https://www.iprofesional.com/impuestos/425337-iva-en-facturas-las-claves-del-regimen-que-entra-en-plena-vigencia-el-proximo-martes (leído)"
  - "Resolución General AFIP 2408/2008, texto original: https://www.argentina.gob.ar/normativa/nacional/norma-137452/texto (leído; vigencia actual no confirmada)"
  - "Develop Argentina, RG 2408, qué es y cómo calcular la percepción de IVA: https://www.developargentina.com/blog/rg-2408-que-es-como-calcular-percepcion-iva-2026 (leído; proveedor de software)"
  - "INDEC, Encuesta de autoservicios mayoristas, agosto de 2026, cuadro 8: https://www.indec.gob.ar/uploads/informesdeprensa/autoservicios_mayoristas_10_26AFB69B25A5.pdf (leído)"
  - "Rojo y otros, Estructura y dinámica reciente de las mipymes empleadoras, CEP XXI y SEPYME (2022), sección 1, tramos del Registro MiPyME: https://ici.unq.edu.ar/wp-content/uploads/2025/08/ROJO-Estructura_y_dinamica_mipyme.pdf (leído)"
  - "Comercio-electronico/.investigacion/b2b-rasgos-y-factura.md y b2b-cifras.md"
aliases: [factura A, factura B, Factura de Crédito Electrónica, FCE MiPyME, FCEM, percepción de IVA, percepciones, retenciones, IVA discriminado, crédito fiscal]
creado: 2026-11-22
revisado:
---

# Factura entre empresas

En Argentina, una venta entre empresas se documenta con una factura que discrimina el IVA para que el comprador lo descuente, suma las percepciones que el vendedor esté obligado a cobrar y, cuando una pyme le vende a una empresa grande por encima de un monto, tiene que ser una factura de crédito electrónica que se acepta y se puede negociar. Lo que en una tienda al público es un comprobante, acá es parte del precio y del cobro.

Es el rasgo más local del [comercio entre empresas](comercio-b2b.md). Lo general de lo que regula la venta online está en [Normativa](../Normativa/normativa.md) y en la [normativa argentina](../Normativa/normativa-argentina.md); esta nota trata solo lo que cambia cuando el comprador es otra empresa. Los impuestos de la propia empresa están en el tema [Emprender](../../Emprender/emprender.md). Esta nota no reemplaza a un contador.

## Factura A y factura B

> [!WARNING]
> La regla de este apartado viene de un estudio contable leído por el resumen del buscador. No se leyó la norma de ARCA que define cada comprobante (RG 1415 y sus modificatorias): confirmar ahí antes de usarla.

Según esa fuente, la factura A la emite un responsable inscripto en IVA a otro responsable inscripto (o a un monotributista) y muestra el IVA por separado. La B va de un responsable inscripto a un consumidor final o a un exento, con el IVA incluido en el precio, y el comprador no lo puede descontar. Según la misma fuente, para el comercio que compra la A importa porque el IVA que paga en ella se descuenta del IVA que cobra al vender (el crédito fiscal). Tampoco eso se confirmó en el texto de la ley de IVA.

Desde la Ley 27.743, también la factura al consumidor final tiene que mostrar el «IVA Contenido» y los «Otros Impuestos Nacionales Indirectos» (Régimen de Transparencia Fiscal al Consumidor, reglamentado por la RG 5614/2024). Según iProfesional, rige desde el 1 de enero de 2025 para las empresas grandes y desde el 1 de abril de 2025 para el resto. Que el cambio toque sobre todo a la factura B, porque la A ya discriminaba el IVA, es inferencia.

Cuánto de lo que vende un mayorista va con factura A: en el autoservicio mayorista del panel de INDEC, la facturación A fue $ 90.308 millones en agosto de 2026, frente a ventas totales de $ 395.434 millones. El informe la presenta en un cuadro aparte y no queda claro si se suma o se superpone a la B, así que la proporción (entre 19% y 23% según cómo se cuente) es solo un orden de magnitud.

## Percepciones: el impuesto que el mayorista cobra por adelantado

Algunos vendedores están designados como agentes de percepción: le cobran al cliente, junto con la factura, un adelanto de un impuesto que el cliente después descuenta de su declaración. En el IVA, el régimen es la RG 2408. Su texto original de 2008 fija una alícuota general del 3% sobre el precio neto (1,5% para la alícuota reducida) en las ventas a responsables inscriptos. Un proveedor de software contable repite esas alícuotas en 2026 y suma un mínimo de $ 60 por operación (RG 3905/2016) y una modificación de la RG 5750/2025.

> [!NOTE]
> Sin fuente todavía: el texto ordenado vigente de la RG 2408 y la lista de agentes; las percepciones de Ingresos Brutos de cada provincia (ARBA, AGIP, Convenio Multilateral), que cambian por jurisdicción; y las retenciones que aplica el comprador cuando él es el agente. Un resumen del buscador dio una alícuota de 10,5% que no se pudo conciliar.

Para el software, esto quiere decir que el precio final de un pedido depende de la condición fiscal del cliente y de si el vendedor es agente de percepción; si también pesan la provincia y los padrones de Ingresos Brutos, no se verificó. Que una capa mayorista que solo muestra el precio de lista no llegue a la factura es inferencia de esta base.

## La Factura de Crédito Electrónica MiPyME

La FCE nace de la Ley 27.440 (no se leyó el texto) y, una vez aceptada, la pyme que vendió a plazo a una empresa grande puede negociarla para cobrar antes. Según la página oficial:

- **Cuándo es obligatoria**: cuando una MiPyME (una empresa con certificado del Registro MiPyME, que la clasifica por tramos de facturación) le factura a una empresa grande por $ 5.549.862 o más, desde el 14 de abril de 2026, con ambas partes en Argentina y el CBU informado. Entre MiPyMEs es optativa.
- **Plazo para aceptar**: 21 días corridos. Es un plazo excepcional, más largo que el de la ley, que la Resolución 424/2026 extendió hasta el 31 de octubre de 2027. Si el comprador no la acepta ni la rechaza, queda aceptada.
- **Rechazo**: solo por las causales del artículo 8 de la ley.
- **Qué se vuelve**: aceptada, es «un título ejecutivo y valor no cartular» que se negocia en el sistema bancario o en el mercado de capitales.

Sin la prórroga regirían los plazos de la ley, que una nota de prensa da como 15 días para aceptar y 10 para rechazar; el texto de la ley no se leyó. Según el resumen del buscador, el sitio del BCRA todavía mostraba el monto mínimo de abril de 2025, $ 3.958.316: dos fuentes oficiales discrepan por desactualización y manda la de ARCA.

La FCE es la parte del crédito comercial que el Estado formalizó. Lo que pasa con ella después de emitida se cuenta en [cuenta corriente y crédito](cuenta-corriente-y-credito.md).
