#Ejercicio 1
from tp9 import Person  #Importa la clase Person desde el módulo tp9

#Crea una instancia de la clase Person sin proporcionar valores iniciales
user1=Person()

#Muestra los atributos de la instancia antes de ingresar los datos
print(f"Nombre: {user1.name}\nEdad: {user1.age}\nDNI: {user1.dni}")

#Solicita y valida el nombre del usuario
while True:
    user1.name=input("Ingrese su nombre: ")
    if user1.validate_name()==True:
        break

#Solicita y valida la edad del usuario
while True:
    try:
        user1.age=int(input("Ingrese su edad: "))
        if user1.validate_age()==True:
            break
    except ValueError:
        print("¡ERROR! Ingrese un número válido")

#Solicita y valida el DNI del usuario
while True:
    try:
        user1.dni=(input("Ingrese su DNI: "))
        if user1.validate_dni()==True:
            user1.dni=int(user1.dni)
            break
    except ValueError:
        print("¡ERROR! Ingrese un número válido")

#Muestra los atributos de la instancia después de ingresar los datos
print(f"Nombre: {user1.name}\nEdad: {user1.age}\nDNI: {user1.dni}")

#Comprueba si el usuario es mayor de edad y muestra un mensaje correspondiente
if user1.is_of_age(user1.age)==True:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#Ejercicio 2
#Importación de la clase Account desde el archivo tp9.py
from tp9 import Account

#Creación de un objeto de la clase Account
user1=Account()

#Solicitar el nombre del titular de la cuenta
while True:
    user1.titular=input("Ingrese su nombre: ")
    if user1.validate_titular()==True:
        break

#Menú para realizar operaciones en la cuenta (depósito, retiro, consulta o salir)
while True:
    action=input("¿Qué operación desea realizar?\nPara realizar un depósito oprima 1\nPara realizar un retiro oprima 2\nPara realizar una consulta oprima 3\nPara salir oprima cualquier tecla: ")

    if action=="1":
        #Realizar un depósito en la cuenta
        while True:
            try:
                deposit_successful=False
                while True:
                    num=float(input("¿Cuánto desea depositar?: "))
                    if num<=0:
                        print("¡ERROR! Ingrese un número válido (mayor que 0)")
                    else:
                        new_balance=user1.deposit(num)
                        print(f"Saldo actual: {new_balance}")
                        deposit_successful=True
                        break
                if deposit_successful:                    
                    break
            except ValueError:
                print("¡ERROR! Ingrese un número válido")
    elif action=="2":
        #Realizar un retiro de la cuenta
        while True:
            try:
                extraction_successful=False
                while True:
                    num=float(input("¿Cuánto desea retirar?: "))
                    if num<=0:
                        print("¡ERROR! Ingrese un número válido (mayor que 0)")
                    else:
                        new_balance=user1.extraction(num)
                        if new_balance>=0:
                            print(f"Saldo actual: {new_balance}")
                            extraction_successful=True
                            break
                        else:
                            print(f"Saldo actual: {new_balance}\n¡ATENCION! Usted está en números rojos")
                            extraction_successful=True
                            break
                if extraction_successful:                    
                    break
            except ValueError:
                print("¡ERROR! Ingrese un número válido")
    elif action=="3":
        #Consultar datos de la cuenta
        user1.query_data()
    else:
        #Salir del programa
        break

print("Saliendo del sistema...")

#Ejercicio 3
#Importación de la clase Triangle desde el módulo tp9
from tp9 import Triangle

#Bucle principal para solicitar los valores de los lados del triángulo al usuario
while True:
    try:
        #Solicita al usuario ingresar los valores de los tres lados del triángulo
        side_1=float(input("Ingrese el valor del primer lado: "))
        side_2=float(input("Ingrese el valor del segundo lado: "))
        side_3=float(input("Ingrese el valor del tercer lado: "))

        #Crea una instancia de la clase Triangle con los valores ingresados
        triangle_1=Triangle(side_1, side_2, side_3)

        #Calcula el lado más largo y el tipo de triángulo utilizando los métodos de la clase
        larger_side=triangle_1.max_side()
        type_of_triangle=triangle_1.triangle_type()

        #Imprime el lado más largo y el tipo de triángulo
        print(f"Valor del lado más largo: {larger_side}\nTipo de triángulo: {type_of_triangle}")

        break  #Sale del bucle si se ingresan valores válidos

    except ValueError:
        #Captura la excepción si se ingresan valores no numéricos y muestra un mensaje de error
        print("¡ERROR! Ingrese números válidos")

#Ejercicio 4
# Importando las clases Contact y Agenda desde el módulo tp9.
from tp9 import Contact, Agenda

# Creando una instancia de la clase Agenda.
my_agenda = Agenda()

# Iniciando el menú de la agenda.
my_agenda.menu()
