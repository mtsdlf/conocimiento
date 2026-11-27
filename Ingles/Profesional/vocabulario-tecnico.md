---
resumen: >-
  El vocabulario técnico del software se escribe en inglés también en castellano, pero se pronuncia
  y se usa distinto: algunos términos tienen una pronunciación fijada por su proyecto, otros
  conviven con dos o más, y varios préstamos del castellano técnico son falsos amigos.
estado: borrador
estabilidad: semi
fuentes:
  - "nginx.org: https://nginx.org/en/"
  - "YAML Ain't Markup Language, versión 1.2.2: https://yaml.org/spec/1.2.2/"
  - "MySQL 8.0 Reference Manual, What is MySQL?: https://dev.mysql.com/doc/refman/8.0/en/what-is-mysql.html"
  - "PostgreSQL, A brief history of PostgreSQL: https://www.postgresql.org/docs/current/history.html"
  - "Oracle Database SQL Language Reference, History of SQL: https://docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/History-of-SQL.html"
  - "Lista sudo-users (julio de 2006), mensaje de Todd Miller, vía resumen: https://sudo.ws/pipermail/sudo-users/2006-July/002913.html"
  - "NPR (2013), GIF talk: https://www.npr.org/sections/thetwo-way/2013/05/22/186031226/gif-talk-do-you-say-it-with-a-g-or-j"
  - "Wikipedia, GIF (sección de pronunciación): https://en.wikipedia.org/wiki/GIF"
  - "Grunenwald, kubectl: the definitive pronunciation guide (Opensource.com): https://opensource.com/article/18/12/kubectl-definitive-pronunciation-guide"
  - "Cambridge Dictionary, entradas cache, GUI, azure, Linux, data, router, deprecate, depreciate, library, eventually, actual, actually: https://dictionary.cambridge.org/"
  - "Oxford Learner's Dictionaries (American English), entradas cache, GUI, azure, data, router, deprecate: https://www.oxfordlearnersdictionaries.com/"
  - "Wiktionary, entradas char, Kubernetes, regex (último recurso): https://en.wiktionary.org/"
  - "Diccionario de la lengua española (RAE), entradas librería, eventualmente, actual, actualmente, deprecar, depurar: https://dle.rae.es/"
  - "Ingles/.investigacion/profesional-pronunciacion-y-falsos-amigos.md"
aliases:
  - Jerga técnica
  - Technical vocabulary
  - Pronunciación de términos técnicos
  - Falsos amigos técnicos
creado: 2026-11-27
revisado:
---

# Vocabulario técnico

El vocabulario técnico del software se escribe en inglés también en castellano, pero se pronuncia y se usa distinto: algunos términos tienen una pronunciación fijada por su proyecto, otros conviven con dos o más, y varios préstamos del castellano técnico son falsos amigos.

Quien trabaja en software ya lee *cache*, *deploy* o *router* todos los días. Lo difícil es que esas palabras se aprendieron leyendo y se pronuncian con las reglas del castellano, o que el préstamo castellano (*librería*, *deprecar*) arrastra un significado que en inglés no es el mismo. Es un caso particular de lo que tratan [Cognados y falsos amigos](../Lexico/cognados-y-falsos-amigos.md) y [Acento de palabra](../Pronunciacion/acento-de-palabra.md). Las transcripciones usan el [alfabeto fonético](../Fundamentos/alfabeto-fonetico.md) en su versión americana.

## Los que el proyecto fijó

Algunos proyectos dicen en su documentación cómo se pronuncia su nombre:

- **nginx**: la página oficial lo escribe `nginx ("engine x")`, es decir, *engine-x*.
- **YAML**: la especificación dice que se pronuncia "rhymes with 'camel'". Es un acrónimo recursivo de "YAML Ain't Markup Language".
- **MySQL**: "The official way to pronounce 'MySQL' is 'My Ess Que Ell' (not 'my sequel'), but we do not mind if you pronounce it as 'my sequel' or in some other localized way."
- **PostgreSQL**: la documentación reconoce que "people find it easier to pronounce Postgres than PostgreSQL", y *Postgres* sigue siendo un nombre oficial.
- **Linux**: Cambridge da /ˈlɪn.əks/ para el inglés americano, con la primera vocal corta de *lip* y no la /aɪ/ de *line*. El sitio del kernel conserva una grabación de Linus Torvalds diciéndolo, que no se transcribió.

## Los que están en disputa

En otros términos hay una forma "oficial" que el uso no siguió, o ninguna. Lo útil es reconocer todas al escuchar y elegir una sin culpa.

| Término | Formas en uso | Qué dicen las fuentes |
|---|---|---|
| SQL | *S-Q-L* y *sequel* | El lenguaje nació como SEQUEL y, según Wikipedia, cambió de nombre por una marca registrada. Oracle dice que su SQL se sigue pronunciando *sequel*; MySQL prefiere las letras. |
| GIF | /ɡɪf/ y /dʒɪf/ | Su creador, Steve Wilhite, dijo en los Webby de 2013: "It is a soft 'G,' pronounced 'jif'." Según Wikipedia, Oxford y Merriam-Webster registran las dos, con la g dura primero. |
| sudo | *sue-doo* y otras | El mantenedor, Todd Miller, escribió en 2006: "The correct pronunciation is sue due / soo doo for 'superuser do'". En la misma lista otros responden que las formas son intercambiables, y hay quien defiende una parecida a *pseudo*. |
| kubectl | *kube-control*, *kube-cuttle*, *kube-cuddle*, *cube-see-tee-ell* y más | En la documentación oficial revisada no aparece. Una charla de 2018 contó "over a dozen ways". |
| Kubernetes | /kuːbərˈnɛtɪs/, con variantes en la vocal acentuada y el final | Solo Wiktionary la transcribe; el proyecto no publica una pronunciación. |
| char | /tʃɑːr/ (como *charcoal*), /kɛr/ o /kɑːr/ (como *character*) | Solo Wiktionary registra el sentido de programación; los diccionarios generales no lo traen. |
| regex | /ˈrɛɡɛks/ y /ˈrɛdʒɛks/ | Solo Wiktionary. |
| data | /ˈdeɪt̮ə/ y /ˈdæt̮ə/ | Oxford Learner's da las dos para el inglés americano. |

Si no sabés cómo lo dice tu equipo, preguntalo sin problema, por ejemplo con una frase propia: *Do you guys say S-Q-L or sequel?*

## Los que se suelen decir mal

Estos sí tienen una forma clara en los diccionarios, y la lectura en castellano suele errarla:

| Término | Cómo se dice | Error típico |
|---|---|---|
| cache | /kæʃ/, igual que *cash* (Cambridge y Oxford) | *ca-ché* (Wiktionary marca /kæˈʃeɪ/ como forma proscrita y acepta /keɪʃ/ como variante) |
| GUI | /ˈɡuːi/, como *gooey* (Cambridge y Oxford); también se oye deletreado, *G-U-I* | *gui* con u muda, como en castellano |
| Azure | /ˈæʒɚ/ en inglés americano (Cambridge y Oxford) | *a-sur*, con acento al final |
| router | /ˈraʊt̮ɚ/ en inglés americano; /ˈruːtə/ en británico | mezclar las dos en la misma conversación |
| deprecate | /ˈdɛprəkeɪt/, acento en la primera sílaba | confundirlo con *depreciate* /dɪˈpriːʃieɪt/, que es perder valor (*depreciar*, en el DLE) |
| Linux | /ˈlɪnəks/ | *lai-nux* |

La regla de fondo es la del [acento de palabra](../Pronunciacion/acento-de-palabra.md): el acento mal puesto rompe más la comprensión que una vocal imperfecta.

## Falsos amigos del castellano técnico

El castellano técnico tomó palabras del inglés y les dio otro significado, o usa palabras castellanas que se parecen a otras inglesas:

- **Librería y library.** En castellano general, *librería* es la tienda donde se venden libros; en inglés eso es *bookstore* o *bookshop*. En el software se dice *library*, que en inglés es una biblioteca; el DLE también registra *librería* como "conjunto de libros de una biblioteca", y por ahí entró el uso técnico en castellano (inferencia propia). Al hablar en inglés es siempre *library*; *bookstore* no tiene nada que ver.
- **Eventualmente y eventually.** El DLE define *eventualmente* como "incierta o casualmente", y Cambridge define *eventually* como "in the end, especially after a long time or a lot of effort". *The data will eventually be consistent* es "va a terminar siendo consistente", no "quizás". Por eso *eventual consistency* es consistencia final.
- **Actual y actually.** En castellano *actual* es "del presente". En inglés *actual* es "existing in fact" y *actually*, "in fact or really". *The actual value* es el valor real; para el valor presente se dice *the current value*.
- **Deprecar y deprecate.** El DLE registra *deprecar*, pero como "rogar, pedir, suplicar con eficacia o instancia". El sentido de marcar algo como obsoleto viene del inglés *deprecate*. En inglés es correcto; en castellano es un calco que ya se usa en el oficio.
- **Setear y debuggear.** No tienen entrada en el DLE. Son préstamos adaptados del oficio; el DLE trae *depurar* con un ejemplo cercano, "depurar lo de errores". En inglés se dice *set* y *debug*, sin problema.

> [!NOTE]
> Sin fuente todavía: la pronunciación de *async* (ningún diccionario la trae) y una fuente de la RAE o la Fundéu sobre el sentido informático de *deprecar*, *setear* y *depurar*.
