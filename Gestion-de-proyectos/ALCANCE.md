---
tema: Gestión de proyectos
para: llevar cualquier trabajo con incertidumbre hasta un resultado, sea software o no, cuando parte del trabajo lo hacen agentes de IA; lo leen Matias, Fer y los agentes
nivel: ya trabajó en proyectos y con agentes de IA; no se explica qué es un proyecto, una tarea ni un agente
escuela: adaptativa (el enfoque se elige según la incertidumbre), con el flujo y las restricciones (Reinertsen, Goldratt) como lente principal y el realismo de Flyvbjerg para pronosticar; lo predictivo y lo ágil entran como opciones dentro de Enfoque, no como eje; PMBOK 8, PRINCE2 7, ISO 21502 e IPMA ICB4 sirven para comprobar que no falte nada, no como columna
fuera:
  - lo propio del software: el encargo con el cliente, la estimación de software, contratos, plan de entregas y traspaso (tema Desarrollo, Desarrollo/Encargo; se enlaza)
  - descomponer en tareas para un agente de código y verificar su trabajo (tema Desarrollo, Definicion y Verificacion; se enlaza)
  - roadmap, priorización, Shape Up como método de producto y lanzamiento (tema Producto, Planificacion-y-entrega; se enlaza)
  - conducir personas, OKR, ritmo operativo, rendición de cuentas a nivel empresa, decidir, delegar en personas, reuniones y gestión del cambio (tema Liderazgo y dirección; se enlaza)
  - cómo funciona un agente por dentro, sus patrones técnicos, su planificación, fallas y benchmarks (tema IA, IA/Agentes; se enlaza)
  - flujo de valor y métricas DORA (tema DevOps; se enlaza)
  - la fábrica concreta de la organización, su contrato y su cola (repo de la fábrica y mtsdlf/procesos; acá solo lo general, sin nombrarla)
  - preparación para certificaciones (PMP) y compras públicas de grandes obras
fuentes: []
preguntas:
  - Tengo que llevar adelante algo que no es software (mudar una plataforma, lanzar un servicio), ¿cómo lo encuadro y qué enfoque elijo?
  - ¿Qué parte de este trabajo le doy a un agente, con cuánta autonomía y dónde pongo el control de una persona?
  - ¿Cómo pronostico cuándo termina, si la mitad la hacen agentes y no sé bien cuánto rinden?
  - ¿Cómo sé cómo va y cuándo tengo que meterme, sin reuniones de estado?
  - Tengo varios trabajos en paralelo y la revisión se me acumula, ¿qué hago?
  - ¿Qué del PMBOK y de Scrum sigo usando y qué dejo?
aprobado: 2026-11-27
---

# Alcance: Gestión de proyectos

El tema explica cómo se lleva un trabajo con incertidumbre hasta un resultado, en cualquier dominio, cuando una parte la ejecutan agentes de IA. Sale de la conversación del 2026-11-27, en la que se pidió documentar la gestión de proyectos sin atarla a prácticas que pierden vigencia y pensando en trabajar con una fábrica de agentes, donde la parte humana deja de estar en algunos pasos. Se decidió que es un tema aparte, agnóstico del dominio, y que el modelo operativo de personas y agentes (la fábrica, en general) es una vertical del tema y no un tema propio.

## Árbol

```
Gestion-de-proyectos/
  gestion-de-proyectos.md           el todo: las siete partes, qué cambia cuando ejecutan agentes y qué leer según la tarea
  Encuadre/                         qué resultado se busca, por qué vale y cómo se sabe que terminó
    justificacion                     por qué este trabajo y no otro, y cuándo deja de valer la pena
    resultado-y-terminado             el resultado como algo comprobable, no una lista de actividades
    alcance                           qué entra, qué no y qué queda fijo como línea base
    interesados                       quién gana, quién pierde y quién decide
  Enfoque/                          cómo se organiza el trabajo según su incertidumbre
    elegir-un-enfoque                 plan, iteración, flujo o apuesta, y cómo mezclarlos
    enfoque-predictivo                planificar todo antes: cuándo sirve y cuándo engaña
    enfoque-iterativo                 entregar por partes y aprender, sin ceremonias
    flujo-continuo                    colas, límite de trabajo en curso, costo de demora
    apuesta-con-tiempo-fijo           fijar cuánto vale algo en tiempo y recortar alcance
    etapas-y-puntos-de-control        tramos con una decisión de seguir o parar
  Planificacion/                    qué tiene un plan vivo y cuándo se rehace
    descomposicion-del-trabajo        piezas que se entregan y se verifican una por una
    dependencias-y-camino-critico     qué espera a qué; la cadena crítica
    pronostico                        por clase de referencia y por rangos; el sesgo de optimismo
    capacidad-y-costo                 cuánto se puede hacer y cuánto cuesta, con personas y agentes
  Personas-y-agentes/               la fábrica en general: quién hace qué y por dónde pasa el trabajo
    quien-hace-que                    quien decide, ejecuta, verifica y responde
    delegar-a-un-agente               intención, límites, criterio de terminado, presupuesto
    niveles-de-autonomia              cuánto decide el agente solo; gestión por excepción
    frontera-irregular                qué tareas dar a un agente cuando no se sabe de antemano
    patrones-de-trabajo               orquestador y trabajadores, hacer y revisar, persona en el bucle
    la-atencion-humana-como-restriccion  la revisión humana como cuello de botella
    horizonte-de-tareas               ficha: hasta qué largo de tarea completan hoy los agentes
  Seguimiento/                      saber cómo va y cuándo intervenir
    trabajo-en-curso-y-colas          WIP, tamaño de tanda, ley de Little
    medir-el-avance                   tiempo de entrega, rendimiento, curvas y valor ganado
    aceptar-con-evidencia             dar algo por hecho por lo que muestra
    control-de-cambios                cuando cambia lo pedido a mitad de camino
    informar-el-estado                lo que tiene que poder leer quien decide
    herramientas-de-seguimiento       ficha: herramientas para seguir el trabajo
  Incertidumbre-y-riesgo/           lo que puede salir distinto y cómo se trata
    riesgo                            identificar, responder, revisar
    supuestos                         lo que se dio por cierto y cómo se prueba temprano
    margenes                          reservas de tiempo y plata, dónde van y de quién son
    problemas-y-escalamiento          tolerancias y cuándo sube a una persona
    por-que-fallan-los-proyectos      la ley de hierro de Flyvbjerg y lo que sostienen los datos
  Gobierno-y-cierre/                quién manda sobre el proyecto y cómo termina
    gobierno-del-proyecto             patrocinador, aprobación, tolerancias, puertas
    portafolio                        cuántos proyectos en paralelo y cuáles entran
    cerrar-o-cancelar                 terminar bien o parar a tiempo
    aprender-de-un-proyecto           retrospectivas y análisis de fallas que cambian algo
  Fundamentos/
    fundamentos-de-gestion-de-proyectos   entrada de lo transversal
    escuelas-de-gestion-de-proyectos      predictiva, ágil, flujo, cadena crítica, apuestas, adaptativa, megaproyectos
    marcos-de-referencia                  ficha: cómo dividen el campo PMBOK 7 y 8, PRINCE2 7, ISO 21502, ICB4
    lo-que-pierde-peso-en-gestion-de-proyectos  ceremonias, horas-persona, cronogramas detallados
    mitos-de-gestion-de-proyectos         CHAOS, "el 70 % fracasa" y otros números
    bibliografia-de-gestion-de-proyectos
    glosario-de-gestion-de-proyectos
```

## Supuestos

- El nombre es «Gestión de proyectos», con «gestión del trabajo» como alias; la entrada lo define en sentido amplio, incluido el trabajo que entra sin parar.
- Va en el área «Negocio» de `conocimiento.md`.
- La evidencia sobre gestionar con agentes fuera del software es escasa; las notas de `Personas-y-agentes/` lo dicen y separan estudio con método, marco conceptual y opinión de practicante.
- Las notas no nombran herramientas ni ediciones de marcos fuera de las fichas.
