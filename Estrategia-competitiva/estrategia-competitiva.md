---
resumen: >-
  La estrategia competitiva estudia por qué unas empresas ganan más que otras en un mismo mercado: qué tan rentable es la industria, de dónde sale una ventaja que dure, cómo se mueven los rivales y cómo se los analiza. Sirve para decidir dónde y cómo competir antes de diseñar un producto.
estado: vigente
estabilidad: estable
fuentes:
  - "Michael E. Porter, Competitive Strategy, Free Press (1980), cap. 3 A Framework for Competitor Analysis (ver Estrategia-competitiva/.investigacion/analisis-de-competidores-1.md)"
  - "Michael E. Porter (2008), The Five Competitive Forces That Shape Strategy, HBR, enero de 2008, reimpresión R0801E: https://public.dhe.ibm.com/software/data/sw-library/cognos/pdfs/articles/art_the_five_competitive_forces_that_shape_strategy.pdf"
  - "Anita McGahan y Michael Porter (1997), How Much Does Industry Matter, Really?, SMJ 18(S1):15-30: https://ideas.repec.org/a/bla/stratm/v18y1997is1p15-30.html (abstract)"
  - "Vilmos Misangyi, Heather Elms, Thomas Greckhamer y Jeffery LePine (2006), A New Perspective on a Fundamental Debate, SMJ 27:571-590: https://sites.psu.edu/vilmos/wp-content/uploads/sites/35079/2015/10/Misangyi-Elms-et-al.-2006.pdf"
  - "J. Scott Armstrong y Fred Collopy (1996), Competitor Orientation, Journal of Marketing Research 33(2):188-199: https://repository.upenn.edu/marketing_papers/120"
  - "Henry Mintzberg y Joseph Lampel (1999), Reflecting on the Strategy Process, MIT Sloan Management Review: https://sloanreview.mit.edu/article/reflecting-on-the-strategy-process"
  - "Estrategia-competitiva/.investigacion/ (vistazos, informes por vertical y posición contraria, 2026-11-22)"
aliases: [competitive strategy, estrategia de competencia, análisis competitivo, competitive analysis]
creado: 2026-11-22
revisado: 2026-11-22
---

# Estrategia competitiva

La estrategia competitiva estudia por qué unas empresas ganan más que otras en un mismo mercado: qué tan rentable es la industria, de dónde sale una ventaja que dure, cómo se mueven los rivales y cómo se los analiza. Sirve para decidir dónde y cómo competir antes de diseñar un producto.

El tema junta la teoría (Porter, la visión basada en recursos, la rivalidad) con la práctica de analizar competidores, que Porter abre en el capítulo 3 de *Competitive Strategy* (1980). La teoría sola no llega a una decisión sobre un rival concreto, y el análisis sin teoría queda en una planilla de funcionalidades.

Termina donde empieza la [estrategia de producto](../Producto/Estrategia/estrategia-de-producto.md), que elige dónde jugar y cómo ganar con lo que este tema le da, y el [posicionamiento](../Marketing/Propuesta/posicionamiento.md), que decide contra qué alternativas se presenta el producto ante el cliente. La competencia entre plataformas de dos lados está en [Plataformas](../Producto/Plataformas/plataformas.md), del tema Producto.

Los ejemplos del tema son de software, sobre todo de SaaS, el software por suscripción. Los términos que se repiten entre notas, como VRIO o costos de cambio, están en el [glosario](Fundamentos/glosario-de-estrategia-competitiva.md).

## De qué está hecha la estrategia competitiva

Las cuatro partes van de lo más amplio a lo más concreto. La industria fija el piso de rentabilidad; la ventaja explica por qué una empresa queda por encima de ese piso; la dinámica muestra cómo se defiende esa ventaja en el tiempo; y el análisis de competidores aplica todo a rivales con nombre y apellido.

```mermaid
flowchart LR
  I[Análisis de industria] -->|fija el rendimiento medio que| V[Fuentes de ventaja]
  V -->|explican quién queda arriba y por qué, y eso alimenta| D[Dinámica competitiva]
  D -->|anticipa cómo responde el rival en| A[Análisis de competidores]
  A -->|devuelve datos de rivales concretos a| I
  A -->|entrega opciones y riesgos a| E[Estrategia de producto]
```

- [Análisis de industria](Analisis-de-industria/analisis-de-industria.md): las cinco fuerzas y los grupos estratégicos. Se entra para saber si un mercado vale la pena y quiénes compiten de verdad contra quién.
- [Fuentes de ventaja](Fuentes-de-ventaja/fuentes-de-ventaja.md): estrategias genéricas, cadena de valor, recursos y capacidades, los 7 Powers y los costos de cambio. Se entra para saber qué haría difícil copiar a un rival, o al producto propio.
- [Dinámica competitiva](Dinamica-competitiva/dinamica-competitiva.md): acción y respuesta, ventaja del primero, disrupción, océano azul, elegir el terreno y coopetición. Se entra para anticipar qué pasa cuando alguien mueve, o cuando el rival también es socio.
- [Análisis de competidores](Analisis-de-competidores/analisis-de-competidores.md): identificar rivales, perfilarlos, mirarlos desde varias perspectivas, juntar información de forma legal y no engañarse. Es la parte práctica y la más desarrollada.

## La industria importa, pero la empresa importa más

Porter sostiene que la estructura de la industria fija la rentabilidad media de quienes compiten en ella. La visión basada en recursos sostiene que la ventaja sale de lo que cada empresa tiene y otros no pueden copiar. Los dos enfoques se midieron con un mismo método: descomponer las diferencias de rentabilidad entre unidades de negocio.

McGahan y Porter (1997) atribuyen el 19 % de esa varianza a la industria y el 32 % a la unidad de negocio. Rumelt (1991) había encontrado 4 % y 44,2 %, según la tabla de Misangyi et al. (2006). Los estudios no coinciden en las cifras, y Misangyi et al. atribuyen la diferencia "largely" a las técnicas de análisis. Sí coinciden en el orden: la unidad de negocio explica más que la industria en todos los estudios con cifras verificadas, y la industria no es nula. Por eso el tema tiene las dos partes, y ninguna alcanza sola.

Todos esos datos son de empresas grandes, sobre todo de Estados Unidos y de décadas pasadas. No se encontró un estudio equivalente para software.

## Los marcos son listas de preguntas, no predicciones

Las cinco fuerzas, los 7 Powers o el modelo de acción y respuesta de Chen ordenan qué mirar, pero ninguno predice qué va a pasar con un producto. La evidencia es despareja: la visión basada en recursos tiene una crítica de tautología abierta; los 7 Powers no tienen contraste empírico independiente; y el modelo de Chen tiene respaldo parcial. Cada nota dice cuánto respaldo tiene su marco. La regla de uso es tratar lo que sale de un marco como una hipótesis que se verifica con el caso.

## Mirar al rival sin perder de vista al cliente

> [!IMPORTANT]
> Analizar competidores y fijarse como objetivo ganarles son dos cosas distintas, con evidencia distinta. Armstrong y Collopy (1996) encontraron que, en 20 empresas, el objetivo de cuota de mercado se correlacionó negativamente con el retorno sobre la inversión (de -0,37 a -0,54), y que en experimentos más del 40 % de 1016 sujetos sacrificó beneficios por ganarle a un rival. La muestra es chica y no se encontró una réplica independiente. Del otro lado, el meta-análisis de Kirca et al. (2005) asocia la orientación al mercado (cliente más competidor más coordinación) con mejor desempeño, aunque en el texto leído no aparece una cifra separada para el componente competidor. La lectura de esta base: el análisis de competidores es una herramienta para decidir qué hacer por el cliente, no un objetivo. El detalle está en [obsesión por el competidor](Analisis-de-competidores/obsesion-por-el-competidor.md).

## Dónde entra en el diseño de un producto

El análisis de competencia es un paso del medio, entre conocer al cliente y decidir. Cada paso tiene su nota, en este tema o en otro:

0. **La pregunta**: qué se quiere decidir con el análisis. Sin una decisión, la recolección no termina nunca ([ciclo de inteligencia](Analisis-de-competidores/ciclo-de-inteligencia.md)).
1. **El dominio**: cómo funciona la industria por dentro. Es un tema propio por industria, fuera de este; el de tiendas online es [Comercio electrónico](../Comercio-electronico/comercio-electronico.md).
2. **El mercado**: qué abarca ([definición de mercado](../Marketing/Mercado-y-cliente/definicion-de-mercado.md)), cómo se divide ([segmentación](../Marketing/Mercado-y-cliente/segmentacion.md)), su tamaño ([tamaño de mercado](../Emprender/Validacion/tamano-de-mercado.md)) y su estructura ([análisis de industria](Analisis-de-industria/analisis-de-industria.md)).
3. **El cliente**: qué trabajo quiere resolver ([jobs to be done](../Marketing/Mercado-y-cliente/jobs-to-be-done.md)) y cómo se lo investiga ([métodos de investigación](../UX/Investigacion/metodos-de-investigacion.md)).
4. **Los rivales**: quiénes son ([identificación de competidores](Analisis-de-competidores/identificacion-de-competidores.md)).
5. **El análisis por perspectivas**: qué quiere, qué hace y cómo respondería cada uno ([perfil del competidor](Analisis-de-competidores/perfil-del-competidor.md), [perspectivas de análisis](Analisis-de-competidores/perspectivas-de-analisis.md)). El [recorrido de Análisis de competidores](Analisis-de-competidores/analisis-de-competidores.md#el-recorrido-de-la-decisión-al-perfil-de-respuesta) detalla los pasos 4 y 5 y entrega el perfil de respuesta que usan los pasos 7 y 8.
6. **La mirada propia**: dónde se es más fuerte o más débil que cada rival ([análisis propio](Analisis-de-competidores/analisis-propio.md)).
7. **La síntesis**: qué oportunidades quedan y en qué terreno pelear ([árbol de oportunidades](../Producto/Descubrimiento/arbol-de-oportunidades.md), [elegir el terreno](Dinamica-competitiva/elegir-el-terreno.md)).
8. **La decisión**: dónde jugar y cómo ganar ([estrategia de producto](../Producto/Estrategia/estrategia-de-producto.md)), contra qué alternativas presentarse ([posicionamiento](../Marketing/Propuesta/posicionamiento.md)) y qué probar primero ([prueba de supuestos](../Producto/Descubrimiento/prueba-de-supuestos.md)).
9. **El seguimiento**: vigilar a los rivales de forma periódica y no una sola vez ([puntos ciegos](Analisis-de-competidores/puntos-ciegos.md)).

El orden es de esta base, armado a partir de las fuentes de cada paso; ninguna fuente lo da entero.

## Qué leer según lo que tengas que averiguar de la competencia

Si tenés que hacer el análisis completo, seguí los pasos de arriba con el [recorrido de un análisis de competencia](Fundamentos/recorrido-analisis-de-competencia.md), con las acciones, los errores típicos y la plantilla del documento final. Para una tarea puntual:

- Si tenés que averiguar algo de un rival: [ética y legalidad](Analisis-de-competidores/etica-y-legalidad.md) primero, después [fuentes públicas](Analisis-de-competidores/fuentes-publicas.md) y, si cotiza, [lectura de reportes públicos](Analisis-de-competidores/lectura-de-reportes-publicos.md).
- Si tenés que comparar tu producto con el de un rival: [desarme de producto](Analisis-de-competidores/desarme-de-producto.md); la usabilidad se compara con la [evaluación competitiva](../UX/Evaluacion/evaluacion-competitiva.md) de UX.
- Si tenés que anticipar cómo responde un rival a una jugada tuya, como bajar el precio: [acción y respuesta](Dinamica-competitiva/accion-y-respuesta.md) y [precios de la competencia](../Producto/Monetizacion/precios-de-la-competencia.md).
- Si sos socio de una plataforma que también te puede competir, o tenés que decidir si cooperar con un competidor: [coopetición](Dinamica-competitiva/coopeticion.md) y [competencia con la plataforma](../Producto/Plataformas/competencia-con-la-plataforma.md).
- Si tenés que entender el mercado de servicios de software o de desarrollo con IA: [servicios de software y la IA](Analisis-de-industria/servicios-de-software-y-la-ia.md) para la industria y [quién vende desarrollo con IA](Analisis-de-competidores/quien-vende-desarrollo-con-ia.md) para los rivales; el cliente, en [qué le compra una empresa a una consultora de software](../Marketing/Mercado-y-cliente/que-compra-una-empresa-a-una-consultora-de-software.md).
- Si tenés que decidir si entrar a un mercado o cómo pelear contra uno grande: [cinco fuerzas](Analisis-de-industria/cinco-fuerzas.md) y [elegir el terreno](Dinamica-competitiva/elegir-el-terreno.md).

## Orden de lectura

Para quien empieza: esta entrada, después Análisis de competidores, que es lo que se usa, y obsesión por el competidor; por último, las otras tres partes en el orden del diagrama.

- [Fundamentos](Fundamentos/fundamentos-de-estrategia-competitiva.md): escuelas y evidencia, historia, bibliografía por necesidad, fuentes, mitos y glosario.
