---
resumen: >-
  El producto mínimo viable (MVP) es, según Ries, la versión de un producto nuevo que le permite a un equipo juntar la mayor cantidad de aprendizaje validado sobre sus clientes con el menor esfuerzo; se elige por la hipótesis que prueba, no por lo chico que es.
estado: vigente
estabilidad: semi
fuentes:
  - "Eric Ries, Minimum Viable Product: a guide (2009-08-03): https://www.startuplessonslearned.com/2009/08/minimum-viable-product-guide.html"
  - "Eric Ries, The Lean Startup (2011), capítulo Test según resúmenes; en castellano, El método Lean Startup (Deusto)"
  - "theleanstartup.com, Principles: https://theleanstartup.com/principles"
  - "Resumen del libro de un lector: https://publish.obsidian.md/dk/Reading/Books/The+Lean+Startup"
  - "Shortform, value hypothesis y growth hypothesis: https://www.shortform.com/blog/value-hypothesis-growth-hypothesis-lean-startup/"
  - "Dropbox, video de demostración en Hacker News (2007-04-04): https://news.ycombinator.com/item?id=8863"
  - "Dan Kaplan, Peter Thiel is wrong about lean startups (TechCrunch, 2015-05-09): https://techcrunch.com/2015/05/09/peter-thiel-is-wrong-about-lean-startups"
  - "Emprender/.investigacion/validacion.md"
  - "Emprender/.investigacion/posicion-contraria.md"
aliases: [MVP, minimum viable product, producto mínimo, smoke test, concierge MVP, video MVP]
creado: 2026-11-22
revisado: 2026-11-22
---

# Producto mínimo viable

El producto mínimo viable (MVP) es, según Ries, la versión de un producto nuevo que le permite a un equipo juntar la mayor cantidad de aprendizaje validado sobre sus clientes con el menor esfuerzo; se elige por la hipótesis que prueba, no por lo chico que es.

La definición literal es del blog de Ries, del 3 de agosto de 2009: «the minimum viable product is that version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort». En la misma entrada aclara: «MVP, despite the name, is not about creating minimal products». En el libro, según un resumen, lo define por su función dentro del ciclo: «that version of the product that enables a full turn of the build-measure-learn loop». Es lo que se construye en cada vuelta de [construir-medir-aprender](construir-medir-aprender.md).

## Qué mide un MVP que una conversación no mide

Las entrevistas del [descubrimiento de clientes](descubrimiento-de-clientes.md) dicen lo que la gente cuenta; un MVP mide lo que hace. En el recorrido de la [validación](validacion.md) viene después: cuando un problema sobrevivió a las conversaciones, el MVP pone a prueba si alguien actúa en consecuencia, ya sea dejando su correo, pagando o volviendo. La página de principios dice que sirve «to begin the process of learning as quickly as possible».

El tamaño del MVP lo decide la [hipótesis de salto de fe](hipotesis-de-salto-de-fe.md) que prueba. Según la entrada de 2009, el MVP original de IMVU tardó unos seis meses en salir; en la misma entrada, un smoke test con anuncios alcanza para descubrir que un concepto es débil.

## Los tipos de MVP

Ries nombra uno en el blog de 2009, y el libro trae otros según resúmenes. Los que aparecen en lo investigado:

| Tipo | Qué es | Qué prueba | Ejemplo y fuente |
|---|---|---|---|
| Smoke test | Un anuncio o una página que ofrece algo que todavía no existe, para medir cuántos lo piden | Si hay demanda por el concepto | El «AdWords smoke test» que Ries nombra en 2009 como forma barata de descubrir que un concepto es débil; para un servicio, la [página de oferta que mide](pagina-de-oferta-que-mide.md) |
| Video | Un video que muestra cómo funcionaría el producto | Si el problema interesa lo suficiente como para anotarse | Dropbox, publicado en Hacker News el 4 de abril de 2007 como parte de su solicitud a Y Combinator (según notas secundarias; el libro lo usa como ejemplo según resúmenes) |
| Concierge | El servicio se presta a mano, personalizado, a veces a un solo cliente | Si la solución resuelve el problema, antes de automatizarla | Del libro, según resúmenes |
| Venta real hecha a mano (nombre de la base; los resúmenes lo llaman «la prueba de Zappos») | La vidriera parece un producto completo; atrás, todo se hace a mano | La hipótesis de valor con transacciones reales | Zappos, que compraba los zapatos recién cuando entraba un pedido (según resúmenes) |

Sobre Dropbox, la lista de espera habría pasado de unos 5.000 a 75.000 inscriptos después del video. La cifra viene de notas secundarias, y las fuentes discrepan sobre si el video duraba tres o cuatro minutos y sobre si salió el 4 o el 5 de abril.

Las fuentes nombran los tipos y los ejemplos; la descripción del smoke test y la columna «Qué prueba» son de la base.

> [!NOTE]
> Sin fuente todavía: el MVP «mago de Oz» y el prototipo como tipos, que se usan en la práctica pero no aparecen nombrados en fuentes primarias de lo investigado. Concierge y video están sostenidos solo por resúmenes.

## Cómo se elige el MVP más barato que sirve

El criterio sale de la definición: el MVP correcto es el que aprende lo que hace falta con menos esfuerzo. En la práctica, eso es una secuencia de preguntas (inferencia de la base sobre la definición de Ries):

1. ¿Qué hipótesis se prueba, y qué resultado la refutaría?
2. ¿Cuál es la conducta más barata que, si ocurre, distingue entre que la hipótesis sea cierta o falsa?
3. ¿Qué es lo mínimo que hay que construir, o simular, para que esa conducta pueda ocurrir?

Si la respuesta a la tercera pregunta es un producto entero, probablemente la hipótesis está mal recortada. Lo que se mide después, y cómo se distingue un resultado real de uno que sube solo, es tarea de la [contabilidad de la innovación](contabilidad-de-la-innovacion.md).

> [!IMPORTANT]
> El MVP tiene críticos. Peter Thiel, en *Zero to One* (2014), lee al Lean Startup como «code for unplanned» y como «making small changes to things that already exist», según las citas que reproduce Dan Kaplan en TechCrunch (2015). Kaplan, un practicante, responde que el método parte de mapear supuestos, lo que ya es planificar, y cita a Blank: un MVP es «whatever you need to show customers to maximize your learning». Otra crítica es por sector: practicantes sostienen que en salud y servicios financieros el enfoque puede ser peligroso, y el MIT Orbit lo discute para hardware y dispositivos médicos de ciclos largos; un post en Springer Nature argumenta lo contrario para biotecnología con mercados adyacentes (todo según resúmenes del buscador). Que un MVP mal hecho dañe la marca no tiene, en lo investigado, una fuente revisada por pares.

> [!NOTE]
> Sin fuente todavía: la entrada de Blank «AI Killed the MVP – Long Live the IUP» (2026-09-25), que no se pudo leer y puede cambiar esta nota.

## La guía de Ries de 2009

La entrada «Minimum Viable Product: a guide» del blog de Ries es corta y se puede verificar; conviene leerla antes que el capítulo Test del libro. Fijarse en que el criterio de elección es el aprendizaje buscado, no el tamaño del producto.
