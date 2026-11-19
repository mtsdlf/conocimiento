---
tipo: concepto
resumen: >-
  RDFS y OWL son lenguajes del W3C para describir un dominio (clases, propiedades, restricciones)
  de los que un reasoner deriva hechos implícitos y detecta inconsistencias; OWL asume mundo
  abierto.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://www.w3.org/TR/rdf11-mt/
  - https://www.w3.org/TR/owl2-primer/
  - https://www.w3.org/TR/shacl/
  - https://github.com/mtsdlf/investments-strategist/blob/main/docs/research/prosa-como-software.md
aliases: [RDFS, OWL, OWL 2, reasoner, razonador, ontología, inferencia semántica]
parte_de: [conceptos-ia]
requiere: []
relacionado: []
---

# Inferencia en RDFS y OWL

RDFS y OWL son lenguajes del W3C para describir un dominio (clases, propiedades, restricciones)
de los que un reasoner deriva hechos implícitos y detecta inconsistencias; OWL asume mundo
abierto.

## Por qué importa

Lo que un sistema sabe de su dominio suele estar disperso en prosa y en código. Escrito como
ontología, un **reasoner** (un programa genérico de deducción lógica) calcula sus consecuencias y avisa cuando un
conjunto de afirmaciones no puede ser verdadero a la vez.

## Cómo funciona

**RDFS** agrega reglas simples sobre datos RDF, que son tripletas sujeto–propiedad–objeto.
Según la semántica de RDF 1.1:

- si `perro subClassOf mamífero` y `rex type perro`, entonces `rex type mamífero`;
- `subClassOf` es transitiva;
- si una propiedad declara `domain`, el sujeto de cada tripleta recibe ese tipo; si declara
  `range`, lo recibe el objeto.

RDFS casi no detecta contradicciones: su caso típico es un valor que choca con el tipo de dato
declarado.

**OWL 2** suma clases disjuntas, cardinalidades ("a lo sumo cuatro hijos") y equivalencias. Con
eso un reasoner encuentra **inconsistencias**: según el OWL 2 Primer, un conjunto de
afirmaciones es consistente si existe un estado del mundo donde todas son verdaderas. Dos
supuestos cambian lo que se puede chequear:

- **Mundo abierto**: un dato ausente puede ser verdadero; no se lo toma como falso.
- **Sin nombres únicos**: dos nombres pueden ser el mismo individuo.

Por eso OWL no sirve para exigir "todo pedido tiene cliente": sin el dato, el reasoner supone que
el cliente existe y no está escrito.

## Ejemplo

Una ontología declara `Bono subClassOf RentaFija` y `RentaFija disjointWith Accion`. Con
`X type Bono`, el reasoner deduce `X type RentaFija`. Si además alguien afirma `X type Accion`,
el reasoner informa una inconsistencia.

En el repo investments-strategist se evaluó esta técnica para chequear los 71 criterios de su
estrategia, y se descartó. Solo 4 criterios trataban sobre las tablas de datos; los defectos
encontrados eran de forma del dato y de verdad del mensaje que imprime el programa, de los que
ninguno de los tres (SHACL, RDFS, OWL) habla. Además, OWL es de mundo abierto y sumaba dependencias.

## No confundir con

**SHACL** (W3C, 2017) valida un grafo RDF contra "formas" (shapes: condiciones que deben
cumplir los nodos, como "tiene exactamente un cliente") y produce un reporte. Su uso típico
es de mundo cerrado: lo que falta es una violación. OWL infiere; SHACL chequea.

## Relaciones

- Parte de: [IA](conceptos-ia.md) — Mapa del Tema IA.
- La usa: [El LLM emite, el reasoner verifica](llm-emite-reasoner-verifica.md) — el reasoner que verifica lo que emite un LLM.
