# Rubro: gastronomía con pedidos para llevar y delivery (Argentina)

Consulta: 2026-11-22. Capa cruda: mide, no propone ni puntúa.

Cupo: **no se agotó**. Quedaron huecos porque algunas páginas no se dejaron leer: la página de socios de PedidosYa (403), la landing de restaurantes de Mercado Libre (403 para WebFetch; se leyó con curl), la ficha de gastronomía de CABA (404), la nota de iProUP sobre comisiones (vino truncada) y la ayuda oficial de Tiendanube y Shopify (WebFetch bloqueado; se leyeron con curl).

## 1. Respuesta primero

- **El dolor es de plata y de control, y está documentado.** La prensa de 2026 ubica la comisión de PedidosYa entre 25% y 35% según quién reparte; ese número es una estimación de una consultora, porque PedidosYa no publica tarifario (fuentes 1 y 3). En Rosario, la Cámara de Hamburgueseros dice que PedidosYa llega al 35% semanal sumando descuentos, publicidad e impuestos, y que el local paga el 85% del producto cuando un cliente reclama (fuente 3, abril 2026).
- **Las reseñas confirman el dolor, con un matiz.** Leímos 400 reseñas de apps para comercios y 330 son negativas (1-2 estrellas). En PedidosYa (180 reseñas), el tema más repetido es que **la app falla** (86). Después vienen el **soporte inaccesible** (52), los **cobros y comisiones** (42), los **repartidores** (21) y los **reclamos y cancelaciones que paga el local** (21).
- **El canal propio ya está atendido, y barato.** Fudo, Pedix, OlaClick, Bistrosoft y Maxirest venden tienda o menú online con zonas, horarios y comandas, con precios oficiales en pesos de $12.000 a $101.800 por mes. Algunos lo ofrecen sin comisión; Fudo cobra 1,9% + IVA por venta y no cobra abono por la tienda.
- **Las plataformas generales de tiendas resuelven mal lo propio del rubro, según su propia ayuda.** Tiendanube trae variantes (3 propiedades, 999 combinaciones), envío propio por km o código postal con monto mínimo y retiro en local con horario. No trae, en lo que leímos, agregados con precio fuera de las variantes, cierre del checkout fuera de horario, comanda a cocina ni avisos en tiempo real; para eso hay apps de terceros con 0 a 4 reseñas.
- **Tamaño, cifra débil.** Hay 25.134 locales gastronómicos empleadores (CEP XXI 2022). PedidosYa dice tener más de 45.000 comercios adheridos, de todos los rubros, y Rappi alrededor de 25.000 en una cifra vieja. No hay dato de cuántos gastronómicos venden por delivery ni de cuántos tienen canal propio.
- **No hay tope legal vigente a las comisiones.** El acuerdo de topes con FEHGRA (10% o 18% + IVA) venció el 30/09/2021. Los proyectos de 2025 y 2026 que encontramos regulan a los repartidores, no las comisiones. Lo nuevo de 2026 viene de arriba: Uber compra Delivery Hero, la dueña de PedidosYa (falta la aprobación de competencia), y Mercado Libre entró con una comisión estimada cercana al 13%.

## 2. Tamaño, de abajo hacia arriba

| paso | cuenta | resultado | pieza que la sostiene |
|---|---|---|---|
| 1 | Locales gastronómicos empleadores, CLAE 5610xx, 2022 | 25.134 (21.685 en 2021) | CEP XXI, dato de base (A2) |
| 2 | Restamos bares (1.222) y locales con espectáculo (587), porque piden delivery poco | ≈23.300 | **supuesto**: bares y espectáculo casi no venden por delivery |
| 3 | De esos, los de formato «para llevar» por naturaleza: fast food 3.273 + heladerías 2.962 + comidas para llevar 1.836 | 8.071 | CEP XXI (A2) |
| 4 | Restaurantes con mesa (10.350) y sin espectáculo (4.888) que además hacen delivery | sin dato: entre 0 y 15.238 | **hueco**: no hay encuesta de cámara que lo mida |
| 5 | Monotributistas sin empleados (rotiserías chicas, cocinas en casa, dark kitchens) | sin dato | **hueco**. Una ficha de CABA da 30,2% de informalidad en gastronomía en 2024 [S], pero no cuenta monotributistas |
| 6 | Cruce: comercios adheridos a PedidosYa, todos los rubros | más de 45.000 | Forbes 05/11/2025 y Chequeado, ambas con el dato que dio la prensa de PedidosYa (lo dice quien vende, C3) |
| 7 | Cruce: comercios aliados a Rappi | ≈25.000 (fecha incierta); ≈15.000 en notas anteriores | búsqueda [S], C4 |
| 8 | Cruce: negocios que usan Fudo | más de 35.000, en varios países | fu.do (lo dice quien vende, C4) |

**Inferencia, fuerza débil.** Si PedidosYa declara más de 45.000 comercios y el padrón de locales gastronómicos empleadores es de 25.134, el universo que vende por app supera al padrón de empleadores. Eso pasa porque PedidosYa suma súper, farmacias y kioscos, cada sucursal cuenta como un comercio y entran los gastronómicos sin empleados.

**Supuesto, sin fuente:** si entre la mitad y las tres cuartas partes de los comercios de PedidosYa fueran gastronómicos, serían de 22.000 a 34.000. Lo damos solo como orden de magnitud: un rango de **8.000 a 35.000 locales gastronómicos con delivery o take away por app**. El piso es el paso 3; el techo, el padrón más los no empleadores. Ninguna fuente lo mide directo.

**Cuánto pesa el delivery en sus ventas:**
- Hamburgueserías de Rosario: entre 30% y 80% de las ventas, con algunos locales en 90% (Letra P, abril 2026, fuente 3).
- Un comerciante de Rosario: entre 15% y 30% de la facturación diaria (La Capital, octubre 2024, fuente 4).
- Una cadena de fast food: «entre 15 y 20%» (búsqueda [S], fuente 22).
- No encontramos una encuesta de FEHGRA, CAME ni de la Cámara de Restaurantes que lo mida.

**Fuerza de la cifra: débil.** El padrón de empleadores es sólido (A2). Lo que no tiene medición es qué parte hace delivery, cuántos son monotributistas y cuántos tienen canal propio.

## 3. Cuánto pagan hoy

### Marketplaces de delivery (comisión sobre el pedido)

| Quién | Comisión | Otros costos | Plazo de cobro | Fuente |
|---|---|---|---|---|
| PedidosYa | 25% a 35% según quién reparte (estimación de Focus Market, mayo 2026) | Tarifa de servicio al usuario de 1,5% a 2% (la paga el cliente). Las reseñas nombran publicidad no pedida ($60.000), «servicio de configuración inicial» ($35.000) y «costos de mantenimiento» (≈$11.000), sin confirmar | Semanal (Letra P 2026 y reseñas). La cifra de 20 o 30 días sale de iProUP, fecha incierta | 1, 3, reseñas |
| PedidosYa, según comercios de Rosario | Hasta 35% semanal con descuentos, publicidad e impuestos; de $10 millones facturados se quedaba con $4,5 a $5 millones | El local paga el 85% del producto si el cliente reclama | Semanal | 3 (abril 2026) |
| PedidosYa, según comercios de Rosario en 2024 | Promedio de 21% a 23%; 10% los primeros 30 días y después 17% a 25% | Promociones del 40% al 50% que el local subsidia casi enteras | — | 4 (octubre 2024) |
| Rappi | «No superan el 25%», según la propia empresa; 15% a 20% como máximo, según los hamburgueseros de Rosario | Su página oficial dice: comisión de «un porcentaje más IVA» sobre cada venta, sin costo de alta, y que varía por país. No publica el número | Las reseñas hablan de hasta 2 semanas | 1, 3, 5 |
| Mercado Libre (Restaurantes / Mercado Pago Delivery) | «Cercana al 13%», según Focus Market. No hay tarifario oficial | El alta solo se hace con un contacto comercial; se integra por API o con el «Gestor de Pedidos» | Sin dato | 1, 6, 7 |

Cobertura de Mercado Libre Restaurantes, según su propia página: «CABA, en algunos barrios de zona sur, zona norte y zona oeste y en La Plata» (fuente 6).

### Software vertical argentino (abono mensual, precios oficiales de noviembre 2026)

| Quién | Precio | Qué trae para delivery | Fuente |
|---|---|---|---|
| Fudo | Inicial $23.900, Avanzado $46.500, Pro $93.500 por mes, precio final (sin impuestos nacionales: $19.752 / $38.430 / $77.273). Módulos: Delivery Apps +$19.500, Facturación +$13.500, Mesas +$8.500, Recepcionista IA +$60.000 | Tienda online propia **sin abono**: 1,9% + IVA por venta con Fudo Pagos, con tope de $99.000 + IVA por mes. Envío fijo o por zonas, horarios, repartidores a demanda con Rapiboy | 8, 9 |
| Bistrosoft | Web $21.600, Avanzado $70.200, Premium $101.800 por mes + IVA (15% menos en pago anual) | Avanzado: tienda propia de hasta 50 pedidos e integración con PedidosYa, Rappi, Rappi Turbo y Mercado Pago. Premium: pedidos ilimitados y gestor de pedidos | 10 |
| Maxirest | Full $42.500 por mes (anual $36.125); Pro $89.000 de lista ($66.750 con promoción). La página dice «IVA incluido» y la letra chica dice que no lo incluye | Integración con apps de delivery +$15.900 por mes. Pro trae módulo de delivery propio y Menú QR con pedidos por WhatsApp | 11 |
| Pedix | Principiante $19.000, Especialista $25.500, Pro $35.000 por mes (no aclara IVA) | Tienda con pedidos por WhatsApp, variantes, opciones y extras, horarios, zonas, Mercado Pago, impresión térmica. «No pagás comisiones por tus ventas»; el reparto con Rapiboy o Puni cobra por pedido | 12 |
| OlaClick | Advanced $12.000, Premium $30.000, Elite $71.000, Impulso $245.000 por mes, en ARS según los datos de la página | Menú digital, punto de venta y CRM en todos los planes. Dice tener «más de 40.000 negocios» en varios países (lo dice quien vende) | 13 |

### Plataforma general de tiendas y sus apps del rubro

En la tienda de apps de Tiendanube:
- «Abejita: Menú de Restaurante»: gratis.
- «Horario de Atención»: gratis; muestra el horario pero no dice que bloquee la compra.
- «Entrega programada»: ARS 12.900 por mes.
- «Campo personalizado»: Nivel 1 a ARS 10.991,92 por mes [S].

(Fuentes 14 a 16 y 19.)

### Ejemplo de cuenta (**inferencia**)

Tomamos un pedido de pizza de $25.000 (precio de abril 2026, fuente 1).
- **Por PedidosYa con su logística, al 30% + IVA:** la comisión es $7.500 + $1.575 de IVA, unos $9.075 por pedido, sin contar promociones cofinanciadas ni cargos por reclamo.
- **Por la tienda propia de Fudo:** 1,9% + IVA son unos $575 por pedido. El reparto lo pone el local o se paga aparte con Rapiboy (precio no medido).
- **Por Pedix:** el plan Especialista ($25.500 por mes) cuesta lo mismo que la comisión de unos 3 pedidos en la app. Cobrar con Mercado Pago tiene su propia tarifa, que no medimos acá.

La cuenta deja afuera lo principal: **la demanda que trae la app y el canal propio no**. No sabemos cuántos pedidos consigue un local por su cuenta.

## 4. De qué se quejan

**Qué leímos.**
- Google Play: las reseñas más recientes de cuatro apps para comercios, bajadas con google-play-scraper (idioma es, país AR). Google Play no filtra por país, así que hay reseñas de México, Colombia y otros países, sobre todo en Rappi.
- App Store Argentina: las reseñas de PedidosYa Portal, todas de la tienda argentina.

**Cómo las contamos.** Leímos las reseñas una por una y las codificamos a mano. Una reseña puede caer en más de un tema. Las de menos de 25 caracteres (por ejemplo «pésimo») se leyeron pero no se codificaron.

| Ficha | Reseñas codificadas | Negativas (1-2 estrellas) | Años | Nota |
|---|---|---|---|---|
| PedidosYa Portal, Google Play (com.deliveryhero.pedidosyapartner; 2,54 estrellas con 518 calificaciones) | 149 de 200 bajadas | 131 | 04/2025 a 11/2026 | Mayoría rioplatense, con algunas de Bolivia, Chile o Perú |
| PedidosYa Portal, App Store Argentina (id6494987310) | 31 de 31 | 27 | 02/2025 a 10/2026 | Todas argentinas |
| RappiAliado, Google Play (com.rappi.restaurants; 2,53 estrellas con 4.964 calificaciones) | 152 de 200 | 140 | 01/2026 a 11/2026 | **Mayoría de México y Colombia**; sirve para Rappi en general, poco para Argentina |
| Fudo, Google Play (do.fu.app; 3,57 estrellas con 472 calificaciones) | 68 (de 2024 a 2026; también leímos las ≈82 anteriores, de 2017 a 2023) | 32 | 01/2024 a 11/2026 | Muchas son de mozos y no de dueños |
| Rappi Partners App, Google Play (com.rappi.partners) | ≈70 leídas, sin codificar en detalle | casi todas | 2022 a 2026 | Mayoría de México; casi todo son fallas de la app |
| Apps de restaurante en la tienda de Tiendanube | 4 (Abejita, en portugués y genéricas); Horario de Atención y Entrega programada no tienen reseñas | 0 | 2026 | No sirven como señal |

**Total codificado: 400 reseñas, 330 negativas, de 2024 a 2026.**

**PedidosYa (Play + App Store Argentina, n = 180, 158 negativas)**

| Tema | n | Ejemplos |
|---|---|---|
| La app falla (no deja entrar, se cierra, suena sin pedido, no muestra finanzas, impresora) | 86 | «refresh or try again later», «se desloguea mucho eso hace que se pierdan pedidos» |
| Soporte inaccesible, solo un bot o asesores que no responden | 52 | «siempre hablas con un chat bot» |
| Comisión alta y descuentos o cargos que no se explican | 42 | «me cobran el 33%», «la comision ya es del 60%» |
| Repartidores (GPS falso, demoras, robo, no se los puede contactar) | 21 | «marquen 'llegada al local' cuando el GPS muestra que están a 8 km» |
| Reclamos y cancelaciones que paga el local | 21 | «te cobran prácticamente todo el pedido» |
| Alta trabada (fotos, verificación, semanas sin poder vender) | 12 | «hace 1 mes y medio cargue los datos de mí heladeria» |
| Liquidación: pagan menos, tarde o retienen | 12 | «más de 2 meses esperando una liquidación» |
| Promociones o publicidad que el local no autorizó | 5 | «me encajaron una supuesta publicidad» |
| No hay datos ni contacto del cliente | 4 | «deberían poner los datos completos de los clientes» |
| Positivas | 7 | |
| Otras o sin contenido | 15 | |

**RappiAliado (n = 152, 140 negativas, mayoría fuera de Argentina):**
- La app falla: 95 (la tienda se cierra sola, entran pedidos fuera de horario, alarmas).
- Soporte, sobre todo bots o IA: 59.
- Repartidores: 14.
- Comisión: 13.
- Reclamos que paga el local: 13.
- Liquidación: 12.
- Promociones o publicidad no autorizadas: 6.

**Fudo (n = 68, 32 negativas):**
- Le faltan funciones en la app móvil frente a la web: 20.
- Falla o una actualización empeoró la app: 18.
- Positivas: 15.
- Precio, aumentos o cobro de porcentaje: 10 (una reseña de 2024 dice que el abono subió 290% de un mes a otro).
- Soporte: 10.

**Citas textuales (sin nombre de quien la escribió):**
- «en su información dice que te descuentan el 25% más impuestos, llevo dos meses donde me cobran el 33%» (PedidosYa, Play, 2026)
- «Cuando un cliente reclama, casi siempre le dan la razón sin investigar y te cobran prácticamente todo el pedido, devolviéndote muy poco» (PedidosYa, Play, 2026)
- «Para apelar una deduccion por reclamo te piden foto del pedido. Sino le sacaste te anulan la apelacion» (PedidosYa, App Store Argentina, 2026)
- «Es inaceptable que los repartidores marquen 'llegada al local' cuando el GPS muestra que están a 8 km de distancia. Esto nos genera una mora por retraso injusta» (PedidosYa, Play, 2026)
- «Cuando se reanuda un turno, se habilitan opciones de menú que anteriormente habías deshabilitado» (PedidosYa, App Store Argentina, 2026)
- «más de 2 meses esperando una liquidación cada semana es una excusa nueva» (PedidosYa, Play, 2025)
- «Todo era bueno hasta que les dió por empezar a querer cobrar un porcentaje de las ventas del negocio» (Fudo, Play, 2026)
- «terrible la seleccion de item y grupos modficadores un desastre» (Fudo, Play, 2025)

**Quejas en prensa (testimonios por rol):**
- El dueño de una rotisería de Rosario: «Los clientes no son ya del negocio sino de Pedidos Ya» (La Capital, 2024, fuente 4).
- Una fuente de la Cámara de Hamburgueseros de Rosario: «Se hace imposible poder sostener esto» (Letra P, 2026, fuente 3).
- Un ex presidente de una asociación gastronómica: «Cobran entre el 18 y hasta el 33% de comisión, según el tamaño del restaurante, y encima liquidan a los 20 o 30 días» (iProUP, fecha incierta, [S], fuente 17).

**No se pudo leer:** Capterra de Fudo (no lo intentamos de nuevo; el barrido previo dio 403), las reseñas de Rappi Partners en el App Store de Argentina (no tiene ninguna), Reddit y foros (la búsqueda no devolvió hilos de dueños) y la página de reclamos de Defensa del Consumidor.

## 5. Quién atiende

| Quién | Qué cubre | Qué no cubre | Precio | Fuente |
|---|---|---|---|---|
| PedidosYa | Demanda (clientes), logística propia, pagos, publicidad dentro de la app, créditos | Datos del cliente; contacto directo con el cliente o el repartidor (según reseñas); reglas de reclamo que el local controle | 25% a 35% estimado; no publica | 1, 2, 3 |
| Rappi | Lo mismo que PedidosYa; Turbo Restaurantes | No publica la comisión antes del alta | % + IVA, sin número; «no supera el 25%» según la empresa | 1, 4, 5 |
| Mercado Libre / Mercado Pago Delivery | Demanda dentro de la app de Mercado Libre, cobro con Mercado Pago, Gestor de Pedidos | Solo CABA, parte de GBA y La Plata; alta por contacto comercial; según una fuente reparte el propio local [S] | ≈13% estimado | 1, 6, 7 |
| Fudo | Punto de venta, comandas, mesas, facturación, tienda online propia, WhatsApp con IA, integraciones con apps | La app móvil tiene menos funciones que la web (reseñas); la tienda no trae demanda | $23.900 a $93.500 por mes + módulos; tienda 1,9% + IVA | 8, 9 |
| Bistrosoft | Punto de venta, comandas, tienda propia, PedidosYa, Rappi y Mercado Pago integrados | La tienda propia no está en el plan Web | $21.600 a $101.800 por mes + IVA | 10 |
| Maxirest | Punto de venta, cocina (KDS), facturación, delivery propio en Pro | Tienda online, no la nombra | $36.125 a $89.000 por mes | 11 |
| Pedix | Tienda con pedidos por WhatsApp, extras, zonas, horarios, Mercado Pago, impresión térmica | No trae demanda; el reparto es aparte | $19.000 a $35.000 por mes, sin comisión | 12 |
| OlaClick | Menú digital, punto de venta, CRM | (no verificado en detalle) | $12.000 a $245.000 por mes | 13 |
| Tiendanube (núcleo) | Variantes con precio (3 propiedades, 999 combinaciones); envío propio por km, código postal o zona, con monto mínimo y horario de corte; retiro en local con horario | No encontramos en su ayuda agregados con precio fuera de las variantes, cierre del checkout fuera de horario, comanda a cocina, avisos sonoros ni estado del pedido en tiempo real | según plan | 18, 19 |
| Tiendanube (apps del rubro) | Menú (Abejita, gratis), cartel de horario (gratis), franjas de entrega (ARS 12.900 por mes), campos personalizados (≈ARS 11.000 por mes) | Tienen 0 a 4 reseñas; ninguna bloquea la compra fuera de horario según su ficha | 0 a ≈ARS 12.900 por mes | 14 a 16 |
| Shopify | Variantes hasta 2.048 con 3 opciones por producto; reparto local por radio (hasta 160 km) o código postal, con hasta 10 zonas por local, mínimo de pedido y precio por zona | Agregados fuera de las 3 opciones (requieren apps); horario de tienda nativo (según la comunidad) | según plan | 20, 21 |

## 6. Huecos con fuerza

| Hueco (dolor sin atender o mal atendido) | Fuerza | Por qué esa fuerza |
|---|---|---|
| El costo y la opacidad de lo que cobra el marketplace: deducciones, promociones y publicidad no autorizadas, cargos por demora | **Fuerte** | Lo dicen 42 reseñas de PedidosYa más 5 de promociones; lo dice una cámara (Rosario 2026); hay un fallo de 2022 y tres notas independientes con números. No lo atiende nadie: el software vertical gestiona el canal propio, pero no audita la liquidación de la app (eso no lo medimos) |
| Los reclamos y cancelaciones los paga el local, sin forma de apelar | **Fuerte** | 21 reseñas de PedidosYa y 13 de Rappi; el 85% del producto según la cámara de Rosario. Solo lo puede cambiar el propio marketplace |
| No hay soporte humano para el comercio | **Fuerte** en reseñas, **débil** como hueco atacable | 52 reseñas de PedidosYa y 59 de Rappi. Es interno del marketplace |
| El canal propio no trae demanda: el cliente «es de PedidosYa» | **Media** | Lo dicen la prensa y 4 reseñas. Hay herramientas de canal propio desde $12.000 por mes, pero **no medimos cuánto venden** por ese canal |
| Las plataformas generales de tiendas no traen nada para comida (agregados, horario que cierre el checkout, comanda, tiempo real) | **Débil** como hueco de mercado | El faltante está verificado en la ayuda oficial, pero el software vertical lo cubre barato y con más reseñas |
| Reparto propio confiable | **Media** | Hay 21 reseñas de PedidosYa sobre repartidores; el canal propio depende de Rapiboy, Puni o un cadete del local. No medimos precio ni calidad de esos servicios |

## 7. Lo que puede cerrar un hueco desde arriba

- **Mercado Libre / Mercado Pago.** Entró con una comisión estimada cercana al 13% y una cobertura acotada (fuentes 1 y 6). Ya tiene Gestor de Pedidos y cobro propio, y es el jugador con escala para bajar la comisión de referencia.
- **Uber + Delivery Hero (PedidosYa).** La compra se anunció en julio de 2026 por unos US$ 14.800 millones; Argentina queda bajo Uber y falta la aprobación de los organismos de competencia (fuente 23). Puede cambiar las condiciones a los socios, en cualquier dirección.
- **Rappi.** Es la alternativa a la que migraron los hamburgueseros de Rosario, con un tope que la propia empresa declara en 25% (fuentes 1 y 3).
- **Fudo y el software vertical.** Fudo ofrece tienda propia sin abono y usa «Sin comisiones del 30%» como argumento de venta (fuente 9). Ya ocupa el lugar del canal propio.
- **Tiendanube y Shopify.** No vimos señales de funciones propias para restaurantes en su ayuda oficial; lo que hay son apps de terceros.

## 8. Evidencia para los criterios (sin puntuar)

**¿Pagan hoy y se quejan?** Sí. Pagan comisión de 25% a 35% (estimada) y software de $12.000 a $101.800 por mes. Hay 330 reseñas negativas de 400 y conflicto en Rosario en 2026.

**¿Quién decide y cómo se llega?**
- Decide el dueño del local.
- Cámaras: FEHGRA, APPYCE (pizzerías y casas de empanadas), AFADHYA (heladeros), AAMF (franquicias), AHRCC (CABA) y la Cámara de Hamburgueseros de Rosario.
- Agregadores: PedidosYa junta socios en convenciones (más de 300 en noviembre de 2025, fuente 2) y los vendedores de punto de venta (Fudo, Maxirest, Bistrosoft) llegan a los locales.
- No medimos el rol de los distribuidores de insumos.

**¿Depende de un solo tercero?**
- Para integrarse con PedidosYa y Rappi hacen falta sus APIs; las de Mercado Pago Delivery piden contacto comercial (fuente 7).
- Los pedidos por WhatsApp dependen de Meta.
- La logística depende de las apps o de Rapiboy.

**¿Hay una opción gratis que hace lo central?**
- Para el menú: sí (Abejita, gratis).
- Para la tienda propia: casi. Fudo cobra 1,9% + IVA sin abono.
- Para recibir el pedido directo, WhatsApp es gratis, pero no lo medimos como herramienta.
- Para la demanda: no.

## 9. Lo que no se sabe

- Cuántos locales gastronómicos venden por delivery o take away, y cuántos tienen canal propio.
- Cuántos monotributistas gastronómicos hay.
- Cuántos de los 45.000 comercios de PedidosYa son gastronómicos.
- Qué parte de las ventas del local entra por canal propio frente a la app, en una medición de cámara o de las propias apps.
- La comisión oficial de PedidosYa, de Rappi Argentina y de Mercado Libre Restaurantes; ninguno la publica.
- La cifra de 20 o 30 días de liquidación es vieja; hoy las fuentes dicen semanal.
- Si el canal propio retiene clientes: la tasa de recompra, sin dato.
- El precio de Rapiboy y Puni por envío.
- El detalle de las funciones de OlaClick, MenuQR, Wabi, Justo y Pidely: Justo no tiene precio en pesos y las otras tres no se pudieron leer.
- Si Tiendanube tiene algo nativo para cerrar el checkout fuera de horario: en lo leído no aparece.

## 10. Fuentes

Calificación: fuente A (confiable) a F (sin poder juzgar); dato 1 (confirmado por otra fuente independiente) a 6 (sin poder juzgar). [L] es página leída entera (con WebFetch o con extracción por curl); [S] es solo resumen del buscador.

1. iProfesional, «Más pedidos y cargos de hasta 35%…», 14/05/2026 (cita a Focus Market) — https://www.iprofesional.com/index.php/negocios/454816-mas-pedidos-y-cargos-de-hasta-35-por-cento-la-presion-del-delivery-sobre-comercios-y-repartidores — B3 [L]. Corrección al barrido: **no trae plazos de liquidación ni el conflicto de Rosario**.
2. Forbes Argentina, «El futuro del delivery: planes de PedidosYa…», 05/11/2025 — https://www.forbesargentina.com/negocios/el-futuro-delivery-estos-son-planes-pedidosya-impulsar-crecimiento-su-ecosistema-argentina-n81086 — C3 [L] (lo dice quien vende).
3. Letra P, «Rosario: PedidosYa se queda el 35%…», 14/04/2026 — https://www.letrap.com.ar/economia/rosario-pedidosya-se-queda-el-35-la-recaudacion-y-desata-una-guerra-los-gastronomicos-n5423159 — B3 [L].
4. La Capital, «Apps de delivery: las promociones ponen en alerta a los comerciantes», 25/10/2024 — https://www.lacapital.com.ar/la-ciudad/apps-delivery-las-promociones-ponen-alerta-los-comerciantes-n10160252.html — B2 [L].
5. Rappi Partners, página de registro y preguntas frecuentes — https://partners.rappi.com/ar — A1 sobre el modelo de cobro [L con curl]; muestra RUC y +593 (plantilla regional).
6. Mercado Libre, landing de restaurantes — https://www.mercadolibre.com.ar/landing/restaurantes — A1 [L con curl; WebFetch dio 403].
7. Mercado Pago Developers, introducción a MP Delivery — https://www.mercadopago.com.ar/developers/es/docs/mp-delivery/introduction — A1 [L].
8. Fudo, precios de Argentina — https://fu.do/es-ar/precios/ — A1 (precio de lista) [L].
9. Fudo, delivery y tienda online — https://fu.do/es-ar/delivery/ y la portada https://fu.do/es-ar/ («35.000+ negocios», lo dice quien vende) — A1 precio, C4 cantidad [L].
10. Bistrosoft, precios de Argentina — https://bistrosoft.com/ar/precios/ — A1 [L].
11. Maxirest, precios — https://maxirest.com.ar/maxi-rest-precios/ — B1 (la página se contradice sobre el IVA y tiene texto de relleno) [L].
12. Pedix, Argentina — https://info.pedix.app/ar/ — A1 precio, C4 cantidad de tiendas [L].
13. OlaClick, precios — https://pricing.olaclick.app/es — B2 (la moneda ARS sale de los datos de la página) [L con curl].
14. Tiendanube, app Abejita Menú — https://www.tiendanube.com/tienda-aplicaciones-nube/abejita-restaurant-menu — A1 [L].
15. Tiendanube, app Entrega programada — https://www.tiendanube.com/tienda-aplicaciones-nube/entrega-programada — A1 [L].
16. Tiendanube, app Horario de Atención — https://www.tiendanube.com/tienda-aplicaciones-nube/abejita-open-hours — A1 [L]; «Campo personalizado» https://www.tiendanube.com/tienda-aplicaciones-nube/campo-personalizado — [S].
17. iProUP, «PedidosYa, Rappi: cuánto cuesta un delivery» — https://www.iproup.com/economia-digital/34259-pedidosya-rappi-cuanto-cuesta-un-delivery — C4 [S] (vino truncada; fecha incierta).
18. Ayuda de Tiendanube, variantes — https://ayuda.tiendanube.com/es_AR/160434-variantes-del-producto/que-son-las-variantes-y-como-configurarlas-en-mis-productos — A1 [L con curl], actualizada 6/11/2026.
19. Ayuda de Tiendanube, envíos personalizados — https://ayuda.tiendanube.com/es_AR/122892-envios-personalizados/como-ofrecer-otros-envios-o-entregas-personalizadas — A1 [L con curl] (el código postal «se habilita de forma progresiva»); retiro en local con horario: https://ayuda.tiendanube.com/es_ES/122909-locales-y-puntos-de-retiro/como-agregar-un-local-o-punto-de-retiro-en-mi-tienda — [S].
20. Ayuda de Shopify, Local delivery — https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/local-delivery — A1 [L con curl].
21. Shopify changelog, límite de 2.048 variantes — https://shopify.dev/changelog/the-product-variant-limit-is-now-2048-for-all-merchants — A2 [S]; comunidad de Shopify sobre horario — https://community.shopify.com/t/activar-y-desactivar-ventas-en-rangos-horarios/14516/1 — D4 [S].
22. La Nación, «El nuevo mapa del fast food», 31/01/2026 — https://www.lanacion.com.ar/economia/negocios/el-nuevo-mapa-del-fast-food-menos-consumo-cambios-de-habitos-y-un-negocio-que-se-reinventa-nid31012026-2/ — B4 [S].
23. iProfesional, «Uber compra dueña de PedidosYa por US$ 14.800 millones», 16/07/2026 — https://www.iprofesional.com/negocios/460144-uber-compra-duena-de-pedidosya-por-14800-millones-dolares-y-nace-un-gigante-global-de-delivery — B2 [S]; Forbes Argentina, nota n93888 — [S].
24. iProfesional, «PedidosYa y gastronómicos extienden acuerdo por comisiones», **02/07/2021** (el buscador la fechó 2026) — https://www.iprofesional.com/economia/342659-pedidosya-y-gastronomicos-extienden-acuerdo-por-comisiones — B2 [L]. Topes de 10% + IVA (marketplace) y 18% + IVA (con logística) hasta el 30/09/2021, solo para socios de FEHGRA, APPYCE, AFADHYA y AAMF.
25. La Capital y Cronista, multa de $4,6 millones a PedidosYa en Santa Fe, junio 2022 — https://www.lacapital.com.ar/economia/pedidos-ya-pago-una-multa-46-millones-que-le-aplico-la-provincia-n10018154.html — B3 [S]. Discrepan: La Capital da topes de 18% y 21% y Cronista de 18%; también discrepan sobre el tribunal.
26. HCDN, proyecto 6464-D-2025, «Régimen de Autónomos Digitales en Plataformas de Delivery» — https://www4.hcdn.gob.ar/dependencias/dsecretaria/Periodo2025/PDF2025/TP2025/6464-D-2025.pdf — A1 [L]. Regula a repartidores, **no a las comisiones**.
27. HCDN, proyecto 0185-D-2025 — https://www4.hcdn.gob.ar/dependencias/dsecretaria/Periodo2025/PDF2025/TP2025/0185-D-2025.pdf — A1 [L]. Topes a aranceles de tarjetas, no a apps de delivery.
28. Concejo Deliberante de General Pueyrredon, proyecto 2026 (26E01696), 20/08/2026 — https://www.concejomdp.gov.ar/sgl/expedientes/proyectos/2026/26E01696/original.docx — A1 [L]. Sobre repartidores; menciona el proyecto bonaerense de protección a repartidores y el Convenio 193 de la OIT (junio 2026).
29. iProfesional, «Delivery en CABA: repartidores y comercios cuestionan la nueva norma», 13/11/2026 — https://www.iprofesional.com/negocios/469043-delivery-en-caba-repartidores-y-comercios-cuestionan-la-nueva-norma — B3 [L]. Lineamientos porteños publicados en el Boletín Oficial el 28/10: los locales deben tener un lugar de espera para los repartidores, y APPYCE objeta.
30. Mercado, «PedidosYa creció 22% en órdenes en 2025», 05/02/2026 — https://mercado.com.ar/tendencias/pedidosya-crecio-22-en-ordenes-en-2025-y-gano-peso-en-super-online — C3 [L] (pedidos de restaurantes +18,5%).
31. iProfesional, «El negocio del delivery en Argentina…», 15/10/2025 — https://www.iprofesional.com/management/439612-el-negocio-del-delivery-en-argentina-cuanto-dinero-mueve-y-cuantos-empleos-genera — C4 [L] (US$ 1.860 millones de ingresos en 2024, según Page Manager).
32. UADE CIS, «Dark kitchens…», 2026 — https://uade.edu.ar/media/yzvmw0kd/informe-cis-dark-kitchens-_con-agregado-carreras-uade.pdf — B4 [L]. No cuenta dark kitchens; dice que el punto de equilibrio es de 70 pedidos por mes frente a 2.938 cubiertos de un restaurante tradicional.
33. Chequeado, radiografía de repartidores (45.000 comercios según la prensa de PedidosYa) — https://chequeado.com/el-explicador/radiografia-de-los-repartidores-y-conductores-de-apps-en-argentina-quienes-trabajan-cuanto-ganan-y-por-que-crece-el-sector/ — C3 [S].
34. Fichas de Google Play: PedidosYa Portal https://play.google.com/store/apps/details?id=com.deliveryhero.pedidosyapartner&hl=es_AR&gl=AR ; RappiAliado https://play.google.com/store/apps/details?id=com.rappi.restaurants ; Rappi Partners https://play.google.com/store/apps/details?id=com.rappi.partners ; Fudo https://play.google.com/store/apps/details?id=do.fu.app — A1 como reseñas [L, bajadas con google-play-scraper].
35. App Store Argentina, PedidosYa Portal, reseñas — https://itunes.apple.com/ar/rss/customerreviews/page=1/id=6494987310/sortby=mostrecent/json — A1 [L].
36. Ficha de gastronomía de CABA, junio 2025 — https://buenosaires.gob.ar/sites/default/files/2025-07/Ficha%20Gastronom%C3%ADa%20-%20Junio%202025.pdf — A [S]: 30,2% de informalidad en 2024; al abrirla dio 404.
