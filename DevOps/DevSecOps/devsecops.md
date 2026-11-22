---
resumen: >-
  DevSecOps es integrar la seguridad en todo el ciclo de entrega como responsabilidad compartida
  y automatizada (shift-left), en vez de un control al final.
estado: borrador
estabilidad: estable
fuentes:
  - "OWASP DevSecOps Guideline: https://owasp.org/www-project-devsecops-guideline/"
  - "NIST SP 800-204C, Implementation of DevSecOps for a Microservices-based Application with Service Mesh (2022): https://csrc.nist.gov/pubs/sp/800/204/c/final"
  - "Archivo/DevOps/devsecops-pipeline-avanzado.md (original, texto generado con IA)"
aliases: [DevSecOps, Shift-left security, Seguridad shift-left]
creado: 2026-10-03
revisado:
---

# DevSecOps

DevSecOps es integrar la seguridad en todo el ciclo de entrega como responsabilidad compartida
y automatizada (shift-left), en vez de un control al final.

Dentro de [DevOps](../devops.md), DevSecOps cruza la entrega: sus controles corren como etapas del
[Pipeline de CI/CD](../Integracion-y-entrega/pipeline-de-ci-cd.md), y los PR de
[GitOps](../Despliegue/gitops.md) son donde se aplican antes de desplegar.

## Por qué la seguridad no puede ser un control al final

Si la seguridad es una revisión manual antes de cada salida a producción, frena la entrega y
encuentra los problemas cuando arreglarlos cuesta más. Un equipo que despliega varias veces por
día no puede esperar una auditoría por despliegue. DevSecOps resuelve ese choque: la seguridad
corre en el mismo pipeline, con la misma frecuencia que las pruebas.

## Seguridad clásica y DevSecOps

| Aspecto | Seguridad clásica | DevSecOps |
|---|---|---|
| Quién | un equipo central de seguridad | cada equipo, con apoyo de seguridad |
| Cuándo | al final del ciclo | en cada etapa, desde el diseño |
| Cómo | revisiones manuales | controles automáticos en el pipeline |
| Evidencia | auditorías periódicas | reportes generados en cada build |

**Shift-left** es mover cada control lo más temprano posible: detectar un secreto antes del
commit, una dependencia vulnerable en el PR y una configuración insegura antes de aplicarla.
NIST SP 800-204C describe la seguridad aplicada a cinco tipos de código que viajan por el
pipeline: el de la aplicación, el de los servicios de la aplicación, la infraestructura como
código, la política como código y la observabilidad como código.

El equipo de seguridad pasa de aprobar cambios a escribir los controles y las políticas que el
pipeline aplica. Una práctica habitual es tener un **security champion** en cada equipo: una
persona con formación extra que acerca las dudas al equipo de seguridad.

## Una dependencia vulnerable frenada en el PR

Un desarrollador agrega una librería con una vulnerabilidad crítica conocida. El escaneo de
dependencias falla en el PR y lo bloquea antes del merge. El desarrollador sube la versión
corregida en el mismo PR, sin esperar una revisión externa.

## Un equipo DevSecOps repite el problema

**Un equipo DevSecOps**: crear un equipo con ese nombre que revisa todo al final repite el
problema de siempre con otro nombre, igual que el [Anti-patrón del equipo DevOps](../../Platform-Engineering/Colaboracion-Dev-Ops/anti-patron-equipo-devops.md).

## Qué hay adentro de DevSecOps

- [Seguridad en el pipeline](seguridad-en-el-pipeline.md) — los controles automáticos por etapa.
- [Herramientas de seguridad del pipeline](herramientas-de-seguridad-del-pipeline.md) — ficha con la herramienta habitual de cada control, copiada el 2026-10-03.
- [Cadena de suministro de software](cadena-de-suministro-de-software.md) — asegurar que el artefacto desplegado es el esperado.
- [Gestión de secretos](gestion-de-secretos.md) — credenciales fuera del código: almacén externo, vida corta, federación por OIDC, cifrado en Git y detección.
- [SOPS](sops.md) — cómo cifrar los valores de un archivo de configuración para guardarlo en Git y que GitOps lo descifre al aplicar.
- [Policy as code](policy-as-code.md) — las reglas de seguridad como código evaluable.
