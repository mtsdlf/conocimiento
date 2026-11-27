---
tema: Diseño instruccional
para: entender la pedagogía como campo (aprender y enseñar), con sus verticales y su evidencia; la leen Matias y Fer
nivel: sin formación docente; lector práctico que enseña o aprende de adulto
escuela:
fuera:
  - "teorías del aprendizaje, en Ciencias-del-aprendizaje"
  - "historia general de la enseñanza y de la didáctica, en Didactica"
  - "cómo leer la evidencia educativa (Hattie, EEF), en los Fundamentos del área"
  - "diseño de pruebas y evaluar si un curso funcionó, en Evaluacion-educativa"
  - "plataformas, cursos masivos y su abandono, en Tecnologia-educativa"
  - "el mecanismo de la memoria y del aprendizaje, en Psicologia/Aprendizaje-y-memoria"
fuentes: []
preguntas:
  - "Tengo que armar una capacitación de ocho horas: ¿por dónde empiezo y en qué orden la diseño?"
  - "¿Cómo se ordena un temario para que cada parte se apoye en la anterior?"
  - "¿Qué cambia si el curso es a ritmo propio en lugar de con cohorte?"
aprobado: 2026-11-27
---

# Alcance: Diseño instruccional

Sale de la conversación del 2026-11-27: un área nueva, Pedagogía, con verticales abstractas del campo (no guías de pasos). Se escribió en borrador desde los informes `analisis-objetivos-secuencia.md` y `modelos-materiales-formatos.md` de `.investigacion/` y los del área en `Didactica/.investigacion/`.

## Árbol

```
Diseno-instruccional/
  diseno-instruccional.md                el todo, con tareas y orden de lectura
  Analisis-previo/                       si hace falta enseñar, qué hace el experto, desde dónde arranca quien aprende
    analisis-previo.md
    analisis-de-necesidades.md           Mager y Pipe, BEM de Gilbert
    analisis-cognitivo-de-tareas.md      CTA, la cifra del 70 %, punto ciego del experto
    analisis-de-quien-aprende.md         conductas de entrada, inversión de la experticia
  Objetivos-de-aprendizaje/              escribir, clasificar y alinear
    objetivos-de-aprendizaje.md          con la evidencia de si los objetivos sirven
    objetivo-de-desempeno.md             Mager: desempeño, condición, criterio
    taxonomia-de-bloom.md                la revisión de 2001 y sus críticas
    alineacion-constructiva.md           Biggs, backwash, currículo oculto
  Secuencia-y-curriculo/                 orden de contenidos y orden de tareas
    secuencia-y-curriculo.md
    jerarquia-de-aprendizaje.md          Gagné, grafo de competencias, espacios de conocimiento
    secuencia-de-contenidos.md           elaboración de Reigeluth, espiral de Bruner
    secuencia-por-tareas-completas.md    clases de tareas de 4C/ID, condiciones simplificadoras
    conceptos-umbral.md                  Meyer y Land
  Modelos-de-diseno/                     procesos, orden de decisiones y listas de principios
    modelos-de-diseno.md                 con la evidencia (casi nula) de los modelos
    addie-y-sam.md                       ADDIE como rótulo, SAM, Dick y Carey
    diseno-hacia-atras.md                Wiggins y McTighe
    4c-id.md                             cuatro componentes, diez pasos, d = 0,79
    principios-de-instruccion.md         Merrill y los nueve eventos de Gagné
  Materiales-y-carga-cognitiva/          el material didáctico visto desde la memoria de trabajo
    materiales-y-carga-cognitiva.md
    carga-cognitiva-en-el-aprendizaje.md Sweller, inversión de la experticia, crítica de de Jong
    principios-multimedia.md             Mayer: tabla de efectos y condiciones de borde
  Formatos/                              tres ejes: medio, ritmo y estructura social, contexto
    formatos.md                          con bootcamps y microaprendizaje como huecos
    en-linea-presencial-y-mixto.md       Means 2013, Bernard 2004
    cohorte-o-ritmo-propio.md            sin evidencia comparativa
    aprender-en-el-trabajo.md            70-20-10 como folklore
  Fundamentos/
    fundamentos-de-diseno-instruccional.md  lo que se toma del área y los manuales de referencia
    historia-del-diseno-instruccional.md    de la formación militar a ADDIE y 4C/ID
    mitos-del-diseno-instruccional.md       70-20-10, andragogía, aprendiz que sabe, ADDIE, Bloom
    glosario-de-diseno-instruccional.md
```

## Supuestos

- El mecanismo psicológico del aprendizaje vive en Psicología/Aprendizaje-y-memoria y se enlaza, no se copia. La carga cognitiva vista desde una interfaz vive en `UX/Percepcion-y-decision/carga-cognitiva.md`; la nota de este tema la mira desde el material didáctico y la enlaza.
- **Análisis pasó a `Analisis-previo/`**: `analisis.md` ya existía en `Datos/` y los nombres de archivo son únicos en la base.
- **La alineación constructiva va con los objetivos**, no como subtema de Bloom, porque Biggs y el diseño hacia atrás tratan objetivo y evaluación como un solo problema (propuesta del informe). El diseño hacia atrás queda en Modelos como orden de decisiones y las dos notas se enlazan.
- **La secuencia se partió en contenidos y tareas**: la literatura mezcla el orden de los contenidos (Gagné, Reigeluth, Bruner) y el de las tareas completas (4C/ID). La secuencia por tareas explica el orden; el modelo 4C/ID entero vive en Modelos.
- **El grafo de competencias no tiene nota propia**: es una herramienta de representación de la jerarquía de prerrequisitos y va dentro de `jerarquia-de-aprendizaje.md`, con los espacios de conocimiento como su base formal.
- **El currículo oculto va dentro de la alineación constructiva** (por el backwash), no como nota.
- **Los modelos se dividieron en tres clases** (procesos de proyecto, orden de decisiones, qué lleva una buena instrucción) y 4C/ID como modelo que cubre las tres. Merrill y Gagné van juntos en una nota porque ninguno tiene evidencia propia suficiente para una nota por autor. Dick y Carey va dentro de `addie-y-sam.md` como modelo de proceso.
- **Formatos se organizó por ejes** (medio, ritmo y estructura social, contexto) y no por formato. Bootcamps y microaprendizaje no tienen nota: no hay evidencia investigada y quedan como hueco declarado en `formatos.md`.
- **Materiales tiene dos componentes**: la atención dividida y los ejemplos resueltos con subobjetivos quedan como hueco hasta investigarlos.
- **Los manuales de referencia van en la entrada de Fundamentos**, sin nota de bibliografía aparte. Teorías del aprendizaje, historia general y cómo leer la evidencia educativa se nombran y se enlazan a los temas del área que las escriben.
- La andragogía se trata como mito en este tema (la asignó así el informe de mitos del área); su crítica completa como teoría del adulto es de Ciencias del aprendizaje.
