
#Crea un juego interactivo del ahorcado en Python. El juego debe seleccionar una palabra al azar de una lista de palabras predefinidas y
#permitir que el jugador adivine la palabra letra por 
#letra. El jugador tiene un número limitado de intentos antes de perder el juego.
#Requisitos:
# Define una lista de palabras que el programa pueda elegir al azar para que el jugador 
#adivine. Puedes usar palabras relacionadas con la programación, tecnología o 
#cualquier tema que te guste.
# El programa debe seleccionar una palabra al azar de la lista para cada partida.
# El juego debe mostrar el estado actual de la palabra oculta con guiones bajos (_) que 
#representan las letras no adivinadas y las letras adivinadas deben mostrarse en su 
#lugar correspondiente.
# El jugador debe poder ingresar una letra adivinada en cada turno.
# El programa debe verificar si la letra adivinada está en la palabra secreta y actualizar el 
#tablero en consecuencia.
# El jugador tiene un número limitado de intentos (por ejemplo, 6) antes de perder el 
#juego.
# Muestra mensajes informativos al jugador, como "Adivinaste una letra correctamente" 
#o "Letra incorrecta, te quedan X intentos".
# El juego debe terminar cuando el jugador adivina todas las letras o se quedan sin 
#intentos.
# Proporciona un mensaje de victoria si el jugador adivina la palabra y un mensaje de 
#derrota si se quedan sin intentos.

from functions import select_word

word = select_word().lower()
guess_list = []
word_list = []
lives = 6

print(word)
print(f"---HANGMAN (x_x)--- ")
name = input("Please enter your name below: ")
print(f"Hi {name}, lets play!\nYour word has been chosed, it has {len(word)} letters.")

for i in word:
    print("_", end=" ")
    word_list.append(i)
    guess_list.append("_")

choice = ''
count = 0
while True:
    choice = input("\nPlease enter a letter\n")
    for index, i in enumerate(word_list):
        if choice == i:
            guess_list[index] = choice
            count += 1
            print("You entered a correct letter")
    if guess_list == word_list:
        print("You won the game! Congratulations")
        print(word_list)
        break
    elif count == 0 and lives>0:
        lives -= 1
        print(f"You lose 1 live, keep trying! You have {lives} left")
    elif lives <= 0:
        print("You lose, better luck next time!")
        break
    count=0
    print(guess_list)
    