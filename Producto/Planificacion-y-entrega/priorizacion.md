---
resumen: >-
  Priorizar es decidir en qué orden se construye lo que vale la pena construir. Los métodos más citados lo resuelven con un puntaje (RICE, costo de demora) o con una clasificación (Kano), y cada uno sirve para un tipo de decisión distinto.
estado: vigente
estabilidad: semi
fuentes:
  - "Sean McBride, RICE: Simple prioritization for product managers (Intercom, 2018-01-05): https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/"
  - "SAFe, Weighted Shortest Job First: https://framework.scaledagile.com/wsjf/"
  - "Donald Reinertsen, The Principles of Product Development Flow (Celeritas, 2009), cap. 3, según Scrum.org y Wikipedia (no leído): https://www.scrum.org/node/106834 ; https://wikipedia.com/wiki/Cost_of_delay"
  - "Kano, Seraku, Takahashi y Tsuji (1984), Journal of the Japanese Society for Quality Control 14(2), pp. 147-156 (solo abstract): https://www.jstage.jst.go.jp/article/quality/14/2/14_KJ00002952366/_article/-char/en"
  - "Wikipedia, Kano model (consultado 2026-11-22; la sección sobre el cambio de categoría no tiene referencias): https://en.wikipedia.org/wiki/Kano_model"
  - "Martin Löfgren y Lars Witell (2008), Two Decades of Using Kano's Theory of Attractive Quality: A Literature Review, Quality Management Journal, DOI 10.1080/10686967.2008.11918056: https://doi.org/10.1080/10686967.2008.11918056 (solo abstract, vía OpenAlex)"
  - "Producto/.investigacion/competencia-y-precios.md"
  - "Críticas a RICE: https://dzone.com/articles/rice-score ; https://michaelgoitein.substack.com/p/why-prioritization-frameworks-are?open=false"
  - "Producto/.investigacion/planificacion-y-entrega.md"
aliases: [prioritization, prioritización de producto, RICE, WSJF, costo de demora, cost of delay]
creado: 2026-11-22
revisado: 2026-11-22
---

# Priorización

Priorizar es decidir en qué orden se construye lo que vale la pena construir. Los métodos más citados lo resuelven con un puntaje (RICE, costo de demora) o con una clasificación (Kano), y cada uno sirve para un tipo de decisión distinto.

Priorizar no es descubrir. El [descubrimiento](../Descubrimiento/descubrimiento.md) decide si una idea vale la pena; la priorización ordena las que pasaron. Es una de las tres respuestas a "qué hacemos y en qué orden" que reúne [Planificación y entrega](planificacion-y-entrega.md), junto con el [roadmap](roadmap.md) y las apuestas de [Shape Up](shape-up.md).

## RICE: alcance, impacto, confianza y esfuerzo

RICE lo publicó Sean McBride en el blog de Intercom el 5 de enero de 2018. A veces se lo fecha en 2016; la página del artículo dice 2018, y la diferencia puede ser una republicación o un uso interno anterior. Se cita 2018 como fecha de publicación.

Cada idea recibe cuatro números:

| Factor | Cómo se mide según McBride |
|---|---|
| Reach (alcance) | "number of people/events per time period" |
| Impact (impacto) | massive 3, high 2, medium 1, low 0.5, minimal 0.25 |
| Confidence (confianza) | high 100%, medium 80%, low 50%; debajo de 50%, "total moonshot" |
| Effort (esfuerzo) | "person-months" |

El artículo muestra la fórmula que combina los cuatro factores solo como imagen, y el informe no la transcribe: el detalle se lee en el original. Según sus críticos (ver más abajo), el factor de confianza es el que más dice del método: reconoce que los otros tres son estimaciones.

## Costo de demora y WSJF: cuando el valor depende del momento

El costo de demora mide, en la definición habitual, cuánto se pierde por cada unidad de tiempo que algo no está entregado (la definición no figura en los pasajes leídos). SAFe abre su página con la frase de Reinertsen: "If you only quantify one thing, quantify the Cost of Delay." El libro de Reinertsen es de 2009; la regla de dividir costo de demora por duración se llama también CD3 (Cost of Delay Divided by Duration), y SAFe la popularizó como WSJF.

SAFe define WSJF como "the relative cost of delay divided by the relative job duration". El costo de demora se arma con tres insumos: valor para el usuario y el negocio, criticidad temporal y reducción de riesgo o habilitación de oportunidades. El denominador es el tamaño del trabajo. Lo corto y urgente sube; lo grande y sin apuro baja.

> [!NOTE]
> Sin fuente todavía: el capítulo 3 de Reinertsen leído en el original. Lo que se dice acá del costo de demora y de CD3 viene de resúmenes. Circula una cifra de Reinertsen, "~85% de los product managers no conocen su costo de demora", citada de segunda mano y sin método verificado: no se usa como dato.

## Kano: clasificar atributos, no ordenarlos

El modelo de Kano no da un orden. Según el abstract del artículo de 1984, propone reemplazar la idea de calidad unidimensional por una bidimensional y clasifica los elementos de un producto en atractivos, imprescindibles (*must-be*) y unidimensionales. Lo probaron con una encuesta a consumidores sobre televisores y relojes de mesa. Un seguimiento de Koo y Nakajo (2001) encontró que la categoría de un atributo depende del tipo de producto.

Sirve para saber qué da satisfacción y qué solo evita la queja, no para secuenciar el trabajo. Esa lectura sale de fuentes secundarias.

Frente a los competidores, Kano ordena qué se da por sentado en la categoría. Según Wikipedia, Kano llamó *must-be* a lo que es "the price of entry into a market", y los atributos se corren de atractivos a imprescindibles "as customer expectations change with the level of performance from competing products"; esa sección no cita fuente. En un SaaS, lo que todos los rivales ya traen (exportar datos, por ejemplo) se trata como imprescindible aunque nadie lo pida. La [matriz de funcionalidades](../../Estrategia-competitiva/Analisis-de-competidores/desarme-de-producto.md#la-matriz-de-funcionalidades) dice qué traen los rivales; la clasificación del cliente sigue haciendo falta (inferencia de esta base). Löfgren y Witell (2008), en una revisión de 33 artículos, advierten según su abstract que muchos desarrollos del método "lack sufficient scientific rigor".

> [!NOTE]
> Sin fuente todavía: cómo se aplica Kano (el cuestionario con pregunta funcional y disfuncional) y críticas con método. Solo se leyó el abstract.

## Qué método sirve para qué

La tabla es una síntesis del informe de investigación de esta base, no de una fuente que compare los métodos; la columna de lo que no sirve es inferencia a partir de la primera.

| Método | Sirve para | No sirve para |
|---|---|---|
| RICE | Ordenar ideas de mejora o crecimiento comparables entre sí, en el mismo producto, con alcance medible | Comparar cosas de naturaleza distinta (una mejora contra una obligación contractual) |
| Costo de demora / WSJF | Trabajo en cola cuyo valor depende del tiempo: ventanas de mercado, fechas contractuales, riesgo | Ideas sin urgencia, donde la criticidad temporal es cero para todas |
| Kano | Clasificar atributos por su efecto en la satisfacción | Decidir qué se construye primero |

Para una consultora o una agencia que trabaja con fechas firmadas, el costo de demora es el que incorpora la fecha en la cuenta. RICE supone que el equipo elige libremente entre ideas, cosa que en un contrato no siempre pasa (inferencia a partir de la tabla, sin fuente).

## Dónde falla puntuar

> [!IMPORTANT]
> No hay estudios con método que muestren que puntuar mejore las decisiones de producto. Lo que hay es opinión de practicantes en blogs.
>
> A favor: McBride presenta el número de RICE como una ayuda para decidir.
>
> En contra: según resúmenes de DZone y de Michael Goitein, RICE es útil si apoya el juicio y peligroso si lo reemplaza; el puntaje convierte el desacuerdo en aritmética ("scoring theater"); y el factor de confianza es la admisión de que la precisión es falsa.
>
> Las dos posiciones coinciden en lo práctico, según la lectura de esta base: el puntaje ordena una conversación, no la cierra.

Lectura de esta base, sin fuente: la falla más común es tratar el número como un resultado. Un puntaje de RICE hereda la incertidumbre de sus cuatro estimaciones, y la multiplicación la esconde. La otra es puntuar ideas que nadie probó: si el [descubrimiento](../Descubrimiento/prueba-de-supuestos.md) no redujo el riesgo, el impacto es un deseo con decimales.

## Qué leer

El artículo de McBride en Intercom es corto. Sus partes más útiles son la escala de impacto y de confianza y el aviso de que el número es una ayuda. Para el costo de demora, el recurso primario es el capítulo 3 de *The Principles of Product Development Flow* de Reinertsen; la página de WSJF de SAFe da la versión operativa con sus tres insumos.
