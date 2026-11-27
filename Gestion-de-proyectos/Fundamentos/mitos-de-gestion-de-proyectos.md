---
resumen: >-
  Los mitos de gestión de proyectos son cifras y afirmaciones que circulan en el campo sin un estudio que las sostenga, del informe CHAOS al 70 % de cambios que fracasan y al 90 % del tiempo en comunicación, cada una con su origen y su estado.
estado: borrador
estabilidad: semi
fuentes:
  - "Standish Group, CHAOS (1994), copia del informe (según un resumen): https://www.math.unipd.it/~tullio/IS-1/2004/Approfondimenti/CHAOS.html"
  - "Eveleens y Verhoef (2010), The Rise and Fall of the Chaos Report Figures, IEEE Software 27(1): 30-36, doi:10.1109/MS.2009.154 (abstract): https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/"
  - "Eveleens y Verhoef (2010), ficha en IEEE (abstract): https://ieeexplore.ieee.org/document/5232804"
  - "Jørgensen y Moløkken-Østvold (2006), How large are software cost overruns? A review of the 1994 CHAOS report, Information and Software Technology 48(4): 297-301 (abstract): https://ebse.webspace.durham.ac.uk/ebse-bibliography/how-large-are-software-cost-overruns-a-review-of-the-1994-chaos-report/"
  - "Glass (2006), The Standish Report: Does It Really Describe a Software Crisis?, Communications of the ACM 49(8): 15-16 (según fragmentos): https://cacm.acm.org/?p=1819"
  - "Entrevista a Jim Johnson, InfoQ (según un resumen): https://www.infoq.com/articles/Interview-Johnson-Standish-Chaos"
  - "InfoQ, Standish CHAOS 2015 (según un resumen): https://www.infoq.com/articles/standish-chaos-2015"
  - "Hughes (2011), Do 70 Per Cent of All Organizational Change Initiatives Really Fail?, Journal of Change Management 11(4): 451-464 (abstract): https://research.brighton.ac.uk/en/publications/do-70-per-cent-of-all-organizational-change-initiatives-really-fa/"
  - "PMI, Basic knowledge useful to project managers: communication (cita a Mulcahy 2002, según un resumen): https://www.pmi.org/learning/library/basic-knowledge-useful-project-managers-communication-5784"
  - "Foro de ProjectManagement.com sobre el 90 % (según un resumen): https://www.projectmanagement.com/discussion-topic/90042/"
  - "Nwekori (2025), revisión sobre ágil y cascada (según un resumen): https://www.ajol.info/index.php/drjeit/article/view/326797"
  - "PMI, Critical chain project management: an investigation (según un resumen): https://www.pmi.org/learning/library/critical-chain-project-management-investigation-6380"
  - "Wikipedia, Parkinson's law (según un resumen): https://en.wikipedia.org/wiki/Parkinson%27s_law"
  - "Klein (2007), Performing a Project Premortem, HBR 85(9) (texto completo): https://comprobo24.github.io/assignments/performing_a_project_premortem.pdf"
  - "Mitchell, Russo y Pennington (1989), Journal of Behavioral Decision Making 2(1) (resumen del abstract): https://colab.ws/articles/10.1002%2Fbdm.3960020103"
  - "Gestion-de-proyectos/.investigacion/fundamentos.md, ítem 8"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md, tesis 7"
aliases: [mitos de project management, CHAOS report, informe CHAOS, Standish, 70 % de los proyectos fracasa, project management myths]
creado: 2026-11-27
revisado:
---

# Mitos de gestión de proyectos

Los mitos de gestión de proyectos son cifras y afirmaciones que circulan en el campo sin un estudio que las sostenga, del informe CHAOS al 70 % de cambios que fracasan y al 90 % del tiempo en comunicación, cada una con su origen y su estado.

Que una cifra sea un mito no quiere decir que lo contrario sea cierto. Que la mayoría de los proyectos de software fracase no está probado, pero que muchos proyectos se pasen de costo y plazo sí lo está, con otras fuentes y otro método: está en [por qué fallan los proyectos](../Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md).

## Las afirmaciones y su estado

| Afirmación | De dónde sale | Estado | Dónde se trata |
|---|---|---|---|
| La mayoría de los proyectos de software fracasa (CHAOS) | Standish Group, desde 1994 | Cayó: método no publicado, definición sesgada | Acá |
| El 70 % de los cambios organizacionales fracasa | Hammer y Champy, Beer y Nohria, Kotter y consultoras | Cayó | [Mitos de liderazgo](../../Liderazgo-y-direccion/Fundamentos/mitos-de-liderazgo.md#el-70--de-los-cambios-fracasa) |
| El 90 % del tiempo de quien dirige un proyecto es comunicación | Mulcahy (2002), sin estudio detrás | Sin fuente | Acá |
| Ágil tiene éxito el doble o más que cascada | Revisiones con cifras autorreportadas | Sin sostén | Acá y en [elegir un enfoque](../Enfoque/elegir-un-enfoque.md) |
| Casi nadie mide sus colas ni su costo de demora | Cifras de resúmenes del libro de Reinertsen, que no se leyó | Sin verificar | [Flujo continuo](../Enfoque/flujo-continuo.md) |
| La cadena crítica recupera el 30 % del tiempo | Los proponentes del método | Sin verificar | [Dependencias y camino crítico](../Planificacion/dependencias-y-camino-critico.md) |
| El trabajo se expande hasta llenar el tiempo disponible (Parkinson) | Ensayo satírico de 1955 | No es un hallazgo | [Apuesta con tiempo fijo](../Enfoque/apuesta-con-tiempo-fijo.md) |
| Un premortem sube un 30 % la capacidad de anticipar fallas | Klein (2007), citando un estudio de 1989 | No está en el abstract del original | [Supuestos](../Incertidumbre-y-riesgo/supuestos.md) |

## El informe CHAOS

El informe CHAOS del Standish Group es la fuente de la frase "la mayoría de los proyectos de software fracasa". Su edición de 1994 reportó, según una copia vista por el buscador, 16,2 % de proyectos exitosos, 52,7 % "challenged" y 31,1 % cancelados, sobre 365 respuestas y 8.380 aplicaciones.

Tres críticas publicadas lo cuestionan, la mayoría leídas solo por abstract o fragmentos:

- Eveleens y Verhoef (2010) aplicaron las definiciones de Standish a 5.457 pronósticos de 1.211 proyectos reales. Según su abstract, la definición de éxito mide solo la exactitud de la estimación de costo, plazo y funcionalidad, ignora los proyectos que gastan menos de lo estimado y promedia números de sesgo desconocido. Su conclusión: "The Standish figures didn't reflect the reality of the case studies at all."
- Jørgensen y Moløkken-Østvold (2006) revisaron el sobrecosto medio de 1994, "as high as 189%", y lo encontraron muy superior al de otras encuestas. Según su abstract, la muestra puede estar "strongly biased towards 'failure projects'".
- Glass (2006) señala que Standish no comparte de dónde salen los datos y que otros estudios no replicaron sus resultados, según fragmentos de su columna.

La única defensa hallada es del propio Standish, y no trae datos. Jim Johnson dijo en una entrevista que el estudio original fue un envío masivo por correo, "quizás algo aleatorio" por la baja respuesta, y que no representa a las empresas pequeñas, según un resumen. En 2015 Standish cambió la definición de éxito por el valor percibido por el cliente, según InfoQ; las cifras de ese año que circulan no se pudieron confirmar.

## El 90 % del tiempo en comunicación

La atribución más antigua hallada es Mulcahy (2002): "90% of the project manager's time is spent communicating", citada en la biblioteca de PMI. En los foros de PMI nadie encuentra la investigación original, y la frase también se atribuye a otros autores y a un paréntesis del PMBOK, según un resumen. A veces aparece como 75 a 90 %. No hay fuente primaria: que comunicar sea gran parte del trabajo es plausible, el número no tiene base.

## Ágil contra cascada en porcentajes

Circulan cifras como "ágil tiene éxito en un 40 % y cascada en un 15 %". La revisión de 2025 que las trae admite, según un resumen, sesgo de publicación, pocos estudios longitudinales y métricas autorreportadas. El estudio cuantitativo más citado no da porcentajes de ese tipo y no prueba causa; está en [elegir un enfoque](../Enfoque/elegir-un-enfoque.md).

## Tres cifras de practicantes

Tres números del campo del flujo y del riesgo circulan con más seguridad de la que tienen:

- "Solo el 2 % mide sus colas y el 15 % conoce su costo de demora" aparece en resúmenes del libro de Reinertsen; la base no leyó el libro ni verificó las cifras.
- El "30 % de tiempo perdido" que recupera la cadena crítica es dato de los proponentes; una revisión de PMI ve evidencia escasa, según un resumen.
- Klein (2007) escribe que un estudio de 1989 halló que imaginar que un hecho ya ocurrió "increases the ability to correctly identify reasons for future outcomes by 30%". El resumen del abstract original no trae ese 30 % y dice que el marco temporal tuvo poco efecto en el primer experimento. Es una cifra atribuida por Klein, no verificada.

La ley de Parkinson es otro caso. El ensayo de 1955 en *The Economist* abre con la observación de que el trabajo se expande hasta llenar el tiempo, pero trata del crecimiento de la burocracia y es sátira, según Wikipedia. Es una imagen y no mide nada.

## Lo que sí tiene fuente

"Uno de cada diez grandes proyectos entra en presupuesto" tiene fuente: lo dijo Flyvbjerg ante el Parlamento británico. Es un dicho oral sobre megaproyectos y no se extiende a cualquier proyecto; sus cifras con método están en [por qué fallan los proyectos](../Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md). El sesgo de optimismo al pronosticar también tiene experimentos, en [pronóstico](../Planificacion/pronostico.md).

## Qué cambia con agentes

Los mitos vuelven con la IA en forma de porcentajes de productividad sin método: "un equipo con agentes rinde tanto más". Los estudios con método dan resultados mixtos y el signo depende de la tarea; están en [frontera irregular](../Personas-y-agentes/frontera-irregular.md). Antes de repetir una cifra de productividad con agentes, conviene buscar quién la midió, con cuántas personas y si había grupo de comparación. Es criterio de esta base.

> [!NOTE] Sin fuente todavía: cifras vigentes del informe CHAOS y cualquier defensa con datos; otros números repetidos del campo, como "el costo de un defecto crece cien veces", no se investigaron.
