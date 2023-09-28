import random
words=["montaña","nieve","viento","cerro"]
select_word=random.choice(words)
letters=[]
max_attempts=8
attempts=0
print("¡HOLA!\nAdivina la palabra oculta, solo tienes 8 intentos\n¡A JUGAR!")

def attempts_counter(a,b):
    while attempts<max_attempts:
        reveled_word=""
        for letter in select_word:
            if letter in letters:
                reveled_word+=letter
            else:
                reveled_word+="_ "
    
        print(f"Palabra a adivinar: {reveled_word}")

        user_letter=input("Ingrese una letra: ").lower()

        if user_letter in letters:
            print("Ya adivinaste esa letra. Intenta otra")
            continue

        letters.append(user_letter)

        if user_letter in select_word:
            print("¡BIEN HECHO! La letra está en la palabra")
            attempts+=1
        else:
            print("¡INCORRECTO! La letra no está en la palabra")
            attempts+=1
    
        if set(select_word).issubset(set(letters)):
            print(f"¡FELICIDADES! Has adivinado la palabra: {select_word}")
            break

if attempts==max_attempts:
    print(f"Has agotado tus intentos. La palabra oculta era: {select_word}")