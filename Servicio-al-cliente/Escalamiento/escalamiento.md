---
resumen: >-
  Escalar es pasar un caso que quien lo atiende no puede resolver a alguien que sabe más (escalamiento funcional) o a alguien que puede decidir más (escalamiento jerárquico). La vertical reúne cómo se organiza ese pase en niveles, cuándo el caso pide mandar un técnico y cómo los casos que se repiten se convierten en un problema para atacar su causa.
estado: borrador
estabilidad: estable
fuentes:
  - "Gobierno de Ontario, GO-ITS 37, Enterprise Incident Management Process: https://www.ontario.ca/document/go-its-37-enterprise-incident-management-process (según citas del buscador; la página dio 403)"
  - "APQC, Process Classification Framework, categoría «Manage Customer Service» (6.0), copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/6-manage-customer-service"
  - "ISO 10002:2018, vista previa del editor: https://cdn.standards.iteh.ai/samples/71580/6db527fdda0a42ac8f597ffd406e3509/ISO-10002-2018.pdf (solo el índice de los anexos)"
  - "Gans, Koole y Mandelbaum (2003), «Telephone call centers: tutorial, review, and research prospects», M&SOM 5(2), 79-141, §5: https://aviman.technion.ac.il/files/References/Gans-Koole-Mandelbaum-CCReview.pdf (leído en parte; del §5 solo el índice)"
  - "Consortium for Service Innovation, «Intelligent Swarming 101»: https://www.serviceinnovation.org/intelligent-swarming-101/ (de quien promueve la alternativa)"
  - "ERPNext, Issue: https://docs.frappe.io/erpnext/user/manual/en/support/issue (como evidencia de práctica)"
  - "Servicio-al-cliente/.investigacion/caso-y-escalamiento.md, componentes 5 a 8"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, sección 2 y glosario"
aliases: [escalamiento, escalar, escalation, escalamiento funcional, functional escalation, escalamiento jerárquico, hierarchical escalation, escalada]
creado: 2026-11-27
revisado:
---

# Escalamiento

Escalar es pasar un caso que quien lo atiende no puede resolver a alguien que sabe más (escalamiento funcional) o a alguien que puede decidir más (escalamiento jerárquico). La vertical reúne cómo se organiza ese pase en niveles, cuándo el caso pide mandar un técnico y cómo los casos que se repiten se convierten en un problema para atacar su causa.

Dentro del [Servicio al cliente](../servicio-al-cliente.md), recibe del [Caso](../Caso/caso.md) lo que no se resolvió donde entró y le devuelve la solución, o el aviso de que hay un problema de fondo. Los [Niveles de servicio](../Niveles-de-servicio/niveles-de-servicio.md) le ponen el reloj: el tiempo que corre es una de las razones para escalar. Cuando hace falta una visita, el caso se deriva al servicio de campo, que es del tema Activos y mantenimiento, todavía no armado.

## El campo no trata el escalamiento como categoría propia

Ninguna de las divisiones del campo consultadas tiene al escalamiento como parte de primer nivel. ITIL lo trata como un paso dentro de la gestión de incidentes, según resúmenes de la práctica. La categoría de servicio al cliente de APQC (6.0 en una copia sin versión declarada) no tiene un nodo de escalamiento: el verbo más cercano es «Route», enrutar, dentro del tratamiento de reclamos (6.2.3.2). La ISO 10002 tampoco le da una cláusula, aunque trae un flujograma de escalamiento en su Anexo H. En la literatura de centros de contacto, Gans, Koole y Mandelbaum lo tratan como enrutamiento por habilidades (§5).

Que sea una vertical en esta base es una decisión de la base y no del campo. Se justifica por el lector: quien construye una mesa de ayuda tiene que modelar quién es el dueño del caso en cada momento, a qué grupo pasa, por qué y contra qué reloj.

## Escalamiento funcional y escalamiento jerárquico

La palabra tiene dos sentidos, y un sistema los registra distinto:

- **Funcional**: el caso pasa a un grupo con más conocimiento. El estándar de gestión de incidentes del gobierno de Ontario, que adopta ITIL, lo dice así: «the SDA assigns the incident to a group with more specialized skills. (This is known as functional escalation)». La sigla SDA no se explica en el fragmento leído; por el contexto es quien atiende en la mesa de servicio (lectura de esta base). Es lo que organiza los [niveles de soporte](niveles-de-soporte.md).
- **Jerárquico**: el caso sube a alguien con más autoridad, no con más conocimiento. Según un resumen de ITIL, «hierarchical escalation engages appropriate levels of management». Se escala así, como lectura de esta base, para autorizar una excepción, una compensación o un recurso que el equipo no tiene.

Las dos definiciones salen de adoptantes y resúmenes de ITIL, leídos por citas del buscador; el texto de ITIL 4, que es pago, no se leyó. Valen como «según la práctica de ITIL».

Los dos sentidos pueden darse en el mismo caso. Un reclamo por un producto en garantía puede pasar al especialista para el diagnóstico (funcional) y al supervisor para aprobar un cambio fuera de política (jerárquico). Como lectura de esta base, el funcional cambia quién trabaja el caso y el jerárquico suma a alguien que decide sin sacarle el caso a quien lo trabaja.

## Qué dispara un escalamiento

Las fuentes leídas dan dos disparadores:

1. **El tiempo.** Según el estándar de Ontario, «Each support tier may be allocated a certain amount of time to resolve the incident»; pasado ese tiempo, el caso se escala funcionalmente. Ese tiempo sale del acuerdo que está en [tiempos de respuesta y resolución](../Niveles-de-servicio/tiempos-de-respuesta-y-resolucion.md).
2. **La prioridad.** En una mesa de ayuda de un sistema abierto, cambiar la prioridad de un caso lo escala respecto del acuerdo de nivel de servicio, porque cambia el acuerdo que se le aplica. Cómo se fija la prioridad está en [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md).

El tercer disparador, que quien atiende no sabe resolver, no tiene una regla escrita en las fuentes leídas: lo decide la persona.

> [!NOTE] Sin fuente todavía: criterios generales para decidir cuándo escalar por conocimiento (además del tiempo) y cuándo escalar por autoridad, y qué datos mínimos debe llevar el pase de un nivel a otro.

## Lo que un sistema registra al escalar

Como lectura de esta base, a partir de la práctica de las mesas de ayuda: el caso sigue siendo uno solo y cambia de grupo o de dueño. Lo que importa guardar es quién lo tenía, a quién pasó, cuándo y por qué, para poder medir cuánto tardó cada nivel y cuántos casos rebotan. Un caso que se escala no se cierra y se abre otro: el cliente sigue esperando la misma respuesta, y el reloj del acuerdo sigue corriendo sobre el mismo registro. Los estados y el dueño del caso están en [caso](../Caso/caso.md).

El escalamiento jerárquico, en cambio, suele agregar una aprobación o un aviso, sin mover el caso de cola (lectura de esta base, sin fuente que la sostenga).

## Dónde falla el escalamiento

La crítica más articulada viene de quien promueve una alternativa, el Consortium for Service Innovation. Describe el modelo por niveles como «static, linear, hierarchy-based model» y dice que los procesos lineales de escalamiento «treat every issue the same», que cada equipo optimiza su parte «almost always to the detriment of the customer» y que el resultado es «rework, inefficiency, and frustration». Es una fuente con interés: la alternativa que propone, el enjambre, es marca suya. La discusión con su evidencia está en [niveles de soporte](niveles-de-soporte.md#el-enjambre-como-alternativa).

Como lectura de esta base, falla también cuando nadie mira por qué se escala. Si el mismo tipo de caso sube una y otra vez, el escalamiento resuelve cada uno y deja la causa. Ese es el paso a [problema y causa raíz](problema-y-causa-raiz.md). Y falla cuando el caso sale del tema sin dueño: una visita del técnico que nadie sigue deja al cliente sin respuesta, como se ve en [derivación al técnico](derivacion-al-tecnico.md).

## Qué hay en el escalamiento

- [Niveles de soporte](niveles-de-soporte.md) — del nivel cero (el autoservicio) al tercero, y el enjambre como alternativa, con la evidencia y quién la promueve.
- [Derivación al técnico](derivacion-al-tecnico.md) — cuándo un caso pide una visita y qué pasa del caso a la orden de trabajo del servicio de campo.
- [Problema y causa raíz](problema-y-causa-raiz.md) — de los casos repetidos al problema, el error conocido y la solución provisoria, y el análisis de reclamos de la ISO 10002.
