---
tipo: concepto
resumen: >-
  DevSecOps es integrar la seguridad en todo el ciclo de entrega como responsabilidad compartida
  y automatizada (shift-left), en vez de un control al final.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "OWASP DevSecOps Guideline: https://owasp.org/www-project-devsecops-guideline/"
  - "NIST SP 800-204C, Implementation of DevSecOps for a Microservices-based Application with Service Mesh (2022): https://csrc.nist.gov/pubs/sp/800/204/c/final"
  - "Archivo/DevOps/devsecops-pipeline-avanzado.md (original, texto generado con IA)"
aliases: [DevSecOps, Shift-left security, Seguridad shift-left]
parte_de: []
requiere: [pipeline-de-ci-cd]
relacionado: [gitops]
---

# DevSecOps

DevSecOps es integrar la seguridad en todo el ciclo de entrega como responsabilidad compartida
y automatizada (shift-left), en vez de un control al final.

## Por qué importa

Si la seguridad es una revisión manual antes de cada salida a producción, frena la entrega y
encuentra los problemas cuando arreglarlos cuesta más. Un equipo que despliega varias veces por
día no puede esperar una auditoría por despliegue. DevSecOps resuelve ese choque: la seguridad
corre en el mismo pipeline, con la misma frecuencia que las pruebas.

## Cómo funciona

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

## Ejemplo

Un desarrollador agrega una librería con una vulnerabilidad crítica conocida. El escaneo de
dependencias falla en el PR y lo bloquea antes del merge. El desarrollador sube la versión
corregida en el mismo PR, sin esperar una revisión externa.

## No confundir con

**Un equipo DevSecOps**: crear un equipo con ese nombre que revisa todo al final repite el
problema de siempre con otro nombre, igual que el [[anti-patron-equipo-devops]].

## Relaciones

- Requiere: [[pipeline-de-ci-cd]] — los controles de DevSecOps corren como etapas del pipeline.
- Partes: [[seguridad-en-el-pipeline]] — los controles automáticos por etapa.
- Partes: [[cadena-de-suministro-de-software]] — asegurar que el artefacto desplegado es el esperado.
- Partes: [[gestion-de-secretos]] — credenciales fuera del código.
- Partes: [[policy-as-code]] — las reglas de seguridad como código evaluable.
- Relacionado: [[gitops]] — los PR de GitOps son donde se aplican los controles antes de desplegar.
- Ver también: [[anti-patron-equipo-devops]] — el mismo error organizativo, aplicado a seguridad.
