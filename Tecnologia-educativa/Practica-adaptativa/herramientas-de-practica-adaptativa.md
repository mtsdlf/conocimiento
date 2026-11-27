---
resumen: >-
  Ficha con las herramientas de práctica adaptativa verificadas al 2026-11-27: Anki y sus algoritmos SM-2 y FSRS, con sus valores por defecto y el benchmark público, Math Academy y Khan Academy.
estado: borrador
estabilidad: volatil
fuentes:
  - "Anki: https://apps.ankiweb.net/ (leída 2026-11-27)"
  - "Manual de Anki, algoritmo: https://docs.ankiweb.net/faqs/what-spaced-repetition-algorithm (leída 2026-11-27)"
  - "Manual de Anki, opciones del mazo: https://docs.ankiweb.net/deck-options.html (leída 2026-11-27)"
  - "FSRS: https://www.github.com/open-spaced-repetition/free-spaced-repetition-scheduler"
  - "Benchmark: https://expertium.github.io/Benchmark.html (sin fecha en la página)"
  - "Math Academy, How it works: https://www.mathacademy.com/how-it-works (leída 2026-11-27)"
  - "Skycak, J., Individualized Spaced Repetition in Hierarchical Knowledge Structures: https://justinmath.com/individualized-spaced-repetition-in-hierarchical-knowledge-structures/"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
aliases: [Anki, FSRS, SM-2, SuperMemo, Math Academy, Khan Academy, herramientas de repaso espaciado]
creado: 2026-11-27
revisado:
---

# Herramientas de práctica adaptativa

Ficha con las herramientas de práctica adaptativa verificadas al 2026-11-27: Anki y sus algoritmos SM-2 y FSRS, con sus valores por defecto y el benchmark público, Math Academy y Khan Academy.

Implementan el [repaso espaciado con software](repaso-espaciado-con-software.md) y los [sistemas adaptativos](sistemas-adaptativos.md).

Copiado de las páginas oficiales y del manual de Anki el 2026-11-27. Lo que dice cada proveedor sobre sí mismo no es evidencia de aprendizaje. Re-verificar cada tres meses.

## Anki

| Dato | Valor al 2026-11-27 |
|---|---|
| Qué es | Programa de tarjetas que programa cada repaso para cuando es más probable olvidar |
| Plataformas | Escritorio gratis (Windows, macOS, Linux); AnkiDroid gratis en Android; AnkiMobile de pago en iOS; sincronización AnkiWeb gratis |
| Algoritmo original | Derivado de SuperMemo 2 (SM-2), con cambios: pasos de aprendizaje configurables, cuatro botones, «eases never drop below 130%» |
| Algoritmo FSRS | Basado en el modelo de tres componentes de la memoria (retrievability, stability, difficulty), que el proyecto atribuye a Wozniak; ajusta sus parámetros con el historial; disponible desde Anki 23.10 |
| Retención deseada por defecto | 90 %, «a good balance»; más del 97 % sobrecarga de repasos |
| Datos que necesita el ajuste | «Several reviews»; con «less than a few hundred» repasos, causa común de mal rendimiento |
| FSRS frente a SM-2, según el manual | FSRS «reportedly requires fewer reviews than SM-2»; pruebas preliminares lo ubican «roughly on par» con SM-17, el algoritmo propietario de SuperMemo |

## Benchmark de algoritmos de repaso

La comparación pública de la comunidad de FSRS usa 9.999 colecciones de Anki y 349.923.850 repasos, y mide qué tan bien predice cada algoritmo si se va a recordar una tarjeta (RMSE, log loss y AUC). FSRS-6 supera a SM-2 en log loss en el 99,6 % de los usuarios. El autor advierte: «There is no way to have a truly fair, no caveats, comparison». SM-2 no fue diseñado para dar probabilidades y se le agregó un conversor. Mide predicción del olvido, no aprendizaje.

> [!NOTE]
> Sin fuente todavía: la afirmación de que un promedio móvil sin parámetros queda casi igual que FSRS-7.

## Math Academy

Plataforma paga de matemática (precio no verificado). Según su página, arranca con un diagnóstico adaptativo de 30 a 45 minutos, arma un grafo de conocimiento por alumno y programa repasos; cita práctica distribuida, intercalado, efecto del testeo y ejemplos resueltos, sin estudios ni datos de resultados. Implementa el repaso jerárquico de Skycak descrito en [sistemas adaptativos](sistemas-adaptativos.md). El autor dice que no hay estudios académicos del sistema.

## Khan Academy

Plataforma de práctica de matemática escolar. Su tutor con IA, Khanmigo, está en la ficha de [modos de estudio de la IA](../IA-en-la-educacion/modos-de-estudio-de-la-ia.md). En el ensayo de Oreopoulos y Low (NBER, 2026, sin revisión por pares), el efecto del tutor fue parecido al de la práctica de Khan Academy sin IA, según su resumen.
