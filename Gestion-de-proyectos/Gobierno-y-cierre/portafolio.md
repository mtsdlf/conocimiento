---
resumen: >-
  El portafolio es el conjunto de proyectos que una organización lleva a la vez, y gestionarlo es decidir cuáles entran, en qué orden y cuántos corren en paralelo. El problema que más se repite es tener demasiados proyectos para la gente disponible.
estado: borrador
estabilidad: semi
fuentes:
  - "Cooper, Edgett y Kleinschmidt, portafolios de nuevos productos (Research-Technology Management 40(6), 1997; 2004) (según resúmenes): https://macsphere.mcmaster.ca/bitstream/11375/5432/1/fulltext.pdf"
  - "Reinertsen, The Principles of Product Development Flow (resumen secundario en InformIT): https://www.informit.com/articles/article.aspx?p=2928185&seqNum=6"
  - "Grant y Gergely (2012), revisión de la cadena crítica, PMI (no se leyeron sus conclusiones): https://www.pmi.org/learning/library/critical-chain-project-management-investigation-6380"
  - "IPMA, Individual Competence Baseline 4.0, edición alemana de GPM: https://www.gpm-ipma.de/fileadmin/user_upload/ICB4_Projektmanagement.pdf"
  - "ISO, comité TC 258, ficha de ISO 21502 (según resúmenes): https://committee.iso.org/sites/tc258/home/projects/published/iso-21502.html"
  - "Singer, Shape Up (Basecamp), cap. 8: https://basecamp.com/shapeup/2.2-chapter-08"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
  - "Gestion-de-proyectos/.investigacion/fundamentos.md"
aliases: [cartera de proyectos, portfolio management, gestión de portafolio, project portfolio, proyectos en paralelo, multiproyecto]
creado: 2026-11-27
revisado:
---

# Portafolio

El portafolio es el conjunto de proyectos que una organización lleva a la vez, y gestionarlo es decidir cuáles entran, en qué orden y cuántos corren en paralelo. El problema que más se repite es tener demasiados proyectos para la gente disponible.

Dentro de [gobierno y cierre](gobierno-y-cierre.md), el portafolio mira todos los proyectos juntos, mientras el [gobierno del proyecto](gobierno-del-proyecto.md) mira uno. Los marcos lo separan más: ISO 21502 trata solo proyectos y deja programa y portafolio a otras normas de su familia, según la ficha del comité. El ICB4 de IPMA tiene una competencia, "Select and balance", que no aplica a proyectos sino a portafolios y programas. Esta base lo pone en la misma vertical por decisión propia, no del campo: con equipos chicos, la misma persona gobierna el proyecto y decide qué otros corren al lado.

## Demasiados proyectos a la vez

Cooper, Edgett y Kleinschmidt estudiaron cómo las empresas manejan sus portafolios de nuevos productos. Según los resúmenes, el problema más común que encontraron fue tener demasiados proyectos para los recursos disponibles. Lo acompañaban carteras sobrecargadas, poca priorización, decisiones de seguir o matar sin buena información y demasiados proyectos menores. Ese cuadro se asoció con proyectos de bajo impacto, más demora en llegar al mercado y más fracasos. La muestra es de desarrollo de nuevos productos, no de todo tipo de proyecto, y no se cotejó su tamaño.

Un mecanismo posible, que Cooper y colegas no dan en lo que se leyó, viene de la teoría de colas (inferencia de esta base). Según Reinertsen, las colas crecen mucho cuando la utilización es alta, así que cargar a la gente al máximo alarga la espera de todo lo que está en curso. El umbral de utilización que circula en blogs no se verificó en su texto y esta base no lo usa. La relación entre trabajo en curso, rendimiento y tiempo de entrega, y los estudios que la midieron en equipos, están en [trabajo en curso y colas](../Seguimiento/trabajo-en-curso-y-colas.md).

Un ejemplo: un área con seis personas lleva ocho proyectos, cada persona reparte su semana entre tres. Todos avanzan y ninguno termina, porque cada uno espera a alguien que está en otro. Bajar a tres proyectos a la vez no agrega capacidad, pero hace que los tres terminen antes y que los otros cinco esperen sin consumir a nadie.

## Cuántos proyectos en paralelo

> [!NOTE]
> Sin fuente todavía: no se encontró evidencia controlada sobre cuántos proyectos en paralelo conviene tener. Hay el benchmarking de Cooper en nuevos productos y guías de practicantes. Para la cadena crítica de Goldratt en varios proyectos hay guías y un caso; la revisión de Grant y Gergely sobre la cadena crítica no se leyó.

Sin un número probado, la regla práctica que se desprende de la teoría de colas es fijar un límite y bajarlo hasta que la gente deje de repartirse entre proyectos. Es una inferencia de esta base. El límite se expresa en proyectos activos, no en horas, porque el costo de cambiar de un proyecto a otro no aparece en las horas. Cómo limitar el trabajo en curso como sistema está en [flujo continuo](../Enfoque/flujo-continuo.md).

## Cuáles entran

Decidir qué entra exige comparar proyectos con la misma vara. Cada uno trae su [justificación](../Encuadre/justificacion.md), y el portafolio las ordena. Reinertsen propone ordenar por costo de demora: cuánto vale por semana tener terminado cada proyecto. Es una fuente de practicante, y su respaldo empírico en proyectos no se verificó. Cómo se aplica el costo de demora y otros puntajes para ordenar trabajo de producto está en [priorización](../../Producto/Planificacion-y-entrega/priorizacion.md).

Shape Up resuelve la entrada con una apuesta por ciclo: al empezar cada ciclo de seis semanas se elige qué proyectos ya acotados entran. Es un método de practicante; está en [Shape Up](../../Producto/Planificacion-y-entrega/shape-up.md).

Un portafolio también decide qué sale. Un proyecto que dejó de justificarse ocupa lugar que otro podría usar, y la decisión de pararlo está en [cerrar o cancelar](cerrar-o-cancelar.md).

## Qué cambia cuando ejecutan agentes

> [!NOTE]
> Sin fuente todavía: no se encontró una fuente sobre portafolios de proyectos ejecutados en parte por agentes.

Lo que sigue es inferencia de esta base. Si los agentes ejecutan, la capacidad de producir deja de ser el límite del portafolio, y es tentador abrir más proyectos. Pero cada proyecto sigue necesitando a una persona que encargue, revise y acepte. El límite de proyectos en paralelo pasa a ser también un límite de capacidad de revisión: con más proyectos abiertos que revisores, el trabajo de los agentes se acumula en la cola de revisión en vez de terminar. Eso está en [la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md), y cómo se cuenta esa capacidad, en [capacidad y costo](../Planificacion/capacidad-y-costo.md).
