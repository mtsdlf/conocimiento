---
resumen: >-
  El acuerdo inicial es la conversación con la que arranca un encargo: el cliente y quien
  desarrolla fijan qué problema se resuelve, qué resultado se busca, quién decide, qué
  restricciones hay y qué queda afuera de la primera versión. Termina en un acuerdo entre
  personas; la especificación que lee un agente empieza después.
estado: borrador
estabilidad: estable
fuentes:
  - "Caroli, Lean Inception (martinfowler.com), leído: https://www.martinfowler.com/articles/lean-inception"
  - "Singer, Shape Up, cap. 2, Principles of Shaping, leído: https://basecamp.com/shapeup/1.1-chapter-02"
  - "Boag (2024), Pricing Projects As A Freelancer Or Agency Owner, Smashing Magazine: https://smashingmagazine.com/2024/08/pricing-projects-freelancer-agency-owner/"
  - "PMI, PMBOK Guide 7a ed., ficha (no se abrió el texto): https://www.pmi.org/pmbok-guide-standards/foundational/PMBOK"
  - "DORA, State of AI-assisted Software Development 2025: https://dora.dev/dora-report-2025/"
  - "Desarrollo/.investigacion/encargo.md"
aliases: [kickoff, reunión de arranque, inception, lean inception, project charter, acta de constitución, discovery inicial]
creado: 2026-11-27
revisado:
---

# Acuerdo inicial

El acuerdo inicial es la conversación con la que arranca un encargo: el cliente y quien desarrolla fijan qué problema se resuelve, qué resultado se busca, quién decide, qué restricciones hay y qué queda afuera de la primera versión. Termina en un acuerdo entre personas; la especificación que lee un agente empieza después.

Viene después de la venta y antes de la [especificación](../Definicion/especificacion.md). Las [preguntas de descubrimiento](../../Ventas/Descubrimiento-y-calificacion/preguntas-de-descubrimiento.md) de Ventas ya sacaron el problema y cuánto le cuesta al cliente, lo suficiente para proponerle algo. El acuerdo inicial va más hondo: decide qué entra en la primera versión. Lo que sale de acá es la base del [alcance y aceptación](alcance-y-aceptacion.md).

## Qué tiene que quedar escrito al terminar

El corte entre acuerdo inicial y especificación es de esta base: el acuerdo termina cuando hay respuesta, por escrito y confirmada por el cliente, a estas preguntas.

| Pregunta | Por qué hace falta |
|---|---|
| Qué problema se resuelve y para quién | Sin esto, lo que se especifica después puede estar bien hecho y no servir |
| Qué resultado busca el cliente y cómo se va a notar | Es lo que después se convierte en criterios de aceptación |
| Qué es y qué no es el producto, qué hace y qué no hace | Fija lo que queda afuera antes de que alguien lo pida |
| Quién decide del lado del cliente | Los cambios y las aceptaciones necesitan una persona que diga sí |
| Restricciones: plazo, presupuesto, sistemas con los que tiene que convivir | Acotan la solución y la estimación |
| Qué entra en la primera versión | Es la decisión que separa un acuerdo de una lista de deseos |

La tercera fila sale de Lean Inception, que la arma como el ejercicio «Is – Is not – Does – Does not». Las demás son la síntesis de esta base sobre las fuentes de abajo; ninguna fuente leída da la lista entera.

## Dos formas de llegar al acuerdo

Lean Inception es la forma de taller. Caroli la describe como «a focused form of inception, which can be done in a single week», con una agenda por día: el lunes la visión del producto y el «Is – Is not – Does – Does not»; el martes personas y funciones; el miércoles una revisión técnica, de experiencia y de negocio, y los recorridos de usuario; el jueves las funciones sobre esos recorridos y su secuencia; el viernes el MVP canvas y una muestra a los interesados. El resultado es «the understanding the MVP». Según el resumen del buscador, el formato busca reducir a una semana las inceptions tradicionales de dos a cuatro.

Shape Up es la forma de recorte. En lugar de una lista de requisitos, el equipo recibe un problema ya trabajado que es «rough», «solved» y «bounded»: «It tells the team where to stop». El *pitch* «summarizes the problem, constraints, solution, rabbit holes, and limitations», y viene con un apetito, el tiempo que se está dispuesto a gastar. Shape Up está escrito para un equipo con producto propio; cómo se usa con un cliente externo está en [Shape Up](../../Producto/Planificacion-y-entrega/shape-up.md#shape-up-en-una-consultora), y el paso de oportunidad a solución acotada, en [dar forma a una solución](../../Producto/Descubrimiento/dar-forma-a-una-solucion.md).

Para un encargo chico, la lectura de esta base es que una semana de talleres sobra y alcanzan una o dos sesiones que contesten la tabla de arriba. Cuando el problema es demasiado incierto para cotizar la construcción, la práctica de agencias es cobrar primero un descubrimiento aparte, como cuenta [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#cotizar-después-de-achicar-la-incertidumbre).

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre la reunión de arranque con un cliente externo (quién va, qué se acuerda, qué se firma), y el contenido del *project charter* según el PMBOK, que no se pudo abrir. Lo que se suele decir del charter (un documento corto que autoriza el proyecto, nombra al responsable y fija objetivos y restricciones) es práctica general sin cita.

## Por qué pesa más cuando construye un agente

La lectura de esta base es que el acuerdo inicial es donde más pesa el cuello de botella nuevo. Un agente construye rápido lo que se le pide; si el problema o el resultado se entendieron mal, se entrega rápido lo equivocado. Se apoya en la tesis de DORA 2025 de que la IA amplifica lo que la organización ya hace, bueno o malo, pero ninguna fuente lo midió en el arranque de un proyecto.

El prototipo también cambió de precio. Un prototipo que anda cuesta hoy mucho menos que antes, y eso empuja a reemplazar parte de la conversación por algo a lo que el cliente pueda reaccionar. Es práctica emergente: el informe de la vertical no encontró fuente que la mida. El riesgo, en criterio de esta base, es que el prototipo se tome por acuerdo: el cliente dice que sí a lo que ve y nadie escribió qué problema resuelve ni qué queda afuera. Qué prueba un prototipo y qué no está en [producto mínimo viable](../../Emprender/Validacion/producto-minimo-viable.md).

## Cómo falla el acuerdo inicial

- Sale una lista de funciones en vez de un problema y un resultado. Después no hay contra qué decidir qué recortar.
- Nadie del cliente tiene la última palabra, y cada incremento se discute con alguien distinto.
- Lo que queda afuera no se escribe, y aparece como pedido a mitad del proyecto (ver [cambios de alcance](cambios-de-alcance.md)).
- Se reemplaza por un documento de requisitos largo. En criterio de esta base, ese documento como entregable del arranque es de lo que [pierde peso](../Fundamentos/lo-que-pierde-peso-en-desarrollo.md).

Para leer: el artículo de Caroli en el sitio de Fowler, corto y con la agenda por día, y el capítulo 2 de Shape Up para entender qué es un problema acotado. En los dos, fijate en que el resultado sea una decisión sobre la primera versión.
