---
resumen: >-
  Personas y agentes es el modelo operativo de un trabajo en el que una parte la ejecutan agentes de IA: quién decide, quién ejecuta, quién verifica y quién responde, cuánta autonomía tiene cada agente y por dónde pasa el trabajo hasta que una persona lo acepta.
estado: borrador
estabilidad: estable
fuentes:
  - "Dell'Acqua et al. (2023), Navigating the Jagged Technological Frontier, HBS WP 24-013 (texto del PDF leído en parte): https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf"
  - "Feng, McDonald y Zhang (2025), Levels of Autonomy for AI Agents, arXiv 2506.12469 (abstract y resumen del HTML): https://arxiv.org/abs/2506.12469"
  - "Tomašev, Franklin y Osindero (2026), Intelligent AI Delegation, arXiv 2602.11865 (abstract y resumen de la primera mitad del HTML): https://arxiv.org/abs/2602.11865"
  - "Parasuraman y Manzey (2010), Complacency and bias in human use of automation, Human Factors 52(3) (abstract): https://pubmed.ncbi.nlm.nih.gov/21077562/"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [fábrica, fábrica de agentes, modelo operativo con agentes, human-AI teaming, equipos de personas y agentes]
creado: 2026-11-27
revisado:
---

# Personas y agentes

Personas y agentes es el modelo operativo de un trabajo en el que una parte la ejecutan agentes de IA: quién decide, quién ejecuta, quién verifica y quién responde, cuánta autonomía tiene cada agente y por dónde pasa el trabajo hasta que una persona lo acepta.

Es lo que a veces se llama "la fábrica" de agentes, contado en general: está pensado para cualquier equipo que mezcla personas y agentes, en cualquier dominio, aunque la evidencia que lo respalda es de pocos dominios (ver más abajo). Recibe de [Planificación](../Planificacion/planificacion.md) las piezas de trabajo y la [capacidad](../Planificacion/capacidad-y-costo.md) disponible. Entrega a [Seguimiento](../Seguimiento/seguimiento.md) lo producido, que se da por hecho con [aceptación con evidencia](../Seguimiento/aceptar-con-evidencia.md). Lo que un agente no puede resolver dentro de su tolerancia sube por [problemas y escalamiento](../Incertidumbre-y-riesgo/problemas-y-escalamiento.md).

Cómo funciona un agente por dentro, sus patrones técnicos y cómo falla están en el tema [IA](../../IA/Agentes/agentes.md). Delegar en personas está en [delegación](../../Liderazgo-y-direccion/Decidir/delegacion.md). Acá se mira lo que eso cambia en la organización del trabajo.

## El árbol es una síntesis de cuatro disciplinas

Ninguna fuente junta todo lo que cubre esta vertical. El campo está partido en factores humanos y automatización (niveles de autonomía, complacencia), economía del trabajo (frontera irregular, productividad), diseño de agentes (patrones) y gestión de proyectos clásica (matrices de responsabilidad). La división en siete notas es de esta base.

La evidencia también está concentrada. Los experimentos con método son de software, consultoría y atención al cliente. Aplicarlos a una mudanza de plataforma, un evento o una obra es una extrapolación, y cada nota lo marca.

## Tres decisiones que arman el modelo

Según el modelo de esta base, cada pieza de trabajo pasa por tres decisiones, en este orden:

1. **Si la ejecuta un agente.** Depende de si la tarea cae dentro de lo que el agente hace bien, y eso no se sabe de antemano: es la [frontera irregular](frontera-irregular.md). El largo de tarea que hoy completan los agentes da una cota, en la ficha de [horizonte de tareas](horizonte-de-tareas.md).
2. **Cómo se le encarga.** Un [encargo a un agente](delegar-a-un-agente.md) dice la intención, los límites, el criterio de terminado y el presupuesto.
3. **Cuánto decide solo.** El [nivel de autonomía](niveles-de-autonomia.md) fija cuándo el agente para y pregunta, y cuándo una persona solo mira lo que sale de lo previsto.

Detrás de las tres está [quién hace qué](quien-hace-que.md): para esta base, una persona con nombre responde por el resultado aunque lo ejecute un agente. Es un criterio de la base y no un hallazgo, armado a partir de un marco de delegación que no lo dice así.

## Por qué el control humano es lo más frágil

La respuesta habitual al riesgo de un agente es poner a una persona que revise. La evidencia consultada sugiere que eso no alcanza solo. Parasuraman y Manzey (2010) muestran, según su abstract, que la complacencia y el sesgo de automatización afectan a novatos y a expertos, y que la práctica no los elimina. En el experimento de Dell'Acqua y otros, los consultores con IA acertaron menos justo en la tarea que quedaba fuera de lo que la IA hacía bien.

De ahí sale el problema de capacidad de la vertical. Si los agentes producen más rápido de lo que las personas revisan, la [atención humana](la-atencion-humana-como-restriccion.md) se vuelve la restricción del sistema. Revisar todo no escala y revisar poco deja pasar errores. Los [patrones de trabajo](patrones-de-trabajo.md) son las formas de repartir hacer y revisar entre personas y agentes para que esa atención rinda.

## Lo que hay adentro de Personas y agentes

- [Quién hace qué](quien-hace-que.md) — los cuatro papeles (decidir, ejecutar, verificar, responder) y por qué responder queda en una persona.
- [Delegar a un agente](delegar-a-un-agente.md) — qué lleva un encargo: intención, límites, criterio de terminado y presupuesto.
- [Niveles de autonomía](niveles-de-autonomia.md) — cuánto decide el agente solo, la persona en el bucle o en el borde, y el sesgo de automatización.
- [Frontera irregular](frontera-irregular.md) — qué tareas dar a un agente cuando no se sabe de antemano dónde rinde; los estudios de Dell'Acqua y de METR.
- [Patrones de trabajo](patrones-de-trabajo.md) — orquestador y trabajadores, hacer y revisar, y otras formas de repartir el trabajo, vistas como organización.
- [La atención humana como restricción](la-atencion-humana-como-restriccion.md) — la revisión como cuello de botella y cómo se gestiona.
- [Horizonte de tareas](horizonte-de-tareas.md) — ficha: hasta qué largo de tarea completan hoy los agentes, según METR, copiada el 2026-11-27.
