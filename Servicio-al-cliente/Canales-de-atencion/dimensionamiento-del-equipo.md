---
resumen: >-
  El dimensionamiento del equipo calcula cuántas personas tienen que estar atendiendo en cada franja para cumplir un objetivo de espera, a partir del volumen de contactos y del tiempo medio de atención. En los canales sincrónicos se resuelve con modelos de colas (Erlang C y Erlang A); en el correo el objetivo es de horas y la cuenta cambia.
estado: borrador
estabilidad: estable
fuentes:
  - "Gans, Koole y Mandelbaum (2003), «Telephone call centers: tutorial, review, and research prospects», M&SOM 5(2), 79-141: https://aviman.technion.ac.il/files/References/Gans-Koole-Mandelbaum-CCReview.pdf (leído en parte: secciones 1, 2.3, 2.5, 3, 4.1 y 4.2)"
  - "Koole y Li (2021), planificación de personal en centros de contacto: https://arxiv.org/pdf/2101.10122 (según su resumen)"
  - "Carter, tesis del MIT sobre respuesta por correo y teléfono: https://dspace.mit.edu/handle/1721.1/43832 (según su resumen)"
  - "APQC, Process Classification Framework, categoría «Manage Customer Service» (6.0), 6.2.1, copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/6-manage-customer-service"
  - "Dixon, Freeman y Toman (2010), «Stop Trying to Delight Your Customers», Harvard Business Review, julio-agosto, 116-122: https://beyondphilosophy.com/wp-content/uploads/2013/07/Stop-Trying-to-delight.pdf"
  - "Servicio-al-cliente/.investigacion/canales-y-niveles-de-servicio.md, sección 3"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, secciones 2, 4 (mito 3) y 5"
aliases: [dimensionamiento, dotación, staffing, workforce management, WFM, planificación de personal, nivel de servicio del centro de contacto, service level, telephone service factor, TSF, 80/20, Erlang C, Erlang A, ocupación, occupancy, utilización, utilization, ASA, average speed of answer, velocidad media de respuesta, abandono, abandonment, regla de la raíz cuadrada, square-root staffing]
creado: 2026-11-27
revisado:
---

# Dimensionamiento del equipo

El dimensionamiento del equipo calcula cuántas personas tienen que estar atendiendo en cada franja para cumplir un objetivo de espera, a partir del volumen de contactos y del tiempo medio de atención. En los canales sincrónicos se resuelve con modelos de colas (Erlang C y Erlang A); en el correo el objetivo es de horas y la cuenta cambia.

Es la parte cuantitativa de los [canales de atención](canales-de-atencion.md): el canal fija qué espera tiene sentido, y el dimensionamiento traduce esa espera a personas. El [autoservicio](autoservicio.md) cambia el volumen que entra; las [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md) dicen después si el resultado fue bueno. La copia consultada del marco de APQC lo pone en 6.2.1 «Plan and manage customer service work force», con cuatro pasos: pronosticar el volumen, armar los turnos, seguir la utilización y monitorear la calidad de las interacciones.

## El nivel de servicio del centro de contacto

El objetivo de espera se expresa como **nivel de servicio del centro de contacto**: qué porcentaje de los contactos se atiende antes de un tiempo fijado. Gans, Koole y Mandelbaum lo definen así: «the service level, also called the telephone service factor (TSF), is the fraction of calls whose delay fell below a prespecified "service-level" target. Typically the target is 20 or 30 seconds».

Se escribe como «X% en Y segundos». El «80/20» (80% en 20 segundos) circula como convención de la práctica; el paper no lo da como regla.

> [!NOTE] Sin fuente todavía: una fuente primaria que fije el 80/20 como referencia.

No es lo mismo que el [acuerdo de nivel de servicio](../Niveles-de-servicio/niveles-de-servicio.md), que promete al cliente en cuánto tiempo se responde y se resuelve un caso. Un centro puede atender el 80% en 20 segundos y vencer los casos de su acuerdo, y al revés. Los tres sentidos de «nivel» en el tema están en el [glosario](../Fundamentos/glosario-de-servicio-al-cliente.md).

El nivel de servicio no alcanza solo. La **velocidad media de respuesta** (ASA, average speed of answer) no incluye el tiempo de los que colgaron antes de ser atendidos, y por eso, según Gans y sus coautores, «a reasonably full picture of congestion requires, at a minimum, both ASA and Abn % statistics»: la velocidad de respuesta y el porcentaje de **abandono** juntos.

## Los datos que entran a la cuenta

La cuenta parte de dos números por franja horaria:

- **Volumen** (λ): cuántos contactos llegan por unidad de tiempo. Sale de un pronóstico sobre la historia.
- **Tiempo medio de atención** (E[S]): la conversación más el trabajo posterior que cierra el contacto (este desglose viene de un resumen, no del paper).

Su producto es la **carga ofrecida**, R = λ·E[S], que se mide en Erlangs: cuántas personas estarían ocupadas todo el tiempo si no hubiera esperas ni huecos. Con 120 llamadas por hora y 5 minutos de tiempo medio de atención, la carga es 120 × 5 / 60 = 10 Erlangs (ejemplo de esta base).

La carga es el piso, nunca la dotación. En el modelo de Gans y sus coautores hace falta un número de personas N estrictamente mayor que R. Lo que se agrega por encima de R es lo que compra el nivel de servicio.

## Erlang C: el modelo de base

Erlang C es el modelo de base del dimensionamiento. No tiene en cuenta el bloqueo (la línea ocupada) ni el abandono. Los supuestos habituales del modelo (llegadas al azar, tiempos de atención exponenciales, atención por orden de llegada) no figuran en el informe. Sus fórmulas, según la sección 3 de Gans y sus coautores:

- Ocupación: ρ = R / N.
- Velocidad media de respuesta: ASA = P(Wait > 0) · E[Wait | Wait > 0].
- Nivel de servicio: TSF = P(Wait ≤ T) = 1 − C(N, R) · e^(−Nμ(1−ρ)T), donde C(N, R) es la probabilidad de esperar, μ = 1/E[S] y T es el objetivo en segundos.

Como se sigue de las fórmulas, para dimensionar se prueba con N = R + 1, R + 2… hasta que el TSF cumple el objetivo. Que los supuestos no se cumplan al pie de la letra y el modelo se use igual es lectura de esta base. Supone además un solo tipo de cliente y personas que atienden todas igual.

## Erlang A: los clientes que cuelgan

Erlang A agrega el abandono (la «A» es por abandonment). Cada cliente tiene una **paciencia**, el tiempo máximo que está dispuesto a esperar; si no lo atienden antes, cuelga. El modelo da a la vez el nivel de servicio y el porcentaje de abandono, que es la otra mitad de la foto de la congestión.

## La regla de la raíz cuadrada y la escala

Una aproximación es la regla de la raíz cuadrada: personal = R + β·√R, donde β es un parámetro que fija cuánto personal de seguridad se suma. Según el paper, Erlang ya la describió en 1924. Su ejemplo: con R = 400 y β ≈ 1,68, el personal de seguridad es de unas 34 personas y la utilización queda en 92,2%.

La consecuencia, como lectura de esta base sobre la fórmula, es que el personal de seguridad crece con la raíz de la carga y no con la carga: un centro grande cumple el mismo nivel de servicio con una ocupación más alta que uno chico. Gans y sus coautores describen centros grandes de alto rendimiento donde «Agent utilization levels can average between 90%–95%», cerca de la mitad de los clientes se atiende sin esperar y el abandono es de «1%–2%». En ese régimen, que llaman de calidad y eficiencia a la vez, la ociosidad, la espera y el abandono son de orden 1/√N.

## Ocupación y utilización

El paper distingue dos medidas que se confunden. La **ocupación** es el tiempo atendiendo sobre el tiempo atendiendo más el disponible. La **utilización** del turno (en los reportes que describe, «On Prod %») es la fracción del tiempo conectado en que la persona está atendiendo o disponible. Las pausas y el trabajo fuera del teléfono bajan la utilización diaria a niveles sostenibles, según el paper. El dimensionamiento calcula personas atendiendo; los turnos tienen que agregar lo que se va en pausas, capacitación y ausencias (lectura de esta base).

> [!NOTE] Sin fuente todavía: valores de referencia de ocupación sostenible para una persona que atiende.

## El caso del correo y los canales asincrónicos

En el correo y en muchas mesas de ayuda el contacto se puede guardar y contestar después, y el cálculo cambia de régimen. Gans y sus coautores lo llaman régimen impulsado por la eficiencia: la utilización tiende al 100% y casi todos los contactos esperan. Dan como ejemplos «e-mail response and many help-desk operations». El objetivo pasa de segundos a horas, y lo que se dimensiona, según la lectura de esta base, es cuántas personas hacen falta para que la cola de pendientes no crezca de un día a otro.

La herramienta que vincula la cola con la espera es la ley de Little: el largo medio de la cola es el volumen por la espera media, E[Queue-Length] = λ·E[Wait]. Para el correo, la ley dice que con 200 correos por día y una espera media de 1 día hay unos 200 correos pendientes en la cola (ejemplo de esta base).

> [!NOTE] Sin fuente todavía: un método de dotación para correo y canales asincrónicos leído en una fuente propia (hay una tesis del MIT y un trabajo de Koole y Li, conocidos solo por su resumen).

En 2003 el paper decía que «no analytical model has yet been dedicated to truly multimedia contact centers».

## Cómo lo usa un sistema

Para dimensionar, el sistema tiene que guardar por contacto la hora de llegada, la de atención, la de fin y el trabajo posterior, y marcar los abandonos con el tiempo que esperaron. Con eso se arma por franja el volumen, el tiempo medio de atención, el nivel de servicio, la velocidad media de respuesta y el abandono (lectura de esta base sobre los reportes que describe el paper en su sección 2.3).

## Dónde falla el dimensionamiento

Falla por el pronóstico: un volumen mal estimado da una dotación mal calculada aunque la fórmula sea exacta. Falla cuando se dimensiona con Erlang C un canal con mucho abandono, porque el modelo no lo ve.

Y falla cuando el tiempo medio de atención, que es un dato de entrada, se convierte en objetivo. Dixon, Freeman y Toman dicen que los centros, «overly focused on managing call time», ignoran el esfuerzo del cliente a lo largo de varios contactos, y que la causa más grande de esfuerzo es tener que volver a llamar. La evidencia sobre si bajar el tiempo de atención empeora la resolución al primer contacto es débil en las dos direcciones. La lectura de esta base: el tiempo medio de atención sirve para dimensionar y sirve mal para medir la calidad; cómo se mide la calidad está en [métricas de atención](../Calidad-del-servicio/metricas-de-atencion.md).
