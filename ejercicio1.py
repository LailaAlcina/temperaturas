import random

#Definir constantes
rocK="piedra"
paper="papel"
scissors="tijera"

#Define jugada
def jugada_gana(usuario_action, computer_action)
if usuario_action == computer_action
    print ("Hay un empate")
    return
    if usuario_action == piedra
        if computer_action == tijera
        print ("Gana el usuario al ordenador")
        else
        print("Pierdes!!!!")
    elif usuario_action == papel
        if computer_action == piedra
        print ("Ganaste, ya que el papel gana a la piedra")
        else 
        print ("Pierdes!!!")
    elif usuario_action == tijera
        if computer_action == papel
        print("Gasnaste, que la tijera gana al papel")
        else:
        print("Pierdes!!!")
#Se define el menu
def main ()
#Se define opciones para el menu
    opciones=[rocks,paper,scissors]
    #bucle del juego donde el usuario elige las opciones
    while True
        usuario = (
            imput("\Elige piedra, papel o tijera sino pulsa S de salir: ") 
            )
        if usuario== "s":
                print("¡Has salido del juego!")
                break
        if usuario not in opciones:
                print("La opcion no es valida. Tienes que indicar piedra, papel o tijera")
                continue

        #El pc elige la opcion aleatoria    
        computer =random.choice(opciones)
            print ("\El pc ha elegido: {computer}")
        #Comprueba quien gana
        jugada_gana(usuario, computer)

#Empieza el programa 
if__name__ == "menu"
    main()

