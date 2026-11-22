---
resumen: >-
  Un pipeline de CI/CD es la secuencia automática de etapas (build, pruebas, empaquetado y
  despliegue) que dispara un evento del repositorio; cada artefacto que produce se identifica por
  el commit que lo originó, nunca por "latest".
estado: borrador
estabilidad: estable
fuentes:
  - "Jez Humble, Patterns (deployment pipeline), continuousdelivery.com: https://continuousdelivery.com/implementing/patterns/"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-advanced-collaboration.md (original, texto generado con IA)"
  - "Archivo/DevOps/cicd-aks.md (original, texto generado con IA)"
aliases: [Pipeline, CI/CD pipeline, Deployment pipeline, Pipeline de despliegue]
creado: 2026-10-03
revisado:
---

# Pipeline de CI/CD

Un pipeline de CI/CD es la secuencia automática de etapas (build, pruebas, empaquetado y
despliegue) que dispara un evento del repositorio; cada artefacto que produce se identifica por
el commit que lo originó, nunca por "latest".

## Por qué el pipeline tiene que ser reproducible

Es la pieza que convierte la [Integración continua](integracion-continua.md) y la [Entrega continua](entrega-continua.md) en algo que
ocurre solo en cada cambio. Si el pipeline no es reproducible, nadie sabe con certeza qué versión
corre en producción ni puede volver a construirla.

## Eventos, etapas y las tres reglas

Un evento del repositorio dispara una reacción:

| Evento | Reacción típica |
|---|---|
| PR abierto o actualizado | lint, pruebas, escaneos, entorno de preview |
| Merge a la rama principal | build, artefacto, despliegue a staging |
| Tag de versión | pipeline de release o despliegue a producción |
| Rama borrada | limpieza de entornos efímeros |

Las etapas van de lo más barato a lo más caro: análisis estático, build y pruebas unitarias,
pruebas de integración en un entorno efímero, escaneos de seguridad, despliegue y smoke tests
(pruebas mínimas de que el servicio desplegado responde). Cada etapa es un **gate**: si falla,
las siguientes no corren.

Tres reglas lo hacen confiable:

1. **Reproducible e idempotente**: el build depende solo del código del commit, así que correr
   dos veces el mismo commit da el mismo artefacto.
2. **Aislado**: cada job corre en un entorno limpio y efímero.
3. **Trazable**: el artefacto lleva el SHA del commit en su tag o en sus etiquetas.

Por la regla de Humble de "construir una sola vez", el mismo artefacto avanza de entorno en
entorno. Cada entorno lo pide al **registro** (el almacén de imágenes o paquetes) por SHA o por
**digest**, el hash del contenido, que no cambia nunca. El tag `latest`, en cambio, apunta a otro
contenido cada vez que alguien publica: con él no se sabe qué versión corre ni a cuál volver.

## El commit `a1b2c3d` de main a producción

Un push a `main` del commit `a1b2c3d` construye la imagen `app:a1b2c3d`, corre las pruebas, la
sube al registro y la despliega en staging. El release a producción usa esa misma imagen; si hay
que volver atrás, se redespliega el SHA anterior.

## Un pipeline no es una plantilla compartida

Una plantilla compartida. El pipeline es lo que corre para un repo; cuando muchos repos usan la
misma definición central, eso es un [Pipeline reutilizable](pipeline-reutilizable.md).

## Ver también

- [Infraestructura como código](../../Infraestructura/Aprovisionamiento/infraestructura-como-codigo.md) — el pipeline también valida y aplica la infraestructura.
- [Trazabilidad de cambios](../Repositorios/trazabilidad-de-cambios.md) — usa el SHA del artefacto para seguir un despliegue.
