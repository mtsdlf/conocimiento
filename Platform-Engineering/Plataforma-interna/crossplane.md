---
resumen: >-
  Crossplane es un framework de control plane para platform engineering que extiende Kubernetes
  para que la plataforma ofrezca recursos de infraestructura como APIs declarativas propias.
estado: borrador
estabilidad: estable
fuentes:
  - "Crossplane, documentación oficial: https://docs.crossplane.io/latest/"
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
aliases: [Crossplane]
creado: 2026-10-03
revisado:
---

# Crossplane

Crossplane es un framework de control plane para platform engineering que extiende Kubernetes
para que la plataforma ofrezca recursos de infraestructura como APIs declarativas propias.

## Una base de datos como API propia de la plataforma

Un equipo de plataforma quiere ofrecer "una base de datos" como [Capacidad de plataforma](capacidad-de-plataforma.md), no
como el detalle de un proveedor de nube. Crossplane permite definir ese recurso como una API
propia de la plataforma y conectarla con la infraestructura real. Es un proyecto graduado de la
CNCF, y el white paper de plataformas lo nombra como forma de provisionar capacidades de manera
automática.

## XRD, Composition, managed resource y provider

Según su documentación, Crossplane tiene cuatro piezas:

| Pieza | Qué hace |
|---|---|
| Composite Resource Definition (XRD) | define el tipo de recurso que los usuarios pueden pedir y su esquema, por ejemplo `PostgresInstance` con tamaño y versión |
| Composition | dice cómo se cumple ese pedido: qué recursos de abajo se crean y con qué configuración |
| Managed resource | representa un recurso concreto de infraestructura, como una instancia de base de datos en un proveedor |
| Provider | paquete que conecta Crossplane con una nube o un servicio |

El flujo: un equipo crea un recurso del tipo definido en la XRD; la Composition lo traduce a
managed resources; los providers los crean en la infraestructura. Como corre sobre Kubernetes,
Crossplane reconcilia todo el tiempo: si alguien cambia el recurso a mano, lo vuelve a dejar como
dice la definición.

En una [Plataforma API-first](plataforma-api-first.md), los recursos de Crossplane son una API declarativa más, y pasan
por los mismos controles y la misma auditoría que el resto.

## El tipo `PostgresInstance`

El equipo de plataforma publica el tipo `PostgresInstance` con dos campos: tamaño (chico,
mediano, grande) y versión. Un equipo aplica un manifiesto con `tamaño: chico` y Crossplane crea
la instancia, la red y el secreto con las credenciales en el proveedor que define la Composition.

## Crossplane y Terraform

Terraform aplica un plan cuando alguien lo ejecuta; Crossplane corre como controlador
dentro de Kubernetes y corrige desvíos de forma continua, y expone los recursos como APIs de
Kubernetes que otros equipos consumen.
