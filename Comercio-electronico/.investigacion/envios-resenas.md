# Envíos y logística en Argentina: reseñas y quejas leídas una por una

Fecha de consulta: 2026-11-22. Ángulo: reseñas y quejas de comercios (y, aparte, de compradores), codificadas por tema. No se recomienda nada.

## Método

- Reseñas de comercios (tienda de apps de Tiendanube, categoría Envíos): la categoría tiene 71 apps (https://www.tiendanube.com/tienda-aplicaciones-nube/categorias/envios, 6 páginas). Escribí un script Playwright que abre el modal "Ver todas las evaluaciones", pulsa "Leer más" hasta cargar todo y extrae fecha, estrellas y texto de cada tarjeta (sin autor). Leí todas las reseñas de las 47 apps de envío que tienen al menos una: 1.734 de 1.734 publicadas (100 %, verificado contra el contador de cada ficha y contra la distribución de estrellas publicada). Quedaron afuera 3 apps que no son operadores de envío (Frete Hero 142, Rastreio.net 142, Agenda de Entregas 45) y las 21 apps con 0 reseñas.
- Codificación: leí una por una todas las reseñas de 1 a 3 estrellas (510), más las de 4-5 estrellas que mostraron texto negativo o mixto, y una muestra de las positivas largas. Los temas chicos (precio, cotización, cargos, saldo, alta de cuenta, seguros, cobertura, paros) los asigné a mano por número de reseña. Los temas grandes (soporte, integración, perdido/roto, demora, retiro, elogios) los asigné con reglas por oración que verifiqué con muestras de 12 a 14 reseñas por tema: las muestras mostraron falsos positivos (por ejemplo "pérdida de tiempo" leído como paquete perdido) que corregí con reglas, pero la precisión de los temas grandes es **supuesto** del orden de 80-90 %, no medida. Los elogios cortos genéricos y algunos elogios con contenido quedaron en "elogio genérico", así que los temas positivos están subcontados.
- Una reseña puede tener varios temas. Texto de la reseña manda sobre estrellas: encontré 22 reseñas de 4-5 estrellas con texto claramente negativo (1,8 % de las de 4-5 estrellas; probable error al puntuar) y las codifiqué como negativas.
- Las citas van con fecha y sin autor ni nombre de tienda.

## Respuesta corta

1. En las reseñas de comercios (1.734 leídas), lo que más se queja el comercio es del software de la integración y de que nadie responde, no del precio. Entre las 532 reseñas con texto negativo: 46 % habla de errores de integración, etiquetas, sincronización o de no poder dar de alta la cuenta; 33 % de soporte que no responde; 22 % de servicio físico (paquete perdido, roto, demorado, retiro que no pasan); 12 % de plata (tarifa alta, cotización distinta del cobro, cargos duplicados, saldo, seguro). Dato B/2 (muestra completa de una sola plataforma de reseñas, codificación propia).
2. Andreani (app para Tiendanube, 314 reseñas, 2,9 de promedio) concentra la queja en la herramienta: 117 de sus 195 reseñas negativas hablan de errores de integración/etiquetas/pagos. Todas sus reseñas son de 2025-2026, es decir, de la app nueva. Correo Argentino (393 reseñas, 3,7 de promedio, 238 de 5 estrellas y 109 de 1 estrella) concentra la queja en el servicio físico: 26 de sus 146 negativas hablan de paquete perdido/robado/roto, frente a 9 de las 195 de Andreani. Dato B/3 (mismas fuentes, comparación interna).
3. Cobros: la queja de plata más repetida es que el comercio paga más que lo que le cobró al comprador en el checkout (25 reseñas con ese tema, 12 de ellas de Correo Argentino), y el cobro duplicado al pagar etiquetas (16). "Precio alto" a secas aparece 14 veces; en cambio el precio bajo es el elogio principal de Correo Argentino ("el mejor precio para un servicio estándar"). Dato C/3 (pocos casos por tema).
4. Calificación de las apps con más reseñas, tomada de la ficha: Correo Argentino 3,7 (393), Andreani 2,9 (314), Envia Paquetería 4,5 (253), Pudo 4,5 (101), Postal Más 5,0 (80), Enviamelo 4,6 (74), Envíopack 3,3 (57), Vía Cargo 3,6 (57), shipnow 4,3 (31), OCA 3,2 (29), pickit 2,5 (23), Zipnova 4,2 (23), Moova 2,4 (19). Dato A/1 (leído de la ficha y recomputado de las tarjetas: coincide).
5. Del lado del comprador: en el portal privado defensadelconsumidor.com.ar (no es un organismo oficial) Andreani suma 347 denuncias y Correo OCA 309, por encima de Farmacity (342) y Fibertel (328) y por debajo de Mercado Libre (568) y Mercado Pago (996); Correo Argentino no figura en el top 20. En las 107 denuncias que leí (53 de Andreani y 54 de OCA, todas de 2026) el motivo dominante es incumplimiento de entrega (74 de 107 con esa etiqueta, más 20 con "incumplimiento del servicio"). Dato C/3 (portal privado, denuncias autodeclaradas). No encontré ranking oficial de Ventanilla Única Federal ni de COPREC que separe correos y paquetería (hueco).
6. Sesgos: las apps con 5,0 y muchas reseñas (Postal Más 80/80, Mile Logistic 21/22, Fast Mail 58/62, Bluemail 8/8) tienen perfil de reseñas pedidas; las de operadores grandes tienen más queja porque su app es obligatoria o masiva. Detalle abajo.

## 1. Tienda de apps de Tiendanube (comercios)

### 1.1 Fuentes y lectura

| Fuente | Tipo | Calificación | Marca |
|---|---|---|---|
| https://www.tiendanube.com/tienda-aplicaciones-nube/categorias/envios (lista de 71 apps con promedio y cantidad) | tienda de apps oficial de la plataforma | A / dato 2 | [L] |
| https://www.tiendanube.com/tienda-aplicaciones-nube/andreani2 | ficha + modal de evaluaciones | B / dato 2 | [L] 314 de 314 |
| https://www.tiendanube.com/tienda-aplicaciones-nube/correo-argentino | ídem | B / dato 2 | [L] 393 de 393 |
| https://www.tiendanube.com/tienda-aplicaciones-nube/envia-com | ídem | B / dato 2 | [L] 253 de 253 |
| .../pudo-ar, .../punto-postal, .../enviamelo, .../fastmail, .../enviopack, .../via-cargo, .../shipnow, .../oca, .../rapiboy, .../pickit-v2, .../zipnova-ar, .../mile-logistic, .../moova, .../envios-iflow-s-a, .../jipink, .../dhl-express, .../southpost, .../hop-envos, .../md-correo, .../realexpress, .../bluemail, .../cruz-del-sur, .../cabify-logistics, .../paaq y 23 apps con 1 a 5 reseñas | ídem | B / dato 2 | [L] todas |

Una nota de las fichas: la ficha de cada app dice "La atención para la app es ofrecida por el emprendedor" y muestra un "Resumen de opiniones generado por IA" (por ejemplo, en Zipnova: "Algunas quejas mencionan cobros extra y falta de respuesta ante problemas"). No usé esos resúmenes; leí las reseñas.

Las reseñas son de "tiendas" (comercios) que instalaron la app. Algunas reseñas llevan respuesta del desarrollador (por ejemplo Zipnova, 10 de octubre de 2026: "Lamentamos que Zipnova no sirva para tu caso de uso. Generalmente los vendedores que usan Zipnova valoran la posibilidad de gestionar todo en un solo lugar y contar con servicios de valor agregado como recolecciones, soporte y facturación unificada.").

### 1.2 Cuántas leí por app (todas) y estrellas

| App | Leídas / existentes | 1★ | 2★ | 3★ | 4★ | 5★ | Promedio calculado | de 2024 en adelante |
|---|---|---|---|---|---|---|---|---|
| Correo Argentino | 393 / 393 | 109 | 16 | 13 | 17 | 238 | 3,66 | 248 |
| Andreani | 314 / 314 | 127 | 33 | 25 | 12 | 117 | 2,87 | 314 |
| Envia Paquetería | 253 / 253 | 27 | 2 | 2 | 9 | 213 | 4,50 | 202 |
| Pudo | 101 / 101 | 11 | 2 | 0 | 1 | 87 | 4,50 | 6 |
| Postal Más | 80 / 80 | 0 | 0 | 0 | 0 | 80 | 5,00 | 80 |
| Enviamelo | 74 / 74 | 6 | 1 | 1 | 0 | 66 | 4,61 | 11 |
| Fast Mail | 62 / 62 | 0 | 0 | 1 | 3 | 58 | 4,92 | 16 |
| Envíopack | 57 / 57 | 20 | 3 | 3 | 3 | 28 | 3,28 | 7 |
| Vía Cargo | 57 / 57 | 18 | 2 | 1 | 1 | 35 | 3,58 | 55 |
| shipnow | 31 / 31 | 4 | 1 | 1 | 0 | 25 | 4,32 | 27 |
| OCA | 29 / 29 | 12 | 0 | 2 | 1 | 14 | 3,17 | 20 |
| Rapiboy | 25 / 25 | 2 | 0 | 0 | 1 | 22 | 4,64 | 18 |
| pickit | 23 / 23 | 14 | 0 | 1 | 0 | 8 | 2,48 | 23 |
| Zipnova | 23 / 23 | 4 | 0 | 0 | 3 | 16 | 4,17 | 3 |
| Mile Logistic | 22 / 22 | 1 | 0 | 0 | 0 | 21 | 4,82 | 22 |
| Moova | 19 / 19 | 11 | 2 | 0 | 0 | 6 | 2,37 | 2 |
| iFLOW | 17 / 17 | 4 | 1 | 0 | 0 | 12 | 3,88 | 2 |
| Jipink | 13 / 13 | 2 | 0 | 0 | 1 | 10 | 4,31 | 13 |
| DHL Express | 12 / 12 | 5 | 0 | 0 | 0 | 7 | 3,33 | 4 |
| Southpost | 12 / 12 | 1 | 0 | 0 | 0 | 11 | 4,67 | 6 |
| HOP Envíos | 11 / 11 | 1 | 1 | 0 | 2 | 7 | 4,18 | 11 |
| Cabify Logistics | 7 / 7 | 4 | 0 | 0 | 0 | 3 | 2,71 | 7 |
| PAAQ | 7 / 7 | 2 | 0 | 0 | 0 | 5 | 3,86 | 7 |
| Otras 24 apps (1 a 9 reseñas cada una: Skynde, Real Express, Bluemail, Cruz del Sur, Loginter, OCASA, DPD, Lightdata, Urbano Express, y otras) | 92 / 92 | 11 | 0 | 0 | 2 | 79 | n/d | 43 |
| **Total** | **1.734 / 1.734** | **396** | **64** | **50** | **56** | **1.168** | 3,89 | **1.147** |

Apps conocidas con 0 reseñas en la tienda de Tiendanube: Treggo, Welivery, Despacha, Envia Fulfillment, Smartpost, MiRuta.

Estrellas por período (todas las apps leídas):

| Período | n | 1★ | 2★ | 3★ | 4★ | 5★ | 1-2★ |
|---|---|---|---|---|---|---|---|
| Hasta 2023 | 587 | 130 | 16 | 10 | 20 | 411 | 24,9 % |
| 2024 a 2026 | 1.147 | 266 | 48 | 40 | 36 | 757 | 27,4 % |

Distribución por año de publicación: 2018: 5; 2020: 113; 2021: 200; 2022: 159; 2023: 110; 2024: 178; 2025: 570; 2026 (hasta el 22 de noviembre): 399. El salto 2025-2026 viene sobre todo de Andreani (todas sus 314 reseñas son de esos años) y Correo Argentino.

### 1.3 Temas: conteo (todas las apps; una reseña puede tener varios temas)

Grupos: Andreani = app Andreani; Correo Arg. = app Correo Argentino; Agregadores = Envia, Envíopack, Enviamelo, shipnow, Zipnova, iFLOW, Jipink, Lightdata, QuadMinds Flash, Mile Logistic; Otros = el resto (OCA, Pudo, Postal Más, Fast Mail, Vía Cargo, pickit, Moova, Rapiboy, etc.).

Quejas del comercio:

| Tema | Total | 2024-2026 | Andreani | Correo Arg. | Agregadores | Otros |
|---|---|---|---|---|---|---|
| Error de integración, etiqueta, sincronización, app | 237 | 178 | 122 | 57 | 27 | 31 |
| Soporte / atención que no responde | 195 | 109 | 43 | 43 | 57 | 52 |
| Queja genérica sin motivo ("pésimo", "no anda") | 125 | 92 | 49 | 40 | 17 | 19 |
| Paquete perdido, robado o roto | 63 | 35 | 9 | 26 | 12 | 16 |
| Demora, plazo incumplido, no entregan | 59 | 36 | 15 | 9 | 15 | 20 |
| Alta de cuenta / activación que no avanza | 42 | 37 | 2 | 8 | 9 | 23 |
| Cotización distinta del cobro real (el comercio paga más que el comprador) | 27 | 12 | 5 | 12 | 8 | 2 |
| Retiro / colecta que no pasan | 20 | 8 | 0 | 4 | 7 | 9 |
| Cargos extra, cobros duplicados, tarifas poco claras | 17 | 10 | 4 | 3 | 5 | 5 |
| Precio / tarifa alta | 15 | 10 | 3 | 4 | 6 | 2 |
| Seguro / siniestros que no se cubren | 13 | 4 | 3 | 1 | 7 | 2 |
| Cobertura, zonas, puntos de entrega | 10 | 5 | 1 | 1 | 4 | 4 |
| Saldo prepago, crédito, dinero retenido | 9 | 6 | 2 | 3 | 4 | 0 |
| Paros / medidas gremiales | 3 | 2 | 0 | 3 | 0 | 0 |

Elogios del comercio (subcontados, ver método):

| Tema | Total | 2024-2026 | Andreani | Correo Arg. | Agregadores | Otros |
|---|---|---|---|---|---|---|
| Elogio de soporte / atención | 253 | 117 | 6 | 5 | 116 | 126 |
| Elogio: la herramienta anda / es fácil | 217 | 124 | 15 | 21 | 108 | 73 |
| Elogio: entrega rápida / llega bien | 86 | 44 | 4 | 4 | 20 | 58 |
| Elogio de precio / costo | 51 | 17 | 2 | 5 | 22 | 22 |
| Elogio genérico sin contenido ("excelente", "recomendable") | 711 | 528 | 92 | 214 | 198 | 207 |

Entre las 532 reseñas con texto negativo (368 de 2024-2026): software y alta 246 (46 %; 190 en 2024-2026), soporte 173 (33 %), servicio físico 118 (22 %; 68 en 2024-2026), plata 66 (12 %; 35 en 2024-2026). Los porcentajes suman más de 100 por la superposición de temas. Calificación del dato: B/3.

### 1.4 Citas por tema (comercios, con fecha, sin autor)

**Error de integración / etiqueta / sincronización / app (Andreani y OCA son los más citados)**
- Andreani, 6 de abril de 2026, 1★: "Es un verdadero desastre. No puedo pagar las etiquetas, hay etiquetas que ya no se me generan automaticamente, es realmente un desastre. No puedo enviar mis pedidos, la voy a tener que desactivar"
- Andreani, 20 de abril de 2026, 1★: "mala sincronización. siempre tengo problemas para generar etiquetas, me cobran dos veces loe envíos. no se entiende qué es de envío nube o qué es del panel de andreani. no funciona nada bien."
- OCA, 12 de septiembre de 2023, 1★: "La app no funciona, me hicieron borrar la vieja porque la van a descontinuar y ésta no anda, da error inesperado y no podes generar ningun envio ni desde la venta ni desde el panel de OCA. No te pueden hacer cambiar por una que no funciona, cargar cada envio manualmente no es la idea, se pierden hor..."
- Andreani, 18 de diciembre de 2025, 3★: "tiene errores todavia, no aparecen las etiquetas cuando se pagan, debes poner el numero de operacion para que se te descarguen. Varias veces tira error al loguearse. Es buena la idea pero aun le falta para ser una solucion."

**Soporte que no responde**
- Andreani, 31 de octubre de 2026, 1★: "tuve varios inconvenientes de los cuales NINGUNO pude resolver ya que es IMPOSIBLE comunicarse con andreani, un desastre, los plazos de entrega fallaban y recibir muchisimos reclamos de mis clientes que hizo que tenga que dar de baja el servicio."
- Envíopack, 12 de enero de 2022, 1★: "Luego de mas de 4 años usando EnvioPack decidí dejarlo. La plataforma aunque es muy sencilla y funciona muy bien, siempre y cuando no tengas ningún problema. Cuando tenes cualquier mínimo problema es imposible recibir una respuesta de EnvioPack a tiempo y con una solución, espera al menos 72hrs."
- OCA, 16 de noviembre de 2023, 1★: "La aplicación es nefasa y el soporte es nulo ante un inconveniente, hasta que no se queden con 0 clientes no van a a ctivar un soporte a la altura."
- Zipnova, 4 de enero de 2024, 1★: "Malísimo. No hay forma de hablar con alguien para conocer la app, te hacen depositar plata sin tener ningún envio. Y los costos son superiores a Correo Argentino, para eso sigo directo con ellos."

**Paquete perdido, robado o roto**
- Correo Argentino, 14 de noviembre de 2023, 1★: "el peor servicio del mundo...de 15 paquetes me extraviaron 8, sólo me devolvieron 3 y se quedaron con los de más mercadería. una estafa! Ladrones"
- Correo Argentino, 28 de abril de 2025, 1★: "Realmente pésimo servicio. Productos bien embalados llegan rotos. Paquetes perdidos que nunca vuelven. Atención al cliente nula."
- Andreani, 24 de abril de 2026, 1★: "son unos chorros, 8 paquetes me perdieron en un mes y no se hacen cargo"
- Correo Argentino, 29 de julio de 2024, 1★: "Rompen muchos envíos"

**Demora / plazos incumplidos**
- Andreani, 11 de marzo de 2026, 1★: "Pésima experiencia. En cuanto la instalé envié 12 paquetes. Diez de ellos demoraron entre 15 y 25 días en llegar a los compradores, y no hubo con quien hablar. Bots y respuestas automáticas..."
- Andreani, 4 de marzo de 2026, 1★: "...ha llegado a tardar 15 días en entregar un paquete desde caba a Zárate."
- Envíopack, 24 de junio de 2022, 1★: "Son un verdadero desastre, pedidos sin entregar durante un mes, inclusive las consultas tampoco las responden. Realizo reclamo tras reclamo y nada"

**Retiro / colecta que no pasan**
- pickit, 11 de junio de 2026, 1★: "...envié 12 paquetes, algunos los perdieron, otros no lo retiraron por más de 15 días, son un desastre, el soporte no da respuesta, no pueden localizar donde se encuentra un paquete."
- pickit, 12 de febrero de 2026, 1★: "...Durante la época de las fiestas no retiraron los paquetes de los puntos de despacho el día 22 de diciembre, por ende todos los paquetes llegaron tardisimo."
- Enviamelo, 7 de junio de 2022, 1★: "Despues de dejar los envios en el punto de drop off, demoran hasta 5 dias en retirar, lo cual el seguimiento no actualiza y el cliente piensa que ni fue despachado. Envio al interior eternos, mas de 20 dias faciles."
- Correo Argentino, 3 de mayo de 2023, 1★: "Te cobran por servicio de Pick up y lo vienen a buscar cuando tiene ganas. Todos los meses tienen algún paro o medida de fuerza ¨gremial¨ y te dejan clavado (Eso si; te lo cobran igual)"

**Alta de cuenta / activación que no avanza (casi todo 2024-2026, sobre todo apps chicas y Vía Cargo, Pickit, Jipink, PAAQ)**
- Vía Cargo, 5 de octubre de 2026, 1★: "Descargamos la app en tiendanube, es imposible crear una cuenta y el chat y el chat bot tampoco funcionan"
- Vía Cargo, 11 de agosto de 2023, 1★: "hace mas de 1 mes que no me mandan el mail para activar mi cuenta, y nadie se hace cargo es una lastima, tengo varios clientes que lo usarían."
- Jipink, 29 de agosto de 2026, 1★: "Les tuvimos que escribir por email para activar la cuenta y jamás nos respondieron :/."

**Cotización distinta del cobro real (comercio paga más que lo cobrado al comprador)**
- Andreani, 13 de agosto de 2025, 1★: "cotiza mal.. al cliente le cobra una cosa y al generar la etiqueta quiere cobrar otra.. casi 3000 pesos de diferencia entre lo que paga el cliente con lo que debo pagar yo para generar la etiqueta! PESIMA!"
- Correo Argentino, 29 de agosto de 2022, 1★: "Absolutamente todas las veces me cotiza mal lo que va a terminar costando el envío y me tengo que hacer cargo yo. Pierdo plata con cada venta."
- Envíopack, 4 de mayo de 2021, 2★: "Me cobraban más de lo que le cobraban al cliente. Los reclamos tardaban muchísimo en responderlos y nunca me solucionaban el problema."
- Andreani, 5 de septiembre de 2025, 1★: "...entrando desde la cuenta personal en andreani y simular un envió de un producto el costo es tres veces menor de lo que figura en mi tienda nube."

**Cargos extra, cobros duplicados, tarifas poco claras**
- Moova, 20 de abril de 2021, 1★: "te cobran 2 veces los envíos por motivos desconocidos. El servicio al cliente es deplorable, te contestan48hs después..."
- shipnow, 22 de mayo de 2026, 1★: "...te cobran tarifas por todo (por demás) y no es una mensajería privada, sino que derivan a otras mensajerías para que realicen los envíos..."
- Zipnova, 5 de octubre de 2026, 1★: "Te hacen cargar credito en su pagina , y te cobran excedentes por el servicio , para eso entro en paq ar y las genero yo misma"
- Andreani, 24 de septiembre de 2025, 3★: "...una vez tuve que pagar 2 veces el envio porque cuando los pague me desconto la plata y no me dejaba descargar la etiqueta, asi que lo tuve que pagar de nuevo..."

**Precio / tarifa alta**
- Andreani, 18 de noviembre de 2025, 1★: "Envíos caros y pésima atencion al cliente"
- Envia, 9 de abril de 2025, 1★: "Tarifas Muy altas y no tiene cobertura en algunas partes del Pais, Tarimas que varian de los 120 pesos a los 500 para el envio de una gorra, Nos daremos de baja"
- shipnow, 9 de septiembre de 2025, 1★: "Empezo siendo bueno.. funcionaban bien los envios pero no vayan a sacarlos porqeu te cobran una fortuna!!"
- Correo Argentino, 17 de octubre de 2023, 1★: "...no podemos pagar 1500 pesos de envío para productos económicos como una pulsera de 1500 pesos a octubre de 2023..."

**Saldo prepago / dinero retenido**
- Correo Argentino, 11 de julio de 2024, 1★: "Es barato lo unico bueno, cada tanto le recargamos credito y no se acredita y por un par de dias no podemos enviar nada, un desastre."
- Envia, 10 de noviembre de 2024, 1★: "pones plata para cargar saldo y se te quedan con el dinero, cuidado con usar esta plataforma"

**Seguro / siniestros que no se cubren**
- Envíopack, 13 de mayo de 2021, 1★: "Dejo de utilizar Enviopack ya que -sin avisar por mail- dejaron de cubrir el seguro de los principales operadores como OCA y Andreani. Es decir, si venden algo y se pierde, Enviopack no se hace cargo del costo del producto."
- Envíopack, 1 de diciembre de 2021, 1★: "Pagar el seguro es una perdida de plata porque no se hacen cargo, tuve en el primer mes 5 siniestros..."
- Andreani, 13 de agosto de 2026, 3★: "No hay un canal real de ayuda para cobrar paquetes rotos o perdidos. Son pocos, pero por Instagram siempre empieza la charla nuevamente. Desgaste innecesario."

**Cobertura**
- pickit, 6 de junio de 2025, 1★: "No la pude instalar, dice que estoy fuera del área de cobertura, pero tengo un pickit point frente a mi negocio... raro."
- Envia, 9 de marzo de 2022, 1★: "no detecta los CP de las personas para calculas su envío y aparece como que no hay entregas"

**Paros / medidas gremiales**
- Correo Argentino, 26 de abril de 2025, 1★: "Un desastre el servicio, demoras de 20 dias. paquetes de rehen por cuestiones gremiales. Ni un comunicado de la empresa. Dada de baja."

**Elogio de precio**
- Correo Argentino, 9 de enero de 2023, 5★: "Funciona perfecto, las demás aplicaciones de correos tienen problemas con frecuencia. Correo Argentino NO. El mejor precio para un servicio estándar LEJOS."
- Correo Argentino, 22 de julio de 2022, 5★: "Probé todas las aplicaciones de envíos y Correo Argentino es la que tiene el mejor servicio, llega a todos lados y los mejores precios del mercado. Nunca un problema y enviamos hasta Tierra del Fuego."
- Correo Argentino, 28 de mayo de 2022, 5★: "Practica, bajo costo, despacho seguro y rapido"

**Elogio de soporte**
- Postal Más, 11 de octubre de 2026, 5★: "La atención es muy amable, siempre con buena predisposición para ayudar y resolver cualquier consulta..."
- Fast Mail, 28 de junio de 2021, 5★: "Excelente atención! super recomendable, ya que siempre tenemos respuestas inmediatas y tratan de ayudar en cualquier situación.!!"
- Andreani, 28 de octubre de 2026, 5★: "El soporte es excelente." (se refiere a la atención de una sucursal)

**Elogio: la herramienta anda / es fácil**
- Andreani, 24 de febrero de 2026, 5★: "Muy buena la aplicación! Esta buenisimo que pueda manejar todo desde el panel de la tienda y no tenga que salir de ahi."
- Correo Argentino, 7 de mayo de 2021, 5★: "Excelente. Y la integración se hizo en menos de 30 segundos. Muy bien"

**Elogio: entrega rápida / llega bien**
- Andreani, 26 de febrero de 2026, 5★: "Excelente servicio y puntualidad! Jamás tuve un inconveniente! Desde que dejas tu envío en la sucursal de Río cuarto hasta que le llega a mis clientas todo impecable"
- Correo Argentino, 24 de octubre de 2025, 5★: "Excelente servicio. Envío piezas muy frágiles. Todo llega perfecto."
- Postal Más, 15 de septiembre de 2026, 5★: "...Llegan a muchas zonas y dicen que en menos de 48 hs lo entregan pero la gran mayoria llega el mismo dia de la compra"

**Texto negativo con 5 estrellas (error de puntuación)**
- Correo Argentino, 28 de febrero de 2025, 5★: "Desastroso!!! Soy emprendedora… le cotizaron al cliente $3800 por el envio, cuando voy al correo a enviarlo, resulta que el envio me costó $13.000!!! Yo tuve que hacerme cargo de la diferencia!"

### 1.5 Lo que se ve por tipo de actor (lectura, inferencia mía)

- Operador con app propia y masiva (Andreani, OCA): la queja es la herramienta. Los comentarios de Andreani repiten un cambio de app: "la nueva app anda super lento", "Desde que hicieron la nueva app funciona peor que antes" y pedidos de volver a la integración vieja ("que vuelva la integración como antes porfavor"). En OCA (2023) pasa lo mismo: "me hicieron borrar la vieja porque la van a descontinuar y ésta no anda". Inferencia: una migración forzada de integración produce olas de 1★ visibles en fecha (Andreani, 2025-2026; OCA, 2023-2024).
- Correo Argentino: la queja es el servicio físico (rotura, robo, paro, visita que no ocurre, entrega a sucursal), y la valoración positiva es de precio. Los 5★ y los 1★ conviven: 238 y 109.
- Agregadores (Envia, Envíopack, Enviamelo, shipnow, Zipnova): la queja que los distingue es de intermediario: "no se hacen cargo" de un siniestro porque el reclamo depende del operador de atrás, y soporte lento. En Envíopack 2021, tres reseñas distintas dicen que dejaron de cubrir seguros o que no responden por siniestros.
- Última milla / puntos de entrega (pickit, Moova, Pudo, Enviamelo con drop off): la queja distintiva es el retiro que no pasa y el paquete que queda en el punto.
- Apps chicas: la queja distintiva es no poder dar de alta la cuenta ("nunca me respondieron para hacerme la cuenta").

### 1.6 Sesgos de esta muestra

- Reseña voluntaria: comercios muy enojados o muy contentos. No mide tasa de problema por envío.
- Reseñas pedidas: las fichas con 100 % de 5★ y muchas reseñas (Postal Más 80/80, Bluemail 8/8, Mile Logistic 21/22, Fast Mail 58/62) y los textos que nombran a personas del equipo ("Excelente atención de ...") apuntan a reseñas pedidas. Es una inferencia, no una verificación.
- La reseña es de la app y del servicio mezclados; el comercio no siempre distingue (por ejemplo Andreani: "EL SERVICIO DE ANDREANI LUEGO DE LIDIAR CON ESTA APP ES MUY BUENO. LA APP ES UN DRAMA").
- Muestra por operador desigual: 314 y 393 reseñas para dos y 1 a 29 para la mayoría.
- Solo comercios que usan Tiendanube y llegaron a la tienda de apps. No hay comercios de Mercado Libre ni de otras plataformas.
- Cambios de app y de reglas explican los picos por fecha; un 1★ de 2021 puede no describir el servicio de hoy.
- Codificación por reglas verificada por muestras (ver método).

## 2. Shopify App Store (Argentina)

| URL | Reseñas leídas / existentes | Estrellas | Marca |
|---|---|---|---|
| https://apps.shopify.com/zippin/reviews (Zipnova - Envíos) | 1 / 1 | 2★ | [L] |
| https://apps.shopify.com/shipnow/reviews | 1 / 1 | 5★ | [L] |
| https://apps.shopify.com/enviopack/reviews | 1 / 1 | 2★ | [L] |
| https://apps.shopify.com/escala-andreani-correo-argentino/reviews | 4 / 4 | cuatro 5★ | [L] |
| https://apps.shopify.com/shipy-app/reviews (páginas 1 y 2) | 13 / 13 | 4,1 promedio: 10 de 5★, 1 de 2★, 2 de 1★ | [L] (3 reseñas largas quedaron cortadas con "Mostrar más") |
| https://apps.shopify.com/correo-argentino-integracion/reviews | 8 / 8 | 1,1 promedio: una de 4★, una de 2★, seis de 1★ | [L] (2 cortadas con "Mostrar más") |
| https://apps.shopify.com/moova/reviews, https://apps.shopify.com/treggo/reviews, https://apps.shopify.com/urbano-express/reviews | 0 | "Aún no hay reseñas" | [L] |

Total leído en Shopify: 28 reseñas. Calificación: B/3 (muestra chica).

Las URL que probé y dieron 404 (no existe esa app con ese nombre): andreani, correo-argentino, oca, andreani-envios, oca-envios, andreani-argentina, pickit, envia, envia-com, enviamelo-1, iflow, pudo, cabify-logistics. Enviamelo y Pickit no pude cargarlos (sin salida en la lectura). Es hueco: no sé si esas empresas tienen app en Shopify con otro nombre. El buscador mostró dos apps de Argentina que sí existen y leí (Escala y Shipy).

Temas (28 reseñas, conteo aproximado a mano): elogio de soporte o de atención del dueño: unas 10 (Escala 4, Shipy 6); queja de soporte o trato del desarrollador: 5 (Zipnova 1, Envíopack 1, Shipy 3 reseñas negativas); alta de cuenta o activación que no avanza: 4 de las 8 de Correo Argentino Integración (por ejemplo "hace más de un mes estoy esperando que me activen una cuenta"); descuento Andreani: 3 elogios y 1 queja en Shipy; integración que "se clava" o falla: Shipy 1 y Correo Argentino 3.

Citas (Shopify, sin autor):
- Zipnova, 23 de enero de 2024, 2★: "la app funciona bastante bien, pero la realida que no hay atención al cliente, siempre te mandan a un mail donde tenes que enviarles un mail y es 0 personalizado."
- Envíopack, 23 de abril de 2026, 2★: "No brindan soporte telefónico, no responden los tickets, el ejecutivo abre la cuenta y desaparece."
- Correo Argentino Integración, 26 de junio de 2026, 1★: "Nunca validaron la cuenta... llevo meses esperando. Una perdida de tiempo. No hay informacion que explique como integrar."
- Correo Argentino Integración, 26 de abril de 2023, 1★: "Muy limitada en comparación con otras integraciónes de Correo en argentina para shopify... No se pueden ofrecer envíos gratis, sólo si tienes shopify plus" (reseña truncada en la lectura)
- Shipy, 12 de junio de 2026, 5★: "...cada vez que pago envios ya tiene el 30% OFF, no tengo que ni copiar cupon."
- Shipy, 11 de junio de 2026, 1★: "...prometían un 30% de descuento. El 30% de descuento funcionó una semana sola y después dejó de funcionar." (reseña truncada)
- Escala, 21 de septiembre de 2026, 5★: "muy buen soporte y app facil de manejar"

Sesgos: dos de las cuatro reseñas de Escala dicen "7 días / 18 horas / 3 horas usando la aplicación" y cuatro 5★ en un mes: perfil de reseña pedida (inferencia). Los desarrolladores de Shipy y Zipnova responden a las reseñas; algunas respuestas son hostiles hacia el comercio. No cito nombres.

## 3. Comunidad de vendedores de Mercado Libre y foros

Resultado: no pude leer hilos de vendedores, así que no hay conteo por tema. Es un hueco, no un hallazgo.

| Fuente | Resultado | Marca |
|---|---|---|
| https://comunidad.mercadolibre.com.ar/ | El dominio no resuelve desde el navegador (ERR_NAME_NOT_RESOLVED, 2026-11-22). | [M] |
| https://old.reddit.com/r/emprendedoresargentinos/search?q=envios&restrict_sr=on | 403 "blocked by network security" con el lector con navegador. | [M] |
| https://www.reddit.com/r/emprendedoresargentinos/search.json?q=envios+andreani | 403 por curl. | [M] |
| Búsquedas web de hilos de Reddit y de la comunidad de Mercado Libre | La búsqueda no devolvió hilos de Reddit ni de la comunidad; el cupo de búsquedas se agotó antes de poder repetir (ver al final). | [S] |

Lo único que llegó por buscador sobre Mercado Libre son blogs de herramientas (marcados): jaguarsheet.com, gobots.ai, klicko.com.ar, g2rocket.com y una nota de examedia.com.ar sobre aumento de costos a vendedores. Los usan para decir que Full cobra almacenamiento a partir de los 120 días y que el costo de Flex no aparece en la facturación. Son blogs de proveedores de software: calificación D/4, marca [S], sin números que yo haya verificado en la ayuda oficial de Mercado Libre. No los uso como dato.

## 4. Lado del comprador

### 4.1 Portal de denuncias (privado) defensadelconsumidor.com.ar

El sitio https://www.defensadelconsumidor.com.ar/ no es un organismo oficial (pie: "© 2019 Alus Creativos"); es un portal de denuncias y un servicio de asesoría de asociaciones adheridas. Calificación D/4.

Ranking de empresas más denunciadas (https://www.defensadelconsumidor.com.ar/ranking.php, leído el 2026-11-22 con [L]):

| Empresa | Denuncias |
|---|---|
| Personal (Telecom) | 1.782 |
| Telecentro | 1.270 |
| Mercado Pago | 996 |
| Viagogo | 950 |
| Flybondi | 926 |
| Musimundo | 684 |
| Fiat Planes (FCA Ahorro) | 662 |
| Mercado Libre | 568 |
| EPICO SA | 433 |
| Flow | 388 |
| Frávega | 366 |
| JetSmart | 366 |
| **Andreani** | **347** |
| Farmacity | 342 |
| Fibertel | 328 |
| **Correo OCA** | **309** |
| Directv | 304 |
| Pedidos Ya! | 278 |
| Tarjeta Naranja | 255 |
| Megatone | 246 |

Correo Argentino no aparece en el top 20 de ese portal (inferencia: tiene menos de 246 denuncias en el portal, o los reclamos a Correo Argentino se canalizan por otras vías). El portal no separa "correos" de "paquetería" como categoría. Los contadores cambian: un buscador mostró 314 y luego 346 para Andreani; en la lectura de hoy son 347.

Lectura de las denuncias (páginas 1 a 6 de cada empresa, 10 por página, ordenadas por fecha; todas de 2026):
- Andreani, https://www.defensadelconsumidor.com.ar/denuncias-empresa.php?id_empresa=412: 53 denuncias leídas, entre el 8 de abril y el 25 de octubre de 2026. Etiqueta del portal: incumplimiento de entrega de producto 41, incumplimiento del servicio 6, otro 4, estafa 1, falta de información 1.
- Correo OCA, https://www.defensadelconsumidor.com.ar/denuncias-empresa.php?id_empresa=390: 54 denuncias leídas, entre el 23 de enero y el 20 de noviembre de 2026. Etiqueta: incumplimiento de entrega 33, incumplimiento del servicio 14, cobros indebidos 2, estafa 2, producto defectuoso 1, incumplimiento de oferta 1, servicio defectuoso 1.

Temas que codifiqué (reglas sobre el texto completo, con lectura de las 107; indicativo, no exacto):

| Tema | Andreani (53) | OCA (54) |
|---|---|---|
| Paquete estancado, sin movimiento, demora | 24 | 14 |
| Sin respuesta (bot, 0800, mails, "cierran el caso") | 19 | 12 |
| "Dicen que pasaron por el domicilio y no es cierto" | 4 | 10 |
| Perdido, nunca entregado o marcado entregado sin serlo | 6 | 9 |
| Roto o dañado | 2 | 2 |
| Cobro indebido o reintegro | 4 | 2 |

Citas (sin autor):
- Andreani, 25 de octubre de 2026: "...falta de entrega de mi paquete, que figura en el seguimiento con estado “EN DISTRIBUCIÓN” desde el día 19 de septiembre, sin que hasta la fecha se hayan registrado nuevas actualizaciones."
- Andreani, 19 de octubre de 2026: "Envío despachado desde Córdoba el día 09/10 con fecha estimada de entrega el 16/10. [...] Causando esto muchas pérdidas economicas y descontento en clientes míos por demoradas en la entrega de sus pedidos" (el que reclama es un vendedor)
- OCA, 8 de mayo de 2026: "Dicen que pasaron por el domicilio y no es así! El día 8/5/26 estoy en casa todo el día..."
- OCA, 3 de agosto de 2026: "Llegan notificaciones de Visita a domicilio que no son ciertas, posponen la entrega una y otra vez. El servicio de atención al cliente no existe."
- OCA, 20 de marzo de 2026 (cobros indebidos): "COMPRE 2 CONTROLES CON ENVIO A DOMICILIO Y NUNCA ME LLEGARON, PERO SI ME COBRARON EL ENVIO, LO TUVE QUE RETIRAR DE SUCURSAL Y NO TE DEVUELVEN EL DINERO" (texto cortado en la lectura)

Aparece un patrón en OCA y en Correo Argentino: la queja de la "visita falsa" (el seguimiento dice que pasaron y el comprador estaba en casa). Cuando el denunciante es un vendedor (Andreani, 19 de octubre de 2026), el efecto es de clientes del comercio.

Sesgos: denuncia autodeclarada, sin verificar; los casos más graves se denuncian más; no hay denominador de envíos; el portal no es oficial.

### 4.2 Ventanilla Única Federal y COPREC (hueco)

- La Ventanilla Federal Única de reclamos de consumo se creó por la Disposición 890/2025 (dato por resumen de buscador, [S], sin leer la disposición en el Boletín Oficial). Las fuentes que encontré dicen que el sistema registrará los reclamos para generar estadísticas, y que esas estadísticas todavía no están publicadas.
- Un artículo de economiasustentable.com con un "top 5" de empresas denunciadas (bancos, billeteras, telecomunicaciones, prepagas, comercios) no menciona empresas de correo o logística. Sin fecha clara, [S].
- No encontré ranking de COPREC ni de la Dirección Nacional de Defensa del Consumidor que separe correos de paquetería. No busqué COPREC específicamente (cupo agotado). Es hueco.

### 4.3 Google Play

| App | URL | Resultado | Marca |
|---|---|---|---|
| Correo Argentino (com.correo.argentino) | https://play.google.com/store/apps/details?id=com.correo.argentino | 2,1 de promedio, 625 opiniones, más de 500.000 descargas, actualizada el 30 de julio de 2026 | [L] |
| OCA Mobile (ar.com.oca.mobile) | https://play.google.com/store/apps/details?id=ar.com.oca.mobile | "No se encontró la URL solicitada" el 2026-11-22; no hay reseñas para leer. Una búsqueda dentro de Play no la mostró. | [M] |
| Andreani | n/d | Solo aparecen apps de uso interno de Andreani (App Transportistas, Mobile Elecciones, AStore). No encontré una app de destinatario en Play. | [S] |

Correo Argentino en Play: leí 60 reseñas (las que cargó el panel al desplazarlo; orden "más relevantes", no "más recientes": no logré cambiar el orden). Estrellas: 56 de 1★, 2 de 2★, 1 de 3★, 1 de 4★, 0 de 5★. Fechas: 38 de 2026, 16 de 2025, 6 de 2024. La muestra está sesgada a negativas (el promedio global es 2,1 sobre 625 y esto es una submuestra, no una estimación).

Temas (60 reseñas, lectura una por una; una reseña puede tener varios):
- La app se cierra, se congela o no abre: unas 26.
- No se puede iniciar sesión o registrarse, o la app solo abre la web: 7.
- Cobro de la "autoridad de mesa" (uso electoral, que fuerza a bajar la app): 6.
- "Dicen que pasaron por el domicilio y no es verdad" (cartero): 8.
- Seguimiento que no se actualiza o sin información: 4.
- Perdí un pedido o paquete que no llegó: 3.
- Rótulos / etiquetas de envío con datos viejos o que obligan a entrar desde un dispositivo nuevo: 2 (son de comercios).

Citas (sin autor):
- 21 de octubre de 2026, 1★: "la aplicación no funciona, al abrir se congela y se cierra sola. tengo un teléfono con 8 de ram, el problema no es mi teléfono"
- 6 de mayo de 2026, 1★: "supuestamente dicen que pasaron y que no hay nadie pero, la realidad es que no vienen..."
- 3 de diciembre de 2025, 1★: "dice 'pasamos por tu domicilio y no estabas' cuando en real uno se la pasa esperando y esta adelante esperando, aunque pagues la..."
- 26 de noviembre de 2025, 2★ (comercio): "los envios siempre bien y siempre anda bien todo MENOS los rotulos. no puede ser que SIEMPRE que quiera hacer un envio tenga que entrar por un dispositivo nuevo para gene..."
- 21 de abril de 2026, 1★: "No estoy de acuerdo en que solo te den 5 días hábiles para retirar un paquete. Literal lo devuelven a remitente, sin tolerancia..."

Calificación: C/3. La app de Correo Argentino es una app de seguimiento (su ficha dice "Seguimiento de productos Paq.Ar en primera instancia, búsqueda de sucursales, CPA, token..."): la queja no mide el servicio de entrega, sino la app.

## 5. Cruces y límites

- Dónde coinciden comercio y comprador: la visita que no ocurre pero queda registrada (OCA, Correo Argentino y Andreani, en denuncias, y en Play), el paquete "estancado" en un centro y la falta de respuesta humana. Esto lo vive el comprador y el comercio (que "queda mal con mis clientes", frase repetida en reseñas de comercio).
- Dónde no coinciden: el comercio se queja de la herramienta (etiquetas, pagos, sincronización) y de la cotización; el comprador no ve eso.
- El comercio no nombra "Full" ni "Mercado Envíos" en las reseñas de la tienda de apps; quienes mencionan Mercado Libre lo hacen como canal que se ve afectado por la demora del operador ("me arruinaron la reputación en Mercadolibre", Cabify Logistics, 2026 y Moova, 2025).

## Huecos

- Hilos de vendedores de Mercado Libre (la comunidad no resuelve) y Reddit (403): sin dato.
- Ranking oficial de reclamos (Ventanilla Única Federal, COPREC, Dirección Nacional de Defensa del Consumidor) que separe correos y paquetería: no encontrado.
- Reseñas de apps de Andreani y OCA en Google Play: la app de OCA no está accesible y Andreani no tiene app de destinatario encontrada. Solo Correo Argentino (60 reseñas, orden por relevancia).
- Apps de Shopify de Enviamelo, Pickit, Envia y iFLOW: no localicé una ficha con ese slug.
- Tres reseñas de Shipy y dos de Correo Argentino Integración en Shopify quedaron cortadas ("Mostrar más").
- Los temas grandes no pasaron por doble codificación humana independiente.
- No leí las reseñas de las 3 apps no operadoras (Frete Hero, Rastreio.net, Agenda de Entregas) ni las de apps con 0 reseñas.

## Búsquedas: cupo agotado sí/no

Sí. Hice 11 búsquedas web (cinco para tienda de apps de Shopify y paquetes de Play, dos para el ranking de reclamos, dos para Reddit y Mercado Libre, dos para identificar apps); la última (comunidad de Mercado Libre) fue rechazada por agotarse el presupuesto compartido de la sesión. El resto de la lectura fue con el lector con navegador y scripts Playwright propios (fuera de ese cupo). Scripts y volcados quedaron en el scratchpad de la sesión (`/tmp/claude-1000/-home-dela-repos-nube-lind-negocio/cd230686-c7b6-4f41-8ad7-be90e5a6cb07/scratchpad/`: `resenas-tn2.mjs`, `play.mjs`, `rev/*.json`, `final.json`).
