#TRABAJO PRÁCTICO 5
import funciones_tp5
#Ejercicio 1
"""

while True:
    dni = input("Ingrese su N° de DNI: ")
    if funciones_tp5.validation(dni):
        print("El documento ingresado es válido")
        break

#Ejericicio 2
phrase=str(input("Ingrese una frase: ").lower())
print(f"La ultima palabra de su frase es \"{funciones_tp5.last_phrase(phrase)}\"")

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
        
#Ejercicio 10
prices={2000:10, 4000:20, 6000:30}

print(f"El precio final de su carrito es de {funciones_tp5.aply_discount(prices)}")

#Ejercicio 11
numbers=[2,6,10,43,84]

results=funciones_tp5.aply_function(funciones_tp5.multiply_by_two, numbers)

for i in range(len(numbers)):
    print(f"{numbers[i]} multiplicado por 2 es igual a {results[i]}")
"""

#Ejercicio 12

#Ejercicio 13
vector = (3, 4, 5)

module = funciones_tp5.calculate_module(vector)

print("El módulo del vector es:", module)

