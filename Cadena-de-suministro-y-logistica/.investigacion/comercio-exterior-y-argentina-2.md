# Investigación (ronda 2): Incoterms, documentos y Argentina

Fecha: 2026-11-27. Complementa `comercio-exterior-y-argentina.md` (no editado).

## Aviso previo

El presupuesto de búsquedas web seguía agotado («budget used up», 1 intento). Trabajé solo con WebFetch directo, que resume la página con un modelo chico: las citas son de la página según ese resumen, no verificadas contra el original. Marcas: [L] leída por WebFetch; [S] resumen secundario; [N] conocimiento propio sin verificar. Muchas URLs que adiviné dieron 404/403/500 (listadas en Huecos). **Lo vigente en Argentina a 2026 (sistema de la aduana, importación, courier, selectividad, Ley 24.653, RUTA, CPE) sigue sin verificar.**

---

## Componente 2. incoterms

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|
| ICC, Incoterms 2020: https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/ | primaria | 3 | 1 | 1 | 3 | [L] (no desarrolla reglas, el texto es de pago) |
| ITA (Dpto. de Comercio de EE. UU.), Know Your Incoterms: https://www.trade.gov/know-your-incoterms | secundaria oficial, independiente de la ICC | 2 | 1 | 1 | 2 | [L] |
| Wikipedia, Incoterms: https://en.wikipedia.org/wiki/Incoterms | secundaria | 1 | 2 | 2 | 1 | [L]; error detectado (ver discrepancias) |

### Afirmaciones

- Grupos: «Of the 11 rules, there are seven for ANY mode(s) of transport and four for SEA or LAND or INLAND WATERWAY transport.» Cualquier modo: EXW, FCA, CPT, CIP, DAP, DPU, DDP. Marítimo y vías navegables: FAS, FOB, CFR, CIF. [L] https://www.trade.gov/know-your-incoterms (coincide, mismas listas: https://en.wikipedia.org/wiki/Incoterms)
- Cada regla fija «when the risk of loss or damage to the goods being exported pass from the seller to the buyer», quién contrata el transporte y quién el seguro. [L] https://www.trade.gov/know-your-incoterms
- No regulan: no «address all the conditions of a sale»; no identifican la mercadería ni el precio; no fijan método ni momento del pago; no determinan «when title, or ownership of the goods, passes»; no dicen qué documentos aporta el vendedor para el despacho en destino; no abordan «liability for the failure to provide the goods in conformity with the contract of sale». [L] https://www.trade.gov/know-your-incoterms
- Seguro: bajo CIF, las Institute Cargo Clauses (C) «remains the default level of coverage» (las partes pueden pactar más); bajo CIP la cobertura debe cumplir las Institute Cargo Clauses (A) o similares. [L] https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/ . El 110 % del valor: [S] https://en.wikipedia.org/wiki/Incoterms (no en la ICC leída); [N] además.
- DPU reemplaza a DAT; bajo DAP «the seller does not unload the goods». [L] https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/
- Incoterms 2020 vigente desde el 1/1/2020; reglas reconocidas por UNCITRAL. [L] https://iccwbo.org/business-solutions/incoterms-rules/ (ronda 1)
- **«Incoterms 2030»**: ni la página de la ICC ni Wikipedia lo mencionan (Wikipedia: «does not mention Incoterms 2030»). No hubo búsqueda. Decir solo «versión vigente: 2020».

### Tabla por regla (riesgo, transporte, seguro)

Fuentes: lo que sí dicen las páginas leídas está citado arriba y en la tabla de Wikipedia [S]; lo demás es [N] del texto de la ICC, **a confirmar con el texto de pago**.

| Regla | Riesgo pasa | Transporte principal | Seguro |
|---|---|---|---|
| EXW | en el local del vendedor o lugar nombrado [S]; «There is no obligation for the seller to make a contract of carriage» | comprador | comprador (sin obligación) |
| FCA | al entregar, ya despachada para exportar, en el lugar nombrado [S] | comprador | comprador |
| CPT | al entregar al primer transportista [S] | vendedor | comprador (sin obligación) |
| CIP | al entregar al primer transportista [S] | vendedor | vendedor, cláusulas (A), 110 % [S] |
| DAP | en el destino convenido, sin descargar [S] | vendedor | sin obligación de contratar; el riesgo es del vendedor [S] |
| DPU | en el destino, descargada [S] | vendedor | ídem |
| DDP | en el destino convenido [S]; vendedor además despacha la importación y paga derechos (eso es de Impuestos) | vendedor | ídem |
| FAS | al colocarla al costado del buque en el puerto de embarque [S] | comprador [N] | comprador |
| FOB | al cargarla a bordo [S] | comprador [S] | comprador |
| CFR | al cargarla a bordo en origen [S] | vendedor [S] | comprador |
| CIF | al cargarla a bordo en origen [N] | vendedor | vendedor, cláusulas (C) mínimo [L ICC] |

Punto clave [N, coincide con las fuentes de arriba]: en CPT, CIP, CFR y CIF (grupo C) el costo del flete lo paga el vendedor pero el riesgo ya pasó en origen.

### Qué registra un sistema

Igual que en ronda 1: Incoterm como dato de cabecera (código, lugar nombrado, versión). Evidencia en sistemas abiertos: no consultada.

### Recurso canónico

Texto de Incoterms 2020 de la ICC (de pago): introducción y artículos A y B de cada regla. Como lectura gratuita para el reparto: https://www.trade.gov/know-your-incoterms (la lista y las exclusiones), sabiendo que no detalla cada regla.

---

## Componente 3. documentos-del-comercio-exterior

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|
| UNCITRAL MLETR: https://uncitral.un.org/en/texts/ecommerce/modellaw/electronic_transferable_records | primaria | 3 | 3 | 2 | 3 | no leída (403, dos intentos) |
| Wikipedia, Bill of lading: https://en.wikipedia.org/wiki/Bill_of_lading | secundaria | 1 | 2 | 2 | 1 | [L] |
| Wikipedia, MLETR: https://en.wikipedia.org/wiki/UNCITRAL_Model_Law_on_Electronic_Transferable_Records | secundaria | 1 | 2 | 1 | 1 | [L] |

### Afirmaciones

- B/L, tres funciones: recibo («it is a conclusive receipt»), prueba o contenido del contrato («contains, or evidences» las condiciones del transporte) y título («it serves as a document of title to the goods», sujeto a la regla nemo dat). [L] https://en.wikipedia.org/wiki/Bill_of_lading **Una sola fuente, secundaria**; las funciones son doctrina estándar de derecho marítimo [N].
- El B/L nominativo («straight») entrega a una parte determinada; el «a la orden» se endosa y puede negociarse o darse en garantía. La sea waybill «gives the bearer the right to possession of the cargo, but does not confer title», por eso no hace falta presentar el original. [L] https://en.wikipedia.org/wiki/Bill_of_lading
- eBL: «the legal and functional equivalent of a paper bill of lading». [L] https://en.wikipedia.org/wiki/Bill_of_lading
- MLETR: adoptada por UNCITRAL en 2017; permite usar documentos transmisibles en forma electrónica; arts. 8 y 9 (escritura y firma), art. 10 (condiciones de equivalencia: método fiable para identificar el registro, mantenerlo bajo control y preservar su integridad), art. 11 (posesión: «a reliable method to establish exclusive control»); «control» y singularidad son el núcleo. [L] https://en.wikipedia.org/wiki/UNCITRAL_Model_Law_on_Electronic_Transferable_Records
- Jurisdicciones que la adoptaron (según Wikipedia, con años y fiabilidad dispares): Bahrein (2018), Singapur (2021, año de promulgación no confirmado), Belice (2021), Kiribati (2021), Papúa Nueva Guinea (2021), Paraguay (Ley 6.822, 2 de enero de 2022), Timor-Leste (Decreto-Ley 12/2024), Reino Unido (Electronic Trade Documents Act, vigente el 20 de septiembre de 2023), Abu Dabi (ADGM). Francia: proyecto adoptado, marzo de 2024. [L] mismo enlace. Reino Unido «enacted in July 2023»: https://en.wikipedia.org/wiki/Bill_of_lading . El texto de la propia UNCITRAL lista el estado oficial: no leído.
- AWB, CRT, MIC/DTA: **sin fuente**. [N]: la guía aérea (AWB) no es título de propiedad, solo recibo y prueba del contrato; CRT es la carta de porte internacional por carretera del Acuerdo de Transporte Internacional Terrestre (ATIT) del Mercosur; MIC/DTA es el manifiesto internacional de carga con declaración de tránsito aduanero. Todo [N].

### Qué registra un sistema

Como ronda 1. Añadir, para el eBL: «control» (quién lo tiene hoy), singularidad (un solo original activo) e integridad (historial de transferencias); esos son los conceptos de la MLETR [L secundaria].

### Recurso canónico

Texto de la MLETR en uncitral.un.org (arts. 8 a 11) más su nota explicativa. Me fue imposible leerlo (403).

---

## Componente B. Argentina

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|
| InfoLeg, Cód. Aduanero Título II: https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/16536/Ley22415_S1_TituloII.htm | primaria | 3 | 3 | 1 | 3 | [L] |
| InfoLeg, Título III: https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/16536/Ley22415_S1_TituloIII.htm | primaria | 3 | 3 | 1 | 3 | [L] |
| InfoLeg, destinaciones de importación: https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/16536/Ley22415_S3_TituloII.htm | primaria | 3 | 3 | 1 | 3 | [L] |
| ARCA, envíos internacionales: https://www.afip.gob.ar/envios-internacionales | primaria | 3 | 1 | 1 | 2 | [L] sin cifras |

Las tres páginas de InfoLeg son el mismo texto consolidado (una sola fuente). Para ley, el requisito de dos fuentes independientes **no se cumple**: hay una (InfoLeg).

### Afirmaciones

- Art. 36: «Son despachantes de aduana las personas de existencia visible que, en las condiciones previstas en este código» «realizan en nombre de otros ante el servicio aduanero trámites y diligencias» «relativos a la importación, la exportación y demás operaciones aduaneras.» [L] Título II
- Art. 37: las personas humanas o jurídicas «podrán gestionar el despacho y la destinación de mercadería, por sí o a través de persona autorizada», con excepción de las funciones propias de los agentes de transporte aduanero y de capitanes, comandantes o conductores. [L] Título II. (Hay una interpretación [N]: gestionar por sí mismo es lícito; el despachante no es obligatorio. El texto leído sustenta esto.)
- Art. 57: «Son agentes de transporte aduanero, a los efectos de este código, las personas de existencia visible o ideal que, en representación de los transportistas, tienen a su cargo las gestiones relacionadas con la presentación del medio transportador y de sus cargas ante el servicio aduanero». Art. 58: deben estar inscriptos «en el Registro de Agentes de Transporte Aduanero, con la indicación de la vía o vías de transporte correspondientes». [L] Título II
- Art. 91: «Son importadores las personas que en su nombre importan mercadería, ya sea que la trajeren consigo o que un tercero la trajere para ellos»; ídem exportadores. Art. 92: «Todas las personas humanas y jurídicas podrán solicitar destinaciones aduaneras y realizar operaciones de comercio exterior sin necesidad de inscribirse en ningún registro.» Art. 93 «derogado por art. 106 del Decreto N° 70/2023 B.O. 21/12/2023». [L] Título III. **Cambio respecto de lo que se sabía:** ya no hay registro obligatorio de importadores y exportadores (el art. 93 era el que lo exigía [N]); el texto consolidado que leí refleja el DNU 70/2023. Verificar que siga vigente en 2026 (el DNU tuvo litigios [N]).
- Art. 233: «La destinación de importación para consumo es aquella en virtud de la cual la mercadería importada puede permanecer por tiempo indeterminado dentro del territorio aduanero.» (art. 233 a partir del Capítulo Segundo, «definitiva».) [L] Título II, Sección III
- Art. 250: «La destinación de importación temporaria es aquella en virtud de la cual la mercadería importada puede permanecer con una finalidad y por un plazo determinado dentro del territorio aduanero, quedando sometida, desde el mismo momento de su libramiento, a la obligación de reexportarla para consumo con anterioridad al vencimiento del mencionado plazo.» Art. 251: puede quedar en el mismo estado o transformarse, repararse o perfeccionarse (base del perfeccionamiento activo). [L]
- Art. 217: el importador solicita la destinación; puede hacerlo anticipadamente hasta la llegada del medio transportador (despacho directo a plaza) o dentro de los 15 días desde que llega. [L, resumen del modelo; dato de plazo: tomar con cautela, el texto exacto del artículo no se citó]
- ARCA, envíos: la página nombra los regímenes Courier («Envíos que ingresen o egresen a través de prestadores PSP/COURIER»), Régimen General («Envíos que no encuadran en un régimen especial de importación»), envíos postales por Correo Argentino para uso personal, y exportación postal. No da topes ni norma. [L] https://www.afip.gob.ar/envios-internacionales

### Qué registra un sistema (Argentina)

Complementa ronda 1: la destinación (consumo o temporaria, con su plazo y la obligación de reexportar), el agente de transporte aduanero con su vía (marítima, aérea, terrestre) y la figura de quien gestiona (el propio titular o un despachante).

### Recurso canónico

Código Aduanero en InfoLeg: arts. 36 a 37 (quién gestiona), 57 a 58 (agente de transporte), 91 a 92 (importadores), 233 y 250 (las dos destinaciones). Complementar con el Boletín Oficial para lo vigente tras el DNU 70/2023.

---

## Huecos

1. Incoterms: no hay fuente gratuita que desarrolle la regla por regla; los puntos de riesgo de la tabla son de Wikipedia [S] y [N]. No hay segunda fuente independiente sobre el 110 % del seguro ni un anuncio sobre Incoterms 2030 (búsqueda imposible).
2. MLETR desde UNCITRAL (403): el estado de adopciones oficial queda sin leer. Sin fuente en AWB, CRT, MIC/DTA, ATIT.
3. Sistema informático de la aduana (SIM, Malvina): páginas probadas dieron 404 (afip.gob.ar/sim, es.wikipedia). Sin dato.
4. Canales de selectividad: ARCA no los menciona en su página principal de aduana; página sugerida dio 404. Sin dato.
5. Importación vigente (SIRA a SEDI y lo de 2026): sin fuente.
6. Courier: sin topes, ni norma. La página de ARCA (envios-internacionales) enlaza la normativa en su sección «Ayuda», no leída. Es plata: dos fuentes pendientes.
7. Ley 24.653 y RUTA: InfoLeg devolvió «No se pudo acceder al archivo solicitado» (IDs 65850 y 46481), argentina.gob.ar/normativa 404, página de CNRT 404.
8. CPE de granos, cambios de remito y COT desde abril de 2025: sin dato.
9. Del art. 217 conviene leer el texto completo; el resumen del modelo dio el plazo de 15 días sin cita literal.
10. Vigencia del DNU 70/2023 en 2026 (afecta arts. 92 y 93).

## Discrepancias

- **Seguro en CIF**: la ICC dice que la Cláusula (C) «remains the default level of coverage»; Wikipedia, según el resumen, dice (A) también para CIF. Manda la ICC (Aut 3 contra 1). Probable error del resumen o de Wikipedia; no copiar de Wikipedia.
- Ronda 1 recordaba [N] que existía un registro de importadores y exportadores; el texto consolidado actual lo contradice (art. 92 sin registro; art. 93 derogado). Manda el texto de InfoLeg.
- Ronda 1 proponía que solo el despachante sea persona física: coincide con el art. 36 (existencia visible), y el art. 57 admite persona ideal para el agente de transporte.

## Árbol

- Sin cambio respaldado por fuente. Observación: la nota argentina debería decir, con el art. 37, que se puede gestionar el despacho por sí o por persona autorizada, y no presentar al despachante como obligatorio.
