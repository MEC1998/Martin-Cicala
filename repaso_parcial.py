#Ejercicio 1
phrase=""
while len(phrase)==0:
    phrase=input("Ingrese una frase o palabra: ")

    if len(phrase)==0:
        print("¡ERROR!")
    elif len(phrase)==4:
        print(f"{phrase}!")
    else:
        print(f"{phrase}?")
    
#Ejercicio 2
import random
words=["caja","hola","gato","auto"]
select_word=random.choice(words)
letters=[]
max_attempts=6
attempts=0
print("¡HOLA!\nAdivina la palabra oculta, solo tienes 5 intentos\n¡A JUGAR!")

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

#Ejercicio 3
phrase=input("Ingrese una frase: ")
empty=0

for letter in phrase:
    if letter==" ":
        empty+=1

print(f"La frase ingresada tiene {empty+1} palabras")

#Ejercicio 4
salary=0
hours=0
print("Para saber de cuanto es el adicional que le corresponde complete el siguiente formulario")
while salary<=0 or hours<=0:
    salary=float(input("Ingrese el valor de su salario: "))
    hours=str(input("Ingrese cuantas horas trabajó los domingos: "))
    month_worked=""
    
    while month_worked!="s" or month_worked!="n":
        month_worked=input("Ingrese si trabajo el mes completo o no (Ingrese \"S\" por si o \"N\" por no): ")
        month_worked=month_worked.lower()
        
        if month_worked!="s" or month_worked!="n":
            print("Ingrese un valor válido")
        else:
            break

    if salary<0 or hours<0:
        print("¡ERROR! Ingrese valores válidos")
    elif month_worked=="s" and hours>=3 and hours<=5:
        additional=(3*salary)/100
        total=salary+additional
        print(f"Usted trabajó el mes completo y {hours} horas los domingos. Le corresponde un adicional del 3%\nSu sueldo total es de ${total}")
    elif month_worked=="s" and hours>=6 and hours<=10:
        additional=(10*salary)/100
        total=salary+additional
        print(f"Usted trabajó el mes completo y {hours} horas los domingos. Le corresponde un adicional del 10%\nSu sueldo total es de ${total}")
    elif month_worked=="n" and hours>=3 and hours<=10:
        additional=(2*salary)/100
        total=salary+additional
        print(f"Usted no trabajó el mes completo pero hizo {hours} horas los domingos. Le corresponde un adicional del 2%\nSu sueldo total es de ${total}")
    else:
        print("A usted no le corresponde adicional")
"""

#Ejercicio 5
num1=float(input("Ingrese un número: "))
num2=float(input("Ingrese otro número: "))

if num1==num2:
    print(f"{num1} es igual a {num2}. Se procede a multiplicar\nRESULTADO: {num1*num2}")
elif num1>num2:
    print(f"{num1} es mayor que {num2}. Se procede a restar\nRESULTADO: {num1-num2}")
else:
    print(f"{num1} es menor que {num2}. Se procede a sumar\nRESULTADO: {num1+num2}")

#Ejercicio 6
print(f"BIENVENIDO A ANSES\nPara saber a que caterogia jubilatoria accederá en 2010 complete el siguiente cuestionario")
age=0
while age<=0:
    age=int(input("¿Cuantos años tiene?: "))
    antiquity=int(input("¿Cuantos años de antiguedad laboral tiene?: "))

    if age<=0:
        print("¡ERROR! Ingrese unnúmero válido")
    elif age>=60 and antiquity<25:
        print("Usted entra en la catgoría \"JUBILACIÓN POR EDAD\"")
    elif age<60 and antiquity>=25:
        print("Usted entra en la catgoría \"JUBILACIÓN POR ANTIGUEDAD JÓVEN\"")
    elif age>=60 and antiquity>=25:
        print("Usted entra en la catgoría \"JUBILACIÓN POR ANTIGUEDAD ADULTA\"")
    else:
        print("Usted aun no reune los requisitos para jubilarse")
        
#Ejercicio 7
salary=0
antiquity=0

while salary<=0 or antiquity<0:
    salary=float(input("Ingrese su salario mensual: "))
    antiquity=int(input("Ingrese la cantida de tiempo que lleva en la empesa (en meses): "))

    if salary<=0 or antiquity<0:
        print("¡ERROR! Ingrese valores válidos para el salario(mayor a cero) y para pa antiguedad (mayor  o igual a cero)")
    elif antiquity<12:
        utility=(salary*5)/100
        total=salary+utility
        print(f"Usted obtiene una utilidad del 5%. Su salario total es de {total}")
    elif antiquity>=12 and antiquity<24:
        utility=(salary*7)/100
        total=salary+utility
        print(f"Usted obtiene una utilidad del 7%. Su salario total es de {total}")
    elif antiquity>=24 and antiquity<60:
        utility=(salary*10)/100
        total=salary+utility
        print(f"Usted obtiene una utilidad del 10%. Su salario total es de {total}")
    elif antiquity>=60 and antiquity<120:
        utility=(salary*15)/100
        total=salary+utility
        print(f"Usted obtiene una utilidad del 15%. Su salario total es de {total}")
    else:
        utility=(salary*20)/100
        total=salary+utility
        print(f"Usted obtiene una utilidad del 20%. Su salario total es de {total}")

"""
        