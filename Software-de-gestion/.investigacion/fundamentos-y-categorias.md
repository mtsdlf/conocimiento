# Fundamentos y categorías de producto: investigación cruda

Ángulo: `Fundamentos/` (historia, definiciones, mitos, bibliografía) y `Categorias-de-producto/` (administrativo/operativo, suite/best-of-breed, escalones, una sección por categoría). Fecha de todas las lecturas: 2026-11-27. Parte de `taxonomias-externas-96.md` (en este mismo directorio) y no repite lo que ya dice (APQC, Odoo, ERPNext, los cuadrantes de Gartner por categoría con sus fechas, SCOR/CSCP/CLTD, ISA-95 nivel 3 y 4).

Marcas: [L] texto completo de la fuente o de la página; [M] solo metadatos o abstract; [S] resumen del buscador o de un tercero. Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Tipo: P primaria, S secundaria.

Aviso de método: la mayoría de las fuentes canónicas de este ángulo están detrás de un muro o en revistas de pago. Gartner (glosario, notas de prensa, reviews, documentos) devolvió 403 en todos los intentos; Wiley (Jacobs y Weston), Emerald (Light et al.), ISO y la copia de Davenport en una universidad portuguesa pidieron login o devolvieron 403. Lo que sigue distingue lo leído de lo citado por terceros. Ningún abstract de revista salió de la editorial salvo donde se marca.

---

## 0. En corto

1. **Las definiciones de ERP no convergen, y eso es el hallazgo de fondo**: el trabajo más citado sobre el tema (Klaus, Rosemann y Gable 2000) concluye que «it is unlikely that at this stage a broadly agreed definition of ERP can be achieved». La nota de fundamentos puede apoyar en eso su política de definición (ERP como «forma de empaquetar», decisión #95).
2. **Historia**: MRP (Orlicky, libro de 1975; primer uso comercial en Black & Decker en 1964 según Wikipedia) → MRP II (Wight, 1983) → «ERP» (Gartner, comienzos de los 90; fecha exacta no verificada en primaria) → Y2K como motor de reemplazo → ERP II (Gartner 2000) → postmodern ERP (Gartner 2013-2014) → composable ERP (Gartner, años 2020). La primaria de cada hito (Gartner) está tras muro: todo el tramo Gartner va [S].
3. **Mito del «70 % fracasa»**: no es una tasa medida. La versión actual es una predicción/afirmación de Gartner (más del 70 % de las iniciativas de ERP «recientes» no cumplirán del todo sus objetivos; 25 % fracasan catastróficamente), reportada por The Register en noviembre de 2025 sin nombrar el estudio. Los números viejos (80 %, 75 %) se repiten sin fuente. Los estudios con muestra (Panorama 2010, 1.600 organizaciones) miden otra cosa: retrasos, sobrecostos y beneficios. Standish: no se pudo confirmar ninguna cifra de ERP.
4. **Suite frente a best-of-breed** tiene literatura académica propia (Light, Holland y Wills 2001; ECIS 2000) y una posición de analista (postmodern ERP). Es un debate de 25 años, no una novedad de la nube.
5. **Cada categoría tiene un cuerpo distinto de fuente**: MES y QMS tienen norma (ISA-95/IEC 62264; ISO 9001), EAM tiene norma (ISO 55000), el resto se define por analistas (Gartner, tras muro) y por libros de texto. Se declara dónde no hay primaria.
6. **Sobre la división del árbol**: coincide con cómo el campo parte esta vertical salvo cuatro matices (sección 12).

---

## 1. Fuentes del ángulo (tabla maestra)

| # | Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|---|
| F1 | Klaus, Rosemann y Gable (2000), «What is ERP?», *Information Systems Frontiers* 2(2):141-162 | P | [M] abstract vía RePEc; texto no leído | 3/3/2/3 | https://ideas.repec.org/a/spr/infosf/v2y2000i2d10.1023_a1026543906354.html · DOI https://doi.org/10.1023/A:1026543906354 |
| F2 | Jacobs y Weston (2007), «Enterprise resource planning (ERP)—A brief history», *J. of Operations Management* 25(2):357-363 | P | [M] solo cita y keywords; Wiley dio 403 | 3/3/2/3 | https://doi.org/10.1016/j.jom.2006.11.005 (redirige a Wiley) |
| F3 | Davenport (1998), «Putting the Enterprise into the Enterprise System», *HBR* 76(4):121-131 | P | [M] solo cita y resumen del buscador | 3/3/3/3 | copia con login: https://fenix.iseg.ulisboa.pt/downloadFile/281608120778205/HBR_1998_Davenport_ES.pdf (no leída) |
| F4 | Light, Holland y Wills (2001), «ERP and best of breed: a comparative analysis», *Business Process Management J.* 7(3):216-224 | P | [M] solo cita; Emerald redirigió | 3/2/2/3 | https://doi.org/10.1108/14637150110392683 · repositorio https://salford-repository.worktribe.com/output/1448144/erp-and-best-of-breed-a-comparative-analysis (403) |
| F5 | Light, Holland, Kelly y Willis (2000), «Best of Breed IT Strategy: An Alternative to ERP Systems», ECIS 2000 | P | [M] abstract leído en AIS | 2/2/2/3 | https://aisel.aisnet.org/ecis2000/180 |
| F6 | Mabert, Soni y Venkataramanan (2003), «ERP: Managing the implementation process», *EJOR* 146(2):302-314; y su «The impact of organization size on ERP implementations in the U.S. manufacturing sector», *Omega* 31:235-246 | P | [M] solo citas | 3/2/2/3 | https://ideas.repec.org/a/eee/ejores/v146y2003i2p302-314.html |
| F7 | Gartner, nota de prensa 2014-01-29 «by 2016 the impact of cloud and emergence of postmodern ERP will relegate highly customized ERP systems to legacy status» | P | [S] título confirmado; 403 | 3/1/1/3 | https://www.gartner.com/en/newsroom/press-releases/2014-01-29-gartner-says-by-2016-the-impact-of-cloud-and-emergence-of-postmodern-erp-will-relegate-highly-customized-erp-systems-to-legacy-status |
| F8 | TechTarget, «Postmodern ERP countered by continued appeal of single suite» (cita a Denise Ganly, Gartner) | S | [L] | 2/2/2/2 | https://www.techtarget.com/enterprise-software/feature/Postmodern-ERP-countered-by-continued-appeal-of-single-suite |
| F9 | Gartner, glosario «Enterprise Resource Planning (ERP)» | P | [S] 403; solo extracto del buscador | 3/1/1/3 | https://www.gartner.com/en/information-technology/glossary/enterprise-resource-planning-erp |
| F10 | Wikipedia, «Enterprise resource planning» (historia: MRP→ERP, Y2K, ERP II, nube, postmodern) | S | [L] 100.000 de 119.000 caracteres | 1/2/2/1 | https://en.wikipedia.org/wiki/Enterprise_resource_planning |
| F11 | Wikipedia, «Material requirements planning» (Orlicky, Wight, adopción) | S | [L] | 1/2/2/1 | https://en.wikipedia.org/wiki/Material_requirements_planning |
| F12 | Bond et al. (2000), «ERP Is Dead—Long Live ERP II», GartnerGroup | P | [S] solo catálogo | 3/1/1/3 | https://bibsonomy.org/bibtex/10a564a8b9b226a7f96ea0e6148f4c3e6/stefan.strecker ; contexto https://accountancyage.com/2000/11/19/gartner-predictions-erp-ii-is-served/?amp=1 |
| F13 | The Register (2025-11-13), «ERP carnage continues as orgs jump in unprepared» | S | [L] | 2/2/2/2 | https://www.theregister.com/2025/11/13/erp_disaster_gartner/ |
| F14 | Panorama Consulting (2013-05-08), «What constitutes an ERP failure» | S, con interés comercial | [L] | 1/2/2/2 | https://panorama-consulting.com/what-constitutes-an-erp-failure |
| F15 | Computerworld (2010-03-17), sobre el estudio de Panorama de 2010 | S (de una consultora) | [L] | 1/2/3/2 | https://www.computerworld.com/article/1516480/widespread-discontent-persists-with-erp-projects.html |
| F16 | ISA, página «ISA-95 Standard» | P (del organismo, no la norma) | [L] | 3/2/1/3 | https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard |
| F17 | Siemens, «ISA-95 framework layers» | S, vendor | [L] | 1/2/2/1 | https://www.siemens.com/en-gb/technology/isa-95-framework-layers/ |
| F18 | Wikipedia, «Customer relationship management» | S | [L] 100.000 de 132.000 caracteres | 1/2/2/1 | https://en.wikipedia.org/wiki/Customer_relationship_management |
| F19 | Wikipedia, «Field service management» | S | [L] | 1/1/2/1 | https://en.wikipedia.org/wiki/Field_service_management |
| F20 | Wikipedia, «Professional services automation» (cita a Melik y Melik 2002, Wiley) | S | [L] | 1/1/1/1 | https://en.wikipedia.org/wiki/Professional_services_automation |
| F21 | Wikipedia, «Human capital management» | S | [L] parcial | 1/1/1/1 | https://en.wikipedia.org/wiki/Human_capital_management |
| F22 | Resultados del buscador sobre MES: glosario de Gartner («MES manufacturing execution system») y Market Guide 2016 | P | [S] | 3/1/1/3 | https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/mes-manufacturing-execution-system (redirige a la home; no leída) |
| F23 | Gartner, Market Guide for Professional Services Automation Platforms (2025-10-15) | P | [S] | 3/1/1/3 | https://www.gartner.com/en/documents/7070798 (no leída) |
| F24 | Gartner Research Report G00122453 (IBM lo aloja; 2004; «EAM evolucionó de los sistemas de mantenimiento computarizados») | P | [S] | 2/1/1/2 | https://public.dhe.ibm.com/software/emea/de/tivoli/Gartner-Research-Report_G00122453.pdf (no leída) |
| F25 | Gartner, glosario «Supply Chain Execution (SCE)»: agrupa WMS y TMS | P | [S] | 3/1/1/3 | https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/supply-chain-execution-sce (no leída) |

Cinco textos que parafrasean un mismo documento cuentan como una sola fuente: las citas de Gartner en TechTarget, NetSuite, SAP, CIO.com y blogs de consultoras que se encontraron para postmodern/composable ERP dependen de las mismas notas de Gartner y se cuentan como una (F7/F9), más la voz propia de Ganly en F8.

---

## 2. Fundamentos: de dónde viene

### 2.1 Cronología con fuente

| Hito | Qué se afirma | Fuente | Marca |
|---|---|---|---|
| MRP | Joseph Orlicky lo desarrolló en 1964 «en respuesta al Toyota Manufacturing Program»; Black \& Decker aparece como primer usuario en 1964 (líder de proyecto Dick Alban). Rolls-Royce y General Electric lo computarizaron a comienzos de los 50 sin comercializarlo. | F11 (Wikipedia; sus referencias son Karmarkar *HBR* 1989, Gray *Computerworld* 1986, Orlicky 1975 McGraw-Hill) | [L] secundaria |
| Difusión de MRP | Unas 700 empresas lo habían implantado en 1975 y unas 8.000 en 1981. | F11 | [L] secundaria |
| Libro canónico | Orlicky (1975), *Material Requirements Planning*, McGraw-Hill: «first completely detailed description of MRP logic» según un resultado del buscador. | https://www.oreilly.com/library/view/accounting-information-systems/9781118162309/c15-2.html (resultado del buscador; no abierto) | [S] |
| MRP II | Oliver Wight (1983) lo desarrolla a partir de MRP; hacia 1989 un tercio de la industria del software era MRP II, 1.200 millones de dólares. | F11 | [L] secundaria |
| Discrepancia de fechas del MRP | Otro texto lo ubica en los 60 con IBM y J.I. Case, y otro en fines de los 50. Se dan ambas. | resultados del buscador, sin abrir | [S] |
| «ERP» | «Gartner is credited with first using the acronym ERP in the 1990s»; extiende MRP y MRP II a «a larger whole that reflected the evolution of application integration beyond manufacturing». Otros textos dicen «1990». | F10 | [L] secundaria |
| Años 90 | Los primeros proveedores armaron paquetes en torno a finanzas, mantenimiento y personal, no solo manufactura; a mediados de los 90 cubría todas las funciones centrales. | F10 | [L] secundaria |
| Y2K | «The year 2000 problem led many companies to replace old systems with ERP.» | F10 | [L] secundaria |
| ERP II | Gartner 2000, «ERP Is Dead—Long Live ERP II» (Bond, Genovese, Miklovic, Wood, Zrimsek, Rayner). Definición citada: «business strategy plus industry-specific applications that increase customer and shareholder value by optimising enterprise and inter-enterprise collaborative processes». Tiene dos supuestos de planificación: 80 % de probabilidad de que en 2005 ERP II fuera el habilitador principal de la eficiencia dentro y entre empresas, 20 % de que fallara y fuera desplazado. | F12 y https://www.taylorfrancis.com/books/9781315094373/chapters/10.4324/9781315094373-4 | [S] |
| Nube | Primeros productos puros en la nube desde 1999 (NetLedger); adopción rápida a comienzos de los 2010. | F10 | [L] secundaria |
| Postmodern ERP | «Gartner recognized the shift in 2013». Reemplazar la megasuite de un solo proveedor por un ERP «más federado y débilmente acoplado», con «the best applications, likely from two or more vendors, in each business area». Analista: Denise Ganly. Gartner esperaba que una estrategia «governed, business-led postmodern ERP» pasara de cerca del 15 % de las empresas a más del 40 % hacia 2020. Cita textual de Ganly: «Largely speaking, finance is finance, and general ledger is general ledger» (no personalizar). | F8 | [L] secundaria (cita a Gartner) |
| Postmodern, fecha | Los textos discrepan entre 2013 (concepto) y 2014 (nota de prensa «Predicts 2014» del 29-01-2014: «by 2016 ... will relegate highly customized ERP systems to legacy status»). Se dan las dos. | F7, F8 | [S] / [L] |
| Composable ERP | Gartner, años 2020. Definiciones atribuidas, sin la primaria: «a technology strategy that automates and links administrative and operational business capabilities» (ya citada en el informe #96) y «adaptive technology strategy that enables foundational, administrative, and operational digital capabilities»; arquitectura de bloques modulares unidos por APIs y un data fabric (atribuido a Gartner por CIO.com). El glosario de Gartner dice que «also advocates a composable approach when consolidating ERP projects». Hay un documento «Navigate 10 Ugly Truths of Composable ERP». | https://www.techtarget.com/enterprise-software/feature/Composable-ERP-strategy-Key-benefits-and-steps-for-success · https://www.gartner.com/en/documents/5494395 · https://www.gartner.com/en/documents/6206787 | [S] |

**Lo que se necesita y no se leyó**: el texto de Jacobs y Weston (F2), que es la historia escrita desde el campo de las operaciones y el recurso canónico para todo este cuadro. El resumen del buscador solo confirmó cita, DOI y palabras clave («ERP, functional enterprise, industry, data integration»). Hay que abrirlo con acceso institucional antes de escribir `historia-del-software-de-gestion.md`: el cuadro de arriba tiene fuentes secundarias para todo lo que va antes de 2000.

### 2.2 Definiciones canónicas

| Definición | Fuente | Marca |
|---|---|---|
| Klaus, Rosemann y Gable 2000: con análisis histórico, un metaanálisis de la literatura de sistemas de información y una encuesta a expertos académicos «we reveal dissenting views on the phenomenon»; concluyen que «it is unlikely that at this stage a broadly agreed definition of ERP can be achieved». Buscan mejorar la comunicación entre investigadores, practicantes, clientes, consultores y proveedores. | F1 | [M] abstract leído en RePEc |
| Davenport 1998: un sistema empresarial es «a central database that collects data from and feeds data into modular applications supporting virtually all of a company's business activities» (paráfrasis del buscador, no cita verificada); tesis: los problemas grandes son de negocio, no técnicos; instalarlo sin entender las implicancias de negocio arriesga perder la integración prometida. | F3 | [S] |
| Gartner: ERP son aplicaciones que automatizan y soportan varios procesos administrativos y operativos (línea de negocio, atención al cliente, administración y activos). Texto exacto no verificado. Gartner: ERP «is neither defined as a single integrated suite, nor is it a specific set of modules» (ya en #96). | F9 y NetSuite https://www.netsuite.com/portal/resource/articles/erp/how-does-netsuite-fit-gartners-definition-of-postmodern-erp.shtml | [S] |
| Wikipedia: módulos comunes: contabilidad financiera y de gestión, personal, manufactura, procesamiento de pedidos, SCM, proyectos, CRM, SRM, contratos. | F10 | [L] |

Para la nota: las cuatro definiciones se pisan en un núcleo (aplicaciones modulares sobre una base común de datos) y discrepan en el borde (si incluye CRM/SRM, si exige un proveedor único). Eso es lo que Klaus et al. midieron y es lo que el árbol resuelve al no tratar a ERP como saber.

### 2.3 Mitos con evidencia

**M1. «El 70 % de los ERP fracasan.»**

- **Gartner 2024-2025**: la cifra actual es de Gartner. Su resumen de 2024 dice que para 2027 más del 70 % de las iniciativas de ERP implantadas hace poco no cumplirán del todo sus objetivos originales de negocio (resultado del buscador, el abstract completo dio 403). [S] https://www.gartner.com/en/documents/6908366. En el Symposium de Barcelona, Dixie John (senior director de estrategia de ERP en Gartner) dijo que el 70 % de las iniciativas de ERP «fail to fully meet their original business use case goals» y que el 25 % fracasan catastróficamente; el artículo no nombra el estudio de donde salen. [L] F13. Dos observaciones: es una afirmación sobre «cumplir del todo los objetivos», no sobre proyectos abandonados, y es un pronóstico, no una tasa medida.
- **Panorama 2013**: «It's often been said that 80% or more of ERP implementations are considered failures»; lo presenta como cosa que se dice, sin fuente, y afirma que «there is no clear definition of what constitutes ERP failure». Su propia cifra: 41 % de unas 200 implantaciones estudiadas tuvo alguna disrupción operativa en la puesta en marcha. Tres posiciones sobre qué es fracaso: sobrecostos y retrasos son síntomas de expectativas irreales; mala gestión del proyecto y del cambio es fracaso de quien implanta; no obtener los beneficios es el fracaso más claro. Interés comercial: la consultora vende informes, webinar e implantación, y el artículo los promociona. [L] F14.
- **Panorama 2010** (1.600 organizaciones; es el estudio con muestra más citado): más de la mitad obtuvo 30 % o menos de los beneficios esperados; 51,4 % se pasó de presupuesto, 40 % cumplió, 8,6 % gastó menos; más del 35 % tardó más de lo previsto, 21,5 % terminó antes y 43 % a tiempo; 72 % dijo estar «fairly satisfied» con el paquete. [L] F15. Nota que las cifras son autoinformadas, de una consultora, y que lo que mide es presupuesto, plazo y beneficios percibidos, no «fracaso».
- **Standish Group**: se buscó una cifra de ERP atribuida a Standish y no se encontró ninguna verificable; un texto secundario atribuye vagamente sobrecostos y plazos a Standish sin número. Se declara hueco.
- **Otras cifras que circulan** («más del 75 %», «entre 55 % y 75 %» sin fuente): no se pudieron rastrear a ningún documento. Se tratan como folklore.
- **Para la posición contraria** (la que pidió el brief): lo que sostiene que el mito está inflado es (a) que la cifra nueva es una predicción de un analista con estrategia de ventas de asesoría, (b) la ausencia de una definición común de fracaso (Panorama, F14, y Klaus et al. para la de ERP, F1), y (c) que el único estudio con muestra grande (F15) muestra 72 % de satisfacción y 43 % de proyectos a tiempo. Falta una fuente académica con método sobre tasa de fracaso (p. ej. un metaanálisis tipo Momoh, Roy y Shehab 2010 «Challenges in ERP implementation: state-of-the-art», *BPMJ* 16(4):537-565, https://doi.org/10.1108/14637151011065919, que solo se vio citado en F10 [S]).

**M2. «ERP es una suite de un solo proveedor con módulos fijos.»** Lo desmienten la propia definición de Gartner (arriba), el debate best-of-breed desde 2000 (F4, F5) y el postmodern ERP (F8). No es mito de evidencia mala sino de definición vieja.

**M3. «ERP es para empresas grandes.»** Mabert, Soni y Venkataramanan estudiaron específicamente el efecto del tamaño en implantaciones de manufactura (*Omega* 31:235-246, 2003) [M]; no se leyó. Los paquetes para pyme existen desde mediados de los 90 por la difusión que describe F10. Queda como pista a verificar con F6.

**M4. «El CRM es software.»** Gartner, según un resultado del buscador, lo define como estrategia de negocio («a business strategy that optimizes revenue and profitability while promoting customer satisfaction and loyalty»; versión vieja sin «loyalty»), y un analista dijo: «when people are now talking about CRM, they are talking about the technology». Es un mito de lenguaje que conviene dejar en el glosario. [S] vía https://www.smartsheet.com/content-center/best-practices/project-management/project-management-guide/professional-services-project-management y https://community.pega.com/sites/default/files/crm-industry-glossary/content/crm-glossary/c/customer_relationship_management.htm (ambos de terceros).

**M5. «Fracaso de CRM del 50-70 %.»** Wikipedia (F18) trae: informe de Gartner de 2003 estimando más de 2.000 millones de dólares gastados en software que no se usaba; CSO Insights: menos del 40 % de 1.275 empresas tenía adopción de usuarios por encima del 90 %; encuesta del Reino Unido de 2007: 43 % usaba menos de la mitad de la funcionalidad. [L] secundaria, las tres cifras con la fuente original sin abrir.

### 2.4 Bibliografía comentada propuesta (para `fuentes-de-software-de-gestion.md`)

Con tres escuelas o posiciones visibles en la literatura: la **de la definición** (qué es ERP: F1), la **de la implantación** (Davenport F3; Markus y Tanis, Soh et al. y Brehm et al. son del ángulo de implementación) y la **del modelo de producto** (suite o piezas: F4, F5, y F8 desde la industria).

| Obra | Qué aporta | Estado |
|---|---|---|
| Orlicky (1975), *Material Requirements Planning*, McGraw-Hill | La lógica de MRP, el origen del ERP de manufactura. | No leída; citada en F11 |
| Jacobs y Weston (2007), *J. Oper. Manag.* | Historia del campo, escrita por gente de operaciones. | [M]; hay que leerla |
| Klaus, Rosemann y Gable (2000) | Mapa de definiciones y diagnóstico de que no hay consenso. | [M] |
| Davenport (1998), *HBR* | La tesis de que el sistema impone una lógica de negocio. | [S] |
| Light, Holland y Wills (2001); Light et al. (2000) | El debate suite frente a piezas, con caso. | [M] |
| Mabert, Soni y Venkataramanan (2003), dos artículos | Implantación en manufactura y efecto del tamaño. | [M] |
| Shanks y Willcocks (2003), *Second-Wave ERP Systems*, Cambridge UP; O'Leary (2000), *ERP Systems*, Cambridge UP; Kumar y van Hillegersberg (2000), «ERP: introduction», *CACM* 43(4):22-26, https://doi.org/10.1145/332051.332063; Scheer y Habermann (2000), «Making ERP a success», *CACM* 43(4):57-61, https://doi.org/10.1145/332051.332073 | Libros y números especiales que Wikipedia usa como referencias; no se leyeron. | [S] vía F10 |
| Møller (2005), «ERP II: a conceptual framework for next-generation enterprise systems?», *J. Enterprise Information Management*, https://dx.doi.org/10.1108/17410390510609626 | Crítica académica a ERP II. | [S] apareció en resultados, sin abrir |
| Monk y Wagner, *Concepts in Enterprise Resource Planning* | Libro de texto nombrado por el brief. | No buscado en esta pasada |

---

## 3. Categorías: administrativo frente a operativo

- **Qué dice el campo**: Gartner reparte la funcionalidad del ERP en «administrative» (finanzas, personal, compras) y «operational» (producción, distribución). Un resultado del buscador de Software Advice dice que casi todas las aplicaciones de ERP se dividen en una u otra categoría, sin definir los términos. [S] https://www.softwareadvice.com/resources/postmodern-erp-defined/. La definición de composable ERP también las nombra juntas («administrative and operational business capabilities»). La primaria de Gartner no se pudo leer; el informe #96 ya dejó la misma marca.
- **Qué hace operativo a algo**: según la partición de Gartner en dos cuadrantes (producto frente a servicios) citada en #96, lo operativo es lo que depende del tipo de negocio (manufactura, distribución, cadena en las empresas de producto; proyectos y recursos en las de servicios), mientras que lo administrativo es común a todo. Es una lectura mía a partir de #96, no una cita.
- **Propuesta de lectura para la nota**: administrativo = contabilidad, tesorería, impuestos, compras, personal; operativo = inventario, producción, logística, servicios y mantenimiento. Coincide con la agrupación que el árbol ya hace por dominios y con APQC (operativas 1.0-6.0 frente a gestión y soporte 7.0-13.0, de #96).
- **Hueco**: sin la primaria de Gartner no hay forma de verificar la frontera exacta (por ejemplo si compras es administrativa u operativa; Software Advice la pone con lo administrativo en el mismo lenguaje que TechTarget).

## 4. Suite frente a best-of-breed

| Posición | Argumento | Fuente | Marca |
|---|---|---|---|
| A favor de piezas (BoB) | Los paquetes de un solo proveedor «often fail to fit specific organizational and industry needs»; ensamblar componentes de varios proveedores estándar, a veces con partes a medida, ajusta mejor; el enfoque ganaría importancia porque el ERP se vuelve más modular. Caso: una empresa global de entretenimiento. Se compara implantación, ajuste funcional y mantenimiento. | F5 (abstract) | [M] |
| Comparación 2001 | Light, Holland y Wills 2001 compara ERP y BoB; el texto no se leyó. Otros textos del buscador (IndustryWeek «Best of Breed vs. ERP»; Workforce «ERP versus best of breed») son periodismo de negocios de esa época. | F4; https://industryweek.com/companies-amp-executives/best-breed-vs-erp | [M] / [S] |
| Industria, 2013-14 | Postmodern ERP: federar piezas «likely from two or more vendors», con gobierno desde el negocio; pero al mismo tiempo no personalizar lo común («finance is finance»). | F8 | [L] secundaria |
| Contrapeso | El artículo de TechTarget se titula «countered by continued appeal of single suite»: la suite sigue atrayendo (integración, un solo contrato). El texto leído solo da la voz de Ganly; no trae encuesta de mercado. | F8 | [L] |

Para la nota: el debate es de **dónde poner la frontera de integración** (costo de integrar frente a ajuste funcional). Enlaza con `Arquitectura/Estilos/strangler-fig.md` y con las columnas técnicas de integración. Lo que no hay: evidencia empírica reciente con método (la más citada es de 2000-2001).

## 5. Escalones por tamaño (qué cambia de un facturador a un ERP de grande)

Fuentes encontradas, todas flojas para esta sección:

- **Etiquetas del mercado argentino (ya en el repo)**: facturador, sistema contable, sistema de gestión comercial, ERP, con la advertencia de que «los productos reales cruzan las etiquetas». Está en `Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md` (borrador, fuentes de proveedores). No repetir: enlazar.
- **Panorama 2010 por «tiers»**: reporta sobrecostos y retrasos separados por Tier I, II y III (retraso en 30 %, 18 % y 5 % de los proyectos; sobrecosto en 53 %, 33 % y 59 %). La definición de cada tier no apareció en el texto leído, así que la tabla no se puede interpretar. [L] F15, con interés comercial de la consultora.
- **Mabert et al. 2003 (Omega)**: estudia el efecto del tamaño en la implantación de ERP en manufactura de EE. UU. [M]; hay que abrirlo.
- **Ejes que cambian de escalón, a verificar** (propuestos, sin fuente propia salvo lo que cita cada uno): cantidad de usuarios y de comprobantes, multiempresa y multimoneda (columnas técnicas, ya cubiertas en el tema), localización fiscal, quién implanta (proveedor, partner o propia empresa; es la nota `partners-de-implementacion.md`), y qué se personaliza. Son afirmaciones de diseño del árbol, no de una fuente.
- **Hueco claro**: no apareció una fuente primaria o académica que defina los escalones (facturador, pyme, mediana, grande) con criterios. Gartner ha usado «Tier 1/2/3» en sus mercados de ERP, pero no se pudo leer ni confirmar. La nota `escalones-por-tamano.md` quedaría propia de este tema y se escribiría desde los casos del repo y de las fichas de productos (práctica, marcada como evidencia de que existe, sin nombres).

---

## 6. Categoría ERP

- **Definición**: ver 2.2. Lleva los dominios administrativos (contabilidad, tesorería, impuestos, compras, personal) y, en el ERP «de producto», inventario, producción y distribución.
- **Se pisa con**: MES (ISA-95: el ERP es nivel 4), SCM, HCM, CRM, PSA (Gartner pone «Cloud ERP for Service-Centric Enterprises» como mercado de ERP; los PSA se pisan ahí).
- **Frontera**: Gartner no la define por módulos (F9). Odoo y ERPNext agrupan distinto (ya en #96).
- **Recurso canónico**: Klaus, Rosemann y Gable (2000), secciones de definiciones y de la encuesta; en qué fijarse: qué atributos se repiten (integración, base de datos común, modularidad) y cuáles son discutidos.

## 7. CRM (SFA, centro de atención, marketing)

| Dato | Fuente | Marca |
|---|---|---|
| Definición de Gartner: «a business strategy that optimizes revenue and profitability while promoting customer satisfaction and loyalty»; versión previa: «A business strategy designed to optimize profitability, revenue, and customer satisfaction». | Smartsheet y Pega (terceros) citando el glosario | [S] |
| Tres componentes: operativo (automatización de ventas, de marketing y de servicio, con vista única del cliente), analítico (minería de datos), colaborativo (con proveedores y distribuidores). | F18 | [L] secundaria; viene de la literatura académica (Buttle 2004; Reinartz, Krafft y Hoyer 2004; Mithas, Krishnan y Fornell 2005 sobre CRM y satisfacción) |
| Historia: 1982 marketing de bases de datos (Kestenbaum); 1987 ACT! (agenda digital); 1993 Siebel, «primer producto CRM» según Wikipedia; 1997 se populariza; 2004 primer CRM de código abierto. | F18 | [L] secundaria |
| Mercado: Gartner lo parte en SFA (julio 2025) y Customer Engagement Center (octubre 2025); marketing aparte (ya en #96). | #96 | [S] |

- **Qué dominio lleva**: `Relacion-con-clientes` (registro del cliente, oportunidad, pedido), `Servicio-al-cliente` y `Marketing` (pero no se duplica: ver sección 12).
- **Se pisa con**: ERP (quién es dueño del pedido), field service (el caso y la orden de trabajo), marketing automation.
- **Recurso canónico**: los tres componentes de Buttle (2004, *Customer Relationship Management: Concepts and Tools*, citado en F18 [S]) para explicar por qué hay tres mercados bajo una etiqueta.

## 8. HCM (core HR, nómina, talento)

- **Definición**: HCM «sometimes used synonymously with HR»; el «capital humano» propiamente es lo que el individuo sabe y aporta (Armstrong 2006, citado en F21). HRIS: sistemas que guardan y recuperan registros de empleados. [L] F21, secundaria.
- **Gartner**: «Cloud HCM Suites for 1,000+ Employee Enterprises» evalúa Core HR y beneficios, talento antes y después de la contratación, y Payroll Administration (ya en #96). No leído.
- **Dominio**: `Administracion-de-personal-y-nomina` (legajo, asistencia, licencias, nómina). El resto (contratar, evaluar, compensar) es `Liderazgo-y-direccion/Gestion-de-personas` (ya señalado en #96, punto 8).
- **Se pisa con**: ERP (contabilización de la nómina, gastos), talento (aprendizaje, reclutamiento, que van en un mercado aparte de «talent management»).
- **Hueco**: no hay norma ni cuerpo de saber de HCM como software; solo el cuadrante de Gartner y marcos de personas (SHRM, ya en #96).

## 9. SCM, WMS y TMS

- **Gartner** agrupa WMS y TMS bajo supply chain execution (SCE): «execution-oriented applications, including warehouse management systems (WMSs), transportation management systems (TMSs)». [S] F25; planificación aparte (Supply Chain Planning Solutions, #96).
- **WMS**: «software and processes that control and administer warehouse operations from the time goods or materials enter a warehouse until they move out»: inventario, picking, recepción, ubicación. [S] https://www.techtarget.com/enterprise-software/definition/warehouse-management-system-WMS
- **TMS**: «enables enterprise-wide management, optimization, planning, and execution of logistics services for transporting goods» (Manhattan Associates, proveedor) [S] https://www.manh.com/resources/articles/what-is-transportation-management-system-tms ; Oracle lo describe como plataforma de planificación y optimización del movimiento físico. Un documento de DHL, citando a Gartner, atribuye al TMS ahorros de 5 a 10 % del gasto de transporte [S] https://www.dhl.com/content/dam/dhl/global/dhl-supply-chain/documents/pdf/glo-dsc-next-gen-tms-wms.PDF (cifra de un operador logístico, no leída entera).
- **Dominio**: `Inventario-y-depositos` (WMS) y `Cadena-de-suministro-y-logistica` (TMS y planificación).
- **Se pisa con**: ERP (el inventario básico y los pedidos), MES (inventario de planta), OMS/e-commerce.
- **Hueco**: sin historia de WMS y TMS con fuente; sin primaria de Gartner.

## 10. MES y QMS, con ISA-95

| Dato | Fuente | Marca |
|---|---|---|
| «Level 3 describes manufacturing execution systems (MES).» «Level 4 describes all the activities related to running a business.» «The ISA-95 standard primarily deals with the interface between levels 3 and 4.» También «ISA-95, also known as ANSI/ISA-95 or IEC 62264». | F16 | [L] |
| Partes: 1 «Models and Terminology»; 2 «Objects and Attributes for Enterprise-Control System Integration»; 3 «Activity Models of Manufacturing Operations Management»; 4 modelos de objetos para el intercambio entre las actividades de la Parte 3; 5 transacciones negocio-manufactura entre niveles 3 y 4; 6 servicios de mensajería; 7 alias; 8 perfiles de intercambio (la más reciente). Las partes 1, 2 y 3 son adopciones de IEC 62264-1, -2 y -3. | F16 | [L] |
| Niveles 0 a 2: 0 procesos físicos; 1 sensado y accionamiento; 2 monitoreo y control (PLC, DCS). Nivel 3: flujos de trabajo que producen el bien terminado. | F17 | [L] vendor |
| MOM (Parte 3): «activities, functions and exchanges within level 3 of a manufacturing facility»; cuatro categorías: producción, mantenimiento, calidad e inventario; la página agrega actividades de soporte (seguridad, configuración, cumplimiento regulatorio). **Esto cierra la duda abierta de #96** (la lista de cuatro salía de resúmenes): confirmada por un vendor que cita la norma, todavía no por la norma. | F17 | [L] vendor |
| Gartner sobre MES: sistema que supervisa, sigue y sincroniza los pasos físicos que convierten materias primas en bienes; coordina órdenes de trabajo con la programación y los sistemas empresariales; trazabilidad y genealogía; la definición no incluye la capa de automatización (SCADA, HMI, PLC). El Market Guide de 2016 dice que el MES tiene casi tantas definiciones como proveedores. | F22 | [S] |
| MESA: 11 funciones (1997, según Rockwell): secuenciación/detalle, control de documentos, despacho de unidades de producción, recolección de datos, gestión de procesos, asignación de recursos y estado, gestión de mano de obra, gestión de calidad, seguimiento y genealogía, gestión de mantenimiento, análisis de desempeño. Wikipedia: en 2000 ISA-95 fusionó ese modelo con el Purdue Reference Model. El orden de la lista varía entre fuentes. | https://plex.rockwellautomation.com/content/dam/plex/documents/pdf/mes/WhatIsMES_Feb2025.pdf · https://www.wikipedia.org/wiki/Manufacturing_execution_system | [S] |

- **Frontera ERP/MES**: el ERP planifica y registra el negocio (nivel 4: pedidos, órdenes de producción a nivel de planificación, costos); el MES ejecuta (nivel 3: despachar, registrar consumos, trazabilidad). La norma se ocupa sobre todo de lo que viaja entre los dos. En este repo `Produccion/Ejecucion-en-planta/` ya trata orden de producción, consumo y declaración, programación de planta y eficiencia global del equipo: la nota `mes.md` debe enlazar eso y quedarse con la frontera.
- **QMS como apartado**: los QMS no tienen una definición de Gartner encontrada. Las categorías de ISA-95 incluyen calidad como una de las cuatro operaciones. La norma que da el piso del concepto es ISO 9001:2015 (requisitos de un sistema de gestión de la calidad); no se pudo leer la página de ISO (403). En este repo ya existen `Produccion/Calidad/` (no conformidad, acción correctiva, plan de inspección, trazabilidad de lotes, control estadístico). La nota de software debe decir qué agrega el software (registro de no conformidades, flujos de acción correctiva, control de documentos), no repetir el saber.
- **Recurso canónico**: ISA-95 Partes 1 y 3 (IEC 62264-1 y -3); en qué fijarse: el modelo de actividades de la Parte 3 y los objetos intercambiados de la Parte 2. Pago (norma); la página de ISA es solo descriptiva.

## 11. Mesa de ayuda y FSM, PSA, EAM/CMMS, vertical frente a horizontal

### 11.1 Mesa de ayuda (help desk) y gestión de servicio de campo (FSM)

- **FSM**: «the management of a company's resources employed at or en route to the property of clients, rather than on company property»; ubicar vehículos, programar y despachar trabajo, y enlazar con inventario, facturación y contabilidad. El software suele integrarse con «backend systems such as service management, billing, accounting, parts inventory, and other HR systems». La referencia a Gartner de esa página está muerta; trae un dato de 2012 (25 % de penetración del mercado direccionable; 1.200 millones de dólares en 2012, crecimiento anual compuesto de 12,7 %) que no se debe citar por eso. [L] F19, secundaria, con banner de falta de citas. El Market Guide de Gartner de marzo de 2025 dice que el mercado «is integrating adjacent technologies» (#96).
- **Mesa de ayuda**: no se buscó una fuente específica en esta pasada; es un hueco. La fuente natural es ITIL (gestión de servicios de TI); sin leer. Atención: en el campo la mesa de ayuda se vende de dos maneras, como servicio de TI interno (ITSM) y como atención al cliente (customer service); el árbol enlaza el segundo uso con `Servicio-al-cliente`.
- **Dominios**: `Servicio-al-cliente`, `Activos-y-mantenimiento/Servicio-de-campo` (ya existe en el repo).
- **Se pisa con**: CRM (caso y orden de trabajo), EAM (mantenimiento del equipo del cliente), PSA (cuando el servicio es el producto).

### 11.2 PSA

- **Definición**: software para que profesionales (abogados, auditores, consultores de TI) gestionen proyectos de clientes y recursos y sigan la utilización del personal facturable; núcleo: contabilidad de proyectos, gestión de recursos, tiempo y gastos, facturación; los más completos suman CRM y gestión del conocimiento. [L] F20, secundaria; cita Melik y Melik (2002), *Professional services automation*, Wiley, y Hofferberth (2001), ChannelWeb.
- **Gartner**: no publica Magic Quadrant de PSA; sí un Market Guide for Professional Services Automation Platforms (2025-10-15) con proveedores «representativos» sin ranking, y una lista de características obligatorias (reporting y analítica de actividad y rentabilidad; gestión de contratos). Un sitio (ERPResearch) afirma que existe un Magic Quadrant; contradicen otros dos y no se acepta. [S] F23 y https://www.gartner.com/reviews/market/professional-services-automation-platforms
- **Tamaño de mercado** (de una consultora de mercado, citada por Wikipedia): 12.400 millones de dólares en 2024 y 40.300 millones en 2033 proyectados. [S] F20, una sola fuente de una empresa de estudios; no usar sin cotejar.
- **Dominio**: `Servicios-profesionales-y-proyectos` (ya existen Registro de horas, Asignación de personas, Facturación del proyecto, Rentabilidad de la firma).
- **Se pisa con**: ERP «service-centric», CRM, gestión de proyectos (`Gestion-de-proyectos`).
- **Recurso canónico**: Melik y Melik (2002), no leído; en un Gartner pago, el Market Guide de 2025.

### 11.3 EAM y CMMS

- **EAM**: Gartner, citado por TechTarget: «core EAM» son las capacidades básicas de mantener un registro exacto y detallado de los activos; un informe de Gartner de 2004 dice que EAM evolucionó unos diez años antes desde los sistemas de mantenimiento computarizados (CMMS). [S] https://www.techtarget.com/searcherp/definition/enterprise-asset-management-EAM · F24.
- **Diferencia según vendors**: EAM cubre todo el ciclo de vida del activo (adquisición, instalación, operación, mantenimiento, baja); CMMS se centra en la ejecución del mantenimiento. [S] https://www.g2.com/glossary/enterprise-asset-management-definition y https://tractian.com/en/glossary/eam-enterprise-asset-management (ambos de proveedores o de un sitio de reseñas).
- **Norma de respaldo**: ISO 55000 (gestión de activos) fija el vocabulario del ciclo de vida; no se pudo leer (403). En el repo, `Activos-y-mantenimiento/` ya trata registro de activos, orden de trabajo y estrategia.
- **Se pisa con**: ERP (activo fijo contable, repuestos como inventario), MES (mantenimiento operativo de planta, categoría de ISA-95), FSM.
- **Hueco**: sin definición pública de CMMS por una primaria.

### 11.4 Software por rubro (vertical) frente a horizontal

- **No apareció una fuente académica ni de norma** que defina «vertical» frente a «horizontal» para software de gestión. La distinción se usa en el mercado: vertical = construido para una industria con sus procesos y su normativa; horizontal = funciones que sirven a cualquier industria (contabilidad, personal).
- **Lo que sí hay**: el ERP «de producto» frente al «de servicios» de Gartner (#96) es una partición vertical gruesa; la gran diferencia entre rubros es la localización fiscal y los procesos propios (producción, obra, salud). En el repo, la aplicación al comercio está en `Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/` (borrador).
- **Hueco**: una fuente con método (p. ej. estudios de ERP en SMEs por industria, Loh y Ching 2004, «Critical elements for a successful ERP implementation in SMEs», *Int. J. Production Research* 42(17):3433-3455, https://doi.org/10.1080/00207540410001671679, solo citada en F10 [S]). Hay que decidir si la nota se escribe desde la lógica del árbol, con la marca de «propio de este tema».

---

## 12. Si el árbol coincide con cómo el campo divide esto

1. **La división del árbol es casi la del campo.** ERP, CRM, HCM, SCM (WMS/TMS), MES, FSM, PSA y EAM son los nombres de mercado que usan los analistas, con la salvedad del punto 3.
2. **Mesa de ayuda y FSM juntos** (`servicio-de-campo-y-mesa-de-ayuda.md`) no coincide con el campo: los analistas los tienen en mercados distintos (Customer Engagement Center frente a Field Service Management) y la mesa de ayuda también existe como ITSM, un mercado que el árbol no nombra (#96, punto 5). Conviene dejar en la nota dicha frontera.
3. **EAM y CMMS** van juntos con razón (el CMMS es el antecesor de EAM, F24), pero MES, según ISA-95, también tiene una categoría de mantenimiento: la nota `eam-y-cmms.md` debe señalar esa superposición con `mes.md`.
4. **QMS como apartado de MES** es defendible por ISA-95 (calidad es una de las cuatro operaciones de nivel 3), pero en la práctica los QMS se compran también fuera de la planta (ISO 9001 aplica a cualquier organización, también a servicios). Merece una frase en la nota.
5. **Las categorías del árbol dejan afuera**: BI (decidido, enlaza a Datos), ITSM, comercio electrónico/POS (ya en `Comercio-electronico`), gestión documental, y las plataformas de integración. Ninguna es del dominio del software de gestión en sentido estricto, pero ITSM y gestión documental aparecen en las ofertas de los proveedores grandes.
6. **El corte «administrativo frente a operativo»** es de Gartner y se puede usar como eje; falta la primaria.

## 13. Qué ya está escrito en el repo y qué es propio de este tema

| Ya escrito (enlazar, no copiar) | Es propio de este tema |
|---|---|
| `Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md`: módulos de un sistema de gestión para comercio, cuatro etiquetas (facturador, contable, gestión comercial, ERP), «fuente de verdad», instalado frente a nube. Borrador, fuentes de proveedores. | La definición de ERP con su historia y su desacuerdo (F1, F10); los mitos; las categorías de mercado y cómo se pisan; los escalones como criterio general (no solo del comercio). |
| `Produccion/Ejecucion-en-planta/` y `Produccion/Calidad/`: orden de producción, consumo, programación de planta, OEE; no conformidad, acción correctiva, trazabilidad. | La frontera ERP/MES (ISA-95 niveles 3 y 4) y qué agrega el software de calidad. Ninguna nota del repo menciona ISA-95, best-of-breed ni MRP (búsqueda en el repo, fuera de `.investigacion` y de `conocimiento.md`: solo aparecen en Activos y mantenimiento, y por «MRP» en el sentido de repuestos, no de planificación). |
| `Activos-y-mantenimiento/` (registro de activos, orden de trabajo, servicio de campo), `Servicios-profesionales-y-proyectos/`, `Relacion-con-clientes/`, `Administracion-de-personal-y-nomina/`, `Inventario-y-depositos/`, `Cadena-de-suministro-y-logistica/`: el saber de dominio. | Cómo cada categoría de software lo empaqueta y con qué se pisa. |

---

## 14. Recurso canónico por componente

| Componente | Recurso | Qué parte y en qué fijarse |
|---|---|---|
| Fundamentos, definiciones | Klaus, Rosemann y Gable (2000) | La meta-comparación de definiciones y la conclusión de que no hay definición común; citar el abstract tal cual. |
| Fundamentos, historia | Jacobs y Weston (2007), *J. Oper. Manag.* | La línea MRP→MRP II→ERP→cadena de suministro; sin leer: pedirla antes de escribir. |
| Fundamentos, historia previa | Orlicky (1975) | La lógica de MRP (lista de materiales, explosión de necesidades); como lector, entender el antecedente de todo ERP de manufactura. |
| Fundamentos, mecanismo | Davenport (1998), *HBR* | La imposición de la lógica de negocio sobre la empresa, el costo de la integración. |
| Fundamentos, posición del analista | Gartner postmodern ERP (2013-14) y composable ERP | Pago. Para cita pública: la nota de prensa de 2014 y F8. |
| Fundamentos, mitos | Gartner (la afirmación del 70 %) y Panorama 2010 | Qué mide cada cifra, quién la dice y para qué: marcar el interés comercial. |
| Categorías, suite o piezas | Light, Holland y Wills (2001) | La comparación de los criterios (complejidad de implantación, ajuste, mantenimiento). |
| Categorías, MES | ISA-95 / IEC 62264 (Partes 1 a 3) | Niveles 3 y 4, interfaz y las cuatro operaciones de la Parte 3. |
| Categorías, EAM | ISO 55000 | El vocabulario del ciclo de vida del activo. Sin leer. |
| Categorías, CRM | Buttle (2004) vía Wikipedia (F18) | Operativo, analítico y colaborativo. |
| Categorías, PSA | Melik y Melik (2002), Wiley | Alcance de la categoría. Sin leer. |
| Categorías, escalones | Ninguno hallado | Hueco. |

---

## 15. Huecos

1. **Jacobs y Weston (2007)**, el recurso canónico de la historia: solo cita y keywords. Hay que leerlo con acceso institucional antes de afirmar fechas del tramo MRP→ERP; mientras tanto la historia de arriba descansa en Wikipedia.
2. **Davenport (1998)** y **Light, Holland y Wills (2001)**: solo metadatos; no se pudo citar ninguna frase literal salvo el abstract de ECIS 2000.
3. **Gartner**: todas las definiciones (ERP, MES, CRM, HCM, FSM, PSA, administrativo frente a operativo, composable) son [S]; el glosario, las notas de prensa y los reviews devolvieron 403. La fecha exacta y el documento donde Gartner acuñó «ERP» (¿1990?) no se verificó en primaria.
4. **Tasa real de fracaso de ERP con método**: no hay fuente académica leída. La cifra de Gartner no tiene estudio nombrado; Standish sin cifra de ERP; Panorama es de una consultora y no usa «fracaso».
5. **Escalones por tamaño**: ninguna fuente que los defina; el ejemplo de Panorama por «tiers» no trae sus definiciones.
6. **Vertical frente a horizontal**: sin fuente.
7. **Mesa de ayuda / ITSM**: no se buscó; falta ITIL.
8. **EAM/CMMS**: sin ISO 55000 ni definición primaria; **QMS**: sin ISO 9001 leída.
9. **WMS/TMS**: sin historia ni primaria; las definiciones salen de TechTarget y de proveedores.
10. **ISA-95 operaciones**: confirmadas por un vendor (Siemens), no por la norma (de pago). La MESA de 11 funciones tiene orden inconsistente entre fuentes.
11. **ERP II**: la definición es atribución secundaria; la nota de Gartner de 2000 no se leyó.
12. **Monk y Wagner, Laudon y Laudon, Fowler *Analysis Patterns***: nombrados por el brief; no se buscaron en esta pasada (el último pertenece más al ángulo de columnas técnicas).
13. **Tercera ronda de búsqueda** no usada por componente; se paró por el muro de pago, no porque estuviera agotado.
