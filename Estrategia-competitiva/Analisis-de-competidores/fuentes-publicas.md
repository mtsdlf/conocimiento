---
resumen: >-
  Las fuentes públicas son lo que un competidor deja a la vista de cualquiera: su sitio, sus precios, su documentación, sus ofertas de empleo, lo que dicen sus clientes y lo que estiman herramientas de terceros. Son la etapa de recolección del ciclo de inteligencia, y cada dato vale según quién lo dice y si otra fuente lo confirma.
estado: vigente
estabilidad: semi
fuentes:
  - "Michael E. Porter, Competitive Strategy, Free Press (1980), cap. 3, p. 71 (leído; ver Estrategia-competitiva/.investigacion/analisis-de-competidores-1.md)"
  - "Wikipedia, Admiralty code: https://en.wikipedia.org/wiki/Admiralty_code (leído completo; remite a US Army FM 2-22.3, https://irp.fas.org/doddir/army/fm2-22-3.pdf, que no se abrió)"
  - "Jansen, Jung y Salminen (2022), PLoS ONE 17(5): e0268212: https://pmc.ncbi.nlm.nih.gov/articles/PMC9140287 (leído en parte, los primeros 100.000 de 250.000 caracteres)"
  - "Fishkin, SparkToro (22-nov-2022), Which 3rd party traffic estimate best matches Google Analytics: https://sparktoro.com/blog/which-3rd-party-traffic-estimate-best-matches-google-analytics/ (leído completo)"
  - "Screaming Frog (13-jun-2016), How accurate are website traffic estimators: https://www.screamingfrog.co.uk/how-accurate-are-website-traffic-estimators/ (leído completo)"
  - "Omniconvert, estudio de 1.787 tiendas online: https://www.omniconvert.com/blog/we-analyzed-1787-ecommerce-websites-similarweb-google-analytics-thats-we-learned/ (según resumen; método no verificado)"
  - "OWOX, SimilarWeb vs Semrush (datos de enero de 2020): https://www.owox.com/blog/articles/semrush-vs-similarweb.md (según resumen)"
  - "Estrategia-competitiva/.investigacion/analisis-de-competidores-2.md"
  - "Estrategia-competitiva/.investigacion/vistazo-practica.md"
aliases: [open source intelligence, OSINT, fuentes abiertas, recolección, collection, Admiralty code, escala de confiabilidad, código del almirantazgo, NATO source reliability]
creado: 2026-11-22
revisado: 2026-11-22
---

# Fuentes públicas

Las fuentes públicas son lo que un competidor deja a la vista de cualquiera: su sitio, sus precios, su documentación, sus ofertas de empleo, lo que dicen sus clientes y lo que estiman herramientas de terceros. Son la etapa de recolección del ciclo de inteligencia, y cada dato vale según quién lo dice y si otra fuente lo confirma.

Lo que se puede juntar y cómo tiene un límite ético, en [ética y legalidad](etica-y-legalidad.md), y uno legal, en [ley argentina y competidores](ley-argentina-y-competidores.md). Qué preguntas guían la recolección sale de la decisión, como dice el [ciclo de inteligencia](ciclo-de-inteligencia.md): una lista de fuentes no reemplaza esa pregunta.

## Los datos llegan de a gotas

Porter (1980, cap. 3, p. 71) ya listaba las fuentes de un sistema de inteligencia sobre competidores: informes presentados en público, discursos de la gerencia del rival ante analistas, la prensa de negocios, la fuerza de ventas propia, clientes y proveedores compartidos, la inspección de los productos del rival, las estimaciones de los ingenieros propios y lo que saben quienes dejaron de trabajar para el competidor. Su advertencia sigue vigente: los datos "come in trickles rather than rivers". Ninguna fuente sola alcanza; el valor está en cruzarlas.

## Qué da cada tipo de fuente

La tabla ordena los tipos de fuente abierta sobre un competidor de software. No se encontró un estudio ni un manual abierto que mida la confiabilidad de cada tipo: las columnas "cuánto vale" y "cómo se sesga" son criterio de esta base, no un dato medido.

| Fuente | Qué da | Cuánto vale (criterio propio) | Cómo se sesga |
|---|---|---|---|
| Sitio y página de precios | Planes, límites, segmentos a los que apunta, mensajes | Alto para lo que el rival declara | Muestra lo que quiere vender, no lo que funciona |
| Documentación y API | Funcionalidades reales, límites técnicos, integraciones | Alto: suele describir lo que existe | Puede estar atrasada respecto del producto |
| Registro de cambios (*changelog*) | Ritmo y dirección del desarrollo | Medio-alto, si se sigue en el tiempo | Destaca lo que suma y calla lo que se quita |
| El producto mismo | Experiencia, flujos, calidad | Alto, de primera mano ([desarme de producto](desarme-de-producto.md)) | Se ve la versión de prueba, no la de un cliente grande |
| Reseñas de clientes (directorios de software, tiendas de apps) | Quejas, motivos de elección y de abandono | Medio ([análisis de reseñas](../../UX/Investigacion/analisis-de-resenas.md)) | Escriben los muy conformes y los muy enojados; algunas son incentivadas |
| Ofertas de empleo | Hacia dónde invierte: equipos, tecnologías, mercados | Medio, como señal temprana ([puntos ciegos](puntos-ciegos.md)) | Una búsqueda no es un plan aprobado |
| Reportes a inversores y prensa financiera | Métricas, estrategia declarada, riesgos | Alto si es un reporte regulado ([lectura de reportes públicos](lectura-de-reportes-publicos.md)) | El rival elige qué contar; la prensa repite comunicados |
| Prensa y comunicados | Lanzamientos, alianzas, rondas | Bajo-medio | Es la versión del rival |
| Estimadores de tráfico | Visitas y fuentes de tráfico de un sitio | Orden de magnitud, no cifra (ver abajo) | Error sistemático, peor en sitios chicos |
| Detectores de tecnología | Qué herramientas usa el sitio del rival | Sin estudios de precisión | Ven solo lo que se carga en el navegador |
| Clientes y ventas propias | Contra quién se pierde y por qué | Alto para lo comercial | El vendedor que pierde culpa al precio |

Los nombres concretos de herramientas cambian rápido. Como ejemplos a noviembre de 2026: SimilarWeb, Semrush y Ahrefs estiman tráfico; BuiltWith detecta tecnologías; G2, Capterra y las tiendas de apps juntan reseñas.

## Los registros públicos de una empresa argentina

Una sociedad argentina deja rastro en registros oficiales (Boletín Oficial, IGJ, CNV, INPI, ARCA, la Central de Deudores del BCRA y las compras del Estado), y ninguno da ventas ni clientes. Qué da cada uno y sus límites, con fecha de consulta, está en la ficha de [registros públicos argentinos](registros-publicos-argentinos.md).

## Quién lo dice y si está confirmado

La escala de confiabilidad que usan los servicios de inteligencia, conocida como *Admiralty code*, separa dos preguntas. Una es cuánto se puede confiar en la fuente; la otra, cuánto se puede creer el dato. Se evalúan por separado. Según Wikipedia, que remite al manual FM 2-22.3 del Ejército de EE.UU., los valores son estos:

| Fiabilidad de la fuente | Credibilidad de la información |
|---|---|
| A: "Completely reliable" | 1: "Confirmed by other sources" |
| B: "Usually reliable" | 2: "Probably True" |
| C: "Fairly reliable" | 3: "Possibly True" |
| D: "Not usually reliable" | 4: "Doubtful" |
| E: "Unreliable" | 5: "Improbable" |
| F: "Reliability cannot be judged" | 6: "Truth cannot be judged" |

Según un resultado del buscador, el Ejército de EE.UU. la adoptó en 1951, en el manual FM 30-5 *Combat Intelligence*, para evaluar informantes. En la versión del FM 2-22.3 que reproduce Small Wars Journal, el 6 dice "Cannot be judged". El manual primario no se abrió.

Para quien no es analista, el valor está en no mezclar los dos ejes. Los ejemplos que siguen son de esta base. Una reseña anónima es una fuente F, pero el dato puede subir a 1 si tres clientes en entrevistas dicen lo mismo. La página de precios del rival es una fuente A sobre sus precios y una fuente pobre sobre cuántos clientes tiene cada plan. El 1 exige confirmación independiente: dos notas de prensa que copian el mismo comunicado son una sola fuente.

## Cuánto se equivocan los estimadores de tráfico

Según la lectura de esta base a partir de los estudios, los estimadores de tráfico sirven para comparar sitios entre sí y ver tendencias, y no para dar cifras absolutas. Los estudios discrepan en hacia dónde se equivocan.

- **Jansen, Jung y Salminen (2022, *PLoS ONE*)** compararon SimilarWeb con Google Analytics en 86 sitios de 26 países y 19 rubros durante 12 meses (septiembre de 2019 a agosto de 2020). SimilarWeb dio 19,4 % menos visitas y 38,7 % menos visitantes únicos. La correlación de rankings fue alta (rs = 0,954 y 0,967); para rebote y duración de sesión fue mucho peor (rs = 0,461 y 0,536). Los autores aclaran que miden precisión, no exactitud, porque no hay una verdad de referencia, y que las diferencias parecen sistemáticas. El abstract y el cuerpo del paper dan cifras distintas para el rebote (25,2 % contra 6,8 puntos) y la duración (56,2 % contra 52,6 %).
- **SparkToro (2022)** comparó cuatro proveedores con Google Analytics en 641 sitios, con 7.692 datos sitio-mes entre junio de 2020 y junio de 2021. SimilarWeb fue el que más veces quedó dentro de ±30 % de Google Analytics, salvo en sitios de menos de 5.000 usuarios mensuales, donde fue el peor. En sitios más grandes acertó dentro de ±30 % cerca del 63 % de las veces. Las correlaciones con Google Analytics fueron 0,790 para SEMrush, 0,720 para Datos, 0,659 para SimilarWeb y 0,504 para Ahrefs. Los errores por exceso y por defecto estuvieron bastante balanceados.
- **Screaming Frog (2016)**, con 25 sitios del Reino Unido y solo tráfico orgánico, encontró que SimilarWeb sumó 15,7 millones de visitas contra 13,4 millones reales, y que los sitios de menos de 10.000 visitas orgánicas tuvieron errores de al menos 40 %.

> [!IMPORTANT]
> La dirección del error no coincide entre estudios. *PLoS ONE* encontró que SimilarWeb subestima; Screaming Frog, que sobreestima; SparkToro, que el error está balanceado. Un estudio de Omniconvert sobre 1.787 tiendas online dice que sobreestima cerca de 94 %, y uno de OWOX con datos de enero de 2020 reporta desvíos de 45 % a 61 % para SimilarWeb y Semrush; los dos son de proveedores y su método no se verificó.

De BuiltWith y de los demás detectores de tecnología no se encontró ningún estudio de precisión.

Un competidor chico de un SaaS o una tienda online nueva está justo en el rango donde los estimadores fallan más. Para esos casos, el tráfico estimado sirve como mucho para decir "es diez veces más chico que el líder", y conviene cruzarlo con otra señal, como la cantidad de reseñas o de ofertas de empleo.

## Recurso canónico

Para evaluar fuentes, el cuadro A-F / 1-6 del [FM 2-22.3](https://irp.fas.org/doddir/army/fm2-22-3.pdf), con la página de Wikipedia como atajo: fijarse en que son dos ejes independientes y en que el 1 pide confirmación de otra fuente. Para los estimadores de tráfico, [Jansen et al. (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9140287), con [SparkToro (2022)](https://sparktoro.com/blog/which-3rd-party-traffic-estimate-best-matches-google-analytics/) al lado: fijarse en el tamaño del sitio y en que el ranking se sostiene aunque el nivel esté errado.
