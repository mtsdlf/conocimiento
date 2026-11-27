---
resumen: >-
  Gobierno y calidad es la parte de Datos que pone las reglas para que un dato sea confiable: quién
  responde por cada conjunto de datos, qué cuenta como un dato bueno, de dónde sale cada número, qué
  registro de un cliente o un producto es el que vale y qué permite la ley hacer con los datos de las
  personas.
estado: vigente
estabilidad: semi
fuentes:
  - "DAMA International, Body of Knowledge (solo la página institucional): https://www.dama.org/cpages/body-of-knowledge"
  - "DAMA International, DMBOK2R infographics: https://dama.org/dmbok2r-infographics/"
  - "DAMA-DMBOK2, cap. Data Governance (Technics Publications), no leído: https://technicspub.com/dmbok2"
  - "Joe Reis y Matt Housley, Fundamentals of Data Engineering, cap. 2 (O'Reilly, 2022), según el resumen del buscador: https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html"
  - "Gartner, Data quality (según el buscador): https://www.gartner.com/en/data-analytics/topics/data-quality"
  - "Datos/.investigacion/gobierno-y-privacidad.md"
  - "Datos/.investigacion/fundamentos.md"
  - "Datos/.investigacion/posicion-contraria.md"
aliases: [gobierno de datos, data governance, gestión de datos, data management, gobernanza de datos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Gobierno y calidad

Gobierno y calidad es la parte de Datos que pone las reglas para que un dato sea confiable: quién responde por cada conjunto de datos, qué cuenta como un dato bueno, de dónde sale cada número, qué registro de un cliente o un producto es el que vale y qué permite la ley hacer con los datos de las personas.

Corre al costado de todas las etapas del [recorrido del dato](../datos.md#del-hecho-registrado-a-la-decisión). Pone reglas a lo que guarda [Modelado y almacenamiento](../Modelado-y-almacenamiento/modelado-y-almacenamiento.md) y controla lo que mueve [Ingesta y transformación](../Ingesta-y-transformacion/ingesta-y-transformacion.md). El que más lo sufre cuando falta es el [Análisis](../Analisis/analisis.md): un tablero sobre una tabla con duplicados muestra un número falso con la misma seguridad que uno verdadero.

## El gobierno decide quién responde por cada dato

El gobierno de datos es el reparto de derechos y responsabilidades sobre los datos: quién decide qué significa un campo, quién lo puede cambiar y quién arregla un error. DAMA lo pone en el centro de su rueda de la gestión de datos, con las otras áreas (calidad, metadatos, datos maestros, seguridad, modelado, entre otras) alrededor. La página de infografías del DMBOK2 lista ese diagrama como «Data Governance and Stewardship». En el ciclo de Reis y Housley, la misma preocupación aparece como «gestión de datos», una de las seis que corren debajo de todas las etapas (según el resumen del buscador).

> [!NOTE]
> Sin fuente todavía: la definición literal de gobierno de datos de DAMA y la descripción de sus roles están en el capítulo 3 del DMBOK2, que es de pago y no se leyó.

## Un dueño y un cuidador por conjunto de datos

Los manuales describen comités, consejos y oficinas de datos pensados para empresas grandes. Una empresa chica no necesita nada de eso. Lo que sí necesita, a criterio de la base, son dos papeles por cada conjunto de datos importante (clientes, productos, ventas):

| Papel | Qué hace | En un comercio chico, por ejemplo |
|---|---|---|
| Dueño (*data owner*) | Decide qué significa el dato, quién lo ve y para qué se usa; responde si está mal | La persona que lleva la relación con los clientes, para la base de clientes |
| Cuidador (*data steward*) | Lo mantiene día a día: corrige errores, une duplicados, avisa cuando una regla no se cumple | Quien carga los productos, para el catálogo |

Puede ser la misma persona, y en un negocio de cinco personas casi siempre lo es. Lo que importa es que el nombre esté escrito: cuando nadie es dueño de la lista de clientes, cada canal crea la suya y nadie decide cuál vale (lectura de la base). Los roles técnicos que construyen el recorrido están en [roles de datos](../Fundamentos/roles-de-datos.md); estos dos no son puestos de trabajo sino responsabilidades que alguien del negocio asume.

> [!NOTE]
> Sin fuente todavía: los roles de dueño y cuidador no se verificaron en una fuente primaria. La tabla y el criterio de proporcionalidad son una propuesta de la base.

## Cómo se reparten las cuatro piezas

Las cuatro piezas de la vertical contestan cuatro preguntas que aparecen en ese orden cuando un número no cierra:

1. ¿El dato está bien? Es la [calidad de datos](calidad-de-datos.md): completo, único, consistente, a tiempo, válido y exacto, cada cosa comprobable con una consulta.
2. ¿De dónde salió? Son los [metadatos y el linaje](metadatos-y-linaje.md): qué significa cada columna, quién la mantiene y por qué pasos pasó antes de llegar al tablero.
3. ¿Cuál de los registros es el bueno? Son los [datos maestros](datos-maestros.md): un cliente o un producto tiene un solo registro que vale en todos los sistemas.
4. ¿Lo puedo guardar y usar? Es la [privacidad de los datos personales](privacidad-de-datos-personales.md): en Argentina, la Ley 25.326.

La calidad y la privacidad se tocan en un punto: la ley pide que los datos personales sean «ciertos, adecuados, pertinentes y no excesivos» (art. 4), o sea que la exactitud y la minimización son también obligaciones legales. Los datos maestros dependen del gobierno de manera directa: unir dos registros de un cliente exige que alguien decida cuál manda.

## Cómo falla el gobierno en un negocio chico

El error más común es el de sobra, no el de falta (lectura de la base). Copiar el aparato de una empresa grande (catálogo, comité, políticas escritas que nadie lee) consume el tiempo que haría falta para limpiar la lista de clientes. Las cifras que circulan sobre el costo de los datos malos tampoco sirven de argumento: la más citada, de Gartner, habla de «at least $12.9 million a year» de promedio, pero sale de una encuesta de 2020 a clientes de una consultora, empresas grandes, y no se traslada a un comercio (según el buscador). Para un negocio chico, alcanza con un dueño por conjunto de datos, un diccionario de las columnas que se usan en los tableros, unas pocas comprobaciones automáticas y saber qué dice la ley.

El error opuesto es dejar que cada planilla tenga su propia versión de «cliente» o de «venta». Ahí aparece lo que la [entrada del tema](../datos.md) llama el problema de fondo: dos personas calculan el mismo número con filtros distintos. La solución a la definición del número está en [definición de métrica](../Analitica-de-producto/definicion-de-metrica.md) y en la [capa semántica](../Visualizacion-y-BI/capa-semantica.md); la de esta vertical es que el dato debajo sea uno solo y esté bien.

## Qué hay adentro de gobierno y calidad

- [Calidad de datos](calidad-de-datos.md) — las seis dimensiones de un dato bueno y cómo se detecta un dato malo con tests de datos.
- [Metadatos y linaje](metadatos-y-linaje.md) — el diccionario de datos, el catálogo y el camino que siguió cada número.
- [Datos maestros](datos-maestros.md) — un registro que vale por cliente y por producto, y cómo se encuentran los duplicados.
- [Privacidad de datos personales](privacidad-de-datos-personales.md) — lo que la Ley 25.326 pide a quien guarda datos de clientes en Argentina; ley, para revisar con un abogado.
