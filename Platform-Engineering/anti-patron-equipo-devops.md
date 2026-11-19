---
tipo: concepto
resumen: >-
  El anti-patrón del equipo DevOps es un equipo intermedio que ejecuta los pasos de entrega de los
  demás equipos; en vez de construir capacidades self-service, se vuelve una dependencia fija y un
  cuello de botella.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 4: https://teamtopologies.com/book"
  - "Matthew Skelton y Manuel Pais, DevOps Topologies, Anti-Type B: https://web.devopstopologies.com/"
aliases: [DevOps Team Silo, Anti-Type B, Equipo DevOps intermedio]
parte_de: []
requiere: [self-service, team-topologies]
relacionado: [devops-topologies]
---

# Anti-patrón del equipo DevOps

El anti-patrón del equipo DevOps es un equipo intermedio que ejecuta los pasos de entrega de los
demás equipos; en vez de construir capacidades self-service, se vuelve una dependencia fija y un
cuello de botella.

## Por qué importa

Según Skelton y Pais, el aporte de DevOps fue mostrar los problemas de interacción entre equipos
a lo largo de la cadena de entrega: demoras, retrabajo, fallas y poca empatía con los otros
equipos. Un equipo "DevOps" que se pone en el medio repite ese problema con otro nombre. En
[DevOps Topologies](devops-topologies.md) es el Anti-Type B, "DevOps Team Silo".

## Cómo funciona

El anti-patrón aparece cuando a un equipo DevOps se le pide ejecutar pasos en el camino de
entrega de cada aplicación: desplegar, crear entornos, configurar pipelines. Cada pedido pasa por
su cola, y los equipos de producto no pueden entregar sin él.

Tres preguntas lo detectan:

1. ¿Cuál es el mandato del equipo? "Que los equipos se sirvan solos" es sano; "hacer los
   despliegues de los desarrolladores" es el anti-patrón.
2. ¿Se frena la entrega si el equipo desaparece? Si la respuesta es sí, es un cuello de botella.
3. Si el equipo nació como transición, ¿se disolvió al cumplir su objetivo? Si se volvió
   permanente, cayó en el anti-patrón.

Las salidas que propone DevOps Topologies son un equipo con fecha de disolución (Type 5), un
equipo que facilita sin operar (Type 6) o un equipo que ofrece infraestructura como servicio
(Type 3). En [Team Topologies](team-topologies.md), el equivalente es un platform team que construye
[Self-service](self-service.md), o un enabling team que enseña y se retira.

## Ejemplo

Diez equipos de producto abren tickets al "equipo DevOps" para cada despliegue. La espera
promedio es de dos días, y cuando dos personas de ese equipo se toman vacaciones, nadie despliega.

## No confundir con

Un platform team. Los dos pueden manejar las mismas herramientas; la diferencia es que el
platform team ofrece capacidades que los equipos usan solos, y el equipo DevOps del anti-patrón
hace el trabajo por ellos.

## Relaciones

- Requiere: [Self-service](self-service.md) — la alternativa que este equipo no construye.
- Requiere: [Team Topologies](team-topologies.md) — el modelo con que se diagnostica y se corrige.
- Relacionado: [DevOps Topologies](devops-topologies.md) — donde figura como Anti-Type B.
