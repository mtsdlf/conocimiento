# Investigación: Vidrieras (cv, cv-por-pais, adaptar-por-puesto, linkedin, portfolio-y-github)

Fecha de la investigación: 2026-11-24. Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).

Nota sobre las marcas: WebFetch devuelve el texto pasado por un modelo chico, no la página cruda. Marqué [L] cuando la página se leyó y se citó literal; las citas son fragmentos cortos.

## Observaciones sobre el árbol

- La división en cinco componentes coincide con cómo se parte el campo, con tres salvedades.
- `adaptar-por-puesto`: no encontré ningún experimento aleatorizado que compare CV adaptado vs. genérico. La nota va a ser sobre mecánica y sentido común de práctica, y hay que decir que la evidencia causal falta. No inventar un porcentaje.
- `cv-por-pais` mezcla tres cosas que el campo trata por separado: la ley (qué se puede pedir), la costumbre (qué se espera) y el efecto empírico (qué pasa si lo ponés). Conviene ordenar la nota en ese orden.
- `portfolio-y-github`: la evidencia de que pesa en la selección es cualitativa y chica (13 entrevistas). No hay estudio de resultados de contratación. Está bien como nota, pero tiene que decir esto arriba.

---

## 1. cv (estructura, largo, legibilidad, ATS, PDF vs. Word)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Harvard OCS, guía de CV | https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/ | primaria (guía universitaria) | 3/2/2/1 | [L] |
| MIT CAPD, guía de CV | https://capd.mit.edu/resources/resumes/ | primaria (guía universitaria) | 3/2/2/1 | [L] |
| Workday, guía de administración (resume parsing) | https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html | primaria (doc oficial de ATS) | 3/1/1/3 | [L] |
| Greenhouse, por qué no importó un CV | https://support.greenhouse.io/hc/en-us/articles/200721684-Why-didn-t-the-candidate-s-resume-import-correctly | primaria (doc oficial de ATS) | 3/1/1/3 | [L] |
| Greenhouse, formatos soportados | https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-file-types-for-resumes-and-cover-letters | primaria | 3/1/1/2 | [L] |
| Greenhouse, Talent Matching FAQ | https://support.greenhouse.io/hc/en-us/articles/41131886674075-Talent-Matching-FAQ | primaria | 3/2/1/3 | [L] |
| Greenhouse, Talent Matching | https://support.greenhouse.io/hc/en-us/articles/41396009937307-Talent-Matching | primaria | 3/2/1/2 | [L] |
| Lever, Understanding Resume Parsing | https://help.lever.co/hc/en-us/articles/20087345054749 | primaria | 3/1/1/2 | [S] (la página no cargó dos veces; lo que sé viene del buscador, que cita el artículo) |
| ResumeGo 2018, largo (482 reclutadores) | https://www.cnbc.com/2018/12/19/resumego-hiring-managers-prefer-candidates-with-two-page-resumes.html | secundaria sobre estudio de vendedor | 1/1/1/1 | [S] |
| Jobscan, contra-dato sobre largo | https://www.jobscan.co/blog/page-length-is-not-what-recruiters-say-they-prefer/ | vendedor | 1/1/1/1 | [S] |

### Afirmaciones

**Harvard OCS** (https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/) [L]:
- No fija un largo para el CV. Solo fija largo para la carta ("no more than a single page").
- Los encabezados van "in order of importance"; dentro de cada uno, orden cronológico inverso.
- Pide formato consistente, fácil de leer, balanceando el espacio en blanco, y que "your formatting will translate properly if converted to a .pdf".
- No incluir foto ("Include a picture" figura entre lo que no hay que hacer) ni edad ni género.
- No habla de ATS por nombre ni de columnas.

**MIT CAPD** (https://capd.mit.edu/resources/resumes/) [L]:
- "Stick to one page, unless you have extensive experience or an advanced degree."
- "Pick a standard and consistent format"; los reclutadores "appreciate familiar formats". Recomienda empezar de una página en blanco porque las plantillas se vuelven difíciles de editar.
- "Use a conservative font no smaller than 10pt" y márgenes de al menos media pulgada.
- "Employers may use keyword scanning on resumes": incluir los términos del puesto. Enlaza una guía "ATS-friendly" cuyo contenido no leí.
- "Photos are generally not preferred for U.S. resumes." "Don't include personal information about your age, religion, health or marital status."
- No dice orden de secciones.

**Lo que ambas coinciden**: formato estándar y consistente, sin foto ni datos personales protegidos, contacto completo, sin referencias. Discrepan en el largo solo por omisión: MIT dice una página salvo experiencia extensa o posgrado; Harvard no dice nada. Ojo: son guías pensadas para estudiantes y graduados de EE.UU., no para perfiles senior en tecnología.

**ATS: lo que dice la documentación oficial (no los blogs)**
- Workday: "Resume parsing results can vary based on resume format and order of words." y "For best results, use resumes that don't have images or image-based styles." No rellena automáticamente campos ocultos ni Languages ni Skills (https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html) [L].
- Greenhouse: un CV puede no importarse bien porque "doesn't have enough information", es de tipo no estándar, tiene caracteres que el parser no reconoce, o tiene imágenes enlazadas externamente (no las carga al hacer la vista previa en PDF; "Images embedded directly in the resume file are unaffected") (https://support.greenhouse.io/hc/en-us/articles/200721684-Why-didn-t-the-candidate-s-resume-import-correctly) [L]. Si falla, el reclutador lo carga a mano; el artículo no habla de rechazo.
- Greenhouse acepta .doc, .docx, .pdf, .rtf, .txt, hasta 100 MB (https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-file-types-for-resumes-and-cover-letters) [L]. Un buscador citó un límite de 2,5 MB para el parseo [S]; no lo verifiqué en la página.
- Greenhouse Talent Matching: "does not auto-reject or auto-advance any candidate"; compara términos del CV con las habilidades calibradas por el empleador, además de experiencia y títulos; si no puede analizar un CV, queda en "Needs manual review" (https://support.greenhouse.io/hc/en-us/articles/41131886674075-Talent-Matching-FAQ) [L]. Y: "Talent Matching is assistive AI, not automated-decision-making" (https://support.greenhouse.io/hc/en-us/articles/41396009937307-Talent-Matching) [L].
- Lever (vía buscador): el parser llena el perfil (nombre, historial, contacto) y si falla se carga a mano; máximo 10 MB; acepta Word, PDF, RTF [S] (https://help.lever.co/hc/en-us/articles/20087345054749).
- Lectura conjunta: la documentación oficial habla de parseo (extraer campos al perfil), no de rechazo. Lo que sí documentan como riesgo es que se pierdan datos por imágenes, caracteres raros o formatos atípicos. Que algún empleador configure auto-rechazo por preguntas de filtro es otra cosa y depende de él (ver Hidden Workers HBS en el brief). Tablas, columnas y encabezados/pies: la documentación oficial que leí no los nombra; lo que dicen los blogs sobre ellos no lo pude confirmar en docs de ATS (hueco).

**Largo**
- ResumeGo 2018 (vendedor, no revisado por pares): 482 reclutadores/gerentes eligieron CVs de dos páginas 2,3 veces más que de una; 1,4 veces para nivel inicial, 2,6 medio, 2,9 gerencial; leyeron 2 min 24 s en una página vs. 4 min 5 s en dos [S] (https://www.cnbc.com/2018/12/19/resumego-hiring-managers-prefer-candidates-with-two-page-resumes.html). El brief ya lo marcó como vendedor.
- Contra-dato, también vendedor: Jobscan reporta que en nivel inicial el cuartil de CVs más cortos consigue entrevistas en 17,9 % vs. 2,8 % del más largo [S] (https://www.jobscan.co/blog/page-length-is-not-what-recruiters-say-they-prefer/). Observacional y sin método publicado.
- Dato viejo: encuesta de Accountemps, 47 % dos páginas ideal vs. 46 % una [S] (misma fuente de búsqueda, no verificada).
- No encontré estudio revisado por pares sobre largo. Las dos fuentes serias (Harvard, MIT) dan una página como regla para estudiantes y no hacen del largo un criterio.

**PDF vs. Word**: la única afirmación oficial: Greenhouse acepta ambos; Harvard pide que el formato "translate properly if converted to a .pdf". No encontré doc oficial que diga que uno parsea mejor que otro (hueco). Workday y Greenhouse hablan de imágenes y caracteres, no del formato de archivo.

### Recurso canónico
- Para ATS: la propia documentación de Workday y Greenhouse (los tres artículos de arriba). Fijarse en: qué dicen del parseo (extraer campos) y qué no dicen (rechazo). Son cortos.
- Para estructura: Harvard OCS, la guía completa, y su ejemplo de CV. Fijarse en el orden por importancia y en los ejemplos de viñetas.

---

## 2. cv-por-pais (foto, edad, estado civil, DNI, dirección, idioma)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| EEOC, Prohibited Employment Policies/Practices | https://www.eeoc.gov/prohibited-employment-policiespractices | primaria (organismo) | 3/2/2/3 | [L] |
| Ley 23.592 (texto original 1988), argentina.gob.ar | https://www.argentina.gob.ar/normativa/nacional/20465/texto | primaria (ley) | 3/1/1/3 | [L] (devolvió el texto original) |
| Ruffle y Shtudiner 2015, Management Science 61(8): 1760-1776 | https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2014.1927 y https://econpapers.repec.org/RePEc:inm:ormnsc:v:61:y:2015:i:8:p:1760-1776 | primaria | 3/2/2/3 | [M] (abstract; el sitio de INFORMS dio 403, leí el de EconPapers) |
| López Bóo, Rossi y Urzúa 2013, Economics Letters (IZA DP 6356), Buenos Aires | https://repec.iza.org/dp6356.pdf (resumen vía https://www.povertyactionlab.org/print/pdf/node/1993) | primaria | 3/2/3/3 | [S] (el buscador resumió; no abrí el PDF) |
| Krause, Rinne y Zimmermann 2012, IZA DP 7096 / IZA J. Eur. Labor Studies 1:5 | https://link.springer.com/article/10.1186/2193-9012-1-5 | primaria | 3/2/1/3 | [S] |
| Informe IZA/KOWA, proyecto piloto anonimizado de la ADS (Alemania) | https://docs.iza.org/report_pdfs/iza_report_44.pdf | primaria | 3/2/1/3 | [S] |
| Europass, página de creación de CV | https://europass.europa.eu/en/create-europass-cv | primaria (oficial UE) | 3/1/1/2 | [L] |
| Plantillas/instrucciones Europass antiguas (EEAS) | https://www.eeas.europa.eu/sites/default/files/europass_cv_instructions.pdf | primaria, antigua | 2/1/1/1 | [S] |
| ICO (Reino Unido), selección de personal y protección de datos | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/recruitment-and-selection/ | primaria | 3/1/1/2 | [S] (la guía está en revisión) |
| Acas, recruitment, discriminación | https://www.acas.org.uk/recruitment/follow-discrimination-law | primaria | 3/1/1/1 | [S] |

### Afirmaciones

**EE.UU.**
- EEOC: "Employers should not ask for a photograph of an applicant." "If needed for identification purposes, a photograph may be obtained after an offer of employment is made and accepted." Los datos pedidos "should be limited to those essential for determining if a person is qualified for the job"; y las preguntas que muestran intención discriminatoria "may be used as evidence of an employer's intent to discriminate" (https://www.eeoc.gov/prohibited-employment-policiespractices) [L]. Por eso el empleador estadounidense evita recibir foto; no es que sea ilegal ponerla.
- Harvard y MIT, ya citados: sin foto, sin edad, género, religión, salud ni estado civil.

**Argentina**
- Ley 23.592, art. 1 (texto original de 1988, el que devolvió la página): actos discriminatorios "determinados por motivos tales como raza, religión, nacionalidad, ideología, opinión política o gremial, sexo, posición económica, condición social o caracteres físicos". El "tales como" hace la lista ilustrativa (https://www.argentina.gob.ar/normativa/nacional/20465/texto) [L]. Un buscador indica que la versión vigente, sustituida por la Ley 25.608 (2002), agrega discapacidad y permite pedir que cese el acto y se repare el daño [S]; hay que confirmarlo en la versión consolidada, la página que abrí estaba marcada "TEXTO ORIGINAL".
- La ley no dice nada sobre el CV ni sobre la foto. La conclusión de que pedir foto, edad o estado civil expone al empleador es inferencia mía; no encontré fuente argentina que regule explícitamente el contenido del CV (hueco). La costumbre local de poner foto, edad y estado civil no la pude respaldar con fuente primaria (hueco).
- Protección de datos: Ley 25.326, autoridad AAIP; las opiniones políticas figuran entre los datos sensibles y su tratamiento está prohibido por regla general [S] (https://www.argentina.gob.ar/normativa/nacional/64790/texto, no abierta). La ley está en reforma [S].

**Europa y Reino Unido**
- Europass hoy: en la sección "Polish and fine-tune" aconseja "add a professional photograph of yourself" y dice que uno elige qué información incluir; la página no menciona fecha de nacimiento, nacionalidad ni género (https://europass.europa.eu/en/create-europass-cv) [L].
- Discrepa con las instrucciones antiguas de Europass (2002-2013), según el buscador: foto "if requested (optional)"; fecha de nacimiento, nacionalidad y género marcados opcionales [S] (https://www.eeas.europa.eu/sites/default/files/europass_cv_instructions.pdf). Dar las dos: el estándar europeo actual sugiere foto, el antiguo la daba por opcional.
- Costumbre por país (Austria, Suiza y Dinamarca esperan foto; Reino Unido e Irlanda ninguna) viene de una guía de terceros [S] (https://ep-advisory.com/?p=39053): no está verificada, no usarla como dato firme.
- Alemania: la prensa señala que sigue siendo habitual adjuntar foto, mientras que en EE.UU. y Reino Unido las candidaturas anonimizadas son comunes [S] (https://www.tagesspiegel.de/wirtschaft/anonym-in-die-zukunft-2117131.html). No encontré fuente jurídica (AGG) sobre si la foto es voluntaria (hueco).
- Reino Unido: la Equality Act 2010 regula decisiones de selección, no el formato del CV. No encontré fuente oficial que diga "sin foto"; es práctica [S] (Acas, GOV.UK). La Acas indica separar el formulario de monitoreo de igualdad del CV.
- GDPR/UK GDPR: el ICO dice que el empleador debe recoger "the minimum amount of information that you need" en la selección [S] (https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/recruitment-and-selection/); la guía de reclutamiento está "under review" y su versión final se anunciaba para invierno 2026. Para la UE no encontré guía de una autoridad (EDPB o una DPA nacional) sobre fotos en CVs (hueco).
- Anonimizar solicitudes en Europa: Krause, Rinne y Zimmermann reportan que la anonimización "generally did not change" la chance de entrevista y que la ventaja de las mujeres con solicitudes estándar desapareció con anónimas [S]. Piloto alemán de la ADS (nov 2010-dic 2011): 5 empresas grandes y 3 empleadores públicos, 4.000 solicitudes anonimizadas, 111 puestos; evaluación "no representativa" [S]. No averigüé si el diseño alemán sacaba la foto (la fuente no lo dice).

**Estudios del efecto de la foto**
- Ruffle y Shtudiner 2015, Israel: 5.312 CVs en pares enviados a 2.656 avisos; en cada par uno sin foto y otro con foto de una persona atractiva o común. Cita literal: "Employer callbacks to attractive men are significantly higher than to men with no picture"; "Strikingly, attractive women do not enjoy the same beauty premium". Los callbacks de hombres atractivos son casi el doble que los de hombres comunes; las mujeres sin foto recibieron más llamados que las atractivas o comunes. Explicación propuesta por los autores: celos de las reclutadoras (https://econpapers.repec.org/RePEc:inm:ormnsc:v:61:y:2015:i:8:p:1760-1776) [M].
- López Bóo, Rossi y Urzúa, Buenos Aires, 2010: 2.540 CVs ficticios, seis por aviso (atractivo, no atractivo y sin foto, por género), en sitio de empleo argentino, para puestos de ventas, administrativo, cocina y no calificados. 10,3 % de llamados con foto atractiva vs. 7,6 % con foto no atractiva (36 % más); los atractivos reciben el llamado alrededor de 30 % más rápido; el efecto se concentra en administrativos y atención al cliente. Según el resumen secundario, incluir foto por sí sola no cambió los llamados [S] (https://www.povertyactionlab.org/print/pdf/node/1993). Es el estudio más cercano a Argentina; ojo, son puestos de baja calificación, no tecnología.
- Los dos estudios muestran que la foto abre un canal de sesgo por apariencia. Ninguno es de tecnología ni de trabajo remoto. Ruffle y Shtudiner no son un caso a favor ni en contra de poner foto: el efecto depende del género y de quién lee.

### Recurso canónico
- EEOC, la página citada: es la razón oficial de por qué EE.UU. no recibe foto. Fijarse en la frase sobre fotos y la de "intent to discriminate".
- Ruffle y Shtudiner, el abstract y el diseño. Fijarse en el brazo "sin foto" como comparación.

---

## 3. adaptar-por-puesto

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Wiles, van Inwegen, Munyikwa y Horton, Management Science 2024 (ya relevado) | https://www.nber.org/papers/w30886 | primaria | 3/2/2/3 | [M] (del brief) |
| Greenhouse Talent Matching FAQ (mecánica de comparar términos) | https://support.greenhouse.io/hc/en-us/articles/41131886674075-Talent-Matching-FAQ | primaria | 3/2/1/3 | [L] |
| Revisión de 22skills, "Does Tailoring Your Resume Increase Interview Rates?" | https://www.22skills.com/blog/does-tailoring-your-resume-increase-interview-rates | secundaria, vendedor | 1/1/1/1 | [S] |
| Huntr, tasas por CV personalizado | (citado por el buscador, sin URL propia verificada) | vendedor, observacional | 1/1/1/1 | [S] |

### Afirmaciones
- No encontré ningún experimento (de campo ni de laboratorio) que asigne al azar un CV adaptado vs. uno genérico para el mismo aviso. La revisión de 22skills llega a la misma conclusión: la combinación "adaptar el CV al aviso" no fue aleatorizada [S] (https://www.22skills.com/blog/does-tailoring-your-resume-increase-interview-rates). Es un hueco de evidencia: declararlo.
- Lo más cercano es observacional y de vendedor: Huntr reporta que quienes personalizan convierten 5,75 % de postulaciones en entrevistas u ofertas vs. 2,68 % con CV genérico [S]. Sin control de quién elige personalizar (probablemente los más motivados), no sirve para causalidad.
- Wiles et al.: ayudar al azar a 480.948 postulantes a redactar mejor el CV subió las contrataciones 8 % [S] (https://www.nber.org/papers/w30886; cifras del brief y de un buscador). Mide calidad de redacción, no adaptación.
- Mecánica que sí está documentada: un ATS con matching, como Greenhouse Talent Matching, "compares related terms on each resume to the calibrated skills you set" y varios términos pueden valer por una misma habilidad (https://support.greenhouse.io/hc/en-us/articles/41131886674075-Talent-Matching-FAQ) [L]. Eso respalda usar el vocabulario del aviso para las habilidades reales, pero no dice cuánto. MIT: incluir los términos del puesto (https://capd.mit.edu/resources/resumes/) [L].
- Cuánto adaptar: no hay evidencia cuantitativa. Lo que se puede decir con fuente es qué se adapta (términos, orden de lo más relevante: Harvard "in order of importance") y que no hace falta rehacer todo. Cualquier "adaptá un 30 %" sería práctica sin respaldo. Nota de práctica: McDowell y Bock (practicantes, no leídos en esta ronda) hablan de priorizar lo relevante para el puesto; no los verifiqué.

### Recurso canónico
- No hay uno de investigación. Para la mecánica: Greenhouse Talent Matching FAQ, la pregunta sobre qué lee del CV. Para el criterio: Harvard OCS, "in order of importance". Decir en la nota que el resto es práctica.

---

## 4. linkedin

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| LinkedIn Blog (2017-06-21), "Get found via LinkedIn search" | https://www.linkedin.com/blog/member/product/looking-for-your-next-job-opportunity-get-found-via-linkedin-search | primaria (vendedor, datos propios) | 2/1/1/3 | [L] |
| LinkedIn Help, Open to Work | https://www.linkedin.com/help/linkedin/answer/67405 | primaria | 3/1/1/3 | [L] |
| LinkedIn Talent Solutions, Recruiter features | https://business.linkedin.com/hire/recruiter/recruiter-features | primaria (marketing) | 2/1/1/2 | [S] |
| Rajkumar, Saint-Jacques, Bojinov, Brynjolfsson y Aral, Science 377: 1304-1310 (2022), DOI 10.1126/science.abl4476 | https://ide.mit.edu/wp-content/uploads/2022/09/abl4476.pdf?x19295 | primaria | 3/3/2/3 | [L] (abstract y resultados; el PDF se extrajo con pdftotext) |
| Nota de prensa MIT sobre el estudio | https://news.mit.edu/2022/weak-ties-linkedin-employment-0915 | secundaria | 2/1/1/1 | [S] |

### Afirmaciones

**Qué ve y cómo busca un reclutador**
- Recruiter ofrece "40+ advanced filters" (cargos, ubicación, habilidades); el campo de palabras clave acepta Booleanos; el filtro de cargos se basa en los cargos de la sección Experiencia [S] (https://business.linkedin.com/hire/recruiter/recruiter-features; documento antiguo 2016-2019, posiblemente desactualizado). Hay un filtro "Open to work" y una búsqueda asistida por IA que interpreta una descripción de puesto [S]. No encontré documentación oficial vigente de cómo se ordenan los resultados (hueco).
- Datos de LinkedIn de 2017 (propios, sin método): "Members with a profile photo receive up to 21x more profile views and 9x more connection requests"; "Members with more than 5 skills are 27x more likely to be discovered in searches by recruiters"; "Including the city where you are based makes you stand out up to 23x in searches" (https://www.linkedin.com/blog/member/product/looking-for-your-next-job-opportunity-get-found-via-linkedin-search) [L]. Son correlaciones de la plataforma, de hace casi 10 años. El "36x más mensajes" que circula no lo encontré en LinkedIn [S].
- Open to Work: tres opciones de visibilidad (todos los miembros, con el marco #OpenToWork; "Recruiters only"; solo vos). Con "Recruiters only", LinkedIn dice que intenta ocultarlo a reclutadores de tu empresa actual pero "we can't guarantee complete privacy". Poner tipos de puesto y ubicación puede hacer que aparezcas en búsquedas de reclutadores. La página no da estadísticas (https://www.linkedin.com/help/linkedin/answer/67405) [L]. No encontré estudio revisado por pares ni de LinkedIn sobre si el marco visible ayuda o perjudica.
- "Perfiles completos": no hallé evidencia causal. Solo los multiplicadores de 2017 de arriba. Hueco.
- Foto de perfil: además del dato de 2017, el sesgo por apariencia de la sección 2 aplica también a LinkedIn (en LinkedIn la foto casi no se puede evitar). Inferencia mía, sin estudio específico.

**Conexiones débiles (Rajkumar et al. 2022)** [L]
- Diseño: experimentos aleatorios sobre el algoritmo "People You May Know" que variaron la proporción de lazos débiles en las redes de "over 20 million people over a 5-year period, during which 2 billion new ties and 600,000 new jobs were created".
- Resultados literales: la fuerza de los lazos débiles es no lineal, con relación en U invertida entre fuerza del lazo y transmisión de empleo; "Moderately weak ties (measured by mutual connections) and the weakest ties (measured by interaction intensity) created the most job mobility"; y "weak ties increased job mobility in more digital industries, strong ties increased job mobility in less digital industries".
- Implicancia para un perfil de tecnología: los contactos que más ayudan son moderadamente débiles, no los desconocidos totales ni los amigos cercanos. El estudio mide movilidad laboral entre conexiones, no qué tiene que decir el perfil.

### Recurso canónico
- Rajkumar et al. 2022, el abstract y la Figura 3 (relación entre fuerza del lazo y transmisión de empleo). Para el perfil: LinkedIn Help sobre Open to Work (las tres opciones). Aclarar que el multiplicador de 21x es de 2017 y sin método.

---

## 5. portfolio-y-github

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Marlow y Dabbish, CSCW 2013, pp. 145-156 | https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf | primaria | 3/3/3/3 | [L] (texto extraído con pdftotext) |
| Abou El-Komboz y Goldbeck, ifo Working Paper 405 (2024) | https://ifo.de/publikationen/2024/working-paper/career-concerns-public-good-role-signaling-open-source-software-0 | primaria (borrador) | 3/2/1/2 | [S] |
| Stack Overflow Developer Survey 2024 | https://survey.stackoverflow.co/2024/ | primaria (encuesta) | 2/1/1/1 | [S] |

### Afirmaciones
- Marlow y Dabbish: cuestionario con 128 respuestas, 65 voluntarios para entrevista; entrevistaron a siete empleadores que usaban GitHub para evaluar candidatos y seis candidatos que lo usaban para sus postulaciones (13 entrevistas semiestructuradas). Abstract: los indicios del perfil "were seen as more reliable indicators of technical abilities and motivation than information provided on a resume, because of the transparency of work actions on GitHub and relative difficulty of manipulating behavior traces" (https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf) [L].
- Su tabla de señales: compartir valores de código abierto, aceptación de la comunidad y calidad de las contribuciones, iniciativa y gestión de proyectos, y pasión por programar, marcadas como "Reliable"; popularidad del proyecto (watchers, forks), "Unreliable" [L]. O sea: los empleadores desconfían de las estrellas y confían en la historia de commits y de contribuciones aceptadas.
- Limitación declarada por los autores: "Our sample of interviewees was limited to a small subset of people who volunteered to discuss the topic of GitHub and hiring"; no se mide si la impresión predice desempeño [L]. Los entrevistados ya usaban GitHub, hay sesgo de selección. Es de 2013.
- Abou El-Komboz y Goldbeck (2024): unos 22.900 desarrolladores; con diferencias en diferencias comparan a quienes cambian de trabajo con quienes se mudan por otra razón y reportan que las preocupaciones de carrera motivan las contribuciones [S]. Esto es sobre por qué la gente contribuye, no sobre qué pesa para el que contrata.
- Stack Overflow Developer Survey 2024: no encontré en lo que vi preguntas sobre cómo evalúan los que contratan a portfolios o GitHub; trata de aprendizaje y trabajo [S]. Hueco: no hay encuesta seria que cuantifique cuántos empleadores miran GitHub.
- No encontré estudio con resultados de contratación (comparar tasas de entrevista con y sin GitHub). Un posteo de DEV Community afirma "3,7x" con un "blind study" que no pude rastrear: descartado.
- Qué tiene que tener un proyecto: no hay estudio que lo pruebe. Lo que respalda Marlow y Dabbish es que sirve lo que es verificable y muestra trabajo real y sostenido (commits, contribuciones aceptadas por otros, iniciativa), y no lo que es popularidad. Todo lo demás (README, demo, tests) es práctica de reclutadores técnicos que no leí en esta ronda.

### Recurso canónico
- Marlow y Dabbish 2013, la tabla de señales y la sección de limitaciones. Es el único trabajo primario sobre el tema y hay que leerlo con su n de 13.

---

## Huecos

- Adaptar vs. genérico: sin experimento aleatorizado. Hay solo observacional de vendedores.
- Largo del CV: sin estudio revisado por pares; solo ResumeGo (vendedor) y un contra-dato de Jobscan (vendedor, observacional). Harvard no fija largo; MIT dice una página salvo experiencia extensa.
- ATS: la documentación oficial de Workday, Greenhouse y Lever que leí no habla de tablas, columnas ni encabezados; no pude verificar esas afirmaciones de blogs. Lever solo por buscador. Falta confirmar el límite de 2,5 MB de Greenhouse. No se encontró doc oficial sobre PDF vs. Word. Taleo/Ashby/Workable no revisados.
- Argentina: sin fuente que regule el contenido del CV ni que documente la costumbre local de foto, edad y estado civil. Ley 23.592: leí el texto original de 1988; falta confirmar el consolidado con Ley 25.608. Ley 25.326: solo por buscador.
- Europa: costumbre por país sin fuente primaria; sin fuente jurídica sobre foto en Alemania (AGG) ni guía de EDPB/DPA sobre CVs; Europass: la página actual sugiere foto y las instrucciones antiguas la daban por opcional.
- Efecto de la foto: ninguno de los estudios hallados es de tecnología ni de remoto; el de Buenos Aires es de puestos de baja calificación y lo leí solo por resumen secundario. No hay estudio que compare Argentina con EE.UU. o Europa para el mismo perfil.
- LinkedIn: sin documentación oficial vigente del orden de los resultados de Recruiter; las cifras de 2017 de LinkedIn son sin método; sin estudio sobre el marco #OpenToWork ni sobre perfil completo.
- GitHub/portfolio: sin estudio de resultados de contratación; sin encuesta seria sobre cuántos empleadores lo miran; Stack Overflow no lo cubre en lo que revisé. No busqué Hann/Roberts/Slaughter ni encuestas de HackerRank (vendedor).
- Practicantes (McDowell, Bock, reclutadores técnicos) no leídos en esta ronda.
