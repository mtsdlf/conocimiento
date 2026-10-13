---
tipo: ficha
resumen: >-
  El cuestionario de colaboración Dev–Ops tiene 42 preguntas en 12 secciones y una rúbrica que
  lleva las respuestas a los Types y Anti-Types de DevOps Topologies.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Original en inglés: DevOps & Platform Collaboration Assessment – Full Questionnaire, archivado en Archivo/Platform-Engineering/devops-platform-assessment.md"
  - "Matthew Skelton y Manuel Pais, DevOps Topologies: https://web.devopstopologies.com/"
aliases: [DevOps & Platform Collaboration Assessment, Cuestionario Dev-Ops]
parte_de: []
requiere: [devops-topologies]
relacionado: [evaluar-la-colaboracion-dev-ops]
---

# Cuestionario de colaboración Dev–Ops

El cuestionario de colaboración Dev–Ops tiene 42 preguntas en 12 secciones y una rúbrica que
lleva las respuestas a los Types y Anti-Types de DevOps Topologies.

## Valores

Cada fila da la pregunta y la señal: qué respuesta apunta a qué Type (T1 a T9, formas sanas) o
Anti-Type (A-A a A-H, anti-patrones) de [[devops-topologies]], donde cada uno tiene su nombre.

| N.º | Pregunta | Señal |
|---|---|---|
| **1** | **Interacción y ownership** | |
| 1.1 | ¿En qué etapa se suma Ops (o SRE, plataforma) a un producto o feature nuevo? | diseño: T1/T2; después del release: A-A |
| 1.2 | ¿Qué significa "terminado" para el equipo? | definición compartida: sano; "funcionalidad completa": A-A |
| 1.3 | ¿Quién es dueño de la confiabilidad cuando el feature está en producción? | compartido o del equipo: T1–T2; pasado a Ops: A-A/A-H |
| 1.4 | ¿Con qué frecuencia hacen Dev y Ops post-mortems sin culpas juntos? | seguido: T1; casi nunca: silo |
| **2** | **Límites y estructura** | |
| 2.1 | ¿Hay un equipo "DevOps"? ¿Cuál es su mandato? | habilitar y enseñar: T5/T6; desplegar por otros: A-B |
| 2.2 | ¿Se frena la entrega si ese equipo desaparece? | sí: A-B |
| 2.3 | ¿Hay especialistas de Ops dentro de los equipos? ¿Quién prioriza su trabajo? | con backlog equilibrado: T2; relegados: A-F |
| 2.4 | ¿Esos especialistas tienen una comunidad de práctica o estándares comunes? | sí: mitiga A-F |
| **3** | **Herramientas y plataforma** | |
| 3.1 | ¿Quién construye y mantiene CI/CD, configuración y entornos? | habilitación central: T3/T6; equipo de herramientas por tickets: A-D |
| 3.2 | ¿Cómo piden infraestructura los equipos: self-service, ticket o manual? | self-service: T3; tickets: anti-patrón heredado |
| 3.3 | Cuando una herramienta se rompe, ¿quién la arregla? | compartido: colaboración; solo herramientas: silo |
| 3.4 | ¿Los equipos de herramientas y plataforma recogen feedback? ¿Cada cuánto? | seguido: T3/T6 maduro |
| **4** | **Cultura y organización** | |
| 4.1 | ¿Dev y Ops comparten KPIs u OKRs (frecuencia y estabilidad de entrega)? | sí: T1; metas opuestas: A-A |
| 4.2 | Tras un incidente, ¿mejoran el sistema las mismas personas que lo atendieron? | sí: cultura DevOps; otro equipo: pared |
| 4.3 | ¿Se renombró a sysadmins como "DevOps engineers" sin cambiar sus tareas? | sí: A-E |
| 4.4 | ¿Qué describe mejor la relación: cooperación diaria, proveedor y cliente, o silos? | medida rápida de cultura |
| **5** | **Prácticas operativas** | |
| 5.1 | ¿Los desarrolladores están en la guardia? | común en T2; ausente: A-A o A-H |
| 5.2 | ¿Alguien fuera de Dev monitorea las métricas y alertas de producción? | solo Ops: A-A/A-E |
| 5.3 | ¿Quién decide que un sistema está listo para producción? | decisión conjunta: T1/T7; solo Ops o SRE: A-H |
| 5.4 | ¿Hay SLOs y error budgets definidos y revisados? | sí: T7; no: operación ad hoc |
| **6** | **Base de datos** | |
| 6.1 | ¿Cuándo se suman los DBAs a un feature? | temprano: T9; tarde: A-G |
| 6.2 | ¿Quién aprueba cambios de esquema o de modelo de datos? | conjunto: T9; DBAs como guardianes: A-G |
| 6.3 | ¿La performance o las migraciones de base frenan releases? | seguido: A-G |
| 6.4 | ¿Dev y DBAs comparten el monitoreo y el ajuste de la base? | sí: T9 |
| **7** | **Modelo de plataforma** | |
| 7.1 | ¿Ops o plataforma funciona como proveedor interno de IaaS? | describe T3 |
| 7.2 | ¿Qué interfaz hay con plataforma: APIs, módulos de Terraform, tickets? | API: T3 sano; tickets: heredado |
| 7.3 | ¿Cómo se mide y se comparte la confiabilidad de la infraestructura? | métricas visibles: madurez |
| **8** | **Promoción y habilitación** | |
| 8.1 | ¿Hay un grupo que facilita entre Dev y Ops sin operar? | sí: T6 |
| 8.2 | ¿Mide su éxito por habilitación o por entregas? | habilitación: T6; entregas: deriva a A-B |
| 8.3 | ¿Hay guilds, dojos o charlas internas sobre prácticas DevOps? | sí: T6 maduro |
| **9** | **Equipo de transición** | |
| 9.1 | ¿Hubo un equipo temporal de "transformación DevOps" o de plataforma? | intento de T5 |
| 9.2 | ¿Se disolvió al cumplir sus objetivos? | sí: T5; sigue: A-B |
| 9.3 | ¿Transfirió su conocimiento a otros equipos? | condición para disolverse bien |
| **10** | **Contenedores** | |
| 10.1 | ¿Las aplicaciones corren en contenedores o artefactos parecidos? | base de T8 |
| 10.2 | ¿Quién mantiene las imágenes base y los estándares de runtime? | compartido: sano; solo Ops: vuelve A-A |
| 10.3 | Si falla algo dentro de un contenedor, ¿quién investiga primero? | conjunto: T8; solo Ops: límite mal usado |
| **11** | **Servicios externos** | |
| 11.1 | ¿Se terceriza operación, monitoreo o infraestructura? | aclara si es T4 |
| 11.2 | ¿Quién trae lo que aprende el tercero a los equipos? | alguien: aprendizaje; nadie: dependencia |
| **12** | **Madurez y visión** | |
| 12.1 | ¿Qué describe mejor: Dev y Ops separados, equipo DevOps en el medio, responsabilidad compartida o SRE? | autodiagnóstico rápido |
| 12.2 | ¿Cuáles son los mayores dolores de entrega u operación? | evidencia para los Anti-Types |
| 12.3 | ¿Cómo sería entregar "sin fricción" acá? | topología a la que aspiran |
| 12.4 | ¿Está la dirección dispuesta a cambiar reportes o metas? | factibilidad del cambio |

Rúbrica:

| Patrón observado | Topología probable | Riesgo | Objetivo |
|---|---|---|---|
| KPIs separados, Ops tardío, infraestructura por tickets | A-A | feedback lento | T1 |
| Equipo DevOps intermedio permanente | A-B | cuello de botella | T5 o T6 |
| Dev hace todo y descuida lo operativo | A-C o A-F | agotamiento, fragilidad | T2 |
| Solo un equipo central de herramientas | A-D | automatización sin cambio cultural | T3 |
| "DevOps" igual a ex sysadmin | A-E | ningún cambio real | T1 o T3 |
| DBAs como guardianes | A-G | fricción en releases | T9 |
| SRE de nombre, sin autonomía | A-H | nuevo silo | T7 |

## Relaciones

- Detalla: [[evaluar-la-colaboracion-dev-ops]] — los pasos que usan este cuestionario.
- Requiere: [[devops-topologies]] — los nombres de cada Type y Anti-Type.
