---
tipo: metrica
resumen: >-
  El costo unitario divide el costo de tecnología de un servicio por una unidad de negocio o de
  recurso (transacción, cliente, GB) en el mismo período; mide eficiencia sin que el crecimiento
  la distorsione.
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "FinOps Foundation, Unit Economics: https://www.finops.org/framework/capabilities/unit-economics/"
  - "Archivo/Cloud/finops-referencia.md (original, §5.2; los KPIs sin fuente se descartaron)"
aliases: [costo por unidad, unit cost, unit economics, economía unitaria]
parte_de: [que-es-finops]
requiere: [showback-y-chargeback]
relacionado: []
---

# Costo unitario

El costo unitario divide el costo de tecnología de un servicio por una unidad de negocio o de
recurso (transacción, cliente, GB) en el mismo período; mide eficiencia sin que el crecimiento
la distorsione.

## Definición

- **Fórmula**: costo del servicio en el período / unidades producidas en el mismo período.
  `costo_unitario = costo / unidades`.
- **Unidad y grano**: moneda por unidad (USD por 1.000 transacciones, USD por cliente activo), por
  mes o por semana.
- **Incluye**: el costo asignado al servicio, con su parte de lo compartido (red, observabilidad)
  según el criterio de [[showback-y-chargeback]].
- **Excluye**: lo que no se puede asignar al servicio; si se deja afuera, se dice.

La FinOps Foundation distingue dos familias:

| Familia | Ejemplos | Quién la controla |
|---|---|---|
| Eficiencia de recursos | Costo por GB almacenado, por vCPU, por token | Ingeniería |
| Unidad de negocio | Costo por cliente, por transacción, costo de servir | Producto y negocio |

## Cómo leerla

Si el costo total sube pero el unitario baja, el servicio crece y se vuelve más eficiente. Si el
unitario sube, cada unidad cuesta más: un cambio de arquitectura, recursos ociosos o una tarifa
peor. Según la Foundation, sin relacionar el costo con el beneficio no se puede saber si un gasto
es adecuado.

## Limitaciones

- Una unidad mal elegida engaña: "costo por usuario registrado" baja aunque nadie use el producto.
- Con pocas unidades (un servicio nuevo), el costo fijo domina y el número salta mucho.
- Depende de que la asignación sea buena: si el costo compartido se reparte mal, el unitario
  también.

## Dónde se calcula

No hay un tablero propio: se arma con el costo por etiqueta o suscripción de Cost Management y el
conteo de unidades que da la aplicación o el producto. La Foundation recomienda empezar por
métricas de eficiencia de recursos, que ingeniería controla, y pasar a las de negocio cuando los
datos sean confiables.

## Contexto para agentes

- **Preguntas que responde**: "¿El servicio es más eficiente que el trimestre pasado?", "¿Cuánto
  cuesta servir a un cliente?".
- **Instrucciones**: comparar siempre el mismo período y la misma unidad; no mezclar una métrica
  de recursos con una de negocio en la misma serie.

## Relaciones

- Parte de: [[que-es-finops]] — es la capacidad de economía unitaria del marco.
- Requiere: [[showback-y-chargeback]] — sin asignar el costo al servicio no hay numerador.
