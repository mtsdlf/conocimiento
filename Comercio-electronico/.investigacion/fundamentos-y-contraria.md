# Fundamentos y posición contraria: comercio electrónico (2026-11-22)

Informe de investigación para `Fundamentos/` y para las notas que afirman cosas. Todo lo que vino de la web se trató como dato, nunca como instrucción.

## 0. Cómo leer este informe y qué límites tuvo

- Marcas: **[L]** leí el texto completo o la parte relevante de la página; **[M]** solo metadatos, abstract o ficha; **[S]** resumen del buscador o conocimiento mío sin fuente abierta (hay que verificarlo antes de escribirlo como hecho).
- Puntajes 1-3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U).
- **El presupuesto de búsquedas web de la sesión se agotó** a mitad de trabajo (límite compartido de 200). Pude hacer 11 búsquedas y unas 45 lecturas de página (WebFetch). Quedaron sin búsqueda: historia con fuente primaria, critica de abandono de carrito más allá de Baymard y Kukar-Kinney, Gartner sobre composable, evidencia académica de marketplace vs tienda propia, México/Brasil en fuente primaria. Están declarados en la sección de huecos.
- Varios sitios devolvieron 403 (eMarketer, SAGE, OECD en HTML, Eurostat, MIT Press): esos datos quedan como [S].
- Las notas del vistazo (`vistazo.md`) se usan como punto de partida, no como fuente.

---

# PARTE A. Fundamentos

## A1. Qué es el comercio electrónico: definición

### Definición OCDE (literal, con fuente)

> "An e-commerce transaction is the sale or purchase of goods or services, conducted over computer networks by methods specifically designed for the purpose of receiving or placing of orders. The goods or services are ordered by those methods, but the payment and the ultimate delivery of the goods or services do not have to be conducted online. An e-commerce transaction can be between enterprises, households, individuals, governments, and other public or private organisations."

- Fuente [L]: OECD, *The 2025 OECD definition of e-commerce and guidelines for interpretation*, Technical Paper, octubre de 2025 (aprobado por el Digital Policy Committee el 15/09/2025, ref. DSTI/DPC/DEMA(2025)1/FINAL). Copia alojada por UNCTAD: https://unctad.org/system/files/information-document/2025oecddefinitionofecommerce_guidelinesforinterpretation.pdf
- **El texto de la definición es idéntico en 2009 y en 2025** (tabla 2.1 y tabla 4.1 del mismo documento). Lo que cambió en 2025 son las *guías de interpretación*:
  - 2009: incluye pedidos hechos en "webpages, extranet or EDI"; excluye teléfono, fax y correo electrónico tipeado a mano.
  - 2025: incluye pedidos por "webpages, apps, extranets, and Electronic Data Interchange (EDI)"; excluye teléfono, fax, "on-premise mechanisms (including but not limited to kiosks or QR codes)" y mensajes tipeados a mano.
  - 2025 aclara que las ventas en redes sociales y mensajería entran **solo si el pedido se hace con un método diseñado para eso** (catálogos estructurados dentro de la app, como WhatsApp Carts o TikTok Shop); si la app solo redirige a una web, cuenta la web. También menciona pedidos asistidos por IA y compras digitales automatizadas.
- El tipo de transacción se define **por el método de hacer el pedido**, no por el pago ni la entrega. Esto importa para la base: una venta por WhatsApp con mensaje tipeado a mano **no es** comercio electrónico para la OCDE; una compra online retirada en tienda **sí**.
- Hitos de la propia definición [L]: primera definición estadística en 2001, revisada en 2009, revisada en 2025.
- Intermediarios [L, mismo documento, sección 4.3.1]: las plataformas de intermediación digital (Amazon Marketplace, eBay, Airbnb) "enable third-party transactions without taking ownership of the goods or services involved for a fee", y el desafío de medición es el doble conteo; el documento recomienda medir "only the intermediation fees charged by the platform, rather than the total transaction value" y, dentro del comercio web, distinguir los pedidos hechos en plataformas que intermedian por una comisión.

### Otras definiciones (para mostrar que no hay una sola)

| Fuente | Definición | Marca |
|---|---|---|
| INSEE (Francia) https://www.insee.fr/en/metadonnees/definition/c1769 | "Sales transactions using the Internet or other IT networks such as the exchange of computerised data"; excluye pedidos por teléfono, fax o mail y las operaciones bancarias. La página no atribuye la definición a la OCDE. | [L] |
| Eurostat, Statistics Canada, OMC (vía resumen del buscador) | Eurostat: ventas por internet u otras redes mediadas por computadora; Statistics Canada: solo pedidos recibidos y comprometidos por Internet, extranets o EDI; OMC: mucho más amplia (producción, marketing y entrega por medios electrónicos). No abrí los textos. | [S] |

### UNCTAD

- UNCTAD no tiene una definición propia de uso general en lo que leí; mide con la de la OCDE más datos nacionales. Su nota de 2020 dice que la cifra B2B "incluye ventas en plataformas de mercado en línea e intercambio electrónico de datos (EDI)" https://unctad.org/news/global-E-commerce-hits-256-trillion-latest-unctad-estimates [L]. Cifras en A6.
- Advertencia para la nota: "comercio electrónico" en estadísticas oficiales puede incluir EDI B2B entre empresas grandes, y en estudios de cámaras (CACE, AMVO) suele ser solo venta a consumidores (ver A6).

### Qué dice el campo sobre la división del tema

La división del árbol (modelos, partes de vender online) coincide con Laudon y Traver (modelos de negocio, infraestructura, marketing, retail y B2B). El campo estadístico (OCDE) divide por **método de pedido** y por **participantes** (empresas, hogares, individuos, gobiernos), no por "modelo de negocio". La nota raíz debería decir que hay dos ejes ortogonales: quién vende a quién (B2C, B2B...) y por dónde se hace el pedido (web propia, app, marketplace, red social, EDI).

---

## A2. Modelos de comercio electrónico

No pude abrir los manuales (Laudon y Traver, Chaffey): las definiciones que siguen son las convencionales del campo, marcadas **[S]**, y hay que contrastarlas con el capítulo 1 de Laudon y Traver antes de publicar. Lo verificado:

- La OCDE reconoce transacciones entre empresas, hogares, individuos, gobiernos y otras organizaciones [L, ver A1], que es la base de B2B, B2C, C2C, B2G.
- Wikipedia (secundaria) lista B2B, B2C y C2C citando a Cambridge Dictionary y a Simjanović et al. (2022), y define D2C como fabricantes o marcas que venden "directly to end customers without traditional retail intermediaries" (sin cita en el texto) https://en.wikipedia.org/wiki/E-commerce [M].

| Modelo | Definición propuesta [S] | Ejemplo | Nota para la base |
|---|---|---|---|
| B2C | Una empresa vende a consumidores finales. | Tienda online de una marca de ropa | El que más se mide en cámaras. |
| B2B | Una empresa vende a otras empresas. | Distribuidor que recibe pedidos de comercios | UNCTAD: 83% del e-commerce global de 2018 (A6). Incluye EDI. |
| C2C | Personas venden a personas, mediadas por una plataforma. | Publicaciones de usuarios en un marketplace | Hay que separar de "marketplace" (ver abajo). |
| D2C | Una marca que fabrica vende directo, sin retail intermedio. | Marca propia sobre Shopify o Tiendanube | Es un *canal* de vender, no un tipo de cliente: una D2C es B2C. |
| Marketplace | Una plataforma intermedia entre muchos vendedores y compradores; cobra comisión y a veces logística y publicidad. | Mercado Libre, Amazon (parte de terceros) | La OCDE los llama *digital intermediation platforms*. |
| Social commerce | Pedido hecho dentro de una red social o app de mensajería. | WhatsApp Carts, TikTok Shop | Para la OCDE cuenta solo con catálogo estructurado; el mensaje tipeado no es e-commerce. |

Lo que Laudon y Traver agregan a esta lista (m-commerce, social, local) [S] no lo pude verificar; la ficha de Pearson no trae la tabla de contenidos completa (ver A4).

Headless/composable **no es un modelo de comercio** sino una arquitectura de plataforma; va en `Plataforma-de-tiendas/tipos-de-plataforma`, no en esta lista.

---

## A3. Historia breve (hitos fechados)

Todo con fuente secundaria (Wikipedia, que cita fuentes; autoridad 1-2). **Verificar con primarias antes de afirmar.** Marcas **[M]**.

| Año | Hito | Fuente |
|---|---|---|
| 1948 | El puente aéreo de Berlín obliga a intercambiar grandes volúmenes de datos de carga; inspiración militar del EDI. Los primeros estándares TDCC de EE. UU. vienen después (sin fecha en la página). | https://en.wikipedia.org/wiki/Electronic_data_interchange [M] |
| Década de 1960 | Procesamiento de transacciones en línea de IBM (SABRE, American Airlines) como forma temprana de comercio online. | https://en.wikipedia.org/wiki/History_of_online_shopping [M] |
| 1971 | LACES en Heathrow: agentes cargan datos directo en el sistema de aduanas. | EDI, ídem [M] |
| 1979 | Michael Aldrich conecta un televisor modificado a una computadora de transacciones por línea telefónica. | History_of_online_shopping [M] |
| 1982 | Minitel se despliega en toda Francia y se usa para pedidos. | https://en.wikipedia.org/wiki/E-commerce [M] |
| 1984 | CompuServe lanza su Electronic Mall; Gateshead SIS/Tesco, primer sistema B2C de compra online. | E-commerce [M] |
| 1989-1991 | Berners-Lee crea el primer servidor y navegador web; la web abre al uso comercial en 1991. | History_of_online_shopping [M] |
| 1994 | Netscape 1.0 con SSL; Pizza Hut vende online; primera transacción minorista segura en la web (NetMarket). | E-commerce y History_of_online_shopping [M] |
| 1995 | Lanzan Amazon y eBay (como AuctionWeb). | E-commerce [M] |
| 1999 | Se funda Alibaba. | E-commerce [M] |
| 2002 | eBay compra PayPal por US$ 1.500 millones. | E-commerce [M] |
| 2003 / 2008 | Alibaba lanza Taobao y Tmall. | History_of_online_shopping [M] |
| 2004 | Snowdevil, la tienda de snowboards que originó Shopify. | https://en.wikipedia.org/wiki/Shopify [M] |
| junio 2006 | Se lanza Shopify (Liquid como lenguaje de plantillas). | Shopify [M] |
| junio 2009 | Shopify lanza API y App Store. | Shopify [M] |
| agosto 2013 | Shopify Payments, con Stripe. | Shopify [M] |
| 21 mayo 2015 | IPO de Shopify (más de US$ 131 millones). | Shopify [M] |
| abril 2017 | Shop Pay (antes Shopify Pay). | Shopify [M] |
| 2021 | Hydrogen y Oxygen: stack headless de Shopify. | Shopify [M] |
| 2025 | La OCDE reconoce explícitamente WhatsApp Carts y TikTok Shop como métodos de pedido. | OECD 2025 [L] |

Observaciones:
- La narrativa pedida ("de EDI a la web, a las plataformas SaaS, al móvil y lo social") tiene hitos para EDI (1948-1980s), web (1989-1995), SaaS (2006-2009) y plataforma de pagos propia (2013). **Hueco: comercio móvil** (iPhone 2007, apps de compra) no apareció en ninguna fuente que pude abrir; se podría fechar con el Census Bureau o con el 10-K de Amazon. Social/mensajería sí: OECD 2025.
- Wikipedia se contradice en Shopify: usa "2004" y "2006" como fundación. La nota debe decir "2004 (Snowdevil) y 2006 (Shopify)".
- Para Tiendanube/Nuvemshop y Mercado Libre (fechas de fundación) no tengo fuente abierta: [S], hueco.
- El EDI es anterior a la web y sigue vigente: es la razón por la que las cifras B2B de UNCTAD son tan grandes (A6).

---

## A4. Bibliografía por necesidad

| Necesidad | Recurso | Qué verifiqué | Marca |
|---|---|---|---|
| Panorama del dominio (negocio, tecnología, sociedad) | Laudon, K. y Traver, C., *E-commerce 2023-2024: business. technology. society.*, 18.ª ed., Global Edition, Pearson. | Pearson la fecha **2 de agosto de 2024 (© 2024)**; el ISBN de la edición impresa 9781292449722 trae "Published 2023". Hay que citar "18.ª ed., 2023/2024" y avisar la discrepancia. https://www.pearson.com/store/en-gb/p/e-commerce-2023-2024-business-technology-society-global-edition/P200000010016 | [M] |
| Gestión del negocio digital | Chaffey, D., Hemphill, T. y Edmundson-Bird, D., *Digital Business and E-commerce Management*, 8.ª ed., Pearson (ISBN 9781292457536 según la URL). | **No pude verificar edición, año ni índice** (la página de Pearson devolvió solo navegación). Vistazo dice que Pearson da 2024 y 2026. Hueco. | [S] |
| Economía de plataformas y pagos (teoría) | Rysman, M., "The Economics of Two-Sided Markets", *Journal of Economic Perspectives* 23(3), 2009, pp. 125-143, DOI 10.1257/jep.23.3.125. | https://www.aeaweb.org/articles?id=10.1257/jep.23.3.125. Ejemplos del artículo: consolas, tarjetas de pago, buscadores, medios con publicidad. Artículo corto, lectura inicial. | [L] (ficha y resumen) |
| Idem, fuente primaria del campo | Rochet, J.-C. y Tirole, J., "Platform Competition in Two-Sided Markets", *Journal of the European Economic Association*, 2003. | No verificado. | [S] |
| Plataformas, libros | Parker, Van Alstyne y Choudary, *Platform Revolution* (2016); Evans, Hagiu y Schmalensee, *Invisible Engines* (MIT Press; la primera edición es 2006, el vistazo decía 2008, probablemente la edición en rústica). | MIT Press y Wikipedia devolvieron 403/404. No verificado. | [S] |
| Checkout | Baymard Institute, método y benchmark de checkout (https://baymard.com/checkout-usability/methodology) | Ver A5. | [M] |
| En castellano | Laudon y Traver, *E-commerce: negocios, tecnología, sociedad*, Pearson: 4.ª ed., México, 2009 (ISBN 9786074420494 según una librería universitaria); *E-commerce 2013: negocios, tecnología, sociedad*, Pearson, c2014 (trad. Núñez Ramos y Enríquez Brito, según catálogo de biblioteca). | Registros de catálogos de bibliotecas (UNQ, CSUCA), no de la editorial. **No encontré traducción de la 18.ª edición**: la última en castellano es de 2014. | [S] |
| En castellano, mercado | Estudios de CACE (Argentina), AMVO (México), NuvemCommerce/NubeCommerce de Nuvemshop/Tiendanube. | Ver A5 y A6. El PDF de NuvemCommerce 2026 pesa más de 10 MB y no se pudo leer. | [M] |

Recurso canónico propuesto para el tema: Laudon y Traver (capítulos de modelos de negocio y de infraestructura), solo como referencia general y declarando la edición; para plataformas, Rysman 2009 como puerta a la literatura; para checkout, Baymard con las advertencias de A5 y B4. Libros de pagos: queda como hueco (candidatos: CPMI/BIS *Red Book* y documentos del BCRA y Banco Central do Brasil; ver `Pagos/`).

---

## A5. Fuentes del dominio, peso y conflicto de interés

| Fuente | Tipo | A | P | E | U | Conflicto de interés / límite | Marca |
|---|---|---|---|---|---|---|---|
| OCDE, definición 2025 (UNCTAD la aloja) | primaria, estándar estadístico | 3 | 3 | 2 | 3 | Ninguno relevante. Es una definición, no una cifra. | [L] |
| UNCTAD, estimaciones globales | primaria (organismo), estimaciones | 3 | 2 | 2 | 3 | Cubre pocas economías; dice que la estimación de comercio ordenado digitalmente es "relatively uncertain" (resumen del buscador). | [L]/[S] |
| US Census Bureau, e-commerce trimestral | primaria, estadística oficial | 3 | 2 | 1 | 3 | Solo EE. UU. | [L] |
| CACE (Argentina) | cámara, estudio anual con Kantar | 2 | 2 | 1 | 3 | Encuesta a unas 200 empresas socias; informe completo solo para socios; cobra por membresía. | [M] |
| AMVO (México) | asociación, estudio anual | 2 | 2 | 1 | 3 | Base de n = 1.048 compradores digitales en panel online (NetQuest/Bilendi); estimación propia. Fuente: nota de prensa especializada. | [M] |
| ABComm / ABIACOM (Brasil) | asociación | 2 | 1 | 1 | 3 | Metodología no descrita en las notas que leí; cambió de nombre. | [M] |
| eMarketer | estudio comercial | 2 | 2 | 1 | 2 | Pronósticos propios; paywall; 403 al abrir. | [S] |
| Baymard Institute | investigación de usabilidad + base de datos comercial | 3 en método, 2 en independencia | 3 | 3 | 3 | Vende la suscripción a sus guías; su promedio de abandono es media de 50 estudios de terceros, varios de proveedores. Ver B4. | [L] |
| Marketplace Pulse | consultora/medio de investigación de marketplaces | 2 | 2 | 2 | 3 | Muestra de P&L de vendedores sin tamaño publicado; Amazon discrepa (resumen del buscador). | [L] |
| Blogs de proveedores (Nuvemshop, VTEX, Fastr, Elogic, Growth Suite, Stripe, EBANX, dLocal) | secundarias, comerciales | 1 | 1-2 | 2 | 1 | Cada uno vende lo que recomienda o procesa pagos de las cuotas que elogia. | [L] |
| Wikipedia | terciaria | 1 | 2 | 2 | 1 | Útil para fechar; verificar en primarias. | [M] |

Regla propuesta para la base: toda cifra de cámara lleva "año de los datos", "quién la mide y con qué muestra" y, si es de un proveedor, la leyenda "afirmación de proveedor".

---

## A6. Cifras del mercado (ficha, fechada y literal)

Fecha de consulta: 2026-11-22.

### Mundo y EE. UU.

| Cifra | Año de los datos | Fuente | Marca |
|---|---|---|---|
| E-commerce global US$ 25,6 billones (trillion), +8% sobre 2017; B2B US$ 21 billones (83%, incluye plataformas y EDI); B2C US$ 4,4 billones, +16%; B2C transfronterizo US$ 404.000 millones | 2018 (publicado en abril de 2020; la fecha exacta no figura en la página, se infiere del contexto) | UNCTAD https://unctad.org/news/global-E-commerce-hits-256-trillion-latest-unctad-estimates. El texto aclara que "muchos países no publican estadísticas oficiales" y que la nueva metodología revisó 2017 a US$ 23,8 billones. | [L] |
| Retail e-commerce de siete países: US$ 2,9 billones; las 13 mayores empresas e-commerce al consumidor: US$ 3,9 billones de ventas brutas | 2021 (nota de abril de 2022, fecha inferida) | UNCTAD https://unctad.org/news/covid-19-boost-e-commerce-sustained-2021-new-unctad-figures-show. Los siete países suman "around half of global GDP". Sin total mundial. | [L] |
| "Casi US$ 27 billones" en 2022 (+10%) | 2022 | UNCTAD, nota técnica 2024 (https://unctad.org/publication/business-e-commerce-sales-and-role-online-platforms-advance-copy). Resumen del buscador: es e-commerce *empresarial* de un subconjunto de economías (43), no total mundial. | [S] |
| E-commerce minorista EE. UU.: US$ 347.300 millones desestacionalizados, 17,9% de las ventas minoristas totales (US$ 1,94 billones); sin ajustar US$ 335.700 millones, 17,2% | 3.er trimestre 2026 | US Census https://www.census.gov/retail/ecommerce.html | [L] |

**Lectura:** "comercio electrónico mundial" de UNCTAD (25,6 billones, 2018) y "retail e-commerce" (2,9 billones, siete países, 2021) no son comparables: el primero es B2B + B2C con EDI, el segundo solo minorista. Un error común es poner las dos en el mismo gráfico.

### América Latina

- eMarketer: ventas retail e-commerce de US$ 191,25 mil millones en 2025 (+12,2%); Argentina, Brasil y México suman 84,5% (dato del vistazo; **no pude abrir la página, 403**) https://www.emarketer.com/content/latin-america-ecommerce-forecast-2025 [S]. Es un *pronóstico*; otras coberturas hablan de US$ 215 mil millones sin base conocida (vistazo, no reverificado).
- Ebanx/PCMI: Pix 42% del e-commerce de Brasil en 2025, tarjetas 41%; otra nota da 44% contra 40% (vistazo, no verificado) https://ebanx.com/en/beyond-borders-2025/ [S].

### Argentina (CACE) y la discrepancia entre 34 y 35 billones de pesos

**No es un error de lectura: son dos publicaciones de CACE sobre el mismo año de datos (2025), con fechas y bases distintas.**

| | Adelanto | Estudio anual |
|---|---|---|
| Fecha | 5/02/2026 (nota del 6/02/2026) | 19/03/2026 |
| Facturación | $35.326.983 millones (35,33 billones) | $34.033.238 millones (34,03 billones) |
| Variación | +60% nominal | +55% |
| Otros datos | Inflación interanual 31% (según la nota, sin indicar índice); "alrededor de 200 empresas socias", con Kantar, encuesta | 253 millones de órdenes (+3%); ticket promedio $134.519 (+46%); 25,1 millones de compradores, 1.338.952 nuevos |
| Fuente | https://mercado.com.ar/tendencias/cace-el-ecommerce-facturo-35-326-983-millones-en-2025-y-subio-60 [L] | https://mercado.com.ar/tendencias/comercio-electronico-el-estudio-anual-de-cace-midio-34-033-238-millones-en-2025 [L] |

- Cómo resolverlo: el adelanto se llamó "resultados preliminares" y el estudio anual, que salió siete semanas después, es el definitivo; la base cita ambos, **la cifra vigente es 34.033.238 millones (+55%)**, y el adelanto queda como dato histórico. No encontré explicación oficial de la diferencia: la página de CACE (https://www.cace.org.ar/pages/biblioteca-de-estudios) solo ofrece el resumen para prensa y el informe completo "solo para socios", y no pude leerlos. La nota de la estudio anual no menciona el adelanto. Declarar "no se encontró explicación de la revisión".
- Chequeo aritmético mío: 253 millones de órdenes × $134.519 = $34,03 billones, o sea que la cifra final es coherente con órdenes por ticket.
- Otros datos con fecha: CACE MidTerm 2026: +28% de facturación frente al primer semestre de 2025 (página de CACE, solo el titular, [M]). El e-commerce "aún representa el 12% del total de transacciones minoristas" de Argentina (Cronista, 13/10/2025, firmado por Lola Loustalot, **sin fuente ni año del dato**) https://www.cronista.com/negocios/a-pesar-del-boom-de-shein-y-temu-el-comercio-electronico-solo-representa-el-12-de-las-compras [L]; no usar el 12% como cifra sin fuente.
- Advertencias de método: es facturación en pesos corrientes. Con inflación de 31% el crecimiento real queda en torno de +18% (1,55/1,31) o +22% (1,60/1,31), pero el 31% viene de una nota y no lo contrasté con INDEC. CACE mide empresas socias; el rubro más grande es "Pasajes y turismo" (resumen del buscador), así que incluye servicios y no es "retail" en el sentido de eMarketer.

### Brasil

| Cifra | Año de los datos | Fuente | Marca |
|---|---|---|---|
| R$ 204,3 mil millones, +10,5%; 414,9 millones de pedidos; ticket R$ 492,40; 91,3 millones de compradores | 2024 (publicado 14/01/2025) | ABComm, vía https://mercadoeconsumo.com.br/14/01/2025/ecommerce/e-commerce-brasileiro-cresce-105-e-fatura-r-2043-bilhoes-em-2024 | [L] (nota, sin metodología) |
| Proyección 2025: R$ 224,7 mil millones, luego R$ 234,9 mil millones | 2025 (proyección) | ABComm (resumen del buscador) | [S] |
| Resultado 2025: R$ 235,5 mil millones, +15,3% | 2025 | "ABIACOM" (nuevo nombre de ABComm, según resumen del buscador; no abrí la nota) | [S] |
| R$ 208,4 mil millones en el primer semestre de 2026, +16,9% | 1.er semestre 2026 | Confi, vía CNN Brasil (resumen del buscador) | [S] |

- Chequeo: 235,5 / 204,3 = +15,3%, consistente con lo publicado.
- Hueco: no encontré la serie de Ebit/Nielsen ni de Neotrust como primaria.

### México

| Cifra | Año de los datos | Fuente | Marca |
|---|---|---|---|
| E-commerce retail de $941 mil millones de pesos, +19,2% nominal (+13,6% en USD), 17,7% de las ventas minoristas, 77,2 millones de compradores digitales, 8.º lugar mundial; n = 1.048 compradores, panel NetQuest (Bilendi); pure players +23,7%, brick & click +14,9% | **datos de 2025**, estudio llamado "Estudio de Venta Online 2026", publicado el 11/03/2026 | AMVO, vía https://marketing4ecommerce.mx/estudio-de-venta-online-2026-amvo-mexico/ | [L] (nota especializada; no abrí el informe) |
| Crecimiento 2024: +20,0% (también 2021 +27,0%, 2022 +23,0%, 2023 +24,6%) | 2024 y anteriores | misma nota | [L] |

- Chequeo: 941 / 1,192 = 789 mil millones, coherente con "casi 790 mil millones" para 2024 que traía el vistazo. **El año del título del estudio es posterior al año de los datos**: citar siempre "datos 2025, estudio 2026".
- Otra cifra mexicana, de la plataforma Tiendanube: el comercio independiente (tiendas propias y D2C) creció 57% en facturación en el primer semestre de 2025, ticket $1.391 a $1.772 (+14%), compradores +45% (Expansión, 1/04/2026, https://expansion.mx/tecnologia/2026/04/01/ecommerce-fuera-marketplaces-crece-mexico-cambios-fiscales) [L]. Dato de un proveedor, con base de comparación no declarada.

---

## A7. Glosario (56 términos; definiciones propias, todas **[S]**)

Las definiciones son síntesis del campo; los términos subrayados con fuente están donde corresponde. Para la nota final hay que citar al menos una fuente por término de dinero (GMV, take rate, contracargo).

| Término | En inglés | Definición |
|---|---|---|
| Comercio electrónico | e-commerce | Venta o compra con pedido hecho por un método diseñado para eso (definición OCDE, A1). |
| Tienda online | online store / webstore | Sitio o app con catálogo, carrito y pago. |
| Plataforma de tiendas alojada | hosted platform / SaaS commerce | Software que el comercio alquila y que corre en la nube del proveedor. |
| Código abierto autoalojado | self-hosted open source | Software que el comercio instala y mantiene por su cuenta. |
| Marketplace | marketplace | Sitio donde muchos vendedores publican; la plataforma cobra comisión. |
| Headless | headless commerce | La vitrina se separa del motor de comercio y se comunica por API. |
| Composable | composable commerce | El comercio se arma con servicios independientes elegidos uno por uno. |
| MACH | MACH (microservices, API-first, cloud-native, headless) | Principios de arquitectura promovidos por la MACH Alliance. |
| Multi-tenant | multi-tenancy | Una instalación sirve a muchas tiendas con datos aislados. |
| Tema | theme | Diseño intercambiable de la vitrina. |
| Tienda de apps | app store | Catálogo de extensiones de terceros. |
| API | API | Interfaz para que otros sistemas lean y escriban datos. |
| Webhook | webhook | Aviso automático que un sistema envía a otro ante un evento. |
| SKU | SKU (stock keeping unit) | Código de una variante vendible. |
| Catálogo | catalog | Conjunto de productos y variantes. |
| Inventario | inventory | Existencias disponibles. |
| Pedido | order | Compra confirmada por un cliente. |
| Carrito | cart | Selección de productos antes de pagar. |
| Checkout | checkout | Los pasos de datos, envío y pago. |
| Embudo | funnel | Etapas del recorrido de visita a compra. |
| Tasa de conversión | conversion rate | Compras sobre visitas (o sesiones); la definición del denominador cambia entre fuentes (B3). |
| Abandono de carrito | cart abandonment | Carritos creados que no terminan en compra. |
| Ticket promedio | average order value (AOV) | Facturación dividida por pedidos. |
| GMV | gross merchandise value | Valor bruto de lo vendido en la plataforma, antes de devoluciones y comisiones. |
| Take rate | take rate | Porcentaje del GMV que se queda la plataforma. |
| MRR | monthly recurring revenue | Ingreso mensual recurrente por suscripciones. |
| ARPU | average revenue per user | Ingreso medio por cliente. |
| Churn | churn | Porcentaje de clientes que se dan de baja. |
| LTV | customer lifetime value | Valor esperado de un cliente a lo largo del tiempo. |
| CAC | customer acquisition cost | Costo de conseguir un cliente. |
| Pasarela de pagos | payment gateway | Servicio que transmite los datos del pago al procesador. |
| Adquirente | acquirer | Entidad que procesa los cobros de tarjeta para el comercio. |
| Procesador | processor | Empresa que ejecuta técnicamente la autorización. |
| Agregador de pagos | payment facilitator / aggregator | Cobra por muchos comercios bajo una sola cuenta (por ejemplo, billeteras de marketplace). |
| Emisor | issuer | Banco que emitió la tarjeta del comprador. |
| Red de tarjetas | card network / scheme | Visa, Mastercard y similares, que fijan reglas entre emisor y adquirente. |
| Autorización | authorization | Aprobación del emisor para un pago. |
| Liquidación / acreditación | settlement | Transferencia del dinero al comercio. |
| Conciliación | reconciliation | Cruce entre ventas, cobros y bancos. |
| Contracargo | chargeback | El titular desconoce un pago y el emisor revierte el cobro. |
| Fraude | fraud | Uso no autorizado del medio de pago. |
| 3-D Secure | 3-D Secure (3DS) | Autenticación extra del titular. |
| Tokenización | tokenization | Reemplazo del número de tarjeta por un token. |
| PCI DSS | PCI DSS | Estándar de seguridad para datos de tarjeta. |
| Cuotas | installments | Pago dividido en pagos mensuales. |
| Cuotas sin interés | interest-free installments | Cuotas con tasa 0% para el comprador; alguien financia el costo (B6). |
| CFT | total financial cost (CFT) | Costo financiero total de un crédito, con tasa y cargos. |
| Billetera virtual | digital wallet | App que guarda medios de pago. |
| Transferencia instantánea | instant payment | Transferencia inmediata entre cuentas (Pix, en Brasil). |
| BNPL | buy now pay later | Compra ahora, pago diferido. |
| Fulfillment | fulfillment | Preparar y despachar pedidos. |
| Última milla | last mile | Tramo final de la entrega al comprador. |
| Logística inversa | reverse logistics | Devoluciones. |
| Omnicanal | omnichannel | Canales de venta conectados con inventario y cliente compartidos (B5). |
| Multicanal | multichannel | Varios canales, sin integración necesaria. |
| D2C | direct-to-consumer (D2C / DTC) | Marca que vende directo sin retail. |
| Comercio social | social commerce | Compra dentro de redes o mensajería. |
| POS | point of sale | Punto de venta físico. |
| Botón de arrepentimiento | withdrawal button | Enlace para revocar la compra (Res. 424/2020, Argentina; la norma se trata en `Normativa/`). |

(56 filas.)

---

## A8. Recursos canónicos propuestos para `Fundamentos/`

1. **OECD 2025, definición y guías** (A1): leer sección 4.3 (intermediarios, redes sociales). Fijarse en que la definición no cambió desde 2009 y que cambió la interpretación.
2. **UNCTAD, nota de 2020 sobre B2B y B2C** y la nota técnica de 2024: leer qué se incluye (EDI, plataformas) y la cobertura. Fijarse en la salvedad de que faltan datos oficiales de muchos países.
3. **US Census Bureau, e-commerce trimestral**: para el orden de magnitud de la penetración (17,9% del retail en 3T 2026) y para mostrar que no es la mayoría.
4. **CACE, estudio anual** (para Argentina): el resumen público; fijarse en año de datos, tipo de muestra y si es pesos corrientes.
5. **Rysman 2009** como puerta a la teoría de plataformas.
6. **Laudon y Traver**, declarando la edición.

---

# PARTE B. Posición contraria

Para cada punto: evidencia en contra de lo que la base tiende a afirmar, evidencia a favor, y cómo escribirlo.

## B1. "El headless/composable es mejor"

**Evidencia que matiza o contradice**
- Costos: Fastr (CTO Ryan Breen, 20/04/2023, actualizado 20/06/2026) afirma que el TCO composable de una marca mediana "often runs 30% to 60% higher than projected" y que se subestima el mantenimiento de integraciones "by 3x to 5x" https://getfastr.com/blog/the-headless-commerce-productivity-myth-why-composable-stacks [L]. **Sin fuente ni método**; Fastr vende un producto de vitrina y lo promueve en el mismo artículo.
- Elogic (consultora, Adobe Silver y Shopify Plus Partner; 12/05/2026, actualizado 3/11/2026): para un negocio de US$ 20 millones de GMV, "composable TCO can run 100–200% higher" que un SaaS bien gestionado, atribuido a "research" sin cita; no recomienda composable si el equipo de ingeniería tiene menos de 15 personas, si marketing depende de ingeniería para cambios rutinarios, o si el GMV anual está bajo unos US$ 20 millones con menos de 10 integraciones. Pide calcular el costo total de cambio a tres años https://elogic.co/blog/composable-commerce-vs-headless/ [L].
- VTEX (Jordan Jewell, 25/03/2025): "MACH principles are no longer special; they're table stakes", y critica el enfoque best-of-breed; **cero datos**, y VTEX vende la alternativa unificada https://vtex.com/en-us/blog/mach-mirage [L].
- TechRepublic (resumen del buscador): los equipos composable deben coordinar lanzamientos y fallas entre sistemas, lo que exige madurez de DevOps [S].

**Evidencia a favor**
- Los mismos casos de Elogic muestran resultados positivos con composable o headless: un fabricante alemán B2B con 25% menos TCO y 30% menos tiempo de salida a mercado en tres años, aunque con costo mayor el primer año; un marketplace saudí con +48% de conversión tras headless con PWA. Todos son casos propios de la consultora, sin verificación [L].
- Elogic cita a Gartner con una reducción de TCO de 20-30% para adoptantes composable, solo en empresas con licencias de plataforma de US$ 500.000 a 2 millones por año; sin enlace [L, no verificado en Gartner].
- Shopify lanzó Hydrogen (headless, 2021) [M]: es una señal de que la oferta existe, no una prueba de que rinda.

**Conclusión del estado de la evidencia:** no encontré **ningún estudio independiente** (académico o de analista abierto) que mida costos o fracasos de headless/composable. Todas las cifras, a favor y en contra, vienen de proveedores o consultoras con algo que vender. Gartner no apareció en los resultados.

**Veredicto, cómo escribirlo:** como una decisión con condiciones, no como una mejora. Escribir "headless y composable dan independencia de la vitrina y de cada servicio, a cambio de integraciones propias y un equipo que las sostenga". Poner las condiciones de Elogic **como criterios de un proveedor** y no como regla. No citar 30-60% ni 100-200% como hechos. Si el tema los menciona, la frase es "una consultora afirma, sin método publicado". Marcar la brecha como hueco en la sección de fuentes.

## B2. "La tienda propia es mejor que vender en un marketplace"

**Evidencia a favor de la tienda propia**
- Costos en Amazon (EE. UU.): Marketplace Pulse (Juozas Kaziukėnas, 13/02/2023) estima que un vendedor típico paga más de 50% de sus ingresos entre comisión (15%, de 8% a 15% según categoría), FBA (20-35%) y publicidad (hasta 15%), contra unos 40% cinco años antes; "algunos vendedores reportaron pagar 60% e incluso 70%". Datos de P&L de una muestra de vendedores sin tamaño declarado; los rangos sumados dan entre 35% y 65%, no 50% exacto, y no incluyen inventario ni flete https://www.marketplacepulse.com/articles/amazon-takes-a-50-cut-of-sellers-revenue [L]. Una nota de marzo de 2024 repite 50-60% para vendedores de marca propia en 2023 (https://www.marketplacepulse.com/articles/amazon-fees-only-go-up) [L].
- Cliente: "el cliente que compra de ti en Mercado Livre o Shopee no va a volver", dice Claudio Dias de Magis5, citado por Nuvemshop (autora: Growth Acquisition Manager de Nuvemshop, que vende tiendas) https://www.nuvemshop.com.br/blog/ecommerce-ou-marketplace/ [L].
- Datos de un proveedor de tiendas: en México el comercio independiente creció 57% (facturación, primer semestre de 2025), atribuido por la nota al aumento de retenciones a vendedores de marketplace (de 1% a 2,5%, y hasta 20% más 16% de IVA para no regularizados). La nota admite que la reforma rige desde 2026, así que **la causa no explica un crecimiento de 2025** https://expansion.mx/tecnologia/2026/04/01/ecommerce-fuera-marketplaces-crece-mexico-cambios-fiscales [L].

**Evidencia a favor del marketplace**
- Inversión inicial menor; tráfico y credibilidad ya construidos; pagos resueltos (Nuvemshop, mismo artículo, que lo admite) [L].
- Peso del canal: ">75% de las ventas online" en marketplaces (Claudio Dias, Magis5) frente a ">50% del e-commerce brasileño" (Bruno de Oliveira, Nuvemshop): las dos cifras salen de charlas, no coinciden y no tienen metodología [L, en la nota de Nuvemshop].
- El 94% del GMV de Mercado Libre en 2025 (US$ 65.037 millones) sería de terceros (ECDB, resumen del buscador [S]); eso describe la plataforma, no la rentabilidad del vendedor.
- Los números de Amazon son de EE. UU. No hay evidencia independiente sobre las comisiones totales de Mercado Libre; la única nota sobre comisiones altas de MELI (iProUP 32296) no la abrí. **No extrapolar los 50% de Amazon a Mercado Libre.** Amazon dice que sus tarifas son de 15% o menos en la mayoría de las categorías (resumen del buscador [S]).
- Mercado Shops (tienda de Mercado Libre) habría cerrado en diciembre de 2025 (resumen del buscador [S]): dato relevante si se confirma.

**Veredicto, cómo escribirlo:** no es "mejor", es **un trade-off que depende de la etapa y del tipo de producto**. Escribir los costos de cada lado con su fuente y su mercado, y que la tienda propia gana en relación con el cliente y el margen pero exige conseguir tráfico propio. Los vendedores no eligen una u otra: muchos usan las dos (multihoming), pero no encontré medición independiente de cuántos. Marcar las notas de Nuvemshop como fuentes con interés comercial.

## B3. "Los benchmarks de conversión sirven para compararse"

**Evidencia en contra**
- Fuente de los datos: "los competidores no tienen incentivos para publicar cifras precisas", las cifras públicas son "una versión sanitizada", y no se sabe si el otro calcula igual (por ejemplo, incluir ventas mayoristas en la conversión D2C la infla) (The Good, consultora de optimización) https://thegood.com/insights/ecommerce-benchmarks/ [L].
- Sesgos de muestra: de supervivencia (se miden tiendas activas), de plataforma (Shopify, BigCommerce y WooCommerce tienen perfiles distintos), de canal, de estacionalidad y de definición (sesiones vs. visitantes únicos); el ejemplo "joyería 0,8% y compra impulsiva 6%, promedio 3,4%, no describe a ninguna de las dos" (Growth Suite, 21/05/2026) https://www.growthsuite.net/blog/the-problem-with-benchmarking-your-store-against-industry-averages [L]. **El autor es fundador de una app que vende analítica y el artículo promueve su producto; además no cita primarias** (los enlaces van a páginas de inicio de Littledata, Baymard, HBR, Shopify) y sus cifras (por ejemplo, brecha de medición de 40-60%) no tienen fuente. Los argumentos son razonables; sus números, no verificables.
- Rangos publicados muy dispersos: banda global de 1,4% a 3,0% (guía de 2026), 1% a 4% (Adobe, guía antigua), 2,2% en el primer trimestre de 2023 (Monetate), mediana de tienda Shopify de 1,5% según Littledata (todos de resúmenes del buscador [S]; no encontré la fuente del 1,4% de Shopify).

**Evidencia a favor**
- The Good: las tasas reales suelen estar en "a low, single digit"; el benchmark sirve para ubicar un orden de magnitud y desconfiar de una cifra de dos dígitos. Recomienda en cambio la propia serie histórica y metas por experimento [L].
- Cada benchmark tiene un sesgo de proveedor, pero no hay evidencia de que los rangos estén sistemáticamente en la dirección equivocada; el problema es la comparabilidad, no la falsedad.

**Veredicto, cómo escribirlo:** "una tasa de conversión sirve de orden de magnitud, no de vara de medir". Toda cifra de conversión lleva su **definición del denominador, su fuente, su tipo de tiendas y su fecha**. La recomendación es compararse con la propia historia y con el propio segmento. No usar ninguna cifra como "el promedio de la industria" salvo que una fuente primaria publique método y muestra.

## B4. "~70% de abandono de carrito significa una pérdida recuperable"

**Evidencia en contra**
- El 70,22% de Baymard (50 estudios, 2006 a 2025) es la **media simple, sin ponderar, de estudios con rango de 55% a 84%**; las fuentes citadas incluyen SaleCycle, Listrak, IBM, Barilliance y Forrester (varios proveedores de software de recuperación); la fórmula de abandono es (1 − compras ÷ carritos creados) × 100, **pero Baymard no dice si cada estudio usó esa definición** https://baymard.com/blog/cart-abandonment-rate [L].
- Gran parte es navegación, no pérdida: 42% de los compradores online de EE. UU. dice haber abandonado un carrito por "I was just browsing / not ready to buy", que Baymard llama "largely unavoidable". Pero atención: ese 42% es la proporción **de compradores que alguna vez abandonaron por ese motivo**, no la proporción de carritos abandonados. No se puede multiplicar para obtener la parte "irrecuperable". Y Baymard no publica el año, la muestra ni la forma de calcular esa encuesta [L].
- Evidencia académica: Kukar-Kinney y Close (*Journal of the Academy of Marketing Science* 38, 2010, pp. 240-250): "many customers use online carts for entertainment or as a shopping research and organizational tool, which may induce them to buy at a later session or via another channel", y los factores de búsqueda y consideración "play a larger role in cart abandonment than factors at the purchase decision stage" https://link.springer.com/article/10.1007/s11747-009-0141-5 [M, solo resumen; el artículo es de acceso restringido]. Es decir, parte de lo "abandonado" se compra después o en otro canal y por eso no es pérdida.
- La cifra de recuperabilidad: Baymard calcula US$ 260.000 millones multiplicando una mejora de conversión de 35,26% por US$ 738.000 millones de ventas e-commerce de EE. UU. y la UE; la mejora viene de "problemas solucionables" según sus pruebas, "no se presenta como resultado de experimentos medidos", y no explica cómo pasa de los sitios analizados (incluidos Walmart y Amazon) a todo el mercado [L]. El 35,26% es una estimación del propio proveedor de la base de datos.

**Evidencia a favor**
- Entre las razones "no evitables" de la encuesta de Baymard (excluida la navegación), los costos extra de envío, impuestos y tarifas son 40%, la entrega lenta 20%, la desconfianza con los datos de tarjeta 19%, la cuenta obligatoria 18%, el proceso largo 17%, los errores del sitio 17%, la política de devoluciones 13%, el total no visible 12%, la tarjeta rechazada 10% y pocos medios de pago 9% (porcentajes de las respuestas restantes, año de la encuesta no indicado) https://baymard.com/lists/cart-abandonment-rate [L]. Eso apoya que una parte de los abandonos tiene causas de diseño que se pueden corregir.
- El método de pruebas de usabilidad de Baymard (25 rondas de pruebas moderadas; más de 110 guías) es sólido como método cualitativo (vistazo, [M]).

**Veredicto, cómo escribirlo:** "alrededor de 70% de los carritos creados no termina en compra (media de 50 estudios con rango de 55% a 84%); no es una pérdida: una parte es navegación o compra posterior, y el potencial de mejora por checkout es una estimación del proveedor". Nunca "se pierde el 70% de las ventas" ni "recuperable". Poner la definición de abandono y el hueco de método.

## B5. "La omnicanalidad siempre rinde"

**Evidencia a favor**
- Sopadjieva, Dholakia y Benjamin (Medallia y Rice University), "A Study of 46,000 Shoppers Shows That Omnichannel Retailing Works", HBR, 3/01/2017: el título afirma que sí; **no pude leer el cuerpo** (la página solo devolvió la introducción) y los autores incluyen a empleados de Medallia https://hbr.org/2017/01/a-study-of-46000-shoppers-shows-that-omnichannel-retailing-works [M].
- Bell, Gallino y Moreno, "Offline Showrooms in Omnichannel Retail", *Management Science*, 2017: con datos de Warby Parker, abrir showrooms físicos aumentó la demanda total y la online (resumen del buscador, sobre páginas de Wharton y Tuck) [S].

**Evidencia en contra o que matiza**
- Gallino y Moreno (working paper, 83 tiendas de un retailer): poner compra online con retiro en tienda **redujo las ventas online** (aunque las compras con retiro cuentan como online) y aumentó el tráfico y las ventas en tienda [S].
- *Journal of Marketing* (2023, DOI 10.1177/00222429231193371): la entrada de tiendas de marca **canibaliza** las ventas del canal online propio de la marca y tiene efecto positivo en ventas de supermercado; las ventas de la propia tienda compensan lo perdido en el canal online [S, no pude abrir la página, 403].
- El costo de integrar inventarios, precios y pedidos entre tableros distintos es un riesgo operativo (Thinkinsights, ensayo analítico, no empírico) [S].
- Casi toda la evidencia positiva es de casos de retailers puntuales. No encontré un estudio general de rentabilidad (después de costos) de la omnicanalidad.

**Veredicto, cómo escribirlo:** "la omnicanalidad *puede* aumentar la demanda total y *puede* canibalizar un canal; depende del producto y de cómo se integra". Presentar los estudios con su caso (Warby Parker, un retailer de 83 tiendas) como ejemplos, no como ley. Distinguir multicanal (varios canales) de omnicanal (integrados). Marcar como hueco: rentabilidad neta.

## B6. "Las cuotas sin interés aumentan las ventas sin costo"

**Evidencia de que tienen costo y de quién lo paga**
- Argentina (iProfesional, 19/02/2020, **datos de entonces**): un producto de lista de $1.100 se ofrece a $1.200 en 12 cuotas "sin interés" de $100 (el interés se traslada al precio); el comercio paga un 3% de comisión por el posnet y espera hasta 18 días hábiles para cobrar; quienes pagan al contado "subsidian" a quienes compran en cuotas; el consejo es mirar el CFT. TEA de tarjetas entre 63% y 224% (promedio 131%) en esa nota https://www.iprofesional.com/finanzas/309622-los-secretos-detras-de-las-cuotas-sin-interes [L]. Tasas, plazos y comisiones han cambiado; no usarlas como vigentes.
- Argentina, norma de 2017: la Secretaría de Comercio exigió exhibir el costo financiero total en la comunicación de Ahora 12 y Ahora 18; la nota oficial dice que la operación "tiene un costo financiero y una tasa de interés asociada" https://www.argentina.gob.ar/node/8000 (24/01/2017) [L]. La frase "No existen las cuotas sin interés", atribuida a funcionarios en un resumen del buscador, **no aparece en la página oficial**: no usarla como cita.
- Ahora 12 tenía costo financiero total subsidiado por el Estado y subió cuando subieron las tasas (Cronista, resúmenes del buscador, sin fecha clara) [S]. Desde febrero de 2024 el régimen que reemplazó a Ahora 12 (Cuota Simple) ofrece 3 y 6 cuotas, según Infobae (resumen del buscador, sin abrir) [S].
- México: el comercio "normalmente absorbe" los intereses y paga una comisión mayor al banco, "from a few percentage points to much higher" (Stripe, actualizado 21/05/2026; guía de un procesador de pagos) https://stripe.com/resources/more/meses-sin-intereses-an-in-depth-guide [L]. No da cifras de efecto en ventas.
- Brasil: Brazil Journal afirma que los intereses están en el precio y que las compras al contado subsidian a las de plazo; ValorFinal calcula que rechazar 10% de descuento al contado por pagar en 10 cuotas equivale a unos 33% anual (cuenta propia, no oficial). No encontré un estudio del Banco Central que cuantifique el sobreprecio en el retail (resúmenes del buscador) [S].

**Evidencia sobre el efecto en ventas**
- A favor: EBANX (proveedor de pagos): "paying in installments can double the average order value (AOV) in Brazil" y +20% en ingresos en Brasil; +41% en México, con "EBANX internal data" sin muestra ni método https://www.ebanx.com/en/beyond-borders-2026/section-recurring-payments/chapter-installments-and-subscription [L]. dLocal habla de aumento de ventas de casi 12% sin metodología (resumen del buscador) [S]. Ambos cobran por procesar esas compras.
- Maesen y Ang (2024, *Journal of Marketing*): evidencia causal de que los pagos en cuotas BNPL ("pay in 4") aumentan el gasto, con datos de un gran retailer de EE. UU. y tres experimentos preregistrados; es BNPL y mercado de EE. UU., no cuotas bancarias latinoamericanas (resumen del buscador, [S]).
- Matiz: Cho y Rust, "The Free Installment Puzzle" (octubre de 2011, borrador "not for quotation"): con datos de una tarjeta, la probabilidad de que se ofrezca una cuota sin interés es de 27% pero solo 2,7% de las compras se hacen así, y concluyen que la demanda de crédito es "remarkably inelastic": la probabilidad de que un cliente típico elija la cuota gratis cuando se le ofrece es de 1 en 10 [L, texto completo del borrador, el país no figura en lo que leí; datos de una tarjeta]. Mide demanda de crédito, **no efecto en ventas del comercio**, así que no contradice los datos de los procesadores pero sí sugiere que el uso real puede ser menor al que se supone.
- No encontré ningún estudio académico sobre el efecto en ventas de cuotas sin interés en Argentina, Brasil o México.

**Veredicto, cómo escribirlo:** "'sin interés' significa que el comprador no ve la tasa: el costo lo paga el comercio (comisión mayor), los compradores al contado (precio de lista más alto) o, en programas oficiales, el Estado". Los aumentos de ventas son números de procesadores de pago, con interés comercial y sin método. Usar "puede aumentar la venta" con la fuente, nunca "sin costo". Fechar tasas y regímenes (Ahora 12, Cuota Simple).

## B7. Mitos documentados del e-commerce

Cada mito con su evidencia.

1. **"El e-commerce ya es la mayor parte del comercio minorista."** US Census, 3T 2026: 17,9% de las ventas minoristas de EE. UU. (17,2% sin ajustar) https://www.census.gov/retail/ecommerce.html [L]. En México, 17,7% (AMVO, datos 2025) [L]. En Argentina, 12% según una nota de Cronista, **sin fuente ni año** [L]. En el Reino Unido llegó a 37,8% en enero de 2021 y bajó a 26,3% en enero de 2024 (Wikipedia, secundaria) [M]. La penetración depende del país y puede bajar.
2. **"El comercio electrónico es principalmente B2C."** UNCTAD, 2018: B2B era el 83% (US$ 21 de 25,6 billones), con una definición que incluye EDI [L]. Para B2C, solo US$ 4,4 billones.
3. **"El crecimiento en pesos es crecimiento real."** CACE: +55% nominal de 2025 contra inflación de 31% citada en la nota del adelanto; eso es crecimiento real cercano a 18% (o 22% con el +60% del adelanto) [L, con mi cálculo].
4. **"Las cifras de e-commerce de distintos países se pueden comparar."** Miden cosas distintas: CACE mide facturación de empresas socias (incluye turismo, primera categoría); AMVO usa un panel de 1.048 compradores; ABComm no declara método; la OCDE define por método de pedido y no incluye WhatsApp tipeado a mano; Statistics Canada y la OMC usan definiciones distintas [L/S].
5. **"Los marketplaces cobran solo la comisión visible."** Marketplace Pulse: comisión 15% + FBA 20-35% + publicidad hasta 15%, más de 50% en total para el vendedor típico de Amazon (EE. UU., 2023, muestra sin tamaño) [L].
6. **"Tres de cada cuatro compras online se hacen en marketplaces."** Dos cifras que no coinciden (>75% y >50%) salen de charlas citadas por un proveedor de tiendas, sin metodología [L].
7. **"El promedio de conversión de la industria es X."** B3: no hay uno.
8. **"Cuotas sin interés = gratis."** B6.
9. **"Dos fuentes confirman el mismo dato"** cuando son la misma: en este tema, ABComm/ABIACOM, Confi/Neotrust y las notas de prensa que repiten la proyección son una fuente por dato. Proyecciones de enero de 2025 se reproducen en otros sitios "como si fueran actuales" (resumen del buscador) [S].

---

# Huecos (declarados)

1. **Presupuesto de búsqueda agotado:** no quedaron búsquedas para: Gartner y MACH Alliance (composable), literatura académica de marketplaces vs tienda propia (por ejemplo, Hagiu y Wright), estudios de recuperación de carritos abandonados con emails, estadísticas oficiales del Reino Unido (ONS) para el mito 1, historia con primarias (EDI, Minitel, móvil), Ebit/Nielsen y Neotrust de Brasil, normativa sobre cuotas del BCRA.
2. No pude leer: el informe completo de CACE (solo socios), el estudio completo de AMVO (se lee vía una nota especializada), los capítulos de Laudon y Traver y de Chaffey, eMarketer (403), el texto completo de Maesen y Ang, de Gallino y Moreno y de Kukar-Kinney y Close (solo resumen).
3. Sin explicación oficial de CACE sobre la revisión de 35,3 a 34,0 billones.
4. Sin evidencia independiente sobre costos de headless/composable, ni sobre comisiones totales de Mercado Libre, ni sobre rentabilidad de la omnicanalidad, ni sobre efecto en ventas de cuotas sin interés en Argentina, Brasil o México.
5. Fecha de fundación de Tiendanube/Nuvemshop y de Mercado Libre; hito de comercio móvil.
6. Edición y año de Chaffey 8.ª ed.; si existe traducción de la 18.ª de Laudon y Traver.
7. Año y muestra de la encuesta de razones de abandono de Baymard.
8. Inflación usada por CACE en el adelanto (31%) sin contrastar con INDEC.

## Cómo encaja con el árbol de ALCANCE.md

- La división coincide con Laudon y Traver para modelos y con la OCDE para el concepto, pero el campo estadístico no divide por "plataforma de tiendas / pagos / checkout" sino por método de pedido. Conviene que `Fundamentos/` incluya la definición OCDE y diga que las partes del árbol son una división propia de este proyecto.
- B1, B2 y B5 van a `Plataforma-de-tiendas/tipos-de-plataforma` y a `Venta-en-varios-canales/`; B3 y B4, a `Checkout-y-conversion/`; B6, a `Pagos/cuotas-y-medios-locales`. El árbol no tiene un lugar para "mitos": propongo una sección corta en `Fundamentos/` que enlace a esas notas.
