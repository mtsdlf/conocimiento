---
resumen: >-
  Evolución es lo que le pasa al software después de la primera entrega: se le pagan o no las deudas,
  se lo reordena sin cambiar lo que hace, alguien que no lo escribió lo toma y se lo mantiene al día
  con sus dependencias y plataformas.
estado: borrador
estabilidad: estable
fuentes:
  - https://martinfowler.com/bliki/TechnicalDebtQuadrant.html
  - https://martinfowler.com/books/refactoring.html
  - https://research.google/blog/accelerating-code-migrations-with-ai/
  - https://arxiv.org/abs/2511.04427
  - https://www.gitclear.com/ai_assistant_code_quality_2025_research
  - "Desarrollo/.investigacion/verificacion-y-evolucion.md (2026-11-27)"
aliases: [mantenimiento de software, evolución del software, software maintenance, mantenimiento evolutivo]
creado: 2026-11-27
revisado:
---

# Evolución

Evolución es lo que le pasa al software después de la primera entrega: se le pagan o no las deudas, se lo reordena sin cambiar lo que hace, alguien que no lo escribió lo toma y se lo mantiene al día con sus dependencias y plataformas.

En el todo de [Desarrollo](../desarrollo.md), Evolución recibe el sistema que [Encargo](../Encargo/encargo.md) entregó en el [traspaso](../Encargo/traspaso.md) y abre nuevos encargos cuando hace falta un cambio que el cliente tiene que acordar. Cada cambio vuelve a pasar por el ciclo técnico: se define, se construye y se [verifica](../Verificacion/verificacion.md). Lo que distingue a esta vertical es que parte de un sistema que ya funciona y que alguien usa: lo primero es no romperlo.

## El comportamiento actual como punto de partida

Según la lectura de esta base, las cuatro prácticas de la vertical tienen la misma forma. Primero se fija lo que el sistema hace hoy con pruebas; después se cambia; al final las pruebas dicen si algo se rompió. Refactorizar es cambiar la forma sin cambiar el comportamiento, según la definición de Fowler, y eso es una especificación que se puede verificar. En un sistema heredado sin pruebas, el primer paso es escribirlas sobre lo que hace hoy. En una migración, la suite es la que decide si cada cambio entra.

Sin esas pruebas no hay forma barata de saber si un cambio rompió algo (inferencia de esta base).

## Lo que cambia cuando el código lo cambia un agente

Los agentes tiran en dos direcciones. Por un lado, la deuda se acumula más rápido: según el resumen de un estudio causal sobre repositorios que adoptaron un editor con agente (MSR 2026), la ganancia de velocidad fue transitoria y el aumento de complejidad y de advertencias de análisis estático, persistente. GitClear, que vende análisis de código, midió más líneas copiadas y menos líneas movidas (la señal de refactor) entre 2020 y 2024; las cifras están en [deuda técnica](deuda-tecnica.md#la-deuda-que-acumula-un-agente).

Por el otro, un agente hace barato el trabajo mecánico de pagarla: renombrar, extraer, migrar miles de archivos. Google reporta que en una migración interna 80 % de los cambios de código aprobados los generó un modelo, y que cada cambio se validó compilando y corriendo pruebas, con revisión de personas. Es un autoinforme de la empresa.

El patrón que queda es criterio de esta base, a partir de esos casos: el modelo propone, una verificación determinista decide y las personas revisan. Decidir qué deuda pagar y qué migrar es de personas; hacerlo, con pruebas que decidan, puede ser de agentes.

## Cómo falla la evolución

Falla por posponer: las dependencias se atrasan hasta que actualizar obliga a cambiar código en muchos lugares a la vez, y la deuda se acumula hasta que cada cambio cuesta más. Falla también por reescribir de golpe un sistema que funciona, en vez de reemplazarlo de a partes con [strangler fig](../../Arquitectura/Estilos/strangler-fig.md), el patrón de Arquitectura para modernizar sin apagar. Y falla cuando se cambia sin pruebas que fijen el comportamiento, porque nadie se entera de lo que se rompió hasta que lo ve el cliente.

> [!NOTE]
> Sin fuente todavía: las tres fallas de arriba son criterio de esta base; no se leyó una fuente que las mida.

## Qué hay adentro de Evolución

- [Deuda técnica](deuda-tecnica.md): qué es, cuánto cuesta según los estudios, cuándo se paga y cuándo no.
- [Refactorizar](refactorizar.md): cambiar la forma sin cambiar el comportamiento, y por qué es el trabajo mejor acotado para un agente.
- [Sistema heredado](sistema-heredado.md): entrar a un código que no escribiste: costuras, pruebas de caracterización y lo que un agente entiende o no.
- [Migraciones y actualizaciones](migraciones-y-actualizaciones.md): dependencias, versiones y cambios masivos, con el patrón de las migraciones asistidas por modelos.

Las versiones que se publican siguen el [versionado semántico](../../DevOps/Ramas-y-versiones/versionado-semantico.md), y lo que un sistema le cuesta a quien lo mantiene empieza a pesar desde la [plantilla de proyecto](../Construccion/plantilla-de-proyecto.md).
