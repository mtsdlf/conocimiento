# Tamaño de la zona de vidrieras a medida (headless, composable, código abierto) en Argentina

Fecha de consulta: 2026-11-22. Ángulo: tamaño de abajo hacia arriba (marcas que ya tienen una vitrina a medida y marcas que podrían quererla), cruzado por el lado de la oferta (agencias) y por eventos de la cámara (Hot Sale). Método: lectura de las páginas públicas de StoreLeads por plataforma y por tecnología, el directorio de integradores de VTEX filtrado por país con un navegador real, Clutch, los directorios de Medusa y Saleor, la página de agencias de Tiendanube, prensa del Hot Sale 2026; 5 búsquedas web (cupo no agotado). Calificación: fuente A a F / dato 1 a 6; [L] leído (la página entera, con WebFetch o con el navegador), [S] por resumen del buscador. Las cuentas son mías; los **supuesto** están marcados. Lo que ya está en la base (`Plataforma-de-tiendas/presencia-en-argentina.md`, `tipos-de-plataforma.md`, `segmentos-de-comerciantes.md`) y en el barrido liviano (`lind-negocio/el-taller/analisis/2026-11-22-el-bosque/motor-para-vidrieras-a-medida.md`) se cita y no se repite.

## Respuesta primero

- **Marcas que hoy tienen una vitrina a medida detectable: 100 a 250, centro ~150.** Lo medido es chico: StoreLeads ve Next.js en 81 tiendas argentinas, Nuxt en 19 y Shopify Hydrogen en 5 (105 en total, 13-nov-2026). Se descuenta ruido (sitios que no son marcas) y se suman los marcos que no se pudieron medir (**supuesto**).
- **Marcas que podrían quererla (las que ya pagan una plataforma de gama alta o tienen tamaño de empresa): 1.200 a 1.900, centro ~1.500.** Suma de VTEX (438), Magento (332), Salesforce Commerce Cloud (20), Shopify Plus (114), Tiendanube Evolución ("+400", dicho por la empresa) y las tiendas de WooCommerce y carrito propio con 50 o más empleados (179 + 69).
- **De esas, las que cumplen las condiciones para que convenga (equipo propio, GMV alto): 150 a 450, centro ~300, todo supuesto.** Coincide en orden de magnitud con las ~150 que ya lo hicieron.
- **Agencias y estudios que las construyen: 18 integradores de VTEX con sede o atención en Argentina (medido); 25 a 70 con capacidad de hacer una vitrina a medida, centro ~40 (supuesto).** Clutch lista 151 firmas de e-commerce que atienden Argentina, 44 de Shopify y 39 de Magento, con mucho solapamiento. En los directorios de Medusa (26 expertos) y Saleor (14 agencias) no hay ninguna que declare sede en Argentina.
- **Techo regional:** Next.js en tiendas de Chile 126, México 227, Uruguay 12 y Brasil 1.432; Hydrogen en Chile 13 y México 43. Argentina más Uruguay, Chile y México suman 446 tiendas con Next.js, unas 5,5 veces Argentina sola.
- **Cruce:** el Hot Sale 2026 tuvo "más de 800 marcas" (1.010 en 2025, según una nota de VTEX), del mismo orden que el universo de ~1.500. El lado de la oferta (18 integradores VTEX para ~440 tiendas VTEX; ~40 agencias con capacidad headless) da ~100 a 300 vitrinas a medida, del orden de lo detectado.
- **Fuerza:** media para el universo de ~1.500 (conteos de terceros con fecha, más una cifra de la empresa); débil a media para las ~150 que ya tienen vitrina a medida (el rastreador detecta poco y con ruido); débil para las agencias con capacidad headless.

## Método

1. **Lo que ya existe (detección por tecnología).** StoreLeads cuenta tiendas por marco de frontend. Se leyeron las páginas de Next.js, Nuxt y Shopify Hydrogen para Argentina, y Next.js e Hydrogen para la región. Las de React, Vue.js, Gatsby y Shopify Plus por tecnología dieron 404: no existen con ese nombre. Medusa, Saleor, Vendure, commercetools no aparecen en la lista de 100 plataformas de StoreLeads (https://storeleads.app/reports).
2. **El universo que podría quererla.** Tiendas en plataformas de gama alta (VTEX, Magento, Salesforce Commerce Cloud, Shopify Plus, Tiendanube Evolución) más las tiendas de plataformas masivas con 50 o más empleados según StoreLeads.
3. **La oferta.** Directorio de integradores de VTEX filtrado por país (leído con un navegador real), Clutch por categoría para Argentina, directorios de Medusa y Saleor, programa de agencias de Tiendanube, avisos de empleo (Get on Board, LinkedIn).
4. **Cruces.** Hot Sale (marcas que pagan por estar en el evento de la cámara), CACE (socios), relación entre integradores y tiendas, y la región como techo.

## 1. Lo que ya existe: vitrinas a medida detectadas

| Fuente | URL | Tipo | Calif. | Marca |
|---|---|---|---|---|
| StoreLeads, Next.js en Argentina | https://storeleads.app/reports/technology/Next.js/country/AR | Rastreador comercial | B / 3 | [L] |
| StoreLeads, Nuxt en Argentina | https://storeleads.app/reports/technology/Nuxt/country/AR | Rastreador comercial | B / 3 | [L] |
| StoreLeads, Shopify Hydrogen en Argentina | https://storeleads.app/reports/technology/Shopify%20Hydrogen/country/AR | Rastreador comercial | B / 3 | [L] |
| StoreLeads, Shopify Hydrogen mundial | https://storeleads.app/reports/technology/Shopify%20Hydrogen | Rastreador comercial | B / 3 | [L] |
| StoreLeads, Custom Cart en Argentina | https://storeleads.app/reports/custom/AR/top-stores | Rastreador comercial | C / 4 (sus cifras no cierran entre sí) | [L] |
| VTEX, guía de FastStore | https://developers.vtex.com/docs/guides/faststore | Primaria (el proveedor) | A / 3 | [L] |

Afirmaciones (todas con datos actualizados al 13-nov-2026):

- **Next.js: 81 tiendas en Argentina.** Por plataforma de comercio: Magento 28, VTEX 22, carrito propio 16, Shopify 7, WooCommerce 3, Tiendanube 2, Sitecore 1, Oracle 1, neto 1. Las cinco primeras por ranking: Frávega, Personal, Rappi Argentina, Cetrogar, Juleriaque; entre las recién instaladas, Bonafide, una inmobiliaria, una tienda "FastStore Starter" y una marca de cripto. **Inferencia:** el conteo mezcla marcas con sitios que no son de una marca de consumo (una telefónica, una app de reparto, una inmobiliaria).
- **Nuxt: 19 tiendas.** Carrito propio 14, Tiendanube 2, WooCommerce 1, Magento 1, Ecwid 1.
- **Shopify Hydrogen: 5 tiendas en Argentina** (BRAFH, Parva libros, Celeste Aloe, RITO, un sitio mayorista de Picafili), todas fuera del primer millón del ranking mundial. En el mundo, 5.447; Estados Unidos 1.735.
- **VTEX con Next.js: 22.** La guía de FastStore pide conocer Next.js para trabajar con él. **Inferencia:** esas 22 son en buena parte vitrinas FastStore; la guía no dice que FastStore esté hecho sobre Next.js.
- **Tiendanube con un marco de frontend: 4 (2 con Next.js, 2 con Nuxt).** **Inferencia:** el uso de su API de vitrina se ve muy poco en el rastreador; puede ser poco uso o que no se detecte.
- **Carrito propio ("Custom Cart"): 8.120 en Argentina**, encabezado por Mercado Libre, Frávega, Personal, Movistar y Turismocity. Su tabla trimestral (pico de 9.731 en el tercer trimestre de 2025, 6.579 en el cuarto de 2026) no cierra con el titular. **Inferencia:** es una bolsa de todo lo que no es una plataforma conocida; no sirve como conteo de vitrinas a medida.
- Las páginas de React, Vue.js y Gatsby por país dieron 404. Lo que corre sobre esos marcos sin Next.js ni Nuxt (Astro, Angular, una aplicación React propia) no se midió: hueco.

## 2. El universo que podría quererla

| Fuente | URL | Tipo | Calif. | Marca |
|---|---|---|---|---|
| StoreLeads, VTEX en Argentina | https://storeleads.app/reports/vtex/AR/top-stores | Rastreador comercial | B / 2 (VTEX dice ~400 clientes en el país, ver la base) | [L] |
| StoreLeads, Magento en Argentina | https://storeleads.app/reports/magento/AR/top-stores | Rastreador comercial | B / 3 | [L] |
| StoreLeads, Salesforce Commerce Cloud en Argentina | https://storeleads.app/reports/demandware/AR/top-stores | Rastreador comercial | B / 3 | [L] |
| StoreLeads, Shopify en Argentina | https://storeleads.app/reports/shopify/AR/top-stores | Rastreador comercial | B / 3 | [L] |
| StoreLeads, Tiendanube y WooCommerce en Argentina | https://storeleads.app/reports/tiendanube/AR/top-stores ; https://storeleads.app/reports/woocommerce/AR/top-stores | Rastreador comercial | B / 3 | [L] |
| Tiendanube, clientes de Evolución | https://www.tiendanube.com/evolucion/clientes | La empresa (vende el plan) | C / 4 | [L] |
| Ámbito, 20-oct-2025 | https://www.ambito.com/negocios/tiendanube-acelera-inteligencia-artificial-y-apunta-al-millon-marcas-latinoamerica-n6198958 | Prensa sobre lo que dice la empresa | C / 4 | [L] |

Afirmaciones:

- **VTEX: 442 tiendas vivas en Argentina** (438 en la tabla del cuarto trimestre de 2026), con pico de 469 en el primer trimestre de 2026 y estable interanual. Primeras: Farmacity, Easy, Jumbo, Nike, Carrefour.
- **Magento: 322 tiendas** (332 en la tabla), -27% interanual en el tercer trimestre de 2026; pico de 568 en el tercer trimestre de 2023. Primeras: River Plate, Solo Deportes, Casa del Audio, Tiendamia, Rapsodia.
- **Salesforce Commerce Cloud: 20** (18 en la tabla): Moov, Dexter, Stock Center, Flecha Bus, New Balance.
- **Shopify: 9.034 tiendas vivas, 114 de ellas Plus.**
- **Tiendanube Evolución:** "+400 negocios líderes en Argentina ya están escalando sus ventas en nuestra plataforma" (página de la empresa). Regional: el segmento Evolución "ya reúne 3.000 marcas y concentra el 40% del total de ventas procesadas en la plataforma" (Ámbito, octubre de 2025). No se aclara si las 400 de Argentina son todas del plan Evolución.
- **Tiendas por cantidad de empleados** (StoreLeads asigna tamaño solo a las que puede cruzar con una empresa; el resto es "Unknown"):

| Plataforma | Sin dato | 1-49 | 50-249 | 250+ | 50 o más |
|---|---|---|---|---|---|
| Tiendanube | 58.804 | 466 | 138 | 92 | **230** |
| WooCommerce | 24.403 | 231 | 104 | 75 | **179** |
| VTEX | 287 | 49 | 42 | 64 | **106** |
| Carrito propio | 7.876 | 175 | 34 | 35 | **69** |
| Shopify | 8.875 | 84 | 33 | 42 | **75** |
| Magento | 262 | 14 | 28 | 18 | **46** |

  **Inferencia:** la columna "sin dato" no quiere decir chica; en VTEX 287 de 442 no tienen tamaño asignado y la plataforma es casi solo de empresas. Las cifras de 50 o más son pisos.

## 3. La oferta: agencias y estudios

| Fuente | URL | Tipo | Calif. | Marca |
|---|---|---|---|---|
| VTEX, directorio de integradores (filtro por país) | https://vtex.com/us-en/partners | Primaria (el proveedor) | A / 3 | [L] navegador |
| Clutch, e-commerce en Argentina | https://clutch.co/ar/developers/ecommerce | Directorio con reseñas pagas en parte | C / 4 | [L] (100.000 de 160.000 caracteres) |
| Clutch, Shopify en Argentina | https://clutch.co/ar/developers/shopify | Directorio | C / 4 | [L] |
| Clutch, Magento en Argentina | https://clutch.co/ar/developers/magento | Directorio | C / 4 | [L] (parcial) |
| Tiendanube, programa de agencias | https://www.tiendanube.com/socios/comerciales | La empresa (vende el programa) | C / 4 | [L] navegador |
| Medusa, expertos | https://medusajs.com/experts | Primaria | A / 3 | [L] |
| Saleor, partners | https://saleor.io/partners | Primaria | A / 3 | [L] |
| Shopify, directorio de partners | https://www.shopify.com/partners/directory/services/store-setup/headless-commerce?locationCountryCodes=AR | Primaria | sin calificar | no se pudo leer: el filtro por país no carga sin sesión |

Afirmaciones:

- **VTEX: 244 integradores en el mundo** (Brasil 114, LATAM 80, EMEA/APAC 37, Estados Unidos 21; Diamond 20, Gold 51, Silver 173). **Con Argentina en el filtro: 18.** Diamond: Infracommerce, Known Online, Pierce Commerce. Gold: Innew, We Are. Silver: Arbusta, Cruce, Fulljaus, Goldben, Inbound Digital, Iurco, Kudos, Lindo Software, MADE OF, Nomada Digital, POW, Red Clover, Solucionet. Chile también tiene 18 y México 21. La página dice que el programa premia a los integradores que hacen tiendas FastStore.
- **Clutch:** 151 firmas en "e-commerce developers" para Argentina, incluidas algunas de afuera que "atienden" el país; 44 en Shopify (43 de las visibles con sede argentina) y 39 en Magento (casi todas con sede argentina). Los nombres se repiten entre las tres listas (Serfe, eCloud, Greencode, Kudos, Iurco, Wuala y otras). Proyecto mínimo declarado entre US$ 1.000 y US$ 75.000. Lo dicen las firmas; Clutch cobra por ubicación destacada.
- **Tiendanube:** "+1450 agencias activas", "$280M USD generados en facturación por clientes gestionados junto a nuestras agencias en los últimos 12 meses", "+1960 nuevos clientes". Lo dice quien vende el programa; no aclara si es solo Argentina. Cuenta agencias de marketing, diseño y freelancers, no solo de desarrollo.
- **Medusa: 26 expertos**, ninguno con sede declarada en Argentina; dos (Seeed y Alpha Solutions) dicen atender Sudamérica. **Saleor: 14 agencias**, ninguna con país declarado; una (Basement) dice atender América Latina en inglés y castellano.
- **Avisos de empleo:** Get on Board muestra 1 aviso con la etiqueta VTEX (en Chile) y 5 con Shopify (ninguno de Argentina). LinkedIn, sin sesión, da "4,000+" avisos de VTEX en Argentina, "1,000+" de Shopify Plus y "910" de Hydrogen: es búsqueda difusa por palabra y no sirve como conteo (F/6). El barrido liviano ya citó dos avisos sueltos de VTEX.

## 4. Tabla de abajo hacia arriba

| Paso | Cuenta | Resultado | Pieza que la sostiene (calif.) |
|---|---|---|---|
| 1 | Vitrinas con marco de frontend detectadas: Next.js 81 + Nuxt 19 + Hydrogen 5 | 105 | StoreLeads, 13-nov-2026 (B/3) |
| 2 | Menos ruido: **supuesto** 20% a 40% no son marcas de consumo (3 o 4 de las 10 visibles en Next.js no lo son) | 63 a 84 | Lista visible de StoreLeads (B/3); proporción supuesta (F/6) |
| 3 | Más lo no detectado (otros marcos, aplicaciones propias, detección fallida): **supuesto** ×1,5 a ×3 | **100 a 250; centro ~150** | Supuesto (F/6); que existe lo no detectado es inferencia de cómo trabaja un rastreador |
| 4 | Universo de gama alta: VTEX 438 + Magento 332 + Salesforce 20 + Shopify Plus 114 + Tiendanube Evolución 400 + WooCommerce 50+ empleados 179 + carrito propio 50+ empleados 69 | 1.552 | StoreLeads (B/3); Tiendanube, dicho por la empresa (C/4) |
| 5 | Ajuste del universo: Magento y WooCommerce incluyen tiendas viejas o poco activas (Magento cae 27% interanual); las de "sin dato" de tamaño suman empresas no vistas. **Supuesto** -20% a +20% | **1.200 a 1.900; centro ~1.500** | Supuesto (F/6) |
| 6 | Las que cumplen condiciones para que la vitrina a medida convenga: **supuesto** 10% a 25% del paso 5. Elogic pone el umbral en equipo de ingeniería de 15+ personas o GMV anual de US$ 20 millones (ya en la base, `tipos-de-plataforma.md`); NubeCommerce dice que las grandes marcas tienen en promedio más de 10 personas en el canal digital ([S]) | **150 a 450; centro ~300** | Criterio de un proveedor (D/5); proporción supuesta (F/6) |
| 7 | Agencias con capacidad de hacer vitrinas a medida: integradores VTEX 18 + firmas de Clutch con desarrollo propio y experiencia en Next.js o headless, **supuesto** 10 a 50 | **25 a 70; centro ~40** | VTEX (A/3) para los 18; el resto F/6 |

## 5. El cruce

**Por el Hot Sale (lado demanda).** El Hot Sale 2026 tuvo "más de 800 marcas", 48% pymes y 241 del interior (Mercado, 5-may-2026: https://mercado.com.ar/agenda/hot-sale-2026-mas-de-800-marcas-y-foco-en-financiacion, B/2 [L]). Una nota de VTEX citada por el buscador da 1.010 marcas para 2025 (https://mercado.com.ar/ruta-digital/hot-sale-2026-vtex-pone-el-foco-en-planificacion-y-tecnologia-para-el-pico, C/4 [S]). La CACE tendría unos 1.400 socios según una nota sin fecha (https://infonegocios.info/default/la-cace-renovo-autoridades-alberto-calvo-presidente, D/5 [S]; la página de socios dio 429). Marcas que pagan por estar en el evento grande del año: 800 a 1.000. Coincide en orden de magnitud con el universo del paso 5 (1.200 a 1.900); el Hot Sale es un piso porque no todas las marcas grandes participan y la mitad son pymes.

**Por la oferta.** 442 tiendas VTEX y 18 integradores con presencia en el país: ~25 tiendas por integrador (sin contar las que mantiene un equipo propio ni los integradores de afuera). Si ~40 agencias (paso 7) tuvieran de 3 a 8 vitrinas a medida cada una (**supuesto**), habría 120 a 320. Coincide con el paso 3 (100 a 250).

**Por la región (techo).**

| País | Next.js | Shopify Hydrogen | VTEX | Integradores VTEX |
|---|---|---|---|---|
| Argentina | 81 | 5 | 442 | 18 |
| Uruguay | 12 | sin dato | sin dato | sin dato |
| Chile | 126 | 13 | 312 | 18 |
| México | 227 (115 sobre Shopify) | 43 | 232 | 21 |
| Brasil | 1.432 (722 carrito propio, 394 Shopify, 201 VTEX) | sin dato | sin dato | 114 (región Brasil) |

Fuentes: páginas de StoreLeads por tecnología y país (B/3, [L]) y directorio de VTEX ([L]). **Inferencia:** Argentina tiene más tiendas VTEX que Chile y México pero menos vitrinas con Next.js; en México el uso de Next.js viene sobre todo de Shopify. Argentina más Uruguay, Chile y México: 446 tiendas con Next.js. Con Brasil, ~1.900.

## Fuerza de la cifra

- **Universo de ~1.500 marcas que podrían quererla: media.** Conteos de un rastreador con fecha, una cifra de la empresa y un cruce (Hot Sale) del mismo orden.
- **~150 marcas con vitrina a medida hoy: débil a media.** Lo detectado es medido (105), pero el ruido y lo no detectado son supuestos que mueven el número de 60 a 250.
- **150 a 450 marcas a las que les convendría: débil.** El criterio viene de un proveedor y la proporción es supuesta.
- **~40 agencias con capacidad headless: débil.** Solo los 18 integradores de VTEX están medidos.
- **La pieza que más mueve el rango:** cuánto no ve el rastreador. Una vitrina a medida bien hecha puede no dejar rastro del marco ni de la plataforma; el ×1,5 a ×3 del paso 3 es la mitad de la incertidumbre. Le sigue la proporción del paso 6.

## Huecos

- **Cuántas vitrinas a medida no detecta el rastreador.** StoreLeads no publica cómo detecta los marcos ni tiene páginas de React, Vue, Gatsby o Astro por país. Se cerraría con una muestra a mano: tomar las ~440 tiendas VTEX y las ~330 Magento y mirar el HTML de cada una.
- **Cuántas agencias argentinas hacen vitrinas a medida.** El directorio de Shopify filtrado por país y por "headless commerce" no carga sin sesión; Clutch no tiene esa categoría; Medusa y Saleor no tienen ninguna agencia con sede declarada en Argentina.
- **Cuántas tiendas usan la API de vitrina de Tiendanube.** Solo 4 tiendas Tiendanube aparecen con Next.js o Nuxt; la empresa no publica la cifra.
- **Facturación de las tiendas medianas y grandes.** No hay una fuente con GMV por marca ni por plataforma en Argentina (ya declarado en la base, `presencia-en-argentina.md`).
- **Avisos de empleo como conteo.** Get on Board tiene pocos avisos y LinkedIn sin sesión da cifras infladas por búsqueda difusa. Bumeran no se consultó.
- **Uruguay:** sin dato de VTEX ni de Hydrogen.
- **Commercetools, Medusa, Saleor, Vendure en Argentina:** StoreLeads no los detecta como plataforma; ninguna fuente pública da clientes por país.
- **CACE:** la página de socios dio 429; la cifra de ~1.400 socios es sin fecha y por resumen.
- **Shopify Plus por tecnología:** la página dio 404; el 114 sale del resumen de la página de Shopify en Argentina.

## Fuentes

Todas consultadas el 2026-11-22.

- StoreLeads, Next.js por país (AR, UY, CL, MX, BR): https://storeleads.app/reports/technology/Next.js/country/AR (y /UY, /CL, /MX, /BR) [B/3, L]
- StoreLeads, Nuxt en Argentina: https://storeleads.app/reports/technology/Nuxt/country/AR [B/3, L]
- StoreLeads, Shopify Hydrogen (mundial, AR, CL, MX): https://storeleads.app/reports/technology/Shopify%20Hydrogen y /country/AR, /CL, /MX [B/3, L]
- StoreLeads, plataformas en Argentina: https://storeleads.app/reports/vtex/AR/top-stores ; https://storeleads.app/reports/magento/AR/top-stores ; https://storeleads.app/reports/demandware/AR/top-stores ; https://storeleads.app/reports/shopify/AR/top-stores ; https://storeleads.app/reports/tiendanube/AR/top-stores ; https://storeleads.app/reports/woocommerce/AR/top-stores ; https://storeleads.app/reports/custom/AR/top-stores [B/3, L]
- StoreLeads, VTEX en Chile y México: https://storeleads.app/reports/vtex/CL/top-stores ; https://storeleads.app/reports/vtex/MX/top-stores [B/3, L]
- StoreLeads, lista de plataformas: https://storeleads.app/reports [B, L]
- VTEX, directorio de integradores: https://vtex.com/us-en/partners [A/3, L con navegador y filtro por país]
- VTEX, guía de FastStore: https://developers.vtex.com/docs/guides/faststore [A/3, L]
- Clutch: https://clutch.co/ar/developers/ecommerce ; https://clutch.co/ar/developers/shopify ; https://clutch.co/ar/developers/magento [C/4, L parcial]
- Tiendanube, agencias partner: https://www.tiendanube.com/socios/comerciales [C/4, L]
- Tiendanube, clientes Evolución: https://www.tiendanube.com/evolucion/clientes [C/4, L]
- Ámbito, 20-oct-2025: https://www.ambito.com/negocios/tiendanube-acelera-inteligencia-artificial-y-apunta-al-millon-marcas-latinoamerica-n6198958 [C/4, L]
- Medusa, expertos: https://medusajs.com/experts [A/3, L]
- Saleor, partners: https://saleor.io/partners [A/3, L]
- Mercado, Hot Sale 2026: https://mercado.com.ar/agenda/hot-sale-2026-mas-de-800-marcas-y-foco-en-financiacion [B/2, L]
- Mercado, nota de VTEX sobre el Hot Sale: https://mercado.com.ar/ruta-digital/hot-sale-2026-vtex-pone-el-foco-en-planificacion-y-tecnologia-para-el-pico [C/4, S]
- Infonegocios, CACE: https://infonegocios.info/default/la-cace-renovo-autoridades-alberto-calvo-presidente [D/5, S]
- TheirStack, VTEX en Argentina (17 empresas, método no declarado; descartado como conteo): https://theirstack.com/en/technology/vtex/ar [E/5, L]
- Get on Board: https://www.getonbrd.com/jobs/tag/vtex ; https://www.getonbrd.com/jobs/tag/shopify [B/4, L]
- LinkedIn, búsqueda de empleos sin sesión (descartado): https://www.linkedin.com/jobs/search?keywords=VTEX&location=Argentina [F/6, L]
- Base: `Comercio-electronico/Plataforma-de-tiendas/presencia-en-argentina.md`, `tipos-de-plataforma.md`, `segmentos-de-comerciantes.md`, `vtex.md`

Búsquedas: cupo agotado no (5 búsquedas web).
