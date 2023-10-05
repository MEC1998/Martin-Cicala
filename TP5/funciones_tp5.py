#Ejericio 1
def validation(dni):
    if not dni.isdigit():
        print("El documento ingresado no es válido. Debe contener solo números.")
        return False
    if len(dni) not in [7, 8]:
        print("El número de DNI debe tener 7 u 8 dígitos.")
        return False
    return True
#Ejercicio 2
def last_phrase (phrase):
    words=phrase.split() [-1]
    return words

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
#Ejercicio 10
def aply_discount(prices):
    final_price=0
    shopping_cart=float(input("Ingrese el monto total de su carrito de compra: "))
    if shopping_cart<=0:
        print("¡ERROR! El valor ingresado no es válido")
        aply_discount(prices)
    else:    
        if shopping_cart>=2000 and shopping_cart<4000:
            discount=(shopping_cart*prices[2000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[2000]}%")

        elif shopping_cart>=4000 and shopping_cart<6000:
            discount=(shopping_cart*prices[4000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[4000]}%")

        elif shopping_cart>=6000:
            discount=(shopping_cart*prices[6000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[6000]}%")

        else:
            final_price=shopping_cart
            print(f"Por el monto de su carrito no obtiene ningún descuento")

        return final_price
    
#Ejercicio 11
def aply_function(func, numbers):
    results=[]
    
    for num in numbers:
        results.append(func(num))
    
    return results
def multiply_by_two(num):
    
    return num*2

#Ejercicio 13
import math

def calculate_module(vector):
    x, y, z = vector
    module = math.sqrt(x**2 + y**2 + z**2)
    return module