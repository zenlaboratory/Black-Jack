''' 
----------------------------- BLACK JACK O 21 ----------------------------------

Juego que pretende emular una partida del juego de cartas conocido como Black Jack o 21.

El juego consiste principalmente en que dos jugadores (banca y jugador) deben acercarse mediante la obtención de cartas, una a una, al numero 21.

El mazo se compone de una baraja francesa, 52 cartas repartidas entre los cuatro palos, corazones, diamantes, picas y tréboles. ♥ ♦ ♠ ♣

El valor de las cartas es el que determina el naipe excepto en el caso de los ases que pueden valer 1 u 11 y las figuras que pasan a valer todas 10 puntos.

--------------------------------------------------------------------------------

'''

# - Imports utilizados en la elaboración del programa.
# - 'random' para poder utilizar números aleatorios y 'time' para poder utilizar pausas en el desarrollo del juego.

from random import randint
from time import sleep

# - Variables y constantes utilizadas en el programa.

baraja = {1:('♠','♦'), 2:('♠','♦')}
baraja_mezclada = []
valores_cartas = ()
valor_as = 0
numero_maximo_cartas = 0
puntos_jugador = 0
puntos_cpu = 0
ganador = True

BLACK_JACK = 21
JUGADA_MAXIMA_CPU = 17

print(baraja.values())


