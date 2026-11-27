---
resumen: >-
  En la Argentina, una firma que factura proyectos de servicios tiene cuatro reglas propias: la factura electrónica de un servicio lleva el período facturado y el vencimiento del pago; la factura se emite al terminar la prestación o al cobrar algo del precio, lo que pase primero; los honorarios son libres salvo los mínimos de la ley de abogados en la justicia nacional y federal; y ajustar en pesos por un índice choca con la prohibición de indexar, que sigue vigente.
estado: borrador
estabilidad: semi
fuentes:
  - "ARCA, Manual del desarrollador WSFEv1 (RG 4291), tablas del detalle del comprobante y de validaciones: https://www.arca.gob.ar/fe/ayuda/documentos/wsfev1-RG-4291.pdf"
  - "RG AFIP 1415/2003, art. 13 (copia de la UNC, con la sustitución de la RG 2098/2006): https://www.unc.edu.ar/sites/default/files/RG-AFIP-01415-03.pdf"
  - "RG ARCA 5866/2026, Boletín Oficial del 29/06/2026, cuadro del art. 13 de la RG 1415 (según resumen): https://www.boletinoficial.gob.ar/detalleAviso/primera/343656/20260629"
  - "RG AFIP 4291/2018 (copia de la UNC, leída en parte): https://www.unc.edu.ar/sites/default/files/RG-AFIP-N%C2%BA-4291-2018.pdf"
  - "Decreto DNU 2284/1991, arts. 8 a 11, texto actualizado: https://www.argentina.gob.ar/normativa/nacional/norma-7539/actualizacion"
  - "Ley 27.423 de honorarios de abogados, procuradores y auxiliares de la Justicia, texto actualizado: https://www.argentina.gob.ar/normativa/nacional/norma-305057/actualizacion"
  - "Ley 23.928, arts. 7 y 10 (texto de la Ley 25.561), texto actualizado: https://www.argentina.gob.ar/normativa/nacional/norma-328/actualizacion"
  - "DNU 70/2023, arts. 250 a 257 (reforma del Código Civil y Comercial): https://www.boletinoficial.gob.ar/pdf/aviso/primera/301122/20231221"
  - "Allende & Brea, Modificaciones al Código Civil y Comercial por el DNU 70/2023 (según resumen): https://allende.com/reforma-argentina/desregulacion-economica/modificaciones-al-codigo-civil-y-comercial-de-la-nacion-01-03-2024/"
  - "Servicios-profesionales-y-proyectos/.investigacion/argentina.md"
aliases: [servicios profesionales en Argentina, factura de servicios ARCA, honorarios profesionales Argentina, UMA, indexación de contratos, ajuste por inflación en contratos de servicios]
creado: 2026-11-27
revisado:
---

# Servicios profesionales en la Argentina

En la Argentina, una firma que factura proyectos de servicios tiene cuatro reglas propias: la factura electrónica de un servicio lleva el período facturado y el vencimiento del pago; la factura se emite al terminar la prestación o al cobrar algo del precio, lo que pase primero; los honorarios son libres salvo los mínimos de la ley de abogados en la justicia nacional y federal; y ajustar en pesos por un índice choca con la prohibición de indexar, que sigue vigente.

Es la nota de país de [Servicios profesionales y proyectos](servicios-profesionales-y-proyectos.md). Toca dos verticales: [Facturación del proyecto](Facturacion-del-proyecto/facturacion-del-proyecto.md), por la factura y su momento, y [Proyecto del cliente](Proyecto-del-cliente/proyecto-del-cliente.md), por el precio que se pacta. Si el trabajo es una obra (armar algo que se entrega) o un servicio (una actividad que se repite) lo explica [contrato de servicio](../Emprender/Legal-e-impuestos/contrato-de-servicio.md#obra-para-armar-servicio-para-cuidar); cómo se emite una factura electrónica y qué letra lleva, [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md); cobrar a un cliente del exterior, [cobrar servicios del exterior](../Emprender/Legal-e-impuestos/cobrar-servicios-del-exterior.md). Lo impositivo recurrente (alícuotas, declaraciones, regímenes de retención) va al tema Impuestos, que todavía no está escrito.

Es dinero y ley: cada regla dice cuántas fuentes tiene. La nota no reemplaza a un contador ni a un abogado.

## La factura de un servicio lleva el período y el vencimiento

En el servicio web de factura electrónica de ARCA, cada comprobante declara un concepto: 1 productos, 2 servicios o 3 productos y servicios. Con los conceptos 2 y 3, el manual del desarrollador exige tres fechas que una factura de mercadería no lleva:

| Dato | Qué es, según el manual | Validación |
|---|---|---|
| `FchServDesde` | «Fecha de inicio del abono para el servicio a facturar» | obligatoria con concepto 2 o 3 |
| `FchServHasta` | «Fecha de fin del abono para el servicio a facturar» | no puede ser anterior a la de inicio |
| `FchVtoPago` | «Fecha de vencimiento del pago servicio a facturar» | «Debe ser igual o posterior a la fecha del comprobante» |

Si se informa una de las tres, hay que informar las otras (errores 10031, 10033 y 10035 del manual). Para quien construye el sistema, el proyecto tiene que poder dar el período que cubre cada factura: las horas de un mes en un proyecto por hora, o el tramo que cierra un hito.

El manual llama «abono» al período facturado, que no es el [abono](Facturacion-del-proyecto/abono-y-bolsa-de-horas.md) como forma de cobro. En un proyecto sin período natural, informar las fechas de la prestación que se factura es lectura de esta base, porque el manual no lo dice. Hay una sola fuente para este punto, el manual de ARCA; el artículo de la RG 4291 que crea esos datos no se leyó.

## Cuándo nace la obligación de facturar

Para las prestaciones de servicios y las locaciones de obras y de servicios, la factura se emite cuando pasa lo primero de dos cosas: que termine la prestación o que se cobre algo del precio. El art. 13 de la RG 1415 lo dice así: «cuando se concluya la prestación o ejecución, o se perciba —en forma total o parcial— el precio, lo que fuera anterior». La RG 5866/2026, que reemplazó ese cuadro desde el 1 de julio de 2026, mantiene la regla, según el resumen de su aviso en el Boletín Oficial: «Día en que se concluya la prestación o ejecución o en que se perciba -en forma total o parcial- el precio».

Son dos redacciones del mismo artículo, no dos fuentes independientes. Para un proyecto tiene una consecuencia directa, que es lectura de la norma sin doctrina que la confirme: **cobrar un anticipo, aunque sea parcial, obliga a facturarlo**. Un anticipo o una bolsa de horas prepaga se factura al cobrarse, aunque el ingreso se reconozca después, como explica [trabajo en curso](Facturacion-del-proyecto/trabajo-en-curso.md).

Para los servicios continuos, los que no tienen un plazo de finalización, las dos redacciones difieren. La copia anterior de la RG 1415 hace nacer la obligación «a la finalización de cada uno» de los períodos cuando superan el mes; el cuadro de la RG 5866, según su resumen, pone «Último día de cada mes calendario», salvo que antes se termine o se cobre. Es la regla que toca a un abono mensual.

Según la RG 4291, en las prestaciones de servicios los datos del comprobante pueden transmitirse a ARCA dentro de los 10 días corridos anteriores o posteriores a su fecha.

> [!NOTE] Sin fuente todavía: el texto completo de la RG 5866/2026 (se leyó por resumen) y el artículo de la RG 4291 que fija ese plazo de 10 días.

## Los honorarios son libres, con una excepción

El Decreto 2284/1991 dejó sin efecto las declaraciones de orden público sobre aranceles de servicios profesionales «en cualquier clase de actividad» (art. 8), y prohibió que una entidad pública o privada impida «la libre contratación de honorarios» cuando las partes quieran apartarse de las escalas (art. 11). Es la regla general para contadores, arquitectos, ingenieros y el resto de las profesiones, salvo normas posteriores o provinciales que esta pasada no leyó: el precio de un proyecto se pacta.

La excepción leída son los abogados. La Ley 27.423 (2017) fija honorarios en UMA, una unidad que vale el 3 % de la remuneración básica de un juez federal de primera instancia y que la Corte Suprema publica cada mes (art. 19). Trae mínimos también para el trabajo fuera de un juicio: media UMA por una consulta verbal, dos como mínimo por redactar un contrato de locación, cinco por un estatuto de sociedad. Su art. 16 dice que esos mínimos «revisten carácter de orden público», y el art. 5 declara nulo el pacto que los reduzca, con excepciones. El art. 1 la aplica a los «asuntos cuya competencia correspondiere a la justicia nacional o federal».

> [!IMPORTANT]
> La Ley 27.423 es posterior al Decreto 2284/1991 y declara sus mínimos de orden público, mientras el decreto los había desregulado en todas las actividades. No se encontró un análisis jurídico que diga cuál rige para el trabajo de un abogado fuera de un juicio con un cliente privado. Lo cierto es el ámbito judicial nacional y federal. Las leyes provinciales de aranceles y las de cada colegio profesional no se leyeron.

## Ajustar el precio en un proyecto largo

Con inflación, un proyecto de varios meses pactado en pesos pierde valor. La ley vigente limita cómo se ajusta. El art. 7 de la Ley 23.928, en el texto de la Ley 25.561, dice que «en ningún caso se admitirá actualización monetaria, indexación por precios, variación de costos o repotenciación de deudas, cualquiera fuere su causa», y declara inaplicables las cláusulas contractuales que lo contravengan. El art. 10 impide que una cláusula contractual se use como causa de ajuste de los precios «de los bienes, obras o servicios».

El DNU 70/2023 no tocó esos dos artículos. La única mención que hace de la Ley 23.928 está en la locación de inmuebles: permite ajustar el alquiler por «cualquier índice» y dice que a esos contratos no se les aplica el art. 10. Que la excepción se escriba solo para la locación sugiere que fuera de ella el art. 10 sigue rigiendo; es lectura de esta base, y un estudio jurídico que comentó el DNU lo lee igual (según su resumen): el DNU cambió el contrato de locación y no los de obra y servicios.

Lo que el DNU sí cambió sirve para un contrato de servicios. El nuevo art. 765 del Código Civil y Comercial permite deber dinero en una moneda «sea o no de curso legal en el país», y dice que el deudor solo se libera pagando en la moneda pactada. El art. 960 dice que los jueces no pueden modificar lo que las partes estipularon, salvo que una lo pida cuando la ley lo autoriza.

Para quien arma el proyecto, eso deja tres caminos, que son lectura de esta base sobre las normas y no práctica verificada:

1. **Pactar en moneda extranjera**, con respaldo expreso en los arts. 765 y 766.
2. **Cortar el proyecto en tramos con precio propio**, de modo que cada tramo se cotice al empezar. Nada de lo leído prohíbe que las partes acuerden un precio nuevo para el tramo siguiente, y es la misma forma que el [precio cerrado por fase](../Desarrollo/Encargo/modelos-de-contrato-y-cobro.md#qué-se-fija-y-quién-carga-el-riesgo).
3. **Una cláusula de ajuste en pesos por índice**, que choca con el texto de los arts. 7 y 10.

> [!NOTE] Sin fuente todavía: la práctica y la jurisprudencia sobre cláusulas de ajuste en contratos de servicios entre privados después de 2023, y las excepciones a los arts. 7 y 10 que anotan las leyes 27.798, 27.701, 27.591 y 27.467. Antes de redactar una cláusula de ajuste conviene consultar a un abogado.

La imprevisión, que permite pedir que se revise un contrato cuando una circunstancia extraordinaria lo vuelve excesivamente oneroso, está tratada en [contrato de servicio](../Emprender/Legal-e-impuestos/contrato-de-servicio.md).

## Las retenciones que sufre quien factura

Un cliente que es agente de retención descuenta impuestos al pagar una factura de servicios. Los regímenes más comunes son el de Ganancias sobre honorarios y locaciones de obras y servicios (la RG 830) y los de Ingresos Brutos de cada provincia. Para el registro del proyecto importa una cosa, que es criterio de esta base: el cobro neto es menor que la factura, y la diferencia es un impuesto pagado a cuenta, no un descuento al cliente ni una pérdida de [realización](Rentabilidad-de-la-firma/realizacion.md). No hay que confundirla con la [retención de garantía](Facturacion-del-proyecto/facturacion-por-hito.md), que es una parte del precio que el cliente guarda hasta el final del trabajo.

La factura que recibe retención lleva en la clase A la leyenda «OPERACIÓN SUJETA A RETENCIÓN», que reemplazó a la clase M; está en [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md#qué-letra-lleva-cada-comprobante).

> [!NOTE] Sin fuente todavía: el texto de la RG 830 y de los regímenes de Ingresos Brutos (no se pudieron leer en esta pasada); las retenciones de IVA y de seguridad social. Van al tema Impuestos.
