---
resumen: >-
  Revisar el producto propio es juzgar lo que ya está construido contra una oferta nueva para decidir qué queda, qué se esconde, qué se apaga y qué falta, mirando lo que vive cada rol, y bajarlo a trabajo acotado. Las recetas son de practicantes; solo la evaluación de pantallas tiene estudios, y están discutidos.
estado: vigente
estabilidad: semi
fuentes:
  - "Des Traynor, «Before you plan your product roadmap», Intercom, 2-oct-2014: https://www.intercom.com/blog/before-you-plan-your-product-roadmap/"
  - "Des Traynor, «How to sunset a feature», Intercom, 23-abr-2015: https://www.intercom.com/blog/how-to-sunset-a-feature/"
  - "Gov.uk Service Manual, «Retiring your service» (actualizada 26-ago-2025): https://www.gov.uk/service-manual/phases/retirement"
  - "Gov.uk Service Manual, «Service Standard»: https://www.gov.uk/service-manual/service-standard"
  - "Pendo, «2019 Feature Adoption Report»: https://www.pendo.io/resources/the-2019-feature-adoption-report/ (dato de un proveedor)"
  - "Mike Cohn, «Are 64% of Features Really Rarely or Never Used?», Mountain Goat Software: https://mountaingoatsoftware.com/blog/are-64-of-features-really-rarely-or-never-used"
  - "Chapman y Callegaro, «Kano Analysis: A Critical Survey Science Review», Sawtooth Software Conference 2022: https://quantuxbook.com/papers/REPRINT-Chapman-Callegaro-SawtoothConference2022.pdf"
  - "Osterwalder, Pigneur, Bernarda y Smith, Value Proposition Design, Wiley, 2014, vía el resumen de Strategyzer: https://www.strategyzer.com/library/value-proposition-design-book-summary (el libro no se leyó)"
  - "Christensen, Hall, Dillon y Duncan, «Know Your Customers' Jobs to Be Done», HBR, sep-2016: https://hbr.org/2016/09/know-your-customers-jobs-to-be-done (no leído entero, muro de pago)"
  - "Nielsen (2000), «Why You Only Need to Test with 5 Users», NN/g, según la nota de test de usabilidad: https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/"
  - "Teresa Torres, «Opportunity Solution Trees», Product Talk, 6-dic-2023: https://www.producttalk.org/opportunity-solution-trees/"
  - "Dan North, «Introducing BDD» (2006): https://dannorth.net/introducing-bdd/ ; Martin Fowler, «GivenWhenThen»: https://martinfowler.com/bliki/GivenWhenThen.html"
  - "Producto/.investigacion/revision-del-producto-propio.md"
aliases: [feature audit, auditoría de funcionalidades, auditoría de producto, revisión de producto, revisar lo propio, sunsetting, sunset, retirar una funcionalidad, deprecación, apagar una funcionalidad, gap analysis, análisis de brechas, value proposition canvas, lienzo de la propuesta de valor]
creado: 2026-11-23
revisado: 2026-11-24
---

# Revisión del producto propio

Revisar el producto propio es juzgar lo que ya está construido contra una oferta nueva para decidir qué queda, qué se esconde, qué se apaga y qué falta, mirando lo que vive cada rol, y bajarlo a trabajo acotado. Las recetas son de practicantes; solo la evaluación de pantallas tiene estudios, y están discutidos.

Hace falta cuando cambia lo que se vende y el producto queda igual: un software que el cliente usaba solo pasa a venderse como servicio que otro arma y mantiene, o aparece un plan para otro comprador. Es el reflejo del [desarme de producto](../../Estrategia-competitiva/Analisis-de-competidores/desarme-de-producto.md), que estudia el producto de un rival; acá la vara no es el rival sino la [propuesta](../../Marketing/Propuesta/propuesta.md) nueva. Termina en lo que la [estrategia de producto](estrategia-de-producto.md) necesita: pocos problemas elegidos y una lista explícita de lo que no se hace.

## La vara es el trabajo que contrata el comprador nuevo

Cuando cambia la oferta, cambia el [trabajo que el cliente contrata](../../Marketing/Mercado-y-cliente/jobs-to-be-done.md). Quien antes contrataba una herramienta para hacer algo él mismo, ahora contrata que otro se lo tenga andando. Cada funcionalidad se juzga contra ese trabajo nuevo y no contra el viejo. Esto es una aplicación de esta base: Christensen y sus coautores presentan el marco con casos, y no hablan de revisar un producto existente.

El cambio de oferta suele cambiar también quién usa cada parte del producto. Lo que antes tocaba el cliente puede pasar a tocarlo alguien de adentro que lo opera por él. Por eso la revisión se hace por rol y no por pantalla. En esta nota hay tres: el que compra, que paga y usa lo que la oferta le promete; el que atiende, que habla con él (ventas, soporte); y el que opera, que hace el trabajo por detrás sin que el comprador lo vea.

## Los cuatro destinos de lo que hay

| Destino | Cuándo | Qué se mira |
|---|---|---|
| Queda | Sirve al trabajo nuevo y alguien lo usa | Uso, y que el comprador nuevo lo dé por sentado o lo valore |
| Se esconde | Unos pocos dependen de él, o lo usa el que opera y no el que compra | Quién es ese poco y si el rol que lo usa cambió |
| Se apaga | No sirve al trabajo nuevo y se probó subir su uso sin resultado | Los cuatro pasos de retiro, más abajo |
| Falta | El trabajo nuevo lo pide y no está | Lo que queda sin cubrir al cruzar la oferta con lo que hay |

La tabla es una síntesis de esta base; ninguna fuente usa estos cuatro nombres juntos.

## Medir el uso antes de opinar

Traynor (Intercom, 2014) propone poner cada funcionalidad en dos ejes: cuánta gente la usa y con qué frecuencia. Lo que muchos usan seguido es el corazón del producto. Se dejan afuera las cosas administrativas, como crear una cuenta o recuperar la contraseña, que son el costo de tener un producto y no lo que lo distingue. Para lo poco usado da cuatro salidas: sacarlo, conseguir que lo use más gente, conseguir que lo usen más seguido o mejorarlo para quienes ya dependen de él.

El aviso que más importa al cambiar de oferta es el de la esquina de pocos usuarios que lo usan mucho. Según Traynor, eso es una funcionalidad mal adoptada o una de los planes para clientes grandes, y hay que mirar quién es ese poco antes de sacarla. Con una oferta nueva, ese poco puede ser justo el comprador que se busca, o el rol que va a operar el producto.

Las cifras que circulan sobre cuánto de un producto no se usa son flojas: el 80 % de Pendo (2019) sale de 615 suscripciones de clientes de un proveedor de analítica, y el «64 %» atribuido a Standish, según Cohn, de cuatro aplicaciones internas.

## Clasificar lo que queda: Kano y el canvas

Lo que queda se clasifica según lo que espera el comprador nuevo, con las categorías de [Kano](../Planificacion-y-entrega/priorizacion.md#kano-clasificar-atributos-no-ordenarlos). Además de las tres que nombra esa nota (imprescindible, unidimensional y atractivo), el modelo suele sumar dos más, según resúmenes del original: indiferente, lo que a nadie le importa si está o no, e inverso, lo que molesta si está. La aplicación es de esta base: lo imprescindible para el comprador nuevo va a «queda» o a «falta», lo indiferente es candidato a esconder y lo inverso es el candidato más claro a sacar.

Kano por encuesta es frágil con pocos clientes: Chapman y Callegaro (2022) sostienen que sus preguntas piden predecir sentimientos ante algo hipotético y que la clasificación es inestable con menos de unos 200 encuestados. Con una base chica de compradores, Kano sirve como vocabulario para discutir y no como medición.

El canvas de propuesta de valor de Osterwalder y sus coautores (2014) pone de un lado los trabajos, dolores y ganancias del cliente, y del otro los productos, lo que alivia cada dolor y lo que crea cada ganancia. Usado contra un producto existente, se dibuja el lado de la oferta con lo que el producto tiene hoy y se une cada pieza con el dolor que cubre. Lo que queda sin línea del lado del cliente es lo que falta; lo que queda sin línea del lado del producto sobra para esta oferta. Esa forma de contar las líneas sale de una adaptación de terceros, no del libro. El resumen de Strategyzer pide validar el encaje con evidencia y no con lo que opina el cliente sobre soluciones hipotéticas; el libro no se leyó.

## Apagar o esconder

Traynor (Intercom, 2015) ordena el retiro de una funcionalidad en cuatro pasos:

1. **Confirmar que no tiene arreglo**: cuántos la usan seguido, cuánto facturan esos clientes, qué se probó para subir el uso, por qué no la usan los demás y si hoy se haría igual.
2. **Dejar de ofrecerla a los nuevos**: se apaga para ellos y se saca del material de venta y de las conversaciones comerciales.
3. **Separar a los que la probaron una vez**, a los que se les puede esconder casi sin aviso, de los que dependen de ella, que necesitan atención directa.
4. **Avisar a los que quedan** con fecha de cierre, el porqué, alternativas y cómo llevarse sus datos, con un aviso de un mes a un año.

Los pasos 2 y 3 son la diferencia entre esconder y apagar: esconder es dejar de ofrecer sin sacarle nada a quien depende; apagar es el paso 4. El manual de servicios del gobierno británico suma una pregunta antes de apagar: qué pasa con la necesidad que cubría, si desaparece, la cubre otro servicio o la cubre un tercero. Pide avisar temprano a quienes se integran por API y por sus propios canales a quienes usan atención asistida, y mantener las redirecciones alrededor de un año, con reglas que dependen de cuánto tiempo estuvo en línea el servicio.

## Mirar lo que vive cada rol

Cada rol (el que compra, el que atiende, el que opera por detrás) se mira por separado, porque cada uno hace otro recorrido y se traba en otros lugares. Hay cinco métodos y cada uno ve otra cosa:

| Para ver | Método | Respaldo |
|---|---|---|
| El recorrido entero de un rol, incluido lo que pasa fuera de la pantalla | [Mapa del recorrido](../../UX/Investigacion/mapa-del-recorrido-del-cliente.md) de estado actual, con datos | Práctica documentada, sin estudios de eficacia |
| Cómo se reparte el trabajo entre el que compra, el que atiende y el que opera | [Plano de servicio](../../Marketing/Propuesta/plano-de-servicio.md) | Práctica documentada con casos |
| Problemas de pantalla, rápido y barato | [Evaluación heurística](../../UX/Evaluacion/evaluacion-heuristica.md), con 3 a 5 evaluadores | Estudios, discutidos |
| Tareas que se hacen por primera vez, como un alta o una configuración inicial | Recorrido cognitivo | Práctica de sus autores y un estudio comparativo |
| Los problemas graves de verdad | [Test de usabilidad](../../UX/Evaluacion/test-de-usabilidad.md), unos pocos por rol y en rondas | Estudios |

El plano de servicio es el único de la lista que pone en el mismo papel a los tres roles: el mapa del recorrido mira a uno solo. El recorrido cognitivo, explicado en la [evaluación heurística](../../UX/Evaluacion/evaluacion-heuristica.md#la-comparación-de-jeffries-cuatro-técnicas-sobre-el-mismo-producto), sirve cuando la oferta nueva pone a alguien de adentro a hacer por primera vez lo que antes hacía el cliente.

Con roles tan distintos, cinco usuarios en total no alcanzan. Nielsen propone 3 o 4 participantes por grupo si son dos grupos y 3 por grupo si son tres o más, en varias rondas chicas en lugar de una grande; con tres roles, son 3 por rol (las cifras y su debate están en [test de usabilidad](../../UX/Evaluacion/test-de-usabilidad.md#de-dónde-sale-la-regla-de-los-cinco-usuarios)).

Ningún método da solo la lista completa de problemas: la heurística encuentra muchos y barato, el test es el mejor para los recurrentes, y cada uno deja pasar problemas serios que otro ve; la comparación de Jeffries y sus críticas están en la misma nota.

## De la revisión a lo que se construye

Lo que sale de la revisión baja a trabajo por cuatro caminos que ya están en la base:

- **Lo que falta y su orden**: el recorrido de cada rol tiene la forma de la columna vertebral del [mapa de historias](../Descubrimiento/dar-forma-a-una-solucion.md#story-mapping-el-recorrido-y-los-cortes-de-entrega) de Patton, y las entregas se cortan de punta a punta. Pasar del mapa del recorrido al de historias es una inferencia de esta base: ni Patton ni NN/g lo formalizan.
- **Las oportunidades**: Torres arma un mapa de experiencia con las historias de las entrevistas y cuelga cada oportunidad del momento donde ocurre, como primera capa del [árbol de oportunidades](../Descubrimiento/arbol-de-oportunidades.md). Su mapa es más general que el [mapa del recorrido](../../UX/Investigacion/mapa-del-recorrido-del-cliente.md#con-qué-se-confunde), pero cumple el mismo papel: es el puente más explícito entre un recorrido y el trabajo.
- **Lo que se esconde o se apaga**: entra como «lo que no entra» (*no-gos*) del [pitch](../Descubrimiento/dar-forma-a-una-solucion.md#el-pitch-y-el-prd-corto), con un apetito que acota la solución. Así el «no» queda escrito y no se reabre en cada ciclo.
- **Lo que tiene que hacer cada rol**: cada paso del plano de servicio se puede escribir como escenario «dado, cuando, entonces», el formato de North y Matts para los criterios de aceptación de una [historia de usuario](../../Desarrollo/Especificacion-y-prueba/historia-de-usuario.md). Hacerlo por rol es una inferencia de esta base.

Lo que se entrega se juzga después por el [resultado](resultados-y-entregables.md) que mueve y no por la lista de lo construido. Como vara del servicio entero sirve el estándar del gobierno británico, que pide resolver un problema entero y no un pedazo, unir todos los canales, también los no digitales, y operar un servicio confiable (puntos 2, 3 y 14).

## Un orden para hacerlo

El orden es de esta base, armado con las piezas de arriba:

1. Escribí la oferta nueva como trabajo del comprador y nombrá los roles que la viven: el que compra, el que atiende, el que opera.
2. Dibujá el recorrido actual de cada rol con datos, y el plano de servicio de la oferta nueva.
3. Medí el uso de cada funcionalidad por frecuencia y por cantidad, y mirá quién está en la esquina de pocos que la usan mucho.
4. Cruzá lo que hay con el trabajo nuevo: queda, se esconde, se apaga o falta. Marcá qué celdas tienen un dato y cuáles son opinión del equipo.
5. Probá con usuarios de cada rol las tareas que la oferta promete, en rondas chicas, y sumá una heurística antes de cada ronda.
6. Bajá lo que falta al mapa de historias o a un pitch, con lo que sale como «no entra» y criterios de aceptación por rol.
7. Retirá lo que se apaga con los cuatro pasos de Traynor.

> [!IMPORTANT]
> Lo que no tiene evidencia: no se encontraron estudios de que mejoren decisiones o resultados la auditoría de uso, el retiro de funcionalidades, el canvas, el análisis de brechas (comparar el estado de hoy con el deseado, sin un método canónico), los mapas, el pitch, el árbol de oportunidades, los criterios «dado, cuando, entonces» ni el estándar británico. Tampoco nada sobre un software que pasa a venderse como servicio gestionado. Jobs to be done se apoya en casos de sus autores. Solo la evaluación de pantallas tiene estudios, y están discutidos.

> [!NOTE]
> Sin fuente todavía: el texto original de Kano (1984). El modelo de las brechas de servicio de Parasuraman, Zeithaml y Berry (1985) tiene nota propia en [modelo de las brechas](../../Marketing/Servicio-y-relacion/modelo-de-las-brechas.md), aunque el paper original tampoco se leyó.

## Qué leer

Las dos notas de Traynor en el blog de Intercom son cortas y concretas: en la de 2014, el gráfico de dos ejes y la esquina de pocos que usan mucho; en la de 2015, los cuatro pasos. Para retirar algo que otros usan para integrarse, «Retiring your service» del manual británico. Para no confiar en un solo método de evaluación, la [evaluación heurística](../../UX/Evaluacion/evaluacion-heuristica.md), con la comparación de Jeffries y sus críticas.
