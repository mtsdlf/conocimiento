---
resumen: >-
  Estos pasos diagnostican con entrevistas qué topología de DevOps Topologies tiene hoy una
  organización y arman el plan para pasar a la siguiente.
estado: borrador
estabilidad: semi
fuentes:
  - "Matthew Skelton y Manuel Pais, DevOps Topologies: https://web.devopstopologies.com/"
aliases: [DevOps & Platform Collaboration Assessment, Assessment de colaboración Dev-Ops]
creado: 2026-10-03
revisado:
---

# Evaluar la colaboración Dev–Ops de una organización

Estos pasos diagnostican con entrevistas qué topología de DevOps Topologies tiene hoy una
organización y arman el plan para pasar a la siguiente.

## Qué hace falta antes de las entrevistas

- Conocer los Types y Anti-Types de [DevOps Topologies](devops-topologies.md): el diagnóstico se expresa en ellos.
- Tener el [Cuestionario de colaboración Dev–Ops](cuestionario-de-colaboracion-dev-ops.md), con sus 12 secciones y la rúbrica: es el instrumento
  que se usa en los pasos 2 a 4.
- Acordar con un sponsor ejecutivo que las respuestas se usan para mejorar, no para evaluar
  personas.

## De las entrevistas al plan

1. **Elegí a quién entrevistar**: líderes de desarrollo, gerentes de operaciones, líderes de
   plataforma o SRE, product owners, gerentes de ingeniería, DBAs, QA, seguridad y sponsors
   ejecutivos. Resultado: una lista con al menos una persona por rol.
2. **Hacé las entrevistas**: sesiones individuales o en grupos chicos de unos 45 minutos, o el
   cuestionario como formulario si hay muchas personas. Las preguntas se responden con sí o no,
   una escala de 1 a 5 o texto corto. Anotá los comentarios textuales.
3. **Puntuá cada sección** de 1 (bajo) a 5 (alto). Resultado: un puntaje por sección y por
   persona.
4. **Mapeá los resultados** a Types y Anti-Types con la rúbrica del cuestionario. Si varias
   personas describen lo mismo con palabras distintas, esa es la evidencia más fuerte.
5. **Armá la tabla de hallazgos**, una fila por área:

   | Área | Evidencia | Type o Anti-Type | Impacto | Próximo paso |
   |---|---|---|---|---|
   | Colaboración Dev–Ops | "Ops se suma a los post-mortems cada trimestre" | Anti-A | Alto | OKR compartido y reunión semanal |
   | Base de datos | "Las aprobaciones frenan los releases" | Anti-G | Alto | Sesiones conjuntas de diseño de datos (Type 9) |

6. **Escribí el plan** en tres plazos: arreglos inmediatos (huecos de ownership, guardias que
   faltan), cambios de estructura a mediano plazo (KPIs alineados, revisiones conjuntas) y la
   topología objetivo a largo plazo, por ejemplo de Anti-B a Type 5 y después a Type 1.

## Qué tiene un diagnóstico terminado

- Cada patrón encontrado tiene su Type o Anti-Type y su evidencia textual.
- Hay un puntaje por dominio: cultura, herramientas, operación y datos.
- El plan está priorizado y nombra la topología objetivo.
