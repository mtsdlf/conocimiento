---
tema: Bases de datos
para: entender qué es una base de datos, elegir una para un sistema y escribir SQL con soltura; lo leen Matías y Fer y los agentes que construyen sistemas
nivel: se da por sabido usar una planilla; no se dan por sabidos SQL ni bases de datos
escuela:
fuera:
  - "El interior del motor (páginas, B-tree, LSM, WAL) y la operación fina (tuning, replicación a mano): queda afuera por pedido"
  - "Teoría del modelo relacional (claves según Codd, normalización): Datos/Modelado-y-almacenamiento/modelo-relacional.md"
  - "Base de la aplicación contra base para analizar: Datos/Modelado-y-almacenamiento/oltp-y-olap.md"
  - "Almacenes analíticos: Datos/Modelado-y-almacenamiento/almacenes-analiticos.md"
  - "SQL para análisis (el grano, el uso del analista): Datos/Analisis/sql-para-analisis.md"
  - "La planilla y cuándo deja de alcanzar: Planillas-de-calculo/ (Planillas-de-calculo/cuando-pasar-a-una-base.md)"
  - "Servicios de bases de datos de Azure: Cloud/Datos-operacionales/"
  - "Multi-tenancy: Arquitectura/Sistemas-distribuidos/multi-tenancy.md"
fuentes: []
preguntas:
  - "¿PostgreSQL, MongoDB o SQLite para un sistema nuevo de un comercio? ¿Con qué criterios elijo?"
  - "Tengo pedidos, clientes y productos en tablas: ¿cómo saco el total vendido por cliente en el último mes, incluidos los que no compraron?"
  - "Quiero el último pedido de cada cliente: ¿subconsulta, CTE o función de ventana?"
  - "Dos personas compran el último producto al mismo tiempo: ¿cómo evito vender stock que no hay?"
  - "Una consulta tarda mucho con 100 mil pedidos: ¿qué miro primero?"
  - "¿Cuándo conviene un ORM y cuándo SQL a mano, y qué es el problema N+1?"
aprobado: 2026-11-27
---

# Alcance: Bases de datos

Bases de datos explica qué es una base, qué modelos hay y cómo se elige una para un sistema, y va a
fondo en SQL del lado de quien escribe consultas. Salió de una conversación del 2026-11-27: la
persona pidió conceptos para entender y elegir, y SQL en profundidad sin el interior del motor.

## Árbol

```
Bases-de-datos/
  bases-de-datos.md           el todo: qué hace una base, sus partes y cómo se elige
  Modelos-de-datos/           cómo organiza los datos cada familia de bases
    base-relacional           tablas, claves y SQL; la teoría está en Datos/Modelado-y-almacenamiento/modelo-relacional.md
    base-de-documentos        documentos JSON anidados, esquema flexible
    base-clave-valor          una clave, un valor; caché y sesiones
    modelos-especializados    grafos, series de tiempo, búsqueda, vectores
    registro-de-movimientos   stock y saldos como filas que no se editan (sumado el 2026-11-27)
  SQL/                        hondo: el lenguaje para consultar y modificar
    consulta-select           cláusulas y orden lógico de ejecución
    join                      inner, left, cross, autojoin; joins que multiplican
    agregacion                GROUP BY, HAVING, funciones de agregado
    subconsultas-y-cte        subconsulta, EXISTS, WITH, recursiva
    funciones-de-ventana      OVER, PARTITION BY, ranking, acumulados
    null-y-tipos              lógica de tres valores, tipos y conversiones
    modificar-datos           INSERT, UPDATE, DELETE, upsert, RETURNING
    definir-tablas            CREATE TABLE, restricciones, migraciones, vistas
    indice                    qué es, cuándo se usa, leer un plan
    sql-desde-una-aplicacion  parámetros, inyección SQL, ORM, N+1
    ficha: dialectos de SQL
  Transacciones/              varias operaciones como una sola
    transaccion               ACID, commit y rollback
    nivel-de-aislamiento      qué ve una transacción de las otras y sus anomalías
    concurrencia              actualización perdida, bloqueo optimista y pesimista
  Elegir-una-base/            criterios y opciones
    criterios-de-eleccion     modelo, garantías transaccionales, escala, operación, costo
    base-administrada         propia o administrada; respaldo y réplica como requisitos
    ficha: motores de bases de datos
  Fundamentos/
    glosario-de-bases-de-datos
    fuentes-de-bases-de-datos
    ruta-de-sql               ejercicios para aprender SQL en orden
```

## Supuestos

- SQL vive acá como lenguaje; `Datos/Analisis/sql-para-analisis.md` queda para el grano y el uso
  del analista, y las dos se enlazan en los dos sentidos (issue #77).
- Respaldo y replicación entran solo como requisitos al elegir, no como operación.
