---
tipo: concepto
resumen: >-
  Policy as code es escribir las reglas de seguridad y cumplimiento como código, que se evalúa
  en el pipeline y en el clúster (OPA/Rego, Conftest, admission controllers).
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Open Policy Agent, documentación: https://www.openpolicyagent.org/docs/latest/"
  - "Conftest: https://www.conftest.dev/"
  - "OPA Gatekeeper: https://open-policy-agent.github.io/gatekeeper/website/docs/"
  - "Kubernetes, Admission Controllers: https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/"
  - "Archivo/DevOps/devsecops-pipeline-avanzado.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
aliases: [Políticas como código, PaC]
parte_de: [devsecops]
requiere: [devsecops]
relacionado: [seguridad-en-el-pipeline]
---

# Policy as code

Policy as code es escribir las reglas de seguridad y cumplimiento como código, que se evalúa
en el pipeline y en el clúster (OPA/Rego, Conftest, admission controllers).

## Por qué importa

Una regla escrita en un documento ("ningún contenedor corre como root") depende de que alguien
la recuerde en cada revisión. Escrita como código, se aplica igual a cada cambio, se versiona y
se revisa en un PR como cualquier otro código, y su historial muestra cuándo cambió la regla.

## Cómo funciona

**Open Policy Agent** (OPA, proyecto graduado de la CNCF) separa la decisión de su aplicación: el
sistema le pasa un JSON a OPA, OPA lo evalúa contra políticas escritas en **Rego** y devuelve la
decisión. El mismo motor sirve en dos momentos:

- **En el pipeline**: **Conftest** evalúa manifiestos de Kubernetes, planes de Terraform u otros
  archivos de configuración. Hace fallar el job si se cumple una regla `deny` o `violation`;
  una regla `warn` solo avisa.
- **En el clúster**: un **admission controller** intercepta cada pedido de crear o modificar un
  recurso, después de autenticarlo y antes de guardarlo. **OPA Gatekeeper** es un webhook de
  admisión que aplica políticas definidas como recursos de Kubernetes y además audita los
  recursos que ya existen. Un **ConstraintTemplate** define la lógica de la regla en Rego y sus
  parámetros. Un **Constraint** la aplica a un conjunto de recursos con valores concretos, por
  ejemplo "todo Namespace debe tener la etiqueta `owner`".

Evaluar en los dos lugares cubre los dos caminos: el pipeline da aviso temprano en el PR, y el
clúster rechaza lo que llegue por otro lado.

Es la herramienta con la que una plataforma da autonomía sin perder control, como describe
[Gobernanza de plataforma](../Platform-Engineering/gobernanza-de-plataforma.md); las reglas sobre el repositorio mismo están en
[Gobernanza de repositorios](gobernanza-de-repositorios.md).

## Ejemplo

Una política de Conftest que rechaza Deployments sin `runAsNonRoot`:

```rego
package main

deny contains msg if {
  input.kind == "Deployment"
  not input.spec.template.spec.securityContext.runAsNonRoot
  msg := "Los contenedores no deben correr como root"
}
```

`conftest test deployment.yaml` falla en el PR con ese mensaje, y Gatekeeper rechaza el mismo
Deployment si alguien lo aplica directo al clúster.

## No confundir con

**Escaneo de IaC con reglas predefinidas** (Checkov, Trivy): trae cientos de reglas genéricas
listas. Policy as code son las reglas propias de la organización, escritas por ella.

## Relaciones

- Parte de y requiere: [DevSecOps](devsecops.md) — es la forma de expresar los controles de DevSecOps.
- Relacionado: [Seguridad en el pipeline](seguridad-en-el-pipeline.md) — el policy gate del pipeline evalúa estas reglas.
- Ver también: [Gobernanza de plataforma](../Platform-Engineering/gobernanza-de-plataforma.md) — la autonomía con límites que estas reglas hacen cumplir.
- Ver también: [Gobernanza de repositorios](gobernanza-de-repositorios.md) — las reglas sobre quién cambia qué en un repositorio.
