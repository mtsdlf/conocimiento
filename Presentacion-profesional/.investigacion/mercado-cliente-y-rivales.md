# Mercado de roles de IA: el cliente y los rivales (pasos 3 a 5 del recorrido)

Fecha de la investigación: 2026-11-24. Ángulo: quién contrata (paso 3), contra quién se compite por clase (paso 4) y qué traen los candidatos que consiguen el puesto (paso 5), para plataforma/inferencia/MLOps, forward-deployed engineer (FDE) y AI engineer aplicado, con foco en quien viene de infraestructura.

Nota de método: las páginas marcadas [L] se leyeron con WebFetch, que devuelve un extracto hecho por un modelo chico, no el texto literal completo; las citas entre comillas son las que ese extracto trajo. [S] es solo resumen del buscador. Una ronda de 3 búsquedas ya agotó lo accesible en varias preguntas; los huecos están al final. Ninguna fuente de acá es específica de Argentina: todo es mercado global o de EE.UU.

## 1. Fuentes

Puntajes 1-3: A = autoridad, P = profundidad, E = ejemplos, U = unicidad.

| # | Fuente | URL | Tipo | A | P | E | U | Lectura |
|---|---|---|---|---|---|---|---|---|
| F1 | Northzone, On The Pulse: AI Engineer Hiring (2025-10-13) | https://northzone.com/2025/10/13/ai-engineer-hiring/ | secundaria (encuesta de un fondo a su cartera; n no declarado) | 2 | 2 | 2 | 3 | L |
| F2 | Heavybit, So You Want to Be an AI Engineer (2026-02-03) | https://heavybit.com/library/article/so-you-want-to-be-an-ai-engineer | secundaria (31 avisos de 21 empresas, más entrevistas) | 1 | 2 | 2 | 2 | L |
| F3 | 365 Data Science, AI Engineer Job Outlook (2026-04-23) | https://365datascience.com/career-advice/career-guides/ai-engineer-job-outlook-2025/ | vendedor (curso) con muestra: 903 avisos de Glassdoor EE.UU. | 1 | 3 | 2 | 2 | L |
| F4 | Ashby, Talent Trends: AI job postings (2026-07-09) | https://www.ashbyhq.com/talent-trends-report/reports/ai-job-postings | primaria (datos propios de un ATS; más de 200.000 avisos 2021-Q2 2026), vendedor | 3 | 2 | 1 | 3 | L |
| F5 | Fortune, FDE (2026-09-03), con datos Lightcast | https://www.fortune.com/2026/09/03/forward-deployed-engineers-fast-growing-six-figure-silicon-valley-job-integrate-ai-with-customers-tech-careers-palantir/ | secundaria (prensa que cita a Lightcast) | 2 | 1 | 2 | 2 | L |
| F6 | The Pragmatic Engineer, ¿FDE menos deseable? (2026-03-26) | https://newsletter.pragmaticengineer.com/p/is-the-fde-role-becoming-less-desirable | secundaria (periodista especializado, entrevistas a candidatos) | 2 | 2 | 3 | 2 | L |
| F7 | Lightcast, AI Pathways (2025-09-20) | https://lightcast.io/resources/blog/ai-pathways-profiles | primaria (perfiles en línea; método no descrito), vendedor de datos | 3 | 1 | 1 | 3 | L |
| F8 | LinkedIn Economic Graph, AI engineering talent (2025-05-22) | https://economicgraph.linkedin.com/blog/understanding-the-talent-infrastructure-powering-ai-transformation (la página redirige; el extracto vino de la entrada de OECD.AI) y https://oecd.ai/en/wonk/ai-workforce-what-linkedin-data-reveals-about-ai-talent-trends-in-oecd-ai-live-data | primaria | 3 | 1 | 1 | 2 | L (OECD.AI) / S (LinkedIn) |
| F9 | Andela vía CIO Dive (2026-09-17) | https://www.ciodive.com/news/tech-job-market-andela-AI/830591/ | vendedor (nearshore) citado por prensa; método no descrito | 1 | 1 | 1 | 2 | L |
| F10 | Menlo Ventures, State of Generative AI in the Enterprise (2025-12-09) | https://menlovc.com/perspective/2025-the-state-of-generative-AI-in-the-enterprise/ | secundaria (n = 495 decisores de EE.UU., campo 7-25 nov 2025) | 2 | 2 | 1 | 2 | L |
| F11 | a16z, How 100 Enterprise CIOs Are Building and Buying Gen AI (2025-06-10) | https://a16z.com/ai-enterprise-2025/ | secundaria (n = 100 CIO, datos al 8 mayo 2025) | 2 | 2 | 2 | 2 | L |
| F12 | Amplify Partners, The 2025 AI Engineering Report (2025-06-24) | https://amplifypartners.com/blog-posts/the-2025-ai-engineering-report | secundaria (cientos de ingenieros, n no declarado, con Latent Space: sesgo de audiencia) | 2 | 2 | 2 | 3 | L |
| F13 | Workday, More Candidates, Fewer Matches (2026-10-27) | https://www.workday.com/en-us/perspectives/hr/2026/10/ai-hiring-match-problem.html | vendedor (reporte propio; sin n) | 1 | 1 | 1 | 2 | L |
| F14 | BambooHR, State of Hiring 2026 | https://www.bamboohr.com/resources/data-at-work/data-stories/state-of-hiring-2026 | vendedor | 1 | 1 | 1 | 1 | S |
| F15 | The Pragmatic Engineer, job market 2026 | https://newsletter.pragmaticengineer.com/p/state-of-the-job-market-2026 | secundaria | 2 | 2 | 2 | 2 | S |
| F16 | Indeed/FT, Bloomberry, Paraform, Lightcast vía IT Brew y KDnuggets (crecimiento de avisos de FDE) | https://kdnuggets.com/forward-deployed-engineer-ais-hottest-new-career-or-consulting-with-a-better-title ; https://www.itbrew.com/stories/2025/12/19/will-2026-be-the-year-of-the-forward-deployed-engineer | secundaria | 1 | 1 | 1 | 1 | S |
| F17 | Instituto for Ethical AI & ML, encuesta de 170 profesionales (Q4 2024) vía The New Stack | https://thenewstack.io/ml-and-llm-adoption-challenged-most-often-by-observability/ | secundaria | 2 | 1 | 1 | 2 | S |
| F18 | arXiv 2410.20791, From Cool Demos to Production-Ready FMware (cita encuesta de 430 profesionales) | https://arxiv.org/html/2410.20791v2 | primaria académica | 3 | 1 | 1 | 2 | S |
| F19 | Second Talent / AI Talent Report / HeroHunt (oferta y demanda de infra de IA) | https://www.secondtalent.com/occupations/ai-inference-engineer/ ; https://atr-blog.pages.dev/ai-infra-engineer-demand-2026 ; https://www.herohunt.ai/blog/how-to-recruit-ai-inference-engineers-2026-guide/ | vendedores (reclutadores) | 1 | 1 | 1 | 1 | S |
| F20 | InterviewStack vía DEV Community (3.449 avisos, mayo 2026) y KDnuggets (390 avisos) | https://dev.to/gnana_6392e836fd500a957dc/ai-engineer-skills-companies-want-in-2026-3449-posting-analysis-5f9l ; https://kdnuggets.com/the-ai-skills-that-actually-show-up-in-job-postings-right-now | vendedor / secundaria | 1 | 1 | 1 | 1 | S |
| F21 | Guías de DevOps a MLOps (Interview Kickstart, DevOpsCube, etc.) | https://interviewkickstart.com/career-transition/devops-engineer-to-mlops-engineer ; https://devopscube.com/devops-to-mlops/ | vendedores (formación) | 1 | 1 | 1 | 1 | S |

Los puntajes de F14 a F21 son bajos a propósito: solo se vieron por el buscador. No se leyó el PDF de LinkedIn "US software engineer talent landscape 2026": se descargó pero está comprimido y WebFetch no pudo extraerlo (archivo local en la carpeta tool-results de la sesión).

## 2. Paso 3: el cliente (quien contrata)

### 2.1 El trabajo que contrata la empresa

Formulación de trabajo (inferencia mía a partir de las afirmaciones de abajo, a validar con entrevistas): cuando tengo un prototipo de LLM o un cliente que pide IA, quiero que llegue a producción confiable, con costo y latencia controlados, y integrado a lo que ya existe, para entregar valor sin armar un equipo de investigación.

Afirmaciones con fuente:

1. **Llegar a producción es el criterio central.** "Companies want people who've already shipped LLM applications in production" (F2, 2026-02-03). Un respondiente de Northzone: "Any AI Engineer also needs to be a good SWE to get things into production" (F1, 2025-10-13).
2. **Se prefiere ingeniería de software sobre investigación.** Northzone: los prioritarios son los ingenieros de software generalistas y los ML engineers aplicados; la empresa puede "upskillear" a quien entiende "the product, codebase, and infrastructure" en lugar de contratar PhDs difíciles de hallar (F1). El extracto de F1 no da cifras de estos grupos.
3. **Lo que hace un AI engineer, por cuántos lo citan** (Northzone, 2025-10-13, n no declarado, cartera de un fondo): colaborar con producto y diseño casi todos; prompt engineering y optimización de recuperación 90%; evaluación 80%; armado de stack LLM (RAG, cadenas, agentes) 70%; fine-tuning 50%; **infraestructura (inferencia, GPUs, serving a escala) 35%**; construir y desplegar modelos de ML 5% (F1). Lectura: para el rol de AI engineer aplicado, infraestructura es un tercio de los casos, no el centro.
4. **Qué piden los avisos** (Heavybit, 31 avisos de 21 empresas, 2026-02-03): Python 77%, TypeScript 29%, agentes 71%, evals 61%, RAG 29%, fine-tuning 29%, MCP 16%, PyTorch 16%, TensorFlow 10%; "Python is table stakes" (F2). Muestra chica.
5. **Infra de MLOps en avisos** (365 Data Science, 903 avisos de Glassdoor EE.UU., 2026-04-23): Kubernetes 17,6% ("the top MLOps tool"), Docker 15,4%, despliegue continuo 10,4%; nube AWS 33% y Azure 26% en el gráfico, pero el texto de la fuente se contradice en el orden de AWS y Azure (F3). Es un muestreo de avisos de AI engineer en general, no de roles de plataforma.
6. **FDE: producción más cliente.** Lightcast vía Fortune (2026-09-03): los empleadores piden programación, ML, IA generativa e infraestructura tecnológica; APIs, pipelines de datos, nube y llevar sistemas de IA a producción; consultoría y comunicación; juicio de negocio y evidencia de resultados (F5). Una fuente secundaria describe una entrevista con caso de estudio y, a veces, simulación de cliente (F16, [S]).
7. **El título es un cajón de sastre.** Andela (casi 50.000 descripciones, más de 1.800 de AI/ML engineer): más de la mitad de los avisos con título de IA mezclan habilidades de al menos dos roles (F9, 2026-09-17; método no descrito, vendedor). Cita: "Companies are saying, 'I need to go hire an AI engineer,' but that's an extremely broad term". Andela menciona un rol nuevo, "FinOps reliability engineer", que suma costo de nube y presupuesto de tokens (F9).
8. **La no-demanda por el cargo FDE existe.** Pragmatic Engineer (2026-03-26): el FDE se parece al ingeniero de ventas o de soluciones; un reclutador estima que solo "maybe 10% of the market" quiere el rol aunque "everyone wants them" (F6). Un ingeniero renunció a las cuatro semanas con la descripción "a typical IT services mindset" (F6).

### 2.2 Qué frena llevar IA a producción (el problema del cliente)

| Dato | Fuente | Fecha | Fiabilidad |
|---|---|---|---|
| Observabilidad y monitoreo fue el mayor desafío para pasar modelos a producción; seguridad y gobernanza quedaron mucho más abajo (n = 170 practicantes, Q4 2024) | F17 | publicada 2025 | [S], n chico, ML clásico y LLM mezclados |
| Encuesta de 430 profesionales: solo 10% de las organizaciones había lanzado FMware (software con modelos de fundación) a producción; los desafíos principales fueron confiabilidad, costo de implementación alto, latencia, cumplimiento y privacidad | F18 | 2024 (preprint) | [S] |
| Los CIO de a16z (n = 100, datos al 8 mayo 2025): "Security and cost now weigh more heavily in procurement than accuracy"; las herramientas internas "are hard to maintain" y a menudo no dan ventaja; el costo de cambiar de modelo sube con los flujos de agentes ("all the prompts have been tuned for OpenAI") | F11 | 2025-06-10 | [L] extracto |
| Los costos por modelo caen "about an order of magnitude every 12 months" (afirmación de a16z, sin método en el extracto); el gasto neto sube igual: "Net spend on generative AI continues to rise despite falling costs of inference" (Menlo) | F11, F10 | 2025 | [L] |
| Amplify (2025-06-24): más de 40% no quiere pagar más por cómputo de inferencia; 60% usa observabilidad estándar y más de 50% evals offline; 80% dice que los LLM funcionan bien en el trabajo contra menos de 20% de los agentes; el extracto no nombra el "dolor número 1" | F12 | 2025-06 | [L], n no declarado |
| Menlo (n = 495, 7-25 nov 2025): solo 16% de los despliegues de empresas y 27% de los de startups son agentes verdaderos; el resto son flujos fijos o ruteo en torno a una llamada a un modelo | F10 | 2025-12-09 | [L] |

Lectura (inferencia): los problemas de costo, latencia, confiabilidad y observabilidad aparecen en todas las fuentes y son trabajo de ingeniería de plataforma. No encontré una encuesta del tipo MLOps Community ni Retool State of AI que ordene los frenos con porcentajes (hueco).

Dato que discrepa: Menlo y a16z muestran que las empresas compran más de lo que construyen (Menlo: 76% de los casos de uso de IA se compran contra 53% el año anterior; a16z: giro hacia comprar aplicaciones de terceros). Eso reduce la demanda de equipos internos de aplicación, pero ambas encuestas son de grandes empresas de EE.UU. y Menlo excluye de su medición la inferencia y el model serving (F10).

### 2.3 Señales del candidato que resuelven ese trabajo

Todo lo siguiente es inferencia mía, armada con las afirmaciones de 2.1 y 2.2:

| Trabajo del cliente | Señal que lo resuelve | Fuente de la demanda |
|---|---|---|
| Que llegue a producción | Un sistema real en producción con tráfico, alertas, despliegues y su historia | F1, F2, F5 |
| Costo y latencia de inferencia | Mediciones propias: tokens por dólar, latencia p95, comparación de modelos o de servidores de inferencia | F11, F12, F19 |
| Confiabilidad y observabilidad | Trazas, evals, tableros, manejo de fallas de proveedor | F12, F17, F18 |
| Integrarse al cliente (FDE) | Entregas cerca del usuario, comunicación escrita, resultado cuantificado | F5, F6 |
| Menor riesgo que contratar un investigador | Ingeniería de software sólida con la IA como extensión | F1 |

## 3. Paso 4: los rivales por clase

La tipología es la de [identificación de competidores](../../Estrategia-competitiva/Analisis-de-competidores/identificacion-de-competidores.md). La lista es de trabajo mía; solo las cifras de la columna "Evidencia" tienen fuente.

| Clase | Rival | Por qué está | Evidencia |
|---|---|---|---|
| Directo | ML engineers aplicados | Los nombra Northzone como segundo grupo de contratados | F1 |
| Directo | Ingenieros de software generalistas que se capacitan en IA | Primer grupo de contratados en Northzone; Amplify: entre los de 10+ años de experiencia en software, 45% tiene 3 años o menos de experiencia en IA (el buscador mostró 51% en la página de resultados compartida: dos cifras para el mismo dato) | F1, F12 |
| Directo | Investigadores con PhD | "Almost five times more likely to have a PhD than the average worker" (AI engineers); en avisos, 28% pide PhD según 365 Data Science | F7, F3 |
| Directo | Recién graduados | Del lado de la oferta, 36% de los AI engineers se graduó en los últimos cinco años (Lightcast); del lado de la demanda, solo 3% de los avisos son para nuevos graduados (Heavybit) y 2,5% pide 0-2 años (365DS) | F7, F2, F3 |
| Directo | DevOps/SRE/plataforma que pivotean | La competencia más cercana para plataforma de inferencia; las guías lo llaman "una extensión" de DevOps, pero son vendedores de formación | F21 [S] |
| Indirecto | Nearshore y staff augmentation (Andela y similares) | Venden el mismo resultado con equipo; Andela publica análisis de avisos y vende talento | F9; F19 (staff augmentation para infra de IA, Ardan Labs, [S]) |
| Indirecto | Consultoras y agencias de IA, equipos de servicios de los labs | Sin dato propio en esta ronda; FDE se describe como "consulting with a better title" | F16 [S], F6 |
| Sustituto | Productos comprados en lugar de construidos | Menlo: 76% de los casos de uso se compran (53% el año anterior); a16z: más de 90% de los encuestados probaba apps de soporte de terceros | F10, F11 |
| Sustituto | APIs de inferencia y plataformas gestionadas | Menlo ubica los despliegues de agentes sobre una sola llamada a un modelo; a16z: Databricks como opción de hosting. Sin cifra de cuántas empresas evitan contratar plataforma por esto | F10, F11 |
| Sustituto | Agentes de código | a16z cita a un CTO de SaaS con "nearly 90% of code is AI-generated", de 10-15% doce meses antes; es un solo testimonio | F11 |
| Potencial | Los propios equipos de producto reconvertidos | Northzone: AI engineers son hoy 25-33% de los equipos y se esperan casi la mitad en etapa temprana | F1 |
| No consumo | No contratar o esperar | Workday: 34% de los gerentes dice que los puestos quedan sin cubrir por falta de candidatos con las habilidades; 60 días de mediana para cubrir | F13 |

### 3.1 Cuántos candidatos compiten

No hay datos específicos de puestos de IA en lo accesible. Lo que hay es general y de vendedores:

- Workday (Global Workforce Report, oct 2026): 69 postulaciones por oferta, 19% más que un año antes; tecnología y medios 40% más. Sin n ni método en el extracto (F13).
- BambooHR (abril 2026): de unas 46 por aviso en 2021 a 95 en 2025 [S] (F14).
- LinkedIn India: las postulaciones por vacante más que se duplicaron desde 2022 y AI Engineer está entre los títulos más postulados [S] (peoplematters.in: https://www.peoplematters.in/news/recruiting-and-onboarding/applicants-per-job-double-in-india-intensifying-job-search-pressure-linkedin-47949). Es India, no Argentina.
- Anécdota, no dato: un aviso con unas 23.000 postulaciones para 8 puestos, unas 3.000 por puesto [S] (F15).
- Ashby (F4): los avisos de tecnología con IA en el título "are less likely to be filled from inbound or referral applications": 28% por sourcing, 9,2% por agencias, 37,1% por inbound. Es decir, buena parte se llena sin pasar por la postulación abierta (contra, no hay desglose del mismo dato para roles sin IA en el extracto).

Dos lecturas que discrepan sobre la escasez: reclutadores dicen que hay 1,6 millones de roles de IA abiertos contra 518.000 calificados (Second Talent, vendedor, sin método; F19 [S]); Workday cita a una psicóloga: "The difficulty in hiring is likely not a lack of qualified people, but a misalignment of roles and skills" (F13). Las dos cosas pueden ser ciertas a la vez.

### 3.2 Demanda por rol (para dimensionar el pozo)

| Dato | Fuente | Fecha |
|---|---|---|
| Los AI Engineers son una participación de contratación 14 veces mayor que en 2019 y 10 veces mayor que en 2022; las transiciones a ingeniero de IA generativa crecieron pero siguen en menos de 1% de los cambios de ingenieros de software (reporte de LinkedIn de febrero 2026, citado por el buscador) | LinkedIn vía buscador [S] | 2026-02 |
| 0,7% de los miembros de LinkedIn son talento de IA en 2024 (7 de cada 1.000), +130% desde 2016; definición: al menos dos habilidades de ingeniería de IA en el perfil o haber tenido un empleo de IA | F8 | 2025-05-22 |
| Avisos de FDE: más de 1.000% de enero a agosto 2026 contra el mismo período de 2025, más de 4.600% contra 2023; avisos de tecnología en general +13%; salario anunciado mediano más de 188.000 USD contra unos 145.000 USD de ingenieros de software tradicionales (Lightcast) | F5 | 2026-09-03 |
| Estimaciones de crecimiento de FDE que discrepan según la fuente y la ventana: 350% (Paraform, Q1 2025 a Q1 2026), 729% (Indeed, abril interanual), más de 800% (Indeed/FT, enero-septiembre 2025), 1.165% (Bloomberry, 2024-2025); "FDE" aparece también como "Applied AI Engineer" | F16 | 2025-2026 |
| Indeed: avisos de FDE crecieron más de diez veces en 2025 contra 2024 | F6 | 2026-03-26 |
| Ashby: la IA aparece en el título del 8% de los avisos de tecnología (menos de 1% en 2023); en la descripción, por encima de 50% | F4 | 2026-07-09 |
| Avisos de infraestructura de IA: +41% en 2025 contra +12% del conjunto de talento; 390.000 avisos globales de "AI infrastructure" en Q1 2026 contra 275.000 (sin poder verificar contra LinkedIn) | F19, solo vendedor [S] | 2026 |

El dato de F19 es de vendedores (un agregador y firmas de reclutamiento); tratar como dirección, no como medida.

## 4. Paso 5: qué traen los candidatos que consiguen estos puestos

Lo que se ve sobre el perfil, por dato:

- **Origen: ingeniería de software.** Northzone: el grupo más grande es el de ingenieros de software generalistas que se capacitaron en IA; después los ML engineers; menos común, los de perfil académico y los de infraestructura o DevOps, "sin cifras" (F1, 2025-10-13).
- **Transiciones desde roles no IA.** OECD.AI con datos de LinkedIn de 19 países, años agrupados: la mayor parte de las transiciones a ocupaciones de IA viene de ocupaciones no IA, como ingeniero de software, analista de datos y asistente de investigación (según el buscador, que cita datos de 2023; no se pudo leer el texto completo) [S].
- **Trayectoria típica.** Lightcast (2025-09-20): la mayoría de los AI engineers pasó por otros dos roles antes de entrar a IA como tercer rol; 31% empezó su carrera en roles relacionados con IA; cerca de 20% empezó en trabajos no STEM (F7). Método de perfiles no descrito.
- **Formación.** 80% de los trabajadores de IA en roles técnicos estudió campos adyacentes (informática u otros STEM); solo 11% de las calificaciones de los AI engineers son de IA (F7). Los avisos piden títulos de ingeniería en 69%, informática en 61%, ML en 42%; niveles: PhD 28%, maestría 24%, grado 24%, sin dato 25% (F3, muestra de Glassdoor EE.UU.). Burtch Works pone PhD en torno de 24% (27% el año anterior) entre profesionales de IA [S].
- **Años.** En los avisos de F3, solo 33% declara experiencia; la mayor parte apunta a 2-6 años (2-4: 9%, 4-6: 12%). Heavybit: roles "mostly mid-to-senior" y 3% para nuevos graduados (F2). En FDE, una encuesta de India menciona 3 a 5 años [S] (F16).
- **Experiencia en IA de quienes ya trabajan.** Amplify (2025-06-24): entre quienes tienen 10+ años de ingeniería de software, 45% tiene 3 años o menos de experiencia en IA; 1 de cada 10 respondientes tiene menos de un año en IA (F12). Lectura: entrar con poca experiencia propia en IA es la norma entre los seniors, no una desventaja.
- **Proyectos, open source y publicaciones.** No encontré ningún estudio con datos de cuántos candidatos contratados tienen open source o publicaciones. Hueco. Lo que sí está: los avisos piden "shipped LLM applications in production" (F2) y evidencia de resultado cuantificada (F5).

Perfil de respuesta de los rivales (inferencia, para el documento final; no hay datos de respuesta de nadie): el rival más fuerte es el ingeniero de software con 4-8 años que ya sumó RAG, evals y agentes a su stack; las plataformas gestionadas compiten por quitar el puesto, no por ocuparlo.

## 5. Terreno: dónde infraestructura más IA tiene menos competencia

Ninguna fuente lo afirma de forma directa. Lo que hay, y lo que es inferencia:

1. **Infraestructura es una parte chica del rol de AI engineer** (35% de las empresas la cita en F1), y los candidatos de perfil infraestructura/DevOps son "menos comunes" entre los contratados en el mismo estudio. Dato: sí. Que eso signifique menos competencia: inferencia mía. Podría ser también poca demanda.
2. **Los avisos mezclan roles** (F9): hay "skill bleeds" en que a los DevOps se les pide nube y se les suma IA, y aparecen roles como "FinOps reliability engineer" que unen costo de nube y presupuesto de tokens. Es una puerta abierta para el perfil de infraestructura, sin cifra.
3. **Costo, observabilidad y confiabilidad son los dolores que recurren** en F11, F12, F17 y F18, y son trabajo de plataforma. No hay encuesta con porcentajes que los ordene.
4. **Los reclutadores de infra de inferencia sostienen que la demanda crece más que la oferta** (F19, vendedores, sin método verificable): tomarlo como hipótesis. Una fuente discrepa sobre el tamaño de la escasez (F13).
5. **FDE: poca gente quiere el cargo** (F6, estimación de un reclutador: 10%) mientras la demanda crece. Es el rol donde el dato sugiere menos competencia por el cargo en sí, con un costo: el trabajo se parece más a servicios que a ingeniería de producto (F6).
6. **Contra el terreno:** Menlo y a16z muestran el desplazamiento hacia comprar en vez de construir, y las APIs de inferencia son sustituto de un equipo de plataforma de inferencia. Un candidato de infraestructura gana terreno donde la empresa corre modelos propios (regulación, on-prem, costo a escala); a16z menciona que las necesidades on-prem favorecen modelos de código abierto en empresas más grandes (F11).

## 6. Tabla resumen por rol (solo lo hallado en este ángulo; la columna de mercados es de otro ángulo)

| Rol | Qué trabajo contrata | Rival principal | Señal más valiosa | Evidencia de demanda | Competencia |
|---|---|---|---|---|---|
| Plataforma/inferencia/MLOps | Costo, latencia, confiabilidad, observabilidad de modelos en producción | DevOps/SRE que pivotean; ML engineers; plataformas gestionadas como sustituto | Medición propia de costo/latencia y un sistema operando | Avisos de infra +41% (vendedores, [S]); Kubernetes 17,6% de avisos de AI engineer (F3) | Sin dato directo; "menos común" en contratados (F1) |
| Forward-deployed engineer | Llevar IA al cliente y hacerla funcionar | Ingenieros de software con perfil de cliente; consultoras y servicios | Entrega con cliente, comunicación, resultado cuantificado | +1.000% de avisos en 2026, mediano 188.000 USD (Lightcast, F5) | Solo ~10% del mercado quiere el cargo (F6, un reclutador) |
| AI engineer aplicado | Producto con LLM en producción | Ingenieros de software capacitados en IA (grupo más grande) | Productos de IA enviados; evals; agentes | Participación de contratación 10-14 veces mayor (LinkedIn, [S]); IA en 8% de los títulos (F4) | Alta: título muy buscado; 69 postulaciones por oferta en general (F13) |

## 7. Huecos

- No hay datos de postulaciones por aviso para puestos de IA (Ashby/Greenhouse no publican ese corte en lo accesible; solo el general de Workday y BambooHR).
- No se encontró encuesta de MLOps Community ni de Retool State of AI con ranking de frenos a producción; solo F17 y F18 por buscador, con n chico o de 2024.
- No se leyó el PDF de LinkedIn "US software engineer talent landscape 2026" (ilegible para WebFetch); las cifras de LinkedIn de 2026 vienen del buscador.
- Sin estudio con perfiles de contratados (open source, publicaciones, proyectos); los datos de Lightcast no describen su método.
- Sin posts de hiring managers recogidos de forma sistemática; los datos de "qué buscan" vienen de encuestas de fondos y de análisis de avisos, que miden lo que dice el aviso y no lo que decide la contratación.
- No hay datos de Argentina ni de LATAM en este ángulo; todo es global o EE.UU. (más India en un caso).
- Sustitutos: ningún estudio mide cuántas empresas evitaron contratar por usar APIs gestionadas; es inferencia.
- Las cifras de salario entre fuentes no coinciden y no se comparan entre sí: Northzone dice que cerca de tres cuartos de los AI engineers gana 150.000 USD o menos de base (F1); Heavybit, base de 130.000 a 325.000 USD según nivel (F2); 365DS, promedio de unos 206.000 USD en avisos de EE.UU. (F3); Lightcast, mediana anunciada de FDE 188.000 USD (F5). Muestras y poblaciones distintas; el ángulo de pago es de otro informe.
