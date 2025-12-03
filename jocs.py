import Robot as rb
import random

def janken():
    #Aquí donem la benvinguda del joc i expliquem les regles del joc.
    print("Benvingut/da al joc de Pedra, paper o tisora! ")
    print("Tria un dels dos modes")
    print("1. El primer que arribi a 3 victòries")
    print("2. Al millor de 5 rondes")
    #Aquí demanem al jugador que elegeixi el mode que vol jugar.
    mode = input("Tria el mode 1 o 2: ")

    #El primer mode és el primer que arribi a 3 victòries i no hi ha un limit de rondes i el segon mode és al millor de 5 rondes. Tambe ficariem el punts del jugador, del robot al guanyar la ronda i si no afegeix res que ho demane de nou el mode que vol jugar el jugador.
    if mode == "1":   
        rondes_per_guanyar = 3
        rondes_maximes = None
    elif mode == "2":
        rondes_per_guanyar = None
        rondes_maximes = 5
    else:
        print("No és vàlid, elegeix un mode correcte")
        return
    punts_del_jugador = 0
    punts_del_robot = 0
    rondes_del_joc = 0 
    opcions = ["pedra", "paper", "tisora"]  
    
    while mode not in ["1", "2"]:
        print("No és vàlid, elegeix un mode correcte")
        mode = input("Tria el mode 1 o 2: ")
    #Aquí tindriem el primer mode del primer joc que és el primer que arribi a 3 victòries.
    if mode == "1":
        while True:
            #Demanar al jugador que eligeix pedra, paper o tisora i si no afegeix res que ho demane de nou.
            jugador = input("Tria pedra, paper o tisora: ")
            while jugador not in ["pedra", "paper", "tisora"]:
                print("No és vàlid, elegeix pedra, paper o tisora")
                jugador = input("Tria pedra, paper o tisora: ")
            #Fer que el robot done una resposta aleatoria.
            r = rb.robot()
            robot = r.playing()
            #Aquí tenim  la comprovació de qui guanya la ronda i afegim els punts al jugador o al robot segons qui hagi guanyat o si els dos han dit la mateixa resposta quedi en empat.
            if jugador == robot:
                print("A quedat en empat.")
            elif (jugador == "pedra" and robot == "tisora") or \
             (jugador == "paper" and robot == "pedra") or \
             (jugador == "tisora" and robot == "paper"):
              punts_del_jugador += 1
              print ("Has guanyat la ronda!")
            else:
                punts_del_robot += 1
                print("Ha guanyat el robot!")
            if punts_del_jugador >= rondes_per_guanyar:
               break
            if punts_del_robot >= rondes_per_guanyar:
               break
    #Aquí tindriem el segon mode del joc que és al millor de 5 rondes.
    while mode == "2":
        #Aquí fem un bucle per a les 5 rondes i el que que guanyi més guanya la partida.
        for ronda in range(5):
            rondes_per_guanyar = 3
            rondes_maximes = 5
            #Demanar al jugador que eligeix pedra, paper o tisora i si no afegeix res que ho demane de nou.
            jugador = input("Tria pedra, paper o tisora: ")
            while jugador not in ["pedra", "paper", "tisora"]:
                print("No és vàlid, elegeix pedra, paper o tisora")
                jugador = input("Tria pedra, paper o tisora: ")
            #Fer que el robot done una resposta aleatoria.
            r = rb.robot()
            robot = r.playing()
            #Aquí tenim  la comprovació de qui guanya la ronda i afegim els punts al jugador o al robot segons qui hagi guanyat o si els dos han dit la mateixa resposta quedi en empat.
            if jugador == robot:
                print("A quedat en empat.")
            elif (jugador == "pedra" and robot == "tisora") or \
                 (jugador == "paper" and robot == "pedra") or \
                 (jugador == "tisora" and robot == "paper"):
                  punts_del_jugador += 1
                  rondes_del_joc += 1
                  print ("Has guanyat la ronda!")
            else:
                punts_del_robot += 1
                print("Ha guanyat el robot!")
                mode = "0"
    print("Punts del jugador:", punts_del_jugador)
    print("Punts del robot:", punts_del_robot)
    if punts_del_jugador > punts_del_robot:
        print("Has guanyat la partida!")
    elif punts_del_robot > punts_del_jugador:
        print("Ha guanyat el robot la partida!")

def nana():
    #Aquí donem la benvinguda al segon joc de endevinar el numero aleatori de l'1 al 100 i que el jugador elegeixi un numero entre l'1 i el 100.
    print("Benvingut/da al joc d'Endevinar el número! ")
    print("Endevina el número entre l'1 al 100: ")
    input("Ficar un número entre l'1 i el 100: ")
    numero = random.randint(1, 100)
    #Ficariem que si no eleigeix un numero entre l'1 i el 100 que ho demani de nou i si el numero del jugador és més alt o més baix que el numero aleatori que avisi asta que el jugador endevini el numero.
    while numero not in range(1, 101):
        if numero < 1 or numero > 100:
            print("El número ha d'estar entre 1 i 100.")
            continue
    while True:
        numero_jugador = int(input("Ficar un número entre l'1 i el 100: "))
        if numero_jugador < numero:
            print("El número és més alt.")
        elif numero_jugador > numero:
            print("El número és més baix.")
        else:
            print("Enhorabona! Has endevinat el número:", numero)
            break