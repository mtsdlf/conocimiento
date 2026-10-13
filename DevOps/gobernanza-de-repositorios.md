---
tipo: concepto
resumen: >-
  La gobernanza de un repositorio son las reglas automáticas sobre quién cambia qué: ramas
  protegidas, checks obligatorios, CODEOWNERS, revisión de PRs y roles, con la idea de que las
  personas deciden y los bots ejecutan.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "GitHub Docs, About protected branches: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches"
  - "GitHub Docs, About rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets"
  - "GitHub Docs, About code owners: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-mastery-workflows.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-advanced-collaboration.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-organizational-topology.md (original, texto generado con IA)"
aliases: [Repository governance, Branch protection, Protección de ramas, CODEOWNERS]
parte_de: []
requiere: []
relacionado: [estrategia-de-branching, conventional-commits, trazabilidad-de-cambios]
---

# Gobernanza de repositorios

La gobernanza de un repositorio son las reglas automáticas sobre quién cambia qué: ramas
protegidas, checks obligatorios, CODEOWNERS, revisión de PRs y roles, con la idea de que las
personas deciden y los bots ejecutan.

## Por qué importa

Sin reglas, cualquiera puede empujar a `main` un cambio sin revisar ni probar. Con reglas
aplicadas por la plataforma, un cambio solo llega a la rama principal con revisión y CI en verde,
y eso queda registrado. Las reglas automáticas permiten mergear rápido sin depender de que
alguien se acuerde de controlar.

## Cómo funciona

- **Ramas protegidas**: en GitHub, una regla sobre `main` puede exigir PR con aprobaciones,
  status checks en verde (los resultados que el CI reporta sobre el commit), conversaciones
  resueltas, commits firmados, historial lineal o merge queue (una fila que prueba cada PR sobre
  lo ya mergeado; ver [[integracion-continua]]). También puede bloquear el force push, que
  reescribe el historial remoto, y el borrado. Los **rulesets** hacen lo mismo con más
  flexibilidad: varios se aplican a la misma rama, y si dos chocan rige el más restrictivo;
  cubren también tags y se desactivan sin borrarlos.
- **CODEOWNERS**: un archivo en `.github/`, en la raíz o en `docs/` asigna dueños por ruta. GitHub
  les pide revisión cuando un PR toca sus archivos, y una regla puede exigir su aprobación. Si
  varias líneas coinciden, gana la última.
- **Roles**: quien contribuye abre PRs; quien es dueño aprueba; quien mantiene mergea y
  administra. Los bots (CI, releases) usan credenciales con el mínimo permiso y son los únicos
  que crean tags de release.
- **Higiene de ramas**: nombres con prefijo y ticket (`feature/ABC-123-login`), borrado al
  mergear y un bot que cierra ramas viejas.

La firma se exige con la regla de commits firmados del proveedor o con un hook `pre-receive` en
un servidor propio; `[receive] rejectUnsigned` no es una opción de configuración de Git.

## Ejemplo

En un repo de un servicio, `main` exige un PR con una aprobación de CODEOWNERS, los checks
`build` y `test` en verde, y no admite force push. La regla `*.tf @equipo-plataforma` hace que
todo cambio de Terraform pase por el equipo de plataforma.

## No confundir con

La [[gobernanza-de-plataforma]], que aplica políticas a lo que se pide a la plataforma interna
(recursos, costos, permisos). La gobernanza de repositorios regula cambios de código.

## Relaciones

- Relacionado: [[estrategia-de-branching]] — define las ramas que estas reglas protegen.
- Relacionado: [[conventional-commits]] — el formato del mensaje se exige como check.
- Relacionado: [[trazabilidad-de-cambios]] — las aprobaciones y checks son la evidencia de auditoría.
- Ver también: [[gobernanza-de-plataforma]] — la misma idea aplicada a la plataforma interna.
