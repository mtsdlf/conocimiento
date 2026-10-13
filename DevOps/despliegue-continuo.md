---
tipo: concepto
resumen: >-
  El despliegue continuo es llevar a producción, sin intervención humana, cada cambio que pasa
  todas las verificaciones automáticas del pipeline.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Martin Fowler, ContinuousDelivery: https://martinfowler.com/bliki/ContinuousDelivery.html"
  - "Martin Fowler (Pete Hodgson), Feature Toggles: https://martinfowler.com/articles/feature-toggles.html"
  - "Archivo/DevOps/cicd-fundamentos.md (original, texto generado con IA)"
aliases: [Continuous deployment]
parte_de: []
requiere: [entrega-continua]
relacionado: [estrategias-de-despliegue]
---

# Despliegue continuo

El despliegue continuo es llevar a producción, sin intervención humana, cada cambio que pasa
todas las verificaciones automáticas del pipeline.

## Por qué importa

Cada aprobación manual es una espera y junta cambios en lotes más grandes. Sin ella, cada
cambio sale solo y chico: si algo falla, se sabe qué commit lo causó y se revierte rápido.
Según Fowler, esto lleva a muchos despliegues a producción por día.

## Cómo funciona

El pipeline es el mismo de la [[entrega-continua]], pero el último paso no espera a nadie: si
las pruebas, los escaneos y las verificaciones de los entornos previos pasan, el cambio se
despliega. Como no hay una persona que frene un cambio malo, el pipeline necesita:

- pruebas automáticas que den confianza suficiente para no revisar a mano;
- una estrategia de despliegue gradual, como canary o blue/green (ver
  [[estrategias-de-despliegue]]), con rollback automático;
- monitoreo que detecte la degradación minutos después del despliegue;
- feature flags para desplegar código incompleto sin mostrarlo al usuario.

Los feature flags son los que permiten separar el **despliegue** (el código llega a producción)
de la **liberación** (el usuario ve la funcionalidad). Con ellos, una funcionalidad a medio
hacer viaja apagada en cada despliegue y se enciende cuando está lista.

## Ejemplo

Un servicio despliega a producción unas 20 veces por día. Cada merge a `main` pasa pruebas,
se despliega al 5 % del tráfico y, si la tasa de errores no sube en 10 minutos, pasa al 100 %.
La funcionalidad nueva de checkout está desplegada desde hace dos semanas, apagada por un flag.

## No confundir con

[[entrega-continua]], donde el paso a producción queda en manos de una persona. Fowler: "para
hacer despliegue continuo hay que estar haciendo entrega continua". Tampoco implica liberar todo
al usuario apenas se despliega: eso lo decide el flag.

## Relaciones

- Requiere: [[entrega-continua]] — agrega el paso automático a producción sobre ella.
- Relacionado: [[estrategias-de-despliegue]] — el despliegue gradual reemplaza a la aprobación manual.
