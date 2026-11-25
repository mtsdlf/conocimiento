---
resumen: >-
  El CV es el documento de una o dos páginas que resume, para un puesto, la parte del material que
  prueba que uno puede hacerlo. Lo lee primero un sistema que extrae sus datos y después una persona
  que decide si seguir.
estado: borrador
estabilidad: semi
fuentes:
  - "Harvard OCS, guía de CV: https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/"
  - "MIT CAPD, guía de CV: https://capd.mit.edu/resources/resumes/"
  - "Workday, resume parsing: https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html"
  - "Greenhouse, por qué no importó un CV: https://support.greenhouse.io/hc/en-us/articles/200721684-Why-didn-t-the-candidate-s-resume-import-correctly"
  - "Greenhouse, formatos soportados: https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-file-types-for-resumes-and-cover-letters"
  - "Greenhouse, Talent Matching FAQ: https://support.greenhouse.io/hc/en-us/articles/41131886674075-Talent-Matching-FAQ"
  - "Greenhouse, Talent Matching: https://support.greenhouse.io/hc/en-us/articles/41396009937307-Talent-Matching"
  - "Lever, Understanding Resume Parsing (según el buscador): https://help.lever.co/hc/en-us/articles/20087345054749"
  - "ResumeGo 2018 vía CNBC: https://www.cnbc.com/2018/12/19/resumego-hiring-managers-prefer-candidates-with-two-page-resumes.html"
  - "Jobscan, largo: https://www.jobscan.co/blog/page-length-is-not-what-recruiters-say-they-prefer/"
  - "Fortune (2024), texto oculto: https://fortune.com/2024/12/05/job-applicants-white-font-hack-hr-applications/"
  - "HR Dive sobre el informe Greenhouse 2026: https://www.hrdive.com/news/job-candidates-ai-usage-is-obscuring-their-viability-report-finds/875232/"
  - "Presentacion-profesional/.investigacion/vidrieras.md"
  - "Presentacion-profesional/.investigacion/contraria.md"
aliases: [currículum, curriculum vitae, résumé, hoja de vida, ATS, largo del CV]
creado: 2026-11-24
revisado:
---

# CV

El CV es el documento de una o dos páginas que resume, para un puesto, la parte del material que
prueba que uno puede hacerlo. Lo lee primero un sistema que extrae sus datos y después una persona
que decide si seguir.

Es la única [vidriera](vidrieras.md) que se rehace para cada búsqueda: sale del
[inventario profesional](../Material/inventario-profesional.md) según
[adaptar por puesto](adaptar-por-puesto.md), y la [plantilla de CV](plantilla-de-cv.md) da su
esqueleto. Quién lo lee y cuánto tiempo le dedica está en
[quién lee un CV](../Seleccion/quien-lee-un-cv.md).

## Un formato estándar, ordenado por importancia

Las dos guías universitarias leídas coinciden en lo básico: formato estándar y consistente,
contacto completo, sin foto, sin datos personales protegidos y sin referencias. Harvard pide los
encabezados «in order of importance» y, dentro de cada uno, orden cronológico inverso. MIT recuerda
que los reclutadores «appreciate familiar formats» y recomienda empezar de una página en blanco,
porque las plantillas se vuelven difíciles de editar.

La legibilidad tiene reglas concretas en MIT: «Use a conservative font no smaller than 10pt» y
márgenes de al menos media pulgada. Harvard pide balancear el espacio en blanco y que el formato
«translate properly if converted to a .pdf». Las dos guías están pensadas para estudiantes y
graduados de EE.UU., no para perfiles senior de tecnología.

## Una página o dos: solo hay estudios de vendedores

El largo no tiene ningún estudio revisado por pares. MIT dice «Stick to one page, unless you have
extensive experience or an advanced degree»; Harvard no fija largo para el CV, solo para la carta.

> [!IMPORTANT]
> Los dos datos que circulan son de vendedores de servicios de CV, sin revisión de pares, y apuntan
> en sentidos opuestos.
> - ResumeGo (2018, según la nota de CNBC): 482 reclutadores y gerentes eligieron CVs de dos
>   páginas 2,3 veces más que de una; 1,4 veces en nivel inicial, 2,6 en nivel medio y 2,9 en
>   gerencial. Leyeron 2 min 24 s una página y 4 min 5 s dos.
> - Jobscan (según un resumen): en nivel inicial, el cuartil de CVs más cortos consiguió
>   entrevistas en 17,9 % de los casos, contra 2,8 % del cuartil más largo. Es observacional y sin
>   método publicado.

Lo que se puede sostener: una página es la regla para quien tiene poca experiencia, y dos es
razonable con experiencia larga. Ningún dato serio dice que el largo, por sí solo, decida. La
regla «una página siempre» figura entre los [mitos del CV](../Fundamentos/mitos-del-cv.md).

## Qué hace un ATS con el archivo: parsear, no rechazar

Un ATS (applicant tracking system) extrae los campos del CV al perfil del candidato: nombre,
contacto, historial. La documentación oficial de Workday y Greenhouse (y la de Lever, según un
buscador) habla de ese parseo, no de rechazar CVs por su formato.

- Workday: «Resume parsing results can vary based on resume format and order of words» y «For best
  results, use resumes that don't have images or image-based styles».
- Greenhouse: un CV puede no importarse bien si tiene poca información, un tipo de archivo no
  estándar, caracteres que el parser no reconoce o imágenes enlazadas desde afuera. Si falla, el
  reclutador carga los datos a mano.
- Greenhouse Talent Matching compara los términos del CV con las habilidades que fijó el empleador,
  pero «does not auto-reject or auto-advance any candidate»; un CV que no puede analizar queda en
  «Needs manual review».
- Lever, según lo que citó un buscador (la página no cargó): si el parser falla, se carga a mano.

El riesgo documentado es perder datos, no quedar afuera por el formato. Por eso conviene texto
plano, sin imágenes ni gráficos que contengan información, y con los títulos de sección comunes.

> [!IMPORTANT]
> Que el software no rechace solo no quiere decir que no haya filtro. Los empleadores configuran
> reglas de rechazo con preguntas de filtro de la postulación, y usan sus sistemas para filtrar o
> rankear. Esa parte vive en [quién lee un CV](../Seleccion/quien-lee-un-cv.md), y la cifra del
> «75 % rechazado por el ATS» en los [mitos del CV](../Fundamentos/mitos-del-cv.md).

> [!NOTE]
> Sin fuente todavía: que las tablas, las columnas o los encabezados y pies de página rompan el
> parseo. Lo dicen muchos blogs, pero la documentación oficial leída no los nombra.

## PDF o Word: los dos se aceptan

Greenhouse acepta .doc, .docx, .pdf, .rtf y .txt, hasta 100 MB; Lever, según el buscador, acepta
Word, PDF y RTF hasta 10 MB. Ninguna documentación oficial leída dice que uno parsee mejor que el
otro: Workday y Greenhouse hablan de imágenes y caracteres, no del tipo de archivo. Si el aviso pide
un formato, se manda ese; si no, un PDF generado desde texto (no escaneado) cumple con lo que pide
Harvard.

## El texto oculto no funciona

Esconder palabras clave en blanco sobre blanco es un truco conocido y detectado: los empleadores
dicen verlo y descartar a quien lo usa. Las cifras, que son declaraciones de empresas y no
estudios, están en
[mitos del CV](../Fundamentos/mitos-del-cv.md#el-texto-blanco-lo-detectan-no-lo-premian).
