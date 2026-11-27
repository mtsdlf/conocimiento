---
resumen: >-
  En la Argentina, una firma que factura proyectos de servicios tiene cuatro reglas propias: la factura electrónica de un servicio lleva el período facturado y el vencimiento del pago; la factura se emite al terminar la prestación o al cobrar algo del precio, lo que pase primero; los honorarios son libres salvo los mínimos de la ley de abogados en la justicia nacional y federal; y ajustar en pesos por un índice choca con la prohibición de indexar, que sigue vigente.
estado: vigente
estabilidad: semi
fuentes:
  - "ARCA, Manual del desarrollador WSFEv1 (RG 4291), tablas del detalle del comprobante y de validaciones: https://www.arca.gob.ar/fe/ayuda/documentos/wsfev1-RG-4291.pdf"
  - "RG AFIP 1415/2003, art. 13 (copia de la UNC, con la sustitución de la RG 2098/2006): https://www.unc.edu.ar/sites/default/files/RG-AFIP-01415-03.pdf"
  - "RG ARCA 5866/2026, Boletín Oficial del 29/06/2026, texto completo (PDF), art. 1 inc. a) (cuadro del art. 13 de la RG 1415) y art. 4 (vigencia): https://www.boletinoficial.gob.ar/pdf/aviso/primera/343656/20260629"
  - "RG AFIP 4291/2018 (copia de la UNC del texto de 2019, leída entera), art. 9 y anexos: https://www.unc.edu.ar/sites/default/files/RG-AFIP-N%C2%BA-4291-2018.pdf"
  - "RG AFIP 830/2000, régimen de retención de Ganancias, Anexo II incs. i) y k) y art. 10, Biblioteca Electrónica de ARCA (leída por resumen de página): http://biblioteca.afip.gob.ar/dcp/REAG01000830_2000_04_26"
  - "Decreto 1077/2017, Boletín Oficial del 21/12/2017, observaciones a la Ley 27.423: https://www.boletinoficial.gob.ar/pdf/aviso/primera/176428/20171221"
  - "Ley 27.423, texto del art. 1, art. 6 inc. i) y tabla b) del art. 19 (copia del Colegio de Traductores): https://www.traductores.org.ar/wp-content/uploads/2022/08/Ley-27.423-de-honorarios-profesionales.pdf"
  - "Leyes 27.798 (art. 62), 27.701 (arts. 51 y 52), 27.591 (art. 57) y 27.467 (art. 53 y 105), excepciones a los arts. 7 y 10 de la Ley 23.928: https://www.argentina.gob.ar/normativa/nacional/norma-422000/texto, https://www.argentina.gob.ar/normativa/nacional/norma-375860/texto, https://www.argentina.gob.ar/normativa/nacional/norma-345117/texto y https://www.argentina.gob.ar/normativa/nacional/norma-316974/texto"
  - "Decreto DNU 2284/1991, arts. 8 a 11, texto actualizado: https://www.argentina.gob.ar/normativa/nacional/norma-7539/actualizacion"
  - "Ley 27.423 de honorarios de abogados, procuradores y auxiliares de la Justicia, texto actualizado: https://www.argentina.gob.ar/normativa/nacional/norma-305057/actualizacion"
  - "Ley 23.928, arts. 7 y 10 (texto de la Ley 25.561), texto actualizado: https://www.argentina.gob.ar/normativa/nacional/norma-328/actualizacion"
  - "DNU 70/2023, arts. 250 a 257 (reforma del Código Civil y Comercial): https://www.boletinoficial.gob.ar/pdf/aviso/primera/301122/20231221"
  - "Allende & Brea, Modificaciones al Código Civil y Comercial por el DNU 70/2023 (según resumen): https://allende.com/reforma-argentina/desregulacion-economica/modificaciones-al-codigo-civil-y-comercial-de-la-nacion-01-03-2024/"
  - "Servicios-profesionales-y-proyectos/.investigacion/argentina.md"
aliases: [servicios profesionales en Argentina, factura de servicios ARCA, honorarios profesionales Argentina, UMA, indexación de contratos, ajuste por inflación en contratos de servicios]
creado: 2026-11-27
revisado: 2026-11-27
---

# Servicios profesionales en la Argentina

En la Argentina, una firma que factura proyectos de servicios tiene cuatro reglas propias: la factura electrónica de un servicio lleva el período facturado y el vencimiento del pago; la factura se emite al terminar la prestación o al cobrar algo del precio, lo que pase primero; los honorarios son libres salvo los mínimos de la ley de abogados en la justicia nacional y federal; y ajustar en pesos por un índice choca con la prohibición de indexar, que sigue vigente.

Es la nota de país de [Servicios profesionales y proyectos](servicios-profesionales-y-proyectos.md). Toca dos verticales: [Facturación del proyecto](Facturacion-del-proyecto/facturacion-del-proyecto.md), por la factura y su momento, y [Proyecto del cliente](Proyecto-del-cliente/proyecto-del-cliente.md), por el precio que se pacta. Si el trabajo es una obra (armar algo que se entrega) o un servicio (una actividad que se repite) lo explica [contrato de servicio](../Emprender/Legal-e-impuestos/contrato-de-servicio.md#obra-para-armar-servicio-para-cuidar); cómo se emite una factura electrónica y qué letra lleva, [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md); cobrar a un cliente del exterior, [cobrar servicios del exterior](../Emprender/Legal-e-impuestos/cobrar-servicios-del-exterior.md). Lo impositivo recurrente (alícuotas, declaraciones, regímenes de retención) está en [impuestos en Argentina](../Impuestos/impuestos-en-argentina.md).

Es dinero y ley: cada regla dice cuántas fuentes tiene. La nota no reemplaza a un contador ni a un abogado.

## La factura de un servicio lleva el período y el vencimiento

En el servicio web de factura electrónica de ARCA, cada comprobante declara un concepto: 1 productos, 2 servicios o 3 productos y servicios. Con los conceptos 2 y 3, el manual del desarrollador exige tres fechas que una factura de mercadería no lleva:

| Dato | Qué es, según el manual | Validación |
|---|---|---|
| `FchServDesde` | «Fecha de inicio del abono para el servicio a facturar» | obligatoria con concepto 2 o 3 |
| `FchServHasta` | «Fecha de fin del abono para el servicio a facturar» | no puede ser anterior a la de inicio |
| `FchVtoPago` | «Fecha de vencimiento del pago servicio a facturar» | «Debe ser igual o posterior a la fecha del comprobante» |

Si se informa una de las tres, hay que informar las otras (errores 10031, 10033 y 10035 del manual). Para quien construye el sistema, el proyecto tiene que poder dar el período que cubre cada factura: las horas de un mes en un proyecto por hora, o el tramo que cierra un hito.

El manual llama «abono» al período facturado, que no es el [abono](Facturacion-del-proyecto/abono-y-bolsa-de-horas.md) como forma de cobro. En un proyecto sin período natural, informar las fechas de la prestación que se factura es lectura de esta base, porque el manual no lo dice. Hay una sola fuente para este punto, el manual de ARCA. El texto de la RG 4291 (copia de 2019, leída entera) no menciona estas fechas: su art. 6 inc. b) remite a las especificaciones técnicas del servicio web, publicadas en el sitio de ARCA, y ahí están.

## Cuándo nace la obligación de facturar

Para las prestaciones de servicios y las locaciones de obras y de servicios, la factura se emite cuando pasa lo primero de dos cosas: que termine la prestación o que se cobre algo del precio. El art. 13 de la RG 1415 lo dice así: «cuando se concluya la prestación o ejecución, o se perciba —en forma total o parcial— el precio, lo que fuera anterior». La RG 5866/2026 (art. 1 inc. a) reemplazó ese cuadro y rige desde el 1 de julio de 2026 (art. 4). Mantiene la regla: para «Locaciones y prestaciones de servicios» y «Locaciones de obras», la fecha límite es el «Día en que se concluya la prestación o ejecución o en que se perciba -en forma total o parcial- el precio, el que fuera anterior».

Son dos redacciones del mismo artículo, no dos fuentes independientes; las dos se leyeron en el texto. Para un proyecto tiene una consecuencia directa, que es lectura de la norma sin doctrina que la confirme: **cobrar un anticipo, aunque sea parcial, obliga a facturarlo**. Un anticipo o una bolsa de horas prepaga se factura al cobrarse, aunque el ingreso se reconozca después, como explica [trabajo en curso](Facturacion-del-proyecto/trabajo-en-curso.md).

Para los servicios continuos, los que no tienen un plazo de finalización, las dos redacciones difieren. La copia anterior de la RG 1415 hace nacer la obligación «a la finalización de cada uno» de los períodos cuando superan el mes; el cuadro de la RG 5866 pone «Último día de cada mes calendario, excepto que con anterioridad se hubiera percibido -en forma total o parcial- el precio o concluido la operación», y en la columna «Plazo de entrega» fija «Dentro de los DIEZ (10) días corridos contados desde la fecha de emisión». Es la regla que toca a un abono mensual.

Según el art. 9 de la RG 4291, «cuando se trate de prestaciones de servicios, la transferencia podrá efectuarse dentro de los DIEZ (10) días corridos anteriores o posteriores a la fecha consignada en el comprobante» (para el resto, cinco días). Es el texto de la copia de 2019: la RG 5866 no toca este artículo, pero no se revisaron las modificaciones intermedias.

## Los honorarios son libres, con una excepción

El Decreto 2284/1991 dejó sin efecto las declaraciones de orden público sobre aranceles de servicios profesionales «en cualquier clase de actividad» (art. 8), y prohibió que una entidad pública o privada impida «la libre contratación de honorarios» cuando las partes quieran apartarse de las escalas (art. 11). Es la regla general para contadores, arquitectos, ingenieros y el resto de las profesiones, salvo normas posteriores o provinciales que esta pasada no leyó: el precio de un proyecto se pacta.

La excepción leída son los abogados. La Ley 27.423 (2017) fija honorarios en UMA, una unidad que vale el 3 % de la remuneración básica de un juez federal de primera instancia y que la Corte Suprema publica cada mes (art. 19). Trae mínimos también para el trabajo fuera de un juicio, en la tabla b) del art. 19: media UMA por una consulta verbal, una por una consulta con informe, una por una carta documento. Los mínimos por redactar contratos (dos UMA por uno de locación, cinco por un estatuto de sociedad) los observó el Decreto 1077/2017 al promulgar la ley, así que no son parte de ella; no se verificó si el Congreso lo rechazó. El art. 16 dice que los mínimos «revisten carácter de orden público», y el art. 5 declara nulo el pacto que reduzca el arancel, con excepciones. El art. 1 aplica la ley a los «asuntos cuya competencia correspondiere a la justicia nacional o federal».

> [!IMPORTANT]
> La Ley 27.423 es posterior al Decreto 2284/1991 y declara sus mínimos de orden público, mientras el decreto los había desregulado en todas las actividades. Para el trabajo de un abogado fuera de un juicio con un cliente privado, el art. 6 inc. i) de la propia ley dice: «Se podrán celebrar libremente, entre cliente y abogado, convenios de honorarios exclusivamente para determinar las retribuciones de aquellas tareas de asesoramiento profesional extrajudicial, en cuyo caso las pautas establecidas en la presente ley serán de aplicación supletoria». Es una sola fuente, la norma: no se encontró doctrina ni fallo que diga si la redacción de un contrato cuenta como «asesoramiento», ni cuál de los dos textos prevalece. Los mínimos firmes son los del ámbito judicial nacional y federal. Las leyes de aranceles de arquitectos e ingenieros, nacionales o de la Ciudad y la provincia de Buenos Aires, no se encontraron ni se leyeron (el listado de normas que modifican el Decreto 2284/1991 no muestra ninguna sobre aranceles en las diez primeras de 82). Las leyes provinciales de aranceles y las de cada colegio profesional tampoco.

## Ajustar el precio en un proyecto largo

Con inflación, un proyecto de varios meses pactado en pesos pierde valor. La ley vigente limita cómo se ajusta. El art. 7 de la Ley 23.928, en el texto de la Ley 25.561, dice que «en ningún caso se admitirá actualización monetaria, indexación por precios, variación de costos o repotenciación de deudas, cualquiera fuere su causa», y declara inaplicables las cláusulas contractuales que lo contravengan. El art. 10 impide que una cláusula contractual se use como causa de ajuste de los precios «de los bienes, obras o servicios».

El DNU 70/2023 no tocó esos dos artículos. La única mención que hace de la Ley 23.928 está en la locación de inmuebles: permite ajustar el alquiler por «cualquier índice» y dice que a esos contratos no se les aplica el art. 10. Que la excepción se escriba solo para la locación sugiere que fuera de ella el art. 10 sigue rigiendo; es lectura de esta base, y un estudio jurídico que comentó el DNU lo lee igual (según su resumen): el DNU «introdujo únicamente reformas (sustanciales) a las normas sobre contratos de locación» y «no se han modificado normas relativas a otros tipos de contratos». No nombra la obra ni los servicios. Es la única fuente jurídica leída, junto con el texto del DNU.

Lo que el DNU sí cambió sirve para un contrato de servicios. El nuevo art. 765 del Código Civil y Comercial permite deber dinero en una moneda «sea o no de curso legal en el país», y dice que el deudor solo se libera pagando en la moneda pactada. El art. 960 dice que los jueces no pueden modificar lo que las partes estipularon, salvo que una lo pida cuando la ley lo autoriza.

Para quien arma el proyecto, eso deja tres caminos, que son lectura de esta base sobre las normas y no práctica verificada:

1. **Pactar en moneda extranjera**, con respaldo expreso en los arts. 765 y 766.
2. **Cortar el proyecto en tramos con precio propio**, de modo que cada tramo se cotice al empezar. Nada de lo leído prohíbe que las partes acuerden un precio nuevo para el tramo siguiente, y es la misma forma que el [precio cerrado por fase](../Desarrollo/Encargo/modelos-de-contrato-y-cobro.md#qué-se-fija-y-quién-carga-el-riesgo).
3. **Una cláusula de ajuste en pesos por índice**, que choca con el texto de los arts. 7 y 10.

Las excepciones a los arts. 7 y 10 que Infoleg anota se leyeron en las leyes: la 27.798 (art. 62) y la 27.701 (art. 52) las dan para títulos públicos de provincias y de la Ciudad destinados a obras o a reestructurar deuda; la 27.701 (art. 51) y la 27.591 (art. 57), para la asistencia financiera del Fondo Fiduciario para el Desarrollo Provincial; la 27.467 (arts. 53 y 105), para valores negociables del gobierno nacional y para leasing y préstamos prendarios. Ninguna es regla para servicios entre privados.

> [!NOTE] Sin fuente todavía: la práctica y la jurisprudencia sobre cláusulas de ajuste en contratos de servicios entre privados después de 2023 (no se encontró análisis jurídico ni fallo en las búsquedas hechas), y una segunda fuente jurídica sobre que el DNU 70/2023 no tocó la indexación en obra y servicios. Antes de redactar una cláusula de ajuste conviene consultar a un abogado.

La imprevisión, que permite pedir que se revise un contrato cuando una circunstancia extraordinaria lo vuelve excesivamente oneroso, está tratada en [contrato de servicio](../Emprender/Legal-e-impuestos/contrato-de-servicio.md).

## Las retenciones que sufre quien factura

Un cliente que es agente de retención descuenta impuestos al pagar una factura de servicios. Los regímenes más comunes son el de Ganancias sobre honorarios y locaciones de obras y servicios y los de Ingresos Brutos de cada provincia. El de Ganancias es la RG 830 de AFIP: su Anexo II incluye las «Locaciones de obra y/o servicios, no ejecutadas en relación de dependencia» (inc. i) y el «Ejercicio de profesiones liberales u oficios» (inc. k), y su art. 10 dispone que se retiene al momento del pago. La Biblioteca Electrónica de ARCA la marca vigente, con modificaciones hasta la RG 5822/2026; es una sola fuente. Para el registro del proyecto importa una cosa, que es criterio de esta base: el cobro neto es menor que la factura, y la diferencia es un impuesto pagado a cuenta, no un descuento al cliente ni una pérdida de [realización](Rentabilidad-de-la-firma/realizacion.md). No hay que confundirla con la [retención de garantía](Facturacion-del-proyecto/facturacion-por-hito.md), que es una parte del precio que el cliente guarda hasta el final del trabajo.

La factura que recibe retención lleva en la clase A la leyenda «OPERACIÓN SUJETA A RETENCIÓN», que reemplazó a la clase M; está en [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md#qué-letra-lleva-cada-comprobante).

Los regímenes de Ingresos Brutos (los padrones provinciales, el SIRCREB sobre las acreditaciones bancarias y el SIRTAC sobre los cobros electrónicos), las alícuotas y montos de la RG 830 y las retenciones de IVA están en [retenciones y percepciones en Argentina](../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md), en Impuestos; cómo se computa lo retenido, en [pagos a cuenta](../Impuestos/Recaudacion-en-la-fuente/pagos-a-cuenta.md).

> [!NOTE] Sin fuente todavía: las retenciones de seguridad social sobre una factura de servicios. Ninguna nota de la base las trata.
