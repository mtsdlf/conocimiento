---
resumen: >-
  Los fundamentos de arquitectura son lo que cruza todo el tema sin ser una parte del sistema: las
  escuelas que lo piensan distinto, lo que pierde peso y por qué, la bibliografía y las creencias
  que la evidencia no sostiene.
estado: borrador
estabilidad: estable
fuentes:
  - https://nealford.com/books/SAF2e.html
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://research.chalmers.se/publication/247094
  - https://pubs.opengroup.org/architecture/o-aa-standard/DDD-strategic-patterns.html
  - https://www.infoq.com/news/2019/09/evans-improve-language-ddd
  - https://www.infoq.com/news/2020/05/monolith-decomposition-newman/
  - https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/
creado: 2026-11-27
revisado:
---

# Fundamentos de arquitectura

Los fundamentos de arquitectura son lo que cruza todo el tema sin ser una parte del sistema: las
escuelas que lo piensan distinto, lo que pierde peso y por qué, la bibliografía y las creencias que
la evidencia no sostiene.

El [tema](../arquitectura.md) se escribe desde una escuela elegida: AI engineering centrado en
evaluación (Huyen) sobre el canon de estilos y características (Richards y Ford). Esta carpeta dice
qué otras escuelas existen, en qué chocan con la elegida y qué se dejó fuera, para que la elección se
pueda revisar.

## Una disciplina con poca evidencia empírica

Casi todo lo que se enseña en arquitectura es canon de práctica y de consultoría, no resultado de
estudios. Van der Ven y Bosch (2016) pusieron a prueba creencias comunes de arquitectos (sobre el
esfuerzo de documentación, el tamaño del equipo y quién decide) con 39 arquitectos y 54 decisiones:
solo unas pocas tuvieron respaldo estadístico, y titulan su conclusión "folklore for the tales". La
muestra es chica y autorreportada, pero alcanza para leer con cuidado cualquier regla general,
también las de este tema.

Algunas confusiones documentadas, cada una con su fuente:

- **Bounded context no es subdominio.** Evans dijo que el término se malinterpreta y que un servicio
  no es siempre un bounded context, aunque un microservicio puede ser uno bueno (según resúmenes
  secundarios de sus charlas).
- **Monolito no es sinónimo de legacy.** Según Newman, "monolito" nombra la unidad de despliegue, no
  la edad del código; el peor caso es el monolito distribuido. Ver
  [monolito modular](../Estilos/monolito-modular.md).
- **Prime Video no prueba que los microservicios fracasaron.** Según comentaristas vistos solo por buscador, el caso de 2023 movió un componente,
  no un sistema entero, y la etiqueta está disputada; el detalle está en
  [lo que pierde peso](lo-que-pierde-peso.md).

## Qué hay en los fundamentos

- [Escuelas de arquitectura](escuelas-de-arquitectura.md) — las seis formas vivas de pensar la
  arquitectura (estilos, evolutiva, DDD, MLOps, AI engineering, agentes y harness), qué sostiene cada
  una y dónde chocan.
- [Lo que pierde peso](lo-que-pierde-peso.md) — lo que este tema dejó fuera, con la evidencia a favor
  y en contra de cada ítem y lo que gana peso en su lugar.
- [Bibliografía de arquitectura](bibliografia-de-arquitectura.md) — qué leer de cada libro y de cada
  fuente viva, y en qué fijarse.
