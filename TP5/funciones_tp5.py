#EJericio 1
def validation(dni):
    if not dni.isdigit():
        print("El documento ingresado no es válido. Debe contener solo números.")
        return False
    if len(dni) not in [7, 8]:
        print("El número de DNI debe tener 7 u 8 dígitos.")
        return False
    return True

#Ejericicio 3
def dni_validator(dni):
    if not dni.isdigit():
        print("El documento ingresado no es válido. Debe contener solo números.")
        return False
    if len(dni) not in [7, 8]:
        print("El número de DNI debe tener 7 u 8 dígitos.")
        return False
    return True

#Ejercicio 4
def is_multiple(num1,num2):
    if num1%num2==0:
        return True
    else:
        return False

#Ejercicio 5
def media_calculator(maxi,mini):
    media=(maxi+mini)/2
    return media

#Ejercicio 6
def enter_space (phrase):
    new_phrase=""
    for letter in phrase:
        new_phrase+=letter + " "
    return new_phrase

#Ejericicio 7
def fill_list(nums):
    for i in range(5):
        num=float(input("Ingrese un número: "))
        nums.append(num)
    return nums

def number_comparator(nums):
    max_num=0
    for i in nums:
        if i>max_num:
            max_num=i
    return max_num

#Ejericico 8
import math
def area_per_calculator(radio):
    perimeter=radio*2
    area=math.pi*(radio)**2
    return(print(f"El perímetro de la circunferencia es de {perimeter}cm y el area es de {area}cm2"))

#Ejericicio 9
def login (username, password):
    
    if username=="usuario1" and password=="asdasd":
        return True
    else:
        return False