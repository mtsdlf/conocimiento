---
resumen: >-
  Una cohorte de comportamiento agrupa a los usuarios por una acción que hicieron (o no
  hicieron) en un período, como usar una función en su primera semana, para comparar cómo se
  comportan después.
estado: borrador
estabilidad: estable
creado: 2026-10-03
fuentes:
  - https://amplitude.com/docs/analytics/behavioral-cohorts
  - https://docs.mixpanel.com/docs/users/cohorts
aliases: [behavioral cohort, cohorte conductual]
---

# Cohorte de comportamiento

Una cohorte de comportamiento agrupa a los usuarios por una acción que hicieron (o no
hicieron) en un período, como usar una función en su primera semana, para comparar cómo se
comportan después.

## Qué acciones tempranas van con quedarse

Muestra qué acciones tempranas van de la mano con quedarse. Si los que invitan a un compañero en
la primera semana retienen el doble, esa acción es candidata a empujarse en el onboarding.

## La acción, su ventana y la comparación

Es un tipo de [cohorte](cohorte.md), con una acción como evento de entrada. Se define la acción, su ventana (por ejemplo, "en los primeros 7 días desde el alta") y, a veces,
una cantidad mínima ("al menos 3 veces"). Después se compara la retención de quienes la hicieron
contra la de quienes no. La comparación se hace dentro de una misma
[cohorte de adquisición](cohorte-de-adquisicion.md), para no mezclar usuarios de épocas distintas.

## Crear un proyecto el primer día

De la cohorte de agosto, 400 usuarios crearon un proyecto en su primer día y 1.600 no. En la
semana 4 retienen 45 % y 18 %, respectivamente.

## Correlación, no causa

Una diferencia de retención entre los dos grupos es una correlación, no una causa: los que hacen
la acción pueden ser usuarios más motivados de entrada. Para afirmar que la acción causa la
retención hace falta un experimento, por ejemplo un test A/B que empuje la acción a la mitad de
los usuarios.
