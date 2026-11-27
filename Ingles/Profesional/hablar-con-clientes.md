---
resumen: >-
  Hablar con clientes en inglés, para un rol técnico, es relevar necesidades preguntando por hechos
  pasados, mostrar el producto en una demo que abre con el resultado y explicarle a alguien no
  técnico qué hace un sistema, cuándo se equivoca y cuánta incertidumbre hay.
estado: borrador
estabilidad: semi
fuentes:
  - "van der Bles et al. (2019), Communicating uncertainty about facts, numbers and science, Royal Society Open Science 6(5), 181870: https://pmc.ncbi.nlm.nih.gov/articles/PMC6549952"
  - "van der Bles et al. (2020), The effects of communicating uncertainty on public trust in facts and numbers, PNAS 117(14), vía resumen: https://pmc.ncbi.nlm.nih.gov/articles/PMC7149229"
  - "Google PAIR, People + AI Guidebook, Errors + Graceful Failure: https://pair.withgoogle.com/chapter/errors-failing/"
  - "Google PAIR, People + AI Guidebook, Explainability + Trust: https://pair.withgoogle.com/chapter/explainability-trust/"
  - "Fitzpatrick, The Mom Test, vía resumen secundario: https://www.shortform.com/blog/what-is-the-mom-test/"
  - "Cohan, Great Demo!, vía resúmenes secundarios: https://customerthink.com/demo-do-let-your-champion-drive/"
  - "Palantir, Dev versus Delta: demystifying engineering roles at Palantir, vía resumen: https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87"
  - "Andrusko, The Palantirization of everything (a16z, 16 de enero de 2026): https://a16z.com/the-palantirization-of-everything/"
aliases:
  - Customer communication
  - Client communication
  - Demo
  - Discovery
  - Forward deployed engineer
  - FDE
  - Explicar incertidumbre
creado: 2026-11-27
revisado:
---

# Hablar con clientes

Hablar con clientes en inglés, para un rol técnico, es relevar necesidades preguntando por hechos pasados, mostrar el producto en una demo que abre con el resultado y explicarle a alguien no técnico qué hace un sistema, cuándo se equivoca y cuánta incertidumbre hay.

Es lo diario de los roles de consultoría y de los *forward-deployed engineers*. Palantir distingue al ingeniero que construye "one capability, many customers" del que trabaja para "one customer, many capabilities" y mide su éxito por el impacto en el objetivo de ese cliente (según el resumen de su blog). Según a16z, estos ingenieros "sit inside the customer's organization", a menudo durante meses. Cómo se relevan y se miden las necesidades en general está en [Entrevista de usuario](../../UX/Investigacion/entrevista-de-usuario.md) y en [Especificación](../../Desarrollo/Definicion/especificacion.md); acá va el inglés de esas conversaciones.

## Relevar: preguntar por lo que pasó, no por lo que harían

*The Mom Test*, de Rob Fitzpatrick, resume en tres reglas cómo preguntarle a un cliente sin que te mienta por amabilidad, según resúmenes secundarios del libro: hablar de su vida y no de tu idea, preguntar por hechos concretos del pasado y no por opiniones sobre el futuro, y hablar menos y escuchar más. En inglés eso cambia el tiempo verbal de las preguntas. Algunos ejemplos propios:

| Pregunta débil | Pregunta que trae hechos |
|---|---|
| *Would you use a tool that does X?* | *How do you handle X today?* |
| *Do you think this is a problem?* | *When was the last time this happened? What did you do?* |
| *How much would you pay for this?* | *What have you already tried? How much did it cost you?* |

El condicional (*would you*) invita a una opinión; el pasado simple y el presente (*did you*, *do you*) piden un hecho. Cómo funcionan esos tiempos está en [Condicionales e hipótesis](../Gramatica/condicionales-e-hipotesis.md) y en [Tiempo y aspecto](../Gramatica/tiempo-y-aspecto.md).

## La demo: el resultado primero

Cohan, en *Great Demo!*, describe el defecto típico de una demo, según resúmenes secundarios: mostrar demasiadas funciones y dejar que el cliente reconstruya solo el valor. Propone abrir con el resultado, mostrar solo lo que le importa a ese cliente y adaptar la demo a cada uno. Es la [respuesta primero](../Discurso/estructura-del-argumento.md#respuesta-primero-con-una-advertencia) aplicada a mostrar un producto. Una apertura con esa forma (ejemplo propio):

> *Let me start with the end result: this is the report your team will get every Monday, with every flagged transaction and the reason it was flagged. Then I'll show you the two steps that produce it.*

Durante la demo sirve anunciar cada paso (*Now I'm going to…*), chequear (*Does this match how your team works?*) y tener lista una frase para cuando algo falla en vivo (*That's not what should happen. Let me show you with a different example and I'll follow up on this one*).

## Explicar por qué un modelo se equivoca

La guía *People + AI* de Google trata los errores de los sistemas de IA desde el diseño de producto, pero sus ideas sirven para la conversación con un cliente. La central: "What the user considers an error is deeply connected to their expectations of the AI system." Separa errores de contexto, fallas del sistema, aciertos por casualidad y errores que el usuario ni nota, y ubica sus causas en los datos de entrenamiento, la entrada, la relevancia y la combinación de sistemas. Para explicar, apunta a una confianza **calibrada**, no total: "The best explanation is likely a partial one", y hay que explicar más cuando hay más en juego. El tono que pide es honesto y humilde: "be human, not machine".

Llevado a una conversación, eso da una estructura en tres pasos (una inferencia propia): qué esperaba el cliente, por qué el modelo hizo otra cosa, y qué se puede hacer (cambiar los datos, poner a una persona a revisar los casos dudosos, aceptar una tasa de error). Un ejemplo:

> *The model flagged this invoice because it looks very similar to the fraudulent ones it learned from: same supplier pattern, unusual amount. It's not reading the contract, so it can't know this one was approved. For cases like this, we can route low-confidence results to your team for review.*

## Decir cuánta incertidumbre hay

Van der Bles y colegas (2019), en un trabajo sobre cómo comunicar incertidumbre del que se leyeron el resumen y el recuadro de consejos, listan nueve formas de expresarla: la distribución completa, un intervalo, un número redondeado o un rango, una categoría predefinida, un calificativo verbal (*probably*, *very likely*), una lista de posibilidades, un reconocimiento general, no mencionarla y negarla. Sus consejos para quien comunica empiezan por "What do you have uncertainty about?" y "Why is there uncertainty?", y piden elegir una expresión "that suits the degree of precision you have". Agregan que "stating uncertainty does not necessarily undermine trust". En cinco experimentos con 5.780 personas, mostrar la incertidumbre hizo que se la percibiera más, pero bajó poco la confianza (van der Bles et al., 2020, según su resumen; cómo varía el efecto entre números y palabras no quedó claro en lo leído).

PAIR advierte algo que parece ir en contra: en la interfaz de un modelo, los porcentajes de confianza son riesgosos porque la gente no sabe leerlos, y propone categorías como alta, media y baja. Las dos fuentes son compatibles, porque una habla de números públicos y la otra de la pantalla de un producto. Para una conversación con un cliente no técnico, y como inferencia propia, conviene dar la categoría y el porqué (*It's right most of the time on standard invoices, but much less reliable on handwritten ones*) y tener el número listo para quien lo pida.

> [!NOTE]
> Sin fuente todavía: investigación sobre cómo explicar IA a no técnicos en una conversación de consultoría (PAIR y van der Bles cubren el diseño de producto y la comunicación pública de la ciencia), y el texto original de *The Mom Test* y *Great Demo!* (solo resúmenes).
