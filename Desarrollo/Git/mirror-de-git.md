---
resumen: >-
  Un mirror de Git es un clon bare que copia todas las refs del original (branches, tags, notas) y
  se sincroniza pisándolas; se usa como respaldo, como cache de CI o como réplica en otro
  servidor.
estado: borrador
estabilidad: estable
revisado:
creado: 2026-10-03
fuentes:
  - "Git Documentation, git-clone (--mirror): https://git-scm.com/docs/git-clone"
  - "Git Documentation, git-push (--mirror): https://git-scm.com/docs/git-push"
  - "Git Documentation, git-remote (update --prune): https://git-scm.com/docs/git-remote"
  - "Git Documentation, git-bundle: https://git-scm.com/docs/git-bundle"
  - "Git Documentation, git-fsck: https://git-scm.com/docs/git-fsck"
  - "Archivo/DevOps/git/git-scaling-performance.md (original, texto generado con IA)"
aliases: [Mirror, Espejo de Git, git clone --mirror, Respaldo de un repositorio Git, git bundle]
---

# Mirror de Git

Un mirror de Git es un clon bare que copia todas las refs del original (branches, tags, notas) y
se sincroniza pisándolas; se usa como respaldo, como cache de CI o como réplica en otro
servidor.

## Por qué un clon común no reconstruye el servidor

Un clon común trae los branches del remoto como `origin/*` y no copia todas las [refs](branch-git.md), así que no
sirve para reconstruir el servidor si se pierde. Un mirror sí: tiene exactamente las mismas refs
que el original. También baja la carga del servidor principal cuando muchos jobs de CI clonan el
mismo repositorio: es una de las formas de acelerar los clones en
[repositorios grandes](git-en-repositorios-grandes.md).

## Clon bare, push --mirror y bundles

`git clone --mirror <url>` crea un repositorio **bare** (sin directorio de trabajo) y configura un
refspec que mapea todas las refs del remoto a las mismas refs locales. Después,
`git remote update --prune` lo sincroniza: trae lo nuevo, pisa las refs que cambiaron y borra las
que ya no existen en el original.

En sentido contrario, `git push --mirror <destino>` hace que el destino tenga exactamente las refs
locales, borrando las que sobran. Así se replica un repositorio a otro servidor, por ejemplo al
migrar de GitLab a GitHub. Las plataformas rechazan las refs que administran ellas (en GitHub,
`refs/pull/*`), así que ese push puede terminar con errores en esas refs aunque el resto pase.

Un mirror no es un respaldo completo por sí solo: si alguien borra un branch o fuerza un push en
el original, la próxima sincronización copia el borrado. Para respaldo conviene además una
**instantánea** fechada:

- `git bundle create repo-2026-10-03.bundle --all` empaqueta todas las refs y objetos en un solo
  archivo, que se restaura con `git clone repo-2026-10-03.bundle` y se valida con
  `git bundle verify`, ejecutado dentro de un repositorio.
- `git fsck` verifica la integridad de los objetos del mirror o del clon restaurado.

Un mirror o un bundle es la última fuente para
[recuperar un commit perdido](recuperar-trabajo-perdido-en-git.md).

Los mirrors no copian lo que la plataforma guarda fuera de Git: issues, PRs, wikis en otro
almacenamiento, configuración de protección de ramas.

## Un job nocturno y los runners de CI

Un job nocturno actualiza un mirror y guarda un bundle con la fecha:

```bash
git -C /respaldos/catalogo.git remote update --prune
git -C /respaldos/catalogo.git bundle create /respaldos/catalogo-$(date +%F).bundle --all
```

Los runners de CI clonan con `git clone --reference /respaldos/catalogo.git --dissociate <url>`:
reutilizan los objetos del mirror y descargan solo lo que falta. Sin `--dissociate`, el clon
queda dependiendo del mirror, y se rompe si el mirror borra objetos en un `gc`.

## Mirror y fork

Un fork. El fork es una copia en la plataforma que diverge a propósito y recibe trabajo propio; el
mirror no recibe commits directos y solo sigue al original.
