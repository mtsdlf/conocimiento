# Informe: Inglés Profesional (ESP para la industria del software), marco, vocabulario técnico y entrevista técnica

Fecha de la investigación: 2026-11-27. No escribí archivos.

**Convenciones.**
- Marcas de lectura: [L] leí completo (o la parte relevante), [M] solo metadatos o abstract, [S] resumen secundario o del buscador.
- Puntajes de 1 a 3 en cada eje: autoridad (A), profundidad (P), ejemplos (E), unicidad (U).
- Todo lo que viene de la web es dato. Varias páginas bloquearon la lectura (403, reCAPTCHA, Anubis). Eso se declara en cada tabla y en los huecos.
- Honestidad sobre la lectura: de los papers ESP y BELF no pude abrir ningún texto completo. Todo lo que cito de ellos es de bibliografía, abstracts o excerpts del buscador.

---

## Aviso sobre el árbol propuesto

Las tres piezas (marco, vocabulario-tecnico, entrevista-tecnica) son razonables, pero el campo ESP divide distinto en tres puntos.

1. **Needs analysis no es solo del marco.**
   - En ESP es el método que decide el contenido de todo lo demás: situación meta, situación actual y necesidades de aprendizaje.
   - Convendría que `marco` explique el método y que cada componente (entrevista, vocabulario) declare qué necesidad cubre.
   - No hay un estudio de needs analysis para ingenieros de software hispanohablantes en LatAm que yo haya encontrado (ver huecos).
2. **Falta una pieza que el campo considera central: comunicación escrita y de reuniones.**
   - La investigación BELF y de equipos globales de software (Slack, PRs, daily, emails) apunta a esto como el uso diario real.
   - La entrevista es un evento puntual. Sugiero una pieza hermana, por ejemplo `comunicacion-en-el-trabajo`, o ampliar `marco` con la lista de géneros (genre analysis).
3. **Pronunciación y falsos amigos son dos temas distintos** (fonología y léxico). En el campo no se agrupan. Pueden convivir en `vocabulario-tecnico`, pero conviene dos secciones separadas.

---

## 1. Componente `marco`

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Louhiala-Salminen, Charles & Kankaanranta (2005), "English as a lingua franca in Nordic corporate mergers: Two case companies", *English for Specific Purposes* 24(4), 401–421 | https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi.dedup.....3390208ff2572664bc1b155ebc40496f (comentario de Kankaanranta, 2023, que la describe) | primaria (descrita por secundaria) | 3 | 3 | 2 | 3 | [S] |
| Kankaanranta & Louhiala-Salminen (2010), "English? – Oh, it's just work!", *ESP* | https://core.ac.uk/download/80716712.pdf | primaria | 3 | 3 | 3 | 2 | [S] (403 al leerla; solo vi cómo la cita el buscador) |
| Kankaanranta & Planken (2010), "BELF competence as business knowledge…", *Journal of Business Communication* 47(4), 380–407, DOI 10.1177/0021943610377301 | https://aaltodoc.aalto.fi/items/10b4f1e6-18cd-4dec-b01f-8fe00c1e8866 | primaria | 3 | 3 | 2 | 3 | [S] (Anubis bloqueó la página; datos bibliográficos y conclusión vía buscador) |
| Kankaanranta & Louhiala-Salminen (2013), Ibérica, sobre el paso de "Business English as Lingua Franca" a "English as Business Lingua Franca" | https://doaj.org/article/7f2a78e32f514e0aad10ed4a74b76592 | primaria | 3 | 2 | 1 | 2 | [S] (403) |
| Swales (1990), *Genre Analysis: English in Academic and Research Settings*, Cambridge UP | https://genreacrossborders.uwaterloo.ca/biblio/genre-analysis-english-academic-and-research-settings | primaria (referencia bibliográfica) | 3 | 3 | 3 | 3 | [S] (ficha bibliográfica; el buscador no devolvió las definiciones) |
| Dudley-Evans & St John (1998), *Developments in ESP*, Cambridge UP | https://en.wikipedia.org/wiki/English_for_specific_purposes | secundaria | 1 | 1 | 1 | 1 | [S] (Wikipedia, texto garbled) |
| Wang et al. (2025), CSCW vol. 34, no nativos en equipos de software globales | https://dl.eusset.eu/items/7b6a3438-77c6-4cce-8eea-a664ef824e99/full | primaria | 2 | 2 | 2 | 3 | [S] |
| Neeley (HBS), 96 trabajadores en 6 equipos de desarrollo de una empresa tecnológica global | https://www.library.hbs.edu/working-knowledge/language-wars-divide-global-companies | secundaria | 2 | 2 | 2 | 3 | [S] |
| Estudios de needs analysis en IT (Kazajistán, 85 egresados; Indonesia, 95 estudiantes; uin-malang, 243 estudiantes y 23 profesionales) | https://journal.uny.ac.id/index.php/cp/article/download/52373/pdf/168994 · https://doaj.org/article/bda758f701fb4236a70c305b847ae12f · https://ejournal.uin-malang.ac.id/index.php/jetle/article/download/12202/pdf | primarias de baja escala | 1 | 1 | 1 | 2 | [S] |

### Afirmaciones con URL

- BELF se introdujo en el artículo de 2005 de *English for Specific Purposes*, con comunicación interna entre finlandeses y suecos en dos fusiones corporativas nórdicas. El primer proyecto fue de 2000 a 2002 y estudió dos fusiones "over the Gulf of Bothnia". Fuente: https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi.dedup.....3390208ff2572664bc1b155ebc40496f
- Datos del artículo: volumen 24, número 4, páginas 401–421, año 2005. Fuente: búsqueda del título exacto; la cita bibliográfica coincide en los resultados (https://core.ac.uk/download/14919771.pdf, no abierto).
- BELF es "English used as a shared communication code in business within the global business discourse community" (paráfrasis del buscador, no cita literal). Fuente: https://dialnet.unirioja.es/descarga/articulo/4510884.pdf [S]
- El acrónimo pasó de "Business English as Lingua Franca" a "English as Business Lingua Franca". Fuente: https://doaj.org/article/7f2a78e32f514e0aad10ed4a74b76592 [S]
- Kankaanranta y Planken (2010) concluyen que la competencia en BELF "can be considered an essential component of business knowledge required in today's global business environment". Muestra: encuesta en línea N=987 y entrevistas N=27, en entornos europeos. Fuente: https://aaltodoc.aalto.fi/items/10b4f1e6-18cd-4dec-b01f-8fe00c1e8866 [S]
- Su marco posterior de "Global Communicative Competence" lista business know-how, competencia en BELF y competencia multicultural. Fuente: misma búsqueda [S].
- Swales (1990) es el libro canónico de genre analysis. Su objetivo declarado es pedagógico: ofrecer un enfoque para enseñar inglés académico y de investigación. Fuente: https://genreacrossborders.uwaterloo.ca/biblio/genre-analysis-english-academic-and-research-settings [S]
- Dudley-Evans y St John listan como características variables de ESP: limitado a ciertas habilidades, sin metodología preestablecida y por lo general para estudiantes intermedios o avanzados. Es el perfil B2 a C1 del lector. Fuente: https://en.wikipedia.org/wiki/English_for_specific_purposes [S]. Verificar contra el libro.
- Estudios de needs analysis en IT:
  - Kazajistán: 85 egresados de tres institutos de IT; las destrezas clave fueron lectura, escucha y habla. Fuente: https://journal.uny.ac.id/index.php/cp/article/download/52373/pdf/168994 [S]
  - Indonesia: 95 estudiantes de informática, 10 áreas de uso del inglés. Fuente: https://doaj.org/article/bda758f701fb4236a70c305b847ae12f [S]
  - uin-malang: 243 estudiantes y 23 profesionales. Fuente: https://ejournal.uin-malang.ac.id/index.php/jetle/article/download/12202/pdf [S]
  - Tema recurrente: brecha entre el currículo universitario y los requisitos laborales, y lectura como habilidad dominante. Las muestras son pequeñas, de estudiantes y no de LatAm.
- No nativos en equipos de software globales:
  - Wang et al. (2025) entrevistaron a 27 desarrolladores chinos y encontraron que la falta de "capital lingüístico" les impide acceder a otros capitales. Fuente: https://dl.eusset.eu/items/7b6a3438-77c6-4cce-8eea-a664ef824e99/full [S]
  - Neeley siguió a 96 trabajadores de 6 equipos de desarrollo en una empresa que estandarizó el inglés dos años antes. Fuente: https://www.library.hbs.edu/working-knowledge/language-wars-divide-global-companies [S]
  - Un estudio mixto sobre reuniones y Slack reporta que la calidad de la comunicación baja en segunda lengua y que quienes tienen más confianza dominan las reuniones. Fuente: https://arxiv.org/pdf/2007.02328 [S]

**Discrepancia a registrar.** No hallé conflicto directo entre fuentes. Hay una diferencia de énfasis: los estudios de needs analysis en IT (estudiantes) subrayan la lectura. Wang y el estudio de Slack/reuniones, con profesionales, subrayan el habla y la participación en reuniones. Esa diferencia es un dato de diseño para la vertical.

### Recurso canónico del componente
- **Kankaanranta & Louhiala-Salminen (2010), "English? – Oh, it's just work!"** (https://core.ac.uk/download/80716712.pdf).
  - Qué parte: toda; es corta.
  - En qué fijarse: cómo los profesionales perciben su propio inglés como "just work", con foco en que el mensaje funcione y no en la corrección. Ese es el criterio para definir "C1 profesional".
  - Estado: no la pude abrir; hay que leerla antes de usarla.
- **Complemento:** el capítulo introductorio de Swales (1990) para la noción de género y comunidad discursiva.

### Frases modelo
Ninguna fuente leída las respalda. Este componente no necesita frases.

---

## 2. Componente `vocabulario-tecnico`

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| nginx.org, página principal | https://nginx.org/en/ | primaria | 3 | 1 | 1 | 3 | [L] |
| YAML 1.2.2 spec | https://yaml.org/spec/1.2.2/ | primaria | 3 | 1 | 1 | 3 | [L] (solo el abstract y el cap. 1; leí 100.000 de 191.847 caracteres) |
| MySQL Reference Manual, "What is MySQL?" | https://dev.mysql.com/doc/refman/8.0/en/what-is-mysql.html | primaria | 3 | 1 | 2 | 3 | [L] |
| PostgreSQL docs, historia | https://www.postgresql.org/docs/current/history.html | primaria | 3 | 1 | 1 | 2 | [L] |
| kernel.org SillySounds | https://www.kernel.org/pub/linux/kernel/SillySounds/ | primaria | 3 | 1 | 1 | 3 | [M] (listado de archivos, sin texto) |
| Opensource.com, Grunenwald sobre kubectl | https://opensource.com/article/18/12/kubectl-definitive-pronunciation-guide | secundaria | 2 | 1 | 1 | 2 | [L] |
| Microsoft k8s-on-azure-workshop | https://microsoft.github.io/k8s-on-azure-workshop/module-1/architecture/kube-ctl/index.html | secundaria | 2 | 1 | 1 | 1 | [S] |
| Wikipedia, GIF | https://en.wikipedia.org/wiki/GIF | secundaria | 1 | 2 | 2 | 1 | [L] (leí 100.000 de 159.182 caracteres) |
| Merriam-Webster (SQL, GIF) | https://www.merriam-webster.com/dictionary/GIF | primaria | 3 | 2 | 1 | 2 | no leída (403) |
| Cambridge Dictionary | https://dictionary.cambridge.org | primaria | 3 | 2 | 1 | 2 | no leída (la búsqueda no devolvió las entradas) |

### Afirmaciones con URL

- **nginx.** La página oficial dice: `nginx ("engine x")`. Se dice "engine-x". Fuente: https://nginx.org/en/ [L]
- **YAML.**
  - El abstract de la especificación dice que se pronuncia "rhymes with 'camel'" (rima con "camel"). Fuente: https://yaml.org/spec/1.2.2/ [L]
  - Es un "recursive acronym for 'YAML Ain't Markup Language'". Fuente: https://yaml.org/spec/1.2.2/ [L]
- **MySQL y SQL.**
  - Cita literal: "The official way to pronounce 'MySQL' is 'My Ess Que Ell' (not 'my sequel'), but we do not mind if you pronounce it as 'my sequel' or in some other localized way." Fuente: https://dev.mysql.com/doc/refman/8.0/en/what-is-mysql.html [L]
  - La misma página solo expande SQL como "Structured Query Language"; no dice cómo se pronuncia SQL a secas. Fuente: https://dev.mysql.com/doc/refman/8.0/en/what-is-mysql.html [L]
- **PostgreSQL.** Cita literal: "Postgres is still considered an official project name, both because of tradition and because people find it easier to pronounce Postgres than PostgreSQL." Fuente: https://www.postgresql.org/docs/current/history.html [L]. No trata la pronunciación de SQL.
- **GIF.**
  - Wilhite, su creador, defendió la g suave ("jif") en los Webby Awards de 2013. Su discurso generó más de 17.000 tuits. Fuente: https://en.wikipedia.org/wiki/GIF [L]
  - Oxford Dictionaries registra ambas pronunciaciones y pone primero la g dura. El *New Oxford American Dictionary* dio solo la g suave en su 2.ª edición (2005) y añadió la dura en la 3.ª (2012). Fuente: https://en.wikipedia.org/wiki/GIF [L]
  - Merriam-Webster también registra ambas, con la dura primero. Fuente: https://en.wikipedia.org/wiki/GIF [L] (secundaria; no pude abrir la entrada de M-W).
  - Conclusión práctica: ambas son aceptables; hay que saber que existen las dos.
- **Linux.**
  - El kernel.org conserva grabaciones de Torvalds en inglés y sueco: `english.au`, `english.ogg`, `english.wav`, `swedish.*`. Fuente: https://www.kernel.org/pub/linux/kernel/SillySounds/ [M]
  - No pude reproducir el audio, así que no puedo transcribir lo que dice. Una cita atribuida ("Linux is always Lih-nix") viene de un blog secundario (https://danielmiessler.com/p/how-pronounce-linux) y queda sin verificar. Otras fuentes discuten si la grabación es una norma (https://apenwarr.ca/log/20170925) [S].
- **kubectl.**
  - La documentación oficial de Kubernetes no fija pronunciación en la página que revisé. Los 100.000 primeros caracteres no la mencionan; faltan los últimos 22.197. Fuente: https://kubernetes.io/docs/reference/kubectl/ [L parcial]
  - Las variantes documentadas por terceros son kube-control, kube-cuttle, kube-cuddle y cube-see-tee-ell. Fuente: https://microsoft.github.io/k8s-on-azure-workshop/module-1/architecture/kube-ctl/index.html [S]
  - Una cita atribuida a un changelog de Kubernetes 1.9 afirma que "cube control" es lo canónico. No pude verificarlo. Fuente: https://community.kodekloud.com/t/when-pronouncing-kube-as-a-prefix-e-g-kubectl-is-it-more-correct-to-rhyme-w/21657 [S]
  - La charla de Waldo Grunenwald (All Things Open 2018) enumera "over a dozen ways" de decirlo. Fuente: https://opensource.com/article/18/12/kubectl-definitive-pronunciation-guide [L]
  - Una charla de devopsdays dice que la comunidad abraza la ambigüedad. Fuente: https://devopsdays.org/events/2022-tampa/program/waldo-g-t1/ [S]
- **Discrepancia SQL.** MySQL dice oficialmente "Ess Que Ell" pero tolera "sequel". Las dos pronunciaciones conviven y la preferida depende del producto: Microsoft SQL Server y la historia del lenguaje favorecen "sequel", pero no lo verifiqué con fuente primaria. Se declaran las dos.

### No verificado (sin fuente primaria leída)
cache (kash vs. cash-ay), GUI, char, sudo, Azure, async, regex (g suave o dura) y Kubernetes. Para estos no tengo fuente. No los afirmo.

### Falsos amigos técnicos
No encontré fuentes en esta ronda: librería/library, eventual/eventually, actual, deprecar y similares. Quedan como hueco.

### Recursos canónicos
- **Pronunciación:** los textos oficiales de cada proyecto, cuando existen. Lo que hay es nginx.org, la especificación de YAML (abstract) y el manual de MySQL.
- **Qué parte:** la frase literal del proyecto. Mostrarla en la nota como evidencia.
- **En qué fijarse:** que los proyectos se dividen entre los que fijan una pronunciación (nginx, YAML), los que la toleran en varias (MySQL) y los que no la fijan (Kubernetes, kubectl). Para estos últimos, mejor enseñar "las que se usan" que "la correcta".

### Frases modelo
Ninguna fuente leída trae frases. Sugerencias propias, no respaldadas: "Should I say S-Q-L or sequel?" para preguntar a un equipo nuevo cómo lo dicen. Marcar la nota como sin fuente.

---

## 3. Componente `entrevista-tecnica`

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Amazon, Leadership Principles | https://atoz.amazon/en-us/discover/leadership-principles | primaria | 3 | 2 | 1 | 3 | [L] |
| Meta Careers, "Preparing for your software engineering interview at Meta" | https://www.metacareers.com/blog/preparing-for-your-software-engineering-interview-at-meta/ | primaria | 3 | 2 | 2 | 3 | [L] |
| Google re:Work, "Use structured interviewing" | https://rework.withgoogle.com/en/guides/hiring-use-structured-interviewing | primaria | 3 | 2 | 1 | 2 | [S] |
| Google, careers.google.com/how-we-hire | https://careers.google.com/how-we-hire/ | primaria | 3 | 2 | 1 | 3 | [M] (la URL que abrí era solo navegación; no vi el contenido de "how we hire") |
| Tech Interview Handbook, behavioral | https://www.techinterviewhandbook.org/behavioral-interview/ | secundaria (practicante reconocido) | 2 | 2 | 2 | 2 | [L] |
| Tech Interview Handbook, behavioral questions | https://www.techinterviewhandbook.org/behavioral-interview-questions/ | secundaria | 2 | 2 | 3 | 2 | [L] |
| Tech Interview Handbook, coding interview | https://www.techinterviewhandbook.org/coding-interview-prep/ | secundaria | 2 | 2 | 2 | 2 | [L] |
| Tech Interview Handbook, system design | https://www.techinterviewhandbook.org/system-design/ | secundaria | 2 | 1 | 1 | 1 | [L] |
| Stripe, guía de team screen (alojada por GreatFrontEnd) | https://www.greatfrontend.com/static/guides/stripe-eng-team-screen-guide.pdf | primaria (no confirmé que sea de Stripe) | 2 | 2 | 2 | 3 | [S] (429 al leerla) |
| Alex Xu, *System Design Interview* (4 pasos) | https://bytebytego.com/courses/system-design-interview/a-framework-for-system-design-interviews | primaria (curso del autor) | 3 | 3 | 2 | 3 | [S] (resumen de terceros) |

### Afirmaciones con URL

- **Amazon.**
  - Son 16 Leadership Principles: Customer Obsession, Ownership, Invent and Simplify, Are Right, A Lot, Learn and Be Curious, Hire and Develop the Best, Insist on the Highest Standards, Think Big, Bias for Action, Frugality, Earn Trust, Dive Deep, Have Backbone; Disagree and Commit, Deliver Results, Strive to be Earth's Best Employer, Success and Scale Bring Broad Responsibility. Fuente: https://atoz.amazon/en-us/discover/leadership-principles [L]
  - La frase introductoria empieza: "We use our Leadership Principles every day, whether we're discussing ideas for new projects". Está truncada por la herramienta. Fuente: misma URL [L]
  - La URL antigua `amazon.jobs/en/principles` redirige (301) a esta. Vale la pena registrarlo para el enlace.
  - Las listas anteriores de 14 principios aparecen en fuentes viejas; hoy son 16.
- **Meta, pensar en voz alta.** Cita literal: "We pay a lot of attention to the way you solve problems." Y: "Thinking out loud gives the interviewer insight into your thinking process." Fuente: https://www.metacareers.com/blog/preparing-for-your-software-engineering-interview-at-meta/ [L]
- **Meta, aclaraciones.**
  - "Be sure to ask clarifying questions."
  - "Usually, the interviewer knows the question well enough to provide information that may help you move forward."
  - Fuente: misma URL [L]
- **Meta, behavioral.**
  - "Use the S.T.A.R. (Situation, Task, Actions, Results) method".
  - "Be honest". Hablar de los fracasos no se castiga; lo que se valora es lo que aprendiste.
  - Dar ejemplos concretos y no teóricos.
  - Fuente: misma URL [L]
- **Meta, formato.** Fuentes de terceros dan formatos distintos (35 minutos con 5 preguntas, según el blog de Meta resumido; 35 minutos con 2 problemas, según igotanoffer). Hay que verificar con el recruiter. Fuente: https://igotanoffer.com/en/advice/meta-coding-interviews [S]
- **Tech Interview Handbook, behavioral.**
  - STAR: Situation, Task, Action, Result. Recomienda un quinto paso, "Reflection", para perfiles senior.
  - Aconseja preparar de 3 a 5 historias de alto impacto en vez de memorizar respuestas, y centrarse en las acciones propias.
  - Dice que las empresas evalúan si el candidato "has a history of demonstrating the right behaviors" para la compañía.
  - Fuente: https://www.techinterviewhandbook.org/behavioral-interview/ [L]
  - La página no cubre las preguntas finales al entrevistador; enlaza a otra página ("Preparing final questions to ask") que no leí.
- **Tech Interview Handbook, preguntas de ejemplo.**
  - "Tell me about a time when you had a conflict with a co-worker."
  - "What was the most difficult bug that you fixed in the past 6 months?"
  - "Tell me about a time you met a tight deadline."
  - "How have you handled criticism of your work?"
  - "What would you hope to achieve in the first six months after being hired?"
  - Amazon: "How do you deal with a failed deadline?" Stripe: "How do you stay up to date with the latest technologies?"
  - Fuente: https://www.techinterviewhandbook.org/behavioral-interview-questions/ [L]
- **Tech Interview Handbook, qué se evalúa en comunicación.** La comunicación es el primero de cuatro criterios, descrita como "Asking clarifying questions" y "communication of approach and tradeoffs clearly". Los otros: resolución de problemas, competencia técnica ("with no significant struggle") y testing contra casos normales y de borde. La página no usa la frase "thinking out loud". Fuente: https://www.techinterviewhandbook.org/coding-interview-prep/ [L]
- **Tech Interview Handbook, system design.**
  - Evalúa la habilidad de diseñar sistemas reales con varios componentes (paráfrasis de la herramienta).
  - Lo suelen recibir perfiles más senior.
  - Recomienda *System Design Interview – An insider's guide* (Alex Xu) como introducción amigable.
  - Fuente: https://www.techinterviewhandbook.org/system-design/ [L]
- **Alex Xu, 4 pasos.**
  - (1) entender el problema y fijar el alcance, (2) proponer un diseño de alto nivel y lograr acuerdo, (3) deep dive, (4) cierre.
  - Los tiempos varían según el resumen: 3–10, 10–15, 10–25 y 3–5 minutos en uno; 5, 20, 15 y 5 en otro.
  - No leí el texto del libro; todo viene de resúmenes de terceros.
  - Fuente: https://bytebytego.com/courses/system-design-interview/a-framework-for-system-design-interviews [S]
- **Google.** Los cuatro atributos que se reportan son habilidad cognitiva general, liderazgo emergente, conocimiento del rol y "Googleyness". Los tres últimos fueron paráfrasis de Laszlo Bock en medios (LinkedIn Talent Connect, OpenView). El rol knowledge se describe como el menos importante. Fuente: https://talent.linkedin.com/blog/index.php/2014/10/googles-hiring-secrets-revealed [S]. No leí la página oficial "how we hire"; la fuente es de 2014 y puede estar desactualizada. Los atributos y la estructura (entrevista estructurada con rúbrica) son más predictivos y justos según re:Work. Fuente: https://rework.withgoogle.com/en/guides/hiring-use-structured-interviewing [S]
- **Stripe.** Según un resumen del buscador de la guía de team screen, se juzga qué tan legible resuelves el problema y cómo manejas el feedback; recomienda explicar el razonamiento en voz alta y no usar un lenguaje que no domines; dice que no usa trivia estilo LeetCode. Fuente: https://www.greatfrontend.com/static/guides/stripe-eng-team-screen-guide.pdf [S]. No pude abrirla.

### Discrepancias
- Formato de la entrevista de Meta: según fuente, 35 minutos con 5 preguntas o con 2 problemas. Se declaran las dos, sin resolver.
- Google: los atributos de 2014 pueden no ser los de hoy; The Information (paywall) dice que "Googleyness" se aclaró para reducir sesgo. Fuente: https://www.theinformation.com/articles/google-discourages-culture-fit-in-hiring-with-googleyness-update?pu=hackernewsfsar1p [S]

### Recurso canónico del componente
- **Meta Careers, "Preparing for your software engineering interview at Meta"** (https://www.metacareers.com/blog/preparing-for-your-software-engineering-interview-at-meta/).
  - Qué parte: las secciones de pensar en voz alta, aclaraciones y STAR.
  - En qué fijarse: que es una guía oficial de una empresa, corta, con frases literales y reutilizables; y que dice que se evalúa el proceso, no solo la respuesta.
- **Complementos:** Tech Interview Handbook (behavioral y coding) por las preguntas de ejemplo y los cuatro criterios; los principios de Amazon como lista oficial para armar historias STAR.

### Frases modelo respaldadas por una fuente
Todas son citas literales de la guía de Meta o del Tech Interview Handbook. Las usaría tal cual en la nota.
- "Be sure to ask clarifying questions." (Meta)
- "Thinking out loud gives the interviewer insight into your thinking process." (Meta)
- "Tell me about a time when you had a conflict with a co-worker." (pregunta que el candidato debe saber contestar)
- Frases que el candidato diría y que las fuentes sugieren sin darlas literalmente: "communication of approach and tradeoffs clearly" describe el criterio, no la frase. No hay fuente primaria con frases listas para pedir aclaraciones. Quedan como hueco.

---

## Huecos

1. **Needs analysis específico de ingenieros de software hispanohablantes en LatAm.** No lo encontré. Lo que hay son estudios de estudiantes de Indonesia, Kazajistán y universidades; muestras chicas, abstracts sin texto completo.
2. **Texto completo de los papers ESP y BELF.** El de 2005 (*ESP* 24(4)), el de 2010 (*ESP*), el de Kankaanranta y Planken (*Journal of Business Communication*) y el de Ibérica dieron 403, Anubis o solo bibliografía. Hay que abrirlos desde acceso institucional antes de citar nada textual.
3. **Definiciones de Swales** (género, propósito comunicativo, comunidad discursiva) y características absolutas de Dudley-Evans y St John: sin cita literal. Falta el libro o una reseña que las cite.
4. **Hutchinson & Waters (1987)** y la distinción EOP/EAP: no lo busqué en esta ronda; PMC bloqueó la lectura.
5. **Diccionarios.** Merriam-Webster (403) y Cambridge: no leí ninguna entrada. Faltan cache, SQL, GUI, GIF, char, sudo, async, regex, Azure.
6. **Pronunciación sin fuente primaria:** Kubernetes (el nombre), kubectl (la docs oficial no lo fija en lo que leí), Linux (audio de kernel.org no transcrito), cache, GUI, char, sudo, Azure, async y regex.
7. **Falsos amigos técnicos** (librería/library, eventual/eventually, actual, deprecar y otros): ninguna fuente. Los habituales son diccionarios bilingües o la Fundéu; no los busqué.
8. **Préstamos del software en castellano** (Fundéu, RAE): no busqué.
9. **Guías oficiales.**
   - Google "how we hire": solo leí fuentes secundarias.
   - Stripe: la guía se alojó en GreatFrontEnd y dio 429; la URL de Stripe devolvió 404.
   - Meta: la URL del primer intento dio 404; la del blog funcionó.
   - Libros (Cracking the Coding Interview, System Design Interview de Alex Xu): solo resúmenes de terceros.
10. **Preguntas finales al entrevistador** ("Preparing final questions to ask" del Tech Interview Handbook): no leída.
11. **Frases modelo para pedir aclaraciones y para pensar en voz alta:** no encontré una fuente primaria con frases listas. Lo único respaldado son las citas literales de Meta.
12. **Comunicación escrita y de reuniones** (Slack, PRs, daily, emails): solo encontré estudios sobre barreras, no sobre géneros. Es el hueco que más pesa para la vertical, según el aviso del principio.
13. **Rondas de búsqueda:** usé como máximo tres por componente; lo que no apareció está arriba como hueco.
