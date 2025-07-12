#Ejercicio 1:
"""Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser menor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError."""

#Solución:
def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            x, y = map(int, fraccion.split('/'))
            if y == 0:
                raise ZeroDivisionError
            if x > y or x < 0:
                raise ValueError
            porcentaje = round((x / y) * 100)
            if porcentaje <= 1:
                print("E")
            elif porcentaje >= 99:
                print("F")
            else:
                print(f"{porcentaje}%")
            break
        except ZeroDivisionError:
            print("Error: División entre cero. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese solo números enteros y asegúrese de que X ≤ Y y Y ≠ 0.")

obtener_fraccion()