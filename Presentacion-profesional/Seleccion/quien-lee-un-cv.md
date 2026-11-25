---
resumen: >-
  Un CV que entra por una postulación tiene hasta tres lectores: el ATS, que lo guarda, extrae sus
  campos y aplica las reglas del empleador; el recruiter, que filtra; y el hiring manager, que
  decide a quién entrevistar. El software rechaza solo con reglas que escribió el empleador, y
  esas reglas igual dejan afuera a gente calificada.
estado: borrador
estabilidad: semi
fuentes:
  - "Presentacion-profesional/.investigacion/seleccion.md (sección 1)"
  - "Presentacion-profesional/.investigacion/vidrieras.md (sección 1)"
  - "Presentacion-profesional/.investigacion/contraria.md (secciones 1.1 y 3c)"
  - "Greenhouse Support, Application rules overview: https://support.greenhouse.io/hc/en-us/articles/203105595-Application-rules-overview"
  - "Greenhouse, What really happens after you apply for a job: https://my.greenhouse.com/blogs/what-really-happens-after-you-apply-for-a-job"
  - "Greenhouse Support, Talent Matching FAQ: https://support.greenhouse.io/hc/en-us/articles/41131886674075-Talent-Matching-FAQ"
  - "Greenhouse Support, Talent Matching: https://support.greenhouse.io/hc/en-us/articles/41396009937307-Talent-Matching"
  - "Greenhouse Support, Why didn't the candidate's resume import correctly: https://support.greenhouse.io/hc/en-us/articles/200721684-Why-didn-t-the-candidate-s-resume-import-correctly"
  - "Workday, guía de administración, resume parsing: https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html"
  - "Lever Help Center, Searching the database for candidates: https://help.lever.co/hc/en-us/articles/20087317030685-Searching-the-database-for-candidates"
  - "Lever, Applicant tracking system myths debunked: https://www.lever.co/blog/applicant-tracking-system-myths-debunked"
  - "Fuller et al. (2021), Hidden Workers: Untapped Talent, HBS y Accenture: https://pubwww.hbs.edu/managing-the-future-of-work/Documents/research/Hidden%20Workers%20Executive%20Summary.pdf"
  - "Brown y Campion (1994), Journal of Applied Psychology 79, 897-908"
aliases: [ATS, applicant tracking system, sistema de seguimiento de postulantes, recruiter, reclutador, hiring manager, parseo de CV, resume parsing, pregunta filtro, knockout question, auto-reject]
creado: 2026-11-24
revisado:
---

# Quién lee un CV

Un CV que entra por una postulación tiene hasta tres lectores: el ATS, que lo guarda, extrae sus
campos y aplica las reglas del empleador; el recruiter, que filtra; y el hiring manager, que
decide a quién entrevistar. El software rechaza solo con reglas que escribió el empleador, y
esas reglas igual dejan afuera a gente calificada.

| Lector | Qué hace con el CV | Qué fuente lo dice | Firmeza |
|---|---|---|---|
| ATS | Lo guarda, extrae campos (parseo), lo vuelve buscable y aplica reglas de rechazo configuradas | Documentación oficial de Greenhouse, Workday y Lever | Media: vendedores sobre su producto |
| Recruiter | Revisa, filtra y busca en la base con los campos parseados | Greenhouse y Lever; Brown y Campion (1994) | Media |
| Hiring manager | Define requisitos y preguntas filtro; decide a quién entrevistar | Solo menciones en documentación de vendedores | Baja |

## El ATS guarda y busca; rechaza con reglas del empleador

Un ATS (*applicant tracking system*) es el sistema donde caen las postulaciones. Su trabajo
documentado es guardar, extraer los datos del CV al perfil del candidato y permitir buscar y
filtrar. Ninguna documentación oficial leída describe un rechazo automático por el contenido del
CV.

El rechazo automático existe, pero se arma con las respuestas a preguntas de la postulación. En
Greenhouse, «Auto-Reject uses custom application questions to screen and reject candidates based
on their responses»: licencia, ubicación, hasta cinco preguntas combinadas con AND, en los planes
Plus y Pro. Lever llama a lo mismo *knockout questions*, «defined by recruiters and hiring
managers». Según el blog de Greenhouse para candidatos, esas reglas «are set and controlled
directly by recruiters», y «Over 50% of roles are set to send you an email if your application is
auto-rejected».

La función de IA de Greenhouse, Talent Matching, compara los términos del CV con las habilidades
que calibró el empleador, más la experiencia y los títulos. Según su documentación, «does not
auto-reject or auto-advance any candidate» y es «assistive AI, not automated-decision-making».
Cuando no puede analizar un CV, lo deja en «Needs manual review». Que esa comparación ordene la
lista del recruiter aunque no decida es una inferencia de esta nota, no algo que la documentación
diga.

La cifra de que el ATS rechaza el 75 % de los CVs no tiene método publicado; su origen está en
[mitos del CV](../Fundamentos/mitos-del-cv.md).

## Lo que el parseo pierde

Más que el rechazo, el riesgo documentado de un ATS es que el parseo extraiga mal los datos.
Workday advierte que «Resume parsing results can vary based on resume format and order of words»
y recomienda CVs «that don't have images or image-based styles». Greenhouse lista por qué un CV
no se importa bien: poca información, un tipo de archivo no estándar, caracteres que el parser no
reconoce o imágenes enlazadas de afuera. Si falla, el recruiter carga los datos a mano.

El parseo importa porque alimenta la búsqueda. Según la ayuda de Lever (leída solo en el resumen
del buscador), los filtros por empresa, cargo, escuela y años de experiencia salen de datos
parseados, y los años se calculan «from dates parsed from the resume»; del parseo, «no
information is guaranteed». Un CV con fechas o cargos que el parser no entiende aparece menos en
las búsquedas del recruiter. Cómo armar un CV que se parsee bien está en [CV](../Vidrieras/cv.md),
y qué términos usar, en [habilidades y palabras clave](../Material/habilidades-y-palabras-clave.md).

## Los filtros que el empleador sí pone

Que el software no decida solo no quiere decir que no filtre. En la encuesta *Hidden Workers*
(HBS y Accenture, 2021), «more than 90% of employers in our survey use their RMS to initially
filter or rank» candidatos de habilidades medias (94 %) y altas (92 %). Esos sistemas usan
«proxies (such as a college degree or possession of precisely described skills)» y toman «a gap
in full-time employment» como base para excluir. El 88 % de los empleadores acepta que deja afuera
candidatos calificados de habilidades altas por no calzar con el criterio exacto del aviso.

> [!IMPORTANT]
> Greenhouse dice, sobre su producto, que «AI doesn't score or rank applications» y que las
> postulaciones «are reviewed by real people, one by one, in the order received». *Hidden Workers*
> dice que más del 90 % de los empleadores usan su sistema para «filter or rank». No se
> contradicen del todo: la primera es un vendedor hablando de un producto; la segunda, una
> encuesta de percepción sobre la práctica de los empleadores en general, que incluye otros
> sistemas y filtros manuales. *Hidden Workers* no es sobre tecnología en particular, sino sobre
> trabajadores con huecos o sin título.

De ahí sale una regla práctica: lo que excluye a alguien calificado suele ser una regla literal
del aviso (un título, un hueco, una habilidad nombrada de otra forma). Leer el aviso para
detectarlas está en [leer una búsqueda](../Posicionamiento/leer-una-busqueda.md), y cómo contar un
hueco, en [huecos y cambios de carrera](../Material/huecos-y-cambios-de-carrera.md).

## El recruiter infiere atributos, no solo lee

El recruiter deduce del CV los atributos que el puesto pide. Brown y Campion
(1994), con 344 reclutadores de 28 empresas en tres estudios, encontraron que los reclutadores
juzgaban que los datos biográficos reflejan habilidades (lenguaje, matemática) y otros atributos
(interpersonales, liderazgo, motivación). Calificaban más atractivo un CV cuanto más sus datos
reflejaban lo que pedía el puesto. Esta nota se apoya en el resumen del estudio, no en el texto
completo.

Esas inferencias son poco confiables, como muestra
[qué predice la selección](que-predice-la-seleccion.md), pero deciden quién pasa. Quien se postula
controla qué datos pone, no cómo se interpretan.

## Lo que no se sabe de cada lector

No hay un estudio independiente y revisado por pares sobre cuánto tiempo mira un recruiter un CV.
La cifra de los «6 segundos» sale de un estudio de eye-tracking de un vendedor de servicios de
empleo, sin método publicado. Según un resumen periodístico (HR Dive), mide la primera decisión
«encaja o no encaja». Un análisis de una plataforma de entrevistas técnicas, sin revisión de pares,
midió una mediana de 31 segundos por CV. Los detalles de las dos cifras están en
[mitos del CV](../Fundamentos/mitos-del-cv.md).

> [!NOTE]
> Sin fuente todavía: qué mira distinto el hiring manager del recruiter, y en qué orden recorre
> cada uno el CV. Las fuentes relevadas solo dicen que el hiring manager define requisitos y
> preguntas filtro. Tampoco se encontró documentación de Workday sobre ranking, ni evidencia sobre
> cómo ordenan los ATS con IA en uso entre 2024 y 2026.
