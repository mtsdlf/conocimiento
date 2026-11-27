---
resumen: >-
  El mantenimiento centrado en la confiabilidad (RCM) es un método para decidir qué mantenimiento necesita cada equipo partiendo de su función: qué tiene que hacer, de qué maneras puede dejar de hacerlo, qué consecuencias tiene cada falla y qué tarea, si alguna, la previene o la detecta a tiempo. Elige entre los tipos de mantenimiento: lo que sale de él, para cada modo de falla, es una tarea de la estrategia o la decisión de no hacer ninguna.
estado: borrador
estabilidad: estable
fuentes:
  - "Nowlan y Heap, Reliability-Centered Maintenance, United Airlines para el Departamento de Defensa de EE.UU., 29 de diciembre de 1978, DTIC ADA066579, secs. 1.2, 2.3, 2.4, 2.8 y cap. 3 (copia de la Wayback Machine del PDF de DTIC; la URL original, apps.dtic.mil/sti/pdfs/ADA066579.pdf, da 403): https://web.archive.org/web/2020/https://apps.dtic.mil/sti/pdfs/ADA066579.pdf"
  - "NASA, Reliability Centered Maintenance Guide for Facilities and Collateral Equipment, copia de febrero de 2000, sec. 1.2 y sec. 2.4.5, fig. 2-4: https://everyspec.com/NASA/NASA-General/download.php?spec=NASA_RCM_GUIDE_2000.030306.pdf"
  - "Reliable Media, «The Six Failure Patterns: Nowlan and Heap Explained», 1 de septiembre de 2026, actualizado el 13 de octubre de 2026: https://reliamag.com/topics/guides/six-failure-patterns-nowlan-heap/"
  - "SAE JA1011, Evaluation Criteria for Reliability-Centered Maintenance (RCM) Processes, ficha oficial (revisión de agosto de 2009; la norma es paga y no se leyó): https://www.sae.org/standards/content/ja1011_200908/"
  - "Moubray, «The Case Against Streamlined RCM», Reliabilityweb, que cita la sec. 5 de JA1011 (las siete preguntas; leído vía herramienta de resumen): https://reliabilityweb.com/articles/entry/the_case_against_streamlined_reliability_centered_maintanance"
  - "Wikipedia, Reliability-centered maintenance (según su resumen): https://en.wikipedia.org/wiki/Reliability-centered_maintenance"
  - "Wikipedia, Failure mode and effects analysis (según su resumen): https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis"
  - "Klutke, Kiessler y Wortman, «A critical look at the bathtub curve», IEEE Transactions on Reliability, 2003 (no leído): http://ieeexplore.ieee.org/document/1179819/"
  - "Moubray, capítulo 1 de Reliability-centred Maintenance (extracto publicado en Plant Maintenance Resource Center; texto de la figura 1.5, leído vía herramienta de resumen): http://www.plant-maintenance.com/RCM-intro.shtml"
  - "Activos-y-mantenimiento/.investigacion/verificacion-estrategia.md (2026-11-27)"
  - "Oxmaint, página sobre activos de aeropuertos (reparto distinto de los patrones; vía buscador, no leída): https://oxmaint.com/industries/aviation-management/why-airport-asset-age-fails-reliability-predictor-best-cmms"
  - "AvWeb, The Savvy Aviator #47, Reliability-Centered Maintenance, part 1 (vía buscador, no leída): https://avweb.com/features_old/the-savvy-aviator-47-reliability-centered-maintenance-part-1/"
  - "Activos-y-mantenimiento/.investigacion/estrategia-y-fundamentos.md (componente D, 2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/tercera-ronda.md (Nowlan y Heap, 2026-11-27)"
aliases: [mantenimiento centrado en la confiabilidad, RCM, reliability-centered maintenance, reliability-centred maintenance, RCM2, mantenimiento centrado en la fiabilidad, patrones de falla, failure patterns, curvas de Nowlan y Heap, curva de la bañera, bathtub curve, FMEA, AMEF, análisis de modos y efectos de falla, failure mode and effects analysis, SAE JA1011]
creado: 2026-11-27
revisado:
---

# Mantenimiento centrado en la confiabilidad

El mantenimiento centrado en la confiabilidad (RCM) es un método para decidir qué mantenimiento necesita cada equipo partiendo de su función: qué tiene que hacer, de qué maneras puede dejar de hacerlo, qué consecuencias tiene cada falla y qué tarea, si alguna, la previene o la detecta a tiempo. Elige entre los tipos de mantenimiento: lo que sale de él, para cada modo de falla, es una tarea de la estrategia o la decisión de no hacer ninguna.

Para cada modo de falla de un equipo, el resultado es una de las opciones de la [estrategia de mantenimiento](estrategia-de-mantenimiento.md): un [preventivo](mantenimiento-preventivo.md) por edad, una tarea de [mantenimiento por condición](mantenimiento-por-condicion.md), dejar fallar o cambiar el diseño (lectura de la base). Conviene empezar por los equipos de mayor [criticidad](../Registro-de-activos/criticidad.md), porque el análisis lleva tiempo (criterio de la base).

## De la aviación de los sesenta a la norma

El RCM nació en las aerolíneas. Según la NASA, el análisis de la política de mantenimiento de la aviación de fines de los sesenta y principios de los setenta mostró que «a strong correlation between age and failure rate did not exist and the basic premise of time based maintenance was false for the majority of equipment». Estudios del Departamento de Defensa y de varias centrales nucleares lo confirmaron.

El texto fundador es *Reliability-Centered Maintenance*, de F. Stanley Nowlan y Howard F. Heap, de United Airlines, publicado para el Departamento de Defensa de EE.UU. el 29 de diciembre de 1978. Se leyó en una copia de la Wayback Machine del PDF de DTIC (el sitio de DTIC rechaza la descarga directa). Según el resumen de Wikipedia, los militares de EE.UU. lo adoptaron a mediados de los setenta, la industria nuclear comercial en los ochenta, y John Moubray encabezó desde fines de los ochenta la variante RCM2.

La SAE publicó la norma JA1011. Según la ficha oficial de la SAE, la primera edición salió el 1 de agosto de 1999 y la vigente es la revisión del 26 de agosto de 2009; Wikipedia dice 1998, y la ficha de la SAE no lo confirma. Wikipedia resume su fin como fijar «the minimum criteria that any process should meet before it can be called RCM», y Moubray cita su texto: «This standard presents criteria against which a process may be compared». El TPM y la ISO 55000 están en [fundamentos de activos y mantenimiento](../Fundamentos/fundamentos-de-activos-y-mantenimiento.md).

## Las siete preguntas

JA1011 ordena el análisis en siete preguntas, que según Moubray hay que responder en ese orden. El texto de la norma es pago y no se leyó; Moubray cita las preguntas de su sección 5, y esta es la traducción de la base:

1. ¿Cuáles son las funciones del activo y sus estándares de desempeño deseados, en su contexto operativo actual?
2. ¿De qué maneras puede dejar de cumplir sus funciones (fallas funcionales)?
3. ¿Qué causa cada falla funcional (modos de falla)?
4. ¿Qué pasa cuando ocurre cada falla (efectos de falla)?
5. ¿De qué manera importa cada falla (consecuencias de falla)?
6. ¿Qué se debe hacer para predecir o prevenir cada falla (tareas proactivas e intervalos)?
7. ¿Qué se debe hacer si no se encuentra una tarea proactiva adecuada (acciones por defecto)?

La pregunta 1 parte de qué tiene que hacer la bomba, no de qué mantenimiento lleva. Por ejemplo (inventado por la base), si el estándar es mover 50 metros cúbicos por hora, una bomba que mueve 40 ya falló, aunque siga andando. Según la lectura de la base, la séptima pregunta deja entrar dejar fallar, rediseñar o buscar una falla oculta.

## La lógica de decisión de Nowlan y Heap

El informe de 1978 es la fuente de la lógica que lleva de la consecuencia a la tarea. Parte de que lo que manda en toda decisión de mantenimiento no es la falla de una pieza sino sus consecuencias para el equipo entero. Las agrupa en cuatro categorías: de seguridad, operativas («an indirect economic loss as well as the direct cost of repair»), no operativas («only the direct cost of repair») y de falla oculta («no direct impact, but increase the likelihood of a multiple failure»). Define la falla funcional como «the inability of an item (or the equipment containing it) to meet a specified performance standard» y la falla potencial como «an identifiable physical condition which indicates a functional failure is imminent». Una función oculta es la que «will not be evident to the operating crew during the performance of normal duties».

Todas las tareas de mantenimiento programado se reducen a cuatro formas: inspección a intervalos para encontrar fallas potenciales (tarea «a condición»), reparación a una edad límite, descarte a una vida límite, e inspección de un elemento de función oculta para encontrar fallas funcionales (búsqueda de fallas ocultas). Una tarea tiene que ser aplicable (que el elemento tenga las características que la hacen posible) y efectiva (que logre el objetivo que fija la consecuencia). Si la falla tiene consecuencias de seguridad, la tarea tiene que evitarla; si no, se mide en términos económicos, y solo vale si cuesta menos que lo que evita. Los elementos de función oculta que no admiten otra tarea reciben la búsqueda de fallas. Donde falta información, el diagrama de decisión da respuestas por defecto que protegen al equipo hasta que haya datos, y un programa de «exploración de edad» junta los datos para revisar las decisiones. Cuando no hay tarea aplicable y efectiva y hay consecuencias de seguridad, recomienda cambiar el diseño; si no, no asignar tarea hasta tener más información. Sobre la seguridad, la sección 1.2 dice que en los diseños modernos «very few items fall into this category».

## Los seis patrones de falla

La figura más citada del RCM tiene seis curvas de probabilidad de falla según la edad del componente. La Exhibit 2.13 de Nowlan y Heap muestra las seis curvas, derivadas de análisis de confiabilidad hechos por United Airlines durante varios años, con una barra que reparte el total de componentes analizados. El texto del informe da 4 % para A, 6 % para A y B juntos, 5 % para C y 89 % para D, E y F juntos; el reparto de B, D, E y F por separado no está escrito en el informe y sale del extracto de Moubray (figura 1.5) y de la figura 2-4 de la NASA, que coinciden. Los patrones de United Airlines son:

| Letra en Nowlan y Heap | Forma de la curva | Componentes de UAL |
|---|---|---|
| A | Bañera: mortalidad infantil alta, tramo plano, desgaste al final | 4 % |
| B | Probabilidad constante o en leve aumento, y desgaste marcado al final (característica de los motores alternativos de avión) | 2 % |
| C | Aumento gradual, sin edad de desgaste identificable (característica de las turbinas de avión) | 5 % |
| D | Baja al principio, sube rápido a un nivel constante | 7 % |
| E | Constante a toda edad | 14 % |
| F | Mortalidad infantil alta y después constante o muy lentamente creciente (particularmente aplicable al equipo electrónico) | 68 % |

El informe dice: «Some 89 percent of the items analyzed had no wearout zone; therefore their performance could not be improved by the imposition of an age limit», y «Only 6 percent of the items studied showed pronounced wearout characteristics (curves A and B)». Los porcentajes de D, E y F (7, 14 y 68) suman ese 89 %; Moubray los da en el texto de su figura 1.5 («4% of the items conformed to pattern A, 2% to B, 5% to C, 7% to D, 14% to E and no fewer than 68% to pattern F») y la NASA en su figura 2-4.

Según estos porcentajes, solo el 11 % de los componentes (A, B y C) muestra relación con la edad; la figura del informe lo rotula «11% might benefit from a limit on operating age». Nowlan y Heap agregan que «just 4 percent of the items fell into this pattern (curve A)», aunque suele suponerse que la bañera representa a la mayoría. Sobre la revisión programada dicen: «In many cases scheduled overhaul actually increases the overall failure rate by introducing a high infant-mortality rate in an otherwise stable system», que la NASA repite.

> [!WARNING]
> Los porcentajes son de componentes de aviones de una aerolínea de los sesenta. Moubray advierte que «The number of times these patterns occur in aircraft is not necessarily the same as in industry», y Reliable Media dice que el 89 % es «not a number you can drop into your own asset register without analysis». El orden de letras cambia según la fuente: en la figura 2-4 de la NASA la bañera es el tipo E y los motores alternativos son el tipo A, mientras que en Nowlan y Heap y en Moubray la bañera es el patrón A. Esta tabla usa las letras de Nowlan y Heap; no se pueden cruzar letras entre fuentes sin mirar la forma de la curva.

La NASA pone tres estudios lado a lado, y el reparto cambia mucho (la figura rotula el segundo «Bromberg 1973»; un resumen de PNNL, laboratorio del Departamento de Energía, cita «Broberg 1973», un informe citado en un libro de L. F. Pau de 1981):

| Forma de la curva | UAL 1968 | Broberg 1973 | Marina de EE.UU. 1982 |
|---|---|---|---|
| Bañera | 4 % | 3 % | 3 % |
| Constante o creciente y desgaste marcado | 2 % | 1 % | 17 % |
| Aumento gradual sin desgaste | 5 % | 4 % | 3 % |
| Baja al principio y sube a constante | 7 % | 11 % | 6 % |
| Constante a toda edad | 14 % | 15 % | 42 % |
| Mortalidad infantil y después constante | 68 % | 66 % | 29 % |

La NASA fecha el estudio de la Marina en 1982 en la figura y en 1983 en el texto, y PNNL lo rotula «MSDP 1993»; la fecha queda sin resolver. En la Marina el desgaste pesa 17 % contra 2 % en UAL, y la mortalidad infantil 29 % contra 68 %. Ninguna fuente dice a qué se debe la diferencia; es probable que dependa del tipo de equipo y de cómo se juntaron los datos (inferencia de la base).

La NASA agrega que los elementos simples, de una sola pieza (neumáticos, álabes de compresor, pastillas de freno, piezas estructurales), suelen tener curvas con desgaste, y que la mayoría de los complejos tiene las otras. Por eso el [preventivo](mantenimiento-preventivo.md) por edad sigue teniendo lugar.

Según el buscador, una página de un proveedor reparte el 89 % de otra manera y da 2 % a A, y una revista de aviación habla de 72 % de componentes no estructurales sin patrón de edad. Ninguna se leyó.

## El FMEA, la herramienta de las preguntas 2 a 5

Las preguntas sobre modos de falla y sus efectos se responden con un análisis de modos y efectos de falla (FMEA, AMEF en castellano). Se arma como una tabla que lista, por cada función, cada modo de falla, su causa, su efecto y su consecuencia (descripción de la base). Su variante con un número de criticidad, el FMECA, está en [criticidad](../Registro-de-activos/criticidad.md).

Según el resumen de Wikipedia, el FMEA empezó con la norma militar de EE.UU. MIL-P-1629 en 1949, lo usaron los contratistas de la NASA a comienzos de los sesenta, la SAE lo publicó como ARP926 en 1967 y la industria automotriz lo tomó a mediados de los setenta. El manual AIAG/VDA de 2019 reemplazó el número de prioridad de riesgo (RPN) por la «Action Priority».

Los modos de falla del FMEA son los que el [historial del equipo](../Registro-de-activos/historial-del-equipo.md) debería codificar al [cerrar cada orden](../Orden-de-trabajo/cierre-de-la-orden.md). El RCM suele quedar fuera del software: entran sus resultados, las tareas y los intervalos del plan. Ambas afirmaciones son inferencia de la base.

## Cautelas sobre las cifras del RCM

Los seis patrones no valen para cualquier flota: la tabla de la NASA muestra que un solo patrón cambia de 68 % a 29 % según el estudio, y Reliable Media y Moubray advierten que los datos son de aviación. Klutke, Kiessler y Wortman revisan la curva de la bañera en IEEE Transactions on Reliability (2003); esta base no los leyó.

> [!NOTE] Sin fuente todavía: las críticas al RCM como método (su costo y su duración en planta, la dependencia de datos de falla, las variantes abreviadas que JA1011 no reconoce). La disputa entre el RCM completo y el simplificado, según Moubray y sus críticos, está en [fundamentos de activos y mantenimiento](../Fundamentos/fundamentos-de-activos-y-mantenimiento.md).
