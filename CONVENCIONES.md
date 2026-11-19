# Convenciones de esta base

Lo propio de esta base para la skill `documentar` (the-software-co/skills). El método general
está en la skill; esto lo completa.

- **Base**: la raíz de este repo, compartida por Matias y Fer. La entrada raíz es `conocimiento.md`, y la
  entrada de cada Tema y de cada vertical se llama como su carpeta (`<Tema>/<tema>.md`). Los enlaces van como Markdown relativo
  (`[texto](../Datos/cohorte.md)`), que se leen en GitHub y en cualquier editor. Nació como
  vault de Obsidian y se pasó a Markdown común en 2026-11.
- **Temas**: se estructuran por capas (el todo, las verticales como carpetas, los componentes y lo
  operativo), como dice el método de la skill. Los arma el modo `nuevo`, con su `ALCANCE.md` y sus
  informes crudos en `<Tema>/.investigacion/`. `Marketing/` es el primero con esta forma; los temas
  anteriores se pasan con el modo `existente` cuando se los toque.
- **Dueños**: `matias` por defecto; una nota lleva `dueno` solo si es de `fer` o de `familia`.
- **Apuntes personales**: quedan en la carpeta de cada Persona (p. ej. `Fer/Estudio/`) y se citan
  en `fuentes`.
- **Archivo**: los originales que se reemplazan van a `Archivo/<Tema>/`, en la raíz del Vault.
- **Volcar desde el Marco**: cuando el volcado sale de una Idea Clarificada como Conocimiento en
  la Revisión semanal, la ruta de la nota principal, relativa al Vault (p. ej.
  `Conocimiento/Datos/cohorte.md`), es la que va en `nota_vault` del Clarificar.
- **Conocimiento de un Sistema o una Iniciativa**: va a los docs de su repo (Espacio de trabajo),
  no acá.
- **Nunca**: secretos (van a Vaultwarden) ni lo confidencial de un empleador (queda en sus
  herramientas, con un enlace).
