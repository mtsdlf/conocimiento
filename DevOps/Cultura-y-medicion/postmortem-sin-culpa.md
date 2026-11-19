---
resumen: >-
  Un postmortem sin culpa es el registro escrito de un incidente que busca sus causas para
  mejorar el sistema, sin señalar a ninguna persona ni equipo como culpable.
estado: borrador
estabilidad: estable
fuentes:
  - "Betsy Beyer y otros, Site Reliability Engineering (Google), cap. 15 Postmortem Culture: Learning from Failure: https://sre.google/sre-book/postmortem-culture/"
  - "Archivo/DevOps/devops-referencia.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-organizational-topology.md (original, texto generado con IA)"
aliases: [Blameless postmortem, Postmortem, Revisión post-incidente]
creado: 2026-10-03
revisado:
---

# Postmortem sin culpa

Un postmortem sin culpa es el registro escrito de un incidente que busca sus causas para
mejorar el sistema, sin señalar a ninguna persona ni equipo como culpable.

## Por qué culpar frena el aprendizaje

Según el libro de SRE de Google, si en una organización se señala y avergüenza a quien "hizo
lo incorrecto", la gente deja de reportar problemas por miedo al castigo. Sin reportes no hay
aprendizaje, y el mismo incidente se repite. Por eso el postmortem sin culpa es la práctica
central de las dimensiones Culture y Sharing de [CALMS](../Fundamentos/calms.md).

## Cuándo se escribe y quién lo escribe

Google define el postmortem como el registro de un incidente, su impacto, las acciones para
mitigarlo, sus causas y las acciones de seguimiento para que no se repita. Que sea sin culpa
significa suponer que cada persona actuó con buena intención y con la información que tenía.

Se escribe cuando el incidente supera un umbral acordado de antemano. Google da como ejemplos:

- caída o degradación visible para los usuarios por encima de un límite;
- cualquier pérdida de datos;
- una intervención de la guardia (la persona de turno, on-call, que atiende alertas), como un rollback o un desvío de tráfico;
- una resolución que tardó más de lo definido;
- una falla del monitoreo que obligó a descubrir el problema a mano.

Lo escriben quienes atendieron el incidente, en los días siguientes a resolverlo. Cada acción
de seguimiento tiene dueño y fecha, y el documento se comparte para que otros
equipos aprendan. Si el cambio que causó el incidente está en Git, el postmortem enlaza el
commit y el revert.

## Una tabla borrada sin culpar a Juan

Un despliegue borra una tabla de configuración. El postmortem no concluye "Juan corrió el script
equivocado", sino que el script se podía correr contra producción sin confirmación y que no
había respaldo probado. Las acciones son una confirmación obligatoria y una prueba de restore
mensual.

## Error humano no es una causa

Un análisis de causa raíz buscando un responsable. Un incidente casi nunca tiene una sola causa,
y "error humano" no es una causa sino el punto donde empieza la pregunta de por qué el sistema
permitió ese error.
