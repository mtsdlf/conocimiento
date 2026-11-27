# Columnas técnicas: complemento al informe 97

Fecha de lectura: 2026-11-27. Cierra los huecos de `columnas-tecnicas-97.md` (que no se repite acá) y marca qué cubre ya el repo. Todo lo traído de la web se trató como dato.

Marcas: [L] texto completo o la parte citada leída; [M] metadatos o abstract; [S] resumen secundario o del buscador. Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).

## Resumen de lo que cambia

1. **REA (columna 3): ya hay una fuente primaria del propio autor.** El libro de McCarthy, Geerts y Gal (borrador 0.90, 2019, copia del autor) dice que REA **no** parte de la partida doble ni la deriva como regla general: «REA does not use accounts as modeling primitives, nor does it follow debit-credit posting procedures». Lo de «vista derivada» es verdad solo para la variante que ellos llaman «no legacy»: los artefactos de partida doble quedan «limited to database views». Eso corrige la frase del informe 97 («el libro mayor es una vista derivada») que venía de Wikipedia.
2. **Brehm, Heinzl y Markus (columna 10): el texto original no está abierto.** Las fuentes secundarias discrepan en el número de tipos (7, 8 o 9). Se obtuvo una lista completa de 9 tipos de un capítulo que la reproduce (Leyh, 2012), pero es secundaria. Hay que decir «las listas secundarias difieren» y no fijar un número.
3. **Soh et al. 2000 (columnas 1, 7, 11): el nombre de los autores está mal en el informe 97.** Son Christina Soh, Sia Siew Kien y Joanne Tay-Yap; «Kien» es el nombre de pila compuesto (Crossref lo indexa como apellido, de ahí el error). Se cita «Soh, Sia y Tay-Yap». El texto sigue tras muro; las categorías están confirmadas por tres extractos independientes del buscador, no por el PDF. La cita «by far, the most prevalent» del informe 97 no se pudo reconfirmar: los extractos de ahora dicen «the most prevalent form of misfit noted».
4. **Numeración (columna 2): el texto de la Directiva no dice «sin huecos».** Dice «a sequential number, based on one or more series, which uniquely identifies the invoice». La Comisión aclara que las series las elige el negocio. «Sin huecos» es lectura (la de la nota de Impuestos ya la marca como inferencia).
5. **Separación de funciones (columna 7):** el repo ya cubre bien el contenido; lo que queda propio es lo de sistema (qué acciones distingue el registro, qué se prohíbe incluso al administrador) y el hecho de que COSO no nombra «autorizar, registrar, custodiar»: esa tríada es de manuales y de OpenStax.
6. **Costo de personalizar (columna 10):** hay un estudio empírico abierto (Dittrich y Vaucouleur 2008, 3 entrevistas, 42 respuestas, con un proveedor como socio) y un caso reciente (Gool y Seymour 2018). Cifras de «porcentaje de costo extra en cada actualización» solo las dan vendedores o consultoras; no hay medición independiente que traiga un número confiable. Se declara hueco.

---

## Columna 3 (parte). REA y la partida doble

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| McCarthy, Geerts y Gal, *The REA Accounting Model as an Accounting and Economic Ontology*, versión 0.90, 2019 (borrador de los autores; la versión final es de la AAA) | https://static1.squarespace.com/static/5feb9bf81c227637fcd6262b/t/667f4e6e846ebb74f8b18595/1719619185764 | primaria (el autor de REA) | 3/3/3/3 | [L] preface, cap. 1, cap. 5, cap. 6 en lo citado |
| McCarthy 1982, *The Accounting Review* 57(3):554-578 | https://www.jstor.org/stable/246878 | primaria | 3/3/2/3 | [M] (sin acceso; se lee a través del libro de 2019, que reproduce sus cuatro críticas) |
| Nikitkov, «REA model, its development and integration as an enterprise ontology framework», *Accounting and Management Information Systems* 19(3):566-594, 2020 (revisión de 55 publicaciones) | https://online-cig.ase.ro/RePEc/ami/articles/19_3_6.pdf | secundaria académica | 2/2/1/2 | [L] en lo citado |
| Hruby, *Model-Driven Design Using Business Patterns*, Springer 2006 | https://link.springer.com/10.1007/3-540-30327-2 | primaria | 3/3/3/2 | [M] solo ficha; su tesis sobre partida doble viene de una reseña [S] |
| ISO 15944-4 (2007, 2015) | (de pago) | norma | 3/3/2/3 | [S]: solo vía el libro de 2019, que le toma los términos «independent view» y «trading partner view» |

### Afirmaciones

- La subtítulo del paper de 1982 («a generalized framework for accounting systems in a shared data environment») buscaba unir dos puntos de vista: el de los usuarios tradicionales de datos contables y el de quienes toman decisiones fuera de contabilidad. Fuente: libro 2019, prefacio. URL arriba.
- Las cuatro críticas a la contabilidad convencional del paper de 1982 (pp. 554-555, según el libro): (1) dimensiones limitadas, casi todo en términos monetarios; (2) esquemas de clasificación (el plan de cuentas) no siempre apropiados; (3) nivel de agregación demasiado alto («information concerning economic events and objects should be kept in as elementary a form as possible to be aggregated by the eventual user»); (4) poca integración con otras áreas, con la misma información mantenida por separado por contadores y no contadores. Los autores dicen que las cuatro siguen vigentes en 2019. En 2019 suman dos: no sirve para razonamiento automático y no sirve para un repositorio distribuido de vista independiente, porque «the fundamental accounting equation (A=L + OE) ... is a trading-partner view of commerce». URL arriba.
- Qué es REA frente a la partida doble, cap. 1: «REA accounting systems take an approach different from double-entry bookkeeping in that they use a modeling pattern to develop a database for the same purpose of producing a transactional memory of between-company resource transfers and within-company resource transformations. REA does not use accounts as modeling primitives, nor does it follow debit-credit posting procedures. Instead, it builds a linked database where rows in different tables are connected to capture the semantics or meaning of the modeled transactions.» URL arriba.
- La dualidad: es una asociación entre dos eventos económicos (un «incremento» y un «decremento»): lo que se entrega y lo que se recibe a cambio. Cap. 1, figura 1-5(b). URL arriba.
- La vista derivada, con el matiz que importa. El cap. 5 clasifica los sistemas en cinco tipos. En el tipo «sistemas ERP de cadena de valor, no heredados» (los organizados con principios REA), la partida doble se relega «to a database view (as opposed to being part of the core database set of elements)» y «financial reporting can be accomplished quite well by a minimal general ledger with other double-entry artifacts limited to database views». Del tipo «ERP heredado» dicen que «retain many double-entry artifacts as mainstream features, including bloated charts of accounts with long faceted account codes». URL arriba, cap. 5.
- Quién lo usa: los autores citan un producto comercial en la nube (Nittler 2018, según ellos) y el uso de REA como principio de mensajería entre empresas en ISO 15944-4. El libro afirma, sobre ese producto, que REA «seamlessly produces all of the traditional accounting reports and financial statements». Es testimonio de parte (los autores promueven REA): fuente para decir «existe una implementación», no para decir «anda mejor». Nikitkov 2020 dice lo mismo: REA fue incorporada a normas ISO y «served as the basis for at least one cloud-based enterprise system» y «has not received sufficient attention from IS academics or practitioners». URL Nikitkov arriba.
- Evidencia experimental: según Nikitkov, Dunn y Grabski (2000) reportaron que REA es «significantly more expressive» que el modelo débito-crédito, y estudios de ajuste cognitivo muestran que los usuarios lo prefieren para encontrar información. Son estudios con estudiantes en laboratorio, leídos por esta revisión [S].
- Críticas: Weber dice que REA es demasiado general para eventos no contables; Verdaasdonk (2003) que no da datos contables ex ante (según Nikitkov, sin leer los originales) [S].
- Frase que el informe 97 tomó de Wikipedia («double-entry bookkeeping disappears in an REA system»): coincide con el libro en lo grueso (REA no usa cuentas como primitiva) pero omite que una variante conserva un libro mayor mínimo como vista.

### Qué hay en el repo

- `Contabilidad/Fundamentos/fundamentos-de-contabilidad.md` ya tiene una sección «REA: registrar los hechos y no los asientos» con McCarthy 1982 [M] y una lectura de la base («el asiento como algo que se deriva de ellos»), y cita un taller que dice que los sistemas siguieron con asientos. No tiene el libro de 2019.
- `Contabilidad/Registro/partida-doble.md` enlaza esa sección.
- `Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md` tiene el patrón de fila que no se edita, y declara «Sin fuente todavía» a Fowler en contabilidad.

**Propio de la columna 3:** la comparación explícita partida doble frente a REA con la fuente del autor, y la advertencia de que «vista derivada» es una variante, no el consenso. Conviene corregir el pasaje de la nota de Contabilidad con el libro de 2019 (alcance fuera de este tema; declararlo como pendiente).

### Recurso canónico

McCarthy, Geerts y Gal 2019, cap. 1 (el ejemplo de las mismas transacciones en cuentas T y en tablas REA) y cap. 5 (los cinco tipos de sistema, figura 5-1). Fijarse en cómo se ve el mismo hecho con y sin cuentas, y en la frase sobre el libro mayor mínimo como vista.

---

## Columna 10 (parte). Tipos de adaptación y costo al actualizar

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Brehm, Heinzl y Markus, HICSS-34, 2001, pp. 1-9, DOI 10.1109/HICSS.2001.927130 | https://doi.org/10.1109/HICSS.2001.927130 | primaria | 3/3/2/3 | [M]: Crossref y Semantic Scholar no traen abstract ni PDF abierto |
| Leyh, cap. 6 «Tailoring of ERP Systems», en *Readings on Enterprise Resource Planning* (Monk y otros, ed.), 2012 | https://web.eng.fiu.edu/chen/Summer%202012/EGN%205621%20Enterprise%20Systems%20Collaboration/Reading%20ERP/Readings_on_ERP_chapter06.pdf | secundaria (capítulo de libro que reproduce y extiende el esquema de Brehm et al.) | 2/3/2/2 | [L] las secciones 6.2 y 6.3 |
| Gool y Seymour, «Managing ERP System Customisation Post-Implementation: The Case of an African Petroleum Organisation», ICEIS 2018 | https://scitepress.org/Papers/2018/66764/pdf/index.html | primaria (caso) | 2/2/2/2 | [L] vía lectura asistida; no cuantitativo |
| Dittrich y Vaucouleur, *Customization and Upgrade of ERP Systems: An Empirical Perspective*, ITU Technical Report TR-2008-105, 2008 | https://en.itu.dk/-/media/EN/Research/About-ITU-Research/Technical-Reports/2008/ITU-TR-2008-105-pdf.pdf | primaria (informe técnico) | 2/3/3/3 | [L] |
| Revisión sistemática 2024 «The Evolution of Original ERP Customization» (ICEIS) | https://scitepress.org/publishedPapers/2024/123055/pdf/index.html | secundaria | 2/2/1/1 | [L] en lo citado |

### Afirmaciones

**Lista de tipos de Brehm et al.**

- El original no se pudo leer. La revisión de 2024 dice que los autores «delineate 7 tailoring types adding extended reporting, workflow programming and interfaces» y los clasifican por la capa que tocan y el esfuerzo de mantenimiento. Un resumen de la Universidad Binus lista ocho; un paper de arXiv atribuye nueve a una referencia sin nombre. **Tres fuentes secundarias, tres números: 7, 8 y 9.** URLs: https://scitepress.org/publishedPapers/2024/123055/pdf/index.html, https://sis.binus.ac.id/?p=34376, https://arxiv.org/pdf/1211.2445 (los dos últimos solo vía buscador [S]).
- Leyh (2012) reproduce el esquema (su figura 2) y atribuye a Brehm et al. la base. Agrupa nueve tipos de la menos a la más invasiva, con «the degree of freedom increases from left to right» y más esfuerzo a la derecha:
  - **Modificación** (sin tocar el código fuente): configuración, ajuste de pantallas (*screen mask adjustment*), ajuste de reportes (*report adjustment*), complementos de terceros (*bolt-ons*), programación de flujos de trabajo (*workflow programming*).
  - **Desarrollo**: desarrollo de interfaces, programación en el lenguaje del ERP (*ERP programming*), puntos de extensión que da el proveedor (*user exits*), modificación del código del paquete (*package code modification*).
  - Aparte, lo que queda antes de la personalización: el ajuste del estándar (selección de módulos).
  URL: Leyh arriba. Lo que es de Leyh y lo que es de Brehm no se puede separar sin el original: no atribuir los nueve a Brehm.
- Configuración, según Leyh: elegir entre procesos de referencia y fijar parámetros «without changing the source code»; hay tantas tablas que «it is almost impossible for "normal" employees ... to get an overview of all configuration parameters and their interdependencies», y las opciones varían mucho entre productos («some small ERP systems provide little or no configuration options»). Es afirmación de Leyh, no de Brehm.
- Qué dice Leyh del costo al actualizar, por tipo:
  - *User exits*: el proveedor define la interfaz y «the exit once provided by the manufacturer is usually not removed in later versions or releases»; por eso, a diferencia de los otros tipos de desarrollo, «does not severely threaten maintainability».
  - *Package code modification*: «the most dangerous form of adjustment»; «very expensive in terms of maintenance, as changes may be corrupted by updates or overwritten by new versions»; algunos proveedores la prohíben o sancionan quitando el soporte.
  - Es el único tramo que da el mecanismo (qué se rompe y por qué) en una sola fuente. Todavía es argumento de texto, no medición.

**Estudios sobre el costo de personalizar al actualizar**

- Dittrich y Vaucouleur 2008 [L]: estudio con videograbaciones, entrevistas con tres consultores y una encuesta en foros de práctica con **42 respuestas**; el socio industrial era un proveedor de ERP (se estudian dos de sus productos). Hallazgos sobre actualizar:
  - La estrategia más común es «go standard»: repasar con el cliente cada personalización y decidir si se mantiene o se descarta; si se mantiene, hay que portarla a la versión nueva («one strategy for upgrading customizations in many cases is to get rid of them»).
  - Dificultades «intrínsecas»: una función a medida toca varios objetos relacionados, y algunos objetos reciben modificaciones de varias funciones; ejemplo textual: «the postings to the general ledger are often modified to mirror specific business rules. Here each modification has to be identified, analysed and re-applied or redesigned.»
  - Dificultades por código mal hecho o sin documentar: la más crítica es la personalización sin documentación, sobre todo de otra consultora; programar «directly into the standard functionality instead of developing an independent object» es el error típico; los cambios en la capa núcleo se consideran «dangerous and risky when upgrading».
  - Por tipo de cambio del estándar: si cambia el modelo de datos del que depende una función a medida, «require a total redesign of the feature»; si cambia la lógica de negocio hay que inspeccionarla y decidir si la nueva reemplaza la personalización; el diseño de formularios y reportes hay que reajustarlo.
  - Quién empuja la actualización: según la encuesta, los socios (revendedores) tienen «a strong influence». No hay cifras de costo.
  - Límites: muestra chica y por conveniencia; un solo proveedor como socio; informe técnico sin revisión de pares.
- Gool y Seymour 2018 [L]: caso de una petrolera africana. «ERP modifications need to be reapplied and tested with each upgrade» (conclusión); el ERP «had undergone numerous upgrades that were very challenging due to the large amount of ERP programming»; para la siguiente actualización «needed to reduce their custom objects». El paper cita a Brehm et al. 2001 como fuente de que los costos de actualización son un factor de costo de la personalización, y a Panorama Consulting (2017) para una referencia de 10-20 % de personalización. **No mide** el costo; sin números propios.
- Leyh, sobre el estudio de pymes (6.3.2): las empresas dejan el desarrollo (interfaces, programación) al fabricante para «avoid self-programmed features interfering with system updates, new releases, service, and support contracts», y en un caso el fabricante incorporó la función a medida al estándar y la entregó a todos con la versión siguiente. Es un caso, no un dato general.
- Cifras sueltas que circulan («una actualización cuesta 25-33 % de la implantación» citando a Ohlson 2000; «hasta 30 % según Gartner»): salieron del buscador, de páginas de consultoras y vendedores, sin fuente primaria leída. **No usar.**

### Qué hay en el repo

- `Desarrollo/Evolucion/migraciones-y-actualizaciones.md` y `sistema-heredado.md` (otras cosas: migraciones de código y deuda), sin tratamiento de personalización de paquetes.
- `Compras-y-abastecimiento/Abastecimiento-estrategico/costo-total-de-adquisicion.md` y `Estrategia-competitiva/Fuentes-de-ventaja/costos-de-cambio.md` (marco de costo total; la personalización como parte del costo aparece en `Mercado-y-economia/costo-total-para-quien-compra.md` del árbol).
- `Arquitectura/Sistemas-distribuidos/multi-tenancy.md` toca configuración por cliente en SaaS (solo en ese contexto).

**Propio de la columna 10:** todo el espectro configurar / extender / modificar y su efecto al actualizar. No hay nota previa en el repo.

### Recurso canónico

Dittrich y Vaucouleur 2008, secciones 4.4 y 4.5 («Challenges of customizations», «Upgrading customizations»): es lo único abierto que describe, con citas de practicantes, por qué una personalización se rompe. Para el mapa de tipos, el capítulo de Leyh (6.2), con el aviso de que es secundario. Para el original, Brehm et al. 2001 (hay que conseguirlo por biblioteca).

---

## Columnas 1, 7 y 11 (parte). Soh, Sia y Tay-Yap 2000: categorías de desajuste

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Soh, Sia y Tay-Yap, «Enterprise resource planning: cultural fits and misfits: is ERP a universal solution?», *CACM* 43(4):47-51, abril 2000, DOI 10.1145/332051.332070 | https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits (403 para el fetch; la página de ACM exige JavaScript) | primaria | 3/2/2/3 | [S]: tres extractos de buscador que reproducen el texto del paper (core.ac.uk, Cambridge, typeset.io), sin ver la fuente |
| Datos bibliográficos (Crossref) | https://api.crossref.org/works/10.1145/332051.332070 | metadatos | 3/1/1/1 | [M] |
| Sia y Soh, cap. «An exploratory analysis of the sources and nature of misfits in ERP implementations», en *Second-Wave ERP Systems*, Cambridge 2003 | https://www.cambridge.org/core/books/secondwave-enterprise-resource-planning-systems/an-exploratory-analysis-of-the-sources-and-nature-of-misfits-in-erp-implementations/3A868C86D665F1E335AF64057E2170EC | primaria | 3/2/2/2 | [M] solo resumen, tras muro; define misfit como «the gaps between the functionality offered by the package and that required by the adopting organization» |

### Afirmaciones

- Autores: Christina Soh, Sia Siew Kien (NTU, Singapur) y Joanne Tay-Yap (hospital KK, Singapur). El capítulo de Cambridge cita el paper como «Soh, C., Sia, S. K., and Tay-Yap, J. (2000)». Corrige «Soh, Kien y Tay-Yap» del informe 97.
- Base empírica: **un hospital**, con documentos de implantación más entrevistas a miembros del equipo; los autores lo presentan como hallazgos tempranos de un estudio mayor (según los extractos). Un trabajo posterior de Sia y Soh (ICIS 2002) aplicó un marco de severidad a cientos de desajustes en tres hospitales [S].
- Tres categorías (según los extractos, que coinciden entre sí):
  - **Datos**: desajuste en el formato de los datos o en las relaciones entre entidades del modelo de datos subyacente; arreglarlos obliga a reestructurar tablas, o sea un cambio costoso en el núcleo del paquete.
  - **Funcional** (o de proceso): desajuste en los procedimientos de procesamiento requeridos; tres subtipos: **acceso**, **control** y **operativo**.
  - **De salida** (*output*): desajuste en el formato de presentación o en el contenido de la información; es «the most prevalent form of misfit noted» según el extracto más reciente. El informe 97 trae «by far, the most prevalent form» de un resumen anterior: las dos formulaciones difieren; no citar «by far» sin ver el texto.
- No hay recuento de desajustes por categoría en ninguna fuente leída.
- Relación con las columnas: datos con la 1; acceso y control con la 7 (la categoría «control» es lo más cercano a una validación de negocio que el producto no trae); salida con la 11. Ojo: es un solo hospital público de Singapur (el origen cultural es el tema del paper); no generalizar el «más frecuente» a cualquier empresa.

### Qué hay en el repo

Nada del paper. Solo el informe 97.

### Recurso canónico

El paper (5 páginas), la sección con la tabla de los tres tipos de desajuste y sus ejemplos hospitalarios. Falta conseguir el PDF por biblioteca o por la copia de los autores.

---

## Columna 7. Permisos y separación de funciones

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| COSO, *Internal Control — Integrated Framework*, Executive Summary, mayo 2013 | https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf | primaria | 3/2/1/3 | [L] el componente «Control Activities» y la lista de los 17 principios |
| COSO 2013, puntos de foco del principio 10 (volumen del marco, de pago) | (de pago) | primaria | 3/3/2/3 | [S]: los nombra el buscador sobre compilaciones de la AAA, sin ver COSO |
| McGill University, Internal Audit, «Internal Controls» | https://www.mcgill.ca/internalaudit/node/647 | secundaria institucional | 1/1/1/1 | [L] |
| University of Missouri System, política de segregación de funciones | https://www.umsystem.edu/ums/policies/finance/segregation | secundaria institucional | 1/2/2/2 | [S] (ya usada por la nota del repo) |

### Afirmaciones

- Principio 10 de COSO 2013, literal: «The organization selects and develops control activities that contribute to the mitigation of risks to the achievement of objectives to acceptable levels.» (Executive Summary, lista de principios). URL arriba [L].
- Lo que COSO dice de la separación de funciones en el Executive Summary no está en el enunciado del principio, sino en la descripción del componente de actividades de control (p. 4): «Segregation of duties is typically built into the selection and development of control activities. Where segregation of duties is not practical, management selects and develops alternative control activities.» **Importante:** COSO no menciona «autorizar, registrar y custodiar». Esa tríada no sale del marco. Es la división clásica de los manuales y de las guías.
- Los puntos de foco del principio 10 (la lista que tiene un punto «Addresses Segregation of Duties») no se pudieron leer: son del volumen de pago. Según compilaciones de la AAA y una presentación de la Universidad de Illinois [S], el punto es la 10.CA.43 y pide separar las tareas incompatibles y, si no es práctico, buscar actividades alternativas. No citar el texto del punto de foco.
- La tríada, según McGill: las funciones «must be segregated among different people to reduce the risk of error or inappropriate action», con autorización («responsibilities for authorizing transactions (approval)»), registro («recording transactions (accounting/record keeping)») y custodia («handling the related asset (custody)»). La conciliación **no** figura como función separada: McGill la trata como otra actividad de control. Coincide con lo que ya dice la nota del repo sobre Missouri.
- En un sistema de gestión (inferencia, la columna es de diseño): los permisos se pueden expresar con tres capas (rol sobre tipo de documento, restricción por registro, incompatibilidades entre roles). Eso ya está sostenido por documentación de productos en el informe 97 y por la Green Book vía `controles-sobre-sistemas.md`.

### Qué hay en el repo

- `Contabilidad/Control-interno/separacion-de-funciones.md` (vigente): la tríada autorizar, registrar, custodiar con ejemplos de compras; las cinco funciones de Missouri; la tabla de combinaciones incompatibles; colusión (ACFE 2024); controles compensatorios; y un apartado «Lo que un sistema tiene que poder impedir» (acción distinta del objeto, negar combinaciones también al administrador, dejar rastro cuando se permite). Cita COSO 2013 del mismo Executive Summary.
- `Contabilidad/Control-interno/controles-sobre-sistemas.md`: principio 11 de COSO, Green Book (accesos, cambios al programa, operación), pista de auditoría, tabla «lo que un sistema tiene que poder hacer». Cita explícitamente que Cómo resuelve cada producto estas capacidades va al tema Software de gestión.
- `Contabilidad/Control-interno/autorizaciones.md`: niveles de aprobación, matriz de autorizaciones y numeración prenumerada.
- `Contabilidad/Control-interno/auditoria-y-fraude.md`: anulación de controles.
- Declarado hueco en la propia nota: un catálogo neutral de combinaciones incompatibles por ciclo.

**Propio de la columna 7:** nada de la teoría; no repetirla. Lo propio es el diseño del software: el modelo de permisos en tres capas (rol/tipo, registro, incompatibilidad entre roles), cómo se expresa una regla de incompatibilidad como dato configurable, y el caso de un SaaS con muchas empresas (permisos por empresa). La columna debe enlazar las dos notas de Contabilidad y declarar en una línea que la tríada es de manuales y no de COSO.

### Recurso canónico

Para la teoría, la nota existente del repo. Para la columna, COSO 2013 Executive Summary p. 4 (el párrafo de actividades de control) como única referencia normativa abierta, más la Green Book que cita `controles-sobre-sistemas.md`.

---

## Columna 2 (parte). Numeración correlativa de comprobantes

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Directiva 2006/112/CE, art. 226 (texto original de 2006, copia del BOE) | https://www.boe.es/doue/2006/347/L00001-00118.pdf | norma | 3/3/1/2 | [L] según la nota del repo, no re-leída acá |
| Directiva 2006/112/CE, art. 226, copia de legislation.gov.uk (versión UE retenida) | https://www.legislation.gov.uk/eudr/2006/112/article/226 | norma | 3/3/1/1 | [S]: el buscador reproduce el punto 2 en inglés; el fetch devolvió vacío |
| Comisión Europea, *Explanatory notes: VAT invoicing rules (Directive 2010/45/EU)*, 05/10/2011, documento C-1/C-2 | https://taxation-customs.ec.europa.eu/system/files/2016-09/explanatory_notes_en.pdf | guía oficial no vinculante | 3/2/2/3 | [L] |
| EUR-Lex (texto consolidado) | https://eur-lex.europa.eu/eli/dir/2006/112/2020-01-01/eng | norma | 3/3/1/1 | no accesible (bloqueo del sitio a clientes automáticos) |
| Directiva (UE) 2025/516 (ViDA), cambio al art. 226 desde 1/7/2030 | https://datenbank.nwb.de/Dokument/452295_Article226 | secundaria (base alemana) | 1/1/1/1 | [S] no contrastada con el Diario Oficial |

### Afirmaciones

- Art. 226, punto 2: «un número secuencial, basado en una o varias series, que identifique la factura de forma única». En inglés: «a sequential number, based on one or more series, which uniquely identifies the invoice». La nota `comprobante-fiscal.md` ya cita esto (art. 226 punto 2) con la copia del BOE.
- La Comisión (nota C-2, 2011), literal: «The sequential number required in Article 226(2) to uniquely identify the invoice may be based on one or more series of numbers, which may include as well alphanumeric characters. The choice of using a different series of numbers lies with the business and it may be used for instance for each branch, or for each type of supply or for each customer, and covers as well self-billed invoices or invoices issued by third parties.» Los Estados miembros pueden exigir numeración secuencial en las facturas simplificadas con la misma regla de series. URL arriba [L].
- **Lo que no dice ninguna de las dos fuentes:** que la serie deba ser continua, sin huecos, ni que no se reutilicen números. El requisito legal de la Directiva es «secuencial» y «único». Un recomendado «sin huecos» sale de la práctica y del derecho nacional de cada país. La nota de Impuestos ya lo marca como inferencia de la base; la columna debe repetir esa cautela.
- Un comentario de Stripe (página de práctica, no se usa como fuente de derecho) lee el requisito como «único dentro de la serie y sin huecos» y advierte del riesgo al reiniciar por año: es la gloss de un tercero [S].
- Cambio futuro: según una base alemana [S], la Directiva 2025/516 agrega al art. 226, desde el 1 de julio de 2030, que la factura rectificativa lleve el número secuencial de la que corrige. Coincide con el art. 219 (rectificativa que «hace referencia expresa e inequívoca» a la inicial) que la nota del repo ya cita. Verificar con el Diario Oficial antes de usarlo.
- Alto riesgo (ley): dos fuentes para el texto de la Directiva (BOE y legislation.gov.uk) más la guía oficial; son copias del mismo texto, pero la guía de la Comisión es independiente en lo interpretativo. Para Argentina, no se investigó: pertenece a `software-de-gestion-en-argentina.md` y a `Comercio-electronico/Normativa/factura-electronica-de-arca.md`.

### Qué hay en el repo

- `Impuestos/Cumplimiento/comprobante-fiscal.md` (vigente): qué datos lleva, el art. 226, por qué la numeración no puede tener huecos (con la inferencia marcada), nota de crédito y débito, autofactura, factura electrónica (clearance), ViDA. Ya incluye la regla «un sistema asigna el número al emitir y no lo reutiliza».
- `Contabilidad/Control-interno/autorizaciones.md`: la numeración como control interno (prenumerados), con la inferencia y la declaración de que no hay fuente más allá de OpenStax.
- `Comercio-electronico/Normativa/factura-electronica-de-arca.md` (Argentina).

**Propio de la columna 2:** los estados del documento y cómo el sistema asigna el número (¿al borrador o al confirmar?, ¿qué pasa con un número asignado a un borrador que se descarta?, ¿series por sucursal o tipo?). Eso es diseño y lo único que la fuente nueva le suma es que la ley europea permite varias series por sucursal, tipo o cliente. Si se asigna al confirmar, un hueco por descarte no ocurre; es una decisión de diseño, no una fuente.

### Recurso canónico

La nota C-2 de las *Explanatory notes* de la Comisión Europea (una página) para lo que la norma deja a la elección del negocio, más la nota del repo `comprobante-fiscal.md` para el resto.

---

## Columna 9 y 11 (parte). Integración, sistema de registro y reportes

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Hohpe y Woolf, *Enterprise Integration Patterns*, cap. 2 «Integration Styles», sitio del libro | https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html | primaria | 3/2/2/2 | [L] la página introductoria |
| Fowler, «Integration Database», 25/5/2004 | https://martinfowler.com/bliki/IntegrationDatabase.html | primaria (practicante) | 3/2/2/2 | [L] completa |
| Fowler, «Reporting Database», 2/4/2014 | https://martinfowler.com/bliki/ReportingDatabase.html | primaria (practicante) | 3/2/2/2 | [L] completa |
| IBM, «What is a system of record?» | https://www.ibm.com/think/topics/system-of-record | secundaria de proveedor | 1/1/2/1 | [L] vía lectura asistida |
| Wikipedia, «System of record» | https://en.wikipedia.org/wiki/System_of_record | terciaria | 1/1/1/1 | [S] |
| Artículo de Medium sobre system of record, system of reference y golden record | https://medium.com/all-things-data/system-of-record-system-of-reference-golden-records-and-other-confusing-terms-in-master-data-23a87064bc05 | secundaria, blog | 1/1/1/1 | [S]; el propio texto dice que no coincide con el DMBOK |

### Afirmaciones

**Estilos de integración (Hohpe y Woolf).**
- Cuatro estilos, cada uno con su lema literal: *File Transfer* («Have each application produce files of shared data for others to consume, and consume files that others have produced»); *Shared Database* («Have the applications store the data they wish to share in a common database»); *Remote Procedure Invocation* («Have each application expose some of its procedures so that they can be invoked remotely»); *Messaging* («Have each application connect to a common messaging system, and exchange data and invoke behavior using messages»).
- Criterios para elegir: acoplamiento («Tightly coupled applications make numerous assumptions about how the other applications work»), frescura de los datos («the longer sharing can take, the more opportunity for shared data to become stale»), y fallas del otro lado («the remote application may not be running or the network may be unavailable»). Dicen que cada estilo tiene ventajas y desventajas y que la mensajería es «often the best style» en muchos casos. URL arriba. El informe 97 ya trae la lista de estilos; lo nuevo es la frase de criterios.

**Base compartida (el estilo que usan muchos productos de gestión de forma implícita).**
- Fowler: una *integration database* es «a database which acts as the data store for multiple applications»; exige un esquema que contemple a todos, suele estar controlada por una organización aparte, y los cambios «have to be negotiated»; sus ventajas (los cambios se ven al confirmar, sin capa de servicios) tienen como costo que «the database becomes a point of coupling»; concluye que «integration databases should be avoided». URL arriba.
- Un ERP como módulos sobre una sola base es, en este vocabulario, una base de integración con un solo dueño; la advertencia de Fowler pesa distinto cuando la misma organización controla todos los módulos. Esta es una lectura de la base, no de la fuente.

**Sistema de registro.**
- IBM: «A system of record (SOR) is an authoritative source of business data.» Lista al ERP entre los ejemplos (junto a CRM, HCM, MES, CMDB). Distingue de una única fuente de verdad (*single source of truth*): «An SSOT is more of a principle or practice for designing data systems», y da un ejemplo: un MES puede ser el sistema de registro del avance del montaje y una plataforma de datos maestros que combina varios sistemas podría ser la fuente de verdad. Es un texto de proveedor.
- Otros usan «sistema de referencia» (*system of reference*) con una definición distinta; el artículo de Medium dice que no coincide con DMBOK y que los términos son inconsistentes. **Las definiciones varían; la nota debe definir el término para sí y marcarlo.** No se encontró la definición de DAMA-DMBOK ni de Gartner.
- Dentro del repo, `Datos/Gobierno-y-calidad/datos-maestros.md` ya trata «quién manda en cada dato» y aconseja decidirlo «por campo y no por sistema». Es la misma idea sin el término *system of record*. `Arquitectura/Sistemas-distribuidos/api-led-connectivity.md` usa «sistema de registro» en una tabla (capa System).

**Por qué el reporte pesado no sale de la base operativa.**
- Fowler, *Reporting Database*, literal en lo clave: «The operational needs and the reporting needs are, however, often quite different - with different requirements from a schema and different data access patterns.» Recomienda una base de reportes con una copia de los datos operativos en otro esquema. Ventajas que lista: se puede diseñar para escribir reportes; no hace falta normalizarla porque es de solo lectura; el equipo puede refactorizar la base operativa sin tocar los reportes; «Queries run against the reporting database don't add to the load on the operational database»; admite datos derivados. Costo: mantenerla al día (carga nocturna o mensajería). Matiz útil: «many reporting needs work perfectly well with yesterday's data», y duda del valor del tiempo casi real. URL arriba [L].
- **Esto verifica y refuerza `oltp-y-olap.md`**, que se apoyaba en Kleppmann (no leído), C-Store y reseñas [S]. Fowler es una segunda fuente primaria, independiente y legible, para la misma afirmación. La nota no necesita repetirse en la columna; sí puede sumar este matiz de «reporte con datos de ayer» y el contraste con el reporte legal.
- Lo propio del software de gestión que **no** está en Fowler ni en `oltp-y-olap.md`: los reportes legales (libros) se exigen sobre la base de registro, con corte a una fecha y reproducibles; un libro no puede salir de una réplica atrasada. No se encontró fuente primaria que lo diga como tal; queda como hueco.

### Qué hay en el repo

- Columna 9: `Arquitectura/Sistemas-distribuidos/` (outbox, clave de idempotencia, saga, api-led, circuit breaker), `Datos/Gobierno-y-calidad/datos-maestros.md` (quién manda), `Datos/Ingesta-y-transformacion/etl-y-elt.md`, `Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion-en-el-comercio/integracion-con-tiendas-y-marketplaces.md` (según el informe 97), `Desarrollo/Evolucion/migraciones-y-actualizaciones.md`. No hay nota de los cuatro estilos de Hohpe y Woolf en el repo (verificar con búsqueda: no hay coincidencias en `Arquitectura/`).
- Columna 11: `Datos/Modelado-y-almacenamiento/oltp-y-olap.md`, `modelado-dimensional.md`, `Datos/Visualizacion-y-BI/` (capa semántica, tablero), `Contabilidad/Registro/libros-contables-en-argentina.md` e `Impuestos/Cumplimiento/registros-fiscales.md` (los reportes legales).

**Propio de la 9:** los cuatro estilos aplicados al ERP, la base compartida entre módulos como caso, y la carga inicial. **Propio de la 11:** qué reportes hay (operativos, legales), que se piden sobre datos con fecha de corte y que el ajuste de salida es el desajuste más citado (Soh et al.); el resto va en Datos.

### Recurso canónico

Hohpe y Woolf, cap. 2 (la página de estilos) para la 9; Fowler, *Reporting Database* y *Integration Database* para el contraste, ambos de una pantalla.

---

## Mapa de cobertura del repo por columna

Qué hay ya escrito y qué le queda propio (las notas se enlazan, no se copian).

| # | Columna | Ya cubierto en el repo | Propio de la columna |
|---|---|---|---|
| 1 | Datos maestros y partes | `Datos/Gobierno-y-calidad/datos-maestros.md` (registro de oro, dedupe, quién manda por campo); `Contabilidad/Registro/cuentas-corrientes.md` (cliente y proveedor) | La parte con roles y maestro frente a transacción; desajuste de datos de Soh et al. |
| 2 | Documento y estados | `Impuestos/Cumplimiento/comprobante-fiscal.md` (numeración, no se borra, nota de crédito); `Contabilidad/Control-interno/autorizaciones.md` (aprobaciones, prenumerados); `Contabilidad/Registro/asiento-y-libros.md` (corregir con otro asiento); `Bases-de-datos/Transacciones/` | El ciclo borrador → confirmado → anulado como diseño (en qué momento se numera, qué produce movimientos), la enmienda que apunta al anulado |
| 3 | Registro de movimientos y dimensiones | `Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md`; `Contabilidad/Registro/partida-doble.md` y `asiento-y-libros.md`; `Contabilidad/Contabilidad-de-gestion/centros-de-costo.md` (la dimensión analítica en contabilidad); `Datos/Modelado-y-almacenamiento/tabla-de-eventos.md`; `Arquitectura/Estilos/event-driven.md` | Reglas de contabilización (del documento al asiento), REA frente a partida doble (con la fuente de 2019) y dimensiones como atributo de la fila |
| 4 | Fechas, vigencias y cierre | `Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/retroactivos-y-reliquidaciones.md` (fecha del hecho y de registro, corregir con movimientos nuevos); `Contabilidad/Estados-contables/ajustes-de-cierre.md`; `Impuestos/Cumplimiento/declaracion-y-pago.md` | El patrón general (dos fechas, vigencia, fecha de bloqueo) y cómo lo traduce el software; hoy cada dominio lo explica por su lado |
| 5 | Cantidades, unidades y monedas | `Contabilidad/Operaciones/moneda-extranjera.md` (moneda funcional, diferencia realizada y no realizada); `Inventario-y-depositos/Existencias/articulo.md` (unidad de medida y conversiones); `Planillas-de-calculo/Modelo-de-la-planilla/tipos-de-dato.md` (redondeo) | Un número de negocio viaja con su unidad o moneda; redondeo y conversión como decisión de diseño |
| 6 | Estructura de la organización | `Arquitectura/Sistemas-distribuidos/multi-tenancy.md` (lo que no es); `Administracion-de-personal-y-nomina/Legajo/puesto-y-estructura.md` (estructura de personas); `Contabilidad/Contabilidad-de-gestion/centros-de-costo.md` | Varias empresas, sucursales, qué se comparte y qué es de cada una; opcionalidad |
| 7 | Permisos y separación de funciones | `Contabilidad/Control-interno/separacion-de-funciones.md` y `controles-sobre-sistemas.md` y `autorizaciones.md` (muy completas); `Cloud/Gobernanza-e-identidad/` (RBAC de la nube, otra capa) | Modelo de permisos del software (rol, registro, incompatibilidad) y reglas configurables; no repetir la teoría de control interno |
| 8 | Auditoría | `Contabilidad/Control-interno/controles-sobre-sistemas.md` (pista de auditoría, tabla de lo que el sistema debe registrar); `Datos/Gobierno-y-calidad/metadatos-y-linaje.md`; `DevOps/Repositorios/trazabilidad-de-cambios.md` (según el informe 97) | Rastro de cambios en maestros y configuración (lo que no deja movimientos); frontera con la columna 3 |
| 9 | Integración y migración | `Arquitectura/Sistemas-distribuidos/*`; `Datos/Gobierno-y-calidad/datos-maestros.md` («quién manda»); `Datos/Ingesta-y-transformacion/etl-y-elt.md`; `Desarrollo/Evolucion/migraciones-y-actualizaciones.md` | Sistema de registro por dato, estilos de Hohpe y Woolf aplicados, carga inicial |
| 10 | Configurar o personalizar | Casi nada (`costo-total-de-adquisicion.md`, `costos-de-cambio.md` como marco) | Toda la columna |
| 11 | Reportes | `Datos/Modelado-y-almacenamiento/oltp-y-olap.md`; `Datos/Visualizacion-y-BI/`; `Contabilidad/Registro/libros-contables-en-argentina.md`; `Impuestos/Cumplimiento/registros-fiscales.md` | Reportes operativos y legales como salida del sistema, con corte a una fecha; el desajuste de salida |

Columnas 4, 5, 6 y 8 no se investigaron acá (no estaban en el encargo).

## Huecos

- **Brehm, Heinzl y Markus 2001**: no hay copia abierta; ni Semantic Scholar ni Crossref traen abstract. La lista de tipos solo está en secundarias que discrepan (7, 8 o 9). Hay que pedirlo por biblioteca.
- **Soh, Sia y Tay-Yap 2000**: PDF tras muro (ACM, 403 y verificación de JavaScript; core.ac.uk, 403). Categorías confirmadas por extractos; sin recuento por categoría y sin la cita exacta de «más frecuente».
- **McCarthy 1982**: sin acceso al texto; se usa el libro de 2019 (el mismo autor) y la revisión de Nikitkov. La tesis de Hruby 2006 sobre la partida doble: solo una reseña [S]. ISO 15944-4: de pago, sin leer. Falta además una fuente independiente de REA (no promotora); lo leído es de los autores o de revisiones de la comunidad REA.
- **COSO 2013, puntos de foco del principio 10**: de pago; solo el Executive Summary [L]. La tríada autorizar-registrar-custodiar no tiene fuente normativa en COSO; sale de manuales y de OpenStax.
- **Directiva 2006/112**: EUR-Lex bloquea clientes automáticos; se usó copia del BOE (según la nota del repo), legislation.gov.uk por buscador y la guía oficial de la Comisión. La modificación de 2025/516 al art. 226, por una base alemana [S]. Sin numeración de comprobantes de Argentina (fuera de alcance de este ángulo).
- **Costo de personalizar al actualizar**: ningún estudio independiente con cifras. Los números que circulan salen de consultoras y vendedores. El estudio más sólido es chico y con un proveedor como socio. Podría buscarse el trabajo de Rothenberger y Srite (2009, IEEE TEM) y a Zach y Munkvold (2012), que el buscador sugirió pero no se leyeron.
- **Sistema de registro**: sin la definición de DAMA-DMBOK ni la de Gartner; las que hay son de un proveedor y de blogs, y se contradicen en «sistema de referencia».
- **Reportes legales sobre la base de registro con fecha de corte**: no hay fuente primaria que lo afirme; es lectura propia.
- **Hohpe y Woolf**: solo la página de introducción de estilos [L]; el libro no se leyó.
