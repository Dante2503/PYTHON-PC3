#Ejercicio 4:
"""Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase. Además cree una clase CUADRADO que heredé de rectangulo. Cree un
objeto de tipo rectangulo y 1 de tipo cuadrado."""

#solución:
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho #Constructor 

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado) #Con el super() llamamos al constructor 

# Prueba
r = Rectangulo(4, 5)
c = Cuadrado(3)
print("Área del rectángulo:", r.calcular_area())
print("Área del cuadrado:", c.calcular_area())
