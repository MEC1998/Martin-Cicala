#Ejercicio 1

def most(x,y):
    if(x>y):
        return x
    else:
        return y
    
def least(a,b):
    if(x<y):
        return x
    else:
        return y
    
x=int(input("Un número: "))
y=int(input("Otro número: "))

print(most(x-3, least(x+2, y-5)))