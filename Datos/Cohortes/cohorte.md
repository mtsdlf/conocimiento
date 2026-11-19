---
resumen: >-
  Una cohorte es un grupo de personas (usuarios, clientes) que comparten un evento de entrada
  en el mismo período, como registrarse la misma semana, y que se sigue junto a lo largo del
  tiempo.
estado: borrador
estabilidad: estable
creado: 2026-10-03
fuentes:
  - https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section7.html
  - http://www.brucehardie.com/notes/033/what_is_wrong_with_this_CLV_formula.pdf
  - https://www.publichealth.columbia.edu/research/population-health-methods/age-period-cohort-analysis
  - https://docs.mixpanel.com/docs/users/cohorts
  - https://support.google.com/analytics/answer/9670133?hl=en
aliases: [cohort, cohortes]
---

# Cohorte

Una cohorte es un grupo de personas (usuarios, clientes) que comparten un evento de entrada
en el mismo período, como registrarse la misma semana, y que se sigue junto a lo largo del
tiempo.

## Separar antigüedad de calendario

Comparar grupos que empezaron en el mismo momento separa el efecto de la antigüedad (cuánto
hace que alguien llegó) del efecto del calendario (qué pasaba en el negocio ese mes). Un
promedio de toda la base mezcla usuarios nuevos con veteranos y esconde esos cambios. Comparar cohortes entre sí a la
misma edad es el [análisis de cohortes](analisis-de-cohortes.md).

## Evento de entrada y ventana

Una cohorte se define con dos cosas: el evento de entrada (registrarse, hacer la primera compra,
usar una función) y la ventana en que ocurrió (un día, una semana, un mes). Quien cumple ambas
entra a la cohorte y queda ahí: la membresía no cambia con lo que haga después. Sobre ese grupo
fijo se mide qué pasa en cada período contado desde la entrada (semana 0, 1, 2…). Según el
evento de entrada, es una [cohorte de adquisición](cohorte-de-adquisicion.md) o una
[cohorte de comportamiento](cohorte-de-comportamiento.md).

El término viene de la demografía y la epidemiología, donde una cohorte es, por ejemplo, la
gente nacida el mismo año.

## La cohorte del 1 al 7 de septiembre

Los usuarios que se registraron entre el 1 y el 7 de septiembre de 2026 forman una cohorte de
1.200 personas. Ocho semanas después siguen siendo esas 1.200, aunque solo 300 estén activas.

## Cohorte y segmento

Un **segmento** agrupa por un atributo en el momento de la consulta (país, plan, dispositivo), y
su membresía cambia cuando cambia el atributo. Una cohorte queda fija por su evento y su fecha de
entrada. Los dos se combinan: "cohorte de septiembre, segmento plan pago".

En Mixpanel, "cohort" nombra cualquier grupo guardado, incluso uno por atributo que se recalcula
en cada consulta: en los términos de esta nota, un segmento.
