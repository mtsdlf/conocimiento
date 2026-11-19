---
tipo: concepto
area: como-funciona
resumen: >-
  La incrementalidad es la parte de las ventas que no habría ocurrido sin el anuncio. Solo un experimento con grupo de control la mide, mientras que la atribución reparte crédito entre clics y el marketing mix modeling lo estima sobre series agregadas.
estado: borrador
estabilidad: estable
dueno: matias
umbral: true
responde: [P10]
es_un: []
parte_de: [medicion-de-marketing]
instancia_de: []
requiere: []
relacionado: [metrica-que-importa, efectos-de-corto-y-largo-plazo, growth-y-product-led-growth, respuesta-directa]
fuentes:
  - "Blake, Nosko y Tadelis (2015), Econometrica 83(1):155-174; copia del autor, versión forthcoming del 12/8/2014: https://faculty.haas.berkeley.edu/stadelis/BNT_ECMA_rev.pdf"
  - "Lewis y Rao (2015), QJE 130(4):1941-1973: https://gwern.net/doc/economics/advertising/2015-lewis.pdf"
  - "Gordon, Zettelmeyer, Bhargava y Chapsky, borrador del 12/4/2018: https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf"
  - "Gordon et al. (2019), Marketing Science 38(2):193-225 (solo metadatos): https://econpapers.repec.org/RePEc:inm:ormksc:v:38:y:2019:i:2:p:193-225"
  - "Vaver y Koehler (2011), geo experiments (resumen): https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/"
aliases: [incrementality, lift, lift incremental, efecto incremental, prueba de incrementalidad, holdout, geo experiment]
creado: 2026-11-18
revisado:
autoria: ia
idioma: es
---

# Incrementalidad

La incrementalidad es la parte de las ventas que no habría ocurrido sin el anuncio. Solo un experimento con grupo de control la mide, mientras que la atribución reparte crédito entre clics y el marketing mix modeling lo estima sobre series agregadas.

## Por qué existe

Los experimentos de campo de 2015 a 2019 mostraron que un canal suele atribuirse más de lo que causa. Los anuncios apuntan a quien ya iba a comprar. Lewis y Rao (2015) llaman a ese sesgo «a crippling concern for widely employed observational methods».

## Cómo funciona

| Método | Qué hace | Límite |
|---|---|---|
| Atribución | Reparte el crédito de las conversiones entre puntos de contacto | Mide correlación, no causa |
| Experimento | Asigna al azar quién no ve el anuncio: usuarios (holdout) o regiones (geo experiments) | Necesita mucho volumen |
| Marketing mix modeling | Regresión sobre series agregadas de gasto, estacionalidad y precio | Sin experimentos, puede confundir causa con coincidencia |

## Ejemplo

eBay apagó sus anuncios de marca en Yahoo! y MSN, y «almost all (99.5 percent)» del tráfico perdido llegó por búsqueda natural (Blake, Nosko y Tadelis 2015, copia del autor de 2014). El ROI observacional daba «over 4,100%» sin controles y «over 1,400%» con ellos; el experimental, «-63%», con IC 95% de -124% a -3%. La tabla 1 dice «over 4000» y «greater than 1500»: se citan rangos.

En 15 experimentos en Facebook, los métodos observacionales «mostly overestimate» el efecto, y en la mitad erraban por un factor de tres (Gordon et al.). En el estudio 4, expuestos contra no expuestos daban 316% de lift y el experimento 73% (borrador de 2018). La prensa cita 416% contra 77%, quizá de la versión de 2019, no leída.

## Qué implica para un equipo chico

Medir cada campaña puede ser inviable. En 25 experimentos con «$2.8 million» de gasto, el intervalo mediano del ROI superaba 100 puntos porcentuales (Lewis y Rao). Distinguir +50% de 0% exigiría una campaña mediana 9 veces más grande. Con poco volumen, la alternativa es apagar y prender un canal por período o zona y mirar ventas totales (inferencia).

> [!NOTE]
> Sin fuente todavía: marketing mix modeling con pocos datos, y experimentos en marcas nuevas, tiendas chicas o Argentina.

## Para profundizar

- **[Blake, Nosko y Tadelis (2015)](https://faculty.haas.berkeley.edu/stadelis/BNT_ECMA_rev.pdf)**: la introducción, la tabla 1 y la sección de anuncios de marca. Fijarse de dónde sale el contrafáctico. Alternativa: [Gordon et al.](https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf), estudio 4.

## Relaciones

- Parte de: [Medición de marketing](medicion-de-marketing.md) — su concepto umbral.
- Relacionado: [Una métrica que importa por etapa](metrica-que-importa.md) — sin experimento, esa métrica mide correlación.
- Relacionado: [Efectos de corto y largo plazo](../Marca-y-crecimiento/efectos-de-corto-y-largo-plazo.md) — estos experimentos miden el corto plazo, no el largo.
- Relacionado: [Growth marketing y product-led growth](../B2B-y-salida-al-mercado/growth-y-product-led-growth.md) — sus métricas de conversión no prueban causa sin control.
- Relacionado: [Respuesta directa](../Persuasion/respuesta-directa.md) — su respuesta no prueba causa.
