# Gobierno y calidad de datos: informe de investigación

Fecha de la investigación: 2026-11-27. Vertical en nivel panorama, salvo la privacidad (ley, alto riesgo). Marcas: [L] texto completo leído, [M] metadatos/abstract, [S] resumen secundario o del buscador. Aclaración de método: las páginas se leyeron con un extractor que devuelve resúmenes y citas cortas, no el texto completo; por eso las normas figuran como [L] solo en los artículos cuyas citas literales se obtuvieron, y se aclara artículo por artículo.

## Sobre la división del árbol

La vertical "Gobierno-y-calidad" coincide con cómo DAMA agrupa el campo (gobierno, calidad, metadatos, datos maestros y de referencia son áreas de conocimiento separadas del DMBOK), pero tiene una asimetría: la privacidad no es un área propia de DAMA (DMBOK la trata dentro de seguridad y de gobierno/ética), y acá pesa más que el resto porque es ley. Recomendación: nota propia de privacidad (Ley 25.326) dentro de la vertical, separada de las notas conceptuales de gobierno y calidad. Linaje y catálogo se ubican con metadatos; la "calidad" se toca con Ingesta-y-transformacion (los tests de dbt viven en la transformación) y con Analitica-de-producto (calidad del tracking de eventos). No hay tensión mayor con el árbol.

---

## 1. Gobierno de datos

### Fuentes

| Fuente | Tipo | Autoridad | Profundidad | Ejemplos | Unicidad | Marca |
|---|---|---|---|---|---|---|
| DAMA International, página DMBOK https://www.dama.org/cpages/body-of-knowledge | Primaria (institución) | 3 | 1 | 1 | 2 | [M] |
| DAMA-DMBOK2 (libro, Technics Publications) https://technicspub.com/dmbok2 | Primaria | 3 | 3 | 2 | 3 | No leído (de pago); hueco |

### Afirmaciones

- DAMA presenta la 2.ª edición del DMBOK como la vigente; la página menciona una "DAMA-DMBOK 2.0 Revision" lanzada en 2024 y un proyecto "DMBOK 3.0" (evergreening) iniciado en 2025. La página lista como novedades de la 2.ª edición más ética de datos, contenido de gobierno actualizado, integración e interoperabilidad. https://www.dama.org/cpages/body-of-knowledge [M]
- No se pudo citar literalmente la definición de DAMA de "data governance" ni la lista de áreas de conocimiento: están en el libro. Quien escriba la nota debe leer el capítulo 3 (Data Governance) del DMBOK2 o declarar la definición como no verificada. Hueco.
- Roles (data owner, data steward): no se verificaron en fuente primaria en esta ronda. Se declara hueco; el criterio de proporcionalidad para empresa chica (una persona con el rol de dueña de cada conjunto de datos, sin comité) es una recomendación editorial, no un hallazgo.

### Recurso canónico

DAMA-DMBOK2, capítulo "Data Governance" (y capítulo "Data Quality"). Fijarse en: definición de gobierno como decisión de derechos y responsabilidades sobre los datos, roles (owner, steward) y los principios; ignorar la parte de organización corporativa grande, o presentarla como "lo que una empresa chica no necesita".

---

## 2. Calidad de datos

### Fuentes

| Fuente | Tipo | Autoridad | Profundidad | Ejemplos | Unicidad | Marca |
|---|---|---|---|---|---|---|
| UK Government, "Meet the data quality dimensions" https://www.gov.uk/government/news/meet-the-data-quality-dimensions | Primaria (gobierno; adopta las definiciones de DAMA UK) | 2 | 2 | 2 | 2 | [L] (definiciones citadas literalmente) |
| UK Government Data Quality Framework https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework | Primaria | 2 | 3 | 2 | 2 | [S] |
| DAMA UK, "The Six Primary Dimensions for Data Quality Assessment" (2013), copia en https://joelbth.codeberg.page/community-notices/dama-quality-dimensions.pdf | Primaria, copia de tercero (procedencia no verificada) | 2 | 2 | 1 | 2 | [S] |
| ISO/IEC 25012:2008 (catálogo ISO) https://iso.org/standard/35736.html | Primaria (norma) | 3 | 3 | 1 | 3 | [M] |
| ISO/IEC 25012 vista previa (VDE) https://assets.vde-verlag.de/iec-normen/preview-pdf/info_isoiec25012%7Bed1.0%7Den.pdf | Primaria (solo índice) | 3 | 1 | 1 | 2 | [L] del índice |
| iso25000.com sobre ISO 25012 https://iso25000.com/index.php/en/iso-25000-standards/iso-25012 | Secundaria (sitio de divulgación de la familia SQuaRE) | 1 | 2 | 1 | 1 | [L] |
| dbt Docs, Data tests https://docs.getdbt.com/docs/build/data-tests | Primaria (documentación oficial de proveedor), sin fecha visible; menciona v1.10.5 y v2 | 3 | 2 | 3 | 2 | [L] |

### Afirmaciones

- Las seis dimensiones, con las definiciones literales del gobierno del Reino Unido, que las recomienda "as defined by the Data Management Association UK (DAMA(UK))": https://www.gov.uk/government/news/meet-the-data-quality-dimensions [L]
  - Completitud: "Data is considered complete when all the data required for a particular use is present and available to be used."
  - Unicidad: "Data is unique if it appears only once in a data set."
  - Consistencia: "Consistency is achieved when data values do not conflict with other values within a record or across different data sets."
  - Oportunidad (timeliness): "Timeliness indicates whether the data is available when expected and needed."
  - Validez: "Validity is defined as the extent to which the data conforms to the expected format, type, and range."
  - Exactitud: "We have accuracy when data reflects reality."
- Discrepancia de atribución: una página de IBM atribuye las mismas seis dimensiones a DAMA International y no a DAMA UK. La definición original es del documento de DAMA UK (grupo de trabajo, octubre de 2013, según el buscador [S]). Conviene citar "DAMA UK" y aclarar que DMBOK las recoge. https://ibm.com/docs/SSQNUZ_5.2.x/wsj/quality/dq-dimensions.html [S]
- ISO/IEC 25012:2008 define un modelo de calidad de datos "retained in a structured format within a computer system"; fue revisada y confirmada en 2025, o sea que la edición de 2008 sigue vigente. https://iso.org/standard/35736.html [S del buscador sobre la página ISO]
- El modelo tiene quince características vistas desde dos puntos de vista, inherente y dependiente del sistema. El índice oficial de la norma confirma tres secciones: 5.3.1 punto de vista inherente, 5.3.2 inherente y dependiente del sistema, 5.3.3 dependiente del sistema. https://assets.vde-verlag.de/iec-normen/preview-pdf/info_isoiec25012%7Bed1.0%7Den.pdf [L, solo índice]
- Definiciones literales de iso25000.com para tres características inherentes: exactitud ("The degree to which data has attributes that correctly represent the true value"), completitud ("The degree to which subject data associated with an entity has values for all expected attributes") y consistencia ("The degree to which data has attributes that are free from contradiction and are coherent with other data"). Nombra además credibilidad, actualidad (currentness) y accesibilidad. https://iso25000.com/index.php/en/iso-25000-standards/iso-25012/ [L, secundaria]
- NO VERIFICADO: la lista completa de las quince y su reparto (la distribución 5 inherentes / 7 mixtas / 3 del sistema que circula proviene de memoria y de la respuesta del extractor, no de un texto legible). No usarla en la nota sin confirmarla contra el texto de la norma (de pago) o con el resumen de arc42: https://quality.arc42.org/standards/iso-iec-25012 [no leído].
- Cómo se detecta: en dbt, un test de datos es una consulta SQL que busca filas que contradicen la afirmación: "they are `select` statements that seek to grab 'failing' records, ones that disprove your assertion"; "If the data test returns zero failing rows, it passes". https://docs.getdbt.com/docs/build/data-tests [L]
- dbt trae cuatro tests genéricos: `unique`, `not_null`, `accepted_values` y `relationships` (integridad referencial: cada `customer_id` de `orders` existe como `id` en `customers`). Los tests singulares son archivos `.sql` propios en la carpeta `tests`. `dbt test --store-failures` guarda las filas que fallan. Severidad `warn` o `error` configurable. https://docs.getdbt.com/docs/build/data-tests [L]
- Correspondencia útil para la nota (editorial, no de una fuente): `not_null` mide completitud, `unique` mide unicidad, `accepted_values` mide validez, `relationships` mide consistencia referencial; exactitud y oportunidad no salen de un test genérico (la oportunidad se mide con frescura de la fuente, que dbt maneja aparte con `source freshness`: no verificado acá).

### Recurso canónico

La página de gov.uk "Meet the data quality dimensions" para el vocabulario (corta, definiciones citables, apta para un lector sin base), más la página de data tests de dbt para el "cómo se detecta". Para el rigor, el modelo ISO/IEC 25012 (solo la sección 5.3). Fijarse en: que cada dimensión se traduce en una pregunta que se puede responder con una consulta.

---

## 3. Metadatos, linaje y catálogo

### Fuentes

| Fuente | Tipo | Autoridad | Profundidad | Ejemplos | Unicidad | Marca |
|---|---|---|---|---|---|---|
| OpenLineage, documentación y modelo de objetos https://openlineage.io/docs/spec/object-model | Primaria (especificación abierta) | 3 | 2 | 2 | 2 | [S] (resultado del buscador) |
| OpenLineage, facets https://openlineage.io/docs/spec/facets/ | Primaria | 3 | 2 | 2 | 1 | [S] |

### Afirmaciones

- OpenLineage se describe como "an open framework for data lineage collection and analysis"; el modelo gira sobre tres entidades, job, run y dataset; dataset y job se identifican por `namespace` y `name`, el run por `runId`; los "facets" son las extensiones de metadatos sobre esas entidades (por ejemplo `schema` de un dataset, `sql` o `sourceCode` de un job). La documentación vista cubría la versión 1.40.1. https://openlineage.io/docs/spec/object-model y https://openlineage.io/docs/spec/facets/ [S]
- HUECO: no se halló en esta ronda una definición canónica de "metadatos", "catálogo de datos" ni de "linaje" en fuente primaria general (DMBOK cap. Metadata Management sería la fuente; no leído). OpenLineage sirve para el linaje como especificación técnica, no como definición de concepto.
- Para el nivel de la audiencia (empresa chica, usa planillas): el equivalente cotidiano es un diccionario de datos (qué significa cada columna, quién la mantiene, de dónde viene). Es propuesta editorial.

### Recurso canónico

Capítulo "Metadata Management" del DMBOK2 para el concepto (no leído); la página de object model de OpenLineage para ver cómo se modela el linaje (fijarse en que el linaje se registra como eventos de ejecuciones que leen y escriben datasets).

---

## 4. Datos maestros y de referencia

### Fuentes

| Fuente | Tipo | Autoridad | Profundidad | Ejemplos | Unicidad | Marca |
|---|---|---|---|---|---|---|
| TechTarget, definición de MDM https://www.techtarget.com/searchdatamanagement/definition/master-data-management | Secundaria (prensa técnica) | 1 | 2 | 1 | 1 | [S] |
| IBM, "What is MDM" https://ibm.com/topics/master-data-management | Secundaria (proveedor) | 2 | 2 | 1 | 1 | [S] |
| SAP, MDM overview https://www.sap.com/mena/resources/what-is-mdm | Secundaria (proveedor) | 2 | 2 | 1 | 1 | [S] |
| Built In https://builtin.com/articles/master-data-management | Secundaria | 1 | 2 | 2 | 1 | [S] |

### Afirmaciones

- MDM crea "a uniform set of data on customers, products, suppliers and other business entities across different IT systems"; el registro de referencia se llama "golden record". https://www.techtarget.com/searchdatamanagement/definition/master-data-management [S]
- El trabajo es identificar registros que refieren a la misma entidad real y fusionarlos en uno ("Identify records that refer to the same real-world entity and combine them into a single, complete master record"). https://www.sap.com/mena/resources/what-is-mdm [S]
- Métodos de coincidencia: reglas determinísticas (campos exactos), puntuación probabilística (nombre, dirección, teléfono) y modelos de aprendizaje automático; estilo "registry": un índice de referencias cruzadas ("record #123 in System A is the same as record #456 in System B") sin copiar los datos. https://builtin.com/articles/master-data-management [S] (fuente de divulgación, tomar con cuidado)
- Datos de referencia: códigos genéricos como países, monedas, estados de pedido. https://www.techtarget.com/searchdatamanagement/definition/master-data [S]
- Todas son fuentes secundarias de proveedores y prensa que parafrasean la misma idea: valen como una sola fuente. La definición de DAMA no se leyó. El ejemplo del cliente duplicado entre tienda online, punto de venta y mercado de pagos es editorial; se conecta con la nota de Comercio electrónico (otro tema de la base).

### Recurso canónico

DMBOK2, capítulo "Reference & Master Data" (no leído). Alternativa de bajo costo: la definición de IBM, avisando que es de proveedor.

---

## 5. Privacidad de datos personales en Argentina (alto riesgo)

Este informe no reemplaza asesoramiento legal: la nota debe decirlo. Regla de la tarea: dos fuentes independientes por afirmación; abajo, el texto de la norma va primero y la segunda fuente (la autoridad de aplicación, AAIP, o secundaria) se indica. Cuando hay una sola, se dice.

### Fuentes

| Fuente | Tipo | Autoridad | Profundidad | Ejemplos | Unicidad | Marca |
|---|---|---|---|---|---|---|
| Ley 25.326, texto en infoleg https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/norma.htm | Primaria (norma) | 3 | 3 | 1 | 3 | [L] parcial (citas ≤125 caracteres por artículo) |
| Ley 25.326, argentina.gob.ar https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto | Primaria (misma norma, otro portal oficial; cuenta como un solo texto) | 3 | 3 | 1 | 1 | [L] parcial |
| Decreto 1558/2001 https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368/texto | Primaria (norma reglamentaria) | 3 | 2 | 1 | 3 | [L] parcial |
| AAIP, obligaciones de responsables https://www.argentina.gob.ar/node/53779 | Primaria (autoridad de aplicación) | 3 | 1 | 1 | 2 | [L] resumido |
| AAIP, transferencias internacionales https://www.argentina.gob.ar/transferencias-internacionales | Primaria (autoridad) | 3 | 2 | 1 | 3 | [L] |
| Resolución AAIP 244/2022 https://www.argentina.gob.ar/normativa/nacional/norma-376196/texto | Primaria (norma) | 3 | 2 | 1 | 3 | [L] |
| Resolución AAIP 240/2022 (clasificación de infracciones), vía IAPP/Baker McKenzie https://iapp.org/news/a/se-modifico-la-clasificacion-y-graduacion-por-infracciones-a-la-ley-de-proteccion-de-datos-personales-en-argentina | Secundaria | 2 | 2 | 1 | 1 | [S] |
| Ley 27.699 (Convenio 108+), argentina.gob.ar https://www.argentina.gob.ar/normativa/nacional/norma-375738/texto | Primaria (norma) | 3 | 1 | 1 | 3 | [L] parcial |
| Ley 27.483 (Convenio 108), vía buscador; copias https://cijur.mpba.gov.ar/files/auctions/resolutions/Ley_N__27483.pdf | Primaria (copia de tercero) | 3 | 1 | 1 | 2 | [S] |
| Diario Judicial, abril 2026 https://www.diariojudicial.com/news-103126-proteccion-de-datos-personales-sigue-siendo-suficiente-la-ley-25326-en-2026 | Secundaria (prensa) | 1 | 1 | 1 | 1 | [L] |

### 5.1 Definiciones

- Dato personal: "Información de cualquier tipo referida a personas físicas o de existencia ideal determinadas o determinables." (art. 2). Nota para la base: la ley protege también a personas de existencia ideal (jurídicas), a diferencia del RGPD europeo. https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/norma.htm [L]
- Datos sensibles: "Datos personales que revelan origen racial y étnico, opiniones políticas, convicciones religiosas, filosóficas o morales, afiliación sindical e información referente a la salud o a la vida sexual." (art. 2). https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]
- Email, teléfono y compras de un cliente son datos personales (identifican o hacen determinable a la persona). Es inferencia sobre el texto del art. 2, no una afirmación literal de una norma; ver hueco.
- Ninguna persona puede ser obligada a dar datos sensibles: "Ninguna persona puede ser obligada a proporcionar datos sensibles." (art. 7 inc. 1). https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]

### 5.2 Calidad, finalidad y conservación (art. 4)

- "Los datos personales que se recojan a los efectos de su tratamiento deben ser ciertos, adecuados, pertinentes y no excesivos en relación al ámbito y finalidad para los que se hubieren obtenido." (art. 4 inc. 1). https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]; segunda fuente (resumen del mismo texto): https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/norma.htm [L]. Nota: ambas son la misma norma en dos portales.
- "Los datos deben ser destruidos cuando hayan dejado de ser necesarios o pertinentes a los fines para los cuales hubiesen sido recolectados." (art. 4 inc. 7). https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]
- Conexión con la vertical: el art. 4 pone por ley dos dimensiones de calidad (exactitud y actualización) y la minimización de datos. Es el punto donde calidad y privacidad se tocan.

### 5.3 Consentimiento (art. 5) y deber de informar (art. 6)

- "El tratamiento de datos personales es ilícito cuando el titular no hubiere prestado su consentimiento libre, expreso e informado" (art. 5 inc. 1). https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]
- Excepciones al consentimiento (art. 5 inc. 2), la ley enumera a) a e): fuentes de acceso público irrestricto; funciones propias del Estado u obligación legal; listados limitados a nombre, DNI, identificación tributaria y similares (texto cortado en la cita); y la que más importa a un comercio, d) "Deriven de una relación contractual, científica o profesional del titular de los datos, y resulten necesarios para su desarrollo o cumplimiento"; e) operaciones de entidades financieras. https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]. Implicancia, con cautela: el email y el domicilio necesarios para entregar una compra caen en la excepción contractual; usar esos mismos datos para marketing o para analítica con terceros va más allá de lo "necesario para el desarrollo o cumplimiento" y requiere consentimiento. Es lectura del texto, no doctrina verificada.
- Consentimiento informado, según el Decreto 1558/2001 art. 5: "El consentimiento informado es el que está precedido de una explicación, al titular de los datos, [...]" adecuada a su nivel social y cultural; y "El consentimiento dado para el tratamiento de datos personales puede ser revocado en cualquier tiempo." (sin efectos retroactivos). https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368/texto [L, citas parciales]
- Deber de informar (art. 6): "Cuando se recaben datos personales se deberá informar previamente a sus titulares en forma expresa y clara:" finalidad, destinatarios, existencia del archivo y su responsable, carácter obligatorio o facultativo de las respuestas, y derechos de acceso, rectificación y supresión. https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]; segunda fuente: AAIP https://www.argentina.gob.ar/node/53779 [L resumido].

### 5.4 Derechos de acceso, rectificación y supresión (arts. 14 a 16)

- Acceso: "El titular de los datos, previa acreditación de su identidad, tiene derecho a solicitar y obtener información" (art. 14); plazo: "El responsable o usuario debe proporcionar la información solicitada dentro de los diez días corridos de haber sido intimado fehacientemente." (art. 14 inc. 2). https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]. El derecho de acceso se ejerce gratuitamente a intervalos no menores de seis meses salvo interés legítimo (resumen del extractor sobre infoleg [S]).
- Rectificación, actualización o supresión: "en el plazo máximo de cinco días hábiles de recibido el reclamo del titular de los datos" (art. 16 inc. 2); si no se cumple, el interesado puede "promover sin más la acción de protección de los datos personales o de hábeas data" (art. 16 inc. 3). https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]
- El Decreto 1558/2001 dice que el pedido de acceso "no requiere de fórmulas específicas, siempre que garantice la identificación del titular" (art. 14 reglamentado). https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368/texto [L, cita parcial]
- Habeas data (arts. 33 y 34): acción para saber qué datos hay en bancos públicos o privados destinados a informes y para exigir corrección, supresión o confidencialidad. https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/norma.htm [S del extractor].

### 5.5 Seguridad (art. 9)

- "El responsable o usuario del archivo de datos debe adoptar las medidas técnicas y organizativas que resulten necesarias" para garantizar la seguridad y confidencialidad; está prohibido registrar datos en sistemas sin condiciones de integridad y seguridad. https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]; segunda fuente (AAIP): "Las bases de datos personales deben garantizar la seguridad y confidencialidad de los datos personales." https://www.argentina.gob.ar/node/53779 [L resumido]. La ley no fija medidas concretas; no se verificó en esta ronda si la AAIP publicó medidas mínimas de seguridad (hueco: existen disposiciones de la AAIP sobre medidas de seguridad en bases, no leídas).

### 5.6 Registro de bases ante la AAIP (arts. 21 y 24)

- "Todo archivo, registro, base o banco de datos público, y privado destinado a proporcionar informes debe inscribirse en el Registro que al efecto habilite el organismo de control." (art. 21 inc. 1). https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]
- "Los particulares que formen archivos, registros o bancos de datos que no sean para un uso exclusivamente personal deberán registrarse conforme lo previsto en el artículo 21." (art. 24). Mismo texto, mismo portal. [L]
- La AAIP dice: "deben estar inscriptos en el Registro Nacional de Bases de Datos Personales"; los archivos de uso personal están exceptuados; "Incumplir con esta obligación puede ocasionar sanciones." https://www.argentina.gob.ar/node/53779 [L resumido]
- Tensión de lectura que la nota debe mostrar: el art. 21 dice "destinado a proporcionar informes" y el art. 24 dice cualquier base de particulares que no sea de uso exclusivamente personal. El Decreto 1558/2001 art. 24 figura "Sin reglamentar" y su art. 1 amplía el concepto de bases privadas "destinadas a dar informes" a las que van más allá del uso personal o transfieren datos. https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368/texto [L resumido]. Conclusión prudente: una base de clientes de un comercio probablemente debe inscribirse; esto requiere confirmación legal.

### 5.7 Transferencia internacional (art. 12) y analítica en el exterior

- "Es prohibida la transferencia de datos personales de cualquier tipo con países u organismos internacionales o supranacionales, que no propocionen niveles de protección adecuados." (art. 12 inc. 1; "propocionen" tal como figura en la fuente). Excepciones (inc. 2): colaboración judicial internacional; datos médicos si lo exige el tratamiento; transferencias bancarias o bursátiles; tratados; cooperación entre organismos de inteligencia. https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]
- El Decreto 1558/2001 agrega que la prohibición "no rige cuando el titular de los datos hubiera consentido expresamente la cesión." https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368/texto [L, cita parcial]
- Países considerados adecuados por la AAIP (Disposición DNPDP 60/2016 y Resolución AAIP 34/2019): Estados miembros de la UE y del EEE; Reino Unido; Suiza; Guernsey; Jersey; Isla de Man; Islas Feroe; Canadá (solo sector privado); Andorra; Nueva Zelanda; Uruguay; Israel (solo tratamiento automatizado). Estados Unidos no figura en la lista, y la página no menciona el Data Privacy Framework. https://www.argentina.gob.ar/transferencias-internacionales [L]. Fecha de verificación: 2026-11-27; la lista cambia por resolución.
- Para destinos no adecuados: excepciones del art. 12, consentimiento expreso, cláusulas contractuales modelo aprobadas (Disposición 60/2016 y Resolución 198/2023, Red Iberoamericana), o normas corporativas vinculantes; los contratos que se aparten de los modelos deben presentarse ante la AAIP "dentro de los 30 días" de la firma. https://www.argentina.gob.ar/transferencias-internacionales [L]; coincide la página de obligaciones: https://www.argentina.gob.ar/node/53779 [L resumido]. Dos fuentes, ambas de la AAIP (no son independientes entre sí en autoría, pero sí en páginas); el origen primario son las disposiciones, no leídas en su texto.
- Implicancia para "mandar datos de clientes a una herramienta de analítica en el exterior": es una transferencia internacional si los datos personales viajan a servidores en un país no adecuado (típicamente EE. UU.). Las vías son consentimiento expreso informado, cláusulas modelo con el proveedor o un contrato aprobado. Si los datos se envían seudonimizados o agregados, si dejan de ser "determinables" es una cuestión de hecho que no se resolvió acá. El proveedor puede ser además un "prestador de servicios de tratamiento por cuenta de terceros" (art. 25: no puede aplicar los datos a fin distinto del contrato y debe destruirlos al terminar, con posible retención hasta dos años [S del extractor]).

### 5.8 Sanciones

- Administrativas (art. 31 inc. 1, texto original): "el organismo de control podrá aplicar las sanciones de apercibimiento, suspensión, multa de mil pesos ($ 1.000.-) a cien mil pesos ($ 100.000.-), clausura o cancelación del archivo, registro o banco de datos." https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto [L]
- Los topes en pesos de la ley fueron superados por la Resolución AAIP 244/2022 (05/12/2022, B.O. 06/12/2022): infracciones leves hasta "PESOS TRES MILLONES ($ 3.000.000.-)", graves "PESOS DIEZ MILLONES ($ 10.000.000.-)", muy graves "PESOS QUINCE MILLONES ($ 15.000.000.-)". El texto no menciona UVA ni indexación automática. https://www.argentina.gob.ar/normativa/nacional/norma-376196/texto [L]. Segunda fuente, secundaria: la Resolución 240/2022 clasifica las infracciones en leves, graves y muy graves; apercibimientos máximos de 2, 4 y 6 respectivamente; y mantiene el Registro de Infractores. https://iapp.org/news/a/se-modifico-la-clasificacion-y-graduacion-por-infracciones-a-la-ley-de-proteccion-de-datos-personales-en-argentina [S]. La Resolución 179/2025 (26/09/2025) modificó la estructura del Registro de Infractores (solo vía buscador [S]; texto en https://www.argentina.gob.ar/normativa/nacional/norma-418053/texto, no leído).
- Cómo se gradúan (Decreto 1558/2001 art. 31): "La cuantía de las sanciones se graduará atendiendo a la naturaleza de los derechos personales afectados," entre otros factores, con reincidencia en tres años. https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368/texto [L, cita parcial]
- Penales (art. 32, que agrega los arts. 117 bis y 157 bis al Código Penal): insertar a sabiendas datos falsos, acceder ilegítimamente o revelar datos de un banco de datos personales; agravantes para funcionarios y si hay daño. https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/norma.htm [S del extractor]. Una sola fuente; el texto de los arts. 117 bis y 157 bis del Código Penal no se leyó.
- Autoridad: el Decreto 1558/2001 creó la Dirección Nacional de Protección de Datos Personales; hoy la función la ejerce la AAIP (Agencia de Acceso a la Información Pública) según sus propias páginas. https://www.argentina.gob.ar/node/53779 [L resumido]

### 5.9 Convenio 108 y 108+

- La Ley 27.483 aprueba el Convenio 108 del Consejo de Europa (Estrasburgo, 28 de enero de 1981); sancionada el 6 de diciembre de 2018, promulgada por el Decreto 1197/2018 el 28/12/2018, publicada en el B.O. el 2/1/2019. https://www.argentina.gob.ar/normativa/nacional/norma-318246/texto (Decreto 1197/2018, no leído) y copia https://cijur.mpba.gov.ar/files/auctions/resolutions/Ley_N__27483.pdf [S]. Una fuente indica que el Convenio entró en vigor en Argentina en junio de 2019; la publicación oficial es de enero de 2019. Discrepancia entre entrada en vigor y publicación, dar ambas.
- Ojo: el enlace que figuraba como argentina.gob.ar/normativa/nacional/ley-27483-317275/texto devolvió otra norma (Disposición 34/2018 de trabajo), no usarlo.
- La Ley 27.699 aprueba el Protocolo modificatorio (Convenio 108+, suscripto en Estrasburgo el 10 de octubre de 2018); sancionada el 9 de noviembre de 2022 y publicada en el B.O. el 30 de noviembre de 2022 (B.O. 35058). https://www.argentina.gob.ar/normativa/nacional/norma-375738/texto [L parcial]. Segunda fuente: el Decreto 792/2022 la promulgó, según el buscador [S].
- Qué implican: Argentina quedó obligada a tener una ley acorde al Convenio, lo que alimenta la reforma de la 25.326. Los tratados no crean por sí obligaciones directas para un comercio; las crea la ley interna. (Inferencia editorial.)

### 5.10 Estado de los proyectos de reforma (fechado 2026-11-27)

- La Ley 25.326 sigue vigente. Diario Judicial (07/04/2026) dice que "Los proyectos de reforma buscan modernizar el sistema y alinearlo con estándares internacionales" y lista contenidos en discusión: más responsabilidad, "sanciones más altas vinculadas a la capacidad económica", roles ampliados y privacidad desde el diseño; no nombra proyectos ni etapa. https://www.diariojudicial.com/news-103126-proteccion-de-datos-personales-sigue-siendo-suficiente-la-ley-25326-en-2026 [L]
- Según el buscador (no confirmado en fuente primaria): la AAIP presentó un anteproyecto (documento "mensaje proyecto ley PDP 2023" en https://www.argentina.gob.ar/sites/default/files/mensaje_proyecto_leypdp2023.pdf, PDF escaneado que no se pudo leer); el 16 de julio de 2026 el diputado Agustín Rossi habría ingresado el expediente 3397-D-2026 para derogar las leyes 25.326 y 26.343; hay proyectos de Pablo Carro y Martín Doñate; ninguno con dictamen ni aprobación en los resultados. [S]. Verificar en https://www.hcdn.gob.ar antes de citar expedientes.
- Conclusión: a la fecha, para efectos prácticos rige la 25.326 con su Decreto 1558/2001 y las resoluciones de la AAIP. El estado legislativo se declara no verificado.

### Qué implica para un comercio (resumen editorial, sujeto a confirmación legal)

1. Email, teléfono y compras son datos personales: finalidad clara, no excesivos, informados (arts. 4 y 6).
2. Usarlos para cumplir la compra cae en la excepción contractual; usarlos para otra cosa (marketing, analítica con terceros) pide consentimiento libre, expreso e informado, revocable.
3. Dar acceso, corregir o borrar si el cliente lo pide: 10 días corridos y 5 días hábiles.
4. Cuidar seguridad (art. 9) y probablemente inscribir la base en la AAIP.
5. Enviar a analítica en EE. UU. es transferencia a país no adecuado: consentimiento expreso o cláusulas modelo.
6. Multas administrativas hasta $15.000.000 por infracción muy grave (Res. 244/2022; no se verificó actualización posterior) y responsabilidad penal en los casos del art. 32.

### Recurso canónico

El texto de la Ley 25.326 en infoleg/argentina.gob.ar (artículos 2, 4, 5, 6, 9, 12, 14 a 16, 21, 24, 31) leído junto con el Decreto 1558/2001, y la sección de datos personales de la AAIP (https://www.argentina.gob.ar/aaip/datospersonales) para obligaciones, registro y transferencias vigentes. Fijarse en: la excepción contractual del art. 5 inc. 2 d), la lista de países adecuados (cambia) y las resoluciones de sanciones. Citar siempre con fecha de consulta.

---

## Huecos

- Definición de DAMA de gobierno de datos, roles de owner y steward, y áreas del DMBOK: no verificados (libro de pago, la página institucional no los trae).
- ISO/IEC 25012: las quince características y su reparto, no verificados contra el texto (la vista previa legible solo tiene el índice).
- Dimensiones de calidad: el documento original de DAMA UK solo se vio en una copia de tercero [S]; se usó la adopción del gobierno británico como fuente citable.
- Metadatos y catálogo: sin fuente primaria conceptual; linaje solo vía especificación OpenLineage [S].
- MDM: solo fuentes secundarias y de proveedores (cuentan como una); falta la definición de DAMA y un caso real de cliente duplicado.
- Privacidad: textos de normas leídos mediante extractor con citas cortas; los artículos 25, 26, 32 a 34 y las disposiciones de la AAIP (60/2016, 34/2019, 198/2023, 159/2018, 240/2022, 179/2025) solo por resumen. Falta leer el texto completo del art. 5 inc. 2 c), del art. 14 (gratuidad) y la norma actual de medidas de seguridad. Falta confirmar si un cliente-comercio debe inscribirse (tensión art. 21 vs art. 24), si la seudonimización saca el dato del alcance de la ley, y si los topes de la Res. 244/2022 fueron actualizados después de 2022.
- Reforma: estado de expedientes (Rossi 3397-D-2026, Carro, Doñate, anteproyecto AAIP) sin verificar en fuente primaria; PDF del mensaje 2023 escaneado sin leer.
- Segunda fuente independiente: para la mayoría de afirmaciones legales la segunda fuente es el mismo texto en otro portal oficial o una página de la AAIP; no hubo fuente doctrinaria o jurídica independiente (estudio jurídico, manual universitario) leída. Un abogado debe revisar la nota antes de pasarla a vigente.
- No se consultaron: Ley 27.483 en su texto oficial; criterio de la AAIP sobre analítica web/cookies; dictámenes o sanciones efectivas aplicadas.
