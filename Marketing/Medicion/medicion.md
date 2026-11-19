---
resumen: >-
  La medición es la parte del marketing que dice si funciona: qué métrica seguir según la etapa del negocio, si cada venta deja plata y si un canal causa las ventas o solo las acompaña.
estado: borrador
estabilidad: estable
fuentes:
  - "Blake, Nosko y Tadelis (2015), Econometrica 83(1):155-174; copia del autor: https://faculty.haas.berkeley.edu/stadelis/BNT_ECMA_rev.pdf"
  - "Lewis y Rao (2015), QJE 130(4):1941-1973: https://gwern.net/doc/economics/advertising/2015-lewis.pdf"
  - "Gordon, Zettelmeyer, Bhargava y Chapsky, borrador del 12/4/2018: https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf"
  - "Alistair Croll y Benjamin Yoskovitz, Lean Analytics (2013)"
  - "Binet y Field, presentación de The Long and the Short of It (IPA): https://ipa.co.uk/media/14463/long_and_short_of_it_presentation_final_030424.pdf"
  - "Ward y Sharp (2024), Three common mistakes in awards entries: https://ipa.co.uk/knowledge/ipa-blog/three-common-mistakes-in-awards-entries/"
  - "Informe .investigacion/medicion-y-persuasion.md, sección P10"
creado: 2026-11-19
revisado:
---

# Medición

La medición es la parte del marketing que dice si funciona: qué métrica seguir según la etapa del negocio, si cada venta deja plata y si un canal causa las ventas o solo las acompaña.

Es la parte que cierra el circuito. Evalúa lo que hicieron los [canales](../Canales/canales.md) y la [comunicación](../Comunicacion/comunicacion.md), y lo aprendido vuelve a corregir a quién se le habla en [Mercado y cliente](../Mercado-y-cliente/mercado-y-cliente.md) y qué se le promete en la [propuesta](../Propuesta/propuesta.md). La [marca](../Marca/marca.md) le pone un límite: sus efectos largos no se ven en las ventas de la semana y se miden con otras métricas.

## Un canal que convierte puede no causar la venta

La idea que ordena la medición es la diferencia entre correlación y causa. Los anuncios no se reparten al azar: apuntan a quien ya iba a comprar. Lewis y Rao (2015) llaman a ese sesgo de selección «a crippling concern for widely employed observational methods». Por eso todas las métricas de esta parte se leen con esa advertencia.

El caso más citado es el de eBay. Al apagar sus anuncios de marca en Yahoo! y MSN, casi todo el tráfico perdido llegó igual por búsqueda natural, y el retorno que daba positivo sin experimento salió negativo con él. Las cifras y su lectura están en [incrementalidad](incrementalidad.md).

## Atribución, experimento y marketing mix modeling

Tres métodos responden preguntas distintas sobre el mismo gasto:

- **La atribución** reparte el crédito de las conversiones entre los puntos de contacto. Mide correlación, no causa.
- **El experimento con grupo de control** asigna al azar quién no ve el anuncio, por usuario (holdout) o por región (geo experiments). Es el único que mide la incrementalidad, pero necesita mucho volumen.
- **El marketing mix modeling** es una regresión sobre series agregadas de gasto, estacionalidad y precio. Sin experimentos, puede confundir causa con coincidencia.

En 15 experimentos en Facebook, los métodos observacionales sobre todo sobreestimaron el efecto, y ninguno ganó de forma consistente (Gordon et al., borrador de 2018). Si conviene calibrar un marketing mix modeling con experimentos está en disputa: las plataformas que publican herramientas de MMM lo proponen, y un proveedor sostiene lo contrario con un estudio propio, no independiente (según resúmenes secundarios).

## Cuánto volumen pide medir

Para un equipo chico, medir cada campaña puede ser inviable. En los 25 experimentos de Lewis y Rao, el intervalo mediano del ROI superaba los 100 puntos porcentuales. Con poco volumen, lo que queda es apagar y prender un canal por período o por zona y mirar las ventas totales, no la atribución por clic (inferencia de la base sobre Lewis y Rao). Cómo se llega a ese número está en [incrementalidad](incrementalidad.md).

## Qué se mide a corto y a largo plazo

Los experimentos de incrementalidad miden el corto plazo, no el largo. Según Binet y Field, el corto plazo se mide con respuestas directas, cupones o ventas inmediatas, y el largo con cuota, rentabilidad, cuota de voz en exceso y elasticidad de precio. Ward y Sharp coinciden en el límite: los efectos sobre la disponibilidad mental «cannot be judged by short-term sales changes». El detalle de los dos plazos, y por qué sin efecto corto tampoco aparece el largo, está en [efectos de corto y largo plazo](../Marca/efectos-de-corto-y-largo-plazo.md).

## Si crecer deja plata

Medir si el marketing causa ventas no alcanza: también hay que saber si esas ventas pagan lo que costaron. [Lean Analytics](metrica-que-importa.md) propone seguir una sola métrica principal según la etapa del negocio. En la etapa de ingresos, esa métrica sale de la [economía unitaria](economia-unitaria.md): el gasto máximo por venta, el CAC contra el LTV y el payback. El LTV es frágil en una marca chica, porque la lealtad sigue al tamaño de la marca, como dice el doble riesgo de [Cómo crecen las marcas](../Marca/como-crecen-las-marcas.md).

> [!NOTE]
> Sin fuente todavía: marketing mix modeling con pocos datos, y experimentos en marcas nuevas, tiendas chicas o Argentina.

## Las tres piezas

- [Incrementalidad](incrementalidad.md) — la parte de las ventas que no habría ocurrido sin el anuncio, y por qué los métodos sin grupo de control suelen inflarla. Leerla primero: las otras dos se apoyan en ella.
- [Una métrica que importa por etapa](metrica-que-importa.md) — una sola métrica principal por vez, según la etapa del negocio. Para elegir qué mirar ahora.
- [Economía unitaria](economia-unitaria.md) — si cada venta deja plata después de pagar su adquisición: CAC, LTV y payback. Antes de subir el gasto en adquisición.
