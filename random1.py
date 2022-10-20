#from random import randint, shuffle
#numeros = list(range(5,50,5))
#shuffle(numeros)
#print(numeros)
#-------------------------------------------
# from random import randint
#aleatorio = randint(1,10)
#print(aleatorio)
#-----------------------------------
# from random import *
#nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
#sorteo = choice(nombres)
#print(sorteo)
#........................................................
#COMPRENSION DE LISTAS
#palabra = 'python'
#lista = [letra for letra in palabra]
#print(lista)
# Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius.
#(grados_fahrenheit-32)*(5/9)
temperatura_fahrenheit = [32, 212, 275]
 
grados_celsius = [(temperatura-32)*(5/9) for temperatura in temperatura_fahrenheit]
print(grados_celsius)