---
resumen: >-
  La ingesta es traer el dato crudo desde los sistemas donde nace hasta el almacén donde se
  analiza, por lotes cada cierto tiempo, en flujo a medida que ocurre o copiando los cambios de una
  base.
estado: vigente
estabilidad: estable
fuentes:
  - "Joe Reis y Matt Housley, Fundamentals of Data Engineering, cap. 7 Ingestion (O'Reilly, 2022); no leído, estructura vía buscador: https://oreilly.com/library/view/fundamentals-of-data/9781098108298"
  - "Debezium, sitio oficial: https://debezium.io/"
  - "Debezium, Features (leída entera en Datos/.investigacion/bi-gestion-extraccion.md): https://debezium.io/documentation/reference/stable/features.html"
  - "PostgreSQL, Logical Decoding Concepts (leída entera en Datos/.investigacion/bi-gestion-extraccion.md): https://www.postgresql.org/docs/current/logicaldecoding-explanation.html"
  - "Apache Flink, Concepts overview: https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/overview/"
  - "Datos/.investigacion/modelado-e-ingesta.md (sección 7)"
aliases: [ingesta de datos, data ingestion, carga de datos, CDC, change data capture, streaming, batch]
creado: 2026-11-27
revisado: 2026-11-27
---

# Ingesta

La ingesta es traer el dato crudo desde los sistemas donde nace hasta el almacén donde se
analiza, por lotes cada cierto tiempo, en flujo a medida que ocurre o copiando los cambios de una
base.

Es el primer paso de [ingesta y transformación](ingesta-y-transformacion.md). Termina cuando el
dato llegó al [almacén analítico](../Modelado-y-almacenamiento/almacenes-analiticos.md) tal como
salió del origen; darle forma es la [transformación](etl-y-elt.md). Los sistemas de origen son
variados: la base de la aplicación, una API de pagos, la planilla de costos, los eventos de la
[tabla de eventos](../Modelado-y-almacenamiento/tabla-de-eventos.md).

## Tres maneras de traer el dato

| | Por lotes | En flujo | Copia de cambios (CDC) |
|---|---|---|---|
| Cuándo trae | cada cierto tiempo: una vez por noche, cada hora | cada evento apenas ocurre | cada alta, cambio o borrado en la base de origen |
| Qué trae | todo o lo nuevo desde la última vez | un evento por vez | la fila antes y después del cambio |
| Latencia | horas o minutos | segundos | segundos o minutos |
| Complejidad | baja | alta | media |

Las filas de latencia y complejidad son lectura de la base.

**Por lotes** es lo más simple (lectura de la base): una tarea programada lee del origen y escribe en el almacén. Puede
traer la tabla entera cada vez (carga completa) o solo lo nuevo desde la última corrida (carga
incremental), que necesita una columna confiable de fecha de modificación.

**En flujo** trata los datos como una corriente que no termina. La documentación de un motor de
flujo solo menciona las corrientes acotadas (*bounded*) y las no acotadas (*unbounded*); leído así,
un lote es un pedazo con principio y fin y un flujo no tiene fin (lectura de la base).

**La copia de cambios** (*change data capture*, CDC) escucha la base de la aplicación y emite un
evento por cada inserción, actualización o borrado. Una plataforma abierta de CDC lo describe como
la forma de que otras aplicaciones respondan a esos cambios sin modificar las que escriben en la
base; cada evento registra el tipo de operación, el estado de la fila antes y después, y de dónde
vino.

Los cambios salen del registro de transacciones de la base, no de consultar las tablas. En
PostgreSQL, la decodificación lógica en que se apoya la copia de cambios «is implemented by
decoding the contents of the write-ahead log», el registro que la base escribe antes de cada
cambio, y lo devuelve como una secuencia de filas o de sentencias. Por eso, según la misma
plataforma de CDC, capta los borrados y no obliga a cambiar el modelo de datos. Tiene un costo en el
origen: mientras un lector lo necesite, la base no puede borrar ese registro, y un lector abandonado
lo hace crecer; PostgreSQL pide dar de baja el que ya no se usa.

> [!NOTE]
> Sin fuente todavía: una definición literal de lote contra flujo en la bibliografía canónica.

## La latencia que hace falta decide

Lo que decide es cada cuánto alguien necesita el dato nuevo. Un tablero
de ventas que se mira cada mañana no gana nada con datos al segundo; un control de fraude en pagos,
sí. Cada salto de latencia suma piezas que mantener y costo (lectura de la base). El capítulo de Reis
y Housley tiene secciones separadas para la ingesta por lotes y la de mensajes y flujos, según la
estructura que muestra el buscador; que la plantee en términos de latencia contra complejidad es
lectura de la base.

En un comercio chico, un lote por noche alcanza para casi todo (lectura de la base). Se pasa a flujo o a CDC cuando una
decisión depende de lo que pasó hace minutos, o cuando la carga completa ya tarda demasiado y la
base de origen no tiene una fecha de modificación confiable para la incremental.

## Cómo falla la ingesta

- El origen cambia sin avisar. Una columna nueva, otra renombrada, un formato de fecha distinto.
  La ingesta sigue corriendo y carga columnas vacías.
- Lo incremental pierde filas. Si la fecha de modificación no se actualiza en cada cambio, los
  cambios no llegan nunca.
- Duplicados por reintento. Un lote que falla a la mitad y se vuelve a correr carga dos veces
  lo que alcanzó a cargar. Una ingesta que se puede repetir sin duplicar evita el problema.
- Una API con límites. Las APIs de terceros limitan cuántas consultas aceptan, y una carga
  completa diaria puede no entrar.

Todo eso se detecta con controles de [calidad de
datos](../Gobierno-y-calidad/calidad-de-datos.md) a la llegada, y la ingesta se encadena con los
pasos siguientes por medio de la [orquestación](orquestacion.md). Los fallos de esta lista son
lectura de la base, no una lista de una fuente.

## Dónde se lee la versión larga

Reis y Housley, *Fundamentals of Data Engineering*, cap. 7, «Ingestion»: según el informe, lotes contra flujo, CDC y
traer contra recibir (*push* contra *pull*), sin confirmar. Conviene fijarse en la tensión entre la latencia que se
necesita y la complejidad y el costo que agrega. Para CDC, la página principal de Debezium y su
documentación de arquitectura. Las herramientas concretas están en la ficha de
[herramientas de pipeline](herramientas-de-pipeline.md).
