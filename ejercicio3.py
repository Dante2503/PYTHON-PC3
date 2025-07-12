#Ejercicio 3:
"""Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.
Cree 2 objetos de tipo circulo y calcule su área.
"""

#Solución:
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)
# Prueba
circulo1 = Circulo(10)
circulo2 = Circulo(15)
print("Área del círculo 1:", circulo1.calcular_area())
print("Área del círculo 2:", circulo2.calcular_area())
