---
resumen: >-
  Un producto es lo que atiende un equipo que dura frente a un problema que sigue ahí; un proyecto se define por un alcance y una fecha y termina al entregarse; un servicio entrega valor con trabajo de personas en cada entrega. La distinción viene de argumentos de practicantes (Fowler, Cagan, Perri), no de estudios.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, Products Over Projects (2019): https://martinfowler.com/articles/products-over-projects.html"
  - "Marty Cagan y Chris Jones, The Product Model in Traditional IT (SVPG): https://svpg.com/the-product-model-in-traditional-it"
  - "Marty Cagan, Product vs. Feature Teams (SVPG, 29-ago-2019): https://www.svpg.com/product-vs-feature-teams/"
  - "Will Larson, notas sobre Perri, Escaping the Build Trap (O'Reilly, 2018): https://lethain.com/notes-escaping-the-build-trap/"
  - "UXmatters, reseña de Escaping the Build Trap (2021): https://www.uxmatters.com/mt/archives/2021/08/book-review-escaping-the-build-trap.php (resumen)"
  - "McKinsey, The bottom-line benefit of the product operating model: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-bottom-line-benefit-of-the-product-operating-model (cifras por buscador)"
  - "Planview, informe 2024: https://newsroom.planview.com/new-planview-research-confirms-product-operating-model-drives-better-business-performance/ (resumen)"
  - "AppUnite, A lot Needs to Change in Outsourcing to Software Agencies: https://appunite.notion.site/A-lot-Needs-to-Change-in-Outsourcing-to-Software-Agencies-61c5eac64f7443f9878cb43cf057e87a (resumen)"
  - "BCG, Benefits of agile outsourcing (2021): https://www.bcg.com/publications/2021/benefits-of-agile-outsourcing (resumen)"
  - "Producto/.investigacion/estrategia.md, sección 0; Producto/.investigacion/vistazo.md, sección 2; Producto/.investigacion/organizacion-y-fundamentos.md, sección 2.1"
aliases: [product vs project, producto vs proyecto, producto vs servicio, qué es un producto digital, products over projects]
creado: 2026-11-22
revisado: 2026-11-22
---

# Qué es producto

Un producto es lo que atiende un equipo que dura frente a un problema que sigue ahí; un proyecto se define por un alcance y una fecha y termina al entregarse; un servicio entrega valor con trabajo de personas en cada entrega. La distinción viene de argumentos de practicantes (Fowler, Cagan, Perri), no de estudios.

> [!NOTE]
> Sin fuente todavía: una definición formal de "producto" con texto literal. La que usa la [entrada del tema](../producto.md) es una síntesis de esta base sobre Fowler, Cagan y Perri.

## Producto, proyecto y servicio

Fowler define el modo producto por el tipo de equipo que lo trabaja: "Product-mode instead uses durable, ideate-build-run teams working on a persistent business issue." En el modo proyecto, la plata se asigna a un alcance definido de antemano y el equipo suele disolverse al entregar. Cagan agrega que el financiamiento por proyecto está "designed for predictability, but undermine[s] outcomes", y que la TI tradicional se manejó como centro de costo mientras el modelo de producto está "designed for technology as a profit center".

Los equipos empoderados también hacen proyectos, aclara Cagan. Cambia cómo se planifica, se descubre y se entrega, y el trabajo se mide contra [resultados](../Estrategia/resultados-y-entregables.md) en lugar de entregables.

Perri separa producto de servicio por el trabajo humano, según las notas de lectura de Larson. Un producto entrega valor una y otra vez sin trabajo humano nuevo en cada entrega. Un servicio depende de personas para entregar valor, aunque esté automatizado en parte. Una reseña de su libro le atribuye además una definición amplia: producto es "essentially any user experience that a customer would pay for—whether a physical product, virtual product, or service". Las dos lecturas vienen de fuentes secundarias distintas; la distinción que sirve es la operativa, cuánto trabajo humano cuesta cada entrega.

| | Producto | Proyecto | Servicio |
|---|---|---|---|
| Se define por | Un problema que persiste (Fowler) | Un alcance definido de antemano (Fowler) | Personas que entregan valor (Perri) |
| El equipo | Dura e idea, construye y opera (Fowler) | Suele disolverse al entregar (Fowler) | Trabaja en cada entrega (Perri) |
| Se mide por | Resultados (Cagan) | Previsibilidad (Cagan: el financiamiento por proyecto está pensado para ella) | Sin fuente todavía |

La tabla ordena lo que dicen Fowler, Cagan y Perri; el armado es de esta base. El gestor de proyecto es dueño del cuándo; el product manager, del qué y el porqué (Perri, según Larson).

## Lo que no prueba nadie

Fowler admite que no trae datos cuantitativos: su caso descansa en razonamiento, anécdotas y la recomendación de pilotear. Las cifras que circulan a favor son correlaciones de consultoras y vendedores de herramientas.

> [!IMPORTANT]
> Según el buscador (el informe no se pudo abrir), McKinsey reporta que las empresas más maduras en el modelo operativo de producto tuvieron "60 percent greater total returns to shareholders" y "16 percent higher operating margins" que la mitad inferior, con un índice de madurez propio. Es correlación; una lectura posible de esta base (no de McKinsey) es que las empresas que ganan más pueden permitirse organizarse así. Planview, que vende el marco de Kersten, dice que las empresas de élite usan el modelo de producto el doble que las de bajo desempeño. No se encontró un estudio revisado por pares ni causal que compare organizaciones por producto con organizaciones por proyecto.

## Qué cambia en una consultora que vende proyectos

Una consultora de software que construye para clientes vende alcance: el contrato fija qué se entrega y cuándo, aunque adentro trabaje con equipos ágiles. Vive en el modo proyecto del lado de la venta: el cliente compra entregables, y el resultado del negocio del cliente no lo controla quien construye. Es una inferencia de esta base sobre las fuentes de arriba.

Una agencia de software le respondió a Cagan que las agencias prefieren trabajo con alcance cerrado y que el mercado lo refuerza. Señaló además un conflicto: satisfacer al cliente que contrata no es lo mismo que servir a los usuarios de su producto (resumen de la respuesta de AppUnite). BCG (2021) recomienda contratos que permitan equipos empoderados y responsables de resultados, con el cliente reteniendo los roles de product owner y de líder técnico (resumen).

> [!NOTE]
> Sin fuente todavía: un texto de Cagan sobre agencias y consultoras, y una fuente que trate el caso en que quien paga (el cliente) y quien usa (sus usuarios) son personas distintas.

El caso toca varias partes del tema, y cada una lo trata donde le corresponde:

- el roadmap cuando el cliente paga por fechas y alcance: [Roadmap](../Planificacion-y-entrega/roadmap.md#el-roadmap-cuando-el-cliente-paga-por-fechas-y-alcance);
- cómo cobra una consultora y quién carga con el riesgo, con los estudios de contratos de precio fijo y de tiempo y materiales: [Pricing y empaquetado](../Monetizacion/pricing-y-empaquetado.md#como-cobra-una-consultora-o-una-agencia);
- cómo se miden resultados cuando el contrato se cumple con entregables: [Resultados y entregables](../Estrategia/resultados-y-entregables.md#donde-no-alcanza-consultoras-y-contratos);
- qué fuentes leer: [Bibliografía de producto](bibliografia-de-producto.md#consultora-de-software).

## Los nombres vecinos y dónde vive cada uno

Los roles cercanos se confunden porque comparten la palabra "producto". La tabla da la línea de cada uno según las fuentes del informe y dónde se trata en la base. Las definiciones de SVPG llegan por resúmenes; las de product marketing, project manager y CPO no tienen fuente primaria leída.

| Nombre | Qué es | Dónde vive en la base |
|---|---|---|
| Product management | Responde por que el producto sea valioso y viable para el negocio; decide qué construir y por qué (SVPG, resumen) | [Roles de producto](../Organizacion/roles-de-producto.md) |
| Product owner | Una responsabilidad de Scrum: "accountable for maximizing the value of the product resulting from the work of the Scrum Team", dueño del backlog (Scrum Guide 2020) | [Roles de producto](../Organizacion/roles-de-producto.md) |
| Product design | Diseño de interacción y visual; atiende el riesgo de usabilidad (resumen secundario) | [UX](../../UX/ux.md) |
| Product strategy | Elige dónde jugar y cómo ganar; en ISPMA es un área propia | [Estrategia de producto](../Estrategia/estrategia-de-producto.md) |
| Product ops | Soporte al equipo: datos, conocimiento de cliente y mercado, procesos (Perri y Tilles, 2023, resumen) | [Roles de producto](../Organizacion/roles-de-producto.md) |
| Product marketing | Salida al mercado: posicionamiento y lanzamiento; Cagan recomienda separarlo de product management (resumen) | [Lanzamiento](../Planificacion-y-entrega/lanzamiento.md) y [posicionamiento](../../Marketing/Propuesta/posicionamiento.md) |
| Project manager | Dueño del cuándo de un proyecto (Perri, según Larson) | Esta nota |

Cagan marca la frontera entre product manager y project manager: en un equipo de funcionalidades, "The feature-team product manager job is fundamentally about project management." En un equipo empoderado, "the product manager is explicitly responsible for ensuring value and viability." La diferencia entre los dos tipos de equipo está en [Equipo empoderado](../Organizacion/equipo-empoderado.md).

Producto termina donde empiezan tres temas vecinos. El [encaje producto-mercado](../../Emprender/Crecimiento/encaje-producto-mercado.md) y el [producto mínimo viable](../../Emprender/Validacion/producto-minimo-viable.md) son de Emprender. El product-led growth como canal de adquisición está en [Growth y product-led growth](../../Marketing/Canales/growth-y-product-led-growth.md).

## Leer a Fowler y a Cagan juntos

Fowler, "Products Over Projects", en la parte sobre qué se pierde al financiar proyectos, y Cagan, "The Product Model in Traditional IT". Conviene notar que los dos son argumentos sin estudios y que ninguno trata el caso de quien construye para otro.
