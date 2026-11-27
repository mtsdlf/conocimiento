---
resumen: >-
  Los niveles de soporte ordenan quién atiende un caso según cuánto sabe: el nivel cero es el autoservicio, el primer nivel recibe y resuelve lo conocido, el segundo toma lo que requiere especialistas y el tercero llega a quien hace el producto. El enjambre (swarming) es la alternativa que reemplaza el pase de nivel en nivel por pedir ayuda a quien sabe, con evidencia que publica sobre todo quien la promueve.
estado: borrador
estabilidad: semi
fuentes:
  - "Consortium for Service Innovation, «Intelligent Swarming 101»: https://www.serviceinnovation.org/intelligent-swarming-101/ (de quien promueve el modelo)"
  - "Consortium for Service Innovation, Intelligent Swarming Practices Guide, introducción: https://library.serviceinnovation.org/Intelligent_Swarming/Practices_Guide (solo índice y presentación)"
  - "Consortium for Service Innovation, «Why Intelligent Swarming»: https://library.serviceinnovation.org/Intelligent_Swarming/Practices_Guide/15_Why_Intelligent_Swarming (leído en parte)"
  - "Consortium for Service Innovation, caso Akamai (2022): https://library.serviceinnovation.org/Case_Studies/Intelligent_Swarming_Case_Studies/05_2022_Akamai (autoinformado)"
  - "Consortium for Service Innovation, casos de swarming (Ping Identity 2024, BMC 2010, Autodesk, Cisco): https://library.serviceinnovation.org/Case_Studies/Intelligent_Swarming_Case_Studies (según resúmenes del buscador)"
  - "Salesforce, «What is case swarming» y material de PagerDuty sobre el mismo tema: https://www.salesforce.com/blog/what-is-case-swarming/ (según resúmenes del buscador; comercial)"
  - "Gobierno de Ontario, GO-ITS 37, Enterprise Incident Management Process: https://www.ontario.ca/document/go-its-37-enterprise-incident-management-process (según citas del buscador; la página dio 403)"
  - "Servicio-al-cliente/.investigacion/caso-y-escalamiento.md, componente 6"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, mito 6 y glosario"
aliases: [niveles de soporte, nivel de soporte, primer nivel, segundo nivel, tercer nivel, nivel cero, tier, support tiers, L1, L2, L3, tiered support, modelo por niveles, enjambre, swarming, intelligent swarming]
creado: 2026-11-27
revisado:
---

# Niveles de soporte

Los niveles de soporte ordenan quién atiende un caso según cuánto sabe: el nivel cero es el autoservicio, el primer nivel recibe y resuelve lo conocido, el segundo toma lo que requiere especialistas y el tercero llega a quien hace el producto. El enjambre (swarming) es la alternativa que reemplaza el pase de nivel en nivel por pedir ayuda a quien sabe, con evidencia que publica sobre todo quien la promueve.

Es la forma más común de organizar el escalamiento funcional que describe la entrada de [Escalamiento](escalamiento.md). «Nivel» acá es nivel de soporte (en inglés, tier): no tiene que ver con el nivel de servicio del centro de contacto ni con el acuerdo de nivel de servicio, que están en [Niveles de servicio](../Niveles-de-servicio/niveles-de-servicio.md). El [glosario](../Fundamentos/glosario-de-servicio-al-cliente.md) separa los tres sentidos.

## Del nivel cero al tercero

No se encontró una fuente neutral que defina cada nivel. Lo que sigue es la práctica común, tal como la usan las mesas de ayuda y los adoptantes de ITIL; el estándar de Ontario habla de «support tier» sin definir cuántos ni cuáles.

| Nivel | Quién atiende | Qué resuelve |
|---|---|---|
| Cero | El cliente solo, con el [autoservicio](../Canales-de-atencion/autoservicio.md): base de conocimiento, preguntas frecuentes, portal, bot | Lo que ya está escrito y el cliente encuentra |
| Primero | Quien recibe el contacto en la mesa de ayuda o el centro de contacto | Lo conocido, con guiones y la base de conocimiento; registra y clasifica el [caso](../Caso/caso.md) |
| Segundo | Especialistas de un producto o de un tipo de caso | Lo que requiere diagnóstico, acceso o conocimiento que el primer nivel no tiene |
| Tercero | Quien hace el producto: ingeniería, desarrollo, el fabricante | Lo que requiere cambiar el producto o saber cómo está hecho por dentro |

> [!NOTE] Sin fuente todavía: una definición neutral (norma o libro) de los niveles cero a tercero. La tabla describe la práctica común. El caso de Akamai del Consortium confirma que en la práctica existen un nivel 2 y un pase posterior a «Ingeniería de Producto».

El modelo funciona como un embudo: cada nivel resuelve lo que puede y pasa el resto. Por eso el primer nivel se mide por la [resolución al primer contacto](../Calidad-del-servicio/metricas-de-atencion.md), y cada nivel puede tener un tiempo asignado, pasado el cual el caso sube («Each support tier may be allocated a certain amount of time to resolve the incident», según el estándar de Ontario).

## Cómo se modela en un sistema

Como lectura de esta base: en el modelo por niveles, cada nivel es un grupo o una cola, y escalar es reasignar el caso a otra cola. El sistema guarda el grupo actual, el dueño, el historial de pases y el tiempo en cada grupo, que es lo que permite ver dónde se acumulan los casos. Las reglas de pase suelen ser por tiempo, por tipo de caso o por prioridad, como se ve en [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md).

En el enjambre el caso no cambia de cola: quien lo tiene pide ayuda, y la ayuda se registra al lado del caso. La guía del Consortium organiza la práctica en tres partes: Connect (perfiles de las personas y del trabajo, con un modelo de clasificación para encontrar a quién preguntar), Collaborate y Recognize (la reputación de quien ayuda). Un sistema que lo soporte necesita saber quién sabe qué, no solo a qué grupo pertenece.

## El enjambre como alternativa

El Consortium for Service Innovation, que también desarrolló KCS, describe Intelligent Swarming como una organización «dynamic, fluid, adaptive» basada en una red sin límites, donde las interacciones son «emergent based on the work to be accomplished». Intelligent Swarming es marca de servicio del Consortium, y sus miembros son empresas de soporte de tecnología.

Su crítica al modelo por niveles tiene un umbral explícito. Según su guía, los niveles son eficientes «if the majority (95% or more) of issues are simple and known»; en entornos de complejidad media o alta, «the tiered model has serious flaws» y «creates organizational silos and handoffs/escalations that inhibit the exchange of information». El Consortium aclara que el enjambre no es solo para lo difícil («difficult is in the eye of the beholder») y que hacen falta límites para asegurar que «the work is getting done».

La evidencia publicada es de casos de empresas, informados por ellas mismas a través del Consortium:

- **Akamai (2022)**, en menos de dos trimestres: 20% menos de nivel de esfuerzo en los casos resueltos en enjambre frente a los escalados al nivel 2; 7% menos de pases a Ingeniería de Producto; un pedido de ayuda tardó en promedio 16 minutos en recibir respuesta, frente a casi 2 horas para que se aceptara un pedido de escalamiento. La empresa ya usaba KCS desde 2017. El caso no da tamaños de muestra ni define «esfuerzo», y compara dos medidas distintas (respuesta a un pedido de ayuda contra aceptación de un escalamiento).
- **Ping Identity (2024)**, en las primeras 10 semanas: tiempo medio de cierre 15% menor, cumplimiento del acuerdo 13% mayor, pendientes 25% menos, primera respuesta 75% más rápida y resolución de los casos más complejos 81% más rápida. Se leyó por resúmenes del buscador, no el texto del caso.
- **BMC (2010)**: satisfacción de 81% a 87%, según un resumen del buscador.

> [!IMPORTANT]
> No hay un estudio independiente, con grupo de control o que controle la complejidad de los casos, que compare los niveles con el enjambre. Toda la evidencia a favor del enjambre la publica quien lo promueve, y la reproducen proveedores de software que venden herramientas para hacerlo. Los niveles tampoco tienen un estudio a favor: su respaldo es que están en todas partes. Un proveedor de alertas, con interés comercial, reconoce que los niveles «can be highly effective for handling less severe issues and one-off questions», y los resúmenes de proveedores recomiendan modelos mixtos.

Como lectura de esta base: la elección depende de qué parte de los casos son simples y conocidos. Una mesa de ayuda de un comercio, con consultas repetidas, está cerca del 95% que el propio Consortium da como terreno de los niveles. El soporte de un producto técnico complejo es donde se publicaron los casos de enjambre.

## Dónde fallan los niveles

Fallan por los pases. Cada nivel que no resuelve agrega una espera y una nueva explicación del cliente, y el Consortium señala los silos que cada equipo optimiza por su lado. Fallan también cuando el primer nivel escala de más para cuidar su tiempo medio de atención, o de menos para cuidar su resolución al primer contacto: los dos incentivos están en [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md).

El enjambre falla, según el mismo Consortium, si no tiene límites: sin ellos no queda claro quién es dueño del caso ni si el trabajo se hace. Y depende de saber quién sabe qué, un dato que el modelo por niveles no necesita guardar.
