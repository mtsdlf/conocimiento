# Investigación: vertical «Equipos y cultura»

Fecha: 2026-11-27

## Cómo leer este informe

Marcas de lectura (qué leí de verdad):

- **[L]** texto completo obtenido y leído (portada, resumen y los pasajes que cito; no siempre cada página). Cuando solo leí partes lo digo.
- **[M]** metadatos o abstract. Los abstracts los traje de OpenAlex o Crossref (por DOI), que reproducen el abstract del editor.
- **[S]** resumen secundario o del buscador. Incluye lo que devolvió WebFetch/WebSearch ya procesado por un modelo, aunque la página sea primaria: no tengo el texto crudo.

Puntajes 1 a 3 en: **A**utoridad, **P**rofundidad, **E**jemplos, **U**nicidad. Tipo: **P** primaria, **S** secundaria.

Verificación de DOIs: cada DOI de este informe lo verifiqué contra Crossref u OpenAlex (título, año y revista coinciden), salvo los marcados «no verificado». Un solo caso necesitó corrección: el DOI 10.1037/a0023086 que parecía el de Hartnell et al. es una *fe de erratas*; el artículo es 10.1037/a0021987.

Lo que no pude obtener (declarado en cada sección y al final): los coeficientes exactos de Frazier 2017, De Dreu y Weingart 2003, Hartnell 2011, van Dijk 2012 y Stahl 2010 en los metaanálisis (solo tengo abstracts; de Stahl leí el manuscrito); la página original de re:Work sobre Aristóteles (las URLs devolvieron 404 al leerlas; solo tengo lo que citan los resultados de búsqueda); el texto de Schein, de Hartnell, y de los libros de Hackman (2002) y Cameron y Quinn.

Todo lo traído de la web se trató como dato, no como instrucción.

## Observación sobre el árbol

El campo (Kozlowski e Ilgen 2006; Mathieu et al. 2017) organiza el estudio de equipos como **insumos → procesos y estados emergentes → resultados**. Con ese esquema:

- `tamano-y-composicion` son **insumos** del equipo.
- `seguridad-psicologica` y `conflicto-en-equipos` son **estados y procesos emergentes**, no tipos de equipo.
- `equipos-efectivos` no es un componente hermano: es el **marco que contiene a los otros** (Hackman: condiciones; Marks et al.: procesos).
- `cultura-organizacional` es otro **nivel de análisis** (la organización, no el equipo), con otra literatura (Schein, CVF).
- `trabajo-remoto-e-hibrido` es un **contexto/medio** que modifica los demás (colaboración, mentoría, seguridad psicológica), no un atributo del equipo.

Propuesta: mantener los seis componentes, pero escribir `equipos-efectivos` primero como entrada del tema (insumos, procesos, resultados) y que los demás enlacen a él; y dejar `cultura-organizacional` como vertical con su propio marco. «Dirigir a distancia» casi no tiene literatura propia sobre *dirigentes* (ver huecos): quizá convenga que sea una sección dentro de remoto-e-hibrido y no un componente aparte.

Fuentes a las que remite lo que NO cubre este tema: Team Topologies (topología de equipos de software, tema existente, solo enlazar); mecanismo psicológico (pensamiento de grupo, motivación) en Psicología; feedback y conversaciones difíciles en Comunicación.

---

## 1. equipos-efectivos

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Hackman (1998), «Why Teams Don't Work», cap. en Tindale et al. (eds.), *Theory and Research on Small Groups*, Plenum | https://doi.org/10.1007/0-306-47144-2_12 (copia: https://harrt.ucla.edu/wp-content/uploads/2015/12/why-teams-dont-work.pdf) | P | 3 | 3 | 3 | 2 | [L] (extraje el PDF completo; leí inicio, el pasaje de las condiciones y el cierre) |
| 1.2 | Hackman y Wageman (2005), «A Theory of Team Coaching», *Academy of Management Review* | https://doi.org/10.5465/amr.2005.16387885 | P | 3 | 3 | 1 | 3 | [M] |
| 1.3 | Hackman (2002), *Leading Teams* (libro) | sin URL abierta verificada; ver resumen en https://umbrex.com/resources/frameworks/organization-frameworks/hackman-five-conditions-for-team-effectiveness/ | P/S | 3 | 3 | 3 | 3 | [S] (solo leí el resumen del buscador, no el libro) |
| 1.4 | Google re:Work, «Understand team effectiveness» (Proyecto Aristóteles) | https://rework.withgoogle.com/en/guides/understanding-team-effectiveness (la leí solo vía fragmentos de búsqueda; las URLs `/guides/understand-team-effectiveness` e `/intl/en/...` respondieron 404 al leerlas) | P | 2 | 1 | 2 | 2 | [S] |
| 1.5 | Woolley, Chabris, Pentland, Hashmi y Malone (2010), *Science* | https://doi.org/10.1126/science.1193147 | P | 3 | 2 | 1 | 3 | [M] |
| 1.6 | Credé y Howardson (2017), comentario a Woolley et al., *Journal of Applied Psychology* | https://doi.org/10.1037/apl0000176 | P | 3 | 2 | 1 | 3 | [M] |
| 1.7 | Riedl, Kim, Gupta, Malone y Woolley (2021), *PNAS* | https://doi.org/10.1073/pnas.2005737118 | P | 3 | 2 | 1 | 3 | [M] |
| 1.8 | «Task structure as a boundary condition for collective intelligence», *Personnel Psychology* (2021) (autores no verificados) | https://doi.org/10.1111/peps.12489 | P | 2 | 2 | 1 | 3 | [M] |
| 1.9 | Marks, Mathieu y Zaccaro (2001), «A temporally based framework and taxonomy of team processes», *Academy of Management Review* | https://doi.org/10.5465/amr.2001.4845785 | P | 3 | 3 | 1 | 3 | [M] (solo título y año) |
| 1.10 | LePine, Piccolo, Jackson, Mathieu y Saul (2008), metaanálisis de procesos de equipo, *Personnel Psychology* | https://doi.org/10.1111/j.1744-6570.2008.00114.x | P | 3 | 3 | 1 | 3 | [M] |
| 1.11 | Salas, DiazGranados, Klein, Burke, Stagl, Goodwin y Halpin (2008), «Does Team Training Improve Team Performance? A Meta-Analysis», *Human Factors* | https://doi.org/10.1518/001872008x375009 | P | 3 | 3 | 1 | 3 | [S] (resultados vía buscador; no abrí el texto) |
| 1.12 | Kozlowski e Ilgen (2006), «Enhancing the Effectiveness of Work Groups and Teams», *Psychological Science in the Public Interest* | https://doi.org/10.1111/j.1529-1006.2006.00030.x | P | 3 | 3 | 2 | 3 | [S] (propósito y marco según resultados de búsqueda; no abrí el texto) |
| 1.13 | Mathieu, Hollenbeck, van Knippenberg e Ilgen (2017), «A century of work teams in the Journal of Applied Psychology» | https://doi.org/10.1037/apl0000128 | P | 3 | 2 | 1 | 2 | [M] (solo metadatos) |

### Afirmaciones con fuente

- Hackman (1998) enumera «six facts» que, si se cumplen, hacen que un equipo «would be likely to perform very well»: tarea apropiada para un equipo; equipo intacto cuyos miembros se perciben como equipo; «a clear, authoritative, and engaging direction»; estructura (tarea, composición y normas) que «promotes rather than impedes competent teamwork»; contexto organizacional que da soporte; y coaching experto disponible «at those times when members most need it and are ready to receive it». [L] https://harrt.ucla.edu/wp-content/uploads/2015/12/why-teams-dont-work.pdf
- La versión de 2002 (*Leading Teams*) se resume habitualmente como cinco condiciones: equipo real, dirección convincente, estructura habilitante, contexto de apoyo, coaching experto. [S] https://umbrex.com/resources/frameworks/organization-frameworks/hackman-five-conditions-for-team-effectiveness/. Esto es una **discrepancia de conteo**: el texto de 1998 que leí lista seis (agrega «la tarea es apropiada para un equipo»); los resúmenes del libro de 2002 hablan de cinco. No pude abrir el libro para ver cómo reagrupa. Dar las dos.
- Hackman distingue coaching según tres momentos de apertura: el inicio (motivacional), el punto medio y el final de un ciclo de desempeño; tres funciones (motivacional, consultiva, educativa). Hackman (1998) dice que es «nearly impossible to coach a team» si la situación de base (estructura, contexto) es mala. [L] https://harrt.ucla.edu/wp-content/uploads/2015/12/why-teams-dont-work.pdf. Hackman y Wageman (2005) formalizan esto: modelo centrado en las funciones del coaching, los momentos en que funciona y las condiciones en que facilita o no el desempeño. [M] https://doi.org/10.5465/amr.2005.16387885
- Woolley et al. (2010): en dos estudios con 699 personas, en grupos de dos a cinco, hay un factor general de inteligencia colectiva que «explains a group's performance on a wide variety of tasks»; no está fuertemente correlacionado con la inteligencia promedio o máxima de los individuos, sí con la sensibilidad social promedio, la equidad en la distribución de turnos de conversación y la proporción de mujeres. [M] https://doi.org/10.1126/science.1193147
- Credé y Howardson (2017) reanalizaron 6 muestras publicadas y concluyen que «the empirical support for the construct is generally weak»: el factor general explica poca varianza en muchas tareas grupales, y dos artefactos (esfuerzo bajo y datos anidados) pueden haber inflado la covariación. «These findings suggest that there is insufficient support for the existence of a collective intelligence construct.» [M] https://doi.org/10.1037/apl0000176
- Riedl et al. (2021) analizaron 22 estudios, 5.279 individuos en 1.356 grupos: «support the conclusion that a robust CI factor characterizes a group's ability to work together across a diverse set of tasks»; la proporción de mujeres lo predice, mediada por la percepción social promedio; «group collaboration process is more important in predicting CI than the skill of individual members». [M] https://doi.org/10.1073/pnas.2005737118
- El estudio de *Personnel Psychology* (2021) comparó 21 estudios experimentales: los grupos muestran inteligencia colectiva en tareas bien estructuradas pero no en tareas mal estructuradas; propone reconceptualizarla como multidimensional. [M] https://doi.org/10.1111/peps.12489
- LePine et al. (2008): los procesos de equipo estrechos cargan en tres dimensiones de orden superior, que cargan en un factor general; hay relaciones positivas con desempeño del equipo y satisfacción; las relaciones son similares entre dimensiones; las dimensiones intermedias se relacionan con cohesión y potencia; la relación con desempeño depende algo de la interdependencia de la tarea y del tamaño. [M] https://doi.org/10.1111/j.1744-6570.2008.00114.x
- Marks et al. (2001) propone la taxonomía de procesos basada en fases temporales (transición, acción, interpersonal). Esa tripartición **la sé de memoria, no la verifiqué en el texto**; el abstract de LePine 2008 confirma solo que Marks et al. proponían «3 higher-order teamwork process dimensions». [M] https://doi.org/10.1111/j.1744-6570.2008.00114.x
- Entrenamiento de equipos (Salas et al. 2008): 93 tamaños de efecto, 2.650 equipos; concluyen que el entrenamiento de equipos es una opción práctica con beneficios en resultados cognitivos, afectivos, procesos y desempeño; contenido, estabilidad de la membresía y tamaño moderan la efectividad. [S] https://stars.library.ucf.edu/scopus2000/9425 (el resumen viene de resultados de búsqueda; no abrí el paper). Hay además una revisión sistemática de entrenamiento de teamwork (PLoS ONE 2017) cuyo existencia verifiqué por metadatos: https://doi.org/10.1371/journal.pone.0169604 [M, título solamente]. Metaanálisis de Delise et al. (2010) aparece como pista sin verificar.
- Proyecto Aristóteles (Google): «the study tested how both team composition (e.g., personality traits, sales skills, demographics on the team) and team dynamics (e.g., what it was like to work with teammates) impact team effectiveness»; los miembros calificaron la cultura del equipo como la medida más importante, los ejecutivos se enfocaron en resultados. Las cinco dinámicas que se citan: seguridad psicológica, confiabilidad (dependability), estructura y claridad, significado e impacto; la seguridad psicológica va primera. Una segunda página de re:Work lista colocación, tamaño del equipo y antigüedad como factores sin asociación significativa con la efectividad, con la salvedad de que «no significa que no importen en otros contextos». [S] (fragmentos de búsqueda de https://rework.withgoogle.com/en/guides/understanding-team-effectiveness; no pude leer la página). El «180 equipos» aparece en prensa (p. ej. https://www.inc.com/marcel-schwantes/google-found-most-successful-teams-share-1-trait.html [S]); **no encontré método publicado**: no hay paper revisado por pares ni tamaños de efecto accesibles. Tratar como estudio de campo interno, de una empresa.

### Estado de la evidencia

- **Se sostuvo**: que los procesos de equipo (planificar, coordinar, monitorear, apoyarse) se asocian con desempeño y satisfacción (LePine et al. 2008, metaanálisis); que el entrenamiento de equipos mejora resultados (Salas 2008, metaanálisis, con la salvedad de que lo leí por resumen).
- **Se achicó**: la inteligencia colectiva como un «factor c» general: replicada en 22 estudios (Riedl 2021) pero acotada a tareas bien estructuradas (2021 *Personnel Psychology*).
- **Cayó o está en disputa**: la existencia del factor c como construcción general (Credé y Howardson 2017 dicen que el apoyo es débil; Riedl 2021 dice que es robusto). Las dos posturas son contemporáneas y no hay una síntesis que las reconcilie del todo; la de 2021 en *Personnel Psychology* es la que más se acerca.
- **Sin prueba comparativa propia**: las condiciones de Hackman son teoría + investigación de campo del autor; no encontré un metaanálisis que pruebe las cinco condiciones como conjunto. La escala TDS (Team Diagnostic Survey, Wageman, Hackman y Lehman 2005) existe: https://doi.org/10.1037/t23765-000 [M].
- **Aristóteles**: hallazgo de una sola empresa, método no publicado en lo que pude ver; coincide con lo que dice la literatura sobre seguridad psicológica, pero no es prueba independiente.

### Recurso canónico

Hackman (1998), «Why Teams Don't Work» (https://harrt.ucla.edu/wp-content/uploads/2015/12/why-teams-dont-work.pdf), por ser corto, abierto y completo: leer las secciones de los errores comunes y las condiciones, y fijarse en que el diseño (estructura y contexto) pesa más que el liderazgo en la marcha. Para la visión de campo de conjunto, Kozlowski e Ilgen (2006), que sigue siendo la revisión de referencia sobre insumos y procesos (no pude confirmar sus conclusiones puntuales; leer entera).

---

## 2. seguridad-psicologica

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 2.1 | Edmondson (1999), «Psychological Safety and Learning Behavior in Work Teams», *Administrative Science Quarterly* | https://doi.org/10.2307/2666999 | P | 3 | 3 | 2 | 3 | [M] |
| 2.2 | Edmondson y Lei (2014), «Psychological Safety: The History, Renaissance, and Future of an Interpersonal Construct», *Annual Review of Organizational Psychology and Organizational Behavior* | https://doi.org/10.1146/annurev-orgpsych-031413-091305 | P | 3 | 3 | 2 | 2 | [M] |
| 2.3 | Frazier, Fainshmidt, Klinger, Pezeshkan y Vracheva (2017), metaanálisis, *Personnel Psychology* | https://doi.org/10.1111/peps.12183 | P | 3 | 3 | 1 | 3 | [M] |
| 2.4 | Newman, Donohue y Eva (2017), «Psychological safety: A systematic review of the literature», *Human Resource Management Review* | https://doi.org/10.1016/j.hrmr.2017.01.001 | P | 3 | 3 | 1 | 2 | [S] (resumen de un agregador, https://explore.psychsafety.com/n/newman-donohue-eva-2017/) |
| 2.5 | Edmondson y Bransby (2023), «Psychological Safety Comes of Age: Observed Themes in an Established Literature», *Annual Review of Organizational Psychology and Organizational Behavior* | https://doi.org/10.1146/annurev-orgpsych-120920-055217 | P | 3 | 3 | 2 | 2 | [M] |
| 2.6 | Edmondson y Kerrissey (2025), nota HBR sobre malentendidos | no verifiqué la URL del editor; mención vía buscador | S | 2 | 1 | 2 | 1 | [S] |

### Afirmaciones con fuente

- Edmondson (1999) introduce el constructo: «a shared belief held by members of a team that the team is safe for interpersonal risk taking». En 51 equipos de trabajo de una empresa manufacturera, la seguridad psicológica se asocia con conducta de aprendizaje, la eficacia del equipo no lo hace al controlar por seguridad psicológica; la conducta de aprendizaje media entre la seguridad psicológica y el desempeño. [M] https://doi.org/10.2307/2666999
- Edmondson y Lei (2014): la seguridad psicológica es «people's perceptions of the consequences of taking interpersonal risks in a particular context such as a workplace»; la revisión sitúa sus orígenes en los años 60 y su «renaissance» desde los 90, y la vincula con voz, trabajo en equipo, aprendizaje de equipo y aprendizaje organizacional. [M] https://doi.org/10.1146/annurev-orgpsych-031413-091305
- Frazier et al. (2017): 136 muestras independientes, más de 22.000 individuos y casi 5.000 grupos; compara la fuerza relativa de los antecedentes; examina si la seguridad psicológica influye en el desempeño de tarea y en las conductas de ciudadanía organizacional «over and beyond» las relaciones positivas con el líder y el engagement; si el diseño de investigación y la cultura nacional cambian las validez; y si los efectos se mantienen entre el nivel individual y el de grupo («homology assumption»). [M] https://doi.org/10.1111/peps.12183. **Los coeficientes no los obtuve**; un resumen secundario dice que está «fuertemente» ligada a compartir información y a aprendizaje [S] (https://www.michigan.gov/documents/mdhhs/Questions-about-Psychological-Safety-Answered_684423_7.pdf), pero no es la fuente primaria. Las fuentes secundarias discrepan sobre el número de estudios (136 muestras en el abstract; 117 estudios en otro resumen): usar el abstract.
- Edmondson y Bransby (2023): cuatro temas dominantes: «getting things done, learning behaviors, improving the work experience, and leadership»; concluye que la seguridad psicológica «plays important roles in enabling organizations to learn and perform in dynamic environments». [M] https://doi.org/10.1146/annurev-orgpsych-120920-055217. La revisión la escriben quienes crearon el constructo; no es una crítica independiente.
- Newman et al. (2017) señalan huecos y problemas de medición; un resumen secundario cita antecedentes consistentes: liderazgo, confianza y diseño de equipo (62 estudios según ese resumen). Superposición con confianza: Edmondson sostiene que no son intercambiables y que la seguridad psicológica se experimenta a nivel grupal; otras revisiones usan los conceptos de forma casi equivalente. [S] https://explore.psychsafety.com/n/newman-donohue-eva-2017/, https://hsph.harvard.edu/news/debunking-misconceptions-about-workplace-psychological-safety/
- «Ser amable»: Edmondson y Kerrissey (2025) argumentan que no es ser amable, ni tener trabajo seguro, ni un intercambio con el desempeño; la definen como «a shared sense of permission for candor». [S] (cita de resultados de búsqueda; no verifiqué la nota).

### Estado de la evidencia

- **Se sostuvo**: la asociación con aprendizaje y desempeño aparece en el estudio original (51 equipos) y en un metaanálisis de 136 muestras; Frazier et al. testean validez incremental sobre liderazgo y engagement, que es la pregunta correcta (pero no obtuve los números).
- **En disputa o por precisar**: causalidad (casi todos los estudios son transversales o de campo; no revisé la proporción experimental), nivel de análisis (la prueba de «homología» entre individuo y grupo está en el metaanálisis; su resultado no lo leí), y solapamiento con confianza y con clima de liderazgo.
- **No hay una réplica independiente en pre-registro** que yo haya encontrado (no la busqué en profundidad).
- **Aristóteles** (ver 1) agregó atención pública y es la fuente de la popularidad, pero no es evidencia independiente.

### Recurso canónico

Edmondson (1999) en lo original; Frazier et al. (2017) para «qué lo predice y qué no»: fijarse en la tabla de antecedentes (con qué fuerza lo predicen la conducta del líder frente a otros) y en la sección de validez incremental. Para una mirada de conjunto, Edmondson y Bransby (2023), sabiendo que es una autorrevisión.

---

## 3. conflicto-en-equipos

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 3.1 | Jehn (1995), «A Multimethod Examination of the Benefits and Detriments of Intragroup Conflict», *Administrative Science Quarterly* | https://doi.org/10.2307/2393638 | P | 3 | 3 | 2 | 3 | [M] (solo título/revista) |
| 3.2 | Jehn y Mannix (2001), «The Dynamic Nature of Conflict», *Academy of Management Journal* | https://doi.org/10.2307/3069453 | P | 3 | 3 | 1 | 2 | [M] (solo título/revista) |
| 3.3 | De Dreu y Weingart (2003), metaanálisis, *Journal of Applied Psychology* | https://doi.org/10.1037/0021-9010.88.4.741 | P | 3 | 3 | 1 | 3 | [M] |
| 3.4 | de Wit, Greer y Jehn (2012), «The paradox of intragroup conflict: A meta-analysis», *Journal of Applied Psychology* | https://doi.org/10.1037/a0024844 | P | 3 | 3 | 1 | 3 | [M] |

### Afirmaciones con fuente

- De Dreu y Weingart (2003): correlaciones «strong and negative» entre conflicto de relación, desempeño de equipo y satisfacción; y, **contra lo que se afirmaba en la literatura académica y en los libros de texto, correlaciones «strong and negative (instead of the predicted positive)» entre conflicto de tarea y desempeño y satisfacción**. El conflicto tuvo relaciones más negativas con el desempeño en tareas complejas (decisión, proyecto, mixtas) que en tareas menos complejas (producción); el conflicto de tarea fue menos negativo cuando estaba débilmente correlacionado con el de relación. [M] https://doi.org/10.1037/0021-9010.88.4.741. (Los valores de ρ no los tengo; los recuerdo de memoria pero no los verifiqué: no citar números.)
- de Wit et al. (2012): 116 estudios, 8.880 grupos; desde 2003 hubo más de 80 estudios nuevos, con relaciones moderadas y un tercer tipo (conflicto de proceso). «Stable negative relationships were found between relationship and process conflict and group outcomes. In contrast to the results of De Dreu and Weingart, we did not find a strong and negative association between task conflict and group performance.» La relación entre conflicto de tarea y desempeño fue más positiva cuando la asociación entre conflicto de tarea y de relación era débil, en equipos de alta dirección (frente a los que no lo son), y cuando el desempeño se medía como desempeño financiero o calidad de decisiones. [M] https://doi.org/10.1037/a0024844
- Jehn (1995), original de la distinción tarea/relación y de la hipótesis de beneficios del conflicto de tarea: no leí el contenido; solo verifiqué que existe. [M]

### Estado de la evidencia

- **Cayó**: la idea sencilla «el conflicto de tarea es bueno y el de relación malo» como regla general. El metaanálisis de 2003 ya no la sostenía, y el de 2012 la matiza de nuevo.
- **Se sostuvo**: el conflicto de relación (y el de proceso) se asocia negativamente con desempeño y satisfacción, de forma estable, en los dos metaanálisis.
- **En disputa/condicionado**: el efecto del conflicto de tarea. Los dos metaanálisis discrepan en la fuerza (2003: fuerte y negativo; 2012: no fuerte), y el segundo lo hace depender de (a) cuánto se mezcle con conflicto de relación, (b) el tipo de equipo (alta dirección), (c) cómo se mide el resultado. Dar las dos fuentes.
- **Para quien dirige**: lo que importa es que el desacuerdo sobre ideas no se convierta en personal; no hay evidencia de que haya que *fomentar* el conflicto.

### Recurso canónico

de Wit, Greer y Jehn (2012), por ser el más reciente y el que discute al anterior: leer el abstract y la sección de moderadores; luego De Dreu y Weingart (2003) para el punto de partida de la disputa.

---

## 4. tamano-y-composicion

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 4.1 | Hackman (1998), cap. «Why Teams Don't Work» (ver 1.1) | https://harrt.ucla.edu/wp-content/uploads/2015/12/why-teams-dont-work.pdf | P | 3 | 3 | 3 | 2 | [L] |
| 4.2 | Staats, Milkman y Fox (2012), «The team scaling fallacy», *OBHDP* | https://doi.org/10.1016/j.obhdp.2012.03.002 | P | 3 | 2 | 2 | 3 | [L] parcial (extraje el PDF; leí resumen e introducción, no los experimentos) |
| 4.3 | Curral, Forrester, Dawson y West (2001), «It's what you do and the way that you do it…», *European Journal of Work and Organizational Psychology* | https://doi.org/10.1080/13594320143000627 | P | 2 | 2 | 1 | 3 | [M] |
| 4.4 | Ingham, Levinger, Graves y Peckham (1974), «The Ringelmann effect», *Journal of Experimental Social Psychology* | https://doi.org/10.1016/0022-1031(74)90033-x | P | 3 | 2 | 1 | 3 | [M] (solo metadatos) |
| 4.5 | van Dijk, van Engen y van Knippenberg (2012), «Defying conventional wisdom…», *OBHDP* | https://doi.org/10.1016/j.obhdp.2012.06.003 | P | 3 | 3 | 1 | 3 | [M] (sin abstract disponible; solo metadatos) |
| 4.6 | Stahl, Maznevski, Voigt y Jonsen (2010), «Unraveling the effects of cultural diversity in teams», *Journal of International Business Studies* | https://doi.org/10.1057/jibs.2009.85 (manuscrito: https://leeds-faculty.colorado.edu/dahe7472/Stahl%202009.pdf) | P | 3 | 3 | 2 | 3 | [L] (manuscrito aceptado; leí el resumen y secciones; no la tabla de resultados entera) |
| 4.7 | Bell (2007), metaanálisis de composición de nivel profundo, *Journal of Applied Psychology* | https://doi.org/10.1037/0021-9010.92.3.595 | P | 3 | 3 | 1 | 3 | [M] |
| 4.8 | Green y Hand (2021), «Diversity matters/delivers/wins revisited in S&P 500 firms» (documento de trabajo; publicado en 2024 en *Econ Journal Watch* según resultados de búsqueda) | https://doi.org/10.2139/ssrn.3849562 (PDF: https://kenaninstitute.unc.edu/wp-content/uploads/2021/05/Green-Hand-DIV-FFP-McKinsey-revisited-in-SP500-firms-20210519.pdf) | P | 2 | 3 | 3 | 3 | [L] (versión 2.1, 19-may-2021; leí resumen, resultados y métodos citados) |
| 4.9 | McKinsey (2015, 2018, 2020), «Diversity Matters / Delivers / Wins» | no abrí los informes; solo los conozco por Green y Hand | P | 1 | 1 | 2 | 2 | [S] (a través de Green y Hand) |
| 4.10 | Chicago Booth Review, nota sobre el seguimiento de Green, Hand y Bermiss | https://www.chicagobooth.edu/review/do-diverse-leadership-teams-produce-better-performance | S | 2 | 1 | 2 | 1 | [S] |
| 4.11 | Kozlowski e Ilgen (2006) (ver 1.12) | https://doi.org/10.1111/j.1529-1006.2006.00030.x | P | 3 | 3 | 2 | 3 | [S] |

### Afirmaciones con fuente

- Tamaño y procesos: Hackman (1998) trabaja con la idea de Steiner (1972) de que el desempeño real de un equipo es el potencial menos las pérdidas de proceso (coordinación y motivación), y propone sumar las ganancias de proceso. [S] (lo vi por resumen en una búsqueda; en el PDF [L] está la discusión de la estructura del equipo, que no cuenta con una cifra de tamaño óptimo que yo haya localizado). Una regla «5 a 9 personas» que circula en resúmenes de Hackman es de un resumen secundario (https://umbrex.com/resources/frameworks/organization-frameworks/hackman-five-conditions-for-team-effectiveness/) y **no la verifiqué en Hackman**.
- Staats, Milkman y Fox (2012): «as team size increases, people increasingly underestimate the number of labor hours required to complete projects»; lo llaman «team scaling fallacy»; hay evidencia en dos experimentos de laboratorio y en datos archivados de proyectos en una empresa de software; los equipos más grandes terminan las tareas más rápido, pero con costos de coordinación crecientes. Aumentar el tamaño «can hamper its coordination, diminish its members' motivation, and increase conflict». [L parcial] https://faculty.wharton.upenn.edu/wp-content/uploads/2012/05/OBHDP_2012b.pdf
- Curral et al. (2001): en 87 equipos portugueses de distintas industrias, los equipos grandes tenían peores procesos (medidos con el Team Climate Inventory); los grandes con alta exigencia de innovar tenían peores procesos que los grandes sin esa exigencia. [M] https://doi.org/10.1080/13594320143000627
- LePine et al. (2008) encontraron que la relación entre procesos y desempeño depende algo del tamaño; Salas et al. (2008) lo mismo para el entrenamiento; Stahl et al. (2010) tratan el tamaño como moderador de la diversidad cultural. [M/S] (ver 1.10, 1.11, 4.6)
- Aristóteles: tamaño, colocación y antigüedad no se asociaron significativamente con la efectividad. [S] https://rework.withgoogle.com/en/guides/understanding-team-effectiveness. Esto **discrepa en apariencia** con Curral y Staats: ambos tipos de evidencia coexisten (un estudio de una empresa con equipos mayoritariamente de rango limitado de tamaño frente a estudios con rangos amplios).
- Ringelmann: el efecto original, y su revisión por Ingham et al. (1974), que separó la pérdida de coordinación de la pérdida de motivación. Solo verifiqué que el artículo existe (título, revista, año); **no leí su contenido**. [M]
- Diversidad, Stahl et al. (2010): metaanálisis de 108 estudios, 10.632 equipos; «cultural diversity leads to process losses through task conflict and decreased social integration, but to process gains through increased creativity and satisfaction. The effects are almost identical for both levels and types of cultural diversity.» Moderadores: complejidad de la tarea, tamaño, antigüedad y dispersión del equipo. Sus autores resumen: la diversidad cultural es «an asset and a liability» en el mismo equipo. [L] https://leeds-faculty.colorado.edu/dahe7472/Stahl%202009.pdf
- Bell (2007): en el laboratorio, el mínimo y el máximo de habilidad mental general y la inteligencia emocional media se asocian con el desempeño; en el campo, el mínimo de amabilidad y la media de responsabilidad, apertura, colectivismo y preferencia por el trabajo en equipo. [M] https://doi.org/10.1037/0021-9010.92.3.595
- van Dijk et al. (2012) comparan diversidad demográfica con diversidad relacionada con el trabajo en su relación con el desempeño. No pude leer el abstract ni los resultados; **de memoria**, la conclusión es que la diversidad demográfica casi no se relaciona con el desempeño y la relacionada con el trabajo se relaciona algo positivamente, pero esto es un recuerdo no verificado. [M] https://doi.org/10.1016/j.obhdp.2012.06.003
- McKinsey vs. Green y Hand: McKinsey informa una relación positiva y significativa entre el margen EBIT ajustado por industria y la diversidad racial/étnica de los ejecutivos. Green y Hand, con datos recientes de empresas del S&P 500, encuentran relaciones «statistically insignificant» con el margen EBIT y también con crecimiento de ventas, margen bruto, ROA, ROE y TSR. De 40 estadísticos de prueba, 37 no son significativos, uno es positivo y dos negativos. McKinsey no entregó ni los nombres de las empresas de sus conjuntos de datos; Green y Hand aclaran que su método de inferir raza/etnia a partir de fotos y nombres tiene sesgos. [L] https://kenaninstitute.unc.edu/wp-content/uploads/2021/05/Green-Hand-DIV-FFP-McKinsey-revisited-in-SP500-firms-20210519.pdf. Un seguimiento (con Bermiss) encontró que la diversidad predecía el desempeño del año siguiente en poco menos de 5% de las regresiones. [S] https://www.chicagobooth.edu/review/do-diverse-leadership-teams-produce-better-performance. Caveats: el documento era preprint cuando lo leí; las empresas del S&P 500 no son una muestra aleatoria de empresas públicas de EE.UU.; la réplica de ellos no prueba que no haya relación causal en otras muestras.
- Dos cosas distintas que no mezclar: el metaanálisis de equipos (desempeño de un equipo) y los estudios de rentabilidad de empresas (diversidad en la alta dirección contra resultados financieros). McKinsey no es un metaanálisis ni un experimento: es correlación entre empresas.

### Estado de la evidencia

- **Se sostuvo**: las pérdidas de proceso al crecer; la subestimación de esas pérdidas (experimentos + datos de software, Staats 2012); un efecto doble de la diversidad cultural (pérdida en integración, ganancia en creatividad) (Stahl 2010).
- **Se achicó**: la diversidad como «ventaja» automática: el efecto depende de la tarea, el tipo de diversidad y cómo se maneja. Los efectos de nivel superficial y profundo, en el metaanálisis de Stahl, eran casi idénticos.
- **Cayó**: el argumento «la diversidad de la alta dirección produce mayor rentabilidad» como evidencia sólida: no se reproduce en una reevaluación con datos públicos (Green y Hand), con las salvedades dichas. Está en disputa; McKinsey tiene una posición discrepante y yo no abrí sus informes ni su respuesta.
- **Sin número verificado**: el tamaño óptimo. No hay una cifra respaldada en lo que leí.

### Recurso canónico

Para tamaño: Staats, Milkman y Fox (2012), por su claridad sobre por qué se subestima el costo de sumar gente (útil para quien contrata en una empresa que crece). Para diversidad: Stahl et al. (2010) (leer el modelo de pérdidas y ganancias de proceso y la sección de implicaciones para gerentes) y, para la polémica del «business case», Green y Hand (2021) (leer la introducción y la tabla de resultados; mirar qué dice sobre la falta de datos de McKinsey). Remite, solo como enlace, a Team Topologies (tema existente) para la estructura de equipos de software.

---

## 5. cultura-organizacional

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 5.1 | Schein, *Organizational Culture and Leadership* (varias ediciones) | https://doi.org/10.5465/amr.1986.4306282 (reseña/ficha de la 1.ª ed. en AMR; libro sin URL abierta verificada) | P | 3 | 3 | 3 | 3 | [S] (no abrí el libro; resumen de buscadores y de índice de la edición) |
| 5.2 | Hartnell, Ou y Kinicki (2011), metaanálisis del Competing Values Framework, *Journal of Applied Psychology* | https://doi.org/10.1037/a0021987 | P | 3 | 3 | 1 | 3 | [M] |
| 5.3 | Cameron y Quinn, *Diagnosing and Changing Organizational Culture* (libro) | no verificado; solo hallé una entrada de metadatos de otra edición | P | 3 | 3 | 3 | 3 | [S] (no leí; no lo busqué más allá de la ficha) |
| 5.4 | Guiso, Sapienza y Zingales (2015), «The value of corporate culture», *Journal of Financial Economics* | https://doi.org/10.1016/j.jfineco.2014.05.010 | P | 3 | 2 | 1 | 3 | [M] (solo título/revista/año) |
| 5.5 | Encuesta a 1.348 ejecutivos norteamericanos, «Corporate culture: Evidence from the field», *Journal of Financial Economics* (2022) (autores no verificados; los recuerdo como Graham, Grennan, Harvey y Rajgopal, sin verificar) | https://doi.org/10.1016/j.jfineco.2022.07.008 | P | 3 | 2 | 2 | 3 | [M] |
| 5.6 | Netflix, «Netflix Culture» (jobs.netflix.com) | https://jobs.netflix.com/culture | P (de practicante) | 1 | 2 | 3 | 2 | [S] (procesada por WebFetch; no tengo el texto crudo) |
| 5.7 | Reportes de prensa sobre el deck de 2009 y su revisión de 2024 | https://fortune.com/2024/06/25/netflix-managers-keeper-test-rehire-or-fire-staff/, https://www.library.hbs.edu/working-knowledge/freedom-fear-and-feedback-should-other-companies-follow-netflixs-lead | S | 2 | 1 | 2 | 1 | [S] (solo en la lista de resultados; no los abrí) |

### Afirmaciones con fuente

- Schein, tres niveles: artefactos (lo visible, fácil de observar y difícil de interpretar sin los supuestos), valores declarados (metas, estrategias y filosofías que los líderes y miembros enuncian, que pueden o no coincidir con la conducta), y supuestos básicos (dados por sentados, normalmente inconscientes, tratados como no negociables). [S] https://courses.lumenlearning.com/wm-organizationalbehavior/chapter/levels-of-organizational-culture/ y https://resources.rework.com/libraries/business-culture/schein-three-levels-of-culture. Son cursos y blogs que parafrasean el mismo libro: cuentan como **una sola fuente**.
- Fundadores y mecanismos de incorporación: la quinta edición abre su capítulo de incorporación diciendo que los fundadores y los líderes nombrados o promovidos «have available to them many mechanisms and processes to articulate and embed the culture they have created» [S] https://www.oreilly.com/library/view/organizational-culture-and/9781119212041/c10.xhtml (índice). Mecanismos primarios, tal como los listan los resultados de búsqueda: qué atienden, miden y controlan regularmente los líderes; cómo reaccionan ante crisis; el modelado de roles; la asignación de recompensas y estatus; y cómo reclutan, seleccionan, promueven y excluyen. **Discrepancia**: una página (changingminds.org) habla de cinco mecanismos primarios y cinco secundarios; las demás fuentes listan seis primarios. Resolver con el libro. [S]
- Hartnell et al. (2011): 84 estudios empíricos, 94 muestras independientes; las culturas de clan, adhocracia y mercado se asocian positivamente y de forma distinta con criterios de efectividad (actitudes de los empleados, desempeño operativo —innovación y calidad— y desempeño financiero), «though not always as hypothesized»; «mixed support for the CVF's nomological validity» y falta de apoyo a aspectos de la estructura interna propuesta; los autores proponen un enfoque teórico alternativo. [M] https://doi.org/10.1037/a0021987. **Los coeficientes no los tengo.**
- Guiso et al. (2015) estudia la cultura corporativa y el desempeño; solo verifiqué metadatos; no leí el abstract. [M] https://doi.org/10.1016/j.jfineco.2014.05.010
- Encuesta a ejecutivos (JFE 2022): «Ninety-two percent of the 1348 North American executives we survey believe that improving corporate culture would increase firm value. A striking 84% believe their company needs to improve its culture.» Distingue valores declarados de normas cotidianas, y lista obstáculos como líderes desatentos e incentivos desalineados. Es evidencia de **creencias de ejecutivos**, no de efecto causal, aunque los autores dicen que las respuestas son consistentes con datos externos. [M] https://doi.org/10.1016/j.jfineco.2022.07.008
- Netflix (práctica; dato de practicante, no evidencia): la página actual se describe a sí misma como un modelo de «a professional sports team, not a family», con el «keeper test» («if X wanted to leave, would I fight to keep them?»), «context not control» y «highly aligned and loosely coupled» (un «capitán» informado decide, equipos separados ejecutan); encabezados «The Dream Team», «People Over Process», «Uncomfortably Exciting», «Great and Always Better». La página dice que viene de «our first culture deck» de 2009 y no trae fecha de revisión. [S] https://jobs.netflix.com/culture. La prensa reporta que el deck original es de agosto de 2009 y que se revisó varias veces; en el memo de 2024 el encabezado «Freedom and Responsibility» se reemplazó por «People Over Process». [S] (fuentes de prensa de la lista de resultados; no abiertas). **No encontré un estudio que evalúe el modelo de Netflix** ni compare su efecto con alternativas; es un caso, sin grupo de comparación, y de una empresa de un tamaño y sector concretos.

### Estado de la evidencia

- **Se sostuvo** (con matices): que hay asociación entre tipos de cultura (CVF) y resultados, pero **no** con la estructura teórica del marco: Hartnell et al. encuentran apoyo «mixto» y proponen un enfoque alternativo.
- **Se achicó**: el CVF como modelo de tipos excluyentes con efectos diferenciales previstos: la estructura interna no se sostuvo.
- **Sin prueba**: que la cultura se pueda *diseñar* o *cambiar* de modo dirigido. No encontré estudios causales sobre eso en estas rondas (declaro hueco). Lo que hay es la teoría de Schein (los líderes y fundadores incorporan la cultura mediante lo que atienden, premian y a quién contratan) y creencias de ejecutivos.
- **Netflix**: caso de practicante; sin evaluación comparativa que yo haya hallado.

### Recurso canónico

Schein, *Organizational Culture and Leadership* (el capítulo de los tres niveles y el de los mecanismos de incorporación; elegir la edición vigente, que no pude verificar). Para evidencia sobre desempeño, Hartnell et al. (2011): leer el abstract y la parte que prueba la estructura interna del CVF (y qué «no se sostuvo»). Para práctica marcada, el memo de Netflix, leído como declaración de un practicante, no como prueba.

---

## 6. trabajo-remoto-e-hibrido

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 6.1 | Bloom, Liang, Roberts y Ying (2015), «Does Working from Home Work? Evidence from a Chinese Experiment», *Quarterly Journal of Economics* | https://doi.org/10.1093/qje/qju032 (documento NBER: https://doi.org/10.3386/w18871) | P | 3 | 3 | 2 | 3 | [M] |
| 6.2 | Bloom, Han y Liang (2024), «Hybrid working from home improves retention without damaging performance», *Nature* | https://doi.org/10.1038/s41586-024-07500-2 | P | 3 | 3 | 2 | 3 | [M] (abstract cortado en el volcado; sin el final) |
| 6.3 | Gajendran y Harrison (2007), metaanálisis, *Journal of Applied Psychology* | https://doi.org/10.1037/0021-9010.92.6.1524 | P | 3 | 3 | 1 | 3 | [M] |
| 6.4 | Yang et al. (2022), «The effects of remote work on collaboration among information workers», *Nature Human Behaviour* | https://doi.org/10.1038/s41562-021-01196-4 | P | 3 | 3 | 2 | 3 | [S] (la página de la revista pidió autenticación; abstract no disponible; cifras vía resúmenes de prensa) |
| 6.5 | Emanuel, Harrington y Pallais (2023), «The Power of Proximity to Coworkers», NBER | https://doi.org/10.3386/w31880 | P | 2 | 3 | 2 | 3 | [M] (documento de trabajo; no verifiqué si fue publicado) |
| 6.6 | Barrero, Bloom y Davis (2021), «Why Working from Home Will Stick», NBER | https://doi.org/10.3386/w28731 | P | 2 | 2 | 1 | 2 | [M] (solo metadatos) |
| 6.7 | Bloom, Han y Liang (2022), «How Hybrid Working From Home Works Out», NBER (versión de trabajo del 6.2) | https://doi.org/10.3386/w30292 | P | 2 | 2 | 1 | 1 | [M] (solo metadatos; misma investigación que 6.2) |

### Afirmaciones con fuente

- Bloom et al. (2015), Ctrip, 16.000 empleados, NASDAQ, China: empleados de call center que se ofrecieron como voluntarios fueron asignados al azar a trabajar desde casa o en la oficina durante nueve meses. «Home working led to a 13% performance increase, of which 9% was from working more minutes per shift (fewer breaks and sick days) and 4% from more calls per minute.» Mejora de satisfacción; la tasa de renuncia «halved»; pero la tasa de ascensos condicionada al desempeño bajó. Tras extender la opción a toda la empresa, más de la mitad de los participantes cambió de régimen, y las ganancias casi se duplicaron a 22%, lo que los autores atribuyen a selección y aprendizaje. [M] https://doi.org/10.1093/qje/qju032. Limitaciones: un solo tipo de trabajo (call center, tareas medibles), voluntarios.
- Bloom, Han y Liang (2024): ensayo aleatorizado de seis meses con 1.612 empleados de una empresa tecnológica china (2021-2022); el híbrido «improved job satisfaction and reduced quit rates by one-third»; la reducción de renuncias fue significativa para no gerentes, mujeres y quienes tienen largos traslados; pruebas de equivalencia nula: el híbrido no afectó las calificaciones de desempeño de las dos revisiones siguientes, no hubo diferencia en ascensos y no afectó las líneas de código de los ingenieros; los 395 gerentes del experimento revisaron su opinión, del efecto negativo estimado en productividad (-2,6% en promedio) antes al positivo (+1,0%) después. [M] https://doi.org/10.1038/s41586-024-07500-2
- Gajendran y Harrison (2007): 46 estudios en ambientes naturales, 12.883 empleados; el teletrabajo tuvo efectos pequeños pero mayormente beneficiosos en autonomía percibida y conflicto trabajo-familia (menor); sin efecto dañino general en la calidad de las relaciones laborales; efectos beneficiosos en satisfacción, desempeño, intención de renuncia y estrés de rol; mediado en parte por la autonomía percibida; la alta intensidad (más de 2,5 días por semana) acentúa el beneficio sobre el conflicto trabajo-familia pero perjudica las relaciones con compañeros. [M] https://doi.org/10.1037/0021-9010.92.6.1524. Datos previos a la pandemia, con teletrabajo mayormente voluntario.
- Yang et al. (2022), Microsoft: el cambio a trabajo remoto en toda la empresa hizo que la red de colaboración se volviera más estática y aislada en silos: el tiempo de colaboración con vínculos entre grupos cayó alrededor de 25%; menos nuevos colaboradores incorporados y menos dejados; las horas de reunión bajaron alrededor de 5% y subió la comunicación asincrónica. El diseño comparó a quienes ya trabajaban en remoto antes de marzo de 2020 con los que cambiaron de golpe. [S] https://newsroom.haas.berkeley.edu/research/when-everyone-works-remotely-communication-and-collaboration-suffer-study-finds/ (resultados de búsqueda; no abrí el paper). La frase exacta «more static and siloed» está confirmada para el documento de trabajo, no para el abstract publicado.
- Emanuel, Harrington y Pallais (2023): ingenieros de software de una empresa Fortune 500: la proximidad «increases long-run human capital development at the expense of short-term output»; con las oficinas abiertas, los ingenieros del mismo edificio que todo su equipo recibían 22% más de feedback en línea que quienes tenían compañeros lejos, y esa ventaja desaparece con el cierre por COVID-19; sentarse juntos reduce la producción de código, sobre todo de los senior; los costos y beneficios son más agudos para las mujeres, que dan y reciben más mentoría; la proximidad modera los aumentos de salario a corto plazo y los eleva a largo plazo; tener un solo compañero lejano reducía el feedback de los que estaban juntos. [M] https://doi.org/10.3386/w31880. Un solo empleador.
- Dirigir a distancia: lo único verificado sobre cómo cambia la dirección es lo de Bloom et al. 2024 (los gerentes cambiaron de opinión tras el experimento) y el costo en ascensos de Bloom 2015. No encontré en estas rondas literatura sobre *prácticas de quien dirige* a distancia (reuniones, medición, confianza); queda como hueco.

### Estado de la evidencia

- **Se sostuvo**: beneficios en retención y satisfacción con el híbrido (ensayo aleatorizado, 2024) y con el trabajo remoto parcial (Gajendran y Harrison 2007), sin pérdida de desempeño medible en esos estudios.
- **Se achicó**: la productividad: +13% en Ctrip (call center, voluntarios), nula en el híbrido de Nature (grupo de empresa tecnológica); no extrapolar la cifra de Ctrip a otras tareas.
- **En tensión (dar las dos)**: Yang et al. y Emanuel et al. muestran costos de colaboración, feedback y mentoría con el trabajo remoto; Bloom et al. 2024 no encuentra costo en desempeño ni ascensos con el híbrido. No son incompatibles: remoto total en empresa grande frente a híbrido de dos días a la semana, y distintos plazos; la comparación directa no la encontré.
- **Cayó**: «el remoto reduce la productividad» como regla general (Gajendran 2007; Bloom 2015, 2024). Los efectos en innovación y carrera a largo plazo son la parte menos asentada.

### Recurso canónico

Bloom, Han y Liang (2024), en *Nature* (https://doi.org/10.1038/s41586-024-07500-2): ensayo aleatorizado con medidas de desempeño externas al autoinforme; fijarse en el apartado de qué grupos de empleados se retienen más y qué pasó con los ascensos. Para el costo de la distancia, leer a la par Yang et al. (2022) y Emanuel et al. (2023).

---

## Huecos (lo que no encontré o no pude verificar)

1. **Coeficientes exactos** de Frazier 2017, De Dreu y Weingart 2003, de Wit 2012, Hartnell 2011, van Dijk 2012, LePine 2008 y Salas 2008: solo tengo los abstracts o resúmenes secundarios. Cualquier nota que dé números debería volver al texto. Los valores de ρ de De Dreu y Weingart que tengo en la cabeza no están verificados y no los uso.
2. **Marks, Mathieu y Zaccaro 2001**: solo título y año; la tripartición transición/acción/interpersonal es de memoria. **Jehn 1995 y Jehn y Mannix 2001**: solo metadatos, no leí el contenido.
3. **Proyecto Aristóteles**: no pude leer la página de re:Work (404 en dos URLs); lo que tengo viene de fragmentos de búsqueda y de prensa. No hay método publicado accesible.
4. **Hackman 2002 (*Leading Teams*)** no se pudo abrir; la versión de cinco condiciones es [S] y la de seis (1998) es [L]. Falta ver cómo reagrupa. Tampoco hay cifra verificada de tamaño óptimo de equipo (5-9 viene de un resumen secundario).
5. **Ringelmann** (efecto original y su pérdida por coordinación frente a motivación): solo metadatos de Ingham et al. 1974.
6. **Diversidad**: no pude leer van Dijk et al. (2012); tampoco abrí los informes de McKinsey ni su respuesta a Green y Hand; la publicación de 2024 en *Econ Journal Watch* viene de un resultado de búsqueda. Falta evidencia metaanalítica sobre diversidad de *género* en equipos pequeños (aparece solo como predictor del factor c en Woolley 2010 y Riedl 2021, por abstract).
7. **Seguridad psicológica**: no hay réplica independiente ni experimento aleatorizado que yo haya encontrado; la crítica de Newman et al. la tengo solo por un agregador; no pude confirmar el contenido crítico de Edmondson y Bransby ni la nota de HBR de 2025 (URL no verificada).
8. **Cultura**: ningún estudio causal sobre si la cultura puede diseñarse o cambiarse; Schein y Cameron y Quinn no se leyeron (solo resúmenes). Las dos versiones del número de mecanismos de incorporación (cinco frente a seis) quedan sin resolver. Papel del fundador: solo Schein, vía resúmenes; no busqué literatura empírica (p. ej. sobre fundadores y cultura) en las tres rondas. Netflix: sin evaluación independiente; sin texto crudo.
9. **Remoto**: sin literatura hallada sobre *dirigir* a distancia (prácticas de gerentes, medición, confianza); Emanuel et al. no confirmé si está publicado; Yang et al. leído por prensa; Bloom 2024 con el abstract cortado.
10. **Empresas chicas**: casi toda la evidencia viene de empresas medianas o grandes (Ctrip, Microsoft, Fortune 500, S&P 500) y de equipos formales; casi nada sobre 2 a 50 personas. Hay que decirlo en las notas.
11. **Entrenamiento de equipos**: no leí Salas 2008 y no verifiqué la revisión de 2017 ni Delise et al. 2010.
