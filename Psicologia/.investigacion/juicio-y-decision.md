# Vertical Juicio y decisión: informe de investigación

Fecha de la búsqueda: 2026-11-27. Alcance: dos sistemas, heurísticas y sesgos, teoría de las perspectivas, sobreconfianza, intuición experta, ruido. Frontera: UX y marketing.

## Cómo leer este informe

- Marcas de lectura: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o del buscador.
- Puntajes de 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).
- Las URL son enlaces DOI o de repositorio. Las verifiqué por el registro de metadatos (OpenAlex, Europe PMC, Crossref), que devolvió título, revista, año y DOI coincidentes. En varios casos la página del editor o PubMed/PMC no se pudo abrir desde acá (403, cookies o verificación anti-bot); no esquivé esos bloqueos. Por eso casi todo es [M].
- Lo que cito entre comillas va en el idioma original.

## Hallazgos principales

1. El marco de dos sistemas (sistema 1 / sistema 2) es una forma cómoda de hablar, no un mecanismo establecido. Sus propios defensores lo redefinieron a «Tipo 1 / Tipo 2» y sus críticos dicen que no tiene soporte empírico (disputa abierta).
2. Aversión a las pérdidas: está en disputa. La teoría de las perspectivas se replicó en 19 países (94% de los ítems), pero «las pérdidas pesan más que las ganancias» como principio general fue cuestionado en serio (Gal y Rucker 2018), y la defensa (Mrkva et al. 2020) concede moderadores.
3. Los nudges: Mertens et al. 2022 halló d = 0,45; Maier et al. 2022 dice que al corregir el sesgo de publicación no hay evidencia. Pero los propios autores, en su réplica, dicen que el Bayes factor es «undecided». La respuesta honesta es «incierto», no «no funcionan».
4. El efecto Dunning-Kruger, tal como se cuenta («los incompetentes se creen expertos»), está en disputa y la explicación de «doble carga» fue refutada en al menos un estudio; hay réplicas con datos mayores que sí encuentran un efecto pequeño.
5. Many Labs 2 (2018): solo 54% de 28 hallazgos replicaron y el tamaño mediano de efecto bajó de d = 0,60 a 0,15. Eso es el marco para leer todo el campo, no solo esta vertical.
6. El ruido (variabilidad entre jueces que deberían coincidir) es una idea distinta del sesgo. La cifra famosa (55% de diferencia mediana entre suscriptores de seguros) viene de una auditoría de empresa, no de un experimento publicado revisado por pares.

## Sobre el árbol propuesto

- «Dos sistemas» no es un componente del mismo nivel que los otros: es un marco teórico que atraviesa heurísticas, perspectivas e intuición. Conviene tratarlo como nota de «marco y críticas» y no como mecanismo.
- «Sobreconfianza» y «heurísticas y sesgos» se solapan: la sobreconfianza y la falacia de planificación suelen listarse entre los sesgos. Se justifican por separado porque tienen literatura propia (calibración, pronóstico de clase de referencia).
- El efecto Dunning-Kruger lo estudia el campo de la metacognición y la autoevaluación; está bien ubicarlo dentro de sobreconfianza, con aviso.
- «Intuición experta» y «ruido» tratan de la calidad del juicio (de personas y de organizaciones) más que de errores. Es consistente con cómo lo hace el campo en Kahneman y Klein 2009 y en el libro Noise. Se pueden agrupar como «cuándo confiar en el juicio».
- Las fronteras con UX y marketing (nudges, economía del comportamiento) están reservadas a esas ramas. Acá solo se deja el estado de la evidencia.

---

## 1. dos-sistemas

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Kahneman (2011), *Thinking, Fast and Slow*, libro | Divulgación del autor | [S] (no abrí el libro; solo hallé una reseña en Statistical Papers) | 2/3/3/2 | https://doi.org/10.1007/s00362-013-0533-y (reseña) |
| Evans y Stanovich (2013), «Dual-Process Theories of Higher Cognition: Advancing the Debate», Perspectives on Psychological Science | Primaria (revisión/defensa) | [M] | 3/3/2/3 | https://doi.org/10.1177/1745691612460685 |
| Keren y Schul (2009), «Two Is Not Always Better Than One», Perspectives on Psychological Science | Primaria (crítica) | [M] | 3/3/2/3 | https://doi.org/10.1111/j.1745-6924.2009.01164.x |
| Melnikoff y Bargh (2018), «The Mythical Number Two», Trends in Cognitive Sciences | Primaria (crítica) | [M] | 3/2/1/3 | https://doi.org/10.1016/j.tics.2018.02.001 |
| Comentario a Evans y Stanovich 2013 (Perspectives on Psychological Science) | Secundaria | [M] | 2/1/1/1 | https://doi.org/10.1177/1745691613483475 |

### Afirmaciones

- Defensa: Evans y Stanovich dicen que el marco «has been attacked as a category, incorrectly assuming there is a generic version that applies to all», y proponen que «rapid autonomous processes (Type 1) are assumed to yield default responses unless intervened on by distinctive higher order reasoning processes (Type 2). What defines the difference is that Type 2 processing supports hypothetical thinking and load heavily on working memory.» https://doi.org/10.1177/1745691612460685
- Crítica: Keren y Schul concluyen que «two-system models currently provide little scientific advance». https://doi.org/10.1111/j.1745-6924.2009.01164.x
- Crítica más reciente: Melnikoff y Bargh dicen que «the dual-process typology is a convenient and seductive myth». https://doi.org/10.1016/j.tics.2018.02.001
- Salida intermedia: un comentario sobre Evans y Stanovich sugiere que la evidencia apoya «quantitative differences rather than qualitatively distinct processes». https://doi.org/10.1177/1745691613483475
- Dato útil para la base: lo que la gente llama «sistema 1 / sistema 2» se redefinió en la literatura académica como Tipo 1 / Tipo 2 (con memoria de trabajo como criterio definitorio), que no es lo que describe la divulgación. https://doi.org/10.1177/1745691612460685

### Estado de replicación

No es un efecto replicable, es un marco. Disputa abierta: los autores de ambos lados siguen publicando. No encontré réplicas multisitio preregistradas de «el marco» (no corresponde).

### Recurso canónico

- Evans y Stanovich 2013, leer primero las cinco críticas y las respuestas, luego Keren y Schul 2009 y Melnikoff y Bargh 2018. Fijarse en qué propiedades se atribuyen a cada «tipo» y si son realmente conjuntas (autonomía, memoria de trabajo, rapidez).
- Evitar presentar el libro de Kahneman (2011) como fuente del estado actual: es de antes de las críticas citadas.

---

## 2. heuristicas-y-sesgos

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Tversky y Kahneman (1974), «Judgment under uncertainty: Heuristics and biases», Science 185 | Primaria fundacional | No pude abrir el abstract (403 en Science); verifiqué solo que existe en OpenAlex/Crossref | 3/3/3/3 | https://doi.org/10.1126/science.185.4157.1124 |
| Klein et al. (2014), Many Labs 1, Social Psychology | Réplica multisitio | [M] | 3/3/2/3 | https://doi.org/10.1027/1864-9335/a000178 |
| Klein et al. (2018), Many Labs 2, AMPPS | Réplica multisitio preregistrada | [M] | 3/3/2/3 | https://doi.org/10.1177/2515245918810225 |
| Gigerenzer y Gaissmaier (2011), «Heuristic decision making», Annual Review of Psychology | Revisión | [M] | 3/3/2/3 | https://doi.org/10.1146/annurev-psych-120709-145346 |
| Gigerenzer (1996), «On narrow norms and vague heuristics: A reply to Kahneman and Tversky», Psychological Review | Primaria (crítica) | [M] | 3/2/1/3 | https://doi.org/10.1037/0033-295x.103.3.592 |
| Morewedge et al. (2015), «Debiasing Decisions», Policy Insights from the Behavioral and Brain Sciences | Primaria (experimentos) | [M] | 2/2/2/3 | https://doi.org/10.1177/2372732215600886 |
| Anclaje: «50 Years of Anchoring Effects», metaanálisis (preprint PsyArXiv, 2023) | Metaanálisis, preprint sin revisión por pares | [M] | 2/3/1/3 | https://doi.org/10.31234/osf.io/teq7k |
| Revisión de 1974 en el volumen «Revisiting Tversky & Kahneman (1974)» (Springer, 2026) | Secundaria | [M] | 1/1/1/1 | https://doi.org/10.1007/978-3-032-30515-2_4 |

### Afirmaciones

- Fundacional: no pude leer el abstract original; el capítulo de 2026 resume que el texto «introduced a heuristic-based account of reasoning» y que su base son «hypothetical scenarios and controlled laboratory tasks», con preguntas sobre «ecological validity». https://doi.org/10.1007/978-3-032-30515-2_4 [M]
- Anclaje (el sesgo mejor sostenido): el metaanálisis analiza «2,601 total effect sizes (1,280 comparing high anchors against low anchors)» y halla un efecto grande «Hedges' g = 0.825, 95% CI [0.765, 0.884], I2 = 93.73%» que sigue grande «even after accounting for extensive publication bias». También dice que hay efectos «reduced (or null)» para el anclaje incidental, con números aleatorios, con incentivos o con intervenciones de debiasing. https://doi.org/10.31234/osf.io/teq7k (ojo: preprint)
- Many Labs 1: «13 classic and contemporary effects across 36 independent samples totaling 6,344 participants. In the aggregate, 10 effects replicated consistently. One effect – imagined contact reducing prejudice – showed weak support for replicability. And two effects – flag priming influencing conservatism and currency priming influencing system justification – did not replicate.» https://doi.org/10.1027/1864-9335/a000178
- Many Labs 1 incluyó anclaje y encuadre (ganancia vs pérdida); según un resumen del buscador, los efectos de anclaje y de «allowed/forbidden» fueron subestimados por los originales. No pude abrir el texto completo (403), así que no doy tamaños de efecto por sesgo. [S] Ver hueco.
- Many Labs 2: «15 (54%) of the replications provided evidence of a statistically significant effect in the same direction as the original finding», con «median comparable Cohen's ds were 0.60 for the original findings and 0.15 for the replications». https://doi.org/10.1177/2515245918810225
- Many Labs 2 incluyó el encuadre de Tversky y Kahneman (1981); según un resumen del buscador replicó con d = 0,40 (menor que el original). [S] No lo pude verificar contra el texto. Un metaanálisis de la réplica da g = 0,44 según la misma búsqueda [S].
- Disponibilidad, representatividad y sesgo de confirmación: no hallé réplicas multisitio de la formulación de 1974 ni del sesgo de confirmación. Declaro hueco; no afirmo estado de replicación.
- Crítica de Gigerenzer: «At issue is the imposition of unnecessarily narrow norms of sound reasoning that are used to diagnose so-called cognitive illusions and the continuing reliance on vague heuristics that explain everything and nothing.» https://doi.org/10.1037/0033-295x.103.3.592
- Gigerenzer y Gaissmaier: «ignoring part of the information can lead to more accurate judgments than weighting and adding all information, for instance for low predictability and small samples.» Y «individuals and organizations often rely on simple heuristics in an adaptive way». https://doi.org/10.1146/annurev-psych-120709-145346
- Racionalidad ecológica y «less-is-more» (Gigerenzer y Brighton 2009, «Homo heuristicus»): el resumen del buscador dice que los fenómenos «less-is-more» emergen del dilema sesgo-varianza. [S] La fuente existe en https://sites.socsci.uci.edu/~lpearl/courses/readings/GigerenzerBrighton2009_HomoHeuristicus.pdf pero solo la vi por el resumen del buscador.
- Debiasing: dos experimentos longitudinales con una sola intervención (juego de computadora o video). «Both kinds of interventions produced medium to large debiasing effects immediately (games ≥ −31.94% and videos ≥ −18.60%) that persisted at least 2 months later (games ≥ −23.57% and videos ≥ −19.20%). Games that provided personalized feedback and practice produced larger effects than did videos.» «Debiasing effects were domain general.» https://doi.org/10.1177/2372732215600886
- Debiasing, cautela: los dos experimentos son del mismo grupo; no hallé una réplica independiente en mis tres rondas. Los sesgos medidos fueron, en el experimento 1, bias blind spot, confirmación y error fundamental de atribución; en el 2, anclaje, representatividad y proyección social. Lo midieron con tareas parecidas a las de entrenamiento, así que la transferencia a decisiones reales no está mostrada. https://doi.org/10.1177/2372732215600886

### Estado de replicación

- Sostenido: anclaje (g ≈ 0,8 en metaanálisis, con aviso de preprint), encuadre de tipo ganancia/pérdida (en Many Labs 1 y 2, d = 0,40 en el segundo según [S]).
- Cayó: priming conductual de bandera y de dinero (Many Labs 1). Esto no es de la lista de sesgos del título, pero afecta a la divulgación de Kahneman (2011), que dedica un capítulo al priming; no verifiqué lo que Kahneman dijo después (hueco).
- En disputa: representatividad, disponibilidad y confirmación como mecanismos (no hallé réplica multisitio). La disputa de fondo es normativa: si desviarse de la lógica formal es un error (Gigerenzer 1996) o una adaptación (Gigerenzer y Gaissmaier 2011).

### Recurso canónico

- Qué es: Tversky y Kahneman 1974 (leer el artículo entero; son 10 páginas).
- Cómo falla: Many Labs 2 (leer la tabla por efecto) y Gigerenzer 1996.
- Qué conviene: Morewedge et al. 2015 con la cautela de que son experimentos del propio grupo y de corto plazo (2 meses).

---

## 3. teoria-de-las-perspectivas

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Kahneman y Tversky (1979), «Prospect theory: An analysis of decision under risk», Econometrica | Primaria fundacional | [M] (en la reedición de Cambridge 1988) | 3/3/3/3 | https://doi.org/10.1017/cbo9780511609220.014 |
| Ruggeri et al. (2020), «Replicating patterns of prospect theory for decision under risk», Nature Human Behaviour | Réplica multinacional | [M] | 3/3/2/3 | https://doi.org/10.1038/s41562-020-0886-x |
| Gal y Rucker (2018), «The Loss of Loss Aversion: Will It Loom Larger Than Its Gain?», Journal of Consumer Psychology | Primaria (crítica) | [M] | 3/3/2/3 | https://doi.org/10.1002/jcpy.1047 |
| Comentario a Gal y Rucker (2018), «Bringing (Contingent) Loss Aversion Down to Earth», Journal of Consumer Psychology | Crítica a la crítica | [M] | 2/2/1/2 | https://doi.org/10.1002/jcpy.1046 |
| Mrkva, Johnson, Gächter y Herrmann (2020), «Moderating Loss Aversion», Journal of Consumer Psychology | Primaria (defensa con datos) | [M] | 3/3/2/3 | https://doi.org/10.1002/jcpy.1156 |
| Replicación territorial 2025 (preprint PsyArXiv) | Réplica extendida, preprint | [M] | 1/2/2/2 | https://doi.org/10.31234/osf.io/z5n9g_v2 |

Nota: en el encargo, «Mrkva et al. 2020» figura sin los demás autores; el registro de Crossref los da como Mrkva, Johnson, Gächter y Herrmann.

### Afirmaciones

- Original: Kahneman y Tversky describen «several classes of choice problems in which preferences systematically violate the axioms of expected utility theory» y proponen una alternativa descriptiva. https://doi.org/10.1017/cbo9780511609220.014
- Réplica: «n = 4,098 participants, 19 countries, 13 languages ... The results replicated for 94% of items, with some attenuation. Twelve of 13 theoretical contrasts replicated, with 100% replication in some countries. Heterogeneity between countries and intra-individual variation highlight meaningful avenues for future theorizing.» Los autores concluyen que los fundamentos empíricos «replicate beyond any reasonable thresholds». https://doi.org/10.1038/s41562-020-0886-x
- Alcance de la réplica: usó los problemas originales de elección con dinero hipotético. No prueba por sí sola la aversión a las pérdidas como ley general en decisiones cotidianas.
- Crítica a la aversión a las pérdidas: «current evidence does not support that losses, on balance, tend to be any more impactful than gains.» https://doi.org/10.1002/jcpy.1047
- Crítica matizada: otros autores concuerdan en que «loss aversion is less robust and universal than has been assumed» y que el efecto de dotación y el sesgo de statu quo admiten explicaciones alternativas, pero disienten con la «overstated conclusion». https://doi.org/10.1002/jcpy.1046
- Defensa con datos: «Across five unique samples (N total = 17,720)... more domain knowledge and experience were associated with lower loss aversion, though people of all knowledge and experience levels were loss averse.» Los mayores eran más aversos. Concluyen que hay moderadores y que cuestionan que la aversión «is a fallacy». https://doi.org/10.1002/jcpy.1156
- Encuadre: ver sección anterior (replicó en Many Labs 1 y 2). Esa evidencia es de encuadre (cómo se describe el mismo problema), no de aversión a las pérdidas en sí.
- Réplica 2025 en decisiones territoriales (preprint): reproduce «certainty, framing, isolation and overweighting of small probabilities effects while providing evidence against the robustness of the reflection effect». https://doi.org/10.31234/osf.io/z5n9g_v2 Importante: la reflexión (invertir el riesgo entre ganancias y pérdidas) es lo más frágil; también aparece en la réplica de 2020 como atenuación.

### Estado de replicación

- Sostenido: la teoría de las perspectivas como patrón de elecciones en problemas hipotéticos, en 19 países (94% de ítems).
- En disputa: la aversión a las pérdidas como principio general (λ ≈ 2). Hay evidencia en ambos sentidos y consenso en que depende de moderadores (experiencia, tamaño, contexto).
- Frágil: el efecto de reflexión.

### Recurso canónico

- Ruggeri et al. 2020 para «qué replicó». Luego Gal y Rucker 2018 y Mrkva et al. 2020 como par: leer los dos, porque no están de acuerdo.
- Para el lector no especialista: decir «la teoría se sostiene en problemas de laboratorio; que las pérdidas duelan el doble en general está discutido».

---

## 4. sobreconfianza

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Moore y Healy (2008), «The trouble with overconfidence», Psychological Review | Primaria (teoría) | [M] | 3/3/2/3 | https://doi.org/10.1037/0033-295x.115.2.502 |
| Buehler, Griffin y Ross (1994), falacia de planificación | Primaria fundacional | No abrí el abstract; verifiqué su existencia por citas en otro estudio | 3/3/2/3 | cita en https://doi.org/10.1002/1099-0992(200011/12)30:6<873::aid-ejsp22>3.0.co;2-u |
| «Overcoming the planning fallacy through willpower» (2000), Eur. J. Soc. Psychol. (autoría no verificada por mí; el registro la cita como intenciones de implementación) | Primaria | [M] | 2/2/2/2 | https://doi.org/10.1002/1099-0992(200011/12)30:6<873::aid-ejsp22>3.0.co;2-u |
| Flyvbjerg (2006), «From Nobel Prize to Project Management: Getting Risks Right», Project Management Journal | Primaria, método | [M] | 2/3/3/3 | https://doi.org/10.1177/875697280603700302 |
| Kruger y Dunning (1999), «Unskilled and unaware of it», JPSP | Primaria fundacional | [M] | 3/3/2/3 | https://doi.org/10.1037/0022-3514.77.6.1121 |
| Gignac y Zajenkowski (2020), «The Dunning-Kruger effect is (mostly) a statistical artefact», Intelligence | Primaria (crítica) | [L] del abstract y primera página | 3/3/2/3 | https://doi.org/10.1016/j.intell.2020.101449 |
| McIntosh, Moore, Liu y Della Sala (2022), «Skill and self-knowledge», Royal Society Open Science | Primaria (crítica) | [S] (resumen del lector) | 3/2/2/3 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9727674 |
| Revisión del DK con datos de cohorte británica (J. Behav. Exp. Econ. 2025) | Primaria | [M] | 2/2/2/2 | https://doi.org/10.1016/j.socec.2025.102362 |

Los autores del estudio de 2000 no los verifiqué (el registro devolvió título, año y DOI, no la autoría). Ver hueco.

### Afirmaciones

- Tres formas: «(a) overestimation of one's actual performance, (b) overplacement of one's performance relative to others, and (c) excessive precision in one's beliefs.» En tareas difíciles la gente sobreestima su desempeño pero cree estar peor que otros; en fáciles, lo contrario. «Overprecision appears to be more persistent than either of the other 2 types.» https://doi.org/10.1037/0033-295x.115.2.502
- Falacia de planificación: la gente subestima el tiempo de sus tareas (Buehler, Griffin y Ross 1994, citado en https://doi.org/10.1002/1099-0992(200011/12)30:6<873::aid-ejsp22>3.0.co;2-u). Un estudio con intenciones de implementación (dónde y cuándo) redujo el sesgo óptimo en la predicción (mejoró el cumplimiento) en ese experimento; es un solo estudio.
- Pronóstico de clase de referencia: Flyvbjerg describe un método que «achieves accuracy by basing forecasts on actual performance in a reference class of comparable projects and thereby bypassing both optimism bias and strategic misrepresentation», aplicado a proyectos de infraestructura de transporte. https://doi.org/10.1177/875697280603700302 (la fuente es un caso aplicado, no un ensayo controlado)
- Dunning-Kruger, original: «Although their test scores put them in the 12th percentile, they estimated themselves to be in the 62nd» (cuartil inferior en humor, gramática y lógica). https://doi.org/10.1037/0022-3514.77.6.1121
- Crítica estadística: el método habitual «has been argued to be confounded by the better-than-average effect and regression toward the mean». Con N = 929 y el test de Raven, no hallaron heterocedasticidad y «the association between objectively measured intelligence and self-assessed intelligence was found to be essentially entirely linear»; concluyen que el efecto «may be much smaller than reported previously». https://doi.org/10.1016/j.intell.2020.101449 [L del abstract]
- Segunda crítica: con 151 participantes y tarea de matrices, los peores en desempeño estaban menos confiados, no más; los autores dicen que el efecto clásico es «largely a statistical regression artefact» y refutan la «doble carga». https://pmc.ncbi.nlm.nih.gov/articles/PMC9727674 [S]
- Réplica a favor del efecto: con datos de una cohorte británica de nacimiento, «We replicate their models and show that the DKE exists in our secondary data». https://doi.org/10.1016/j.socec.2025.102362 Un resumen del buscador dice que Dunkel, Nedelec y van der Linden (2023) hallaron un efecto pequeño pero significativo con datos nacionales; no abrí ese artículo. [S]

### Estado de replicación

- Sostenido: sobreprecisión (la más persistente según Moore y Healy), sobreestimación en tareas difíciles; la falacia de planificación es un hallazgo antiguo y citado, sin metaanálisis que yo haya leído (hueco).
- En disputa: Dunning-Kruger. La versión popular («los menos capaces se creen más capaces que los expertos») no la sostienen los datos; queda un efecto pequeño o artefacto según el método. La explicación de metacognición deficiente fue refutada en un estudio.

### Recurso canónico

- Moore y Healy 2008 (el modelo que ordena las tres formas). Fijarse en que dependen de la dificultad de la tarea: no es «la gente se cree mejor».
- Flyvbjerg 2006 para el método de la clase de referencia.
- Para DK: Gignac y Zajenkowski 2020, leyendo el abstract y el gráfico de cuartiles.

---

## 5. intuicion-experta

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Kahneman y Klein (2009), «Conditions for intuitive expertise: a failure to disagree», American Psychologist | Primaria canónica | [M] (el texto completo no se pudo abrir) | 3/3/3/3 | https://doi.org/10.1037/a0016755 |

### Afirmaciones

- «Starting from the obvious fact that professional intuition is sometimes marvelous and sometimes flawed, the authors attempt to map the boundary conditions that separate true intuitive skill from overconfident and biased impressions. They conclude that evaluating the likely quality of an intuitive judgment requires an assessment of the predictability of the environment in which the judgment is made and of the individual's opportunity to learn the regularities of that environment. Subjective experience is not a reliable indicator of judgment accuracy.» https://doi.org/10.1037/a0016755
- Es un acuerdo entre dos escuelas que se creían opuestas: heurísticas y sesgos (Kahneman) y toma de decisiones naturalista (Klein).
- No leí los ejemplos concretos del texto (qué profesiones tienen entornos válidos) ni cifras. Un intento de bajar el PDF del sitio del autor devolvió vacío. Esta es la fuente más importante de la vertical y quedó sin lectura completa.

### Estado de replicación

No aplica en el sentido de un efecto: es un marco condicional de dos criterios (entorno predecible y práctica con retroalimentación). No hallé réplicas ni pruebas formales; es una propuesta de consenso de expertos. Marco útil, no teorema.

### Recurso canónico

- Kahneman y Klein 2009 completo: leer la sección de «validity of the environment» y la lista de ejemplos de entornos de alta y baja validez.

---

## 6. ruido

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Kahneman, Sibony y Sunstein (2021), *Noise: A Flaw in Human Judgment*, libro | Divulgación de autores | [S] (reseña en Numeracy; no abrí el libro) | 2/3/3/3 | https://doi.org/10.5038/1936-4660.15.2.1422 (reseña) |
| Kahneman, Rosenfield, Gandhi y Blaser (2016), «Noise: How to Overcome the High, Hidden Cost of Inconsistent Decision Making», Harvard Business Review | Primaria resumida (artículo de gestión) | [S] (la página solo trae la presentación) | 2/2/2/2 | https://hbr.org/2016/10/noise |
| «How noisy is your company?», strategy+business | Secundaria | [S] | 1/1/2/1 | https://www.strategy-business.com/article/How-noisy-is-your-company |

### Afirmaciones

- La reseña dice que los autores demuestran «the pervasiveness and harmfulness of unwanted internal variability or noise» y que, pese a objeciones de costo, dificultad y deshumanización, reducirlo es imperativo para la equidad. https://doi.org/10.5038/1936-4660.15.2.1422
- Auditoría de ruido en seguros: «55%: median difference in pricing that underwriters set for identical policies»; «43%: median difference in payouts that claims adjusters set for identical claims». https://www.strategy-business.com/article/How-noisy-is-your-company [S] Una búsqueda adicional dice que los ejecutivos esperaban alrededor de 10%; Kahneman en una entrevista de 2022 lo describió como «closer to 50%». [S] (hay dos cifras en circulación: 55% en el libro y artículos, ~50% en la entrevista)
- Tipos: el artículo de strategy+business lista ruido de nivel, de patrón y de ocasión (level, pattern, occasion noise). https://www.strategy-business.com/article/How-noisy-is-your-company
- Ruido vs. sesgo: el ruido es variabilidad no deseada entre juicios que deberían coincidir; el sesgo es un error sistemático en una dirección. No encontré en las fuentes abiertas una definición literal de los autores del contraste; está en el libro, que no leí. Declaro hueco.
- Reducción: HBR 2016 propone auditar el ruido. No pude leer el texto completo del artículo, así que no afirmo cuáles son las recomendaciones («higiene de decisiones») ni su evidencia.

### Estado de replicación

No hay réplica independiente publicada que haya encontrado de la auditoría de seguros; las cifras vienen de datos de una empresa que no pude revisar. Es una idea con apoyo en estadística básica (la varianza se descompone), pero el tamaño empírico en cada rubro es dato anecdótico hasta ver los datos. Una reseña académica es favorable; no encontré una crítica metodológica en mis rondas (hueco).

### Recurso canónico

- El libro *Noise* (2021), capítulos 1 a 6 (qué es el ruido y su auditoría) y la parte de «higiene de decisiones». La versión corta es HBR 2016. Fijarse en que la auditoría de ruido pide juicios independientes sobre los mismos casos.

---

## Fronteras (solo mencionadas)

### Nudges y economía del comportamiento (rama marketing y UX)

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Mertens, Herberz, Hahnel y Brosch (2022), «The effectiveness of nudging», PNAS | Metaanálisis | [M] | 3/3/3/3 | https://doi.org/10.1073/pnas.2107346118 |
| Maier, Bartoš, Stanley, Shanks, Harris y Wagenmakers (2022), «No evidence for nudging after adjusting for publication bias», PNAS | Carta (sin abstract en PubMed) | [S] | 3/2/2/3 | https://doi.org/10.1073/pnas.2200300119 |
| Réplica de los autores, «Rejoinder – No Evidence for Nudging After Adjusting for Publication Bias» | Secundaria del propio grupo | [S] | 2/2/2/2 | https://bayesianspectacles.org/rejoinder-no-evidence-for-nudging |

- Mertens et al.: «more than 200 studies reporting over 450 effect sizes (n = 2,149,683)»; efecto global «Cohen's d = 0.45 (95% CI [0.39, 0.52])»; los nudges que cambian la estructura de las opciones superan a los que cambian la información o refuerzan intenciones; alimentos hasta 2,5 veces más; «a moderate publication bias toward positive results». https://doi.org/10.1073/pnas.2107346118
- Maier et al.: es una carta (PubMed la lista sin abstract); el argumento es que el sesgo de publicación que halló Mertens es el hallazgo central y que, corregido, no hay evidencia de nudging. https://doi.org/10.1073/pnas.2200300119 [S]
- Los mismos autores, en su réplica: «the Bayes factor that we observe for nudging overall is undecided», que «does not provide evidence in favour of nudges, but it also does not provide evidence against nudges»; «after correcting for bias only 21.5% of academic nudge effects are larger than d = 0.3»; y un ejemplo en que d = 1,18 se reduce a 0,07. https://bayesianspectacles.org/rejoinder-no-evidence-for-nudging [S]
- Estado: en disputa. Lo que sí está claro: el d = 0,45 inflado por sesgo de publicación; lo que no: cuánto vale el efecto real y en qué dominios.
- La traducción a interfaces y marketing (opciones por defecto, arquitectura de la elección) es de esas ramas; acá solo se deja el aviso de que la evidencia depende de esta disputa.

### Clínica

Fuera del alcance. Lo único que toca a esta vertical es que «sesgo cognitivo» tiene otro sentido en terapia cognitiva; no lo investigué.

---

## Huecos

1. **Many Labs 1 por efecto.** No pude abrir el texto completo (403 en Hogrefe, unipd y core.ac.uk). No tengo tamaños de efecto por sesgo ni confirmo cuáles de anclaje, encuadre, costos hundidos y «allowed/forbidden» entraron y cómo les fue. Solo tengo lo de [S]. Pendiente: bajar de OSF (osf.io/wx7ck, según lo indica una búsqueda).
2. **Many Labs 2 por efecto**, igual: el abstract no dice qué efectos de juicio y decisión fallaron.
3. **Tversky y Kahneman 1974 y Kahneman y Tversky 1979**: no leí el abstract original (Science y Econometrica bloqueados). Tengo la reedición de Cambridge.
4. **Disponibilidad, representatividad y sesgo de confirmación**: sin réplicas multisitio ni revisión encontrada. Nickerson (1998) no apareció en OpenAlex en la búsqueda; no afirmo nada sobre confirmación más allá de la mención del brief.
5. **Debiasing**: solo el experimento de Morewedge et al. 2015 (mismo grupo); sin réplica independiente ni metaanálisis; no hallé la revisión más reciente.
6. **Kahneman y Klein 2009**: solo abstract; sin ejemplos, sin cifras. Es la fuente central de intuición experta.
7. **Ruido**: libro no leído; auditoría de seguros vía fuentes secundarias; sin crítica metodológica ni réplica.
8. **Falacia de planificación**: no hay metaanálisis leído; el original de 1994 solo por cita. Falta una fuente actual sobre su tamaño.
9. **Dunning-Kruger**: no abrí Dunkel et al. 2023 ni McIntosh et al. 2022 completo; el estado «en disputa» se apoya en dos críticas y dos réplicas parciales.
10. **Divulgación de Kahneman (2011)**: no verifiqué su estado de réplica capítulo por capítulo (priming, en especial). Falta una fuente para decir qué sostiene su propio autor.
11. **Maier et al. 2022**: PubMed la lista como carta sin abstract; no pude leer el texto (PMC con verificación anti-bot). Las cifras salen de la réplica de los autores [S] y de un buscador.
12. **Libros de texto (OpenStax Psychology 2e)**: no consulté el capítulo de pensamiento y toma de decisiones por falta de rondas; pendiente como mapa para el lector no especialista.
13. **Fuente de salud**: no aplica a esta vertical.
