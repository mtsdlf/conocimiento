---
tipo: ficha
area: referencia
resumen: >-
  Valores de referencia del gecko leopardo (temperaturas, humedad, luz, frecuencia de comida, pesos, tamaños y recinto), cada uno con su fuente y su desacuerdo; para varios no hay fuente primaria todavía y queda dicho.
estabilidad: semi
dueno: matias
estado: borrador
responde: [P18]
es_un: []
parte_de: []
instancia_de: []
requiere: [termorregulacion-conductual]
relacionado: []
fuentes:
  - https://www.merckvetmanual.com/multimedia/table/important-husbandry-requirements-for-selected-reptiles
  - https://www.msdvetmanual.com/exotic-and-laboratory-animals/reptiles/management-and-husbandry-of-reptiles
  - https://www.merckvetmanual.com/management-and-nutrition/nutrition-exotic-and-zoo-animals/nutrition-in-lizards
  - https://www.rspca.org.uk/adviceandwelfare/pets/other/leopardgecko
  - https://edepot.wur.nl/531850
  - https://jzar.org/jzar/article/download/150/89
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC7213736
  - https://biomechanics.ucr.edu/Jagnandan_etal_2014.pdf
  - https://web.natur.cuni.cz/~kratoch1/_private/BJLS.pdf
  - https://animaldiversity.org/accounts/Eublepharis_macularius
  - https://www.reptifiles.com/leopard-gecko-care/leopard-gecko-enclosure-size/
aliases: [tabla de valores, parámetros, números del cuidado]
creado: 2026-11-11
revisado:
autoria: ia
idioma: es
---

# Valores de referencia

Valores de referencia del gecko leopardo (temperaturas, humedad, luz, frecuencia de comida, pesos, tamaños y recinto), cada uno con su fuente y su desacuerdo; para varios no hay fuente primaria todavía y queda dicho.

Copiado de las fuentes del frontmatter el 2026-11-11, con las unidades de cada fuente. Los valores salen de manuales, una ONG de bienestar y estudios de laboratorio; ninguno es una prescripción. La base no es consejo veterinario, y vale para los valores de salud de esta ficha. El modelo detrás de los números está en [[termorregulacion-conductual|termorregulacion-conductual]]: el animal elige entre temperaturas, así que los valores describen un rango y no un punto.

## Temperatura

| Parámetro | Valor | Fuente | Nota |
|---|---|---|---|
| Zona óptima preferida (aire) | 25–30 °C | Merck, tabla de husbandry | Gradientes de aire |
| Punto de asoleo | 5 °C más que la zona óptima | Merck | Con 25–30 °C implica unos 30–35 °C; es cuenta del informe, Merck no lo escribe |
| Noche | 5 °C menos | Merck | No coincide con UV-Tool (aire nocturno 15–20 °C) ni con el umbral de 18 °C ambiente de la RSPCA para sumar calor; ninguna fuente lo concilia |
| Zona caliente / extremo frío | 28–30 °C / 24–26 °C | RSPCA | Bajo 18 °C ambiente, calor suplementario |
| Sobre la malla / extremo frío | 26–30 °C / 20–21 °C | Vet Times 2011 | El extremo frío difiere de la RSPCA (24–26 °C); ninguna de las dos lo justifica con datos |
| Superficie de asoleo, aire diurno, aire nocturno | 32 °C, 25–29 °C, 15–20 °C | UV-Tool (tabla de zoológicos) | Hay otras columnas de invierno sin desglosar |
| Superficie medida con manta a 32 °C | 33,0 ± 1,1 °C atrás, 29,9 al centro, 29,8 adelante | Oonincx 2020 | Crías de 6 meses |
| Zona caliente / lado frío según criadores | 90–95 °F / 72–77 °F | ReptiFiles | Secundaria, sin estudios |

> [!IMPORTANT]
> Disputado: el punto caliente. RSPCA propone 28–30 °C y Merck una zona óptima de 25–30 °C con el asoleo 5 °C más arriba. ReptiFiles propone 90–95 °F (unos 32–35 °C). El estudio de Oonincx midió 33,0 °C en superficie, con termostato a 32 °C. Nadie probó un máximo de seguridad, y esa temperatura máxima descansa en dos fuentes que no la ensayaron como límite. Detalle en [[temperatura-del-punto-caliente|temperatura-del-punto-caliente]].

Otras guías de comercio, vistas solo en resúmenes de buscador, dan 88–95 °F, 90–92 °F y hasta 90–100 °F (35–38 °C); este último está por encima de lo que respaldan Merck y el estudio, y no se toma como valor. Una guía advierte que 94–95 °F o más es peligroso.

**Temperatura corporal preferida medida**: dos cifras de protocolos distintos, vistas en resúmenes. Werner y colaboradores (2005) midieron unos 25,8 °C en un gradiente que combina calor y contacto; Autumn y DeNardo (1995) usaron unos 30 °C en un experimento de crecimiento, donde los animales que podían termorregular crecieron 0,16 g/día contra 0,11 g/día a 25 °C constantes. No hay una única temperatura preferida consensuada: se cita el rango con el protocolo de cada fuente.

## Humedad

| Parámetro | Valor | Fuente |
|---|---|---|
| Humedad ambiente | 20–30 %, con "substantially greater" durante la muda | Merck, tabla de husbandry |
| Humedad ambiente según criadores | 30–40 % | ReptiFiles |

> [!NOTE]
> Sin fuente todavía: la humedad de la cueva húmeda (en guías ronda 70 %). El estudio de Oonincx incluyó un refugio con arena húmeda pero no midió su humedad. Cómo se aplica está en [[humedad-localizada|humedad-localizada]].

## Luz

| Parámetro | Valor | Fuente |
|---|---|---|
| UVI en zona caliente / en sombra | 0,7 / 0 | RSPCA |
| UVI usado en crías, 2 h por día | 1,0 a 1,6 (33–51 µW/cm²) | Oonincx 2020 |
| Iluminación especial | "NS" (sin requisitos especiales); luz de amplio espectro recomendada | Merck |

El desacuerdo sobre si hace falta UVB está en [[uvb-si-o-no|uvb-si-o-no]].

> [!NOTE]
> Sin fuente todavía: fotoperíodo recomendado. Un estudio usó 12:12 y otro 12/12, pero como diseño experimental, no como recomendación.

## Comida

| Parámetro | Valor | Fuente |
|---|---|---|
| Frecuencia | Juveniles a diario, adultos día por medio | RSPCA |
| Lagartos chicos y jóvenes | A diario o al menos día por medio | Merck, nutrición en lagartos (pauta genérica) |
| Ejemplo medido | Larvas al 5 % del peso corporal, tres veces por semana, machos adultos; comieron unos 2,74 % del peso por comida | Boykin et al. 2020 |

> [!NOTE]
> Sin fuente todavía: calendario de comidas por edad y cantidades. Las frecuencias para adultos de cada 2 a 4 días y las cantidades salen solo de fichas comerciales. Ver [[alimentar-y-suplementar|alimentar-y-suplementar]].

## Pesos y tamaños

| Parámetro | Valor | Fuente | Nota |
|---|---|---|---|
| Peso al nacer | 3,2 ± 0,54 g y 3,3 ± 0,48 g | Oonincx 2020 | Dos grupos |
| Peso a los 175 días | 52,0 ± 6,81 g y 59,6 ± 12,36 g | Oonincx 2020 | Alimentación ad libitum: techo de crecimiento, no lo esperable |
| Hembras adultas | 39,4 ± 1,2 g | Jagnandan et al. 2014 | n = 7 |
| Machos adultos | 50,7 ± 11,5 g (peso inicial) | Boykin et al. 2020 | |
| Largo total | Crías unos 85 mm, adultos unos 220 mm | Animal Diversity Web | |
| Largo hocico-cloaca máximo medido | 137,8 mm machos, 128,7 mm hembras | Kratochvíl y Frynta 2002 | Crecimiento asintótico |

> [!NOTE]
> Sin fuente todavía: una curva de peso por edad de fuente veterinaria o institucional. Las tablas por edad halladas son de sitios de mascotas y no se usan. Contexto en [[crecimiento-del-gecko|crecimiento]].

## Recinto

| Parámetro | Valor | Fuente |
|---|---|---|
| Mínimo para un adulto | 60 cm de largo, 40 de alto, 30 de fondo; "Larger is better" | RSPCA |
| Lagartos terrestres en general | "0.2 m2/0.1 m total length" | Merck |
| Según criadores | 36 × 18 × 18 pulgadas y al menos 4,5 sq ft de piso | ReptiFiles |

> [!IMPORTANT]
> Disputado: el tamaño mínimo. La RSPCA fija 60 × 30 cm de base; ReptiFiles, unos 91 × 46 cm, y rechaza los 10 o 20 galones de otras guías sin citar estudios. Ninguna fuente primaria justifica un mínimo con datos propios. Ver [[armar-el-terrario|armar-el-terrario]].

## Relaciones

- Requiere: [[termorregulacion-conductual|termorregulacion-conductual]] — los valores de temperatura describen el rango entre el que el animal elige.
