# Mensaje de bienvenida
print("¡BIENVENIDO A NÚMEROS Y PALABRAS!")

# Solicitar el nombre de usuario y convertirlo a mayúsculas
username = input("Ingrese su nombre de Usuario: ").upper()

# Variable para seleccionar el juego (inicialmente 1)
game = "1"

# Bucle principal del programa
while game != "1" or game != "2":
    # Solicitar al usuario que elija un juego (1, 2) o salir (cualquier otra tecla)
    game = input(f"{username}, ¿Qué juego te gustaría intentar?\n- Juego de números (oprima 1): \n- Juego de palabras (oprima 2): \n- Salir (oprima cualquier tecla): ")

    if game == "1":
        # Juego de números
        print(f"Hola {username}, bienvenido al Juego de Números")

        # Inicializar variables para el juego de números
        max_num = 0  # Almacenará el número par más grande
        counter = 0  # Contador de números impares
        odd_sum = 0  # Suma de números impares

        # Bucle para ingresar números
        while True:
            try:
                # Solicitar al usuario que ingrese un número o 0 para salir
                num = float(input(f"{username}, ingresa un número entero o 0 (cero) para salir del juego: "))

                if num == 0:
                    # Salir del juego si se ingresa 0
                    print("Saliendo del juego...")
                    break
                elif num % 2 == 0:
                    # Si es un número par, actualizar el número máximo par
                    if num > max_num:
                        max_num = num
                else:
                    # Si es un número impar, sumarlo y contarlos
                    odd_sum += num
                    counter += 1
            except ValueError:
                # Capturar excepción si el usuario ingresa un valor no numérico
                print(f"¡CUIDADO {username}! Ingresaste un valor que no es un número. Intenta nuevamente.")

        # Mostrar resultados del juego de números
        if counter > 0:
            average = odd_sum / counter
            print(f"{username}, el mayor número par que ingresaste es {max_num}\nTambién ingresaste {counter} números impares, cuyo promedio es {average}")
        else:
            print(f"{username}, el mayor número par que ingresaste es {max_num}\nNo ingresaste números impares")

    elif game == "2":
        # Juego de palabras
        print(f"Hola {username}, bienvenido al Juego de Palabras")
        phrase = input(f"{username}, ingresa una frase: ").upper()

        # Contadores para las vocales
        a_counter = 0
        e_counter = 0
        i_counter = 0
        o_counter = 0
        u_counter = 0

        # Contar ocurrencias de cada vocal en la frase
        for letter in phrase:
            if letter == "A":
                a_counter += 1
            elif letter == "E":
                e_counter += 1
            elif letter == "I":
                i_counter += 1
            elif letter == "O":
                o_counter += 1
            elif letter == "U":
                u_counter += 1

        # Mostrar resultados del juego de palabras
        print(f"{username}, hay {a_counter} \"A\", {e_counter} \"E\", {i_counter} \"I\", {o_counter} \"O\" y {u_counter} \"U\" en la frase que ingresaste")
    else:
        # Opción para salir del programa
        print("¡HASTA PRONTO!")
        break
