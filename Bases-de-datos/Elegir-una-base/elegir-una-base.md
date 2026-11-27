---
resumen: >-
  Elegir una base es juntar el modelo de datos, las garantías de las transacciones y lo que cuesta
  operarla en una decisión para un sistema concreto. No tiene un texto canónico propio: se arma con
  la documentación de cada motor, los análisis independientes y la experiencia de quien opera.
estado: vigente
estabilidad: estable
fuentes:
  - "SQLite, Appropriate Uses For SQLite: https://www.sqlite.org/whentouse.html"
  - "Jepsen, índice de análisis: https://jepsen.io/analyses"
  - "Bases-de-datos/.investigacion/modelos-transacciones-elegir.md (informe del 2026-11-27)"
aliases: [elegir una base de datos, choosing a database, selección de base de datos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Elegir una base

Elegir una base es juntar el modelo de datos, las garantías de las transacciones y lo que cuesta
operarla en una decisión para un sistema concreto. No tiene un texto canónico propio: se arma con
la documentación de cada motor, los análisis independientes y la experiencia de quien opera.

Es la vertical que cierra [Bases de datos](../bases-de-datos.md). Recibe de
[Modelos de datos](../Modelos-de-datos/modelos-de-datos.md) qué forma puede tener el dato y de
[Transacciones](../Transacciones/transacciones.md) qué garantías hacen falta cuando varios escriben a
la vez. Le suma lo que ninguna de las dos mira: quién la opera, cuánto cuesta y qué sabe el equipo.

## No hay un libro que lo resuelva

Los libros de bases de datos tratan los modelos y las transacciones en capítulos propios, pero la
elección es una síntesis de esos capítulos con la operación. Lo que hay sobre elegir es de tres
tipos, y conviene leerlo sabiendo de cuál es:

| Tipo de fuente | Ejemplo | Para qué sirve | Cuidado |
|---|---|---|---|
| Documentación del propio motor | La página de SQLite sobre cuándo usarlo | Criterios explícitos y límites declarados | La escribe quien tiene interés en el motor |
| Análisis independientes | Los informes de Jepsen sobre garantías de cada motor | Saber si el motor cumple lo que promete | Están fechados y prueban una versión |
| Opinión de practicantes y rankings | Encuestas de uso, casos de migración de empresas | Ver qué usa la gente y por qué dejó algo | Popularidad no es calidad; cada caso tiene su carga |

La página de SQLite es lo más parecido a una guía con criterios: termina en una lista de
verificación de pocas preguntas. Por eso se usa como punto de partida en
[criterios de elección](criterios-de-eleccion.md), aunque sea del propio proyecto.

## Cómo se decide para el sistema de un comercio

El orden que sigue sale de las otras dos verticales; ninguna fuente lo propone así:

1. Mirá las preguntas que se le van a hacer a los datos y elegí el modelo. Para pedidos, clientes,
   productos y stock que se cruzan, es relacional.
2. Mirá cuántos escriben a la vez y desde dónde. Una aplicación en un solo equipo con pocas
   escrituras puede usar SQLite; un sistema web con varios usuarios cargando pedidos pide una base
   cliente-servidor.
3. Decidí quién la opera: un servidor propio o una
   [base administrada](base-administrada.md), y qué respaldo y restauración exigís.
4. Recién entonces elegí el motor y el plan en la
   [ficha de motores](motores-de-bases-de-datos.md).

La decisión falla de dos maneras típicas. Una es elegir por moda o por volumen imaginado ("NoSQL
escala más"), que discute la [posición contraria](../Fundamentos/fundamentos-de-bases-de-datos.md).
La otra es elegir bien el motor y no pedir el respaldo: el plan gratis de un servicio puede no
guardar copias.

## Lo que hay en esta vertical

- [Criterios de elección](criterios-de-eleccion.md) — modelo, garantías transaccionales, concurrencia de escritura,
  escala, operación, costo y experiencia del equipo; PostgreSQL por defecto y sus críticas, y
  cuándo alcanza SQLite.
- [Base administrada](base-administrada.md) — propia contra administrada; respaldo, restauración a un
  punto, réplica y alta disponibilidad como requisitos a pedir.
- [Motores de bases de datos](motores-de-bases-de-datos.md) — ficha fechada con versiones, licencias y
  lo que trae el plan gratis de algunos servicios administrados.

Si la decisión es dejar una planilla, el paso previo está en
[cuándo pasar a una base](../../Planillas-de-calculo/cuando-pasar-a-una-base.md). Los servicios de
Azure, en
[Almacenamiento y bases de datos en Azure](../../Cloud/Datos-operacionales/almacenamiento-y-bases-de-datos-en-azure.md).
