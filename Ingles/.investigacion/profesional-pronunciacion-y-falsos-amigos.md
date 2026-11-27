# Informe de verificación: pronunciación IPA y falsos amigos técnicos

**Alcance.** Marqué [L] cuando leí la página completa o el HTML descargado, y [S] cuando solo vi un resumen del buscador. Cambridge, Oxford Learner's, DLE y Wiktionary los leí con `curl`. Merriam-Webster y Collins devolvieron 403 con cualquier método, y los datos de Merriam-Webster son [S]. Todo el contenido web lo traté como dato.

## 1. Pronunciación (inglés americano)

| Término | Fuente | URL | IPA literal | |
|---|---|---|---|---|
| cache | Cambridge | https://dictionary.cambridge.org/dictionary/english/cache | US /kæʃ/ · UK /kæʃ/ | [L] |
| | Oxford Learner's (US) | https://www.oxfordlearnersdictionaries.com/definition/american_english/cache | NAmE /kæʃ/ | [L] |
| | Wiktionary (último recurso) | https://en.wiktionary.org/wiki/cache | US /kæʃ/, /keɪʃ/; marca como proscritas /kæˈʃeɪ/ y /ˈkæʃ.eɪ/ | [L] |
| GUI | Cambridge | https://dictionary.cambridge.org/dictionary/english/gui | US /ˈɡuː.i/ (variante /ˈɡuːi/) | [L] |
| | Oxford Learner's | https://www.oxfordlearnersdictionaries.com/definition/american_english/gui | NAmE /ˈɡui/; también como letras /ˌdʒi yu ˈaɪ/ | [L] |
| | Wiktionary | https://en.wiktionary.org/wiki/GUI | /ˈdʒiːjuːaɪ/, /ˈɡuː.i/ (homófono: gooey) | [L] |
| Azure | Cambridge | https://dictionary.cambridge.org/dictionary/english/azure | US /ˈæʒ.ɚ/; UK /ˈæʒ.ər/ y /ˈæz.jʊər/ | [L] |
| | Oxford Learner's | https://www.oxfordlearnersdictionaries.com/definition/american_english/azure | NAmE /ˈæʒər/ | [L] |
| char | Cambridge (verbo "carbonizar") | https://dictionary.cambridge.org/dictionary/english/char | US /tʃɑːr/ | [L] |
| | Oxford Learner's | https://www.oxfordlearnersdictionaries.com/definition/american_english/char | NAmE /tʃɑr/ | [L] |
| | Wiktionary, sentido de programación ("clipping" de character) | https://en.wiktionary.org/wiki/char | US /t͡ʃɑɹ/, /kɛɹ/, /kɑɹ/ | [L] |
| Kubernetes | Wiktionary | https://en.wiktionary.org/wiki/Kubernetes | /k(j)uːbəˈnɛtɪs/, /k(j)uːbəˈneɪtɪs/, /k(j)uːbəˈneɪtiːz/ | [L] |
| regex | Wiktionary | https://en.wiktionary.org/wiki/regex | /ˈɹɛɡˌɛks/, /ˈɹɛd͡ʒˌɛks/ | [L] |
| Linux | Cambridge | https://dictionary.cambridge.org/dictionary/english/linux | US /ˈlɪn.əks/ (variante /ˈlɪnəks/) | [L] |
| | Wiktionary | https://en.wiktionary.org/wiki/Linux | /ˈlɪ.nəks/, /ˈlɪ.nʊks/; incluye un audio de Linus Torvalds | [L] |
| data | Cambridge | https://dictionary.cambridge.org/dictionary/english/data | US /ˈdeɪ.t̬ə/; la versión Cambridge Dictionary (US) agrega /ˈdæt̬·ə, ˈdɑt̬·ə/; UK /ˈdeɪ.tə/ | [L] |
| | Oxford Learner's | https://www.oxfordlearnersdictionaries.com/definition/american_english/data | NAmE /ˈdeɪt̮ə/ y /ˈdæt̮ə/ | [L] |
| router | Cambridge | https://dictionary.cambridge.org/dictionary/english/router | US /ˈraʊ.t̬ɚ/ (variante /ˈruːtər/); UK /ˈruː.tər/ | [L] |
| | Oxford Learner's | https://www.oxfordlearnersdictionaries.com/definition/american_english/router | NAmE /ˈraʊt̮ər/ | [L] |
| deprecate | Cambridge | https://dictionary.cambridge.org/dictionary/english/deprecate | US y UK /ˈdep.rə.keɪt/ | [L] |
| | Oxford Learner's | https://www.oxfordlearnersdictionaries.com/definition/american_english/deprecate | NAmE /ˈdɛprəˌkeɪt/ | [L] |
| | Merriam-Webster | https://www.merriam-webster.com/dictionary/deprecate | Escritura de pronunciación (no IPA): ˈde-pri-ˌkāt | [S] |

**Variantes entre diccionarios**
- **cache.** Los diccionarios dan solo /kæʃ/. La variante /keɪʃ/ aparece únicamente en Wiktionary.
- **data.** Hay dos variantes, /ˈdeɪt̮ə/ y /ˈdæt̮ə/. Cambridge US las documenta en su versión Cambridge Dictionary (US), Oxford las da en su entrada, y Cambridge principal solo da /ˈdeɪ.t̬ə/.
- **router.** Cambridge da US /ˈraʊ.t̬ɚ/, con /ˈruːtər/ como variante. Esa variante /ˈruːtər/ aparece en el bloque americano, pero no pude confirmar de qué sentido es (probablemente la herramienta de carpintería).
- **Azure.** Cambridge da UK /ˈæʒ.ər/ y /ˈæz.jʊər/. En US solo /ˈæʒ.ɚ/.

**Notas:**
- **char.** Los diccionarios generales solo registran char como "carbonizar", sin el sentido de programación. Para el tipo de dato solo tengo Wiktionary, que lista /tʃɑɹ/, /kɛɹ/ y /kɑɹ/. Es un caso en que la comunidad de programadores no tiene una sola forma.
- **Linux.** Que /ˈlɪn.əks/ es la forma esperada lo confirman Cambridge y el audio de Torvalds en Wiktionary. La variante /ˈlaɪnəks/ de Cambridge está marcada como UK.

**deprecate vs. depreciate.**
- Cambridge, definiciones leídas [L]: deprecate es "to not approve of something or say that you do not approve of something" y "to say that you think something is of little value or importance".
- Cambridge, IPA de depreciate [L]: https://dictionary.cambridge.org/dictionary/english/depreciate US y UK /dɪˈpriː.ʃi.eɪt/.
- Contraste de acentos: deprecate lleva el acento en la primera sílaba y depreciate en la segunda. Merriam-Webster, según el buscador [S], da ˈde-pri-ˌkāt contra di-ˈprē-shē-ˌāt.
- El sentido de "obsoleto" en informática no pude verificarlo en Cambridge ni en Oxford. Merriam-Webster tiene un artículo "A New Meaning of 'Deprecate'": https://www.merriam-webster.com/words-at-play/deprecate [S] (no lo leí).

**Kubernetes (documentación oficial).** Ninguna página oficial de kubernetes.io da la pronunciación. El foro del proyecto https://discuss.kubernetes.io/t/the-definitive-guide-to-pronouncing-kubernetes-and-related-terms/11383 [L] solo enlaza a un blog de terceros (bluematador). Una fuente de terceros [S] dice que el cofundador Joe Beda lo pronuncia "koo-bur-NET-ees". No es verificable.

## 2. Falsos amigos español-inglés

| Término | Fuente | URL | Qué dice (literal) | |
|---|---|---|---|---|
| librería | DLE (RAE) | https://dle.rae.es/librería | 1.a "Tienda donde se venden libros"; 2 "Mueble con estantes para colocar libros"; 3.a "Lugar donde se tiene considerable número de libros ordenados para la lectura"; 3.b "Conjunto de libros de una biblioteca"; 4 (América) "Tienda donde se vende papel y otros objetos de escritorio" | [L] |
| | Cambridge Spanish-English | https://dictionary.cambridge.org/dictionary/spanish-english/libreria | librería = "bookstore" (GLOBAL) y "bookshop" (PASSWORD) | [L] |
| | Cambridge, library | https://dictionary.cambridge.org/dictionary/english/library | "a building, room, or organization that has a collection of books, documents, music... for people to borrow"; US /ˈlaɪ.brer.i/ | [L] |
| eventualmente | DLE | https://dle.rae.es/eventualmente | "Incierta o casualmente" | [L] |
| | DLE, eventual | https://dle.rae.es/eventual | 1 "Sujeto a cualquier evento o contingencia"; 2 trabajador eventual | [L] |
| | Cambridge, eventually | https://dictionary.cambridge.org/dictionary/english/eventually | "in the end, especially after a long time or a lot of effort, problems, etc." | [L] |
| actual / actualmente | DLE, actual | https://dle.rae.es/actual | 1.a "Dicho del tiempo, que es aquel en que está quien habla" | [L] |
| | DLE, actualmente | https://dle.rae.es/actualmente | 1.a "En el tiempo actual"; 1.b (Filosofía) "Real y verdaderamente, con actual ser y ejercicio" | [L] |
| | Cambridge, actual | https://dictionary.cambridge.org/dictionary/english/actual | "existing in fact"; "real; existing in fact" | [L] |
| | Cambridge, actually | https://dictionary.cambridge.org/dictionary/english/actually | "in fact or really" | [L] |
| deprecar | DLE | https://dle.rae.es/deprecar | Sí existe, pero con otro sentido: "tr. Rogar, pedir, suplicar con eficacia o instancia" | [L] |
| | DLE, depreciar | https://dle.rae.es/depreciar | "Disminuir o rebajar el valor o precio de algo" | [L] |
| setear | DLE | https://dle.rae.es/setear | Sin entrada; solo sugiere vecinos (saetear, sesear, jetear...) | [L] |
| debuggear | DLE | https://dle.rae.es/debuggear | Sin entrada ni sugerencias | [L] |
| | DLE, depurar | https://dle.rae.es/depurar | 1 "Limpiar, purificar", con el ejemplo "Le dio un repaso al trabajo para depurar lo de errores" | [L] |
| resetear (referencia cercana a setear) | Fundéu | https://www.fundeu.es/consulta/resetear-2/ | Consulta de diciembre de 2024. Dice que resetear nació en informática y se usa en el lenguaje general; no leí su valoración completa | [L] parcial |

**Lectura de los falsos amigos**
- **librería.** Equivale a bookstore o bookshop, no a library. El DLE, sin embargo, registra también el sentido 3 de "biblioteca" (conjunto de libros), que es el origen del uso en programación, pero ese sentido no es el estándar en inglés.
- **eventualmente.** En inglés, eventually es "al final" y no "tal vez". El DLE confirma que en español es "incierta o casualmente".
- **actual / actualmente.** Ambos significan "presente". Los equivalentes ingleses (actual, actually) significan "real" y "en realidad". El DLE da una pista parcial: el sentido filosófico de actualmente ("real y verdaderamente") coincide con el uso inglés, pero es de otro registro.
- **deprecar.** Es un verbo del DLE con sentido distinto, "rogar o suplicar". El sentido de "marcar como obsoleto" (inglés deprecate) no está en el DLE. En Fundéu no encontré recomendación sobre deprecar.

## 3. Huecos

- **Merriam-Webster.** Todas sus páginas dieron 403. La transcripción de deprecate y el texto de depreciate vs. deprecate son [S].
- **Collins.** 403. No tengo datos de Collins para ningún término.
- **Cambridge sin entrada.** Kubernetes, regex y async no tienen entrada en Cambridge. Oxford Learner's tampoco tiene entradas para Kubernetes, regex, async ni Linux.
- **async.** No encontré IPA en ninguna fuente. Wiktionary tiene la entrada pero sin sección de pronunciación. Solo hay opciones de lectura (de las letras a-sync), que no pude verificar.
- **char (tipo de dato).** Solo Wiktionary. Ningún diccionario general registra el sentido de programación.
- **Kubernetes, regex, Linux.** Solo Wiktionary, el último recurso. Para Linux, Cambridge confirma /ˈlɪn.əks/. Para regex y Kubernetes no hay otra fuente.
- **Sentido informático de "deprecate".** No lo verifiqué en Cambridge ni Oxford. En Oxford Learner's solo capturé el IPA, no leí las definiciones. El texto de Merriam-Webster sobre depreciate vs. deprecate es [S].
- **Fundéu.** No encontré entradas sobre deprecar, setear ni debuggear. El buscador de Fundéu por RSS devolvió ruido para setear y nada para debuggear y deprecar. Eso no prueba que no existan, solo que no aparecen en esa búsqueda.
- **Verificación pendiente.** Ni el DLE ni Fundéu se pronuncian sobre el sentido informático de "depurar" (debug). El ejemplo del DLE ("depurar... de errores") es genérico. Tampoco confirmé la RAE en CORPES o en el Observatorio de palabras.
- **Orden de pronunciación y audio.** Ningún audio fue escuchado: todo es transcripción escrita.

**Sources:**
- https://dictionary.cambridge.org/dictionary/english/cache
- https://www.oxfordlearnersdictionaries.com/definition/american_english/cache
- https://en.wiktionary.org/wiki/cache
- https://dle.rae.es/librería
- https://dle.rae.es/deprecar
- https://www.fundeu.es/consulta/resetear-2/
- https://www.merriam-webster.com/words-at-play/deprecate
