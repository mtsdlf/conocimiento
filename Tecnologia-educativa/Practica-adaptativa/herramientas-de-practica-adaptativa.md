---
resumen: >-
  Ficha con las herramientas de práctica adaptativa verificadas al 2026-11-27: Anki y sus algoritmos SM-2 y FSRS, con sus valores por defecto y el benchmark público, Math Academy y Khan Academy.
estado: vigente
estabilidad: volatil
fuentes:
  - "Anki: https://apps.ankiweb.net/ (leída 2026-11-27)"
  - "Anki, releases: https://github.com/ankitects/anki/releases (leída 2026-11-27)"
  - "AnkiMobile Flashcards, App Store de EE.UU.: https://apps.apple.com/us/app/id373493387 (leída 2026-11-27)"
  - "Manual de Anki, algoritmo: https://docs.ankiweb.net/faqs/what-spaced-repetition-algorithm (leída 2026-11-27)"
  - "Manual de Anki, opciones del mazo: https://docs.ankiweb.net/deck-options.html (leída 2026-11-27)"
  - "FSRS: https://www.github.com/open-spaced-repetition/free-spaced-repetition-scheduler (README leído 2026-11-27)"
  - "Woźniak, P. (1990, en la web desde 1998), SuperMemo 2: Algorithm: https://www.super-memory.com/english/ol/sm2.htm (texto completo)"
  - "Benchmark: https://expertium.github.io/Benchmark.html (sin fecha en la página; leída 2026-11-27)"
  - "srs-benchmark, README (último cambio 2026-11-19): https://github.com/open-spaced-repetition/srs-benchmark (leído 2026-11-27)"
  - "Math Academy, How it works: https://www.mathacademy.com/how-it-works (leída 2026-11-27)"
  - "Math Academy, inicio y FAQ: https://www.mathacademy.com/ y https://www.mathacademy.com/faq (leídas 2026-11-27)"
  - "Skycak, J., Individualized Spaced Repetition in Hierarchical Knowledge Structures: https://justinmath.com/individualized-spaced-repetition-in-hierarchical-knowledge-structures/"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
  - "Tecnologia-educativa/.investigacion/fuentes-ia-y-practica-adaptativa-2026-11.md"
aliases: [Anki, FSRS, SM-2, SuperMemo, Math Academy, Khan Academy, herramientas de repaso espaciado]
creado: 2026-11-27
revisado: 2026-11-27
---

# Herramientas de práctica adaptativa

Ficha con las herramientas de práctica adaptativa verificadas al 2026-11-27: Anki y sus algoritmos SM-2 y FSRS, con sus valores por defecto y el benchmark público, Math Academy y Khan Academy.

Implementan el [repaso espaciado con software](repaso-espaciado-con-software.md) y los [sistemas adaptativos](sistemas-adaptativos.md).

Copiado de las páginas oficiales y del manual de Anki el 2026-11-27 y re-verificado el mismo día. Lo que dice cada proveedor sobre sí mismo no es evidencia de aprendizaje. Re-verificar cada tres meses.

## Anki

| Dato | Valor al 2026-11-27 |
|---|---|
| Qué es | Programa de tarjetas que, según su página, ayuda a dedicar más tiempo a lo difícil y menos a lo que ya se sabe |
| Versión | 26.09.4 (2026-11-04); hay una beta 26.11b1 (2026-11-12) |
| Plataformas | Escritorio gratis (Windows, macOS, Linux); AnkiDroid gratis en Android; AnkiMobile de pago en iOS (USD 24,99 en el App Store de EE.UU.); sincronización AnkiWeb gratis |
| Algoritmo original | Derivado de SuperMemo 2 (SM-2), con cambios: pasos de aprendizaje configurables, cuatro botones, «Eases will never be decreased below 130%» |
| Algoritmo FSRS | Basado en el modelo de tres componentes de la memoria (retrievability, stability, difficulty: cuán probable es recordar la tarjeta hoy, cuánto dura en memoria y cuán difícil es), que el proyecto FSRS atribuye a Piotr Woźniak. Woźniak creó SuperMemo: «I wrote the first SuperMemo program in December 1987». FSRS ajusta sus parámetros con el historial y está disponible desde Anki 23.10. Anki 26.09 actualizó su biblioteca FSRS a la 6.6.2 |
| Retención deseada por defecto | 90 %, «a good balance»; más del 97 % sobrecarga de repasos |
| Datos que necesita el ajuste | «Several reviews»; con «less than a few hundred» repasos, causa común de mal rendimiento |
| FSRS frente a SM-2, según el manual | «With FSRS, users have to do fewer reviews than with Anki's default algorithm to achieve the same retention level»; pruebas preliminares lo ubican «roughly on par» con SM-17, el algoritmo propietario de SuperMemo |

> [!WARNING] Obsoleto desde 2026-11: esta ficha citaba que FSRS «reportedly requires fewer reviews than SM-2». La página del manual leída el 2026-11-27 ya no tiene ese «reportedly» y lo afirma sin matiz (fila de arriba).

## Benchmark de algoritmos de repaso

La comparación pública de la comunidad de FSRS usa 9.999 colecciones de Anki y 349.923.850 repasos, y mide qué tan bien predice cada algoritmo si se va a recordar una tarjeta (RMSE, log loss y AUC). FSRS-6 supera a SM-2 en log loss en el 99,6 % de los usuarios. El autor advierte: «There is no way to have a truly fair, no caveats, comparison». SM-2 no fue diseñado para dar probabilidades y se le agregó un conversor. Mide predicción del olvido, no aprendizaje.

Al 2026-11-27, la versión más nueva es FSRS-7, con 34 parámetros, y la página del benchmark dice: «FSRS-7 is the final version, there will be no major releases in the foreseeable future». Las cifras de FSRS-7 están en el README del repositorio del benchmark, actualizado el 2026-11-19. Las notas de versión de Anki no mencionan FSRS-7.

Un promedio móvil sin parámetros (MOVING-AVG, que sube su predicción si los últimos repasos salieron bien y la baja si fallaron) queda casi igual que FSRS-7 en log loss y RMSE cuando no se cuentan los repasos del mismo día. Su log loss es 0,3369, contra 0,3370 de FSRS-7 con peso de lo reciente y 0,3401 de FSRS-7 base; su RMSE, 0,05915, contra 0,0634 de FSRS-7 base. En AUC queda atrás (0,7001 contra 0,7220), y cuando se cuentan los repasos del mismo día pierde también en log loss (0,3301 contra 0,3178). Como lectura de esta base, el olvido de una persona se predice bastante bien con su historial reciente, y la ventaja de un modelo de la memoria sobre una regla simple es chica en predicción.

## Math Academy

Plataforma paga de matemática: USD 49 por mes por alumno al 2026-11-27, presentado como precio de la etapa beta («JOIN BETA Only $49/mo per student»). No ofrece prueba gratis y devuelve el pago si se cancela en los primeros 30 días. Según su página, arranca con un diagnóstico adaptativo, arma un grafo de conocimiento por alumno y programa repasos; cita práctica distribuida, intercalado, efecto de testeo y ejemplos resueltos, sin estudios ni datos de resultados. Implementa el repaso jerárquico de Skycak descrito en [sistemas adaptativos](sistemas-adaptativos.md). El autor dice que no hay estudios académicos del sistema. Cómo infiere el diagnóstico lo que sabe cada alumno, y las dos versiones sobre cuánto dura, están en la ficha de [sistemas de diagnóstico adaptativo](../../Evaluacion-educativa/Evaluacion-adaptativa/sistemas-de-diagnostico-adaptativo.md).

## Khan Academy

Plataforma de práctica de matemática escolar. Su tutor con IA, Khanmigo, está en la ficha de [modos de estudio de la IA](../IA-en-la-educacion/modos-de-estudio-de-la-ia.md). En el ensayo de Oreopoulos y Low (NBER, 2026, sin revisión por pares), el efecto del tutor fue parecido al de la práctica de Khan Academy sin IA, según su resumen.
