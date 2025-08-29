import os
import argparse
import re

def es_comentario(linea, dentro_bloque):
    # Comentario de línea
    if linea.strip().startswith('--'):
        return True, dentro_bloque

    # Inicio de bloque de comentario
    if '/*' in linea:
        dentro_bloque = True

    # Fin de bloque de comentario
    if '*/' in linea:
        dentro_bloque = False
        return True, dentro_bloque

    return dentro_bloque, dentro_bloque

def buscar_patron_en_archivos(patron_regex, directorio, archivo_salida, ignorar_comentarios):
    patron_compilado = re.compile(patron_regex, re.IGNORECASE)
    resultados = []

    for root, _, files in os.walk(directorio):
        for file in files:
            if file.endswith(".sql"):
                ruta_completa = os.path.join(root, file)
                try:
                    with open(ruta_completa, 'r', encoding='utf-8') as f:
                        dentro_bloque = False
                        for num_linea, linea in enumerate(f, start=1):
                            es_com, dentro_bloque = es_comentario(linea, dentro_bloque)
                            if ignorar_comentarios and es_com:
                                continue
                            if patron_compilado.search(linea):
                                resultados.append(f"{file};{num_linea};{linea.strip()}")
                except Exception as e:
                    print(f"⚠️ Error al leer {ruta_completa}: {e}")

    # Guardar resultados
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as f_out:
            f_out.write("<FICHERO> ; <LINEA> ; <TEXTO> \n")
            for resultado in resultados:
                f_out.write(resultado + "\n")
        print(f"✅ Resultados guardados en: {archivo_salida}")
    except Exception as e:
        print(f"⚠️ Error al escribir el archivo de salida: {e}")

def main():
    parser = argparse.ArgumentParser(description="Buscar patrón (regex) en archivos SQL y guardar resultados")
    parser.add_argument("-p", "--patron", required=True, help="Expresión regular a buscar")
    parser.add_argument("-d", "--directorio", required=True, help="Directorio con archivos SQL")
    parser.add_argument("-o", "--output", default="resultados.txt", help="Archivo de salida")
    parser.add_argument("-K", action="store_true", help="Ignorar coincidencias dentro de comentarios SQL")
    args = parser.parse_args()

    buscar_patron_en_archivos(args.patron, args.directorio, args.output, args.K)

if __name__ == "__main__":
    main()