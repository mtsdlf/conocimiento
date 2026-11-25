---
resumen: >-
  Lo que se sabía al 2026-11-24 de quién contrata AI engineering y para qué trabajo, contra quién se
  compite por clase de rival, qué perfil consigue el puesto y cuál es la mejor evidencia en contra de
  apostar a esos roles.
estado: borrador
estabilidad: volatil
fuentes:
  - "Presentacion-profesional/.investigacion/mercado-cliente-y-rivales.md"
  - "Presentacion-profesional/.investigacion/mercado-cobro-y-contraria.md"
  - "Northzone, On The Pulse: AI Engineer Hiring (2025-10-13): https://northzone.com/2025/10/13/ai-engineer-hiring/"
  - "Heavybit, So You Want to Be an AI Engineer (2026-02-03): https://heavybit.com/library/article/so-you-want-to-be-an-ai-engineer"
  - "365 Data Science, AI Engineer Job Outlook (2026-04-23): https://365datascience.com/career-advice/career-guides/ai-engineer-job-outlook-2025/"
  - "Ashby, Talent Trends: AI job postings (2026-07-09): https://www.ashbyhq.com/talent-trends-report/reports/ai-job-postings"
  - "The Pragmatic Engineer, Is the FDE role becoming less desirable? (2026-03-26): https://newsletter.pragmaticengineer.com/p/is-the-fde-role-becoming-less-desirable"
  - "Lightcast, AI Pathways (2025-09-20): https://lightcast.io/resources/blog/ai-pathways-profiles"
  - "Andela vía CIO Dive (2026-09-17): https://www.ciodive.com/news/tech-job-market-andela-AI/830591/"
  - "Andela vía HR Dive (2026-09-17): https://www.hrdive.com/news/ai-makes-a-mess-of-the-tech-job-market/830636/"
  - "Menlo Ventures, State of Generative AI in the Enterprise (2025-12-09): https://menlovc.com/perspective/2025-the-state-of-generative-AI-in-the-enterprise/"
  - "a16z, How 100 Enterprise CIOs Are Building and Buying Gen AI (2025-06-10): https://a16z.com/ai-enterprise-2025/"
  - "Amplify Partners, The 2025 AI Engineering Report (2025-06-24): https://amplifypartners.com/blog-posts/the-2025-ai-engineering-report"
  - "Workday, More Candidates, Fewer Matches (2026-10-27): https://www.workday.com/en-us/perspectives/hr/2026/10/ai-hiring-match-problem.html"
  - "Indeed Hiring Lab, AI and Job Postings: From Destruction to Creation? (2026-07-08): https://hiringlab.indeed.com/?p=20708"
  - "Indeed Hiring Lab, AI Is No Longer Just a Tech Occupation Story (2026-07-08): https://hiringlab.indeed.com/?p=20706"
  - "LinkedIn Economic Graph, U.S. Software Engineer Talent Landscape (febrero de 2026): https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/PDF/us-software-engineer-talent-landscape-2026.pdf"
  - "Bain, AI in software engineering: the reliability paradox (2026-10-19): https://www.bain.com/fr/insights/ai-in-software-engineering-the-reliability-paradox/"
  - "Stanford Digital Economy Lab, Canaries in the Coal Mine (rev. agosto de 2026): https://digitaleconomy.stanford.edu/news/canariesaug26/"
aliases: [rivales en AI engineering, quién contrata AI engineers, competencia por puestos de IA, comprar vs. construir IA]
creado: 2026-11-24
revisado:
---

# Cliente y rivales en AI engineering (2026-11)

Lo que se sabía al 2026-11-24 de quién contrata AI engineering y para qué trabajo, contra quién se
compite por clase de rival, qué perfil consigue el puesto y cuál es la mejor evidencia en contra de
apostar a esos roles.

Implementa los pasos de cliente y rivales del
[recorrido para elegir a qué apuntar](recorrido-elegir-a-que-apuntar.md). El mercado (Argentina,
remoto, sueldos y la tabla rol por mercado) está en
[mercado de AI engineering desde Argentina](mercado-de-ai-engineering-desde-argentina.md), y los
roles, en el [caso de los roles de AI engineering](caso-roles-de-ai-engineering.md).

> [!WARNING]
> Datos al 2026-11-24. Re-verificar cada 3 meses (la próxima, antes del 2027-02-24). Ninguna fuente
> de esta ficha es de Argentina: todo es mercado global o de EE.UU., y buena parte viene de fondos de
> inversión, vendedores de datos o de talento.

## Quien contrata paga por llevar LLMs a producción

El criterio que se repite es haber puesto un sistema en producción. Heavybit, sobre 31 avisos de 21
empresas (2026-02-03): «Companies want people who've already shipped LLM applications in
production». Un respondiente de la encuesta de Northzone a su cartera (2025-10-13): «Any AI Engineer
also needs to be a good SWE to get things into production».

Se prefiere ingeniería de software a investigación. Northzone pone primero a los ingenieros de
software generalistas y después a los ML engineers aplicados, porque la empresa puede formar a quien
ya entiende «the product, codebase, and infrastructure». En esa encuesta (n no declarado), 35 % de
quienes contratan pone la infraestructura (inferencia, GPUs, serving a escala) entre las tareas del
AI engineer, contra 90 % que pone prompts y recuperación y 80 % que pone evaluación.

Lo que frena la producción es costo, confiabilidad y observabilidad. Según los CIO de a16z (n=100,
2025-06-10), «Security and cost now weigh more heavily in procurement than accuracy». Una encuesta
de 430 profesionales, vista en el buscador, halla que solo 10 % de las organizaciones había llevado
modelos de fundación a producción, con confiabilidad, costo y latencia como frenos. No hay encuesta
leída que ordene esos frenos con porcentajes.

Formulado como trabajo, por inferencia de la investigación y sin validar con entrevistas: cuando hay
un prototipo con LLM o un cliente que pide IA, quien contrata quiere que llegue a producción
confiable, con costo y latencia controlados, sin armar un equipo de investigación.

## Los rivales por clase

La tipología es la de [identificación de competidores](../../Estrategia-competitiva/Analisis-de-competidores/identificacion-de-competidores.md).
La lista de rivales es de la investigación; solo las cifras tienen fuente.

| Clase | Rival | Evidencia |
|---|---|---|
| Directo | Ingenieros de software que se capacitan en IA | El grupo más contratado según Northzone; Amplify: entre quienes tienen 10+ años de software, 45 % tiene 3 años o menos en IA (el buscador mostró 51 %) |
| Directo | ML engineers aplicados | Segundo grupo contratado según Northzone |
| Directo | DevOps, SRE o plataforma que pivotean | Solo guías de vendedores de formación, vistas en el buscador |
| Directo | Investigadores con PhD | 28 % de los avisos de 365 Data Science pide PhD |
| Directo | Recién graduados | 3 % de los avisos para nuevos graduados (Heavybit); 2,5 % pide 0 a 2 años (365 Data Science) |
| Indirecto | Nearshore y staff augmentation | Venden el mismo resultado con equipo; sin cifra propia |
| Indirecto | Consultoras de IA y equipos de servicios | Forward-deployed descrito como «consulting with a better title» (buscador) |
| Sustituto | Comprar en vez de construir | Menlo (n=495): 76 % de los casos de uso de IA se compran, contra 53 % el año anterior |
| Sustituto | APIs de inferencia y plataformas gestionadas | Sin cifra de cuántas empresas evitan contratar por esto |
| Sustituto | Agentes de código | Un solo testimonio de un CTO citado por a16z |
| No consumo | No contratar o esperar | Workday: 34 % de los gerentes dice que hay puestos sin cubrir por falta de habilidades; 60 días de mediana para cubrir |

En forward-deployed hay menos competencia por el cargo, pero el trabajo se parece más a servicios
que a producto. Un reclutador citado por The Pragmatic Engineer (2026-03-26) estima que solo
«maybe 10 % of the market» quiere el rol; es la estimación de una persona.

Cuántos candidatos compiten por puesto de IA no tiene dato. Lo general es de vendedores: Workday da
69 postulaciones por oferta (oct. 2026), y Ashby, que los avisos con IA en el título se llenan menos
por postulación abierta (37,1 % inbound, 28 % por sourcing).

## El perfil típico de quien consigue el puesto

- **Viene de software**: el grupo más grande en Northzone; los de infraestructura o DevOps son
  «menos comunes», sin cifra.
- **Es su tercer rol**: según Lightcast (2025-09-20), la mayoría de los AI engineers pasó por otros
  dos roles antes; 31 % empezó en roles de IA. Lightcast no describe su método.
- **Tiene años, no títulos de IA**: solo 11 % de las calificaciones de los AI engineers son de IA
  (Lightcast); los avisos apuntan sobre todo a 2 a 6 años (365 Data Science) y son «mostly
  mid-to-senior» (Heavybit).
- **Ya mostró producción**: los avisos piden aplicaciones enviadas a producción y resultados
  cuantificados. Ningún estudio cuenta cuántos contratados tienen open source o publicaciones.

## La posición contraria: la demanda es senior y el título es ruido

> [!IMPORTANT]
> La mejor evidencia en contra de apostar a AI engineering. Ninguna fuente la aplica a quien viene
> de infraestructura con años de experiencia; para ese perfil pesa menos.

- **La suba es de seniors.** Indeed (2026-07-08): las vacantes de software de EE.UU. subieron casi
  15 % desde fines de febrero de 2025 pero siguen 27,5 % abajo de febrero de 2020; el 71 % del
  aumento neto (mayo de 2025 a mayo de 2026) fue en puestos senior.
- **Los juniors no rebotaron, y la causa no es clara.** LinkedIn (febrero de 2026, leída la primera
  parte): «Changes in real interest rates account for most of the variation in SWE hiring» y la
  falta de rebote junior «is not enough to conclude that AI is the cause». Stanford (agosto de 2026,
  vía buscador) halla el empleo de 22 a 25 años en ocupaciones expuestas a IA unos 19 % por debajo
  de lo esperable, sin afirmar causa.
- **El título se infla y mezcla roles.** Indeed: los títulos con IA pasaron de 2,6 % (2022) a
  8,3 % (primer trimestre de 2026), y 63 % está fuera de tecnología. Las menciones de IA en el
  texto del aviso son otra medida, en el
  [caso de los roles](caso-roles-de-ai-engineering.md#la-demanda-con-fecha). Andela, que vende talento: más de la
  mitad de los avisos de AI o ML engineer mezcla habilidades de al menos dos roles.
- **La IA absorbe tareas de infraestructura.** Bain (n=293, 2026-10-19): el monitoreo continuo y
  la optimización automatizada, liderados por IA, pasarían de 24 % a 62 % y las migraciones de
  plataforma de 11 % a 37 %. La misma fuente dice que la IA «can inflate the cost of running it»,
  a favor de quien opera.
- **Comprar reduce los equipos internos**: el 76 % de Menlo es de grandes empresas de EE.UU. y no
  mide inferencia ni serving, que es donde corre un equipo de plataforma.

A favor, en la misma ronda: según LinkedIn, AI engineer es 14 veces más frecuente entre los
contratados que en 2019, aunque las transiciones hacia IA generativa son menos del 1 % de los
cambios de software.

## Huecos

> [!NOTE]
> Sin fuente todavía: postulaciones por aviso en puestos de IA y de DevOps; un ranking con
> porcentajes de los frenos a producción; perfiles de contratados (open source, publicaciones,
> proyectos); posts de hiring managers recogidos con método; cuántas empresas evitan contratar
> plataforma por usar APIs gestionadas; cualquier dato de Argentina o LatAm sobre cliente y rivales.
