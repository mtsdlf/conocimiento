---
tipo: concepto
resumen: >-
  En Spring Boot, lo que cambia entre entornos o es secreto se inyecta desde afuera (variables de
  entorno, argumentos), y `application.properties` solo guarda valores por defecto no sensibles.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Spring Boot Reference, Externalized Configuration: https://docs.spring.io/spring-boot/reference/features/external-config.html"
  - "Spring Framework Reference, Using @Value: https://docs.spring.io/spring-framework/reference/core/beans/annotation-config/value-annotations.html"
  - "Adam Wiggins, The Twelve-Factor App, III. Config: https://12factor.net/config"
aliases: [Externalized configuration, Configuración externa, Variables de entorno en Spring Boot, application.properties]
parte_de: []
requiere: []
relacionado: [yaml]
---

# Configuración externalizada en Spring Boot

En Spring Boot, lo que cambia entre entornos o es secreto se inyecta desde afuera (variables de
entorno, argumentos), y `application.properties` solo guarda valores por defecto no sensibles.

## Por qué importa

Un secreto en un archivo versionado queda en el historial de Git para siempre, aunque después se
borre. Y un artefacto que trae la URL de producción adentro necesita un build distinto por
entorno. The Twelve-Factor App lo resume así: la configuración vive en el entorno, separada del
código, para que el mismo artefacto corra en todos lados.

## Cómo funciona

Spring Boot junta propiedades de muchas fuentes, y cuando una clave aparece en varias gana la de
mayor precedencia. La documentación lista quince fuentes, incluidas las de los tests y las de
DevTools; para una app común alcanza esta simplificación, de mayor a menor:

1. argumentos de línea de comando (`--server.port=9000`);
2. variables de entorno del sistema operativo;
3. archivos de perfil, `application-{perfil}.properties` o `.yml`, que pisan al archivo base de
   su misma ubicación;
4. `application.properties` o `application.yml` (uno externo, junto al jar, pisa al empaquetado);
5. el valor por defecto en el código: `@Value("${miapp.pagina:25}")`.

Una variable de entorno se mapea a una propiedad por **relaxed binding**: se pasa a mayúsculas,
los puntos se reemplazan por `_` y los guiones se eliminan. `miapp.api-key` se lee de
`MIAPP_APIKEY`, y `spring.datasource.url` de `SPRING_DATASOURCE_URL`. La variable no necesita que
la clave esté declarada en ningún archivo.

Los **perfiles** se activan con `SPRING_PROFILES_ACTIVE=dev` y cargan su archivo encima del base.
Sirven para diferencias de comportamiento (un mock, un flag), no para secretos: un archivo de
perfil también se versiona.

| Va en `application.properties` | Se inyecta desde el entorno |
|---|---|
| tamaño de página, nombre de la app, timeouts por defecto | contraseñas, API keys, tokens |
| flags de comportamiento iguales en todos lados | URLs de bases y servicios externos |

Para un dato crítico conviene que la app falle al arrancar si falta: `@Value("${miapp.api-key}")`,
sin default, hace fallar el arranque, en lugar de un default que esconda el error.

## Ejemplo

`application.properties` trae `spring.datasource.url=` vacío. En local, un `.env` define
`SPRING_DATASOURCE_URL=jdbc:postgresql://db:5432/miapp`; en el clúster, el pod recibe la misma
variable desde un Secret. El jar es el mismo.

## No confundir con

Un servidor de configuración (Spring Cloud Config, Consul). Es otra fuente de propiedades, que
centraliza la configuración de muchos servicios; el principio de separar configuración y código
es el mismo.

## Relaciones

- Relacionado: [YAML](yaml.md) — `application.yml` es la alternativa en YAML a `application.properties`.
- Base de: [Levantar un entorno local con Docker Compose](levantar-un-entorno-local-con-docker-compose.md) — cómo se inyectan las variables en local.
- Ver también: [Gestión de secretos](../DevOps/gestion-de-secretos.md) (DevOps) — dónde viven los secretos fuera del código.
