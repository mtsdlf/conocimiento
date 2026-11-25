---
resumen: >-
  Una plantilla en Markdown para llevar el inventario profesional: una sección por período y una
  ficha por entrada, con preguntas para llenar cada campo. Está basada en la plantilla de brag
  document de Julia Evans, adaptada a lo que necesitan las vidrieras.
estado: vigente
estabilidad: semi
fuentes:
  - "Julia Evans, Get your work recognized: write a brag document: https://jvns.ca/blog/brag-documents/"
  - "Yale OCS, Writing Impactful Resume Bullets: https://ocs.yale.edu/resources/writing-impactful-resume-bullets/"
  - "Presentacion-profesional/.investigacion/material.md (secciones 1 y 2)"
aliases: [plantilla de brag document, plantilla de master resume]
creado: 2026-11-24
revisado: 2026-11-24
---

# Plantilla de inventario

Una plantilla en Markdown para llevar el inventario profesional: una sección por período y una
ficha por entrada, con preguntas para llenar cada campo. Está basada en la plantilla de brag
document de Julia Evans, adaptada a lo que necesitan las vidrieras.

Implementa el [inventario profesional](inventario-profesional.md). De Evans toma las secciones
(proyectos, colaboración, diseño y documentación, aprendizaje, fuera del trabajo) y la regla de
anotar el resultado después del lanzamiento. Le suma, en cada entrada, los campos que después
piden los [logros](logros.md) y las [habilidades y palabras clave](habilidades-y-palabras-clave.md):
contexto, qué hiciste vos, resultado y cómo se sabe, evidencia y palabras del campo. Evans
también trae preguntas para cuando uno se traba; las de «Si te trabás» son una versión propia,
pensada para trabajo de tecnología.

## Cómo usarla

1. Copiá el bloque de abajo en un archivo privado (no en un repositorio público: va a tener cosas
   de tus empleadores).
2. Elegí una frecuencia y anotala arriba. Evans prefiere una sesión cada seis meses o cada año;
   otros, cada dos semanas. Probá y quedate con la que sostengas.
3. Abrí una entrada cuando empieza algo que importa, no cuando termina. Dejá `Resultado` en
   `pendiente` y volvé después del lanzamiento.
4. Para una búsqueda, no edites el inventario: copiá las entradas que sirven y redactalas como
   logros en la vidriera ([adaptar por puesto](../Vidrieras/adaptar-por-puesto.md)).

## La plantilla

```markdown
# Inventario profesional

Frecuencia de revisión: <cada 2 semanas | cada 6 meses | otra>
Última revisión: AAAA-MM-DD

## Hacia dónde voy

- ¿Qué querés estar haciendo dentro de uno o dos años? ¿Qué tipo de puesto?
- ¿Qué evidencia te falta para ese puesto? (Revisalo contra avisos reales.)

## <Período: AAAA-S1, o empleador y años>

### <Nombre corto de la entrada>

- **Fechas**: AAAA-MM a AAAA-MM
- **Contexto**: ¿En qué equipo, sistema o producto? ¿Qué problema había y por qué importaba?
  ¿Qué tamaño tenía (usuarios, tráfico, datos, cantidad de servicios)?
- **Qué hice yo**: ¿Qué parte fue tuya y qué parte del equipo? ¿Qué decidiste, qué
  construiste, qué propusiste? Escribilo con verbos en primera persona.
- **Resultado y cómo se sabe**: ¿Qué cambió? Si hay número: ¿de cuánto a cuánto, medido cómo?
  Si no hay: ¿qué alcance tuvo, quién lo usa ahora, qué se dejó de hacer, cómo era antes y cómo
  es ahora? Si todavía no se sabe, poné `pendiente` y una fecha para volver.
- **Evidencia**: ¿Qué enlace, documento, PR, charla o persona (por su rol) lo confirma? ¿Se
  puede mostrar en público o es confidencial?
- **Palabras del campo**: ¿Qué tecnologías, prácticas y conceptos usaste, con el nombre que
  aparece en los avisos?
- **Lo que aprendí**: ¿Qué sabés hacer ahora que antes no?

## Colaboración y mentoría

- ¿A quién ayudaste a crecer, a quién incorporaste, qué revisiones o pares hiciste?
- ¿Qué cambió para esa persona o ese equipo?

## Diseño y documentación

- ¿Qué documentos de diseño, guías, RFCs o runbooks escribiste? ¿Quién los usa?

## Mejoras que no son un proyecto

- Para el trabajo difuso (calidad, procesos, cultura): ¿cuál era la meta, qué acciones tomaste
  y qué efectos observaste?

## Fuera del trabajo

- Posts, charlas, open source, cursos con entregable, proyectos propios. Con enlace.

## Huecos y giros

- Períodos sin empleo o cambios de área: fechas, qué hiciste en ese tiempo y qué se puede probar.

## Si te trabás

- ¿Qué problema arreglaste que nadie te pidió?
- ¿Qué te preguntan los demás porque sabés hacerlo?
- ¿Qué incidente ayudaste a resolver o a que no se repita?
- ¿Qué te agradecieron en una revisión, un chat o una retro?
- ¿Qué decisión tomaste que, mirada hoy, salió bien? ¿Y una que salió mal y de la que aprendiste?
```

## Cómo se llena bien una entrada

La regla es la de Evans: «make it sound exactly as good as it is». Un resultado sin número está
bien; uno con número inventado no, porque el inventario es la fuente de lo que vas a contestar en
una entrevista. El criterio para decidir si un número entra está en [logros](logros.md).

> [!NOTE] Sin fuente todavía: no hay estudio que compare plantillas de inventario ni que muestre
> que alguna rinde más. Esta es una adaptación de práctica, no un formato validado.
