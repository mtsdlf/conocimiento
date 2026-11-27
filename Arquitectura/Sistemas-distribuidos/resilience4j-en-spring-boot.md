---
resumen: >-
  Cómo proteger un cliente HTTP de Spring Boot con `@CircuitBreaker` y `@Retry` de Resilience4j,
  con su fallback y su configuración en `application.yml`.
estado: borrador
estabilidad: semi
fuentes:
  - "Resilience4j, Getting Started (Spring Boot 3): https://resilience4j.readme.io/docs/getting-started-3"
  - "Resilience4j, CircuitBreaker: https://resilience4j.readme.io/docs/circuitbreaker"
  - "Resilience4j, Retry: https://resilience4j.readme.io/docs/retry"
  - "Archivo/Arquitectura/circuit-breaking-resilience4j.md (original)"
aliases: [Resilience4j, Circuit breaker en Spring Boot]
creado: 2026-10-03
revisado:
---

# Proteger un cliente HTTP con Resilience4j en Spring Boot

Cómo proteger un cliente HTTP de Spring Boot con `@CircuitBreaker` y `@Retry` de Resilience4j,
con su fallback y su configuración en `application.yml`.

## Qué hay que decidir y tener antes

- Entender los estados de un [Circuit breaker](circuit-breaker.md) y decidir la [Degradación controlada](degradacion-controlada.md) de la
  llamada: qué devuelve el fallback.
- Tener las dependencias `io.github.resilience4j:resilience4j-spring-boot3`,
  `spring-boot-starter-aop` y `spring-boot-starter-actuator`.

## Timeout, anotaciones, configuración y fallback

1. **Poné el timeout en el cliente HTTP**, no en una anotación. La documentación usa
   `@TimeLimiter` solo con métodos que devuelven `CompletableFuture` o un tipo reactivo (`Mono`),
   y no lo lista entre las anotaciones que aceptan métodos síncronos; en un método que termina en
   `.block()` no conviene. Configurá `responseTimeout` en el `HttpClient` del `WebClient`.
2. **Anotá el método del cliente** y poné el fallback en `@Retry`, no en `@CircuitBreaker`.
   Por defecto, Retry envuelve a CircuitBreaker: si el fallback estuviera en el breaker, el retry
   recibiría siempre un valor y nunca reintentaría. El fallback va en la misma clase, con los
   mismos parámetros más una excepción al final:

   ```java
   @CircuitBreaker(name = "precios")
   @Retry(name = "precios", fallbackMethod = "precioEstimado")
   public PrecioDto precioVigente(String productoId, String tenantId) {
       return webClient.get()
           .uri(u -> u.path("/precios/vigente").queryParam("productoId", productoId).build())
           .header("X-Tenant-Id", tenantId)
           .retrieve()
           .bodyToMono(PrecioDto.class)
           .block();
   }

   private PrecioDto precioEstimado(String productoId, String tenantId, WebClientRequestException ex) {
       return PrecioDto.estimado(productoId); // último precio guardado, marcado como estimado
   }
   ```

3. **Configurá la instancia** con el mismo `name`:

   ```yaml
   resilience4j:
     circuitbreaker:
       instances:
         precios:
           sliding-window-type: COUNT_BASED
           sliding-window-size: 20
           minimum-number-of-calls: 10
           failure-rate-threshold: 50
           slow-call-duration-threshold: 800ms
           wait-duration-in-open-state: 10s
           permitted-number-of-calls-in-half-open-state: 3
     retry:
       instances:
         precios:
           max-attempts: 2
           wait-duration: 100ms
           ignore-exceptions:
             - io.github.resilience4j.circuitbreaker.CallNotPermittedException
   ```

4. **Ajustá qué degrada el fallback.** Cada reintento pasa por el breaker y cuenta como una
   llamada. Con el breaker abierto, `ignore-exceptions` evita reintentar contra el rechazo
   inmediato (`CallNotPermittedException`). El fallback del ejemplo solo atiende errores de red
   (`WebClientRequestException`); sumá otro con `CallNotPermittedException` para el breaker
   abierto. Resilience4j elige el fallback cuyo tipo coincide mejor, y un 4xx sin fallback se
   propaga, porque es un error de quien llama.
5. **Reintentá solo lo idempotente.** Un `POST` de pago se reintenta solo si lleva una
   [Clave de idempotencia](clave-de-idempotencia.md).

| Parámetro del breaker | Qué controla | Default |
|---|---|---|
| `sliding-window-size` | llamadas (o segundos) de la ventana | 100 |
| `minimum-number-of-calls` | llamadas antes de calcular la tasa | 100 |
| `failure-rate-threshold` | % de fallas que abre el breaker | 50 |
| `slow-call-duration-threshold` | desde cuándo una llamada es lenta | 60 s |
| `wait-duration-in-open-state` | tiempo en abierto antes de probar | 60 s |
| `permitted-number-of-calls-in-half-open-state` | llamadas de prueba | 10 |

## Cómo se ve el breaker abierto

Con la dependencia apagada, las primeras llamadas fallan después del timeout y, pasado el umbral,
responden enseguida con el fallback. `GET /actuator/circuitbreakers` muestra la instancia
`precios` en estado `OPEN`, si el endpoint está expuesto en
`management.endpoints.web.exposure.include`.

## Ver también

- [Sintaxis de YAML](../../Desarrollo/Configuracion/sintaxis-de-yaml.md), en Desarrollo: la sintaxis del `application.yml`.
