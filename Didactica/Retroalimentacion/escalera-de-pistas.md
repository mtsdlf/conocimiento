---
resumen: >-
  La escalera de pistas es graduar la ayuda ante un error o un bloqueo: primero una pista general, después una más concreta y al final la solución. Es práctica común de tutores humanos y de sistemas de tutoría; no se encontró una revisión que la evalúe como técnica de aula.
estado: borrador
estabilidad: semi
fuentes:
  - "VanLehn (2011), The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems, Educational Psychologist 46(4), DOI 10.1080/00461520.2011.611369: https://eric.ed.gov/?id=EJ946764 (abstract)"
  - "Shih, Koedinger y Scheines (2008), EDM: https://www.cmu.edu/dietrich/philosophy/docs/scheines/Shih_Koedinger_Scheines_2008_EDM.pdf (resumen)"
  - "Lepper y Woolverton (2002), The wisdom of practice, en Aronson (ed.), Improving Academic Achievement (según un resumen secundario)"
  - "Chi, Siler, Jeong, Yamauchi y Hausmann (2001), Learning from human tutoring, Cognitive Science 25(4), DOI 10.1207/s15516709cog2504_1 (abstract)"
  - "Didactica/.investigacion/explicita-practica-preguntas-feedback.md"
  - "Didactica/.investigacion/indagacion-tutoria-especificas.md"
aliases: [escalera de pistas, pistas graduales, hint ladder, graduated hints, pista final, bottom-out hint, ayuda escalonada]
creado: 2026-11-27
revisado:
---

# Escalera de pistas

La escalera de pistas es graduar la ayuda ante un error o un bloqueo: primero una pista general, después una más concreta y al final la solución. Es práctica común de tutores humanos y de sistemas de tutoría; no se encontró una revisión que la evalúe como técnica de aula.

Es la tercera decisión de la [retroalimentación](retroalimentacion.md): cuánto decir. Se parece al [andamiaje](../Practica-guiada-y-andamiaje/andamiaje.md), pero en escala chica: el andamiaje se retira a lo largo de semanas, y la escalera se sube y se baja dentro de un mismo problema. Es la herramienta típica de la [tutoría](../Tutoria-y-mentoria/tutoria.md), donde quien enseña ve cada paso.

## Los escalones

Un ejemplo de escalera ante un programa que falla, ilustrativo y no de una fuente:

1. **Orientar.** «Algo pasa cuando la lista está vacía.»
2. **Señalar el lugar.** «Mirá qué devuelve la función en la línea del bucle si no entra nunca.»
3. **Nombrar la idea.** «Falta un valor inicial para el caso sin elementos.»
4. **Mostrar la solución**, y pedir que se explique.

Cada escalón da un poco más que el anterior. Se sube solo si el escalón anterior no alcanzó.

## Lo que hacen los tutores expertos

Según un resumen secundario del capítulo de Lepper y Woolverton (2002), los tutores expertos usan un enfoque predominantemente socrático, dan pistas graduales, dan retroalimentación indirecta para bajar la presión de sentirse evaluado, y equilibran la información con el apoyo emocional. No se verificó contra el capítulo.

El estudio de Chi et al. (2001) muestra hasta dónde puede llegar el primer escalón: con tutores que solo podían hacer preguntas guía, sin explicar ni corregir, los alumnos aprendieron igual que con tutores que explicaban. Los autores lo atribuyen a que quien aprende construye más y a más episodios de andamiaje.

## La última pista como ejemplo resuelto

El último escalón da la respuesta, y eso tiene un riesgo: quien aprende puede saltar los escalones para llegar a ella. Shih, Koedinger y Scheines (2008), con datos de un tutor por computadora, proponen que «bottom-out hints can act as worked examples»: la solución mostrada enseña si quien la recibe la lee y se la explica. Su modelo de tiempos de respuesta distingue ese buen uso del abuso. Por eso, después de mostrar la solución conviene pedir [autoexplicación](../Preguntas-y-dialogo/autoexplicacion.md).

> [!NOTE] Sin fuente todavía: si enseñar a pedir ayuda mejora el aprendizaje. Un trabajo que se cita sobre el tema (Aleven, Roll, McLaren y Koedinger 2016) no se verificó.

## Qué dice la tutoría por computadora sobre el grano de la ayuda

VanLehn (2011) clasificó los sistemas de tutoría por el tamaño del paso en que dan ayuda: por respuesta final, por paso o por subpaso. Se creía que la tutoría humana rendía d = 2,0 y los tutores inteligentes d = 1,0; su revisión encontró 0,79 para la tutoría humana y 0,76 para los tutores inteligentes, «nearly as effective as human tutoring». Según un resumen secundario, los sistemas que solo corrigen la respuesta final rinden bastante menos (0,31) y la efectividad deja de crecer al bajar del paso al subpaso. La lectura para una escalera de pistas, que es inferencia: ayudar paso a paso rinde más que corregir solo el resultado, pero no hace falta intervenir en cada microdecisión. Los tutores por computadora como sistema están en [Tecnología educativa](../../Tecnologia-educativa/tecnologia-educativa.md).

## Cuándo mostrar la solución

Ninguna fuente leída fija cuántos intentos esperar antes de mostrar. Dos líneas de evidencia tiran para lados distintos: la [falla productiva](../Aprendizaje-activo-e-indagacion/falla-productiva.md) sugiere dejar intentar antes de enseñar, y el metaanálisis de Alfieri et al. (2011) muestra que el descubrimiento sin ayuda pierde (ver [guía o descubrimiento](../Aprendizaje-activo-e-indagacion/guia-o-descubrimiento.md)). Las dos son compatibles: el momento de mostrar es una decisión de diseño que esta evidencia no define. Con quien ya sabe mucho, la [inversión de la experticia](../Practica-guiada-y-andamiaje/inversion-de-la-experticia.md) sugiere empezar más arriba en la escalera, con menos ayuda.
