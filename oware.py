def bienvenida_juego():
    '''
    Entrada: Ninguna
    Salida: Menu de bienvenida del juego
    Restricciones: Se debe dar 1, 2, o 3 como input
    Esta funcion hace print al menu de bienvenida del juego y da la opcion de mostrar las instrucciones, jugar, o salir.
    '''
    
    print(""" 
 _______           _______  _______  _______  _ 
(  ___  )|\     /|(  ___  )(  ____ )(  ____ \( )
| (   ) || )   ( || (   ) || (    )|| (    \/| |
| |   | || | _ | || (___) || (____)|| (__    | |
| |   | || |( )| ||  ___  ||     __)|  __)   | |
| |   | || || || || (   ) || (\ (   | (      (_)
| (___) || () () || )   ( || ) \ \__| (____/\ _ 
(_______)(_______)|/     \||/   \__/(_______/(_)
""")
    print("\n")
    
    respuesta = input("Bienvenido!\n\nEscriba el numero de la opcion que quiere:\n\n1. Mostrar las instrucciones\n2. Jugar\n3. Salir del juego\n")
        
        
    if respuesta == "1":
        print("""\n1. Este juego consiste en un juego de mesa para dos jugadores llamado Oware.\n
2. Al inicio se va a rifar el jugador que empieza. Este jugador escoge un terreno, y luego esparcirá una por una las semillas de este terreno en orden de las manecillas del reloj. Cuando este jugador termina de esparcirlas, es el turno del otro jugador, y asi se iran turnando ambos jugadores hasta que uno gane.\n
3. Si la ultima semilla cae en un terreno del jugador contrario y este terreno tiene 2 o 3 semillas, se captura el terreno.\n
4. Si los terrenos anteriores consecutivos a este tambien tienen 2 o 3 semillas, se capturaran estos tambien.\n
5. Al capturar semillas, estas se agregan a un marcador.\n
6. Un jugador gana cuando se le acaban todas las semillas al jugador contrario.""")
        print("\nVolviendo al menu principal...")
        bienvenida_juego()
    
    elif respuesta == "2":
        inicio_juego()
    
    elif respuesta == "3":
        print("\nSaliendo del juego...")
        raise SystemExit
    
    elif respuesta != "1" or respuesta != "2" or respuesta != "3":
        print("\nError 01")
        bienvenida_juego()

def inicio_juego():
    '''
    Entrada: Ninguna
    Salida: Ganador de la rifa de quien juega primero, inicio del juego
    Restricciones: Ninguna
    Esta funcion escoge cual de los dos jugadores sera el primero en jugar y luego inicia el juego.
    '''
    import random
    
    
    jugador1 = "jugador 1"
    jugador2 = "jugador 2"
        
    
    ganador_rifa = random.choice([jugador1,jugador2])
        
        
    respuesta = input("\nBienvenido a Oware: Edicion Texto! Presione cualquier tecla para seleccionar cual jugador ira primero.")
    print("\nEl jugador que se ha elegido al azar para ir de primero es el "+ganador_rifa+"!")
    respuesta = input("\nPor favor, "+ganador_rifa+", presione cualquier tecla para iniciar su turno.")
        
    return menu_juego(ganador_rifa)


def menu_juego(jugador_elegido):
    '''
    Entrada: Jugador ganador de la rifa
    Salida: El tablero del juego
    Restricciones: El jugador elegido debe ser un string
    Esta funcion define las variables usadas en el tablero y define la funcion del display del tablero y retorna este ultimo.
    '''
    global tablero
    global marcador_jugador1
    global marcador_jugador2
    
    if type(jugador_elegido) != str:
        return "\nError 02"
    
    primero_en_jugar = jugador_elegido
    
    jugador1_hoyo1 = 4
    jugador1_hoyo2 = 4
    jugador1_hoyo3 = 4
    jugador1_hoyo4 = 4
    jugador1_hoyo5 = 4
    jugador1_hoyo6 = 4
    
    jugador2_hoyo1 = 4
    jugador2_hoyo2 = 4
    jugador2_hoyo3 = 4
    jugador2_hoyo4 = 4
    jugador2_hoyo5 = 4
    jugador2_hoyo6 = 4
    
    
    marcador_jugador1 = 0
    marcador_jugador2 = 0
    
    no_sumar = 0

    tablero = [jugador1_hoyo1,jugador1_hoyo2,jugador1_hoyo3,jugador1_hoyo4,jugador1_hoyo5,jugador1_hoyo6,
jugador2_hoyo1,jugador2_hoyo2,jugador2_hoyo3,jugador2_hoyo4,jugador2_hoyo5,jugador2_hoyo6,no_sumar,marcador_jugador1,marcador_jugador2]
    
    def display(lista_tablero,jugador_actual):
        '''
        Entrada: Lista con elementos del tablero y el jugador actual
        Salida: El display del tablero del juego
        Restricciones: La lista del tablero debe ser tipo list, y el jugador_actual debe ser tipo string
        Esta funcion hace display al tablero del juego mediante y para hacer esto hace uso de las variables contenidos en la lista tablero.
        '''
        global tablero
        global marcador_jugador1
        global marcador_jugador2
        
        if type(lista_tablero) != list:
            return "Error 03"
        
        elif type(jugador_actual) != str:
            return "Error 04"
        
        largo = len(tablero)
        indice = 0
        posicion = 0
        contador_marcador = 0
        diferencia = 0
        posicion_inicial = 0
        
        print('''\n                   |   6   |   5   |   4   |   3   |   2   |   1   |\n'''
        ,'''                  -------------------------------------------------\n''',
        "    Jugador 2: ",tablero[14],"|  ",tablero[11],"  |  ",
        tablero[10],"  |  ",tablero[9],"  |  ",tablero[8],"  |  ",tablero[7],"  |  ",
        tablero[6],"  |  ",'''\n      --------------------------------------------------------------\n''',"    Jugador 1: ",tablero[13],"|  ",tablero[0],"  |  ",
        tablero[1],"  |  ",tablero[2],"  |  ",tablero[3],"  |  ",tablero[4],"  |  ",tablero[5],"  |  "
        '''\n                   -------------------------------------------------\n                   |   1   |   2   |   3   |   4   |   5   |   6   |''')
        
        if tablero[0] == 0 and tablero[1] == 0 and tablero[2] == 0 and tablero[3] == 0 and tablero[4] == 0 and tablero[5] == 0:
            print("\nFelicidades! El jugador 2 ha ganado!")
            respuesta = input("\nPresione cualquier tecla para salir.")
            return
        
        elif tablero[6] == 0 and tablero[7] == 0 and tablero[8] == 0 and tablero[9] == 0 and tablero[10] == 0 and tablero[11] == 0:
            print("\nFelicidades! El jugador 1 ha ganado!")
            respuesta = input("\nPresione cualquier tecla para salir.")
            return
        
        respuesta = input("\nPor favor, "+jugador_actual+", escriba el numero del terreno en donde desea plantar.")
        
        if jugador_actual == "jugador 1":
            if respuesta == "1":
                if tablero[0] == 0:
                    print("\nNo puede plantar en un territorio vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[0]
                while tablero[0] != 0:
                    if indice == 11:
                        break
                    tablero[indice+1] = tablero[indice+1] + 1
                    tablero[0] = tablero[0] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[0] != 0:
                    if posicion == 11:
                        break
                    tablero[0] = tablero[0] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial > 5 and posicion_inicial < 12:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[13] = tablero[13] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == 5:
                                break
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "2":
                if tablero[1] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[1]
                while tablero[1] != 0:
                    if indice == 10:
                        break
                    tablero[indice+2] = tablero[indice+2] + 1
                    tablero[1] = tablero[1] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[1] != 0:
                    if posicion == 11:
                        break
                    tablero[1] = tablero[1] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                contador_marcador = contador_marcador + 1
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial > 4 and posicion_inicial < 11:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[13] = tablero[13] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == 5:
                                break
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "3":
                if tablero[2] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[2]
                while tablero[2] != 0:
                    if indice == 9:
                        break
                    tablero[indice+3] = tablero[indice+3] + 1
                    tablero[2] = tablero[2] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[2] != 0:
                    if posicion == 11:
                        break
                    tablero[2] = tablero[2] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                contador_marcador = contador_marcador + 2
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial > 3 and posicion_inicial < 10:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[13] = tablero[13] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == 5:
                                break
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "4":
                if tablero[3] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[3]
                while tablero[3] != 0:
                    if indice == 8:
                        break
                    tablero[indice+4] = tablero[indice+4] + 1
                    tablero[3] = tablero[3] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[3] != 0:
                    if posicion == 11:
                        break
                    tablero[3] = tablero[3] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                if contador_marcador == 10:
                    contador_marcador = contador_marcador - 1
                contador_marcador = contador_marcador + 3
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial > 2 and posicion_inicial < 9:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[13] = tablero[13] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == 5:
                                break
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "5":
                if tablero[4] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[4]
                while tablero[4] != 0:
                    if indice == 7:
                        break
                    tablero[indice+5] = tablero[indice+5] + 1
                    tablero[4] = tablero[4] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[4] != 0:
                    if posicion == 11:
                        break
                    tablero[4] = tablero[4] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                contador_marcador = contador_marcador + (indice)
                if posicion_inicial == 1:
                    contador_marcador = contador_marcador + 3
                if posicion_inicial == 2:
                    contador_marcador = contador_marcador + 2
                if posicion_inicial == 3:
                    contador_marcador = contador_marcador + 1
                if posicion_inicial == 5:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial == 6:
                    contador_marcador = contador_marcador - 2
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial > 1 and posicion_inicial < 8:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[13] = tablero[13] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == 5:
                                break
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "6":
                if tablero[5] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[5]
                while tablero[5] != 0:
                    if indice == 6:
                        break
                    tablero[indice+6] = tablero[indice+6] + 1
                    tablero[5] = tablero[5] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[5] != 0:
                    if posicion == 11:
                        break
                    tablero[5] = tablero[5] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                contador_marcador = contador_marcador + indice
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial == 1:
                    contador_marcador = contador_marcador + 4
                if posicion_inicial == 2:
                    contador_marcador = contador_marcador + 3
                if posicion_inicial == 3:
                    contador_marcador = contador_marcador + 2
                if posicion_inicial == 4:
                    contador_marcador = contador_marcador + 1
                if posicion_inicial < 7:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[13] = tablero[13] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == 5:
                                break
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
            
            else:
                print("\nPor favor escriba un numero del 1 al 6.")
                return display(tablero,jugador_actual)
        
        elif jugador_actual == "jugador 2":
            if respuesta == "1":
                if tablero[6] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[6]
                while tablero[6] != 0:
                    if indice == 5:
                        break
                    tablero[indice+7] = tablero[indice+7] + 1
                    tablero[6] = tablero[6] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[6] != 0:
                    tablero[6] = tablero[6] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                if contador_marcador >= 6 and contador_marcador < 12:
                    while contador_marcador != 0:
                        if contador_marcador > 6:
                            diferencia = diferencia + 1
                        contador_marcador = contador_marcador - 1
                    contador_marcador = contador_marcador + diferencia
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial > 5 and posicion_inicial < 12:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[14] = tablero[14] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == -1:
                                contador_marcador = contador_marcador + 1
                            if posicion_inicial == 6 and tablero[contador_marcador] == 2:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                            if posicion_inicial == 6 and tablero[contador_marcador] == 3:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "2":
                if tablero[7] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[7]
                while tablero[7] != 0:
                    if indice == 4:
                        break
                    tablero[indice+8] = tablero[indice+8] + 1
                    tablero[7] = tablero[7] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[7] != 0:
                    tablero[7] = tablero[7] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                if contador_marcador >= 5 and contador_marcador < 12:
                    while contador_marcador != 0:
                        if contador_marcador > 5:
                            diferencia = diferencia + 1
                        contador_marcador = contador_marcador - 1
                    contador_marcador = contador_marcador + diferencia
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial > 4 and posicion_inicial < 11:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[14] = tablero[14] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == -1:
                                contador_marcador = contador_marcador + 1
                            if posicion_inicial == 5 and tablero[contador_marcador] == 2:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                            if posicion_inicial == 5 and tablero[contador_marcador] == 3:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "3":
                if tablero[8] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[8]
                while tablero[8] != 0:
                    if indice == 3:
                        break
                    tablero[indice+9] = tablero[indice+9] + 1
                    tablero[8] = tablero[8] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[8] != 0:
                    tablero[8] = tablero[8] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                if contador_marcador >= 4 and contador_marcador < 12:
                    while contador_marcador != 0:
                        if contador_marcador > 4:
                            diferencia = diferencia + 1
                        contador_marcador = contador_marcador - 1
                    contador_marcador = contador_marcador + diferencia
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial > 3 and posicion_inicial < 10:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[14] = tablero[14] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            if posicion_inicial == 4:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                                break
                            contador_marcador = contador_marcador - 1
                                
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "4":
                if tablero[9] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[9]
                while tablero[9] != 0:
                    if indice == 2:
                        break
                    tablero[indice+10] = tablero[indice+10] + 1
                    tablero[9] = tablero[9] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[9] != 0:
                    tablero[9] = tablero[9] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                if contador_marcador >= 3 and contador_marcador < 12:
                    while contador_marcador != 0:
                        if contador_marcador > 3:
                            diferencia = diferencia + 1
                        contador_marcador = contador_marcador - 1
                    contador_marcador = contador_marcador + diferencia
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if posicion_inicial > 2 and posicion_inicial < 9:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[14] = tablero[14] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == -1:
                                contador_marcador = contador_marcador + 1
                            if posicion_inicial == 3 and tablero[contador_marcador] == 2:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                            if posicion_inicial == 3 and tablero[contador_marcador] == 3:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "5":
                if tablero[10] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[10]
                while tablero[10] != 0:
                    if indice == 1:
                        break
                    tablero[indice+11] = tablero[indice+11] + 1
                    tablero[10] = tablero[10] - 1
                    indice = indice + 1
                    contador_marcador = contador_marcador + 1
                while tablero[10] != 0:
                    tablero[10] = tablero[10] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                if contador_marcador >= 2 and contador_marcador < 12:
                    while contador_marcador != 0:
                        if contador_marcador > 2:
                            diferencia = diferencia + 1
                        contador_marcador = contador_marcador - 1
                    contador_marcador = contador_marcador + diferencia
                while contador_marcador >= 12:
                    contador_marcador = contador_marcador - 1
                if  posicion_inicial > 1 and posicion_inicial < 8:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[14] = tablero[14] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == -1:
                                contador_marcador = contador_marcador + 1
                            if posicion_inicial == 2 and tablero[contador_marcador] == 2:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                            if posicion_inicial == 2 and tablero[contador_marcador] == 3:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
        
            elif respuesta == "6":
                if tablero[11] == 0:
                    print("\nPor favor plante en un territorio que no este vacio.")
                    return display(tablero,jugador_actual)
                posicion_inicial = tablero[11]
                while tablero[11] != 0:
                    tablero[11] = tablero[11] - 1
                    tablero[posicion] = tablero[posicion] + 1
                    posicion = posicion + 1
                    contador_marcador = contador_marcador + 1
                contador_marcador = contador_marcador - indice - 1
                if posicion_inicial < 7:
                    if tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                        while tablero[contador_marcador] == 2 or tablero[contador_marcador] == 3:
                            tablero[14] = tablero[14] + tablero[contador_marcador]
                            tablero[contador_marcador] = 0
                            contador_marcador = contador_marcador - 1
                            if contador_marcador == -1:
                                contador_marcador = contador_marcador + 1
                            if posicion_inicial == 1 and tablero[contador_marcador] == 2:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                            if posicion_inicial == 1 and tablero[contador_marcador] == 3:
                                tablero[14] = tablero[14] + tablero[contador_marcador]
                if jugador_actual == "jugador 1":
                    jugador_actual = "jugador 2"
                else:
                    jugador_actual = "jugador 1"
                return display(tablero,jugador_actual)
            
            else:
                print("\nPor favor escriba un numero del 1 al 6.")
                return display(tablero,jugador_actual)
        
        
    return display(tablero,primero_en_jugar)

bienvenida_juego()
