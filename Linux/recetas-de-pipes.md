---
resumen: >-
  Combinaciones de pipes y redirecciones listas para usar: contar IPs en un log, sumar una columna
  de un CSV, separar salida y errores, renombrar en lote.
estado: borrador
estabilidad: estable
fuentes:
  - "Original reemplazado: nota linux-pipes-unix (secciones C y D), borrada al migrar; la receta de renombrado se corrigió"
  - "Bash Reference Manual, Process Substitution: https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html"
aliases: [Recetas de bash, One-liners de Linux]
creado: 2026-10-03
revisado:
---

# Recetas de pipes

Combinaciones de pipes y redirecciones listas para usar: contar IPs en un log, sumar una columna
de un CSV, separar salida y errores, renombrar en lote.

## De dónde salen

Recetas propias; cada comando se documenta en su página de manual (`man awk`, `man sort`). La
sintaxis de pipes y redirecciones está en [Pipe y redirección](pipe-y-redireccion.md).

## Las recetas

### IPs con más errores en un log de acceso

Las 10 IPs que más respuestas 5xx recibieron en un log de Apache o nginx (formato combinado, el
código de estado es el campo 9):

```bash
awk '$9 >= 500 {print $1}' /var/log/apache2/access.log | sort | uniq -c | sort -nr | head -10
```

`awk` deja la IP de las líneas con error, `sort | uniq -c` cuenta cada IP, `sort -nr` ordena de
mayor a menor y `head` corta en 10.

### Valores que se repiten más de 10 veces

```bash
cut -d' ' -f2 archivo.log | sort | uniq -c | sort -nr | awk '$1 > 10'
```

### Los 5 scripts más grandes del home, en MB

```bash
find ~ -type f -name '*.sh' -printf '%s\t%p\n' | sort -nr | head -5 | awk -F'\t' '{printf "%s\t%.2f MB\n", $2, $1/1024/1024}'
```

### Las 20 líneas con FAIL más largas, con errores aparte

```bash
find . -type f -name '*.log' -print0 | xargs -0 grep -H 'FAIL' 2> errores.txt | awk '{print length, $0}' | sort -nr | cut -d' ' -f2- | head -20 > fails_largos.txt
```

`-print0` y `xargs -0` aguantan nombres de archivo con espacios; `-H` antepone siempre el nombre
del archivo, aunque haya uno solo.

### Sumar una columna de un CSV con condición

Suma la columna 3 de las filas cuya columna 4 es `OK`, salteando la cabecera:

```bash
tail -n +2 archivo.csv | awk -F, '$4 == "OK" {sum += $3} END {print sum}'
```

### Guardar salida y errores en archivos separados y verlos en pantalla

```bash
comando > >(tee salida.txt) 2> >(tee errores.txt >&2)
```

Cada `>(tee …)` es una sustitución de procesos: `tee` escribe a su archivo y repite en pantalla;
`>&2` devuelve los errores a stderr.

### Renombrar a minúsculas y dejar registro

```bash
for i in *.JPG; do mv -v -- "$i" "$(printf '%s' "$i" | tr 'A-Z' 'a-z')"; done | tee cambios.log
```

`mv` no imprime nada por defecto: sin `-v`, `cambios.log` queda vacío. Las comillas en `"$i"`
evitan que un nombre con espacios se parta en dos.

### La última línea de cada archivo

```bash
for f in *.txt; do tail -n 1 "$f"; done
```

### Mensaje según si un comando encontró algo

```bash
grep -q 'algo' archivo && echo 'Encontrado' || echo 'No encontrado'
```

Si `archivo` no existe, también dice "No encontrado": `grep` sale con error y `||` no distingue
el motivo.
