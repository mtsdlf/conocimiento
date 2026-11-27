# Informe de investigación: vertical CIERRE de proyectos de inversión

**Estado de la investigación:** está incompleta. El presupuesto de WebSearch de la sesión se agotó después de una sola búsqueda. Quedaron sin cubrir los manuales de capitalización de prácticas, OpenStax, Gordon y Myers, Azzone y Maccarrone, Neale y Pierce y Tsay. La sección de huecos lo detalla.

Dos límites más de método:
- La herramienta de lectura web devuelve extractos de como máximo unos 125 caracteres por cita. Por eso los párrafos de las normas están literales solo en esos fragmentos. Donde hay "(sigue)", el resto es paráfrasis de la herramienta y hay que cotejarlo con el HTML oficial.
- Los textos de Gordon y Myers, Azzone y Maccarrone, Neale, Pierce y Tsay y Pruitt y Gitman los conozco solo por la tesis de Huikku (2009). Eso es [S], resumen secundario.

Escala de puntajes: autoridad / profundidad / ejemplos / unicidad, de 1 a 3.

## Sobre la división en componentes

La división pedida se sostiene, pero el campo la parte en tres mundos que casi no se hablan entre sí.
- **Contabilidad financiera (NIC 16 y NIC 23).** Es la activación y el cese de la capitalización.
- **Práctica interna de las organizaciones.** Es la liquidación de la orden de inversión, la activación por partes y los costos posteriores. Es el lado de SAP, de los manuales públicos y de la contabilidad pública. Las normas no lo cubren.
- **Contabilidad de gestión.** Es la revisión posterior, que la literatura llama "post-completion audit" (PCA), la auditoría posterior a la terminación.

Dos observaciones que afectan el diseño del tema:
- **"Disponible para usar" no es un solo momento.** La NIC 16 y la NIC 23 usan criterios parecidos pero separados. Se verá abajo.
- **La revisión posterior no es contable.** Compara con lo previsto en la propuesta, no con una norma, y se hace meses o años después del alta.

---

## Componente 1: Activación, o paso de obra en curso a bien de uso

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Leído |
|---|---|---|---|---|---|---|
| IAS 16 *Property, Plant and Equipment*, edición 2026 (IFRS Foundation). https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html | primaria | 3 | 3 | 2 | 3 | [L] parcial, con límite de cita |
| IAS 23 *Borrowing Costs*, edición 2026. https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias23.html | primaria | 3 | 3 | 2 | 3 | [L] parcial, con límite de cita |

### Afirmaciones sobre la NIC 16

- **Párr. 16.** "The cost of an item of property, plant and equipment comprises:" Es la apertura de la lista de componentes del costo (https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html).
- **Párr. 17.** "Examples of directly attributable costs are:" (mismo URL). El inciso (e) incluye el costo de probar si el activo funciona bien, es decir, si su desempeño técnico y físico permite usarlo como se pretende. Eso es paráfrasis de la herramienta. La enmienda de 2020 modificó este párrafo.
- **Párr. 19.** "Examples of costs that are not costs of an item of property, plant and equipment are:" (mismo URL).
- **Párr. 20.** El cese de la capitalización está confirmado literal: "Recognition of costs in the carrying amount of an item of property, plant and equipment ceases when the item is in the l[ocation and condition necessary for it to be capable of operating in the manner intended by management]". Los corchetes completan el texto con la cita parcial de la herramienta, que dio "ceases when the item is in the location and condition necessary for it to be capable of operating." Fuente: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html
  - Los incisos están literales: "(a) costs incurred while an item capable of operating in the manner intended by management has yet to be brought into use", "(b) initial operating losses, such as those incurred while demand for the item's output builds up" y "(c) costs of relocating or reorganising part or all of an entity's operations".
  - Para quien implementa software: los costos del inciso (a) y del (b) no se capitalizan. Se reconocen en resultados aunque el sistema "ya esté, pero todavía no se use".
- **Párr. 20A (enmienda 2020).** "Items may be produced while bringing an item of property, plant and equipment to the location and condition necessary" (sigue). La herramienta también dio esta cita de la parte siguiente: "An entity recognises the proceeds from selling any such items, and the cost of those items, in profit or loss." El costo de esos ítems se mide con la NIC 2. Es decir, lo que se produce en las pruebas ya no se resta del costo del activo. Va a resultados (mismo URL).
- **Párr. 80D y 81N.** La enmienda "Proceeds before Intended Use" (mayo de 2020) modificó los párr. 17 y 74 y agregó el 20A y el 74A. Se aplica retrospectivamente, y la fecha de vigencia es 1 de enero de 2022, con adopción anticipada permitida. La aprobación fue de los 14 miembros del Board (mismo URL). Las referencias van a los párr. BC16A-BC16R y BC36B-BC36D de los Fundamentos de las Conclusiones, que no pude leer.
- **Párr. 21.** "Some operations occur in connection with the construction or development of an item of property, plant and equipment," (sigue). El ejemplo que da la norma es usar el terreno de la obra como estacionamiento. Esos ingresos y gastos, por no ser necesarios para dejar el activo listo, van a resultados (paráfrasis de la herramienta).
- **Párr. 22.** "The cost of a self‑constructed asset is determined using the same principles as for an acquired asset." La segunda oración excluye de ese costo las cantidades anormales de material, trabajo u otros recursos desperdiciados (paráfrasis de la herramienta). La alusión para quien construye software propio es directa.
- **Párr. 55.** "Depreciation of an asset begins when it is available for use, ie when it is in the location and condition necessary" (sigue).
  - La depreciación termina en la fecha más temprana entre la clasificación como mantenido para la venta y la baja. El tiempo ocioso por sí solo no la detiene, salvo que el activo esté totalmente depreciado (paráfrasis).
  - El párr. 20 y el 55 usan la misma fórmula, "location and condition necessary". El momento en que cesa la capitalización y el momento en que empieza la depreciación coinciden en la norma.

### Afirmaciones sobre la NIC 23 (activación por partes)

Todas desde https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias23.html.

- **Párr. 5.** "A qualifying asset is an asset that necessarily takes a substantial period of time to get ready for its intended use or sale."
- **Párr. 17, comienzo.** "An entity shall begin capitalising borrowing costs as part of the cost of a qualifying asset on the commencement date." La fecha de comienzo es cuando se cumplen las tres condiciones: "(a) it incurs expenditures for the asset; (b) it incurs borrowing costs; and (c) it undertakes activities that are necessary to prepare the asset for its intended use or sale."
- **Párr. 19.** "The activities necessary to prepare the asset for its intended use or sale encompass more than the physical construction of the asset. They include technical and administrative work prior to the commencement of physical construction, such as the activities associated with obtaining permits prior to the commencement of the physical construction. However, such activities exclude the holding of an asset when no production or development that changes the asset's condition is taking place." El ejemplo de la norma es el terreno: los intereses mientras se urbaniza se capitalizan, y los intereses mientras se lo mantiene sin desarrollo no.
- **Párr. 20, suspensión.** "An entity shall suspend capitalisation of borrowing costs during extended periods in which it suspends active development of a qualifying asset." El párr. 21 agrega: "Such costs are costs of holding partially completed assets and do not qualify for capitalisation."
- **Párr. 22, cese.** "An entity shall cease capitalising borrowing costs when substantially all the activities necessary to prepare the qualifying asset for its intended use or sale are complete."
- **Párr. 23.** "An asset is normally ready for its intended use or sale when the physical construction of the asset is complete even though routine administrative work might still continue. If minor modifications, such as the decoration of a property to the purchaser's or user's specification, are all that are outstanding, this indicates that substantially all the activities are complete."
- **Párr. 24, partes.** "When an entity completes the construction of a qualifying asset in parts and each part is capable of being used while construction continues on other parts, the entity shall cease capitalising borrowing costs when it completes substantially all the activities necessary to prepare that part for its intended use or sale."
- **Párr. 25, ejemplos.** "A business park comprising several buildings, each of which can be used individually, is an example of a qualifying asset for which each part is capable of being usable while construction continues on other parts." Contraejemplo: una planta industrial con procesos en secuencia, como una acería ("a steel mill"), que debe estar completa antes de que cualquier parte se use.

**Discrepancia entre las dos normas.** La NIC 16 dice "capable of operating in the manner intended by management" (párr. 20). La NIC 23 mide el cese por "substantially all the activities necessary ... are complete" (párr. 22). Son dos criterios distintos que normalmente dan la misma fecha, pero no necesariamente. El tema debería nombrarlos por separado.

**Alta de un sistema por módulos.** La NIC 23 párr. 24-25 es la analogía normativa más cercana a la puesta en marcha por módulos o por fases. Una parte que puede usarse sola se activa sola, y una cadena donde nada funciona hasta que todo está lista se activa al final. Esa es mi lectura, no un texto de la norma.

### Hueco de este componente

- **IFRIC / agenda decisions sobre costos de prueba.** No las busqué ni las leí por el presupuesto de búsqueda. Hay que consultarlas en ifrs.org.
- **Basis for Conclusions de la enmienda 2020** (BC16A en adelante), que explica por qué se eliminó el neteo de ingresos de prueba.
- **Manuales públicos de capitalización de universidades o gobiernos** (práctica). No encontré ninguno. Es el hueco más importante para quien implementa software.

### Recurso canónico propuesto

Los párr. 16-22 y 55 de la NIC 16 y los párr. 17-25 de la NIC 23, en las ediciones HTML del IFRS (los dos URL de arriba). Para un lector no financista habría que sumar una nota propia de traducción a lenguaje llano.

---

## Componente 2: Liquidación, activación por partes y costos posteriores (práctica)

**Hueco total.** No encontré ni leí una fuente para este componente: ni manuales públicos de capitalización de universidades o gobiernos, ni documentación de procedimientos de liquidación de órdenes de inversión. Con la búsqueda agotada, lo que sigue no tiene respaldo.

Lo que sí hay, dentro de las normas ya leídas:
- **Activación por partes.** Está cubierta en lo contable por la NIC 23 párr. 24-25 para los costos por préstamos. La NIC 16 no la mencioné arriba porque no leí los párr. sobre componentes (43-47).
- **Costos que llegan después del alta.** El párr. 20 de la NIC 16 deja afuera los costos incurridos después de que el activo ya puede operar. Está cubierto por (a), (b) y (c). El tratamiento de mejoras posteriores (párr. 12-14) no lo leí.
- **Obra abandonada.** No hay párrafo propio que leí. La NIC 16 trata la baja en los párr. 67 en adelante, que no leí.

### Recurso canónico propuesto

Ninguno por ahora. Hay que buscar manuales públicos (un manual de capitalización de una universidad pública, o de un gobierno, por ejemplo) en una próxima ronda. Hay que marcarlos como práctica, no como norma.

---

## Componente 3: Revisión posterior a la inversión (post-completion audit)

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Leído |
|---|---|---|---|---|---|---|
| Huikku, J. (2009), tesis doctoral *Post-Completion Auditing of Capital Investments and Organizational Learning*, Helsinki School of Economics. https://epub.lib.aalto.fi/pdf/diss/a347.pdf | primaria (tesis) | 3 | 3 | 2 | 3 | [L] introducción y resumen; los tres artículos no |
| Huikku, J. (2007), "Explaining the Non-Adoption of Post-Completion Auditing", *European Accounting Review* 16(2), 363-398, DOI 10.1080/09638180701391006. https://ideas.repec.org/a/taf/euract/v16y2007i2p363-398.html | primaria | 3 | 2 | 2 | 3 | [M] abstract (resumido por la herramienta) |
| Huikku, J. y Lukka, K. (2016), *Accounting and Business Research* 46(3), 243-277. https://ideas.repec.org/a/taf/acctbr/v46y2016i3p243-277.html | primaria | 3 | 2 | 2 | 3 | [M] abstract |
| Neale, C.W. (1995), "Post-completion audits: avoiding the pitfalls", *Managerial Auditing Journal*. https://www.emeraldinsight.com/insight/content/doi/10.1108/02686909510079675/full/html | primaria | 3 | s/d | s/d | 2 | [S] solo por el buscador. La página dio 403 |
| Gordon, L.A. y Myers, M.D. (1991), *Strategic Management Journal* (título y DOI 10.1002/smj.4250120804 sin verificar) | primaria | 3 | s/d | s/d | 3 | [S] vía la tesis de Huikku. Wiley dio 403 |
| Azzone y Maccarrone (2001), Neale (1989, 1991, 1994), Pierce y Tsay (1992), Neale y Holmes (1991), Farragher et al. (1999), Arnold y Hatzopoulos (2000) | primaria | 3 | s/d | s/d | s/d | [S] solo vía la tesis de Huikku |

### Afirmaciones

**Qué es y qué compara.** La tesis define PCA con tres criterios, tomados de Gadella (1986), Pierce y Tsay (1992), Chenhall y Morris (1993) y CIMA (2005): (1) la revisión ocurre cuando la inversión ya fue terminada y empezó a generar flujos o ahorros, (2) "PCA reporting is at least partly focused on a comparison between the pre-investment estimates of an investment project and the actual figures and achievements after completion" y (3) es sistemática y regular, con instrucciones. Fuente: https://epub.lib.aalto.fi/pdf/diss/a347.pdf. El monitoreo y los informes de rutina no cuentan: "monitoring alone cannot be considered as fulfilling the criteria for PCA", porque en esa fase suele ser temprano para saber si se alcanzarán las metas.

**Para qué sirve.** Mismo URL, citando a Neale y Holmes (1991), Mills y Kennedy (1993), Corr (1983) y Pierce y Tsay (1992).
- El aprendizaje organizacional para proyectos futuros es "the major objective of PCA" y también el principal beneficio percibido.
- Secundarios: dar feedback para corregir o abandonar proyectos que rinden mal, y mejorar la integridad de las propuestas.
- Algunas empresas lo usan para evaluar a las personas involucradas (Smith 1994, Neale 1994).
- Huikku (2009) concluye que el uso para corregir o abandonar proyectos en curso "can be minor" por "inherently inappropriate timing". También que acoplar la PCA a la evaluación y premios formales es raro por problemas de tiempos. Las mismas conclusiones salen de lo reportado por Neale (1989), Pierce y Tsay (1992) y Corr (1983).

**Para disciplinar las propuestas.** Pierce y Tsay (1992), vía la tesis, dicen que las empresas ven la PCA como útil para mejorar la integridad de las propuestas de inversión. Las propuestas pueden tener sesgos intencionales al alza: "managers exaggerate project cash flows in order to gain approval for their investment proposals", citando a Pruitt y Gitman (1987, *Financial Management* 16(1), 46-51) y Pohlman et al. (1988). Lumijärvi (1990) sostiene que la PCA es el único factor que reduce el juego estratégico en el proceso de inversión. Fuente: https://epub.lib.aalto.fi/pdf/diss/a347.pdf. Es una afirmación de un solo autor, y las otras dos las conozco solo de segunda mano.

**Cuántas empresas la hacen (tasas de adopción).** Todas vía la tesis de Huikku (https://epub.lib.aalto.fi/pdf/diss/a347.pdf), nota al pie 9. No pude leer los estudios originales.
- Reino Unido: 98% (Arnold y Hatzopoulos, 2000) y 79% (Neale, 1991b).
- Estados Unidos: 88% (Farragher et al., 1999), 76% (Gordon y Myers, 1991) y 90% (Klammer y Walker, 1984).
- Noruega: 41% de las grandes empresas (Neale, 1994).
- Italia: 71% de las grandes empresas (Azzone y Maccarrone, 2001).
- Finlandia, 30 mayores manufactureras: 20 de 30 (67%), según la propia tesis. Las otras 10 no comparan formalmente las estimaciones previas con los resultados posteriores.

Las cifras difieren mucho entre países, años y definiciones de la muestra. "Large companies" no es la definición de todos los estudios. No las sumaría en un promedio.

**Por qué algunas no la hacen.** Huikku (2007) halla que los controles alternativos ("alternate capital investment controls") pueden sustituir a la PCA. Son el seguimiento de cifras de producción, los centros de ganancia y el uso de expertos internos. Las empresas más chicas, con pocas inversiones grandes, complejas o repetitivas, los perciben como suficientes. Fuentes: https://ideas.repec.org/a/taf/euract/v16y2007i2p363-398.html (abstract resumido por la herramienta) y https://epub.lib.aalto.fi/pdf/diss/a347.pdf. La tesis agrupa las razones de no adopción en tres: escasez de inversiones, dificultades de la PCA y formas alternativas de lograr los beneficios.

**Diseño y quién la hace.** Huikku (2009) concluye que "organizational-memory-related aspects, such as adequate filing of PCA results and convenient access to them, can aid a company to effectively convey past investment experiences to new projects." Las empresas grandes, con una masa crítica de inversiones, tienen diseños más sofisticados. Fuente: https://epub.lib.aalto.fi/pdf/diss/a347.pdf. La tesis enumera como dimensiones de diseño la selección de proyectos, el momento, quién la hace, entre otras (línea 329 del texto extraído). El detalle de las prácticas de cada dimensión está en el artículo 3 y no lo leí.

**Credibilidad de la autoevaluación.** Huikku y Lukka (2016) estudiaron 22 informes de PCA en una empresa forestal europea, con 24 entrevistas. Encuentran tres condiciones que favorecen informes persuasivos, la primera de las cuales es "alignment with relevant external/internal reference points". Plantean que la teoría de agencia, que alerta sobre la manipulación de datos en la autoauditoría, deja el proceso como una "caja negra". Fuente: https://ideas.repec.org/a/taf/acctbr/v46y2016i3p243-277.html [M].

### Discrepancia entre fuentes

La literatura de adopción en EE. UU. y Reino Unido (76% a 98%) contrasta con Noruega (41%), con Italia (71%) y con la muestra finlandesa (67%). Huikku (2007) lo explica por los controles alternativos, mientras que Neale y Holmes (1991) y Azzone y Maccarrone (2001) también lo atribuyen a las buenas relaciones entre gerentes, según la tesis. No es una discrepancia entre autores sobre el mismo hecho. Es una diferencia de contexto y definición.

### Hueco de este componente

- **Gordon y Myers (1991), Azzone y Maccarrone (2001), Pierce y Tsay (1992), Neale (1989, 1991, 1994), Mukherjee.** No los leí. Solo tengo lo que la tesis de Huikku dice de ellos.
- **OpenStax.** Probé dos URL de OpenStax (`principles-managerial-accounting/pages/12-3-capital-investment-analysis` y `12-1-capital-investment-decisions`) y ambos dieron 404. No sé si el libro trata post-audit. Falta encontrar la URL correcta.
- **Optimismo de los pronósticos de flujo.** Solo tengo la mención de Pruitt y Gitman (1987) y Pohlman et al. (1988) vía Huikku. No leí los estudios que comparan flujos previstos contra reales. Flyvbjerg, pedido solo de pasada, no se consultó.
- **Huikku (2007, 2008, 2009 artículo 3).** Solo leí el abstract y la introducción de la tesis. Faltan los hallazgos de timing, de quién la hace y de cuántos años después.
- **Qué compara exactamente, y cuándo.** Sé que compara estimaciones previas con cifras reales (VAN, costos, plazos son mi traducción, no una cita). No tengo fuente sobre cuánto tiempo después se hace.

### Recurso canónico propuesto

La tesis de Huikku (2009), https://epub.lib.aalto.fi/pdf/diss/a347.pdf. Es de acceso abierto, resume la literatura previa (adopción, usos, diseño) y es la única fuente que pude leer entera. Hay que validar sus citas con los originales antes de afirmarlas en una nota vigente. No la dejaría como única fuente de una nota confirmada.

---

## Huecos finales, en orden de importancia

1. **Prácticas de liquidación y manuales de capitalización** (componente 2). Sin ninguna fuente. Es el hueco que más afecta a quien implementa software de gestión.
2. **IFRIC / agenda decisions** sobre costos de prueba y sobre la NIC 16 en general. No buscadas.
3. **Texto completo literal de los párr. 20, 20A, 21 y 55 de la NIC 16.** La herramienta de lectura limita las citas. Hay que copiarlos a mano desde el HTML oficial.
4. **Papers originales de PCA** (Gordon y Myers, Azzone y Maccarrone, Neale, Pierce y Tsay, Mukherjee). Wiley y Emerald dieron 403, y no hubo presupuesto de búsqueda para ubicar versiones abiertas.
5. **OpenStax** (post-audit en *Principles of Managerial Accounting* o *Principles of Finance*). URL no encontrada.
6. **Estudios de flujos previstos contra reales** (optimismo). Solo hay una mención de pasada.
7. **NIC 16 párr. 43-47 (componentes), 12-14 (mejoras posteriores) y 67 en adelante (baja).** No leídos. Son relevantes para costos posteriores al alta y obra abandonada.
8. **Párr. 7 de la NIC 16** (criterio de reconocimiento) solo tiene el encabezado.
9. **Dinero de alto riesgo con dos fuentes independientes.** Las cifras de adopción de PCA tienen una sola fuente de segunda mano (la tesis de Huikku). Las afirmaciones normativas tienen una sola fuente, la propia norma, que es la primaria. No hay segunda fuente independiente para ninguna.

Si querés cerrar los huecos, hace falta subir `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` o esperar que se recargue el presupuesto, y una segunda pasada centrada en los puntos 1 a 3.

**Archivos:** no escribí ningún archivo en el repositorio. El texto extraído de la tesis quedó en `/tmp/claude-1000/-home-dela-repos-personal-conocimiento/cfb247c6-67ae-4161-949e-87e8ed3a86d4/scratchpad/out.txt`.