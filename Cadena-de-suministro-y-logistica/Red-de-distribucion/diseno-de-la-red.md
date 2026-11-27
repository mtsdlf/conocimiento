---
resumen: >-
  El diseño de la red es la decisión de cuántos depósitos o centros de distribución tener, dónde ponerlos y a qué clientes atiende cada uno, buscando el menor costo total para el servicio que se le quiere dar al cliente. Se toma con un horizonte de un año o más.
estado: borrador
estabilidad: estable
fuentes:
  - "Caplice, C. (MIT CTL), Transportation Management: Network & Hubs, ESD.260 Logistics Systems, archivo lect25, diciembre de 2006, diapositivas 2 a 11 y 27: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/421e474d22fae64f415aea445a34a254_lect25.pdf"
  - "Chopra, S., Designing the Distribution Network in a Supply Chain, Kellogg School of Management, Northwestern University (PDF de noviembre de 2002; se leyó el artículo, no el libro), sección 1 (figuras 4.1 a 4.3, de las que solo se leen los pies) y sección 2.1: https://transportation.tech.northwestern.edu/docs/research/core-topics/logistics-and-supply-chain-management/Chopra_DistributionSupplyChain.pdf"
  - "Cadena-de-suministro-y-logistica/.investigacion/red-de-distribucion-2.md (sección 2)"
aliases: [diseño de la red, diseño de red, network design, supply chain network design, localización de depósitos, localización de instalaciones, facility location, cuántos depósitos, ubicación de centros de distribución, DC location, modelo de localización, programación lineal entera mixta, MILP, posponer, postponement]
creado: 2026-11-27
revisado:
---

# Diseño de la red

El diseño de la red es la decisión de cuántos depósitos o centros de distribución tener, dónde ponerlos y a qué clientes atiende cada uno, buscando el menor costo total para el servicio que se le quiere dar al cliente. Se toma con un horizonte de un año o más.

Es la decisión de más largo plazo de la [red de distribución](red-de-distribucion.md). Elige los lugares; cuánto stock tiene cada uno lo afina la [centralización del stock](centralizacion-del-stock.md), y cuánto se manda a cada uno cada semana, la [planificación de la distribución](../Planificacion/planificacion-de-la-distribucion.md).

## Las tres preguntas

Las clases del MIT definen el problema así: «Network design is the selection of nodes and links that minimize total cost». Para una red de distribución lo bajan a tres preguntas:

1. «How many DCs should there be?»
2. «Where should the DCs be located?»
3. «For each SKU and each customer: which DC should serve the customer, and which plant should serve the DC?»

La tercera es la que después usa todos los días el sistema: de qué depósito sale cada pedido y de dónde se repone cada depósito (lectura de la base).

La misma fuente separa tres horizontes: «Strategic – longer scope and less data available (yr+)», «Tactical – shorter scope w/ planning data (week to yr)» y «Operational – very short scope real data (daily)». El MIT ubica el diseño de la red en el horizonte estratégico; según la lectura de la base, el plan de distribución es táctico y el despacho, operativo.

## Los cuatro tironeos

El MIT ordena el problema en cuatro compromisos, cada uno con dos fuerzas que tiran para lados opuestos:

| Compromiso, literal | Qué pasa al sumar depósitos (lectura de la base sobre Chopra) |
|---|---|
| «Transportation Costs (Inbound versus Outbound)» | la salida hacia el cliente se acorta; la entrada se reparte en más destinos |
| «Facility Costs (Fixed versus Throughput)» | sube el costo fijo de tener más lugares abiertos |
| «Inventory Costs (Cycle versus Safety Stock)» | sube el stock total, sobre todo el de seguridad |
| «Customer Service (Availability versus Order Cycle Time)» | baja el tiempo hasta la entrega |

Chopra llega a lo mismo con otras palabras: el inventario, el transporte, las instalaciones y el servicio, sin abrir cada uno en dos.

## La curva de costo total

El dibujo de las clases del MIT pone el costo del flete, el de las instalaciones, el del inventario y el total contra la cantidad de depósitos, de 0 a 20. Chopra explica cada curva:

- Inventario: sube con la cantidad de lugares. Su ejemplo de 2002: una tienda en línea con unos cinco depósitos rotaba el stock «about twelve times a year», y una cadena de librerías «with about 400 facilities achieves only about two turns per year».
- Transporte: el total baja al sumar lugares «as long as inbound transportation economies of scale are maintained», y vuelve a subir cuando cada depósito ya no recibe cargas completas.
- Instalaciones: bajan al reducir la cantidad de lugares.
- Total: al sumar instalaciones, «first decrease and then increase».

El servicio va por otro eje. Para Chopra, «a decrease in the response time customers desire increases the number of facilities required in the network»: la cadena con 400 locales entregaba en el día; la tienda en línea, en «about a week». La regla que saca es que se agregan depósitos más allá del mínimo de costo solo si el ingreso que trae responder más rápido supera el costo extra: «A firm should add facilities beyond the cost-minimizing point only if managers are confident that the increase in revenues because of better responsiveness is greater than the increase in costs because of the additional facilities».

El punto de menor costo no es un número universal: depende de cuánto pesa cada curva en cada negocio (inferencia de la base). La curva de inventario es la que explica la [centralización del stock](centralizacion-del-stock.md).

## Cómo se resuelve con un modelo

Con muchas instalaciones candidatas, la decisión se arma como un modelo de optimización. El MIT lo plantea como programación lineal entera mixta: minimizar el costo de los flujos más un costo fijo por cada instalación abierta, con la condición de que se cubra la demanda de cada cliente y cada producto.

El tamaño crece rápido. El ejemplo de la clase, con «20 Plants, 30 Products/ Product Groups, 50 Potential DCs, and 400 Customers Regions», da «12,000,000 possible flows!». Separando el flujo de entrada al depósito del de salida, la versión que el MIT llama mejor baja a «50,000 (30k IB & 20k OB) possible flows».

Conseguir los datos cuesta más que resolver el modelo. Las clases listan los problemas: «Demand Point Aggregation», «Demand over Time Periods», «Profiling freight cost data», «Fixed Costs: Periodic versus One-Time» y «Cost Estimating Functions». En una red internacional se suman «Freight Rate Availability», «Transfer Prices and Taxes», «Exchange Rates» y «Duty and Duty Drawback».

> [!NOTE] Sin fuente todavía: el método del centro de gravedad y los modelos de localización continuos; las clases leídas no los tratan.

## Lo que el modelo deja afuera

El mismo MIT termina la formulación con dos preguntas abiertas: «What about Inventory?» y «What about Customer Service?». El modelo de flujos decide lugares y asignaciones, pero no cuánto stock pone en cada uno ni qué plazo de entrega resulta.

El stock se agrega en un segundo paso. Para cada artículo i y depósito j, el MIT calcula el costo de mantener el stock de seguridad como «ICCij = COGi x ICC%ij x SSij»: costo de lo vendido del artículo, por el porcentaje de costo de mantener en ese depósito, por el [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md) que necesita ahí. El porcentaje de mantener es el de [reposición](../../Inventario-y-depositos/Reposicion/reposicion.md#los-tres-costos-que-se-equilibran), y el costo de lo vendido, el de [Contabilidad](../../Contabilidad/Operaciones/costo-de-lo-vendido.md).

## La red de depósitos y la red de transporte se deciden juntas

El MIT trata en la misma clase la ubicación de los depósitos y la de los centros de consolidación del transporte. Su ejemplo de servicio: por un centro único, «3 days, $100»; por centros regionales, «2 days, $120»; directo, «1 day, $200». Elegir cuántos centros de consolidación usar es la misma cuenta de costo contra plazo; está en [consolidación y ruteo](../Transporte/consolidacion-y-ruteo.md) y en [Transporte](../Transporte/transporte.md).

## Posponer la terminación del producto

Una red con el stock centralizado permite terminar el producto después de que el cliente lo pide. Chopra lo menciona como ventaja del envío directo: «postponing customization until after the customer order has been placed», con el ejemplo de un fabricante de computadoras que armaba a pedido. Es lo único que dicen las fuentes leídas sobre posponer.

> [!NOTE] Sin fuente todavía: un tratamiento propio de posponer (postponement): sus formas, cuándo conviene y qué exige de la red.

## Qué guarda un escenario de red

El diseño de la red es un escenario de planificación. Según la formulación del MIT, el escenario tiene:

- las instalaciones candidatas, cada una con su costo fijo (y si es periódico o de una vez);
- los flujos posibles entre cada par de nodos, con su costo por unidad, separados en entrada y salida;
- la demanda por zona de cliente y por producto o grupo de productos, y por período;
- el resultado: qué instalaciones se abren y qué zona atiende cada una.

El resultado se vuelve dato operativo cuando se carga como ubicación y como relación de abastecimiento entre ubicaciones (inferencia de la base), que es lo que registran los sistemas de ejecución (ver [red de distribución](red-de-distribucion.md#qué-tiene-que-poder-representar-un-sistema-de-la-red)). Que un sistema guarde varios escenarios para compararlos es una inferencia de la base.

## Cómo falla un diseño de red

- Optimizar solo el costo. El mínimo de la curva no cuenta el ingreso que se pierde por entregar más lento; Chopra pide justificar cualquier depósito extra con ese ingreso.
- Datos agregados de más. Las zonas de demanda y las tarifas promedio esconden diferencias que mueven el resultado (lectura de la base); es el primer problema de datos que lista el MIT.
- Olvidar el stock. Un modelo de flujos sin el segundo paso de stock subestima lo que cuesta tener muchos depósitos (inferencia de la base sobre el MIT).
- No revisarlo. Es una decisión de un año o más, pero hay que revisarla (lectura de la base sobre los horizontes del MIT).

Para leer más: Caplice, archivo lect25, diapositivas 2 a 11, tiene las tres preguntas, los cuatro compromisos y los problemas de datos; el artículo de Chopra, sección 1, explica las curvas en prosa.
