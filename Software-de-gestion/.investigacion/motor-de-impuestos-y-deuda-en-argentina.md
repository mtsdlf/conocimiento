Fecha de lectura: 2026-11-27. Material de alto riesgo (ley).

Lo que no encontré o no pude leer entero está declarado como hueco. Dos afirmaciones de las preguntas no se pudieron confirmar y las marco abajo:

- **IDs de IVA 8 y 9:** el manual WSFEv1 no los lista, y los códigos 8 = 5 % y 9 = 2,5 % quedan como hueco.
- **SIRPEI:** no es un régimen de ventas internas sino de importaciones.

## Resumen para el motor y la deuda

- **IVA por alícuota.** La alícuota general es 21 %, la reducida es la mitad (10,5 %) y la incrementada es 27 %. Existen 2,5 % y 5 % solo para editoriales (Ley IVA, artículo sin número a continuación del art. 28).
- **Redondeo en WSFEv1.** El manual no exige cálculo al centavo. La tolerancia es 0,01 % relativo o 0,01 absoluto, y en los arreglos se multiplica por la cantidad de alícuotas o tributos.
- **Factura B.** El IVA va incluido, pero el motor sigue calculando neto y alícuota por renglón. La RG 5614 exige mostrar «IVA Contenido» y «Otros Impuestos Nacionales Indirectos».
- **Percepción de IIBB.** La alícuota sale de un padrón por CUIT que publica cada fisco. Cada padrón trae una alícuota fuera de padrón (ARBA 6 %, AGIP 6 %).
- **Deuda.** La retención se practica al pagar y se entrega un comprobante o certificado. El cobro es factura menos retenciones y el comprobante es el respaldo.

## 1. Alícuotas de IVA (Ley 23.349, t.o. 1997, art. 28)

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Ley IVA t.o. 1997 (Decreto 280/97), texto InfoLEG actualizado, copia alojada en unc.edu.ar | https://www.unc.edu.ar/sites/default/files/LEY-23349%20-texto-ordenado-dcto-280-1997.pdf | Primaria (copia del texto InfoLEG) | 2 | 3 | 2 | 3 | [L] art. 28 y el artículo siguiente |

Sobre la fuente:
- No pude abrir argentina.gob.ar ni InfoLEG directamente (HTTP 500 en la norma).
- La copia no trae fecha de corte visible. Los montos de facturación de editoriales ($63.000.000 / $126.000.000) pueden estar actualizados por decreto y hay que cotejarlos.

Afirmaciones, todas de la misma fuente:
- Art. 28: «La alícuota del impuesto será del veintiuno por ciento (21%).»
- Incrementada: «Esta alícuota se incrementará al veintisiete por ciento (27%) para las ventas de gas, energía eléctrica y aguas reguladas por medidor y demás prestaciones comprendidas en los puntos 4, 5 y 6, del inciso e) del artículo 3º, cuando la venta o prestación se efectúe fuera de domicilios destinados exclusivamente a vivienda o casa de recreo o veraneo […] y el comprador o usuario sea un sujeto categorizado en este impuesto como responsable inscripto o se trate de sujetos que optaron por el Régimen Simplificado».
- Reducida: «Estarán alcanzados por una alícuota equivalente al cincuenta por ciento (50%) de la establecida en el primer párrafo», es decir 10,5 %. Aplica a:
  - Animales vivos de ganado bovino, ovino, camélido y caprino, y sus carnes (inc. a, 1 y 2).
  - Frutas, legumbres y hortalizas frescas, miel a granel, granos y legumbres secas, harina de trigo y pan (inc. a, 3 a 7).
  - Labores agrícolas (inc. b).
  - Obras y construcciones destinadas a vivienda (inc. c).
  - Intereses y comisiones de préstamos de entidades de la Ley 21.526 a responsables inscriptos (inc. d).
  - Bienes de las planillas anexas (inc. e y f).
  - Transporte de pasajeros (inc. h).
- «Facúltase al Poder Ejecutivo para reducir hasta en un veinticinco por ciento (25%) las alícuotas».
- El 2,5 % y el 5 % salen del artículo sin número a continuación del art. 28 (incorporado por Ley 26.982). Son solo para editoriales: diarios, revistas y publicaciones periódicas, y espacios publicitarios en ellos.
  - Ventas de diarios y revistas, para quien produce la edición: «Igual o inferior a $ 63.000.000 … 2,5%», «Superior a $ 63.000.000 e igual o inferior a $ 126.000.000 … 5%», «Superior a $ 126.000.000 … 10,5%».
  - Espacios publicitarios, para el editor: 2,5 %, 10,5 % y 21 % con los mismos tramos.
  - La alícuota se recalcula cada cuatrimestre sobre la facturación de los 12 meses anteriores sin IVA.
  - El primer párrafo del artículo fija el 50 % de la general (10,5 %) para ventas de diarios y revistas.
- Hay una sola fuente: la ley. Para la tasa vigente hoy, un segundo texto consolidado en InfoLEG sería lo correcto.

## 2. Manual WSFEv1 (RG 4291, v4.8)

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Manual del desarrollador WSFEv1 «RG 4291 – Proyecto FE v4.8» (121 págs.) | https://www.arca.gob.ar/fe/ayuda/documentos/wsfev1-RG-4291.pdf | Primaria | 3 | 3 | 3 | 3 | [L] por pdftotext. El PDF tiene fecha de creación 27-08-2026. Copia local en `.../scratchpad/ar-fe/wsfev1.pdf` y `w.txt`. |

Arreglo `AlicIva` (Id, BaseImp, Importe):
- Estructura: «IVA: Detalle de alícuotas relacionadas con el comprobante». Los campos son `Id` Int(2) «Código de tipo de iva. Consultar método FEParamGetTiposIva», `BaseImp` Double(13+2) y `Importe` Double(13+2).
- Código 10022: «El campo Id en AlicIVA no debe repetirse. Deberá totalizarse por alícuota.»
- Código 10018: «Si <ImpIVA> es igual a 0 los objetos <IVA> y <AlicIva> solo deben informarse con ImpIVA = 3 (iva 0). Si <ImpIVA> es mayor a 0 el objeto <IVA> y <AlicIva> son obligatorios.» No aplica a comprobantes tipo C.
- Código 10020: `BaseImp` es obligatorio y mayor a 0. Excepto para comprobantes 2, 3, 7, 8, 52 y 53, donde puede ser cero o no informarse.
- Código 10021: `Importe` es obligatorio y mayor o igual a 0. Tiene la misma excepción.
- Código 10019: «Siempre que se informe Id, debe ser un valor devuelto por el método FEParamGetTiposIva.»

IDs de alícuota:
- El manual no lista la tabla. `FEParamGetTiposIva` devuelve `IvaTipo` con Id, Desc, FchDesde y FchHasta.
- Los ejemplos del manual confirman: `Id 3` = 0 %, `Id 4` = 10,5 %, `Id 5` = 21 % y `Id 6` = 27 %.
- Los Id 8 = 5 % y 9 = 2,5 % son hueco.

Importes y total:
- Código 10048: «“Importe Total” <ImpTotal>, debe ser igual a la suma de ImpTotConc + ImpNeto + ImpOpEx + ImpTrib + ImpIVA».
- Para comprobantes C, `ImpTotal` = `ImpNeto` + `ImpTrib`.
- `ImpIVA`: «Suma de los importes del array de IVA».
- `ImpTotConc` es el neto no gravado, `ImpNeto` el neto gravado y `ImpOpEx` el exento. Los tres deben ser mayores o iguales a cero. En C, `ImpTotConc` y `ImpOpEx` deben ser 0.
- Código 10061: «La suma de los campos <BaseImp> en <AlicIva> debe ser igual al valor ingresado en ImpNeto».
- Código 10023: la suma de los `Importe` del IVA debe ser igual a `ImpIVA`.
- Código 10051: «Los importes informados en AlicIVA se deben corresponder según el tipo de iva seleccionado». Es la regla Importe = BaseImp × alícuota.

Tolerancia, literal en 10023, 10048, 10051, 10061 y 10029:
- «Error relativo porcentual deberá ser <= 0.01% o el error absoluto <=0.01».
- En 10023, 10061 y 10029 se agrega «* cantidad de alícuotas de IVA ingresadas *» (en 10029, «* cantidad de tributos *»). En 10048 y 10051 la tolerancia es 0,01 sin multiplicador.
- Código 10056: los importes deben informarse «con la precisión indicada». Son 13 enteros y 2 decimales.

Arreglo `Tributos`:
- Campos: `Id` Int(2) «Código tributo según método FEParamGetTiposTributos», `Desc` String(80), `BaseImp`, `Alic` Double(3+2) e `Importe`.
- Código 10042: `Desc` es obligatorio cuando `Id` = 99.
- Código 10024: si `ImpTrib` es 0, `Tributos` no se envía. Si es mayor a 0, el arreglo es obligatorio.
- Código 10029: la suma de los importes de `Tributo` debe ser igual a `ImpTrib`.
- `FEParamGetTiposTributos` devuelve Id, Desc, FchDesde y FchHasta. El manual no lista los tipos ni sus códigos, así que la clasificación (nacional, provincial, municipal, interno, percepción de IIBB) es hueco.
- El ejemplo 9620 del manual muestra «importes de Tributos (IIBB)».

Ejemplo del manual (A con 21 % y 10,5 %):
- Renglón 1: neto 100,00 y IVA 21,00. Renglón 2: neto 50,00 y IVA 5,25.
- Tributo: base 150,00, 5,2 %, importe 7,80.
- Totales: neto 150,00, IVA 26,25, tributos 7,80, total 184,05.

Receptor: `CondicionIVAReceptorId` figura «obligatorio conforme lo reglamentado por la Resolución General N° 5616», sin fecha en esa celda. Ya está en la base.

## 3. Factura A frente a B (RG 5614/2024, Ley 27.743)

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| RG ARCA 5614/2024, texto original (B.O. 13-12-2024) | https://www.argentina.gob.ar/normativa/nacional/norma-407183/texto | Primaria | 3 | 3 | 2 | 3 | [L] |
| Manual WSFEv1 (arriba) | https://www.arca.gob.ar/fe/ayuda/documentos/wsfev1-RG-4291.pdf | Primaria | | | | | [L] |

- Considerandos de la RG 5614: «el artículo 99 de la Ley N° 27.743 […] estableció para todos aquellos sujetos que realicen ventas, locaciones de obra o prestaciones de servicios a consumidores finales, la obligación de detallar en las facturas o tickets […] el importe discriminado del impuesto al valor agregado y de los demás impuestos nacionales indirectos que incidan en los precios».
- Art. 2, punto 5 de la RG 5614 (sustituye el Anexo II, Título IV, a, de la RG 1415). Para el emisor responsable inscripto:
  - Hacia inscriptos o monotributistas, se discrimina alícuota, monto del impuesto, restantes tributos y percepción.
  - «De tratarse de operaciones gravadas efectuadas con sujetos exentos, no alcanzados o consumidores finales frente al impuesto al valor agregado deberá discriminarse el impuesto que recae sobre la operación.» Es el 2.
- Art. 2, punto 7, inciso g, abajo a la izquierda del comprobante: título «Régimen de Transparencia Fiscal al Consumidor (Ley 27.743)», luego «IVA Contenido» y luego «Otros Impuestos Nacionales Indirectos», cada uno con su valor.
- Art. 6: grandes empresas desde el 1-1-2025, con IVA e impuestos internos. El resto podía discriminar desde el 1-1-2025 y es obligatorio «a partir del 1 de abril» de 2025.
- Qué le cambia al cálculo por línea. Es mi lectura, no está en una sola norma:
  - La RG exige mostrar el IVA contenido, no esconderlo. El precio al consumidor sigue incluyendo IVA.
  - El WS sigue pidiendo neto y alícuotas. El manual trae un ejemplo de «Factura B con Importe Gravado y alícuota de IVA al 21 %» con `AlicIva` (sección 9521).
  - El motor debe poder calcular neto = precio / (1 + alícuota) y el IVA por diferencia, agrupado por alícuota, y de ahí sacar el «IVA Contenido» del pie.
  - «Otros Impuestos Nacionales Indirectos» (por ejemplo, impuestos internos) es un segundo agregado del pie, aparte del IVA.
- Hueco: no leí la RG 1415 ni la Ley 27.743 primaria. El art. 99 de la Ley 27.743 llega solo a través de los considerandos de la RG 5614. Las notas periodísticas que aparecieron son secundarias y no las uso.

## 4. Percepciones de IIBB por padrón

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| ARBA RN 2/2013 con modificaciones (incluye arts. 344 y 411 de la DN B 1/04) | https://web.arba.gov.ar/sites/default/files/2024-03/RN%202-2013.pdf | Primaria | 3 | 3 | 2 | 2 | [L] las partes de percepción |
| ARBA RN 38/2025 | https://www.arba.gov.ar/archivos/Tramites/RN%2038-2025.pdf | Primaria | 3 | 2 | 1 | 2 | [L] parcial (art. 1 a 3) |
| AGIP Res. 296/2019, Anexo I (Texto unificado) | https://documentosboletinoficial.buenosaires.gob.ar/publico/PE-RES-MEFGC-AGIP-296-19-ANX.pdf | Primaria | 3 | 3 | 2 | 3 | [L] las partes citadas; el PDF es de nov. 2019 |
| Comisión Arbitral, texto actualizado SIRPEI (RG 6/2020 y 6/2025) | https://www.ca.gob.ar/resoluciones/ta/Texto_atualizado_acapite_SIRPEI.pdf | Primaria | 3 | 2 | 1 | 2 | [L] |

ARBA, alícuota por cliente:
- Fuente: RN 2/2013, art. 34, que sustituye el art. 344 de la DN B 1/04.
- Se aplica «la alícuota que con relación a cada contribuyente en particular se consignará en el padrón de contribuyentes que la Autoridad de Aplicación publicará en su página web».
- La tabla de grupos es 0,00 / 0,10 / 0,15 / 0,20 / 0,30 / 1,50 / 2,50 / 2,60 / 2,70 / 3,00 / 3,20 / 3,50 / 4,00 / 5,00 / 6,00 %.
- El padrón se actualiza mensualmente, con al menos 7 días hábiles de antelación.
- El agente consulta con su CUIT y CIT, y existe consulta en lote.
- Proveedores de luz, gas, agua, cloacas y telecomunicaciones usan un padrón trimestral.
- Cliente fuera del padrón: 6 % «siempre que […] la entrega o realización tenga lugar en jurisdicción de la Provincia de Buenos Aires».
- Si el padrón no se puede consultar porque el sitio está caído todo el día, se aplica 3 %. También 3 % en Venta Directa.
- Con la consulta en lote, un cliente sin alícuota informada lleva 6 %.
- Excluidos, art. 32 de la RN 2/2013 (art. 322 de la DN B 1/04): Estado y municipios, sujetos no alcanzados, y quienes tienen alícuota 0 por certificado (RN 64/10).
- RN 38/2025: ARBA ofrece un mecanismo alternativo, a pedido del contribuyente, para bajar sus alícuotas en los regímenes con padrón.
- Hueco: el monto mínimo y la base de cálculo (art. 342) de ARBA no los leí. Los artículos 342 y 322 son de la DN B 1/04, que no bajé. Declaro la base «neto» solo para AGIP.

AGIP (CABA):
- Fuente: Res. 296/2019, Anexo I.
- Art. 60: los agentes aplican la alícuota del «Padrón de Regímenes Generales» publicado en www.agip.gob.ar, también para contribuyentes de Convenio Multilateral.
- Art. 65: grupos de 0,00 / 0,01 / 0,10 / 0,20 / 0,50 / 0,75 / 1,00 / 1,50 / 2,00 / 2,50 / 3,00 / 3,50 / 4,00 / 4,50 / 5,00 / 6,00 %.
- Art. 66: sin padrón y sin acreditar inscripción, 6 %, y se considera hecha en CABA la venta o prestación materializada dentro de ella.
- Art. 67: «alícuota general de percepción en 3,5 %» y retención 3 %.
- Art. 32: «la percepción al emitirse la factura o documento equivalente».
- Art. 33: se percibe «sobre el monto de la operación», detrayendo los conceptos del art. 229, inc. 1 del Código Fiscal, y solo si están discriminados en la factura. El texto de ese inciso no lo leí.
- Art. 34: «monto mínimo sujeto a percepción» de $500 y a retención de $3.000. Son valores de 2019, probablemente desactualizados.
- Art. 52: excluye las ventas a consumidores finales de los regímenes de percepción.
- Art. 53: excluye los bienes de uso, con declaración por escrito del comprador y la leyenda «Bien a ser afectado como bien de uso».
- Art. 54: la factura con el impuesto percibido discriminado es la constancia.
- Art. 50, inc. e: excluye las operaciones realizadas fuera de CABA por contribuyentes inscriptos exclusivamente en otra jurisdicción, y por Convenio Multilateral sin la jurisdicción 901.
- Art. 61: la alícuota considera, entre otros datos, el coeficiente unificado de CABA para Convenio Multilateral.
- Art. 57 a 59, Factura de Crédito Electrónica MiPyME: el importe se consigna discriminado y se adiciona al monto a pagar.
- Art. 48 y Anexo II: quién es agente. Se fija por designación y por parámetros de magnitud (art. 3: ingresos de más de $200.000.000 el año anterior y tributo de más de $12.000.000).

Jurisdicción en venta a otra provincia:
- Ambos fiscos exigen un nexo con su territorio, no hay una regla única. ARBA mira dónde ocurre la entrega o realización. AGIP excluye lo realizado fuera de CABA por quien no tiene alta ahí.
- SIRPEI (RG CA 6/2020, texto de la Comisión Arbitral) es una percepción en aduana sobre importaciones, no para ventas internas. Cada jurisdicción informa su alícuota general e individual por contribuyente.
- Hueco: no encontré en este tramo la regla de la Comisión Arbitral para repartir una percepción interna entre jurisdicciones de un contribuyente de Convenio Multilateral. Tampoco leí la RG 6/2020 en su forma original. Hay mención de SIRCIP (RG 9/2025) como sistema para administrar padrones y alícuotas, solo vía buscador [S].
- Hueco: no leí el padrón de ARBA ni el de AGIP en formato descargable, ni su especificación de archivo.

## 5. Retenciones al pagar (lado deuda con proveedores)

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| RG 2854 (IVA), texto InfoLEG de 02/06/2016 | https://www.unc.edu.ar/sites/default/files/RG-IVA-2854.pdf | Primaria, desactualizada | 2 | 3 | 1 | 2 | [L] arts. 7 a 16 |
| RG ARCA 5762/2025 (vigente desde 01/12/2025) | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5762%7Co%3A9%7Ca%3A2025%7Cf%3A24%2F09%2F2025 | Primaria | 3 | 3 | 2 | 3 | [L] arts. 13 a 22 |
| RG 2408 (percepción IVA), texto actualizado | https://www.argentina.gob.ar/normativa/nacional/norma-137452/texto | Primaria | 3 | 2 | 1 | 3 | [L] parcial (arts. 1 a 4) |

Retención de IVA, RG 2854 (texto de 2016):
- Art. 8: la retención se calcula sobre el IVA discriminado en la factura, con 50 % para compraventa de cosas muebles y 80 % para servicios y alícuotas reducidas.
- Art. 10: si el IVA no está discriminado, se calcula sobre el IVA contenido.
- Art. 11: pagos parciales.
- Art. 12: «no corresponderá practicar retención cuando el importe a retener resulte igual o inferior a CUATROCIENTOS PESOS ($ 400.-)». Es un valor de mayo de 2016.
- Art. 14: comprobante entregado «en el momento en que se efectúe el pago y se practique la retención», con numeración propia, consecutiva y progresiva.
- Art. 16: el importe retenido «tendrá el carácter de impuesto ingresado».
- Esta RG puede haber sido modificada o reemplazada. No lo verifiqué.

RG 5762/2025 (facturas A con leyenda «OPERACIÓN SUJETA A RETENCIÓN»; sustituye a la RG 1575). Es otro régimen:
- Art. 13: IVA «el CIEN POR CIENTO (100%) de la alícuota», Ganancias el 6 % sobre esa base.
- Art. 14: la retención se practica «en el momento en que se efectúe el pago», incluidas señas y anticipos que congelen precios. Con pagos parciales la retención se imputa hasta la concurrencia del pago.
- Art. 15: se entrega «el comprobante o certificado» de SICORE (RG 2233) o SIRE (RG 3726).
- Art. 16: códigos 99 (Ganancias) y 499 (IVA) para esas facturas.
- Art. 17: la retención de IVA «tendrá […] el carácter de impuesto ingresado» y se computa en la DJ del período en que se sufrió.
- Art. 22, en el tramo de «PAGO EN CBU INFORMADA» (no «sujeta a retención»): el comprador responsable inscripto cancela «la diferencia entre el importe total facturado y las retenciones que por otros regímenes pudieran corresponder», por transferencia a la CBU informada. Si el receptor es monotributista, se cancela el total.

Percepción de IVA, RG 2408:
- Art. 1: agentes de percepción por ventas de cosas muebles (excluye bienes de uso), locaciones y prestaciones gravadas a responsables inscriptos.
- Art. 2: se calcula «sobre el precio neto de la operación que resulte de la factura […] la alícuota del TRES POR CIENTO (3%)». Es 1,50 % en operaciones con alícuota del 50 %.
- Art. 3: solo si la percepción supera $21,30. Es un valor viejo.
- El «texto actualizado» no muestra fecha de corte en lo que leí.

Secundaria [S], sin tratamiento aquí:
- La RG 5370/2023 subió un piso a $2.000, pero parece ser el régimen de medios de pago con tarjeta y no el general.

Hueco:
- No leí el texto de la RG 830 de Ganancias. Solo la citan la RG 5762 (arts. 18 y 19) y las notas de prensa.
- No leí el certificado de retención de la RG 830 ni sus montos mínimos actuales.
- Los pisos de $400 y de $2.000 siguen sin verificar.

## 6. Retenciones sufridas al cobrar

Lo que sí consta en fuente oficial:
- La retención de IVA es «impuesto ingresado» y se computa en la DJ del período en que se sufrió (RG 5762, art. 17).
- Se respalda con el comprobante o certificado de SICORE o SIRE (RG 5762, art. 15).
- Ese comprobante lleva numeración propia, consecutiva y progresiva (RG 2854, art. 14).
- En el supuesto específico de facturas «PAGO EN CBU INFORMADA», el cliente paga la factura menos las retenciones de otros regímenes (RG 5762, art. 22).

Hueco:
- No hay lectura oficial de cómo se cancela contablemente la factura del cliente con el certificado.
- Tampoco la hay de cómo ARCA muestra las retenciones sufridas (SIRE, Mis Retenciones) ni de la imputación de IIBB sufridas.
- Para el modelo, el diseño es inferencia: la factura se cancela con efectivo y certificados de retención y percepción, cada uno con su número, tipo y régimen.

## Recursos canónicos

- Ley IVA t.o. 1997: https://www.unc.edu.ar/sites/default/files/LEY-23349%20-texto-ordenado-dcto-280-1997.pdf
- Manual WSFEv1 v4.8: https://www.arca.gob.ar/fe/ayuda/documentos/wsfev1-RG-4291.pdf
- RG 5614/2024: https://www.argentina.gob.ar/normativa/nacional/norma-407183/texto
- ARBA RN 2/2013: https://web.arba.gov.ar/sites/default/files/2024-03/RN%202-2013.pdf
- AGIP Res. 296/2019 Anexo I: https://documentosboletinoficial.buenosaires.gob.ar/publico/PE-RES-MEFGC-AGIP-296-19-ANX.pdf
- RG ARCA 5762/2025: https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5762%7Co%3A9%7Ca%3A2025%7Cf%3A24%2F09%2F2025
- RG 2408: https://www.argentina.gob.ar/normativa/nacional/norma-137452/texto
- RG 2854 (2016): https://www.unc.edu.ar/sites/default/files/RG-IVA-2854.pdf

## Huecos

1. IDs 8 (5 %) y 9 (2,5 %) de `FEParamGetTiposIva`, y los tipos de `FEParamGetTiposTributos`, no están en el manual. Se necesita llamar al WS de homologación.
2. Ley 27.743 primaria y RG 1415 (anexos de facturación A/B): no leídas.
3. Base y mínimo de la percepción de ARBA (DN B 1/04, arts. 322 y 342): no leídos.
4. Mínimos y datos de AGIP vigentes: el PDF es de 2019.
5. Regla de la Comisión Arbitral para repartir una percepción interna entre jurisdicciones (Convenio Multilateral).
6. RG 830 y su certificado de retención: no leídos.
7. Pisos de retención de IVA y Ganancias vigentes en 2026.
8. Vigencia de la RG 2854 frente a la RG 5762.
9. Cancelación de la factura del cliente con las retenciones sufridas.
10. Fecha de corte de los textos «actualizados» de la Ley IVA y de la RG 2408.

Los archivos bajados están en `/tmp/claude-1000/-home-dela-repos-personal-conocimiento/cfb247c6-67ae-4161-949e-87e8ed3a86d4/scratchpad/ar-fe/`. No ejecuté nada de lo bajado ni escribí en el repo.
