---
resumen: >-
  Las finanzas de una empresa que empieza responden dos preguntas: cuánto tiempo le dura la plata que tiene y de dónde sale la que le falta, sabiendo lo que cuesta cada fuente.
estado: vigente
estabilidad: estable
fuentes:
  - "Paul Graham, Default Alive or Default Dead? (octubre de 2015): https://paulgraham.com/aord.html"
  - "Paul Graham, Ramen Profitable (julio de 2009): https://paulgraham.com/ramenprofitable.html"
  - "Y Combinator, documentos del SAFE: https://www.ycombinator.com/documents"
  - "John Mullins, The Customer-Funded Business (Wiley, 2014), según la ficha de LBS: https://lbsresearch.london.edu/id/eprint/709"
  - "Kauffman Foundation, We Have Met the Enemy... and He Is Us (2012), según resúmenes: https://kauffman.org/reports/we-have-met-the-enemy-and-he-is-us"
  - "Brad Feld y Jason Mendelson, Venture Deals, 4.ª ed. (Wiley, 2019), según su ficha: https://www.oreilly.com/library/view/venture-deals-4th/9781119594826/"
  - "Kerr, Nanda y Rhodes-Kropf (2014), Entrepreneurship as Experimentation, Journal of Economic Perspectives 28(3): https://www.nber.org/papers/w20358"
  - "Emprender/.investigacion/finanzas-equipo-legal.md"
  - "Emprender/.investigacion/posicion-contraria.md"
aliases: [burn rate, runway, default alive, default dead, ramen profitable, break-even, bootstrapping]
creado: 2026-11-22
revisado: 2026-11-22
---

# Finanzas

Las finanzas de una empresa que empieza responden dos preguntas: cuánto tiempo le dura la plata que tiene y de dónde sale la que le falta, sabiendo lo que cuesta cada fuente.

Recibe sus números del [modelo de negocio](../Modelo-de-negocio/modelo-de-negocio.md): qué se cobra, a quién y con qué costos. Le devuelve a [Validación](../Validacion/validacion.md) y a [Crecimiento](../Crecimiento/crecimiento.md) un límite de tiempo, la pista, que dice cuántos intentos quedan antes de quedarse sin plata. Si cada venta deja plata o no es una cuenta de [economía unitaria](../../Marketing/Medicion/economia-unitaria.md), que vive en el tema Marketing con el CAC y el LTV. La forma legal que se elija en [Legal e impuestos](../Legal-e-impuestos/legal-e-impuestos.md) condiciona qué fuentes de plata se pueden recibir.

## Caja y resultado

La caja es la plata que hay en la cuenta; el resultado es la diferencia entre ingresos y gastos de un período. Una empresa puede dar ganancia en el papel y quedarse sin caja, si cobra a 60 días y paga a 30, o si invierte en stock antes de vender. En una empresa que empieza, la pregunta que decide si sigue viva es la de caja.

> [!NOTE]
> Sin fuente todavía: las definiciones de caja y resultado, consumo mensual, pista y punto de equilibrio de esta nota son contabilidad estándar y no se contrastaron con un texto de referencia. Falta un manual de contabilidad o la biblioteca de Y Combinator.

## Consumo mensual y pista

El consumo mensual (burn) es cuánta caja pierde la empresa por mes: lo que sale menos lo que entra. La pista (runway) es cuántos meses faltan para que la caja llegue a cero a ese ritmo: la caja dividida por el consumo mensual. Con 12.000 de caja y un consumo de 1.000 por mes, la pista es de 12 meses, si nada cambia.

La pista cambia de sentido en una empresa que todavía busca su modelo. Según resúmenes de *The Lean Startup*, Ries propone medirla en pivotes: cuántas veces más se puede cambiar de rumbo antes de que se acabe la plata. Esa lectura está en [pivotar o perseverar](../Validacion/pivotar-o-perseverar.md), y su formulación literal no se verificó en el libro.

## Default alive: llegar a ser rentable con lo que hay

Paul Graham (2015) reduce la situación financiera a una pregunta: «do they make it to profitability on the money they have left?». Si la respuesta es sí, con los ingresos y gastos actuales, la empresa está *default alive*; si no, está *default dead* y depende de conseguir más plata. Leída junto a la pista, la pregunta suma la evolución de los ingresos a la caja: una empresa con poca pista e ingresos que crecen rápido puede estar viva (inferencia de la base).

El mismo ensayo da dos consejos. El primero, literal: «Don't hire too fast. Hiring too fast is by far the biggest killer of startups that raise money». El segundo es tener por escrito qué hacer si no se consigue más plata, un plan B. Las contrataciones conectan esta parte con [Fundadores y equipo](../Fundadores-y-equipo/fundadores-y-equipo.md).

## Ramen profitable y punto de equilibrio

Graham (2009) define un escalón previo a la rentabilidad: «Ramen profitable means a startup makes just enough to pay the founders' living expenses». Lo que gana la empresa en ese punto es independencia: «you're no longer at the mercy of investors». Se puede leer como una versión mínima de default alive, medida contra los gastos de vida de quienes fundan (inferencia de la base).

El punto de equilibrio es el nivel de ventas en el que los ingresos cubren todos los costos, fijos y variables, y el resultado es cero. Se calcula dividiendo los costos fijos por el margen que deja cada unidad vendida. Ese margen por unidad es el mismo que usa la [economía unitaria](../../Marketing/Medicion/economia-unitaria.md) para decidir cuánto se puede gastar en conseguir un cliente.

## De dónde sale la plata y lo que cuesta

Cada fuente de financiamiento cobra un precio distinto: dilución (parte de la propiedad), control (lugar en las decisiones), exigencia de retorno o riesgo personal. La columna del costo es lectura de la base; la tercera dice qué sostienen las fuentes leídas.

| Fuente | Qué cuesta | Qué dicen las fuentes |
|---|---|---|
| Ahorro e ingresos propios (bootstrapping) | No diluye ni cede control; el riesgo es de quien funda | Sin fuente todavía sobre su costo. Si conviene emprender sin dejar el empleo se discute en [mitos de emprender](../Fundamentos/mitos-de-emprender.md). |
| Clientes (adelantos, suscripciones, pagos por anticipado) | No diluye; obliga a vender antes de terminar el producto | Mullins (2014) describe cinco modelos de negocio financiados por clientes, entre ellos el de Dell, según la ficha del libro; el libro no se leyó. |
| Inversores tempranos con un instrumento convertible | Diluye cuando el instrumento se convierte en acciones | Ver instrumentos, abajo. |
| Capital de riesgo (venture capital) | Diluye, suma control y exige un retorno muy grande | Los retornos de los fondos se concentran en pocos casos (ver abajo). Venture Deals dedica capítulos a los términos económicos, a los de control y a la tabla de propiedad (cap table), según su ficha. |
| Apoyo estatal | Depende del programa | En Argentina, el fondo de capital emprendedor de la Ley 27.349 se disolvió en 2024: el dato está en la [normativa para empezar en Argentina](../Legal-e-impuestos/normativa-para-empezar-en-argentina.md). Aceleradoras, subsidios y ángeles locales no se investigaron. |

Kerr, Nanda y Rhodes-Kropf (2014) describen las probabilidades de éxito, según un resumen, como «low, extremely skewed and unknowable until an investment is made». La base lee de ahí que un fondo vive de los pocos casos extremos y busca empresas que puedan crecer mucho más de lo que necesitan para ser rentables (inferencia).

> [!IMPORTANT]
> La mayoría de los fondos de capital de riesgo no le ganó al mercado en el informe de la Kauffman Foundation (2012), que analiza unos 100 fondos a lo largo de más de 20 años, según resúmenes. Las cifras varían según el resumen: uno dice que solo 20 de 100 superaron a un índice de mercado público; otro, que 62 de 100 no lo superaron después de comisiones. Las dos son compatibles solo si hay 18 casos intermedios, y el PDF no se leyó. El informe habla de una distribución sesgada de retornos; el término «power law» no aparece en lo leído.

Los instrumentos con que entra la plata temprana se mencionan acá y tendrán su propio componente. El SAFE (Simple Agreement for Future Equity) de Y Combinator es «a short contract an investor signs to fund your startup now», que se convierte en acciones en una ronda con precio. Según Y Combinator, «a SAFE is not a debt and not a loan»: no tiene interés ni vencimiento. Todo lo del SAFE tiene una sola fuente, el propio Y Combinator. La nota convertible no se investigó. Cómo se recibe un SAFE desde una sociedad argentina tampoco está investigado.

## Cómo fallan las finanzas de una empresa que empieza

- **Contratar antes de tiempo.** Graham lo nombra como «by far the biggest killer» de las startups que levantaron plata.
- **Confundir resultado con caja.** Vender con ganancia y cobrar tarde deja a la empresa sin plata para pagar lo que vence antes (sin fuente todavía, ver arriba).
- **Medir la pista solo en meses.** Una pista de un año alcanza para muchos pivotes si cada ciclo es corto, y para dos si cada ciclo lleva seis meses (inferencia de la base sobre [pivotar o perseverar](../Validacion/pivotar-o-perseverar.md)).
- **Elegir la fuente sin mirar su precio.** Capital de riesgo para un negocio que no puede crecer órdenes de magnitud cede propiedad y control a cambio de una exigencia que la empresa no va a cumplir (inferencia de la base sobre Kerr, Nanda y Rhodes-Kropf).

## Lo que se va a sumar a Finanzas

Esta parte todavía no tiene componentes propios. Cuando se escriban, van a ser estos, tomados de la investigación:

- Caja y resultado: por qué una empresa rentable se queda sin plata.
- Consumo mensual, pista y default alive: cuánto dura la plata y cómo se calcula.
- Punto de equilibrio: cuánto hay que vender para no perder.
- Fuentes de financiamiento: lo que cuesta cada una en dilución, control y retorno esperado.
- Financiarse con clientes y bootstrapping: adelantos, suscripciones y pagos por anticipado.
- Capital de riesgo y la concentración de sus retornos: cuándo tiene sentido y cuándo no.
- Instrumentos de la plata temprana: SAFE y nota convertible, como mención.
- Plan financiero mínimo: la planilla de doce meses de caja.

El margen por cliente no va a tener componente acá: vive en [economía unitaria](../../Marketing/Medicion/economia-unitaria.md).
