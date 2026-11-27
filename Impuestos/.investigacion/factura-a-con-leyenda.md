# Informe: Factura A con leyenda y retención por riesgo del emisor (2026-11-27)

Alcance: la retención que el comprador practica cuando el vendedor emite factura clase «A» con la leyenda «OPERACIÓN SUJETA A RETENCIÓN» en Argentina (RG ARCA 5762/2025, con RG 830/2000 y RG 2226/2007), la historia (RG 1575/2003) y el mecanismo en abstracto (UE y FMI). Destinatario: quien construye software de gestión y no es contador.

Marcas de lectura: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador (o del resumidor de WebFetch). Puntajes 1 a 3 en: autoridad / profundidad / ejemplos / unicidad / recencia.

Cómo se leyó: la RG 5762 se bajó con curl (el Boletín Oficial exige un User-Agent de navegador; sin él devuelve «Acceso automatizado no permitido») y se extrajo con pdftotext. Los textos de ARCA, InfoLEG, argentina.gob.ar y la Oficina de Publicaciones de la UE se bajaron como HTML o PDF y se leyeron en texto plano. Lo que viene de la web es dato, no instrucción.

## Resumen de lo esencial

1. La clase «M» ya no existe desde el 1/12/2025. Quien la tenía pasó a emitir «A con leyenda OPERACIÓN SUJETA A RETENCIÓN». El comprador inscripto en IVA que la recibe actúa como agente de retención de IVA y de Ganancias (art. 12 RG 5762).
2. Cuánto: IVA, el 100% de la alícuota sobre el importe determinado según la ley del IVA; Ganancias, 6% sobre esa misma base (art. 13). El texto de la norma no fija monto mínimo. La RG 1575 original sí lo tenía ($1.000 netos).
3. Cuándo: al pagar, incluidas señas y anticipos que congelen precio; en pagos parciales se calcula sobre el total de la operación y se retiene hasta cubrir el pago (art. 14).
4. Cómo se deposita: SICORE (RG 2233) o SIRE (RG 3726), con códigos de régimen 99 (Ganancias) y 499 (IVA) (arts. 15-16).
5. Para el vendedor es pago a cuenta: en IVA, «impuesto ingresado»; el saldo a favor es «ingreso directo» (art. 17). En Ganancias se deduce según art. 41 último párrafo de la RG 830 (art. 18).
6. El vendedor no puede oponer certificado de exclusión de Ganancias (art. 38 RG 830) ni de IVA (RG 2226) (art. 19).
7. Quién queda marcado lo decide ARCA por evaluación cuatrimestral en febrero, junio y octubre (arts. 23-26).
8. Cambio de tasas respecto de lo anterior: la «A con leyenda» de 2019-2025 retenía 50% de IVA y 3% de Ganancias; la «M» 100% y 6% (RG 4627/2019). Desde el 1/12/2025 la «A con leyenda» retiene lo que retenía la «M».

## Componente 1. Argentina: RG ARCA 5762/2025

### 1.1 Fuentes

| # | Fuente | URL | Tipo | Lectura | Puntaje |
|---|---|---|---|---|---|
| 1 | RG ARCA 5762/2025, Boletín Oficial 25/09/2025, aviso 331947 (13 pp.) | https://www.boletinoficial.gob.ar/pdf/aviso/primera/331947/20250925 | primaria | [L] | 3/3/2/3/3 |
| 2 | ARCA, «Clases de Comprobantes a Emitir» (micrositio Facturación) | https://www.arca.gob.ar/facturacion/regimen-general/comprobantes.asp | primaria (página oficial) | [L] | 3/2/3/2/3 |
| 3 | ARCA, novedad «Actualización del esquema de facturación» (25/09/2025) | https://servicioscf.afip.gob.ar/publico/sitio/contenido/novedad/ver.aspx?id=5179 | primaria (página oficial) | [L] | 3/1/1/1/3 |
| 4 | ARCA, «Consulta de Responsables Inscriptos en IVA autorizados a emitir comprobantes - RG 5762» | https://serviciosweb.afip.gob.ar/genericos/nuevosInscriptos/consultaComprobantesMain.asp | primaria (servicio oficial) | [L] de la pantalla de consulta; no se consultó un CUIT | 3/1/2/3/3 |
| 5 | RG ARCA 5764/2025, biblioteca ARCA (BO 25/09/2025) | https://biblioteca.afip.gob.ar/dcp/REAG09005764_2025_09_24 | primaria | [L] | 3/3/2/2/3 |
| 6 | RG ARCA 5830/2026, Boletín Oficial 26/02/2026, aviso 338761 | https://www.boletinoficial.gob.ar/detalleAviso/primera/338761/20260226 | primaria | [L] | 3/2/1/3/3 |
| 7 | Informe previo de otra sesión (Compras-y-abastecimiento/.investigacion/argentina.md) | ruta local del repo | interna | [L] de lo que cita de la RG 5762 | punto de partida, verificado abajo |

Fuentes 1 a 6 son oficiales. Para la RG 5762 la ley y el dinero tienen dos fuentes independientes entre sí que dicen lo mismo en lo central: el texto de la norma (1) y la página de ARCA (2), con la salvedad de que ambas son del mismo organismo. No hay fuente de un organismo distinto.

### 1.2 Hechos, con artículo y cita (fuente 1 salvo que se diga otra)

**Norma.** «Resolución General 5762/2025 ... Procedimiento. Impuestos al Valor Agregado y a las Ganancias. Autorización de emisión de comprobantes clase "A". Regímenes de Retención. Régimen especial de pago. RG N° 1.575. Su Sustitución.» Fecha 24/09/2025; Boletín Oficial 25/09/2025; firma Juan Alberto Pazo. Vigencia: art. 32, «entrarán en vigencia el día 1 de diciembre de 2025».

**Quién queda obligado a emitir A con leyenda.**
- El Título I rige para los responsables inscriptos que piden «por primera vez» la autorización de emitir A (art. 1). Pedirla exige Clave Fiscal, servicio «Regímenes de Facturación y Registración (REAR/RECE/RFI)», formulario F. 855 (personas humanas) o F. 856 (demás), CUIT con «estado administrativo activo sin limitaciones» (RG 3832) y al menos una actividad declarada (art. 2).
- Art. 5: se autoriza clase «A» «cuando superen los requisitos del artículo 3°» y clase «A con leyenda "OPERACIÓN SUJETA A RETENCIÓN"» «cuando no cumplan con alguno de los requisitos establecidos en el artículo 3°».
- Requisitos del art. 3: (a) no estar entre las causales de habilitación de A con leyenda, según el análisis integral de la RG 4132; (b) acreditar solvencia patrimonial (art. 4); (c) no haber pedido una o más bajas de IVA en los 12 meses anteriores si al momento de la última baja estaban habilitados a emitir M, A con leyenda OSR o inhabilitados.
- Solvencia patrimonial (art. 4), personas humanas: Bienes Personales de los últimos dos períodos presentada dentro de 30 días corridos del vencimiento, con bienes por encima del mínimo no imponible y bienes en el país (sin efectivo ni artículos del hogar) por más del 15% de ese mínimo; o inmuebles y/o automotores cuyo valor supere el 6% del mínimo no imponible (art. 4 punto 1.2). Demás responsables: al menos el 33% de quienes otorgan la voluntad social, o la entidad misma con inmuebles/automotores.
- Los criterios de las causales no están en la RG 5762: remite a la RG 4132. El art. 2 de la RG 4132, según lo sustituyó la RG 5764 (art. 6), habilita A con leyenda cuando ARCA verifica «1. Inconsistencias en la relación entre los montos facturados y la capacidad técnico-económica para realizar las prestaciones de servicios y/o ventas de bienes. 2. Irregularidades o incumplimientos vinculados a las obligaciones fiscales», analizando «en forma integral los parámetros de control establecidos en el Anexo» (fuente 5). El Anexo de la RG 4132 (la lista de parámetros) no se leyó.

**Cómo decide ARCA después (evaluación periódica).**
- Art. 23: los autorizados a emitir A, A con leyenda OSR y A con leyenda «PAGO EN CBU INFORMADA» «serán evaluados por las operaciones que hayan informado en el curso de cada cuatrimestre calendario», por el Libro de IVA Digital (RG 4597) o la DDJJ F. 2051 (RG 5705).
- Art. 24: «La evaluación del comportamiento fiscal se efectuará en los meses febrero, junio y octubre de cada año, sobre la base de la información correspondiente al último período cuatrimestral vencido». Condición: información presentada y operaciones «como mínimo en DOS (2) meses» del cuatrimestre. En los primeros 7 días corridos de esos meses hay una «simulación preventiva», notificada en el domicilio fiscal electrónico, con la lista de inconsistencias.
- Art. 25: tras la evaluación definitiva, ARCA notifica «hasta el día 20 de los meses indicados» (o primer día hábil posterior) en el domicilio fiscal electrónico y «publicará las novedades en la consulta pública disponible en el micrositio "Facturación"». El detalle de inconsistencias se ve en el servicio REAR/RECE/RFI, «Resultado de la Evaluación Periódica de su Habilitación». Si se subsanan, hay «reproceso de los controles» para obtener el nuevo resultado.

**Cómo se entera el emisor y cómo sale.**
- Se entera por notificación en el domicilio fiscal electrónico (art. 25) y consultando el servicio REAR/RECE/RFI. El comprador se entera por la consulta pública (fuente 4: «permite a los receptores de comprobantes ... verificar que el emisor se encuentre habilitado», se ingresa el CUIT del emisor con captcha). La pantalla advierte que la consulta no informa sobre comprobantes emitidos por controladores o impresoras fiscales.
- Salidas: (a) subsanar y pedir el reproceso (art. 25); (b) volver a ser evaluado en la siguiente ronda (art. 24); (c) disconformidad por Presentaciones Digitales, trámite «Facturas clase A con leyenda OPERACIÓN SUJETA A RETENCIÓN - Disconformidad» (art. 6): ARCA puede pedir elementos en 10 días hábiles administrativos (art. 7), resuelve en 15 días hábiles administrativos (art. 8). Se puede manifestar disconformidad «hasta el vencimiento de la obligación de presentación de la declaración jurada F. 2051 del último período mensual del cuatrimestre calendario siguiente» al evaluado (art. 26).
- Quienes no superan los controles del art. 3 inc. a) (RG 4132) solo pueden manifestar disconformidad según arts. 6 y 9 de la RG 4132 (art. 9 RG 5762). La RG 5764 (art. 6, punto 4) agrega que a los habilitados por la RG 4132 «no siendo de aplicación lo previsto en los artículos 6°, 7° y 8°» de la RG 5762 (fuente 5). Consecuencia práctica: hay dos vías de disconformidad según el origen de la marca.
- Opción de CBU: quien cumple los requisitos de art. 3 incisos a) y c) pero no acredita solvencia «podrán ejercer la opción para emitir comprobantes clase "A" con leyenda "PAGO EN CBU INFORMADA"» (art. 5, último párrafo; Título IV). Se ejerce solo al presentar F. 855/F. 856: «No resultará válida la opción que se efectúe con posterioridad» (art. 20). No hay opción de garantía en el texto. La opción de CBU es un camino distinto, no una salida del A con leyenda OSR. ARCA lo expresa así: A con leyenda OSR es para quienes no cumplen alguno, algunos o ninguno de los requisitos «y a quienes, incumpliendo únicamente el requisito relativo a la acreditación de solvencia patrimonial, no hayan optado» por la CBU (fuente 2).
- Quien tenía M al 1/12/2025: ARCA «adjudicará automáticamente» la habilitación A con leyenda OSR y mantiene la codificación y la numeración (fuente 3; art. 28 RG 5762: «continuarán con la progresividad y correlatividad en su numeración de aquellos generados, para cada código de comprobante clase "M"»).

**Quién retiene (art. 12).** «El adquirente, locatario o prestatario inscripto en el impuesto al valor agregado que reciba el comprobante clase "A" con leyenda "OPERACIÓN SUJETA A RETENCIÓN" deberá actuar como agente de retención de los impuestos al valor agregado y a las ganancias.»
- No hace falta ser agente designado de antemano: la norma convierte en agente a todo comprador inscripto en IVA que reciba la factura.
- Excepciones: operaciones «a) Alcanzadas por regímenes de retención especiales ... b) Que, por normas específicas, hayan sido excluidas».
- Regla del mayor: «Si por aplicación del régimen general de retención establecido por la Resolución General N° 830 ... surgiera que el monto de retención sea superior al que resultaría por la aplicación de lo que se establece por la presente, corresponderá la aplicación del monto mayor.» La RG 5762 ya no nombra la RG 2854 (la RG 4627/2019 sí nombraba RG 830 y RG 2854).

**Cuánto (art. 13).**
- IVA: «aplicando sobre el importe determinado de acuerdo con lo dispuesto por la ley del gravamen, el CIEN POR CIENTO (100%) de la alícuota que corresponda, según el hecho imponible de que se trate». Para empresas promovidas con «Bonos de Crédito Fiscal - IVA Compras», la retención es «el monto del gravamen no cancelado mediante los citados bonos».
- Ganancias: «aplicando sobre la base de cálculo indicada en el primer párrafo del inciso anterior, el SEIS POR CIENTO (6%)».
- Neto o total. El texto no dice «neto». La base es «el importe determinado de acuerdo con lo dispuesto por la ley del gravamen», es decir la base imponible del IVA, que no incluye el impuesto. Dos apoyos: la RG 1575 original definía esa base como «el importe neto de la operación —conforme a lo dispuesto por el artículo 10 de la Ley de Impuesto al Valor Agregado» (fuente 8), y ARCA repite la fórmula («sobre el importe determinado conforme la Ley del Impuesto al Valor Agregado, el 6 %») (fuente 2). La lectura «6% del neto gravado» es una inferencia de esas dos fuentes, no una cita literal de la RG 5762. El 6% no es 6% del IVA. Es 6% del neto, mientras que la retención de IVA es el 100% del IVA facturado, es decir alícuota × neto.
- Mínimo: el texto de la RG 5762 no contiene ningún monto mínimo. La RG 1575 original lo tenía (art. 12 inc. a: neto igual o mayor a $1.000). No se encontró en la RG 5762 una cláusula equivalente y tampoco las normas anteriores leídas (RG 4627) lo reponen. La leyenda de la M original decía «LA OPERACION IGUAL O MAYOR A UN MIL PESOS ($ 1.000.-) ESTA SUJETA A RETENCION», y la RG 4627 (art. 3) la reemplazó por «OPERACIÓN SUJETA A RETENCIÓN».
- Si el comprador no es agente designado: ver art. 12; igual retiene. Si no es inscripto en IVA (consumidor final, monotributista, exento), el art. 12 no lo alcanza, y ARCA lo dice así: «Esto no aplica cuando el receptor sea monotributista» (fuente 2). La A solo se emite a responsables inscriptos; a consumidor final corresponde B, así que no se da el caso.

**Cuándo (art. 14).** «La retención debe practicarse en el momento en que se efectúe el pago de los importes atribuibles a la operación, incluidos aquellos que revistan el carácter de señas o anticipos que congelen precios.» Pagos parciales: «el monto de la retención se determinará considerando el importe total de la respectiva operación. Si la retención a practicar resultara superior al importe del pago parcial ..., procederá hasta la concurrencia de dicho pago». «Pago» con el alcance del antepenúltimo párrafo del art. 24 de la ley de Ganancias.

**Constancia, depósito e información (arts. 15-16).**
- Se entrega al retenido «el comprobante o certificado que establece la Resolución General N° 2.233 ... (SICORE) o la Resolución General N° 3.726 ... (SIRE), según corresponda, en el momento en que se efectúe el pago».
- Información e ingreso según esas normas, con los códigos: **99** «Factura "A" con leyenda "OPERACIÓN SUJETA A RETENCIÓN" - Ganancias - Emisión de comprobantes con discriminación del gravamen» y **499** «... - IVA - ...». Los saldos a favor del agente por retenciones en exceso reintegradas están sujetos a esas normas.
- La RG 2854 no se invoca en el texto de la RG 5762. Su biblioteca todavía lista una categoría «5 - Retención Sustitutiva 100 % RG 2.854 - RG 1575 - HABILITADO FACTURA M» (fuente 10); el art. 31 RG 5762 manda leer esas referencias como hechas a la RG 5762 y a la A con leyenda.

**Carácter para el emisor (arts. 17-18).**
- IVA: «tendrá para los responsables el carácter de impuesto ingresado, debiendo su importe ser computado en la declaración jurada del período fiscal en el cual se sufrieron». También computan las practicadas hasta el vencimiento de la DDJJ por ventas de ese período. Si hay saldo a favor: «tendrá el carácter de ingreso directo y podrá ser utilizado de acuerdo con lo dispuesto en el artículo 24, segundo párrafo del Título III de la Ley de IVA».
- Ganancias: «podrá ser deducido de conformidad con lo dispuesto en el último párrafo del artículo 41 de la RG 830». Ese párrafo (leído en InfoLEG, fuente 9) dice que lo retenido «podrá ser deducido a fin de la determinación de los anticipos del impuesto a las ganancias imputables al período fiscal inmediato siguiente» según RG 327.
- Costo para el emisor: pierde liquidez (el comprador le retiene el 100% del IVA que facturó) y queda con saldo a favor técnico que debe recuperar por el art. 24 LIVA.

**Certificados de exclusión (art. 19).** «no podrán oponer el certificado de exclusión de retenciones del impuesto a las ganancias que establece el artículo 38 de la Resolución General N° 830 ..., así como tampoco la exclusión de retenciones del impuesto al valor agregado, otorgada de acuerdo con lo previsto en la Resolución General N° 2.226». Ver componente 2.

**Si el comprador no retiene (art. 29).** Los agentes que omitan retener o mantengan lo retenido vencidos los plazos «serán responsables en forma personal y solidaria en los términos del artículo 8° de la Ley N° 11.683 ... por el tributo que omitieron retener o que, retenido, dejaron de ingresar», con sanciones de los arts. 45 o 48 de esa ley y, si corresponde, el art. 4 del Título IX de la Ley 27.430; además aplica el art. 43 de la ley de Ganancias. Párrafo siguiente: si las inconsistencias son «reiteradas y/o por importes relevantes», ARCA puede habilitar al comprador-agente a emitir A con leyenda en lugar de A.

**«PAGO EN CBU INFORMADA» (arts. 20-22).** El vendedor informa una CBU propia al pedir la habilitación (art. 20). Los compradores inscriptos «deberán cancelar el monto correspondiente a la diferencia entre el importe total facturado y las retenciones que por otros regímenes pudieran corresponder, mediante transferencia bancaria o depósito, en la cuenta bancaria cuya CBU fuera informada por el vendedor ... la cual podrá ser consultada en el micrositio "Facturación"» (art. 22). Si el receptor es monotributista, «la totalidad del importe facturado deberá cancelarse por alguno de los medios mencionados». Este tipo no lleva retención del régimen de la RG 5762 (fuentes 2 y 3). La consulta de CBU habilitada está en https://servicios1.afip.gov.ar/genericos/CBUHabilitadas/consulta.aspx (enlace tomado de la fuente 2; no se pudo abrir desde esta sesión).

**Controlador fiscal (art. 11).** «Los comprobantes clase "A" con leyenda "OPERACIÓN SUJETA A RETENCIÓN" no podrán ser emitidos a través del equipamiento electrónico denominado "Controlador Fiscal"» (RG 3561). El art. 11 también fija las vías de emisión: comprobantes electrónicos originales (RG 4291) o, para contingencias y tipos no cubiertos, RG 100 con talonarios limitados a 100 comprobantes. La RG 5764 (art. 5) lo repite. La leyenda debe ir «junto a la letra "A"» y, en impreso o representación gráfica, «en la cabecera o parte superior del documento» (art. 10). Los comprobantes cumplen la RG 1415 como cualquier A. La RG 5764 reasigna los códigos de comprobante «A con leyenda OSR» (factura, ND, NC, recibo, notas de venta al contado, etc.) (fuente 5); para «PAGO EN CBU INFORMADA» se usan los códigos de la A común.

**Abrogaciones y referencias (arts. 27, 30, 31).**
- Art. 30: «Abrogar las Resoluciones Generales Nros. 1.575, 1.672, 1.681, 1.934, 1.941, 2.499, 4.627, 5.569 y 5.716, y derogar el Título V de la Resolución General N° 4.597 y el Capítulo B del Título V de la Resolución General N° 5.003, sin perjuicio de la aplicación de esas normas a los hechos y situaciones acaecidos durante su vigencia».
- Art. 31: toda referencia a la RG 1575 o a la clase M, «excepto para la Resolución General N° 3.561», se entiende hecha a la RG 5762 o a la A con leyenda OSR.
- Art. 27: las M impresas según RG 100 «podrán utilizarse hasta los plazos de validez otorgados en la respectiva autorización de impresión».

**Cambios posteriores.**
- RG 5764/2025 (BO 25/09/2025, misma fecha): modifica RG 100, 1702, 2904, 2926, 4132, 4290 y 4367 y reordena códigos y vencimiento de impresos. No toca la RG 830, 2226 ni 2854 (fuente 5, texto completo revisado por «830», «2226», «2854», «2233»: sin coincidencias en el articulado).
- RG ARCA 5830/2026 (25/02/2026, BO 26/02/2026, aplica desde el 1/7/2026): «Exceptuar de lo establecido en el Título I ... de la Resolución General N° 5.762, a las entidades financieras sujetas al régimen de la Ley N° 21.526 ... y a las entidades de seguros comprendidas en la Ley N° 20.091» (art. 1). No cambia el Título III (retención). Es la única modificación de la RG 5762 encontrada.
- Búsqueda sin poder confirmar exhaustividad: la página de argentina.gob.ar «normas que modifican» a la RG 5762 devolvió error 500 y se agotó el cupo de búsquedas web. Hay que tratar la lista de modificaciones de marzo a noviembre de 2026 como no verificada.

**Página de ARCA y consulta (fuentes 2 y 4).** La página «Clases de Comprobantes a Emitir» repite el régimen (retención 100% IVA, 6% Ganancias, códigos 99 y 499, no oponibilidad de certificados) y trae el cuadro comparativo RG 1575 / RG 5762. La consulta de emisores (fuente 4) es una pantalla con captcha por CUIT. No se encontró un servicio web (API) documentado para consultarla desde un sistema: ver huecos.

### 1.3 Verificación del informe previo

Lo que dice el informe previo sobre la RG 5762 coincide con el texto: vigencia 1/12/2025, retención 100% IVA y 6% Ganancias al pagar (arts. 13-14), exclusión no oponible (art. 19), responsabilidad personal del comprador (art. 29) y CBU (arts. 20-22). Se agrega: la evolución de tasas (componente 3), que no hay mínimo en el texto, la regla del mayor con RG 830, la RG 5764 y la RG 5830, y la consulta de emisores.

## Componente 2. RG 830/2000, RG 2226/2007, RG 2854 y RG 18

### 2.1 Fuentes

| # | Fuente | URL | Tipo | Lectura | Puntaje |
|---|---|---|---|---|---|
| 9 | RG 830/2000 (AFIP), texto actualizado, InfoLEG | https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/62872/texact.htm | primaria | [L] (buscados arts. 38, 41, 43, Anexos VI y VII) | 3/3/2/3/2 |
| 10 | RG 2854/2010 (IVA, régimen de retención), biblioteca ARCA | https://biblioteca.afip.gob.ar/search/query/norma.aspx?p=t:RAG\|n:2854\|o:3\|a:2010 | primaria | [L] parcial (arts. 8-9, Anexo con consulta de proveedores, requisitos) | 3/2/2/2/2 |
| 11 | RG 2226/2007 (IVA, exclusión), biblioteca ARCA | https://biblioteca.afip.gob.ar/search/query/norma.aspx?p=t:RAG\|n:2226\|o:3\|a:2007 | primaria | [L] arts. 1-4 y lista de modificaciones | 3/3/2/3/2 |
| 12 | ARCA, «Certificados de exclusión - IVA - Resolución» | https://www.arca.gob.ar/iva/solicitud-certificados-exclusion/resolucion.asp | primaria (página oficial) | [L] | 3/2/2/2/3 |
| 13 | RG 18/1997, biblioteca ARCA | https://biblioteca.afip.gob.ar/search/query/norma.aspx?p=t:RAG\|n:18\|o:3\|a:1997 | primaria | [M] (estado: abrogada por RG 2854) | 3/1/1/1/1 |

### 2.2 RG 830/2000 (Ganancias)

- La RG 830 no contiene un artículo para la factura M ni para la A con leyenda. El texto actualizado de InfoLEG (fuente 9) no menciona la RG 1575. El régimen de la M/A con leyenda es propio (RG 1575 → RG 5762) y se vincula con la RG 830 por tres puntos.
- Art. 38: «Cuando las retenciones a sufrir en el curso del período fiscal puedan dar lugar a un exceso en el cumplimiento de la obligación tributaria correspondiente a dicho período, los sujetos pasibles podrán solicitar un certificado de exclusión de acuerdo con lo dispuesto en el Anexo VI». Para evitar la retención el sujeto exhibe el certificado al agente, «quien constatará su veracidad mediante consulta en el sitio "web" institucional».
- Anexo VI, A (Exclusiones): no procede el certificado cuando los sujetos «e) Se encuentren obligados a emitir comprobantes Clase "M"». El texto de InfoLEG no se actualizó a la nomenclatura de la RG 5762 (art. 31 RG 5762 obliga a leer «M» como A con leyenda OSR). Misma cláusula, inciso f), en el Anexo VII A (régimen excepcional de ingreso, art. 39).
- Art. 41, último párrafo: lo retenido «podrá ser deducido a fin de la determinación de los anticipos del impuesto a las ganancias imputables al período fiscal inmediato siguiente conforme a las previsiones del Artículo 3º, inciso a), puntos 2. y 3., de la Resolución General Nº 327». La RG 5762 (art. 18) remite a ese párrafo.
- Art. 43: el régimen de la RG 830 «no será de aplicación cuando ... se prevea una forma distinta de retención»; junto con el art. 12 RG 5762 (regla del monto mayor) define cuál retención rige cuando conviven.
- Interacción resumida: el vendedor marcado no puede pedir certificado de exclusión de Ganancias (Anexo VI A e) ni oponer uno ya obtenido (art. 19 RG 5762); si una retención de RG 830 resulta mayor que el 6%, se aplica la mayor.

### 2.3 RG 2226/2007 (IVA, exclusión)

- Art. 3 (texto vigente según RG 4656/2019): «Los sujetos mencionados en el artículo anterior no podrán solicitar el certificado de exclusión, cuando: ... f) Se encuentren obligados a emitir comprobantes clase "M" o clase "A" con la leyenda "Obligación Sujeta a Retención"» (la biblioteca escribe «Obligación», no «Operación»). Versión original: «f) ... comprobantes clase "M"». Es una cita literal del texto publicado; la biblioteca no muestra una actualización posterior a la RG 5762.
- La RG 2226 figura como «Vigente», emitida el 16/03/2007, BO 20/03/2007, modificada por las RG 3598/2014, 3412/2012, 4656/2019, 5390/2023 y 5774/2025 (fuente 11). La RG 5774/2025 no se leyó; una búsqueda la ubica con vigencia desde el 21/10/2025 y referida a subsidios y alícuotas reducidas [S].
- Condición adicional de saldo (ARCA, fuente 12, citando art. 4 inc. h): «poseer saldo de libre disponibilidad equivalente, como mínimo, al 20 % del promedio del impuesto determinado en las declaraciones juradas de los últimos 12 períodos fiscales».
- Interacción: un vendedor marcado no puede pedir exclusión de IVA y no puede oponer la que ya tenía (art. 19 RG 5762).

### 2.4 RG 2854/2010 y RG 18/1997

- RG 2854 es el régimen general de retención de IVA que sustituyó a la RG 18/1997 (esta figura «Abrogada», fuente 13). Su art. 8 fija porcentajes sobre el IVA facturado (50% y 80% según el caso, texto RG 3732/2015) y su art. 9 los sustituye por el 100% para proveedores con ciertas categorías en el «Archivo de Información sobre Proveedores» («Reproweb»).
- La consulta por CUIT del proveedor y mes de pago devuelve categorías: «0 - RG 2.226», «1 - Retención General», «2 - Retención sustitutiva 100 %» (incumplimientos de presentación de DDJJ), «3 - Crédito Fiscal No Computable» (proveedor no inscripto en IVA), «4 - ... Irregularidades en la cadena de comercialización» (permanece 3 meses, 12 si reincide) y «5 - Retención Sustitutiva 100 % RG 2.854 - RG 1575 - HABILITADO FACTURA M» (Anexo con la consulta, citado por el art. 9). Es el antecedente argentino más claro de «retención activada por calificación de riesgo del proveedor», y sirve para ejemplificar el concepto general (componente 4).
- Interacción con la RG 5762: la RG 5762 no remite a la RG 2854 (la RG 4627 sí). El art. 9 de la RG 2854 (texto RG 3887/2016) sustituye por 100% solo cuando se verifican las situaciones de los puntos 2 o 4 del inciso e) del Anexo IV; la categoría 5 (ex M) no figura en esa remisión. No se verificó cómo se evitan duplicaciones entre ambos regímenes ni qué categoría corresponde hoy a un proveedor marcado (hueco).

## Componente 3. Historia: RG 1575/2003 y sus cambios

### 3.1 Fuentes

| # | Fuente | URL | Tipo | Lectura | Puntaje |
|---|---|---|---|---|---|
| 8 | RG AFIP 1575/2003, texto original, argentina.gob.ar | https://www.argentina.gob.ar/normativa/nacional/norma-89267/texto | primaria | [L] (considerandos, arts. 12-13 y partes del articulado) | 3/3/2/3/1 |
| 8b | Resumen de la RG 1575 | https://www.argentina.gob.ar/normativa/nacional/norma-89267 | primaria | [L] | 3/1/1/1/2 |
| 14 | RG AFIP 4627/2019, texto original, argentina.gob.ar | https://www.argentina.gob.ar/normativa/nacional/norma-331464/texto | primaria | [L] (art. 1 puntos 9-10, arts. 2-3, 6) | 3/3/2/3/2 |

### 3.2 Hechos

- RG 1575: sanción 10-10-2003, publicada en el Boletín Oficial 15-10-2003 (BO n.º 30255, p. 4). Título: «Procedimiento. Impuestos al Valor Agregado y a las Ganancias. Emisión de comprobantes con discriminación del gravamen. Factura clase 'M'. Requisitos y condiciones. Régimen de retención de los impuestos al valor agregado y a las ganancias. Régimen especial de pago. Régimen de información de operaciones.» Estado: «ABROGADA POR EL ARTICULO 30 DE LA RESOLUCION GENERAL» 5762 (fuentes 8 y 8b).
- Motivo declarado en los considerandos: «una considerable utilización de facturas o documentos equivalentes apócrifos con la finalidad de generar créditos fiscales ilegítimos o erogaciones inexistentes», y la necesidad de «requisitos adicionales de información a través del aporte de datos patrimoniales que posibiliten evaluar la solvencia del responsable». Quienes no acreditan: «un comprobante diferenciado identificado con la letra 'M'». Alternativa: una 'A' con leyenda 'PAGO EN C.B.U. INFORMADA', con pago por depósito en CBU.
- Régimen original (arts. 12-13): el comprador inscripto en IVA que recibe la M retiene IVA y, en su caso, Ganancias cuando el neto de la operación (art. 10 LIVA) sea igual o mayor a $1.000; IVA al 100% de la alícuota; Ganancias al 3% sobre la misma base. Las operaciones así retenidas quedaban «excluidas de la aplicación de otros regímenes de retención, percepción y pagos a cuenta» (salvo guía fiscal ganadera/harinera).
- RG 4627/2019 (BO 07/11/2019, vigente desde el 11/11/2019, art. 6): reemplazó la leyenda de la M por «OPERACIÓN SUJETA A RETENCIÓN» y la leyenda «PAGO EN CBU INFORMADA» de la A también por «OPERACIÓN SUJETA A RETENCIÓN» (art. 3), y fijó por art. 13: IVA «Comprobantes clase "M": 100%», «A con leyenda OPERACIÓN SUJETA A RETENCIÓN: 50%»; Ganancias M 6%, A con leyenda 3%. Su art. 12 nombraba las RG 830 y 2854 para la regla del monto mayor.
- RG 5762 (2025): deja una sola clase con retención (A con leyenda OSR, 100% y 6%) y recrea «PAGO EN CBU INFORMADA» sin retención. Es decir, la «A con leyenda OSR» de 2019-2025 (50%/3%) y la «A con leyenda OSR» desde 2025 (100%/6%) llevan el mismo nombre y distinta tasa. Hueco: las RG 5569 y 5716 (abrogadas por el art. 30) no se leyeron, por lo que no se sabe si cambiaron tasas entre 2019 y 2025.

## Componente 4. General: retención activada por una marca o por el riesgo del emisor

### 4.1 Fuentes

| # | Fuente | URL | Tipo | Lectura | Puntaje |
|---|---|---|---|---|---|
| 15 | Directiva 2006/112/CE, texto consolidado 01.01.2024 (ES), Oficina de Publicaciones de la UE | http://publications.europa.eu/resource/celex/02006L0112-20240101 (con cabecera Accept: application/pdf y Accept-Language: spa) | primaria | [L] arts. 194, 199, 199 bis, 199 ter, 395 | 3/3/2/3/2 |
| 16 | Decisión de Ejecución (UE) 2019/310 del Consejo (Polonia, pago fraccionado) | http://publications.europa.eu/resource/celex/32019D0310 (Accept: application/xhtml+xml, inglés) | primaria | [L] | 3/2/2/3/2 |
| 17 | Decisión de Ejecución (UE) 2025/373 del Consejo (prórroga a Polonia) | http://publications.europa.eu/resource/celex/32025D0373 (ídem) | primaria | [L] | 3/2/2/3/3 |
| 18 | Harrison y Krelove, «VAT Refunds: A Review of Country Experience», FMI WP/05/218 | https://www.imf.org/external/pubs/ft/wp/2005/wp05218.pdf | primaria (FMI) | [L] del pasaje sobre retenciones y su entorno; resto no leído | 3/2/1/2/1 |
| 19 | Pessoa et al., «How to Manage Value-Added Tax Refunds», FMI How To Note 2021/004 | https://www.imf.org/-/media/files/publications/howtonotes/2021/english/htnea2021004.pdf.md | primaria (FMI) | [S] (resumido por WebFetch; sin páginas) | 3/2/1/2/2 |
| 20 | FMI WP 2021, «VAT Invoice Management in Latin America» | https://www.imf.org/-/media/files/publications/wp/2021/english/wpiea2021231-print-pdf.pdf.md | primaria (FMI) | [S] (resumido por WebFetch): sin discusión de retención de IVA | 3/1/1/1/2 |

EUR-Lex (eur-lex.europa.eu) bloquea la descarga automática (devuelve un desafío); se usó la Oficina de Publicaciones. La consolidada leída es del 01.01.2024: puede haber versiones posteriores. Ley y dinero: para la Directiva y las decisiones hay una sola fuente por norma (el texto oficial), sin segunda fuente independiente.

### 4.2 Mecanismos (todos en fuente 15 salvo que se diga otra)

**(a) Inversión del sujeto pasivo doméstica.**
- Art. 199.1: «Los Estados miembros podrán disponer que la persona deudora del IVA sea el sujeto pasivo destinatario de cualquiera de las siguientes operaciones», con una lista: construcción (a), puesta a disposición de personal (b), entrega de inmuebles con opción de imposición (c), material usado, desechos y residuos (d, anexo VI), bienes dados en garantía (e), cesión de reserva de propiedad (f) y venta por deudor judicial (g). Art. 199.2: los Estados pueden limitar las entregas y las categorías de proveedores o destinatarios.
- Art. 199 bis (en la numeración inglesa, 199a): «Hasta el 31 de diciembre de 2026, los Estados miembros podrán establecer que el deudor del IVA sea el sujeto pasivo destinatario» de derechos de emisión, teléfonos móviles, circuitos integrados, gas y electricidad, telecomunicaciones, consolas, tabletas, cereales y cultivos industriales y metales (apdo. 1 a-j). El apdo. 1 ter supedita las letras c) a j) a «obligaciones de información adecuadas y efectivas». Hoy (27/11/2026) el plazo vence dentro de un mes; no se verificó si se prorrogó.
- Art. 199 ter (199b, mecanismo de reacción rápida): «en casos de urgencia imperiosa» un Estado puede designar al destinatario como deudor, «como medida especial ... para combatir modalidades de fraude repentino y masivo que puedan generar pérdidas económicas significativas e irreparables», con control de los proveedores y duración máxima de «nueve meses» (apdo. 1); notifica a la Comisión (apdo. 2) y esta puede emitir dictamen negativo en un mes (apdo. 3).
- Diferencia con Argentina: la inversión traspasa al comprador la deuda del IVA de todo un sector, sin mirar al vendedor concreto. La retención argentina se activa por la calificación del vendedor y deja la deuda en el vendedor, aunque el comprador ingresa el impuesto.

**(b) Pago fraccionado (split payment).**
- Art. 395.1: el Consejo, por unanimidad y a propuesta de la Comisión, puede autorizar a un Estado «medidas especiales de excepción ... para simplificar el procedimiento de cobro del impuesto o para impedir ciertos tipos de evasión o elusión fiscal».
- Decisión 2019/310 (fuente 16): Polonia puede, derogando el art. 226 de la Directiva, aplicar un pago fraccionado. Motivación citada de Polonia: el IVA queda en una cuenta separada del proveedor con uso restringido, «it is better guaranteed that the tax authorities will receive the whole VAT amount»; sectores: acero, chatarra, electrónica, oro, metales no ferrosos, combustibles y plásticos. La autorización inicial corrió del 1/3/2019 al 28/2/2022; Polonia debía informar el impacto a los 18 meses (considerandos y art. 2).
- Decisión 2025/373 (fuente 17): el art. 1 cambia en el art. 3, segundo párrafo, la fecha «28 February 2025» por «29 February 2028». Según Polonia, la medida «resulted in the reduction of, in particular, carousel fraud» y redujo el plazo de devolución a menos de 20 días en los casos de saldo a favor. La mención de Italia (Decisión 2023/1552) viene solo de un resumen del buscador [S]; no se leyó.
- Diferencia con la retención: en el pago fraccionado el comprador no retiene ni ingresa; paga la parte del IVA a una cuenta bloqueada del vendedor. Es primo de la retención: asegura que el impuesto no se evapore entre el cobro y la declaración.

**(c) Retenciones de IVA en América Latina y su costo.**
- FMI WP/05/218 (fuente 18), pasaje inmediatamente posterior al pie «- 13 -» (es decir p. 14 del PDF): «Registered traders subject to withholding arrangements—some countries, particularly in Latin America and West Africa, require certain business and government entities to withhold amounts of VAT from payments to their suppliers. These schemes have several drawbacks: in particular, refund claims can proliferate under these arrangements, especially if withholding rates are set too high.» Es la fuente primaria que sostiene el costo (saldo a favor del vendedor) en abstracto.
- FMI HTN 2021/004 (fuente 19) [S]: entre las circunstancias que generan créditos de IVA excedentes lista el «Use of VAT withholding and reverse charge mechanisms». No desarrolla quién retiene ni tasas.
- Pista no verificada: una búsqueda devolvió un estudio de Honduras (no del FMI) que dice que tasas de retención altas dejan a muchas firmas con saldo negativo que luego deben reclamar [S]. No se abrió; no usar sin leerlo.
- Antecedente de riesgo por calificación del vendedor: RG 2854 art. 9 y su archivo de proveedores (componente 2.4).

### 4.3 Definición abstracta que las fuentes permiten

Una retención en la fuente activada por una marca en el comprobante o por la calificación del emisor es un mecanismo por el que la administración tributaria identifica a un vendedor de riesgo (por inconsistencias, incumplimientos o falta de solvencia) y obliga a su comprador a ingresar al fisco, al pagar, parte o todo el impuesto que el vendedor facturó, en lugar de dejar que el vendedor lo declare. Lo sostienen: la RG 5762 (el caso argentino), la RG 2854 art. 9 (la calificación por categoría de proveedor), el art. 199 ter de la Directiva (marca por sector en emergencia, no por vendedor) y el pago fraccionado de Polonia (el IVA no llega a manos del vendedor).
- Ventaja (con fuente): asegura el cobro del impuesto cuando el vendedor puede desaparecer. Dicho por la UE al evaluar el pago fraccionado, «better guaranteed» (fuente 16) y la reducción de fraude tipo carrusel que informa Polonia (fuente 17); en Argentina, los considerandos de la RG 1575 (facturas apócrifas y créditos fiscales ilegítimos).
- Costo (con fuente): saldo a favor del vendedor y reclamos de devolución (FMI WP/05/218, fuente 18); y para el comprador, la obligación de calcular, retener, ingresar y entregar constancia, con responsabilidad personal y solidaria si omite (art. 29 RG 5762).
- No hay en las fuentes leídas una medición de cuánto fraude evita la retención argentina ni cuántos vendedores marcados quedan con saldo a favor: es un hueco, y no debe afirmarse como dato.

## Notas para el software de gestión (derivadas, no citas)

- Del lado de quien compra: el dato maestro del proveedor necesita la clase de comprobante habilitada (A, A con leyenda OSR, A con leyenda CBU); la consulta oficial es por CUIT con captcha. En la factura electrónica la marca viaja en el código de tipo de comprobante (la RG 5764 asigna códigos propios a «A con leyenda OSR»; la lista completa está en la fuente 5); la tabla de códigos exacta no se transcribió acá.
- Al pagar: retención de IVA = alícuota × neto gravado (100% del IVA facturado) y de Ganancias = 6% del neto gravado, sin mínimo en el texto; con pagos parciales, calcular sobre el total y retener hasta cubrir cada pago; comparar contra la retención de RG 830 (la mayor gana); emitir la constancia SICORE/SIRE con códigos 99 y 499.
- Del lado de quien vende: las retenciones sufridas son pago a cuenta (IVA: impuesto ingresado en la DDJJ del período; Ganancias: se deducen de los anticipos del período siguiente) y el saldo de IVA es de ingreso directo.
- Para el caso «PAGO EN CBU INFORMADA»: el pago es por transferencia o depósito a la CBU informada; no hay retención de este régimen.

## Huecos

1. Parámetros de la RG 4132 (Anexo): no se leyeron; son los criterios concretos de la marca. La RG 5762 solo remite a ellos (art. 3 inc. a).
2. Lista exhaustiva de normas posteriores a la RG 5762: se halló la RG 5764/2025 (complementaria) y la RG 5830/2026 (exceptúa a entidades financieras y aseguradoras del Título I). La página oficial de modificaciones de argentina.gob.ar devolvió error 500 y se agotó el cupo de búsquedas web antes de verificar modificaciones de marzo a noviembre de 2026. Un título de prensa («ARCA modifica requisitos para emitir facturas A», iProfesional) apareció en la búsqueda; al abrir el enlace trataba de la RG 5762 original y sus fechas no son confiables. Sin fuente primaria que lo confirme, no hay otra modificación afirmada.
3. Si la RG 5569 y la RG 5716 (abrogadas por el art. 30) cambiaron las tasas de la A con leyenda entre 2019 y 2025: no leídas. Lo afirmado sobre 50%/3% es el texto de la RG 4627/2019.
4. Mínimo de la retención: el texto de la RG 5762 no trae uno; no se encontró norma que lo reponga, pero no se leyó el texto actualizado completo de toda la normativa de retenciones (SICORE/RG 2233, RG 830 art. de montos no sujetos a retención). Tratarlo como «sin mínimo en la RG 5762», no como «sin mínimo en ninguna norma».
5. «Neto o total» para el 6%: inferido (ver 1.2). Falta una fuente que lo diga con la palabra «neto» para la RG 5762 (por ejemplo, un instructivo de ARCA o el micrositio de SICORE/SIRE).
6. Cómo se evitan duplicaciones entre la RG 5762 y la RG 2854 art. 9, y qué categoría de la RG 2854 corresponde hoy a un proveedor marcado: no se leyó la RG 2854 más allá de lo citado, y su texto en la biblioteca todavía dice «RG 1575 - HABILITADO FACTURA M».
7. RG 5774/2025 (modifica la RG 2226): no leída. Tampoco el texto actualizado de la RG 2226 posterior a la RG 5762.
8. Servicio web (API) o descarga masiva para consultar la habilitación de un emisor: no se encontró; solo la pantalla con captcha (fuente 4). Tampoco la consulta de CBU (el enlace no abrió).
9. Código exacto de comprobante de ARCA para «A con leyenda OSR» (factura, nota de débito, etc.): está en la RG 5764 (fuente 5) pero no se transcribió.
10. Fecha de actualización del texto de InfoLEG de la RG 830: la página no la muestra. No hay certeza de que incorpore las últimas modificaciones.
11. UE: la versión consolidada leída es del 01.01.2024; el plazo del art. 199 bis («hasta el 31 de diciembre de 2026») puede haberse prorrogado o cambiado. No se leyeron las decisiones sobre Italia ni se buscó el Reglamento de la UE sobre el IVA en la era digital (ViDA).
12. FMI/CIAT/BID: hay una sola frase primaria (WP/05/218) y una de segunda mano [S] (HTN 2021/004) que respaldan el costo; no se encontró un paper del FMI, CIAT o BID dedicado a retenciones de IVA ni al riesgo por emisor. Se agotó el cupo de búsquedas antes de la tercera ronda sobre ese punto. Lo del estudio de Honduras queda como pista sin abrir.
13. Ley y dinero con una sola fuente independiente: Directiva y decisiones de la UE (solo el texto oficial); RG 5762 (el texto y la página de ARCA son del mismo organismo).
14. Texto legal sin verificar: art. 24 LIVA (segundo párrafo, devolución/compensación del saldo técnico) y art. 8 de la Ley 11.683: se citan por remisión de la RG 5762, sin leerlos.
