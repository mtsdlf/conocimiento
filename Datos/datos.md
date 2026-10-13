---
tipo: mapa
resumen: >-
  Mapa del Tema Datos: conceptos y métricas de análisis de datos, por ahora centrado en
  análisis de cohortes, retención y churn, para quien está aprendiendo Data Analytics.
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [conocimiento]
---

# Datos

Mapa del Tema Datos: conceptos y métricas de análisis de datos, por ahora centrado en
análisis de cohortes, retención y churn, para quien está aprendiendo Data Analytics.

Para aprenderlo en orden: [[recorrido-analisis-de-cohortes]].

## Conceptos base

- [[cohorte]] — qué es una cohorte y en qué se diferencia de un segmento; se lee primero.
- [[cohorte-de-adquisicion]] — agrupar por cuándo llegó cada usuario; la cohorte por defecto.
- [[cohorte-de-comportamiento]] — agrupar por lo que hizo; para buscar qué acciones van con
  quedarse.
- [[retencion]] — qué significa que un usuario "se quede" y las tres cosas que se definen para
  medirlo.
- [[churn]] — la pérdida de clientes; cómo se define "irse" con contrato y sin él.
- [[analisis-de-cohortes]] — por qué se comparan cohortes a la misma edad en vez de promedios.

## Métricas

- [[tasa-de-retencion-por-cohorte]] — la métrica central: % de la cohorte que vuelve en el
  período N.
- [[retencion-de-n-dias]] — volver en el período exacto (D1, D7, D30); para productos de uso
  frecuente.
- [[retencion-unbounded]] — volver en N o después; para productos de uso irregular.
- [[tasa-de-churn]] — % de la base que se va en un período, y por qué el promedio engaña.

## Leer y armar cohortes

- [[tabla-de-cohortes]] — cómo se lee el triángulo por fila, columna y diagonal.
- [[curva-de-retencion]] — qué dice la forma de la curva: si se aplana o cae a cero.
- [[armar-una-tabla-de-cohortes]] — los pasos para calcularla desde una tabla de eventos.

## Referencia de herramientas

- [[cohortes-en-herramientas-de-analitica]] — dónde está la retención en GA4, Amplitude,
  Mixpanel y PostHog, y cómo se llama cada variante en cada una.
