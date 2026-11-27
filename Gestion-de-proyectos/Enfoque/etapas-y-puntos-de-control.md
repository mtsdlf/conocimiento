---
resumen: >-
  Las etapas y puntos de control parten un proyecto en tramos y, al final de cada uno, obligan a decidir con información nueva si se sigue, se cambia o se para. No es un enfoque más sino una capa de gobierno que se monta sobre cualquiera, predictivo, iterativo, de flujo o de apuesta.
estado: vigente
estabilidad: estable
fuentes:
  - "PRINCE2, principio de gestionar por etapas (según una guía de referencia rápida y Wikipedia; manual no leído): https://en.wikipedia.org/wiki/Managing_stage_boundaries"
  - "Cooper y Edgett (2012), Best practices in the idea-to-launch process and its governance, Research-Technology Management 55(2) (según la ficha): https://experts.mcmaster.ca/scholarly-works/319986"
  - "Cooper, artículo de 2002 sobre decisiones de puerta (según resumen del buscador): https://experts.mcmaster.ca/scholarly-works/319941"
  - "Cooper y Sommer (2016), The Agile-Stage-Gate Hybrid Model, JPIM 33(5) (ficha): https://experts.mcmaster.ca/display/publication319920"
  - "Baxter et al. (2022), crítica del stage-gate, Prometheus 38(2) (según resumen del buscador): https://eprints.soton.ac.uk/468604/"
  - "Cooper y Zhao (2026), New product governance in a time-compressed world, PDMA (según resumen): https://community.pdma.org/knowledgehub/bok/product-innovation-process/new-product-governance-in-a-time-compressed-world"
  - "Flyvbjerg y Gardner (2023), How Big Things Get Done (según una reseña): https://www.independent.org/tir/2023-fall/how-big-things-get-done/"
  - "Gestion-de-proyectos/.investigacion/enfoque.md"
aliases: [stage-gate, puertas, compuertas, gestionar por etapas, manage by stages, go/kill, puntos de decisión, phase gates]
creado: 2026-11-27
revisado: 2026-11-27
---

# Etapas y puntos de control

Las etapas y puntos de control parten un proyecto en tramos y, al final de cada uno, obligan a decidir con información nueva si se sigue, se cambia o se para. No es un enfoque más sino una capa de gobierno que se monta sobre cualquiera, predictivo, iterativo, de flujo o de apuesta.

Los [enfoques](enfoque.md) dicen cómo se organiza el trabajo adentro de un tramo; las etapas dicen cuándo alguien con autoridad mira el conjunto y decide. Un proyecto puede iterar en semanas dentro de una etapa de tres meses, y tener tres puertas en todo su recorrido. Quién decide en cada puerta, con qué tolerancias y quién patrocina está en [gobierno del proyecto](../Gobierno-y-cierre/gobierno-del-proyecto.md).

## Cómo se arma una etapa

Una etapa es un tramo con un objetivo propio y un final donde se decide. Criterio de la base, a partir de lo que PRINCE2 actualiza en cada límite de etapa: a la puerta conviene llevar qué se logró, cuánto costó contra lo previsto, cómo quedaron la [justificación](../Encuadre/justificacion.md) y los [riesgos](../Incertidumbre-y-riesgo/riesgo.md), y el plan del tramo siguiente. Las respuestas posibles son tres, según las secundarias de PRINCE2: autorizar la siguiente etapa tal cual, con condiciones o parar.

PRINCE2 hace de esto un principio obligatorio, según una guía de referencia y Wikipedia: sin gestión por etapas, no es un proyecto PRINCE2. Pide al menos dos etapas, la primera de iniciación. Al final de cada una se actualizan el caso de negocio, los riesgos y el plan, y la junta del proyecto decide si autoriza la siguiente. La tolerancia de cada etapa es de la junta (según una tabla de Wikipedia, ilegible en parte); si se va a exceder, el problema [sube](../Incertidumbre-y-riesgo/problemas-y-escalamiento.md) antes de la puerta.

En el desarrollo de productos, Cooper trabaja el mismo mecanismo como stage-gate. Según un artículo suyo de 2002 (por un resumen), las empresas con mejores prácticas construyen puertas exigentes y usan tableros de puntaje para evaluar y priorizar los proyectos en cada una.

## Dónde cortar las etapas

Criterio de la base, sin fuente: las etapas se cortan donde cambia lo que se sabe o lo que se arriesga, no por calendario. Tres cortes naturales:

1. **Después de explorar y antes de comprometer.** Un piloto, un prototipo o un estudio termina en una puerta que decide si se firma el contrato o se compra el equipo.
2. **Antes de un gasto que no tiene vuelta.** En una mudanza de plataforma, antes del corte del sistema viejo; en una obra, antes de demoler. Lo que se puede deshacer barato no necesita puerta; ese criterio es el de las [decisiones reversibles](../../Liderazgo-y-direccion/Decidir/decisiones-reversibles.md).
3. **Cuando un supuesto clave se pone a prueba.** Si el proyecto depende de que los usuarios adopten algo, la puerta va después de la primera prueba con usuarios. Los [supuestos](../Incertidumbre-y-riesgo/supuestos.md) que se prueban temprano son los que definen estas puertas.

## La puerta sirve si puede parar

Una puerta solo sirve si parar es una respuesta posible. Flyvbjerg describe dos formas de la falacia del compromiso, según una reseña de su libro de 2023: aprobar antes de explorar alternativas y seguir porque ya se gastó mucho. Que un punto de control con una decisión real de parar ataque las dos es lectura de la base. No hay estudio que mida cuántos proyectos se paran bien en las puertas. Por qué cuesta tanto parar, con la evidencia sobre escalada del compromiso, está en [cerrar o cancelar](../Gobierno-y-cierre/cerrar-o-cancelar.md).

La evidencia de que las puertas mejoran los resultados es correlacional. El estudio de Cooper y Edgett (2012) sobre 211 empresas identificó prácticas ligadas a mejor desempeño en innovación, y los propios autores señalan que falta evidencia firme sobre qué estructura de gobierno funciona mejor y cuál es su impacto, si lo hay (según la ficha). No se encontró metaanálisis ni estudio controlado que aísle el efecto de las puertas.

## Etapas con incertidumbre alta, en disputa

> [!IMPORTANT]
> **Las etapas fijas se adaptan mal a la incertidumbre alta.** Baxter y colegas (2022) sostienen que el modelo de etapas falla en contextos de mucha incertidumbre, digitalización o innovación abierta, porque ahí hay que poder cambiar el concepto y el mercado objetivo a mitad de camino (según un resumen).
>
> **El modelo nunca fue rígido.** Cooper responde que no se pensó lineal, que no todo proyecto usa todas las etapas y que los problemas vienen de la burocracia y de malas aplicaciones de Six Sigma y lean (según un resumen de PDMA). Con Sommer (2016) propuso un híbrido, Agile-Stage-Gate, que pone sprints dentro de las etapas; sus autores reportan respuesta más rápida, mejor voz del cliente y menos tiempo a mercado, y dicen que falta investigación. Es evidencia de casos, de los autores del modelo.
>
> Cooper y Zhao (2026) proponen que las puertas maximicen la velocidad de aprendizaje en lugar de optimizar la inversión, y sugieren que mejorar las decisiones de seguir o parar ya llegó a su límite práctico (según un resumen). Que esa versión encaje con la escuela adaptativa de este tema es lectura de la base.

## Cómo falla

Inferencias de la base, sin fuente.

- **Puertas que solo aprueban.** Si nadie recuerda una puerta que haya parado algo, la puerta es un trámite. Conviene registrar cuántas veces se respondió "parar" o "seguir con condiciones".
- **Puertas que juzgan documentos.** La puerta revisa planes y presentaciones en vez de lo que el tramo produjo. Lo que se lleva a la puerta se [acepta con evidencia](../Seguimiento/aceptar-con-evidencia.md).
- **Demasiadas puertas.** Cada puerta frena el flujo mientras se espera la decisión. Más puertas no dan más control si quien decide no tiene tiempo de mirar.

## Puntos de control cuando ejecutan agentes

Inferencia de esta base: cuando un agente ejecuta un tramo, lo que se gasta antes de cada punto de control es poco, y eso baja el costo de parar. Con menos gastado, la falacia del compromiso pesa menos y las puertas pueden ser más frecuentes y más dispuestas a parar. Lo que vale más es que cada punto tenga verificación real de lo hecho, porque un agente puede informar que terminó sin haber terminado. En un trabajo delegado, el punto de control es también donde una persona decide si el agente sigue con la misma autonomía, como trata [niveles de autonomía](../Personas-y-agentes/niveles-de-autonomia.md).
