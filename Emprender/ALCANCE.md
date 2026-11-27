---
tema: Emprender
para: fundar el área de conocimiento de emprendimiento, que la lean Matias, Fer y los agentes; a futuro la usan los repos de negocio de cada empresa de la organización, que enlazan las notas de acá
nivel: intermedio; conoce el vocabulario general de negocio y leyó o va a leer El método Lean Startup (Ries, 2011)
escuela: Lean Startup y Customer Development como columna; effectuation y el enfoque científico como contraste, con su evidencia
fuera:
  - lo de una empresa concreta: su modelo, sus precios, sus clientes (va a su repo de negocio)
  - quién compra y por qué, posicionamiento, canales y medición de marketing (tema Marketing, se enlaza)
  - análisis de cohortes, retención y churn como técnica (tema Datos, se enlaza)
  - innovación dentro de empresas grandes (intraemprendimiento), salvo como mención
  - lo recurrente de la empresa en marcha (decisión de #98): caja y resultado (Contabilidad/Registro/devengado.md, Tesoreria/Caja-y-liquidez/proyeccion-de-caja.md), punto de equilibrio (Contabilidad/Contabilidad-de-gestion/punto-de-equilibrio.md), monotributo en marcha (Impuestos/Obligacion-tributaria/monotributo-en-marcha.md), Ingresos Brutos (Impuestos/Impuestos-al-consumo/ingresos-brutos.md), factura electrónica (Comercio-electronico/Normativa/factura-electronica-de-arca.md) y la primera contratación (Administracion-de-personal-y-nomina/Legajo/ingreso-y-egreso.md); se enlaza
fuentes:
  - "Eric Ries, The Lean Startup (2011); en castellano, El método Lean Startup (Deusto)"
preguntas:
  - "¿Cómo se comprueba que una idea resuelve un problema real antes de construirla, y qué cuenta como evidencia?"
  - "¿Qué producto mínimo viable conviene para probar una hipótesis concreta, y cuál es el más barato que sirve?"
  - "¿Cuándo se pivota y cuándo se persevera, y con qué métricas se decide?"
  - "¿Qué formas de pensar el emprender hay (Lean Startup, plan de negocios, effectuation, enfoque científico) y qué evidencia tiene cada una?"
  - "¿Cuáles son las partes de emprender y en qué orden importan para una empresa que recién empieza?"
  - "Tengo cinco zonas de mercado posibles y quiero elegir dos o tres para probar: ¿con qué criterios y con qué cuidado las comparo?"
  - "¿De dónde salen las oportunidades de negocio y qué fuentes son más confiables?"
  - "¿Cuánto pesa que quienes fundan conozcan el mercado, y qué dice la evidencia?"
  - "¿Qué cambia si en lugar de buscar la mejor oportunidad se empieza con lo que se tiene y lo que se puede perder?"
  - "¿Qué diferencia hay entre vender software solo, software con servicio o una plataforma de dos lados, en cómo cobra, cómo crece y qué márgenes deja?"
  - "Voy a armar y cuidar por mes la tienda online de un comercio sobre Shopify o Tiendanube: ¿qué contrato es, qué tiene que decir y qué pasa si el cliente quiere cortar el abono antes de tiempo?"
  - "Si la plataforma se cae o una actualización mía rompe la tienda, ¿de qué respondo, y vale una cláusula que limite eso al valor del abono?"
  - "¿Cómo entro a la tienda, el dominio y los pagos del comercio sin quedarme con sus contraseñas, y qué hago cuando termina la relación?"
  - "Al operar la tienda veo y exporto los datos de los compradores: ¿qué me deja hacer la ley con ellos y qué tiene que firmar el comercio conmigo?"
  - "Voy a empezar a facturar servicios a mi nombre en la Argentina: ¿qué trámites hago en ARCA, en qué orden, y cómo elijo entre el monotributo y el régimen general?"
  - "Si no entro en el monotributo, ¿cuánto aporto por mes como autónomo, en qué categoría y qué cubre?"
  - "Tengo un empleo en relación de dependencia y quiero facturar aparte: ¿aporto dos veces?"
aprobado: 2026-11-22
ampliado: 2026-11-27
---

# Alcance: Emprender

El tema funda el área de conocimiento de emprendimiento de la organización: primero la estructura que va a alojar todo lo que se aprenda sobre emprender, y adentro lo que cubre El método Lean Startup, a fondo. El pedido sale de la conversación del 2026-11-21; el uso futuro, de los repos `tsc-negocio` y `lind-negocio`, que hoy no lo consumen. La estructura anterior (las ocho partes heredadas de `mtsdlf/fundar`) se descartó por pedido de la persona: el árbol se armó de nuevo desde cómo se divide el campo (Ries, Blank, Aulet, Osterwalder).

## Árbol

```
Emprender/
  emprender.md                 el todo: las seis partes y cómo se encadenan
  Validacion/                  ¿hay un problema real y alguien que pague? (a fondo)
    hipotesis-de-salto-de-fe     los supuestos de valor y de crecimiento que se prueban primero
    descubrimiento-de-clientes   salir a hablar con clientes sin sesgar las respuestas
    producto-minimo-viable       qué es un MVP, sus tipos y cómo se elige uno
    construir-medir-aprender     el ciclo de Ries y los lotes pequeños
    contabilidad-de-la-innovacion  medir el avance con métricas accionables y no de vanidad
    pivotar-o-perseverar         la decisión y los tipos de pivote
    tamano-de-mercado            TAM, SAM y SOM, y cómo se estiman
    Oportunidades/               (nuevo) de dónde salen y cómo se elige cuál validar
      oportunidades                (nuevo) entrada: qué es una oportunidad y el recorrido de encontrar a elegir
      fuentes-de-oportunidades     (nuevo) problemas, cambios y huecos; Drucker, Shane y Venkataraman; descubrir o crear
      criterios-de-oportunidad     (nuevo) qué se mira para comparar: Mullins, Aulet, Timmons, Gans, Scott y Stern
      matriz-de-oportunidades      (nuevo) cómo se arma la comparación: filtro, puntajes, pesos y sesgos, con su evidencia
      encaje-fundador-mercado      (nuevo) founder-market fit: qué saben y a quién conocen quienes fundan
      effectuation                 (nuevo) Sarasvathy: empezar con los medios y la pérdida asumible, como contraste
  Modelo-de-negocio/           cómo se crea, entrega y cobra valor
    modelos-de-negocio-de-software  (nuevo) software solo, con servicio o plataforma, comparados
    saas                            (nuevo) software solo: cómo cobra, crece y qué márgenes deja
    servicios-habilitados-por-tecnologia  (nuevo) software con servicio, «done for you»
    marketplace                     (nuevo) la plataforma de dos lados como negocio: comisión, liquidez y fuga
    margenes-por-modelo-de-negocio  (nuevo) ficha: márgenes, comisiones y múltiplos de empresas públicas, 2025
  Crecimiento/                 de los primeros clientes a crecer de forma repetible
    encaje-producto-mercado      la frontera entre validar y crecer
    motores-de-crecimiento       pegajoso, viral y pagado (Ries)
  Finanzas/                    números de la empresa que empieza y de dónde sale la plata (entrada)
  Fundadores-y-equipo/         propiedad, decisiones y primeras personas (entrada)
  Legal-e-impuestos/           formas legales y régimen impositivo en Argentina (entrada)
    contrato-de-servicio         (nuevo) obra para armar, servicio continuado para cuidar; plazo, preaviso, baja y qué escribir
    responsabilidad-del-prestador  (nuevo) actividad o resultado, caída de la plataforma, límites a la cláusula y comercio consumidor
    acceso-a-las-cuentas-del-cliente  (nuevo) cuentas del comercio, usuario propio y permisos justos, autorización escrita, salida
    accesos-delegados-por-plataforma  (nuevo) ficha: cómo da acceso cada plataforma y cómo se quita, al 2026-11-24
    tratamiento-de-datos-por-cuenta-de-otro  (nuevo) art. 25 de la Ley 25.326: el prestador como encargado
    encuadre-fiscal-y-previsional  (nuevo) qué decide quien arranca por su cuenta: inscribirse, régimen simplificado o general, cómo aporta, la provincia
    autonomos-y-sipa-en-argentina  (nuevo) Ley 24.241: quién aporta, 27 % más 5 %, las cinco categorías, mayo, montos de noviembre de 2026
    inscripcion-en-arca-al-arrancar  (nuevo) clave fiscal, CUIT digital, domicilios y actividad, monotributo o régimen general, punto de venta, al 2026-11-27
  Fundamentos/                 qué es una startup, escuelas y evidencia, mitos, bibliografía, fuentes, glosario
```

## Supuestos

- Profundidad de esta primera pasada: el árbol completo con la entrada de cada parte; Validación y Fundamentos a fondo, más los dos componentes de Crecimiento que vienen de Ries. Las otras partes se llenan cuando se vuelque algo leído o vivido.
- Mercado y cliente no es una parte propia: el tamaño de mercado va a Validación y quién compra y por qué se enlaza al tema Marketing.
- Lo legal e impositivo es de Argentina y vive en la capa operativa, con fecha: cambia seguido.
- Emprender se queda con las decisiones de una vez y la pista; lo recurrente de la empresa en marcha es de los temas de dominio (decisión de #98). Varios componentes que Finanzas y Legal e impuestos tenían pendientes ya están escritos allá, y en la sesión 16 del mapa (#123) se enlazaron desde las entradas: caja y resultado en [devengado](../Contabilidad/Registro/devengado.md) y [proyección de caja](../Tesoreria/Caja-y-liquidez/proyeccion-de-caja.md), el [punto de equilibrio](../Contabilidad/Contabilidad-de-gestion/punto-de-equilibrio.md), el [monotributo en marcha](../Impuestos/Obligacion-tributaria/monotributo-en-marcha.md), [Ingresos Brutos](../Impuestos/Impuestos-al-consumo/ingresos-brutos.md), la [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md) y la primera contratación en [ingreso y egreso](../Administracion-de-personal-y-nomina/Legajo/ingreso-y-egreso.md#hacerse-empleador-la-primera-contratación).

## Ampliación del 2026-11-22: Oportunidades y tipos de modelo

Pedida en el mapa «qué oportunidad de negocio explorar primero» de un repo de negocio de la organización: hacía falta saber cómo se comparan oportunidades y qué modelos de negocio de software hay antes de elegir criterios y pesos. La persona aprobó el alcance (las dos ampliaciones); el árbol detallado lo decidió quien escribe:

- **Oportunidades va dentro de Validación**, como subcarpeta, porque elegir qué oportunidad validar es el paso anterior a la hipótesis de salto de fe y sus componentes se estudian por separado. No es una vertical nueva: el tema sigue teniendo seis partes.
- **Effectuation tiene nota propia en Oportunidades** porque su aporte central acá es cómo se elige qué hacer (medios y pérdida asumible). La comparación de escuelas sigue en [Escuelas de emprender](Fundamentos/escuelas-de-emprender.md), que la enlaza.
- **La evaluación se partió en dos notas**: criterios (qué se mira) y matriz (cómo se combinan), porque la matriz se enlaza sola desde quien tiene que fijar criterios y pesos.
- **Las cifras de empresas van a una ficha** (`volatil`), y las notas de los modelos dan rangos y la enlazan.
- **Los tipos de modelo de software van en Modelo de negocio** como componentes. La estrategia de plataformas (precio a cada lado, efecto de red, arranque) sigue en Producto/Plataformas y se enlaza; acá queda solo la mirada de negocio: cómo cobra, cómo crece y qué economía tiene.

## Ampliación del 2026-11-24: los contratos de un servicio

Pedida en el issue #55, parte del plan #48 (lo que la base tiene que saber para una empresa chica que arma, muda y cuida tiendas online de comercios pyme sobre plataformas de otros, con un abono). El issue fijó el lugar (Legal e impuestos) y el contenido; el árbol detallado lo decidió quien escribe:

- **Cuatro componentes y una ficha.** El contrato, la responsabilidad, el acceso y los datos se enlazan por separado desde otras notas (el abono, los socios de una plataforma, la normativa del comercio electrónico), así que cada uno tiene nota propia. Los pasos de cada plataforma para dar acceso cambian seguido y van a una ficha `volatil`.
- **Legal e impuestos deja de ser solo «para empezar».** La entrada suma una sección con los contratos de un servicio; la Ley 25.326 vista desde la tienda que junta datos sigue en Comercio electrónico y se enlaza.
- **El texto de las normas se bajó de Infoleg** y quedó entero en `.investigacion/contratos-y-datos-textos-oficiales.md`, porque los lectores web de los subagentes solo devolvían fragmentos.

## Ampliación del 2026-11-27: encuadre fiscal y previsional, autónomos e inscripción en ARCA

Pedida en el issue #175, pendiente que dejó la sesión de mantenimiento #123: el régimen de autónomos y el SIPA, y la inscripción en ARCA al arrancar. El árbol detallado lo decidió quien escribe, en una sesión sin la persona; queda para revisar en el PR:

- **Una nota general y dos de la Argentina.** Lo que vale en cualquier país (qué decide quien arranca sobre su encuadre fiscal y previsional) va en `encuadre-fiscal-y-previsional`; lo argentino, en dos notas aparte, porque se enlazan por separado: el aporte de autónomos desde quien ya está en el régimen general y la inscripción desde quien recién empieza.
- **Lo recurrente se queda en Impuestos.** La recategorización y la exclusión del monotributo siguen en `Impuestos/Obligacion-tributaria/monotributo-en-marcha`, el IVA y Ganancias en sus notas; acá solo la decisión de una vez y el alta, como dice el alcance de Impuestos.
- **Las cuotas de autónomos se copian con fecha** en `autonomos-y-sipa-en-argentina`, que es `volatil`: cambian todos los meses con la movilidad, y es el único lugar de la base donde están.
- **Ganancias de personas humanas y la factura A con leyenda quedan fuera**: los escribe en paralelo el issue #172 en Impuestos, y estas notas enlazan las notas de Impuestos que ya existen.
