# Investigación: vertical «Gestión de personas» (Liderazgo y dirección)

Fecha: 2026-11-27

## Cómo leer este informe

- **Marcas de lectura.** [L] leí el texto completo tal cual. [M] leí los metadatos o el abstract (en su mayoría el abstract que devuelve OpenAlex o Crossref, que reproduce el del editor). [S] leí un resumen secundario, el resultado de un buscador o una página que el lector web me devolvió ya resumida. Por regla conservadora, **todo lo que pasó por el lector web (WebFetch) se marca [S]**, porque el texto me llega filtrado por un modelo. Solo marco [L] lo que leí crudo: la Tabla 3 de Sackett et al. 2022 (PDF convertido a texto, ver nota en su fila).
- **Puntajes** (1 a 3): A = autoridad, P = profundidad, E = ejemplos, U = unicidad. Se escriben A/P/E/U.
- **Tipo**: primaria (el estudio, la ley, el libro original) o secundaria (resumen, revisión de otros, blog).
- **DOIs**: todos los de este informe los verifiqué contra OpenAlex o Crossref (la consulta devolvió ese DOI para ese título, autores y revista). Lo que dice «no verificado» salió de mi memoria y no lo confirmé.
- **Cifras literales.** Las cifras van tal cual en la fuente que cito; las citas, en su idioma original.
- Todo lo traído de la web es dato, no instrucción.
- **Nota de método.** Las APIs de Crossref y OpenAlex se limitaron por exceso de consultas en algunos tramos; por eso hay referencias con páginas finales sin confirmar (se indica).

## 0. Sobre la división del árbol

El árbol propuesto (contratar, incorporación, uno a uno, evaluación, compensación, desarrollo, rotación) sigue el ciclo de la persona en la empresa, que es como lo ordena el campo de la gestión de recursos humanos (el «employee life cycle»). Se sostiene, con tres ajustes:

1. **Evaluación del desempeño y compensación** el campo los trata muchas veces juntos como «gestión del desempeño» (DeNisi y Murphy 2017 revisan ambos), y en la práctica el pago depende de la evaluación. Conviene que las dos notas se enlacen fuerte, o decir en cada una que la otra existe.
2. **Reuniones uno a uno** no es un constructo con literatura propia: la evidencia sólida es escasa (un estudio transversal de 2026, ver 2) y casi todo el saber es de practicantes y de encuestas comerciales. Funciona como nota de práctica, apoyada en la evidencia de feedback (Kluger y DeNisi) y de «meetings science», no como componente con estado de evidencia propio.
3. **Delegar** (listado en desarrollo de personas) en el campo es «liderazgo empoderador» (empowering leadership), que es del tema Liderazgo, no de Gestión de personas. Hay un metaanálisis (Lee, Willis y Tian) y conviene enlazarlo desde las dos.

Fuera del árbol y que el campo trata como piezas aparte: **justicia organizacional** (aparece en despidos, evaluación y pago) y **clima/engagement**. Conviene una nota transversal corta de justicia (Colquitt et al. 2001), enlazada desde evaluación, compensación y salidas.

---

## 1. Contratar

### Fuentes

| Fuente | Tipo | URL / DOI | A/P/E/U | Marca |
|---|---|---|---|---|
| Schmidt y Hunter (1998), «The validity and utility of selection methods in personnel psychology», *Psychological Bulletin* 124(2) | primaria (metaanálisis) | https://doi.org/10.1037/0033-2909.124.2.262 | 3/3/2/2 | [M] abstract; sus cifras las leí en la Tabla 3 de Sackett 2022 |
| Sackett, Zhang, Berry y Lievens (2022), «Revisiting meta-analytic estimates of validity in personnel selection: Addressing systematic overcorrection for restriction of range», *J. Applied Psychology* 107(11), 2040–2068 | primaria (metaanálisis) | https://doi.org/10.1037/apl0000994 ; PDF (copia en gwern.net): https://www.Gwern.net/doc/statistics/meta-analysis/2021-sackett.pdf | 3/3/3/3 | [M] abstract + **Tabla 3 leída en el PDF convertido a texto** (no leí el artículo entero); no se la puede marcar [L] completa |
| Sackett et al. (2023), «Revisiting the design of selection systems in light of new findings regarding the validity of widely used predictors», *Industrial and Organizational Psychology* 16(3), 283–300 | primaria (artículo de síntesis) | https://ideas.repec.org/a/cup/inorps/v16y2023i3p283-300_1.html | 3/2/2/2 | [S] (solo ficha y títulos del buscador) |
| SIOP, «Is cognitive ability the best predictor of job performance?» (TIP) | secundaria | https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance | 2/1/1/1 | [S] |
| Levashina, Hartwell, Morgeson y Campion (2014), «The structured employment interview: Narrative and quantitative review…», *Personnel Psychology* 67(1), 241–293 | primaria (revisión) | https://doi.org/10.1111/peps.12052 | 3/3/2/2 | [M] abstract |
| Sackett et al. (2023), «A contemporary look at the relationship between general cognitive ability and job performance», *J. Applied Psychology* (autores según el buscador: Sackett, Demeke, Bazian, Griebie, Priest, Kuncel; volumen y DOI 10.1037/apl0001159 sin verificar, vino del buscador) | primaria | https://experts.umn.edu/en/publications/a-contemporary-look-at-the-relationship-between-general-cognitive/ | 3/2/1/2 | [S] |
| Ben Horowitz, «The Hard Thing About Hard Things» (2014), sobre contratar | practicante (libro) | https://a16z.com/books/the-hard-thing-about-hard-things/ | 2/2/3/2 | [S] |

No pude consultar la guía de entrevista estructurada de Google re:Work (la URL que probé dio 404); es un hueco.

### Afirmaciones

- Schmidt y Hunter resumen «85 years of research» y concluyen que las tres combinaciones con mayor validez multivariada fueron «GMA plus a work sample test (mean validity of .63), GMA plus an integrity test (mean validity of .65), and GMA plus a structured interview (mean validity of .63)». https://doi.org/10.1037/0033-2909.124.2.262 [M]
- Sackett et al. 2022 concluyen que la sobrecorrección por restricción de rango infló las validez: «most of the same selection procedures that ranked high in prior summaries remain high in rank, but with mean validity estimates reduced by .10–.20 points. Structured interviews emerged as the top-ranked selection procedure.» https://doi.org/10.1037/apl0000994 [M]
- Tabla 3 de Sackett et al. 2022 (validez operacional ρ; entre paréntesis lo que daba Schmidt y Hunter 1998): entrevista estructurada **.42** (.51); pruebas de conocimiento del puesto **.40** (.48); biodata con clave empírica **.38** (.35); muestras de trabajo **.33** (.54); pruebas de capacidad cognitiva **.31** (.51); pruebas de integridad **.31** (.41); centros de evaluación **.29** (.37); conscienciosidad general **.19** (.31); entrevista no estructurada **.19** (.38); años de experiencia **.07** (.18). Referencias: Schmidt y Hunter daban **.26**; Sackett las dejó fuera por información insuficiente. Fuente: Tabla 3 en https://www.Gwern.net/doc/statistics/meta-analysis/2021-sackett.pdf (texto convertido, columnas leídas a mano).
- En la misma tabla, la diferencia estándar entre grupos Negro-Blanco (d) es 0.79 para pruebas cognitivas, 0.67 para muestras de trabajo y 0.23 para entrevista estructurada. Ver diversidad: la capacidad cognitiva baja pero con más diferencia entre grupos. Misma fuente.
- El valor inferior del intervalo de credibilidad al 80 % de la entrevista estructurada es .18 (SD de ρ = .19), el de la capacidad cognitiva .13, y el de la entrevista no estructurada incluye cero (−.01). Es decir: la validez varía mucho entre contextos. Misma fuente.
- Sobre las entrevistas, Sackett et al. dicen (texto extraído, p. «Structured and Unstructured Interviews») que reestimaron con la metaanálisis de Huffcutt et al. (2014), que reportó validez observada de .36 (estructurada) y .13 (no estructurada). Misma fuente.
- Levashina et al. cubren ocho temas, incluyendo «reducing bias through structure» y «impression management in structured interviews», y concluyen que «much is known about structured interviews, but there are still many unanswered questions». https://doi.org/10.1111/peps.12052 [M]
- SIOP resume: «structured interviews had the highest mean operational validity» (.42), cognitiva .31. https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance [S]
- Hay debate vivo sobre la capacidad cognitiva: respuestas publicadas en 2023 («Rumors of general mental ability's demise are the next red herring», «It takes more than meta-analysis to kill cognitive ability») cuestionan que haya perdido su lugar. Aparecen en el buscador: https://cambridge.org/core/services/aop-cambridge-core/content/view/FC0F79EC4FDF5BEEA5F934E9098E2756/S1754942623000378a.pdf/rumors-of-general-mental-abilitys-demise-are-the-next-red-herring.pdf [S, solo título]
- Tests de personalidad: en la tabla, conscienciosidad general .19, contextualizada .25 (con SD de ρ = 0.00, único dato «limpio»); extraversión general .10, afabilidad .10, estabilidad emocional .09, apertura .07 (general) / .05. Misma Tabla 3. El mecanismo y la crítica de los rasgos viven en Psicología (enlazar).

### Estado de la evidencia

- **Se sostuvo** (en la revisión de 2022): el orden general. Los procedimientos estructurados y basados en contenido del puesto (entrevista estructurada, conocimiento del puesto, muestras de trabajo) siguen arriba; la experiencia y los rasgos de personalidad sueltos siguen abajo.
- **Se achicó**: todas las cifras entre .10 y .20 puntos; la capacidad cognitiva pasó de .51 a .31 y las muestras de trabajo de .54 a .33; la entrevista no estructurada de .38 a .19.
- **Cayó**: la idea de que la capacidad cognitiva es «el mejor predictor» (ya no está primera) y la de que la entrevista no estructurada vale casi como la estructurada.
- **En disputa**: cuánto hay que corregir por rango restringido y qué lugar queda para la capacidad cognitiva (Sackett et al. 2023 y las réplicas de 2023). El .42 es una media con credibilidad amplia; en una empresa chica no hay cómo saber en qué parte de la distribución se cae.
- **Hueco de generalización a empresas chicas**: ningún metaanálisis citado separa por tamaño de empresa. Las cifras vienen de muestras grandes (concurrent y predictive) y de puestos sobre todo operativos y administrativos.

### Sesgos al entrevistar (hueco)

No encontré en estas rondas la fuente primaria que cuantifique sesgos de entrevista (por ejemplo atractivo, similitud, primeras impresiones) ni su reducción con estructura, salvo el título «reducing bias through structure» de Levashina et al. [M]. Queda como hueco: leer ese capítulo.

### Contratar en una empresa chica (practicante)

Horowitz es la voz de práctica más citada (libro de 2014). No pude leer el texto del capítulo; solo encontré sus títulos y resúmenes secundarios (https://fortune.com/2014/03/04/five-management-lessons-from-ben-horowitz [S]). Hueco: no verifiqué ninguna cita literal sobre contratar en etapas tempranas. Tampoco encontré un estudio de campo sobre contratación en empresas de 2 a 50 personas.

### Recurso canónico

**Sackett, Zhang, Berry y Lievens (2022), Tabla 3.** Fijarse en: (1) la entrevista estructurada primera con ρ = .42, (2) la columna del rango de credibilidad (la dispersión es grande), (3) la columna de diferencias entre grupos. Complemento: Levashina et al. (2014) para cómo estructurar.

---

## 2. Incorporación

### Fuentes

| Fuente | Tipo | URL / DOI | A/P/E/U | Marca |
|---|---|---|---|---|
| Bauer, Bodner, Erdogan, Truxillo y Tucker (2007), «Newcomer adjustment during organizational socialization: A meta-analytic review of antecedents, outcomes, and methods», *J. Applied Psychology* 92(3), 707 | primaria (metaanálisis; 70 muestras) | https://doi.org/10.1037/0021-9010.92.3.707 | 3/3/2/3 | [M] |
| Work Institute, nota sobre rotación del primer año | comercial | https://workinstitute.com/?p=3585 | 1/1/1/1 | [S] (solo resultado del buscador) |
| Employ vía Korn Ferry, «The 90-Day Breakup» | comercial | https://www.kornferry.com/insights/this-week-in-leadership/the-90-day-breakup | 1/1/1/1 | [S] |
| SHRM sobre retención de nuevos ingresos | comercial | https://www.shrm.org/resourcesandtools/hr-topics/talent-acquisition/pages/new-hires-retention-turnover.aspx | 1/1/1/1 | [S] (solo título del buscador) |

### Afirmaciones

- El metaanálisis probó un modelo en el que el ajuste (claridad de rol, autoeficacia y aceptación social) media el efecto de las tácticas de socialización de la organización y de la búsqueda de información sobre los resultados (satisfacción, compromiso, desempeño, intención de quedarse, rotación). «The results generally supported this model.» Además miró moderadores de método: cross-seccional vs longitudinal, de la escuela al trabajo vs de trabajo a trabajo. https://doi.org/10.1037/0021-9010.92.3.707 [M]
- No obtuve los tamaños de efecto de Bauer et al.: el abstract no los trae y no leí el texto completo. Hueco.
- Cifras de salida temprana: son comerciales y discrepan. Una fuente secundaria atribuye a Work Institute «around 40% of employee turnover occurs within the employee's first year» (cuota del total de las salidas); Employ reporta rotación del primer año de 12.1 % en 2025 contra 23.7 % en 2024 (por nuevos ingresos); una nota de Workable dice que «about 20% of employees leave within their first 45 days» sin fuente. Son medidas distintas (parte de las salidas vs tasa entre las altas) y ninguna es revisada por pares. https://www.kornferry.com/insights/this-week-in-leadership/the-90-day-breakup ; https://resources.workable.com/tutorial/new-hire-turnover-rate [S]
- Work Institute afirma que un buen onboarding ayuda a que la persona se sienta preparada y conectada; es afirmación de proveedor sin medición. https://workinstitute.com/?p=3585 [S]

### Estado de la evidencia

- **Se sostuvo**: el modelo de ajuste (rol, autoeficacia, aceptación social) con tácticas organizacionales e iniciativa del recién llegado como antecedentes; es el metaanálisis estándar (más de 1.100 citas según Crossref).
- **Achicó / cayó**: sin datos en estas rondas.
- **En disputa / sin evidencia sólida**: las cifras de salida temprana (todas de proveedores) y que un programa de onboarding concreto reduzca la rotación (no hallé un experimento ni un metaanálisis de programas).

### Recurso canónico

**Bauer et al. (2007)**, el modelo de la Figura de ajuste. Fijarse en qué se mide como «ajuste» (claridad de rol, autoeficacia, aceptación social) porque de ahí salen las tres cosas que un onboarding puede mover. Es lectura obligada antes de escribir la nota; no pude leerla completa.

---

## 3. Reuniones uno a uno

### Fuentes

| Fuente | Tipo | URL / DOI | A/P/E/U | Marca |
|---|---|---|---|---|
| Gray, Flinchum, Rogelberg, Gerson, Dilley y Kreamer (2026), «One Meeting That Should Not Be an Email: Manager–Direct Report One-on-One Meetings and Employee Engagement», *J. Organizational Behavior* (en línea) | primaria (dos encuestas con intervalo, N = 303) | https://doi.org/10.1002/job.70134 | 3/2/1/3 | [M] |
| Allen y Rogelberg (2013), «Manager-led group meetings: A context for promoting employee engagement», *Group & Organization Management* 38(5), 543–569 | primaria (N = 319) | https://doi.org/10.1177/1059601113503040 | 2/2/1/2 | [M] |
| Harter y Adkins (Gallup, 8-abr-2015), «Employees Want a Lot More from Their Managers» (título según la página; el texto menciona «regular meetings») | **encuesta comercial** | https://www.gallup.com/workplace/236570/one-on-one-meetings.aspx | 1/1/1/1 | [S] (vía lector web) |
| Andy Grove, *High Output Management* (1983), sobre las «one-on-ones» | practicante (libro) | sin URL del texto; resúmenes: https://a16z.com/2015/11/13/high-output-management/ | 3/3/3/3 | [S] (no leí el libro; solo resúmenes de terceros) |

### Afirmaciones

- Gray et al. (2026): la calidad de las reuniones uno a uno, reflejada en conductas del jefe orientadas a la tarea y a la relación, «was more consistently associated with engagement than meeting quantity». Se sostuvo tras controlar que el jefe usara esas conductas fuera de las reuniones. Muestra: dos encuestas con intervalo, N = 303; fundamentos teóricos: JD-R, autodeterminación y Kahn. Es una asociación autorreportada, no un experimento. https://doi.org/10.1002/job.70134 [M]
- Allen y Rogelberg (2013) encontraron que cuando los jefes hacen relevantes sus reuniones de grupo, dejan voz a los empleados y manejan el tiempo, aumenta el engagement; es sobre reuniones de equipo, no de uno a uno. https://doi.org/10.1177/1059601113503040 [M]
- Gallup (2015): «employees whose managers hold regular meetings with them are almost three times as likely to be engaged». La página no dice «one-on-one» (dice «regular meetings»), no da tamaño de muestra para ese dato y no especifica frecuencia. Afirma además que el engagement es más alto entre quienes tienen alguna comunicación diaria con el jefe. https://www.gallup.com/workplace/236570/one-on-one-meetings.aspx [S] Encuesta comercial, no revisada por pares; asociación, no causa.
- Frecuencia: no encontré fuente de investigación que fije una. Las recomendaciones de semanal, quincenal o de 30 a 60 minutos son de practicantes y de guías (por ejemplo Baylor HR sugiere 30 min semanales; Microsoft Viva sugiere al menos dos veces por mes; ninguna es investigación). Grove: según resúmenes, la reunión dura cerca de una hora y la agenda la lleva la persona del equipo; una fuente secundaria afirma que el libro defendía el formato semanal, otra describe 90 minutos; no coinciden y no pude cotejar con el libro. https://getlighthouse.com/blog/high-output-management [S]

### Estado de la evidencia

- **Se sostuvo**: nada con metaanálisis ni réplica específico de uno a uno.
- **Disputa / débil**: la asociación calidad de la reunión con engagement, con un estudio transversal de 2026; la cifra «tres veces» de Gallup (sin método público).
- **Sin evidencia**: la frecuencia óptima y la duración.
- Lo que sí tiene respaldo fuerte es lo que los uno a uno *transportan*: feedback bien hecho (ver sección 4, Kluger y DeNisi) y, para el mecanismo de motivación, el tema Psicología.

### Recurso canónico

**Grove, cap. sobre «one-on-ones»** (practicante, a leer en el libro, no en resúmenes) para el *para qué* (la reunión es de la persona, el jefe transfiere conocimiento y valores). Para la evidencia, **Gray et al. (2026)** con la salvedad de que es un solo estudio autorreportado. Gallup solo como dato de encuesta comercial.

---

## 4. Evaluación del desempeño

### Fuentes

| Fuente | Tipo | URL / DOI | A/P/E/U | Marca |
|---|---|---|---|---|
| DeNisi y Murphy (2017), «Performance appraisal and performance management: 100 years of progress?», *J. Applied Psychology* 102(3) | primaria (revisión) | https://doi.org/10.1037/apl0000085 | 3/3/2/3 | [M] |
| Kluger y DeNisi (1996), «The effects of feedback interventions on performance…», *Psychological Bulletin* 119(2), 254–284 | primaria (metaanálisis; 607 tamaños de efecto) | https://doi.org/10.1037/0033-2909.119.2.254 | 3/3/2/3 | [M] |
| Scullen, Mount y Goff (2000), «Understanding the latent structure of job performance ratings», *J. Applied Psychology* 85(6), 956–970 | primaria | https://doi.org/10.1037/0021-9010.85.6.956 | 3/3/2/3 | [M] |
| Scullen, Bergey y Aiman-Smith (2005), «Forced distribution rating systems and the improvement of workforce potential: A baseline simulation», *Personnel Psychology* 58(1), 1–32 | primaria (simulación) | https://doi.org/10.1111/j.1744-6570.2005.00361.x | 3/3/2/3 | [M] |
| Cappelli y Tavis (2016), «The performance management revolution», *Harvard Business Review* (oct. 2016) | secundaria / divulgación | https://hbr.org/2016/10/the-performance-management-revolution | 2/1/2/2 | [S] (la página está tras suscripción; solo vi el encabezado) |
| Buckingham y Goodall (2015), «Reinventing performance management», *HBR* (abr. 2015), sobre Deloitte | practicante / divulgación | https://hbr.org/2015/04/reinventing-performance-management | 2/1/2/2 | [S] (idem; solo introducción) |
| Documento con título «Rater source factors represent important subcomponents of the criterion construct space, not rater bias» (Human Resource Management Review 18, 2008, según el encabezado del buscador; autores y DOI sin verificar) | primaria | https://www.psychology.uga.edu/sites/default/files/CVs/Rater%20source%20factors%20represent%20construct%20space%2C%20not%20rater%20bias-1%20%281%29.docx | 2/1/1/2 | [S] (solo título) |

### Afirmaciones

- Kluger y DeNisi: 607 tamaños de efecto, 23.663 observaciones. Las intervenciones de feedback mejoraron el desempeño en promedio (d = .41), pero «over ⅓ of the FIs decreased performance». La efectividad baja cuando la atención se desplaza hacia el yo y se aleja de la tarea. https://doi.org/10.1037/0033-2909.119.2.254 [M] (el abstract dice «'/3», que es la fracción «un tercio» mal extraída; lo normalizo a «un tercio»).
- DeNisi y Murphy: revisan 100 años en ocho áreas (formatos de escala, criterios, entrenamiento, reacciones, propósito, fuentes, diferencias demográficas, procesos cognitivos) y concluyen que el papel de JAP «has not been to propose models and new ideas, but has been primarily to test ideas and models proposed elsewhere». Piden más investigación sobre gestión del desempeño. https://doi.org/10.1037/apl0000085 [M]
- Scullen, Mount y Goff: en dos grandes bases (n = 2.350 y 2.142 gerentes, 3 dimensiones, 7 evaluadores: 2 jefes, 2 pares, 2 subordinados y uno mismo), «idiosyncratic rater effects (62% and 53%) accounted for over half of the rating variance»; el desempeño real del evaluado (general y por dimensión) explicó «21% and 25%»; el error aleatorio, 11 % y 18 %. https://doi.org/10.1037/0021-9010.85.6.956 [M] Replicación parcial en Japón con 1.380 gerentes: efecto idiosincrásico «over half», desempeño real de «less than 25%», error 15 % (J. Japanese Admin. Science 18(2), 2005; https://doi.org/10.5651/jaas.18.89 [M]).
- Disputa sobre la lectura: parte del campo sostiene que lo que se llama «sesgo de evaluador» es en parte construcción legítima de lo evaluado (título del buscador: «Rater source factors represent important subcomponents of the criterion construct space, not rater bias»). No leí el argumento: [S].
- Scullen, Bergey y Aiman-Smith (simulación): un sistema de distribución forzada «could lead to noticeable improvement in workforce potential, that most of the improvement should be expected to occur over the first several years, and that improvement is largely a function of the percentage of workers to be fired and the level of voluntary turnover». Es un modelo que *supone* ciertas validez y confiabilidad, no un estudio de campo. https://doi.org/10.1111/j.1744-6570.2005.00361.x [M]
- Cappelli y Tavis (HBR): el sumario dice que las evaluaciones tradicionales «have been abandoned by more than a third of U.S. companies» (afirmación del sumario de HBR; no vi su fuente). La nota cuenta el caso de Colorcon, que dejó las evaluaciones anuales y dio feedback instantáneo más bonos semanales chicos. https://hbr.org/2016/10/the-performance-management-revolution [S]
- Deloitte (Buckingham y Goodall, 2015): el sumario dice «At Deloitte we're redesigning our performance management system»; el resto de los datos (horas, cuatro preguntas) no pude leerlo. La cifra de «2 millones de horas al año» que circula **no la verifiqué** (de memoria). El caso de Adobe tampoco lo verifiqué. https://hbr.org/2015/04/reinventing-performance-management [S]

### Estado de la evidencia

- **Se sostuvo**: (a) las calificaciones de evaluadores individuales reflejan mucho del evaluador (dos bases grandes, 53–62 %); (b) el feedback no mejora siempre el desempeño y un tercio empeora (metaanálisis).
- **Se achicó**: la fuerza de la afirmación «el 62 % es sesgo» (en disputa con la lectura de constructo).
- **Cayó**: no hay un único consenso de caída para el ciclo anual; lo que cayó es la defensa de la calificación única, numérica y anual como instrumento de mejora, según las revisiones (DeNisi y Murphy); falta una evaluación experimental de «sin calificaciones».
- **En disputa**: la distribución forzada (solo simulación; nada de campo en estas rondas); la «revolución» de eliminar las evaluaciones (divulgación de HBR, sin estudio comparativo que haya encontrado).
- **Hueco**: los tamaños de efecto de rotación, justicia y reacciones a la evaluación; qué sustituto tiene respaldo (feedback frecuente centrado en la tarea es lo que apunta Kluger y DeNisi, pero no hay comparación directa con el ciclo anual).

### Recurso canónico

**Kluger y DeNisi (1996)**, la introducción y el resumen del modelo de tres niveles de control (tarea, motivación, meta-tarea o yo). Fijarse en qué hace que el feedback empeore (se centra en la persona, no en la tarea). Para el ciclo: **DeNisi y Murphy (2017)** como mapa. Las habilidades de dar feedback van en Comunicación.

---

## 5. Compensación e incentivos

### Fuentes

| Fuente | Tipo | URL / DOI | A/P/E/U | Marca |
|---|---|---|---|---|
| Jenkins, Gupta, Mitra y Shaw (1998), «Are financial incentives related to performance? A meta-analytic review of empirical research», *J. Applied Psychology* 83(5), 777 | primaria (39 estudios, 47 relaciones) | https://doi.org/10.1037/0021-9010.83.5.777 | 3/2/1/2 | [M] |
| Gerhart y Fang (2014), «Pay for (individual) performance: Issues, claims, evidence and the role of sorting effects», *Human Resource Management Review* 24(1), 41–52 | primaria (revisión) | https://doi.org/10.1016/j.hrmr.2013.08.010 | 3/2/2/2 | [M] (sin abstract; solo metadatos; no leí su contenido) |
| Deci, Koestner y Ryan (1999), «A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation», *Psychological Bulletin* 125(6), 627 | primaria (128 estudios) | https://doi.org/10.1037/0033-2909.125.6.627 | 3/3/2/2 | [M] |
| Gneezy y Rustichini (2000), «A fine is a price», *J. Legal Studies* 29(1) | primaria (experimento de campo) | la búsqueda por DOI no devolvió el original; solo reseñas; no verificado | 3/2/3/3 | [S] (no leído; ni el DOI ni las páginas verificados) |
| Adams (1963), «Towards an understanding of inequity», *J. Abnormal and Social Psychology* 67(5), 422–436 | primaria | **no verificado** (de memoria; no encontré el registro) | 3/2/1/2 | ninguna |
| Cullen (2024), «Is pay transparency good?», *J. Economic Perspectives* 38(1), 153 | primaria (revisión económica) | https://doi.org/10.1257/jep.38.1.153 | 3/3/2/3 | [M] |
| Bennedsen, Simintzi, Tsoutsoura y Wolfenzon (2022), «Do firms respond to gender pay gap transparency?», *J. Finance* 77(4), 2051–2091 | primaria (Dinamarca) | https://doi.org/10.1111/jofi.13136 | 3/2/2/2 | [M] |
| Kim y Ouimet (2014), «Broad-based employee stock ownership: Motives and outcomes», *J. Finance* 69(3), 1273–1319 | primaria (empresas cotizantes de EE. UU.) | https://doi.org/10.1111/jofi.12150 | 3/2/1/3 | [M] |

### Afirmaciones

- Jenkins et al.: «Financial incentives were not related to performance quality but had a corrected correlation of .34 with performance quantity.» Moderan el entorno (laboratorio, campo, simulación) y el marco teórico; el tipo de tarea no. https://doi.org/10.1037/0021-9010.83.5.777 [M]
- Gerhart y Fang (2014): título y revista confirmados; el mensaje central (el efecto del pago por desempeño es en buena parte *selección* de quién entra y se queda, no solo esfuerzo) lo sé por el título («the role of sorting effects»), pero no leí el texto: **no lo uso como afirmación**. https://doi.org/10.1016/j.hrmr.2013.08.010 [M]
- Deci, Koestner y Ryan: las recompensas «engagement-contingent, completion-contingent, and performance-contingent» socavaron significativamente la motivación intrínseca de elección libre (d = −0.40, −0.36 y −0.28); también las recompensas tangibles y esperadas. Los comentarios verbales positivos la aumentaron (d = 0.33 en conducta de elección libre; 0.31 en interés autorreportado). Los efectos tangibles fueron más dañinos en niños que en universitarios. https://doi.org/10.1037/0033-2909.125.6.627 [M] Muestras sobre todo de laboratorio, con niños y estudiantes; el mecanismo vive en Psicología.
- Gneezy y Rustichini (guardería con multas por buscar tarde a los niños: la multa aumentó los retrasos): lo conozco de memoria y de las reseñas; **no lo verifiqué** en el original. Una reseña lo encuadra como el estudio de referencia del «crowding out» (https://doi.org/10.15027/46589 [S], título confirmado, contenido no leído). Marcar «sin verificar» en la nota.
- Cullen (2024): desde 2000 el 71 % de los países de la OCDE aprobó políticas de transparencia salarial. La transparencia horizontal (entre colegas de un mismo trabajo) «narrowed coworker wage gaps» pero «led to counterproductive peer comparisons and caused employers to bargain more aggressively, lowering average wages»; la transparencia vertical (entre niveles) «can lead to more accurate and more optimistic beliefs about earnings potential, increasing employee motivation and productivity». https://doi.org/10.1257/jep.38.1.153 [M]
- Bennedsen et al.: la ley danesa de 2006 de estadísticas salariales por género redujo la brecha 2 puntos porcentuales (13 % de la media previa), sobre todo frenando el salario de los varones; el efecto en rentabilidad no fue significativo y la productividad bajó. https://doi.org/10.1111/jofi.13136 [M]
- Kim y Ouimet: las participaciones accionarias para empleados pequeñas (menos de 5 % de las acciones, empresas con empleados moderados) «increase the economic pie»; los efectos son más débiles cuando hay demasiados empleados por free-riding; «the average impacts are small because they are often implemented for nonincentive purposes». https://doi.org/10.1111/jofi.12150 [M] Son empresas cotizadas: no generaliza a startups ni a empresas de 2–50 personas.
- Opciones y participación para empleados (practicantes) y equidad de Adams: sin fuentes verificadas en estas rondas (ver huecos).

### Estado de la evidencia

- **Se sostuvo**: el pago contingente sube la cantidad pero no la calidad (Jenkins); las recompensas contingentes pueden bajar la motivación intrínseca en experimentos (Deci et al.) con efectos de tamaño moderado.
- **Se achicó**: Deci et al. son sobre todo laboratorio con estudiantes y niños; la generalización a salarios de adultos no está probada en esos datos.
- **En disputa**: cuánto del efecto del incentivo es esfuerzo y cuánto es selección (Gerhart y Fang, sin leer); cuánto de la transparencia es neta positiva (Cullen: la horizontal baja salarios medios, la vertical motiva).
- **Cayó**: sin datos en estas rondas.

### Recurso canónico

**Jenkins et al. (1998)** para «qué hacen los incentivos» y **Cullen (2024)** para transparencia. Fijarse en la diferencia entre cantidad y calidad (Jenkins), y entre transparencia horizontal y vertical (Cullen). El mecanismo del crowding out se enlaza a Psicología (Deci et al.).

---

## 6. Desarrollo de personas

### Fuentes

| Fuente | Tipo | URL / DOI | A/P/E/U | Marca |
|---|---|---|---|---|
| Allen, Eby, Poteet, Lentz y Lima (2004), «Career benefits associated with mentoring for proteges: A meta-analysis», *J. Applied Psychology* 89(1), 127 | primaria (metaanálisis) | https://doi.org/10.1037/0021-9010.89.1.127 | 3/3/2/3 | [M] |
| Eby, Allen, Evans, Ng y DuBois (2008), «Does mentoring matter? A multidisciplinary meta-analysis comparing mentored and non-mentored individuals», *J. Vocational Behavior* 72(2), 254– | primaria (metaanálisis) | https://doi.org/10.1016/j.jvb.2007.04.005 | 3/3/2/3 | [M] (sin abstract; solo metadatos) |
| Theeboom, Beersma y van Vianen (2014), «Does coaching work? A meta-analysis…», *J. Positive Psychology* 9(1), 1–18 (Crossref lo fecha 2013 en línea) | primaria | https://doi.org/10.1080/17439760.2013.837499 | 3/2/2/3 | [M] |
| Jones, Woods y Guillaume (2016), «The effectiveness of workplace coaching: A meta-analysis…», *J. Occupational and Organizational Psychology* 89(2), 249 | primaria | https://doi.org/10.1111/joop.12119 | 3/2/2/3 | [M] |
| Lacerenza, Reyes, Marlow, Joseph y Salas (2017), «Leadership training design, delivery, and implementation: A meta-analysis», *J. Applied Psychology* | primaria (335 muestras) | https://doi.org/10.1037/apl0000241 | 3/3/3/3 | [M] |
| Clardy (2018), «70-20-10 and the Dominance of Informal Learning: A Fact in Search of Evidence», *Human Resource Development Review* 17(2), 153–178 | primaria (revisión crítica) | https://doi.org/10.1177/1534484318759399 | 2/2/2/3 | [S] (la página del editor dio 403; el abstract lo vi citado en el buscador y no lo pude cotejar en la fuente) |
| ATD, «70:20:10: Where is the evidence?» | secundaria | https://www.td.org/insights/70-20-10-where-is-the-evidence | 1/1/1/1 | [S] (403 al abrirla; solo lo que muestra el buscador) |
| Lee, Willis y Tian (2018), «Empowering leadership: A meta-analytic examination…», *J. Organizational Behavior* 39(3), 306–325 | primaria (105 muestras) | https://doi.org/10.1002/job.2220 | 3/3/2/3 | [M] |

### Afirmaciones

- Allen et al. (2004): metaanálisis de beneficios del mentoreo para el protegido, objetivos (p. ej. compensación) y subjetivos (satisfacción de carrera). «The findings were generally supportive of the benefits associated with mentoring, but effect sizes associated with objective outcomes were small.» https://doi.org/10.1037/0021-9010.89.1.127 [M]
- Eby et al. (2008): confirmé el título y los datos de publicación; no leí el abstract ni resultados: no cito cifras. https://doi.org/10.1016/j.jvb.2007.04.005 [M]
- Theeboom et al.: el coaching «has significant positive effects on all outcomes with effect sizes ranging from g = 0.43 (coping) to g = 0.74 (goal-directed self-regulation)»; cinco categorías: desempeño y habilidades, bienestar, afrontamiento, actitudes laborales, autorregulación orientada a metas. https://doi.org/10.1080/17439760.2013.837499 [M]
- Jones et al. (k = 17): el coaching tuvo efectos positivos en resultados organizacionales «δ = 0.36» (habilidades .28; afectivos .51; resultados individuales 1.24). El efecto fue mayor con coaches internos que con externos y **menor** con retroalimentación multifuente; no hubo moderación por formato ni por duración. El análisis *excluye* el coaching del jefe al subordinado y entre pares, es decir, no es lo que hace un jefe con su equipo. https://doi.org/10.1111/joop.12119 [M]
- Lacerenza et al. (335 muestras): el entrenamiento de liderazgo «is substantially more effective than previously thought»; mejoras en reacciones (δ = .63), aprendizaje (δ = .73), transferencia (δ = .82) y resultados (δ = .72). Mejor con análisis de necesidades, feedback, varios métodos de entrega (sobre todo práctica), sesiones espaciadas, lugar en el sitio y presencial no autoadministrado. https://doi.org/10.1037/apl0000241 [M]
- 70-20-10: Clardy (2018) examina cinco tradiciones que parecen converger en que «70% or more of work-based learning occurs informally» y concluye que esa «70% rule» «needs to be set aside» (cita del buscador). Según la misma fuente secundaria, el origen es *The Career Architect Development Planner* de Lombardo y Eichinger, la cifra salió de una encuesta a gerentes exitosos que recordaban qué les sirvió, y Morgan McCall la llamó «folklore»; la «falta de datos empíricos» la atribuyen a Kajewski y Madsen (el buscador dice 2012; otro dato dice 2013; no verificado). https://journals.sagepub.com/doi/abs/10.1177/1534484318759399 ; https://www.td.org/insights/70-20-10-where-is-the-evidence [S]
- Delegar: Lee, Willis y Tian encuentran efectos positivos del liderazgo empoderador (105 muestras) sobre desempeño, ciudadanía organizacional y creatividad a nivel individual y de equipo, mediados por confianza en el líder y empoderamiento psicológico. https://doi.org/10.1002/job.2220 [M] Es una asociación; en gran parte, datos de encuesta.

### Estado de la evidencia

- **Se sostuvo**: el coaching tiene efecto medio positivo (dos metaanálisis, en un k chico y con calidad dispar); el mentoreo ayuda sobre todo en resultados subjetivos (Allen: lo objetivo es chico); el entrenamiento de liderazgo funciona, con matices de diseño.
- **Se achicó**: el mentoreo en lo objetivo.
- **Cayó**: el 70-20-10 como hecho (la cifra viene de recuerdos de gerentes exitosos, según una revisión crítica y su cobertura).
- **En disputa**: sin poder separar cuánto del efecto del coaching es expectativa (muestras chicas, sin ciego); no se evaluó coaching de jefe a empleado en Jones et al.
- **Hueco**: no hallé un estudio sobre delegar como práctica del jefe en pequeñas empresas.

### Recurso canónico

**Lacerenza et al. (2017)**, la parte de moderadores (qué diseño funciona), sobre todo práctica, feedback y sesiones espaciadas. Para coaching, **Jones et al. (2016)** por la diferencia entre coach interno y externo. Para 70-20-10, **Clardy (2018)** (a leer completo).

---

## 7. Rotación y salidas

### Fuentes

| Fuente | Tipo | URL / DOI | A/P/E/U | Marca |
|---|---|---|---|---|
| Griffeth, Hom y Gaertner (2000), «A meta-analysis of antecedents and correlates of employee turnover…», *J. Management* 26(3), 463 | primaria (metaanálisis) | https://doi.org/10.1177/014920630002600305 | 3/3/2/2 | [M] |
| Rubenstein, Eberly, Lee y Mitchell (2018), «Surveying the forest: A meta-analysis, moderator investigation, and future-oriented discussion of the antecedents of voluntary employee turnover», *Personnel Psychology* 71(1), 23– (OpenAlex lo fecha 2017 en línea) | primaria (metaanálisis) | https://doi.org/10.1111/peps.12226 | 3/3/2/3 | [M] |
| Hom, Lee, Shaw y Hausknecht (2017), «One hundred years of employee turnover theory and research», *J. Applied Psychology* 102(3), 530–545 | primaria (revisión histórica) | https://doi.org/10.1037/apl0000103 | 3/3/2/3 | [M] |
| Mitchell, Holtom, Lee, Sablynski y Erez (2001), «Why people stay: Using job embeddedness to predict voluntary turnover», *Academy of Management J.* 44(6), 1102 | primaria | https://doi.org/10.5465/3069391 | 3/2/2/3 | [M] (solo metadatos; sin abstract) |
| Jiken y Yusoff (2026), reseña integrativa de 39 trabajos sobre si «la gente se va de los jefes», probablemente en *Int. J. of Organizational Analysis* 34(12) (revista sin confirmar), con nota de Durham de 21-abr-2026 | primaria / secundaria | https://dur.ac.uk/business/news-and-events/news/2026/04/the-old-adage-that-people-leave-managers-not-companies-is-true--but-only-up-to-a-point/ | 2/1/1/3 | [S] (nota de prensa; no leí la reseña) |
| Gallup (Harter y Adkins, 2015) | **encuesta comercial** | https://www.gallup.com/workplace/236570/one-on-one-meetings.aspx | 1/1/1/1 | [S] |
| Culture Amp, «The biggest lie in HR: people quit managers» | **encuesta comercial** | https://www.cultureamp.com/blog/the-biggest-lie-people-quit-bosses | 1/1/1/2 | [S] (solo resultado del buscador) |
| Colquitt, Conlon, Wesson, Porter y Ng (2001), «Justice at the millennium: A meta-analytic review of 25 years of organizational justice research», *J. Applied Psychology* 86(3), 425–445 | primaria (183 estudios) | https://doi.org/10.1037/0021-9010.86.3.425 | 3/3/2/3 | [M] |
| Brockner et al. (1994), «Interactive effects of procedural justice and outcome negativity on victims and survivors of job loss», *Academy of Management J.* 37(2), 397–409 | primaria (tres estudios) | https://doi.org/10.2307/256835 | 3/2/2/3 | [M] (el abstract llegó cortado) |
| Horowitz (2010), «The right way to lay people off» | practicante | https://a16z.com/the-right-way-to-lay-people-off/ | 2/2/3/2 | [S] |

### Afirmaciones

- Griffeth et al. (2000) actualizan Hom y Griffeth (1995): «the most wide-ranging quantitative review to date of the predictive strength of numerous turnover antecedents» e identifican moderadores. No obtuve sus coeficientes (el abstract no los trae). https://doi.org/10.1177/014920630002600305 [M]
- Rubenstein et al. (2018): metaanálisis que actualiza efectos y suma nuevos antecedentes; encuentran que muchas relaciones antecedente-rotación son «context-dependent» y piden salirse del paradigma tradicional; no tengo las magnitudes (hueco: leer el texto). https://doi.org/10.1111/peps.12226 [M]
- Hom et al. (2017): resumen de la teoría en 100 años: primero métodos para reducir la rotación, luego teoría (mitad del siglo XX), luego psicología de *quedarse* (embeddedness) y rotación colectiva. https://doi.org/10.1037/apl0000103 [M]
- Mitchell et al. (2001, embeddedness): título y datos confirmados (4.200 citas según OpenAlex); no leí abstract ni cifras. Una revisión posterior: Lee, Burch y Mitchell (2014), «The story of why we stay: A review of job embeddedness», *Annual Review of Organizational Psychology and Organizational Behavior* 1(1), 199 (https://doi.org/10.1146/annurev-orgpsych-031413-091244, [M] solo metadatos).
- «La gente se va de los jefes»: Gallup (2015) dice «one in two left a job to get away from a manager» (7.272 adultos de EE. UU.) y que los gerentes explican «at least 70% of variance» del engagement (la nota dice «at least» en el cuerpo y «up to» en el resumen: inconsistencia interna). https://www.gallup.com/workplace/236570/one-on-one-meetings.aspx [S] Culture Amp señala que Gallup no hace públicos sus datos y que su propio estudio de 2017 puso «oportunidades de desarrollo» por delante de líderes y jefes, aunque después dijo que parte de esas afirmaciones no resistieron; su réplica de 2024 halló un efecto de amplificación de buen jefe más buenos líderes (resumen del buscador: https://www.cultureamp.com/blog/whats-driving-employee-retention/ [S]).
- La reseña de 2026 (39 trabajos de la última década): la rotación suele resultar «of both leadership and organisational conditions, not managers alone»; «leadership alone can be overpowered when workload remains high and resources are consistently below par»; «Retention improves when organisations see leadership and structural change as complementary levers in the same system.» Recomiendan cambios estructurales y fortalecer el liderazgo. Nota de prensa de Durham, [S].
- Cómo despedir y justicia: Colquitt et al. (183 estudios) encuentran que las dimensiones de justicia (distributiva, procedimental, interpersonal, informacional) están relacionadas pero aportan varianza incremental en la percepción de justicia, con relaciones con satisfacción, compromiso, ciudadanía, retiro y desempeño. https://doi.org/10.1037/0021-9010.86.3.425 [M] Brockner et al. (1994): tres estudios sobre el efecto interactivo de la justicia procedimental y la negatividad del resultado sobre los despedidos, los sobrevivientes y quienes sabían que iban a ser despedidos (lame ducks). https://doi.org/10.2307/256835 [M] (sin los resultados concretos: el abstract llegó cortado).
- Horowitz (2010), «The right way to lay people off» (resumen del lector web, no el texto original): decir que fue una falla de la empresa y no de las personas; que cada jefe despida a su gente; el CEO se dirige a todos y «the message is for the people who are staying»; «the people who stay will care deeply about how you treat their colleagues». Es práctica de un solo caso (tres rondas en su empresa). https://a16z.com/the-right-way-to-lay-people-off/ [S]
- Entrevistas de salida: no hallé evidencia en estas rondas (hueco).

### Estado de la evidencia

- **Se sostuvo**: la rotación voluntaria tiene muchos antecedentes y depende del contexto (Griffeth 2000; Rubenstein 2018); la justicia percibida importa (Colquitt).
- **Se achicó**: «la gente se va de los jefes»: el dato que lo sostiene es de una consultora que no abre sus datos; la reseña de 2026 lo matiza.
- **Cayó**: nada confirmado como caído.
- **En disputa**: peso del jefe vs condiciones estructurales (carga, desarrollo, pago).
- **Hueco**: magnitudes de los antecedentes y evidencia sobre entrevistas de salida.

### Derecho laboral argentino: límite (solo nota de frontera, sin detalle)

Este es un párrafo de límite: no reemplaza consulta con una persona abogada ni con un contador de sueldos.

- La Ley de Contrato de Trabajo **20.744** (texto ordenado por Decreto 390/1976, Bs. As. 13/5/1976) regula el contrato de trabajo; su **art. 245** fija la indemnización por antigüedad o despido sin justa causa: «un (1) mes de sueldo por cada año de servicio o fracción mayor de tres (3) meses». https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm [S] (leída vía lector web sobre un texto de 200.000 caracteres; el art. 245 lo vi en el tramo final y refleja ya la reforma).
- **Reforma vigente a 2026**: la **Ley 27.802 de Modernización Laboral** (sancionada 27-feb-2026 según el buscador; promulgada por Decreto 137/2026; **publicada en el Boletín Oficial el 6-mar-2026**) sustituyó el art. 245 (art. 51 de la ley): sigue «un mes de sueldo por cada año de servicio o fracción mayor de tres meses», con base de «la mejor remuneración mensual, normal y habitual devengada durante el último año», tope de «tres (3) veces el importe del salario mensual promedio» del convenio y piso del «sesenta y siete por ciento (67%)», y «la única reparación procedente». Crea además un **Fondo de Asistencia Laboral** con aportes patronales (1 % grandes, 2.5 % pymes, según la página del Boletín) cuya vigencia se fijó al 1-jun-2026, prorrogable hasta seis meses. https://www.boletinoficial.gob.ar/detalleAviso/primera/339128/20260306 [S] (la página tiene más de 200.000 caracteres; leí hasta unos 100.000; sanción y decreto no figuran en el tramo que vi: los tomo del buscador).
- **Estado judicial**: la CGT obtuvo una cautelar el 30-mar-2026 (juzgado laboral N.º 63) que suspendió artículos (la cifra varía: 43, 81 o 82); la jueza federal Macarena Marra Giménez la revocó (competencia) y la Cámara Contencioso Administrativo Federal, Sala IV, confirmó la revocación (nota iProfesional del 8-jul-2026: «sigue en efecto mientras se resuelve su constitucionalidad de fondo»). https://www.iprofesional.com/index.php/legales/459478-reforma-laboral-reves-judicial-feroz-cgt-queda-sin-margen [S]. El fondo sobre la constitucionalidad **sigue pendiente** a julio de 2026 y **no encontré nada posterior**. Un titular de Perfil sobre un per saltum rechazado por la Corte no lo pude confirmar con otra fuente.
- **Independencia de las fuentes**: el Boletín Oficial e InfoLeg son las dos fuentes oficiales del mismo texto; no son independientes entre sí (InfoLeg reproduce lo del Boletín). Se pide otra fuente independiente para el estado judicial o decirlo como una sola. Para el estado de la ley, **hay una sola cadena oficial más prensa**; fechar «a 2026-11-27, con última noticia verificada de julio de 2026».
- **Hueco**: no leí la ley completa; hay otros cambios (período de prueba, preaviso, banco de horas, indemnización en convenios) que no analizo. Conviene que la nota sea una frase de límite y un enlace.

### Recurso canónico

**Rubenstein et al. (2018)** como mapa de antecedentes; **Hom et al. (2017)** para ver cómo cambió la teoría; **Colquitt et al. (2001)** para justicia. Para despedir: Horowitz (2010) como práctica, con la salvedad de que es un solo caso. Fijarse en qué se mide como rotación (voluntaria vs involuntaria).

---

## Huecos principales

1. **Magnitudes**: no tengo coeficientes de Bauer et al. (2007), Griffeth et al. (2000), Rubenstein et al. (2018) ni de Eby et al. (2008); solo los abstracts. Leer los textos.
2. **Gerhart y Fang (2014)**, **Mitchell et al. (2001)**, **Adams (1963)** y **Gneezy y Rustichini (2000)**: sin abstract o sin verificar; no usar sus afirmaciones hasta leerlos.
3. **Empresa chica**: ninguna fuente separa por tamaño (2 a 50 personas). Contratar, evaluar y pagar en ese rango es extrapolación de estudios de empresas grandes.
4. **Sesgos al entrevistar**, **entrevistas de salida**, **delegar** como práctica y **opciones/participación para empleados en empresas chicas** no se cubrieron; algunos no se pudieron buscar por límite de rondas y consultas.
5. **Fuentes bloqueadas o de pago**: HBR (Cappelli y Tavis; Buckingham y Goodall), SAGE (Clardy) y ATD no se leyeron; las cifras de Deloitte y Adobe quedan sin verificar.
6. **Grove**, **Horowitz** y **Google re:Work**: no se leyó el texto original; las afirmaciones de práctica vienen de resúmenes.
7. **Evaluación**: sin estudio de campo que compare el ciclo anual con alternativas; la distribución forzada solo tiene simulación.
8. **Derecho**: estado judicial verificado hasta julio de 2026; no encontré nada de noviembre. Las dos fuentes oficiales no son independientes.
9. **Rogelberg y colegas sobre one-on-ones**: encontré un solo estudio de 2026 (transversal); no hay metaanálisis ni experimento.
10. **«La gente se va de los jefes»**: lo más citado es de encuestas comerciales; no encontré un metaanálisis que lo pruebe o refute directamente.
