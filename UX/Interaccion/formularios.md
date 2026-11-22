---
resumen: >-
  Un formulario funciona mejor con etiquetas visibles fuera del campo, validación en línea cuidada y la menor cantidad de campos posible; los estudios que lo sostienen son chicos o de instituto, y por eso sus cifras se leen como indicativas.
estado: borrador
estabilidad: semi
fuentes:
  - "Matteo Penzo, Label Placement in Forms, UXmatters, 12 de julio de 2006: https://www.uxmatters.com/mt/archives/2006/07/label-placement-in-forms.php"
  - "Luke Wroblewski, Inline Validation in Web Forms, A List Apart, 1 de septiembre de 2009: https://alistapart.com/article/inline-validation-in-web-forms/"
  - "Luke Wroblewski, Web Form Design: Filling in the Blanks, Rosenfeld Media, 2008 (solo índice)"
  - "Baymard Institute, Checkout Flow Average Form Fields, 26 de junio de 2024: https://baymard.com/blog/checkout-flow-average-form-fields"
  - "Baymard Institute, Cart Abandonment Rate Statistics: https://baymard.com/lists/cart-abandonment-rate"
  - "NN/g, Sherwin, Placeholders in Form Fields Are Harmful, 11 de mayo de 2014 (rev. 10 de septiembre de 2018): https://www.nngroup.com/articles/form-design-placeholders/"
  - "Estudio de Napier University sobre alineación de etiquetas (solo resumen del buscador): https://napier-repository.worktribe.com/OutputFile/232503"
  - "UX/.investigacion/arquitectura-e-interaccion.md"
aliases: [formulario, formularios web, validación en línea, checkout, form design]
creado: 2026-11-22
revisado:
---

# Formularios

Un formulario funciona mejor con etiquetas visibles fuera del campo, validación en línea cuidada y la menor cantidad de campos posible; los estudios que lo sostienen son chicos o de instituto, y por eso sus cifras se leen como indicativas.

Es el punto donde la [interacción](interaccion.md) pide trabajo a la persona, y donde los [principios de interacción](principios-de-interaccion.md) (feedback, prevención de errores, control) se vuelven decisiones concretas. Cada campo puede sumar [carga cognitiva](../Percepcion-y-decision/carga-cognitiva.md); un formulario que fuerza crear una cuenta cruza con el [patrón oscuro](../Percepcion-y-decision/patron-oscuro.md). Las etiquetas y el contraste de los textos auxiliares son también asunto de [accesibilidad](../Accesibilidad/accesibilidad.md).

## Dónde poner la etiqueta

Penzo (2006) probó con eye-tracking, con expertos y novatos y sin diseño visual, tres posiciones. El número de participantes no figura en lo leído.

| Posición | Lo que midió Penzo |
|---|---|
| Izquierda, alineada a la izquierda | Sacadas de unos 500 ms, que el autor lee como carga cognitiva alta |
| Izquierda, alineada a la derecha | Fijaciones y tiempo casi a la mitad (sin base de comparación en lo leído); sacadas de unos 170 ms (expertos) y 240 ms (novatos) |
| Arriba | La mayoría de las fijaciones cae en los campos; sacadas de unos 50 ms |

Su conclusión: arriba suele funcionar mejor, y si deben ir al costado, alineadas a la derecha. El propio autor lo describe como punto de partida, no como respuesta final.

> [!IMPORTANT]
> Disputado. Penzo (2006) favorece las etiquetas arriba. Según un resumen de buscador, sin leer el texto, un estudio de Napier University halló arriba y derecha cerca en velocidad (cinco participantes más rápidos con la alineación a la derecha y cinco con la de arriba, con una diferencia de al menos 3 segundos, cerca de 5 % del tiempo total) y sugiere que la brecha puede deberse al diseño de columnas. Según un resultado de buscador, las diapositivas de Wroblewski dicen cosas como "diez veces más rápido" sin aclarar la comparación; esta base no cita esas cifras.

## Validación en línea: qué mejoró y qué empeoró

Wroblewski publicó en 2009 un estudio con Etre: 22 usuarios de 21 a 49 años, seis variantes de un formulario de registro, en orden aleatorio. El control validaba solo al hacer clic en "crear cuenta". La mejor variante, contra ese control, dio:

- éxito de completado: +22 %;
- errores: -22 %;
- satisfacción: +31 %;
- tiempo de completado: -42 %;
- fijaciones oculares: -47 %.

Las salvedades pesan tanto como las cifras. En preguntas obvias, como el nombre, solo entre 30 % y 50 % notó los mensajes, y la marca verde confundió. Validar mientras la persona escribe empeoró el tiempo, los errores y la satisfacción. Los mensajes de éxito que se desvanecen se pierden. Con 22 personas, los números son indicativos y no estimaciones estables. Sobre el contenido del mensaje de error, NN/g pide que explique cómo arreglarlo y no solo qué falló, y desaconseja los toasts para errores (ver [Interacción](interaccion.md)).

## Cuántos campos y cuánto abandono de checkout

Baymard (26 de junio de 2024) midió que "the average in 2024 was 11.3 form fields" en checkouts, y sostiene que "most sites need only 8 form fields in total". Una búsqueda sobre otras páginas suya da la serie 12,7 (2019), 11,8 (2021) y 11,3 (2024), pero esa serie es de buscador, sin leer.

La cifra de abandono por complejidad difiere según la página, y esta base da las tres con su fecha en vez de elegir una:

| Cifra | Fuente |
|---|---|
| 26 % ("too long or too complex") | artículo de 2019, según el buscador |
| 22 % | otra página de Baymard, según el buscador |
| 17 % ("have abandoned due to checkout complexity") | página de 2024, leída; cita su estudio premium GC050 sin tamaño de muestra |

En su lista de abandono de carrito, Baymard promedia 70,22 % sobre 50 estudios publicados entre 2006 y 2025, sin contar "solo estaba mirando". Los motivos: costos extra, 40 %; entrega lenta, 20 %; desconfianza en la tarjeta, 19 %; pedían crear cuenta, 18 %; proceso largo o complicado, 17 %; errores del sitio, 17 %; devoluciones, 13 %; no ver el total, 12 %; tarjeta rechazada, 10 %; pocos medios de pago, 9 %. La página no da la muestra ni la fecha de la encuesta de motivos. Baymard es un instituto con método propio y de pago; en lo leído no hay revisión de pares ni auditoría independiente de sus cifras.

## Placeholders: por qué no reemplazan a la etiqueta

Sherwin (NN/g, 2014, revisado en 2018) dice que el placeholder "makes it difficult for people to remember what information belongs in a field". Enumera siete problemas: memoria, imposibilidad de revisar lo escrito, dificultad para recuperarse de errores, fricción con el tabulador, campos llenos menos notables según eye-tracking, lectura como dato precargado y el trabajo de borrarlos. Suma el bajo contraste y que algunos lectores de pantalla no los anuncian.

Su recomendación: no usarlos como reemplazo de etiquetas, poner etiquetas visibles fuera del campo y pistas persistentes también fuera, y dejar el placeholder para ejemplos complementarios. Las etiquetas flotantes son mejores que la etiqueta usada como placeholder, pero peores que la etiqueta fuera del campo.

## Formularios en sistemas internos

> [!NOTE]
> Sin fuente todavía: formularios largos y entrada de datos en sistemas internos. Cooper dedica un capítulo a la entrada, el almacenamiento y la recuperación de datos, pero solo se leyó el índice.

Para profundizar, leer *Web Form Design* de Wroblewski (etiquetas, acciones, ayuda y validación), junto con "Inline Validation in Web Forms", y el artículo de Baymard para checkout. En ambos estudios hay que fijarse en el tamaño de la muestra y en que son de 2006 y 2009.
