import numpy as np
import random
from variables import *
import os
from clases import *


def instrucciones():
    print(
        """¡Bienvenido a hundir la flota!
    Este juego consiste en hundir los barcos del contrario. En cada tirada, tienes 
    que dar las coordenadas x e y, como números del 0 al 9, para disparar 
    a los barcos del contrario.
    Si aciertas, verás un mensaje de ¡Tocado! y podrás seguir disparando.
    Si fallas, el turno pasa al otro jugador, que disparará contra tus barcos.
    Gana el primero que hunda los barcos del contrario.
    ¡Disfruta del juego!"""
    )


def crear_tablero():
    """Esta función crea un tablero vacío con un array de Numpy. Tiene un tamaño de 10x10, y las casillas están rellenas con el signo =, que a lo largo del juego se sustituirá por:
    O si hay un barco
    X si ha sido un disparo acertado
    N si ha sido un disparo fallido"""
    tablero = np.full((10, 10), "=")
    return tablero


def colocacion_aleatoria(tablero):
    """La función sirve para ubicar al azar los barcos de cada jugador. Para el listado de barcos de dic_barcos, inicialmente determina la orientación del barco, y  después las coordenadas x e y."""
    for barco, eslora in dic_barcos.items():
        lista_orientaciones = ["Norte", "Sur", "Este", "Oeste"]
        orientacion = np.random.choice(lista_orientaciones)
        if orientacion == "Norte":
            x = np.random.randint(eslora, 9)
            y = np.random.randint(0, 9)
            for i in range(eslora):
                if tablero[x - i, y] != "O":
                    tablero[x - i, y] = "O"
                else:
                    continue
        if orientacion == "Sur":
            x = np.random.randint(0, 9 - eslora)
            y = np.random.randint(0, 9)
            for i in range(eslora):
                if tablero[x + i, y] != "O":
                    tablero[x + i, y] = "O"
                else:
                    continue
        if orientacion == "Este":
            x = np.random.randint(0, 9)
            y = np.random.randint(0, 9 - eslora)
            for i in range(eslora):
                if tablero[x, y + i] != "O":
                    tablero[x, y + i] = "O"
                else:
                    continue
        if orientacion == "Oeste":
            x = np.random.randint(0, 9)
            y = np.random.randint(eslora, 9)
            for i in range(eslora):
                if tablero[x, y - i] != "O":
                    tablero[x, y - i] = "O"
                else:
                    continue


def jugar():
    """Esta función agrupa la partida entera de este juego."""
    instrucciones()
    tablero1 = crear_tablero()
    tablero2 = crear_tablero()
    tablero3 = crear_tablero()
    colocacion1 = colocacion_aleatoria(tablero1)
    colocacion2 = colocacion_aleatoria(tablero2)
    turno = 1
    while turno == 1:
        coord_x = int(input("Teclea el número de fila del 0 al 9: "))
        coord_y = int(input("Teclea el número de columna del 0 al 9: "))
        if tablero2[coord_x][coord_y] == "O":
            tablero3[coord_x][coord_y] = "X"
            print("\nTablero del jugador 1")
            print(tablero1)
            print("\nTablero del jugador 2")
            print(tablero3)
            print("¡Tocado!")
            if not any("O" in coord_x for coord_x in tablero2):
                print("¡Enhorabuena, has ganado!")
                break
            else:
                print("¡Tocado! Dispara otra vez")
                continue
        else:
            tablero3[coord_x][coord_y] = "N"
            print("Agua")
            print("\nTablero del jugador 1")
            print(tablero1)
            print("\nTablero del jugador 2")
            print(tablero3)
            turno = 2
        while turno == 2:
            x_pc = np.random.randint(0, 9)
            y_pc = np.random.randint(0, 9)
            if tablero1[x_pc][y_pc] == "O":
                tablero1[x_pc][y_pc] = "X"
                print(tablero1)
                print(tablero3)
                print(f"Ha disparado el jugador 2, ¡Tocado!")
                if not any("O" in x_pc for x_pc in tablero1):
                    print("¡Mala suerte, el jugador 2 te ha ganado!")
                    break
                else:
                    print("¡Tocado! El jugador 2 dispara otra vez")
                    turno = 2
            else:
                tablero1[x_pc][y_pc] = "N"
                print("Ha disparado el jugador 2, ¡Agua!")
                turno = 1
