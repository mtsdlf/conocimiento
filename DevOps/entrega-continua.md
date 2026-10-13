---
tipo: concepto
resumen: >-
  La entrega continua es construir el software de forma que cada cambio validado quede listo
  para pasar a producción en cualquier momento; el paso a producción sigue siendo una decisión
  manual.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Martin Fowler, ContinuousDelivery: https://martinfowler.com/bliki/ContinuousDelivery.html"
  - "Jez Humble, Patterns (deployment pipeline), continuousdelivery.com: https://continuousdelivery.com/implementing/patterns/"
  - "Archivo/DevOps/cicd-fundamentos.md (original, texto generado con IA)"
  - "Archivo/DevOps/devops-referencia.md (original, texto generado con IA)"
aliases: [Continuous delivery, CD, Entrega continua de software]
parte_de: []
requiere: [integracion-continua]
relacionado: [estrategias-de-despliegue]
---

# Entrega continua

La entrega continua es construir el software de forma que cada cambio validado quede listo
para pasar a producción en cualquier momento; el paso a producción sigue siendo una decisión
manual.

## Por qué importa

Si preparar una versión lleva semanas, se libera poco y en lotes grandes, y cada salida es
riesgosa. Con entrega continua, liberar pasa a ser una decisión de negocio y no un proyecto
técnico: se puede salir hoy con lo que está en la rama principal.

## Cómo funciona

Fowler la resume con una prueba: ¿se puede desplegar a producción la versión actual "con un
minuto de aviso"? Para eso, cada cambio que pasa la [[integracion-continua]] sigue por un
pipeline de despliegue ([[pipeline-de-ci-cd]]) que lo instala en entornos de preproducción (staging, pruebas de carga,
pruebas exploratorias) y corre más validaciones.

Dos reglas de Jez Humble sostienen el pipeline:

- **Construir una sola vez**: el paquete que llega a producción es el mismo que se probó.
- **Desplegar igual en todos los entornos**: así el mecanismo de despliegue también se prueba.

| | Integración continua | Entrega continua | Despliegue continuo |
|---|---|---|---|
| Build y pruebas automáticas | sí | sí | sí |
| Despliegue automático | opcional, a pruebas | sí, a preproducción | sí, a producción |
| Aprobación manual para producción | no aplica | sí | no |

## Ejemplo

Cada merge a `main` produce una imagen que se despliega sola en staging y pasa pruebas de
aceptación. Producción se actualiza los martes, cuando el responsable de producto aprueba el
paso en el pipeline; técnicamente se podría hacer cualquier día.

## No confundir con

[[despliegue-continuo]]. Fowler distingue: en despliegue continuo cada cambio llega a producción
solo; en entrega continua el equipo puede hacerlo, pero elige cuándo. Todo despliegue continuo
requiere entrega continua, no al revés.

## Relaciones

- Requiere: [[integracion-continua]] — la entrega parte de una rama principal siempre integrada.
- Relacionado: [[estrategias-de-despliegue]] — cómo se hace el paso a producción con bajo riesgo.
- Base de: [[despliegue-continuo]] — el paso siguiente, sin aprobación manual.
- Ver también: [[pipeline-de-ci-cd]] — la automatización que recorre los entornos.
