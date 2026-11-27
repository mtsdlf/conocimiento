---
resumen: >-
  El router decide qué modelo atiende cada consulta y el gateway es el punto único por el que la
  aplicación llama a los modelos, con el control de acceso, el costo y el fallback en un solo lugar.
estado: vigente
estabilidad: semi
fuentes:
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 10 «Step 3. Add Model Router and Gateway», p. 456; cap. 4 «Model Selection», p. 179"
  - https://arxiv.org/abs/2406.18665
  - https://docs.litellm.ai/docs/simple_proxy
  - https://www.latent.space/p/ainews-is-harness-engineering-real
aliases: [model router, router de modelos, model gateway, AI gateway, LLM gateway, gateway de modelos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Router y gateway de modelos

El router decide qué modelo atiende cada consulta y el gateway es el punto único por el que la
aplicación llama a los modelos, con el control de acceso, el costo y el fallback en un solo lugar.

Huyen los suma juntos, en el paso 3 de su arquitectura de referencia, pero hacen cosas distintas:
el router decide, el gateway controla. Se pueden tener por separado; el gateway sirve aunque haya
un solo modelo, y el router solo cuando hay más de uno (inferencia de esta base).

## El router: no mandar todo al modelo caro

Un router mira la consulta y elige a dónde va. Huyen lo describe con un clasificador de intención
y da la razón económica: "Instead of routing all queries to an expensive model, you can route
simpler queries to cheaper models."

El router mueve la característica que con un modelo pasa al frente, el
[costo y la latencia](../Caracteristicas/costo-y-latencia.md). RouteLLM (Ong et al., preprint de
2024) entrena routers con datos de preferencia y, según su resumen, reporta bajar el costo "more
than 2x in some cases" sin perder calidad. Es la afirmación de los autores, sin revisión por pares
ni datos de producción de terceros. Un router también se equivoca (lectura de esta base): si manda una consulta difícil al
modelo barato, la respuesta empeora sin que nadie lo note, y eso solo lo ve la
[evaluación](../Evaluacion-y-observabilidad/evaluacion.md) separada por ruta.

Elegir un modelo para cada ruta es el mismo problema que elegir el modelo de toda la aplicación, que
Huyen trata en el cap. 4 ("Model Selection", p. 179, con la decisión entre construir y comprar).

## El gateway: un solo lugar para llamar a los modelos

"A model gateway is access control and cost management", dice Huyen. Concentra en una pieza lo que
si no se repetiría en cada servicio que llama a un modelo (Huyen nombra el control de acceso, el
costo y el fallback; el resto sale de la documentación de LiteLLM y Cloudflare):

- una interfaz única para varios proveedores, que permite cambiar de modelo sin tocar la aplicación;
- claves y permisos por usuario, equipo o proyecto, con presupuestos y límites de gasto;
- reintentos y "fallback policies to overcome rate limits or API failures";
- el registro de cada llamada, que alimenta la [observabilidad](../Evaluacion-y-observabilidad/observabilidad-de-modelos.md);
- a veces, la [cache](cache-de-modelos.md) y filtros de [guardrails](../../IA/guardrails.md) como datos personales.

Un gateway de código abierto como el de la ficha de [Plataformas de IA](plataformas-de-ia.md)
reúne todo eso detrás de un endpoint compatible con la API de un proveedor, según su
documentación. Es el mismo patrón que un [API gateway](../Sistemas-distribuidos/api-gateway-y-bff.md),
con proveedores de modelos del otro lado. El fallback a otro modelo es una forma de
[degradación controlada](../Sistemas-distribuidos/degradacion-controlada.md), y cortar a tiempo un
proveedor que falla seguido es un [circuit breaker](../Sistemas-distribuidos/circuit-breaker.md):
esa lectura es de esta base, no de Huyen.

En una organización con varios equipos, el gateway suele ser una capacidad de la plataforma
interna, del tipo que describe [Platform Engineering](../../Platform-Engineering/platform-engineering.md);
es inferencia de esta base, sin una fuente que lo trate.

## Si los routers van a hacer falta

> [!IMPORTANT]
> No hay acuerdo sobre si el router tiene futuro. Latent Space (2026-03-04) recoge a Noam Brown
> (OpenAI), para quien los andamiajes alrededor del modelo "will also just be replaced by the
> reasoning models", y según esa lectura los routers de modelos deberían desaparecer. Del otro lado,
> los gateways del mercado ofrecen el ruteo automático como producto. Ningún
> estudio independiente arbitra; cada bando tiene interés comercial. Es una tensión abierta, parte
> de la disputa más amplia sobre modelo grande o harness grande que se cuenta en [Agente](agente.md).

La parte del gateway no entra en esa disputa: el control de acceso, el presupuesto y el fallback
hacen falta con cualquier modelo.

> [!NOTE]
> Sin fuente todavía: cuánto ahorra un router en producción, medido fuera de un paper o de un
> proveedor.

El recurso canónico es la sección "Router and gateway" del
[post de plataforma de Huyen](https://huyenchip.com/2024/07/25/genai-platform.html) (en el libro,
cap. 10, p. 456). Conviene fijarse en que separa las dos funciones. Para ver el mecanismo concreto,
la documentación de un gateway de código abierto, como la que enlaza la ficha, sirve de ejemplo
auditable.
