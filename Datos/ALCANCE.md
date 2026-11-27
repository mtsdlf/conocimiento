---
tema: Datos
para: aprender Data Analytics y medir comercios y productos digitales; lo leen Matías y Fer
nivel: se da por sabido usar una planilla; no se dan por sabidos SQL, estadística ni bases de datos
escuela:
fuera:
  - "Machine learning y modelos predictivos: IA/ o más adelante"
  - "Bases de la aplicación en Azure: Cloud/Datos-operacionales/"
  - "North Star, activación y experimento A/B: Producto/Medicion/"
  - "Atribución, incrementalidad y economía unitaria: Marketing/Medicion/"
  - "Observabilidad de sistemas: DevOps/"
  - "La base de un sistema (modelos, transacciones, elegir una): Bases-de-datos/"
  - "SQL como lenguaje (cláusulas, joins, agregación, NULL, ventanas): Bases-de-datos/SQL/"
  - "La planilla como herramienta (fórmulas, tablas dinámicas, gráficos en Excel y Sheets, versiones y límites): Planillas-de-calculo/"
fuentes: []
preguntas:
  - "Me piden un tablero de ventas de un comercio: ¿qué pasos sigo, desde los datos crudos hasta el tablero?"
  - "¿Qué diferencia hay entre la base de la app, un data warehouse y un data lake, y cuándo necesito cada uno?"
  - "Las ventas subieron después de una promoción: ¿puedo decir que la causó?"
  - "¿Cómo defino una métrica para que dos personas la calculen igual?"
  - "¿Qué hace un analista de datos y qué un analytics engineer o un ingeniero de datos, y qué aprendo primero?"
  - "¿Qué datos personales de los clientes puedo guardar en Argentina?"
  - "Tengo el ERP de un cliente y me piden un tablero de margen por cliente de los últimos cuatro años: ¿lo saco del reporte del sistema o armo un BI, y cómo traigo los datos sin frenar la facturación?"
  - "El tablero de ventas no da lo mismo que el balance: ¿por dónde busco la diferencia?"
  - "Un grupo con dos empresas, una que factura en pesos y otra en dólares, quiere un tablero consolidado: ¿qué hago con las ventas entre ellas y con los tipos de cambio?"
  - "¿Cómo muestro la evolución de las ventas de cuatro años en la Argentina sin que la inflación la distorsione?"
aprobado: 2026-11-27
---

# Alcance: Datos

Datos se amplía de un tema solo de análisis de cohortes a todo el recorrido del dato, para quien
aprende Data Analytics y para medir comercios y productos digitales. Salió de una conversación del
2026-11-27 y de lo que ya decía la entrada del tema («para quien está aprendiendo Data Analytics»).

## Árbol

```
Datos/
  datos.md                     el todo: el recorrido del dato y quién hace cada tramo
  Modelado-y-almacenamiento/   panorama
    oltp-y-olap                base de la aplicación contra base para analizar
    modelo-relacional          tablas, claves, normalización
    modelado-dimensional       hechos y dimensiones; Kimball, Inmon y Data Vault
    almacenes-analiticos       data warehouse, data lake, lakehouse
    tabla-de-eventos           cómo se registra lo que hace un usuario
    ficha: motores analíticos
  Ingesta-y-transformacion/    panorama
    ingesta                    por lotes, en flujo, copiar cambios
    etl-y-elt                  transformar antes o después de cargar
    orquestacion               encadenar y programar los pasos
    ficha: herramientas de pipeline
  Gobierno-y-calidad/          panorama
    calidad-de-datos           qué es un dato malo y cómo se detecta
    metadatos-y-linaje         de dónde sale cada número
    datos-maestros             un cliente es uno solo en todos los sistemas
    privacidad-de-datos-personales   Ley 25.326, con dos fuentes
  Analisis/                    hondo
    analisis.md                el proceso: pregunta, preparar, limpiar, analizar, comunicar, actuar
    tipos-de-analitica         descriptiva, diagnóstica, predictiva, prescriptiva
    pregunta-de-analisis       una pregunta que los datos pueden contestar
    limpieza-de-datos
    sql-para-analisis          el grano y para qué usa el analista cada pieza; el lenguaje, en Bases-de-datos/SQL/
    analisis-exploratorio
    segmentacion-de-clientes
    ficha: planilla, SQL, Python
  Estadistica/                 hondo
    estadistica-descriptiva    centro, dispersión, distribución
    muestreo-e-inferencia      intervalos, p-valor
    correlacion-y-causalidad
    sesgos                     Simpson, supervivencia, selección
    significancia              frecuentista y bayesiana; el A/B queda en Producto
  Analitica-de-producto/       hondo
    definicion-de-metrica      KPI, árbol de métricas, métricas de vanidad
    embudo
    Cohortes/, Retencion-y-churn/, Lectura-de-cohortes/   las notas que ya estaban
  Visualizacion-y-BI/          hondo
    elegir-un-grafico
    tablero
    capa-semantica             una métrica, una sola definición
    contar-con-datos
    ficha: herramientas de BI
    BI-sobre-software-de-gestion/   el BI con los datos de un sistema de gestión (ampliación 2026-11-27)
      extraer-de-un-sistema-de-gestion, hechos-de-gestion, dimensiones-conformadas,
      historia-en-el-bi-de-gestion, varias-fuentes-de-gestion, multiempresa-y-moneda-en-el-bi,
      bi-de-gestion-en-argentina, conciliar-el-bi
  Fundamentos/
    roles-de-datos             analista, analytics engineer, ingeniero, científico, BI
    bibliografia-de-datos      bibliografía del tema
    ruta-de-data-analytics     orden para aprender, con ejercicios
    recorrido-analisis-de-cohortes   el que ya estaba
```

## Supuestos

- Un solo tema y no dos: gestión e ingeniería de datos y análisis comparten el recorrido del dato.
  Se parte en dos si la ingeniería crece y tiene otros lectores.
- Las notas de cohortes se movieron a `Analitica-de-producto/` sin cambiar su contenido. Las rutas
  guardadas fuera del repo (por ejemplo, en el Marco) quedan con la ruta vieja.
- Se planeó en dos PRs (primero análisis, después ingeniería), pero las notas de análisis enlazan a
  las de ingeniería y el primero habría quedado con enlaces rotos: va en un PR con dos commits.

## Ampliación: BI sobre el software de gestión

Sesión 15 del mapa «el mundo del software de gestión» (issue #94; ticket #122). Las decisiones de
ese mapa (#95 y #101) ponen la inteligencia de negocio sobre el software de gestión en Datos y no
en un tema propio, y #100 fija el límite con la columna de reportes de Software de gestión. Va como
subcarpeta de Visualización y BI, con una entrada y ocho notas, porque aplica todas las verticales
de Datos a una fuente concreta y sus componentes se enlazan entre sí; no es una vertical nueva del
tema, que sigue dividido por el recorrido del dato.

### Límites con los vecinos

Esta parte es dueña de **lo que se hace con los datos de un sistema de gestión para decidir**:
sacarlos a una copia, modelarlos en hechos y dimensiones, guardarles la historia, juntarlos con
otras fuentes, convertir empresas y monedas y conciliarlos con el sistema y el balance.

| Vecino | Es dueño de | La frontera con esta parte |
|---|---|---|
| [Software de gestión](../Software-de-gestion/software-de-gestion.md), columna de [reportes operativos y legales](../Software-de-gestion/Columnas-tecnicas/reportes-operativos-y-legales.md) | lo que el sistema saca de su propia base y tiene que entregar: listados del día, libros legales con corte a una fecha | Allá, lo que el sistema no puede dejar de producir por sí mismo; acá, lo que junta fuentes o historia, o corta de otra forma que la del sistema |
| Software de gestión, demás columnas técnicas | cómo está hecho el sistema: documentos y estados, registro de movimientos, fechas de bloqueo, monedas, estructura de la organización, integración | Allá, cómo guarda el sistema el dato; acá, cómo se lee ese dato para analizarlo |
| Temas de Gestión de la empresa (Contabilidad, Tesorería, Inventario, Compras, Servicios profesionales, Producción, Procesos de negocio y los demás) | qué mide cada dominio: margen, DSO, rotación, OTIF, utilización, OEE, días de cierre; la norma contable (moneda extranjera, consolidación, ajuste por inflación) | Allá se define cada indicador y cada regla, una sola vez; acá se enlazan y se dice qué hecho los alimenta |
| [Comercio electrónico](../Comercio-electronico/comercio-electronico.md) | la integración del sistema con la tienda y los marketplaces | Allá, qué viaja entre sistemas para operar; acá, cómo se juntan para analizar |
| [Planillas de cálculo](../Planillas-de-calculo/planillas-de-calculo.md) | la planilla como herramienta | Allá, cómo se arma; acá, la planilla como fuente del BI |

### Supuestos

- La ubicación (subcarpeta de Visualización y BI y no vertical de Datos) se decidió en esta sesión
  sin preguntar, porque #95 hablaba de «una vertical» y el ticket pide sumar a
  `Datos/Visualizacion-y-BI`. Queda para revisar en el PR.
- Lo de la Argentina va en una nota aparte (`bi-de-gestion-en-argentina`), que enlaza a
  Contabilidad para la norma en lugar de repetirla.
- Los informes de la investigación están en `.investigacion/bi-gestion-*.md`.
