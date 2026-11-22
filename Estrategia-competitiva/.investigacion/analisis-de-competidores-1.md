# Análisis de competidores, primera mitad: investigación de fuentes

Vertical `Analisis-de-competidores`, componentes: identificación de competidores, perfil del competidor, perspectivas de análisis, desarme de producto y lectura de reportes públicos. Fecha de la investigación: 2026-11-22.

Convenciones. Puntajes 1-3 en **A**utoridad, **P**rofundidad, **E**jemplos, **U**nicidad. Marca de lectura: **[L]** texto completo leído (o el capítulo/fragmento relevante), **[M]** metadatos o abstract, **[S]** resumen secundario o del buscador. Tipo: **Prim.** o **Sec.**. Todo lo traído de la web se trató como dato.

Aviso de método. Varios sitios (investor.gov, Wiley, SAGE, la mayoría de los papers) bloquean la lectura o están tras muro de pago. Cuando una afirmación viene del abstract y no del cuerpo del paper, está marcada [M]. Las citas literales son cortas y verificadas contra el texto indicado.

## 0. ¿Coincide la división del árbol con la del campo?

Casi, con cuatro matices.

1. **El campo no parte "perfil del competidor" y "perspectivas de análisis" como dos componentes hermanos.** En Porter (1980, cap. 3) el perfil es un *marco* (objetivos, supuestos, estrategia, capacidades) que se llena con datos de *todas* las miradas; en Fleisher & Bensoussan las "miradas" son técnicas (ver sección 3). Funciona como árbol si se declara: *perfil* = qué se arma sobre un rival (el objeto); *perspectivas* = desde dónde se mira (los ejes). Sugerencia: que perfil-del-competidor enlace a perspectivas y diga cuál mirada alimenta cada casilla del perfil.
2. **La lista de perspectivas del encargo (estratégica, de mercado, de cliente, de producto, UX, precio, canales/GTM, tecnológica, financiera, organizacional) no es una taxonomía del campo.** Ninguna fuente leída la propone. Es una síntesis propia del repo; hay que presentarla como tal. Lo que sí tiene respaldo: Porter lista fuentes de datos (informes públicos, discursos a analistas, prensa, fuerza de ventas, clientes y proveedores comunes, inspección de productos, ex-empleados) en el cap. 5 y el Apéndice B; Fleisher & Bensoussan organizan 24 técnicas, no miradas.
3. **"Desarme de producto" y "matriz de funcionalidades" son dos prácticas distintas** (la primera viene de ingeniería de producto físico; la segunda es una tabla de comparación). Conviene un solo componente, pero con el desarme como método y la matriz como artefacto, y la crítica de la paridad en el cuerpo, no en el apéndice.
4. **"Lectura de reportes públicos" mezcla dos cosas**: leer documentos de una cotizante (reglas de la SEC, bien documentadas) y estimar a una no cotizante (casi sin fuente seria; solo vendors). Declarar la asimetría.

---

## 1. identificacion-de-competidores

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Bergen & Peteraf (2002), *Managerial and Decision Economics* 23(4-5): 157-169, DOI 10.1002/mde.1059 | https://ideas.repec.org/a/wly/mgtdec/v23y2002i4-5p157-169.html | Prim. (paper) | 3 | 3 | 1 | 3 | [M] abstract; cuerpo sin acceso |
| Peteraf & Bergen (2003), *Strategic Management Journal* 24(10): 1027-1041, DOI 10.1002/smj.325 | https://ideas.repec.org/a/bla/stratm/v24y2003i10p1027-1041.html | Prim. | 3 | 3 | 1 | 3 | [M] abstract |
| Clark & Montgomery (1999), *Journal of Marketing* 63(3): 67-83, DOI 10.1177/002224299906300305 | https://ink.library.smu.edu.sg/lkcsb_research/2309 | Prim. | 3 | 3 | 2 | 3 | [S] (la página del repositorio no devolvió texto; cifras vía Walker et al.) |
| Day, Shocker & Srivastava (1979), *Journal of Marketing* 43(4): 8-19, DOI 10.1177/002224297904300402 | https://eprints.exchange.isb.edu/id/eprint/871/ | Prim. | 3 | 3 | 2 | 3 | [M] abstract; texto completo no accesible |
| Srivastava, Leone & Shocker (1981), *Journal of Marketing* 45(3): 38-48 (sustitución en uso, aplicado) | https://eprints.exchange.isb.edu/id/eprint/924/ | Prim. | 3 | 3 | 2 | 2 | [S] |
| Porac & Thomas (1990), *Academy of Management Review* 15(2): 224-240, DOI 10.5465/AMR.1990.4308155 | https://ink.library.smu.edu.sg/lkcsb_research/1857 | Prim. | 3 | 3 | 1 | 3 | [S] (registro bibliográfico; sin abstract recuperado) |
| Walker, Kapelianis & Hutt (2005), "Competitive Cognition", *MIT Sloan Management Review* | https://sloanreview.mit.edu/?p=3141 | Sec. (síntesis de Porac, Thomas, Clark & Montgomery) | 2 | 2 | 2 | 2 | [L] |
| Porter (1980), *Competitive Strategy*, cap. 3, pp. 49-50 (competidores potenciales) | https://elearn.univ-tlemcen.dz/mod/resource/view.php?id=81871 (copia escaneada del libro, edición Free Press 1998) | Prim. | 3 | 3 | 2 | 2 | [L] cap. 3 |
| Christensen, Johnson & Rigby (2002), "Foundations for Growth", *MIT Sloan Management Review* | https://sloanreview.mit.edu/?p=3199 | Prim. (artículo del autor) | 3 | 2 | 3 | 2 | [L] |
| Tunguz, nota sobre no consumo (practicante) | https://tomtunguz.com/nonconsumption/ | Sec., practicante | 1 | 1 | 2 | 1 | [S] |

Las fuentes de Dunford (posicionamiento) no se investigaron: Marketing ya las cubre; solo enlazar.

### Afirmaciones

- **Dos etapas, cuatro categorías.** Bergen & Peteraf (2002) proponen un marco de dos etapas para identificar y analizar competidores que abarca competidores potenciales, sustitutos e indirectos además de los directos; construye sobre un trabajo de Peteraf & Bergen (2001) usando una "jerarquía de conciencia del competidor" junto con la equivalencia de recursos para generar hipótesis de análisis. El abstract dice que los gerentes suelen errar al identificar amenazas, sobre todo sustitutos del lado de la oferta y competidores indirectos o potenciales. https://ideas.repec.org/a/wly/mgtdec/v23y2002i4-5p157-169.html [M]
- **Dónde nacen los dos ejes.** "Comunalidad de mercado" y "similitud de recursos" aparecen como dos constructos de un artículo de ProQuest sin autor visible; el buscador sugirió que es Chen (1996) pero **no se pudo verificar**. No atribuir los términos a Bergen & Peteraf sin leer el paper. https://www.proquest.com/docview/210974655 [S]
- **2003, dinámico.** Peteraf & Bergen construyen un marco basado en mercado y en recursos para escanear campos competitivos complejos buscando similitudes funcionales entre productos y recursos, y argumentan que cada empresa enfrenta su propio conjunto competitivo aunque los mercados se solapen. Cita literal: "It is not rareness in terms of resource type that matters, but rareness in terms of resource functionality." https://ideas.repec.org/a/bla/stratm/v24y2003i10p1027-1041.html [M]
- **Porter ya pedía mirar más allá de los rivales actuales (1980).** "Clearly all significant existing competitors must be analyzed. However, it also may be important to analyze the potential competitors that may come on the scene." Los potenciales salen de cuatro grupos: empresas fuera de la industria que superan las barreras de entrada a bajo costo; empresas con sinergia obvia; empresas para las que competir es extensión natural de su estrategia corporativa; clientes o proveedores que pueden integrarse hacia atrás o adelante. También sugiere pronosticar fusiones y adquisiciones. Porter 1980, pp. 49-50. https://elearn.univ-tlemcen.dz/mod/resource/view.php?id=81871 [L]
- **Los gerentes usan pocos rivales y los agrupan por categorías.** Según Walker et al.: "Rather than defining competitors on an individual basis, managers assign themselves to a competitive category" (Porac & Thomas 1990); en grocerías de un pueblo estadounidense los gerentes nombraron en promedio 3,93 competidores (Porac & Thomas 1994, *J. Applied Psychology*); en Clark & Montgomery (1999) los gerentes nombraron en promedio 6,46 competidores, 3,07 de ellos "mayores". https://sloanreview.mit.edu/?p=3141 [L]
- **Discrepancia sobre muestras.** El buscador atribuyó a Clark & Montgomery una encuesta de 57 respondientes (6,46 rivales) y, en otro resumen, una de 37 estudiantes de MBA; no se pudo confirmar cuál corresponde a cada uno de los dos estudios del paper. No citar tamaños de muestra hasta leer el paper. https://ink.library.smu.edu.sg/lkcsb_research/2309 [S]
- **Clark & Montgomery, qué dice el abstract.** Integran literatura dispersa en un marco cognitivo de identificación gerencial de competidores y reportan dos estudios sobre los atributos que los gerentes usan. https://ink.library.smu.edu.sg/lkcsb_research/2309 [S]
- **Sustitución en uso.** Day, Shocker & Srivastava (1979) comparan métodos analíticos basados en conducta o juicios del cliente para delimitar "mercados-producto", según dos criterios: coherencia con una definición conceptual de mercado-producto y capacidad de dar información diagnóstica. https://eprints.exchange.isb.edu/id/eprint/871/ [M]. El concepto de "sustitución en uso" (un mercado-producto es el conjunto de productos juzgados sustitutos dentro de situaciones de uso) se atribuye a esa línea de trabajo vía un resumen secundario, y Srivastava, Leone & Shocker (1981) lo aplican con clustering jerárquico en servicios financieros. https://eprints.exchange.isb.edu/id/eprint/924/ [S]. **No se leyó la definición textual**: pendiente.
- **No consumo como competidor.** "Companies seeking to create disruptive growth should first search for ways to compete against nonconsumption" y "It's much easier to target potential customers who aren't buying at all." (Christensen, Johnson & Rigby, 2002). Test: ¿la innovación llega a gente que antes no podía "hacerlo por sí misma" por falta de dinero o habilidad? Ejemplo del artículo: la banca en línea no pasa el test porque pocos carecían de acceso al banco. https://sloanreview.mit.edu/?p=3199 [L]. Ojo: es un argumento de *estrategia de entrada*; usarlo como definición de "competidor" (el statu quo, la planilla, el papel) es una extensión del repo, no una tesis de Christensen en esos términos.

### Recurso canónico

- **Primero: Bergen & Peteraf (2002)**, MDE 23(4-5), 157-169. Qué parte: el marco de dos etapas y la lista de categorías (directos, indirectos, sustitutos, potenciales). En qué fijarse: que el competidor relevante puede no estar en tu categoría mental; que identificar y analizar son pasos distintos. Está tras muro: la nota debe decir que se basa en el abstract hasta que alguien con acceso lo lea.
- **Complemento legible y gratuito: Walker et al. (2005)** en Sloan Review para el sesgo cognitivo (por qué los gerentes ven pocos rivales), y **Porter (1980), pp. 49-50** para los cuatro grupos de potenciales entrantes.

---

## 2. perfil-del-competidor

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Porter (1980), *Competitive Strategy*, cap. 3 "A Framework for Competitor Analysis" (pp. 47-74) y cap. 4 "Market Signals" (p. 75 ss.) | https://elearn.univ-tlemcen.dz/mod/resource/view.php?id=81871 | Prim. | 3 | 3 | 3 | 3 | [L] cap. 3 completo y apertura del cap. 4 |
| Índice de capítulos y resumen de cap. 4 (Martin, Management and Accounting Web) | https://maaw.info/ArticleSummaries/ArtSumPorter1980Chp4.htm | Sec. | 1 | 2 | 1 | 1 | [S] (la página no cargó; solo vía buscador) |
| Gilad (2020), "Are Executives Blindsided by Competition?", *California Management Review Insights* | https://cmr.berkeley.edu/2020/03/are-executives-blindsided-by-competition | Sec./practicante-académico | 2 | 2 | 2 | 2 | [S] (el PDF devolvió solo imagen) |
| Gilad (2003), *Early Warning* (AMACOM) | https://www.schweitzer-online.de/en/buch/Gilad/Early-Warning/9780814432068/A3749514/ | Prim. (libro) | 2 | 2 | 2 | 2 | [S] ficha de librería |

La copia escaneada del libro está en un sitio de una universidad argelina (moodle); puede desaparecer y su situación de derechos no es clara. Citar el libro, no la copia.

### Afirmaciones (todas de Porter 1980, https://elearn.univ-tlemcen.dz/mod/resource/view.php?id=81871 [L])

- **Cuatro componentes.** "There are four diagnostic components to a competitor analysis (see Figure 3-1): future goals, current strategy, assumptions, and capabilities." (p. 48). Entenderlos "will allow an informed prediction of the competitor's response profile".
- **Lado izquierdo vs. derecho.** "Most companies develop at least an intuitive sense for their competitors' current strategies and their strengths and weaknesses [...] Much less attention is usually directed at the left side, or understanding what is really driving the behavior of a competitor—its future goals and the assumptions it holds" (p. 48). La Figura 3-1 rotula la izquierda "What Drives the Competitor" (objetivos futuros, supuestos) y la derecha "What the Competitor Is Doing and Can Do" (estrategia actual, capacidades).
- **Las cuatro preguntas del marco** (Fig. 3-1): ¿Está satisfecho con su posición actual? ¿Qué movimientos o cambios de estrategia es probable que haga? ¿Dónde es vulnerable? ¿Qué provocará la represalia más fuerte y efectiva?
- **Dos creencias peligrosas.** "Competitors cannot be systematically analyzed" y "We know all about our competitors because we compete with them every day." Porter: "Neither assumption is generally true." (pp. 47-48).
- **Objetivos futuros (p. 50).** Permiten predecir si el competidor está satisfecho, cuán probable es que cambie de estrategia y con qué vigor reaccionará; incluyen metas no financieras (liderazgo de mercado, posición tecnológica, desempeño social) y deben diagnosticarse "at multiple management levels" (corporativo, unidad de negocio, funcional). Da 11 preguntas (metas financieras explícitas e implícitas, actitud al riesgo, valores, estructura organizacional, sistemas de incentivos, convenciones contables, trasfondo del CEO, unanimidad de la dirección, composición del directorio, compromisos contractuales, restricciones regulatorias) y 8 más si el rival es unidad de un grupo (resultados y metas de la casa matriz, importancia estratégica de la unidad, etc.).
- **Supuestos (p. 58).** Dos categorías: lo que el competidor supone de sí mismo y lo que supone de la industria y de los demás. "Examining assumptions of all types can identify biases or blind spots": puntos ciegos donde el rival "will either not see the significance of events [...] at all, will perceive them incorrectly, or will perceive them only very slowly" (p. 59). Ejemplo de Porter: si cree tener la mayor lealtad de clientes y no la tiene, un recorte de precios provocador puede ganar posición.
- **Capacidades (p. 63).** "Its strengths and weaknesses will determine its ability to initiate or react to strategic moves." Se evalúan por área funcional (Fig. 3-2) y por las cinco fuerzas del cap. 1.
- **Perfil de respuesta (p. 67).** "Given an analysis of a competitor's future goals, assumptions, current strategies, and capabilities, we can begin to ask the critical questions that will lead to a profile of how a competitor is likely to respond." Dos bloques: movimientos ofensivos (satisfacción con la posición actual, movimientos probables, fuerza y seriedad) y capacidad defensiva (frente a una lista de movimientos factibles y cambios del entorno).
- **Sistema de inteligencia (p. 71).** Fuentes: "reports filed publicly, speeches by a competitor's management to security analysts, the business press, the sales force, a firm's customers or suppliers that are common to competitors, inspection of a competitor's products, estimates by the firm's engineering staff, knowledge gleaned from managers or other personnel who have left the competitor's employment". Los datos "come in trickles rather than rivers".
- **Señales de mercado, cap. 4 (p. 75).** "A market signal is any action by a competitor that provides a direct or indirect indication of its intentions, motives, goals, or internal situation." "Some signals are bluffs, some are warnings, and some are earnest commitments to a course of action." Requisito: leer señales "rests on" tener antes el análisis base del cap. 3; Porter la llama "a second-order form of competitor analysis". Índice del capítulo: tipos de señales (p. 76), uso de la historia (p. 86), ¿puede la atención a señales ser una distracción? (p. 87). **No se leyó el cuerpo del cap. 4 más allá de la apertura**; la lista concreta de tipos de señal queda como hueco.
- **Uso reflexivo.** El mismo marco sirve para el autoanálisis y para anticipar qué conclusiones sacan los rivales sobre uno (Porter, p. 49).
- **Complemento actual.** Gilad sostiene que la inteligencia es alerta temprana basada en "perspective and context (interpretation, insight) not facts" (paráfrasis del buscador, no cita verificada). https://cmr.berkeley.edu/2020/03/are-executives-blindsided-by-competition [S]

### Recurso canónico

**Porter (1980), cap. 3, pp. 47-74**, con la Figura 3-1 como ficha del perfil. En qué fijarse: (1) la asimetría izquierda/derecha (la gente llena lo observable y se salta objetivos y supuestos); (2) las preguntas de supuestos y puntos ciegos (p. 59); (3) el perfil de respuesta como producto final, no el listado. Leer cap. 4 (apertura, p. 75) para pasar de perfil estático a señales. Los manuales de Fleisher & Bensoussan **no** sustituyen a Porter acá; los usa la sección 3.

---

## 3. perspectivas-de-analisis

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Fleisher & Bensoussan (2015), *Business and Competitive Analysis*, 2.ª ed. (Pearson/FT Press), índice | https://www.informit.com/store/business-and-competitive-analysis-effective-application-9780133086409 | Prim. (libro) | 3 | 3 | 2 | 3 | [M] índice completo; capítulos no leídos |
| Fleisher & Bensoussan (2007), 1.ª ed., diapositivas oficiales cap. 5 "Applying the FAROUT Method" | https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch5.pdf | Prim. (material del editor) | 3 | 2 | 2 | 3 | [L] |
| Ídem, cap. 15 "Win/Loss Analysis" (diapositivas) | https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch15.pdf | Prim. | 3 | 2 | 2 | 3 | [L] |
| Kaivo-oja & Roth (2023/2024), modelo de selección de técnicas basado en FAROUT, *Int. J. Foresight and Innovation Policy* 16, DOI 10.1504/IJFIP.2023.136714 | https://www.inderscience.com/info/inarticle.php?artid=136714 | Prim. (paper) | 2 | 1 | 1 | 2 | [S] vía buscador |
| Pragmatic Institute, Win/Loss | https://pragmaticinstitute.com/product/framework/win-loss-analysis | Sec., practicante | 1 | 1 | 1 | 1 | [S] |
| OpenView, "24 Tips for a Winning Win/Loss Analysis" | https://labs.openviewpartners.com/24-tips-winning-win-loss-analysis/ | Sec., practicante (VC) | 1 | 1 | 2 | 1 | [S] |
| Nielsen Norman Group, "Competitive Usability Evaluations" | https://www.nngroup.com/articles/competitive-usability-evaluations/ | Prim. (guía de método) | 3 | 2 | 2 | 3 | [L] |
| HBR (Shi, ago. 2026), "What You Can Learn from a Competitor's Job Postings" | https://store.hbr.org/product/what-you-can-learn-from-a-competitor-s-job-postings/H09A87 | Sec./prensa de negocios | 2 | 1 | 1 | 2 | [M] abstract |

Win/loss: las guías de vendors (SurveyMonkey, Maze, Dovetail, Copper, Corporate Visions, etc.) repiten el mismo método; cuentan como **una** fuente de práctica, no varias.

### Afirmaciones

- **Fleisher & Bensoussan no organizan por "miradas" sino por 24 técnicas** (2.ª ed.). Sección I: definición y contexto, proceso, trampas, comunicación, FAROUT. Sección II: SWOT mejorado, análisis de hipótesis competidoras, benchmarking, modelo de negocio, posicionamiento competitivo, flujo de caja del competidor, factores críticos de éxito, fuerzas impulsoras, eventos y cronología, historiográfico, indicaciones y alertas, fusión de industrias, estadística, linchpin, McKinsey 7S, línea de productos, escenarios, SERVO, shadowing, relaciones estratégicas, cadena de suministro, pronóstico tecnológico, juegos de guerra, win/loss. https://www.informit.com/store/business-and-competitive-analysis-effective-application-9780133086409 [M]
- **FAROUT.** Seis criterios, puntuados 1-5: *F*uture-oriented, *A*ccurate, *R*esource efficient, *O*bjective, *U*seful, *T*imely. "1 = the model's output provides a low level of future orientation. It may be too anchored in the past or present", 5 = muy orientado al futuro; en resource-efficiency, 1 = pide mucho dato, dinero y gente. Antes de elegir técnica, el analista debe preguntarse: cuál es el rango de técnicas posibles, cuál es el foco y alcance del fenómeno, y qué restricciones (personales, de información, organizacionales, de recursos, de contexto) hay. Cierre: "There are no universal tools, 'one size fits all'". https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch5.pdf [L]
- **Puntajes (1.ª ed., 2007; pueden diferir en la 2.ª).** Win/Loss: F4 A3 R4 O4 U5 T2. Competitor Cash Flow: 4/4/1/3/5/2. Benchmarking: 3/3/2/3/5/2. Posicionamiento competitivo: 4/4/4/4/5/3. Shadowing: 4/3/2/3/5/4. Line de producto: 3/3/3/4/3/2. Indications & Warnings: 5/3/3/2/4/3. Análisis de hipótesis competidoras: 1/3/2/5/3/2. Ojo: el buscador devolvió erróneamente "4 en orientación al futuro y 5 en utilidad" y "1 en F" para otras filas; los valores arriba son los leídos de la tabla. Numeración de capítulos distinta entre ediciones (win/loss es cap. 15 en la 1.ª y cap. 29 en la 2.ª). https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch5.pdf [L]
- **Win/loss, definición y método.** "WLA is direct feedback from a client or potential client about why you won or lost a specific sale or contract." Los elementos clave (Schulz, 2002, citado por Fleisher): continuo, feedback del cliente (no solo del vendedor), a tiempo, metodología consistente, usuarios definidos. Siete pasos: definir segmentos y prospectos; entender la cultura interna; armar el cuestionario (cuatro áreas según Naylor 2002: atributos de venta, reputación de la empresa, atributos del producto, servicio); preparar las entrevistas; entrevistar ("Use of an independent third party will avoid results being skewed by any pre-existing relationships"; hacerlas cerca de la decisión); analizar; difundir. https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch15.pdf [L]
- **Win/loss, límites (los mismos autores).** "Interviews are only as good as the interviewer conducting them"; la demora degrada la memoria; la fuerza de ventas puede resistirse si se siente señalada; otras áreas pueden usar el proceso para sus agendas; "Value of WLA is only as good as the system set up to inform interested parties". https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch15.pdf [L]
- **Win/loss, práctica de vendors (secundario, [S]).** Muestra inicial de unos 20 tratos cerrados (10 ganados, 10 perdidos) de los últimos 90 días y entrevistas de 30 minutos (OpenView); entrevistador ajeno a ventas (Pragmatic, Dovetail). Discrepan en si los "sin decisión" entran al análisis (SurveyMonkey los excluye del denominador; Ballpark y Drive Research los incluyen). https://labs.openviewpartners.com/24-tips-winning-win-loss-analysis/
- **Mirada de UX: NN/g.** Dos enfoques: *competitive reviews* (un experto examina productos relacionados) y *competitive testing* (usuarios hacen tareas clave en el producto propio y en los ajenos; "typically" 2 o 3 sitios por participante). Recomienda enfocarse en unos 2 a 4 sitios; hay que alternar el orden por sesgo de aprendizaje; es caro; "The goal is to improve your design." y "You want to beat the competition, not copy them." (la segunda, citada según el resumen leído; verificar literal antes de citar). Qué NO responde: no es un ranking ni dice por qué un cliente compró. https://www.nngroup.com/articles/competitive-usability-evaluations/ [L]
- **Mirada organizacional / contratación.** Argumento: las empresas contratan antes de lanzar productos o entrar a mercados, así que las ofertas de empleo exponen prioridades antes de los anuncios; sirve mejor combinada con otras fuentes y leída como patrón. https://store.hbr.org/product/what-you-can-learn-from-a-competitor-s-job-postings/H09A87 [M]. Fuera de eso solo hay vendors (Contify, JobsPikr) y una nota de GMU sobre un estudio con datos de Burning Glass cuyo paper no se localizó; **no hay estudio empírico verificado** sobre qué tan bien predicen las ofertas el producto.
- **Porter como fuente de miradas y datos.** El cap. 3 (p. 71) enumera fuentes de datos; la Fig. 3-2 enumera áreas funcionales para capacidades (ver sección 2). Es lo más cercano a un catálogo "de miradas" con respaldo primario.

### Catálogo propuesto (síntesis del repo, no del campo)

Cada mirada con la pregunta, una técnica con respaldo, y lo que NO responde. Las filas con "respaldo" citan fuente leída; las demás son propuesta a confirmar con una fuente.

| Mirada | Pregunta | Técnica | NO responde | Respaldo |
|---|---|---|---|---|
| Estratégica | ¿Qué quiere y cómo reaccionará? | Perfil de Porter, señales, juegos de guerra | Qué hace bien en el producto | Porter cap. 3-4 [L] |
| De mercado | ¿Quién compite por el mismo cliente y uso? | Comunalidad de mercado, sustitución en uso, grupos estratégicos | Cuánto vale cada rival | Sec. 1 [M] |
| De cliente | ¿Por qué eligen o rechazan? | Win/loss | Por qué no entran al embudo los que ni te consideran | Fleisher cap. 15 [L] |
| De producto | ¿Qué hace y qué no? | Desarme, matriz, análisis de línea de productos | Si los clientes lo valoran | Sec. 4 |
| UX | ¿Qué tan fácil de usar es para una tarea? | Revisión experta y test comparativo | Por qué compran | NN/g [L] |
| Precio | ¿Cómo cobra y a quién? | Revisión de planes, tarifas y descuentos | Su costo | Sin fuente leída: **hueco** |
| Canales/GTM | ¿Cómo llega al cliente? | Shadowing, análisis de canales | Satisfacción | Sin fuente leída: **hueco** (Fleisher tiene "Shadowing" [M]) |
| Tecnológica y de ecosistema | ¿Qué sabe hacer y con quién se alía? | Pronóstico tecnológico, relaciones estratégicas | Demanda | Índice Fleisher [M] |
| Financiera | ¿Cuánto aguanta? | Flujo de caja del competidor | Intenciones | Fleisher cap. 27/11 [L] |
| Organizacional/contratación | ¿Hacia dónde invierte? | Ofertas de empleo, estructura | Resultados | HBR [M] |

### Recurso canónico

**Fleisher & Bensoussan, 2.ª ed., cap. 5 (FAROUT)** más el capítulo de la técnica elegida. En qué fijarse: no hay técnica universal; elegir por la pregunta y las restricciones antes que por la moda; los puntajes son orientativos y propios de los autores. Para ventas ganadas/perdidas: **cap. 29 (2.ª ed.) / cap. 15 (1.ª ed.)**, pasos 5 y 6. Para UX: **NN/g competitive usability evaluations**.

---

## 4. desarme-de-producto

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| TIME (22-oct-1973), "Business: Tearing Down the Competition" | https://time.com/archive/6841903/business-tearing-down-the-competition/ | Prim. (prensa de época) | 2 | 1 | 3 | 3 | [L] |
| Munro & Associates, material de teardown benchmarking | https://leandesign.com/benchmarking/ (redirige a https://www.munrocommercial.com/services) | Sec., practicante comercial | 1 | 1 | 2 | 1 | [S] (la página de destino no describe el método) |
| Umbrex, "Teardown Benchmarking and Competitive Cost Analysis" | https://umbrex.com/resources/rd-playbooks/the-design-to-value-playbook/teardown-benchmarking-and-competitive-cost-analysis/ | Sec., practicante | 1 | 2 | 1 | 2 | [S] |
| LogRocket, "Product teardown: process and tools" | https://blog.logrocket.com/product-management/product-teardown-process-tools/ | Sec., practicante | 1 | 1 | 2 | 1 | [S] |
| NN/g, competitive usability evaluations | https://www.nngroup.com/articles/competitive-usability-evaluations/ | Prim. | 3 | 2 | 2 | 3 | [L] |
| Fleisher & Bensoussan, "Product Line Analysis" (cap. 21 en 2.ª ed.) y "Benchmarking" (cap. 8) | https://www.informit.com/store/business-and-competitive-analysis-effective-application-9780133086409 | Prim. | 3 | 3 | 2 | 3 | [M] solo títulos y puntajes FAROUT |
| Blogs sobre "feature parity" (Featurebase, ProdPad, Userjot, Userpilot, Nulab, ClickUp) | https://www.prodpad.com/glossary/feature-parity/ | Sec., practicantes de producto (vendors) | 1 | 1 | 2 | 1 | [S]: tratan como **una** fuente de opinión |
| HubSpot / UXPin, matriz de funcionalidades en UX | https://www.uxpin.com/studio/blog/competitive-analysis-for-ux/ | Sec., vendor | 1 | 1 | 1 | 1 | [S] |

### Afirmaciones

- **Origen: la industria automotriz, antes de 1973.** TIME (22-oct-1973): Ford lo llama "value analysis", International Harvester "competitive analysis"; cuando aparece un vehículo nuevo, los demás fabricantes compran uno y lo mandan a una "teardown room", donde se lo desarma en hasta 15.000 piezas; los ingenieros estudian cada pieza para ver si supera la propia y cuánto costaría copiarla. Ejemplo: Ford juzgó superior el cilindro maestro de freno de un rival y construyó uno parecido con dos tornillos en lugar de cuatro; dos años después ese diseño apareció en autos de rivales que lo habían desarmado. https://time.com/archive/6841903/business-tearing-down-the-competition/ [L]. La prensa no data el *comienzo* de la práctica; **el origen histórico anterior a 1973 es un hueco**.
- **Teardown de hardware hoy, practicante comercial.** Munro & Associates afirma que el 70% de los costos queda fijado por el diseño del producto y que costea cada pieza y subconjunto (material, herramental, mano de obra, gastos generales). Es material promocional; las cifras no están verificadas de forma independiente. https://leandesign.com/benchmarking/ [S]. Una guía de Umbrex advierte que la selección del producto debe seguir la decisión que el desarme apoya, y que desarmar una versión recortada del rival contra la completa propia exagera diferencias de costo. https://umbrex.com/resources/rd-playbooks/the-design-to-value-playbook/teardown-benchmarking-and-competitive-cost-analysis/ [S]
- **Versión en software: sin fuente primaria de método.** LogRocket lo describe como "systematic dissection of a product to analyze its features, design decisions, user experience, and overall strategy" (paráfrasis del buscador, [S]). Fuentes con método reconocible: la evaluación competitiva de usabilidad de NN/g (revisión experta o test de tareas con 2-3 sitios, 2-4 competidores, alternar orden). https://www.nngroup.com/articles/competitive-usability-evaluations/ [L]. Fleisher & Bensoussan incluyen "Product Line Analysis" (F3 A3 R3 O4 U3 T2) y "Benchmarking" (F3 A3 R2 O3 U5 T2), pero no se leyeron los capítulos. https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch5.pdf [L, solo puntajes]
- **Matriz de funcionalidades.** HubSpot y UXPin la recomiendan para ver quién ofrece qué y detectar oportunidades de diferenciación, y sugieren 3 a 5 competidores directos más 1 o 2 indirectos y completar la revisión en 1 a 2 semanas. https://www.uxpin.com/studio/blog/competitive-analysis-for-ux/ [S]
- **Crítica: la trampa de la paridad.** Todas son opiniones de vendors de software de producto: la trampa es construir lo que otro tiene porque lo tiene; la presión suele venir de la dirección y apunta a borrar la ventaja del rival, no a una necesidad del usuario (Userpilot); el error es suponer que los clientes del rival usan o quieren esa función (Userjot); ProdPad pide distinguir paridad de plataforma, de migración y competitiva. Contrapunto: faltar una función clave puede empujar clientes a la competencia (Userpilot), y mantenerse al día sigue siendo necesario (ClickUp). https://www.prodpad.com/glossary/feature-parity/ [S]. **No hay fuente académica ni de libro** leída para esta crítica; es el hueco más claro del componente. La crítica de NN/g es más sólida y está leída: "You want to beat the competition, not copy them." (verificar literal).
- **Límite metodológico de la matriz.** Mide presencia, no calidad ni uso: lo que cuenta NN/g sobre pasar de "tiene" a "qué funcionó y qué no" y sus "details of what worked and what didn't matter more" que los porcentajes. https://www.nngroup.com/articles/competitive-usability-evaluations/ [L]

### Recurso canónico

No hay uno que cubra ambas versiones. Propuesta: **TIME (1973)** como ejemplo fundacional del *para qué* (costo y diseño de piezas, no copiar por copiar) y **NN/g, "Competitive Usability Evaluations"** como método utilizable en producto digital. Fijarse en: elegir 2-4 rivales con sentido, definir la pregunta antes, medir tareas y no presencia de funciones, usar los hallazgos para mejorar el propio diseño. La crítica de la paridad se cita como opinión de practicantes hasta tener mejor fuente.

---

## 5. lectura-de-reportes-publicos

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| SEC Office of Investor Education and Advocacy, "Investor Bulletin: How to Read a 10-K" (PDF) | https://www.sec.gov/files/reada10k.pdf | Prim. (oficial) | 3 | 2 | 2 | 3 | [L] (leído el PDF local); sin fecha recuperada |
| Misma guía, página web | https://www.investor.gov/introduction-investing/getting-started/researching-investments/how-read-10-k | Prim. | 3 | 2 | 2 | 1 | [S] (403) |
| SEC, Form 20-F | https://www.sec.gov/file/form20-fpdf | Prim. | 3 | 3 | 1 | 2 | [S] |
| Harvard Law School Forum on Corporate Governance, "Preparing your 2024 Form 20-F" | https://corpgov.law.harvard.edu/2024/12/14/preparing-your-2024-form-20-f/ | Sec. (estudios jurídicos) | 2 | 2 | 1 | 2 | [S] |
| Fleisher & Bensoussan, "Competitor Cash Flow Analysis" (cap. 27 en 1.ª ed., cap. 11 en 2.ª ed.), diapositivas | https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch27.pdf | Prim. | 3 | 2 | 2 | 3 | [L] |
| 10-K de ejemplo con definiciones de RPO y retención neta (formularios de empresas, sin analizar a ninguna) | https://www.sec.gov/Archives/edgar/data/0001432133/000117891322000830/zk2227356.htm | Prim. | 3 | 1 | 2 | 1 | [S] solo para el hecho metodológico de que cada empresa define su propia métrica |
| Skok, "SaaS Metrics 2.0" (ForEntrepreneurs) | https://www.forentrepreneurs.com/saas-metrics-2/ | Sec., practicante (inversor) | 2 | 2 | 2 | 2 | [L] |
| Dealroom, Grata, Specter, Exploding Topics: estimadores de ingresos de privadas | https://dealroom.co/blog/revenue-prediction | Sec., vendors | 1 | 1 | 1 | 1 | [S] |
| Porter (1980), p. 71, sobre fuentes de datos | https://elearn.univ-tlemcen.dz/mod/resource/view.php?id=81871 | Prim. | 3 | 2 | 1 | 2 | [L] |

### Afirmaciones: cotizante

- **Qué es el 10-K y qué no.** "The 10-K typically includes more detailed information than the annual report to shareholders." La SEC "neither writes the 10-K nor vouches for its accuracy"; los filings públicos están en EDGAR. Las empresas extranjeras suelen presentar otros formularios. https://www.sec.gov/files/reada10k.pdf [L]
- **Estructura (Partes e ítems).** Ítem 1 "Business": productos y servicios, filiales, mercados, a veces competencia y regulación; "a good place to start". Ítem 1A "Risk Factors": riesgos más significativos, "generally in order of their importance"; se centra en los riesgos, no en cómo la empresa los atiende. Ítem 7 "MD&A": la gerencia cuenta "its story in its own words": operaciones y resultados, liquidez y capital, "known trends or uncertainties", cambios materiales respecto del período previo, juicios contables críticos. Ítem 7A: riesgo de mercado. Ítem 8: estados financieros auditados con notas. Ítems 10-14 (gobierno, compensación) suelen venir del *proxy statement*. https://www.sec.gov/files/reada10k.pdf [L]
- **Medidas no-GAAP.** Pueden aparecer en el 10-K, y la empresa debe mostrar cómo difieren de la medida GAAP comparable; "it is up to you to decide how much weight to give" (idea de la guía; verificar literal en el PDF). https://www.sec.gov/files/reada10k.pdf [L]
- **Lo que la guía no dice.** El boletín **no trata segmentos, KPIs, cartas a accionistas, presentaciones a inversores ni earnings calls**; no se encontró en esta ronda una fuente oficial que los cubra. Segmentos y KPIs quedan como hueco con fuente primaria. (Un resumen genérico generado por la herramienta de lectura mencionó la nota de segmentos en el Ítem 8; **no es una fuente**, no citar.)
- **KPIs no son comparables entre empresas.** Un 10-K de ejemplo informa retención neta de dólares (118% en 2021 frente a 107% en 2020) y obligaciones de desempeño pendientes (RPO), y aclara que su cálculo "may differ" del de métricas con nombre parecido en otras empresas. https://www.sec.gov/Archives/edgar/data/0001432133/000117891322000830/zk2227356.htm [S]. Otro 10-K advierte que el RPO no necesariamente anticipa crecimiento de ingresos. https://www.sec.gov/Archives/edgar/data/1108524/000110852424000005/crm-20240131.htm [S]
- **20-F (extranjeras).** Disclosure similar al 10-K, con diferencias: reconciliación con US GAAP si usan otras normas, compensación ejecutiva agregada y sin CD&A. https://corpgov.law.harvard.edu/2024/12/14/preparing-your-2024-form-20-f/ [S]. Equivalencias aproximadas: Ítem 3.D riesgos, Ítem 4 información de la empresa, Ítem 5 "Operating and Financial Review and Prospects" (el MD&A de las extranjeras), según un blog secundario no confiable y White & Case. **Discrepancia sobre plazo de presentación**: las instrucciones del formulario dicen cuatro meses desde el cierre; un extracto de la eCFR dice seis meses. No se resolvió; verificar la regla vigente. https://www.sec.gov/file/form20-fpdf y https://www.ecfr.gov/current/title-17/chapter-II/part-249/subpart-C/section-249.220f [S]
- **Flujo de caja del competidor (Fleisher).** "Cash flow is the prime measure of viability and also is a major determinant of operating flexibility — the ability to fund new initiatives and to defend against competitive attacks." No alcanza solo; sirve de contraste de otras técnicas. Menos manipulable por contabilidad creativa; "Historic cash flow not indicative of future performance." Preguntas: cuantitativa (cuánto efectivo hay) y cualitativa (de dónde viene, adónde va, si es sostenible); "Profitable companies can fail!". Compararlo con pares del sector mejora el análisis. Límites: "The validity of any model rests on the validity of the assumptions on which it is built." FAROUT: F4 A4 R1 O3 U5 T2. https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch27.pdf [L]
- **Porter sobre la fuente.** Los "reports filed publicly" y los "speeches by a competitor's management to security analysts" figuran entre las fuentes del sistema de inteligencia (p. 71). https://elearn.univ-tlemcen.dz/mod/resource/view.php?id=81871 [L]

### Afirmaciones: no cotizante

- Solo hay fuentes de vendors. Dealroom dice combinar registros mercantiles con un algoritmo propio de predicción de ingresos (más de 180.000 startups); Specter usa rondas con precio como anclas que luego se alejan hacia su propia trayectoria; Grata propone escalar los ingresos de un par público por relación de plantilla (ejemplo: 25% de la plantilla, dividir por 4). Exploding Topics: clientes por precio y "not an exact science". https://dealroom.co/blog/revenue-prediction [S]. Todas son afirmaciones de empresas que venden esos datos; precisión no verificada.
- **Registros societarios**: ni Companies House ni registros de Argentina/Latinoamérica se investigaron con fuente primaria: hueco.

### Estimar economía unitaria de un rival y sus límites

- Definiciones y umbrales de un practicante inversor (Skok): CAC, LTV, "LTV:CAC higher than 3, sometimes as high as 7 or 8"; recuperar el CAC en 5-7 meses para los mejores, y "the profitability is anemic if the time to recover CAC extends beyond 12 months"; el autor los llama "only guidelines". https://www.forentrepreneurs.com/saas-metrics-2/ [L]. Skok escribe para medir el propio negocio, no el ajeno.
- **No se encontró** un método publicado y verificable para estimar el CAC o la economía unitaria *de un rival* a partir de filings; la búsqueda devolvió solo ejemplos de 10-K y vendors. Cualquier receta (gasto de ventas y marketing sobre nuevos clientes, margen bruto, retención) es propuesta del repo, no del campo: marcar como tal y listar sus límites: métricas definidas distinto por cada empresa, gasto de ventas no separado por producto, ingresos reconocidos vs. contratados, ausencia de datos de cohortes.

### Recurso canónico

**SEC, "How to Read a 10-K"** (el PDF de 5 páginas) para la estructura y para saber dónde está cada cosa, más **Fleisher & Bensoussan, "Competitor Cash Flow Analysis"** para la lectura *competitiva* de las cuentas. En qué fijarse: Ítem 1 para el modelo de negocio y la competencia que la empresa admite; 1A comparado año contra año; MD&A para tendencias conocidas; que la empresa define sus propias métricas. La SEC no cubre el uso competitivo; el vínculo lo hace Fleisher.

---

## Huecos (lo que no se encontró o no se pudo leer)

1. **Texto completo de Bergen & Peteraf (2002), Peteraf & Bergen (2003), Clark & Montgomery (1999), Day et al. (1979) y Porac & Thomas (1990).** Solo abstracts y secundarias. Faltan: definiciones literales de las categorías de competidor, la cita de "sustitución en uso", los criterios que los gerentes usan según Clark & Montgomery y los tamaños de muestra.
2. **Origen de "comunalidad de mercado" y "similitud de recursos"** (probable Chen 1996): sin verificar.
3. **Porter cap. 4, cuerpo**: lista de tipos de señales y el uso de la historia; solo se leyó la apertura.
4. **Fleisher & Bensoussan, 2.ª ed.**: solo índice; los puntajes FAROUT son de la 1.ª ed. (2007) y pueden haber cambiado. Capítulos de producto (línea de productos, benchmarking), shadowing y win/loss de la 2.ª ed. no leídos. El paper de Kaivo-oja & Roth, solo por buscador.
5. **Gilad**: sin lectura del libro ni del artículo CMR (el PDF era una imagen); sin cita verificada.
6. **Origen histórico del teardown** anterior a 1973 y literatura académica de *reverse engineering* competitivo: sin cubrir.
7. **Desarme en software**: ninguna fuente primaria con método, más allá de NN/g (competitive usability). Sin libro de product management leído.
8. **Crítica de la paridad**: solo opiniones de vendors; sin fuente académica ni de libro.
9. **Perspectivas de precio y de canales/GTM**: sin fuente leída. La taxonomía de miradas es propuesta del repo.
10. **Win/loss**: sin estudio empírico de validez; solo Fleisher (con citas a Schulz 2002 y Naylor 2002, no leídos) y guías de vendors.
11. **Lectura de reportes**: sin fuente oficial sobre segmentos, KPIs, cartas a accionistas, presentaciones a inversores y earnings calls; sin fecha de la guía de la SEC; sin lectura del Form 20-F oficial; plazo de presentación del 20-F con fuentes en conflicto.
12. **No cotizantes**: sin fuente primaria o académica sobre registros societarios, rondas y estimación de ingresos; solo vendors.
13. **Economía unitaria de un rival**: sin método verificado; solo umbrales de un practicante para el negocio propio.
14. **Señales de contratación**: sin estudio empírico verificado; solo abstract de HBR (no se pudo comprobar autoría ni fecha más allá de la ficha de la tienda).
15. **Lectura en español**: ninguna fuente es en español. Registros societarios y reportes locales (Argentina/Latinoamérica) no investigados.
