---
resumen: >-
  La preparación de pedidos (picking) es sacar de sus ubicaciones las unidades que pide cada pedido, juntarlas, embalarlas y controlarlas hasta dejarlas listas en la puerta de salida. Es la tarea más cara del depósito y casi todo su tiempo es caminar, por eso se organiza por pedido, por lote, por zona o por ola según cuánto se ahorra de caminata.
estado: borrador
estabilidad: semi
fuentes:
  - "Bartholdi y Hackman, Warehouse & Distribution Science, versión 0.98.1 (16-ago-2019), §3.3-3.6 (preparación, embalaje y despacho): https://www.warehouse-science.com/book/editions/wh-sci-0.98.1.pdf"
  - "De Koster, Le-Duc y Roodbergen (2007), Design and control of warehouse order picking: a literature review, EJOR 182(2), 481-501, abstract, §2, §7 y Fig. 4 (que toma de Tompkins et al., 2003): https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.4.3.4 «Pick, pack, and ship product for delivery»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Inventario-y-depositos/.investigacion/operacion-del-deposito.md (2026-11-27), sección 4"
aliases: [preparación de pedidos, picking, order picking, armado de pedidos, preparación, pick and pack, picking por pedido, discrete picking, picking por lote, batch picking, picking por zona, zone picking, picking por ola, wave picking, embalaje, packing, control de pedido, línea de picking, pick line]
creado: 2026-11-27
revisado:
---

# Preparación de pedidos

La preparación de pedidos (picking) es sacar de sus ubicaciones las unidades que pide cada pedido, juntarlas, embalarlas y controlarlas hasta dejarlas listas en la puerta de salida. Es la tarea más cara del depósito y casi todo su tiempo es caminar, por eso se organiza por pedido, por lote, por zona o por ola según cuánto se ahorra de caminata.

Es el último paso de [Operación del depósito](operacion-del-deposito.md). Empieza con un pedido que ya tiene su [reserva](reserva.md) y termina cuando el bulto está registrado como listo para salir. Desde ahí, el despacho y el transporte son de Cadena de suministro y logística, todavía no armado. APQC 7.4 junta las tres cosas en 4.4.3.4 «Pick, pack, and ship product for delivery»; la base corta en la puerta.

## El picking es la mayor parte del costo

Según Bartholdi y Hackman, preparar pedidos suele ser cerca del 55 % del costo operativo de un depósito. De Koster, Le-Duc y Roodbergen dan la misma cifra como estimación de máxima («as much as 55%»). Las dos remiten a la misma literatura de origen, así que es una sola cifra con dos reportes.

## Dónde se va el tiempo de quien prepara

Las dos fuentes reparten el tiempo de quien prepara de manera distinta:

| Actividad | Bartholdi y Hackman | De Koster et al., Fig. 4 (de Tompkins et al., 2003) |
|---|---|---|
| Caminar entre ubicaciones | 55 % | 50 % |
| Buscar | 15 % | 20 % |
| Sacar del estante | 10 % | 15 % |
| Preparación de la tarea | no la separa | 10 % |
| Papeleo y otras | 20 % | 5 % (otros) |

Coinciden en lo que importa: caminar es la mitad o más. Bartholdi y Hackman lo resumen en una cadena: la mayor parte del gasto es mano de obra, la mayor parte de la mano de obra es preparar y la mayor parte de preparar es caminar. Casi todas las decisiones que siguen buscan acortar la caminata.

## Línea de pedido y línea de picking

El pedido y la tarea del depósito no se cuentan igual. Bartholdi y Hackman distinguen la línea de pedido (lo que pidió el cliente) de la línea de picking (lo que se saca de una ubicación). Su ejemplo: si el cliente pide 15 unidades de un artículo que viene en cajas de 12, el pedido tiene una línea y el depósito prepara dos, una caja y 3 unidades sueltas. La conversión entre unidades del [artículo](../Existencias/articulo.md) es la que hace esa cuenta.

Preparar cajas completas y preparar unidades sueltas son trabajos distintos: el libro señala que abrir cajas para sacar unidades es lo que más trabajo pide. Por eso muchos depósitos separan dónde se prepara cada uno (criterio de la base).

## Cuatro maneras de organizar el picking

De Koster, Le-Duc y Roodbergen describen las variantes:

| Manera | Cómo trabaja | Qué gana y qué cuesta (en parte criterio de la base) |
|---|---|---|
| Por pedido (discreto) | una persona recorre el depósito con un pedido por vez | simple, sin clasificar después; la caminata más larga |
| Por lote (batch) | una persona junta varios pedidos en un mismo recorrido | menos caminata; hay que separar los pedidos, mientras se saca o después |
| Por zona | el depósito se divide en partes, cada una con su gente; el pedido pasa de zona en zona (progresivo) o todas trabajan en paralelo (sincronizado) | cada uno camina poco y aprende su zona; hay que juntar las partes y balancear la carga |
| Por ola | se liberan juntos los pedidos que tienen un destino común, como un camión que sale a una hora fija, en varias zonas a la vez | ordena el trabajo según la salida; la ola siguiente espera a que termine la anterior |

Según la misma revisión, una ola suele durar entre 30 minutos y 2 horas. Las maneras se combinan (criterio de la base): un depósito puede preparar por ola, dentro de la ola por zona y dentro de cada zona por lote.

Bartholdi y Hackman dan la regla para agrupar. Casi siempre conviene juntar los pedidos de una sola línea, porque no hay que separarlos después; los pedidos muy grandes no necesitan agruparse; la decisión difícil es con los medianos. Se agrupa cuando lo que cuesta separar los pedidos y el espacio extra es menos que la caminata que se ahorra. El picking por zona, agregan, funciona como una línea de montaje: los pedidos salen en el orden en que se liberaron, pero hay que balancear la carga entre zonas.

## El recorrido

Elegir el orden de las ubicaciones es un problema de recorrido mínimo, el del viajante. La revisión de De Koster et al. explica que en la práctica se usan reglas simples (volver por el mismo pasillo, ir hasta la mitad, recorrer en S, entre otras) porque el óptimo no existe para cualquier plano y a quienes preparan les resulta poco lógico seguirlo. Para quien construye un sistema, la consecuencia práctica es ordenar la lista de picking según la dirección de [ubicaciones](ubicaciones.md), en el orden en que se camina (criterio de la base).

## Cuando la ubicación está vacía

La preparación saca de la zona de picking, que tiene poco de cada artículo. Si se vacía, alguien tiene que bajar mercadería de la zona de reserva antes de seguir; esa reposición interna está en [ubicaciones](ubicaciones.md#la-reposición-de-la-zona-de-picking). Si lo que falta no está en ninguna ubicación aunque el sistema lo muestre, el problema es del registro: queda como faltante en el pedido y como diferencia para [Control del stock](../Control-del-stock/control-del-stock.md) (criterio de la base).

## Embalaje y control hasta la puerta

Al embalar, Bartholdi y Hackman ven el momento para revisar que el pedido esté completo y correcto, y llaman a la exactitud del pedido una medida clave del servicio. El costo de no hacerlo es alto: según el libro, manejar una devolución puede costar hasta diez veces lo que costó mandar el producto. Lo embalado se escanea para registrar que el pedido está listo para salir; ese registro es, para la base, donde termina este tema.

Al embalar también se decide si se espera a juntar todo o se manda en partes. El libro da el ejemplo de una gran tienda online que probablemente manda dos paquetes si se piden dos libros con quince minutos de diferencia. Es una decisión de política, no del depósito: lo que se promete al cliente sobre entregas parciales está en [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md).

En la Argentina, el remito tiene que estar hecho antes de que la mercadería salga; está en [Inventario y depósitos en la Argentina](../inventario-y-depositos-en-argentina.md). Cuando la preparación la hace un tercero para una tienda online, el caso y lo que se cobra están en [fulfillment](../../Comercio-electronico/Operaciones-del-comercio/Envios-y-logistica/fulfillment.md).

> [!NOTE] Sin fuente todavía: las definiciones exactas de las reglas de recorrido y las comparaciones de picking por lote y por zona de De Koster et al. (secciones 5 a 7, leídas en parte), y el capítulo de Bartholdi y Hackman sobre recorridos.
