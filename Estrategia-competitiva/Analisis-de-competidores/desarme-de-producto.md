---
resumen: >-
  El desarme de producto (teardown) es estudiar el producto de un rival pieza por pieza para entender cómo está hecho, qué resuelve bien y cuánto costaría igualarlo. Su artefacto más común en software es la matriz de funcionalidades, que muestra quién ofrece qué y sirve para ver el espacio, no para decidir qué construir.
estado: vigente
estabilidad: semi
fuentes:
  - "TIME (22 de octubre de 1973), Business: Tearing Down the Competition: https://time.com/archive/6841903/business-tearing-down-the-competition/ (leído)"
  - "Nielsen Norman Group, Competitive Usability Evaluations: https://www.nngroup.com/articles/competitive-usability-evaluations/ (leído)"
  - "Umbrex, Teardown Benchmarking and Competitive Cost Analysis: https://umbrex.com/resources/rd-playbooks/the-design-to-value-playbook/teardown-benchmarking-and-competitive-cost-analysis/ (según resumen)"
  - "Munro & Associates, material de teardown benchmarking: https://leandesign.com/benchmarking/ (según resumen; material promocional)"
  - "LogRocket, Product teardown: process and tools: https://blog.logrocket.com/product-management/product-teardown-process-tools/ (según resumen)"
  - "UXPin, Competitive analysis for UX: https://www.uxpin.com/studio/blog/competitive-analysis-for-ux/ (según resumen), y HubSpot sobre la misma práctica"
  - "Blogs de proveedores sobre feature parity (ProdPad, Userpilot, Userjot, Featurebase, Beamer, Nulab, ClickUp), contados como una sola familia de fuentes: https://www.prodpad.com/glossary/feature-parity/ (según resúmenes)"
  - "Canny (2025, Jenna Potter), citas de gestores de producto sobre paridad: https://canny.io/blog/?p=9227 (leído)"
  - "Fleisher y Bensoussan, 1.ª ed. (2007), diapositivas del cap. 5, puntajes FAROUT: https://ptgmedia.pearsoncmg.com/imprint_downloads/ftpress/bookreg/9780131873667/Ch5.pdf (leídas)"
  - "Marvin Lieberman y Shigeru Asaba (2006), Why Do Firms Imitate Each Other?, Academy of Management Review 31(2):366-385 (según resumen)"
  - "J. Scott Armstrong y Green (2007), Competitor-oriented Objectives, International Journal of Business 12(1):117-136: https://mpra.ub.uni-muenchen.de/81674/ (leído; reporta a Lukas y Ferrell 2000)"
  - "Estrategia-competitiva/.investigacion/analisis-de-competidores-1.md"
  - "Estrategia-competitiva/.investigacion/posicion-contraria.md (evidencia transversal sobre copiar e imitar)"
aliases: [teardown, product teardown, desarme, benchmarking de producto, matriz de funcionalidades, feature matrix, feature comparison, paridad de funcionalidades, feature parity]
creado: 2026-11-22
revisado: 2026-11-22
---

# Desarme de producto

El desarme de producto (teardown) es estudiar el producto de un rival pieza por pieza para entender cómo está hecho, qué resuelve bien y cuánto costaría igualarlo. Su artefacto más común en software es la matriz de funcionalidades, que muestra quién ofrece qué y sirve para ver el espacio, no para decidir qué construir.

Es la técnica de la mirada de producto en el catálogo de [perspectivas de análisis](perspectivas-de-analisis.md). Llena las casillas de estrategia actual y capacidades del [perfil del competidor](perfil-del-competidor.md), que Porter llama "inspection of a competitor's products". Qué rivales se desarman sale de la [identificación de competidores](identificacion-de-competidores.md).

## El origen en la industria automotriz

TIME describió la práctica en octubre de 1973. Ford la llamaba "value analysis" e International Harvester "competitive analysis". Cuando salía un vehículo nuevo, los otros fabricantes compraban uno y lo mandaban a una "teardown room", donde lo desarmaban en hasta 15.000 piezas. Los ingenieros estudiaban cada pieza para ver si superaba a la propia y cuánto costaría copiarla.

El ejemplo de la nota: Ford juzgó superior el cilindro maestro de freno de un rival y construyó uno parecido, con dos tornillos en lugar de cuatro. Dos años después, ese diseño apareció en autos de rivales que habían desarmado el Ford. Lo que se buscaba era el costo y el diseño de piezas concretas.

> [!NOTE] Sin fuente todavía: cuándo empezó la práctica; TIME la describe en 1973, pero no la fecha. Tampoco se leyó literatura académica sobre ingeniería inversa competitiva.

En hardware la práctica sigue, con fuentes comerciales. Según un resumen de su material, Munro & Associates, una consultora del rubro, afirma que el 70 % de los costos queda fijado por el diseño del producto; es promoción y la cifra no está verificada. Una guía de Umbrex advierte dos cosas, según un resumen: el producto que se desarma tiene que seguir a la decisión que el desarme apoya, y comparar una versión recortada del rival con la completa propia exagera las diferencias de costo.

## Cómo se desarma un producto de software

No hay una fuente primaria con método para el desarme de software. Un blog de producto (LogRocket) lo describe como la disección sistemática de un producto para analizar sus funcionalidades, sus decisiones de diseño, su experiencia de uso y su estrategia, según un resumen. El método más sólido que se leyó es la evaluación competitiva de usabilidad de Nielsen Norman Group. Para ver el producto por dentro hace falta una cuenta de prueba propia; cómo se abre y qué no se hace con ella está en [cuenta de prueba y automatización](cuenta-de-prueba-y-automatizacion.md#cuándo-hace-falta-una-cuenta-de-prueba).

NN/g distingue dos formas. En la revisión competitiva, un experto examina productos parecidos. En el test competitivo, usuarios hacen tareas clave en el producto propio y en los ajenos, "typically" 2 o 3 sitios por participante. La guía recomienda concentrarse en 2 a 4 competidores y alternar el orden entre participantes, porque el que se prueba segundo se beneficia de lo aprendido en el primero. Avisa que es caro. El método completo, con métricas y tamaño de muestra, está en [evaluación competitiva](../../UX/Evaluacion/evaluacion-competitiva.md), del tema UX.

Pasos para desarmar el producto de un rival de software, armados por esta base a partir de esas fuentes:

1. Escribí qué decisión apoya el desarme: qué construir, qué no, dónde diferenciarse.
2. Elegí de 2 a 4 rivales y la misma versión o plan para todos; no compares su plan gratis con tu plan completo.
3. Definí las tareas del cliente que importan para esa decisión, por ejemplo, publicar el primer producto o cobrar la primera venta en una plataforma de tiendas online.
4. Recorré cada tarea en cada producto: pasos, tiempos, trabas, qué resolvieron distinto.
5. Anotá lo que funcionó y lo que no, no solo si la funcionalidad existe.
6. Volvé a la decisión del paso 1 y escribí qué cambia.

NN/g insiste en ese paso 5: los detalles de "what worked and what didn't" importan más que los porcentajes. Fleisher y Bensoussan tienen dos técnicas cercanas, el análisis de línea de productos y el benchmarking, cuyos capítulos no se leyeron.

## La matriz de funcionalidades

La matriz pone a los rivales en columnas y las funcionalidades en filas, y marca quién tiene qué. HubSpot y UXPin la recomiendan para ver quién ofrece qué y encontrar dónde diferenciarse. Sugieren de 3 a 5 competidores directos más 1 o 2 indirectos, y completar la revisión en 1 a 2 semanas, según un resumen.

La matriz mide presencia, no calidad ni uso. Un tilde en "carrito abandonado" dice que la función existe, no si los comerciantes la usan ni si recupera ventas. Por eso sirve para ver el espacio (qué existe, qué falta y dónde está todo el mundo amontonado) y no como lista de pendientes.

## Paridad que cuesta clientes y paridad por inercia

La trampa de la paridad es construir lo que otro tiene porque lo tiene. La describen sobre todo blogs de proveedores de software de producto, que acá cuentan como una sola fuente de opinión. Según esos resúmenes, la presión suele venir de la dirección y apunta a borrar la ventaja del rival, no a una necesidad del usuario. El error de base es suponer que los clientes del rival usan o quieren esa función. ProdPad propone distinguir paridad de plataforma, de migración y competitiva.

Hay evidencia más sólida en la misma dirección, aunque no es de software. Lukas y Ferrell (2000), según Armstrong y Green (2007), encontraron que las empresas muy orientadas al competidor lanzaban menos productos nuevos y más productos "me-too". El costo de mirar demasiado al rival está en [obsesión por el competidor](obsesion-por-el-competidor.md).

La distinción que importa es entre dos clases de paridad:

| | Paridad que cuesta clientes | Paridad por inercia |
|---|---|---|
| De dónde sale | ventas que se pierden o clientes que se van por la falta | "el rival lo tiene" |
| Cómo se verifica | win/loss, motivos de baja, entrevistas | no se verifica |
| Ejemplo en un SaaS | se pierden contratos grandes por no tener inicio de sesión único | copiar un tablero que el rival lanzó el mes pasado |

Las citas que junta Canny (2025) muestran las dos posiciones. A favor: "If we'll lose a big contract without this feature, we replicate". En contra: "a risky blanket statement that causes bloat by including all the mistakes you made". Es un blog de un proveedor y no trae datos; es opinión de profesionales. La paridad que cuesta clientes se prueba con el [win/loss](analisis-de-ventas-ganadas-y-perdidas.md) y después compite por lugar en la [priorización](../../Producto/Planificacion-y-entrega/priorizacion.md) como cualquier otra oportunidad.

> [!IMPORTANT]
> Seguir al líder puede ser racional. Lieberman y Asaba (2006), según un resumen, distinguen dos familias de razones para imitar: seguir a quien se cree mejor informado, y mantener la paridad o limitar la rivalidad. Los datos sobre pioneros y seguidores, que muestran que entrar después puede rendir, están en [ventaja del primero](../Dinamica-competitiva/ventaja-del-primero.md). Del otro lado, la evidencia de la trampa de la paridad es de práctica: no se encontró un estudio que mida cuántos equipos de producto caen en ella ni cuánto les cuesta.

## Qué leer

No hay un recurso que cubra las dos versiones. TIME (1973) es corto y muestra para qué se desarma: costo y diseño de piezas concretas, no copiar por copiar. Para software, el artículo de NN/g "Competitive Usability Evaluations": fijarse en elegir de 2 a 4 rivales con sentido, definir la pregunta antes, medir tareas y no presencia de funciones, y usar lo encontrado para mejorar el diseño propio.
