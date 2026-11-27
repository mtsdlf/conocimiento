---
resumen: >-
  La cadena de valor es la descomposición de una empresa en las actividades que hace para entregar su producto, para ver en cuáles se genera su costo y en cuáles su diferencia. En Porter es una herramienta de análisis interno, y sirve para comparar actividad por actividad con un rival.
estado: vigente
estabilidad: estable
fuentes:
  - "Michael E. Porter (1985), Competitive Advantage: Creating and Sustaining Superior Performance, Free Press, caps. 2 y 3 (no abierto)"
  - "Institute for Manufacturing, University of Cambridge, Porter's Value Chain: https://www.ifm.eng.cam.ac.uk/research/dstools/value-chain-/ (por resumen)"
  - "Rayport y Sviokla (1995), Exploiting the Virtual Value Chain, HBR 73(6):75-85: https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/32198995 (por resumen)"
  - "Michael E. Porter (2008), The Five Competitive Forces That Shape Strategy, HBR: https://public.dhe.ibm.com/software/data/sw-library/cognos/pdfs/articles/art_the_five_competitive_forces_that_shape_strategy.pdf (leído completo)"
  - "Romney, Steinbart, Mula, McNamara y Tonkin (2013), Accounting Information Systems, edición australasiana, Pearson Australia, cap. 1, figura 1.10 (páginas publicadas, leídas en Procesos-de-negocio/.investigacion/fundamentos.md): https://researchonline.jcu.edu.au/38329/11/38329_Romney_etal_2013_FrontPages.pdf"
  - "Estrategia-competitiva/.investigacion/industria-y-ventaja.md (sección 0 y A3)"
  - "Estrategia-competitiva/.investigacion/fundamentos.md (bibliografía)"
aliases: [value chain, cadena de valor de Porter, Porter's value chain, actividades primarias, actividades de apoyo, cadena de valor virtual, virtual value chain]
creado: 2026-11-22
revisado: 2026-11-22
---

# Cadena de valor

La cadena de valor es la descomposición de una empresa en las actividades que hace para entregar su producto, para ver en cuáles se genera su costo y en cuáles su diferencia. En Porter es una herramienta de análisis interno, y sirve para comparar actividad por actividad con un rival.

Porter la presentó en *Competitive Advantage* (1985). Es la herramienta que baja las [estrategias genéricas](estrategias-genericas.md) a lo concreto: una empresa no es barata o distinta en general, lo es en ciertas actividades. Por eso vive en [Fuentes de ventaja](fuentes-de-ventaja.md) y no en el [análisis de industria](../Analisis-de-industria/analisis-de-industria.md), aunque a veces se la presente junto a las cinco fuerzas: según el informe de esta base, Porter la usa para mirar la empresa por dentro, no la estructura de la industria. Porter (2008) hace el puente cuando dice que las economías de escala existen "in virtually every activity in the value chain".

## Las actividades primarias y las de apoyo

Según resúmenes del libro de 1985, la cadena tiene cinco actividades primarias:

1. Logística interna.
2. Operaciones.
3. Logística externa.
4. Marketing y ventas.
5. Servicio.

Y cuatro de apoyo, que atraviesan a las primarias: infraestructura de la empresa, gestión de recursos humanos, desarrollo de tecnología y abastecimiento. Según un resumen secundario, el margen es el valor que se crea menos lo que cuesta crearlo.

La lista de las cuatro de apoyo coincide con la de un libro de texto de sistemas de información contable, Romney y otros (2013, cap. 1, figura 1.10): «Firm infrastructure», «Human resources activities», «Technology activities» y «Purchasing activities», junto a las cinco primarias que «directly provide value to customers». El fragmento leído no nombra a Porter.

> [!NOTE] Sin fuente todavía: la lista de las actividades de apoyo en el libro de Porter, que no se abrió.

## La cadena de un SaaS

Las categorías de Porter son de manufactura: "logística interna" supone materia prima que entra a una planta. Para servicios de información, Rayport y Sviokla (1995) proponen una "cadena de valor virtual" con cinco actividades sobre la información: reunir, organizar, seleccionar, sintetizar y distribuir. Se leyó por resúmenes. Es lo más cercano a una versión para software que encontraron los informes; una versión canónica para SaaS no apareció.

En la práctica, al analizar un SaaS se reemplazan las categorías por las actividades reales del negocio. La lista que sigue es una adaptación de esta base para una plataforma de tiendas online, no una fuente:

| Actividad | Qué incluye | Dónde puede estar el costo o la diferencia |
|---|---|---|
| Desarrollo de producto | Ingeniería, diseño, calidad | Velocidad para sacar funciones, calidad del editor de tiendas |
| Infraestructura | Servidores, nube, seguridad | Costo por tienda activa, disponibilidad en picos de venta |
| Adquisición | Marketing, ventas, socios | Costo de conseguir un comerciante, canal de agencias |
| Alta y migración | Puesta en marcha, importación de catálogo | Tiempo hasta la primera venta |
| Soporte y éxito del cliente | Atención, educación, comunidad | Costo por ticket, retención |
| Ecosistema | Apps de terceros, API, temas | Amplitud del catálogo de apps sin costo propio |
| Pagos y servicios financieros | Cobros, créditos, conciliación | Margen por transacción |

La relación entre adquisición, retención y margen por cliente se mide con la [economía unitaria](../../Marketing/Medicion/economia-unitaria.md).

## Cómo se compara con la de un rival

La cadena es interna, pero sirve para leer a un competidor. El procedimiento es de esta base, armado a partir del uso que Porter le da (ubicar dónde se genera el costo o la diferencia):

1. Armá la cadena propia, o la del producto que se va a diseñar, con las actividades reales.
2. Para cada actividad, estimá cómo la hace el rival. Las fuentes son su producto, sus precios, sus ofertas de empleo y sus [reportes públicos](../Analisis-de-competidores/lectura-de-reportes-publicos.md); el [desarme de producto](../Analisis-de-competidores/desarme-de-producto.md) cubre lo que se ve desde afuera.
3. Marcá dónde el rival tiene un costo menor o una diferencia que el cliente paga. Esas son sus fuentes de ventaja.
4. Preguntá por qué no se copia cada una: escala, red, un recurso propio, un proceso de años. Ahí la cadena se conecta con [recursos y capacidades](recursos-y-capacidades.md) y con los [siete poderes](siete-poderes.md).
5. Decidí en qué actividades el producto nuevo va a ser distinto, y en cuáles alcanza con no ser peor.

El informe de esta base advierte contra dibujar la cadena y no sacar nada de ella: sirve para ubicar dónde se genera el costo o la diferencia.

> [!NOTE] Sin fuente todavía: un texto que describa el uso de la cadena de valor para comparar con competidores (benchmarking de costos por actividad); el procedimiento de arriba es de esta base.

## Leer a Porter (1985)

*Competitive Advantage*, capítulo 2 (la cadena de valor y la ventaja) y capítulo 3 (costo y diferenciación como impulsores). Fijarse en cómo cada actividad puede ser fuente de costo o de diferencia. Esta base no lo abrió: queda como recomendación de biblioteca. Hay traducción, *Ventaja competitiva*, de Ediciones Pirámide.
