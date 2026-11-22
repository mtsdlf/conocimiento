---
resumen: >-
  Los roles de producto son los cargos que se reparten las decisiones sobre qué construir y por qué: product manager, Product Owner, product ops y product marketing, entre otros. Lo que hace cada uno depende de tres cortes que se cruzan: el rol formal, la actividad y el modelo de equipo.
estado: borrador
estabilidad: semi
fuentes:
  - "Ken Schwaber y Jeff Sutherland, The Scrum Guide (2020), sección Product Owner: https://scrumguides.org/scrum-guide.html"
  - "Ben Horowitz, Good Product Manager/Bad Product Manager (a16z, fechada 15 de junio de 2012): https://a16z.com/good-product-manager-bad-product-manager/"
  - "Marty Cagan, Product vs. Feature Teams (SVPG, 2019): https://www.svpg.com/product-vs-feature-teams/ ; Transformed FAQ: https://svpg.com/transformed-faq"
  - "Will Larson, notas sobre Melissa Perri, Escaping the Build Trap (2018): https://lethain.com/notes-escaping-the-build-trap/"
  - "Melegati et al., Product managers in software startups: A grounded theory, IST 174:107516 (2024), solo metadatos: https://doi.org/10.1016/j.infsof.2024.107516 ; https://zenodo.org/records/10070156"
  - "Maglyas, Nikula y Smolander, What are the roles of software product managers? An empirical investigation, JSS 86(12):3071-3090 (2013), solo metadatos: https://researchr.org/publication/MaglyasNS13/bibtex"
  - "Empirical Software Engineering (2022), problemas de software product management, solo metadatos: https://link.springer.com/doi/10.1007/s10664-022-10134-5"
  - "Melissa Perri y Denise Tilles, Product Operations (2023), según el sitio de las autoras: https://melissaperri.com/book"
  - "Lenny's Newsletter, Product management theater (Marty Cagan), según el buscador: https://www.lennysnewsletter.com/p/product-management-theater-marty"
  - "Pragmatic Institute Framework, según resúmenes: https://pragmaticinstitute.com/framework"
  - "Teresa Torres, Adopting Continuous Product Discovery (2017), según secundarias: https://www.producttalk.org/2017/07/adopting-continuous-product-discovery/"
  - "Jason Fried, posteo de 2016 en Medium, según el buscador: https://medium.com/@jasonfried/469234e3d5bf ; Skift, Airbnb CEO Brian Chesky: I Never Called it Founder Mode (2024): https://skift.com/2024/09/21/airbnb-ceo-brian-chesky-i-never-called-it-founder-mode/"
  - "Producto/.investigacion/organizacion-y-fundamentos.md"
  - "Producto/.investigacion/vistazo.md"
  - "Producto/.investigacion/posicion-contraria.md"
aliases: [roles de producto, product manager, PM, product owner, PO, product ops, product marketing, PMM]
creado: 2026-11-22
revisado:
---

# Roles de producto

Los roles de producto son los cargos que se reparten las decisiones sobre qué construir y por qué: product manager, Product Owner, product ops y product marketing, entre otros. Lo que hace cada uno depende de tres cortes que se cruzan: el rol formal, la actividad y el modelo de equipo.

El mismo cargo cambia de contenido según la empresa. Melegati y coautores (2024) describen el rol de product manager en startups como "multidisciplinary and ill-defined, dependent on the context" (según el abstract). Por eso un organigrama no alcanza para entender quién decide. Es parte de la vertical [Organización](organizacion.md).

## Rol, actividad y modelo

Cada fuente del campo mira el trabajo de producto desde un eje distinto, y los tres ejes se cruzan.

| Corte | Qué define | Fuente |
|---|---|---|
| Rol formal | Una responsabilidad dentro de un equipo: el Product Owner responde por el valor y el backlog | Scrum Guide 2020 |
| Actividad | Las tareas del dominio, como estrategia, planificación o lanzamiento, sin asignarlas a un cargo | ISPMA, Pragmatic Institute |
| Modelo de equipo | Qué se le delega al equipo, y con eso qué hace el product manager | Cagan (SVPG) |

Para saber qué hace una persona con un cargo de producto hay que responder tres preguntas: qué rol formal tiene, qué actividades le tocan y en qué modelo de equipo trabaja. Un "PM" de un [equipo de funcionalidades](equipo-empoderado.md) hace otro trabajo que uno de un equipo empoderado, aunque la tarjeta diga lo mismo.

## El Product Owner de Scrum

El Scrum Guide 2020 define el rol así: "The Product Owner is accountable for maximizing the value of the product resulting from the work of the Scrum Team." Además gestiona el Product Backlog: desarrolla y comunica el Product Goal, crea y ordena los ítems y los mantiene visibles. Puede delegar ese trabajo, pero sigue siendo responsable, y es una persona, no un comité (paráfrasis del extracto). El Product Goal "describes a future state of the product which can serve as a target for the Scrum Team to plan against".

El Guide no habla de descubrimiento, de estrategia ni de viabilidad de negocio. Define una responsabilidad dentro de un equipo, no un cargo en la empresa. Que el Product Owner y el product manager sean la misma persona es una convención de cada empresa. Esa lectura sale del texto del Guide; no se encontró una fuente primaria que compare los dos roles.

## El product manager según quién lo describa

Ben Horowitz escribió "A good product manager is the CEO of the product" y "Good product managers crisply define the target, the 'what' (as opposed to the how)." La página de a16z lleva fecha del 15 de junio de 2012 y un aviso: "This document was written 15 years ago and is probably not relevant for today's product managers." La fecha de 1996 que suele circular no se pudo verificar.

Cagan define el rol por el tipo de equipo. En un equipo de funcionalidades, "the product manager role is mainly project manager, and partly (unskilled) designer". En un equipo empoderado, "the product manager is explicitly responsible for ensuring value and viability". Pasar de uno a otro, según su FAQ de *Transformed* vista por el buscador, cambia las responsabilidades y no las suma.

> [!NOTE]
> Sin fuente todavía: los hallazgos de los estudios empíricos sobre el rol. Maglyas, Nikula y Smolander (2013) y un estudio de 2022 en Empirical Software Engineering (10 entrevistas, 89 encuestados, 95 problemas en 7 áreas) solo se vieron por sus metadatos. Melegati et al. (2024) tiene texto abierto y es el recurso para leer entero: la sección de resultados.

## Product manager y project manager

La confusión más común es entre los dos "PM". Perri, según las notas de Larson, los separa por la pregunta que contesta cada uno: el project manager es dueño del cuándo, y el product manager, del qué y el porqué. Cagan dice que en un equipo de funcionalidades la diferencia desaparece: "The feature-team product manager job is fundamentally about project management." Un proyecto tiene alcance y fecha; un producto, un problema que sigue (ver [Qué es producto](../Fundamentos/que-es-producto.md)).

## Product ops

Product operations es el soporte del trabajo de producto. Perri y Tilles, en *Product Operations* (2023), le dan tres pilares según el sitio de las autoras: "Data and Insights; Customer and Market Insights; and Process and Governance". Otras fuentes llaman al tercero "Process and Practices". Cagan, según un resumen de Lenny's Newsletter, critica que muchos puestos de product ops y de Product Owner hacen trabajo de relleno, al que llama "theater".

## Product marketing

Product marketing lleva el producto al mercado: posicionamiento y lanzamiento. Según resúmenes, Cagan recomienda mantenerlo separado de product management. El marco de Pragmatic Institute cubre los dos en 37 cuadros y 7 categorías, sin asignar las actividades a un cargo. El [posicionamiento](../../Marketing/Propuesta/posicionamiento.md) se estudia en Marketing, y el [lanzamiento](../Planificacion-y-entrega/lanzamiento.md) en Planificación y entrega.

> [!NOTE]
> Sin fuente todavía: el límite entre product manager y product marketing manager, el rol de CPO, y el product designer como cargo. Ninguna fuente primaria leída los trata.

## Empresas sin product manager

El rol no es obligatorio. Jason Fried escribió en 2016 que Basecamp no tiene un rol dedicado de product management: la visión sale de un grupo chico y los equipos de cada ciclo se dirigen solos (según el buscador). Según la prensa, en 2023 Brian Chesky anunció que Airbnb eliminaba el rol tradicional de PM y lo fusionaba con marketing; el original no se verificó. Son casos sueltos y no estudios, y Basecamp es un producto único con un equipo chico.

## Qué leer

Melegati et al. (2024), la sección de resultados, para lo que hacen los product managers reales. El Scrum Guide 2020, sección "Product Owner", por el párrafo de responsabilidad y la nota sobre delegar. Y Cagan, "Product vs. Feature Teams", para comparar qué responde el product manager en cada tipo de equipo.
