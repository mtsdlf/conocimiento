---
tema: Inglés
para: pasar de un inglés intermedio-alto (B2) a uno avanzado (C1/C2) siendo hispanohablante adulto, con las metodologías y prácticas que tienen evidencia; lo lee quien ya entiende casi todo y habla, pero se estancó
nivel: B2; se da por sabido el inglés de todos los días y la gramática básica (presente, pasado, futuro simple)
escuela: neutral entre las escuelas de adquisición, cada una con su evidencia; en pronunciación, el principio de inteligibilidad (Munro y Derwing, Levis) y General American como modelo, con las diferencias británicas marcadas
fuera:
  - "el nivel, los errores y el plan de una persona concreta: van a un lugar privado, porque esta base es pública"
  - "inglés desde cero o para niños"
  - "la enseñanza del inglés como profesión (didáctica para docentes)"
  - "otros idiomas"
fuentes: []
preguntas:
  - "Entiendo todo pero me estanqué en el intermedio: ¿por qué pasa y qué lo destraba?"
  - "¿Qué sonidos me conviene corregir primero para que me entiendan sin esfuerzo, siendo hispanohablante?"
  - "¿Cuándo va present perfect y cuándo past simple, y cómo dejo de pensarlo al hablar?"
  - "¿Cómo conecto ideas al hablar para que no suene traducido del castellano?"
  - "Tengo una entrevista de trabajo en inglés en dos semanas: ¿qué practico?"
  - "¿Cómo armo una rutina semanal de práctica que respalde la evidencia?"
  - "Tengo una entrevista técnica para una empresa de EE.UU.: ¿cómo cuento un proyecto y cómo pienso en voz alta en el system design?"
  - "¿Cómo se pronuncian cache, SQL, GUI o nginx sin quedar mal?"
  - "¿Cómo dejo un comentario de code review que no suene brusco?"
  - "En la daily, ¿cómo digo corto que estoy bloqueado o que no llego?"
  - "Se cayó producción: ¿cómo escribo el aviso y después el postmortem?"
  - "Tengo que explicarle a un cliente no técnico por qué el modelo se equivoca: ¿cómo lo digo?"
aprobado: 2026-11-27
---

# Alcance: Inglés

Se documenta cómo un hispanohablante adulto pasa del inglés intermedio-alto al avanzado: cómo se adquiere un idioma, los sistemas del inglés (sonido, gramática, vocabulario, discurso) vistos desde los errores típicos del castellano, y las técnicas de práctica con su evidencia. Salió de una conversación del 2026-11-27, en la que se pidió una estructura que saliera del dominio (el MCER y la investigación en adquisición de segundas lenguas) y no solo de lo que la persona quería mejorar: pronunciación, conjugación y conectar ideas.

## Árbol

```
Ingles/
  ingles.md                     el todo: qué cambia de B2 a C1, las partes, orden de lectura y qué leer según la tarea
  Adquisicion/                  cómo aprende un idioma un adulto
    input-comprensible          entender mucho como motor (Krashen) y sus límites
    output-e-interaccion        producir obliga a notar el hueco; negociar el significado (Swain, Long, Schmidt)
    feedback-correctivo         recasts contra prompts, oral y escrito (Lyster, Li, Truscott)
    instruccion-explicita       estudiar la forma sirve: el debate de la interfaz y los metaanálisis
    automatizacion              del conocimiento declarativo al uso sin pensar (DeKeyser)
    repeticion-espaciada        el efecto de espaciado y la práctica de recuperación
    edad-y-diferencias-individuales   período crítico, aptitud y motivación
    meseta-intermedia           diagnóstico: por qué el B2 se estanca (fosilización) y qué se sabe de destrabarlo
  Pronunciacion/                meta: inteligibilidad; modelo General American
    vocales                     largas y cortas, schwa, /ʌ/ y /æ/
    consonantes                 th, v/b, s inicial, grupos y finales, -ed y -s
    acento-de-palabra
    ritmo-y-habla-conectada     ritmo acentual, formas débiles, linking, elisión, flap
    entonacion                  foco, tonos y lo que comunican
  Gramatica/
    tiempo-y-aspecto            el modelo mental del sistema verbal
    present-perfect
    futuro                      will, going to, presente continuo y otros
    condicionales-e-hipotesis   condicionales, wish, if only, would have
    modales                     deducción, obligación y modales en perfecto
    pasiva-y-causativa
    articulos                   sobre todo los genéricos
    estructura-de-la-oracion    sujeto obligatorio, orden de palabras, preguntas indirectas
    estructuras-avanzadas       inversión, cleft sentences, relativos
  Lexico/
    colocaciones-y-chunks       enfoque léxico, lenguaje formulaico, preposiciones regidas
    phrasal-verbs
    cognados-y-falsos-amigos    la ventaja de los cognados, los falsos amigos y el registro latino
    amplitud-de-vocabulario     cuántas palabras, cobertura y cómo medirse (Nation)
  Discurso/                     conectar ideas
    conectores-y-cohesion
    estructura-del-argumento    anunciar, ordenar, información conocida y nueva, respuesta primero
    registro-y-cortesia         suavizar, matizar, lo directo del castellano
    interaccion                 turnos, estrategias de comunicación, reparar
    escritura                   mails y textos de trabajo
  Practica/                     cómo se entrena; la entrada son las cuatro ramas (Nation)
    fluidez                     4/3/2 y repetición de tareas
    shadowing
    entrenamiento-perceptivo    HVPT, pares mínimos y dictado
    escucha-y-lectura-extensiva
    conversacion-con-correccion tutor y tándem
    conversacion-con-ia
    grabarse-y-medirse
    examenes-de-ingles          ficha fechada
    herramientas-de-ingles      ficha fechada
    plataformas-de-tutores      ficha fechada
  Profesional/                  el inglés de trabajo en la industria del software (sumada el 2026-11-27)
    vocabulario-tecnico         jerga que no se traduce y términos que se pronuncian mal
    entrevista-tecnica          behavioral, pensar en voz alta en system design y live coding
    reuniones-de-equipo         daily, planning, retro: updates, bloqueos, estimar, discrepar
    escritura-tecnica           PRs, issues, design docs y RFC, documentación
    code-review                 comentar sin sonar brusco y recibir comentarios
    trabajo-remoto-asincronico  mensajería, hilos, status updates, zonas horarias, equipos no nativos
    incidentes                  avisar en vivo, on-call, postmortem sin culpables
    hablar-con-clientes         demos, relevar necesidades, explicar lo técnico a no técnicos
    recursos-de-ingles-tecnico  ficha fechada: guías de estilo, glosarios, cursos
  Fundamentos/
    niveles-mcer                qué sabe hacer alguien en B2, C1 y C2
    alfabeto-fonetico           leer la pronunciación del diccionario
    bibliografia-de-ingles      Swan, la serie «in Use», Learner English, Nation, Lightbown y Spada
    ruta-de-ingles              plan paso a paso con ejercicios y respuestas
```

## Supuestos

- Pronunciación con General American como modelo y las diferencias con el británico marcadas.
- ~~Inglés general, sin vertical de inglés profesional~~. Cambió el 2026-11-27: se suma la vertical `Profesional/`, el inglés de trabajo en la industria del software (inglés para fines específicos), para roles técnicos y de cara al cliente (desarrollo, IA, plataforma, consultoría, forward-deployed). Queda afuera el inglés de ventas y marketing. Lo general de la escritura, los turnos y la cortesía sigue en Discurso y la vertical lo enlaza.
- La escritura va dentro de Discurso.
- Exámenes, herramientas y plataformas de tutores van como fichas fechadas en Práctica.
- Ajustes después de investigar: feedback correctivo y edad salen como componentes propios; ritmo y habla conectada se juntan; registro y falsos amigos se juntan en cognados; Gramática suma estructura de la oración; Práctica parte el entrenamiento perceptivo y la conversación con IA, y la fluidez pasa a ser componente.
