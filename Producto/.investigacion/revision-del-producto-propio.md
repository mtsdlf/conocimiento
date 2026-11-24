# Revisar un producto que ya existe contra una oferta nueva

Qué se sabe, contra fuentes primarias, de cómo se revisa un producto que ya anda cuando cambia lo que se vende (por ejemplo, un software que pasa a ofrecerse como servicio gestionado).

Investigado el 23/11/2026. Los niveles de evidencia que se usan:

- **estudio empírico**: un paper o un estudio con datos, publicado.
- **práctica documentada por el autor**: el que creó el método cuenta cómo se hace, sin medir si funciona.
- **opinión/consenso de practicantes**: lo dice gente del oficio, sin datos.
- **sin evidencia encontrada**: se buscó y no apareció.

Cuando una fuente es secundaria (un resumen, un blog), se marca **[secundaria]**.

## Lo corto

1. **Qué queda, qué sale y qué falta** se decide con métodos que tienen buen respaldo de práctica pero casi nada de evidencia empírica sobre su eficacia. La auditoría de uso (Intercom) y el retiro ordenado (Intercom, Gov.uk) son recetas de practicantes. Kano tiene literatura académica, y en buena parte la critica por poco confiable. El canvas de propuesta de valor y JTBD son marcos de sus autores, sin estudios que muestren que funcionan mejor que otra cosa.
2. **Lo que vive cada rol** es la parte con mejor evidencia, pero solo del lado de la evaluación de interfaces: hay estudios sobre cuántos evaluadores y cuántos usuarios hacen falta, sobre heurística contra pruebas con usuarios y sobre lo poco que coinciden los evaluadores entre sí. Los mapas (journey, blueprint) son práctica documentada y no se encontró ningún estudio de su eficacia.
3. **Bajarlo a entregables** (story mapping, pitches de Shape Up, árbol de oportunidades, criterios de aceptación, el estándar de Gov.uk) es todo práctica documentada por los autores. No se encontraron estudios.

---

## 1. Qué queda, qué sale y qué falta

### Auditoría de uso (feature audit)

- **Qué es.** Se pone cada funcionalidad en dos ejes: cuánta gente la usa y con qué frecuencia. Lo que está arriba a la derecha (mucha gente, seguido) es el corazón del producto. Se dejan afuera las cosas administrativas (crear cuenta, cambiar contraseña), que son el costo de tener un producto y no lo que lo distingue. Fuente: Des Traynor, «Before you plan your product roadmap», Intercom, 2/10/2014, https://www.intercom.com/blog/before-you-plan-your-product-roadmap/. **Práctica documentada por el autor.** Los gráficos del artículo son ilustrativos, no datos.
- **Qué hacer con una funcionalidad poco usada.** Hay cuatro salidas: matarla, conseguir que la use más gente, conseguir que la usen más seguido o mejorarla para los que ya dependen de ella. Misma fuente. **Práctica documentada por el autor.**
- **Un aviso de Intercom para el caso de un cambio de oferta.** Lo que está arriba a la izquierda (pocos lo usan, pero esos lo usan mucho) suele ser cosa de planes grandes. Antes de matarlo, hay que mirar quién es ese poco. Misma fuente.
- **Cuánto de un producto no se usa.**
  - Pendo, «2019 Feature Adoption Report»: el 80 % de las funcionalidades de un software promedio se usan poco o nunca, sobre 615 suscripciones de clientes suyos. https://www.pendo.io/resources/the-2019-feature-adoption-report/. Es **un dato de un proveedor**, sin revisión de pares ni método abierto. Las fuentes no coinciden en cuánto tiempo cubre la medición.
  - El famoso «64 % de las funcionalidades se usan poco o nunca» (Standish Group, Jim Johnson, charla en XP 2002) sale de cuatro aplicaciones internas de cuatro empresas, según Mike Cohn: https://mountaingoatsoftware.com/blog/are-64-of-features-really-rarely-or-never-used **[secundaria]**. El propio Standish dio después otras cifras (20 % se usa seguido y 50 % casi nunca, en el informe de 2013). **No sirve como evidencia general.**
- **Que la auditoría lleve a mejores decisiones: sin evidencia encontrada.**

### Retirar una funcionalidad o un servicio (sunsetting, deprecación)

- **Intercom, «How to sunset a feature»**, Des Traynor, 23/4/2015, https://www.intercom.com/blog/how-to-sunset-a-feature/. Son cuatro pasos:
  1. Confirmar que no tiene arreglo: cuántos la usan seguido, cuánto facturan esos clientes, qué se probó para subir el uso, por qué no la usan los demás y si hoy se haría igual.
  2. Dejar de ofrecerla a los nuevos: se apaga con un interruptor y se saca del material de venta y de las conversaciones comerciales.
  3. Separar a los que la probaron una vez, a los que se les puede esconder casi sin aviso, de los que dependen de ella, que necesitan atención directa.
  4. Avisar a los que quedan con fecha de cierre, el porqué, alternativas y cómo llevarse sus datos. El aviso va de un mes a un año.

  **Práctica documentada por el autor**, sin datos.
- **Gov.uk Service Manual, «Retiring your service»** (publicada el 4/8/2016, actualizada el 26/8/2025), https://www.gov.uk/service-manual/phases/retirement. Un servicio se retira si cambia la política o si hay evidencia de que la necesidad del usuario cambió. Antes de apagar hay que decir qué pasa con esa necesidad: desaparece, la cubre otro servicio o la cubre un tercero. A los usuarios se les explica qué cambia, por qué, qué tienen que hacer y qué pasa con sus datos. A los que se integran por API se los avisa temprano, y a los que usan canales asistidos, por esos canales. Las redirecciones se mantienen hasta un año. **Práctica documentada por la organización que creó el método.**
- **Que retirar funcionalidades mejore el producto o la retención: sin evidencia encontrada.** Lo que hay son argumentos («restar hace lugar para sumar»).

### Kano aplicado a lo que ya existe

- **El modelo.** Kano, Seraku, Takahashi y Tsuji, 1984, en la revista de la Sociedad Japonesa de Control de Calidad. Clasifica los atributos en:
  - **básicos (must-be):** si faltan, molestan, y si están no suman;
  - **lineales (one-dimensional):** cuanto más, mejor;
  - **atractivos:** si están encantan, y si faltan nadie los extraña;
  - **indiferentes;**
  - **inversos:** molestan si están.

  No se encontró el texto original. La descripción viene de reseñas académicas (Wikipedia, «Kano model», https://en.wikipedia.org/wiki/Kano_model **[secundaria]**).
- **Para qué sirve en un producto existente.** Las categorías se mueven con el tiempo: lo atractivo se vuelve lineal y después básico. Eso permite preguntarse qué de lo que hay es «básico» para el comprador nuevo, que, si falta, molesta, y qué es indiferente, que es candidato a esconder. Los **inversos** son los candidatos más claros a sacar. Esto último es una aplicación razonada, no algo que diga el modelo.
- **Lo que dice la evidencia: el cuestionario es frágil.**
  - Chapman y Callegaro, «Kano Analysis: A Critical Survey Science Review», Sawtooth Software Conference 2022 (los dos en Google), https://quantuxbook.com/papers/REPRINT-Chapman-Callegaro-SawtoothConference2022.pdf. Las preguntas de Kano son malos ítems de encuesta, porque piden predecir sentimientos ante algo hipotético. La teoría del puntaje tiene poco respaldo empírico, y la clasificación es inestable con menos de unos 200 encuestados. **Revisión crítica con análisis de datos.**
  - Mikulić y Prebežac, 2011, «A critical review of techniques for classifying quality attributes in the Kano model», *Managing Service Quality*, https://www.emerald.com/insight/content/doi/10.1108/09604521111100243/full/html. Compara cinco técnicas de clasificación. El cuestionario de Kano es de las pocas que sirven en la etapa de diseño, y las basadas en quejas e incidentes son válidas pero poco confiables. **Revisión académica.**
  - Para una empresa chica, con pocos compradores, **Kano por encuesta no da resultados estables**. Sirve más como vocabulario para discutir que como medición.

### Canvas de propuesta de valor (Osterwalder)

- **Qué es.** Del lado del cliente: trabajos, dolores y ganancias. Del lado de la oferta: productos y servicios, aliviadores de dolor y creadores de ganancia. Hay encaje (fit) cuando los aliviadores cubren los dolores fuertes y los creadores dan las ganancias esperadas. Osterwalder, Pigneur, Bernarda y Smith, *Value Proposition Design*, Wiley, 2014. Strategyzer: https://www.strategyzer.com/library/value-proposition-design-book-summary. **Práctica documentada por el autor.**
- **Cómo se usa contra un producto existente.** Se dibuja el mapa de valor con lo que el producto tiene hoy y se unen con líneas aliviadores y dolores. Lo que queda sin línea de un lado es lo que falta. Lo que queda sin línea del otro lado es lo que sobra para esta oferta. La técnica de «contar los dolores sin cubrir» es de una adaptación del Wade Institute, https://studio.wadeinstitute.org.au/canvas-value-proposition-canvas.html **[secundaria]**.
- **El propio autor lo dice:** el encaje es una hipótesis hasta que los clientes lo confirman con entrevistas, prototipos o experimentos (Strategyzer, misma fuente).
- **Que el canvas mejore las decisiones: sin evidencia encontrada.**

### Jobs to be done (JTBD)

- **Christensen, Hall, Dillon y Duncan**, «Know Your Customers' "Jobs to Be Done"», *Harvard Business Review*, septiembre de 2016, y el libro *Competing Against Luck*, 2016. La gente «contrata» un producto para un trabajo en una circunstancia. Entender ese trabajo, con su lado funcional, social y emocional, reduce el azar de innovar. https://hbr.org/2016/09/know-your-customers-jobs-to-be-done. **Práctica documentada por el autor.** La evidencia que dan son casos, como el del batido de McDonald's.
- **Para revisar un producto existente.** Cuando cambia la oferta, cambia el trabajo que el cliente contrata. Antes contrataba «una herramienta para hacer mi tienda» y ahora contrata «que alguien me la tenga andando». Cada funcionalidad se juzga contra el trabajo nuevo. Esto es una aplicación razonada.
- **Que JTBD dé mejores resultados que otros enfoques: sin evidencia encontrada**, más allá de casos contados por sus autores.

### Gap analysis

- Es comparar el estado actual con el deseado y listar las brechas. Es un término genérico de gestión, sin un autor ni un método canónico. En experiencia de servicio, la fuente académica de referencia es el «modelo de las brechas» de Parasuraman, Zeithaml y Berry (1985), que no se revisó en esta pasada. **Sin evidencia encontrada** de eficacia del gap analysis como técnica.

---

## 2. Cómo se mira lo que vive cada rol

### Los mapas: journey, experience map y service blueprint

- **Definiciones (NN/g).** Sarah Gibbons, «UX Mapping Methods Compared: A Cheat Sheet», 5/11/2017, https://www.nngroup.com/articles/ux-mapping-cheat-sheet/:
  - **Journey map:** un cliente puntual, en un producto o servicio puntual, en orden de tiempo, con acciones, pensamientos y emociones.
  - **Experience map:** lo mismo, pero general, sin atarse a un producto. Se hace antes del journey o para juntar varios.
  - **Service blueprint:** lo que hace la organización detrás de cada punto de contacto. Va después del journey, cuando se quiere cambiar algo adentro o encontrar dónde se rompe.

  **Práctica documentada por practicantes de referencia.**
- **Estado actual y estado futuro.** Un journey puede mapear lo que pasa hoy, para encontrar los momentos buenos y malos, o lo que se quiere que pase («to-be»), para diseñar algo que no existe. Kate Kaplan, «When and How to Create Customer Journey Maps», NN/g, 31/7/2016, https://www.nngroup.com/articles/customer-journey-mapping/. **Práctica documentada.** La autora no cita datos de eficacia.
- **El blueprint en detalle.** Tiene varios carriles: acciones del cliente, lo que se ve de frente (personas o pantallas), lo que se hace detrás, los procesos de soporte y la evidencia física. Tres líneas los separan: la de interacción, la de visibilidad y la de interacción interna. Conviene en servicios complejos, con varios canales o varias áreas, y hace falta uno por cada recorrido. Sarah Gibbons, «Service Blueprints: Definition», NN/g, 27/8/2017, https://www.nngroup.com/articles/service-blueprints-definition/.
- **Origen del blueprint.** G. Lynn Shostack, «Designing Services That Deliver», *Harvard Business Review*, enero-febrero de 1984. Lo retoman Bitner, Ostrom y Morgan, «Service Blueprinting: A Practical Technique for Service Innovation», *California Management Review* 50(3), 2008, pp. 66-94, https://cmr.berkeley.edu/2008/05/50-3-service-blueprinting-a-practical-technique-for-service-innovation/. Bitner y su equipo lo presentan con casos (IBM, Yellow Transportation, los San Francisco Giants). **Práctica documentada con casos**, sin comparación controlada.
- **Por qué sirve para nuestra pregunta.** En un servicio gestionado, el blueprint es lo único de esta familia que pone en el mismo papel al que compra, al que atiende y al que opera por detrás. El journey solo mira al cliente. Kalbach generaliza esto como «diagramas de alineación»: un lado es la experiencia de la persona, el otro lo que hace la organización, y donde se tocan se intercambia valor. Jim Kalbach, *Mapping Experiences*, O'Reilly, 2016 (2.ª ed. 2020), cap. 1, https://www.oreilly.com/library/view/mapping-experiences/9781491923528/maex_ch01.xhtml. **Práctica documentada por el autor.**
- **Límites.**
  - Un mapa vale lo que vale la investigación que lo alimenta. NN/g dice que puede salir de hipótesis o de datos reales.
  - Un mapa de estado futuro es una hipótesis.
  - El blueprint no muestra emociones del cliente, porque omite a propósito ese detalle.
- **Evidencia de que los mapas funcionan.**
  - Følstad y Kvale, «Customer journeys: a systematic literature review», *Journal of Service Theory and Practice*, 2018, https://sintef.brage.unit.no/sintef-xmlui/bitstream/handle/11250/2483763/Customer%252Bjourney%252Bliterature%252Breview_authors%252Bversion.pdf?sequence=4. Revisan 45 papers. El campo es conceptual y fragmentado, y casi no hay estudios que comparen el recorrido ideal con el real para encontrar brechas. **Revisión sistemática**, que encuentra que falta la evidencia.
  - **Que un journey map o un blueprint mejoren resultados (ventas, retención, satisfacción): sin evidencia encontrada.**

### Evaluación heurística

- **Origen.** Nielsen y Molich, «Heuristic evaluation of user interfaces», CHI 1990. Nielsen, *Usability Engineering*, 1993, y el capítulo de 1994 en *Usability Inspection Methods*.
- **Cuántos evaluadores.** Un evaluador solo encuentra en promedio el 35 % de los problemas (entre 19 % y 51 % en seis casos). La curva es N(1 − (1 − l)^i). La recomendación es de 3 a 5 evaluadores, y en el ejemplo de costo y beneficio el óptimo dio 4. Jakob Nielsen, «How to Conduct a Heuristic Evaluation / The Theory Behind Heuristic Evaluations», NN/g, 1/11/1994, https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/theory-heuristic-evaluations/. **Estudio empírico** (seis casos propios, más Nielsen y Landauer 1993).
- **Qué no hace.** No reemplaza la investigación con usuarios. Que algo viole una heurística no quiere decir que sea un problema en ese contexto. Kate Moran y Kelley Gordon, «How to Conduct a Heuristic Evaluation», NN/g, 25/6/2023, https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/. **Práctica documentada.**

### Pruebas de uso con usuarios: ¿cuántos?

- **Virzi 1992.** Con 4 o 5 participantes se encuentra el 80 % de los problemas, y los graves aparecen primero. Robert Virzi, «Refining the test phase of usability evaluation: how many subjects is enough?», *Human Factors* 34(4), 457-471, https://journals.sagepub.com/doi/10.1177/001872089203400407. **Estudio empírico.**
- **Nielsen: 5 usuarios por ronda**, en estudios cualitativos, con estas condiciones:
  - se itera, porque varias rondas chicas rinden más que una grande;
  - con varios grupos de usuarios distintos, 3 o 4 por grupo;
  - para números (estudios cuantitativos), 20 o más.

  Jakob Nielsen, «How Many Test Users in a Usability Study?», NN/g, 3/6/2012, https://www.nngroup.com/articles/how-many-test-users/, sobre Nielsen y Landauer 1993. **Estudio empírico más práctica del autor.**
- **La crítica: Faulkner 2003.** Hizo 100 simulaciones sobre 60 usuarios reales. Con 5 usuarios, el porcentaje de problemas encontrados fue de casi 100 % a apenas 55 %, según qué cinco tocaran. Con 10 usuarios, el mínimo subió mucho. Laura Faulkner, «Beyond the five-user assumption», *Behavior Research Methods, Instruments & Computers* 35(3), 379-383, https://pubmed.ncbi.nlm.nih.gov/14587545/. **Estudio empírico.** Las cifras exactas se tomaron de resúmenes **[secundaria]**, porque el texto completo no estaba abierto.
- **Qué sale de esto.** Con roles muy distintos (el comercio, su cliente comprador, el que opera), cada rol es un grupo aparte. Cinco en total no alcanzan: hacen falta unos pocos por rol.

### Recorrido cognitivo (cognitive walkthrough)

- **Qué es.** Un evaluador recorre una tarea paso a paso con los ojos de un usuario nuevo y en cada paso se pregunta si el usuario sabría qué hacer, si vería cómo hacerlo y si entendería que avanzó. Mide sobre todo qué tan fácil es aprender a usarlo. Wharton, Rieman, Lewis y Polson, «The cognitive walkthrough method: a practitioner's guide», en Nielsen y Mack (eds.), *Usability Inspection Methods*, Wiley, 1994, pp. 105-140. NN/g, «Defining Cognitive Walkthroughs», https://www.nngroup.com/articles/cognitive-walkthroughs/. **Práctica documentada por los autores.** El texto exacto de las cuatro preguntas no se verificó en el original.
- **Cuándo conviene.** Para tareas que alguien hace pocas veces o por primera vez, como el alta de un comercio o la primera configuración. Es relevante si la oferta nueva pone a alguien de adentro a operar en lugar del cliente.

### Heurística contra pruebas con usuarios: la evidencia

- **Jeffries, Miller, Wharton y Uyeda**, «User interface evaluation in the real world: a comparison of four techniques», CHI 1991, pp. 119-124, https://doi.org/10.1145/108844.108862 (texto en https://www.miramontes.com/writing/uievaluation/). **Estudio empírico.** Evaluaron el mismo producto con cuatro técnicas:

  | Técnica | Problemas | Entre los más graves | Horas-persona |
  |---|---|---|---|
  | Heurística (especialistas en interfaz) | 105 | 28 | 35 |
  | Pruebas con usuarios | 31 | 18 | 199 |
  | Guías de diseño | 35 | 12 | 86 |
  | Recorrido cognitivo | 35 | 9 | 43 |

  - La heurística encontró más problemas y más barato, pero requiere varios especialistas, y produce muchos problemas menores y puntuales.
  - Las pruebas con usuarios encontraron los problemas graves, recurrentes y generales. El peor de todos (borrar sin querer la carpeta del usuario) lo encontraron **solo** las pruebas.
  - Límites: la técnica se confunde con la experiencia de quien la aplicó, y fue un solo producto con seis usuarios.
- **La crítica metodológica: Gray y Salzman 1998.** Wayne Gray y Marilyn Salzman, «Damaged Merchandise? A Review of Experiments That Compare Usability Evaluation Methods», *Human-Computer Interaction* 13(3), 203-261, https://rauterberg.employee.id.tue.nl/lecturenotes/JFS-lecture/Gray&Salzman98a_HCI.pdf. Revisan cinco comparaciones influyentes, entre ellas la de Jeffries 1991, y encuentran fallas de validez que no permiten sacar las conclusiones que la práctica sacó («la heurística es más eficiente», etc.). **Revisión metodológica.** Hubo réplica en el mismo número.
- **El efecto evaluador.**
  - Hertzum y Jacobsen, «The evaluator effect: a chilling fact about usability evaluation methods», *International Journal of Human-Computer Interaction* 13(4), 2001, https://forskning.ruc.dk/da/publications/the-evaluator-effect-a-chilling-fact-about-usability-evaluation-m/. En 11 estudios, dos evaluadores que miran lo mismo coinciden entre el 5 % y el 65 % de los problemas. Pasa con la heurística, con el recorrido cognitivo y con las pruebas pensando en voz alta. **Revisión de estudios empíricos.**
  - Estudios CUE de Rolf Molich: equipos profesionales evaluando el mismo sitio. En CUE-2 (9 equipos), el 75 % de los problemas los encontró un solo equipo (Molich y otros, *Behaviour & Information Technology* 23(1), 2004). **Estudio empírico.** Las cifras se tomaron de resúmenes **[secundaria]** (https://measuringu.com/evaluator-effect/, de Jeff Sauro, y dscout).
  - **Qué sale de esto.** Ningún método, ni ningún evaluador solo, da «la lista» de problemas. Hacen falta varios evaluadores o varias rondas, y combinar métodos.

### Cuándo usar cuál (síntesis, con su nivel)

| Para ver… | Método | Respaldo |
|---|---|---|
| El recorrido entero de un rol, de punta a punta, incluido lo que pasa fuera de la pantalla | Journey map de estado actual, con datos reales | Práctica documentada, sin estudios de eficacia |
| Cómo se reparte el trabajo entre el que compra, el que atiende y el que opera | Service blueprint | Práctica documentada con casos (Shostack 1984, Bitner 2008) |
| Problemas de pantalla rápidos y baratos | Heurística, con 3 a 5 evaluadores | Estudio empírico (Nielsen), discutido (Gray y Salzman) |
| Tareas de primera vez | Recorrido cognitivo | Práctica documentada y un estudio comparativo (Jeffries 1991) |
| Los problemas graves de verdad | Pruebas con usuarios reales, unos pocos por rol y en rondas | Estudio empírico (Virzi, Nielsen, Faulkner, Jeffries) |

---

## 3. Cómo baja a especificaciones y entregables

### Del recorrido al backlog: user story mapping (Jeff Patton)

- **Qué es.** Arriba, de izquierda a derecha, van las actividades grandes del usuario en orden de tiempo: la columna vertebral, que no se prioriza. Abajo de cada una, las tareas, más arriba cuanto más necesarias. Lo de más arriba de punta a punta es el **esqueleto que camina**: el sistema mínimo que funciona entero, un término que Patton toma de Alistair Cockburn. Las entregas se marcan como franjas horizontales. Patton dice que la lista plana de historias es una «bolsa de hojas sin árbol». Para productos que ya existen, sugiere un mapa chico por funcionalidad. Jeff Patton, «The New User Story Backlog is a Map», 8/10/2008, actualizado en 2023, https://jpattonassociates.com/the-new-backlog/, y el libro *User Story Mapping*, O'Reilly, 2014. **Práctica documentada por el autor.**
- **El puente con el journey.** La columna vertebral del story map tiene la misma forma que las etapas de un journey (acciones en el tiempo). Pasar de uno al otro es natural, pero ni Patton ni NN/g lo formalizan en las fuentes revisadas. Es una inferencia.

### Shape Up: el pitch (Basecamp)

- **Qué es.** Un pitch tiene cinco partes. Ryan Singer, *Shape Up*, Basecamp, 2019, cap. 6, https://basecamp.com/shapeup/1.5-chapter-06. **Práctica documentada por el autor.**
  1. **Problema:** una historia concreta de por qué lo de hoy no anda.
  2. **Apetito:** cuánto tiempo estamos dispuestos a gastar, por ejemplo dos o seis semanas. Es un tope que achica la solución, no una estimación.
  3. **Solución:** bocetos gruesos, sin diseño visual cerrado.
  4. **Agujeros (rabbit holes):** lo que puede descarrilar el trabajo, resuelto en pocas líneas.
  5. **Lo que no entra (no-gos):** lo que se deja afuera a propósito para entrar en el apetito.
- **Para un producto existente.** Los «no-gos» y el apetito son la herramienta explícita para decir qué no se hace. Lo que una auditoría marca como «sale» o «se esconde» puede ir como no-go del pitch.

### Árbol de oportunidades y soluciones (Teresa Torres)

- **Qué es.** Arriba va un resultado a mover, mejor si es un comportamiento del cliente. Debajo, las oportunidades: necesidades, dolores y deseos. Debajo, las soluciones. Debajo, las pruebas de supuestos. Las oportunidades salen de entrevistas que piden historias concretas del pasado («contame la última vez que…»), se ordenan en un mapa de experiencia y se cuelgan del momento donde ocurren. Las ventas, los reclamos y la analítica sirven para elegir de qué entrevistar, no como fuente directa. Teresa Torres, «Opportunity Solution Trees», Product Talk, 6/12/2023, https://www.producttalk.org/opportunity-solution-trees/, y *Continuous Discovery Habits*, 2021. **Práctica documentada por la autora.**
- **El puente con el journey.** Torres sí lo formaliza: el mapa de experiencia es la primera capa de las oportunidades.
- **Evidencia.** La autora no cita estudios del árbol en sí, solo investigación general de que comparar opciones mejora las decisiones. **Sin evidencia encontrada** de eficacia del método.

### Criterios de aceptación

- **Dado / cuando / entonces (Given/When/Then).** Lo propusieron Dan North y Chris Matts dentro de BDD, con antecedentes de 2004 y el texto «Introducing BDD» de 2006 (https://dannorth.net/introducing-bdd/). North, en «What's in a Story?», agrega que el «dado» define todo el contexto necesario y nada más (https://dannorth.net/whats-in-a-story/). Martin Fowler lo describe como una forma de especificar el comportamiento con ejemplos: https://martinfowler.com/bliki/GivenWhenThen.html. **Práctica documentada por el autor.** Los detalles de historia se tomaron de la Agile Alliance y de Wikipedia **[secundaria]**.
- **Para nuestra pregunta.** Cada paso del blueprint («el comercio pide un cambio; el que atiende lo recibe; el que opera lo hace») se puede escribir como escenario con dado, cuando y entonces, para cada rol. Esto es una inferencia.
- **Evidencia de eficacia: sin evidencia encontrada** en esta pasada.

### El estándar de servicio de Gov.uk

- Son 14 puntos. Los que tocan esta pregunta son:
  - **1.** Entender a los usuarios y sus necesidades.
  - **2.** Resolver un problema entero para el usuario, no un pedazo.
  - **3.** Unir la experiencia en todos los canales, incluidos los que no son digitales.
  - **8.** Iterar y mejorar seguido.
  - **10.** Definir qué es el éxito y publicar los datos de cómo anda.
  - **14.** Operar un servicio confiable.

  Gov.uk Service Manual, «Service Standard», https://www.gov.uk/service-manual/service-standard. **Práctica documentada por la organización.** Se usa como vara de evaluación en auditorías formales del gobierno británico.
- **Para un servicio gestionado.** Los puntos 2, 3 y 14 son los que más pesan: el problema entero del comercio, todos los canales (también el humano) y que ande siempre.
- **Evidencia de que aplicar el estándar mejora resultados: sin evidencia encontrada.**

---

## Sin evidencia

Se buscaron y **no se encontraron** estudios empíricos (controlados, cuantitativos o comparativos) sobre:

1. **La eficacia de la auditoría de funcionalidades** (uso por frecuencia): no hay estudios de que lleve a mejores decisiones o resultados. Los datos de cuánto no se usa son de un proveedor (Pendo) o de una muestra chica y vieja (Standish).
2. **Que retirar o esconder funcionalidades mejore retención, satisfacción o foco.** Hay solo argumentos y recetas (Intercom, Gov.uk).
3. **La eficacia del canvas de propuesta de valor.** Sus autores lo presentan como hipótesis a validar, sin estudios.
4. **La superioridad de JTBD sobre otros enfoques.** Hay casos de sus autores, no estudios comparativos.
5. **La eficacia del gap analysis** como técnica.
6. **La eficacia de los journey maps y los service blueprints.** Una revisión sistemática (Følstad y Kvale 2018) encuentra el campo conceptual y sin comparaciones entre recorrido ideal y real. Bitner 2008 aporta casos, no comparaciones.
7. **La eficacia de user story mapping, de los pitches de Shape Up, del árbol de oportunidades y de los criterios de aceptación con dado/cuando/entonces.** Son todos práctica documentada por sus autores.
8. **La eficacia del Service Standard de Gov.uk** en resultados medidos.
9. **Ningún estudio sobre el caso puntual** de un software que pasa a venderse como servicio gestionado, y qué conviene revisar del producto en ese pasaje.

Lo único con evidencia empírica real es la **evaluación de interfaces** (heurística, pruebas con usuarios, recorrido cognitivo), y esa misma evidencia está discutida: Gray y Salzman 1998, y el efecto evaluador de Hertzum y Jacobsen 2001 y los estudios CUE. Kano tiene literatura académica abundante, en buena parte crítica de su confiabilidad.

## Lo que no se pudo verificar en el original

- El texto de Kano 1984, en japonés.
- Las cuatro preguntas exactas de Wharton y otros 1994.
- Las cifras exactas de Faulkner 2003 y de los estudios CUE: se tomaron de resúmenes.
- El texto completo de Christensen y otros 2016, que tiene muro de pago.
- La página oficial del canvas en Strategyzer, que devolvió solo la navegación.
