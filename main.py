BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
print ("Hola!, espero te guste mi trivia sobre cine")

import time
time.sleep (2)

print ("Es super sencilla, suerte :) ")
puntaje=0

nombre=input(BLUE+ "Primero escribe tu nombre :  " +RESET )

print ("Entonces", nombre, ", Cuando sepas la respuesta escribe la opcion correcta y le das la tecla 'Enter' para enviarla")

print (GREEN+" 1: cuando se estreno el señor de los anillos: el retorno del rey ?"+RESET)
print ("a) 2000 ")
print ("b) 2001 ")
print ("c) 2003 ")
print ("d) 2004 ")

respuesta_1 = input (RED+ "tu opcion es : "+RESET )

while respuesta_1 not in( "a","b","c","d"):
  respuesta_1 =input ("debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_1 == "c":
  puntaje += 10
  print ("correcto", nombre , ":)")
else:
  puntaje += -5
  print ("incorrecto", nombre , ":(")

  
time.sleep (1)

print (GREEN+" 2: Quien fue el director de la película: la forma del agua ?"+RESET)
print ("a) Alejandro Gonzales Iñarritu ")
print ("b) Guillermo del Toro ")
print ("c) Damien Chazelle ")
print ("d) Steven Spielberg ")

respuesta_2 = input (RED+ "tu opcion es : "+RESET)

while respuesta_2 not in( "a","b","c","d"):
  respuesta_2 =input ("debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_2 == "b":
    puntaje += 10
    print ("correcto", nombre , ":)")
else:
  puntaje += -5
  print ("incorrecto", nombre , ":(")
time.sleep (1)

print (GREEN+" 3: Cual fue la primera pelicula extranjera en ganar el premio 'Mejor Pelicula' en los Premios Oscar ?"+RESET)
print ("a) Parasite ")
print ("b) Roma ")
print ("c) El laberinto del fauno ")
print ("d) Minari ")

respuesta_3 = input (RED+"tu opcion es : "+RESET)

while respuesta_3 not in( "a","b","c","d"):
  respuesta_3 =input ("debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_3 == "a":
  puntaje += 10
  print ("correcto", nombre , ":)")
else:
  puntaje += -5
  print ("incorrecto", nombre , ":(")

print ("gracias por participar",nombre,"!, tienes",puntaje, "puntos" )

time.sleep (2) 
if puntaje < 20 :
  print ("sigue intentandolo")
else :
  print ("Eres un verdadero cinefilo!")