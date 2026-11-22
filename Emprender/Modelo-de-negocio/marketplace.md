---
resumen: >-
  Un marketplace es una plataforma de dos lados como negocio: conecta a quienes venden con quienes compran, los deja fijar entre ellos las condiciones y cobra una comisión sobre lo que pasa por él. Si funciona, deja márgenes brutos como los del software, pero la mayoría fracasa pronto, y los que sobreviven pierden parte del negocio cuando los lados se arreglan por fuera.
estado: borrador
estabilidad: estable
fuentes:
  - "Andrei Hagiu y Julian Wright (2015), Multi-sided platforms, International Journal of Industrial Organization 43:162-174, leído como documento de trabajo HBS 15-037: https://www.hbs.edu/ris/Publication%20Files/15-037_cb5afe51-6150-4be9-ace2-39c6a8ace6d4.pdf"
  - "Andrei Hagiu y Julian Wright (2015), Marketplace or reseller?, Management Science 61(1):184-203 (según el resumen de los autores en el documento anterior), DOI 10.1287/mnsc.2014.2042"
  - "Bill Gurley, A Rake Too Far: Optimal Platform Pricing Strategy (18 de abril de 2013): https://abovethecrowd.com/2013/04/18/a-rake-too-far-optimal-platformpricing-strategy/"
  - "a16z, The marketplace glossary, según resumen: https://a16z.com/the-marketplace-glossary/"
  - "Grace Gu y Feng Zhu (2021), Trust and disintermediation: evidence from an online freelance marketplace, Management Science 67(2):794-807 (según su abstract): https://ideas.repec.org/p/hbs/wpaper/18-103.html"
  - "Grace Gu, Technology and disintermediation in online marketplaces (borrador preliminar): https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2021/03/Gu-Grace_Technology-and-Disintermediation-in-Online-Marketplaces.pdf"
  - "Michael Cusumano, Annabelle Gawer y David Yoffie, The Business of Platforms (2019), según MIT Sloan (8 de mayo de 2019): https://mitsloan.mit.edu/ideas-made-to-matter/digital-platforms-high-valuations-high-risk-failure y una reseña: https://blog.irvingwb.com/blog/2019/09/despite-their-huge-upside-potential-why-do-most-platforms-fail.html"
  - "Feng Zhu y Marco Iansiti (2019), Why some platforms thrive and others don't, Harvard Business Review 97(1):118-125 (solo el comienzo): https://hbr.org/2019/01/why-some-platforms-thrive-and-others-dont"
  - "Presentaciones anuales 2025 de eBay, Etsy, Airbnb, Upwork y Uber (ver Emprender/Modelo-de-negocio/margenes-por-modelo-de-negocio.md)"
  - "Emprender/.investigacion/modelos-plataforma-y-tipologia.md"
aliases: [marketplace, mercado en línea, plataforma de dos lados como negocio, multi-sided platform, MSP, take rate, comisión de plataforma, rake, desintermediación, leakage, fuga]
creado: 2026-11-22
revisado:
---

# Marketplace

Un marketplace es una plataforma de dos lados como negocio: conecta a quienes venden con quienes compran, los deja fijar entre ellos las condiciones y cobra una comisión sobre lo que pasa por él. Si funciona, deja márgenes brutos como los del software, pero la mayoría fracasa pronto, y los que sobreviven pierden parte del negocio cuando los lados se arreglan por fuera.

Es el modelo de plataforma en la comparación de [modelos de negocio de software](modelos-de-negocio-de-software.md). La estrategia de una plataforma (a qué lado cobrarle, con quién arrancar, cómo compite) está en [Plataformas](../../Producto/Plataformas/plataformas.md), y el [efecto de red](../../Producto/Plataformas/efecto-de-red.md) que la hace crecer, en su nota. Acá queda la mirada de negocio: qué cobra, qué margen deja y cómo se pierde.

## Qué lo hace marketplace y no revendedor

Hagiu y Wright (2015) dan dos condiciones: la plataforma habilita interacciones directas entre los lados, y cada lado se afilia, es decir, hace una inversión propia para estar. Interacción directa quiere decir que «the two or more distinct sides retain control over the key terms of the interaction, as opposed to the intermediary taking control of those terms». Si la empresa fija precios, compra el inventario o maneja la relación con el comprador, es un revendedor.

La elección entre los dos no es de todo o nada. En «Marketplace or reseller?», los mismos autores muestran que conviene el modo marketplace cuando la información local de los vendedores sobre cada producto varía más que la del intermediario: «MSP mode is preferred to the reseller mode if and only if the variance of the suppliers' local information exceeds the variance of the intermediary's local information». Por eso una misma empresa puede revender unas categorías y abrir otras a terceros.

## Cómo cobra: la comisión

La comisión (take rate) es la parte del volumen transado que se queda la plataforma. Gurley la define como «the amount that the marketplace charges as a percentage of GMS (gross merchandise sales), which typically represents net revenues for the marketplace». En 2025, los marketplaces públicos de bienes, alojamiento y trabajo independiente cobraron entre 13,4 % y 24,2 % del volumen, según sus presentaciones anuales, y el software que solo cobra los pagos se queda cerca del 3 % ([márgenes por modelo de negocio](margenes-por-modelo-de-negocio.md#comisión-sobre-el-volumen-take-rate-2025)).

Cobrar mucho es el error más caro, según Gurley: «The most dangerous strategy for any platform company is to price too high». Su caso es un marketplace de trabajo independiente que bajó la comisión de 30 % a 10 % y pasó a liderar su mercado; el propio Gurley advierte que sus cifras no son exactas. La comisión también se complementa: Etsy saca el 30 % de su ingreso de servicios como publicidad, pagos y envío. Cómo se reparte el precio entre los lados, y a cuál se subsidia, está en [mercado de dos lados](../../Producto/Plataformas/mercado-de-dos-lados.md#a-qué-lado-cobrarle-la-estructura-de-precios-y-el-subsidio).

## La economía: margen de software si no toca la mercadería

Un marketplace de intermediación pura tiene margen bruto parecido al del SaaS: 71,5 % a 83,0 % en los cuatro públicos de la ficha, porque no compra lo que vende. Lo que lo baja es hacerse cargo de más cosas. Un marketplace con pagos y logística propios ronda el 44,5 %, y un revendedor, el 30 %. La lectura de que la diferencia la explica el procesamiento de pagos, el envío o el servicio es de esta base, a partir de esas cifras.

No se encontró una fuente con método sobre el margen de contribución de los marketplaces (lo que deja cada transacción después de los costos variables). Damodaran tampoco tiene una categoría de marketplaces para comparar su valuación con la del software y la de los servicios.

## Cómo crece y cómo falla

Crece con liquidez: cuando hay suficientes de cada lado para que una búsqueda termine en una transacción, cada lado atrae al otro. Llegar ahí es el problema del huevo y la gallina, en [mercado de dos lados](../../Producto/Plataformas/mercado-de-dos-lados.md#el-huevo-y-la-gallina-con-quién-se-empieza).

La mayoría fracasa pronto, por varias causas, entre ellas el arranque. Cusumano, Gawer y Yoffie (2019) compararon 209 plataformas que fracasaron entre 1995 y 2015 con 43 exitosas. Según una reseña del libro, 174 de las fracasadas eran de transacción, la vida media fue de 4,9 años y la mediana, de 3. Según MIT Sloan, los marketplaces entre empresas, los navegadores y los de viajes compartidos «fare particularly poorly, typically lasting less than three years». Las causas que listan son el precio mal puesto, la falta de confianza, subestimar a la competencia, el momento, no resolver el arranque y entrar en un negocio de margen bajo; Cusumano lo resume en que una plataforma «doesn't make a bad business magically profitable». Las cifras vienen de la prensa del instituto de los autores y de una reseña, no del libro.

## La fuga: cuando los lados se arreglan por fuera

La desintermediación, o fuga, es que dos usuarios que se conocieron en la plataforma sigan haciendo negocios sin pasar por ella para no pagar la comisión. Gu y Zhu (2021) la midieron con un experimento en un marketplace de trabajo independiente. Según su abstract, mejorar la confianza entre los lados aumenta las contrataciones de calidad, pero «When the trust level is sufficiently high, however, it also increases disintermediation, which offsets the revenue gains». La magnitud no se leyó.

Un borrador de Gu cita una encuesta en una plataforma grande de trabajo independiente según la cual «About 90% of transactions involve disintermediation after platforms match customers with service providers»; es un dato de segunda mano, de un solo tipo de plataforma. El mismo borrador estudia el bloqueo de un canal de comunicación externo y, según la parte que se pudo leer, encuentra que la intermediación subió.

Bajar la comisión no alcanza para frenarla. La fuga depende de si la plataforma sigue haciendo algo que los lados no pueden hacer sin ella: cobrar, garantizar, dar herramientas o comunicación propia (lectura de esta base a partir de Gu y Zhu). Zhu e Iansiti (2019) la ponen entre los factores que deciden si una plataforma prospera, junto con los efectos de red, cómo se agrupa la red, el multi-homing y los puentes con otras redes; esa lista viene de un resumen y no se verificó en el artículo.

Para leer más, el documento de trabajo de Hagiu y Wright para la definición y los casos de revendedor e insumo, y «A Rake Too Far» de Gurley para la intuición de la comisión; fijarse en el caso del marketplace de trabajo independiente.
