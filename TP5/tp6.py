"""
#Ejercicio 1
nums_list=[]
num=""

while num!="0":
    num=input("Ingrese un número: ")

    if num=="0":
        break
    else:
        try:
            float_num=float(num)
            nums_list.append(float_num)
        except ValueError:
            print("¡ERROR! Ingrese solo números")
    
print(nums_list)

#Ejercicio 2
user_num=input("Ingrese un número para saber si está en la lista: ")

try:
    float_user_name=float(user_num)
        
    if float_user_name in nums_list:
        nums_list.remove(float_user_name)
        print(f"La primera ocurrencia de {float_user_name} se eliminó de la lista")
    else:
        print("El número no está en la lista")
except ValueError:
    print("¡ERROR! Ingrese solo números") 
print(nums_list)

#Ejercicio 3
sum_num=0
for i in nums_list:
    sum_num+=i
print(sum_num)

#Ejercicio 4
new_num=input("Ingrese otro número: ")
new_list=[]
try:
    float_new_num=float(new_num)
    
    for i in nums_list:
        if i<float_new_num:
            new_list.append(i)
            print(i)
except ValueError:
    print("¡ERROR! Ingrese solo números")

#Ejercicio 5
frequencies={}

for i in nums_list:
    frequencies[i]=frequencies.get(i, 0)+1

new_other_list=list(frequencies.items())
print(new_other_list)
"""
#Ejercicio 6
