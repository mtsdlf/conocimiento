---
resumen: >-
  Un arquetipo de Maven es una plantilla de proyecto que `mvn archetype:generate` copia y completa
  con parámetros, para que todos los proyectos nuevos arranquen con la misma estructura.
estado: borrador
estabilidad: estable
revisado:
creado: 2026-10-03
fuentes:
  - "Apache Maven, Guide to Creating Archetypes: https://maven.apache.org/guides/mini/guide-creating-archetypes.html"
  - "Apache Maven, Archetype Descriptor Model: https://maven.apache.org/archetype/archetype-models/archetype-descriptor/archetype-descriptor.html"
  - "Apache Maven, Maven Archetype Plugin, Advanced usage: https://maven.apache.org/archetype/maven-archetype-plugin/advanced-usage.html"
aliases: [Maven archetype, Archetype, Plantilla de proyecto Maven]
---

# Arquetipo de Maven

Un arquetipo de Maven es una plantilla de proyecto que `mvn archetype:generate` copia y completa
con parámetros, para que todos los proyectos nuevos arranquen con la misma estructura.

Es la implementación para Java de la [plantilla de proyecto](plantilla-de-proyecto.md), del tipo que
copia una vez.

## Los recursos, el descriptor y el post-generate

Un arquetipo es un artefacto Maven con dos partes:

- **`archetype-resources/`**: los archivos que se copian. Si un fileSet tiene `filtered="true"`,
  sus archivos se procesan como plantillas de Velocity, y `${groupId}`, `${artifactId}`,
  `${package}` o cualquier propiedad propia se reemplazan por su valor.
- **`META-INF/maven/archetype-metadata.xml`**: el descriptor. Lista los fileSets y las
  `requiredProperties`, cada una con su `defaultValue` opcional y, desde la versión 1.1.0 del
  descriptor, un `validationRegex`.

El descriptor decide dónde va cada archivo. Un fileSet con `packaged="true"` se copia debajo de la
ruta del paquete: `src/main/java/com/ejemplo/productos/…`. Un nombre de archivo o carpeta con el
patrón `__propiedad__` se reemplaza por el valor de la propiedad: con `-DEntidad=Producto`,
`__Entidad__Service.java` pasa a `ProductoService.java`. Un fileSet con `packaged="false"` se
copia sin la ruta del paquete, para archivos de la raíz como el `README` o el `.gitignore`; que
se procese como plantilla o no lo decide `filtered`, aparte.

Desde maven-archetype-plugin 3.0.0, un script `META-INF/archetype-post-generate.groovy` corre al
final de la generación. Recibe el objeto `request` (con el directorio de salida, el paquete y las
propiedades) y puede renombrar, borrar o reescribir archivos. Es el lugar para lo que una plantilla
no resuelve sola, como [derivar nombres de clase a partir del `artifactId`](derivar-nombres-en-un-arquetipo-de-maven.md).

En un proyecto multimódulo, el arquetipo trae un `pom.xml` padre y un fileSet por módulo; el
paquete de cada módulo puede incluir su capa (`com.ejemplo.productos.dominio`).

## Generar el servicio productos

```bash
mvn archetype:generate \
  -DarchetypeGroupId=com.ejemplo -DarchetypeArtifactId=servicio-archetype -DarchetypeVersion=1.0.0 \
  -DgroupId=com.ejemplo -DartifactId=productos -Dpackage=com.ejemplo.productos
```

Genera un proyecto `productos/` con su `pom.xml`, las clases base en `com/ejemplo/productos/` y la
configuración común del equipo.

## Arquetipo y proyecto padre

Un proyecto padre (`<parent>` en el `pom.xml`) no es lo mismo: el padre se hereda y sus cambios llegan a todos
los hijos en la próxima versión; el arquetipo se copia una sola vez, y lo generado ya no se
actualiza solo.
