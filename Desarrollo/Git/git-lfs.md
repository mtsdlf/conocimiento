---
tipo: concepto
resumen: >-
  Git LFS (Large File Storage) es una extensión de Git que guarda los archivos grandes fuera del
  repositorio y deja en su lugar un archivo puntero chico, versionado como cualquier otro.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Git LFS: https://git-lfs.com/"
  - "git-lfs, documentación de git-lfs-track, git-lfs-lock y git-lfs-migrate: https://github.com/git-lfs/git-lfs/tree/main/docs/man"
  - "Archivo/DevOps/git/git-scaling-performance.md y git-advanced-collaboration.md (originales, texto generado con IA)"
aliases: [LFS, Large File Storage, git lfs track, Archivos grandes en Git]
parte_de: []
requiere: [modelo-de-objetos-de-git]
relacionado: [git-en-repositorios-grandes]
---

# Git LFS

Git LFS (Large File Storage) es una extensión de Git que guarda los archivos grandes fuera del
repositorio y deja en su lugar un archivo puntero chico, versionado como cualquier otro.

## Por qué importa

Git guarda cada versión de cada archivo para siempre (ver [Modelo de objetos de Git](modelo-de-objetos-de-git.md)). Un
`.psd` de 200 MB editado diez veces suma unos 2 GB al historial, y todo clon los descarga, aunque
solo necesite la última versión. Los binarios casi no se comprimen por deltas, así que el
repositorio crece con cada cambio.

## Cómo funciona

- `git lfs install` registra los filtros de LFS en la configuración global de Git, una vez por
  usuario.
- `git lfs track "*.psd"` agrega un patrón a `.gitattributes`. Ese archivo se versiona, para que
  todo el equipo use LFS con los mismos patrones.
- Al agregar un archivo que coincide, el filtro lo sube a un almacenamiento LFS y guarda en Git un
  **puntero** de tres líneas: versión del formato, hash SHA-256 del contenido y tamaño.
- Al hacer checkout, el filtro baja el contenido real de las versiones que se usan. Las versiones
  viejas quedan en el servidor y no se descargan.

El servidor tiene que soportar LFS: GitHub, GitLab, Bitbucket y Azure Repos lo hacen, con cuotas
de almacenamiento y de transferencia aparte.

**Bloqueo**: los binarios no se pueden combinar en un merge. `git lfs lock archivo.psd` marca el
archivo como bloqueado en el servidor, para que nadie más lo edite en paralelo, y `git lfs unlock`
lo libera.

**Migrar un repo existente**: `git lfs track` solo afecta a lo que se agrega desde ese momento.
Para mover archivos que ya están en el historial, `git lfs migrate import --include="*.psd"`
reescribe los commits del branch actual (con `--everything`, los de todos los branches y tags), con las mismas consecuencias que un [Rebase](rebase.md) sobre branches compartidos.

## Ejemplo

```bash
git lfs install
git lfs track "*.psd" "*.mp4"
git add .gitattributes diseno/portada.psd
git commit -m "Agrega la portada en LFS"
```

`git lfs ls-files` lista los archivos que quedaron como punteros.

## No confundir con

Un repositorio de artefactos (Nexus, Artifactory, un bucket). LFS versiona archivos fuente que
cambian junto con el código, como diseños o datos de prueba; los binarios que produce el build
(jars, imágenes de contenedor) van a un repositorio de artefactos, no a Git.

## Relaciones

- Requiere: [Modelo de objetos de Git](modelo-de-objetos-de-git.md) — explica por qué un binario grande pesa en cada clon.
- Relacionado: [Git en repositorios grandes](git-en-repositorios-grandes.md) — LFS es una de las técnicas para que un repositorio grande siga siendo usable.
