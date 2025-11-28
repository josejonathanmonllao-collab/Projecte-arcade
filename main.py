from time import sleep
import jocs


while True:
    print("\n---BENVINGUT/DA AL MINI ARCADE--- ")
    print("1. Jugar a Pedra, paper o tisora")
    print("2. Jugar a Endevinar el número")
    print("S. Per sortir")
    joc = input("Tria el joc que vols jugar 1 o 2 'S' per sortir: ")
    
    match joc:
        case '1':
            jocs.janken()
        case '2':
            jocs.nana()
        case 'S':
            print("Adeu!")
            break
        case _:
            print("Error, tens que tria una opció vàlida")   
            sleep(3)