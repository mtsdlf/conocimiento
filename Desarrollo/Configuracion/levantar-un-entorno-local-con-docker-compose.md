---
resumen: >-
  Cómo levantar una app de Spring Boot con sus dependencias en local, con Docker Compose y un
  `.env` propio que nunca se versiona.
estado: borrador
estabilidad: semi
revisado:
creado: 2026-10-03
fuentes:
  - "Docker Docs, Set environment variables within your container's environment: https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables/"
  - "Docker Docs, Set, use, and manage variables in a Compose file with interpolation: https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/"
  - "Spring Boot Reference, Externalized Configuration: https://docs.spring.io/spring-boot/reference/features/external-config.html"
aliases: [Entorno local con Docker Compose, docker compose up, .env.example]
---

# Levantar un entorno local con Docker Compose

Cómo levantar una app de Spring Boot con sus dependencias en local, con Docker Compose y un
`.env` propio que nunca se versiona.

## Lo que tiene que traer el repo

- Entender qué se inyecta desde el entorno y cómo se nombran las variables:
  [Configuración externalizada en Spring Boot](configuracion-externalizada-spring-boot.md).
- Tener Docker con el plugin `docker compose` instalado.
- El repo tiene que traer un `Dockerfile` de la app, un `docker-compose.yml` con la app y sus
  dependencias, y un `.env.example` con todas las variables requeridas, sin valores reales.

El compose y el `.env.example` que provee el equipo son un camino estándar chico para arrancar, un
[golden path](../../Platform-Engineering/Plataforma-interna/golden-path.md).

## Del `.env.example` a `docker compose up`

1. **Copiá el ejemplo**: `cp .env.example .env`. Confirmá que `.env` está en `.gitignore`.
2. **Completá `.env` con valores de desarrollo**: credenciales de la base local, claves de prueba
   de los proveedores, URLs de mocks. Nunca pongas una credencial de un entorno real.

   ```text
   SPRING_PROFILES_ACTIVE=dev
   SPRING_DATASOURCE_URL=jdbc:postgresql://db:5432/miapp
   SPRING_DATASOURCE_USERNAME=dev
   SPRING_DATASOURCE_PASSWORD=dev
   EXTERNAL_API_KEY=
   ```

3. **Revisá que el servicio de la app lea ese archivo** con `env_file`. Compose también usa el
   `.env` del directorio del proyecto para interpolar `${VARIABLE}` dentro del propio
   `docker-compose.yml`, pero eso no pasa las variables al contenedor:

   ```yaml
   services:
     app:
       build: .
       env_file: [.env]
       ports: ["8080:8080"]
       depends_on: [db]
     db:
       image: postgres:16
       environment:
         POSTGRES_DB: miapp
         POSTGRES_USER: ${SPRING_DATASOURCE_USERNAME}
         POSTGRES_PASSWORD: ${SPRING_DATASOURCE_PASSWORD}
   ```

4. **Levantá todo**: `docker compose up --build`. La app se conecta a `db` por el nombre del
   servicio, no por `localhost`. `depends_on` solo ordena el arranque; si la app falla porque la
   base todavía no acepta conexiones, agregá un `healthcheck` a `db` y
   `condition: service_healthy`.
5. **Si agregás una variable nueva**, sumala a `.env.example` sin valor y documentá para qué es,
   para que el resto la conozca.

## Los servicios corriendo y el `.env` fuera de git

`docker compose ps` muestra los dos servicios en estado `running`, y
`docker compose exec app env | grep SPRING_` lista las variables del `.env`. Si la app arrancó con
el perfil correcto, el log muestra `The following 1 profile is active: "dev"`. `git status` no
muestra el `.env`.
