---
tipo: concepto
resumen: >-
  Una cohorte de comportamiento agrupa a los usuarios por una acción que hicieron (o no
  hicieron) en un período, como usar una función en su primera semana, para comparar cómo se
  comportan después.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://amplitude.com/docs/analytics/behavioral-cohorts
  - https://docs.mixpanel.com/docs/users/cohorts
aliases: [behavioral cohort, cohorte conductual]
parte_de: [cohorte]
requiere: [cohorte]
relacionado: [cohorte-de-adquisicion]
---

# Cohorte de comportamiento

Una cohorte de comportamiento agrupa a los usuarios por una acción que hicieron (o no
hicieron) en un período, como usar una función en su primera semana, para comparar cómo se
comportan después.

## Por qué importa

Muestra qué acciones tempranas van de la mano con quedarse. Si los que invitan a un compañero en
la primera semana retienen el doble, esa acción es candidata a empujarse en el onboarding.

## Cómo funciona

Se define la acción, su ventana (por ejemplo, "en los primeros 7 días desde el alta") y, a veces,
una cantidad mínima ("al menos 3 veces"). Después se compara la retención de quienes la hicieron
contra la de quienes no. La comparación se hace dentro de una misma
[[cohorte-de-adquisicion|cohorte de adquisición]], para no mezclar usuarios de épocas distintas.

## Ejemplo

De la cohorte de agosto, 400 usuarios crearon un proyecto en su primer día y 1.600 no. En la
semana 4 retienen 45 % y 18 %, respectivamente.

## No confundir con

Una diferencia de retención entre los dos grupos es una correlación, no una causa: los que hacen
la acción pueden ser usuarios más motivados de entrada. Para afirmar que la acción causa la
retención hace falta un experimento, por ejemplo un test A/B que empuje la acción a la mitad de
los usuarios.

## Relaciones

- Parte de: [[cohorte]] — es un tipo de cohorte, con una acción como evento de entrada.
- Requiere: [[cohorte]] — define el evento de entrada y la ventana, que esta nota da por sabidos.
- Relacionado: [[cohorte-de-adquisicion]] — se cruza con ella para comparar dentro de la misma
  época.
