# Envíos en Argentina: transportistas, tarifas y cotización de un envío tipo

Fecha de consulta: 2026-11-22. Método: lector con navegador real (Playwright), WebFetch, WebSearch (unas 16 búsquedas, cupo no agotado) y un script propio que completó el cotizador público de Andreani sin cuenta. Los PDF oficiales (OCA, Correo Argentino) se bajaron con curl y se leyeron con pdftotext o como imagen. Nada se cotizó con cuenta. No se recomienda nada.

Envío tipo: 1 kg reales, 20x15x10 cm (peso volumétrico 0,6 kg con divisor 5000, inferencia: el real manda), valor declarado $30.000, origen CABA (CP 1414). Destinos: Córdoba capital (5000), Villa Dolores (5870), Esquel (9200).

## Respuesta corta

- **Cotizado en vivo, público, sin cuenta (Andreani, con IVA incluido):** 1 kg desde CABA cuesta $11.449,61 a sucursal y $13.890,41 a domicilio hasta Córdoba capital; $11.449,61 / $15.919,52 hasta el CP 5870; $13.736,33 / $15.964,70 hasta el CP 9200. Más el 1% del valor declarado ($300 si se declara $30.000). Fuente A, dato 3, [L].
- **Lista de precios pública de OCA (vigencia 28/09/2026, con IVA):** 0 a 1 kg, entrega en sucursal $13.865 a $20.034 según zona; a domicilio $17.426 a $24.274; express a domicilio $25.217 a $35.807. El PDF no dice qué zona es cada destino. Fuente A, dato 3, [L].
- **Correo Argentino, mostrador (Encomienda Correo Clásica, página oficial sin fecha):** hasta 1 kg, $19.500 regional y $26.400 nacional, solo a domicilio, 3 a 6 días. La Prioritaria: $31.100 / $38.900, 1 a 3 días hábiles. Fuente A, dato 3, [L]. La página no dice si incluye IVA.
- **Correo Argentino Paq.ar (la tarifa e-commerce):** no hay tarifa 2026 pública sin cuenta. El único PDF público de precios (Monotributista y Consumidor Final) dice "rigen desde Febrero de 2023". Es un hueco para el precio actual.
- **Envío Nube (Tiendanube):** la página de tarifas no tiene tarifario ni enlace a uno. Publica descuentos (5% adicional sobre tarifas estándar de Correo Argentino y Andreani; 10% adicional en la misma ciudad hasta 10 kg). No se puede calcular el envío tipo por esta vía con fuente primaria. Fuente A, [L], hueco en el precio.
- **Mercado Libre, lo que paga el vendedor por 1 kg con envío gratis (producto de menos de $33.000, tabla vigente desde 1/9/2026):** $10.906 con reputación verde o MercadoLíder, $12.464 amarilla, $15.580 naranja o roja. Viene de un blog que cita la ayuda oficial (que dio 403). Fuente C, dato 3, [S].
- **Umbral de envío gratis:** la baja de $33.000 a $15.000 es real, pero es del beneficio Meli+ para el comprador, y Mercado Libre dice que lo absorbe. No es un cambio en lo que paga el vendedor. Rige desde el lunes 14/9/2026 (inferencia desde "desde el próximo lunes" en una nota del jueves 10/9). Fuente B, dato 2, [L] y [S].
- **Full (almacenamiento, stock antiguo):** no hay fuente primaria legible. Un blog dice 120 días corridos; otra fuente dice 90. Hueco.

## 1. Tabla del envío tipo (1 kg, valor declarado $30.000, origen CABA)

| Canal / servicio | Destino | Precio | ¿IVA? | Plazo | Fuente |
|---|---|---|---|---|---|
| Andreani, paquetería (cotizador público) | Córdoba 5000, sucursal | $11.449,61 | Sí, "Precio con IVA incluido" | No lo muestra el cotizador; 2 a 3 días hábiles según ayuda de Tiendanube (secundaria) | andreani.com/?tab=cotizar-envio, consultado 2026-11-22 |
| Andreani | Córdoba 5000, domicilio | $13.890,41 | Sí | idem | idem |
| Andreani | CP 5870, sucursal | $11.449,61 | Sí | idem | idem |
| Andreani | CP 5870, domicilio | $15.919,52 | Sí | idem | idem |
| Andreani | CP 9200, sucursal | $13.736,33 | Sí | idem | idem |
| Andreani | CP 9200, domicilio | $15.964,70 | Sí | idem | idem |
| OCA, entrega en sucursal | Local / Regional / Nac. 1 / Nac. 2 | $13.865 / $14.395 / $19.356 / $20.034 | Sí ("precios con IVA") | no figura en el PDF | oca.com.ar/Content/preciosPDF/precios.pdf, vigencia 28/09/2026 |
| OCA, entrega en domicilio | idem | $17.426 / $17.978 / $23.564 / $24.274 | Sí | idem | idem |
| OCA, express a domicilio | idem | $25.217 / $27.602 / $31.355 / $35.807 | Sí | idem | idem |
| Correo Argentino, Encomienda Clásica (mostrador) | Regional / Nacional | $19.500 / $26.400 | No dice | 3 a 6 días | correoargentino.com.ar/servicios/paqueteria/encomienda-correo-clasica |
| Correo Argentino, Encomienda Prioritaria (mostrador) | Regional / Nacional | $31.100 / $38.900 | No dice | 1 a 3 días hábiles | .../encomienda-correo-prioritaria |
| Correo Argentino, Paq.ar Clásico / Expreso | los tres | sin tarifa pública vigente | | Clásico 2 a 5 días hábiles; Expreso 1 a 3 | correoargentino.com.ar/MiCorreo/public/infopaqarpymes |
| Envío Nube (Correo Argentino / Andreani) | los tres | sin tarifario público | | Correo Clásico 2 a 5; Expreso 1 a 3; Andreani 2 a 3 días hábiles | ayuda.tiendanube.com/es_AR/envio-nube/cuales-son-los-tiempos-de-envio-de-envio-nube |
| Vía Cargo, Cruz del Sur, Urbano | los tres | no se encontró cotizador público ni tarifa | | | hueco |

Notas de lectura de la tabla:
- Andreani: el script puso 1414 como origen y el CP de destino. Para 5870 y 9200 el autocompletado eligió la primera localidad del CP ("San Roque" y "La Cancha"), no Villa Dolores ni Esquel. Los precios dependen del CP (inferencia: el cotizador pide "CP o Localidad" y devuelve un solo precio por CP), pero no se verificó que otra localidad del mismo CP dé lo mismo. El cotizador no pidió valor declarado; la nota al pie dice "se adicionará un 1% del valor que declares". Su validación interna acepta valor declarado de $30.000 a $2.500.000 (respuesta de `/api/cotizador/validations`).
- Andreani, paquete con dimensiones y peso ingresados: alto 10, ancho 15, largo 20, 1000 g.
- OCA: el PDF dice que el precio "se tarifa de acuerdo a su peso en kg y distancia según código postal de origen y destino". No define Local, Regional, Nacional 1 ni Nacional 2. **Supuesto**: Córdoba capital cae en una de las dos nacionales y Esquel en la más lejana; no se verificó. OCA, seguro: "Comisión: 2% s/valor declarado", con "Monto mínimo: $32.810" y "máximo: $100.000" (el envío tipo, de $30.000, queda debajo del mínimo si el mínimo es de valor declarado; lectura literal, ambigua).
- Correo Argentino, Encomienda Clásica: "Regional" y "Nacional" no se definen en la página. Valor declarado: "De $ 20.000,01 a $ 200.000,00: 3%", o sea $900 sobre $30.000 (aritmética propia). La página no publica fecha de vigencia de la tabla.
- Cada transportista pone un precio distinto a un servicio que no es el mismo: Andreani cotiza "paquetería" con red de sucursales y puntos; Correo Clásica es solo a domicilio y de mostrador.

## 2. Fuentes y afirmaciones por transportista

### Andreani

| URL | Tipo | Calificación | Marca |
|---|---|---|---|
| https://www.andreani.com/?tab=cotizar-envio y https://www.andreani.com/api/cotizador/prices | Cotizador oficial sin cuenta | A, dato 3 | [L] |
| https://www.andreani.com/precios-productos | Tarifas oficiales de mostrador (postales, encomiendas) | A, dato 3 | [L] |
| https://ayuda.tiendanube.com/es_AR/envio-nube/cuales-son-los-tiempos-de-envio-de-envio-nube | Ayuda de Tiendanube (plazos) | B, dato 3 | [S] |

- El cotizador es público y no pide cuenta ("Creá tu cuenta profesional y accedé a descuentos y beneficios exclusivos" es la oferta para negocios). Cotiza "Paquetería: hasta 50 kg".
- Distingue público y empresa: el cotizador público da una tarifa y la cuenta profesional ofrece "descuentos y beneficios exclusivos" sin cifras. La tarifa e-commerce o de contrato no es pública.
- Precios de mostrador (https://www.andreani.com/precios-productos, 2026-11-22): Bolsa Andreani Pack $29.500; Bolsa Pack 24 hs $36.500; Andreani Encomienda $34.100; Caja Pack 2 kg $31.000, 3 kg $33.000, 5 kg $36.000, 10 kg $40.500, 20 kg $56.500. Son productos de mostrador con embalaje o prepago, no comparables uno a uno con el cotizador (inferencia). Nota de la página: "Tarifa válida para todo el territorio nacional excepto Tierra del Fuego".
- Plazo: 2 a 3 días hábiles, 2 a 3 intentos, 5 días hábiles de guarda en sucursal (Tiendanube cita el FAQ de Andreani). Otra fuente (directorio de seguimiento, sin marcar como oficial) dice 3 a 5 días hábiles. No se leyó la página oficial de plazos (la búsqueda no la devolvió; la ficha de preguntas frecuentes de andreani.com cargó pero no mostró plazos).

### OCA

| URL | Tipo | Calificación | Marca |
|---|---|---|---|
| https://www.oca.com.ar/Content/preciosPDF/precios.pdf | Lista oficial, "Vigencia: 28/09/2026, Tarifario: 09/2026" | A, dato 3 | [L] |
| https://www5.oca.com.ar/ocaepak/ | Plataforma ePak (pide e-mail y contraseña) | A | [L], sin datos |
| https://developers.oca.com.ar/epakenglish.html | Documentación de la API | A | [S]: cotizar por servicio web requiere usuario ePak |

- La lista pública es la de paquetería de mostrador/sucursales. Tabla completa, con IVA, para 0 a 1 kg:
  - Entrega en sucursal: Local $13.865, Regional $14.395, Nacional 1 $19.356, Nacional 2 $20.034.
  - Entrega en domicilio: $17.426, $17.978, $23.564, $24.274.
  - Express a domicilio: $25.217, $27.602, $31.355, $35.807.
  - 1 a 2 kg, sucursal: $14.395, $16.207, $19.780, $21.751. 2 a 5 kg, sucursal: $14.872, $17.988, $20.204, $23.437. Excedente por kg a partir de 25 kg: $678 a $2.067.
- "NOTA: No se comercializarán envíos bajo las modalidades de entrega en sucursal y entrega en domicilio hacia la provincia de Tierra del Fuego."
- El cotizador de oca.com.ar no se encontró como página pública; ePak (para e-commerce) exige cuenta. La tarifa de contrato no es pública.
- Packaging a la venta: Caja N° 1 $2.215 (hasta 1 kg), Caja N° 2 $3.456, Bolsa N° 1 $1.378 (hasta 2 kg).
- Plazo: el PDF no lo trae. Un blog de Tiendanube (resumen del buscador, [S]) habla de 2 a 4 días hábiles para sucursal y domicilio y 1 a 2 para express. No leído entero: dato 6.

### Correo Argentino

| URL | Tipo | Calificación | Marca |
|---|---|---|---|
| https://www.correoargentino.com.ar/servicios/paqueteria/encomienda-correo-clasica | Página oficial de producto | A, dato 3 (sin fecha de vigencia) | [L] |
| https://www.correoargentino.com.ar/servicios/paqueteria/encomienda-correo-prioritaria | Idem | A | [L] |
| https://www.correoargentino.com.ar/MiCorreo/public/infopaqarpymes | Atributos y términos de Paq.ar | A | [L] |
| https://www.correoargentino.com.ar/MiCorreo/public/files/lista-de-precios-CF-MiCorreo.pdf | PDF de precios Paq.ar, Monotributista y Consumidor Final | A, pero vencido | [L] (tablas leídas en imagen) |
| https://ayuda.tiendanube.com/es_AR/correo-argentino/preguntas-frecuentes-sobre-correo-argentino | Ayuda de Tiendanube | B | [S] |
| https://www.tiendanube.com/blog/como-enviar-un-paquete-por-correo-argentino/ (actualizado 09/10/2026) | Blog | C | [S] |

- No hay cotizador público sin cuenta: la página pública de MiCorreo ofrece iniciar sesión o registrarse y "Gestionar devolución". El blog de Tiendanube dice: "Para conocer el precio exacto, cargá los datos del envío en MiCorreo y hacé clic en Cotizar".
- El PDF de precios Paq.ar (Monotributista y Consumidor Final) dice: "Los precios rigen desde Febrero de 2023 y pueden sufrir modificaciones sin previo aviso" y "Precios Finales con IVA". Valores de entonces para 1 kg (leídos en imagen a baja resolución): zona 2 a domicilio $1.153,64 y a sucursal $695,01; zona 4 a domicilio $1.266,51 y a sucursal $798,55. Contra los $19.500 de la Clásica 2026 se ve que está vencido: no se usa como precio. La matriz de zonas del mismo PDF ubica Buenos Aires a Córdoba en zona 2 y Buenos Aires a Chubut en zona 4 (lectura de imagen; inferencia con riesgo de error de lectura).
- La página de MiCorreo enlaza además una lista de precios para Responsable Inscripto (`lista-de-precios-PY-MiCorreo.pdf`) que no se pudo bajar (curl devolvió una página HTML en lugar del PDF). Hueco.
- Zonas Paq.ar (Clásico y Expreso): Zona 1 ciudad y alrededores; Zona 2 hasta unos 750 km; Zona 3 de 751 a 1.300 km; Zona 4 desde 1.301 km. Peso máximo real 50 kg (30 en el PDF de 2023). Rangos de peso: 0,5, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40 y 50 kg.
- Plazos oficiales: Clásico "2 a 5 días hábiles según origen y destino"; Expreso "1 a 3 días en todo el país"; Paq.ar Hoy, el mismo día en CABA y GBA con corte a las 12:30. Encomienda Clásica "3 a 6 días" y Prioritaria "1 a 3 días hábiles". Voluminosos suman hasta 48 hs.
- Tarifa al público y tarifa de empresa: la de mostrador es la de las páginas de Encomienda; la de MiCorreo (Paq.ar) es la tarifa para negocios y monotributistas, con otra lista para Responsables Inscriptos. En los términos de Paq.ar: "Las tarifas de los envíos son producto de negociación comercial con el cliente o las establecidas para el servicio". El portal dice "Tenemos el precio más bajo" (afirmación comercial, sin cifra).

### Paq.ar como contrato e-commerce: mínimos y facturación

- Mínimo de envíos: no se encontró ninguno publicado. La ayuda de Tiendanube dice: "cuanto más enviás, menos pagás" (sin cifras) y que en Correo hay una escala de bonificaciones por pick-up en la sección Precios de sus FAQ (sin montos en la ayuda). Esa sección de las FAQ de MiCorreo no mostró contenido al leerla con navegador (acordeón sin desplegar): hueco.
- Cómo se paga: sin factura mensual de cuenta corriente publicada. Según Tiendanube (ayuda, [S]): el comerciante paga la etiqueta online, con crédito precargado o al generar la etiqueta, y "el medio de pago es Mercado Pago con todas sus opciones"; los comprobantes están en "Mi Saldo > Movimientos de saldo"; una etiqueta cancelada queda como saldo a favor. Según los términos de Paq.ar, "no se generan gastos sin que el Usuario cargue los datos de facturación".
- IVA: Tiendanube dice que consumidores finales ven la tarifa con IVA incluido y los responsables inscriptos sin IVA, con el IVA "desglosado luego en la factura". Los precios son los mismos.
- Seguro: Tiendanube dice "Por el momento, no ofrece seguro para los envíos" (Paq.ar vía MiCorreo, [S]).
- Diferencias de peso: se re-pesa en sucursal antes de admitir; si el peso real supera lo declarado se paga la diferencia en efectivo o se cancela la preimposición. En el PDF de 2023 el kilo adicional costaba $140 (precio final).
- Retiro a domicilio (pick-up): "tiene un costo adicional" según Tiendanube; disponible de lunes a sábado (sábados solo por la mañana) y no para todos los códigos postales.
- Peso mínimo 0,010 kg y máximo 50 kg; hasta 300 cm sumando lados, ninguno más de 200 cm (Tiendanube e infopaqarpymes coinciden).
- Hueco: el contrato (Condiciones comerciales para empresas, plazos de pago, topes de volumen) no es público. La clasificación "Persona / Pyme / Corporativo" del sitio sugiere tres canales, pero no se leyeron las condiciones de Pyme ni de Corporativo.

## 3. Envío Nube (Tiendanube)

| URL | Tipo | Calificación | Marca |
|---|---|---|---|
| https://ayuda.tiendanube.com/es_AR/envio-nube/tarifas-envio-nube ("Última actualización: 29/10/2026") | Ayuda oficial | A, dato 3 | [L] (además se revisó el HTML: no hay enlace al tarifario) |
| https://www.tiendanube.com/envio-nube | Página comercial | A (promesa) | [L] |
| https://ayuda.tiendanube.com/es_AR/envio-nube/cuales-son-los-tiempos-de-envio-de-envio-nube | Ayuda oficial | A | [S] |

- La ayuda dice: "Accedé a nuestro tarifario para conocer los costos de Envío Nube, con descuentos sobre las tarifas estándar", pero en la página no hay tarifario ni tabla ni enlace (se buscó en el texto renderizado y en el HTML crudo). **Hueco**: el tarifario no está accesible en la página; probablemente vive dentro del panel (inferencia).
- Cita literal: "Con Envío Nube podés hacer envíos tanto a domicilio como a sucursal, con Correo Argentino y Andreani, a todo el país. Activando nuestra solución de envíos, contás con un 5% de descuento adicional sobre las tarifas de estos servicios (...) Además, tenemos un 10% de descuento adicional para la zona 1 (es decir, envíos dentro de la misma ciudad) hasta 10 kilos." El descuento "ya viene aplicado en el precio final que abona el cliente".
- La página comercial promete "Accedé a precios exclusivos con Correo Argentino, Andreani y E-Pick. Hasta un 15% más económicos que si contratás por tu cuenta" y "Sin abonos ni contratos. Solo pagás las etiquetas que generás". También: "Sin mínimo de retiro, sin costo de recolección" y entregas "en el día o next day a AMBA", más interior de Buenos Aires, Rosario y Ciudad de Córdoba (E-Pick).
- Envío tipo por esta vía: sin cifra con fuente primaria. Ilustración **supuesto** (no es un dato): si la tarifa estándar de Andreani fuera la del cotizador público, 5% menos daría $13.196 a domicilio y $10.877 a sucursal para Córdoba. Pero la ayuda dice que el 5% es "adicional" sobre la tarifa de Envío Nube, y no se conoce la base. No usar como precio.
- Cargos posteriores (Tiendanube, blog [S]): "ajuste de aforo logístico" si el peso o las dimensiones reales superan los declarados, y "estas diferencias se facturan al mes siguiente".
- Plazos (ayuda oficial, [S]): Paq.ar Clásico 2 a 5 días hábiles; Expreso 1 a 3; Andreani 2 a 3; E-pick 72 a 96 horas hábiles, más 24 horas.

## 4. Mercado Libre: lo que paga el vendedor por el mismo kilo

Resultado: la ayuda oficial de Mercado Libre (https://vendedores.mercadolibre.com.ar/ayuda/43522 "Costos por ofrecer envíos gratis", https://vendedores.mercadolibre.com.ar/ayuda/42402 "Costos por vender", https://developers.mercadolibre.com.ar/costos-de-envios) dio 403 también con el navegador, y www.mercadolibre.com.ar/ayuda dio 403 con WebFetch. Las cifras de esta sección vienen de un blog que cita esas páginas.

| URL | Tipo | Calificación | Marca |
|---|---|---|---|
| https://algoritmodigital.com.ar/nuevos-costos-mercado-libre-septiembre-2026/ | Blog que transcribe la ayuda oficial (sin fecha de publicación visible) | C, dato 3 (la aritmética de la tabla cierra con los descuentos que declara, ver abajo) | [S] (resumen de WebFetch) |
| https://algoritmodigital.com.ar/full-super-mercado-libre-costos-2026/ | Idem, Full Súper | C | [S] |
| https://www.forbesargentina.com/negocios/mercado-libre-reduce-menos-mitad-piso-envios-gratis-acelera-su-apuesta-consumo-masivo-n97635/amp | Prensa | B | [L] |
| https://www.noticiasnqn.com.ar/noticias/2026/09/10/352025-mercado-libre-cambia-una-de-sus-condiciones-y-desde-el-lunes-habra-envios-gratis-desde-15000 | Prensa (10/9/2026) | B | [S] |
| https://dolarhoy.com/empresas/mercado-libre-baja-el-monto-para-acceder-a-envios-gratis-y-busca-impulsar-las-compras-en-todo-el-pais-20269101550 | Prensa | B | [M] (solo título) |

Las notas de Forbes, noticiasnqn y dolarhoy repiten el mismo anuncio de la empresa: cuentan como una sola fuente.

### Costo de envío gratis, vigente desde el 1/9/2026, producto de menos de $33.000 (el envío tipo vale $30.000)

| Peso | MercadoLíder / verde / sin reputación | Amarilla | Naranja o roja |
|---|---|---|---|
| Hasta 0,3 kg | $8.666 | $9.904 | $12.380 |
| 0,3 a 0,5 kg | $9.506 | $10.864 | $13.580 |
| **0,5 a 1 kg (envío tipo)** | **$10.906** | **$12.464** | **$15.580** |
| 1 a 1,5 kg | $11.186 | $12.784 | $15.980 |
| 1,5 a 2 kg | $11.606 | $13.264 | $16.580 |
| 2 a 3 kg | $12.446 | $14.224 | $17.780 |

Para productos de $33.000 a $49.999 y reputación verde, 0,5 a 1 kg cuesta $7.790; desde $50.000, $8.290. Para amarilla: $9.348 y $9.948.

- Descuentos sobre la tarifa base, según el blog: productos de menos de $33.000, MercadoLíder/verde/sin reputación 30%, amarilla 20%, naranja o roja 0%; desde $33.000, 50%, 40% y 0%. Comprobación aritmética propia: $15.580 (naranja, 0%) x 0,7 = $10.906 (verde) y x 0,8 = $12.464 (amarilla). Entonces la tabla ya trae el descuento aplicado (inferencia).
- Peso: se toma el mayor entre el físico y el volumétrico (largo x alto x ancho / 5000 para Mercado Envíos, según otro resultado del buscador; el blog de Full Súper dice dividir por 6.000: dos divisores distintos según fuente, sin resolver).
- Umbral: "desde este precio ($33.000) el envío gratis es obligatorio" y "ofrecer envío gratis abajo de $33.000 sigue siendo opcional" (blog, vigente desde 1/9/2026). Un producto de $30.000 cae en la zona opcional.

### Umbral de envío gratis $33.000 a $15.000 (el rumor del brief)

- Confirmado con fuente de prensa y no con comunicado a vendedores. Forbes Argentina [L]: "A partir de este lunes, la empresa reducirá de $ 33.000 a $ 15.000 el monto mínimo de compra para acceder a envíos gratis en todo el país a través de su membresía Meli+". Y: "La bajada de línea comercial se financiará íntegramente con recursos de la compañía, sin trasladar costos a los vendedores".
- noticiasnqn (jueves 10/9/2026) [S]: "Desde el próximo lunes, el mínimo necesario para acceder a envíos gratis mediante Meli+ bajará de $33.000 a $15.000" y "Mercado Libre absorberá directamente el costo de la medida". Fecha de vigencia: lunes 14/9/2026 (inferencia desde la fecha de la nota; una fuente del buscador la dio como lunes 15, que no cae lunes).
- No se encontró el comunicado oficial a vendedores. Si la tabla de arriba cambió con esto: el blog no lo dice; se afirma que el cambio no modifica los costos del vendedor. **Hueco**.
- Los $15.000 y $24.000 del blog son tramos del cargo por unidad vendida de Flex, no umbrales de envío gratis.

### Flex y cargo por unidad (blog, vigente desde 1/9/2026, [S])

| Precio del producto | Cargo por unidad vendida en Flex |
|---|---|
| Hasta $14.999 | $1.330 |
| $15.000 a $23.999 | $2.740 |
| $24.000 a $32.999 | $3.320 |

Para el envío tipo ($30.000) son $3.320 por unidad, según esta fuente. El blog dice que Mercado Libre bonifica parte del envío Flex según la zona, sin montos. La nota no publica tabla de costo de envío de Flex.

### Full

- Costo por unidad vendida de Full Súper (blog, [S], para productos de menos de $33.000), hasta 1 kg y precio de $15.000 a $32.999: $880 si es "Esencial" y $1.495 el resto. Tope: el costo por unidad nunca supera el 25% del precio. Desde $33.000 rige envío gratis obligatorio y no hay cargo por unidad vendida.
- Almacenamiento por unidad y día por tamaño y cargo por stock antiguo: no hay fuente primaria. Fuentes secundarias, todas [S]:
  - base.com, 9/6/2026: "una unidad pequeña puede costar alrededor de $0,67 por día de almacenamiento", y el cargo por stock antiguo "empieza a generarse a partir de los 120 días corridos" (supermercado: "a los dos meses"). Sin enlace oficial.
  - base.com, 20/4/2026: el cargo "se activa cuando una unidad lleva más de 120 días corridos en bodega", con tramos de 121 a 180, 181 a 365 y más de 365 días, sin montos; ruta en el panel "Mi cuenta > Ventas > Cargos por stock antiguo".
  - Resumen del buscador: otra fuente habla de unidades "sin venta más de 90 días", y una tabla en dólares (0,011 / 0,040 / 0,090 / 0,500 por día según tamaño, "desde el 6 de abril de 2026") sin país claro; también un cambio mexicano del 14/9/2026. No se leyó ninguna de las dos: dato 6.
  - Conclusión: las dos cifras (90 y 120 días) circulan; la mayoría de las fuentes argentinas dicen 120 días corridos; sin verificación oficial.

## 5. Comparación del costo del mismo kilo desde el lado del comercio

| Quién paga | Canal | Costo del kilo | Qué es |
|---|---|---|---|
| Comercio en Mercado Libre | Envío gratis, reputación verde | $10.906 | Tabla del blog, producto de $30.000, ya con 30% de descuento |
| Comercio en Mercado Libre | Envío gratis, amarilla / naranja o roja | $12.464 / $15.580 | Ídem |
| Comercio en Mercado Libre | Flex | $3.320 por unidad vendida | Cargo, sin el costo del envío propio |
| Comercio en Mercado Libre | Full, 0,5 a 1 kg | $880 o $1.495 por unidad vendida | Cargo Full Súper, más el costo de enviar su stock al depósito y el almacenamiento (no hay cifra oficial) |
| Comercio propio, Andreani por cotizador público | A sucursal / a domicilio (Córdoba) | $11.449,61 / $13.890,41 | Con IVA. Tarifa pública; un comercio con cuenta puede tener otra |
| Comercio propio, OCA, lista pública | Sucursal y domicilio, 0 a 1 kg | $13.865 a $24.274 | Según zona; con IVA |
| Comercio propio, Correo Clásica de mostrador | Domicilio, hasta 1 kg | $19.500 a $26.400 | Más 3% de valor declarado |
| Comercio con Envío Nube | los tres | sin cifra pública | Descuentos declarados: 5% adicional |

Lectura (inferencia): el costo que Mercado Libre le cobra a un vendedor verde por el kilo ($10.906) es del mismo orden que el cotizador público de Andreani a sucursal ($11.449,61). Son productos distintos (Mercado Envíos incluye la gestión completa y la tarifa de venta se cobra aparte). No se midió el costo por pedido total.

## Huecos

- Tarifa Paq.ar 2026 de Correo Argentino y su lista para Responsables Inscriptos (`lista-de-precios-PY-MiCorreo.pdf`): no accesibles sin cuenta; el PDF público es de febrero de 2023. Los términos y condiciones de contrato empresarial, mínimos y facturación mensual: sin fuente primaria.
- Tarifario de Envío Nube: la página oficial promete un tarifario y no lo trae. No se cotizó el envío tipo por esa vía.
- Plazo oficial de Andreani y OCA: sin página oficial leída; solo ayuda de Tiendanube (Andreani, [S]) y un blog (OCA, [S]).
- OCA: significado de las zonas Local, Regional, Nacional 1 y Nacional 2; cotizador público sin cuenta (no existe a la vista; ePak exige cuenta).
- Vía Cargo, Cruz del Sur y Urbano: sin cotizador ni tarifa pública hallados. Un comparador de terceros (servidos.ar, actualizado en junio de 2026) los lista con rangos sin verificar; no se usan.
- Mercado Libre: ayuda oficial de costos, Flex y Full dio 403 (https://vendedores.mercadolibre.com.ar/ayuda/43522, https://vendedores.mercadolibre.com.ar/ayuda/42402, https://developers.mercadolibre.com.ar/costos-de-envios), incluso con navegador real. Almacenamiento de Full, stock antiguo (90 o 120 días) y tabla de Flex sin fuente primaria. Reputación y umbral: sin el comunicado a vendedores.
- Andreani: no se verificó el precio con la localidad correcta (Villa Dolores, Esquel) dentro de cada CP, ni con valor declarado cargado.
- Una comparación de mostrador contra e-commerce solo es posible en Andreani (público y cuenta profesional, sin cifras de la segunda) y en Correo (mostrador y Paq.ar, este último vencido en lo público).

Búsquedas: cupo agotado no (unas 16 búsquedas web; el resto fueron lecturas directas de páginas y PDF).
