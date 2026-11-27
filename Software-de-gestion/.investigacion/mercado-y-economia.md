# Mercado y economía del software de gestión: informe de investigación

Ángulo: cómo se vende y quién gana qué. Fecha de la investigación: 2026-11-27.

**Advertencia de método.** Todo lo de este informe se leyó por resumen del buscador, marcado [S]. Ninguna fuente se leyó entera ([L]) ni por abstract ([M]). Cada cifra es candidata: hay que abrir la fuente antes de escribirla en una nota. No se encontró ningún estudio con método que dé la proporción licencia/implantación ni el reparto del partner: eso es un hueco, no un dato. Las URL salieron de resultados del buscador; las del SEC, SAP, Oracle y Salesforce son del propio emisor.

Puntaje: autoridad / profundidad / ejemplos / unicidad, de 1 a 3.

## 0. Qué ya está escrito y qué es propio de este tema

| Ya está escrito (enlazar, no repetir) | Dónde |
|---|---|
| SaaS: MRR/ARR, CAC y LTV, valle de caja, margen bruto 68-80 %, múltiplo 11,4 contra 1,5 en servicios de TI, servicios de Salesforce FY2025 a −10,3 % de margen, Suarez-Cusumano-Kahl (relación convexa entre parte de servicios y margen), Bain sobre precio por asiento e IA | `Emprender/Modelo-de-negocio/saas.md` |
| Tipología de Hagiu y Wright; software con servicio; pagos como híbrido | `Emprender/Modelo-de-negocio/modelos-de-negocio-de-software.md` |
| Resourcing y securing; apertura óptima; comisión de una tienda de apps de comercio (15 % sobre lo que pasa del primer millón de dólares); absorción por la plataforma | `Producto/Plataformas/ecosistema-de-terceros.md` |
| Farrell y Klemperer, tres tipos de costo de cambio; «bargain-then-ripoff»; poca evidencia empírica (Greenstein 1993, mainframes); Porter 2008 con el software empresarial integrado como ejemplo | `Estrategia-competitiva/Fuentes-de-ventaja/costos-de-cambio.md` |
| TCO de compras (Ellram, Hurkens y otros); hueco declarado sobre cuánto pesan los costos antes y después de comprar; TCO de tecnología popularizado por Gartner en 1987 (de Wikipedia) | `Compras-y-abastecimiento/Abastecimiento-estrategico/costo-total-de-adquisicion.md` |
| Módulos típicos; cuatro etiquetas (facturador, contable, gestión, ERP); instalado frente a nube; los de nube escalan precio por comprobantes, usuarios y cuentas de canal; precios de varios sistemas a 2026-11-22; Tango «licencia por módulos y puestos, vendida por centros de servicio» (D5, sin precio) | `Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion-en-el-comercio/` (tres notas) |

**Propio de este tema:**

1. El mantenimiento anual como porcentaje de la licencia, y por qué vuelve al proveedor de ERP un negocio recurrente aun antes de la nube.
2. La mezcla de ingresos de los grandes proveedores con cifras de informes anuales, y el margen de cada línea (licencia, soporte, nube, servicios).
3. La unidad de cobro en ERP (usuario nombrado o concurrente, módulo, empresa, comprobante) como decisión de diseño.
4. El canal de partners y su reparto, en ERP específicamente.
5. El costo de cambio visto desde la economía del soporte.
6. Dónde entra un software nuevo en esta categoría.
7. Mercado argentino: estructura del canal y tamaño.

**Sobre el árbol.** La división en siete notas coincide con cómo el campo parte el mercado, con dos observaciones. (a) «Licencia y suscripción» y «economía del proveedor» se pisan: el mantenimiento es precio para el cliente y línea de ingresos para el proveedor; conviene que la primera hable del precio y la segunda, de la mezcla. (b) «Ecosistema de extensiones» casi no tiene literatura propia de ERP; vive en la de plataformas (ya escrita), así que la nota debería ser corta y enlazar.

---

## 1. Licencia perpetua más mantenimiento frente a suscripción

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Forrester, blog «Software Maintenance Fees May Not Be Invulnerable To Change After All» (2010-06-29) | Secundaria, analista | [S] | 2/1/1/2 | https://go.forrester.com/blogs/10-06-29-software_maintenance_fees_may_not_be_invulnerable_to_change_after_all/ (el fetch dio 404: la cita viene del buscador y hay que verificarla) |
| Avasant, «High Software Maintenance Fees and What To Do About Them» | Secundaria, consultora de abastecimiento | [S] | 2/2/1/2 | https://avasant.com/report/high-software-maintenance-fees-and-what-to-do-about-them/ |
| CIO.com, «SAP raises software maintenance fees for new customers» | Secundaria, prensa | [S] | 2/1/2/2 | https://www.cio.com/article/276860/enterprise-resource-planning-sap-raises-software-maintenance-fees-for-new-customers.html |
| Rimini Street, «Are Hidden ERP Costs Burying Your IT Department?» | Secundaria con interés (vende soporte de terceros) | [S] | 1/1/1/1 | https://www.riministreet.com/blog/are-hidden-erp-costs-burying-your-it-department/ |
| TechTarget, cómo calcular el TCO de un ERP | Secundaria, prensa técnica | [S] | 2/1/2/1 | https://www.techtarget.com/enterprise-software/tip/How-to-calculate-the-total-cost-of-ownership-of-ERP-software |
| Kinnunen y Kinnunen (ICSIM 2025), «Subscription vs. Perpetual: Analysis of Cloud ERP and Traditional ERP Operational Impact on IS Life Cycle Costs» | Primaria, estudio de cuatro casos | [S] | 2/2/2/3 | https://jyx.jyu.fi/jyx/Record/jyx_123456789_104922 |
| Oracle, Form 10-K FY2025 | Primaria | [S] | 3/3/2/2 | https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm |

**Afirmaciones**

- El mantenimiento anual típico de los grandes proveedores es 18 % a 22 % del precio de licencia inicial: lo dicen Forrester, Rimini Street y un glosario de benchmarking (https://vendorbenchmark.com/glossary/software-maintenance-support-fees). Las fuentes discrepan: CIO.com da 20-25 % del precio neto; InformationWeek, 17-22 % (https://www.informationweek.com/software/software-maintenance-fees-time-for-this-model-to-change/d/d-id/1075860); TechTarget, 15-22 % del precio de lista en instalados; Avasant dice que antes se medía en 15-18 % y hoy se cotiza 20 % o más. [S]
- Por proveedor, según un resumen sin fuente primaria: soporte estándar de SAP 19 % (era 18 % y subió para contratos nuevos, según CIO.com), soporte «enterprise» de SAP 22 %, Oracle 22 %, IBM 20-25 %, Microsoft Software Assurance 25-29 %. [S] Es dato de dinero con una sola familia de fuentes, todas de consultoras o prensa con interés: declararlo en la nota como indicativo y buscar la política publicada de cada proveedor.
- Oracle FY2025 (año al 2025-05-31): soporte de licencias USD 19.523 millones, plano frente a USD 19.609 millones; nube USD 24.506 millones (+24 %). La 10-K espera que «substantially all» los clientes renueven el soporte y no da tasa. [S]
- TCO nube frente a instalado: Nucleus Research, en una guía patrocinada por Oracle, dice que el instalado cuesta 2,1 veces más (https://nucleusresearch.com/?p=25665); Hurwitz, citado por un proveedor, 50 % menos con nube para 100 empleados a cuatro años. Las dos son de parte. Lo único con método es Kinnunen y Kinnunen (cuatro empresas grandes que pasaron a SaaS), que advierte que el TCO de la nube es difícil de calcular. [S]
- Gartner, en un abstract de julio de 2026, dice que la nube desplaza el foco del costo total de propiedad al «costo total de operación», porque el gasto se vuelve continuo (https://www.gartner.com/en/documents/8624133; el buscador no precisó cuál de los abstracts, verificar el número). [S]

**Unidades de cobro.** No hay fuente con método que compare usuario nombrado, concurrente, módulo, empresa, comprobante e ingresos. En el repo solo está el precio por comprobante, usuarios y canales de los sistemas de nube argentinos y la discusión de Bain/BCG sobre asiento frente a uso. **Hueco.** Para la nota habría que leer la documentación de licenciamiento de un proveedor grande, solo como evidencia de que la práctica existe.

**Recurso canónico.** La nota de ingresos por línea del 20-F de SAP o de la 10-K de Oracle: muestra el soporte separado de la licencia y su peso. Complementar con Kinnunen y Kinnunen para la comparación de costos. Fijarse en la proporción de soporte frente a licencia nueva, no en el porcentaje de lista.

---

## 2. Economía del proveedor

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| SAP SE, Form 20-F FY2024 | Primaria | [S] | 3/3/2/2 | https://www.sec.gov/Archives/edgar/data/1000184/000110465925017815/sap-20241224x20f.htm |
| SAP, Integrated Report 2024, datos financieros | Primaria | [S] | 3/3/2/2 | https://www.sap.com/integrated-reports/2024/en/datahub/financial-data.html |
| SAP, presentación Q4 2024 | Primaria | [S] | 3/2/2/2 | https://irpages2.eqs.com/download/companies/sap/Presentations/SAP_Presentation_Q4_2024.pdf |
| Oracle, Form 10-K FY2025 | Primaria | [S] | 3/3/2/2 | (ver arriba) |
| Suarez, Cusumano y Kahl (2013), Management Science 59(2): 420-435 | Primaria académica, 1990-2006, SIC 7372 | [S] (abstract por buscador) | 3/3/2/3 | https://dspace.mit.edu/handle/1721.1/87623 ; texto abierto: https://dspace.mit.edu/bitstream/handle/1721.1/87623/Cusumano__Services%20and.pdf?sequence=1 |

**SAP FY2024, millones de euros [S]**

- Ingresos totales 34.176 (31.207 en 2023, +10 %).
- Nube 17.141 (13.664, +25 %). Margen bruto de la nube 72,8 % IFRS y 73,3 % no IFRS; costo de la nube 4.660.
- Licencias y soporte 12.689 (13.261, −4 %): licencias 1.399, soporte 11.290. Margen bruto combinado 90,1 % no IFRS; costo 1.262.
- Servicios 4.346 (4.283, +1 %), 13 % del total; costo 3.321, ganancia bruta 1.025, margen 23,6 % (el cociente 1.025/4.346 da 23,6 %: cuadra).
- «Ingreso más predecible» según SAP (nube más soporte): 28.431, 83 % del total.
- Lectura de esta base (cálculo): el soporte pesa unas ocho veces las licencias nuevas; el negocio es la base instalada que paga cada año.

**Oracle FY2025 [S]:** nube y soporte USD 44.029 millones (+12 %); margen del segmento 63 % (64 % antes), que es de segmento y no bruto: no usarlo como margen del soporte; licencias aparte USD 5,2 mil millones (+2 %).

**Servicios frente a software.** Ya están Salesforce (−10,3 %) y Suarez y otros en `saas.md`. Aporte propio: en SAP los servicios dan margen bruto positivo de 23,6 %, no negativo. Las definiciones de línea difieren entre proveedores y no se pueden comparar sin leer las notas contables. Suarez y otros: las empresas casi solo de producto son las más rentables y sumar servicios baja el margen operativo hasta que son la mayoría de las ventas; falta leer el umbral en el texto abierto. [S]

**Retención y costos de cambio.** Ningún proveedor de ERP publica una tasa de renovación en lo que se vio (Oracle solo expresa expectativa). La teoría está en `costos-de-cambio.md`; falta evidencia empírica de costos de cambio en ERP. **Hueco.**

**Recurso canónico.** La nota de segmentos del 20-F de SAP (ingresos y costo por línea) y su definición de «ingreso más predecible». Fijarse en el costo por línea para derivar márgenes y recordar que es un proveedor grande con base instalada: el patrón no se traslada sin más a uno chico.

---

## 3. Canal de partners

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Comunidad Dynamics (msdynamicsworld), artículo sobre descuentos de partner | Secundaria comunitaria | [S] | 1/1/2/2 | https://msdynamicsworld.com/node/27417 |
| Computerworld, «NetSuite courts old-school VARs with new offer» (año no confirmado) | Secundaria, prensa | [S] | 2/1/2/2 | https://www.computerworld.com/article/1440455/netsuite-courts-old-school-vars-with-new-offer.html |
| sysgenpro, márgenes de reseller de ERP | Secundaria de baja autoridad (sitio de contenido) | [S] | 1/1/1/1 | https://sysgenpro.com/resources/erp-reseller-margins-what-can-you-earn |
| IDC vía comunicados de Salesforce, «Salesforce Economy» | Secundaria, encargada por el proveedor | [S] | 2/2/2/2 | https://www.salesforce.com/news/press-releases/2021/09/20/idc-salesforce-economy-2021/ |

**Afirmaciones**

- Descuento tradicional de partner sobre lista en software instalado de empresa: 40 %, que cubre ventas, marketing y gastos generales y deja poco margen; descuento preaprobado de alrededor de 10 % sin aprobación. [S] (comunidad Dynamics)
- Un programa de NetSuite de la época daba al revendedor 50 % el primer año y 30 % después, y una oferta aparte 100 % del valor el primer año y 10 % después. [S] Fecha sin confirmar: evidencia de que el reparto con recurrencia existe, no de su valor actual.
- Blogs de baja autoridad: reventa 20-50 % y referido 10-20 %, o 15-40 % de participación recurrente. [S] No usar como cifra; muestran que no hay estándar.
- IDC por encargo de Salesforce: por cada dólar del proveedor, el ecosistema gana USD 3,67 en 2017, proyectado a 5,18 en 2022; 5,80 en 2024 (estudio de 2019); 6,19 en 2026 (estudio de 2021). Son proyecciones pagadas por el proveedor, y el ecosistema incluye empresas que no son partners formales. [S]
- **Alto riesgo (dinero):** el reparto del partner tiene una sola fuente con algo de peso, vieja y comunitaria. Decirlo en la nota.

**Recurso canónico.** No hay uno bueno. Candidato a verificar: los términos públicos de un programa de partners de un proveedor grande (descuento por nivel, recurrencia, requisitos). **Hueco:** qué parte del ingreso de un implantador es reventa y cuál servicios.

---

## 4. Ecosistema de extensiones

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Microsoft, blog «Drive growth with the most partner-focused business platform» (2021-07) | Primaria | [S] | 3/1/1/2 | https://azure.microsoft.com/en-us/blog/drive-growth-with-the-most-partnerfocused-business-platform/ |
| ITPro, «Microsoft lowers marketplace transaction fee from 20% to 3%» | Secundaria, prensa | [S] | 2/1/1/1 | https://www.itpro.com/uk/cloud/platform-as-a-service-paas/360220/microsoft-lowers-marketplace-transaction-fee-to-3 |

**Afirmaciones**

- Desde 2021-07-01 Microsoft bajó la comisión de su mercado comercial (incluye la tienda de aplicaciones de empresa) de 20 % a 3 % para ofertas transaccionables. La prensa repite el comunicado: cuenta como una sola fuente. [S] Complementa el 15 % ya citado en `ecosistema-de-terceros.md`, que es de una plataforma de tiendas.
- Reparto en la tienda de otro proveedor de ERP: no se encontró. Requisitos de certificación: no se leyeron. **Huecos.**
- Propio de este tema (inferencia de esta base, sin fuente): una extensión de ERP toca el mismo registro que lleva la contabilidad, así que una mala extensión cuesta integridad de datos, no solo calidad. Puente a `Columnas-tecnicas/configurar-o-personalizar.md`.

**Recurso canónico.** Ya está en el repo (Ghazawneh y Henfridsson; Parker y Van Alstyne en `ecosistema-de-terceros.md`). La nota de ERP debería citar la comisión de Microsoft como segundo dato y declarar el resto como hueco.

---

## 5. Costo total para quien compra

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Panorama Consulting, «2024 ERP Report» | Secundaria, consultora que vende selección e implantación | [S] | 1/2/2/2 | https://www.panorama-consulting.com/resource-center/erp-report/ ; PDF: https://qt9software.com/hubfs/2024-erp-report-panorama-consulting-group.pdf |
| TechTarget, costos ocultos de implantaciones de ERP | Secundaria | [S] | 2/1/2/1 | https://www.techtarget.com/enterprise-software/feature/Explaining-the-hidden-costs-of-ERP-implementations |
| Computerworld, «The art of ERP done right» (año sin confirmar) | Secundaria, prensa | [S] | 2/1/2/1 | https://www.computerworld.com/article/1724318/the-art-of-erp-done-right.html |
| Gartner, abstracts sobre costo de implantación de ERP | Primaria analista, tras muro | [S] | 3/1/1/2 | https://www.gartner.com/en/documents/8088565 |
| Nucleus Research, guía patrocinada por Oracle | Secundaria con interés | [S] | 1/1/1/1 | https://nucleusresearch.com/?p=25665 |

**Afirmaciones**

- Panorama 2024, según un resumen: costo mediano del proyecto USD 450.000 (USD 625.000 en 2023); 33 % se pasó de presupuesto, 5,3 % «significativamente»; 51 % atribuye el sobrecosto a requisitos técnicos adicionales y 39 % a subestimar el trabajo (el resumen salió cortado). [S]
- Panorama dice que el proveedor estima la implantación técnica en 1:1 respecto de la licencia y que es «woefully low». Es opinión de una consultora. Una cifra antigua que se le atribuye (USD 2,8 millones, 4,6 % de los ingresos anuales) es de hacia 2014 y no se verificó. [S]
- TechTarget: la implantación puede superar a la licencia por un factor de dos a tres «en algunos casos». [S]
- Computerworld, sin atribución clara a Gartner: 25 % software, 40 % servicios profesionales, 25 % personal interno. No citar como Gartner. [S]
- No se halló un estudio de Gartner abierto con la proporción. Las tres cifras discrepan (1:1, 1:2 a 1:3, 25/40/25) y son de parte; se dan las tres. Confirma el hueco que ya declara `costo-total-de-adquisicion.md`.
- Propio de este tema: el TCO del ERP agrega la personalización y su costo al actualizar, y el costo interno del equipo del cliente. La base general (Ellram, Hurkens) ya está en la nota de compras.

**Recurso canónico.** El «2024 ERP Report» de Panorama, leído como encuesta de una consultora (sesgo de muestra y de interés), para sobrecosto y duración. Fijarse en cómo define «costo de proyecto» (¿incluye costo interno?): no se pudo ver.

---

## 6. Dónde entra un software nuevo

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Christensen, Raynor y McDonald (2015), «What Is Disruptive Innovation?», HBR | Primaria teórica | [S] | 3/2/2/3 | https://hbr.org/2015/12/what-is-disruptive-innovation (no se abrió; URL por conocimiento, no verificada) |
| Christensen y Raynor, *The Innovator's Solution* (2003) | Primaria teórica, libro | [S] | 3/3/3/3 | sin URL verificada |
| Stripe y Tidemark, Vertical SaaS Benchmark 2025 | Secundaria con interés (Stripe vende pagos) | [S] | 1/2/2/2 | https://stripe.com/lp/tidemark-vertical-saas-benchmark-report |
| Rainforest, Vertical SaaS Embedded Payments Benchmarking Study 2026 | Secundaria con interés (vende pagos) | [S] | 1/2/2/1 | https://www.rainforestpay.com/blog/2026-vertical-saas-embedded-payments-benchmarking-study |

**Afirmaciones**

- Christensen, Raynor y McDonald: la disrupción empieza en dos terrenos que los incumbentes descuidan: la gama baja (porque dan más de lo que el cliente usa) y el mercado nuevo (donde no había nada). Los incumbentes «ignore the attackers» ante un mercado nuevo y «flee the attack» ante la gama baja. En 2015 la unidad de análisis es el modelo de negocio que habilita la tecnología. [S]
- **Aplicación al ERP (inferencia de esta base; ninguna fuente lo dice):** un facturador o sistema de nube de pyme encaja como gama baja frente a un ERP de mediana; un software para un rubro sin cobertura, como mercado nuevo. Decir en la nota que es una lectura.
- No hay estudio con método que pruebe que el SaaS vertical le gane al ERP horizontal. Hay informes de vendors de pagos: Stripe y Tidemark (más de 200 empresas de SaaS vertical) y Rainforest (primer estudio de pagos embebidos en SaaS vertical, campo en el primer trimestre de 2026). Ya está en `modelos-de-negocio-de-software.md` el dato de pagos como 81,9 % del ingreso de un software de restaurantes. [S]
- Entrada por un módulo que se integra, por un escalón chico y la localización como barrera: **hueco de fuente** específica de software de gestión. La barrera por costos de cambio ya está en `costos-de-cambio.md`.

**Recurso canónico.** HBR 2015, partes sobre los dos tipos de entrada; fijarse en que la teoría exige que el entrante mejore hasta alcanzar al mercado principal, cosa que no todo software barato hace. Como evidencia, el 20-F de SAP: licencias −4 % y nube +25 % muestran cuánto de la entrada nueva ocurre dentro del propio incumbente.

---

## 7. Mercado en Argentina

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| CESSI, Observatorio OPSSI, informe 2024 | Primaria, cámara sectorial | [S] por prensa; el PDF no se abrió | 3/2/1/3 | https://cessi.org.ar/ ; Memoria 2025: https://cessi.org.ar/wp-content/uploads/2025/10/Memoria-2025.pdf |
| Secretaría de Economía del Conocimiento, «Software y servicios informáticos 2024» | Primaria oficial | [S] | 3/2/1/2 | https://argentina.gob.ar/sites/default/files/software_y_servicios_informaticos_2024.pdf |
| ITSitio, «El software argentino bate récords» | Secundaria, prensa | [S] | 1/1/1/1 | https://www.itsitio.com/ar/software/software-argentino-bate-records/ |
| Ámbito (2026-07-29), caída del empleo del sector | Secundaria, prensa | [S] | 1/1/1/1 | https://www.ambito.com/tecnologia/la-industria-del-software-argentino-vuelve-tener-exportaciones-record-pero-el-empleo-cae-primera-vez-seis-anos-n6304732 |
| Axoft, formularios ante el Consejo Profesional de Ciencias Económicas | Primaria del proveedor, con interés | [S] | 1/1/2/2 | https://www.consejo.org.ar/storage/attachments/FORMULARIO AXOFT.pdf-IjbL7u00lN.pdf |
| ITSitio, «Un tango entre la tierra y la nube» (fecha sin confirmar) | Secundaria | [S] | 1/1/2/2 | https://www.itsitio.com/?p=2899 |
| Odoo, localización argentina (solo como evidencia de práctica) | Primaria, documentación | [S] | 2/1/2/1 | https://www.odoo.com/es/app/localization-argentina |
| FACPCE, guía de aplicación del ajuste por inflación (RT 6 y NIC 29) | Primaria, norma profesional | [S] | 3/2/2/2 | https://www.facpce.org.ar/web2014/pdf/Guia de aplicación de las normas contables sobre ajuste por inflación (RT 6 y NIC 29) - Primera parte.pdf |

**Afirmaciones**

- Tamaño del sector de software y servicios (no de ERP), según CESSI vía prensa: facturación USD 22.221 millones en 2024, +13,1 %; 158.179 puestos; 6.131 puestos nuevos en 2024; rotación 20 %. Exportaciones USD 2.810 millones en 2024 (UADE, https://www.uade.edu.ar/media/iy2ohbz0/exportaciones-de-software-en-la-repu-blica-argentina.pdf). [S] Discrepancia: Ámbito (2026-07) da 162.391 empleados y una caída del empleo, la primera en seis años; no se resolvió qué período mide cada cifra. **No se encontró dato público del tamaño del mercado local de ERP ni de su reparto entre nube e instalado.**
- Canal: Axoft declara más de 200 distribuidores y agentes con presencia en el país y más de 200.000 pymes que gestionaron su negocio con su solución. Un artículo viejo da unos 70.000 clientes históricos, 13.000 que actualizan cada año y unos 2.500 en su portal de nube de entonces. Discrepan en un orden de magnitud y no dicen qué cuentan: desconfiar. [S] Un post de LinkedIn dice que Axoft fue adquirida por una subsidiaria de Constellation Software: sin verificar, no usar.
- Ya está en el repo: Tango vendido por módulos y puestos a través de centros de servicio (D5) y los precios por comprobante, usuarios y canales de los de nube.
- Localización: la documentación de Odoo muestra qué entra en una localización argentina: facturación electrónica ante AFIP con certificación y firma, tipos de comprobante (A, N, factura de crédito electrónica MiPyME), plan de cuentas según responsabilidad fiscal, libros de IVA de ventas y compras. Evidencia de que un proveedor extranjero tiene que construirla o comprarla. [S]
- Ajuste por inflación: la guía de la FACPCE describe el método indirecto de la RT 6 con proceso secuencial, y el Consejo publica índices periódicos (había índices a junio de 2026): un sistema tiene que reexpresar y cargar coeficientes. [S]
- **La localización como barrera de entrada para extranjeros es inferencia de esta base:** no se encontró fuente que la mida ni que compare cuotas de proveedores locales y extranjeros. Lo fiscal en sí va a `software-de-gestion-en-argentina.md` e Impuestos; aquí solo la consecuencia económica (costo de mantener la localización al día).

**Recurso canónico.** El informe OPSSI de CESSI (PDF) para el tamaño del sector; no responde por ERP. Para el canal no hay recurso: serían los sitios de los proveedores o entrevistas. Fijarse en si cambió la definición de «sector» entre ediciones.

---

## 8. Huecos

1. Tasa de renovación del soporte de ERP: ningún proveedor la publica en lo visto.
2. Tarifa de mantenimiento: ninguna fuente primaria; todo de consultoras y prensa con interés (Rimini Street vende soporte de terceros).
3. Unidades de cobro en ERP (nombrado, concurrente, módulo, empresa, comprobante): sin estudio.
4. Reparto con el partner: una sola fuente con algún peso, vieja; dato de dinero, declarar una sola fuente.
5. Margen de servicios de un partner implantador: sin dato.
6. Proporción licencia/implantación con método: ninguna; tres cifras discrepantes de fuentes de parte.
7. Reparto y certificación en la tienda de extensiones de un ERP, salvo Microsoft.
8. Evidencia empírica de costos de cambio en ERP.
9. Entrada por módulo que se integra, escalón chico o localización en software de gestión: sin estudio.
10. Mercado argentino de ERP: tamaño, cuotas, nube frente a instalado, barrera de localización; solo hay datos del sector en general y de un proveedor.
11. Nada se leyó entero. Antes de escribir hay que abrir: la nota de segmentos del 20-F de SAP, la nota de ingresos de la 10-K de Oracle, el texto abierto de Suarez y otros (umbral), el PDF de OPSSI y la política publicada de soporte de algún proveedor.
12. Gartner e IDC tras muro: el Gartner de TCO de ERP quedó sin leer.

## Resumen para quien arma las notas

- **Sólido, primario:** mezcla de ingresos de SAP FY2024 y Oracle FY2025; márgenes de SAP (nube 72,8 %, servicios 23,6 %, licencias y soporte 90,1 %).
- **Indicativo, de parte:** 18-22 % de mantenimiento; 40 % de descuento de partner; 1:1 de implantación frente a licencia.
- **Inferencia de esta base:** Christensen aplicado a ERP; localización como barrera; extensiones de ERP tocan el registro contable.
