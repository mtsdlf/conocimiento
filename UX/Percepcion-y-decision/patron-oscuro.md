---
resumen: >-
  Un patrón oscuro es un diseño de interfaz que lleva a la persona a decidir lo que no habría decidido y que puede dañarla. La frontera con la persuasión legítima es disputada: los autores no coinciden en si importa la intención, el engaño o el daño.
estado: vigente
estabilidad: semi
fuentes:
  - "Mathur, Acar, Friedman, Lucherini, Mayer, Chetty y Narayanan (2019), Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites, CSCW 3, art. 81: https://arxiv.org/abs/1907.07032"
  - "Gray, Kou, Battles, Hoggatt y Toombs (2018), The Dark (Patterns) Side of UX Design, CHI 2018, paper 534: https://par.nsf.gov/servlets/purl/10057203"
  - "Luguri y Strahilevitz (2021), Shining a Light on Dark Patterns, Journal of Legal Analysis 13(1), 43-109; cifras del borrador de 2019: https://oag.ca.gov/sites/all/files/agweb/pdfs/privacy/shining-a-light-on-dark-patterns.pdf (versión publicada, solo metadatos: https://academic.oup.com/jla/article/13/1/43/6180579)"
  - "Mathur, Mayer y Kshirsagar (2021), What Makes a Dark Pattern... Dark?, CHI 2021: https://arxiv.org/abs/2101.04843"
  - "FTC, Bringing Dark Patterns to Light, informe del personal (septiembre de 2022): https://www.ftc.gov/reports/bringing-dark-patterns-light"
  - "Reglamento (UE) 2022/2065 (Ley de Servicios Digitales, DSA), art. 25: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065"
  - "Harry Brignull, deceptive.design (fuente de practicante): https://deceptive.design/"
  - "UX/.investigacion/percepcion-y-decision.md"
aliases: [dark pattern, dark patterns, deceptive design, diseño engañoso, patrones oscuros]
creado: 2026-11-22
revisado: 2026-11-22
---

# Patrón oscuro

Un patrón oscuro es un diseño de interfaz que lleva a la persona a decidir lo que no habría decidido y que puede dañarla. La frontera con la persuasión legítima es disputada: los autores no coinciden en si importa la intención, el engaño o el daño.

Harry Brignull acuñó el término en 2010 (según Gray et al. y la FTC). Lo definió como una interfaz "carefully crafted to trick users into doing things", que no es un error y se hace "with a solid understanding of human psychology". La FTC lo formula como "design practices that trick or manipulate users into making choices they would not otherwise have made and that may cause harm". Mathur et al. (2019) listan los sesgos cognitivos que explota, entre ellos anclaje, bandwagon, default, framing y escasez, que se tratan en [Percepción y decisión](percepcion-y-decision.md).

## Qué tipos hay

Mathur et al. (2019) rastrearon unos 11.000 sitios de compras (unas 53.000 páginas de producto) y hallaron 1.818 instancias de 15 tipos en 7 categorías. 183 sitios tenían prácticas engañosas y 22 terceros vendían los patrones como solución lista para instalar. Son cifras mínimas, porque solo miraron texto en una muestra de páginas. Los más frecuentes (instancias / sitios):

| Categoría | Tipos más frecuentes |
|---|---|
| Scarcity | Low-stock Message 632/581, High-demand Message 47/43 |
| Urgency | Countdown Timer 393/361, Limited-time Message 88/84 |
| Social Proof | Activity Message 313/264 |
| Misdirection | Confirmshaming 169/164, Pressured Selling 67/62 |
| Sneaking, Obstruction y Forced Action | Hidden Subscription 14/13, Hard to Cancel 31/31, Forced Enrollment 6/6 |

Gray et al. (2018), sobre 118 artefactos de practicantes, agrupan los tipos de Brignull en cinco estrategias: nagging, obstruction, sneaking, interface interference y forced action. Concluyen que los practicantes mezclan bajo un nombre problemas éticos muy distintos. deceptive.design lista 18 tipos y es una fuente de practicante.

## Qué evidencia hay de que funcionan

Luguri y Strahilevitz asignaron al azar a una muestra representativa de consumidores de EE. UU. a control, patrones suaves o agresivos, tras decirles que estaban inscriptos en un plan de protección contra robo de identidad. Aceptaron 11,3 % del control (73 de 644), 25,8 % con patrones suaves (155 de 600) y 41,9 % con agresivos (217 de 518). Contando a quienes abandonaron como rechazos, las cifras bajan a 25 % y 37 %. Son cifras del borrador de 2019; las de la versión publicada no se verificaron. Según el abstract, los agresivos generaron rechazo fuerte y los suaves no.

Casi toda la evidencia es de tiendas online y suscripciones en EE. UU.; para apps internas y dashboards no se encontraron estudios.

## Dónde termina la persuasión legítima

> [!IMPORTANT] No hay una definición única; cada posición pone la frontera en otro lugar.
>
> - La intención del diseñador (Brignull, 2010): es una interfaz hecha a propósito para engañar, "not mistakes".
> - Un concepto de ética mezclada (Gray et al., 2018): "design is inherently a persuasive act", y el problema es el grado "unreasonable" de persuasión.
> - Ninguna definición cierra (Mathur, Mayer y Kshirsagar, 2021): hallaron 19 definiciones que difieren en si exigen engaño, intención o daño. Confirmshaming suele ser transparente y Nagging no es engañoso por naturaleza, y se los llama igual patrones oscuros. Proponen cuatro lentes: bienestar individual, bienestar colectivo, objetivos regulatorios y autonomía individual.
> - El efecto medido (Luguri y Strahilevitz): hay que medir lo que el patrón produce. Los suaves son los que más justifican intervenir, porque rinden sin generar rechazo. Proponen una regla cuantitativa con pruebas A/B para decidir cuáles son ilegales.

Del lado de la persuasión, según Mathur et al., el nudge de Thaler y Sunstein "steer people in particular directions but that also allow them to go their own way", y Thaler llama "sludge" a la fricción excesiva que perjudica. En filosofía, la persuasión apela al razonamiento consciente y la manipulación lo subvierte. Según los mismos autores, todo el marketing moldea preferencias, y por eso la línea es un problema central de la lente de autonomía. El modelo de Fogg (la conducta ocurre cuando coinciden motivación, capacidad y un disparador) es el marco de la tecnología persuasiva; ninguna fuente leída lo usa para trazar esta frontera.

Un caso: el mensaje de poco stock (632 instancias) y el temporizador (393), los dos más frecuentes, no son engañosos por naturaleza, y lo son cuando el dato es falso (lectura de esta base a partir de las fuentes): 157 temporizadores, en 140 sitios, se reiniciaban tras vencer con la misma oferta vigente. Un criterio operativo, que es inferencia de esta base y no una cita: la cifra es verdadera y rechazar es tan fácil como aceptar.

Los mismos [sesgos](../../Psicologia/Juicio-y-decision/heuristicas-y-sesgos.md) aplicados al mensaje, y cuánto de su efecto resiste la replicación, están en [Economía del comportamiento en marketing](../../Marketing/Comunicacion/economia-del-comportamiento-en-marketing.md). Los defaults y las cancelaciones suelen vivir en los [formularios](../Interaccion/formularios.md). Luguri y Strahilevitz proponen decidir con pruebas A/B; esta base infiere que las [métricas de UX](../Evaluacion/metricas-de-ux.md) no distinguen por sí solas una variante mejor de un patrón oscuro que sube la conversión.

## Normativa, a 2026-11-22

Lo que sigue resume lo leído en dos textos, no reemplaza asesoramiento legal y no se revisó nada posterior a ellos (el informe de la FTC es de septiembre de 2022). Hay una sola fuente primaria por régimen.

- FTC (EE. UU.): Es un informe del personal, no una regla. Agrupa cuatro categorías: diseños que inducen creencias falsas, que ocultan o demoran información material, que llevan a cargos no autorizados y que subvierten opciones de privacidad. Se apoya en leyes vigentes, como la sección 5 de la FTC Act y ROSCA (suscripciones con opción negativa).
- DSA (UE), artículo 25: Las plataformas en línea no diseñarán sus interfaces "in a way that deceives or manipulates the recipients of their service or in a way that otherwise materially distorts or impairs the ability of the recipients of their service to make free and informed decisions". Excluye lo cubierto por la Directiva 2005/29/CE y el Reglamento (UE) 2016/679. La Comisión puede emitir guías, entre otras sobre "making the procedure for terminating a service more difficult than subscribing to it". El artículo no usa la expresión "dark patterns".

Las categorías no coinciden: la FTC se define por tipos de conducta y el DSA por el efecto sobre la decisión.

## Dónde leer más

Mathur et al. (2019), tabla 1, como mapa de qué mirar en una landing o un checkout. Mathur, Mayer y Kshirsagar (2021), sección 4, para decidir qué es y qué no es patrón oscuro. El artículo 25 del DSA y el informe de la FTC, como requisitos legales.

> [!NOTE] Sin fuente todavía: el informe de la Comisión Europea de 2022 sobre patrones oscuros, las guías sobre el artículo 25, el considerando 67 en EUR-Lex, la Directiva 2005/29/CE, y los textos de Thaler y Sunstein y de Fogg.
