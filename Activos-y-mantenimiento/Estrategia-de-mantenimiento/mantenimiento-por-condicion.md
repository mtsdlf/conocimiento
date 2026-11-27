---
resumen: >-
  El mantenimiento por condición es el que mide el estado de un equipo y lo interviene cuando la medición muestra que una falla está en camino, en lugar de hacerlo a intervalos fijos. Funciona solo si la falla avisa con tiempo para actuar: ese tiempo es el intervalo P-F.
estado: vigente
estabilidad: semi
fuentes:
  - "DOE/FEMP, O&M Best Practices Guide, Release 3.0, cap. 5, sec. 5.4 «Predictive Maintenance (Condition-Based Maintenance)» y comparación de programas: https://www1.eere.energy.gov/femp/pdfs/OM_5.pdf"
  - "Nowlan y Heap, Reliability-Centered Maintenance, 1978, DTIC ADA066579 (copia de la Wayback Machine del PDF de DTIC; la URL original da 403): https://web.archive.org/web/2020/https://apps.dtic.mil/sti/pdfs/ADA066579.pdf"
  - "NASA, Reliability Centered Maintenance Guide for Facilities and Collateral Equipment, copia de febrero de 2000, glosario y fig. 1-1: https://everyspec.com/NASA/NASA-General/download.php?spec=NASA_RCM_GUIDE_2000.030306.pdf"
  - "Kevin Clark, «Improving maintenance by adopting a P-F curve methodology», InTech (ISA), marzo/abril de 2019: https://www.isa.org/intech-home/2019/march-april/features/improving-maintenance-by-adopting-a-p-f-curve-meth"
  - "Tractian, glosario, P-F curve (regla de la mitad del intervalo; vía buscador, no leído): https://tractian.com/en/glossary/p-f-curve-potential-failure-curve"
  - "Wikipedia, Preventive maintenance y Predictive maintenance (según su resumen): https://en.wikipedia.org/wiki/Predictive_maintenance"
  - "Moubray, Reliability-centred Maintenance (RCM II), 1997 (no leído): https://books.google.com/books?id=bNCVF0B7vpIC"
  - "Activos-y-mantenimiento/.investigacion/estrategia-y-fundamentos.md (componente C y mitos, 2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/tercera-ronda.md (curva P-F, 2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/verificacion-estrategia.md (2026-11-27)"
aliases: [mantenimiento por condición, mantenimiento predictivo, predictive maintenance, PdM, mantenimiento basado en la condición, condition-based maintenance, CBM, monitoreo de condición, condition monitoring, curva P-F, P-F curve, intervalo P-F, P-F interval, falla potencial, potential failure, falla funcional, functional failure, tarea a condición, on-condition task]
creado: 2026-11-27
revisado: 2026-11-27
---

# Mantenimiento por condición

El mantenimiento por condición es el que mide el estado de un equipo y lo interviene cuando la medición muestra que una falla está en camino, en lugar de hacerlo a intervalos fijos. Funciona solo si la falla avisa con tiempo para actuar: ese tiempo es el intervalo P-F.

El DOE lo distingue del [preventivo](mantenimiento-preventivo.md) por basar la necesidad de intervenir «on the actual condition of the machine rather than on some preset schedule». Su ejemplo es el aceite: en lugar de cambiarlo cada 3.000 a 5.000 millas, se lo analiza y el cambio se estira hasta 10.000. Es uno de los tipos de la [estrategia de mantenimiento](estrategia-de-mantenimiento.md), y el [mantenimiento centrado en la confiabilidad](mantenimiento-centrado-en-confiabilidad.md) es el método que dice a qué modos de falla aplicarlo.

## Predictivo y por condición, un solo término en esta base

El DOE usa los dos nombres como uno: titula su sección «Predictive Maintenance (Condition-Based Maintenance)». Wikipedia, según su resumen, presenta el predictivo como una forma del mantenimiento por condición que usa sensores y tendencias. Esta base usa **mantenimiento por condición** para todo el tipo y deja predictivo como sinónimo.

## Inspeccionar o monitorear

La condición se puede conocer de dos maneras. La **inspección** es periódica: un técnico recorre los equipos, mira, escucha, toca o mide con un instrumento portátil y anota. El **monitoreo** es continuo o casi: un sensor fijo manda lecturas a un sistema que avisa cuando una pasa un umbral. Las dos son mantenimiento por condición; cambia cada cuánto se mira y cuánto cuesta mirar. Esta distinción es criterio de la base.

La guía de la NASA trata las tecnologías de medición en su capítulo 4, que no se leyó; el DOE da solo el ejemplo del aceite.

Para quien construye el software, la diferencia importa en el dato, según la base. Una inspección produce una orden con lecturas anotadas a mano; el monitoreo produce una serie de lecturas sin orden de trabajo, que genera una orden solo cuando algo se sale de rango. Las dos terminan en el [historial del equipo](../Registro-de-activos/historial-del-equipo.md). Analizar esas series para predecir fallas es una técnica de datos que no es de este tema: lo más cercano en la base es la analítica predictiva de [tipos de analítica](../../Datos/Analisis/tipos-de-analitica.md), dentro de [Datos](../../Datos/datos.md), y los modelos en [IA](../../IA/ia.md).

## La curva P-F

La curva P-F dibuja cómo un equipo pasa de estar bien a fallar, y dónde en ese camino se puede ver que viene la falla. Tiene dos puntos:

- **P, la falla potencial.** Nowlan y Heap (1978) la definen como «an identifiable physical condition which indicates a functional failure is imminent»; la NASA, como «An identifiable condition that indicates a failure is imminent». Clark, en la revista de la ISA, la describe como «a detectable state of failure, or the point at which degradation begins».
- **F, la falla funcional.** Nowlan y Heap la definen como «the inability of an item (or the equipment containing it) to meet a specified performance standard», que incluye no rendir al nivel especificado además de la pérdida total de la función. Según Clark, es cuando el equipo «has reached a failed state or no longer performs satisfactorily»: dejó de cumplir su función.

El **intervalo P-F** es el tiempo entre que la falla potencial se detecta y la falla funcional ocurre. Es el margen para actuar: pedir el repuesto, programar la parada y cambiar la pieza (lectura de la base). Clark aclara que «The method and frequency of detection essentially determine the length of the P-F interval».

```mermaid
flowchart LR
  A[Equipo sano] --> P[P: la falla se puede detectar]
  P -->|intervalo P-F: margen para actuar| F[F: el equipo deja de cumplir su función]
```

Clark cita a John Bernet: «The P-F curve is a conceptual representation only and does not have any units or scale». Sirve para razonar, no para leer números. Nowlan y Heap fundan los conceptos de falla potencial y funcional, pero en su informe no aparece la sigla «P-F»; varias fuentes secundarias atribuyen el término a John Moubray, según el buscador, y el libro de Moubray no se abrió.

De la curva sale la regla para fijar la frecuencia de inspección. Nowlan y Heap piden como condición que haya un intervalo de edad razonablemente consistente entre la falla potencial y la funcional, y fijan el intervalo de inspección para que dé «ample opportunity to detect a potential failure before a functional failure can occur». Dicho de otro modo (lectura de la base), hay que mirar más seguido que el intervalo P-F, o la falla puede pasar entre dos inspecciones sin que nadie la vea. Un glosario de un proveedor da como regla práctica inspeccionar a la mitad del intervalo P-F, según el buscador; no es una regla que se pueda atribuir a Moubray ni a una norma.

> [!NOTE] Sin fuente todavía: la regla de inspeccionar a la mitad del intervalo P-F (Moubray, RCM II, capítulo de tareas a condición, no abierto; Nowlan y Heap no la dan), y valores de intervalo P-F por técnica y tipo de falla.

## Cuándo vale la pena vigilar en lugar de cambiar

El mantenimiento por condición tiene condiciones técnicas y económicas. Las condiciones técnicas coinciden con los tres criterios de aplicabilidad de Nowlan y Heap para una tarea a condición: poder detectar la pérdida de resistencia a la falla en un modo de falla específico, poder definir una condición de falla potencial detectable con una tarea explícita, y un intervalo razonablemente consistente entre esa condición y la falla funcional. Dicho en la curva (lectura de la base), el intervalo P-F tiene que ser lo bastante largo para actuar y lo bastante estable para fijar una frecuencia de inspección. Si la falla no avisa, o avisa con horas cuando la reparación lleva semanas, vigilarla no sirve.

La NASA lo recomienda para las fallas aleatorias, las que no dependen de la edad, y para las que induce el propio preventivo al abrir el equipo. Según la NASA, la mayoría de los equipos no falla por edad, como cuenta [mantenimiento centrado en la confiabilidad](mantenimiento-centrado-en-confiabilidad.md); que sean fallas aleatorias es lectura de la base.

Las condiciones económicas las pone el DOE entre las desventajas: «Increased investment in diagnostic equipment», «Increased investment in staff training» y «Savings potential not readily seen by management». En su comparación de programas dice que funciona «very well if personnel have adequate knowledge, skills, and time». El ahorro de 8 a 12 por ciento sobre el preventivo que la misma guía le atribuye no tiene estudio citado; la advertencia está en [estrategia de mantenimiento](estrategia-de-mantenimiento.md#las-cifras-de-ahorro-que-circulan-y-por-qué-no-sirven-de-dato).

El mito que circula es que el predictivo siempre conviene. La página de Wikipedia sobre mantenimiento predictivo lleva desde mayo de 2024 un aviso de contenido promocional, y sus cifras de ahorro no tienen fuente. Elegirlo depende de la [criticidad](../Registro-de-activos/criticidad.md) del equipo; por ejemplo, un sensor caro sobre una bomba con respaldo probablemente cuesta más que dejarla fallar (ejemplo de la base).

> [!NOTE] Sin fuente todavía: un criterio publicado para comparar el costo del monitoreo contra el costo de la falla, y una crítica de la curva P-F leída (el buscador mostró una en Scribd que sostiene que la curva no representa el preventivo por edad ni el dejar fallar, sin abrirla).
