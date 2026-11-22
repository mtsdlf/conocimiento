---
resumen: >-
  Un mercado de dos lados es uno en que una plataforma atiende a dos grupos que se necesitan, y el precio que cobra a cada uno cambia cuántos llegan del otro. Por eso la plataforma suele subsidiar a un lado, tiene que resolver con quién empieza y compite según cuánto le cuesta a cada lado estar en varias plataformas a la vez.
estado: vigente
estabilidad: estable
fuentes:
  - "Jean-Charles Rochet y Jean Tirole (2003), Platform Competition in Two-Sided Markets, JEEA 1(4):990-1029, DOI 10.1162/154247603322493212: https://academic.oup.com/jeea/article-abstract/1/4/990/2280902 (solo abstract; borrador libre: https://www.ugr.es/~scarbo/ROCHETIR.pdf)"
  - "Thomas Eisenmann, Geoffrey Parker y Marshall Van Alstyne (2006), Strategies for Two-Sided Markets, HBR 84(10):92-101: https://www.kth.se/social/files/546b8e7ef2765474dd3f23fe/4.Eisenmann+et+al+(2006).pdf (leído en pasajes)"
  - "Eisenmann, Parker y Van Alstyne (2011), Platform envelopment, Strategic Management Journal 32:1270-1285 (solo la cita bibliográfica)"
  - "Bernard Caillaud y Bruno Jullien (2003), Chicken & Egg: Competition among Intermediation Service Providers, RAND Journal of Economics 34(2): https://ideas.repec.org/a/rje/randje/v34y2003i2p309-28.html (según resumen)"
  - "Andrew Chen (2021), The Cold Start Problem, según https://a16z.com/books/the-cold-start-problem/ y https://andrewchen.com/solve-a-hard-problem-cold-start-problem/ (resúmenes y adelanto del cap. 8)"
  - "Parker, Van Alstyne y Choudary, Platform Revolution (2016), cap. 5 Chicken or Egg? Eight Ways to Launch a Successful Platform, p. 79, y cap. 6 Monetization, p. 106 (no leídos; índice: https://toc.uni.li/FLMF051021.pdf)"
  - "David Yoffie, HBS Working Knowledge, How to be a business platform leader: https://hbswk.hbs.edu/item/how-to-be-a-business-platform-leader (vía buscador)"
  - "Michael Cusumano, Annabelle Gawer y David Yoffie (2019), The Business of Platforms, según MIT Sloan: https://mitsloan.mit.edu/ideas-made-to-matter/digital-platforms-high-valuations-high-risk-failure (resumen)"
  - "David McIntyre, Beyond a 'Winner-Takes-All' Strategy for Platforms, MIT Sloan Management Review: https://sloanreview.mit.edu/article/beyond-a-winner-takes-all-strategy-for-platforms"
  - "Producto/.investigacion/plataformas.md"
  - "Producto/.investigacion/posicion-contraria.md (afirmación 6)"
aliases: [two-sided market, two-sided markets, mercado bilateral, marketplace, mercado multilateral, multi-homing, huevo y gallina, cold start]
creado: 2026-11-22
revisado: 2026-11-22
---

# Mercado de dos lados

Un mercado de dos lados es uno en que una plataforma atiende a dos grupos que se necesitan, y el precio que cobra a cada uno cambia cuántos llegan del otro. Por eso la plataforma suele subsidiar a un lado, tiene que resolver con quién empieza y compite según cuánto le cuesta a cada lado estar en varias plataformas a la vez.

Lo que lo define es el [efecto de red](efecto-de-red.md) cruzado: el valor de un lado depende del otro. La teoría de Rochet y Tirole, Eisenmann et al. y Parker et al. trata las dos cosas como una sola; acá se separan para enseñar el mecanismo en una nota y las decisiones en esta.

## A qué lado cobrarle: la estructura de precios y el subsidio

En un mercado de dos lados no alcanza con decidir cuánto cobrar: hay que decidir a quién. Rochet y Tirole (2003), según su abstract, modelan la competencia entre plataformas de dos lados, comparan plataformas con fines de lucro con joint ventures sin fines de lucro y estudian cómo el multi-homing y la diferenciación afectan el precio. La literatura les atribuye la idea de que importa la estructura de precios, cuánto paga cada lado, y no solo el nivel. El abstract leído no lo dice con esas palabras.

Eisenmann, Parker y Van Alstyne (2006) lo bajan a una regla: "In most cases, though, it makes sense to subsidize certain users". Llaman "subsidy side" al lado que se subsidia y "money side" al que paga. Adobe cobraba a quienes leían PDF y dio vuelta el esquema: regaló el lector y cobró a quienes creaban documentos.

El subsidio tiene una condición. "Your giveaway will be wasted if your network's subsidy side can transact with a rival platform provider's money side", escriben, con el caso de Netscape. Si los lectores gratis pueden usarse con el producto pago de un rival, el regalo trabaja para el rival.

> [!IMPORTANT]
> Subsidiar un lado no está probado como condición necesaria. No se encontró un estudio que muestre que una plataforma tiene que subsidiar a un lado para ganar. Es una recomendación de Eisenmann et al. apoyada en casos. Cusumano, Gawer y Yoffie cuentan los errores de precio y de modelo de negocio entre las causas por las que fallan las plataformas, según resúmenes de su libro. Que un subsidio mal puesto cuente como error de precio es lectura de la base: los resúmenes no lo dicen así.

Cómo se arma el precio de cada plan, y cuándo regalar una parte del producto conviene en un producto de un solo lado, está en [pricing y empaquetado](../Monetizacion/pricing-y-empaquetado.md) y en [freemium y prueba gratuita](../Monetizacion/freemium-y-prueba-gratuita.md).

## Cuándo gana una sola plataforma

Eisenmann et al. dan tres condiciones para que un mercado termine con una sola plataforma, con el formato DVD como ejemplo:

1. Al menos un lado tiene costos altos para estar en varias plataformas (multi-homing).
2. Los efectos de red cruzados son fuertes.
3. Hay poca diferenciación técnica entre las plataformas.

Si falta alguna, pueden convivir varias (lectura de la base). McIntyre, en un artículo de revisión, sostiene que el ganador único encaja con redes sociales y subastas, pero que en muchos mercados sobreviven varias plataformas.

## El multi-homing decide más que el tamaño

Multi-homing es que un usuario esté en varias plataformas a la vez, como un comerciante que vende en dos o un desarrollador que publica su app en dos tiendas. Rochet y Tirole, Caillaud y Jullien y Eisenmann et al. lo tratan como variable decisiva. Yoffie lo pone en primer plano: "network effects are not enough. Beyond network effects, successful platforms make it hard for their users to multihome" (dato de una entrevista, vía buscador). Cita el caso de los teléfonos de Microsoft: aun con mejor producto se puede perder "if it is too slow in developing customers on each side".

## El envolvimiento: cuando otra plataforma te mete en su paquete

Una plataforma vecina, con una base de usuarios que se solapa con la tuya, puede ofrecer tu función adentro de un paquete. Eisenmann et al. lo advierten así: "The real damage comes when your new rival offers your platform's functionality as part of a multiplatform bundle". Sus ejemplos son Real, Microsoft, Yahoo y Apple. El análisis formal está en Eisenmann, Parker y Van Alstyne (2011), "Platform envelopment", que esta base no abrió. La versión del mismo riesgo dentro de un ecosistema, cuando la plataforma absorbe una app de terceros, está en [ecosistema de terceros](ecosistema-de-terceros.md).

## El huevo y la gallina: con quién se empieza

Sin comerciantes no vienen compradores, y sin compradores no vienen comerciantes. Caillaud y Jullien (2003), según un resumen, modelan este problema con efectos de red indirectos y multi-homing. Encuentran que pueden darse estructuras de mercado eficientes e ineficientes, y que "the most profitable market equilibrium may precisely be the inefficient one". También muestran que las tarifas por transacción sirven como arma para ganar cuota.

Andrew Chen, practicante e inversor, propone una receta en *The Cold Start Problem* (2021). Define la "red atómica" como la red más chica que se sostiene sola, y el "hard side" como el lado más difícil de conseguir, que en los marketplaces suele ser la oferta. Su consejo es resolver ese lado primero. En una plataforma de tiendas online, el lado difícil serían los comerciantes; esto es una aplicación de la idea, no un dato. Es opinión de practicante sin estudio, leída por resúmenes.

*Platform Revolution* dedica el capítulo 5, "Chicken or Egg? Eight Ways to Launch a Successful Platform", a las formas de arrancar. No se leyó, así que las ocho formas no están acá.

## La comisión de la plataforma

La comisión (take rate) es la parte de cada transacción que se queda la plataforma, y es una forma de cobrarle al lado que paga. Caillaud y Jullien la tratan como arma competitiva. El ejemplo documentado del reparto con desarrolladores de apps, con sus umbrales, está en [ecosistema de terceros](ecosistema-de-terceros.md#el-reparto-de-ingresos-con-los-desarrolladores).

Las comisiones de marketplaces públicos en 2025 y la evidencia experimental sobre la desintermediación (cuando los lados se conocen por la plataforma y siguen por fuera para no pagarla) están en [marketplace](../../Emprender/Modelo-de-negocio/marketplace.md), en Emprender.

> [!NOTE] Sin fuente todavía: un estudio que compare comisiones entre plataformas y su efecto sobre el crecimiento.
