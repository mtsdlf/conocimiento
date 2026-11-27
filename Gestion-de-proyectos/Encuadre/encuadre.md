---
resumen: >-
  El encuadre fija qué resultado busca un proyecto, por qué vale la pena, qué entra y qué no, quién gana, quién pierde y quién decide, y cómo se va a saber que terminó.
estado: borrador
estabilidad: estable
fuentes:
  - "PMI, The Standard for Project Management and A Guide to the PMBOK, 8.ª ed. (2025), folleto e índice: https://www.pmi.org/-/media/pmi/documents/public/pdf/publications/pmbok-guide-eighth-edition_table-of-contents.pdf"
  - "DIN/Beuth, índice de ISO 21502:2020 (solo el índice): https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:334145134/toc-3233385/download"
  - "PRINCE2, resumen de principios en Wikipedia (secundaria): https://en.wikipedia.org/wiki/PRINCE2"
  - "Flyvbjerg (2014), What You Should Know About Megaprojects and Why: https://arxiv.org/abs/1409.0003"
  - "Anthropic, Effective harnesses for long-running agents: https://anthropic.com/engineering/effective-harnesses-for-long-running-agents"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
  - "Gestion-de-proyectos/.investigacion/fundamentos.md"
aliases: [encuadre del proyecto, project framing, definición del proyecto, inicio del proyecto, project initiation]
creado: 2026-11-27
revisado:
---

# Encuadre

El encuadre fija qué resultado busca un proyecto, por qué vale la pena, qué entra y qué no, quién gana, quién pierde y quién decide, y cómo se va a saber que terminó.

Es la primera vertical de la [gestión de proyectos](../gestion-de-proyectos.md) y la que alimenta a todas las demás. Le pasa a [Enfoque](../Enfoque/enfoque.md) cuánto se sabe del resultado, que es lo que decide cómo organizar el trabajo. Le da a [Planificación](../Planificacion/planificacion.md) el alcance que hay que partir y pronosticar. Y le da a [Gobierno y cierre](../Gobierno-y-cierre/gobierno-y-cierre.md) la vara contra la que se decide seguir, cambiar o parar: la cancelación debería apoyarse en que el encuadre dejó de sostenerse (criterio de esta base, sin fuente que lo pruebe).

## Cinco preguntas que se contestan antes de ejecutar

El encuadre contesta cinco preguntas, y cada una tiene su nota:

| Pregunta | Qué deja escrito | Nota |
|---|---|---|
| ¿Por qué este trabajo y no otro? | El caso: costo, beneficio esperado y la condición bajo la cual deja de valer | [justificación](justificacion.md) |
| ¿Qué tiene que ser verdad al final? | El resultado como algo comprobable, con su criterio de terminado | [resultado y terminado](resultado-y-terminado.md) |
| ¿Qué entra y qué no? | La lista de lo incluido, la de lo excluido y qué queda fijo | [alcance](alcance.md) |
| ¿A quién afecta y quién decide? | Quién gana, quién pierde, quién puede frenar y quién aprueba | [interesados](interesados.md) |
| ¿Cómo se sabe que terminó? | La evidencia que va a mostrar que el resultado se logró | [resultado y terminado](resultado-y-terminado.md) |

Los marcos reparten estas preguntas de distinto modo. La 8.ª edición del PMBOK tiene alcance e interesados como dominios de desempeño propios; no tiene un dominio de justificación, y el valor aparece como uno de sus seis principios ("Focus on Value"). PRINCE2 las trata como principios: justificación continua del negocio y foco en los productos, según el resumen de Wikipedia. ISO 21502 pone el caso de negocio dentro del gobierno del proyecto (cláusula 4.3.2) y separa la justificación inicial (6.5) de la justificación progresiva (6.6), según su índice. Cómo divide el campo cada marco está en [marcos de referencia](../Fundamentos/marcos-de-referencia.md).

## El encuadre se revisa, no se firma una vez

Un encuadre escrito al principio y archivado no sirve para gobernar. La justificación se vuelve a mirar en cada [punto de control](../Enfoque/etapas-y-puntos-de-control.md), y el alcance cambia por [control de cambios](../Seguimiento/control-de-cambios.md), no en silencio. ISO 21502 lo dice con la palabra "progresiva": la justificación acompaña al proyecto mientras dura.

El caso más claro de por qué hay que revisarlo viene de los megaproyectos. Según Flyvbjerg, sus casos de negocio se apoyan en costos subestimados y beneficios sobreestimados. La causa de esos desvíos está en disputa, y también la eficacia de corregirlos con clase de referencia. Un encuadre que no corrige ese sesgo con datos de proyectos parecidos promete más de lo que va a dar: el remedio está en [pronóstico](../Planificacion/pronostico.md) y la evidencia, en [por qué fallan los proyectos](../Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md).

## Cómo falla un encuadre

- **Una lista de actividades en lugar de un resultado.** "Migrar los servidores" dice qué se hace; "el servicio atiende desde la plataforma nueva con la misma latencia" dice qué tiene que ser verdad. Con la primera se puede terminar todo y no haber logrado nada.
- **Un alcance sin lo excluido.** Lo que no se escribió como afuera se va a pedir como adentro.
- **Interesados sin mapa.** Quien pierde con el proyecto y no fue tenido en cuenta aparece tarde, cuando frenarlo cuesta más.
- **Un caso de negocio optimista que nadie vuelve a leer.** El proyecto sigue aunque las razones que lo justificaban ya no se cumplan, y cancelarlo se vuelve difícil ([cerrar o cancelar](../Gobierno-y-cierre/cerrar-o-cancelar.md)).

## Qué cambia cuando ejecutan agentes

Lo que sigue es inferencia de esta base, salvo la práctica de Anthropic que se cita. Cuando un agente ejecuta, el encuadre pasa a ser también la instrucción. Un agente no pregunta en el pasillo qué se quiso decir: hace lo que el encargo permite leer y declara haber terminado cuando cree que lo logró. Por eso el criterio de terminado tiene que poder comprobarse sin interpretar, y tiene que quedar fuera del alcance de quien ejecuta. Anthropic describe una práctica así: una lista de funcionalidades que arrancan todas como fallidas y que el agente solo puede marcar como logradas, sin editar las pruebas. El detalle está en [resultado y terminado](resultado-y-terminado.md), y cómo se arma el encargo para un agente, en [delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md).

La justificación también cambia, según una inferencia de esta base sin fuente que la pruebe: si ejecutar se abarata, el costo que pesa en el caso de negocio pasa a ser el de especificar, revisar y aceptar.

## Qué hay adentro del encuadre

- [Justificación](justificacion.md) — por qué este trabajo y no otro, qué beneficio se espera y en qué momento deja de valer la pena; leerla antes de comprometer recursos y en cada punto de control.
- [Resultado y terminado](resultado-y-terminado.md) — cómo escribir el resultado como algo comprobable y no como una lista de actividades, y qué cambia cuando quien declara "terminado" es un agente.
- [Alcance](alcance.md) — qué entra, qué no, qué queda fijo como línea base y qué se deja variar.
- [Interesados](interesados.md) — quién gana, quién pierde, quién puede frenar el proyecto y quién decide, y qué tan poco se sabe de que gestionarlos mejore el resultado.

Si el proyecto es software para un cliente, el acuerdo inicial, el alcance y la aceptación con el cliente están en [Encargo](../../Desarrollo/Encargo/encargo.md).
