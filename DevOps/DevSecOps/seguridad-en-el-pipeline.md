---
resumen: >-
  Los controles de seguridad del pipeline son las verificaciones automáticas por etapa: secretos
  antes del commit, SAST, SCA, escaneo de IaC y de imágenes, DAST y un policy gate.
estado: borrador
estabilidad: estable
fuentes:
  - "OWASP DevSecOps Guideline: https://owasp.org/www-project-devsecops-guideline/"
  - "OWASP Top 10 CI/CD Security Risks: https://owasp.org/www-project-top-10-ci-cd-security-risks/"
  - "Archivo/DevOps/devsecops-pipeline-avanzado.md (original, texto generado con IA)"
aliases: [Controles de seguridad del pipeline, Security gates, Pipeline seguro]
creado: 2026-10-03
revisado:
---

# Seguridad en el pipeline

Los controles de seguridad del pipeline son las verificaciones automáticas por etapa: secretos
antes del commit, SAST, SCA, escaneo de IaC y de imágenes, DAST y un policy gate.

## Por qué cada control corre lo antes posible

Cada control encuentra un tipo de problema distinto, y lo encuentra más barato cuanto antes
corre. Un secreto detectado antes del commit no llega nunca al historial; el mismo secreto
detectado en producción obliga a rotarlo y a revisar quién lo usó.

## Los controles por etapa según OWASP

La OWASP DevSecOps Guideline ordena los controles según la etapa del ciclo:

| Etapa | Control | Qué detecta |
|---|---|---|
| Antes del commit | detección de secretos | contraseñas, claves y tokens en el código |
| Build | **SAST** (análisis estático) | patrones inseguros en el código propio |
| Build | **SCA** (análisis de composición) | dependencias con vulnerabilidades conocidas o licencias no permitidas |
| Build | escaneo de IaC | configuraciones riesgosas en Terraform, Helm o Kubernetes |
| Empaquetado | escaneo de imagen | paquetes vulnerables dentro del contenedor |
| Entorno de prueba | **DAST** (análisis dinámico) | fallas que solo aparecen con la aplicación corriendo |
| PR y antes de desplegar | policy gate | si el conjunto de reportes cumple las reglas para mergear o desplegar |
| Producción | seguridad en ejecución | comportamientos anómalos de procesos y contenedores |

Cada etapa produce un reporte legible por máquina que se guarda junto al build. El **policy
gate** lee esos reportes y decide con reglas escritas como [Policy as code](policy-as-code.md), por ejemplo "no
avanza con vulnerabilidades críticas sin excepción aprobada".

El pipeline mismo también es un blanco. OWASP lista diez riesgos propios del CI/CD, entre ellos
el manejo pobre de credenciales y la validación insuficiente de la integridad de los
artefactos. Esos dos se tratan en [Gestión de secretos](gestion-de-secretos.md) y en
[Cadena de suministro de software](cadena-de-suministro-de-software.md).

Las herramientas concretas de cada fila están en [Herramientas de seguridad del pipeline](herramientas-de-seguridad-del-pipeline.md).

## Un puerto 22 abierto frenado en el PR

Un PR cambia un módulo de Terraform y abre el puerto 22 de una máquina a internet. El escaneo de
IaC lo marca, el policy gate del PR bloquea el merge y muestra la regla que falló. Si el cambio
llegara igual a la etapa de despliegue, el mismo gate lo frenaría ahí.

## Los controles del pipeline son una parte de DevSecOps

**DevSecOps**: es la práctica completa, con cultura y responsabilidades
([DevSecOps](devsecops.md)). Esta nota es solo la parte automática dentro del pipeline.
