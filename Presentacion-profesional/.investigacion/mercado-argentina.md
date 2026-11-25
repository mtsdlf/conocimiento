# Mercados (1) Argentina local y (5) empresas extranjeras con entidad en Argentina

Investigado el 2026-11-24. Cobertura parcial: ver Huecos. La Encuesta de Sueldos se calculó directamente del dataset abierto (fuente primaria); lo demás es prensa o página de organismo leída con WebFetch (resumen de un modelo chico, no lectura literal).

## Tabla de fuentes

Puntajes 1-3: autoridad / profundidad / ejemplos / unicidad. [L] leído entero, [M] metadatos o abstract, [S] resumen del buscador.

| # | Fuente | Tipo | Aut/Prof/Ej/Uni | Lectura |
|---|---|---|---|---|
| F1 | Dataset sysarmy 2026.1 (Google Sheet): https://sysar.my/sueldos20261 (CC BY-NC-SA 4.0) | primaria | 3/3/3/3 | [L] procesado entero, 4.939 filas |
| F2 | Dataset sysarmy 2025.1: https://sysar.my/sueldos20251arg | primaria | 3/3/3/3 | [L] procesado, 5.196 filas |
| F3 | Dataset sysarmy pulso 2025.2: https://sysar.my/sueldos20252arg | primaria | 3/3/3/3 | [L] procesado, 3.748 filas |
| F4 | Blog sysarmy 2026.1 (6-mar-2026): https://sysarmy.com/blog/posts/resultados-de-la-encuesta-de-sueldos-2026-1/ | primaria | 3/1/1/2 | [L] solo da participación y enlaces |
| F5 | Página de openqube 2026.1: https://sueldos.openqube.io/encuesta-sueldos-2026.01/ | primaria | 3/?/?/? | [M] es una SPA; no se pudo leer el análisis |
| F6 | Ámbito, 29-jul-2026, informe OPSSI/CESSI 1T2026: https://www.ambito.com/tecnologia/la-industria-del-software-argentino-vuelve-tener-exportaciones-record-pero-el-empleo-cae-primera-vez-seis-anos-n6304732 | secundaria (cita primaria OPSSI) | 2/2/2/1 | [L] |
| F7 | ItSitio sobre exportaciones: https://www.itsitio.com/ar/software/la-industria-del-software-argentino-alcanzo-un-record-de-exportaciones-de-usd-2-967-millones-en-2026/ | secundaria | 1/1/1/1 | [S] |
| F8 | El Economista, 9-sep-2026, estudio CAF/IIEP (UBA-CONICET): https://eleconomista.com.ar/economia/mercado-laboral-2026-cuales-son-perfiles-inteligencia-artificial-mas-buscados-argentina-n98048 | secundaria (estudio primario CAF no leído) | 2/2/2/3 | [L] |
| F9 | iProUP, 6-nov-2026, Argencon: https://www.iproup.com/empleo/72978-sector-que-genera-350000-empleos-en-argentina-busca-evitar-que-la-ia-cambie-las-reglas | secundaria | 1/1/1/1 | [L] con inconsistencia interna |
| F10 | El Observador, 13-may-2026, Beyond: https://www.elobservador.com.uy/espana/empresas-y-negocios/un-socio-google-cloud-europa-anuncia-una-inversion-tecnologica-argentina-n6043836 | secundaria | 1/1/2/2 | [L] |
| F11 | Mercado.com.ar, Indra en Puerto Madero (nov-2025): https://mercado.com.ar/innovacion/indra-group-inaugura-oficinas-en-puerto-madero-para-impulsar-innovacion-tecnologica-en-argentina | secundaria | 1/1/1/2 | [S] |
| F12 | Cronista/InfoTechnology, nota de sueldos IA (sin fecha confirmada): https://www.cronista.com/informacion-gral/ni-programador-ni-disenador-el-nuevo-trabajo-vinculado-a-ia-que-ofrece-sueldos-de-hasta-us-7000/ | secundaria | 1/1/1/1 | [S] |
| F13 | Cessi Memoria 2025: https://cessi.org.ar/wp-content/uploads/2025/10/Memoria-2025.pdf | primaria | 3/?/?/? | [M] solo aparece en el buscador, no abierta |
| F14 | Coderhouse (vendedor de cursos), ML engineer Argentina y remoto: https://www.coderhouse.com/coderlibrary/cuanto-gana-un-ingeniero-de-machine-learning-en-argentina-y-remoto | vendedor | 1/1/1/1 | [S] |
| F15 | Maximiliano Firtman en X, resumen del análisis openqube: https://x.com/maxifirtman/status/2029577326652977241 | secundaria | 2/1/1/1 | [S] |

Descartadas por fecha inconsistente: varias notas de iProfesional con "fecha" 2026 en el buscador (por ejemplo https://www.iprofesional.com/management/362143-especialistas-en-inteligencia-artificial-que-sueldo-cobran-hoy) listan sueldos de ARS 180.000 a 550.000 por mes, que corresponden a años atrás: la fecha que muestra el buscador no es la de publicación. No usar.

## 1. Títulos de puesto y demanda

- **La encuesta local casi no tiene los roles de IA.** El campo `trabajo_de` de F1 (n=4.939) trae "AI Engineer" (12 personas, 0,2%), "AI / Prompt / Chatbots" (2) y "R&D" (2). No existe "ML Engineer", "MLOps" ni "LLM engineer". Sí existen "Data Scientist" (93), "Data Engineer" (144) y "SysAdmin / DevOps / SRE" (555, 11% de la muestra). Fuente: F1, conteo propio. "AI Engineer" aparece en F2 con 7 y en F3 con 0: la categoría es nueva y mínima.
- **Para los avisos, la medición más seria es el estudio CAF/IIEP:** analizó "más de 1,2 millones de búsquedas laborales en la región, de las cuales 64.088 corresponden a Argentina" (Computrabajo, ZonaJobs, Workana). La proporción de avisos con competencias de IA pasó de 0,6% (2017-2022) a 2,6% en 2026, "la mayor aceleración de la región"; "el 97% del mercado aún no lo exige de forma explícita". Ninguno pide solo IA (0%). Habilidades más pedidas: Machine Learning, NLP, chatbot, ChatGPT, TensorFlow, Deep Learning, RAG, MLOps, LangChain, Prompt Engineering, Scikit-Learn, Gemini; emergentes: LangGraph, CrewAI, AutoGen, Pinecone, Weaviate. Fuente: F8 (9-sep-2026). Matiz: son portales masivos, no de tecnología; el sesgo es hacia puestos no técnicos que piden "usar IA".
- **Lo que piden los avisos en años, inglés y stack: no lo encontré con datos.** El buscador mostró un aviso de Computrabajo "Machine Learning IA Enginerr - Híbrido CABA Centro" (ref. 20597) que según el resumen del buscador pide más de cinco años de experiencia en ML/AI engineering, pero no pude abrir el aviso (F14/S) y su sueldo publicado (ARS 11.111) es anómalo. Un solo aviso, [S]: no sirve de tendencia.
- **Qué usa la gente que respondió F1 (stack actual):** Python lo menciona 1.775 de 4.939 (36%), Kubernetes 891 (18%), TensorFlow 102 (2%), LangChain 6, PyTorch 1, Terraform 11 (el campo es de texto libre, no capta bien las variantes de escritura). Es lo que se usa en los puestos, no lo que piden los avisos.
- **Uso de IA en el trabajo (F1):** 2.139 de 4.939 (43%) se autocalifican 5 de 5 en uso de copilot/ChatGPT; 118 (2%) en 0. Contexto: el mercado local ya usa IA como herramienta, lo que no equivale a demanda de quien la construye.

## 2. Sueldos: Encuesta de Sueldos sysarmy / openqube

**Método.** Encuesta autoseleccionada (no probabilística), online, dos ediciones por año (2025.1 en feb-2025; 2025.2 es un "pulso" más corto en ago-2025; 2026.1 con relevamiento dic-2025 a feb-2026, publicada el 6-mar-2026). 2026.1: "5.074 personas participaron... 4.939 respuestas fueron consideradas" (97%) (F4). Solo trabajadores de IT en Argentina. Todo lo de abajo es mío, calculado de F1-F3: **ARS bruto mensual, mediana (valor en la posición n/2 ordenada), n entre paréntesis**. Se excluyeron respuestas menores a ARS 50.000. Mi mediana general de 2026.1 (3.268.000) coincide con el resumen de Firtman en F15 ("$3.254.000 (todos los puestos y seniority)" [S]), diferencia del 0,4% por criterio de filtro. Los valores en USD de quienes cobran en dólares están convertidos a pesos por el encuestado, por lo que dependen del dólar tomado; el campo "último valor del dólar" está incompleto.

| Segmento | 2025.1 (feb-2025) | 2025.2 pulso (ago-2025) | 2026.1 (ene-2026) |
|---|---|---|---|
| Todos | 2.290.000 (5.196) | 2.900.000 (3.748) | 3.268.000 (4.939) |
| Junior | 1.300.000 (914) | 1.566.270 (462) | 1.700.000 (533) |
| Semi-senior | 2.000.000 (1.634) | 2.400.000 (1.208) | 2.700.000 (1.514) |
| Senior | 3.000.000 (2.648) | 3.600.000 (2.078) | 4.100.000 (2.892) |
| Developer (todos) | 2.160.000 (1.776) | 2.700.000 (1.301) | 3.132.530 (1.666) |
| Developer senior | 3.096.000 (705) | 3.500.000 (596) | 4.030.000 (832) |
| SysAdmin / DevOps / SRE (todos) | 2.250.000 (630) | 2.700.000 (419) | 3.200.000 (555) |
| SysAdmin / DevOps / SRE senior | 2.598.000 (408) | 3.000.000 (269) | 3.500.000 (374) |
| Data Engineer (todos) | 2.545.125 (142) | 3.200.000 (110) | 3.570.000 (144) |
| Data Engineer senior | 3.845.000 (48) | 4.000.000 (42) | 4.300.000 (62) |
| Data Scientist (todos) | 2.640.000 (108) | 3.422.000 (87) | 4.138.145 (93) |
| Data Scientist senior | 4.500.000 (23) | 4.700.000 (29) | 5.000.000 (38) |
| AI Engineer | 4.301.000 (7) | sin datos | 3.209.586 (12); senior n=2, no usable |

Lecturas:
- **Tendencia:** en pesos, la mediana general subió de 2,29 M (feb-2025) a 3,27 M (ene-2026), +43% en un año calendario; no ajustado por inflación. La nota de openqube citada por el buscador dice que entre junio-2025 y enero-2026 la inflación del INDEC fue 19% y la mediana subió 13% (F5/F15 [S]), o sea caída real en ese semestre. Firtman resume "13% en pesos, 7% en dólares, bajó 5% ajustado por IPC" (F15 [S]).
- **DevOps/SRE pagan menos que Data y que Architect** en el tramo senior: 3,5 M contra 4,3 M (Data Engineer) y 5,0 M (Data Scientist); Architect senior 6,0 M (n=118) y Technical Leader senior 5,0 M (n=290), 2026.1.
- **Roles de ML/IA como roles separados: la encuesta no los separa.** Solo hay "Data Scientist", "Data Engineer" y "AI Engineer" (n minúsculo). Para ML engineer, MLOps o platform no hay mediana confiable; lo más cercano son Data Scientist y SysAdmin/DevOps/SRE. "Platform engineer" no es categoría.
- **Brecha exterior/local: la encuesta no pregunta a quién se trabaja.** No hay columna de empresa ni de país del empleador en el CSV (columnas de F1: `pagos_en_dolares`, `tipo_de_contrato`, `modalidad_de_trabajo`, entre otras). Proxy usado: quien "cobra todo el salario en dólares", típicamente trabaja para el exterior, pero también hay locales dolarizados. Eso es una inferencia mía, no un dato de la fuente.
  - Cobra todo en dólares: 14,9% (737 de 4.939) en 2026.1; 15,6% en 2025.1; 14,1% en 2025.2. Parte en dólares: 10,0% / 13,7% / 13,2%. "Sueldo dolarizado pero cobra en pesos": 7,1% / 6,2% / 6,6%. Total con alguna relación con el dólar en 2026.1: 32%; 68% 100% en pesos, que coincide con el "68% 100% en pesos, 15% 100% en dólares" de F15 [S].
  - Mediana bruta equivalente en pesos, 2026.1: todo en dólares 5.500.000 (737); parte 3.814.728 (493); solo pesos 3.000.000 (3.356). Brecha todo-dólares contra solo-pesos: **+83%** (en 2025.1: 3,6 M contra 2,05 M, +76%; en 2025.2: 4,3 M contra 2,6 M, +65%).
  - Por rol, senior, 2026.1: Developer todo en dólares 6.651.000 (192) contra solo pesos 3.500.000 (474); DevOps/SRE todo en dólares 7.252.100 (48) contra solo pesos 3.200.000 (272). La diferencia es de 1,9 a 2,3 veces. En USD, entre quienes cobran todo en dólares y declaran el dólar tomado (n=329), la mediana es USD 3.520 por mes bruto (no distingue trabajo por cuenta propia ni contractor).
- Otros cortes 2026.1: contractor 4.000.000 (812) contra staff 3.300.000 (3.526); 100% remoto 3.500.000 (2.352, 48% de la muestra); 22% está buscando activamente trabajo (1.075) y 65% "no, pero escucho ofertas" (3.205).
- **Despidos:** 1.676 (34%) respondieron "Sí" a "hubo reducción de personal en los últimos 6 meses" en su empresa (2.138 "No", 1.125 "No sé").
- **Años de experiencia, inglés:** la encuesta tiene años de experiencia pero no nivel de inglés (no hay columna).

Sobre sesgo: la muestra se arma por difusión en comunidades; seniors son 59% de las respuestas (2.892 de 4.939) y CABA/GBA concentran 72% (2.476 + 1.064), por encima de su peso en el empleo del sector. Tomar las medianas como "personas conectadas a la comunidad IT", no como el mercado.

## 3. Tamaño del sector

- **Software y servicios informáticos (SSI), registrado, 1T2026:** 162.391 trabajadores; -0,5% contra 4T2025, "la primera caída en seis años"; +65.398 puestos desde 2015 (+67,3%); pasó de 1,5% a 2,4% del empleo privado registrado (2015 a 2025). Salario bruto promedio del sector ARS 3.738.000 (110% sobre el promedio de la economía). Exportaciones 1T2026 USD 744 M (récord trimestral); acumulado 12 meses USD 2.848 M; 2025 +13,8%; destinos 2025: EE.UU. 49,1%, España 14,7%, Uruguay 10,7%, México 7,7%. Fuente: F6 (29-jul-2026), que cita a OPSSI/CESSI y a la Secretaría de Trabajo.
- Discrepancia: F7 [S] reporta USD 2.967 M en 12 meses a junio-2026 (+10,6%) y "más de 162.000" puestos; no verificada contra el informe primario. Con F6, el semestre sería +17% interanual.
- **Economía del Conocimiento / SBC, mucho más amplio:** "más de 350.000 profesionales", exportaciones USD 10.500 M (+10,3%), según Argencon en una reunión con el ministro Caputo (F9, 6-nov-2026). La nota se contradice: un recuadro dice que USD 10.500 M es de 2023. Cronista habla de USD 10.085 M anualizados (F12/S, período no claro). No tomar como cifra firme; no hay fuente primaria.
- **Cuántos trabajan para el exterior:** no encontré ese dato. Lo único que ordena: ~49% de las exportaciones SSI van a EE.UU. (F6), y en F1 14,9% cobra todo en dólares. Eso son exportaciones por valor, no personas.
- **Qué mide cada cosa:** SSI registrado en SIPA (CESSI/OPSSI) no incluye monotributistas ni contractors facturando como independientes, que en F1 son 812 contractor + 175 freelance + 389 tercerizados (28% de la muestra). El empleo "no registrado como SSI" de gente que trabaja para el exterior queda fuera de las cifras sectoriales.

## 4. Mercado (5): empresas extranjeras con entidad en Argentina

Datos escasos; ejemplos fechados, no un mapa.
- **Beyond** (socio de Google Cloud en Europa) anunció el 13-may-2026 un centro de entrega en Argentina: "más de 100 ingenieros... en los próximos 12 meses", para modernización cloud, operaciones de seguridad, IA y activación de datos, entre otras áreas. No indica ciudad ni cargos (F10).
- **Indra Group** abrió oficinas en Puerto Madero en nov-2025 como hub regional de IA, ciberseguridad y analítica (F11 [S]).
- No encontré avisos ni cifras de Accenture, Globant, Oracle o Google en Argentina para roles de IA/plataforma. Ojo: Globant y Mercado Libre se consideran empresas argentinas (mercado 1), y el análisis de cuáles son "extranjeras con entidad" no fue hecho.
- En F1, 812 contractors y 389 "tercerizado (consultora o agencia)" indican que parte del mercado pasa por consultoras; no distingue si son locales o extranjeras.

## Tabla resumen rol × mercado (solo lo hallado)

| Rol | (1) Argentina local | (5) Extranjeras con entidad en AR |
|---|---|---|
| AI engineer / applied AI | Título casi inexistente en la encuesta (n=12); 2,6% de avisos masivos piden competencias de IA (F8). Mediana n=12: ARS 3,2 M, poco confiable | Beyond y Indra mencionan IA, sin cargos ni sueldos (F10, F11) |
| Forward-deployed | Sin datos | Sin datos |
| Plataforma/serving de IA, MLOps | MLOps aparece como habilidad pedida en avisos masivos (F8); sin cifras de sueldo propias | Sin datos |
| Evals | Sin datos | Sin datos |
| ML engineer aplicado | Sin categoría; proxy Data Scientist: mediana ARS 4,14 M (n=93), senior 5,0 M (n=38) en 2026.1 (F1) | Sin datos |
| Platform / DevOps / SRE | 555 respuestas, ARS 3,2 M mediana, senior 3,5 M (n=374); +42% en 12 meses nominal (F1, F2); senior que cobra todo en dólares 7,25 M (n=48) contra 3,2 M solo pesos (n=272) | Beyond: operaciones de seguridad y cloud (F10) |

## Huecos

- Informe del OPSSI/CESSI primario (1T2026) y Memoria Cessi 2025 (F13): no abiertos; se usó prensa.
- Análisis publicado de openqube 2026.1 (SPA que no se pudo leer): no se vio qué dice su publicación sobre trabajo para el exterior ni sobre el dólar; se recalculó del CSV.
- OEDE/SIPA: la búsqueda no devolvió nada útil; no hay serie oficial del Ministerio de Trabajo propia.
- Cuántas personas del sector trabajan para el exterior: sin dato.
- Avisos locales de IA y plataforma con años, inglés y stack: sin muestra; no se pudo abrir Indeed (403) ni Computrabajo, y Get on Board no apareció. Recomendación: una ronda específica con un scraping manual de Get on Board, LinkedIn y Computrabajo con búsquedas "AI engineer", "MLOps", "SRE", anotando fecha.
- Mercado (5): sin cifras de empleo, sin salarios de multinacionales en Argentina (Levels.fyi, Glassdoor no se consultaron).
- Estudio CAF/IIEP original (F8): solo vía El Economista.
- La encuesta no tiene a quién se trabaja, nivel de inglés ni roles de ML engineer/MLOps/platform: límite de la fuente, no del análisis.
