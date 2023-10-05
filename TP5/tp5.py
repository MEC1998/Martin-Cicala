#TRABAJO PRÁCTICO 5
import funciones_tp5
#Ejercicio 1
"""

while True:
    dni = input("Ingrese su N° de DNI: ")
    if funciones_tp5.validation(dni):
        print("El documento ingresado es válido")
        break
"""

#Ejericicio 2


"""

#Ejericico 3
print("BIENVENIDO\nPara registrarse siga los pasos")

nombre = input("Ingrese su nombre (de a uno por vez): ")
nombre2 = input("Si posee otro nombre ingréselo, en caso contrario oprima ENTER: ")
apellido = input("Ingrese su apellido: ")

while True:
    dni = input("Ingrese su N° de DNI: ")
    if funciones_tp5.dni_validator(dni):
        break

print(f"Nombre: {nombre} {nombre2} {apellido}")
print(f"DNI: {dni}")
print(f"ID: {nombre}{len(apellido)}{dni[:3]}")

#Ejercicio 4
num1=int(input("Ingrese un número entero: "))
num2=int(input("Ingrese otro número entero: "))

if funciones_tp5.is_multiple(num1,num2):
    print(f"{num1} es multiplo de {num2}")
else:
    print(f"{num1} no es multiplo de {num2}")

#Ejercicio 5
days=int(input("Ingrese la cantidad de días que quiere calcular: "))

for i in range(days):
    maxi_tem=float(input("Ingrese la temperatura máxima(en °C sin el símbolo\"°\"): "))
    mini_tem=float(input("Ingrese la temperatura minima(en °C sin el símbolo\"°\"): "))
    media=funciones_tp5.media_calculator(maxi_tem,mini_tem)
    print(f"La temperatura media del día {i+1} fue de {media}°")

#Ejercicio 6
phrase=input("Ingrese una frase: ")

print(funciones_tp5.enter_space(phrase))

#Ejercicio 7
nums=[5]
print(f"{funciones_tp5.number_comparator(funciones_tp5.fill_list(nums))} es el mayor número ingresado")

#Ejericicio 8
radio=float(input("Ingrese el valor del radio de una circunferencia (en centimetros): "))
funciones_tp5.area_per_calculator(radio)

#Ejericicio 9
attempt=3

while attempt>0:
    username=input("Ingrese su usuario: ")
    password=input("Ingrese la clave: ")

    if funciones_tp5.login(username,password):
        print("¡BIENVENIDO!")
        break
    else:
        attempt-=1
        print(f"Inicio de sesión fallido. Intentos restantes: {attempt}")

if attempt==0:
    print("Has agotado tus intentos")
"""
        
#Ejericicio 10
