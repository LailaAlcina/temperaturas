import random

# Definir constantes (ojo con las mayúsculas/minúsculas)
rock= "piedra"
paper = "papel"
scissors = "tijera"

# Define jugada
def jugada_gana(usuario_action, computer_action):
    if usuario_action == computer_action:
        print("Hay un empate")
        return

    if usuario_action == "piedra":
        if computer_action == "tijera":
            print("Gana el usuario al ordenador")
        else:
            print("Pierdes!!!!")
            
    elif usuario_action == "papel":
        if computer_action == "piedra":
            print("Ganaste, ya que el papel gana a la piedra")
        else:
            print("Pierdes!!!")
            
    elif usuario_action == "tijera":
        if computer_action == "papel":
            print("Ganaste, ya que la tijera gana al papel")
        else:
            print("Pierdes!!!")

# Se define el menú
def main():
    # Se definen opciones para el menú (usando la constante 'rocK' correctamente)
    opciones = [rock, paper, scissors]
    
    # Bucle del juego donde el usuario elige las opciones
    while True:
        usuario = input("Elige piedra, papel o tijera (o pulsa 's' para salir): ").lower()
        
        if usuario == "s":
            print("¡Has salido del juego!")
            break
            
        if usuario not in opciones:
            print("La opción no es válida. Tienes que indicar piedra, papel o tijera")
            continue

        # El PC elige la opción aleatoria    
        computer = random.choice(opciones)
        print("\El PC ha elegido: {computer}")
        
        # Comprueba quién gana
        jugada_gana(usuario, computer)

# Empieza el programa 
if __name__ == "__main__":
    main()

