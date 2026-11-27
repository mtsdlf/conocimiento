---
tema: Evaluación educativa
para: entender la pedagogía como campo (aprender y enseñar), con sus verticales y su evidencia; la leen Matias y Fer
nivel: sin formación docente; lector práctico que enseña o aprende de adulto
escuela:
fuera:
  - "El mecanismo del efecto de testeo: Psicologia/Aprendizaje-y-memoria/practica-espaciada-y-recuperacion.md"
  - "Cómo leer la evidencia educativa, tamaños de efecto, Hattie y la EEF: Didáctica (Fundamentos)"
  - "Qué hace buena a una retroalimentación: Didáctica"
  - "Tutores inteligentes y software de práctica adaptativa como herramientas: Tecnología educativa"
  - "La transferencia como fenómeno cognitivo: Ciencias del aprendizaje"
  - "Tests psicológicos clínicos: Psicologia-infantil/Evaluacion/"
  - "Evaluación del desempeño de empleados: Liderazgo-y-direccion/Gestion-de-personas/"
fuentes: []
preguntas:
  - "¿Cómo sé si de verdad aprendieron, y no solo si les gustó?"
  - "¿Cómo ubico a alguien que entra a un curso según lo que ya sabe?"
  - "¿Qué hace confiable a una prueba?"
aprobado: 2026-11-27
---

# Alcance: Evaluación educativa

Sale de la conversación del 2026-11-27: un área nueva, Pedagogía, con verticales abstractas del campo (no guías de pasos). Las notas se escribieron en borrador a partir de los dos informes de `.investigacion/`.

## Árbol

```
Evaluacion-educativa/
  evaluacion-educativa.md                 el todo
  Propositos/                             para qué se evalúa
    propositos.md
    evaluacion-diagnostica.md             ubicar antes de enseñar
    evaluacion-formativa.md               ajustar mientras se enseña; la disputa 0,4-0,7 frente a 0,20
    evaluacion-como-aprendizaje.md        la prueba de práctica en el aula
  Instrumentos/                           cómo se junta la evidencia
    instrumentos.md
    opcion-multiple.md
    tareas-de-desempeno.md                auténticas, proyectos, portfolios, corrección de código
    rubrica.md
    autoevaluacion-y-evaluacion-entre-pares.md
  Validez-confiabilidad-y-equidad/        cuánto creerle a un resultado
    validez-confiabilidad-y-equidad.md
    validez.md
    confiabilidad.md                      con calibración de correctores
    equidad-y-sesgo.md
    inflacion-de-notas.md                 Campbell, enseñar para la prueba, inflación de calificaciones
  Evaluacion-adaptativa/                  modelar lo que sabe cada uno
    evaluacion-adaptativa.md
    teoria-de-respuesta-al-item.md        con el test adaptativo computarizado
    seguimiento-del-conocimiento.md       BKT y DKT
    espacios-de-conocimiento.md           Doignon y Falmagne
    sistemas-de-diagnostico-adaptativo.md ficha volátil (2026-11)
  Calificacion-y-acreditacion/            de lo observado a una nota o un certificado
    calificacion-y-acreditacion.md
    referencia-a-norma-y-a-criterio.md
    calificacion-por-dominio.md
    notas-y-comentarios.md
    certificados-y-microcredenciales.md
  Evaluar-un-programa/                    si el curso sirvió
    evaluar-un-programa.md
    niveles-de-kirkpatrick.md
    transferencia-de-la-capacitacion.md
    retorno-de-la-capacitacion.md
    evaluacion-con-grupo-de-comparacion.md
  Fundamentos/
    fundamentos-de-evaluacion-educativa.md  historia, dos culturas, mitos
    fuentes-de-evaluacion-educativa.md
    glosario-de-evaluacion-educativa.md
```

## Supuestos

- El mecanismo psicológico del aprendizaje vive en Psicología/Aprendizaje-y-memoria y se enlaza, no se copia.
- **Equidad con nota propia.** Los Standards de 2014 ponen la equidad como tercer fundamento, con capítulo propio, junto con validez y confiabilidad. La vertical «Validez y confiabilidad» pasó a llamarse «Validez, confiabilidad y equidad» y la equidad tiene nota propia (`equidad-y-sesgo.md`).
- **Inflación de notas en Validez.** Lo que el informe proponía como «cuando la nota miente» (Campbell, Koretz) se juntó con la inflación de calificaciones (Denning) en una nota de la vertical de validez, porque es la forma en que un resultado pierde validez con el uso. Así Calificación queda en cuatro componentes.
- **Adaptativa por comunidad, con el diagnóstico afuera.** El informe dice que la reúnen tres comunidades que casi no se citan (psicometría, tutores inteligentes, psicología matemática). Cada una es un componente; IRT y test adaptativo van en una sola nota porque el segundo se construye sobre la primera. El diagnóstico rápido (Kalyuga y Sweller) y los límites de la autoevaluación se movieron a `Propositos/evaluacion-diagnostica.md`, que era el hueco de la vertical Propósitos (sin literatura propia). ALEKS y Math Academy van en una ficha volátil.
- **Calificación y acreditación siguen juntas.** El informe las da como dos temas con literaturas que no se superponen. Se dejaron en una vertical porque la acreditación tiene un solo componente con evidencia (`certificados-y-microcredenciales.md`); la entrada de la vertical explica que son dos preguntas distintas. Si la acreditación crece, se parte.
- **Evaluar un programa con dos tradiciones.** Capacitación en organizaciones (Kirkpatrick, transferencia, ROI) y evaluación educativa con grupo de comparación (WWC). Se mantienen en una vertical porque la pregunta es la misma; la entrada las contrasta en una tabla.
- **Sumativa sin nota propia.** Se define en `propositos.md` y su desarrollo vive en Calificación y acreditación.
- **Portfolios y corrección de código dentro de tareas de desempeño.** El informe no encontró literatura propia de portfolios, y la de corrección de código es una aplicación de tareas y rúbricas.
- Los nombres de carpeta van en ASCII (el esqueleto los tenía con tildes).
