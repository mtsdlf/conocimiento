---
resumen: >-
  Tratar datos por cuenta de otro es manejar los datos personales de una base ajena para el servicio que el dueño encargó: lo que hace quien opera la tienda de un comercio y ve los nombres, direcciones y pedidos de sus compradores. En Argentina lo regula el art. 25 de la Ley 25.326. Los datos se usan solo para lo que dice el contrato, no se ceden y se destruyen al terminar, y el contrato que lo ordena es obligatorio.
estado: borrador
estabilidad: semi
fuentes:
  - "Ley 25.326 de protección de datos personales, Infoleg (arts. 2, 9, 10, 12, 25 y 31, leídos el 2026-11-24): https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/norma.htm"
  - "Decreto 1558/2001, reglamentario, Infoleg (arts. 12 y 25, leídos el 2026-11-24): https://servicios.infoleg.gob.ar/infolegInternet/anexos/70000-74999/70368/norma.htm"
  - "Disposición DNPDP 60-E/2016, cláusulas tipo de transferencia internacional, argentina.gob.ar (leída): https://www.argentina.gob.ar/normativa/nacional/267922/texto"
  - "Resolución AAIP 47/2018, medidas de seguridad recomendadas (anexos leídos en parte): https://www.argentina.gob.ar/normativa/nacional/resolución-47-2018-312662/texto"
  - "Marval O'Farrell Mairal, Nueva resolución sobre medidas de seguridad y datos personales (según resumen): https://www.marval.com/Publicacion/nueva-resolucion-sobre-medidas-de-seguridad-y-datos-personales-13216"
  - "Resolución AAIP 126/2024, clasificación de infracciones y graduación de sanciones, argentina.gob.ar (leída el 2026-11-24): https://www.argentina.gob.ar/normativa/nacional/norma-399750/texto"
  - "IAPP, Últimas sanciones de la autoridad de protección de datos personales en Argentina (2022-01-11): https://iapp.org/news/a/ultimas-sanciones-de-la-autoridad-de-proteccion-de-datos-personales-en-argentina"
  - "Shopify, Data Processing Addendum (actualizado en julio de 2026): https://www.shopify.com/legal/dpa"
  - "Tiendanube, Términos de uso (modificados el 29-07-2026): https://www.tiendanube.com/terminos-de-uso"
  - "Emprender/.investigacion/datos-por-cuenta-de-otro.md"
  - "Emprender/.investigacion/contratos-y-datos-contraria.md"
  - "Emprender/.investigacion/contratos-y-datos-textos-oficiales.md"
aliases: [encargado del tratamiento, encargado de tratamiento, data processor, prestación de servicios informatizados de datos personales, artículo 25 Ley 25.326, contrato de encargo de tratamiento, DPA, data processing agreement]
creado: 2026-11-24
revisado:
---

# Tratamiento de datos por cuenta de otro

Tratar datos por cuenta de otro es manejar los datos personales de una base ajena para el servicio que el dueño encargó: lo que hace quien opera la tienda de un comercio y ve los nombres, direcciones y pedidos de sus compradores. En Argentina lo regula el art. 25 de la Ley 25.326. Los datos se usan solo para lo que dice el contrato, no se ceden y se destruyen al terminar, y el contrato que lo ordena es obligatorio.

> [!WARNING]
> Ley: esta nota no reemplaza a un abogado. El texto de la ley y del decreto sale de Infoleg, que es una sola fuente primaria. No se encontró doctrina argentina independiente sobre el art. 25 ni dictámenes de la autoridad sobre prestadores.

Responsable es quien es dueño de la base de datos; encargado, quien la maneja por cuenta del responsable. Lo que la ley pide a la tienda que junta los datos (consentimiento, derechos de acceso y rectificación, registro) está en la [normativa argentina de comercio electrónico](../../Comercio-electronico/Normativa/normativa-argentina.md#ley-25326-de-datos-personales). Esta nota trata el otro lado: el del prestador que entra a esa base para trabajar. El contrato donde va todo esto es el [contrato de servicio](contrato-de-servicio.md), y cómo se entra a las cuentas, el [acceso a las cuentas del cliente](acceso-a-las-cuentas-del-cliente.md).

## Quién es quién

En una tienda online hay tres papeles, y la ley nombra dos. El art. 2 llama **responsable** al titular de la base: el comercio, que es el titular de la base de sus compradores. El art. 25 habla de quien presta «por cuenta de terceros» servicios de tratamiento, y el decreto reglamentario lo llama **encargado del tratamiento**. En el esquema de la base, el prestador que arma, muda o cuida la tienda es encargado del comercio; ninguna fuente leída trata al socio de una plataforma con esas palabras.

La plataforma es el tercer papel. Shopify lo dice en su acuerdo de tratamiento de datos: el comercio actúa como responsable («You shall act as a Data Controller») y Shopify como encargado de los servicios centrales. Los términos de uso de Tiendanube no usan esas palabras y dicen que «Cada tienda es gestionada por su respectivo titular». Ninguna de las dos prevé en esos textos al socio que entra a la tienda. Que el prestador sea un segundo encargado del comercio, al lado de la plataforma, es inferencia de la base: ni la ley ni el decreto usan la palabra subencargado.

## Lo que el art. 25 no deja hacer

El art. 25, inciso 1, dice: «Cuando por cuenta de terceros se presten servicios de tratamiento de datos personales, éstos no podrán aplicarse o utilizarse con un fin distinto al que figure en el contrato de servicios, ni cederlos a otras personas, ni aun para su conservación». Aplicado a una tienda, eso deja afuera tres usos (inferencia de la base sobre el texto):

- usar la lista de compradores de un comercio para otro cliente o para promocionar al prestador;
- pasarle a un tercero la exportación de pedidos, salvo que el contrato lo prevea;
- guardar «por las dudas» una copia en una cuenta propia que el contrato no contempla.

## Qué tiene que decir el contrato

El decreto 1558/2001 vuelve obligatorio el contrato. Su art. 25 dice que el tratamiento por encargo «deberá estar regulada por un contrato que vincule al encargado del tratamiento con el responsable». Ese contrato tiene que disponer, en particular, dos cosas:

1. «que el encargado del tratamiento sólo actúa siguiendo instrucciones del responsable del tratamiento»;
2. «que las obligaciones del artículo 9º de la Ley Nº 25.326 incumben también al encargado del tratamiento».

El mismo artículo pide que el contrato contenga los niveles de seguridad de la ley y la confidencialidad que deben mantener los «locatarios» (así en el texto oficial). El deber de seguridad del art. 9 es adoptar «las medidas técnicas y organizativas que resulten necesarias para garantizar la seguridad y confidencialidad de los datos personales». El deber de confidencialidad del art. 10 alcanza a «las personas que intervengan en cualquier fase del tratamiento» y sigue después de terminada la relación.

Si el contrato no existe, el que incumple el decreto es el comercio, y el prestador queda sin reglas escritas sobre lo que puede hacer (lectura de la base y del informe contrario). El decreto no fija un formato, así que alcanzaría con una cláusula o un anexo del [contrato de servicio](contrato-de-servicio.md) (inferencia de la base).

## Qué medidas de seguridad

La ley no fija las medidas concretas, y las que publicó la autoridad son recomendaciones. La Resolución AAIP 47/2018 derogó las disposiciones de 2006 y 2008, que eran obligatorias y se organizaban por niveles, y aprobó medidas «recomendadas» (según Marval y la resolución, que coinciden). Su anexo para datos informatizados cubre la recolección, el control de acceso, los cambios, las copias de seguridad, las vulnerabilidades, la destrucción de datos, los incidentes y los entornos de desarrollo. Los anexos están en parte publicados como imagen y no se leyeron enteros.

Para quien cuida tiendas, la parte que más pesa es, a criterio de la base, el control de acceso. Se ordena con lo que cuenta [acceso a las cuentas del cliente](acceso-a-las-cuentas-del-cliente.md): usuario propio, permisos justos y baja al terminar.

## Qué pasa con los datos al terminar

Los datos se destruyen cuando termina el trabajo. El art. 25, inciso 2, dice: «Una vez cumplida la prestación contractual los datos personales tratados deberán ser destruidos». La excepción exige dos condiciones: «autorización expresa» del comercio y que «razonablemente se presuma la posibilidad de ulteriores encargos». En ese caso se pueden guardar «con las debidas condiciones de seguridad por un período de hasta dos años». Para quien muda una tienda, la exportación de clientes y pedidos que queda en una computadora después de la mudanza es exactamente lo que la ley manda destruir (inferencia de la base).

## Datos que viajan fuera del país

Shopify dice en su acuerdo de tratamiento que puede procesar los datos en cualquier país donde operen ella o sus proveedores; de Tiendanube no se encontró nada. Que eso cuente como transferencia internacional es inferencia de la base. El art. 12 prohíbe transferir datos a países «que no propocionen niveles de protección adecuados» (así en el texto oficial). La Disposición 60-E/2016 lista los países considerados adecuados: la Unión Europea y el Espacio Económico Europeo, Suiza, Guernsey, Jersey, Isla de Man, Islas Feroe, Canadá (solo el sector privado), Andorra, Nueva Zelanda, Uruguay e Israel (solo datos con tratamiento automatizado). Estados Unidos no está en la lista.

La misma disposición aprueba cláusulas contractuales tipo. Su Anexo II es el modelo para el caso en que el encargado está fuera del país. El responsable que transfiere a un país sin legislación adecuada con un contrato distinto de los modelos tiene que pedir aprobación a la autoridad «dentro de los TREINTA (30) días corridos de su firma». El decreto agrega otra salida: la prohibición no rige si el titular de los datos consintió expresamente la cesión. Cómo encaja esto con plataformas que procesan datos en Estados Unidos con sus propios acuerdos no lo resolvió ninguna fuente leída. Es un tema del comercio y la plataforma más que del prestador, salvo que el prestador copie datos a un servicio propio en el exterior.

## Quién controla y qué arriesga

La autoridad es la Agencia de Acceso a la Información Pública (AAIP) desde 2017. Las fuentes que lo dicen son una copia del decreto y un estudio jurídico, leídos por resumen. El art. 31 de la ley prevé apercibimiento, suspensión, multa, clausura o cancelación del archivo, sin perjuicio de la responsabilidad por daños.

Las multas son bajas. La Resolución AAIP 126/2024, vigente desde el 1 de junio de 2024, derogó las anteriores y fijó la escala:

| Infracción | Multa |
|---|---|
| Leve | De $ 1.000 a $ 80.000 |
| Grave | De $ 80.001 a $ 90.000 |
| Muy grave | De $ 90.001 a $ 100.000 |

«Incumplir el deber de confidencialidad y seguridad sobre los datos de carácter personal» figura entre las graves. Entre los criterios de gradación, la resolución dice que ante incidentes de seguridad «se considerará como atenuante la colaboración con la Autoridad de Aplicación» y las medidas preventivas y correctivas del «responsable o encargado de tratamiento». Una nota de IAPP de 2022 contó seis organizaciones multadas a fines de 2021 y dijo que en más de 20 años «no se ha registrado un elevado número de sanciones». No se encontró un conteo oficial más reciente.

> [!IMPORTANT]
> A juicio de la base, la multa no es el motivo principal para cumplir. Con montos así, presentarla como un riesgo alto exagera lo que muestran las fuentes, aunque la autoridad no está quieta: según un resumen, abrió una investigación de oficio el 19-12-2025 por una filtración masiva. Lo que sí pesa es la responsabilidad por daños que el art. 31 deja a salvo. Cuánto responde el encargado frente al comprador, y no solo frente al comercio, lo afirma un estudio jurídico citado por resumen (que responde si incumple el contrato o el art. 25), sin fallo ni criterio oficial que lo confirme.

## Lo que viene y lo que no está claro

La Ley 25.326 sigue vigente. Hay proyectos para reemplazarla, entre ellos el expediente 3397-D-2026, presentado en julio de 2026, según fuentes secundarias; su estado en comisión no se verificó. Los borradores hablan de avisar a la autoridad de un incidente dentro de 72 horas. Hoy la ley no obliga a notificar incidentes, según fuentes secundarias. Si la Resolución 47/2018 o la 332/2020 lo recomiendan está en discusión entre las fuentes y no se leyó en el texto.

## Lo que no se encontró

- Si el prestador tiene que inscribir algo en el registro de bases de datos del art. 21. Por el texto, la inscripción es del titular de la base, pero no se encontró una guía de la AAIP para encargados.
- Doctrina, dictámenes o fallos sobre el art. 25 y sobre la responsabilidad del encargado frente al titular de los datos.
- Los términos de socios y la política de privacidad de Tiendanube, y un texto de Shopify que trate al socio frente a los datos de los compradores.
- El texto completo de los anexos de la Resolución 47/2018.

El recurso canónico es el art. 25 de la ley junto con el art. 25 del decreto 1558/2001, en Infoleg: son dos párrafos cada uno y dicen casi todo. Fijate en que el fin queda atado al contrato, en que no se cede «ni aun para su conservación» y en que guardar los datos después exige autorización expresa.
