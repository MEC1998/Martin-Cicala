print("¡BIENVENIDO A NÚMEROS Y PALABRAS!")
username=input("Ingrese su nombre de Usuario: ").upper()

game="1"

while game!="1" or game!="2":
    game=(input((f"{username}, ¿Que juego te gustaría intentar?\n- Juego de números (oprima 1): \n- Juego de palabras (oprima 2): \n- Salir (oprima cualquier tecla): ")))

    if game=="1":
        print(f"Hola {username}, bienvenido al Juego de Números")

        max_num=0
        counter=0
        odd_sum=0
        
        while True:
            try:
                num=float(input(f"{username}, ingresa un número entero o 0 (cero) para salir del juego: "))
            
                if num==0:
                    print("Saliendo del juego...")
                    break
                elif num%2==0:
                    if num>max_num:
                        max_num=num
                else:
                    odd_sum+=num
                    counter+=1
            except ValueError:
                print(F"¡CUIDADO {username}! Ingresaste un valor que no es un número. Intenta nuevamente.")
                
        if counter > 0:
            average = odd_sum / counter
            print(f"{username}, el mayor número par que ingresaste es {max_num}\nTambién ingresaste {counter} números impares, cuyo promedio es {average}")
        else:
            print(f"{username}, el mayor número par que ingresaste es {max_num}\nNo ingresaste números impares")
    
    elif game=="2":
        print(f"Hola {username}, bienvenido al Juego de Palabras")
        phrase=input(f"{username}, ingresa una frase: ").upper()

        a_counter=0
        e_counter=0
        i_counter=0
        o_counter=0
        u_counter=0

        for letter in phrase:
            if letter=="A":
                a_counter+=1
            elif letter=="E":
                e_counter+=1
            elif letter=="I":
                i_counter+=1
            elif letter=="O":
                o_counter+=1
            elif letter=="U":
                u_counter+=1
    
        print(f"{username}, hay {a_counter} \"A\", {e_counter} \"E\", {i_counter} \"I\", {o_counter} \"O\" y {u_counter} \"U\" en la frase que ingresaste")
    else:
        print("¡HASTA PRONTO!")
        break
          
            