---
tipo: metrica
resumen: >-
  La tasa de churn es el porcentaje de los clientes que había al inicio de un período que se
  fueron durante ese período (por ejemplo, en el mes).
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://www.brucehardie.com/papers/021/sbg_2006-05-30.pdf
  - http://brucehardie.com/papers/037/BdW_JIM_2018-01-10_rev.pdf
aliases: [churn rate, tasa de abandono, tasa de cancelación]
parte_de: []
requiere: [churn]
relacionado: [tasa-de-retencion-por-cohorte]
---

# Tasa de churn

La tasa de churn es el porcentaje de los clientes que había al inicio de un período que se
fueron durante ese período (por ejemplo, en el mes).

## Definición

- **Fórmula**: clientes del inicio del período que se fueron en el período ÷ clientes al inicio
  del período.
- **Unidad y grano**: % por período (mes, trimestre, año).
- **Incluye**: solo a los clientes que estaban al inicio.
- **Excluye**: a los que entraron durante el período. Si además se fueron en ese mismo período,
  tampoco entran al numerador: sumarlos inflaría la tasa.

## Cómo leerla

Más baja es mejor. Con un churn mensual constante *c*, la vida media de un cliente es de unos
1/*c* meses: un 5 % mensual da unos 20 meses. No hay un umbral universal; depende del negocio.

## Limitaciones

- Promedia toda la base: mezcla clientes nuevos, que se van más, con veteranos, que se van menos.
  Según Fader y Hardie, el churn de una cohorte baja con su antigüedad aunque ningún cliente
  cambie, porque los propensos a irse se van primero. Para ver si los nuevos se van más rápido se
  usa la [[tasa-de-retencion-por-cohorte|tasa de retención por cohorte]].
- En productos sin contrato depende de la ventana de inactividad elegida (ver [[churn]]).
- El churn de ingresos (MRR perdido ÷ MRR inicial) es otra métrica: cuenta dinero, no clientes.

## Dónde se calcula

En el sistema de suscripciones o de facturación, o con SQL sobre las altas y bajas de clientes.
Este Tema todavía no tiene un modelo enlazable.

## Contexto para agentes

- **Preguntas que responde**: "¿qué porcentaje de clientes perdimos este mes?".
- **Instrucciones**: se indican siempre el período y la definición de "irse". La tasa no es
  100 % menos la retención de una cohorte: miden grupos distintos.

## Relaciones

- Requiere: [[churn]] — define qué cuenta como irse.
- Relacionado: [[tasa-de-retencion-por-cohorte]] — la mirada por cohorte que corrige el sesgo del
  promedio.
