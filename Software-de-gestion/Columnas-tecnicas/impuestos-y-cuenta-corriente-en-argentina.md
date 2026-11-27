---
resumen: >-
  En la Argentina, el motor de impuestos de un sistema tiene que calcular varias alícuotas de IVA en un mismo comprobante e informarlas a ARCA agrupadas por alícuota, dentro de la tolerancia de redondeo del web service. Tiene que sumar como tributos aparte las percepciones, con la alícuota de cada cliente que publica el padrón de cada provincia, y mostrar el IVA contenido en la factura al consumidor final. La cuenta corriente, a su vez, tiene que cancelar facturas con plata y con comprobantes de retención.
estado: borrador
estabilidad: volatil
fuentes:
  - "Software-de-gestion/.investigacion/motor-de-impuestos-y-deuda-en-argentina.md (2026-11-27)"
  - "ARCA, manual WSFEv1 «RG 4291 – Proyecto FE v4.8», «Revisión correspondiente al 1 de Diciembre de 2026» (leído con pdftotext): https://www.arca.gob.ar/fe/ayuda/documentos/wsfev1-RG-4291.pdf"
  - "RG ARCA 5614/2024, texto en argentina.gob.ar: https://www.argentina.gob.ar/normativa/nacional/norma-407183/texto"
  - "ARBA, RN 2/2013 con sus modificaciones (sustituye arts. 322 y 344 de la DN B 1/04): https://web.arba.gov.ar/sites/default/files/2024-03/RN%202-2013.pdf"
  - "ARBA, RN 38/2025: https://www.arba.gov.ar/archivos/Tramites/RN%2038-2025.pdf"
  - "AGIP, Resolución 296/2019, Anexo I (texto unificado de regímenes de recaudación, PDF de noviembre de 2019): https://documentosboletinoficial.buenosaires.gob.ar/publico/PE-RES-MEFGC-AGIP-296-19-ANX.pdf"
  - "RG ARCA 5762/2025, arts. 13 a 22, en la biblioteca de ARCA: https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5762%7Co%3A9%7Ca%3A2025%7Cf%3A24%2F09%2F2025"
  - "RG AFIP 2854/2010, texto de InfoLEG de junio de 2016, arts. 8 a 16, en una copia alojada por la UNC: https://www.unc.edu.ar/sites/default/files/RG-IVA-2854.pdf"
  - "RG AFIP 2854/2010, texto actualizado en la biblioteca de ARCA (vigente; art. 12 según RG 3887/2016): https://biblioteca.afip.gob.ar/dcp/REAG01002854_2010_06_22"
  - "RG AFIP 830/2000, texto actualizado en la biblioteca de ARCA (arts. 29 y 33): https://biblioteca.afip.gob.ar/dcp/REAG01000830_2000_04_26"
  - "RG AFIP 1415/2003, texto actualizado en la biblioteca de ARCA (Anexo II, Apartado A, Título IV): https://biblioteca.afip.gob.ar/dcp/REAG01001415_2003_01_07"
  - "Ley 27.743, arts. 98 y 99, en InfoLEG: https://servicios.infoleg.gob.ar/infolegInternet/anexos/400000-404999/401268/norma.htm"
  - "Ley de IVA, texto actualizado en InfoLEG (artículo sin número a continuación del art. 28, según Ley 27.701): https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42701/texact.htm"
  - "ARCA, tabla «Otros Tributos» de factura electrónica, enlazada desde https://www.afip.gob.ar/fe/ayuda/tablas.asp: https://www.afip.gob.ar/fe/documentos/otros_Tributos.xlsx"
  - "ARBA, DN Serie B 1/04, texto vigente compilado en abril de 2025 con fines de orientación (arts. 322, 342 y 343): https://web.arba.gov.ar/sites/default/files/2025-04/DN%20B%201-2004%20Texto%20vigente.pdf"
  - "Comisión Arbitral, RG CA 9/2025 (SIRCIP), 14/2017 y 5/2021: https://www.ca.gob.ar/"
  - "Software-de-gestion/.investigacion/motor-de-impuestos-y-deuda-en-argentina-segunda-ronda.md (2026-11-27)"
aliases: [motor de impuestos en Argentina, AlicIva, Tributos WSFEv1, ImpTrib, FEParamGetTiposIva, FEParamGetTiposTributos, tolerancia de redondeo ARCA, IVA contenido, transparencia fiscal al consumidor, percepción de Ingresos Brutos, padrón de ARBA, padrón de AGIP, alícuota fuera de padrón, orden de pago con retenciones, recibo con retenciones, certificado de retención]
creado: 2026-11-27
revisado:
---

# Impuestos y cuenta corriente en la Argentina

En la Argentina, el motor de impuestos de un sistema tiene que calcular varias alícuotas de IVA en un mismo comprobante e informarlas a ARCA agrupadas por alícuota, dentro de la tolerancia de redondeo del web service. Tiene que sumar como tributos aparte las percepciones, con la alícuota de cada cliente que publica el padrón de cada provincia, y mostrar el IVA contenido en la factura al consumidor final. La cuenta corriente, a su vez, tiene que cancelar facturas con plata y con comprobantes de retención.

> [!WARNING]
> Ley y dinero: esto no reemplaza a un contador ni a un abogado tributarista. Las normas se leyeron el 2026-11-27 y varias se leyeron en copias o en textos sin fecha de corte; los importes mínimos cambian por resolución. Antes de construir, se lee la versión vigente.

Lo general está en [motor de impuestos](motor-de-impuestos.md) y en [cuenta corriente y aplicación](cuenta-corriente-y-aplicacion.md). Las reglas tributarias viven en su tema: las alícuotas de IVA, en [IVA en Argentina](../../Impuestos/Impuestos-al-consumo/iva-en-argentina.md#las-alícuotas-en-las-palabras-de-la-ley); los regímenes de recaudación, en [retenciones y percepciones en Argentina](../../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md); Ingresos Brutos y el Convenio Multilateral, en [Ingresos Brutos](../../Impuestos/Impuestos-al-consumo/ingresos-brutos.md). Lo que la norma le pide al sistema en general (el CAE, la contingencia, los libros) está en [software de gestión en la Argentina](../software-de-gestion-en-argentina.md). Acá va lo que cada regla le cambia al cálculo de un renglón y al modelo de la deuda.

## Varias alícuotas de IVA en un mismo comprobante

Una factura argentina mezcla renglones al 21 %, al 10,5 % y al 27 %, y la alícuota de cada uno depende del producto, del cliente y del uso, como lee [IVA en Argentina](../../Impuestos/Impuestos-al-consumo/iva-en-argentina.md#las-alícuotas-en-las-palabras-de-la-ley) sobre el art. 28 de la ley. La ley tiene además dos alícuotas que esa nota no lista. El artículo sin número a continuación del art. 28, sustituido por la Ley 27.701 desde el 1 de enero de 2023, da 2,5 % y 5 % a la locación de espacios publicitarios en diarios, revistas y publicaciones periódicas de quien hace producción editorial, y a las ediciones periodísticas digitales, según la facturación de los últimos doce meses sin IVA: hasta $ 250.000.000, 2,5 %; hasta $ 500.000.000, 5 %; hasta $ 1.000.000.000, 10,5 %; arriba, 21 % (texto actualizado de InfoLEG, donde la tabla es una imagen). La alícuota se recalcula al terminar cada cuatrimestre calendario y, desde 2024, los montos se actualizan «conforme la variación operada en el límite de ventas totales anuales aplicables a las medianas empresas del Tramo 2 correspondientes al sector servicios». Para el motor es una alícuota que depende de la facturación propia del vendedor y cambia cada cuatro meses, no del artículo ni del cliente (lectura de esta base).

El web service de factura electrónica (WSFEv1) recibe el IVA agrupado por alícuota y no por renglón. Según su manual v4.8:

- El arreglo `AlicIva` lleva, por cada alícuota, el código (`Id`), la base (`BaseImp`) y el importe (`Importe`). El código no se repite: «El campo Id en AlicIVA no debe repetirse. Deberá totalizarse por alícuota» (error 10022).
- El código sale del método `FEParamGetTiposIva`, que devuelve cada tipo con su fecha de vigencia (`FchDesde`, `FchHasta`). Los ejemplos del manual usan 3 para el 0 %, 4 para el 10,5 %, 5 para el 21 % y 6 para el 27 %.
- La suma de las bases de `AlicIva` tiene que ser igual al neto gravado, `ImpNeto` (error 10061), y la suma de sus importes, igual al IVA total, `ImpIVA` (error 10023).
- El total separa lo no gravado (`ImpTotConc`), lo gravado (`ImpNeto`), lo exento (`ImpOpEx`), los otros tributos (`ImpTrib`) y el IVA: «“Importe Total” <ImpTotal>, debe ser igual a la suma de ImpTotConc + ImpNeto + ImpOpEx + ImpTrib + ImpIVA» (error 10048).

Lo no gravado y lo exento van en campos distintos. Para el motor, en lectura de esta base, es la misma distinción que hace la lista europea entre la categoría O (fuera del impuesto) y la E (exenta): la categoría del renglón decide en qué campo del total cae.

El ejemplo del propio manual, una factura A:

| Renglón | Neto | IVA | Importe de IVA |
|---|---|---|---|
| ítem 1 | 100,00 | 21 % | 21,00 |
| ítem 2 | 50,00 | 10,5 % | 5,25 |
| Tributo sobre 150,00 al 5,2 % | | | 7,80 |
| **Total** | **150,00** | | **26,25 de IVA, 7,80 de tributos, 184,05 en total** |

## La tolerancia del fisco al redondeo

El manual no dice si el IVA se redondea por renglón o por alícuota: acepta diferencias chicas. En las comparaciones de importes repite la misma regla: «Error relativo porcentual deberá ser <= 0.01% o el error absoluto <=0.01». En la suma de los importes de `AlicIva` contra `ImpIVA` y en la de las bases contra `ImpNeto`, el margen se multiplica por la «cantidad de alícuotas de IVA ingresadas» (errores 10023 y 10061). En la suma de los tributos, por la «cantidad de tributos» (error 10029). En el total del comprobante (10048) y en la correspondencia entre importe y alícuota de cada `AlicIva` (10051), el margen es de 0,01 sin multiplicar. Los importes van con dos decimales (error 10056).

Lo que sale para el diseño, en lectura de esta base sobre esas reglas:

- Redondear por renglón y sumar sirve si el importe de cada alícuota queda a no más de 0,01 % o 0,01 de su base por la alícuota. En una factura grande el margen relativo alcanza de sobra. En una factura chica con muchos renglones a la misma alícuota, los centavos de cada renglón pueden sumar más de un centavo y el comprobante se rechaza.
- Calcular el IVA una vez por alícuota, sobre la suma de las bases, queda siempre dentro del margen. Es lo que pide EN 16931 en Europa ([motor de impuestos](motor-de-impuestos.md#redondear-por-renglón-o-por-total)).
- Lo que se informa a ARCA es lo que va al libro: el comprobante, el libro de IVA y el asiento usan los mismos importes de `AlicIva`.

## Percepciones y otros tributos en la factura

Lo que no es IVA va en el arreglo `Tributos`: por cada uno, el código (`Id`, del método `FEParamGetTiposTributos`), una descripción, la base, la alícuota y el importe. La suma de los importes tiene que dar `ImpTrib` (error 10029). Si el código es 99, la descripción es obligatoria (error 10042). En el ejemplo de factura A de más arriba, el tributo es un impuesto municipal con código 99; otro ejemplo del manual informa Ingresos Brutos de la provincia de Buenos Aires con el código 2. El manual no trae la lista de códigos, pero ARCA publica una tabla de «Otros Tributos» en la página de tablas de factura electrónica:

| Código | Descripción en la tabla |
|---|---|
| 01 | Impuestos nacionales |
| 02 | Impuestos provinciales |
| 03 | Tributos municipales |
| 04 | Impuestos internos |
| 05 | IIBB |
| 6 | Percepción de IVA |
| 7 | Percepción de IIBB |
| 8 | Percepciones por Tributos Municipales |
| 09 | Otras Percepciones |
| 13 | Percepción de IVA a no Categorizado (solo factura electrónica) |
| 99 | Otros |

La tabla trae además el código 10, impuesto interno por ítem, solo para controladores fiscales, y del 14 al 19, retenciones y percepciones de liquidaciones pecuarias. Es la tabla publicada; el servicio puede devolver otra con sus fechas de vigencia, y el sistema la consulta con `FEParamGetTiposTributos`. El ejemplo del manual informa Ingresos Brutos con el código 2 y la tabla tiene uno propio para la percepción de IIBB, el 7: ninguna fuente leída dice cuál corresponde en cada caso.

Para el motor, cada percepción es un impuesto más del comprobante, con su base, su alícuota y su jurisdicción. La de IVA, de la RG 2408, se calcula sobre el precio neto, con 3 % o 1,50 % según la alícuota de la operación y con un mínimo por operación ([los regímenes nacionales](../../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md#los-regímenes-nacionales)). Las de Ingresos Brutos dependen del cliente.

## La alícuota de percepción sale del padrón de cada provincia

En Ingresos Brutos, la alícuota de percepción es del cliente, y la publica cada fisco en un padrón. Dos regímenes leídos lo muestran.

| | Provincia de Buenos Aires (ARBA) | Ciudad de Buenos Aires (AGIP) |
|---|---|---|
| De dónde sale la alícuota | «la alícuota que con relación a cada contribuyente en particular se consignará en el padrón de contribuyentes que la Autoridad de Aplicación publicará en su página web» (RN 2/2013, art. 344 de la DN B 1/04) | el «Padrón de Regímenes Generales» publicado en el sitio de AGIP, también para contribuyentes de Convenio Multilateral (Res. 296/2019, art. 60) |
| Grupos de alícuotas | de 0,00 % a 6,00 %, en quince grupos | de 0,00 % a 6,00 %, en dieciséis grupos (art. 65) |
| Actualización | mensual: se publica con al menos siete días hábiles de anticipación y rige desde el primer día del mes siguiente; trimestral para las empresas de electricidad, gas, agua, cloacas y telecomunicaciones | sin dato leído |
| Cliente que no está en el padrón | 6 %, «siempre que […] la entrega o realización tenga lugar en jurisdicción de la Provincia de Buenos Aires» | 6 %, si no acredita inscripción; se considera hecha en la Ciudad la venta que se materializa en ella (art. 66). Si acredita el alta después de publicado el padrón, 3,5 % (art. 67) |
| Si el padrón no se puede consultar | 3 %, cuando el sitio no responde durante todo el día; también 3 % en la venta directa | sin dato leído |
| Cuándo y sobre qué | sobre el monto total de la factura, con dos alternativas: menos las percepciones de otros regímenes y ciertos conceptos del Código Fiscal, o además menos el IVA cuando el cliente es responsable inscripto y ciertos impuestos internos (art. 342 de la DN B 1/04); solo si la base llega a $ 3.500, salvo en la venta directa (art. 343, según la RN 18/2023) | al emitir la factura (art. 32), sobre el monto de la operación menos los conceptos que la factura discrimina (art. 33) |
| Exclusiones leídas | el Estado nacional, las provincias, la Ciudad y los municipios; los desgravados o no alcanzados; ciertas actividades del Código Fiscal; quien tiene alícuota cero por reducción (art. 322) | las ventas a consumidores finales (art. 52); los bienes de uso, con declaración del comprador (art. 53); lo realizado fuera de la Ciudad por quien no está inscripto en ella (art. 50) |

La RN 38/2025 de ARBA suma un mecanismo, a pedido del contribuyente que cumple ciertos requisitos (doce anticipos presentados y un riesgo fiscal bajo, art. 3), que lleva al mínimo su alícuota en los regímenes sobre acreditaciones bancarias y puede subirla en los demás regímenes con padrón, para compensar (arts. 1 a 3). El padrón, entonces, también cambia por pedidos individuales. Los artículos 322, 342 y 343 de ARBA se leyeron en el texto vigente que la propia ARBA compiló en abril de 2025 «con fines de orientación y difusión»: el texto auténtico es el del Boletín Oficial de la provincia. El monto mínimo de AGIP leído, $ 500 para percibir (art. 34), es del texto de 2019 y casi seguro cambió. La factura con la percepción discriminada es la constancia para el cliente (art. 54).

Lo que sale para el motor, en lectura de esta base:

- Una tabla de alícuotas por cliente y por jurisdicción, con vigencia (mensual en ARBA, trimestral para los servicios públicos), cargada desde el padrón de cada fisco donde la empresa es agente. Es un dato con vigencia como cualquier alícuota ([vigencias](fechas-vigencias-y-cierre.md#vigencias-datos-que-valen-desde-y-hasta)): la factura de ayer usa el padrón del mes de ayer.
- Una regla para el cliente que no está en el padrón, distinta en cada jurisdicción, y otra para cuando no se pudo bajar el padrón.
- Una regla de dónde ocurre la operación. ARBA mira dónde es la entrega y AGIP, dónde se materializa la venta y si el vendedor está inscripto en la Ciudad. No hay una regla única entre provincias. La Comisión Arbitral tiene un sistema para las percepciones a contribuyentes de Convenio Multilateral, el SIRCIP (RG CA 9/2025), pero deja la obligación a «las normas locales» de cada jurisdicción adherida; sus reglas sobre el domicilio del adquirente (RG CA 14/2017 y 5/2021) sirven para repartir la base del impuesto, no para decidir dónde se percibe.
- La percepción se calcula al confirmar la factura y queda congelada en ella, como el resto del cálculo ([motor de impuestos](motor-de-impuestos.md#el-cálculo-queda-congelado-en-el-documento)).

Cómo se descarga cada padrón, con qué formato y qué calendario, queda abierto también en [software de gestión en la Argentina](../software-de-gestion-en-argentina.md#lo-que-se-integra-con-arca-y-con-las-provincias).

## La factura al consumidor final y el IVA contenido

En la factura al consumidor final el precio incluye el IVA, pero desde 2025 el comprobante lo muestra. El art. 99 de la Ley 27.743 dice que las facturas o tiques de las ventas a consumidores finales «deberán detallar el importe discriminado del Impuesto al Valor Agregado y de los demás impuestos nacionales indirectos que incidan en los precios», y el art. 98 cambia el art. 39 de la ley de IVA para que el responsable inscripto discrimine el impuesto, calculado «aplicando sobre el precio neto […] la alícuota correspondiente». La RG 5614/2024 lo reglamenta modificando la RG 1415, que sigue vigente. Para el responsable inscripto, la resolución pide discriminar el impuesto también en las «operaciones gravadas efectuadas con sujetos exentos, no alcanzados o consumidores finales», salvo que otra norma fije un tratamiento específico. En el comprobante impreso, abajo a la izquierda, van el título «Régimen de Transparencia Fiscal al Consumidor (Ley 27.743)», el «IVA Contenido» y los «Otros Impuestos Nacionales Indirectos». Rige para todos desde el 1 de abril de 2025 y para las grandes empresas desde el 1 de enero ([factura electrónica de ARCA](../../Comercio-electronico/Normativa/factura-electronica-de-arca.md)).

Para el motor, en lectura de esta base, la factura B sigue pidiendo el neto y las alícuotas: el manual del WSFEv1 trae un ejemplo de factura B con importe gravado al 21 % que se informa con `AlicIva`. El motor hace la cuenta al revés desde el precio final, separa neto e IVA por alícuota y de ahí saca el IVA contenido del pie. Los impuestos internos, si los hay, irían en el segundo total del pie, «Otros Impuestos Nacionales Indirectos», y no se suman al IVA. La forma general de esa cuenta está en [precio con impuesto incluido](motor-de-impuestos.md#precio-con-impuesto-incluido-e-impuesto-sobre-impuesto), sin fuente primaria todavía.

## El recibo y la orden de pago con retenciones

En la Argentina, una factura se cancela casi siempre con plata y con comprobantes de retención. Quien paga practica la retención en el momento del pago y entrega un comprobante: la RG 2854 lo pide «en el momento en que se efectúe el pago y se practique la retención», con numeración propia, consecutiva y progresiva (art. 14). El régimen de la RG 5762/2025 entrega «el comprobante o certificado» del sistema con que el agente informa, SICORE o SIRE (art. 15; qué es cada uno, en [cómo informa el agente](../../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md#cómo-informa-el-agente-sicore-y-sire)). Para quien la sufre, la retención de IVA tiene «el carácter de impuesto ingresado» (RG 2854, art. 16; RG 5762, art. 17). Las dos conviven: la RG 2854 sigue vigente en la biblioteca de ARCA y la RG 5762 no la nombra entre las que deroga; la RG 5762 crea un régimen aparte para las facturas A con la leyenda «OPERACIÓN SUJETA A RETENCIÓN». En Ganancias, la RG 830 dice que lo que se deduce como retención sale de los «Certificados de Retención» emitidos con SICORE (art. 33), y no retiene por debajo de $ 240, o $ 1.020 en alquileres urbanos a no inscriptos (art. 29, según la RG 4525/2019); la RG 2854 no retiene si el importe es de $ 400 o menos (art. 12, según la RG 3887/2016).

Dos reglas tocan la aplicación. Con pagos parciales, la RG 5762 imputa la retención hasta la concurrencia de cada pago (art. 14), y la RG 2854 también trata los pagos parciales (art. 11). En las facturas que llevan la leyenda «PAGO EN CBU INFORMADA», el comprador responsable inscripto cancela «la diferencia entre el importe total facturado y las retenciones que por otros regímenes pudieran corresponder» (RG 5762, art. 22).

Lo que sale para el modelo, en lectura de esta base sobre esas reglas y sobre [cuenta corriente y aplicación](cuenta-corriente-y-aplicacion.md#los-impuestos-que-cancelan-deuda-retenciones-y-percepciones):

- La orden de pago a un proveedor es un documento con renglones de dos clases: los medios de pago (transferencia, cheque electrónico o ECHEQ) y las retenciones, cada una con su régimen, su base, su alícuota y su número de certificado. Las dos clases se aplican a las facturas que el pago cancela.
- El recibo de un cliente es el mismo documento al revés: la plata y los cheques recibidos, más los certificados de retención que el cliente entregó, como partidas acreedoras que cancelan la factura. El certificado va a la cuenta de impuestos como [pago a cuenta](../../Impuestos/Recaudacion-en-la-fuente/pagos-a-cuenta.md), y no a una pérdida.
- El cálculo de la retención es del motor de impuestos de quien paga, con sus mínimos y sus certificados de exclusión ([certificados de exclusión](../../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md#certificados-de-exclusión)).
- Los cheques y su fecha de acreditación son de la tesorería ([qué tiene que modelar un sistema de gestión](../../Tesoreria/tesoreria-en-argentina.md#qué-tiene-que-modelar-un-sistema-de-gestión)).

> [!NOTE]
> Sin fuente todavía:
> - Los códigos de `FEParamGetTiposIva` para el 2,5 % y el 5 %. Se buscaron en los manuales WSFEv1, WSMTXCA y WSBFEV1, en la página de tablas de factura electrónica y en la RG 4597; ninguno publica la tabla de alícuotas.
> - Los datos que lleva el certificado de retención. Se buscaron en la RG 830 y en la RG 5762, que remiten a SICORE (RG 2233) y SIRE (RG 3726), no leídas.
> - El régimen vigente de AGIP y sus montos mínimos. Se buscó una resolución posterior a la 296/2019 en el sitio de AGIP, cuyo contenido carga por JavaScript, sin resultado.
> - Una regla de la Comisión Arbitral sobre en qué jurisdicción se percibe. Se leyeron sus resoluciones generales de 2020 a 2026 que tratan percepciones o sustento territorial; ninguna la fija, y falta el ordenamiento actualizado.
> - El valor actualizado de los tramos de facturación de las editoriales, que sigue al límite de ventas de las medianas empresas Tramo 2 de servicios; no se buscó la resolución de ese límite.
> - Cómo se cancela la factura del cliente con el certificado de una retención sufrida.
