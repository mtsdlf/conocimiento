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
