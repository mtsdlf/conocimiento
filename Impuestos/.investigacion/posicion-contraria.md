# Investigación: posición contraria y concepciones erróneas (Impuestos)

Ángulo: la mejor evidencia en contra de lo que el tema va a afirmar (según `Impuestos/impuestos.md` y el árbol de `ALCANCE.md`), los debates con evidencia y las concepciones erróneas de quien no es contador. Fecha: 2026-11-27.

Límite de esta ronda: sin buscador web (cupo de la sesión agotado); se trabajó con fetch directo. La OCDE, el IFS (página), CEPAL y las notas técnicas del FMI dieron 403. Los códigos de fuente (F1…F18) son los de `fundamentos.md`; acá se repiten solo los que se usan.

| # | Fuente | URL | Marca |
|---|---|---|---|
| F1 | Mirrlees y otros (2011), *Tax by Design*, IFS/OUP | https://ifs.org.uk/sites/default/files/output_url_files/taxbydesign.pdf | [L] caps. 2, 4, 6, 7, 9 y 20 |
| F2 | Fullerton y Metcalf (2002), *Tax Incidence*, NBER WP 8829 | https://www.nber.org/system/files/working_papers/w8829/w8829.pdf | [L] intro y sec. 2 |
| F3 | Harrison y Krelove (2005), *VAT Refunds*, IMF WP/05/218 | https://www.imf.org/external/pubs/ft/wp/2005/wp05218.pdf | [L] |
| F5 | Thuronyi (ed.), *Tax Law Design and Drafting*, FMI, cap. 16 | https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch16.pdf | [L] sec. IV.B |
| F8 | Wikipedia, *Value-added tax* | https://en.wikipedia.org/wiki/Value-added_tax | [L] parcial |
| F12 | Ley de IVA de Argentina, t.o. 1997, art. 24 | https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42701/texact.htm | [L] por lector automático |
| F13 | OIT (2014), *Monotributo en América Latina* | https://www.ilo.org/wcmsp5/groups/public/---americas/---ro-lima/documents/publication/wcms_357452.pdf | [L] resumen y conclusiones |
| F18 | GOV.UK, VAT for businesses | https://www.gov.uk/vat-businesses | [L] |

## 1. Lo que el tema afirma y la evidencia en contra

### 1.1 «El IVA lo paga el cliente; la empresa solo lo junta» (entrada del tema, párrafo 2)

A favor: F1 (cap. 7, p. 168): el IVA grava todas las ventas pero deja deducir el de las compras; «the tax is in effect imposed on the value of the final product but is collected in small chunks from each link in the supply chain»; «only VAT on retail sales cannot be reclaimed. VAT therefore taxes only final consumption». F18: la empresa inscripta cobra IVA en sus ventas y descuenta el de sus compras. [L]

En contra (incidencia económica): F2: la incidencia económica depende de las elasticidades, no de quién tiene la obligación legal; un impuesto a un bien se reparte entre consumidores y productores. F1 (cap. 2): ante una suba de un impuesto al alcohol, las empresas pueden absorber parte; las empresas no soportan cargas en sí mismas, la carga termina en clientes, empleados o accionistas. F8: la incidencia del IVA «may not fall entirely on consumers», porque los comerciantes a menudo lo absorben para sostener ventas (sin cita en Wikipedia). [L/S]

Excepciones legales donde el IVA sí queda en la empresa (F1, cap. 7, pp. 174-175): la empresa exenta no recupera el IVA de sus compras; el IVA no recuperable de un eslabón exento es «a pure extra cost» si vende a otras empresas. [L]

Lectura para la nota: la frase vale como incidencia legal y como diseño; en lo económico es una simplificación. Va como `[!IMPORTANT]`.

### 1.2 Regresividad del IVA: ¿sobre el ingreso o sobre el consumo?

F1, cap. 4 (pp. 80-81): los impuestos indirectos «are regressive on this measure» (como proporción del ingreso disponible), porque los hogares de bajos ingresos gastan mucho en relación con su ingreso en un momento dado; pero en el Reino Unido el IVA es una proporción menor del gasto de los hogares pobres (tasa cero o reducida en alimentos y energía doméstica), y con una mirada de ciclo de vida, en la que ingreso y gasto se igualan, el IVA «must actually take up a smaller share of lifetime resources for lifetime-poor households, and in that sense it is progressive». El impuesto al tabaco es regresivo en cualquier medida. [L]

F1, cap. 20: su paquete de reforma del IVA «looks progressive when measured against people's expenditure, but slightly regressive when measured against income» y sería aproximadamente neutral en el ciclo de vida. [L]

F1, cap. 20 (conclusiones): las alícuotas diferenciadas por bien suelen venir de no mirar el sistema entero; el impuesto a la renta y las transferencias son el instrumento para redistribuir. F1, cap. 7, cita a Crawford, Keen y Smith (2010): «the extensive rate differentiation still found in the VATs of EU members is coming to look increasingly quaint». [L]

F8: los críticos lo llaman regresivo; los defensores, proporcional; un estudio de la OCDE lo encontró levemente progresivo [sobre el gasto]; puede atenuarse con alícuotas reducidas o transferencias. [S; el estudio OCDE/KIPF 2014 *The Distributional Effects of Consumption Taxes in OECD Countries*, https://www.oecd.org/en/publications/the-distributional-effects-of-consumption-taxes-in-oecd-countries_9789264224520-en.html, dio 403: no leído]

### 1.3 Impuestos en cascada

F1, cap. 20 (p. 476): impuestos sobre ventas sin deducir el costo de los insumos «are in general grossly inefficient and have no place in a good tax system. This leads to a presumption against all kinds of transactions taxes, input taxes, and turnover taxes.» [L]

F1, cap. 6, sec. 6.1.1, eficiencia productiva (Diamond y Mirrlees, 1971): los insumos producidos no deberían gravarse. [L]

Contra-evidencia (la defensa práctica del impuesto a los ingresos brutos o a la facturación): no se encontró una fuente leída que lo defienda con evidencia. Hueco. (Inferencia: su defensa habitual es la recaudación fácil y la autonomía de los gobiernos subnacionales; sin fuente.)

### 1.4 Régimen simplificado y «enanismo fiscal»

F13 (OIT 2014): el propósito del monotributo argentino fue «la formalización de un conjunto heterogéneo y muy numeroso de contribuyentes a través del registro de sus operaciones e ingresos derivados» (p. 37). Los regímenes de cuota fija tienen tasas efectivas decrecientes al crecer el ingreso declarado. Costo: «el costo generado por actitudes de “enanismo fiscal”, elusión y evasión impositiva que el Monotributo podría propiciar a través de la existencia de ciertos incentivos perversos que actúan como barreras de salida del mismo hacia el régimen general». En las conclusiones: el régimen especial puede incentivar a «permanecer indefinidamente dentro del régimen especial aun teniendo la capacidad de tributar bajo el régimen general», con costo en recaudación, eficiencia (enanismo) y equidad; debería ser un «puente transitorio». El SIMPLES brasileño, con alícuotas progresivas, hace el «salto» al régimen general «menos traumático o brusco» que los esquemas de cuota fija (Argentina, Uruguay). [L]

F1, cap. 7 (umbral de registro del IVA en el RU, £70.000 en 2010-11): las empresas que no se registran no cobran IVA ni recuperan el de sus compras, «so they are in effect VAT exempt»; el gobierno estima 2,9 millones de pequeñas empresas no registradas frente a 1,95 millones registradas. Sobre el régimen optativo de tasa plana: obliga a calcular los dos regímenes, lo que sube el costo de cumplimiento, «ironic when the scheme exists precisely to reduce them». Pero «the case for a substantial registration threshold is strong». [L]

No leído: la evidencia econométrica de amontonamiento debajo de los umbrales (Kleven y Waseem 2013; Liu, Lockwood, Almunia y Tam 2021 para el umbral del IVA británico). Hueco: sin URL verificada.

### 1.5 Recaudación en la fuente y saldos inmovilizados

F3, abstract: en el IVA de crédito por factura algunas empresas, sobre todo exportadoras, pagan más en sus compras que lo que deben por sus ventas y piden devolución; «serious problems arise in practice, including opportunities for fraud and corruption, and denial of refunds by governments with cash shortages. This makes the refund process the “Achilles heel” of the VAT.» Muestra de 36 países. [L]

F3, III.B: entre quienes piden devoluciones están los sujetos a retención: «some countries, particularly in Latin America and West Africa, require certain business and government entities to withhold amounts of VAT from payments to their suppliers. These schemes have several drawbacks: in particular, refund claims can proliferate under these arrangements, especially if withholding rates are set too high.» También: saldos por caídas estacionales (muchos países obligan a trasladarlos tres o seis meses), compras grandes de bienes de capital, alícuotas duales. [L]

F3, nota 30: las administraciones avanzadas y las empresas pueden no considerar buena práctica obligar a trasladar el saldo. [L]

F12 (Argentina, art. 24): el saldo a favor que resulta de débitos y créditos «sólo deberá aplicarse a los débitos fiscales correspondientes a los ejercicios fiscales siguientes»; esto no se aplica a los saldos «emergentes de ingresos directos», que pueden compensarse, devolverse o transferirse según los arts. 35 y 36 de la Ley 11.683. [L por lector automático, citas parciales; la expresión «libre disponibilidad» no apareció en la parte leída]

### 1.6 «Lo devengado no es lo pagado» (entrada del tema)

F5, cap. 16, sec. IV.B: bajo el método de lo percibido el ingreso se reconoce cuando se recibe; bajo el de lo devengado, cuando nace el derecho a cobrarlo. «salary and wage earners would normally account for income and deductions on a cash basis, and legal persons conducting businesses account for income and deductions on an accrual basis. Individuals conducting business typically enjoy some flexibility. In particular, it may be appropriate and simpler for smaller businesses to use cash-basis accounting.» [L]

Contra-evidencia para la nota: no es universal; muchas legislaciones dejan a personas y pequeñas empresas usar lo percibido. La afirmación de la entrada vale para sociedades.

## 2. Concepciones erróneas de quien no es contador

Ninguna fuente leída nombra estas frases como «mito»; todas se infieren de textos que explican lo correcto. Se marca así en la nota.

| Creencia | Lo que dicen las fuentes | Fuente | Nota del tema que lo explica |
|---|---|---|---|
| «El IVA lo paga la empresa» | Legalmente lo cobra y lo entrega; solo el IVA de la venta final no se recupera; la empresa sí lo soporta si está exenta, si no puede usar el crédito o si absorbe el impuesto en el precio | F1 caps. 7 y 2; F2 | `Impuestos-al-consumo/iva.md`, `Impuestos-al-consumo/impuestos-al-consumo.md` |
| «Una retención es un impuesto extra» | La retención es una forma de cobrar el impuesto de otro: el PAYE británico lo remite la empresa pero el obligado es el trabajador; las retenciones de IVA generan pedidos de devolución, o sea, son a cuenta | F1 cap. 2; F3 III.B | `Recaudacion-en-la-fuente/recaudacion-en-la-fuente.md`, `Recaudacion-en-la-fuente/pagos-a-cuenta.md` |
| «Facturar con monotributo no lleva IVA, así que es más barato para el cliente» | Para un cliente inscripto en IVA, comprarle a quien no cobra IVA no es más barato en ese impuesto: el IVA de quien no está inscripto no se discrimina y no genera crédito; un eslabón exento en medio de la cadena puede hacer que el producto final pague más que la alícuota plena | F1 cap. 7 (ejemplo A-B-C, pp. 174-175, y no registrados = exentos de hecho, p. 178) | `Obligacion-tributaria/regimen-simplificado.md`, `Impuestos-al-consumo/iva.md` |
| «El saldo a favor es plata que tengo» | El saldo técnico solo se usa contra débitos futuros; el de retenciones y percepciones tiene otro régimen; las devoluciones son el «talón de Aquiles» del IVA y los fiscos con poca caja las demoran | F3; F12 art. 24 | `Recaudacion-en-la-fuente/pagos-a-cuenta.md`, `Cumplimiento/declaracion-y-pago.md`, `Impuestos-al-consumo/iva-en-argentina.md` |
| «El impuesto a la renta se paga sobre lo cobrado» | Las empresas societarias tributan por lo devengado; lo percibido queda normalmente para asalariados y a veces para pequeños negocios | F5 cap. 16 | `Impuestos-a-la-renta/impuestos-a-la-renta.md`, `Impuestos-a-la-renta/resultado-impositivo.md` |
| «Un impuesto a las empresas no lo paga nadie de carne y hueso» | Todo impuesto que paga una empresa recae al final en clientes, empleados o accionistas; «often seen as 'victimless'. They are not.» | F1 cap. 2 | `Fundamentos/fundamentos-de-impuestos.md` |

## 3. Huecos

- Ninguna fuente que nombre literalmente estas concepciones erróneas (material docente, encuestas a pymes).
- Evidencia econométrica de amontonamiento debajo de umbrales (Kleven y Waseem 2013; Liu y otros 2021): no verificada.
- OCDE/KIPF 2014 (regresividad) y *International VAT/GST Guidelines* (neutralidad): 403.
- Una defensa con evidencia de los impuestos a la facturación (Ingresos Brutos) o de los regímenes de retención: no encontrada.
- Costos de cumplimiento medidos (horas por año, por país): no leído.
- Saldos inmovilizados en Argentina con cifras: no leído.
