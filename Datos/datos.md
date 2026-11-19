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

Para aprenderlo en orden: [Análisis de cohortes desde cero](recorrido-analisis-de-cohortes.md).

## Conceptos base

- [Cohorte](cohorte.md) — qué es una cohorte y en qué se diferencia de un segmento; se lee primero.
- [Cohorte de adquisición](cohorte-de-adquisicion.md) — agrupar por cuándo llegó cada usuario; la cohorte por defecto.
- [Cohorte de comportamiento](cohorte-de-comportamiento.md) — agrupar por lo que hizo; para buscar qué acciones van con
  quedarse.
- [Retención](retencion.md) — qué significa que un usuario "se quede" y las tres cosas que se definen para
  medirlo.
- [Churn](churn.md) — la pérdida de clientes; cómo se define "irse" con contrato y sin él.
- [Análisis de cohortes](analisis-de-cohortes.md) — por qué se comparan cohortes a la misma edad en vez de promedios.

## Métricas

- [Tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md) — la métrica central: % de la cohorte que vuelve en el
  período N.
- [Retención de N días](retencion-de-n-dias.md) — volver en el período exacto (D1, D7, D30); para productos de uso
  frecuente.
- [Retención unbounded](retencion-unbounded.md) — volver en N o después; para productos de uso irregular.
- [Tasa de churn](tasa-de-churn.md) — % de la base que se va en un período, y por qué el promedio engaña.

## Leer y armar cohortes

- [Tabla de cohortes](tabla-de-cohortes.md) — cómo se lee el triángulo por fila, columna y diagonal.
- [Curva de retención](curva-de-retencion.md) — qué dice la forma de la curva: si se aplana o cae a cero.
- [Armar una tabla de cohortes](armar-una-tabla-de-cohortes.md) — los pasos para calcularla desde una tabla de eventos.

## Referencia de herramientas

- [Cohortes en herramientas de analítica](cohortes-en-herramientas-de-analitica.md) — dónde está la retención en GA4, Amplitude,
  Mixpanel y PostHog, y cómo se llama cada variante en cada una.
