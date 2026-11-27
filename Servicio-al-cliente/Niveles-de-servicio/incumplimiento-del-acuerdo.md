---
resumen: >-
  El incumplimiento del acuerdo es lo que pasa cuando un caso supera el tiempo prometido: el aviso antes del vencimiento, el registro del vencimiento y, en algunos contratos, una compensación al cliente. Su contracara es el efecto «watermelon»: el acuerdo se cumple en el tablero mientras el cliente está disconforme.
estado: borrador
estabilidad: semi
fuentes:
  - "Barclay Rae, «Watertight not watermelon service level agreements», HDI SupportWorld, 2020: https://www.thinkhdi.com/library/supportworld/2020/watertight-not-watermelon-service-level-agreements (leído en parte)"
  - "Computer Weekly, «Watermelon SLAs – making sense of green and red alerts»: https://www.computerweekly.com/opinion/Watermelon-SLAs-making-sense-of-green-and-red-alerts (según resumen del buscador; la página dio 403)"
  - "HappySignals, «Watermelon effect»: https://happysignals.com/blog/watermelon-effect (como evidencia de práctica, según su resumen)"
  - "Avasant: https://avasant.com/?p=84703 (según su resumen)"
  - "Dixon, Freeman y Toman (2010), «Stop Trying to Delight Your Customers», Harvard Business Review, julio-agosto, 116-122: https://beyondphilosophy.com/wp-content/uploads/2013/07/Stop-Trying-to-delight.pdf"
  - "ERPNext, Service Level Agreement: https://docs.frappe.io/erpnext/user/manual/en/service-level-agreement (como evidencia de práctica)"
  - "Servicio-al-cliente/.investigacion/canales-y-niveles-de-servicio.md, sección 6"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, sección 4, mito 5"
aliases: [incumplimiento del SLA, SLA breach, vencimiento del SLA, violación del SLA, alerta de vencimiento, créditos de servicio, service credits, penalidades, efecto watermelon, watermelon SLA, SLA sandía, acuerdo de experiencia, XLA, experience level agreement]
creado: 2026-11-27
revisado:
---

# Incumplimiento del acuerdo

El incumplimiento del acuerdo es lo que pasa cuando un caso supera el tiempo prometido: el aviso antes del vencimiento, el registro del vencimiento y, en algunos contratos, una compensación al cliente. Su contracara es el efecto «watermelon»: el acuerdo se cumple en el tablero mientras el cliente está disconforme.

Es la parte de los [niveles de servicio](niveles-de-servicio.md) que se ocupa de lo que sale mal. Los vencimientos los calcula el reloj de [tiempos de respuesta y resolución](tiempos-de-respuesta-y-resolucion.md); lo que se hace con un caso trabado es [escalamiento](../Escalamiento/escalamiento.md); y medir si la atención es buena más allá del acuerdo es de [Calidad del servicio](../Calidad-del-servicio/calidad-del-servicio.md).

## El vencimiento y las alertas

Un caso vence cuando el reloj llega al tiempo prometido sin que ocurra el evento esperado: la primera respuesta o la resolución. El sistema conoce el vencimiento desde que el caso entra, porque lo calcula con el acuerdo, la prioridad y el calendario. Por eso puede avisar antes y no solo después.

La lectura de esta base es que el sistema tiene que registrar cada vencimiento como un hecho del caso, con la fecha, el objetivo que se venció (respuesta o resolución) y por cuánto, y no solo como un porcentaje del mes. El porcentaje sale de esos hechos; al revés no se puede reconstruir qué casos fallaron.

> [!NOTE] Sin fuente todavía: cuándo conviene avisar antes del vencimiento (a qué porcentaje del tiempo, a quién) y qué dispara el vencimiento en el caso (una reasignación, un escalamiento jerárquico, un aviso al cliente).

## Créditos y penalidades

Algunos contratos traducen el incumplimiento en plata: un crédito sobre la próxima factura o una penalidad. Es un tema de dinero, que en esta base pide dos fuentes independientes, y hoy no hay ninguna leída.

> [!NOTE] Sin fuente todavía: cómo se calculan los créditos y las penalidades por incumplimiento, con qué topes y cómo se reclaman. No se dan valores hasta tener dos fuentes independientes.

Si el acuerdo prevé una compensación, el caso decide que corresponde y el comprobante (una nota de crédito) es de los temas Contabilidad y Tesorería, todavía en armado.

## El efecto watermelon: verde por fuera, rojo por dentro

El efecto «watermelon» (sandía) describe un acuerdo que se ve verde en el reporte mientras la experiencia del cliente es roja. Barclay Rae, que escribe para HDI, lo presenta como «a simple, graphical way of showing that many service level agreements (SLAs) are not fit for purpose». Cuenta que usa la imagen desde hace más de diez años, que «initially thought that I'd created the idea myself» y que otros llegaron a lo mismo: el origen del término no está verificado. Según un resumen, la guía de ITIL 4 Foundation describe el efecto.

Las causas que se citan son dos. Según Rae, los acuerdos los define el área técnica sin acordar con el negocio qué resultado importa, y miden componentes por separado y no su efecto combinado. Según notas de proveedores, los acuerdos miden cómo se maneja el trabajo y no si el usuario obtuvo lo que necesitaba. Un caso respondido en 10 minutos y resuelto en 8 horas cumple el acuerdo aunque el cliente haya tenido que llamar tres veces (ejemplo de esta base).

Los remedios que proponen esas mismas notas son medir resultados que el usuario reconoce, recoger los datos de forma independiente de quien es medido y sumar al acuerdo un **acuerdo de experiencia** (XLA, experience level agreement). Casi todas esas fuentes son de proveedores que venden la medición de experiencia.

> [!IMPORTANT]
> No se encontró un estudio con método que mida la brecha entre cumplir el acuerdo y la conformidad del cliente: lo que hay es opinión experta y notas de proveedores. Lo más cercano con datos es de Dixon, Freeman y Toman, que miden otra brecha, entre satisfacción y lealtad: «Twenty percent of the "satisfied" customers in our study said they intended to leave the company in question; 28% of the "dissatisfied" customers intended to stay». No es sobre acuerdos de nivel de servicio.

En la práctica, el efecto se ve cuando el cumplimiento del acuerdo sube y al mismo tiempo suben las reaperturas, los contactos repetidos o las quejas. Por eso el acuerdo se lee junto con las [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md) y las [encuestas de satisfacción](../Calidad-del-servicio/encuestas-de-satisfaccion.md), y no solo (lectura de esta base). Por qué el cliente puede juzgar mal una atención que cumplió lo prometido, desde el lado de sus expectativas, está en el [modelo de las brechas](../../Marketing/Servicio-y-relacion/modelo-de-las-brechas.md).

## Cómo se esconde un incumplimiento

El acuerdo también se puede cumplir en el reporte sin cumplirse en el caso, y eso es una forma del mismo efecto (lectura de esta base). Tres maneras: pausar el reloj con un estado de espera cuando el caso no espera al cliente; dar una primera respuesta automática que detiene el reloj de respuesta sin que nadie haya leído el caso; y cerrar el caso para cortar el reloj de resolución y abrir otro si el cliente vuelve. El sistema puede dificultarlas guardando quién cambió cada estado y vinculando el caso nuevo con el anterior, como se describe en [caso](../Caso/caso.md).

Las [cifras sin fuente y lo que sí dice la evidencia](../Fundamentos/mitos-del-servicio-al-cliente.md) sobre acuerdos cumplidos y clientes conformes están entre los mitos del tema.
