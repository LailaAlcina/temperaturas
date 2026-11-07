import random

#Definir constantes
rocK="pieda"
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
    #Se define el bucle