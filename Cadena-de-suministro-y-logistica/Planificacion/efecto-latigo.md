---
resumen: >-
  El efecto látigo es la amplificación de la variabilidad de la demanda a medida que se sube por la cadena: cada eslabón le pide a su proveedor con más variación que la que tienen sus propias ventas. Lee, Padmanabhan y Whang le encontraron cuatro causas estructurales y Sterman una de comportamiento; los datos muestran que lo tienen dos de cada tres empresas, con una magnitud moderada.
estado: borrador
estabilidad: estable
fuentes:
  - "Lee, Padmanabhan y Whang (1997), Information Distortion in a Supply Chain: The Bullwhip Effect, Management Science 43(4):546-558; abstract, introducción y tabla 1 (copia en PDF de un curso universitario): https://courses.ie.bilkent.edu.tr/ie102/wp-content/uploads/sites/12/2019/02/Lee-Padmanabhan-Whang-1997-MS.pdf"
  - "Sterman (1989), Modeling Managerial Behavior: Misperceptions of Feedback in a Dynamic Decision Making Experiment, Management Science 35(3):321-339, abstract: https://doi.org/10.1287/mnsc.35.3.321 (según el resumen)"
  - "Forrester, Industrial Dynamics: A Major Breakthrough for Decision Makers, reedición en The Roots of Logistics (Springer, 2012), pp. 141-172, solo el registro: https://doi.org/10.1007/978-3-642-27922-5_13"
  - "CSCMP, Supply Chain Management Terms and Glossary (2013), entrada bullwhip effect (copia no oficial): https://www.cisco-eagle.com/uploads/cscmp/cscmp-glossary.pdf"
  - "Wikipedia, Bullwhip effect (secundaria, para el juego de la cerveza): https://en.wikipedia.org/wiki/Bullwhip_effect"
  - "Cachon, Randall y Schmidt (2007), In Search of the Bullwhip Effect, MSOM 9(4):457-479, abstract: https://doi.org/10.1287/msom.1060.0149 (según el resumen)"
  - "Bray y Mendelson (2012), Information Transmission and the Bullwhip Effect: An Empirical Investigation, Management Science 58(5):860-875; abstract e introducción: https://www.kellogg.northwestern.edu/faculty/bray/doc/bw/bw_d.pdf"
  - "Cadena-de-suministro-y-logistica/.investigacion/planificacion.md (sección 6), planificacion-2.md (sección 5) y fundamentos-y-contraria-2.md (secciones 0, 4 y 10)"
aliases: [efecto látigo, bullwhip effect, bullwhip, whiplash effect, efecto Forrester, Forrester effect, amplificación de la demanda, demand amplification, distorsión de la información, juego de la cerveza, beer game, beer distribution game]
creado: 2026-11-27
revisado:
---

# Efecto látigo

El efecto látigo es la amplificación de la variabilidad de la demanda a medida que se sube por la cadena: cada eslabón le pide a su proveedor con más variación que la que tienen sus propias ventas. Lee, Padmanabhan y Whang le encontraron cuatro causas estructurales y Sterman una de comportamiento; los datos muestran que lo tienen dos de cada tres empresas, con una magnitud moderada.

Lee, Padmanabhan y Whang (1997) lo definen como el fenómeno en que «orders to the supplier tend to have larger variance than sales to the buyer (i.e., demand distortion), and the distortion often increases as one moves upstream». Está en [Planificación](planificacion.md) porque nace de cómo cada eslabón convierte lo que le piden en lo que pide. Según la definición, la distorsión suele crecer cuanto más lejos se está del consumidor. La lectura de la base es que le toca más al depósito central de la [red de distribución](../Red-de-distribucion/red-de-distribucion.md) y al mayorista; en los datos por industria, el látigo aparece en el mayorista y no en la mayoría de las industrias manufactureras (ver más abajo).

## De Forrester a Lee y otros

El glosario del CSCMP dice que la idea «has its roots in J Forrester's Industrial Dynamics (1961) and thus it is also known as the Forrester Effect». Su artículo «Industrial Dynamics: A Major Breakthrough for Decision Makers» está reeditado en *The Roots of Logistics* (2012). La fecha y la revista del artículo original no se verificaron.

El nombre y el análisis que se cita hoy son de Lee, Padmanabhan y Whang (1997), en Management Science. A juicio de la base, lo que agregaron fue explicar el efecto por cuatro causas de la estructura de la cadena, sin necesidad de suponer que alguien decide mal.

## Las cuatro causas

El resumen del artículo las nombra así: «demand signal processing, rationing game, order batching, and price variations». La tabla 1 del artículo da, para cada una, sus factores:

| Causa | Qué pasa | Factores, según la tabla 1 |
|---|---|---|
| Procesamiento de la señal de demanda (demand signal processing) | cada eslabón pronostica con los pedidos que recibe, no con las ventas finales, y los ajusta | sin visibilidad de la demanda final, pronósticos múltiples, plazos largos |
| Juego del racionamiento (rationing game) | cuando el proveedor raciona, los clientes piden de más para recibir lo que necesitan | racionamiento proporcional, ignorancia de la oferta, pedidos sin restricción |
| Agrupación de pedidos (order batching) | se pide en lotes grandes y espaciados, no lo que se vende cada día | costo alto por pedido, economía del camión completo, pedidos aleatorios o correlacionados |
| Variación de precios (price variations) | las promociones hacen comprar de más en el precio bajo y nada después | precios alto-bajo |

La columna «Qué pasa» es la lectura de la base de cada causa. La agrupación aparece en la [planificación de la distribución](planificacion-de-la-distribucion.md): los depósitos venden parejo y el central ve golpes del tamaño del lote.

## La causa de comportamiento: Sterman

Sterman (1989) puso a personas a manejar «a simulated inventory distribution system which contains multiple actors, feedbacks, nonlinearities, and time delays». Según el resumen de su artículo, las decisiones producen «aggregate dynamics which systematically diverge from optimal behavior». Propuso que quienes deciden siguen una regla de anclaje y ajuste, y que fallan por «misperceptions of feedback»: «subjects are shown to be insensitive to the feedbacks from their decisions to the environment».

El resumen no menciona la cerveza ni el látigo; la conexión la hace una fuente secundaria, que dice que el látigo «is well simulated by the beer distribution game that was developed by MIT Sloan School of Management in the 1960s». La lectura de la base: Lee y otros explican el efecto por la estructura; Sterman, por cómo deciden las personas con demoras. Una fuente secundaria le atribuye a Sterman que quien decide subestima lo que ya pidió y todavía no llegó, pero eso no está en el resumen leído. Las dos explicaciones se suman.

## Los remedios

La tabla 1 de Lee y otros da las contramedidas de cada causa:

| Causa | Contramedidas, según la tabla 1 |
|---|---|
| Señal de demanda | dar acceso a los datos de venta al consumidor; un solo control de la reposición (el proveedor repone, VMI); acortar los plazos |
| Agrupación de pedidos | intercambio electrónico de datos (EDI) para pedir más chico; descuentos por carga mixta; consolidación por terceros; citas de entrega regulares |
| Variación de precios | precio bajo todos los días (EDLP) |
| Racionamiento | asignar según las ventas pasadas, no según lo pedido; compartir la información de capacidad |

El remedio principal es el primero: que cada eslabón vea lo que se vende al final, y no solo lo que le piden. Con el proveedor que maneja la reposición del cliente (VMI), un solo actor decide con los datos de venta en la mano. La consolidación de cargas, que permite pedir más chico sin pagar un camión medio vacío, está en [consolidación y ruteo](../Transporte/consolidacion-y-ruteo.md).

> [!NOTE] Sin fuente todavía: la planificación colaborativa entre cliente y proveedor (CPFR) como remedio, en una fuente leída. Solo apareció un artículo de síntesis sobre CPFR de Thomé, Hollmann y do Carmo (2014), sin leer.

## Cuánto se lo encuentra en los datos

La evidencia empírica depende de cómo se mire.

- Por industria, casi no. Cachon, Randall y Schmidt (2007) midieron industrias enteras de EE.UU. Según su resumen: «wholesale industries exhibit a bullwhip effect, but retail industries generally do not exhibit the effect, nor do most manufacturing industries». Encontraron que la estacionalidad lo esconde: «highly seasonal industries tend to smooth demand volatility whereas nonseasonal industries tend to amplify». Según Bray y Mendelson, que los citan, de 75 industrias 61 muestran látigo al quitar la estacionalidad y solo 39 sin quitarla.
- Por empresa, en la mayoría. Bray y Mendelson (2012) midieron 4.689 empresas públicas de EE.UU. entre 1974 y 2008: «about two-thirds of firms bullwhip». El látigo medio y el mediano son 15,8 % y 6,7 % de la variabilidad total de la demanda, y «From 1974–1994 to 1995–2008, our sample's mean bullwhip dropped by a third».

Las dos son compatibles: medir la industria entera promedia lo que pasa en cada empresa. Cachon y otros, citados por Bray y Mendelson, lo dicen: «it is possible that firms exhibit the bullwhip effect but the industry does not». La lectura de la base: el efecto es real en la mayoría de las empresas y de magnitud moderada, no la catástrofe de los casos de libro. Bray y Mendelson advierten un posible sesgo de publicación en los estudios de caso. La caída desde mediados de los noventa coincide con la difusión de la información compartida, pero esa causa es inferencia de la base.

Según el resumen de su artículo, Bray y Mendelson además separan el efecto por aviso: las señales de demanda que la empresa conoce con menos de un trimestre de anticipación explican el 51 % del látigo, y las de más de tres trimestres, el 30 %. Saber antes reduce el efecto.

## Lo que un sistema necesita para verlo y para atacarlo

Para medirlo, la definición operativa de los dos estudios pide dos series por eslabón y período: lo que se compra o se recibe y lo que se vende. El látigo es la razón entre sus varianzas. Un sistema que guarda los pedidos de compra y las ventas con fecha ya tiene los datos; falta el informe (inferencia de la base).

Para atacarlo, por los remedios de la tabla 1 y por Sterman:

- Datos de venta compartidos con el proveedor, por artículo, lugar y día.
- Lo pedido y en camino a la vista de quien decide el próximo pedido, no solo el stock en el estante. Es la posición de stock del [punto de pedido](../../Inventario-y-depositos/Reposicion/punto-de-pedido.md#qué-se-compara-con-el-punto-la-posición-de-stock).
- Parámetros de reposición que el proveedor pueda manejar (VMI): niveles mínimos y máximos acordados por artículo y lugar.
- El calendario de pedidos y entregas por proveedor, para las citas regulares.
- El historial de promociones y de racionamientos, para limpiar la serie con que se pronostica (ver [pronóstico de demanda](pronostico-de-demanda.md#la-venta-no-es-la-demanda)).

Para leer más: Lee, Padmanabhan y Whang (1997), el resumen, la sección de las cuatro causas y la tabla 1; para la evidencia, la introducción de Bray y Mendelson (2012), que discute a Cachon y otros.
