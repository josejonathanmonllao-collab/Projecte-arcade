from Robot import Robot
import time
import random


def janken():
    print("Benvingut/da al joc de Pedra, paper o tisora! ")
    print("Tria un dels dos modes")
    print("1. El primer que arribi a 3 victòries")
    print("2. Al millor de 5 rondes")
    mode = input("Tria el mode 1 o 2: ")

    while mode not in ["1", "2"]:
        print("No és vàlid, elegeix un mode correcte")
        mode = input("Tria el mode 1 o 2: ")
    
    while mode == "1":
        jugador = input("Tria pedra, paper o tisora: ")
        while jugador not in ["pedra", "paper", "tisora"]:
            print("No és vàlid, elegeix pedra, paper o tisora")
            jugador = input("Tria pedra, paper o tisora: ")
        robot = robot.playing()
        if jugador == robot:
            print("A quedat en empat.")
        elif (jugador == "pedra" and robot == "tisora") or \
             (jugador == "paper" and robot == "pedra") or \
             (jugador == "tisora" and robot == "paper"):
              jugador += 1
              print ("Has guanyat la ronda!")
        else:
            robot += 1
            print("Ha guanyat el robot!")