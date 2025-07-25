#Ejercicio 7:
"""FIGlet, llamado así por las cartas de Frank, Ian y Glen, es un programa de principios de la
década de 1990 para hacer letras grandes a partir de texto ordinario, una forma de arte ASCII:
- En la siguiente web puede ver una lista de fuentes admitidas por FIGlet
figlet.org/examples.html
- Desde entonces, FIGlet ha sido portado a Python como un módulo llamado pyfiglet.
Cree un programa el cual cumpla con las siguientes especificaciones:
- Solicite al usuario el nombre de una fuente a utilizar. En caso no sé ingrese ninguna
fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar.
- Solicite al usuario un texto.
- Finalmente, su programa deberá imprimir el texto solicitado usando la fuente
apropiada.
Notas:
- Instalar la librería usando: pip install pyfiglet
- Para usar la librería, debe hacer:
from pyfiglet import Figlet
figlet = Figlet()
- Puede obtener la lista de fuentes disponibles usando: figlet.getFonts()
- Para seleccionar el fondo a utilizar emplee: figlet.setFont(font=fuente_seleccionada)
- Finalmente podrá imprimir el texto usando : print(figlet.renderText(texto_imprimir))
- Recuerde que random tiene un método random choice"""

#Solución: 
import random
from pyfiglet import Figlet

def imprimir_figlet():
    f = Figlet()
    fuentes = f.getFonts()

    fuente = input("Ingrese el nombre de una fuente (deje vacío para aleatoria): ").strip()
    if fuente == "" or fuente not in fuentes:
        fuente = random.choice(fuentes)

    texto = input("Ingrese el texto a imprimir: ")
    f.setFont(font=fuente)
    print(f.renderText(texto))
imprimir_figlet()

