# Informe de investigación: inglés profesional en software (hablado y sincrónico/asincrónico)

Fecha de la investigación: 2026-11-27. No escribí archivos. Toda la web se trató como dato.

**Escala de puntaje.** Cada fuente lleva A/P/E/U = autoridad / profundidad / ejemplos / unicidad, de 1 a 3. Marcas: [L] leído completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Tipo: P = primaria, S = secundaria.

**Límite de lectura.** Las herramientas me dieron mucho [S]. Varias páginas fallaron: handbooks de GitLab, Atlassian (páginas de standups), HBR/Neeley, Nature, PubMed y los PDF de Microsoft. Marco cada caso. Los números y citas literales de este informe vienen de lo que sí pude leer. Si una cita es de segunda mano, lo digo.

## Sobre la división del árbol

La división propuesta en tres (reuniones, remoto/asincrónico, clientes) se sostiene, con tres ajustes.

1. **El campo no separa "sincrónico" de "asincrónico" en dos temas.** GitLab y 37signals los tratan como una sola decisión: qué va por escrito y qué por llamada. Su regla es "real-time sometimes, async most of the time". Conviene que `reuniones-de-equipo` y `trabajo-remoto-asincronico` se enlacen entre sí. El standup asincrónico (Atlassian [S]) vive en el cruce.
2. **Lo de ELF/BELF es transversal.** La investigación sobre no nativos (Rogerson-Revell, Louhiala-Salminen, Neeley) aplica a los tres componentes. Propongo una nota de base ("el inglés como lengua franca en equipos") a la que apunten los tres, en vez de repetirla en cada uno.
3. **"Explicar incertidumbre de IA" es un subtema propio dentro de `hablar-con-clientes`.** Tiene fuentes distintas (van der Bles, Google PAIR) y una frase modelo propia. Y "Forward-deployed" es un rol, no una habilidad: la nota sobre FDE debería ser contexto y no un componente.

---

## Componente 1: reuniones-de-equipo

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Scrum Guide (nov 2020), Daily Scrum, Planning, Retro | https://scrumguides.org/scrum-guide.html | P (oficial) | 3/2/1/3 | [L] sección leída |
| Stray, Moe, Sjøberg, "Daily Stand-Up Meetings: Start Breaking the Rules" (IEEE Software 37(3), 70-77, 2020; preprint arXiv 2018) | https://arxiv.org/abs/1808.07650 | P (empírica) | 3/3/2/3 | [M] abstract; cuerpo no leído |
| Jason Yip, "It's Not Just Standing Up" (martinfowler.com) | https://www.martinfowler.com/articles/itsNotJustStandingUp.html | S (practicante) | 2/3/3/2 | [L] |
| Atlassian Team Playbook, Retrospective | https://www.atlassian.com/team-playbook/plays/retrospective | S (practicante/empresa) | 2/2/2/1 | [L] |
| Atlassian Team Playbook, Stand-ups | https://www.atlassian.com/team-playbook/plays/standups | S (empresa) | 2/2/2/1 | [S] (la página excedió el límite de descarga; datos vía buscador) |
| Bezos, carta a accionistas 2016 ("disagree and commit") | https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders | P (documento de empresa) | 2/1/3/3 | [L] pasaje |
| Rogerson-Revell (2010), *Journal of Business Communication* 47(4) | https://strategy-business.com/article/re00128 | S del estudio | 3/2/2/3 | [S] (resumen en strategy+business; paper pago) |
| OpenStack Contributor Guide, "Non-native English speakers" | https://docs.openstack.org/contributor-guide/non-native-english-speakers.html | P (guía comunitaria) | 2/1/2/2 | [L] |
| Erin Meyer, *The Culture Map* (2014) / HBR 2014 | https://hbr.org/2014/05/navigating-the-cultural-minefield | S (practicante) | 2/3/2/2 | [M] (solo la apertura; no pude leer el cuerpo) |

### Afirmaciones

- **El Daily Scrum, oficialmente.** "The purpose of the Daily Scrum is to inspect progress toward the Sprint Goal". Dura 15 minutos y es "for the Developers of the Scrum Team". Los Developers "can select whatever structure and techniques they want". Eso desmiente que las "tres preguntas" sean obligatorias. https://scrumguides.org/scrum-guide.html
- **Retro, oficialmente.** "The purpose of the Sprint Retrospective is to plan ways to increase quality and effectiveness." La versión es noviembre de 2020. https://scrumguides.org/scrum-guide.html
- **Las tres preguntas son una convención.** Yip las describe como *Yesterday Today Obstacles*: "What did I accomplish yesterday?", "What will I do today?", "What obstacles are impeding my progress?". Recoge además la sugerencia de poner los obstáculos primero. https://www.martinfowler.com/articles/itsNotJustStandingUp.html
- **Qué decir y qué no.** Yip: "Tell the headline, not the whole story" y "It's a time to raise issues and surface ideas, not a time for in-depth problem-solving". https://www.martinfowler.com/articles/itsNotJustStandingUp.html
- **Evidencia empírica.** Stray et al. observaron 102 standups y entrevistaron a 60 miembros de 15 equipos en cinco países. Hallaron que muchos tienen experiencias negativas, lo que baja la satisfacción, la confianza entre compañeros y el bienestar. Proponen cuatro recomendaciones. https://arxiv.org/abs/1808.07650
- **Retro (Atlassian).** Cinco pasos: tono (~5 min), recoger feedback (~15), convertirlo en insights (~20), acciones con dueño y fecha (~15) y cierre (~5). Formatos: 4Ls (loved, loathed, learned, longed for) y Sad/Mad/Glad. "Focus on improving instead of blaming people for mistakes". https://www.atlassian.com/team-playbook/plays/retrospective
- **Disagree and commit.** Bezos escribió: "Look, I know we disagree on this but will you gamble with me on it? Disagree and commit?". Su propia respuesta en un caso fue "I disagree and commit and hope it becomes the most watched thing we've ever made." https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders
- **Reuniones internacionales.** En el estudio de Rogerson-Revell (reuniones del GCAE, un grupo europeo de actuarios), nativos y no nativos solían dejar pasar los errores menores ("let it pass") para centrarse en el contenido, y casi no se corregían. Eso era práctico y cortés, pero no reducía la frustración de los no nativos ni evitaba malentendidos. Evitar modismos ("going through the roof"), las agendas estrictas y las intervenciones preparadas ayudaban. Conclusión: "Successful accommodation is a two-way street". https://strategy-business.com/article/re00128 [S]
- **Guía comunitaria.** Para nativos: "Speak slowly and use simple words and sentences", circular la agenda antes y compartir notas después. Para no nativos: prepararse antes. https://docs.openstack.org/contributor-guide/non-native-english-speakers.html
- **Discrepancias entre fuentes.**
  - Scrum Guide: el Daily no tiene formato fijo. Yip y Atlassian: sí describen un formato de tres preguntas (Atlassian lo formula como "Since the last Stand-up, I have… / Before the next Stand-up, I will… / What's slowing me down is…" [S]).
  - Meyer (secundario, no leí el cuerpo): una búsqueda ubica a EE.UU. en comunicación de bajo contexto y a Argentina en alto contexto, pero las fuentes secundarias se contradicen sobre la franqueza de la evaluación negativa de EE.UU. Argentina no tiene posición verificada.

### Frases modelo con respaldo

- "Since the last stand-up, I have… / Before the next stand-up, I will… / What's slowing me down is…" (Atlassian, [S]).
- "I know we disagree on this, but will you gamble with me on it? Disagree and commit?" (Bezos, [L]).
- "I disagree and commit." (Bezos, [L]).
- Faltan frases respaldadas por fuente para "no llego", "estoy bloqueado" y "¿podés aclarar?". Ver huecos.

### Recurso canónico

- **Scrum Guide 2020, sección Daily Scrum** (una página), para saber qué es oficialmente. Fijarse en que no impone preguntas.
- Complementos: **Stray et al. 2020** (cuerpo del artículo) para qué falla en la práctica, y **Yip** para el patrón y las 12 antipatrones.
- Para la base ELF de este componente: **Rogerson-Revell 2010**, aunque el original es pago.

---

## Componente 2: trabajo-remoto-asincronico

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| 37signals/Basecamp, "The 37signals Guide to Internal Communication" (30 reglas) | https://basecamp.com/guides/how-we-communicate | P (handbook público) | 2/3/2/3 | [L] |
| GitLab Handbook, async / sync vs async / effective communication / cross-culture guide | https://handbook.gitlab.com/handbook/communication/sync-vs-async-culture/ | P (handbook) | 3/3/2/3 | [S] (los cuerpos no se leyeron; los 404 y el volumen de menús lo impidieron) |
| Yang et al., "The effects of remote work on collaboration among information workers", *Nature Human Behaviour* 6, 43-54 (2022) | https://www.nature.com/articles/s41562-021-01196-4 | P (empírica) | 3/3/1/3 | [S] (la página de Nature redirige a login; datos vía buscador, press y Microsoft Research) |
| Mok et al., "Large Scale Characteristics of Synchronous Collaboration Across Time Zones" (CHI 2023, Microsoft) | https://www.microsoft.com/en-us/research/uploads/prod/2023/02/Large-Scale-Characteristics-of-Synchronous-Collaboration-Across-Time-Zones-CHI-2023.pdf | P (empírica) | 3/3/1/3 | [S] (PDF no legible) |
| Neeley, "Global Business Speaks English" (HBR, mayo 2012, 90(5): 116-124) y *The Language of Global Success* (Princeton, 2017) | https://hbr.org/2012/05/global-business-speaks-english | P/S (académica + libro) | 3/3/2/2 | [M] (resumen y primer párrafo; cuerpo pago) |
| Jenkins, Cogo, Dewey (2011), *Language Teaching* 44(3): 281-315 | https://www.cambridge.org/core/journals/language-teaching/article/review-of-developments-in-research-into-english-as-a-lingua-franca/47A99C70A696371F7F9F06351D0963F1 | P (revisión académica) | 3/3/1/3 | [S] (abstract vía buscador) |
| Louhiala-Salminen y Kankaanranta (2011), *IEEE Trans. Prof. Communication*; (2013), Ibérica | https://aaltodoc.aalto.fi/items/22f74326-82c6-4293-a985-d105de9a80d3 | P (académica) | 3/3/1/3 | [S] (el PDF falló con 403) |
| nohello.net | https://nohello.net/en/ | S (practicante) | 1/1/3/1 | [L] |
| OpenStack, guía no nativos | https://docs.openstack.org/contributor-guide/non-native-english-speakers.html | P (guía comunitaria) | 2/1/2/2 | [L] |

### Afirmaciones

- **Asincrónico por defecto (37signals).** "Real-time sometimes, asynchronous most of the time." (regla 2). "Writing solidifies, chat dissolves." (6). "Speaking only helps who's in the room, writing helps everyone." (7). "The expectation of immediate response is toxic." (9). "Urgency is overrated, ASAP is poison." (21). "Communication shouldn't require schedule synchronization." (15). "If you have to repeat yourself, you weren't clear enough the first time." (10). "Be proactive about 'wait, what?' questions by providing factual context and spatial context." (14). "If you want an answer, you have to ask a question." (19). "Ask if things are clear." (28). https://basecamp.com/guides/how-we-communicate
- **GitLab (solo por el buscador, [S]).**
  - Comunicación de bajo contexto: se asume que el otro tiene poco contexto y se da todo el contexto posible.
  - Guía de colaboración entre culturas: defiende bajo contexto (precisión, simplicidad, claridad).
  - Regla de escalamiento: si un hilo va y viene tres veces, se pasa a video.
  - Todo lo escrito se hace en inglés.
  - Fuentes: https://handbook.gitlab.com/handbook/company/culture/all-remote/management y https://handbook.gitlab.com/handbook/company/culture/cross-culture-collaboration-guide/. Pendiente leer los cuerpos antes de citar literal.
- **Evidencia empírica (Microsoft, Yang et al.).** El trabajo remoto a escala de empresa volvió la red de colaboración "more static and siloed, with fewer bridges between disparate parts"; la comunicación sincrónica bajó y la asincrónica subió. En resúmenes secundarios, el tiempo con gente de otros grupos baja cerca de un 25 % y las horas de reunión bajan cerca de un 5 %. Esas cifras no las leí en el original. https://www.nature.com/articles/s41562-021-01196-4 [S]
- **Husos horarios.** La reunión entre husos acelera la coordinación, pero cuesta encontrar solapamiento y se discute quién carga con el costo. https://www.microsoft.com/en-us/research/uploads/prod/2023/02/Large-Scale-Characteristics-of-Synchronous-Collaboration-Across-Time-Zones-CHI-2023.pdf [S]
- **La escritura ayuda a los no nativos.** OpenStack: "asynchronous written communications (such as email) are easier for non-native English speakers". https://docs.openstack.org/contributor-guide/non-native-english-speakers.html
- **Carga de los no nativos (Neeley, [S]).**
  - Todos los empleados no nativos de la empresa francesa estudiada ("Frenchco") sintieron pérdida de estatus sin importar el nivel de inglés. Lo más difícil fue para quienes tenían fluidez media.
  - En Rakuten, el plazo de dos años obligaba a subir de 650 sobre 990 en TOEIC o enfrentar descenso o despido. Según una reseña, el 90 % cumplió.
  - Son estudios de caso de una sola empresa. https://hbr.org/2012/05/global-business-speaks-english y https://www.strategy-business.com/article/When-a-Japanese-Company-Adopted-English-as-a-First-Language
  - Opuesto o matiz: Neeley defiende que el inglés único es una decisión estratégica. Rogerson-Revell, Jenkins y Louhiala-Salminen enfatizan acomodación mutua y no un estándar nativo.
- **ELF/BELF.** El modelo de Louhiala-Salminen y Kankaanranta separa tres capas de competencia comunicativa global: multicultural, BELF y conocimiento del negocio. https://aaltodoc.aalto.fi/items/22f74326-82c6-4293-a985-d105de9a80d3 [S]
- **"No hello" (practicante).** "Just ask the question!". Ejemplo: "Hiya! What time was that thing?" en un solo mensaje. Sin autor ni fecha precisa (menciona 2022; la idea original se atribuye a nohello.com, archivado desde 2013). https://nohello.net/en/ [L]
- **Discrepancia entre fuentes.** 37signals desaconseja chat como canal de decisión; OpenStack y la idea ELF señalan que los no nativos suelen preferir la escritura. Pero Rogerson-Revell sugiere que en reuniones en vivo la preparación (agenda, notas) también reduce la carga. No es contradicción, pero la nota debería distinguir ambos casos.

### Frases modelo con respaldo

- "Hiya! What time was that thing?" (nohello, [L]), como patrón de pregunta directa en un solo mensaje.
- Los títulos de reglas de 37signals sirven como frases de política de equipo ("Is this clear?", "Ask if things are clear" [L]). No hay una fuente leída con frases de status update ni de zonas horarias. Ver huecos.

### Recurso canónico

- **37signals, "Guide to Internal Communication"** (basecamp.com/guides/how-we-communicate). Se lee en una sentada. Fijarse en las reglas 2, 6, 7, 9, 14 y 15. Es la más citable y legible.
- Para el respaldo empírico: **Yang et al. 2022** (abstract y figuras). Para el costo en no nativos: **Neeley** (HBR 2012 o el libro).
- **GitLab** es el estándar de una empresa grande y pública, pero hay que leer sus cuerpos antes de recomendarlo.

---

## Componente 3: hablar-con-clientes

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| van der Bles et al. (2019), *Royal Society Open Science* 6(5): 181870 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6549952 | P (empírica/revisión) | 3/3/2/3 | [M] abstract y Box 5a leídos; cuerpo no |
| van der Bles et al. (2020), *PNAS* 117(14): 7672-7683 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7149229 | P (empírica) | 3/3/1/3 | [S] |
| Google PAIR, People + AI Guidebook, "Errors + Graceful Failure" | https://pair.withgoogle.com/chapter/errors-failing/ | P (guía de empresa) | 2/2/2/3 | [L] |
| Google PAIR, "Explainability + Trust" | https://pair.withgoogle.com/chapter/explainability-trust/ | P (guía de empresa) | 2/2/2/3 | [L] |
| Palantir, "Dev versus Delta" | https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87 | P (blog de empresa) | 2/2/1/3 | [S] (la lectura directa dio 403 en el post "Day in the life"; este se citó por buscador) |
| a16z, "The Palantirization of Everything" (Andrusko, 16 ene 2026) | https://a16z.com/the-palantirization-of-everything/ | S (analista/inversor) | 2/2/1/2 | [L] |
| Fitzpatrick, *The Mom Test* | https://www.momtestbook.com/ | S (libro de practicante) | 2/2/3/2 | [M] (sitio oficial sin las reglas; reglas vía resúmenes) |
| Cohan, *Great Demo!* (2003; 2005; 3.ª ed.) | https://www.goodreads.com/book/show/278137 | S (libro de practicante) | 2/2/2/2 | [S] |
| Pragmatic Engineer, "Forward deployed engineers" | https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers | S (periodismo) | 2/2/2/1 | [S] (solo apareció en resultados) |

### Afirmaciones

- **Incertidumbre (van der Bles 2019).**
  - Propone tres objetos de incertidumbre (hechos, números, ciencia) y dos niveles (directa e indirecta, esta última sobre la calidad de la evidencia).
  - Lista nueve formas de expresar la incertidumbre directa: distribución completa, resumen (intervalo), cifra redondeada o rango, categoría predefinida, calificativo verbal ("probably", "very likely"), lista de posibilidades, reconocimiento general, no mencionarla, negarla.
  - Consejos al comunicador (Box 5a): "What do you have uncertainty about?", "Why is there uncertainty?", elegir una expresión "that suits the degree of precision you have", separar la magnitud de la incertidumbre de la magnitud de la evidencia, y que "stating uncertainty does not necessarily undermine trust".
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC6549952
- **Costo en confianza (van der Bles 2020, [S]).** Cinco experimentos con 5.780 participantes. Se percibe más incertidumbre, pero la confianza baja poco, sobre todo con expresiones verbales. https://pmc.ncbi.nlm.nih.gov/articles/PMC7149229
- **Errores de un sistema de IA (PAIR).** Tipos: context errors, failstates, happy accidents, background errors. "What the user considers an error is deeply connected to their expectations of the AI system." Fuentes de error: datos de entrenamiento, entrada, relevancia, jerarquía de sistemas. Hay que dar camino tras el fallo: pedir feedback, devolver el control al usuario. Tono: "be human, not machine"; honesto y humilde. https://pair.withgoogle.com/chapter/errors-failing/
- **Explicación y confianza (PAIR).** Apuntar a confianza calibrada, no total. "The best explanation is likely a partial one." Hay que explicar más cuando las apuestas son altas. Confianza en categorías (alta/media/baja) o en n-mejores alternativas; los porcentajes numéricos son riesgosos porque la gente no sabe leerlos. https://pair.withgoogle.com/chapter/explainability-trust/
- **Demos (Cohan, [S]).** El defecto típico es mostrar demasiadas features y dejar que el comprador "buy it back", reconstruyendo el valor por su cuenta. Propone abrir con el resultado, mostrar solo las capacidades que importan y adaptar la demo a cada comprador. https://customerthink.com/demo-do-let-your-champion-drive/ y https://www.reprise.com/?p=4809
- **Relevamiento (Mom Test, [S]).** Tres reglas: hablar de la vida del cliente y no de tu idea, preguntar por específicos del pasado y no por opiniones sobre el futuro, y hablar menos y escuchar más. No pude verificar la redacción literal contra el libro. https://www.shortform.com/blog/what-is-the-mom-test/ (secundaria). Ojo: el PDF que devolvió el buscador es una copia con marca de compra ("Sold to…"), así que no la recomiendo como fuente.
- **FDE (Palantir).** Palantir llama "Devs" y "Deltas" a sus dos grandes grupos de ingeniería. Un Delta trabaja con un cliente y "measures success by the impact on that customer's goal"; la fórmula "one capability, many customers" (Dev) frente a "one customer, many capabilities" (Delta) aparece en su página de carreras. https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87 [S]
- **FDE (a16z).** Los FDE "sit inside the customer's organization", a menudo por meses. La prueba de un modelo creíble es poder decir no a lo custom: "How do you decide not to customize?". Es una posición de inversor, con escepticismo sobre su escala. https://a16z.com/the-palantirization-of-everything/
- **Discrepancia.** van der Bles reporta costo bajo de confianza por mencionar incertidumbre; PAIR advierte que los números de confianza pueden inducir confianza mal calibrada. Son compatibles: una habla de hechos/números públicos; la otra, de la UI de un modelo. La nota debe distinguir cuándo mostrar la cifra y cuándo una categoría.

### Frases modelo con respaldo

- Los calificativos verbales y las expresiones directas del esquema de van der Bles ("probably", "very likely") son respaldo de verbos de incertidumbre. El paper trae una escala de nueve formas, no un banco de frases.
- Para errores, PAIR respalda el tono, no frases. El texto: "be human, not machine", admitir errores, explicar límites e invitar a seguir.
- No encontré frases literales respaldadas por fuente para "explicar por qué un modelo se equivoca", para "manejar expectativas" ni para preguntas de discovery en inglés. Ver huecos.

### Recurso canónico

- **Para explicar incertidumbre: van der Bles 2019**, Box 5a (consejos al comunicador) y la escala de nueve expresiones. Fijarse en separar incertidumbre directa e indirecta.
- **Para errores de IA con clientes: PAIR, capítulos "Errors + Graceful Failure" y "Explainability + Trust".** Fijarse en las categorías de error y en "partial explanation".
- **Para discovery: *The Mom Test*** (libro entero, corto). Es secundaria de practicante, y no pude verificar el texto directo.
- **Para demos: *Great Demo!*** (Cohan), con la misma salvedad.

---

## Huecos

1. **Cuerpos de GitLab sin leer.** Las páginas de async, sync-vs-async, effective communication y cross-culture existen pero no pude extraer su texto. Antes de citar literal hay que leerlas (o usar la API de GitLab en bruto).
2. **Atlassian standups.** La página real superó el límite de descarga. Los enunciados "Since the last Stand-up…" vienen del buscador y no están verificados.
3. **Texto original sin leer.** Estos solo se vieron por resumen: Stray et al. (solo abstract), Yang et al. (Nature/PubMed devolvieron login/cookies), Mok et al. CHI 2023 (PDF), Rogerson-Revell (solo vía strategy+business), Jenkins et al., Louhiala-Salminen y Kankaanranta, Neeley (HBR pago).
4. **Meyer.** No leí el cuerpo ni el mapa de países (es de pago). La posición de Argentina frente a EE.UU. en las escalas de comunicar, evaluar y discrepar no está verificada, y las fuentes secundarias se contradicen sobre EE.UU. en evaluación negativa.
5. **Mom Test y Cohan.** Solo [S]. No pude verificar las reglas ni el método contra el texto original.
6. **Planning y estimación.** No encontré en esta ronda una fuente primaria sobre estimación (planning poker, story points) ni sobre cómo hablar en planning, más allá de la frase de la Scrum Guide ("lays out the work to be performed"). Hueco real.
7. **Frases modelo.** Faltan frases respaldadas para: "no llego", "estoy bloqueado", pedir aclaraciones, discrepar con cortesía en un hilo, status updates escritos, avisar de husos horarios, explicar por qué un modelo falla y manejar expectativas. Habría que buscar un material de inglés profesional (por ejemplo, material de British Council sobre reuniones internacionales, que apareció pero no leí) o escribirlas como propias y marcarlas sin fuente.
8. **Shape Up, Doist y las guías de Slack.** No las busqué ni las encontré en esta ronda. Shape Up trata de ciclos de producto más que de comunicación, así que probablemente no sirva.
9. **Palantir blog.** Solo vía buscador; sin lectura directa. El post "A Day in the Life of a Palantir FDSE" dio 403.
10. **Microsoft sobre ingenieros de software.** No hallé un estudio de MS Research específico sobre ingenieros de software en 2021-2022. Lo más cercano es Yang et al. (trabajadores de información en general).
11. **Investigación sobre explicar IA a no técnicos en un contexto de consultoría.** PAIR y van der Bles cubren el diseño de producto y la comunicación pública de ciencia, no la conversación consultor-cliente. El campo no parece tener una fuente específica; conviene declararlo en la nota.
