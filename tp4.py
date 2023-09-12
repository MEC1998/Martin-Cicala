#Trabajo Práctico N°4
#Ejercicio 1
x=0

while x<30:
    x+=1
    if x==15:
        break
    else:
        if x==4 or x==6 or x==10:
            print(f"The value {x} of \"x\" was skipped")
        else:
            print(x)
    
print(f"The execution of the loop was broken when \"x\" was {x}")

#Ejercicio 2
letters=input('Digite la linea, deje en blanco para finalizar: ').strip(' ') 
lines=[]
while letters != '':
    lines.append(letters)
    letters=input('Digite la linea, deje en blanco para finalizar: ').strip(' ')
else:
    if letters=='' and len(lines)==0:
        print('No digito ninguna linea')
    else:
        for i in lines:
            print(i.upper())

#Ejercicio 3
print(f"Ingrese que operación desea realizar\nPara realizar un depósito oprima \"D\"\nPara realizar un retiro oprima \"R\"\nPara salir ingrese un espacio vacío\" \"")
button="_"
count=0

while button!=" ":
    button=str(input("¿Que operación desea realizar?: "))
    button=button.lower()

    if button=="d":
        value=float(input("Ingrese el monto a depositar: "))
        count+=value
        continue
    elif button=="r":
        value=float(input("Ingrese el monto a retirar: "))
        if value>count:
            print("Saldo insuficiente")
            continue
        else:
            count-=value
        continue
    elif button==" ":
        break
    else:
        print("¡ERROR! Ingrese una operación válida")

print(f"El saldo de su cuenta es ${count}")

#Ejercicio 4
is_prime=0
num=1

while num!=0:
    num=int(input("Ingrese un número entero positivo: "))
    
    if num<0:
        print("¡ERROR! Ingrese un número positivo (mayor a cero)")
        continue
    elif num>0:
        counter=0
        for i in range(1, num+1):
            if num%i==0:
                counter=counter+1
        if counter==2:
            is_prime=is_prime+1
    else:
        break

print(f"Se ingresaron {is_prime} números primos")

#Ejercicio 5
age1 = int(input('Ingrese un primer año: '))
age2 = int(input('Ingrese el siguiente año: '))
for i in range(age1,age2+1):

    if i%4==0 and i%10==0 and not i%100==0:
        print(i)
    elif i%400==0:
        print(i)
    else:
        continue

#Ejercicio 6
for i in range(1,21):
        if i%2==0:
                print(i)
        else:
            continue

#Ejercicio 7
numbers=[7,8,1,9]
num=int(input("Ingrese un número para saber si se encuentra en la lista: "))

for i in numbers:
    if num==i:
        print(f"El número {num} si se encuentra en la lista")
        break
    else:
        continue

#Ejercicio 8
print(f"¡BIENVENIDO! A continuación verá las diferentes opciones de menú\n1- Milanesa con puré\n2- Tarta de jamón y queso\n3- Ñoquis con tuco\n0- Salir")
option=1
account=0
count=[]
while option!=0:
    option=int(input("Ingrese una opción: "))
    if option==0:
        break
    elif option==1:
        print("Milanesas con pure: $1200")
        account+=1200
        count.append(1)
    elif option==2:
        print("Tarta de jamón y queso: $1400")
        account+=1400
        count.append(2)
    elif option==3:
        print("Ñoquis con tuco: $1500")
        account+=1500
        count.append(3)
    else:
        print("¡ERROR! Ingrese una opción válida")
print(f"Usted ha pedido los siguientes menús: {count}\nLa cuenta total es de ${account}")
