---
resumen: >-
  Una característica arquitectónica es una cualidad que el sistema tiene que tener además de hacer
  lo que hace (rendimiento, escalabilidad, disponibilidad, seguridad, costo), y que pesa en cómo se
  estructura; se eligen pocas porque compiten entre sí.
estado: borrador
estabilidad: estable
fuentes:
  - https://nealford.com/books/SAF2e.html
  - "Richards y Ford, Fundamentals of Software Architecture, 2ª ed. (O'Reilly, 2025), caps. 'Architectural Characteristics Defined' e 'Identifying Architectural Characteristics' (no leídos)"
  - https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ch27.html
aliases: [architectural characteristics, -ilities, atributos de calidad, requisitos no funcionales]
creado: 2026-11-27
revisado:
---

# Características arquitectónicas

Una característica arquitectónica es una cualidad que el sistema tiene que tener además de hacer
lo que hace (rendimiento, escalabilidad, disponibilidad, seguridad, costo), y que pesa en cómo se
estructura; se eligen pocas porque compiten entre sí.

## Funcionalidad y característica

La funcionalidad dice qué hace el sistema: cobrar un pedido, responder una pregunta. La
característica dice cómo tiene que hacerlo: en menos de un segundo, sin caerse en el pico de
ventas, sin que un cliente vea los datos de otro. Dos sistemas con la misma funcionalidad pueden
pedir arquitecturas distintas porque piden características distintas (los ejemplos son de esta
base). Richards y Ford les dedican capítulos propios: definirlas, identificarlas, medirlas y
gobernarlas, y delimitar su alcance (según el índice de la 2ª edición).

> [!NOTE] Sin fuente todavía: los criterios del libro para decidir qué cuenta como característica,
> la distinción entre características explícitas e implícitas, la idea de buscar la arquitectura
> "menos mala" y por qué conviene elegir pocas. El capítulo no se pudo leer (acceso bloqueado).

## Todo es un trade-off

Las características se contradicen. Un sistema más disponible necesita copias y eso cuesta; uno
más seguro agrega controles y eso suma latencia; uno muy elástico es más difícil de probar. De ahí
que convenga elegir pocas, las que deciden el éxito, y dejar las demás como deseables (razonamiento
de esta base; el libro no se leyó). Según resúmenes
secundarios del libro, la primera ley de Richards y Ford es "Everything in software architecture is
a trade-off" y la segunda, "the why is more important than how"; la 2ª edición sumaría una tercera,
que las decisiones "aren't binary but rather exist on a spectrum between extremes".

> [!IMPORTANT] Cuántas leyes tiene la 2ª edición (dos o tres) solo sale de resúmenes secundarios;
> no se confirmó en el libro.

La segunda ley es la que conecta esta nota con [Decisiones](../Decisiones/decisiones.md): elegir
una característica implica resignar otra, y eso conviene escribirlo en un [ADR](../Decisiones/adr.md) para
que se pueda revisar cuando cambie el contexto (inferencia de esta base).

## De la característica al estilo y a la medición

Las características elegidas son la entrada para [elegir un estilo](../Estilos/elegir-un-estilo.md):
un [monolito modular](../Estilos/monolito-modular.md) y unos
[microservicios](../Estilos/microservicios.md) puntúan distinto en escalabilidad, costo y
simplicidad. Y una característica sin número no se puede verificar: el paso siguiente es
convertirla en una [fitness function](fitness-function.md). Con un modelo de IA adentro, dos
características suben al frente, el [costo y la latencia](costo-y-latencia.md), y aparece la
calidad de una salida que cambia, que se mide con
[evaluación](../Evaluacion-y-observabilidad/evaluacion.md).

## Qué leer del libro

Richards y Ford, *Fundamentals of Software Architecture*, 2ª ed. (2025), los capítulos
"Architectural Characteristics Defined" e "Identifying Architectural Characteristics". Fijarse en
qué separa una característica de un requisito de dominio, en por qué conviene elegir pocas y en la
primera ley. Están en la [bibliografía](../Fundamentos/bibliografia-de-arquitectura.md).
