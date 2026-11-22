---
resumen: >-
  Los equipos empoderados y el descubrimiento continuo (Cagan, Torres, Perri) son la columna de esta base; Shape Up, los marcos formales (ISPMA, Pragmatic Institute), el liderazgo por visión del fundador y la experimentación a escala son el contraste. Solo la experimentación tiene estudios con método; las demás escuelas se sostienen con opinión de practicantes y casos.
estado: borrador
estabilidad: semi
fuentes:
  - "Marty Cagan, Product vs. Feature Teams (SVPG, 29-ago-2019): https://www.svpg.com/product-vs-feature-teams/"
  - "Marty Cagan, Coaching Founder Mode (SVPG): https://svpg.com/coaching-founder-mode"
  - "Paul Graham, Founder Mode (septiembre de 2024): https://paulgraham.com/foundermode.html"
  - "Ryan Singer, Shape Up, cap. 1, cap. 2, cap. 8 y apéndice 2: https://basecamp.com/shapeup/0.3-chapter-01"
  - "Product Talk, glosario de Continuous Discovery (Torres): https://www.producttalk.org/glossary-discovery-continuous-discovery/"
  - "Jeff Patton, Dual-track development: https://www.jpattonassociates.com/dual-track-development/"
  - "ISPMA, Software Product Management Body of Knowledge: https://ispma.org/bok/"
  - "Pragmatic Institute Framework: https://pragmaticinstitute.com/framework (resumen)"
  - "Scrum Guide 2020: https://scrumguides.org/scrum-guide.html"
  - "DORA, capacidad team experimentation: https://dora.dev/capabilities/team-experimentation/"
  - "John Cutler, A Cagan Critique: https://cutlefish.substack.com/p/a-cagan-critique"
  - "Marty Cagan, The Moral Case for the Product Model (SVPG): https://www.svpg.com/the-moral-case-for-the-product-model/"
  - "Jeremiah Lee, Spotify vs Fitbit: Marty Cagan's false premise and false cause fallacy: https://www.jeremiahlee.com/posts/failed-squad-goals/comments/spotify-vs-fitbit/ (resumen)"
  - "NN/g, Teams aren't empowered: https://www.nngroup.com/articles/teams-arent-empowered/"
  - "Kohavi y Thomke, The Surprising Power of Online Experiments, HBR (2017), reimpresión R1705E: https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf"
  - "Producto/.investigacion/organizacion-y-fundamentos.md, secciones 2.2 y 3.2; Producto/.investigacion/posicion-contraria.md, afirmaciones 3 y 4; Producto/.investigacion/estrategia.md, secciones 1 y 2; Producto/.investigacion/planificacion-y-entrega.md, secciones 2, 3 y 5"
aliases: [escuelas de producto, corrientes de gestión de producto, product schools of thought, founder mode vs empowered teams, Shape Up vs Scrum]
creado: 2026-11-22
revisado:
---

# Escuelas de producto

Los equipos empoderados y el descubrimiento continuo (Cagan, Torres, Perri) son la columna de esta base; Shape Up, los marcos formales (ISPMA, Pragmatic Institute), el liderazgo por visión del fundador y la experimentación a escala son el contraste. Solo la experimentación tiene estudios con método; las demás escuelas se sostienen con opinión de practicantes y casos.

Las escuelas discuten tres cosas: quién decide qué se construye, cómo se planifica el trabajo y qué cuenta como prueba. Se leen mejor con [Fuentes de producto](fuentes-de-producto.md) al lado, que da el peso de cada tipo de evidencia.

## Qué sostiene cada escuela

| Escuela | Qué sostiene | Autores | Evidencia hallada |
|---|---|---|---|
| Equipos empoderados (SVPG) | El equipo recibe problemas, no listas, y se mide por resultados | Cagan, Jones | Posición de practicante; DORA da evidencia parcial sobre autonomía para experimentar |
| Descubrimiento continuo | Contacto semanal del equipo con clientes, con un trío de producto | Torres; Patton para las dos vías | Definición de la autora; sin estudio comparativo |
| Orientada a resultados | Salir de la "build trap": dejar de medir funcionalidades entregadas | Perri, Seiden | Libros de practicantes, leídos por resúmenes; Seiden no se investigó |
| Shape Up | Apetito en lugar de estimación, ciclos de seis semanas, apuestas | Singer (Basecamp) | Experiencia de una empresa; sin estudio |
| Marcos formales | Dividir el dominio en actividades y competencias | ISPMA (Kittlaus, Fricker); Pragmatic Institute; AIPMM | Estudios académicos sobre adopción de ISPMA, solo por metadatos; AIPMM sin fuente |
| Scrum | Un product owner ordena el backlog y responde por el valor | Schwaber, Sutherland | Guía normativa, sin estudio de resultados en el informe |
| Escala (SAFe) | Roles y cadencias para muchos equipos | Scaled Agile | Solo se leyó su página de WSJF (ver [Priorización](../Planificacion-y-entrega/priorizacion.md)); los roles y cadencias no se investigaron |
| Founder mode | El fundador decide en detalle y saltea niveles | Graham (2024); Jobs y Chesky como ejemplos | Ensayo con anécdotas |
| Datos y experimentación | Las ideas se prueban, no se creen | Kohavi y coautores | Experimentos controlados a gran escala |

El product-led growth aparece a veces como escuela de producto, pero es una forma de adquirir clientes: vive en [Growth y product-led growth](../../Marketing/Canales/growth-y-product-led-growth.md).

## La columna y por qué se eligió

Cagan define el equipo empoderado (que él llama *product team*) por su propósito: "to solve problems in ways our customers love, yet work for our business", medido por "outcomes (rather than output)" y "empowered to figure out the best way to solve the problems they've been asked to solve". El equipo de funcionalidades, en cambio, recibe "a prioritized list that is called the roadmap". La versión a fondo está en [Equipo empoderado](../Organizacion/equipo-empoderado.md).

La base la toma como columna porque, en su lectura (ninguna fuente lo dice así), se apoya en la afirmación con más evidencia del campo: la mayoría de las ideas no mejora lo que se quería mejorar (Kohavi y Thomke, 2017; ver la [entrada del tema](../producto.md)). Esa evidencia justifica probar antes de construir. No prueba que un equipo empoderado rinda más que uno de funcionalidades: eso no lo midió nadie. Cagan mismo, en "The Moral Case for the Product Model", no ofrece datos y recomienda pilotos.

La evidencia más cercana es de DORA, que mide desempeño de entrega de software y no resultados de negocio. Los tres componentes de experimentación de equipo que identifica están en [lo que mide DORA](../Organizacion/equipo-empoderado.md#lo-que-mide-dora).

## Las cuatro disputas

> [!IMPORTANT]
> Empoderamiento contra founder mode. Graham (2024) sostiene que el fundador debe decidir los detalles y saltear niveles, en un ensayo basado en anécdotas y sin datos. Cagan responde que empoderar no es delegar sin mirar y que pide mejor gestión, no menos. Las dos posiciones son opinión de practicante, con la misma calidad de evidencia; las citas y la respuesta de Chesky están en [founder mode](../Organizacion/equipo-empoderado.md#founder-mode-el-fundador-en-los-detalles).

> [!IMPORTANT]
> Roadmap, Shape Up o backlog. Para Cagan, el roadmap como lista de funcionalidades con fechas es el sello del equipo de funcionalidades. Shape Up no tiene roadmap largo ni backlog: "We don't rethink our roadmap every two weeks", y en la betting table "there's no "grooming" or backlog to organize"; si un proyecto se pasa, "by default it doesn't get an extension". Scrum, en cambio, pone a un product owner a ordenar el backlog. *Product Roadmaps Relaunched* y Pragmatic mantienen el roadmap como herramienta de comunicación por temas o resultados. Ninguna posición tiene estudio comparativo. El desarrollo está en [Roadmap](../Planificacion-y-entrega/roadmap.md) y [Shape Up](../Planificacion-y-entrega/shape-up.md).

> [!IMPORTANT]
> Actividades contra modelo de equipo. ISPMA divide el dominio en cuatro áreas (Product Strategy, Product Planning, Strategic Management, Orchestration) y Pragmatic en 37 cuadros en siete categorías (los nombres varían según la versión del marco; la página actual tiene una "Go-to-Market", donde vive el lanzamiento). Los dos describen qué actividades hay que cubrir, no quién las hace. Cagan define el campo por el modelo de equipo: qué se le delega y contra qué se lo mide. Los cortes chocan en la estrategia: en ISPMA la estrategia corporativa es un insumo externo y la visión es corporativa; en Cagan los líderes de producto responden por la estrategia de producto y la visión es del producto. Ver [Estrategia de producto](../Estrategia/estrategia-de-producto.md).

> [!IMPORTANT]
> Semanal contra seis semanas. Torres pide "weekly touch points with customers by the team building the product". Shape Up trabaja en ciclos de seis semanas, con dos de "cool-down", y, según el informe de investigación, el moldeado ("shaping") lo hacen una o dos personas antes de la apuesta, no todo el equipo cada semana. También según el informe, Shape Up decide cómo acotar y cuándo apostar, pero no cómo descubrir qué problema vale la pena; las dos lecturas son del informe, no de Singer. Las dos cadencias salen de la práctica de sus autores, sin comparación medida.

## Las críticas a la columna

Las críticas a la columna también son opinión: Cutler y Lee le reprochan a Cagan aprender solo de los casos ganadores, y NN/g sostiene que en organizaciones grandes las dependencias compartidas achican lo que un equipo decide. Las citas están en [Equipo empoderado](../Organizacion/equipo-empoderado.md#lo-que-mide-dora).

Basecamp muestra otro camino: funciona sin un product manager dedicado, un caso que está en [empresas sin product manager](../Organizacion/roles-de-producto.md#empresas-sin-product-manager). El propio Shape Up advierte que sus prácticas "are scale-dependent".

> [!NOTE]
> Sin fuente todavía: un estudio con método que compare equipos empoderados con equipos de funcionalidades, Shape Up con Scrum, o liderazgo del fundador con equipos que descubren; la lectura de SAFe y de AIPMM; y el libro de Seiden.
