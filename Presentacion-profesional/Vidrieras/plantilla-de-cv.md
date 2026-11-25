---
resumen: >-
  Un esqueleto de CV en Markdown, para copiar y llenar desde el inventario profesional, con un
  comentario en cada parte que dice qué va y por qué.
estado: borrador
estabilidad: volatil
fuentes:
  - "Harvard OCS: https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/"
  - "MIT CAPD: https://capd.mit.edu/resources/resumes/"
  - "Workday, resume parsing: https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html"
  - "Presentacion-profesional/.investigacion/vidrieras.md"
aliases: [modelo de CV, template de CV, formato de CV]
creado: 2026-11-24
revisado:
---

# Plantilla de CV

Un esqueleto de CV en Markdown, para copiar y llenar desde el inventario profesional, con un
comentario en cada parte que dice qué va y por qué.

Implementa lo que explica [CV](cv.md): formato estándar, orden por importancia, texto plano que un
ATS pueda parsear. Se llena con lo que sale de [adaptar por puesto](adaptar-por-puesto.md), y antes
de mandarlo se pasa la [revisión antes de mandar](revision-antes-de-mandar.md). Los comentarios
`<!-- -->` se borran al exportar.

## Por qué Markdown

Un CV escrito en texto plano se versiona en git, se adapta copiando el archivo y se exporta a PDF
o Word con cualquier conversor. Además obliga a lo que pide la documentación de los ATS: sin
imágenes ni estilos hechos con imágenes, que según Workday empeoran el parseo. Si el CV final se
arma en otro programa, el orden y los comentarios sirven igual.

## El esqueleto

```markdown
# Nombre Apellido
<!-- Tu nombre como querés que te busquen. Nada más en esta línea: ni foto, ni edad, ni
     estado civil, ni documento. Si te postulás a un país donde se espera foto, mirá
     cv-por-pais.md antes de ponerla. -->

Ciudad, País · correo@ejemplo.com · +54 9 11 0000-0000 · linkedin.com/in/usuario · github.com/usuario
<!-- Contacto completo en una línea de texto (no en el encabezado del documento ni en una
     imagen). La ciudad sirve para filtros de ubicación; para remoto, sumá la zona horaria. -->

Cargo al que apuntás. Dos o tres líneas sobre qué hacés, en qué sos fuerte y qué buscás.
<!-- Opcional. Si lo ponés, reescribilo para cada puesto: es lo primero que se lee y lo que
     más se nota cuando está copiado de otra versión. Sin adjetivos que no se puedan probar
     ("apasionado", "proactivo"); mejor un hecho. -->

## Experiencia
<!-- Va primero si tenés experiencia en el área. Orden cronológico inverso: lo último arriba.
     Si venís de estudiar o cambiás de área y lo más fuerte son proyectos, poné Proyectos
     antes (Harvard: secciones "in order of importance"). -->

### Cargo — Empresa · Ciudad o Remoto · mes año – mes año
<!-- El cargo como figura en el contrato, o el que lo describe mejor si el interno es raro.
     Fechas con mes: los huecos se explican, no se esconden (ver huecos-y-cambios-de-carrera.md). -->

- Logro que prueba algo que el puesto pide: qué hiciste, cómo y qué cambió.
- Otro logro, con número solo si el número es verificable y dice algo.
- Uno más. Tres a cinco por puesto reciente; uno o dos por los viejos.
<!-- Logros, no tareas: "Migré X a Y y bajó el tiempo de despliegue de horas a minutos",
     no "Responsable de despliegues". Salen del inventario; ver logros.md para cuándo
     ponerle número. El más relevante para este puesto, arriba. -->

### Cargo anterior — Empresa · mes año – mes año

- Logro.

## Proyectos
<!-- Lo que muestra trabajo verificable: un repositorio, una contribución aceptada, algo en
     producción. Enlazá el proyecto concreto, no tu perfil en general. Ver portfolio-y-github.md. -->

### Nombre del proyecto · enlace

- Qué problema resuelve, qué hiciste vos y con qué. Una o dos líneas.

## Habilidades
<!-- Las que podés defender en una entrevista, con los nombres que usa el aviso cuando
     describen lo mismo. Agrupadas (lenguajes, infraestructura, datos...), en texto plano,
     sin barras de nivel ni estrellas: no se parsean y no dicen nada verificable.
     Ver habilidades-y-palabras-clave.md. -->

- Lenguajes: …
- Herramientas: …
- Idiomas: Español (nativo), Inglés (nivel)

## Educación
<!-- Título, institución, año. Va al final si tenés experiencia; arriba si recién te
     recibís. Los cursos entran solo si prueban algo que el puesto pide. -->

- Título — Institución · año
```

## Lo que la plantilla deja afuera a propósito

- **Foto y datos personales**: no van por defecto. Cuándo sí, según el país, está en
  [CV por país](cv-por-pais.md).
- **Referencias**: Harvard y MIT coinciden en no incluirlas; se dan cuando las piden.
- **Columnas, tablas, íconos y gráficos de nivel**: la documentación oficial de los ATS no nombra
  las columnas ni las tablas, pero sí pide evitar imágenes. Una sola columna de texto evita el
  problema sin tener que averiguar qué sistema usa cada empleador.
- **Largo**: no hay regla con evidencia. El criterio de MIT es una página salvo experiencia extensa
  o posgrado; lo que importa es que lo de arriba sea lo más relevante para el puesto. La evidencia
  sobre el largo es floja y está en [CV](cv.md#una-página-o-dos-solo-hay-estudios-de-vendedores).

> [!NOTE]
> Sin fuente todavía: el orden exacto de las secciones. Harvard pide ordenarlas por importancia y
> MIT no fija un orden; el que propone la plantilla es la práctica más común, no un resultado medido.
