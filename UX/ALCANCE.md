---
tema: UX
para: fundar el área de conocimiento de diseño de experiencia de usuario e interfaces, que la lean Matias, Fer y los agentes; a futuro la usan los repos de cada empresa de la organización, que enlazan las notas de acá
nivel: entiende de negocio y de software pero no es diseñador; no se da por sabido el vocabulario de diseño
escuela: diseño centrado en el usuario (ISO 9241-210) como columna; design thinking, Lean UX, diseño centrado en la actividad y optimización por experimentos (CRO) como contraste, con su evidencia
fuera:
  - identidad de marca (tema Marketing, Marca)
  - por qué persuade un mensaje (tema Marketing, Comunicación; se enlaza)
  - implementación de interfaces: CSS, frameworks, componentes en código (tema Desarrollo)
  - herramientas de diseño y guías de plataforma (fichas fechadas, cuando hagan falta)
  - patrones por tipo de producto (ficha y checkout de e-commerce, landing, dashboard): en esta pasada solo como bibliografía por necesidad
  - cómo aplica a una empresa concreta (su repo de negocio)
fuentes: []
preguntas:
  - "¿Qué diferencia hay entre UX y UI, y de qué partes está hecho diseñar una experiencia?"
  - "¿Cómo se sabe si una interfaz es usable, con qué método y con cuántos usuarios?"
  - "¿Qué leo primero si tengo que diseñar el checkout de una tienda online, una landing que convierta o un sistema interno lleno de tablas y formularios?"
  - "¿Qué pide la accesibilidad (WCAG) y qué nivel conviene apuntar?"
  - "¿Qué formas de trabajar compiten (centrado en el usuario, design thinking, Lean UX) y qué evidencia tiene cada una?"
  - "¿Cuándo un diseño persuasivo pasa a ser un patrón oscuro?"
aprobado: 2026-11-22
---

# Alcance: UX

El tema funda el área de conocimiento de diseño de experiencia de usuario e interfaces de la organización: primero la estructura que va a alojar todo lo que se aprenda, y adentro lo esencial de cada parte. El pedido sale de la conversación del 2026-11-22. Las necesidades de una agencia de marketing digital, de una plataforma de tiendas online y de una consultora de software generalista sirvieron para elegir las referencias; el contenido es genérico y esas empresas no lo consumen todavía.

## Árbol

```
UX/
  ux.md                          el todo: qué es UX y qué es UI, las siete partes y el ciclo que las une
  Percepcion-y-decision/         cómo ve, recuerda y decide la gente frente a una pantalla
    modelo-mental                  lo que la persona cree que hace el sistema
    carga-cognitiva                cuánto esfuerzo mental pide una interfaz
    leyes-de-fitts-y-hick          el tiempo de apuntar y el de elegir
    patron-oscuro                  cuándo persuadir pasa a ser engañar
  Investigacion/                 entender a quién, qué tarea y en qué contexto
    metodos-de-investigacion       qué método contesta qué pregunta
    entrevista-de-usuario
    entrevista-de-cambio           la entrevista a quien cambió de producto (JTBD)
    analisis-de-resenas            codificar reseñas propias y de rivales, con sus sesgos
  Arquitectura-de-informacion/   cómo se organiza y se encuentra el contenido
    navegacion
  Interaccion/                   cómo se usa: flujos, controles, estados, respuesta
    principios-de-interaccion      affordance, significante, feedback, mapeo
    formularios
  Diseno-visual/                 cómo se ve: jerarquía, tipografía, color, grilla
    jerarquia-visual
    sistema-de-diseno
  Accesibilidad/                 que la pueda usar cualquiera
    wcag
  Evaluacion/                    si funciona: probar con gente y medir
    test-de-usabilidad
    evaluacion-heuristica
    metricas-de-ux
    evaluacion-competitiva         comparar la usabilidad propia con la de los rivales
  Fundamentos/                   qué es UX, historia, escuelas, bibliografía por necesidad, fuentes, mitos, glosario
```

## Supuestos

- Profundidad de esta primera pasada: el árbol completo con la entrada de cada parte, los componentes de arriba y Fundamentos entero. Lo que falta de cada parte (mapa de recorrido, card sorting, búsqueda y filtros, estados de la interfaz, microcopy, experimento A/B) queda nombrado en su entrada.
- Los patrones de cada tipo de producto esperan a un caso real; mientras, la bibliografía se ordena por necesidad (general, conversión, e-commerce, software de negocio).
- Ampliado el 2026-11-22 para el plan de análisis de competencia (issue #24 de mtsdlf/conocimiento): evaluación competitiva, entrevista de cambio y análisis de reseñas.
