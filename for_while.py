#EJERCICIOS EN CLASE: CICLOS
#Ejercicio 1
alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

corrimiento=int(input("Ingrese la cantidad de lugares de corrimiento: "))

for i in range(5):
    mensaje=input(f"Ingrese el mensaje {i+1}: ")
    mensaje=mensaje.lower()
    cifra_del_cesar=""
    
    for letra in mensaje:
        if letra in alfabeto:
            indice=(alfabeto.index(letra)+corrimiento)%27
            nueva_letra=alfabeto[indice]
        else:
            indice=mensaje.index(letra)
            nueva_letra=mensaje[indice]
        cifra_del_cesar+=nueva_letra
    print(f"Mensaje {i+1}: {cifra_del_cesar}")

#Ejercicio 2
num=1
pares=0
impares=0

while num!=0:
    num=int(input("Ingrese un número entero positivo: "))
    if num<0:
        print("¡ERROR! Ingrese solo números enteros positivos")
    else:
        if num>0:
            if num%2==0:
                pares=pares+1
            else:
                impares=impares+1
    print(f"En total hay {pares} números pares y {impares} números impares")
print("SALIENDO DEL PROGRAMA")