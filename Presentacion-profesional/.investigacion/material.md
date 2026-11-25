# Investigación: Material (lo que hay detrás de las vidrieras)

Ángulo: inventario profesional, logros (cuándo cuantificar), habilidades y palabras clave, huecos y cambios de carrera.
Fecha: 2026-11-24. Marcas: [L] texto completo leído, [M] metadatos/abstract, [S] resumen secundario o del buscador. Puntajes 1-3: Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).
Aviso de método: WebFetch resume la página con un modelo chico; lo que va entre comillas es lo que ese resumen devolvió como cita. Los PDF/DOCX binarios y las páginas con 403 no se pudieron leer.

## Sobre la división del árbol

- La división (inventario / logros / habilidades / huecos-y-cambios) coincide razonablemente con cómo lo parten los career services (master resume, bullets, skills, gaps), pero el campo **no** separa "inventario" de "logros": las guías hablan de "bullets" y de "master resume" en la misma página. Conviene que `inventario-profesional.md` sea el registro (cuándo y cómo se anota) y `logros.md` la redacción y el criterio de cuantificar.
- "Habilidades y palabras clave" junta dos cosas que la evidencia trata distinto: palabras clave (práctica de ATS, casi toda de vendedores) y skills-based hiring (política de empleadores, con estudios serios). Conviene dejar claro en la nota que son dos temas.
- "Huecos" y "cambio de carrera" tienen evidencia de calidad muy distinta: huecos tiene experimentos de campo; cambio de carrera no tiene ninguno encontrado (ver huecos de la investigación). La nota `sesgos-en-la-seleccion.md` (otro ángulo) también toca huecos: coordinar para no duplicar.

---

## 1. Inventario profesional

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1.1 | Julia Evans, "Get your work recognized: write a brag document" (practicante) | https://jvns.ca/blog/brag-documents/ | primaria (practicante) | 2/3/3/3 | [L] vía WebFetch |
| 1.2 | MIT CAPD, página de resumes (career services) | https://capd.mit.edu/resources/resumes/ | primaria (guía institucional) | 3/2/2/2 | [L] vía WebFetch |
| 1.3 | Harvard FAS Career Services, "Create a strong resume" | https://careerservices.fas.harvard.edu/resources/create-a-strong-resume | primaria (guía) | 3/2/2/1 | [S] solo buscador |
| 1.4 | Northeastern, Resume Guide 2018 (describe un master document) | https://careers.northeastern.edu/wp-content/uploads/2018/11/Resume-Guide-6.15.2018.pdf | primaria (guía) | 2/1/1/1 | [S] solo buscador |

### Afirmaciones

- Qué es un brag document y para qué: el post de Julia Evans dice «Instead of trying to remember everything you did with your brain, maintain a "brag document" that lists everything». Sirve para evaluaciones de desempeño, para darle contexto a un manager nuevo y para reflexionar. https://jvns.ca/blog/brag-documents/ [L]
- Secciones de su plantilla: metas del año y del próximo; proyectos (contribución propia e impacto, «with numbers where possible»); colaboración y mentoría; diseño y documentación; construir empresa; qué aprendiste; fuera del trabajo (posts, charlas, open source); y prompts para cuando te trabás. https://jvns.ca/blog/brag-documents/ [L]
- Cuándo se actualiza: ella prefiere una sesión larga cada seis meses o año; otros lo actualizan «every 2 weeks». Recomienda probar ambos. Los resultados se anotan después, tras el lanzamiento. https://jvns.ca/blog/brag-documents/ [L]
- Trabajo «difuso» (mejorar calidad de código): anotar la meta, las acciones y los efectos observados. Y la regla de honestidad: «make it sound exactly as good as it is». https://jvns.ca/blog/brag-documents/ [L]
- Master resume en career services: MIT CAPD sugiere guardar un documento más amplio y armar un resume dirigido a cada puesto: «when applying for a job you want to build a resume that targets a specific position or employer». https://capd.mit.edu/resources/resumes/ [L, parafraseado por el resumidor; la frase literal "master resume" viene del buscador]
- Northeastern describe un «comprehensive master document» guardado, con cada bullet empezando con verbo de acción. https://careers.northeastern.edu/wp-content/uploads/2018/11/Resume-Guide-6.15.2018.pdf [S]
- Harvard: no se encontró en las páginas vistas un "master resume" explícito; sí verbos de acción y «quantify and qualify». https://careerservices.fas.harvard.edu/resources/create-a-strong-resume [S]

### Recurso canónico

**Julia Evans, "Get your work recognized: write a brag document"** (https://jvns.ca/blog/brag-documents/): leer las secciones de la plantilla y la regla de anotar el resultado *después* del lanzamiento; es un registro pensado para evaluaciones internas, no para CV, así que hay que decir que el paso a CV es el recorte (MIT CAPD, https://capd.mit.edu/resources/resumes/). Es práctica de un practicante, no evidencia: no hay estudio encontrado de que mantener un inventario mejore resultados de búsqueda.

---

## 2. Logros (logro vs. tarea, XYZ, STAR/CAR, cuándo cuantificar)

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 2.1 | Laszlo Bock, "My Personal Formula for a Winning Resume", LinkedIn Pulse, 29-09-2014 | https://www.linkedin.com/pulse/20140929041000-5421-my-personal-formula-for-a-winning-resume/ (403, no leído; copia DOCX en https://www.calstatela.edu/sites/default/files/formula_for_a_winning_resume.docx, binario sin extraer) | primaria (practicante) | 3/2/2/3 | [S] |
| 2.2 | Yale OCS, "Writing Impactful Resume Bullets" | https://ocs.yale.edu/resources/writing-impactful-resume-bullets/ | primaria (guía) | 3/2/2/1 | [L] vía WebFetch |
| 2.3 | MIT CAPD resumes + MIT CommKit (PAR) | https://capd.mit.edu/resources/resumes/ ; https://mitcommlab.mit.edu/meche/commkit/cv-resume/ | primaria (guía) | 3/2/2/1 | [L] CAPD / [S] CommKit |
| 2.4 | Janiszewski y Uy 2008, Psychological Science 19(2), 121-127 | https://pubmed.ncbi.nlm.nih.gov/18271859/ (no cargó, cookies) | primaria (estudio) | 3/3/1/2 | [S] |
| 2.5 | APS (Wray Herbert), sobre estudios de Oppenheimer (UCLA), ago. 2013 | https://www.psychologicalscience.org/news/were-only-human/precisely-right-no-doubt-trust-me.html | secundaria | 2/1/2/2 | [L] |
| 2.6 | Lerner y Bergman (interviewing.io + Learning Collider), recruiters técnicos | https://interviewing.io/blog/are-recruiters-better-than-a-coin-flip-at-judging-resumes | primaria (blog de estudio, sin revisión de pares) | 2/3/2/3 | [L] |
| 2.7 | dev.to, 12 hiring managers rankean 30 bullets a ciegas | https://dev.to/charliemorrison/i-asked-12-hiring-managers-to-rank-30-resume-bullets-blind-5-patterns-that-won-4-that-lost-1gkl | secundaria, anecdótica | 1/1/2/2 | [S] |
| 2.8 | Hilos de Blind sobre métricas | https://www.teamblind.com/post/does-it-really-make-sense-to-fit-your-resume-into-metrics-achieved-bzyaheco | foro | 1/1/1/1 | [S] |
| 2.9 | Kickresume, 57 CVs de contratados (vendedor) | https://www.kickresume.com/en/press/resumes-that-got-people-hired-top-companies/ | vendedor | 1/1/1/1 | [S] |

### Afirmaciones

- Fórmula de Bock. Publicada el 29-09-2014 en LinkedIn por Laszlo Bock, entonces SVP de People Operations de Google; la estructura es «Accomplished [X] as measured by [Y], by doing [Z]»: verbo activo, resultado medido numéricamente, línea de base para comparar, y qué hiciste. «XYZ» es un apodo posterior. https://www.linkedin.com/pulse/20140929041000-5421-my-personal-formula-for-a-winning-resume/ [S: no se pudo leer el original; datos del buscador]. Lo confirma una guía de Yale que reproduce la misma estructura y pide «a baseline for comparison»: https://ocs.yale.edu/resources/writing-impactful-resume-bullets/ [L]
- Atribución dudosa: un post de dev.to se la atribuye a Gayle McDowell por *Cracking the Coding Interview*; no se confirmó, tratarlo como erróneo. https://dev.to/caroso1222/resume-pro-tip-the-absolute-best-way-to-show-your-work-experience-2o97 [S]
- Importante: la fórmula original dice «numerically measuring the result», o sea que **pide número**. No admite el caso sin número; ese es un límite de la fórmula, no un matiz de los blogs.
- Yale ofrece dos formatos: «Action + Project + Result» («quantifying when possible») y la de Bock. Para el caso sin números no da fallback propio; pregunta «What is the tangible evidence of your accomplishments?». https://ocs.yale.edu/resources/writing-impactful-resume-bullets/ [L]
- MIT CAPD: «Quantify if you can»; ejemplo de convertir una tarea en logro: «was responsible for delivering projects on time» pasa a «ensured projects were delivered on or ahead of schedule»; sugiere tamaños de audiencia y montos. https://capd.mit.edu/resources/resumes/ [L]
- Marco CAR/PAR: MIT usa Project-Action-Result, no STAR ni CAR; CAR (Challenge-Action-Result) aparece en Queen's University y AARP, con «quantify the result wherever possible». https://mitcommlab.mit.edu/meche/commkit/cv-resume/ ; https://www.aarp.org/work/job-search/how-to-refresh-your-resume/ [S]
- Precisión numérica y persuasión (lo más cercano a evidencia directa):
  - Janiszewski y Uy (2008): el ajuste lejos de un ancla numérica es menor si el ancla es precisa que si es redondeada. Es un estudio de **anclaje en estimaciones**, no de credibilidad de logros. https://pubmed.ncbi.nlm.nih.gov/18271859/ [S]. Una réplica de Chandler (2023) apoyó el efecto de precisión pero no la interacción reportada. https://forrt.org/flora-replication-atlas/doi/10.1111/j.1467-9280.2008.02057.x/ [S]
  - Oppenheimer y colegas (UCLA), según APS: expertos en geografía con respuestas más precisas (20.85 millas vs. 21) fueron juzgados «more confident if their answers had more digits»; y en un juego tipo *The Price Is Right* los voluntarios «clearly preferred the more precise advisors» (63 USD vs. 60). El artículo advierte sobre «false precision to create an air of confidence». Sin tamaños de muestra en la fuente. https://www.psychologicalscience.org/news/were-only-human/precisely-right-no-doubt-trust-me.html [L]
  - Hay un trabajo de Psychological Science que, según el buscador, muestra que demasiada precisión puede ser leída por expertos como falta de competencia; no pude ubicar el paper (no confirmado). https://www.psychologicalscience.org/journals/psychological-science/0956797616666074/ [S]
  - **No encontré estudios directos** de logros cuantificados vs. no cuantificados en CVs. Lo anterior es lo más cercano, y no equivale: mide percepción de confianza ante números, no credibilidad de un bullet.
- Evidencia indirecta sobre cómo se lee el CV (relevante porque limita cuánto puede pesar un número): en el estudio de Lerner y Bergman, 76 recruiters técnicos evaluaron 30 CVs cada uno (casi 2.200 evaluaciones, más de 1.000 CVs); dos recruiters coinciden en entrevistar o no el 64% de las veces; la decisión coincidió con el resultado de la primera entrevista «55%», «just slightly better than a coin flip»; mediana de 31 segundos por CV; más probabilidad de entrevistar con experiencia en empresas top (35%). El post no testea cuantificación. https://interviewing.io/blog/are-recruiters-better-than-a-coin-flip-at-judging-resumes [L]
- Prácticos: en el ranking a ciegas de 12 hiring managers (muestra chica, no revisada), tres de los ocho bullets ganadores no tenían números; el autor concluye que penalizan bullets donde no se ve qué hizo personalmente el candidato. https://dev.to/charliemorrison/i-asked-12-hiring-managers-to-rank-30-resume-bullets-blind-5-patterns-that-won-4-that-lost-1gkl [S]
- Críticas a métricas inventadas o infladas: no encontré una fuente de reclutadores técnicos reconocidos que lo diga; solo comentarios en foros (Blind): dejar el bullet sin número antes que meter uno falso, «unless you can talk in depth» sobre él; otros preguntan «how do you measure that» ante un «65% proficiency». https://www.teamblind.com/post/does-it-really-make-sense-to-fit-your-resume-into-metrics-achieved-bzyaheco [S, foro]. La única defensa citable es la regla de Evans: «make it sound exactly as good as it is». https://jvns.ca/blog/brag-documents/ [L]
- Correlación de vendedor (no usar como evidencia): Kickresume, 57 CVs de contratados, mediana de 5 métricas vs. 4 [S]. https://www.kickresume.com/en/press/resumes-that-got-people-hired-top-companies/
- Qué hacer sin números (alcance, escala, antes/después cualitativo): lo respaldan guías (MIT: tamaño de audiencia, proceso mejorado, descubrimiento; Evans: «goal, actions taken, and any observed effects» para trabajo difuso; Yale: «tangible evidence»). No hay estudio que compare esas alternativas. https://capd.mit.edu/resources/resumes/ ; https://jvns.ca/blog/brag-documents/ ; https://ocs.yale.edu/resources/writing-impactful-resume-bullets/

### Posición sugerida para la nota (para decidir en la sesión de escritura)

La evidencia sostiene: (a) los números son una señal que se lee como precisión y confianza (Oppenheimer, vía APS), pero ese estudio también avisa del riesgo de «false precision»; (b) todas las guías institucionales dicen «quantify if you can / when possible», no «siempre»; (c) la fórmula de Bock sí pide número, es práctica de un ejecutivo, no evidencia. La respuesta a «¿le pongo números?» queda como criterio razonado con fuentes parciales, no como hallazgo empírico, y la nota debería decirlo.

### Recurso canónico

**Yale OCS, "Writing Impactful Resume Bullets"** (https://ocs.yale.edu/resources/writing-impactful-resume-bullets/): leer los dos formatos (A+P+R y X-Y-Z) y la pregunta de la «tangible evidence»; fijarse en que ambos dicen «cuando sea posible». Complemento: **la fórmula de Bock original** (LinkedIn, 2014), con la salvedad de que no pude leerla.

---

## 3. Habilidades y palabras clave

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 3.1 | Fuller, Sigelman y Martin (HBS Managing the Future of Work + Burning Glass Institute), "Skills-Based Hiring: The Long Road from Pronouncements to Practice", feb. 2024 | https://www.burningglassinstitute.org/s/Skills-Based-Hiring-02122024-vF-srmp.pdf | primaria (informe) | 3/3/2/3 | [M]: el PDF no devolvió las cifras |
| 3.2 | Joseph Fuller, post del HKS Project on Workforce, 14-02-2024 | https://pw.hks.harvard.edu/post/skills-based-hiring-the-long-road-from-pronouncements-to-practice | secundaria (del mismo autor) | 3/1/1/1 | [L] |
| 3.3 | LinkedIn Economic Graph, "Skills-Based Hiring: Increasing Access to Opportunity", mar. 2025 | https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/PDF/skills-based-hiring-march-2025.pdf | primaria (vendedor, datos propios) | 2/2/1/2 | [S]: el PDF redirige y no se leyó |
| 3.4 | Jobscan, "Resume keyword stuffing" (vendedor) | https://www.jobscan.co/blog/resume-keyword-stuffing/ | vendedor | 1/1/1/1 | [S] |
| 3.5 | CNBC, un recruiter que limita skills a nueve | https://www.cnbc.com/2022/10/12/ive-helped-people-land-jobs-at-google-facebook-heres-the-resume-mistake-ive-been-seeing-lately.html | secundaria (practicante) | 1/1/1/1 | [S] |
| 3.6 | NN/g, "Resumes UX career changers" (E. Sunwall) | https://www.nngroup.com/articles/resumes-ux-career-changers/ | secundaria (consejos; cita estudios) | 2/1/2/1 | [L] |

### Afirmaciones

- Skills-based hiring, la brecha entre anuncio y práctica: «not even 1 in 700 hires last year» (Fuller); 37% de las firmas estudiadas sacó requisitos de título y esas explicaron casi todo el cambio real; cerca de 45% cambió «in name only». https://pw.hks.harvard.edu/post/skills-based-hiring-the-long-road-from-pronouncements-to-practice [L]. Cifras extra (3,6% de los roles que sacaron el requisito; 18% que revirtió; +0,14 pp) vienen de coberturas de prensa y **no las pude verificar en el informe**: https://www.hrdive.com/news/employers-failing-at-skills-based-hiring/707897/ [S]. Los que cumplen: los trabajadores sin título tienen retención «10 percentage points higher» (Fuller, [L]).
- Lectura para el tema: que un anuncio diga «skills-based» no garantiza que el proceso lo sea; para quien busca, vale mostrar habilidades en logros porque no se puede asumir lectura por habilidades.
- LinkedIn (vendedor, datos propios): la nota de marzo 2025 compara candidatos hallados por búsquedas por skills contra por título; el factor de expansión no se pudo leer. https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/PDF/skills-based-hiring-march-2025.pdf [S]. Prensa citó «19x» para el informe 2023 de EE.UU.; la propia nota 2025 desaconseja compararlos. https://www.techrepublic.com/de/article/skills-first-hiring-linkedin/ [S]
- ATS: no encontré documentación oficial de Greenhouse, Lever o Workday leída; la síntesis del buscador dice que el rechazo automático depende de la configuración del empleador (en Workday, preguntas excluyentes) y que la búsqueda de recruiters por palabra clave en Workday es léxica, no semántica. Las fuentes discrepan sobre Workday. Son blogs, no docs. https://aiapply.co/blog/greenhouse-vs-lever-vs-workday [S]. Ya relevado por otro ángulo: Hidden Workers (HBS+Accenture).
- Keyword stuffing: Jobscan lo critica (texto blanco oculto «recruiters find it easily») y Monster aconseja no copiar todo el aviso; ambos son vendedores/medios, sin test independiente. https://www.jobscan.co/blog/resume-keyword-stuffing/ [S]
- Skills listadas vs. mostradas en logros: lo dicen InterviewPal y MyCVCreator («prove each keyword with a concrete achievement»), ambos vendedores; CNBC cita a un recruiter que limita la lista a nueve. NN/g aconseja directamente saltear listas y barras de nivel. https://www.nngroup.com/articles/resumes-ux-career-changers/ [L]. El dato de que un ATS pondera más una skill mencionada en la sección de skills y en la experiencia es de un vendedor y no está verificado. **No hay estudio encontrado** que compare CVs con skills listadas vs. demostradas.

### Recurso canónico

**Burning Glass Institute + HBS, "Skills-Based Hiring: The Long Road..."** (2024): la sección de tipos de empleador (líderes, solo anuncio, retroceso), para entender qué esperar de un aviso que dice «skills-based». Para keywords no hay recurso de autoridad: proponer la documentación oficial de ATS (Greenhouse help center) como pendiente a leer.

---

## 4. Huecos y cambios de carrera

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 4.1 | Kroft, Lange y Notowidigdo, QJE 128(3), 2013 (NBER w18387) | https://www.nber.org/papers/w18387 | primaria (experimento de campo) | 3/3/1/3 | [M] abstract y digest |
| 4.2 | Kristal, Nicks, Gloor y Hauser, Nature Human Behaviour, 2023 | https://www.nature.com/articles/s41562-022-01485-6 (bloqueado); resumen en https://gap.hks.harvard.edu/reducing-discrimination-against-job-seekers-and-without-employment-gaps | primaria (3 estudios) | 3/3/2/3 | [S] página institucional |
| 4.3 | Behavioural Insights Team, ensayo del Reino Unido (mismo estudio, versión BIT) | https://www.bi.team/?p=15197 | primaria (misma investigación que 4.2) | 2/2/1/1 | [L] |
| 4.4 | LinkedIn News, "Career Breaks", mar. 2022 | https://news.linkedin.com/2022/march/new-way-to-represent-career-breaks-on-linkedin | vendedor | 2/1/1/2 | [L] |
| 4.5 | ResumeGo, empleo huecos (vendedor) | https://www.resumego.net/research/resume-employment-gaps | vendedor | 1/2/1/1 | [S] |
| 4.6 | SHRM, candidatos no tradicionales | https://shrm.org/topics-tools/news/talent-acquisition/lesson-recruiters-take-chance-nontraditional-candidates | secundaria | 2/1/1/1 | [S] |

4.2 y 4.3 son el mismo experimento: cuentan como una sola fuente.

### Afirmaciones

- Kroft et al.: experimento de campo con CVs ficticios enviados a avisos reales en las 100 mayores áreas metropolitanas de EE.UU.; unos 3.000 avisos (ventas, atención al cliente, apoyo administrativo, oficina) y unos 12.000 CVs; los callbacks caen con la duración del desempleo, sobre todo en los primeros ocho meses, y la caída es mayor cuando el mercado laboral está más fuerte; los autores atribuyen el patrón al screening del empleador. Limitaciones: solo callbacks, y puede ser específico de adultos jóvenes. https://www.nber.org/papers/w18387 ; https://www.nber.org/digest/mar13/duration-dependence-and-labor-market-conditions [M]. Ojo: el hueco que estudian es **desempleo reciente en el CV**, no un hueco largo explicado.
- Explicar el hueco, ensayo del Reino Unido (Kristal et al. 2023, publicación de Nature Human Behaviour): 9.022 vacantes entre octubre de 2019 y marzo de 2020; cuatro CVs: hueco de 2,5 años sin explicar, empleada actualmente, hueco explicado como cuidado de hijos, y sin fechas con años de experiencia por puesto. Explicar el hueco por cuidado de hijos **no cambió** los callbacks; el formato de años subió los callbacks «about 15%» frente a CVs tradicionales con hueco (con o sin explicación) y «about 8%» frente al CV sin hueco. Los profesionales de RR.HH. dicen preferir la explicación, pero eso no apareció en la conducta. Las fuentes dan 15% (HKS) y 14,6% (NN/g, citando la nota de BIT). https://gap.hks.harvard.edu/reducing-discrimination-against-job-seekers-and-without-employment-gaps ; https://www.bi.team/?p=15197 ; https://www.nngroup.com/articles/resumes-ux-career-changers/ [S/L]. Limitaciones: una sola persona ficticia (madre) y una sola razón; no generaliza a otros motivos.
- Estudios de laboratorio del mismo paper: n total 2.532; el formato de años subió la empleabilidad percibida con 5, 10 y 15 años de experiencia, más con menos años. https://gap.hks.harvard.edu/reducing-discrimination-against-job-seekers-and-without-employment-gaps [S]
- **Discrepancia**: ResumeGo (vendedor, 2019, 36.510 avisos según el buscador) reporta 6,8% de callback con razón vs. 4,3% sin razón (+58,1%). Contradice al ensayo de BIT/Nature. Dar las dos; pesar la de BIT/Nature por diseño preregistrado y fuente. https://www.resumego.net/research/resume-employment-gaps [S]
- Un buscador sugirió que para roles de menor calificación el CV con hueco explicado rindió peor; no lo pude confirmar en la página de BIT; omitir hasta verificar.
- LinkedIn (vendedor), marzo de 2022: función «Career Breaks» con 13 opciones (cuidados, salud y bienestar, etc.); «64% of women» tomaron una pausa; «51% of hirers are more likely to contact a candidate who gives context about a career break». https://news.linkedin.com/2022/march/new-way-to-represent-career-breaks-on-linkedin [L]. Cifras de prensa de la misma encuesta (62% de empleados, 20% de hiring managers que rechazarían) **no están en la fuente oficial leída**. https://www.searchenginejournal.com/linkedin-profiles-can-now-display-career-breaks/441113/ [S]. Notar la discrepancia: el 51% de LinkedIn (declarado) y el ensayo (conducta real) no coinciden.
- Cambio de carrera: **no encontré estudios controlados**. La búsqueda dio solo consejos (liderar con skills transferibles, formato híbrido, evitar el CV puramente funcional) de vendedores y career services; NN/g (consejos, no investigación propia) recomienda poner primero la experiencia del campo destino, reformular trabajos pasados en skills transferibles con resultados, un CV por puesto. https://www.nngroup.com/articles/resumes-ux-career-changers/ [L]. SHRM: los recruiters a menudo no conocen la historia de quienes no encajan en criterios previos. https://shrm.org/topics-tools/news/talent-acquisition/lesson-recruiters-take-chance-nontraditional-candidates [S]
- Respaldo adyacente: NN/g cita un metaanálisis de Van Iddekinge y colegas que no halló «significant correlation between long-term job performance and candidates' prior work experience or job tenure». https://www.nngroup.com/articles/resumes-ux-career-changers/ [L, citado de segunda mano; verificar en el original]

### Recurso canónico

**Kristal, Nicks, Gloor y Hauser (2023), Nature Human Behaviour** (https://www.nature.com/articles/s41562-022-01485-6; mientras no se pueda abrir, la página de HKS y la de BIT): fijarse en las cuatro ramas del experimento y en la limitación de una sola persona y razón. Para el hueco como desempleo reciente, **Kroft et al. 2013** (https://www.nber.org/papers/w18387). Para cambio de carrera no hay recurso canónico encontrado.

---

## Huecos de la investigación

- **Bock 2014, original no leído**: LinkedIn dio 403 y la copia DOCX salió binaria; la fórmula y fecha vienen de buscador y de la guía de Yale. Falta una lectura del original para confirmar el ejemplo y el texto sobre la línea de base.
- **Janiszewski y Uy 2008 y la réplica**: solo [S]; pubmed no cargó. Falta el abstract literal y el paper sobre «demasiada precisión» (no ubicado).
- **Sin estudio directo sobre CVs con logros cuantificados vs. no cuantificados**, ni sobre credibilidad de métricas infladas por parte de reclutadores técnicos reconocidos; solo foros y un ranking informal. Una búsqueda que valga la pena: audit studies sobre impression management/«CV claims» y credibilidad.
- **Informe de Burning Glass**: las cifras 3,6%, 18% y 0,14 pp no están verificadas en el texto del informe; el PDF no devolvió contenido útil. La nota de LinkedIn 2025 tampoco se leyó.
- **Documentación oficial de ATS** (Greenhouse, Lever, Workday): no leída; lo que hay es de blogs.
- **Skills listadas vs. mostradas y keyword stuffing**: sin estudio independiente; solo vendedores.
- **Cambio de carrera**: sin evidencia empírica encontrada; solo consejos.
- **Huecos**: ResumeGo vs. BIT/Nature discrepan (dadas las dos). Falta ver el texto de Nature para los números por rama y confirmar si el resultado de roles de baja calificación es real. LinkedIn: cifras de la encuesta con muestra y porcentajes de hiring managers no verificados en fuente oficial. Nada específico de Argentina ni de remoto para EE.UU./Europa.
- **STAR vs. CAR**: no se encontró una fuente de autoridad que compare los marcos; solo guías de universidades que usan uno u otro (MIT usa PAR).
- Master resume: la práctica está en guías (MIT, Northeastern); sin estudio de efecto.
