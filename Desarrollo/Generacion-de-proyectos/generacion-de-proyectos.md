---
resumen: >-
  Generación de proyectos es la parte del desarrollo que hace que un servicio nuevo salga de una
  plantilla versionada, con la estructura, las dependencias y los archivos base del equipo.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Generación de proyectos

Generación de proyectos es la parte del desarrollo que hace que un servicio nuevo salga de una
plantilla versionada, con la estructura, las dependencias y los archivos base del equipo.

Dentro de [Desarrollo](../desarrollo.md), recibe de [Especificación y prueba](../Especificacion-y-prueba/especificacion-y-prueba.md)
qué hay que construir y entrega un proyecto con la configuración común del equipo, que sigue en
[Configuración](../Configuracion/configuracion.md) y se versiona en [Git](../Git/git.md). Un arquetipo es la
plantilla de un [golden path](../../Platform-Engineering/Plataforma-interna/golden-path.md) para servicios Java.

## Plantilla que se copia una vez

Sin plantilla, cada servicio nuevo copia otro existente y arrastra lo que tenga de más o de menos.
Un arquetipo de Maven fija todo en un solo lugar y un proyecto nuevo sale con un comando: copia los
archivos, los completa con parámetros y, al final, puede correr un script para lo que la plantilla
no resuelve sola. Lo generado ya no se actualiza solo; en eso se diferencia de un proyecto padre,
cuyos cambios llegan a todos los hijos.

## Las dos notas de generación de proyectos

- [Arquetipo de Maven](arquetipo-de-maven.md) — qué es una plantilla de proyecto de Maven y cómo se parametriza;
  leerla antes de armar una plantilla para servicios nuevos.
- [Derivar nombres en un arquetipo de Maven](derivar-nombres-en-un-arquetipo-de-maven.md) — pasos para generar nombres de clase a partir del
  `artifactId`.
