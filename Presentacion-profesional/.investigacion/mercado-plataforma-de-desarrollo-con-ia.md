# Mercado: plataforma de desarrollo con IA (investigación cruda, 2026-11-24)

Tesis: hay una oportunidad laboral en la intersección IA + plataforma + flujo de desarrollo (rediseñar plataforma interna, CI/CD y organización de equipos para que asistentes y agentes de código rindan, y sistemas que se observan y corrigen solos), para alguien con experiencia de líder DevOps/plataforma.

Veredicto corto: el **problema** está bien respaldado por fuentes primarias (DORA 2025, Perforce/Puppet 2026, Faros); el **rol como título de aviso con cantidad medible de vacantes y pago** casi no pudo medirse (huecos grandes). La evidencia de que la IA rinde por sí sola es mixta y sin consenso; eso sostiene la tesis (hace falta sistema alrededor) pero también la contraria (efecto chico, absorbido por equipos existentes).

Nota de método: las marcas [L]/[M]/[S] valen así. [L] = no pude leer entero ninguna fuente (WebFetch devuelve un extracto procesado, no el texto completo), por eso ninguna lleva [L]. [M] = página abierta con WebFetch y citas extraídas de ella. [S] = solo resumen del buscador. Las citas entre comillas de fuentes [M] son las que devolvió el extractor; las verifiqué solo contra esa respuesta.

## 1. Tabla de fuentes

Puntajes 1-3: autoridad / profundidad / ejemplos / unicidad.

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| F1 | Google Cloud, "Highlights from the 10th DORA report" (2024-10-22) | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report | primaria (resumen del propio DORA; Google vende nube) | 3/2/1/2 | M |
| F2 | DORA 2025, anuncio (2025-09-23) | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | primaria (Google) | 3/2/1/2 | M |
| F3 | DORA AI Capabilities Model (Google Cloud blog) | https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model | primaria (Google) | 3/2/1/3 | M |
| F4 | Informe DORA 2025 en PDF (State of AI-assisted Software Development) | https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf | primaria | 3/3/2/3 | no leído (excede 10 MB, WebFetch falló); solo capítulos vistos por el buscador [S] |
| F5 | InfoQ, "AI Is Amplifying Software Engineering Performance" (2026-03-17) | https://infoq.com/news/2026/03/ai-dora-report/ | secundaria | 2/1/1/1 | M |
| F6 | METR, estudio RCT (2025-07-10) | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | primaria | 3/3/2/3 | M |
| F7 | METR, "uplift update" (2026-02-24) | https://metr.org/blog/2026-02-24-uplift-update/ | primaria | 3/3/2/3 | M |
| F8 | Cui et al., Management Science (SSRN 4945566) | https://papers.ssrn.com/abstract=4945566 ; https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2025.00535 | primaria (revisada por pares) | 3/3/2/3 | S (la página de INFORMS dio 403); datos vía MIT Sloan https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-affects-highly-skilled-workers |
| F9 | Faros AI, AI Productivity Paradox Report 2025 (2025-07-23) | https://www.faros.ai/blog/ai-productivity-paradox-report-2025 | **vendedor** (analítica de ingeniería) | 2/2/1/2 | M |
| F10 | Perforce Puppet, State of Platform Engineering 2026, cap. "Where AI works" | https://www.puppet.com/resources/2026-state-of-platform-engineering/where-AI-works | **vendedor** (Perforce vende plataformas) | 2/2/1/2 | M (muestra y fecha de la página no vistas; el buscador dice n=820 y lanzamiento 2026-07-08, vía https://www.perforce.com/press-releases/state-of-platform-engineering-2026 [S]) |
| F11 | Gartner (vía PagerDuty, The Register, Gartner press 2026-10-26) | https://www.pagerduty.com/resources/analyst-reports/analyst-report/gartner-report-autonomous-reliability-unleashing-agentic-ai-for-self-healing-it-operations/ ; https://www.gartner.com/en/newsroom/press-releases/2026-10-26-gartner-identifies-the-top-ai-trends-in-infrastructure-and-it-operations-for-2027 | secundaria / vendedor (PagerDuty revende el informe) | 2/1/1/1 | S |
| F12 | Indeed Hiring Lab, empleo de software 2026 | https://hiringlab.indeed.com/?p=20708 | primaria (datos propios de Indeed) | 3/2/1/3 | M |
| F13 | Dice, informe de julio 2026 (vía HR Dive) | https://www.hrdive.com/news/dice-report-tech-hiring-AI/824902/ | secundaria | 2/1/1/2 | S |
| F14 | Levels.fyi, DevOps Engineer (EE.UU.) | https://www.levels.fyi/t/software-engineer/title/devops-engineer | primaria (datos reportados por usuarios, autoselección) | 2/1/1/3 | S |
| F15 | Coderhouse, cálculo propio sobre datos abiertos de sysarmy 2026.1 | https://www.coderhouse.com/ar/sueldos/sueldo-devops-engineer-buenos-aires-2026 | secundaria / **vendedor** (bootcamp) | 2/2/1/2 | M |
| F16 | Avisos con rango (Chromatic, FlexJobs, Dice, Enumerate, Nortal, Devsu, Workana) | ver sección 3 | primaria (el aviso) | 1/1/2/1 | S (todos vía buscador, salvo el listado de una consultora en LatAm visto en WebFetch) |
| F17 | Consultoría: Allianz Trade IT services; Accenture blog (julio 2026); Alpha-Sense | https://www.allianz-trade.com/sk_SK/novinky-a-analyzy/mapy-rizika-podla-sektorov/it-services.html ; https://www.accenture.com/us-en/blogs/cloud/ai-native-software-delivery | Allianz secundaria; Accenture **vendedor**; Alpha-Sense secundaria | 1-2/1/1/1 | S |
| F18 | MIT NANDA "GenAI Divide" (2025-08) vía The Register | https://www.theregister.com/2025/08/18/generative_ai_zero_return_95_percent | secundaria sobre informe de una iniciativa con intereses | 1/1/1/2 | S |
| F19 | Stack Overflow Developer Survey 2025 (publicada 2025-07-29) | https://stackoverflow.blog/2025/07/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here | primaria | 3/2/1/3 | S |

## 2. Afirmaciones por pregunta

### P1. Evidencia sobre IA y productividad de desarrollo

**DORA 2024** (F1 [M], 2024-10-22)
- "As AI adoption increased, it was accompanied by an estimated decrease in delivery throughput by 1.5%, and an estimated reduction in delivery stability by 7.2%." Son asociaciones estimadas de encuesta, no efecto medido; el buscador (RedMonk, https://redmonk.com/rstephens/2024/11/26/dora2024/ [S]) las encuadra por "cada 25 % más de adopción"; no lo verifiqué en el informe.
- Mismo texto: "AI is boosting productivity for many developers. More than one-third of respondents experienced 'moderate' to 'extreme' productivity increases."
- Plataforma, cuatro hallazgos (F1): las plataformas internas "effectively increase productivity for developers"; son más comunes en empresas grandes; "Implementing a platform engineering initiative might lead to a temporary decrease in performance before improvements manifest"; hace falta diseño centrado en el usuario e independencia del desarrollador. (Los números por métrica de plataforma, que recuerdo de otras lecturas, no los verifiqué: no los uses sin leer el PDF de 2024, https://dora.dev/report/2024.)
- Muestra: más de 39.000 profesionales (InfoQ, https://www.infoq.com/news/2024/11/2024-dora-report/ [S]).

**DORA 2025** (F2 [M], 2025-09-23; F3 [M]; F5 [M])
- Muestra: "survey responses from nearly 5,000 technology professionals" y "over 100 hours of qualitative data".
- Amplificador: "AI doesn't fix a team; it amplifies what's already there." Y: "AI accelerates software development, but that acceleration can expose weaknesses downstream."
- Cambio respecto de 2024: "Unlike last year, we observe a positive relationship between AI adoption on both software delivery throughput and product performance." Pero: "AI adoption does continue to have a negative relationship with software delivery stability."
- Plataforma: "90% of organizations have adopted at least one platform and there is a direct correlation between a high quality internal platform and an organization's ability to unlock the value of AI". Y: "In organizations with quality internal platforms, AI's positive influence on organizational performance is amplified." Es el moderador que la tesis necesita, pero la fuente lo presenta como correlación/modelo; no pude leer el coeficiente ni el diseño en el PDF (hueco).
- Las siete capacidades (F3): (1) postura clara y comunicada sobre IA; (2) ecosistemas de datos sanos; (3) datos internos accesibles para la IA; (4) buenas prácticas de control de versiones (commits frecuentes y rollback); (5) trabajar en lotes chicos; (6) foco en el usuario; (7) plataformas internas de calidad. Solo una de las siete (la 7) es plataforma; las otras seis son de organización, datos y práctica.
- InfoQ (F5, secundaria, 2026-03-17): "AI amplifies the quality of the engineering system it operates within"; "Artificial intelligence will not fix broken engineering systems."; sin plataforma la IA puede producir PR más grandes y patrones inconsistentes.

**METR RCT 2025** (F6 [M], 2025-07-10)
- 16 desarrolladores con experiencia en repos open source grandes, 246 issues asignados al azar a permitir o no IA, principalmente Cursor Pro con Claude 3.5/3.7 Sonnet. Resultado: con IA "take 19% longer". Esperaban 24 % más rápido y después creían haber ido ~20 % más rápido.
- Límites dichos por METR: "We do not claim that our developers or repositories represent a majority or plurality of software development work"; "a snapshot of early-2025 AI capabilities in one relevant setting". En F7 el IC del 19 % es +2 % a +39 %.
- Crítica/réplica por METR mismo (F7 [M], 2026-02-24): con herramientas de fines de 2025, 57 desarrolladores, 143 repos, más de 800 tareas. Estimado de los 10 desarrolladores originales: "-18%" (IC -38 % a +9 %); nuevos: "-4%" (IC -15 % a +9 %) (el signo negativo es aceleración). METR concluye que es "an unreliable signal" y "likely a bad proxy for the real productivity impact", porque "30% to 50%" de los desarrolladores no enviaron tareas que no querían hacer sin IA, y se perdieron los más optimistas; además bajaron la paga de $150/h a $50/h. Creen que hoy los desarrolladores van más rápido que en 2025, "but their data is only very weak evidence of this". Es decir: no hay réplica limpia; la evidencia de 2026 es inconclusa.
- Hay además una encuesta de METR (2026-05-11, https://metr.org/blog/2026-05-11-ai-usage-survey/ [S]) con medianas de "uplift" de valor autorreportado entre 1,4x y 2x; es autorreporte, no experimento.

**Cui et al., Management Science** (F8 [S] + MIT Sloan [S])
- Tres experimentos de campo aleatorizados (Microsoft, Accenture, una Fortune 100 anónima), 4.867 desarrolladores; efecto agrupado: +26,08 % de tareas completadas (error estándar 10,3 %); los autores avisan que varía entre experimentos. Los menos experimentados adoptaron más y ganaron más. No pudieron medir calidad del código. Adopción media ~60 % al año. Es Copilot de la era 2023-2024, y mide cantidad de tareas, no estabilidad.

**Telemetría de vendedor** (F9 [M], 2025-07-23, datos a junio 2025)
- Más de 10.000 desarrolladores en 1.255 equipos. Equipos de alta adopción: "complete 21% more tasks and merge 98% more pull requests"; tiempo de revisión de PR +91 %; tamaño medio de PR +154 %; "9% increase in bugs per developer"; y "we observed no significant correlation between AI adoption and improvements at the company level". Faros vende analítica de ingeniería, y lo que mide (cuello de botella de revisión) es justo lo que su producto mira. Sirve como indicio del mecanismo de DORA (más volumen, más trabajo aguas abajo).

**Plataforma como moderador: lo que hay y lo que no**
- A favor: DORA 2025 (arriba, correlación/modelo). Perforce/Puppet 2026 (F10 [M] y F10b [S]): "A majority (66%) of organizations report using AI somewhere in infrastructure workflows"; "Only 31% ... report fully autonomous AI"; con plataforma interna estandarizada sube a 44 %; "autonomy scales through standardization, not experimentation". Por buscador [S]: 73 % de organizaciones maduras vs 44 % de menos maduras dicen que la madurez de plataforma es factor crítico o significativo para el éxito con IA; confianza en IA 81 % vs 48 %; n=820. Encuesta de vendedor, autodeclarada.
- En contra o sin probar: no encontré ningún experimento ni estudio de campo que manipule la calidad de la plataforma y mida el efecto de la IA. Todo lo que hay es correlación de encuesta. Hueco central de la tesis.

### P2. AIOps y sistemas que se vigilan y corrigen

- Adopción real baja en autonomía: Perforce/Puppet (F10 [M]) 31 % con IA totalmente autónoma en flujos de infraestructura (autodeclarado; incluye la definición laxa de cada encuestado).
- Pronósticos de Gartner (F11 [S], secundarios): 70 % de las empresas desplegarán agentes de IA para operar infraestructura de TI en 2029, desde menos de 5 % en 2025 (resumen de informe); The Register da otra cifra, "60 percent ... up from fewer than ten percent today" (https://www.theregister.com/a/5274712 [S]). PagerDuty: 70 % adoptará "autonomous reliability practices" en 2030, desde 5 % en 2026. Las líneas de base discrepan entre fuentes. Es pronóstico, no adopción, y PagerDuty vende el producto.
- Riesgo (Gartner, vía resumen secundario [S]): 40 % de las organizaciones de I&O que usen agentes en producción a escala sufrirán una interrupción con impacto en el negocio hacia 2028. Gartner (press 2026-10-26 [S]) dice que se despliegan agentes para triage de incidentes, validación de cambios y remediación, con barandas con humano en el circuito.
- Resultados: solo cifras de vendedores (MTTR -80 %, -85 %; Rootly, incident.io, sin metodología; ver https://rootly.com/sre/ai-sre-explained-autonomous-agents-slash-mttr-80 [S]). Voces de practicantes: el análisis de causa raíz rinde hoy; la remediación autónoma se limita a acciones conocidas y reversibles (certificados, discos, balanceadores) (DZone, https://dzone.com/articles/ai-in-sre-whats-actually-coming-in-2026 [S]).
- No encontré un estudio independiente con resultados medidos de auto-remediación en producción. Hueco.

### P3. Mercado laboral

**Demanda agregada** (secundaria/primaria, todas EE.UU. o global; ninguna aísla el rol)
- Indeed Hiring Lab (F12 [M]): "US software development job postings have grown by almost 15% since the launch of Claude Code in late February, 2025" (avisos totales -7 %); "71% of the increase ... between May 2025 and May 2026 is from senior roles" y "37% is due to jobs that mention AI in their title". Datos de avisos de EE.UU. en Indeed, desestacionalizados, hasta junio 2026.
- Dice (F13 [S], informe de julio 2026): avisos con "AI" en el título +173 % interanual en el 1T 2026, mientras los de desarrollo de software cayeron 22 %. Es el mismo tipo de ruido que las otras: "AI" en el título incluye AI engineer, no solo mi rol.
- LinkedIn Economic Graph (https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/PDF/us-software-engineer-talent-landscape-2026.pdf, no pude extraer texto, [S] por el buscador): los avisos que piden alfabetización en IA crecieron "más de 70 %" interanual; el crecimiento más rápido está en títulos de IA.

**Títulos usados en avisos (todos [S] salvo indicación)**
- "Developer Experience Engineer" (varios, FlexJobs/Chromatic/PayNearMe), "Developer Productivity Engineer" (Dice), "Principal Software Engineer, Developer Experience" (FlexJobs), "Senior AI Platform / Developer Experience" (Nortal, LatAm remoto; el cuerpo no se pudo ver), "AI Solutions & Enablement Engineer" (South Geeks), "Forward Deployed AI Engineer" (Devsu, LatAm remoto), "Forward Deployed Engineer" y "Senior Site Reliability Engineer" en la misma consultora con base en LatAm (listado visto en WebFetch, 29 vacantes en total, de las cuales 2 dicen AI Engineer, 1 Forward Deployed y 2 SRE; fecha del listado no visible).
- No busqué ni encontré avisos con "agentic SDLC" ni "engineering effectiveness" en esta ronda. Hueco.

**Cantidad**: no obtuve conteos de avisos por título (ni abiertos a remoto/LatAm). Los sitios de avisos (LinkedIn, Indeed, Levels.fyi jobs) no se pueden consultar con estas herramientas. Hueco principal de P3. La única señal de escala es que los avisos "de desarrollo de software" en EE.UU. rebotaron ~15 % y que el 37 % de ese aumento menciona IA en el título.

**Pago (USD salvo indicación; avisos y estimaciones, todos [S] salvo F15)**
- Developer Experience Engineer, EE.UU.: promedio $127.901 por año (ZipRecruiter, estimación de agosto 2026, https://www.ziprecruiter.com/Salaries/Developer-Experience-Engineer-Salary). Bruto/neto y n no informados.
- Avisos con rango, remotos: Chromatic $175k-$194k por año + equity (junio 2026, remoto América del Norte y Europa, https://jobs.designerfund.com/companies/chromatic-2/jobs/83687180-developer-experience-engineer); Principal SWE DevEx $186k-$210k (https://www.flexjobs.com/publicjobs/principal-software-engineer-developer-experience-2054694); otro DevEx $130k-$170k; otro $149k-$350k (banda muy ancha). Dice "Developer Productivity Engineer": $180.000-$400.000 por año, "remote-first" (la URL dio 410; solo vi el rango en el buscador, y el techo parece de banda multi-ubicación). Todos son rango declarado del aviso (en general base anual bruta, no siempre dicho; equity aparte). No verifiqué la elegibilidad desde Argentina de ninguno.
- Remoto LatAm: Enumerate, Tech Lead de IA como contractor, $3.300-$4.000 por mes (https://job-boards.greenhouse.io/enumerate/jobs/4205025009), cifra que cae muy por debajo de los rangos de EE.UU. anteriores y es la única cifra con alcance LatAm que obtuve.
- DevOps Engineer, EE.UU., Levels.fyi (F14 [S], noviembre 2026): mediana de compensación total $153.000, percentiles 25 y 75 $120K y $189K, más de 200 salarios; autoselección. Otras cifras de base: Payscale (Platform Developer/Engineer) $152.605 (2026) y 1.000 avisos con mediana base $182.000 (Recruiting From Scratch, https://www.recruitingfromscratch.com/blog/devops-platform-engineer-salary-in-2026-real-data-from-1-9-million-job-postings, [S]). Las fuentes difieren entre sí por definición (base vs total); no las promedié.
- Argentina local (F15 [M], sysarmy 2026.1, relevamiento dic 2025 a feb 2026, cálculo de Coderhouse sobre datos abiertos): DevOps/SRE/SysAdmin en CABA, mediana **$3.480.000 ARS bruto por mes**, n=241, full-time; rango intercuartil $2.400.000 a $5.108.000; senior $3.803.000 (n=168). No tengo conversión a USD verificada (hueco). Ojo: mide solo CABA y empleados full-time; no hay corte por IA/plataforma.
- Remuneración remota general de desarrollo: mediana de aviso $160.000 por año sobre 7.644 avisos remotos en 12 meses (Working Nomads, noviembre 2026, https://www.workingnomads.com/salaries/development [S]).

**Qué piden** (de los avisos vistos solo por buscador): experiencia con IA aplicada en producción (Devsu: "shipping production AI/ML systems, including generative or agentic AI"), inglés en entorno profesional (Enumerate), 2+ años con IA generativa (Workana). No tengo texto leído de un aviso de "developer productivity" para decir qué piden de plataforma/CI. Hueco.

### P4. Posición contraria

1. **El efecto neto es chico o nulo según quién mida.** Faros (F9): sin correlación significativa a nivel de empresa; METR 2025 (F6): +19 % más lento, y la réplica 2026 no resolvió el signo con certeza (F7). Stack Overflow 2025 (F19 [S]): 80 % usa IA pero la desconfianza sube (el buscador dio 46 % que no confía en la exactitud, vs 31 % el año anterior; otra salida cita 33 % que sí confía; cifras discrepantes, no resueltas).
2. **Resultado empresarial nulo en pilotos.** MIT NANDA 2025 (F18 [S]): "95 percent of enterprise organizations have gotten zero return"; muestra pequeña (52 entrevistas, 300 iniciativas públicas, 153 encuestados según The Register) y la iniciativa tiene intereses (construye protocolos de agentes). S&P Global citado: 42 % de pilotos abandonados. Evidencia débil pero citada.
3. **Lo absorben los equipos existentes.** DORA 2025 (F2): "90% of organizations have adopted at least one platform" y el buscador dijo 76 % con equipos dedicados ([S], sin fuente única). La capacidad ya existe adentro; el trabajo de "preparar la plataforma para IA" es la misma agenda de plataforma de siempre (DORA lo encuadra como "Invest in your internal platform"). No encontré fuentes que digan explícitamente que un equipo de plataforma absorbió a uno de IA (la búsqueda no lo mostró); es inferencia, no hallazgo.
4. **Los vendedores hacen el trabajo.** Los hallazgos fuertes vienen de vendedores (Faros, Perforce/Puppet, PagerDuty, Rootly), que empaquetan la medición y la plataforma como producto; Accenture (F17 [S]) afirma entregas 60-75 % más rápidas en entornos "AI-native", cifra de vendedor sin metodología.
5. **Remediación autónoma inmadura**: 31 % autónomo y pronóstico de interrupciones por agentes (Gartner, [S]).
6. **El mercado crece sobre todo en senior y en títulos de IA** (Indeed: 71 % del aumento es senior y 37 % menciona IA en el título): señal a favor de la persona con experiencia, pero también de que el título buscado es "AI engineer", no "plataforma de desarrollo con IA".

### P5. Lo comercial (sin profundizar; todo [S])

- Alpha-Sense: "AI is now the biggest driver of consulting demand" (secundaria, sin metodología vista, https://www.alpha-sense.com/blog/trends/consulting-industry-trends/).
- Allianz Trade: el mercado global de consultoría y servicios de TI creció ~3,6 % en 2025, ritmo similar esperado en 2026, con presión de precios y renegociaciones por la ejecución con IA (F17). O sea demanda de servicios sobre IA, pero margen y volumen general bajo presión.
- Accenture sumó casi 40.000 profesionales de IA y datos en dos años (vía MarketScale/Business Insider, secundaria). Grandes y las consultoras indias compiten con plataformas propias (Everest Group). Competencia dura para una consultoría chica.
- No encontré evidencia de demanda específica de consultoría sobre adopción de IA en equipos de ingeniería ni de tarifas. Hueco.

## 3. Tabla resumen (rol × evidencia)

| Pieza de la tesis | Evidencia | Fuerza | Fecha |
|---|---|---|---|
| La IA sola mejora la entrega | Mixta: +26 % tareas (Cui), +21 % tareas pero sin efecto a nivel empresa (Faros), -19 % (METR 2025), METR 2026 inconcluso, DORA 2025 throughput positivo y estabilidad negativa | Media-baja, sin consenso | 2024-2026 |
| La plataforma interna amplifica el efecto de la IA | DORA 2025 (correlación y modelo), Perforce/Puppet 2026 (autoinforme) | Media (sin diseño causal) | 2025-09, 2026 |
| Hace falta rediseñar flujo/CI-CD (lotes chicos, rollback, revisión) | DORA 2025 capacidades 4 y 5; Faros: PR +154 %, revisión +91 % | Media | 2025 |
| Sistemas que se corrigen solos | Pronósticos de Gartner (secundarios), 31 % autónomos, resultados solo de vendedores | Baja | 2026 |
| Hay avisos con este título y pago | Avisos DevEx/DPE EE.UU. remotos $130k-$210k (rango típico), LatAm contractor $3.3k-$4k/mes, Argentina local ARS 3,48 M bruto mensual (DevOps/SRE, CABA) | Baja (no hay conteos) | 2026 |
| Demanda general acompaña | Indeed: avisos de software +15 % desde feb 2025, 37 % del aumento con IA en título | Media (EE.UU., no el rol) | 2026-06 |
| Demanda de consultoría | Comentarios generales | Baja | 2026 |

Rol × mercado (solo lo hallado; ninguna celda está probada con conteos):

| Rol | Argentina local | Nearshore/marketplace | Remoto EE.UU. | Remoto Europa | Entidad extranjera en AR |
|---|---|---|---|---|---|
| Platform/DevOps/SRE clásico | sysarmy 2026.1: mediana ARS 3,48 M bruto/mes (CABA, n=241) | listados de consultoras LatAm con SRE remoto | mediana total $153k (Levels.fyi) | sin dato | sin dato |
| Developer experience / productivity | sin dato | Nortal "AI Platform / DevEx" LatAm remoto | avisos remotos $130k-$210k (algunos de elegibilidad no verificada) | Chromatic: norteamérica y Europa | sin dato |
| AI enablement / forward-deployed | sin dato | Devsu, Enumerate ($3,3k-$4k/mes contractor), South Geeks | sin dato | sin dato | sin dato |
| Agentic SDLC / engineering effectiveness | sin dato | sin dato | sin dato | sin dato | sin dato |

## 4. Huecos

1. Conteos de avisos por título (y abiertos a remoto/LatAm): imposible con estas herramientas; hay que consultar LinkedIn, Indeed, Levels.fyi jobs o Get on Board a mano.
2. DORA 2025: no leí el PDF (excede 10 MB); faltan el tamaño del efecto de la plataforma como moderador, el modelo estadístico y las cifras de throughput/estabilidad de 2025. Tampoco verifiqué las cifras de plataforma 2024 contra el PDF.
3. Cui et al. y el Faros del buscador: la página de INFORMS dio 403; los números vienen de MIT Sloan y del buscador.
4. METR: no hay réplica limpia en 2026 (el propio METR lo dice).
5. Auto-remediación: ningún estudio independiente con resultados medidos; solo pronósticos y vendedores.
6. Argentina: sin cifra en USD ni corte por rol de IA; sysarmy original no leído (solo el cálculo de Coderhouse sobre sus datos abiertos); no vi la metodología de sysarmy/openqube.
7. Elegibilidad real desde Argentina de los avisos de EE.UU. con rango (zona horaria, cobro como contractor): sin verificar; tema legal/fiscal no tocado.
8. Consultoría: sin evidencia de demanda y tarifas para consultoría de adopción de IA en ingeniería.
9. Títulos "agentic SDLC" y "engineering effectiveness": no investigados a fondo (se acabaron las rondas).
