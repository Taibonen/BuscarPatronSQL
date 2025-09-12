
# BuscarPatronSQL

Este script permite buscar patrones definidos mediante expresiones regulares en archivos `.sql` dentro de un directorio. Es ideal para localizar instrucciones específicas en scripts SQL, con la opción de ignorar coincidencias dentro de comentarios.

## 🚀 Características
- Búsqueda por expresiones regulares.
- Recorrido recursivo por subdirectorios.
- Ignora coincidencias dentro de comentarios SQL (`--`, `/* */`) si se desea.
- Guarda resultados con nombre de archivo, número de línea y contenido.

## 📦 Requisitos
- Python 3
- No requiere librerías externas.

## 🛠️ Uso
Ejecuta el script desde la terminal con los siguientes argumentos:

```bash
python BuscarPatronSQL.py -p "SELECT *" -d /ruta/a/sql -o salida.txt -K
```

### Argumentos:
- `-p`, `--patron`: Expresión regular a buscar.
- `-d`, `--directorio`: Directorio raíz con archivos `.sql`.
- `-o`, `--output`: Nombre del archivo de salida (por defecto `resultados.txt`).
- `-K`: (Opcional) Ignorar coincidencias dentro de comentarios SQL.

## 📁 Salida
El archivo de salida tendrá el siguiente formato:

```
<FICHERO> ; <LINEA> ; <TEXTO>
nombre.sql ; 23 ; SELECT * FROM tabla
```

## 🧑‍💻 Autor
Taibonen
