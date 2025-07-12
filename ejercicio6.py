#Ejercicio 6:
"""Empleando la API de SUNAT vista en clase, debemos obtener los diferentes valores para el tipo
de cambio durante el año 2025 hasta donde se tenga información. Una vez realizado ello
calcular:
- Obtener las fechas donde el valor de compra del dólar sea el mínimo.
- Obtener las fechas donde el valor de venta del dólar sea máximo.
- Obtener aquellas fechas donde el valor de la diferencia de compraventa sea máxima.
"""

#Solución:
import requests

def consultar_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?month=5&year=2025"
    headers = { 
        "User-Agent": "Mozilla/5.0"
    }
    try:
        respuesta = requests.get(url, headers=headers)
        respuesta.raise_for_status()  # Lanza excepción si hay error 4xx o 5xx
        data = respuesta.json()

        min_compra = min(data, key=lambda x: x['compra'])
        max_venta = max(data, key=lambda x: x['venta'])
        max_diferencia = max(data, key=lambda x: x['venta'] - x['compra'])

        print("Fecha menor compra:", min_compra['fecha'], "con valor", min_compra['compra'])
        print("Fecha mayor venta:", max_venta['fecha'], "con valor", max_venta['venta'])
        print("Fecha mayor diferencia:", max_diferencia['fecha'], "con diferencia",
              max_diferencia['venta'] - max_diferencia['compra'])

    except requests.RequestException as e:
        print("Error al consultar la API:", e)

consultar_tipo_cambio()

