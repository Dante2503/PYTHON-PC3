#Ejercicio 8:
"""Del siguiente URL
https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format
&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D
%3D
Descargue la imagen que más le agrade, según lo revisado en la clase. Posteriormente crear un
programa que permita el almacenamiento de la imagen como un archivo zip. Finalmente cree
un código que permita hacer un unzip al archivo zipeado."""

#Solución:
import requests
import zipfile
import os

def descargar_y_zippear_imagen():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070"
    nombre_imagen = "imagen.jpg"
    nombre_zip = "imagen.zip"

    # Descargar la imagen
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_imagen, 'wb') as f:
            f.write(response.content)
        print("Imagen descargada correctamente.")
    else:
        print("Error al descargar la imagen.")
        return

    # Crear archivo zip
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        zipf.write(nombre_imagen)
    print(f"Imagen comprimida en {nombre_zip}")

def descomprimir_zip():
    nombre_zip = "imagen.zip"
    with zipfile.ZipFile(nombre_zip, 'r') as zipf:
        zipf.extractall("imagen_extraida")
    print("Imagen extraída correctamente en la carpeta 'imagen_extraida'.")

# Ejecutar funciones
descargar_y_zippear_imagen()
descomprimir_zip()
