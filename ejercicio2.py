#Ejercicio 2:
"""Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)
"""

#Solución:
def procesar_calificaciones():
    entrada = input("Ingrese las calificaciones separadas por comas: ")
    calificaciones = entrada.split(',')

    lista_enteros = []

    for calificacion in calificaciones:
        try:
            lista_enteros.append(int(calificacion.strip()))
        except ValueError:
            print(f"Error: '{calificacion}' no es una calificación válida.")

    print("Calificaciones procesadas:", lista_enteros)
procesar_calificaciones()