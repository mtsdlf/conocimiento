---
resumen: >-
  Mixture of experts (MoE) es una arquitectura en la que un router activa solo algunas subredes
  ("expertos") por token, para tener muchos parámetros con el costo de cómputo de pocos.
estado: borrador
estabilidad: estable
creado: 2026-10-03
fuentes:
  - https://arxiv.org/abs/1701.06538
  - https://arxiv.org/abs/2101.03961
  - https://arxiv.org/abs/2401.04088
aliases: [MoE, mezcla de expertos, sparse mixture of experts, sparse MoE]
---

# Mixture of experts

Mixture of experts (MoE) es una arquitectura en la que un router activa solo algunas subredes
("expertos") por token, para tener muchos parámetros con el costo de cómputo de pocos.

## Capacidad sin costo por token

En un modelo denso, cada token pasa por todos los parámetros: duplicar el modelo duplica el
cómputo de cada respuesta. MoE separa las dos cosas. La capacidad (parámetros totales) crece,
mientras el costo por token depende solo de los parámetros activos. Shazeer y otros (2017)
reportaron más de 1000 veces de capacidad con pérdidas menores de eficiencia de cómputo en GPU,
frente a los modelos densos de la época.

## El router y los expertos

MoE es una forma de construir la red que predice el siguiente token en un [LLM](llm.md).

Una capa MoE reemplaza un bloque feed-forward (la parte de cada capa que transforma cada token
por separado) por varios bloques paralelos, los **expertos**. Una
red de compuerta entrenable, el **router**, mira cada token y elige qué expertos lo procesan; la
salida es la combinación de esos expertos, pesada por el router. Los demás no se calculan para
ese token.

- Shazeer y otros (2017) llamaron a esto "sparsely-gated": activación dispersa entre miles de
  expertos posibles.
- Switch Transformer (Fedus y otros, 2021) simplificó el router a **un solo experto por token**.
  Llegó a un billón de parámetros sin que creciera el cómputo por token, y preentrenó hasta 7
  veces más rápido que T5, un modelo denso de Google, con los mismos recursos.

El costo que no baja es la memoria: todos los expertos tienen que estar cargados aunque cada
token use pocos.

## Mixtral 8x7B

Mixtral 8x7B (Mistral AI, 2024) tiene 8 expertos por capa y el router elige 2 por token. Suma
47 mil millones de parámetros, pero cada token usa 13 mil millones, alrededor del 28 %. No son
8 × 7 = 56 mil millones porque solo los bloques feed-forward se multiplican; el resto de cada
capa es compartido.

## MoE, ensamble y agentes expertos

Un **ensamble** de modelos corre varios modelos completos y combina sus respuestas: el costo se
multiplica. En MoE la elección es por token y por capa, dentro de un solo modelo. Tampoco es un
sistema de agentes "expertos": los expertos de MoE no tienen especialidades con nombre, y lo que
aprende cada uno sale del entrenamiento.
