---
tipo: como-hacer
resumen: >-
  Cómo generar nombres de clase (Pascal, camel, snake) a partir del `artifactId` en un arquetipo
  de Maven, sea por parámetros o con un script post-generate en Groovy.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Apache Maven, Archetype Descriptor Model: https://maven.apache.org/archetype/archetype-models/archetype-descriptor/archetype-descriptor.html"
  - "Apache Maven, Maven Archetype Plugin, Advanced usage: https://maven.apache.org/archetype/maven-archetype-plugin/advanced-usage.html"
  - "Apache JIRA, ARCHETYPE-406, Support of velocity expressions for user-defined properties: https://issues.apache.org/jira/browse/ARCHETYPE-406"
aliases: [Nombres de clase en un arquetipo, archetype-post-generate.groovy]
parte_de: [arquetipo-de-maven]
requiere: []
relacionado: []
---

# Derivar nombres en un arquetipo de Maven

Cómo generar nombres de clase (Pascal, camel, snake) a partir del `artifactId` en un arquetipo
de Maven, sea por parámetros o con un script post-generate en Groovy.

## Antes de empezar

- Entender cómo un arquetipo copia y filtra archivos: [Arquetipo de Maven](arquetipo-de-maven.md).
- El objetivo: con `-DartifactId=orden-de-compra-api`, que el proyecto traiga
  `OrdenDeCompraService.java`, la variable `ordenDeCompra` y la tabla `orden_de_compra`.
- Un `defaultValue` del descriptor acepta expresiones de Velocity sobre otras propiedades (sobre
  propiedades propias, desde el plugin 3.2.1), pero pasar de kebab-case a PascalCase con varias
  palabras no entra cómodo en una expresión. Por eso hay dos caminos.

## Pasos

**Opción A: pedir los nombres como parámetros.** Es la más simple y no tiene código.

1. Declará las propiedades en `archetype-metadata.xml`, sin valor por defecto, para que Maven las
   pida: `<requiredProperty key="Entidad"/>` y `<requiredProperty key="entidad"/>`.
2. Nombrá los archivos de ejemplo con el token: `__Entidad__Service.java`, y usá `${Entidad}` y
   `${entidad}` en el contenido.
3. Generá pasando los valores: `-DEntidad=OrdenDeCompra -Dentidad=ordenDeCompra`.

**Opción B: derivarlos en el post-generate.** Es automática, a cambio de un script.

1. En las plantillas, usá marcadores que Velocity no toque: `__ENTIDAD__Service.java` en los
   nombres de archivo y `%%ENTIDAD_PASCAL%%`, `%%ENTIDAD_CAMEL%%`, `%%ENTIDAD_SNAKE%%` en el
   contenido.
2. Creá `src/main/resources/META-INF/archetype-post-generate.groovy` (va en `META-INF`, no en
   `archetype-resources`). El script quita del `artifactId` el sufijo de capa (`-api`,
   `-dominio`, `-sistema`; ajustalo a tus capas) y renombra archivos, no carpetas:

   ```groovy
   import java.nio.file.*
   import java.util.stream.Collectors

   def base = request.artifactId.replaceAll(/(?i)-(api|dominio|sistema)$/, '')
   def palabras = base.split(/[^A-Za-z0-9]+/).findAll { it }*.toLowerCase()
   def pascal = palabras*.capitalize().join('')
   def camel = palabras.head() + palabras.tail()*.capitalize().join('')
   def snake = palabras.join('_')

   def raiz = Paths.get(request.outputDirectory, request.artifactId)
   def archivos = Files.walk(raiz).filter { Files.isRegularFile(it) }.collect(Collectors.toList())
   archivos.each { p ->
       def nombre = p.fileName.toString()
       if (nombre =~ /\.(java|ya?ml|properties|xml|sql|md)$/) {
           def texto = new String(Files.readAllBytes(p), 'UTF-8')
               .replace('%%ENTIDAD_PASCAL%%', pascal)
               .replace('%%ENTIDAD_CAMEL%%', camel)
               .replace('%%ENTIDAD_SNAKE%%', snake)
           Files.write(p, texto.getBytes('UTF-8'))
       }
       if (nombre.contains('__ENTIDAD__')) {
           Files.move(p, p.resolveSibling(nombre.replace('__ENTIDAD__', pascal)))
       }
   }
   ```

3. Instalá el arquetipo (`mvn install`) y generá un proyecto de prueba.

## Cómo saber que salió bien

En el proyecto generado, `grep -r '%%ENTIDAD\|__ENTIDAD__' .` no devuelve nada, existe
`src/main/java/com/ejemplo/ordendecompra/OrdenDeCompraService.java` (según el paquete elegido) y
el proyecto compila con `mvn verify`.

## Relaciones

- Parte de: [Arquetipo de Maven](arquetipo-de-maven.md) — una técnica dentro de un arquetipo.
