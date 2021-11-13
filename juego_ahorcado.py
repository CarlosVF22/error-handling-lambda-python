#  --------------EL AHORCADO---------------------

#  comprehensions, manejo de errores, manejo de archivos
#  utilizar archivo dara.txt y leelo para obtener las palabras

# investigar funcion enumerate
# metodo get de los diccionearios
# sentencia os.system("clear") - limpiar pantalla

# Mejora el juego
# añade un sistema de puntos
# dibuja el ahorcado con codigo ASCII
# Mejora la interfaz

# 1 busco el archivo data y lo guardo en una variable
# selecciono al azar una palabra dentro de words
# cuento y guardo la cantidad de caracteres en la palabra 
# renderizo la misma cantidad de simbolos en consola que la cantidad de 
# solicito sea ingresada la letra
# recorro el word_game y busco el valor de la letra ingresada
# devuelvo nuevo arr con simbolos y la palabra encontrada
# hacer que el ingreso de letras sea repetitivo
# guardar el arr nuevo y actualizarlo sin eliminar la data anterior.
# imprimir el arr_game en consola
# Limpiar pantalla de los arr_game viejos
# arreglar los caracteres de la data - todo

import random
import os
import time


def read(data):
    words = []
    with open(data, "r", encoding='utf-8') as f:
        for word in f:
            item = word.splitlines()
            words.append(item)
    return words


def iterate(string, search_word, data_game, arr_game):
    arr = [word for word in string]
    
    position = 0
    for word in arr:
        if word == search_word:
            arr_game.pop(position)
            arr_game.insert(position, word)
        position +=1
    
    with open(data_game, "a", encoding='utf-8') as f:
        str_game = "".join(arr_game)
        f.write(str_game)
        f.write("\n")

    return arr_game


def run():
    data_game = "./archivos/game.txt"
    play = True
    data = './archivos/data.txt'
    words = read(data)
    data_len = len(words)
    random_num = random.randint(0, data_len)
    word_game = "".join(words[random_num])
    arr_game = ["-" for item in word_game]
    print(arr_game)
    print(words)


    while play:
        word_input = input("Ingresa una letra: ")
        time.sleep(0.5)
        os.system("clear")
        arr_game= iterate(word_game,word_input, data_game, arr_game)
        print(arr_game)
        print(word_game)


if __name__ == '__main__':
    run()
