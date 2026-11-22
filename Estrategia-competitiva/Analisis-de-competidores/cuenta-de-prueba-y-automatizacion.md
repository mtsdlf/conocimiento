---
resumen: >-
  Casi todo lo que hace falta saber de un rival se ve sin cuenta y sin automatizar nada; una cuenta de prueba propia hace falta solo para ver el lado de adentro del producto, y un navegador automatizado sirve para recorrer y fechar lo público sin cansarse.
estado: borrador
estabilidad: semi
fuentes:
  - "Estrategia-competitiva/Analisis-de-competidores/etica-y-legalidad.md (reglas para recolectar)"
  - "Estrategia-competitiva/Analisis-de-competidores/ley-argentina-y-competidores.md (Ley 26.388 y Ley 25.326)"
  - "Conversación del 2026-11-22 sobre si el análisis necesita cuentas de la competencia (criterio de esta base)"
aliases: [cuenta de prueba, cuenta trial, prueba gratis del rival, Playwright, navegador automatizado, automatizar la recolección, capturas del checkout]
creado: 2026-11-22
revisado:
---

# Cuenta de prueba y automatización

Casi todo lo que hace falta saber de un rival se ve sin cuenta y sin automatizar nada; una cuenta de prueba propia hace falta solo para ver el lado de adentro del producto, y un navegador automatizado sirve para recorrer y fechar lo público sin cansarse.

Es la parte práctica de la recolección: dónde se mira cada cosa de las [fuentes públicas](fuentes-publicas.md) y con qué herramienta. Lo que se hace con una cuenta de prueba es sobre todo el [desarme de producto](desarme-de-producto.md). Esta nota es criterio de esta base, armado a partir de las reglas de [ética y legalidad](etica-y-legalidad.md#reglas-para-recolectar-sin-problemas); no cita una fuente externa propia y no reemplaza asesoramiento legal.

## Lo que se ve sin cuenta

| Qué | Dónde | Paso de la [guía](../Fundamentos/recorrido-analisis-de-competencia.md) |
|---|---|---|
| Planes, precios y comisiones | La página de precios de cada plataforma | 5 |
| Qué deja hacer a terceros | La documentación para desarrolladores y la tienda de apps | 1, 5 |
| Lo que dicen sus clientes | Reseñas en la tienda de apps y en sitios de reseñas | 3 |
| Sus números | Reportes a inversores, si cotiza; prensa y registros públicos, si no | 5 |
| Cómo compra un consumidor | Una tienda real hecha con esa plataforma, recorrida hasta antes de pagar | 5 |
| Qué anuncia | Las bibliotecas públicas de anuncios | 5, 9 |
| Hacia dónde va | Ofertas de empleo, registro de cambios, blog | 9 |

Con eso se cubren casi enteros los pasos de dominio, rivales, análisis y seguimiento. El checkout de una plataforma de tiendas, por ejemplo, se ve en cualquier tienda que la use; lo que fija la plataforma y lo que configura el comercio está en [checkout por plataforma](../../Comercio-electronico/Checkout-y-conversion/checkout-por-plataforma.md).

## Cuándo hace falta una cuenta de prueba

Hace falta para ver el producto desde el lado de quien lo usa para trabajar: en una plataforma de tiendas, el panel del comerciante. Ahí se ve cuánto cuesta dar de alta productos, configurar envíos y medios de pago, qué parte del checkout se puede cambiar y qué viene incluido en cada plan. Es el material del [desarme de producto](desarme-de-producto.md#cómo-se-desarma-un-producto-de-software), con las mismas tareas en cada rival.

Tres reglas, de [ética y legalidad](etica-y-legalidad.md#reglas-para-recolectar-sin-problemas):

1. **La cuenta es propia y con identidad real.** La abre una persona con su nombre. Nada de cuentas a nombre de un comercio inventado ni de hacerse pasar por un cliente que no se es ([comprar como cliente o hacerse pasar por otro](etica-y-legalidad.md#comprar-como-cliente-o-hacerse-pasar-por-otro)).
2. **Nunca credenciales ajenas.** Ni la cuenta de un cliente, ni la de un ex empleado del rival, ni una prestada.
3. **No se saltea ningún límite técnico.** Un login, un tope de uso o un bloqueo se respetan. Entrar sin permiso a un sistema de acceso restringido es lo que castiga la Ley 26.388 ([ley argentina y competidores](ley-argentina-y-competidores.md#lo-que-dice-cada-norma)).

Si el rival no ofrece prueba gratis, se paga el plan más barato o el desarme se hace con lo público y con tiendas reales.

## Automatizar con un navegador

Un navegador automatizado (Playwright es el más usado al 2026-11-22) sirve para tres cosas: recorrer las mismas páginas en todos los rivales, sacar capturas fechadas que después se comparan y repetir el recorrido en el seguimiento para ver qué cambió. Rinde más en lo público: precios, documentación, tiendas de apps, el checkout de tiendas reales.

Sirve también dentro de la cuenta de prueba propia: es usar la propia cuenta, no entrar a una ajena. Lo que no se hace con automatización es lo mismo que no se hace a mano: entrar con credenciales ajenas o pasar un bloqueo.

Cuidados al automatizar:

- **Ritmo bajo.** Pocas páginas, espaciadas: el objetivo es leer, no cargar el sitio del rival.
- **Cada captura con fuente y fecha**, como cualquier dato de las [fuentes públicas](fuentes-publicas.md#quién-lo-dice-y-si-está-confirmado).
- **Datos agregados, no personas.** Si una página muestra nombres de clientes o de empleados, no se guardan en fichas; la Ley 25.326 rige los datos personales ([ley argentina y competidores](ley-argentina-y-competidores.md#lo-que-dice-cada-norma)).
