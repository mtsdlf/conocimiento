# Investigación: Fundamentos de Impuestos

Ángulo: historia (del IVA, sobre todo), principios de un buen impuesto, incidencia, y el mapa de fuentes del saber tributario. Fecha: 2026-11-27.

Límite de esta ronda: el buscador web de la sesión se agotó al empezar (cupo compartido entre subagentes), así que todo se trabajó con fetch directo a URLs conocidas. Los sitios de la OCDE (oecd.org), el IFS (ifs.org.uk, página del libro), econlib (por curl), CEPAL y el índice de notas técnicas del FMI devolvieron 403 a la lectura automática. Lo que depende de ellos queda [M] o [S].

Marcas: [L] texto leído entero o la sección pertinente leída; [M] metadatos, ficha o índice; [S] resumen secundario o de otro texto.

## 1. Tabla de fuentes

| # | Fuente | URL | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|---|---|
| F1 | Mirrlees, J. y otros (2011), *Tax by Design*, Oxford University Press para el IFS (PDF completo) | https://ifs.org.uk/sites/default/files/output_url_files/taxbydesign.pdf | Primaria (informe de comisión de expertos) | 3 | 3 | 3 | 3 | [L] caps. 2, 4, 6, 7, 9 y 20 (por búsqueda en el texto) |
| F2 | Fullerton, D. y Metcalf, G. (2002), *Tax Incidence*, NBER WP 8829 (Handbook of Public Economics, vol. 4) | https://www.nber.org/papers/w8829 ; PDF https://www.nber.org/system/files/working_papers/w8829/w8829.pdf | Primaria (survey académico) | 3 | 3 | 2 | 2 | [L] introducción y sección 2 |
| F3 | Harrison, G. y Krelove, R. (2005), *VAT Refunds: A Review of Country Experience*, IMF WP/05/218 | https://www.imf.org/external/pubs/ft/wp/2005/wp05218.pdf | Primaria (estudio del FMI, 36 países) | 3 | 3 | 3 | 3 | [L] abstract, II, III.B, V.A |
| F4 | Ebrill, Keen, Bodin y Summers (2001), *The Modern VAT*, FMI | https://www.imf.org/external/pubs/nft/2001/vat/ | Primaria (libro del FMI) | 3 | 3 | 2 | 3 | [M] índice y prefacio |
| F5 | Thuronyi, V. (ed.) (1996-1998), *Tax Law Design and Drafting*, FMI | https://www.imf.org/external/pubs/nft/1998/tlaw/eng/index.htm | Primaria (manual del FMI) | 3 | 3 | 2 | 3 | [M] índice; [L] cap. 6 intro (https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch6.pdf) y cap. 16 sec. IV.B (https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch16.pdf) |
| F6 | Smith, A. (1776), *La riqueza de las naciones*, libro V, cap. II, parte II, en Econlib | https://www.econlib.org/library/Smith/smWN.html?chapter_num=36 | Primaria (texto original) | 3 | 2 | 1 | 3 | [L] las cuatro máximas (fragmentos literales) |
| F7 | Wikipedia, *Maurice Lauré* | https://en.wikipedia.org/wiki/Maurice_Laur%C3%A9 | Secundaria | 1 | 1 | 1 | 2 | [L]; una sola referencia (BnF) |
| F8 | Wikipedia, *Value-added tax*, sección History | https://en.wikipedia.org/wiki/Value-added_tax | Secundaria | 1 | 2 | 1 | 1 | [L] parcial (primeros 100.000 caracteres) |
| F9 | TADAT (FMI, Banco Mundial y socios) | https://www.tadat.org/ | Primaria (marco de evaluación) | 3 | 2 | 1 | 3 | [L] portada |
| F10 | CIAT, sitio, publicaciones, biblioteca y CIATData | https://www.ciat.org/ ; https://www.ciat.org/publicaciones ; https://biblioteca.ciat.org ; https://www.ciat.org/ciatdata | Primaria (organismo) | 3 | 2 | 1 | 3 | [M]; el Modelo de Código Tributario no apareció enlazado en la portada (la URL probada dio 404) |
| F11 | Comisión Arbitral del Convenio Multilateral | https://www.ca.gob.ar/ | Primaria (organismo interjurisdiccional) | 3 | 2 | 1 | 3 | [L] portada: Convenio, resoluciones generales, casos concretos, SIFERE, SIRCREB, SIRTAC, Padrón Federal |
| F12 | Ley de IVA de Argentina, t.o. 1997 (Decreto 280/97), en InfoLEG | https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42701/texact.htm | Primaria (norma) | 3 | 3 | 1 | 3 | [L] arts. 1, 24 y 27 (por lector automático, citas cortas) |
| F13 | OIT (2014), Cetrángolo, Goldschmit, Gómez Sabaini y Morán, *Monotributo en América Latina. Los casos de Argentina, Brasil y Uruguay* | https://www.ilo.org/wcmsp5/groups/public/---americas/---ro-lima/documents/publication/wcms_357452.pdf | Primaria (estudio de organismo) | 3 | 3 | 2 | 3 | [L] resumen y conclusiones (por búsqueda en el texto) |
| F14 | Sitios argentinos de normas y profesión: InfoLEG, Boletín Oficial, argentina.gob.ar/normativa, ARCA, biblioteca de ARCA, FACPCE, Consejo Profesional de CABA | https://www.infoleg.gob.ar/ ; https://www.boletinoficial.gob.ar/ ; https://www.argentina.gob.ar/normativa ; https://www.arca.gob.ar/ ; https://biblioteca.arca.gob.ar/ ; https://www.facpce.org.ar/ ; https://www.consejo.org.ar/ | Primaria | 3 | 1 | 1 | 2 | [M] responden 200; la biblioteca de ARCA es una aplicación que no se pudo leer |
| F15 | OCDE: *Revenue Statistics*, *Consumption Tax Trends*, *International VAT/GST Guidelines* (2017) | https://www.oecd.org/en/topics/sub-issues/global-tax-revenues.html ; https://www.oecd.org/en/publications/consumption-tax-trends-2024_dcd4dd36-en.html ; https://www.oecd.org/en/publications/international-vat-gst-guidelines_9789264271401-en.html | Primaria | 3 | 3 | 2 | 3 | No leídas: 403 a la lectura automática |
| F16 | Banco Mundial, Taxes and Government Revenue | https://www.worldbank.org/en/topic/taxes-and-government-revenue | Primaria | 3 | 1 | 1 | 1 | [M] responde 200 |
| F17 | Directiva 2006/112/CE (IVA de la UE), EUR-Lex | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32006L0112 | Primaria (norma) | 3 | 3 | 1 | 3 | No leída: la página vino vacía al lector |
| F18 | GOV.UK, VAT for businesses | https://www.gov.uk/vat-businesses | Primaria (fisco del Reino Unido) | 3 | 1 | 2 | 1 | [L] |

## 2. Historia del IVA

- La idea de un impuesto al valor agregado la propuso en 1918 el industrial alemán Georg Wilhelm von Siemens para reemplazar el impuesto alemán a las ventas; ese impuesto en cascada recién se reemplazó en 1968 (F8, que cita a ICAEW). [S]
- Francia adoptó en 1948 el primer impuesto tipo IVA con mecanismo de crédito por factura: «When France adopted the first VAT-type tax with an invoice-based credit mechanism in 1948...» (F3, sección V.A, p. 26). El esquema «was further developed in 1954 and 1968, when the structure of the tax was improved to become a modern VAT (including broadening the base and extending the VAT credit mechanism)» (F3). [L]
- La *taxe sur la valeur ajoutée* «was introduced in 1954» (F5, cap. 6, nota 1, que remite al *Précis de fiscalité* de la DGI, 1994). [L]
- Maurice Lauré (1917-2001), funcionario francés, politécnico; «In 1952, he became deputy director of the new tax authority, the Direction générale des impôts»; «In 1954, he invented an indirect tax on consumption which became the TVA» (F7, una sola referencia, la BnF). [L de secundaria]
- Según F8, Lauré la aplicó primero en la colonia de Costa de Marfil en abril de 1954 y Francia la adoptó en su territorio en 1958; empezó por las grandes empresas y se extendió a todos los sectores. [S, sin fuente primaria leída; discrepa en el detalle con F3 (1948, 1954, 1968) y F5 (1954)]
- Expansión europea: el informe Neumark (1962) eligió el modelo francés; dos directivas de abril de 1967 lo hicieron común en la CEE (F8). [S]
- Cuántos países: «a key source of government revenue in over 120 countries» (F4, prefacio, 2001). [M]. F8 dice que a enero de 2025 la usan 175 de los 193 miembros de la ONU, todos los de la OCDE salvo Estados Unidos, citando *Consumption Tax Trends* de la OCDE. [S; la fuente de la OCDE no se pudo abrir]
- F5 (cap. 6): ningún país con IVA de los que describía Tait (1988) lo derogó; «the general trend has been to increase the rates of VAT and reduce the exceptions». [L]
- Por qué se adoptó rápido según F7: porque los contribuyentes de cada etapa administran y rinden el impuesto ellos mismos. [S]

## 3. Los cánones de Adam Smith y los principios de un buen impuesto

Smith, libro V, cap. II, parte II (F6), cuatro máximas, primera oración de cada una:

1. Igualdad: «The subjects of every state ought to contribute towards the support of the government, …» (en proporción a sus capacidades).
2. Certeza: «The tax which each individual is bound to pay ought to be certain, and not arbitrary.»
3. Comodidad: «Every tax ought to be levied at the time, or in the manner, in which it is most likely to be convenient …»
4. Economía: «Every tax ought to be so contrived as both to take out and to keep out of the pockets of the people …» (lo menos posible por encima de lo que entra al Estado).

*Tax by Design* (F1, cap. 2) propone, además de los objetivos de fondo, tres guías: «Other things being equal, a tax system is likely to be better if it is simple, neutral, and stable. But none is necessarily the right thing to aim for at all times». Neutralidad: «A neutral tax system is one that treats similar activities in similar ways»; «a neutral system minimizes distortions over people's choices and behaviour»; pero la neutralidad no siempre es deseable (impuestos ambientales, I+D). [L]

Eficiencia productiva: Diamond y Mirrlees (1971) muestran que el sistema debería asegurar la eficiencia productiva, lo que «implies that produced inputs should not be taxed, so that all taxes should fall on final consumption goods» (F1, sec. 6.1.1). [L]

## 4. Incidencia legal y económica

- F2, introducción: «the person who has the legal obligation to make a tax payment may not be the person whose welfare is reduced by the presence of the tax». La incidencia legal (statutory) es la distribución de los pagos según la obligación legal; la económica mide los cambios de bienestar. Ejemplo: el impuesto al salario de EE. UU. se reparte por ley mitad y mitad entre empleador y empleado, pero la visión estándar es que lo soportan enteramente los empleados. [L]
- F2, sec. 2: un impuesto a un bien se reparte entre consumidores y productores según las elasticidades relativas de demanda y oferta; «in markets with no impediments to market clearing, the economic incidence of a tax depends only on behavior (ηS and ηD) and not on legislative intent (statutory incidence)». [L]
- F1, cap. 2: «The legal incidence of a tax can be very different from the economic incidence or who bears the burden»; en el PAYE británico el trabajador es el obligado legal pero la empresa remite el impuesto; ejemplos del impuesto al alcohol (la empresa puede absorber parte) y del impuesto de sellos sobre la vivienda (lo paga el comprador pero, con oferta fija, cae sobre el vendedor). Las empresas son entidades legales: todo impuesto que pagan termina en clientes, empleados o accionistas; los impuestos a las empresas «are often seen as 'victimless'. They are not.» [L]

## 5. Mapa de fuentes del saber tributario

| Tipo | Ejemplos verificados | Peso |
|---|---|---|
| Normas y fiscos | Leyes de cada país; InfoLEG, Boletín Oficial, argentina.gob.ar/normativa, ARCA; Directiva 2006/112/CE; GOV.UK (HMRC) | Primaria y obligatoria donde rige |
| Organismos internacionales | FMI (*Tax Law Design and Drafting*, *The Modern VAT*, working papers), OCDE (*Revenue Statistics*, *Consumption Tax Trends*, *International VAT/GST Guidelines*), CIAT, Banco Mundial, TADAT | Primaria para diseño y administración; no obligatoria |
| Informes de expertos y libros de texto | *Tax by Design* (Mirrlees Review), Handbook of Public Economics (Fullerton y Metcalf) | Alta para principios y evidencia |
| Organismos interjurisdiccionales | Comisión Arbitral del Convenio Multilateral (Ingresos Brutos) | Primaria para su régimen |
| Profesión | FACPCE, Consejo Profesional de Ciencias Económicas de CABA | Práctica; secundaria frente a la norma |
| Estudios regionales | OIT 2014 sobre monotributos; CEPAL (no se pudo abrir) | Evidencia regional |

## 6. Recursos canónicos por vertical (propuestos)

| Vertical | Recurso | Parte | En qué fijarse |
|---|---|---|---|
| Obligación tributaria | FMI, *Tax Law Design and Drafting* | Cap. 2 (marco legal), cap. 4 (administración y procedimiento), cap. 12 (imposición presunta) | Que el hecho imponible y el sujeto los define la ley; que la imposición presunta es la base de los regímenes simplificados |
| Obligación: régimen simplificado | OIT (2014), *Monotributo en América Latina* | Resumen y conclusiones | El «salto» al régimen general y el «enanismo fiscal» |
| Impuestos al consumo | *Tax by Design*, caps. 6 y 7, y FMI *Tax Law Design and Drafting* cap. 6 | Sección del ejemplo A-B-C (exención frente a tasa cero) | Que la exención rompe la cadena y puede encarecer el producto final |
| Impuestos a la renta | FMI, *Tax Law Design and Drafting*, cap. 16 | Sec. IV.B, métodos contables | Percibido frente a devengado y quién usa cada uno |
| Recaudación en la fuente | FMI WP/05/218 (Harrison y Krelove) | III.B (quién pide devoluciones) | Que las retenciones de IVA generan saldos a favor, sobre todo si la alícuota es alta |
| Recaudación: retención de sueldos | FMI *Tax Law Design and Drafting*, cap. 15 (PAYE) | [M] no leído | — |
| Cumplimiento | TADAT | Las nueve áreas de resultado | Inscripción, declaración a tiempo, pago a tiempo, exactitud, disputas |

## 7. Huecos

- No se leyó ninguna página de la OCDE (403): ni la neutralidad de las *International VAT/GST Guidelines* ni el conteo de países de *Consumption Tax Trends*.
- No se leyó la Directiva 2006/112/CE (art. 1.2).
- No hay fuente primaria francesa sobre Lauré (*La taxe sur la valeur ajoutée*, 1952/1953) ni historia escrita por el FMI con fechas de Costa de Marfil.
- No se encontró el Modelo de Código Tributario del CIAT (la URL probada dio 404).
- Ningún libro de texto de finanzas públicas en castellano leído.
- La biblioteca de ARCA no se pudo leer (aplicación con JavaScript).
