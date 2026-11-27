---
tema: Desarrollo de software
para: entender y hacer el proceso entero de convertir la necesidad de un cliente en software andando que el cliente recibe y mantiene, tal como se hace hoy con agentes de código; lo leen Matias, Fer y los agentes
nivel: programa y conoce lo básico de servicios, APIs y Git; no se explica qué es una función ni un repositorio
escuela: ingeniería de software moderna (Farley, Beck, DORA): pasos chicos, retroalimentación rápida y la prueba como especificación ejecutable; el desarrollo guiado por especificaciones con agentes como práctica emergente, con su evidencia; la planificación predictiva y el Scrum ceremonial como contraste
fuera:
  - qué producto construir, para quién y por qué (tema Producto; se enlaza)
  - estructura del sistema, estilos y patrones (tema Arquitectura; se enlaza desde la etapa de diseño)
  - integrar, desplegar y operar en producción (tema DevOps; se enlaza)
  - cómo funciona un modelo de lenguaje (tema IA; se enlaza)
  - vender el proyecto, la propuesta comercial y el precio de lista (tema Ventas; se enlaza)
  - el diseño propio de una fábrica de software con agentes (va al repo de la empresa o a mtsdlf/procesos; acá solo lo general)
  - lo que pierde peso, que solo se nombra en Fundamentos/lo-que-pierde-peso
fuentes: []
preguntas:
  - Un cliente me trae una idea vaga, ¿qué tengo que tener escrito antes de que un agente escriba la primera línea?
  - ¿Cómo parto un producto en tareas que un agente haga solo y que yo pueda verificar sin leer cada línea?
  - ¿Qué revisa una persona, qué se deja a las pruebas y qué a otro agente?
  - ¿Cómo estimo y cobro un proyecto cuando el código sale casi gratis?
  - El cliente cambia lo que quiere a mitad del proyecto, ¿cómo lo manejo sin romper el acuerdo?
  - ¿Qué de lo que se enseñaba sobre el proceso de desarrollo ya no conviene aprender primero?
aprobado: 2026-11-27
---

# Alcance: Desarrollo de software

El tema explica cómo una necesidad se convierte en software andando: el ciclo con el cliente (acordar, entregar incrementos, aceptar, traspasar) y, adentro, el ciclo técnico (definir, construir, verificar, integrar). Sale de la conversación del 2026-11-27, en la que se pidió documentar el desarrollo de software con la mirada puesta en un desarrollo casi automatizado con IA, sin lo que está en desuso ni lo que no se alinea con hacia dónde va la industria. Esa mirada filtra qué entra y cómo se cuenta; la automatización en sí no es un tema a documentar. Reordena y amplía el tema `Desarrollo/`, que ya existía con Git, configuración, arquetipos e historias de usuario.

## Árbol

```
Desarrollo/
  desarrollo.md                   el todo: los dos ciclos, quién hace cada paso y cómo se conectan con Producto, Arquitectura y DevOps
  Encargo/                        el ciclo con el cliente, de "tengo una idea" a "es suyo y lo mantiene"
    acuerdo-inicial                 entender el problema y el resultado que el cliente busca
    alcance-y-aceptacion            qué entra, qué no y cómo se decide que está terminado
    estimacion                      cómo se estima cuando construir es barato: rangos, apetito, previsión por ritmo
    modelos-de-contrato-y-cobro     precio cerrado, tiempo y materiales, alcance variable, por resultado
    plan-de-entregas                incrementos que el cliente puede ver y usar
    cambios-de-alcance              qué hacer cuando el cliente pide otra cosa a mitad del proyecto
    seguimiento-con-el-cliente      qué se le muestra, cada cuánto y con qué evidencia
    traspaso                        entregar código, accesos, documentación y operación
  Definicion/                     pasar de una intención a algo que se puede construir sin adivinar
    especificacion                  la especificación como insumo principal (spec-driven)
    historia-de-usuario             (ya existía)
    criterios-de-aceptacion         ejemplos verificables (dado/cuando/entonces)
    descomposicion-en-tareas        tareas que se hacen solas y se verifican solas
    modelo-de-dominio               el vocabulario del negocio, igual en el código y en las notas
  Construccion/                   escribir el código, con agentes como parte del oficio
    contexto-del-repositorio        lo que un agente necesita saber del repo (AGENTS.md, skills, docs)
    agente-de-codigo                cómo trabaja uno, dónde rinde y dónde falla
    plantilla-de-proyecto           que todo proyecto arranque igual (Generacion-de-proyectos se funde acá; Maven queda como ficha)
    arquetipo-de-maven, derivar-nombres-en-un-arquetipo-de-maven   (ya existían; fichas de plantilla-de-proyecto)
    Configuracion/                  (ya existía)
    Git/                            (ya existía)
  Verificacion/                   cómo se sabe que lo construido hace lo que se pidió
    piramide-de-pruebas             qué se prueba a qué nivel
    tdd                             la prueba primero, como contrato
    disenar-casos-de-prueba-de-api  (ya existía)
    revision-de-codigo              qué revisa una persona, qué otro agente y qué una herramienta
    verificar-lo-que-hizo-un-agente señales de trabajo incompleto o inventado
  Evolucion/                      el software después de la primera entrega
    deuda-tecnica                   cuándo se paga y cuándo no
    refactorizar                    cambiar la forma sin cambiar el comportamiento
    sistema-heredado                entrar a un código que no escribiste
    migraciones-y-actualizaciones   dependencias, versiones y cambios masivos
  Fundamentos/
    escuelas-de-desarrollo          ágil, Shape Up, spec-driven, predictivo, y las posturas sobre la IA
    lo-que-pierde-peso-en-desarrollo  lo que se dejó afuera, con su evidencia y quién lo dice
    bibliografia-de-desarrollo
    glosario-de-desarrollo
```

## Supuestos

- Después de investigar (2026-11-27): `estimacion` se separó de `modelos-de-contrato-y-cobro`; la mutación de pruebas va como sección de `verificar-lo-que-hizo-un-agente`; quedan nombrados como pendientes en su entrada `entorno-reproducible`, `dependencias`, worktrees (en Git), `seguridad-en-el-desarrollo` (enlaza a DevSecOps) y `evidencia-y-medicion`. Requisitos no funcionales y prototipo no tienen nota: los cubren Arquitectura (Características) y Producto (Descubrimiento).

- Se mantiene la carpeta `Desarrollo/` para no romper enlaces; el título del tema pasa a "Desarrollo de software". Las notas que ya existían se mudan a su vertical con `git mv` y se actualizan sus enlaces en toda la base.
- La etapa de diseño no tiene vertical: enlaza a Arquitectura. Integrar y desplegar enlaza a DevOps.
- El ciclo con el cliente es una vertical (`Encargo/`) y no un tema aparte, porque lo que se acuerda en el alcance es lo que se especifica, se construye y se acepta.
- Profundidad de esta primera pasada: el árbol entero con la entrada de cada vertical; `Encargo/` y `Definicion/` a fondo; `Construccion/`, `Verificacion/` y `Evolucion/` en panorama, con los componentes que no se escriban nombrados en su entrada.
- Una vertical `Fabrica/` (autonomía de agentes, orquestación) se propuso y se descartó: la automatización es la mirada del tema, no una parte de él.
- La lista de lo que pierde peso arranca de criterio propio, a verificar con fuentes: el documento de requisitos gigante al principio, story points como medida de productividad, Scrum con todas sus ceremonias, Gitflow (ya está en DevOps) y la cobertura como objetivo.
