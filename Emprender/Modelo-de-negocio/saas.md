---
resumen: >-
  El SaaS (software como servicio) vende acceso a una herramienta que corre en los servidores del proveedor, por una suscripción periódica. Deja márgenes brutos altos y, según la explicación habitual de practicantes, cuesta poco servir a un cliente más, pero conseguir cada cliente cuesta caro y se recupera en meses, así que crece con pérdidas al principio y vive de que los clientes se queden.
estado: borrador
estabilidad: estable
fuentes:
  - "David Skok, SaaS Metrics 2.0 (forEntrepreneurs, con actualización de 2016): https://www.forentrepreneurs.com/saas-metrics-2/"
  - "Salesforce, resultados del 4T del ejercicio 2025 (anexo 99.1 del 8-K): https://www.sec.gov/Archives/edgar/data/0001108524/000110852425000002/crm-q4fy25xexhibit991.htm"
  - "Fernando Suarez, Michael Cusumano y Steven Kahl (2013), Management Science 59(2):420-435 (según su abstract): https://econpapers.repec.org/RePEc:inm:ormnsc:v:59:y:2013:i:2:p:420-435"
  - "Aswath Damodaran, márgenes y múltiplos por industria (2026-01-05): https://pages.stern.nyu.edu/~adamodar/pc/datasets/margin.xls"
  - "Bain & Company, Per-seat software pricing isn't dead (octubre de 2025), según resumen: https://www.bain.com/insights/per-seat-software-pricing-isnt-dead-but-new-models-are-gaining-steam/"
  - "BCG, Rethinking B2B software pricing in the era of AI (agosto de 2025), según resumen: https://www.bcg.com/publications/2025/rethinking-b2b-software-pricing-in-the-era-of-ai"
  - "Alex Wilhelm, Are software companies good businesses?, TechCrunch (17 de julio de 2023): https://techcrunch.com/2023/07/17/are-software-companies-good-businesses/"
  - "Emprender/.investigacion/modelos-saas-y-servicios.md"
  - "Emprender/.investigacion/modelos-plataforma-y-tipologia.md"
  - "Emprender/.investigacion/oportunidades-y-modelos-contraria.md"
aliases: [SaaS, software as a service, software como servicio, software por suscripción, software solo, MRR, ARR, CAC payback, negative churn]
creado: 2026-11-22
revisado:
---

# SaaS

El SaaS (software como servicio) vende acceso a una herramienta que corre en los servidores del proveedor, por una suscripción periódica. Deja márgenes brutos altos y, según la explicación habitual de practicantes, cuesta poco servir a un cliente más, pero conseguir cada cliente cuesta caro y se recupera en meses, así que crece con pérdidas al principio y vive de que los clientes se queden.

Es el modelo de software solo en la comparación de [modelos de negocio de software](modelos-de-negocio-de-software.md): en la tipología de Hagiu y Wright, un proveedor de insumos que le vende la herramienta al negocio y no toca a los clientes de ese negocio (inferencia de esta base). Qué unidad se cobra (asiento, uso o resultado) y qué entra en cada plan está en [pricing y empaquetado](../../Producto/Monetizacion/pricing-y-empaquetado.md); regalar una parte para vender el resto, en [freemium y prueba gratuita](../../Producto/Monetizacion/freemium-y-prueba-gratuita.md).

## Cómo cobra: ingreso recurrente

El SaaS cobra una suscripción que se renueva sola. Skok, inversor, distingue dos negocios según el contrato: los de contratos mayormente mensuales, que se miden por el ingreso mensual recurrente (MRR), y los de contratos anuales, que se miden por el anual (ARR) y por el valor del contrato. La diferencia importa para la caja cuando el contrato anual se cobra por adelantado (lectura de esta base).

La suscripción como modelo de ingreso, con el caso de Netflix, está en [modelo de negocio](modelo-de-negocio.md#modelos-de-ingreso).

## Cómo crece: el costo de adquisición y la retención

Según los practicantes, servir a un cliente más cuesta poco; conseguirlo, no. Skok lo resume en tres umbrales de practicante, sin muestra publicada:

- **Recuperar el costo de adquisición.** «many of the best SaaS businesses are able to recover their CAC in 5-7 months», y la rentabilidad es «anemic» si tarda más de 12.
- **Valor del cliente contra su costo.** «The best SaaS businesses have a LTV to CAC ratio that is higher than 3». Cómo se calculan el LTV y el CAC está en [economía unitaria](../../Marketing/Medicion/economia-unitaria.md).
- **Expansión.** Lo que salva al SaaS de la pérdida de clientes es el «Negative Churn»: que lo que gastan de más los que se quedan supere lo que se pierde con los que se van.

La consecuencia es el valle de caja. Según Skok, los SaaS «face significant losses in the early years (and often an associated cash flow problem)»: cuanto más rápido crecen, más plata ponen antes de recuperarla. Por eso el modelo se lleva bien con capital de riesgo y mal con crecer solo con ingresos propios, salvo que el costo de adquisición sea muy bajo (lectura de esta base; cómo se calcula la pista está en [Finanzas](../Finanzas/finanzas.md)).

## La economía: margen alto, servicios a pérdida

Los SaaS públicos tienen márgenes brutos de 68 % a 80 % en 2025, y el promedio de la industria de software de sistemas y aplicaciones en Estados Unidos es 71,7 % ([márgenes por modelo de negocio](margenes-por-modelo-de-negocio.md)). El costo de ingresos incluye servidores, soporte e implementación; las fuentes leídas no lo desglosan.

Lo que no escala se ve separando las líneas. En el ejercicio 2025 de Salesforce, la suscripción y el soporte dejaron 82,6 % de margen bruto y los servicios profesionales y otros, −10,3 % (cálculo de esta base sobre las cifras publicadas). La lectura de esta base es que esos servicios se venden a pérdida para vender la suscripción. Coincide con el hallazgo de Suarez, Cusumano y Kahl (2013): en empresas de producto de software, sumar servicios baja la rentabilidad hasta que los servicios son la mayoría de las ventas ([detalle](modelos-de-negocio-de-software.md#los-híbridos-software-con-servicios-y-software-con-pagos)).

El mercado lo valúa por múltiplos de ingreso: 11,4 veces las ventas en el promedio de software de sistemas y aplicaciones de Damodaran, una categoría que no aísla el SaaS,, contra 1,5 en servicios de TI. La explicación habitual, la de ingreso recurrente con margen alto y costo marginal bajo, es de practicantes; no se encontró una fuente con método que la pruebe.

## Cómo falla

> [!IMPORTANT]
> Que el SaaS sea el mejor modelo está en discusión.
> - **Margen bruto no es ganancia.** Según un resumen, hay SaaS públicas que declaran ganancia ajustada y pérdida contable por la compensación en acciones. No se encontró una cifra fechada de cuántas pierden plata en términos contables. Lo más cercano: en julio de 2023, 6 de 61 empresas de un índice de software de un fondo tenían flujo de caja libre negativo, según TechCrunch.
> - **La IA y el precio por asiento.** Si el software hace el trabajo de varias personas, cobrar por persona deja de seguir al valor. Según un resumen de su informe, Bain (2025) escribe que «The economics of headcount-based pricing break down when fewer humans are needed to operate the software», y encontró que el 65 % de los proveedores sumó un cargo por uso de IA sobre el asiento y ninguno pasó a cobrar solo por uso o por resultado. BCG (2025) dice que el precio por resultado es de los menos usados porque cuesta acordar qué es un resultado. Las dos son consultoras con interés comercial.
> - **El cliente que no quiere la herramienta.** Un SaaS pide que el cliente aprenda y haga el trabajo. A quien prefiere comprar el trabajo hecho le conviene un [servicio habilitado por tecnología](servicios-habilitados-por-tecnologia.md).

Las métricas de retención neta de ingresos, la regla del 40 y el crecimiento por producto (product-led) no se investigaron con fuente primaria; quedan como hueco.

Para leer más, «SaaS Metrics 2.0» de Skok: fijarse en los gráficos del valle de caja y de recuperación del costo de adquisición, y recordar que es un inversor sin muestra publicada.
