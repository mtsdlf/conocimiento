---
resumen: >-
  Un sistema heredado es código que hay que cambiar sin haberlo escrito y, sobre todo, sin pruebas que
  digan si un cambio lo rompe. Se entra fijando con pruebas lo que hace hoy, buscando costuras donde
  cambiar su comportamiento y recién después modificándolo.
estado: borrador
estabilidad: estable
fuentes:
  - https://www.spinellis.gr/pubs/Breview/2005-CR-Legacy/html/review.html
  - https://archive.org/details/working-effectively-with-legacy-code
  - https://martinfowler.com/bliki/LegacySeam.html
  - https://blog.ploeh.dk/2025/11/03/empirical-characterization-testing/
  - https://code.claude.com/docs/en/best-practices
  - https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
aliases: [código heredado, legacy code, sistema legado, código legado, legacy system]
creado: 2026-11-27
revisado:
---

# Sistema heredado

Un sistema heredado es código que hay que cambiar sin haberlo escrito y, sobre todo, sin pruebas que digan si un cambio lo rompe. Se entra fijando con pruebas lo que hace hoy, buscando costuras donde cambiar su comportamiento y recién después modificándolo.

## Heredado quiere decir sin pruebas

La definición de Michael Feathers, en *Working Effectively with Legacy Code* (2004), es corta: "legacy code is simply code without tests". Se cita a través de reseñas; el libro no se leyó. Por pruebas entiende, según esas reseñas, pruebas de unidad rápidas que se corren después de cada cambio.

La definición corre el problema de la edad del código a la falta de red. Un sistema de hace diez años con buena suite se cambia con confianza; uno de hace seis meses sin pruebas, no (ilustración de esta base).

## Primero fijar lo que hace, después cambiarlo

La regla de Feathers sigue vigente: primero pruebas que fijen el comportamiento, después cambios. Hay dos herramientas para eso.

Una prueba de caracterización se escribe sobre código existente y describe lo que hace hoy, no lo que debería hacer. Según un artículo de Mark Seemann de 2025 que la resume, la receta de Feathers arranca poniendo el código en un arnés de pruebas y escribiendo una aserción que se espera que falle, para ver cuál es el comportamiento real. La receta llega por un blog y conviene contrastarla con el libro.

Una costura (seam) es, según el bliki de Fowler, "a place where you can alter behavior in your program without editing in that place". Cada costura tiene un punto de habilitación donde se elige qué comportamiento usar. La fuente leída es un resumen de una página y no da más detalle.

Con las dos cosas se trabaja así (pasos propuestos por esta base a partir de Feathers, que no se leyó):

1. Elegí la zona que tenés que cambiar, no todo el sistema.
2. Buscá una costura que te permita correrla aislada.
3. Escribí pruebas de caracterización de lo que hace hoy, incluidos los casos raros.
4. Recién ahí cambiá, con las pruebas corriendo después de cada paso, que es [refactorizar](refactorizar.md).

Cuando la zona es tan grande que conviene reemplazarla entera, el patrón es [strangler fig](../../Arquitectura/Estilos/strangler-fig.md), en Arquitectura.

## Lo que un agente entiende y lo que no

Un agente explora y resume un código desconocido rápido, y puede generar pruebas de caracterización corriendo el sistema y fijando las salidas que observa. La guía de buenas prácticas de Anthropic para su agente de código (leída el 2026-11-27) dice que el agente lee el repositorio para encontrar estructura y convenciones, y que conviene anotar lo que no se deduce del código; eso es el [contexto del repositorio](../Construccion/contexto-del-repositorio.md).

Hay dos riesgos. Fijar el comportamiento actual también fija sus bugs: Böckeler encontró una prueba escrita por un agente que consagraba un error. Y lo que un agente "entendió" de un sistema heredado no está verificado: hay que contrastarlo con el sistema corriendo y con quien lo conoce, si existe.

> [!NOTE]
> Sin fuente todavía: no se encontró un estudio con método sobre qué tan bien entienden los agentes un sistema heredado, ni sobre cuántos bugs se consagran al generar pruebas de caracterización con un agente.

## Lo que pierde peso al entrar a un sistema

Pierde peso leer todo el código antes de tocar nada y documentar el sistema a mano antes de empezar: un agente da un primer mapa rápido, que después se verifica. No pierde peso la regla de fijar el comportamiento antes de cambiar. Cómo se recibe un sistema con sus accesos y su documentación, cuando viene de otro equipo, se acuerda en el [traspaso](../Encargo/traspaso.md); lo que se descubre de deuda al entrar va a [deuda técnica](deuda-tecnica.md).

Para leer: Feathers, las partes sobre costuras y sobre pruebas de caracterización (los capítulos exactos están por verificar contra el índice del libro).
