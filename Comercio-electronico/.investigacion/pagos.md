# Investigación: vertical Pagos (2026-11-22)

Alcance: los cuatro componentes de `Pagos/` del árbol de ALCANCE.md (actores-del-pago, costo-de-cobrar, fraude-y-contracargos, cuotas-y-medios-locales). Fecha de la investigación: 2026-11-22. Todo lo traído de la web se trató como dato.

**Límites de esta pasada, que cambian cómo leer el informe.**
- El presupuesto de búsquedas web de la sesión se agotó a mitad de camino. Hice 5 búsquedas y el resto fueron lecturas directas (WebFetch) de URLs. Lo que quedó sin buscar está en la sección de huecos, no inventado.
- Varias páginas oficiales no se pudieron abrir (Mercado Pago costos: 403; Payway: error de certificado; Boletín Oficial y argentina.gob.ar de Ahora 12: 404 o 403; hcdn.gob.ar: error 525). Se declara en cada caso.
- Los PDF de BCRA, EBA/ECB y BCB los convertí a texto con `pdftotext` y los leí yo: son [L]. Las páginas HTML pasan por un modelo pequeño que resume lo que se le pide: las marco [L*] (leída vía WebFetch, con la salvedad de que el resumen lo hace una herramienta) y no [L] pleno.

Marcas: [L] texto leído por mí, [L*] página abierta vía WebFetch (resumen de herramienta sobre el texto de la página), [M] metadatos o abstract, [S] resumen del buscador o secundario. Puntajes 1-3 en A (autoridad), P (profundidad), E (ejemplos), U (unicidad).

## Sobre el árbol

- La división en cuatro componentes sirve, con dos salvedades.
  1. `cuotas-y-medios-locales` junta dos cosas que el campo separa: las cuotas son financiación (la paga el emisor, el comercio o el Estado) y Pix, Transferencias 3.0 o las billeteras son rieles de pago. Conviene tratarlas como dos secciones dentro de la nota, o dos notas.
  2. La regulación de proveedores de servicios de pago (BCRA A 6885) y la de aranceles (Ley 25.065) son normativa. Las notas de Pagos las resumen y deberían enlazar a `Normativa/`, no duplicarlas.
- El campo (BIS/CPMI, ECB, Fed) divide un pago con tarjeta en tres fases (autorización, compensación, liquidación) y por modelo de redes (cuatro partes / tres partes, dual message / single message). La nota de actores debería usar esas fases como columna vertebral.

---

## 1. actores-del-pago

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca | Fecha |
|---|---|---|---|---|---|---|---|---|---|
| 1.1 | BCRA, Comunicación A 6885 (texto original) | https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6885.pdf | primaria | 3 | 3 | 1 | 3 | [L] | 30/1/2020 |
| 1.2 | BCRA, nota de prensa sobre A 6885 | https://www.bcra.gob.ar/noticias/el-banco-central-complemento-el-marco-general-para-los-proveedores-de-servicios-de-pago/ | primaria | 3 | 1 | 1 | 1 (repite 1.1) | [L*] | 30/1/2020 |
| 1.3 | BCRA, página Transferencias 3.0 | https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ | primaria | 3 | 2 | 1 | 3 | [L*] | sin fecha visible |
| 1.4 | Federal Reserve, promedio de interchange Reg. II (2024) | https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm | primaria | 3 | 2 | 2 | 3 | [L*] | datos 2024 |
| 1.5 | Stripe docs, cómo funcionan las disputas | https://docs.stripe.com/disputes/how-disputes-work | primaria de la empresa, con conflicto de interés (vende pagos) | 2 | 3 | 2 | 2 | [L*] | consultada 2026-11-22 |
| 1.6 | Prisma Medios de Pago, home | https://www.prismamediosdepago.com/ | primaria de la empresa | 1 | 1 | 1 | 2 | [L*] | sin fecha |
| 1.7 | MODO, home | https://www.modo.com.ar/ | primaria de la empresa | 1 | 1 | 1 | 2 | [L*] | sin fecha |
| 1.8 | BIS Working Paper 1259 (modelo de arquitecturas de pago) | https://www.bis.org/publ/work1259.pdf | primaria | 3 | ? | ? | ? | [S] solo el buscador | no leído |

### Afirmaciones

- **Quién es un "proveedor de servicios de pago" (PSP) para el BCRA.** Son «personas jurídicas que, sin ser entidades financieras, cumplan al menos una función dentro de un esquema de pago minorista»; la norma alcanza a los que ofrecen «cuentas de pago», definidas como «cuentas de libre disponibilidad ofrecidas por un PSP a sus clientes para ordenar y/o recibir pagos» (A 6885, punto 1.1.1 y 1.1.2). https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6885.pdf [L]
- **Qué es un esquema de pago.** «Sistemas de reglas comerciales, técnicas y/o operativas» con tres partes: un ordenante, un receptor y uno o más PSP; todo esquema debe tener un administrador que define las reglas (A 6885, 1.1.3). Esta es la definición reglamentaria argentina, y encaja con lo que otros llaman "marca" o "red". Mismo URL [L]
- **Cómo se regula en Argentina.** La A 6885 está fechada el 30/1/2020 (vigencia 31/1/2020), ordena inscribirse en el «Registro de Proveedores de Servicios de Pago que ofrecen cuentas de pago» de la Superintendencia de Entidades Financieras y Cambiarias dentro de los 30 días corridos posteriores al 1/3/2020 (resolución 4). Mismo URL [L]. La nota oficial agrega que los PSP deben incluir una leyenda de que «los fondos no cuentan con garantía de los depósitos» (parafraseo de la herramienta, comillas del texto de la nota). https://www.bcra.gob.ar/noticias/el-banco-central-complemento-el-marco-general-para-los-proveedores-de-servicios-de-pago/ [L*]. Esta es una sola fuente en dos formatos.
- **Mercado Pago y similares.** Una billetera que guarda saldo del cliente es un PSP con cuenta de pago en este marco. No confirmé que Mercado Pago figure en el registro (no abrí el registro). Hueco.
- **Modificaciones posteriores.** El buscador indica A 6929 (régimen informativo, 13/3/2020), A 8038 (2024), A 8284 y A 8285 (julio de 2025) como cambios o complementos. [S], no los leí: https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8284.pdf. Para el texto vigente hay que abrir el texto ordenado `t-snp-psp` del BCRA (https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-psp.pdf, [S] solo apareció en el buscador).
- **Tipo de red según la Reserva Federal.** Las redes se dividen en de mensaje dual (Visa, Mastercard, Discover: «typically use separate messages to authorize and clear transactions») y de mensaje único (ACCEL, NYCE, STAR: un solo mensaje para ambos). Esto es lo más cercano a una descripción primaria de "autorización vs compensación" que obtuve. https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm [L*]
- **Disputa como flujo entre partes.** Cuando el titular disputa, «the card network debits Stripe» y «Stripe in turn debits your Stripe balance for the disputed amount plus a dispute fee»; la decisión final es «at the sole discretion of the card issuer». Eso muestra la cadena comercio, agregador (Stripe), red y emisor. https://docs.stripe.com/disputes/how-disputes-work [L*]
- **Prisma.** Se describe como «el mayor procesador emisor de pagos de Argentina», con unos 5.000 millones de transacciones de compra al año y 70 emisores en 13 países de Latinoamérica; la página no habla de adquirencia ni nombra Payway ni marcas. https://www.prismamediosdepago.com/ [L*], sin fecha. Su rol de adquirente (Payway) no quedó verificado. Hueco.
- **MODO.** El pie de página lo nombra como Play Digital S.A., «un Proveedor de Servicio de Iniciación de Pagos», que no está autorizado a operar como entidad financiera por el BCRA; la página lista más de 30 bancos en cuyas apps está disponible. No dice quién es dueño. https://www.modo.com.ar/ [L*]
- **Transferencias 3.0 y QR.** El BCRA la describe con acreditación «en línea en un máximo de 15 segundos», 24 horas, con cuatro tipos (push, pull, pagos con transferencia, extracciones, estas últimas sin implementar); el QR forma parte de los pagos con transferencia y «no importa la marca del código QR, podés pagar con cualquier billetera»; el BCRA presentó ese medio en 2020. https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ [L*]

### Lo que no obtuve para este componente

- La descripción primaria del flujo (autorización, captura, compensación y liquidación) con diagrama de Visa, Mastercard, BIS/CPMI o la Fed. La Fed (regii-about) no define ni describe el flujo. El BIS/CPMI no apareció en la búsqueda (solo el WP 1259, que cita otros trabajos con diagramas). Lo que sé de captura y liquidación es conocimiento general mío, sin URL: no debe entrar a la nota como afirmación sin otra fuente.
- Las definiciones de adquirente, procesador y agregador/facilitador de pagos (payfac) de una fuente primaria (Visa/Mastercard o el glosario del BIS). Sin fuente.
- Fiserv en Argentina: no lo busqué.

### Recurso canónico propuesto

- **Para el flujo y los roles:** el glosario y las figuras de los informes del CPMI-BIS sobre pagos minoristas (el "Red Book"), sección de tarjetas. No lo verifiqué: hay que localizar la edición vigente y abrirla antes de recomendarla. Alternativa a verificar: el glosario de la Reserva Federal o del BCE.
- **Para Argentina:** el texto ordenado `t-snp-psp` del BCRA y la A 6885 completa (https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6885.pdf): leer secciones 1.1.1 a 1.1.5 (quién es PSP y quién no puede serlo) y la Sección 3 (condiciones para funcionar, que no leí).

---

## 2. costo-de-cobrar

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca | Fecha |
|---|---|---|---|---|---|---|---|---|---|
| 2.1 | Reglamento (UE) 2015/751, EUR-Lex | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R0751 | primaria (norma) | 3 | 3 | 1 | 3 | [L*] | vigente desde 2015 |
| 2.2 | Fed, interchange promedio Reg. II | https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm | primaria | 3 | 2 | 2 | 3 | [L*] | datos 2024 |
| 2.3 | Ley 25.065, texto en argentina.gob.ar ("texto", versión original de 1998) | https://www.argentina.gob.ar/normativa/nacional/ley-25065-1998-55556/texto | primaria (norma) | 3 | 3 | 1 | 2 | [L*] | 1998 |
| 2.4 | Ley 25.065, página "actualización" con antecedentes normativos | https://www.argentina.gob.ar/normativa/nacional/ley-25065-1998-55556/actualizacion | primaria | 3 | 2 | 1 | 2 | [L*] | consultada 2026-11-22 |
| 2.5 | DNU 70/2023, texto en argentina.gob.ar | https://www.argentina.gob.ar/normativa/nacional/decreto-70-2023-395521/texto | primaria (norma) | 3 | 3 | 1 | 3 | [L*] (leí 100.000 de 252.729 caracteres) | B.O. 21/12/2023 |
| 2.6 | La Nación, nota sobre el DNU y tarjetas | https://www.lanacion.com.ar/economia/tarjetas-de-credito-que-pasa-cuando-no-se-paga-y-otros-detalles-del-nuevo-decreto-nid21122023/ | secundaria (prensa) | 2 | 1 | 2 | 1 | [L*] | 21/12/2023 (por la URL) |
| 2.7 | Ámbito, nota sobre el DNU y tarjetas | https://www.ambito.com/finanzas/tarjetas-credito-que-cambios-introduce-el-dnu-n5904402 | secundaria (prensa) | 2 | 1 | 1 | 1 | [L*] | fecha no visible |
| 2.8 | BCRA, página Transferencias 3.0 (costos de pagos con transferencia) | https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ | primaria | 3 | 1 | 1 | 3 | [L*] | sin fecha |
| 2.9 | Stripe docs (disputas), costo de la disputa | https://docs.stripe.com/disputes/how-disputes-work | primaria de empresa | 2 | 2 | 1 | 2 | [L*] | 2026-11-22 |

### Afirmaciones

**Interchange en la UE.** El Reglamento (UE) 2015/751 prohíbe pedir o cobrar una tasa de intercambio por transacción de más de 0,2 % del valor para tarjetas de débito de consumo (art. 3.1) y de más de 0,3 % para tarjetas de crédito de consumo (art. 4); los Estados pueden fijar topes menores para operaciones nacionales. Aplica desde el 9/12/2015 en esos artículos (art. 18). Además cuenta como interchange cualquier remuneración con efecto equivalente (art. 5), exige separar esquema y procesamiento (art. 7) y obliga al adquirente a ofrecer cargos desglosados por categoría y marca salvo pedido escrito del comercio (art. 9). https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R0751 [L*]. Una sola fuente primaria; es una norma, por lo tanto no hace falta una segunda para su contenido.

**Interchange en EE. UU. (para comparar).** El promedio de todas las redes en 2024 fue US$ 0,34 por transacción, 0,73 % del valor medio (US$ 46,32); el tope para emisores cubiertos es «$0.21 plus 0.05 percent multiplied by the value of the transaction», más un ajuste de US$ 0,01 por prevención de fraude; el 39,3 % de las transacciones liquidadas en 2024 eran de emisores exentos (activos menores a US$ 10.000 millones) y el 60,7 % cubiertas. https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm [L*]. Aplica al débito.

**Qué dice la Ley 25.065 y qué cambió (Argentina).**
- El texto original (1998) del art. 15 limitaba lo que el emisor podía fijar: aranceles que no difieran en más de tres puntos entre comercios del rubro y descuentos no superiores al 5 % sobre las liquidaciones del proveedor. https://www.argentina.gob.ar/normativa/nacional/ley-25065-1998-55556/texto [L*]
- La página de antecedentes lista las normas que tocaron la ley: Ley 26.010 (B.O. 11/1/2005) sustituyó el art. 15; Decreto 1387/2001 modificó su tercer párrafo; Decreto 70/2023 (B.O. 21/12/2023) derogó varios artículos y modificó otros, entre ellos el 15. https://www.argentina.gob.ar/normativa/nacional/ley-25065-1998-55556/actualizacion [L*]
- El texto actual del art. 15, tal como lo muestra esa página, obliga a la emisora a dar a conocer al público «la tasa de financiación aplicada al sistema de Tarjeta de Crédito»; no habla de aranceles a comercios. El DNU 70/2023, art. 19, es el que sustituye el art. 15 con ese contenido. https://www.argentina.gob.ar/normativa/nacional/decreto-70-2023-395521/texto [L*]
- Los topes anteriores, según prensa: 3 % para crédito y 1,5 % para débito (La Nación: el emisor no podía aplicar descuentos «superiores a un 3 % sobre las liquidaciones presentadas por el proveedor»; para débito, máximo de 1,5 % y acreditación de ventas en hasta tres días hábiles). Según La Nación «esos límites fueron desregulados» y queda sujeto a negociación entre comercios y tarjeteros; Ámbito dice que el DNU «elimina el tope de tasa que se le cobra a comercios». https://www.lanacion.com.ar/economia/tarjetas-de-credito-que-pasa-cuando-no-se-paga-y-otros-detalles-del-nuevo-decreto-nid21122023/ y https://www.ambito.com/finanzas/tarjetas-credito-que-cambios-introduce-el-dnu-n5904402 [L*]. **Dos fuentes de prensa que no se contradicen, más una primaria (la del DNU) cuyo art. 19 es coherente con ellas.** Pero las cifras 3 % y 1,5 % no las vi en el texto de la Ley 26.010 (no lo abrí): quedan afirmadas solo por prensa.
- El DNU 70/2023 también derogó los arts. 5, 7, 8, 9, 17, 32, 35, 53 y 54 de la Ley 25.065 (art. 14 del DNU) y sustituyó el art. 38, sobre el contrato tipo con el comercio, que según la herramienta incluye entre sus contenidos mínimos «Topes máximos por operación de la tarjeta de que se trate» y «Determinación del tipo y monto de las comisiones, intereses y cargos administrativos» (art. 23 del DNU). Esa lectura es de la herramienta sobre el texto y conviene releerla. https://www.argentina.gob.ar/normativa/nacional/decreto-70-2023-395521/texto [L*]

**Costo de cobrar por transferencia (Argentina).** Los pagos con transferencia son «irrevocables»; el comprador no paga comisión; los comercios pagan «entre 6 y 8 por mil más IVA». https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ [L*] (sin fecha en la página, volátil). Es la única cifra argentina de costo por medio que pude citar de una fuente primaria.

**Cargos por disputa.** Un agregador debita el monto disputado más una tarifa de disputa, no reembolsable salvo en México; si el comercio contesta, se suma una tarifa por contestar (devuelta si gana). https://docs.stripe.com/disputes/how-disputes-work [L*]. Montos concretos: ver el enlace de tarifas en esa página, no los abrí.

### Hueco central

No obtuve ninguna tasa de descuento (MDR) argentina vigente ni los plazos de acreditación de una fuente primaria o fuerte: Mercado Pago (403), Tiendanube y Payway no se pudieron leer, y no hay búsqueda disponible. Tampoco obtuve cómo cobra un agregador "todo junto" (tarifa única que incluye interchange, red y margen) de una fuente primaria; el art. 9 del Reglamento UE (cargos desglosados vs. mezclados) es la mejor referencia conceptual que tengo, pero no habla de Argentina. Tampoco verifiqué si el DNU 70/2023 sigue en vigor en su capítulo de tarjetas tras el tratamiento parlamentario; hay proyectos de ley de 2024 y 2025 para volver a topear (referenciados por el buscador, 0641-D-2024 y 0185-D-2025 en hcdn.gob.ar, que no pude abrir) lo que sugiere que el cambio rige, pero no lo confirmé.

### Recurso canónico propuesto

- **Para el mecanismo:** el Reglamento (UE) 2015/751, arts. 3, 4, 5, 7 y 9 (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R0751). Es corto, define los tres precios que se suman (interchange, tarifa de la red, margen del adquirente) y muestra qué regular. Fijarse en la diferencia entre tope y cargo desglosado.
- **Para Argentina:** el DNU 70/2023, arts. 14, 19 y 23 junto con la historia del art. 15 en la página de "actualización" de la ley. Leer el texto de la Ley 26.010 para confirmar el 3 %/1,5 %. Para el costo por transferencia, la página del BCRA de Transferencias 3.0.

---

## 3. fraude-y-contracargos

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca | Fecha |
|---|---|---|---|---|---|---|---|---|---|
| 3.1 | EBA/ECB, *2025 Report on Payment Fraud* (EBA/REP/2025/40) | https://www.ecb.europa.eu/press/intro/publications/pdf/ecb.ebaecb202512.en.pdf | primaria | 3 | 3 | 2 | 3 | [L] | dic. 2025, datos 2022-2024 |
| 3.2 | ECB, informe de fraude con tarjetas SEPA (datos 2021) | https://www.ecb.europa.eu/press/pr/date/2023/html/ecb.pr230526~f09bc3c664.en.html (no leído) | primaria | 3 | ? | ? | 1 (reemplazado por 3.1) | [S] | mayo 2023 |
| 3.3 | Stripe docs, cómo funcionan las disputas | https://docs.stripe.com/disputes/how-disputes-work | primaria de empresa | 2 | 3 | 2 | 2 | [L*] | 2026-11-22 |
| 3.4 | Stripe docs, 3D Secure: flujo y cambio de responsabilidad | https://docs.stripe.com/payments/3d-secure/authentication-flow | primaria de empresa | 2 | 3 | 2 | 2 | [L*] (leído completo) | 2026-11-22 |
| 3.5 | Stripe docs, categorías y códigos de motivo | https://docs.stripe.com/disputes/categories | primaria de empresa (transcribe los códigos de Visa, Mastercard y Amex) | 2 | 3 | 3 | 2 | [L*] (leí Visa; Mastercard solo el principio) | 2026-11-22 |
| 3.6 | EMVCo, 3-D Secure | https://www.emvco.com/emv-technologies/3-d-secure/ | primaria (dueño de la especificación) | 3 | 1 | 1 | 3 | [L*] | consultada 2026-11-22 |
| 3.7 | Ley 25.065, arts. 26-30 (texto original) | https://www.argentina.gob.ar/normativa/nacional/ley-25065-1998-55556/texto | primaria (norma) | 3 | 3 | 1 | 3 | [L*] | 1998, ver nota de DNU |

### Afirmaciones

**Tasas de fraude publicadas (UE/EEE, datos 2024).** El informe conjunto EBA/ECB de diciembre de 2025 estima en 4.200 millones de euros el fraude de pagos en el EEE en 2024; el valor de las transacciones de tarjeta fraudulentas con tarjetas emitidas en la UE/EEE fue de 1.300 millones de euros, con una tasa de fraude de 0,033 % (por valor); por cantidad, unas 17,06 millones de transacciones fraudulentas sobre unas 111,05 mil millones, es decir 0,015 %. https://www.ecb.europa.eu/press/intro/publications/pdf/ecb.ebaecb202512.en.pdf [L], resumen ejecutivo y capítulo 2. Las pérdidas declaradas por tarjetas fueron de 1.329 millones de euros en 2024, +29 % interanual (cap. 5).
- Para una tasa de fraude de tarjetas con datos 2021: 0,028 % del valor de pagos con tarjetas SEPA, 1.530 millones de euros sobre 5,40 billones, y 63 % del valor fraudulento fue transfronterizo. Es el último informe separado del BCE sobre tarjetas, citado por el buscador, no leído. https://www.ecb.europa.eu/press/pr/date/2023/html/ecb.pr230526~f09bc3c664.en.html [S].
- **Nota de método:** el BCE ya no publica un "card fraud report" aparte; desde el informe de agosto de 2024 es un informe conjunto con la EBA, desde la perspectiva del emisor (tarjetas emitidas en la UE/EEE, adquiridas en cualquier parte del mundo). Declararlo cuando la nota cite «el informe del BCE».

**Dónde se da el fraude con tarjeta.** El fraude remoto (sin tarjeta presente) fue alrededor del 83 % del fraude con tarjeta en 2024, aunque los pagos remotos eran solo ~28 % del valor y ~18 % del número de pagos con tarjeta (cap. 3). Dentro del remoto, el robo de datos de la tarjeta explicó más del 56 % del valor (~65 % en cantidad). Alrededor del 70 % del fraude con tarjetas es transfronterizo, y un 30 % del valor fraudulento en 2024 fue transfronterizo fuera del EEE; las tasas de fraude con contraparte fuera del EEE fueron unas 17 veces las nacionales, donde la autenticación fuerte puede no ser exigible (cap. 6 y resumen). Mismo URL [L].

**Autenticación fuerte (SCA) y efecto.** Solo el 40 % de las operaciones de tarjeta iniciadas electrónicamente se autenticaron con SCA en 2024 (por el efecto de contactless y de las exenciones), y «SCA-authenticated transactions showed lower fraud rates than non-SCA transactions, especially for card payments». Mismo URL [L].

**Quién pierde (según el informe).** En 2024 los usuarios del servicio de pago (titulares) cargaron con el 38 % de las pérdidas de tarjeta (53 % en débitos directos y retiros, 26 % en dinero electrónico, 85 % en transferencias); por país varía de 12 % a más de 87 %. El informe lo atribuye a regímenes de responsabilidad distintos. Mismo URL [L]. Importante: esto es pérdida por tarjeta emitida en la UE/EEE, es decir la perspectiva del emisor y del titular. No dice qué parte recae sobre el comercio.

**Qué es un contracargo y cómo corre.** Según Stripe: el titular disputa ante su emisor; el emisor inicia un contracargo, la red debita al adquirente/agregador y este debita al comercio el monto más una tarifa; el comercio tiene normalmente 7-21 días para responder (según la red); el emisor decide en 60-75 días; el ciclo completo toma 2-3 meses; las redes permiten iniciar la disputa normalmente dentro de 120 días desde el pago (más en viajes o eventos). Alrededor del 40 % de las alertas tempranas de fraude de Visa y Mastercard terminan en disputa por fraude. https://docs.stripe.com/disputes/how-disputes-work [L*]. Es una fuente de empresa, no el reglamento de Visa o Mastercard (que no obtuve); las cifras son de Stripe y valen para esa plataforma.

**Códigos de motivo (Visa, según la transcripción de Stripe).** Fraude: 10.1 y 10.2 (cambio de responsabilidad EMV), 10.3 (otro fraude con tarjeta presente), 10.4 (otro fraude, tarjeta ausente: el típico del e-commerce), 10.5 (programa de monitoreo de fraude); no recibido: 13.1; no es como se describió o defectuoso: 13.3; recurrente cancelada: 13.2; crédito no procesado: 13.6; duplicado: 12.6.1. Mastercard usa 4860 (crédito no procesado) y 4834 (diferencias de monto, duplicado), entre otros (no leí el resto). https://docs.stripe.com/disputes/categories [L*]. Para el diccionario oficial hay que ir a los reglamentos de las marcas: hueco.

**3-D Secure y cambio de responsabilidad.**
- EMVCo: «EMV 3-D Secure (EMV 3DS) helps payment card issuers and merchants around the world prevent card-not-present (CNP) fraud»; recomienda v2.2 o superior. La página no dice nada de responsabilidad. https://www.emvco.com/emv-technologies/3-d-secure/ [L*]
- Stripe: el cambio de responsabilidad aplica típicamente a pagos autenticados con 3DS: si el titular lo disputa como fraude, «the liability typically shifts from you to the card issuer». Y lo advierte: «Successful 3DS authentication doesn't guarantee liability shift»; no corre si hay un nivel de fraude excesivo y el comercio está en un programa de monitoreo de Visa; algunas industrias están exentas (Visa no lo da a giros de transferencias, dinero no fiduciario o tarjetas de valor almacenado); el cambio tampoco cubre disputas por «producto no recibido». https://docs.stripe.com/payments/3d-secure/authentication-flow [L*]
- El texto de las reglas de Visa/Mastercard sobre el cambio de responsabilidad no se obtuvo. La afirmación queda en una sola fuente de empresa (Stripe), con conflicto de interés ambiguo: le conviene vender 3DS pero la fuente es cautelosa, no promete.

**Argentina: contracargo y desconocimiento.** La Ley 25.065 (texto original) no usa «contracargo»; habla de «cuestionar» la liquidación: el titular tiene 30 días desde que la recibe, por nota simple (art. 26); el emisor acusa recibo en 7 días y tiene 15 para corregir o explicar, 60 si es operación en el exterior (art. 27); durante el trámite no puede impedir el uso de la tarjeta dentro del límite ni exigir más que el mínimo sobre lo no cuestionado (art. 28); el titular tiene 7 días para aceptar o no las explicaciones y el emisor 10 días hábiles para resolver (art. 29). https://www.argentina.gob.ar/normativa/nacional/ley-25065-1998-55556/texto [L*]. Esto es la relación titular-emisor. La relación emisor-comercio (el contracargo propiamente dicho, con sus plazos y códigos) se rige por contratos y reglas de las marcas. El DNU 70/2023 derogó arts. 5, 7, 8, 9, 17, 32, 35, 53 y 54 y modificó otros; no revisé si cambió los arts. 26-30. Hueco.

### Hueco central

Cifras de contracargos o fraude en e-commerce de Argentina o LatAm de una fuente primaria (BCRA, bancos, Visa/Mastercard): no las hallé. La tasa de contracargos que activa los programas de monitoreo (Visa/Mastercard) tampoco. No encontré a Baymard ni a los estudios académicos relevantes; no son de este componente.

### Recurso canónico propuesto

- **Para cifras:** *2025 Report on Payment Fraud* (EBA/ECB, diciembre de 2025): capítulos 2 (niveles de fraude), 4 (efecto de SCA) y 5 (quién pierde). Fijarse en que los datos son por emisor, en que el valor y el número tienen tasas distintas (0,033 % vs 0,015 %) y en que no cubre Latinoamérica.
- **Para el mecanismo del contracargo:** el reglamento de disputas de Visa (Visa Core Rules and Visa Product and Service Rules) y la guía de contracargos de Mastercard: no los abrí. Hasta tenerlos, la mejor fuente operativa abierta es https://docs.stripe.com/disputes/how-disputes-work, con sus límites.
- **Para 3DS:** el sitio de EMVCo (qué es) y las reglas de la marca (quién carga con el fraude).

---

## 4. cuotas-y-medios-locales

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca | Fecha |
|---|---|---|---|---|---|---|---|---|---|
| 4.1 | BCB, *Relatório de Gestão do Pix 2023-2025* | https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf | primaria | 3 | 3 | 2 | 3 | [L] (texto completo extraído; leí índice, estadísticas clave, MED y Pix Automático) | datos a dic. 2025 |
| 4.2 | EBANX, comunicado sobre billeteras digitales y PCMI | https://business.ebanx.com/en/press-room/press-releases/digital-wallets-become-the-fastest-growing-payment-method-in-brazilian-e-commerce-in-2025-pcmi/ebanx-reports | primaria de empresa (vende pagos en Brasil: conflicto de interés) | 2 | 1 | 1 | 2 | [L*] | 15/1/2026 |
| 4.3 | EBANX vía PRNewswire/AAP, comunicado sobre Pix y UPI | https://www.aap.com.au/aapreleases/cision20260211ae85574 | primaria de empresa (mismo origen que 4.2, otro texto) | 2 | 1 | 1 | 1 (mismo dato que 4.2) | [L*] | 12/2/2026 |
| 4.4 | EBANX, comunicado "Pix to surpass credit cards..." | https://business.ebanx.com/en/press-room/press-releases/pix-to-surpass-credit-cards-in-digital-commerce-in-brazil-by-next-year-ebanx-analyzes-outcomes | primaria de empresa | 2 | 1 | 1 | 2 | [L*] | 10/9/2024 |
| 4.5 | EBANX, *Beyond Borders 2025* (página resumen) | https://ebanx.com/en/beyond-borders-2025/ | primaria de empresa | 2 | 1 | 1 | 1 | [L*] (no da porcentajes) | sin año de datos |
| 4.6 | Worldpay, *Global Payments Report* 2026 (vía buscador) | https://worldpay.com/global-payments-report-2025 (la edición 2025; la 2026 no tenía URL propia en los resultados) | primaria de empresa (procesadora) | 2 | ? | ? | 2 (otra metodología que PCMI, pero no leída) | [S] | edición 2026, datos 2025 |
| 4.7 | BCRA, página Transferencias 3.0 | https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ | primaria | 3 | 2 | 1 | 3 | [L*] | sin fecha |
| 4.8 | MODO, home | https://www.modo.com.ar/ | primaria de empresa | 1 | 1 | 1 | 2 | [L*] | sin fecha |
| 4.9 | Wikipedia, Ahora 12 | https://es.wikipedia.org/wiki/Ahora_12 | secundaria | 1 | 1 | 1 | 1 | [L*] | consultada 2026-11-22 |

### Afirmaciones

**Pix: cifras del Banco Central do Brasil.** En 2025 el número de transacciones creció 25,7 % respecto de 2024 hasta casi 80 mil millones (79,8), y el volumen financiero creció 33,8 % y superó los R$ 35 billones; récord de 313.339.328 transacciones en un día (5/12/2025); en diciembre de 2025 se movieron R$ 3,7 billones en 7,8 mil millones de transacciones, con 148 millones de personas físicas y 12 millones de empresas que enviaron o recibieron un Pix y más de 920 millones de claves registradas. https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf [L]. Cifras de récords posteriores (319,7 millones en un día, 2026) son de prensa [S]: https://www.folhape.com.br/economia/pix-bate-novo-recorde-de-transacoes-em-um-dia-3197-milhoes-de/523244/.

**Pix: reglas y productos que importan al comercio.**
- Pix Automático, para pagos recurrentes por débito autorizado: entró en funcionamiento el 16 de junio de 2025 (informe BCB [L]).
- MED (Mecanismo Especial de Devolução): funciona desde 2021; permite bloquear fondos y pedir la devolución en casos comprobados de golpes, fraudes o crímenes; en octubre de 2025 se implementó el autoservicio del MED (el «botón de contestación») (informe BCB [L]). Es el equivalente funcional más cercano a un contracargo: lo inicia la víctima de un fraude y no hay derecho a disputa por «producto no recibido»; no verifiqué las reglas para ese caso. Hueco.
- «Pix Parcelado» no aparece en el texto completo del informe 2023-2025. No encontré su estado. Hueco.
- Distribución por valor: en 2025, el 59 % de las transacciones fueron de hasta R$ 60 y solo el 8 % mayores de R$ 500 (informe BCB, por lectura de texto con layout; conviene revisarlo contra el gráfico). Con ese ancho de gráficos mi lectura del párrafo es parcial; usarlo con cuidado.

**Pix en el e-commerce de Brasil: la discrepancia 42 % vs 44 %, resuelta.**
- **42 % es el dato medido de 2025; 44 % es la proyección para 2025 publicada en septiembre de 2024.**
  - EBANX, 15/1/2026: «Pix leads Brazilian e-commerce with a 42% share, followed by credit cards at 41%», datos de 2025, atribuidos a PCMI (Payments and Commerce Market Intelligence). https://business.ebanx.com/en/press-room/press-releases/digital-wallets-become-the-fastest-growing-payment-method-in-brazilian-e-commerce-in-2025-pcmi/ebanx-reports [L*]
  - EBANX, 12/2/2026: «Last year, 42% of the total value of purchases in the country were paid with Pix, edging out cards at 41%» (por valor). https://www.aap.com.au/aapreleases/cision20260211ae85574 [L*]
  - EBANX, 10/9/2024: «The projection for 2025 estimates that Pix will account for 44% of all value transacted in online purchases in Brazil», con tarjetas en 41 %: una proyección, por valor. https://business.ebanx.com/en/press-room/press-releases/pix-to-surpass-credit-cards-in-digital-commerce-in-brazil-by-next-year-ebanx-analyzes-outcomes [L*]
- Los tres textos son del mismo emisor (EBANX) y de la misma base (PCMI): es **una sola fuente**, no tres. El 42 % lo corrobora, con otra metodología, el resumen de la edición 2026 del *Global Payments Report* de Worldpay (Pix = 42 % del e-commerce de Brasil en 2025, 34 % en punto de venta) según el buscador, no leído: https://finsidersbrasil.com.br/estudos-e-relatorios/pix-dinheiro-pagamento-global-payments-report/ [S]. Que coincida un 42 % de dos procesadores es una pista, no una confirmación, porque no verifiqué la metodología de ninguna.
- **Lo que quedó sin resolver.** El vistazo habló de «44 % de Pix contra 40 % de tarjetas de crédito». No encontré ese par en ninguna fuente que abrí: lo que existe es 44 % vs 41 % (proyección 2025, septiembre de 2024) y 42 % vs 41 % (medido 2025). El «40 %» puede venir de otra proyección o de otra edición; hueco. Las proyecciones de EBANX para el futuro (45 % en 2026 y 50 % en 2028, o 50 % de transacciones en 2028 contra 36 % de tarjetas) también son proyecciones de la empresa, no datos.
- **Qué mide el 42 %.** Por valor (la nota de PRNewswire lo dice). El comunicado del 15/1/2026 no aclara si es valor o cantidad, ni describe la muestra ni la definición de «e-commerce»; solo la billetera digital tiene una cifra rotulada como volumen (9 % de las transacciones en 2025, +20 % interanual contra +18 % de Pix; Mercado Pago tiene el 40 % del valor de e-commerce de las billeteras). Mismo URL del 15/1/2026 [L*]. La metodología de PCMI: hueco.

**Billeteras y QR en Argentina.** Lo que obtuve de primaria es descriptivo (BCRA y MODO, arriba, sección 1); no hay una cifra de participación de medios de pago en e-commerce argentino en ninguna fuente que abrí. La página *Beyond Borders 2025* de EBANX no da cifras de Argentina (https://ebanx.com/en/beyond-borders-2025/ [L*]).

**Transferencias 3.0: reglas.** Pagos con transferencia irrevocables, sin comisión para el comprador y con 6 a 8 por mil más IVA para el comercio (BCRA, https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ [L*], sin fecha: volátil). La página no da fechas de obligatoriedad ni números de comunicaciones: hueco.

**Cuotas sin interés en Argentina: estado vigente.** No pude establecerlo. Lo único leído: Ahora 12 entró en vigencia en septiembre de 2014; permitía comprar en 12 cuotas sin interés con tarjeta de crédito, y según el artículo los comercios pasaron a pagar un 10 % de financiamiento en lugar de 26 %, con los bancos absorbiendo la diferencia. https://es.wikipedia.org/wiki/Ahora_12 [L*, secundaria]. Sobre Cuota Simple y la vigencia de Ahora 12 en 2026 no hay ninguna fuente leída. Mi recuerdo es que hubo cambios en 2023-2024, pero no tengo fuente y no debe entrar en la nota. Hueco prioritario.

### Recurso canónico propuesto

- **Pix:** el *Relatório de Gestão do Pix 2023-2025* del BCB (https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf): el infográfico de estadísticas de la sección 2 (cifras con serie 2020-2025), 1.1.4 (Pix Automático) y 1.2.1 (MED). Para cifras al día, la página `pix-em-numeros-estatisticas` del BCB y su conjunto de datos abiertos (`dadosabertos.bcb.gov.br/dataset/pix`): no pude leer los datos, solo vi que existen.
- **Participación de medios en e-commerce:** el informe *Beyond Borders* de EBANX con los datos PCMI, siempre citado como «datos de 2025, por valor, fuente de proveedor con interés comercial», junto con el *Global Payments Report* de Worldpay como contraste. Pendiente abrir ambos completos.
- **Argentina:** la página de Transferencias 3.0 del BCRA y los documentos técnicos de pagos con transferencia que enlaza.

---

## Resumen de huecos (lo que falta cerrar)

1. Flujo de una compra con tarjeta (autorización, captura, compensación, liquidación) con diagrama de una fuente primaria (BIS/CPMI Red Book, Visa, Mastercard, Fed). No obtenido.
2. Definiciones primarias de adquirente, procesador, pasarela y agregador/facilitador de pagos. Solo hay la definición del BCRA de PSP y de esquema de pago.
3. Prisma/Payway y Fiserv en Argentina: rol de adquirente y cuota de mercado. Solo la página de Prisma como procesador emisor.
4. Tasa de descuento y plazos de acreditación vigentes en Argentina (Mercado Pago, Payway, Tiendanube): páginas no abiertas (403) y sin búsqueda.
5. Texto de la Ley 26.010 (origen de 3 %/1,5 %), y vigencia actual del DNU 70/2023 en su capítulo de tarjetas. Los topes se afirman solo por prensa.
6. Si hay algún tope o regulación del BCRA vigente sobre aranceles de tarjetas tras el DNU.
7. Cuotas sin interés: Ahora 12, Cuota Simple y su estado y fecha vigente. Sin fuente leída. También cuotas en Brasil (parcelado sem juros) y el estado de Pix Parcelado.
8. Reglas de Visa/Mastercard de contracargos y del cambio de responsabilidad, y los programas de monitoreo con sus umbrales.
9. Cifras de fraude y contracargos para Argentina o Latinoamérica.
10. Metodología de PCMI (muestra, definición de e-commerce) y el origen del par 44 %/40 %; verificar en Worldpay GPR 2026 el 42 % de Pix en Brasil.
11. Participación de medios de pago en el e-commerce argentino (CACE, PCMI) y cifras de Transferencias 3.0/QR/MODO.
12. Normativa de PSP vigente después de A 6885 (A 8284/8285 de 2025): no leída.
13. Mercado Pago en el registro de PSP del BCRA: no verificado.
