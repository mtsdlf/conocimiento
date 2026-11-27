# Investigación: lo de Argentina para la tesorería (vigente a noviembre de 2026)

Fecha de lectura: 2026-11-27. Capa cruda, sin frontmatter. Marcas: [L] leído el texto completo o la parte citada, [M] metadatos o resumen del extractor de páginas, [S] resumen secundario.
Puntajes 1 a 3 en autoridad / profundidad / ejemplos / unicidad.

Nota de método: la cuota de búsquedas web se agotó a mitad del trabajo (200 por sesión, compartidas). Lo que sigue sale de buscar al principio y de leer después fuentes primarias por URL directa. Los PDF del BCRA se bajaron y se leyeron con pdftotext (marca [L]). Lo que no se pudo leer está en «Huecos».

## 0. Fuentes (tabla)

| # | Fuente | Tipo | Aut/Prof/Ej/Uni | Marca | URL |
|---|---|---|---|---|---|
| F1 | BCRA, texto ordenado «Sistema Nacional de Pagos – Cheques y otros instrumentos compensables», al 23/07/2026 (última comunicación A 8458) | primaria | 3/3/2/3 | [L] parcial (secciones 2.3.2, 3.4, 3.5) | https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-cheq.pdf |
| F2 | BCRA, «ECHEQ o Cheque Electrónico» (sin fecha; copyright 2006-2025) | primaria | 3/2/1/2 | [L] | https://www.bcra.gob.ar/echeq-o-cheque-electronico/ |
| F3 | BCRA, «Emitir un cheque y usar ECHEQ de forma correcta» (sin fecha) | primaria | 3/1/1/1 | [L] | https://www.bcra.gob.ar/emitir-un-cheque-y-usar-echeq/ |
| F4 | Ministerio de Justicia, Derecho Fácil, «Cheque» (sin fecha) | primaria (divulgación oficial) | 3/1/1/1 | [L] | https://www.argentina.gob.ar/node/159422 |
| F5 | BCRA, texto ordenado «Sistema Nacional de Pagos – Transferencias», versión citada A 8295, al 07/08/2025 (la sección 2 en su versión A 8176, vigencia 15/01/2025) | primaria | 3/3/2/3 | [L] sección 2 y 1.2.3 | https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-tr.pdf |
| F6 | BCRA, texto ordenado «Transferencias – Normas complementarias», al 08/09/2026 (última comunicación A 8477; secciones 3 y 6 por A 8399, vigencia 13/02/2026) | primaria | 3/3/2/3 | [L] secciones 3.4, 6 | https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-tr-nc.pdf |
| F7 | BCRA, texto ordenado «Exterior y cambios», al 14/09/2026 (última comunicación A 8481, vigencia 15/09/2026) | primaria | 3/3/2/3 | [L] secciones 3.10 y 10.3 a 10.4 | https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-excbio.pdf |
| F8 | BCRA, API de Estadísticas Monetarias v4.0 (valores al 25-26/11/2026; inflación a oct-2026) | primaria (datos) | 3/2/3/3 | [L] | https://api.bcra.gob.ar/estadisticas/v4.0/monetarias |
| F9 | MAV (Mercado Argentino de Valores), portada con «Datos de Mercado» (instantánea del 26/11/2026, deducida de los vencimientos) | primaria (mercado) | 2/2/3/3 | [L] las tablas; [M] la rotulación de cada pestaña | https://www.mav-sa.com.ar/ |
| F10 | BCRA, Boletín Estadístico octubre 2026 (14/10/2026) | primaria | 3/1/1/1 | [L] solo el índice de series; no trae los valores en el texto | https://www.bcra.gob.ar/archivos/Pdfs/PublicacionesEstadisticas/BoletinEstadistico/boldat202610.pdf |
| F11 | Criteria / iProfesional, «El descuento de cheques de pago diferido es ideal para las pymes» (24/01/2023) | secundaria | 1/2/2/1 | [M] | https://www.iprofesional.com/tecnologia/376420-el-descuento-de-cheques-de-pago-diferido-es-ideal-para-las-pymes |
| F12 | Banco de la Nación Argentina, «Crédito: cheques y ECHEQs» para pymes (sin fecha, condiciones modificables por el banco) | primaria (oferta de un banco) | 2/1/1/1 | [M] | https://bna.com.ar/Empresas/Pymes/CreditoChequesyEcheqs |
| F13 | BCRA, Comunicación A 8438 del 15/05/2026 (actualiza «Cheques y otros instrumentos compensables») | primaria | 3/1/1/1 | [L] encabezado | https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8438.pdf |
| F14 | Enlace interno: cifras de ECHEQ de septiembre de 2026 y FCE | repo | | [L] | `Comercio-electronico/Comercio-B2B/cuenta-corriente-y-credito.md` |
| F15 | Enlace interno: Transferencias 3.0 y QR | repo | | [L] | `Comercio-electronico/Pagos/medios-de-pago-locales.md` |

## 1. Cheque y ECHEQ (medios de cobro y pago)

Frontera: Comercio-B2B/cuenta-corriente-y-credito.md ya da las cifras de compensación de septiembre de 2026 (5,1 millones de cheques, ECHEQ 66% de la cantidad y 86,2% del monto, rechazo por falta de fondos 1,7% / 1,1%) y la FCE (obligatoria desde $ 5.549.862, 21 días para aceptar). No repetir: enlazar.

Afirmaciones:
- Hay cuatro tipos de cheque: común, de pago diferido, cancelatorio y ECHEQ. [F3]
- Cheque de pago diferido: «se emite en una fecha, pero puede cobrarse en una fecha posterior (hasta 360 días)»; se presenta dentro de los 30 días «contados desde la fecha de vencimiento fijada por quien lo emitió». [F3] Dos fuentes oficiales independientes coinciden en los 360 días: Derecho Fácil dice «La fecha de pago puede ser entre 1 y 360 días a partir de que el cheque fue hecho» y «debe ser presentado en el Banco dentro de los 30 días posteriores». [F4] El texto de la ley (24.452 y el decreto-ley 4776/63 que modifica) NO se pudo leer (ver Huecos); no atribuir artículo.
- El ECHEQ «puede ser endosado, avalado, negociado, puesto en custodia, cedido y depositado electrónicamente»; solo lo emiten los titulares de cuenta corriente; para emitirlo hace falta el CUIT/CUIL/CDI del beneficiario; «todos los bancos están obligados a recibir un ECHEQ y permitir su depósito»; se le aplican las normas del cheque en papel salvo incompatibilidad. [F2]
- Endosos: F2 dice «Se permiten endosos sin límite»; el texto ordenado de cheques (F1) tiene un motivo de rechazo R11 «Excede el límite de endosos establecido» para cheques compensables en papel. Son dos regímenes: el límite de endosos es del cheque físico; el ECHEQ no lo tiene. (Inferencia mía a partir de F1 y F2; verificar en F1 la sección del límite).
- «Endoso para Negociación» lleva el ECHEQ al mercado bursátil a través de una infraestructura autorizada por el BCRA y la CNV. [F2]
- Rechazo y cesión: un ECHEQ rechazado puede cederse a terceros fuera de la cadena mediante la «cesión electrónica de derechos»; esa función se inhabilita una vez impresa la certificación para ejercer acciones civiles (CAC). [F2, F3]
- Acreditación del depósito: 48 horas, igual que el cheque en papel. Aceptar o desconocer el ECHEQ se puede hasta la fecha de vencimiento; anulación si el beneficiario no lo aceptó, devolución si lo aceptó. [F2]
- Cuando vence el plazo de validez legal de un ECHEQ la entidad girada lo pasa a «caducado»; el tenedor puede pedir la CAC con la leyenda «Cheque caducado». [F1, punto 3.4.5]
- El ciclo del CPD tiene dos partes: registración (sin liquidación de dinero) y pago, que empieza al vencimiento y se rige como un cheque común. [F1, punto 2.3.2]
- Los ECHEQ y su almacenamiento y compensación son infraestructuras de mercado financiero sistémicamente importantes (F1, punto 3.4.2).
- Multas: F3 dice que ante rechazo «puede haber multas o sanciones» sin montos. Los montos no se leyeron.

Qué es del tesorero (para la nota): el cheque a fecha es a la vez medio de cobro, crédito comercial y activo descontable; calendario de vencimientos de cheques recibidos y emitidos, la cartera, el rechazo como riesgo de contraparte, y que el ECHEQ lo emite solo quien tiene cuenta corriente.

## 2. Transferencias, DEBIN, débito, CBU/CVU, alias, dólares

- Las transferencias inmediatas deben estar disponibles «durante las 24 horas del día, todos los días del año»; la resolución de cada una en «no más de 15 segundos»; en pesos y en dólares estadounidenses entre cuentas de la misma moneda. [F5, 2.2.3, 2.2.9, 2.2.12]. Rige para todas las entidades financieras y los proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP). [F5, 2.2.1]
- Límites: hay un mínimo, no un máximo. «No se podrán establecer límites inferiores a los antes señalados, sin perjuicio de que podrán ser incrementados». [F5, 2.2.4] Mínimos diarios por cuenta, sin solicitud especial: push (enviar) 15.000 UVA en pesos y 12.500 dólares o euros; pull (pedir) 2.500 UVA en pesos. [F6, 6.3.2.3] Equivalencia publicada: $ 30.870.000 (push) y $ 5.145.000 (pull) «al 31/07/26»; el BCRA publica las equivalencias en marzo, julio y noviembre. [F6, 6.4] (Con la UVA del 27/11/2026, $ 2.216,40 [F8, id 31], 15.000 UVA son unos $ 33,2 millones; cuenta mía.) Esos mínimos rigen para toda cuenta, no distinguen persona humana de empresa en el texto leído; el banco puede dar más.
- Ampliación temporal: el titular puede pedir la «transferencia inmediata por monto superior (TIS)», en forma remota las 24 horas o presencial, «No deberá exigirse que la solicitud tenga una antelación superior a 1 día hábil». [F5, 2.2.4]
- Costo: el tramo inicial gratuito de transferencias minoristas es de 7.500 UVA por mes calendario, por moneda y por proveedor de cuenta, y los precios no pueden ser porcentajes del monto. [F6, 6.1 a 6.3.2.2]
- DEBIN y CREDIN: el texto vigente ya no usa esos nombres. Pasan a ser «transferencias inmediatas pull» y «push»; a las entidades se les prohíbe usar «DEBIN y CREDIN (o similares)» en lo que muestran al cliente. [F6, 2.5] El pull «permite mediante el débito de la cuenta del cliente receptor de la solicitud y luego de que éste la haya autorizado, la acreditación inmediata de los fondos en la cuenta del cliente ordenante»; la autorización puede darse una sola vez al enrolar la cuenta, salvo para cobros vinculados a préstamos; no aplica a cuentas corrientes (según el índice 3.4.2 y 3.4.x, verificar). [F6, 3.4.1]
- Transferencias en lote y MEP (Medio Electrónico de Pagos): compensación en 24 horas en pesos y 48 horas en moneda extranjera para pago de sueldos, pago a proveedores, etc. [F5, 1.2.3]
- Débito inmediato: citado como norma aparte («Sistema Nacional de Pagos – Débito inmediato») en el historial de F6 (comunicación A 7841). No se leyó su texto. Hueco.
- Cuenta en dólares: las transferencias inmediatas están disponibles en dólares entre cuentas de la misma moneda [F5, 2.2.9]. Lo cambiario de comprar dólares está en la sección 5.
- CBU, CVU y alias: no se leyó la norma de «Cuentas de pago» ni de alias. F6 habla de cuentas «a la vista o de pago» y de «consulta de cuentas activas» antes de transferir [F5, 2.2.10]. Hueco para CBU/CVU/alias.

## 3. Financiamiento pyme

3.1 Tasas de referencia del 25/11/2026 (BCRA, API de estadísticas) [F8]:
| Serie | Valor | Fecha |
|---|---|---|
| Adelantos en cuenta corriente, con acuerdo de 1 a 7 días y de $ 10 millones o más, a empresas del sector privado no financiero (id 13/145), TNA | 25,69% | 25/11/2026 |
| TAMAR bancos privados (depósitos de $ 1.000 millones o más), TNA / TEA | 23,4375% / 26,11% | 25/11/2026 |
| BADLAR bancos privados (depósitos de $ 1 millón o más), TNA | 21,9375% | 25/11/2026 |
| Depósitos a 30 días, TNA | 20,56% | 25/11/2026 |
| Préstamos personales, TNA | 60,16% | 25/11/2026 |
La definición de la serie 13 (importes de $ 10 millones o más, con acuerdo de 1 a 7 días) está en F10 (índice de series, punto 1.1.3). No es la tasa que paga una pyme chica: otra fuente da tasas de descubierto mucho más altas (ver abajo).
- Discrepancia: el extracto de una búsqueda sobre la tabla de «tasas frecuentes» de Banco Provincia dio descubierto de empresas a 62,00% con reciprocidad y 70,00% sin reciprocidad desde el 1/2/2026. No leí esa tabla; es [S]. Es la diferencia entre la tasa grande del BCRA y la de lista del banco. https://www.bancoprovincia.com.ar/CDN/Get/tasas_frecuentes
- Tasa del descubierto: la lista del banco, no el promedio del BCRA, es lo que paga la pyme.

3.2 Descuento de cheques y ECHEQ en el banco: el Banco de la Nación publica una línea con «TASA ADELANTADA FIJA EN PESOS», plazo «Hasta 360 días», sin comisiones, con «calificación crediticia vigente y/o Aval SGR». [F12] [M]; la tasa numérica no está en el texto.

3.3 Descuento en el mercado de capitales (MAV), instantánea del 26/11/2026 [F9]. Las pestañas del sitio (Echeq, Pagarés, FCE, Caución Pesos, Caución Dólar) no se separan en el texto extraído; la primera tabla (segmentos Avalado, Garantizado, No garantizado, Inversor calificado, con plazos de 6 a más de 100 días) es la que figura bajo Echeq, pero eso es [M]. Valores literales de esa tabla:
- Avalado, 15 días (vto 11/12): tasa mínima 22,98%, máxima 28,00%, promedio 26,00%, $ 299.581.179,06 nominales, 22 instrumentos.
- Avalado, 60 días (vto 25/01): 22,99% / 28,00% / 25,81%, $ 824.655.464,03, 29 instrumentos.
- Avalado, 90 días (vto 24/02): 24,00% / 31,00% / 25,54%, $ 430.880.869,35, 20 instrumentos.
- No garantizado, 13 días (vto 09/12): 23,00% / 40,00% / 28,69%, $ 3.566.603.177,70, 26 instrumentos.
- Inversor calificado, 19 días: promedio 46,00% (2 instrumentos).
- Avalado en dólares, 60 días: promedio 6,50% (USD 34.500).
Las unidades de la tasa (nominal anual) no figuran en el texto extraído: declararlo al citar.
- Referencia vieja, no vigente: un reporte de MAV de octubre de 2025 daba tasa promedio de cheques de cadena de valor 64,52%, avalados 51,66% y garantizados MAV 48,24% (septiembre de 2025). Contraste útil con la tasa de noviembre de 2026 para mostrar que cambia mucho. Visto en la portada de F9 como cita de una publicación de MAV en X, [S].
- Descripciones de MAV: el ECHEQ «nace online desde el homebanking»; el pagaré bursátil «Puede emitirse en pesos o dólares»; FCE «se transforma el crédito comercial en crédito financiero»; descuento «hasta un plazo máximo de un año». [F9, texto de presentación] [M]
- Cómo funciona (Criteria, 2023): hace falta una cuenta comitente con una ALyC autorizada por la CNV; para ECHEQ hay que registrarse en la plataforma Epyme; segmentos «Cadena de Valor» (cheques de empresas de primera línea, sin calificación crediticia propia), «Avalado» (con aval de una SGR); el aval de la SGR se califica una vez al año (vigencia aproximada de 12 meses); los fondos pasan a una cuenta bancaria del mismo titular en hasta 24 horas; plazo máximo 360 días. [F11] [M] Es de 2023; no es evidencia de la práctica de 2026, solo de cómo es el mecanismo.

3.4 FCE (Factura de Crédito Electrónica MiPyME): para el circuito de circulación el BCRA define un sistema de circulación abierta administrado por COELSA, gratuito para el usuario («serán gratuitos»), donde la FCE aceptada «expresa o tácitamente» puede transmitirse, cederse, avalarse y negociarse. [F1, punto 3.5] El resto (obligatoriedad, 21 días) está en F14.

3.5 Hueco: giro en descubierto fuera de la serie del BCRA, pagaré bursátil (condiciones CNV), tarjeta corporativa y financiación con tarjeta de empresas, SGR (régimen legal, comisión y costo del aval), costo financiero total (CFT) y la norma de transparencia.

## 4. Colocación de excedentes

- Plazo fijo y tasas: ver tabla 3.1. A 30 días, 20,56% TNA (25/11/2026), BADLAR 21,94%. La tasa de plazo fijo de una empresa depende del monto y del banco; la serie BCRA es solo promedio. [F8]
- Inflación: mensual de octubre de 2026 2,2%; interanual 33,1%; mediana de las expectativas a 12 meses del REM 21,8% (dato del BCRA, serie «Mediana de la variación interanual próximos 12 meses del índice de precios al consumidor del relevamiento de expectativas de mercado», al 31/10/2026). [F8, ids 27-29]. Cuenta mía: 20,56% TNA a 30 días equivale a unos 22,6% de tasa efectiva anual; contra el 33,1% interanual, es una tasa real negativa de alrededor de 8%; contra el 21,8% esperado a 12 meses, es levemente positiva. La conclusión depende de qué inflación se use.
- Caución bursátil (MAV, 26/11/2026, caución en pesos): 1 día (vto 27/11): mínima 15,00%, máxima 24,00%, última 16,01%, concertado $ 29.838.285.214; 7 días (vto 03/12): última 20,00%, $ 1.124.467.854. Caución en dólares a 1 día: última 1,10%; a 14 días 3,00%. Unidad no rotulada en el texto extraído (por el orden de magnitud es nominal anual). [F9] [M]
- Tasa de pases entre terceros a 1 día: 20,52% TNA (25/11/2026). [F8, id 150]
- Tipo de cambio mayorista de referencia: $ 1.600,6872 el 26/11/2026; minorista vendedor $ 1.628,75. [F8, ids 4-5]
- Fondos comunes de inversión money market y T+1: no se leyeron datos (CAFCI trae el rendimiento en una planilla diaria que no se pudo abrir). Hueco. https://www.cafci.org.ar/

## 5. Lo cambiario que toca a la tesorería (2026)

Fuente: texto ordenado «Exterior y cambios» al 14/09/2026, última comunicación A 8481 con vigencia 15/09/2026. [F7] Es la norma vigente más reciente que pude leer; no vi comunicaciones posteriores a septiembre.
- Importaciones: las entidades «podrán dar acceso al mercado de cambios» para pagar importaciones de bienes cuando se reúnen las condiciones de la norma. [F7, 10.1] Con registro de ingreso aduanero: pago contra documentación de embarque o de deudas comerciales, con constancia del registro aduanero, factura comercial a nombre del residente, documento de transporte, y que el beneficiario sea el proveedor del exterior (o la entidad financiera que financió). [F7, 10.3.2] Sin registro aduanero (pago anticipado): el pago se debita de una cuenta del cliente en entidad local, con declaración jurada de que demostrará el ingreso aduanero en «270 (doscientos setenta) días corridos» para bienes de capital y «90 (noventa) días corridos» para el resto. [F7, 10.4.2]
- Seguimiento: sistema SEPAIMPO. [F7, secciones 10 y 11]
- Compras de dólares por empresas para atesorar: «El acceso al mercado de cambios por parte de personas jurídicas que no sean entidades autorizadas a operar en cambios, gobiernos locales, Fondos Comunes de Inversión, Fideicomisos y otras universalidades constituidas en el país, requerirá la conformidad previa del BCRA para la formación de activos externos» (con los códigos de concepto A01 a A24 que lista) y para derivados. [F7, 3.10] Es decir, para una empresa la compra de dólares para ahorrar sigue sujeta a autorización previa del BCRA al 14/09/2026; para pagar una importación con condiciones cumplidas, no. Las personas humanas tienen otro régimen (3.8, 3.9), no leído.
- Cobros de exportaciones y su seguimiento: secciones 7 a 9, no leídas.
- Dividendos a no residentes y deudas: reglas con condiciones (balances cerrados y auditados, BOPREAL); no se desarrolla. [F7, 3.4, 4.6]
- Frase de la norma: solo un cuadro con 15 secciones; el BCRA actualiza el texto con cada comunicación. La fuente viva: https://www.bcra.gob.ar/ (Sistema financiero, Marco legal y normativo, Textos ordenados).
- Hueco: no pude verificar si hay una comunicación posterior al 15/09/2026 ni la «restricción cruzada» que se aplicaba antes. El texto leído no la menciona en las líneas que busqué (búsqueda de «restricción cruzada»: sin resultados), pero no lo leí entero.

## 6. Impuesto a los créditos y débitos bancarios (solo salida de caja)

No se pudo leer ninguna fuente primaria (las URL probadas de Infoleg y de ARCA dieron 404 o la norma equivocada). No hay una cifra verificada. Lo que se sabe de memoria, sin fuente leída y que no debe usarse sin verificar: es la Ley 25.413, con una alícuota general de 0,6% sobre cada débito y cada crédito en cuentas bancarias, y parte computable como pago a cuenta de Ganancias. Declarar como hueco y enviar al tema Impuestos, que es el dueño.

## 7. Recursos canónicos propuestos

| Componente | Recurso | Qué parte | En qué fijarse |
|---|---|---|---|
| Cheque y ECHEQ | BCRA, texto ordenado «Cheques y otros instrumentos compensables» (F1) | 2.3.2 (CPD), 3.4 (ECHEQ), 3.5 (FCE) | la fecha del texto ordenado; las causales de rechazo; infraestructuras involucradas |
| Transferencias | BCRA, «Transferencias» y «Normas complementarias» (F5, F6) | sec. 2 (límites mínimos), 3.4 (pull), 6.4 (equivalencias en pesos) | las equivalencias en pesos se actualizan en marzo, julio y noviembre: buscar la de noviembre de 2026 |
| Tasas | API del BCRA de estadísticas monetarias, series 7, 12, 13, 44 (F8) | valores al día | la definición de cada serie (la 13 es de importes de $ 10 millones o más) |
| Descuento de cheques en el mercado | Portada de MAV, Datos de Mercado, y el informe mensual de MAV (F9) | pestaña Echeq, plazo, segmento | segmento (avalado, no garantizado) y que el rango de tasa es ancho |
| Cambios | BCRA, texto ordenado «Exterior y cambios» (F7) | sec. 3.10, 10.3 y 10.4 | la comunicación incorporada y su fecha |

## 8. Huecos (lo que no se pudo leer o confirmar)

1. Texto de la Ley 24.452 y del decreto-ley 4776/63 (plazo máximo del CPD con artículo). Hay dos fuentes oficiales para los 360 días (F3, F4), pero ninguna es la ley.
2. CBU, CVU y alias (norma de cuentas de pago y de alias), débito inmediato, débito directo.
3. Cuentas en dólares para empresas (qué pueden hacer con ellas más allá de transferir entre cuentas en dólares).
4. Costo financiero total: la obligación de informarlo (texto ordenado de protección de usuarios de servicios financieros o de transparencia) no se leyó.
5. SGR: régimen legal, costo del aval y alcance; la nota usa solo F11.
6. Pagaré bursátil: reglas de la CNV.
7. Giro en descubierto: solo la serie del BCRA de importes grandes; la tabla de Banco Provincia es [S].
8. Tarjeta corporativa y financiación con tarjeta para empresas.
9. Fondos comunes money market y T+1: sin datos de rendimiento. CAFCI no abrió.
10. Impuesto a los créditos y débitos: sin fuente (ver 6).
11. Cambios: no se verificó si hay comunicaciones posteriores al 15/09/2026; cobros de exportaciones y la sección de empresas con deuda no leídas.
12. Cifras de uso de transferencias en 2026 y de ECHEQ más allá de las de F14: no se buscaron.
13. Unidad y rotulación de las tablas de MAV (cuál es Echeq, cuál Pagarés): el texto extraído no separa las pestañas.

## 9. Sobre el árbol

La división «notas de Argentina» funciona, pero conviene dividirla en dos notas porque el campo local tiene dos cuerpos de norma distintos: (1) medios de cobro y pago y financiamiento (cheque, ECHEQ, transferencias, descuento en el mercado, FCE, SGR), y (2) colocación de excedentes y lo cambiario con las tasas fechadas. Que las tasas y los mínimos en UVA vayan en una tabla con fecha y fuente viva, porque cambian en meses (y las equivalencias en pesos de los límites, en marzo, julio y noviembre).
