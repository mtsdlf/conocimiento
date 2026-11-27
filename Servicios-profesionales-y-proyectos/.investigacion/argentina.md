# Argentina para una firma de servicios que factura proyectos

Informe de investigación para la nota aparte de Argentina del tema Servicios profesionales y proyectos. Es dinero y ley: alto riesgo. Fecha de lectura: 2026-11-27. Marcas: [L] texto leído (el artículo citado); [M] metadatos; [S] resumen secundario o del lector de páginas.

Límite de método: el WebSearch se agotó, infoleg.gob.ar devolvió 403 o «No se pudo acceder al archivo» y la Biblioteca Electrónica de ARCA devolvió error. Los textos de leyes salieron de argentina.gob.ar/normativa (Ministerio de Justicia, que republica el texto de Infoleg) y los de ARCA, de PDF y del Boletín Oficial. Cada afirmación dice con qué marca se leyó.

## Tabla de fuentes

Puntajes 1 a 3: autoridad / profundidad / ejemplos / unicidad.

| # | Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|---|
| F1 | Manual del desarrollador WSFEv1 (RG 4291), ARCA | https://www.arca.gob.ar/fe/ayuda/documentos/wsfev1-RG-4291.pdf | primaria | 3/3/2/3 | [L] tablas del campo y de validaciones |
| F2 | RG AFIP 1415/2003, copia de la UNC (con modificaciones hasta la RG 3666/2014 y la sustitución de la RG 2098/2006), art. 13 | https://www.unc.edu.ar/sites/default/files/RG-AFIP-01415-03.pdf | primaria (copia universitaria, no oficial) | 2/3/2/2 | [L] el art. 13 |
| F3 | RG ARCA 5866/2026, Boletín Oficial 29/06/2026, que reemplaza el cuadro del art. 13 de la RG 1415 | https://www.boletinoficial.gob.ar/detalleAviso/primera/343656/20260629 | primaria | 3/3/2/3 | [S] por el lector de páginas (resumen del aviso y la fila del cuadro); el PDF directo no se pudo bajar |
| F4 | RG AFIP 4291/2018, copia de la UNC | https://www.unc.edu.ar/sites/default/files/RG-AFIP-N%C2%BA-4291-2018.pdf | primaria (copia no oficial) | 2/2/1/2 | [L] parcial: la regla de transferencia de datos; no encontré ahí el cuadro de emisión |
| F5 | Ley 23.928, texto actualizado | https://www.argentina.gob.ar/normativa/nacional/norma-328/actualizacion | primaria | 3/3/1/3 | [L] arts. 7 y 10 con sus notas |
| F6 | DNU 70/2023, Boletín Oficial 21/12/2023 (PDF de 89 páginas) | https://www.boletinoficial.gob.ar/pdf/aviso/primera/301122/20231221 | primaria | 3/3/2/3 | [L] arts. 250 a 257 (CCyC) y búsqueda de «23.928» |
| F7 | Allende & Brea, Modificaciones al CCyC por el DNU 70/2023 | https://allende.com/reforma-argentina/desregulacion-economica/modificaciones-al-codigo-civil-y-comercial-de-la-nacion-01-03-2024/ | secundaria | 2/2/2/1 | [S] |
| F8 | Ley 27.423, texto actualizado | https://www.argentina.gob.ar/normativa/nacional/norma-305057/actualizacion | primaria | 3/3/3/3 | [L] arts. 1, 2, 4, 5, 6, 16, 19, 31, 51, 58 y tablas |
| F9 | Decreto DNU 2284/1991, texto actualizado | https://www.argentina.gob.ar/normativa/nacional/norma-7539/actualizacion | primaria | 3/3/2/3 | [L] arts. 8 a 11 y considerandos |

F7 parafrasea la misma norma que F6: cuenta como una sola fuente para lo que el DNU dice.

## 1. Factura de servicios en la factura electrónica

### 1.a Datos propios del concepto «Servicios»

- El campo `Concepto` admite 1 Productos, 2 Servicios y 3 Productos y Servicios. Con 2 o 3 hay tres fechas obligatorias. [L] F1
  - `FchServDesde`: «Fecha de inicio del abono para el servicio a facturar. Dato obligatorio para concepto 2 o 3 (Servicios / Productos y Servicios). Formato yyyymmdd».
  - `FchServHasta`: «Fecha de fin del abono para el servicio a facturar. [...] FchServHasta no puede ser menor a FchServDesde».
  - `FchVtoPago`: «Fecha de vencimiento del pago servicio a facturar. Dato obligatorio para concepto 2 o 3 [...] o Facturas del tipo MiPyMEs (FCE). Formato yyyymmdd. Debe ser igual o posterior a la fecha del comprobante».
- Errores de la tabla de validaciones: 10031, 10033 y 10035 (si se informa una de las tres hay que informar las otras), 10032 (desde posterior a hasta), 10036 (vencimiento «no puede ser anterior a la fecha del comprobante»), 10049 (obligatorias si `Concepto` es 2 o 3). [L] F1
- El manual llama «abono» al período del servicio. Para un proyecto sin período natural, lo razonable es informar el período de la prestación que se factura; es inferencia mía, el manual no lo dice.
- Una sola fuente para este punto (el manual de ARCA). El artículo de la RG 4291 que crea esos datos no se leyó.

### 1.b Cuándo hay que emitir la factura de un servicio

- RG 1415, art. 13 (copia UNC): para «Prestaciones de servicios y locaciones de obras y servicios», la operación se entiende realizada «cuando se concluya la prestación o ejecución, o se perciba —en forma total o parcial— el precio, lo que fuera anterior». La copia anota «Artículo sustituido por art. 1° de la Resolución General N° 2098/2006». [L] F2
- La RG ARCA 5866/2026 reemplazó el cuadro del art. 13 y rige desde el 1 de julio de 2026. Su fila de servicios y de obras dice: «Día en que se concluya la prestación o ejecución o en que se perciba -en forma total o parcial- el precio». [S] F3
- Servicios continuos: F2 los define como los que «no poseen un plazo expreso de finalización» y dice que, si superan el mes calendario, la obligación de emitir «nacerá a la finalización de cada uno». F3 pone en la fila de continuos «Último día de cada mes calendario» (salvo cobro o conclusión anteriores). Las redacciones difieren; la de F3 es posterior pero se leyó por resumen. [L] F2, [S] F3
- F2 y F3 coinciden en lo central (lo que ocurra primero: concluir la prestación o cobrar algo del precio), pero son el mismo artículo en dos redacciones, no dos fuentes independientes.
- La RG 4291 permite que la transferencia de datos a ARCA esté dentro de los 10 días corridos anteriores o posteriores a la fecha del comprobante en prestaciones de servicios (5 días en el caso general). [L] F4. No identifiqué el número del artículo.
- Consecuencia para proyectos con hitos o anticipos: cobrar un anticipo, aunque sea parcial, hace nacer la obligación de facturar. Es lectura directa de «en forma total o parcial», sin doctrina que la confirme.

## 2. Honorarios con arancel

- Decreto DNU 2284/1991, art. 8: «Déjanse sin efecto las declaraciones de orden público establecidas en materia de aranceles, escalas o tarifas que fijen honorarios, comisiones o cualquier otra forma de retribución de servicios profesionales, no comprendidos en la legislación laboral o en convenios colectivos de trabajo, en cualquier clase de actividad». El art. 11 prohíbe que una entidad pública o privada impida «la libre contratación de honorarios [...] cuando las partes deseen apartarse de las escalas vigentes». El art. 10 deja a los peritos de oficio con los honorarios regulados en el proceso. [L] F9. Es la norma general que desreguló los mínimos de las profesiones (arquitectos, ingenieros, contadores y otros). No verifiqué qué normas posteriores la modificaron ni las leyes provinciales de colegios.
- Ley 27.423 (abogados, procuradores y auxiliares de la Justicia): el art. 1 la limita a «asuntos cuya competencia correspondiere a la justicia nacional o federal». [L] F8
  - UMA (art. 19): «equivaldrá al tres por ciento (3 %) de la remuneración básica asignada al cargo de juez federal de primera instancia»; la Corte Suprema publica el valor cada mes. [L] F8
  - Hay mínimos en UMA, también para la labor extrajudicial (consulta verbal 0,5; redacción de contrato de locación, mínimo 2; de estatuto de sociedades, mínimo 5). Art. 16: «Los jueces no podrán apartarse de los mínimos establecidos en la presente ley, los cuales revisten carácter de orden público». [L] F8
  - Art. 4: se puede pactar el monto con el cliente «sin otra sujeción que a esta ley y al Código Civil y Comercial». Art. 5: la renuncia anticipada y el pacto «que tienda a reducir las proporciones establecidas en el arancel» son nulos de nulidad absoluta, con excepciones (familiares, pro bono). El párrafo siguiente (falta de ética) lleva la nota «Párrafo observado por art. 1° del Decreto N° 1077/2017». [L] F8
  - Art. 6: pacto de cuotalitis, hasta el 30% del resultado (40% si el profesional toma a su cargo gastos y costas). [L] F8
- Tensión que la nota tiene que decir: el DNU 2284/91 desreguló los mínimos «en cualquier clase de actividad», pero la Ley 27.423 (2017, posterior) declara los suyos de orden público. No encontré análisis jurídico que concilie las dos para el trabajo extrajudicial de un abogado con un cliente privado. Lo cierto es el ámbito judicial nacional y federal; lo demás queda sin verificar.
- Arquitectos e ingenieros: no se leyó ninguna norma específica. Solo vale lo general del DNU 2284/91. Hueco.

## 3. Ajuste de precios en contratos largos con inflación

- Ley 23.928, art. 7 (sustituido por art. 4 de la Ley 25.561, B.O. 7/1/2002): «El deudor de una obligación de dar una suma determinada de pesos cumple su obligación dando el día de su vencimiento la cantidad nominalmente expresada. En ningún caso se admitirá actualización monetaria, indexación por precios, variación de costos o repotenciación de deudas, cualquiera fuere su causa, haya o no mora del deudor, con las salvedades previstas en la presente ley. Quedan derogadas las disposiciones legales y reglamentarias y serán inaplicables las disposiciones contractuales o convencionales que contravinieren lo aquí dispuesto». [L] F5
- Art. 10 (mismo origen): mantiene derogadas las normas que establecen o autorizan «la indexación por precios, actualización monetaria, variación de costos o cualquier otra forma de repotenciación de las deudas, impuestos, precios o tarifas de los bienes, obras o servicios», y dice que no puede «aplicarse ni esgrimirse ninguna cláusula legal, reglamentaria, contractual o convencional» como causa de ajuste en las sumas de pesos. [L] F5
- Los arts. 8 y 9 están derogados por el art. 3 de la Ley 25.561. [L] F5
- Infoleg anota excepciones puntuales en notas (leyes 27.798 art. 62, B.O. 2/1/2026; 27.701 arts. 51 y 52; 27.591 art. 57; 27.467 art. 105; decretos sobre deuda pública, valores negociables y operaciones financieras con CER). No leí el contenido de esas leyes, solo la nota; no parecen regla general para servicios entre privados. [L] F5, solo las notas.
- DNU 70/2023: no modificó los arts. 7 y 10. En todo el PDF la única mención de la Ley 23.928 es el art. 257, que en el art. 1199 del CCyC (locación de inmuebles) permite ajustar con «cualquier índice» y dice «No será de aplicación a los contratos incluidos en este Capítulo el artículo 10 de la Ley N° 23.928». [L] F6. Que el DNU escriba esa excepción solo para locaciones sugiere que, fuera de ellas, el art. 10 sigue rigiendo (inferencia mía, sin análisis jurídico leído).
- Lo que el DNU sí cambió y sirve para servicios [L] F6:
  - Art. 765 CCyC: se puede deber dinero en moneda «sea o no de curso legal en el país»; «El deudor solo se libera si entrega las cantidades comprometidas en la moneda pactada. Los jueces no pueden modificar la forma de pago o la moneda pactada por las partes».
  - Art. 766: se debe la especie designada, tenga o no curso legal.
  - Art. 958: libertad de contratación; las normas legales son supletorias salvo las expresamente imperativas, con interpretación restrictiva.
  - Art. 960: «Los jueces no tienen facultades para modificar las estipulaciones de los contratos, excepto que sea a pedido de una de las partes cuando lo autoriza la ley».
- F7 (secundaria) dice que el DNU solo cambió el contrato nominado de locación y no los de obra y servicios.
- La práctica de las cláusulas de ajuste (por índice, por paritaria, por dólar, revisión periódica del valor hora): no encontré fuente primaria ni jurídica seria que diga qué se admite hoy entre privados. Lo que sí dicen las normas leídas: el ajuste en pesos por índice choca con el texto de los arts. 7 y 10; el pacto en moneda extranjera tiene respaldo expreso en los arts. 765 y 766 actuales; nada de lo leído prohíbe que las partes acuerden un precio nuevo para el tramo siguiente (inferencia). La nota debe presentarlo como lectura de la norma, no como práctica verificada, y mandar a consultar con un abogado.
- Imprevisión (art. 1091 CCyC): no se releyó acá; la nota `contrato-de-servicio.md` ya lo trata. No está entre los artículos sustituidos que vi en el DNU.

## 4. Retenciones que sufre quien factura servicios

- Ganancias, RG 830 de AFIP (2000): régimen de retención sobre pagos por locaciones de obra y servicios, honorarios y otros conceptos. No verificado: la Biblioteca Electrónica de ARCA devolvió error y no hallé otra copia; el nombre y el contenido salen de mi conocimiento previo, sin fuente leída. Alícuotas, montos no sujetos y modificaciones: tema Impuestos.
- Ingresos Brutos: retenciones y percepciones provinciales con padrón por contribuyente. Ninguna norma leída; se nombra sin cita.
- IVA, retenciones de IVA y seguridad social: no investigados.
- La clase M se reemplazó por la A con la leyenda «OPERACIÓN SUJETA A RETENCIÓN» (RG 5762/2025): ya está en `Comercio-electronico/Normativa/factura-electronica-de-arca.md`.

## Recursos canónicos propuestos

| Tema | Recurso | Parte | En qué fijarse |
|---|---|---|---|
| Datos de la factura de servicios | Manual WSFEv1 de ARCA (F1) | Tabla del detalle del comprobante y tabla de validaciones | Las tres fechas, errores 10031 a 10049; la versión del manual cambia (ver la nota de factura electrónica) |
| Momento de emisión | RG 1415 art. 13 con el cuadro de la RG 5866/2026 | Fila de servicios y obras y la de continuos | Leer la RG 5866 completa en el Boletín Oficial |
| Honorarios | Ley 27.423 (F8) | Arts. 4 a 6, 16, 19 y tablas | Ámbito nacional y federal; mínimo de orden público |
| Desregulación | DNU 2284/91 (F9) | Arts. 8 a 11 | Si la profesión tiene norma posterior |
| Indexación | Ley 23.928 arts. 7 y 10 (F5); CCyC arts. 765, 766, 960 (F6) | | Excepciones solo para locaciones y deuda pública |

## Huecos

1. Texto de la RG 4291 en el artículo que crea los datos de servicios: no leído; las fechas de servicio tienen una sola fuente (el manual).
2. RG 5866/2026 completa: el lector dio un resumen; falta la redacción exacta de servicios continuos y el plazo de entrega. La copia UNC de la RG 1415 es previa al cuadro nuevo.
3. Estado actual del DNU 2284/91 profesión por profesión y leyes de aranceles de arquitectos, ingenieros, contadores y provincias: no leídas.
4. Conciliación entre el DNU 2284/91 art. 8 y la Ley 27.423 art. 16 en lo extrajudicial: sin análisis jurídico. El alcance del Decreto 1077/2017 sobre el art. 5 no se leyó.
5. Práctica y jurisprudencia de cláusulas de ajuste en servicios entre privados después de 2023: sin fuente. Las leyes 27.798, 27.701, 27.591 y 27.467 (excepciones anotadas por Infoleg) no se leyeron.
6. RG 830 de Ganancias e Ingresos Brutos: ningún texto leído.
7. IVA, retenciones de IVA y seguridad social: no investigados.
