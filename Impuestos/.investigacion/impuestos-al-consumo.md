# Investigación: Impuestos al consumo

Ángulo: la vertical Impuestos al consumo (entrada, `iva`, `impuesto-a-las-ventas`, `lugar-de-la-operacion`, `iva-en-argentina`, `ingresos-brutos`). Fecha: 2026-11-27.

Límites de esta ronda:

- El buscador web se agotó al segundo pedido (cupo de la sesión). Todo lo demás se leyó por fetch directo de URLs conocidas o de enlaces encontrados dentro de sitios oficiales.
- La OCDE devolvió 403, 404 o 410 en todas las rutas probadas (página de las *International VAT/GST Guidelines*, el PDF en `oecd.org/ctp`, la copia del archivo web de la OCDE, *Consumption Tax Trends 2024*, el portal de lectura). **Las Directrices de la OCDE no se leyeron.** Lo que las notas digan de ellas va atribuido a fuentes que sí se leyeron (FMI, Comisión Europea) o queda como hueco.
- El FMI respondió 403 a curl pero no a WebFetch; los PDF se bajaron por WebFetch y se leyeron enteros con `pdftotext`.
- *The Modern VAT* (Ebrill, Keen, Bodin y Summers, FMI 2001) no se consiguió. Lo reemplaza, para el método y la cascada, el capítulo 6 de *Tax Law Design and Drafting* y el WP 13/57 de Keen.
- Los textos se guardaron en el scratchpad de la sesión (no en el repo).

## Fuentes

Puntaje de 1 a 3 en autoridad (A), profundidad (P), ejemplos (E) y unicidad (U).

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| C1 | Directiva 2006/112/CE del Consejo, texto original publicado en el DO L 347 del 11/12/2006 (copia del BOE) | https://www.boe.es/doue/2006/347/L00001-00118.pdf | primaria (norma) | 3 | 3 | 1 | 3 | [L] arts. 1, 90, 93, 97 a 99, 146, 168, 169, 173, 174, 183, 196, 285, 287 |
| C2 | Williams, D., «Value-Added Tax», cap. 6 de Thuronyi (ed.), *Tax Law Design and Drafting*, vol. 1, FMI, 1996 | https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch6.pdf | primaria (manual de organismo) | 3 | 3 | 3 | 3 | [L] secs. I, II (ámbito territorial, umbral), V (exenciones), VII (tasa cero), M (importaciones) |
| C3 | Keen, M., *Targeting, Cascading, and Indirect Tax Design*, IMF WP/13/57, 2013 | https://www.imf.org/external/pubs/ft/wp/2013/wp1357.pdf | primaria (paper de organismo) | 3 | 3 | 2 | 3 | [L] abstract, intro, sec. III y conclusiones |
| C4 | Comisión Europea, One Stop Shop | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en | primaria (organismo) | 3 | 2 | 1 | 3 | [L] por lector automático (cita textos cortos) |
| C5 | *South Dakota v. Wayfair, Inc.*, 585 U.S. ___ (2018), syllabus y opinión (Cornell LII) | https://www.law.cornell.edu/supremecourt/text/17-494 | primaria (fallo) | 3 | 3 | 2 | 3 | [L] syllabus y parte I de la opinión |
| C6 | California Department of Tax and Fee Administration, *Publication 103, Sales for Resale* (revisión de abril de 2021) | https://www.cdtfa.ca.gov/formspubs/pub103/ | primaria (organismo) | 3 | 2 | 3 | 2 | [L] |
| C7 | Tax Foundation (Abir Mandal), *State and Local Sales Tax Rates, 2026* (20/01/2026, actualizado 06/07/2026) | https://taxfoundation.org/data/all/state/sales-tax-rates/ | secundaria (centro de estudios) | 2 | 2 | 3 | 2 | [L] |
| C8 | Ley de Impuesto al Valor Agregado, texto ordenado 1997 (Decreto 280/97), texto actualizado en InfoLEG | https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42701/texact.htm | primaria (norma) | 3 | 3 | 1 | 3 | [L] arts. 1, 3 inc. e) ap. 21 m), 10 a 13, 24 y siguientes sin número, 27, 28, 43 |
| C9 | ARCA, IVA Simple (sujetos alcanzados, confección, retenciones y percepciones, presentación, cronograma) | https://www.arca.gob.ar/iva/iva-simple/sujetos-operaciones-alcanzadas.asp | primaria (organismo) | 3 | 2 | 1 | 3 | [L] |
| C10 | ARCA, Servicios digitales (concepto, obligados, régimen de percepción RG 4240/18) | https://www.arca.gob.ar/iva/servicios-digitales/concepto.asp | primaria (organismo) | 3 | 2 | 2 | 2 | [L] |
| C11 | iProfesional, «¿Cuánto es el IVA en Argentina?», 24/12/2022 | https://www.iprofesional.com/impuestos/374830-cuanto-es-el-iva-en-argentina-productos-con-el-21-27-y-105 | secundaria (prensa) | 1 | 1 | 2 | 1 | [L] por lector automático |
| C12 | Convenio Multilateral del 18/08/77, texto en la Comisión Arbitral | https://www.ca.gob.ar/convenio-multilateral-menu-pagina-legales | primaria (norma) | 3 | 3 | 2 | 3 | [L] arts. 1 a 14 y 27 a 28 |
| C13 | Comisión Arbitral, «La Legislatura de Corrientes ratificó las reformas del Convenio Multilateral», 22/09/2026 | https://www.ca.gob.ar/novedades-home/institucional-novedades/la-legislatura-de-corrientes-ratifico-las-reformas-del-convenio-multilateral | primaria (organismo) | 3 | 1 | 1 | 3 | [L] |
| C14 | Comisión Arbitral, SIFERE | https://www.ca.gob.ar/sistemas/sifere | primaria (organismo) | 3 | 1 | 1 | 3 | [L] |
| C15 | Comisión Arbitral, Padrón Federal | https://www.ca.gob.ar/sistemas/padron-federal | primaria (organismo) | 3 | 1 | 1 | 3 | [L] |
| C16 | Código Fiscal de la Provincia de Buenos Aires, Ley 10.397 (t.o. 2011), texto actualizado en normas.gba.gob.ar | https://normas.gba.gob.ar/ar-b/ley/1986/10397/6417 | primaria (norma) | 3 | 3 | 1 | 3 | [L] arts. 182, 186 a 188, 223 |
| C17 | Ley 15.558 de la Provincia de Buenos Aires, Ley Impositiva para el ejercicio fiscal 2026, B.O. 15/12/2025 | https://normas.gba.gob.ar/ar-b/ley/2025/15558/554025 | primaria (norma) | 3 | 3 | 3 | 3 | [L] arts. 20 a 25 (la tabla del art. 20 se leyó aplanada en texto) |
| C18 | Informe `posicion-contraria.md` de esta misma investigación, que leyó Mirrlees y otros (2011), *Tax by Design*, IFS/OUP, y Harrison y Krelove (2005), *VAT Refunds*, IMF WP/05/218 | `Impuestos/.investigacion/posicion-contraria.md` | secundaria para este ángulo | 3 | 2 | 2 | 2 | [S] (leídas por otro ángulo) |

Fuentes que no se pudieron leer: OCDE, *International VAT/GST Guidelines* (2017); OCDE, *Consumption Tax Trends 2024*; FMI, *The Modern VAT* (2001); el texto consolidado vigente de la Directiva 2006/112/CE en EUR-Lex (devolvió una página vacía); la Ley Tarifaria 2026 y el Código Fiscal de la Ciudad de Buenos Aires (el sitio de AGIP es una aplicación de JavaScript); la Ley 27.429 (Consenso Fiscal) en InfoLEG (el identificador probado era de otra norma).

## 1. Impuestos al consumo (entrada)

- Tipos. C2 nombra la VAT como «the main form of indirect taxation» de muchos países y la introducción francesa de 1954 («The taxe sur la valeur ajoutée was introduced in 1954»). C3 define cascada: «the levying of tax on items that have already been taxed».
- Quién lo soporta y quién lo paga: C18 trae de *Tax by Design* (cap. 7, p. 168): «the tax is in effect imposed on the value of the final product but is collected in small chunks from each link in the supply chain» y «only VAT on retail sales cannot be reclaimed». Fullerton y Metcalf (vía C18): la incidencia económica depende de las elasticidades, no de quién tiene la obligación legal. La directiva lo dice como principio (C1 art. 1.2, abajo).
- Retail sales tax: C3 cita a Ring (1989): «about 40 percent of the revenue from the state-level retail sales taxes (RSTs) in the United States are collected on business purchases». [M: Ring no se leyó, viene de Keen].
- Impuestos específicos o internos: no se buscó fuente propia (hueco menor; la entrada los nombra sin cifras). En Argentina, el Código Fiscal PBA (C16 art. 188 a) excluye de la base de Ingresos Brutos «los importes correspondientes a impuestos internos, impuesto al Valor Agregado –débito fiscal-, impuesto sobre los Combustibles Líquidos y Gas Natural…», lo que confirma que existen como impuestos aparte.

## 2. IVA

### Principio y método

- C1 art. 1.2: «El principio del sistema común de IVA consiste en aplicar al comercio de bienes y servicios un impuesto general sobre el consumo exactamente proporcional al precio de los bienes y de los servicios, sea cual fuere el número de operaciones que se produzcan en el circuito de producción y distribución precedente a la fase de gravamen. En cada operación será exigible el IVA, liquidado sobre la base del precio del bien o del servicio gravados al tipo impositivo aplicable a dichos bienes y servicios, previa deducción del importe de las cuotas impositivas devengadas que hayan gravado directamente el coste de los diversos elementos constitutivos del precio. El sistema común de IVA se aplicará hasta la fase de venta al por menor, incluida ésta.»
- C1 art. 168: el sujeto pasivo deduce «en la medida en que los bienes y los servicios se utilicen para las necesidades de sus operaciones gravadas» el IVA devengado o pagado por bienes y servicios que le prestó otro sujeto pasivo.
- C1 art. 93: «Los tipos impositivos aplicables a los hechos imponibles serán los vigentes en el momento en que tenga lugar el devengo del impuesto.»
- C2: el método de crédito por factura «works reasonably well if all supplies are taxable, but starts to break down when some supplies in a chain are exempt».
- Ejemplo numérico de tres etapas: ninguna fuente leída trae uno con números; la nota lo construye (aritmética de la base, con 21 % para que sea reconocible y 10 % como tasa neutra). Marcar como ejemplo propio.

### Exento frente a tasa cero

- C2 (sec. VII.C): «A zero rate is therefore an exemption of the supply from output tax» … la tasa cero «make[s] the supply "taxable" in a technical sense and therefore achieves the objective of bringing these transactions within the operation of the VAT credit for input tax, which an exemption does not. This is because a VAT credit is allowed only for inputs to be used in making taxable supplies.» Los que no aceptan el término hablan de «exempt with credit».
- C2: la UE técnicamente «exime» las exportaciones (art. 146) pero da derecho a deducir (art. 169 b): «This has the same effect as zero rating». C1 art. 169 b) confirma la deducción para operaciones exentas por los arts. 146 a 149.
- C2 (sec. V): exenciones a mitad de la cadena: el banco exento que contrata guardias de seguridad no recupera el IVA, «The bank would have an incentive to hire security guards as its own employees»; «Widespread exemptions can therefore undermine the integrity of the VAT as a whole».
- C3: «Even the best designed VATs embody some degree of cascading in the form of 'exemptions'».
- C2 (VII.E): la tasa cero interna «is widely viewed as inappropriate, because it amounts to a subsidy».

### Prorrata

- C1 art. 173.1: «sólo se admitirá la deducción por la parte de las cuotas del IVA que sea proporcional a la cuantía de las operaciones primeramente enunciadas».
- C1 art. 174.1: numerador = volumen de negocios anual, sin IVA, de operaciones con derecho a deducción; denominador = el mismo más las demás.
- C8 art. 13 (Argentina): cuando las compras «se destinen indistintamente a operaciones gravadas y a operaciones exentas o no gravadas y su apropiación a unas u otras no fuera posible, el cómputo respectivo sólo procederá respecto de la proporción correspondiente a las primeras», estimada durante el ejercicio y ajustada en el último mes.

### Saldo a favor y devolución

- C1 art. 183: «Cuando la cuantía de las deducciones supere la del IVA devengado durante un período impositivo, los Estados miembros podrán trasladar el excedente al período impositivo siguiente, o bien proceder a la devolución de acuerdo con las modalidades por ellos fijadas.»
- C18 (Harrison y Krelove): el proceso de devolución es «the "Achilles heel" of the VAT»; causas de saldos: exportaciones, retenciones de IVA, estacionalidad, bienes de capital, alícuotas duales.

### Alícuotas reducidas

- C1 (texto de 2006): art. 97.1 «el tipo normal no podrá ser inferior al 15 %» (2006-2010); art. 98.1 «Los Estados miembros podrán aplicar uno o dos tipos reducidos»; art. 99.1 «no puede ser inferior al 5 %». La Directiva se modificó después (por ejemplo, en materia de tipos); no se leyó el texto consolidado vigente.
- C3: el caso de las alícuotas reducidas para los pobres es débil: «even poorly targeted spending may be a better way to support the poor than a reduced rate».

### Umbrales de inscripción

- C2 (sec. II.B): «Most states require only some of the many persons active in business within the state to be taxable persons. This is normally achieved by setting a minimum level or threshold». El umbral se mide sobre las operaciones gravadas, varía por país y momento, se justifica por el costo de administrar a los muy chicos, y suele permitir la inscripción voluntaria.
- C1 art. 285 (texto de 2006): franquicia para quienes tengan volumen anual «como máximo igual a 5 000 euros» en los Estados que no usaron la facultad de 1967. Régimen reformado después; no leído.
- C18 (Tax by Design, cap. 7): las empresas debajo del umbral británico «are in effect VAT exempt»; «the case for a substantial registration threshold is strong».

### Descuento y nota de crédito

- C1 art. 90.1: «En los casos de anulación, rescisión, impago total o parcial o reducción del precio, después del momento en que la operación quede formalizada, la base imponible se reducirá en la cuantía correspondiente».
- C8 art. 10: precio neto «neto de descuentos y similares efectuados de acuerdo con las costumbres de plaza»; art. 11: devoluciones, rescisiones, descuentos, bonificaciones o quitas posteriores ajustan el impuesto a la alícuota original y «se presumirá, sin admitirse prueba en contrario, que los descuentos, bonificaciones y quitas operan en forma proporcional al precio neto y al impuesto facturado».

### Recurso canónico propuesto

C2 (capítulo 6 de *Tax Law Design and Drafting*): secs. V (exenciones) y VII (tasa cero) para exento frente a tasa cero; C1 arts. 1, 168, 173 a 175 y 183 como redacción de referencia.

## 3. Impuesto a las ventas

- C5 (syllabus): «South Dakota, like many States, taxes the retail sales of goods and services in the State. Sellers are required to collect and remit the tax to the State, but if they do not then in-state consumers are responsible for paying a use tax at the same rate.» Sostiene: «Because the physical presence rule of Quill is unsound and incorrect, Quill Corp. v. North Dakota, 504 U. S. 298, and National Bellas Hess, Inc. v. Department of Revenue of Ill., 386 U. S. 753, are overruled.» Decidido el 21 de junio de 2018. La ley de Dakota del Sur alcanza a vendedores que «deliver more than $100,000 of goods or services into the State or engage in 200 or more separate transactions». El cumplimiento del use tax por los consumidores es «notoriously low»; el Board of Equalization de California estimó «a 4 percent collection rate».
- C6: «Purchasers who are engaged in the business of selling tangible personal property may issue resale certificates when purchasing items they will sell in the regular course of their business operations. When a seller accepts a valid resale certificate in good faith and in a timely manner, the seller does not owe tax on that sale.» No se usa para lo que el comprador va a usar en lugar de vender; el mal uso tiene multas e intereses.
- C7: «Forty-five states levy a state-level sales tax… and 38 states allow local sales taxes»; cinco estados sin impuesto estatal (Alaska, Delaware, Montana, New Hampshire, Oregon); promedio combinado ponderado por población 7,53 %; California tiene la alícuota estatal más alta, 7,25 %. Glosario de la misma página: «A sales tax should exempt business-to-business transactions which, when taxed, cause tax pyramiding.»
- C3: alrededor del 40 % de la recaudación de los RST estatales recae sobre compras de empresas (Ring 1989, [M]).
- Cascada: C3 resume el informe Chelliah (India): estructura opaca, tasas efectivas «…almost fortuitous and largely unknown to policymakers»; las exportaciones llevan impuesto no recuperado, «…a great hindrance to our export efforts», y favorece importaciones. Integración vertical: «This has indeed always been a major concern in turnover tax systems». Evidencia: Bovenberg (1987, Tailandia) +0,004 % del PBI por reemplazar cascada con IVA; Smart y Bird (2009): pasar a IVA en provincias canadienses subió la inversión «about 12 percent». Keen concluye que las pérdidas «may plausibly be large even at a fairly low nominal tax rate and with relatively few stages of production».
- C18 (*Tax by Design*, cap. 20, p. 476): impuestos sobre ventas sin deducir insumos «are in general grossly inefficient and have no place in a good tax system».
- Contra-evidencia: Bovenberg (vía Keen) encuentra un efecto chico; ninguna fuente leída defiende el impuesto a los ingresos brutos con evidencia (hueco, igual que en C18).

## 4. Lugar de la operación

- C2: dos principios: «the origin principle charges a transaction… if the transaction originates or is created within the state, and the destination principle charges the transaction if it is destined for consumption in the state». Si dos Estados usan principios distintos hay doble imposición o ninguna. «In practice, however, and with limited exceptions, states have adopted the destination basis as the primary basis… This requires a charge to VAT on all transactions occurring within the state and also on all imports to the state.»
- C2 (VII.D): «The destination principle calls not only for removing a direct charge to VAT from exports and international services, but also for removing any VAT indirectly imposed on those supplies in the form of input tax paid by a supplier. Only if the input tax is rebated will the goods leave the state free of VAT.»
- C2 (sec. M): «The destination principle requires a charge to VAT to be placed on all imports», con la ley aduanera como base.
- C2 sobre servicios: el lugar es difícil de determinar; los bienes importados garantizan el pago, los servicios no; «fairness and neutrality require that services that originate overseas be taxed in the same way as services that originate in the state». Reverse charge (nota 89): «Reverse charging applies where the person receiving the supply is deemed also to be the supplier so that a charge to VAT may be applied to it».
- C1 art. 196 (texto de 2006): deudor del IVA es el destinatario sujeto pasivo de ciertos servicios cuando el prestador no está establecido en ese Estado miembro. Las reglas de lugar de los servicios se reformaron desde 2010; no se leyó el texto consolidado.
- C4 (UE): OSS desde el 1 de julio de 2021, sucesora del MOSS (1 de enero de 2015); umbral anual de EUR 10 000 para servicios B2C transfronterizos de telecomunicaciones, radiodifusión y electrónicos y ventas a distancia intracomunitarias; IOSS para envíos de valor intrínseco que no exceda EUR 150; «deemed supplier»: quien facilita una venta «through the use of an electronic interface (e.g. marketplace, platform, portal etc.)» se trata como proveedor a efectos del IVA.
- OCDE: no leída. Lo que se sabe de sus Directrices (neutralidad, destino, cliente B2B, registro simplificado B2C, plataformas) queda sin cita directa.
- Argentina (C8 art. 1 incs. d y e; C10): ver abajo.

## 5. IVA en Argentina

- Norma: Decreto 280/97 aprueba el «texto ordenado en 1997» de la Ley de IVA, fechado el 26/3/97 (C8).
- Objeto (C8 art. 1): ventas de cosas muebles en el país, obras y servicios del art. 3 realizados en el país, importaciones definitivas, servicios del exterior utilizados en el país por responsables inscriptos (inc. d) y servicios digitales del exterior (inc. e).
- Alícuotas (C8 art. 28): «La alícuota del impuesto será del veintiuno por ciento (21%).» «Esta alícuota se incrementará al veintisiete por ciento (27%) para las ventas de gas, energía eléctrica y aguas reguladas por medidor y demás prestaciones comprendidas en los puntos 4, 5 y 6, del inciso e) del artículo 3º, cuando la venta o prestación se efectúe fuera de domicilios destinados exclusivamente a vivienda o casa de recreo o veraneo o en su caso, terrenos baldíos y el comprador o usuario sea un sujeto categorizado en este impuesto como responsable inscripto o se trate de sujetos que optaron por el Régimen Simplificado». «Estarán alcanzados por una alícuota equivalente al cincuenta por ciento (50%) de la establecida en el primer párrafo:» sigue la lista: animales vivos y carnes, frutas, legumbres y hortalizas frescas, granos, harina de trigo, pan sin envasar (inc. a); labores agrícolas (inc. b); vivienda (inc. c); intereses de préstamos a responsables inscriptos (inc. d); bienes de la planilla anexa al inc. e (bienes de capital); planilla del inc. f; transporte de pasajeros (inc. h); medicina prepaga no exenta (inc. i); cooperativas de trabajo al Estado (inc. j); gas licuado (inc. k); fertilizantes (inc. l); energía eléctrica para riego agroindustrial (inc. m, incorporado por la Ley 27.802, B.O. 6/3/2026). El Poder Ejecutivo puede reducir las alícuotas hasta un 25 %.
- Segunda fuente de las tres alícuotas: C11 (prensa, 2022): 21 % «general», 10,5 % «en determinados casos especiales», 27 % «energía eléctrica y telecomunicaciones». Coincide en las cifras; es secundaria.
- Crédito fiscal (C8 art. 12): se resta el gravamen facturado por compras, importaciones, locaciones y servicios, «Sólo… en la medida en que se vinculen con las operaciones gravadas». Límite para automóviles: «VEINTE MIL PESOS ($ 20.000) neto» (cifra de 2001 en el texto, sin actualizar en la copia leída).
- Prorrata: art. 13 (arriba).
- Saldo (C8 art. 24): «El saldo a favor del contribuyente que resultare por aplicación de lo dispuesto en los artículos precedentes… sólo deberá aplicarse a los débitos fiscales correspondientes a los ejercicios fiscales siguientes.» Párrafo 2: no se aplica «a los saldos de impuesto a favor del contribuyente emergentes de ingresos directos, los que podrán ser objeto de las compensaciones y acreditaciones previstas por los artículos 35 y 36 de la Ley Nº 11.683… o en su defecto, le será devuelto o se permitirá su transferencia a terceros». Artículo sin número a continuación: devolución de créditos por bienes de uso que sigan en el saldo después de «seis (6) períodos fiscales consecutivos». Los nombres «saldo técnico» y «saldo de libre disponibilidad» no aparecen en la ley ni en las páginas de ARCA leídas: son los de la práctica para el primer y el segundo párrafo (hueco: falta una fuente oficial que los use).
- Liquidación (C8 art. 27): «se liquidará y abonará por mes calendario sobre la base de declaración jurada»; importaciones con los derechos de importación; AFIP puede establecer retención o percepción en la fuente.
- Exportadores (C8 art. 43): computan el IVA de compras vinculadas a exportaciones; si no alcanza, se acredita contra otros impuestos, se devuelve o se transfiere, hasta un límite sobre el monto exportado.
- Servicios digitales (C8 art. 3 e) 21 m); art. 1 e); artículo sin número a continuación del 27): el prestatario ingresa el impuesto; «De mediar un intermediario que intervenga en el pago, éste asumirá el carácter de agente de percepción». Presunción sin prueba en contrario: IP o SIM, dirección de facturación, cuenta bancaria. Incorporado por la Ley 27.430 (B.O. 29/12/2017).
- C10 (ARCA, RG 4240/18): se aplica cuando el prestatario no es responsable inscripto; las entidades del país que facilitan o administran pagos al exterior actúan como agentes de percepción; sin intermediario, el prestatario ingresa el impuesto «hasta el último día del mes en que se efectuó el pago». Con tarjeta de crédito, la percepción se practica a la fecha de cobro del resumen.
- Registro y declaración (C9): «Desde noviembre 2025, inclusive, los responsables inscriptos en el impuesto al valor agregado deben cumplir con la obligación de determinación e ingreso del gravamen mediante el procedimiento electrónico simple, integral y asistido denominado "IVA Simple", según lo establecido a través de la RG 5705/2025.» Optativo de junio a octubre de 2025; quien optaba no tenía que registrar las operaciones en el «Libro de IVA Digital». Declaración jurada mensual F.2051 en el «Portal IVA», con un módulo de registración electrónica que trae los comprobantes emitidos y recibidos de la base de ARCA para que el contribuyente los valide. Las percepciones se pueden computar en el período en que se sufrieron o en alguno de los 5 siguientes (RG 5750). **Consecuencia: la nota no puede presentar el Libro de IVA Digital como vigente.** Su RG de creación (4597/2019, según la memoria de quien investiga) no se leyó.
- Condición frente al IVA (responsable inscripto, monotributista, exento, consumidor final): ya está en `Relacion-con-clientes/relacion-con-clientes-en-argentina.md` y `Comercio-electronico/Normativa/factura-electronica-de-arca.md` (enlazar).

## 6. Ingresos Brutos

- Hecho imponible (C16 art. 182): «El ejercicio habitual y a título oneroso en jurisdicción de la provincia de Buenos Aires, del comercio, industria, profesión, oficio, negocio, locaciones de bienes, obras y servicios, o de cualquier otra actividad a título oneroso -lucrativo o no-… estará alcanzada con el impuesto sobre los Ingresos Brutos».
- Base (C16 art. 187): «el gravamen se determinará sobre la base de los ingresos brutos devengados durante el período fiscal»; quien no lleva libros, sobre lo percibido. Art. 188 a): no integran la base el IVA débito fiscal, impuestos internos y otros, solo para los contribuyentes de derecho inscriptos.
- Exportaciones (C16 art. 186 d): no constituyen actividad gravada las exportaciones de mercaderías y de servicios «cuya utilización o explotación efectiva se lleve a cabo en el exterior» (texto según Ley 15.079).
- Alícuotas (C16 art. 223): «La Ley Impositiva fijará la alícuota general del impuesto y las alícuotas diferenciales». Ejemplo C17 (Ley 15.558, PBA 2026): la tabla del art. 20 tiene una columna general y siete tramos reducidos por ingresos del año anterior (Tramo 1 hasta $1.834.326.000; Tramo 7 hasta $15.286.053). Clase 4719 (venta al por menor en comercios no especializados): 5 % general, tramos que bajan a 3,50 % y 2,50 %. Clase 6201 (servicios de consultores en informática y suministros de programas): 5 % general y en los tramos 1 a 6, 3,50 % en el tramo 7. Lectura de una tabla aplanada: el orden de las columnas se infiere del encabezado. Art. 25: mínimo mensual de anticipo $10.967.
- CABA: no se leyó la Ley Tarifaria 2026 (hueco).
- Convenio Multilateral (C12): art. 1, alcance: actividades de un mismo contribuyente en dos o más jurisdicciones cuyos ingresos «por provenir de un proceso único, económicamente inseparable, deben atribuirse conjuntamente a todas ellas»; incluye ventas a otra jurisdicción por correspondencia o teléfono cuando hay gastos vinculados. Art. 2: 50 % por gastos «efectivamente soportados» y 50 % por ingresos; los ingresos de las operaciones a distancia se atribuyen «a la jurisdicción correspondiente al domicilio del adquirente». Art. 3: no son gastos computables la materia prima y la mercadería, publicidad, tributos, intereses, honorarios de directores sobre el 1 % de la utilidad. Art. 5: coeficientes del último balance cerrado en el año calendario anterior. Regímenes especiales: construcción 10/90 (art. 6); seguros y créditos 80/20 (art. 7); entidades financieras (art. 8); transporte, origen del viaje (art. 9); profesiones liberales y consultoras 80/20 (art. 10); rematadores y comisionistas 80/20 (art. 11); prestamistas 80/20 (art. 12); productos primarios (art. 13). Art. 14: inicio y cese.
- Reforma (C13, 22/09/2026): Corrientes ratificó «las modificaciones normativas para la reforma del Convenio Multilateral, adoptadas por la COMARB»; para la vigencia plena falta completar el trámite legislativo en provincias pendientes. No se leyó el contenido de la reforma (hueco importante: puede cambiar el art. 2).
- SIFERE (C14): «es un sistema diseñado para que los contribuyentes del Convenio Multilateral puedan liquidar el Impuesto sobre los Ingresos Brutos»; presentación, pagos y consultas de declaraciones juradas mensuales y anuales, con clave fiscal.
- Padrón (C15): el Registro Único Tributario – Padrón Federal permite inscribirse y declarar modificaciones, ceses y altas «a través de un mismo canal»; novena y última etapa el 01/08/2026: «La adhesión de CABA completa las 24 jurisdicciones en Padrón Federal». El «Padrón Web» figura como sistema anterior (aprobación y prórroga).
- Monotributo unificado: ya está en `Emprender/Legal-e-impuestos/normativa-para-empezar-en-argentina.md` (RG Conjunta 5769/25, CABA desde el 01/01/2026, lista de provincias adheridas). Enlazar.
- Cascada: inferencia de la base sobre C16 (la base son los ingresos brutos, sin crédito por lo comprado) y la definición de C3. No se encontró un informe de organismo leído que lo diga de Ingresos Brutos en particular (hueco).
- SIRCREB, SIRTAC, percepciones: solo nombrar; están en la nota de recaudación en la fuente de Argentina y en `Comercio-electronico/Normativa/normativa-argentina.md`.

## Recursos canónicos

| Componente | Recurso | Qué parte | En qué fijarse |
|---|---|---|---|
| IVA | C2 | secs. V a VII | exención con y sin crédito |
| IVA | C1 | arts. 1, 168, 173 a 175, 183 | la redacción del mecanismo |
| Impuesto a las ventas | C3 | sec. III | por qué la cascada distorsiona y empuja a integrarse |
| Impuesto a las ventas | C5 | syllabus | qué es el nexus y por qué cambió |
| Lugar de la operación | C2 | sec. II (ámbito territorial) y M | destino frente a origen |
| Lugar de la operación | C4 | toda la página | OSS, IOSS y el proveedor presunto |
| IVA en Argentina | C8 | arts. 1, 12, 13, 24, 28 | las alícuotas literales y el saldo |
| Ingresos Brutos | C12 | arts. 1 a 5 | el reparto 50/50 |

## Huecos

- Las Directrices de la OCDE (*International VAT/GST Guidelines*, 2017) y *Consumption Tax Trends 2024*: bloqueadas. Sin cifra de cuántos países tienen IVA ni texto literal de las directrices sobre destino, reverse charge y plataformas.
- *The Modern VAT* (FMI 2001): no conseguido.
- Texto consolidado vigente de la Directiva 2006/112/CE: el leído es el de 2006 (tipos, reglas de lugar de los servicios y franquicia de pequeñas empresas cambiaron después).
- Una fuente oficial que use los nombres «saldo técnico» y «saldo de libre disponibilidad».
- La RG 5705/2025 (IVA Simple) en su texto y la RG de creación del Libro de IVA Digital.
- El contenido de la reforma del Convenio Multilateral ratificada por Corrientes y su estado de vigencia.
- Ley Tarifaria 2026 de la Ciudad de Buenos Aires.
- Un informe de organismo sobre Ingresos Brutos como impuesto en cascada en Argentina.
- Impuestos específicos e internos: sin fuente propia.

## División del árbol frente al campo

- El campo (FMI, Directiva) no separa «lugar de la operación» del IVA: es un capítulo del IVA (ámbito territorial). Como nota aparte funciona porque también rige al impuesto a las ventas (nexus) y a Ingresos Brutos (Convenio Multilateral), pero conviene que `iva.md` lo enlace como parte de su mecanismo.
- `impuesto-a-las-ventas` junta dos cosas que el campo separa: el impuesto de una sola etapa a la venta minorista y el impuesto plurifásico acumulativo (cascada). El campo los opone a los dos al IVA; mantenerlos juntos sirve si la nota los distingue con claridad.
- `ingresos-brutos` es la nota argentina de los impuestos en cascada; no lleva el sufijo `-en-argentina` porque el impuesto solo existe allá.
