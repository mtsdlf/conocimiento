# Investigación: Comercio exterior (agnóstico) y Cadena de suministro y logística en la Argentina

Fecha de la investigación: 2026-11-27.

## Aviso previo, leer primero

Este informe es **incompleto por una causa externa**. El presupuesto de búsquedas web de la sesión (200 llamadas compartidas por todos los agentes) estaba agotado cuando empecé: las cuatro búsquedas que intenté (Incoterms 2030, Malvina/SIM, SIRA y su reemplazo, courier) devolvieron «budget used up». Solo pude leer URLs directas (WebFetch), y varias fallaron (403/404). Por eso:

- **[L]**: lo leí en la fuente a través de WebFetch, que resume la página; las citas literales son de la página.
- **[N]**: conocimiento propio sin verificar en esta ronda, sin URL leída. Es hipótesis para verificar, no afirmación para la nota. Donde es ley o plata, el redactor no debe escribirlo sin una segunda ronda.
- Para **lo vigente en Argentina a noviembre de 2026 (sistema de la aduana, régimen de importación, courier) no hay nada verificado**. Está declarado como hueco.

Recomendación: repetir las búsquedas de la sección «Huecos» cuando el presupuesto se reponga (o subiendo `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`) antes de escribir la nota argentina.

---

## Componente 1. comercio-exterior (entrada)

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|
| OMA, Convenio de Kyoto revisado: https://www.wcoomd.org/en/topics/facilitation/instrument-and-tools/conventions/pf_revised_kyoto_conv.aspx | primaria | 3 | 2 | 1 | 3 | [L] |
| OMC, Acuerdo sobre Facilitación del Comercio: https://www.wto.org/english/docs_e/legal_e/tfa-nov14_e.htm | primaria | 3 | 3 | 1 | 3 | [L] parcial (100.000 de 118.808 caracteres) |
| UNCTAD, transporte y logística comercial: https://unctad.org/topic/transport-and-trade-logistics | primaria | 3 | ? | ? | 2 | no leída (403) |
| Chopra y Meindl; Ballou (actores y flujo) | secundaria canónica | 3 | 3 | 2 | 2 | [N] no abiertos |

### Afirmaciones con fuente

- El Convenio de Kyoto revisado «entered into force on February 3, 2006» y es «the blueprint for modern and efficient Customs procedures in the 21st century»; sus principios incluyen transparencia y previsibilidad, declaraciones simplificadas, uso máximo de tecnología de la información, gestión de riesgo y controles basados en auditoría, coordinación con otros organismos de frontera y asociación con el sector privado. [L] https://www.wcoomd.org/en/topics/facilitation/instrument-and-tools/conventions/pf_revised_kyoto_conv.aspx
- Acuerdo de Facilitación del Comercio, párr. 4.2 sobre gestión de riesgo: «Each Member shall design and apply risk management in a manner as to avoid arbitrary or unjustifiable discrimination.»; art. 10, párr. 4.1: «Members shall endeavour to establish or maintain a single window, enabling traders to submit documentation.»; el art. 7 incluye medidas para operadores autorizados: «Each Member shall provide additional trade facilitation measures related to import, export, or transit formalities.» [L] https://www.wto.org/english/docs_e/legal_e/tfa-nov14_e.htm. La lectura no dio la fecha de entrada en vigor (22/2/2017 es [N]) y su numeración del art. 7 difiere de la que recuerdo; verificar.

### Contenido propuesto [N], inferencia del redactor

- Actores: exportador, importador, agente de carga (freight forwarder), despachante o agente de aduana, transportista internacional (naviera, aerolínea, transporte terrestre), terminal, depósito fiscal, aduana, banco (cobranza o carta de crédito), aseguradora.
- Importación, orden típico: compra y Incoterm, reserva y embarque en origen, tránsito, arribo e ingreso a terminal o depósito fiscal, destinación y declaración, selectividad, verificación y liberación, pago de tributos (es de Impuestos), retiro y entrega.
- Exportación: contrato, documentos, entrega a la terminal, declaración, selectividad, embarque, documento de transporte, cobranza.
- Por qué pesa el stock en tránsito: plazos largos y variables (tránsito más aduana); la mercadería está comprometida o pagada y no se puede vender; el plazo de reposición largo e incierto pide más stock de seguridad. **Inferencia**: sin cifra de fuente; no poner días sin fuente.

### Qué registra un sistema [N]

- Operación de comercio exterior: tipo (importación o exportación), país, Incoterm, moneda, estado (planificada, embarcada, en tránsito, arribada, en aduana, liberada, entregada).
- Embarque y contenedor (número, tipo, precintos), documento de transporte, fechas estimadas y reales (ETD, ETA), costos prorrateados al ítem (landed cost).
- Evidencia en sistemas abiertos: no consultada (hueco).

### Recurso canónico

Convenio de Kyoto revisado (principios generales) para el marco; para el flujo, el capítulo de logística internacional de Ballou o de Chopra y Meindl [N, no abiertos].

---

## Componente 2. incoterms

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|
| ICC, página de Incoterms: https://iccwbo.org/business-solutions/incoterms-rules/ | primaria | 3 | 1 | 1 | 3 | [L] |
| ICC, texto de Incoterms 2020 (publicación de pago) | primaria | 3 | 3 | 3 | 3 | no accesible |

### Afirmaciones con fuente

- La ICC publicó las reglas por primera vez en 1936 y «Incoterms 2020 entered into force on 1 January 2020». Son «a set of eleven three-letter trade terms, reflecting business-to-business practice»; están «Recognised by UNCITRAL as the global standard for the interpretation of the most common terms in foreign trade»; «help to avoid costly misunderstandings by clarifying the tasks, costs and risks involved in the delivery of goods». [L] https://iccwbo.org/business-solutions/incoterms-rules/
- La página no lista las once reglas ni menciona una revisión «Incoterms 2030». Una URL de noticias que probé dio 404 y la búsqueda no se pudo hacer. **Hueco: no verifiqué si la ICC anunció una revisión.** La nota debe decir solo «la versión vigente es 2020, según la ICC, consultado el 2026-11-27».

### Contenido propuesto [N], de conocimiento sobre Incoterms 2020; verificar con el texto de la ICC o una segunda fuente

- Cualquier modo (7): EXW, FCA, CPT, CIP, DAP, DPU, DDP. Solo marítimo y fluvial (4): FAS, FOB, CFR, CIF.
- En 2020 DPU reemplazó a DAT (la descarga puede ser en cualquier lugar, no solo en terminal). CIP exige seguro amplio (cláusulas A del Institute Cargo Clauses) y CIF el mínimo (cláusulas C), con cobertura de al menos el 110 % del valor del contrato.
- En los grupos C (CPT, CIP, CFR, CIF) el vendedor paga el transporte principal pero el riesgo pasa en origen: el reparto de costos y el del riesgo no coinciden.
- No regulan: la transferencia de la propiedad, el pago, la ley aplicable ni las consecuencias del incumplimiento.
- Error común: FOB, CFR o CIF con contenedor, donde la mercadería se entrega a la terminal antes de cargarse al buque; corresponde FCA, CPT o CIP.

### Qué registra un sistema [N]

El Incoterm como dato de cabecera de la operación: código, lugar nombrado y versión del conjunto de reglas (p. ej. «FCA Rosario, Incoterms 2020»). Condiciona qué costos (flete, seguro, descarga) cargan a cada parte y desde qué hito el stock deja de ser propio o pasa a serlo.

### Recurso canónico

El texto de Incoterms 2020 de la ICC: la introducción y los artículos A4 a A9 y B4 a B9 de cada regla. Fijarse en el punto de entrega, la transferencia del riesgo, quién contrata transporte y seguro y quién despacha en exportación e importación.

---

## Componente 3. documentos-del-comercio-exterior

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|
| UNCITRAL, Ley Modelo sobre Documentos Transmisibles Electrónicos (MLETR): https://uncitral.un.org/en/texts/ecommerce/modellaw/electronic_transferable_records | primaria | 3 | 3 | 2 | 3 | no leída (403) |

### Afirmaciones

Ninguna con fuente leída. Todo [N]:

- Documentos: factura comercial, lista de empaque, documento de transporte (B/L marítimo, guía aérea AWB, carta de porte internacional CRT en el Mercosur, carta de porte ferroviaria), certificado de origen, póliza o certificado de seguro, certificados sanitarios y fitosanitarios.
- El B/L cumple tres funciones: recibo de la mercadería, prueba del contrato de transporte y título representativo de la mercadería (solo el «a la orden»; no el nominativo ni la sea waybill).
- La MLETR (UNCITRAL, 2017) da equivalencia funcional a los documentos transmisibles electrónicos; el Reino Unido sancionó una ley de documentos comerciales electrónicos en 2023. Años y países, a verificar.

### Qué registra un sistema [N]

Documento: tipo, número, emisor, fecha, partes (cargador, consignatario, notificado), vínculo a la operación y al embarque, estado (borrador, emitido, endosado, liberado, presentado en aduana); en los transmisibles, la cadena de endosos y el tenedor actual.

### Recurso canónico

El texto de la MLETR (equivalencia funcional y «control» en lugar de posesión) y la nota explicativa de UNCITRAL.

---

## Componente 4. aduana

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|
| OMA, qué es el SA: https://www.wcoomd.org/en/topics/nomenclature/overview/what-is-the-harmonized-system.aspx | primaria | 3 | 2 | 1 | 3 | [L] |
| OMA, Kyoto revisado (arriba) | primaria | 3 | 2 | 1 | 3 | [L] |
| OMC, valoración en aduana: https://www.wto.org/english/tratop_e/cusval_e/cusval_e.htm | primaria | 3 | 1 | 1 | 3 | [L] solo introducción (el texto del acuerdo: 403 y 404) |
| OMC, Facilitación del Comercio (arriba) | primaria | 3 | 3 | 1 | 3 | [L] parcial |

### Afirmaciones con fuente

- El SA es «a multipurpose international product nomenclature developed by the World Customs Organization (WCO)»; cada grupo tiene un código de seis dígitos; lo usan más de 200 países y economías; el Comité del SA lo actualiza cada 5 a 6 años aproximadamente. La página no nombra la edición vigente. [L] https://www.wcoomd.org/en/topics/nomenclature/overview/what-is-the-harmonized-system.aspx
- El acuerdo de valoración es el «Agreement on Implementation of Article VII of the General Agreement on Tariffs and Trade 1994» y «aims for a fair, uniform and neutral system for the valuation of goods for customs purposes». [L] https://www.wto.org/english/tratop_e/cusval_e/cusval_e.htm
- Gestión de riesgo, ventanilla única y operadores autorizados: ver componente 1.

### Contenido propuesto [N]

- Seis dígitos del SA; la NCM del Mercosur agrega dos (8); cada país puede agregar más. Edición vigente 2022; la siguiente (2028) a verificar.
- Valoración: el primer método es el valor de transacción (precio realmente pagado o por pagar, con ajustes) y hay seis métodos aplicados en orden. Sin impuestos.
- Canales de selectividad: verde (libera sin control), naranja (control documental), rojo (documental y físico), por gestión de riesgo; nombres y criterios los fija cada país.
- Operador económico autorizado (OEA, marco SAFE de la OMA): trato facilitado a cambio de cumplir criterios de seguridad y de cumplimiento. El enlace de la OMA que probé dio 404.

### Qué registra un sistema [N]

Declaración (destinación, régimen, partes, Incoterm, valor, moneda, país de origen), ítems con posición arancelaria, cantidad y peso, canal asignado, estados (oficializada, con canal, en verificación, liberada, anulada) y la trazabilidad del despacho al depósito.

### Recurso canónico

Convenio de Kyoto revisado, Anexo general (despacho y control basado en riesgo) y las Notas explicativas del SA (reglas generales de interpretación).

---

## Componente B. Cadena de suministro y logística en la Argentina (lo no fiscal)

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|
| InfoLeg, Código Aduanero, índice: https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/16536/texact.htm | primaria | 3 | 1 | 1 | 3 | [L] solo el índice |
| InfoLeg, Código Aduanero, auxiliares: https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/16536/Ley22415_S1_TituloII.htm | primaria | 3 | 2 | 1 | 3 | [L] parcial |
| ARCA, aduana: https://www.argentina.gob.ar/arca/aduana | primaria | 3 | 1 | 1 | 2 | [L] sin detalle |
| InfoLeg, Ley 24.653: https://servicios.infoleg.gob.ar/infolegInternet/anexos/65000-69999/65850/texact.htm | primaria | 3 | - | - | 3 | no leída: «No se pudo acceder al archivo solicitado» |
| Base, remito y COT: Inventario-y-depositos/inventario-y-depositos-en-argentina.md | interna | 2 | 2 | 2 | 1 | [L] |

### Afirmaciones con fuente

- Código Aduanero (Ley 22.415), índice: «Importadores y exportadores», arts. 91 a 108; «Destinaciones de importación», arts. 217 a 320; «Destinaciones de exportación», arts. 321 a 396; «Auxiliares del comercio y del servicio aduanero», arts. 36 a 90. [L] índice.
- Art. 36: «Son despachantes de aduana las personas de existencia visible que, en las condiciones previstas en este código»; art. 57: «Son agentes de transporte aduanero, a los efectos de este código, las personas de existencia visible o ideal». Las citas se cortan ahí en la lectura; el agente de transporte puede ser persona ideal (jurídica), el despachante solo persona física. [L] https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/16536/Ley22415_S1_TituloII.htm
- ARCA «controla los bienes que ingresan y egresan del país»; su página de aduana lista servicios (SITA, ISTA, SICNEA, Exporta Simple, «Envíos internacionales») sin detalle y no menciona Malvina, SIM ni selectividad. [L] https://www.argentina.gob.ar/arca/aduana
- Remito y COT: ya están en la base (el remito puede no imprimirse desde abril de 2025, RG 5678/2025; COT en la provincia de Buenos Aires y jurisdicciones adheridas). **No pude confirmar si cambió algo después de abril de 2025**; la nota existente cita una tabla de valores mínimos de COT de ARBA para 2026 como fuente secundaria. La nota nueva debe enlazar esa y no repetirla. [L] fuente interna.

### Sin verificar (hueco; lo que sigue no es afirmación)

- **Sistema informático de la aduana (SIM y «Malvina»)**: sin fuente. Mi recuerdo, [N]: «Malvina» es el nombre histórico del sistema informático de la aduana, de modo que no sé si el encargo supone un reemplazo real. No lo confirmo ni lo niego.
- **Régimen de importación vigente a noviembre de 2026**: sin fuente. Recuerdo [N] la secuencia DJAI (2012-2015), SIMI (2015-2022) y SIRA (2022-2023), con una apertura posterior a diciembre de 2023; no sé qué rige hoy. Pide dos fuentes (norma de ARCA o de la Secretaría de Comercio, más una secundaria fechada).
- **Courier y régimen simplificado**: sin fuente. No cito topes. Es plata: dos fuentes o decir que hay una.
- **Canales de selectividad en Argentina**: el índice del Código no usa la palabra «canal»; los fija la aduana por resolución. Sin fuente.
- **Ley 24.653 y RUTA (CNRT)**: ni la ley ni la página del RUTA se pudieron leer (404). Recuerdo [N] que la ley regula el transporte automotor de cargas de jurisdicción nacional, con tarifas libres y un registro, y que el RUTA es el registro de transportistas de la CNRT. Verificar.
- **CPE de granos**: existe una carta de porte electrónica para granos (ARCA) [N]; una línea, sin fuente leída.

### Qué registra un sistema (Argentina) [N], salvo remito y COT (fuente interna)

- Importador o exportador: CUIT, inscripción en el registro, estado.
- Despachante: matrícula o CUIT y mandato por operación.
- Declaración de aduana: número, destinación, canal, estado.
- Transportista de cargas: inscripción en el RUTA, vehículo, remito y COT cuando corresponde.

### Recurso canónico

El Código Aduanero en InfoLeg: Título II (despachantes y agentes de transporte), Sección III (destinaciones de importación) y Sección IV (exportación). Fijarse en quién puede gestionar ante la aduana y qué destinaciones existen. Para lo vigente: las páginas de ARCA y el Boletín Oficial.

---

## Huecos (declarados)

1. Noticias de una revisión «Incoterms 2030» (búsqueda no hecha).
2. Texto de las once reglas de Incoterms 2020 (el sitio de la ICC no las lista): hace falta una fuente que las desarrolle, más una segunda independiente.
3. Nombre y estado del sistema informático de la aduana argentina (SIM, Malvina, posible reemplazo).
4. Régimen de licencias o declaraciones de importación vigente a noviembre de 2026.
5. Courier: régimen simplificado y topes, con dos fuentes.
6. Selectividad en Argentina: canales y criterios.
7. Ley 24.653 (texto) y RUTA de la CNRT.
8. CPE de granos; cambios en remito y COT desde abril de 2025.
9. MLETR leída, leyes de documentos electrónicos y países que la adoptaron.
10. Texto del acuerdo de valoración, edición vigente y próxima del SA, compendio de OEA de la OMA, fecha de entrada en vigor del ATF.
11. Evidencia en sistemas abiertos (datos y estados de operación, embarque y declaración).
12. Plazos típicos de tránsito y despacho con cifra.

## Discrepancias con el árbol

- Ninguna respaldada por fuente. Observaciones del redactor:
  - Selectividad y OEA aparecen en `aduana` y en la nota argentina; la agnóstica los explica y la argentina solo dice cómo se llaman acá.
  - `documentos-del-comercio-exterior` y `aduana` comparten la factura comercial y el certificado de origen: el documento se define en la primera y su uso aduanero en la segunda.
- El encargo da por hecho un reemplazo del SIM («Malvina»); esta ronda no lo confirma. No cambiar el árbol por esa premisa.
