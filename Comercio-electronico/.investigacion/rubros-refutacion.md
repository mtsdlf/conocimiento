# Rubros: refutación del borrador de la zona «rubros con necesidades propias» (consulta 2026-11-22)

Revisión adversaria del borrador `el-taller/analisis/2026-11-22-el-bosque/zonas/rubros.md` (repo de Lind) contra sus cinco informes crudos y contra las fuentes reabiertas. Busca refutar, no confirmar. Sin WebSearch (cupo agotado): todo se reabrió con `curl` sobre URL que ya estaban en los informes, y el texto se extrajo con un script.

## Qué se pudo reabrir y qué no

**Reabierto y leído (curl, 200):**

- Mercado, 06/02/2026, adelanto de CACE (ranking de categorías).
- Mercado, 19/03/2026, **estudio anual final de CACE** ($34.033.238 millones). Estaba citado como [S] en `rubros-otros.md` (fuente 11) y resultó decisivo.
- fu.do/es-ar/precios, bistrosoft.com/ar/precios, info.pedix.app/ar, maxirest.com.ar, pricing.olaclick.app/es.
- Letra P, 14/04/2026 (Rosario).
- iProfesional, 14/05/2026 (comisiones), 16/07/2026 (Uber y Delivery Hero), 02/07/2021 (topes con FEHGRA), 25/04/2025 (cautelar de farmacias) y 24/07/2026 (Mercado Libre con receta).
- borisreturns.com/precios.
- Ficha de Peça Certa, de Tilo y de Gestión de Cambios en la tienda de apps de Tiendanube.
- Ayuda de filtros de Tiendanube, versión es_MX (la es_AR redirige a una página de login).
- Ayuda de cambios y devoluciones de Tiendanube (es_ES).
- Documentación de compatibilidades de Mercado Libre, versión `/es_ar/`.
- Los dos PDF de ExpoFerretera (2019 y 2023).
- Boletín Oficial: Resolución MS 638/2026 y Disposición ANMAT 4714/2026.
- Algoritmo Digital (calculadora de Mercado Libre de enero de 2026) y la de septiembre de 2026 que esa página enlaza.
- Mellium10 (comisión de Accesorios para Vehículos).

**No reabierto:** las reseñas de Google Play y del App Store (no se volvieron a bajar; los conteos de reseñas se verificaron solo por aritmética contra los informes), La Capital 2024, El Economista (parque automotor), StoreLeads, Promotive y la página de comisiones de Mercado Libre (el informe ya registró un 403; la calculadora de septiembre de 2026 carga las comisiones por JavaScript y no da el número por categoría).

**Conteo CEP XXI:** recalculado con un script (`python3 -I`) sobre los tres CSV. Resultado en la sección siguiente.

## 1. Conteo CEP XXI: recálculo

| Rubro (2022) | Informe | Recálculo | Veredicto |
|---|---|---|---|
| Gastronomía, locales | 25.134 (21.685 en 2021) | 25.134 (21.685) | Se sostiene |
| Gastronomía, puestos | 179.687 | **179.657** | Error de tipeo de 30 en el informe; no cambia nada |
| Autopartes al por menor | 6.541 (6.263) | 6.541 (6.263); puestos 23.835 | Se sostiene |
| Ferretería y construcción, locales | 14.102 (13.312) | 14.102 (13.312) | Se sostiene |
| Ferretería y construcción, **puestos** | 53.044 | **60.014** (la suma de las 8 clases que el mismo informe lista da 60.014) | **No se sostiene.** Importa para el cruce con la cámara (ver 4) |
| Farmacia | 10.385 | 10.385 | Se sostiene |
| Indumentaria | 17.894 (16.433) | 17.894 (16.433) | Se sostiene |
| Calzado | 3.898 | 3.898 (477220 + 477230; deja afuera marroquinería 477290, bien) | Se sostiene |
| Mayoristas: autopartes 2.146, motos 1.325, ferretería + construcción 2.531 | — | 2.146 / 1.325 / 2.531 | Se sostiene |
| Óptica 2.225, mascotas 1.913, muebles 2.528, alimentos 25.257 | — | iguales | Se sostiene |
| Empresas por CLAE3, oct. 2023: 453 = 7.414, 561 = 20.117, etc. | — | iguales; la serie termina en 2023-10 | Se sostiene |

Detalle de clases de gastronomía, autopartes y ferretería: todos los números coinciden. Ojo con el paso 2 de gastronomía: la clase 561014 que se resta como «bares» incluye **cafeterías** según el diccionario («bares, cervecerías, pubs, cafeterías»), que sí venden por app. Restarlas es un supuesto más fuerte de lo que dice el borrador.

## 2. Respuesta primero y totales

| Afirmación del borrador | Veredicto | Evidencia |
|---|---|---|
| «Se leyeron 754 reseñas (400 + 77 de autopartes **más 63 mensajes** + 62 + 214 + 1)» | **No se sostiene como está escrito** | 400 + 77 + 62 + 214 + 1 = 754. Con los 63 mensajes, el paréntesis suma **817**. Corrección: «754 reseñas, más 63 mensajes de un foro». |
| «Solo las de gastronomía y moda son, en su mayoría, de comercios argentinos del rubro» | **No se sostiene para gastronomía; con matiz para moda** | Gastronomía: las argentinas son como mucho las 180 de PedidosYa (Play: «mayoría rioplatense, con algunas de Bolivia, Chile o Perú»), o sea ≤ 45% de 400. Rappi (152) es «mayoría de México y Colombia», y en Fudo (68) «muchas son de mozos y no de dueños». Moda: las 214 son de la tienda argentina, pero 79 (Abejita) son «muchas en portugués» y posiblemente infladas. |
| Tabla: «400 (unas 180 argentinas)» | Con matiz | «Hasta 180, en su mayoría argentinas». |
| «Moda, el rubro con más evidencia de que se paga por resolver su dolor propio» | **Con matiz, discutible** | Gastronomía tiene más evidencia de pago: cinco programas con precio público, Fudo dice 35.000+ negocios y comisiones del 25% al 35%. En moda, Boris dice en su propia página «Más de 120 tiendas confían en nosotros» (dato nuevo, leído): frente a 26.000–30.000 marcas, la adopción paga es chica. |
| «Al menos cuatro apps argentinas que cobran de $14.999 a $260.000» | **No se sostiene** | Los informes nombran **tres** apps de cambios (Boris, Undo, Gestión de Cambios); las de etiquetas (Enviamelo, Shipnow, Zipnova) no gestionan el cambio. Undo no publica precio. Los $14.999 de Gestión de Cambios son [S]: la ficha reabierta solo dice «Compras en la app». El único precio leído es el de Boris. |
| «205 de 214 reseñas con 5 estrellas: gustan» | Con matiz | Incluye 79 de una app de **talles** (Abejita) señaladas como posiblemente infladas. Para afirmar que las apps de **cambios** gustan hay que contar solo sus 100 reseñas (Boris 51, Undo 43, Gestión 6), y el informe no las separa por estrellas. |

## 3. Gastronomía

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| Comisión de PedidosYa del 25% al 35% como «estimación de la consultora Focus Market» | **No se sostiene la atribución** | En la nota de iProfesional del 14/05/2026, leída entera, Focus Market aparece solo por la caída de 12% del poder adquisitivo. El «PedidosYa: aplica cargos que oscilan entre el 25% y el 35%», el «no superan el 25%» de Rappi y el «cercano al 13%» de Mercado Libre son afirmaciones de la redacción, sin fuente. Corrección: «dato de prensa sin fuente citada (iProfesional, mayo de 2026), coherente con lo que dicen comercios de Rosario». Lo mismo vale para el 13% de Mercado Libre. Baja la fuente de B3 a C4. |
| «Una cámara de Rosario dice hasta 35% semanal… y que el local paga el 85%» | Con matiz | Letra P lo confirma, pero la «cámara» es la que **acaban de formar tres firmas** de hamburgueserías para negociar con Rappi (parte interesada), y la cita es de uno de sus dueños. La misma nota dice que Rappi «afronta ellos mismos los reclamos». El 30%–80% es **de los pedidos**, no de las ventas. |
| Hueco «Los reclamos los paga el local **sin poder apelar**»: fuerte como dolor | **Con matiz; el «sin poder apelar» no se sostiene** | La cita que trae el propio borrador dice que se puede apelar con una foto del pedido: la apelación existe y es difícil. Según Letra P, en Rappi Argentina el reclamo lo absorbe la app; las 13 reseñas de Rappi son mayormente de México y Colombia. Corrección: «en PedidosYa, los reclamos los paga el local y apelar es difícil»; fuerte como dolor solo en PedidosYa. |
| Hueco «Lo que cobra la app y no se explica»: **fuerte** | Con matiz | Las 42 reseñas mezclan «comisión alta» (lo que se sabe y duele) con cargos no explicados (lo opaco); no están separadas. La «cámara» son tres firmas y la nota de iProfesional no cita fuente. Como dolor, fuerte; como hueco que alguien de afuera pueda atender, **sin medir** (el propio borrador dice que no se buscó si alguien audita liquidaciones). |
| Rango de 8.000 a 35.000 locales que venden por app | **No se sostiene como piso y techo** | **Techo:** el borrador dice «el padrón más los no empleadores», pero no hay número de no empleadores. El 35.000 sale de un supuesto que está en el informe y no en el borrador: entre la mitad y tres cuartos de los 45.000 de PedidosYa (22.000 a 34.000). Esa cifra cuenta sucursales y otros rubros, y la da quien vende. **Piso:** los 8.071 asumen que todo fast food, heladería y rotisería vende por app (sin medir), y dejan afuera a los restaurantes con mesa que hacen delivery. El paso 2 (23.300) no se usa en ninguna parte. Corrección: «orden de magnitud de 10.000 a 35.000, con las dos puntas como supuestos». La fuerza «débil» queda bien. |
| Software «de $12.000 a $101.800 por mes» | **Con matiz** | Los precios se confirman en las páginas: Fudo $23.900 / $46.500 / $93.500 con impuestos incluidos; Bistrosoft $21.600 a $101.800 **+ IVA**; Pedix $19.000 a $35.000; Maxirest, $36.125 a $89.000, aunque la cabecera de su página dice «desde $34.000». Pero los $12.000 de OlaClick son un **precio con descuento** (lista $14.118), y OlaClick llega a **$245.000** (también con descuento; lista $288.235). El rango del borrador corta a OlaClick por arriba y no por abajo, y mezcla precios con y sin IVA. Corrección: «planes base de $12.000 a $101.800 (hasta $245.000 en el plan más alto de OlaClick), con y sin IVA según el proveedor». |
| Fudo: tienda con 1,9% + IVA y tope de $99.000 | No se pudo verificar | Está en la página de delivery, que no se reabrió. La página de precios confirma los planes y que los precios son finales. |
| Topes con FEHGRA (10% o 18% + IVA), vencidos el 30/09/2021 | Con matiz | iProfesional 2021 confirma los topes y la prórroga «hasta el 30 de septiembre». Que **no** se haya vuelto a prorrogar es inferencia: el propio informe cita una multa de 2022 en Santa Fe que habla de topes de 18% y 21%. |
| Uber compra Delivery Hero por US$ 14.800 millones; falta la aprobación de competencia | Se sostiene (sube de [S] a [L]) | Nota leída: «disparará alarmas en autoridades de competencia». |
| Liquidación «hoy es semanal» | Con matiz | Es el ciclo nominal: 12 reseñas hablan de liquidaciones que llegan menos o tarde, una de «más de 2 meses». |
| Cuentas de ejemplo ($9.075 contra $575; Pedix, unos 3 pedidos) | Se sostienen | Aritmética correcta. |
| Conteo de reseñas: 149 + 31 + 152 + 68 = 400; negativas 131 + 27 + 140 + 32 = 330 | Se sostiene | — |
| Rappi Partners como A1 «sobre el modelo» | Con matiz | La página muestra RUC y un prefijo +593: es una plantilla regional. |

## 4. Autopartes

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| 8.400 a 16.800, centro de 11.000 | **Aritmética bien; rango y «centro» con matiz fuerte** | 5.600 × 1,5 = 8.400 y 5.600 × 3 = 16.800. El «centro de 11.000» no es el punto medio (12.600): es el caso de 1 monotributista por empresa, sin decirlo. El tramo de 0,5 a 2 no tiene fuente, y en la economía la proporción es de unos 4 a 1. Con esa proporción da unos 28.000, así que 16.800 no es un techo. Además, el rango cuenta **empresas (CUIT)** y no locales, a diferencia de los otros rubros de la tabla, y el 1,17 mezcla 2022 con 2023. Corrección: «de 8.400 a 16.800 si hay entre 0,5 y 2 monotributistas por empresa (supuesto), en CUIT, no en locales»; sacar el «centro». |
| Ranking de CACE: 9.º por facturación y 6.º por unidades | **Se sostiene para el adelanto; no para el estudio final** | Mercado, 06/02/2026, leído: sin elisiones, quedan 9.º y 6.º. Pero en el **estudio anual final** (Mercado, 19/03/2026, leído) el orden por facturación es: Pasajes; Alimentos; Equipos de audio y TI; Hogar; Electrodomésticos; Deportes; **Indumentaria (no deportiva)**; **Accesorios para autos, motos y otros vehículos (8.º)**; Cosmética; Artículos de oficina; **Materiales y herramientas de construcción (11.º)**; Infantiles. El final no publica el orden por unidades. |
| Comisión de Mercado Libre: 13% Clásica y 18,5% Premium + IVA | Con matiz | Mellium10 reabierto: «Datos 2026», «Valores aproximados», sin fecha. Mercado Libre cambió sus costos el 1/09/2026 (lo dice Algoritmo Digital), así que puede ser anterior. Fuente C4, una sola. |
| Peça Certa: ARS 10.593,62, sin base de vehículos, 0 reseñas | Se sostiene | Ficha: «La app no incluye una base automotriz precargada ni consulta por patente o placa». |
| Tiendanube: «no es posible agregar filtros adicionales» (A2, [L]) | Con matiz | Texto confirmado, pero en la versión **es_MX** de la ayuda; la es_AR pide login. |
| Mercado Libre: desde el 15/07/2026 la API ya no deja editar ni copiar las compatibilidades del catálogo | Se sostiene, con matiz | Doc es_ar, actualizada el 12/11/2026: «solo lectura resumida (marca y total)… modificaciones y eliminaciones estarán disponibles únicamente desde la plataforma de Mercado Libre». Solo alcanza a las compatibilidades **del catálogo**; las que carga el vendedor siguen manejándose por API. |
| Hueco «Lo cargado en Mercado Libre no se lleva a otro canal»: **media** | **No se sostiene como está redactado; bajar a débil** | Lo que carga el vendedor sí se maneja por API; lo restringido es lo que pone el catálogo de Mercado Libre. Sin quejas leídas. Corrección: «las compatibilidades que sugiere el catálogo de Mercado Libre no se pueden leer en detalle por API desde el 15/07/2026: **débil**». |
| Hueco «Datos de compatibilidad argentinos para la tienda propia»: **media** | **Inflada; bajar a débil-media** | La evidencia de dolor son 6 reseñas de Shopify de EE. UU. y otros países, más foros de eBay. Ninguna queja argentina, y no se sabe si Promotive o la cámara le venden a un comercio chico. El hueco de oferta es real (los datos no llegan a la tienda), pero el dolor local no está medido. |
| «No hay filtro por vehículo»: fuerte el hecho | Se sostiene como hecho | Lo dicen las ayudas oficiales. Peça Certa trae el buscador: lo que falta es el dato, no el filtro. |

## 5. Ferretería y construcción

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| 14.000 a 24.000 locales; «el piso y la cámara coinciden en orden de magnitud» | **No se sostiene la coincidencia; techo arbitrario** | Se compara el total de la clase 4752 (14.102, con corralones, pinturerías y aberturas) con «15.000 ferreterías» de la cámara. Ferretería sola en el CEP es 4.950: contra 15.000, el triple. El techo suma 15.000 + 9.150, como si la cámara contara solo ferreterías. Pero sus **50.000 empleados** se parecen al empleo de **toda** la clase (60.014 recalculado, no 53.044) y no al de la ferretería sola (15.520). Y en 2019 dijo «desde comercios unipersonales» (incluye no empleadores). Las dos lecturas dan otros rangos: si la cámara cuenta todo, unos 15.000 más los monotributistas de los otros rubros; si cuenta solo ferreterías, unas 10.000 ferreterías sin empleados, y los no empleadores de corralones y pinturerías llevan el techo bastante arriba de 24.000. Corrección: «piso 14.102 locales con empleados; techo no medible hoy; la cámara dice 15.000 ferreterías sin aclarar qué cuenta». |
| Catálogo de 22.000 a 77.000 artículos «lo dice la cámara» | Con matiz | PDF de 2023 reabierto. El texto exacto es «Ventas de entre 22.000 y 77.000 artículos, según el tamaño del comercio». Es ambiguo (pueden ser referencias en venta o unidades); lo más probable es que sean referencias. Además, es un dato de feria, sin método. |
| CAFARA: 14.000 empresas, 34.000 empleados, 90% de barrio (2019) | Se sostiene | PDF de 2019 reabierto. |
| ExpoFerretera: más de 13.000 visitantes en 2023 | Se sostiene | PDF de 2023. |
| Mercado Libre, Herramientas y construcción: 13% a 17% | **Vencido** | Algoritmo Digital reabierto: «desde el 1 de septiembre de 2026 rigen costos nuevos… esta página conserva los valores anteriores». El informe lo anotaba y el borrador lo omite. También omite que esa tabla pone la Clásica (14%–17%) más cara que la Premium (13%–16%). Corrección: «13% a 17% hasta agosto de 2026 (D3); la tarifa vigente no se pudo leer». |
| Cuenta de ejemplo: unos $111.000 por mes contra 7 a 9 pedidos en Mercado Libre | Con matiz | 79.999 + 24.000 + 7.000 = 110.999: bien. Pero 111.000 / 17.000 = 6,5 y 111.000 / 13.000 = 8,5, y a diferencia del ejemplo de gastronomía no suma el IVA a la comisión; con IVA da 5,4 a 7 pedidos. Además usa la tarifa vencida. |
| Tilo, de $24.000 a $49.000 por mes | Se sostiene | Ficha reabierta: «Emprendedor: $24.000 por mes, precio final… Comercio: $49.000». |
| [L] en el informe de ferretería | Con matiz | El informe aclara que su [L] es «el texto que llega como resumen de un modelo chico» (WebFetch), no lectura entera; las 62 reseñas se leyeron así. El borrador define [L] como «leído entero». |
| Reseñas: 62, con 54 negativas | Se sostiene | 20 + 23 + 7 + 12 = 62; 14 + 11 + 11 + 5 + 4 + 4 + 2 + 3 = 54 negativas, más 8 positivas. A la tabla del borrador le faltan las filas «importación CSV (2)» y «otros (3)». |
| Huecos: precios «media», lista del proveedor «media» | Con matiz | «Mantener precios», media: aceptable por el dato de la cámara y la prensa de 2022–2023, con la inflación más baja como contrapeso. «Pasar la lista del proveedor», media: no hay ninguna queja de ferretero y la función la ofrecen sistemas (la cifra de Fidel es D4, de una página espejo). Bajar a **débil-media**. |

## 6. Indumentaria y calzado

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| 26.000 a 30.000 marcas de moda online | **No se sostiene el piso** | 65.000 × 0,46 = 29.900, bien. Pero el 0,40 no tiene fuente: el dato que hay para la punta baja es 44% (2021). Y el borrador cita 70.000 marcas en 2026 sin usarlas: con 44%–46% sobre 65.000–70.000 da **28.600 a 32.200**. Además aplica una proporción de facturación a una cantidad de tiendas (el supuesto ya está marcado). Corrección: «unas 28.000 a 32.000 (supuesto)». |
| «Salió del top de CACE» | **No se sostiene** | En el estudio final (Mercado, 19/03/2026, leído), «Indumentaria (no deportiva)» es **7.ª por facturación**. En el adelanto tampoco salió del top por unidades: «Indumentaria deportiva» aparece 8.ª. `rubros-otros.md` citaba esa nota como [S] para decir lo contrario. |
| «Bajo presión: cayó 14% nominal en la plataforma más grande» | Con matiz | El mismo informe trae que moda facturó $850.047 millones (+53,1%) en esa plataforma y que la contradicción no está resuelta. El borrador cita solo la baja. |
| Boris: $30.000 a $260.000 | Se sostiene | Tabla reabierta: ARS por defecto, sin IVA aclarado. Dato nuevo: «Más de 120 tiendas». |
| Gestión de Cambios: $14.999 | No se pudo verificar | La ficha dice «Compras en la app»; el número sigue siendo [S]. |
| Ejemplo: 50 cambios, $55.000 por mes, $660.000 por año, media venta | Se sostiene | 55.000 / 104.311 = 0,53. |
| Hueco «el cambio de talle no viene en la plataforma»: **fuerte** como dolor | **Inflada; bajar a media** | El dolor sale de 16 relatos de «antes» y 15 sobre el talle, en reseñas con sesgo positivo fuerte de clientes de las apps. No hay tasa de cambios argentina (el 50% citado es internacional, de 2020), ni prensa, ni cámara. Y la adopción paga es chica (Boris, más de 120 tiendas). Que la ayuda de la plataforma lo derive a apps sí se confirma (la página nombra a Boris y a Undo). |
| «Talles sin estándar nacional»: media | Inflada; bajar a débil | Sostenida por una nota [S] sobre la ley y una reseña. |
| 214 reseñas: 43 + 51 + 6 + 12 + 79 + 17 + 4 + 1 + 1 | Se sostiene | Estrellas: 205 + 5 + 4 = 214. |

## 7. Farmacia

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| «La venta online de medicamentos sigue trabada por dos cautelares» (respuesta primero) | **No se sostiene como hecho** | Según iProfesional (25/04/2025, leído), la cautelar suspende las disposiciones del DNU que «habilitaban… la venta de medicamentos de venta libre en establecimientos no farmacéuticos»: no habla de internet. Que alcance a la venta online lo dice el sindicato (iProfesional, 24/07/2026: «Según la organización sindical…»), y Mercado Libre vende con receta en CABA sin fallo en contra. El cuerpo del borrador y su tabla de correcciones lo dicen bien; la respuesta primero y el hueco «no medible por la disputa judicial» lo presentan como hecho. Corrección: «la venta de venta libre fuera de la farmacia está suspendida por cautelares; si eso alcanza a la venta por internet está en disputa». |
| Resolución 638/2026: dispensa digital, 180 días corridos, vence cerca del 3/12/2026 | Se sostiene | Boletín Oficial reabierto. Art. 1: «Las farmacias deberán utilizar sistemas de gestión que adopten mecanismos digitales para la validación y registro del acto de dispensa». Art. 8: «cumplimiento inmediato» con 180 días corridos. Art. 10: vigencia al día siguiente de la publicación (06/06/2026), así que vence el 03/12/2026. |
| Disposición ANMAT 4714/2026: diez principios activos a venta libre, nada de internet | Se sostiene | BO 28/07/2026 (firmada el 27/07). El art. 1 habla de trimebutina; no aparece «internet» ni «electrónico». |
| Hueco «adecuarse a la dispensa digital»: media | Inflada como hueco; bajar a débil | La obligación es A1, pero el hueco (que la farmacia independiente no tenga quien se lo resuelva) descansa en una sola fuente [S], y Farmalink, Winfarma, Zetti y Galbop ya venden eso. Es dolor obligatorio, probablemente atendido. |
| 10.385 a 12.000 | Con matiz | Los 12.000 son «farmacias de barrio» (sin cadenas), C3 [S]: con las cadenas, el total sería mayor. No miden lo mismo que el CEP. |

## 8. Correcciones al barrido

| Corrección del borrador | Veredicto |
|---|---|
| Autopartes 9.º, construcción 10.º por facturación | Se sostiene para el **adelanto**. En el estudio final, autopartes es 8.º, construcción 11.º e indumentaria no deportiva 7.ª. Hay que decir de qué versión es cada puesto y preferir la final. |
| Construcción 2.ª por unidades y +117% | Se sostiene en el adelanto; el final no los publica. |
| «PedidosYa 25%–35%… se confirma, como estimación de una consultora» | **No se sostiene la atribución** (ver 3). |
| Liquidación semanal | Con matiz (ver 3). |
| Fudo «35.000+» y precio oficial | Se sostiene en los precios; los 35.000+ no se reverificaron. |
| CADAM no es la cámara de corralones | No se pudo verificar ([S]). |
| Moda: «sin herramienta argentina» se cae | Se sostiene que hay herramientas; no que sean «al menos cuatro» de cambios (son tres). |
| Farmacia: el decreto habilita la góndola; restringen las cautelares | Se sostiene (Boletín Oficial y notas leídas). |

## 9. Nombres de personas

- **El borrador está limpio:** no aparece ningún nombre de persona. La nota de Letra P nombra al dueño de las hamburgueserías y el borrador no lo trae.
- **Dos informes crudos tienen nombres en URL:**
  - `rubros-otros.md`, fuente 27: la URL de la tesis de UdeSA lleva el nombre completo de su autor.
  - `rubros-ferreteria-y-construccion.md`, fuente 29: la URL de mintlify.wiki lleva un usuario de GitHub con forma de nombre propio.
  - Hay que sacar esas URL o reemplazarlas por una descripción, como ya se hizo con la fuente 39 (CADAM).

## 10. Contradicciones entre informes

- `rubros-otros.md` («salió del top de facturación de CACE», fuente 11 [S]) contra la nota de esa misma fuente: Indumentaria es 7.ª.
- `rubros-gastronomia.md` atribuye el 25%–35% a Focus Market; la nota no lo hace.
- `rubros-conteo-propio.md`: 53.044 puestos en ferretería, cuando la suma de las clases da 60.014. 179.687 en gastronomía, cuando da 179.657.
- `rubros-ferreteria-y-construccion.md` trae los costos de Mercado Libre vencidos con su advertencia; el borrador la pierde.
