#Ejercicio 5:
"""Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante."""

#Solución:
class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None
    def Display(self):
        print(f"Nombre: {self.nombre}, Registro: {self.registro}")
    def setAge(self, edad):
        self.edad = edad
    def setNota(self, nota):
        self.nota = nota

# Prueba
alumno = Alumno("Dante", "AJDN1565")
alumno.Display()
alumno.setAge(21)
alumno.setNota(18)
print("Edad:", alumno.edad)
print("Nota:", alumno.nota)
