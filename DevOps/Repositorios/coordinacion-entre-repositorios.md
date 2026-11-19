---
resumen: >-
  En multirepo, la coordinación entre repositorios se hace con versiones fijadas, bots que
  actualizan dependencias, triggers entre repos y un release train o meta-repo que compone las
  versiones.
estado: borrador
estabilidad: estable
fuentes:
  - "Renovate Docs: https://docs.renovatebot.com/"
  - "GitHub Docs, About Dependabot version updates: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates"
  - "GitHub Docs, Create a repository dispatch event: https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event"
  - "Archivo/DevOps/git-ecosystem-multi-repo.md (original, texto generado con IA)"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
aliases: [Coordinación multirepo, Release train, Meta-repo]
creado: 2026-10-03
revisado:
---

# Coordinación entre repositorios

En multirepo, la coordinación entre repositorios se hace con versiones fijadas, bots que
actualizan dependencias, triggers entre repos y un release train o meta-repo que compone las
versiones.

## Qué se rompe sin coordinación

Cuando cada servicio y cada biblioteca vive en su repo, nada garantiza que las versiones encajen.
Sin coordinación aparecen dependencias desactualizadas, cambios incompatibles que se descubren en
producción y releases que nadie sabe con qué versiones se armaron.

## Versiones fijadas, bots, triggers y release train

- **Versiones fijadas**: cada repo depende de una versión exacta de otro, por tag de
  [Versionado semántico](../Ramas-y-versiones/versionado-semantico.md) o por SHA de commit, nunca de "la última".
- **Bots de actualización**: Renovate o Dependabot leen los manifiestos y abren un PR cuando sale
  una versión nueva. El CI de ese PR prueba la combinación antes de mergearla.
- **Triggers entre repos**: cuando un repo publica un artefacto, dispara el pipeline del repo que
  lo consume. En GitHub se hace con el evento `repository_dispatch`; en GitLab, con trigger jobs
  (un job de un pipeline que lanza el pipeline de otro proyecto).
- **Release train**: un repo central guarda un manifiesto con la versión de cada servicio que
  forma una release del producto. Publicar es actualizar ese manifiesto con un PR.
- **Repo de integración**: no guarda versiones; contiene las pruebas de punta a punta y las
  corre sobre la combinación que propone el manifiesto.
- **Meta-repo o catálogo**: no prueba nada; lista todos los repos con su dueño y sus
  dependencias. La
  automatización lo usa para saber qué clonar, y el catálogo de un [Developer portal](../../Platform-Engineering/Plataforma-interna/developer-portal.md) cumple la
  misma función con interfaz web.

## Un release train que sube facturación a 2.8.0

```yaml
# release-train/producto-2026-10.yaml
servicios:
  auth: 3.4.1
  facturacion: 2.7.0
  web: 8.2.0
```

Cuando `facturacion` publica `2.8.0`, Renovate abre un PR en el release train. El repo de
integración corre las pruebas con esa combinación y, si pasan, el PR se mergea y la release queda
registrada en Git.

## Coordinar versiones no es compartir el pipeline

Un [Pipeline reutilizable](../Integracion-y-entrega/pipeline-reutilizable.md): comparte la definición del pipeline entre repos, pero no coordina
qué versión de cada uno va con cuál.

## Ver también

- [Monorepo y multirepo](monorepo-y-multirepo.md) — esta coordinación es el costo de elegir multirepo.
