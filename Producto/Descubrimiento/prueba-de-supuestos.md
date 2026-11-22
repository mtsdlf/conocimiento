---
resumen: >-
  La prueba de supuestos desarma una solución en lo que tiene que ser cierto para que funcione y evalúa primero los supuestos más riesgosos con actividades chicas, antes de construir la solución.
estado: borrador
estabilidad: semi
fuentes:
  - "Teresa Torres, Assumption testing (Product Talk, 2023): https://www.producttalk.org/2023/10/assumption-testing/"
  - "David Bland y Alexander Osterwalder, Testing Business Ideas (Wiley, 2019); resumen del editor (vía buscador): https://www.strategyzer.com/library/testing-business-ideas-book-summary"
  - "David Bland, mapeo de supuestos (Strategyzer, vía buscador): https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter"
  - "Ron Kohavi y Stefan Thomke, The Surprising Power of Online Experiments, HBR sep-oct 2017, reimpresión R1705E: https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf"
  - "Kohavi, Deng, Frasca, Walker, Xu y Pohlmann, Online Controlled Experiments at Large Scale, KDD 2013, Tenet 3: https://www.exp-platform.com/Documents/2013%20controlledExperimentsAtScale.pdf"
  - "White, Two MVPs every product manager should know (Mind the Product, 2026-03-19): https://mindtheproduct.com/wizard-of-oz-vs-concierge-testing-behind-the-curtain-or-behind-the-desk/"
  - "LearningLoop, concierge vs Wizard of Oz (vía buscador): https://learningloop.io/blog/concierge-vs-wizard-of-oz"
  - "SitePoint, fake door (vía buscador): https://www.sitepoint.com/7-new-ways-to-test-your-minimum-viable-product/"
  - "Helio/Zurb, sesgo del concierge (vía buscador): https://helio.zurb.com/?p=9294"
  - "Producto/.investigacion/descubrimiento.md"
  - "Producto/.investigacion/posicion-contraria.md (afirmaciones 2 y 5)"
aliases: [assumption testing, testear supuestos, experimentos de descubrimiento, fake door, Wizard of Oz, concierge]
creado: 2026-11-22
revisado:
---

# Prueba de supuestos

La prueba de supuestos desarma una solución en lo que tiene que ser cierto para que funcione y evalúa primero los supuestos más riesgosos con actividades chicas, antes de construir la solución.

Torres define cada prueba como "a structured activity that we do to evaluate the risk in an assumption". Es el método del [descubrimiento](descubrimiento.md): los pasos 7 a 9 del [árbol de oportunidades](arbol-de-oportunidades.md), donde cada solución candidata baja a sus supuestos y estos a sus pruebas.

## Por qué probar antes de construir

Las ideas fallan más de lo que sus autores creen. El KDD 2013 de Kohavi y otros lo llama "Tenet 3: We are poor at assessing the value of ideas", y el artículo de HBR de 2017 agrega que "even experts often misjudge which ones will pay off". Las cifras de éxito de Google, Bing y Microsoft están en la [entrada del tema](../producto.md#la-idea-que-cruza-todo-el-tema).

Esas cifras salen de plataformas con tráfico enorme y productos ya optimizados; en un producto joven la proporción puede ser otra. Para un equipo chico, la lección es calibrar la intuición y no tomar la tasa al pie de la letra. Probar un supuesto es más barato y anterior que un [experimento A/B](../Medicion/experimento-ab.md), que mide una solución ya construida (síntesis del informe de esta base).

## De dónde salen los supuestos

Torres pide generar supuestos de cinco categorías: deseabilidad, viabilidad, factibilidad, usabilidad y ética. Importa menos en qué categoría cae cada uno que cubrir las cinco. Las categorías son los [cuatro riesgos](cuatro-riesgos.md) de Cagan con otro nombre más la ética; la comparación entre escuelas está en esa nota.

Para elegir cuáles probar, Bland propone el mapeo de supuestos: cada supuesto se ubica según cuán importante es para la idea y cuánta evidencia lo respalda. Los más riesgosos son los críticos con poca evidencia (Strategyzer, vía buscador). Torres lo dice así: "Our riskiest assumptions are the assumptions that are critical to the success of our idea." La crítica de Maurya a priorizar en una matriz de 2x2 está en [hipótesis de salto de fe](../../Emprender/Validacion/hipotesis-de-salto-de-fe.md#como-se-priorizan-los-supuestos).

Antes de correr la prueba, Torres recomienda definir qué resultado cuenta como bueno. Lectura de esta base, que Torres no dice así en lo leído: sin ese criterio previo, cualquier resultado se puede leer como éxito.

## Los tipos de prueba

Torres nombra cuatro tipos. Fake door, Wizard of Oz y concierge vienen del campo Lean Startup en general, y solo hay fuentes secundarias que los definan. La columna "Qué riesgo cubre" es lectura de esta base, salvo en el research spike, donde lo dice Torres.

| Prueba | Qué es | Qué riesgo cubre | Fuente |
|---|---|---|---|
| Prueba de prototipo | "activities designed to simulate a moment so that we can evaluate customer behavior" | Valor y usabilidad | Torres |
| Encuesta de una pregunta | Una encuesta de una sola pregunta a clientes | Valor | Torres |
| Minería de datos | "the use of existing data to evaluate the inherent risk in an assumption" | Depende del supuesto | Torres |
| Research spike | "an engineering activity that allows us to evaluate feasibility risk" | Factibilidad | Torres |
| Fake door | Un botón o ítem de menú de una funcionalidad que no existe; se cuentan los clics | Valor, solo como intención | SitePoint, vía buscador |
| Wizard of Oz | La interfaz existe; el trabajo de atrás lo hace una persona a mano | Valor y usabilidad | Mind the Product, 2026 |
| Concierge | Hay algo de back end o motor, pero no interfaz (White); otras fuentes lo distinguen porque el usuario sabe que hay una persona detrás | Valor | Mind the Product, 2026; LearningLoop, vía buscador |

El fake door mide intención de clic, no uso ni pago, y no dice nada de usabilidad ni de factibilidad (inferencia del informe). Es pariente del smoke test que describe [producto mínimo viable](../../Emprender/Validacion/producto-minimo-viable.md), donde también está el concierge como tipo de MVP de una empresa nueva; esa nota lo define como un servicio que se presta a mano, con el segundo criterio de la disputa de abajo y no con el de White. En el concierge, la persona que atiende puede producir falsos positivos o falsos negativos (Helio, vía buscador).

> [!IMPORTANT]
> Wizard of Oz y concierge se distinguen con dos criterios distintos según la fuente.
>
> Por qué parte está construida: White (Mind the Product, 2026) dice "With a Wizard of Oz MVP, you have built a front end, but you are substituting manual work for the back end", y del concierge, "You may have some sort of back end or engine built, but no user interface". La regla de uso: "I don't have my back end yet, but I have a screen I want to test out" es Wizard of Oz; "I want to test my back end system but I don't have a screen to connect it to" es concierge.
>
> Por lo que sabe el usuario: otras fuentes, como LearningLoop (vía buscador), los separan según si el usuario sabe que hay una persona detrás. En el Wizard of Oz no lo sabe; en el concierge sí.
>
> Es una disputa de definición y ninguna fuente se equivoca. Al nombrar una prueba conviene decir cuál de los dos criterios se usa.

## La biblioteca de Bland

*Testing Business Ideas* (Bland y Osterwalder, 2019) organiza los experimentos por costo, tiempo y fuerza de la evidencia. El resumen de Strategyzer cita 43 tipos; otra fuente habla de 44, y la discrepancia no se resolvió. No se pudo confirmar que fake door, Wizard of Oz o concierge figuren ahí con esos nombres.

El método de Bland nace en el Lean Startup y prueba ideas de negocio. Torres prueba supuestos de una solución dentro de un producto que ya existe. Ese límite con el tema Emprender es lectura de esta base.

## Cuántas pruebas hacen falta

> [!IMPORTANT]
> Kohavi y Thomke concluyen que hay que correr una cantidad enorme de experimentos: "companies need to kiss a lot of frogs". Torres propone tres soluciones por oportunidad y pruebas chicas cada semana. Los dos coinciden en que la intuición falla, pero no en el volumen. La escala de Bing no está al alcance de un equipo chico (lectura de esta base), y ninguna fuente dice cuántas pruebas semanales hacen falta. Con poco tráfico, además, las pruebas cuantitativas no tienen potencia (blog de proveedor, vía buscador); que ahí pesen más las cualitativas y los prototipos es lectura de esta base.

> [!NOTE]
> Sin fuente todavía: una fuente primaria que defina fake door, Wizard of Oz y concierge (Ries, Nielsen Norman Group); datos de cuántas pruebas por semana hacen los equipos chicos; y tasas de éxito de experimentos en productos con poco tráfico.

## Qué leer

Torres, [Assumption testing](https://www.producttalk.org/2023/10/assumption-testing/), y los capítulos de supuestos de *Continuous Discovery Habits*, con las cinco categorías y la regla de definir el buen resultado antes de probar. Bland y Osterwalder, *Testing Business Ideas*, por la biblioteca de experimentos ordenada por costo y fuerza de evidencia. Para la evidencia de por qué probar, Kohavi y Thomke, HBR 2017, la sección "Build a Large-Scale Capability", y el KDD 2013, "Tenet 3".
