#  TRABAJO PRÁCTICO N°2

#Ejercicio 1 y 2
anios_comp=int(input("Ingrese la cantidad de años que tiene su computadora: "))

if anios_comp<0:
    print("¡ERROR! Ingrese un número válido")
elif anios_comp<=2:
    print("El computador es nuevo")
else:
    print("El computador es viejo")

#Ejercicio 3
nombre1=str(input("Usuario 1, ingrese su nombre: "))
nombre2=str(input("Usuario 2, ingrese su nombre: "))

nombre1=nombre1.lower()
nombre2=nombre2.lower()

if nombre1[0]==nombre2[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

#Ejercicio 4
print("BIENVENIDO AL SISTEMA DE VOTO ELECTRÓNICO")
print("Oprima A para votar por el Partido Rojo")
print("Oprima B para votar por el Partido  Verde")
print("Oprima C para votar por el Partido Azul")
voto=input("Ingrese su voto: ")

voto=voto.upper()

if voto=="A":
    print("Usted ha votado por el candidato A, del Partido Rojo")
elif voto=="B":
    print("Usted ha votado por el candidato B, del Partido Verde")
elif voto=="C":
    print("Usted ha votado por el candidato C, del Partido Azul")
else:
    print("Opción erronea")

#Ejercicio 5
letra=str(input("Ingrese una letra: "))

letra=letra.lower()

if len(letra)==1:
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        print("Es vocal")
    else:
        print("No es vocal")
else:
    print("No se puede procesar los datos, ingrese una sola letra")

#Ejercicio 6
anio=int(input("Ingrese un año para saber si es o no bisiesto: "))

if anio%4==0:
    if anio%100!=0:
        print(anio,"es bisiesto")
    else:
        if anio%400==0:
            print(anio,"es bisiesto")
        else:
            print(anio,"no es bisiesto")
else:
    print(anio,"no es bisiesto")

#Ejercicio 7
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))

if num1<num2:
    if num1<num3:
        print("El menor número es", num1)
    else:
        print("El menor número es", num3)
elif num2<num3:
    print("El menor número es", num2)
else:
    print("El menor número es", num3)

#Ejercicio 8
usuario=str(input("Ingrese su nombre de usuario: "))
clave=str(input("Ingrese su contraseña: "))

usuario=usuario.lower()

if usuario=="gwenevere" and clave=="excalibur":
    print("Usuario y contraseña correctos. Puede entrar a Camelot")
else:
    print("Acceso denegado")

#Ejercicio 9
nombre=str(input("Ingrese la primer letra de su nombre: "))
sexo=str(input("Ingrese su sexo, siendo H para hombre y M para mujer: "))

nombre=nombre.upper()
sexo=sexo.upper()

if nombre<"M" and sexo=="M" or nombre>"N" and sexo=="H":
    print("GRUPO A")
elif nombre>="M" and sexo=="M" or nombre<="N" and sexo=="H":
    print("GRUPO B")
else:
    print("Error al ingresar los datos")

#Ejercicio 10
print("BIENVENIDO")
edad=int(input("¿Cuantos años tiene?: "))

if edad<0:
    print("ERROR, ingrese un número válido")
elif edad>0 and edad<4:
    print("Puede ingresar gratis!")
elif edad>=4 and edad<18:
    print("El valor de su estrada es de $500")
else:
    print("El valor de su entrada es de $1000")

#Ejercicio 11
print("BIENVENIDO A BELLA NAPOLI")
pizza=str(input("¿Desea ordenar la opción vegetariana? Oprima \"S\" para si y cualquier tecla para no: "))
pizza=pizza.lower()
print("Todas nuestras pizzas cuentan como ingredientes base mozzarella y tomate")

if pizza=="s":
    print("INGREDIENTES VEGETARIANOS\n-Pimiento(1)\n-Tofu(2)")
    ingrediente=str(input("Ingrese un ingrediente que desee agregar colocando el número que figura al lado del mismo. Solo puede ingresar 1 solo ingrediente: "))
    if ingrediente=="1":
        print("Eligió una pizza vegetariana con Mozzarella, Tomate y Pimiento")
    elif ingrediente=="2":
        print("Eligió una pizza vegetariana con Mozzarella, Tomate y Tofu")
    else:
        print("Ingrediente inválido")
else:
    print("INGREDIENTES NO VEGETARIANOS\n-Peperoni(1)\n-Jamón(2)\n-Salmón(3)")
    ingrediente=str(input("Ingrese un ingrediente que desee agregar colocando el número que figura al lado del mismo. Solo puede ingresar 1 solo ingrediente: "))
    if ingrediente=="1":
        print("Eligió una pizza no vegetariana con Mozzarella, Tomate y Peperoni")
    elif ingrediente=="2":
        print("Eligió una pizza no vegetariana con Mozzarella, Tomate y Jamón")
    elif ingrediente=="3":
        print("Eligió una pizza no vegetariana con Mozzarella, Tomate y Salmón")
    else:
        print("Ingrediente inválido")

#Ejercicio 12
anio_actual=int(input("Ingrese el año actual (en números): "))
anio=int(input("Ingrese un año cualquiera (Si es un año A.C ingreselo como negativo, en números): "))

if anio<0:
    resultado=anio_actual+abs(anio)
    print("Han pasado", resultado, "años desde el", abs(anio), "A.C")
else:
    if anio<anio_actual:
        resultado=anio_actual-anio
        print("Han pasado", resultado, "años desde el", anio)
    else:
        resultado=anio-anio_actual
        print("Faltan", resultado, "años para que sea", anio)
        
#Ejercicio 13
num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese un segundo número: "))

if num1<0 or num2<0:
    print("ERROR, ingrese números positivos distintos de 0 (cero)")
elif num1==0 or num2==0:
    print("ERROR, ingrese números positivos distintos de 0 (cero)")
else:    
    if num1>num2:
        if num1%num2==0:
            print(num1, "es múltipliplo de", num2)
        else:
            print(num1, "no es múltiplo de", num2)
    else:
        if num2%num1==0:
            print(num2, "es múltipliplo de", num1)
        else:
            print(num2, "no es múltiplo de", num1)

#Ejercicio 14
a=float(input("Ingrese un valor para el coeficiente \"a\": "))
b=float(input("Ingrese un valor para el coeficiente \"b\": "))

if a==0:
    if b==0:
        print("La ecuación tiene infinitas soluciones")
    else:
        print("La ecuación no tiene solución")
else:
    x=-b/a
    print(f"La solución de la ecuación es x={x}")

#Ejercicio 15
area=str(input("Oprima \"T\" si desea calcular el área de un tríangulo, u oprima \"C\" si desea calcular el área de un círculo: "))

area=area.lower()

if area=="t":
    b=float(input("Ingrese el valor (en cm) de la base: "))
    h=float(input("Ingrese el valor (en cm) de la altura: "))
    area_t=(b*h)/2
    print("El area es igual a", area_t,"cm2")
elif area=="c":
    r=float(input("Ingrese el valor (en cm) del radio: "))
    area_c=3.1416*(r**2)
    print("El area es igual a", area_c,"cm2")
else:
    print("ERROR")

#Ejercicio 16
a=float(input("Ingrese el primer número:"))
op=int(input(("¿Que operación desea realizar?\nPulse 1 para sumar\nPulse 2 para restar\nPulse 3 para multiplicar\nPulse 4 para dividir\n: ")))
b=float(input("Ingrese el segundo número: "))

if op==1:
    resultado=a+b
    print("El resultado de la suma es", resultado)
elif op==2:
    resultado=a-b
    print("El resultado de la resta es", resultado)
elif op==3:
    resultado=a*b
    print("El resultado de la multiplicación es", resultado)
elif op==4:
    if b==0:
        print("No se puede dividir por 0 (cero)")
    else:
        resultado=a/b
        print("El resultado de la división es", resultado)
else:
    print("ERROR, operador inválido")

#Ejercicio 17
dia=str(input("Ingrese un día de la semana: "))
dia=dia.upper()

if dia=="LUNES":
    print("BUEN COMIENZO DE SEMANA!")
elif dia=="VIERNES":
    print("VAMOS QUE SE TERMINA LA SEMANA, ÚLTIMO EMPUJÓN!")
elif dia=="SABADO" or dia=="DOMINGO":
    print("FINALMENTE EL MERECIDO DESCANSO, BUEN FIN DE SEMANA!")
elif dia=="MARTES" or dia=="MIERCOLES" or dia=="JUEVES":
    print("FELIZ", dia,"!!!")
else:
    print("QUIZÁS METISTE MAL EL DEDO, NO CONOZCO ESE DÍA")

#Ejercicio 18
horas=float(input("Ingrese la cantidad de horas trabajadas en el mes: "))
salario=float(input("Ingrese su salario por hora: "))

if horas>48:
    horas_extra=horas-48
    salario_extra=horas_extra*(salario*0.1)
    salario_total=(horas*salario)+salario_extra
    print("Usted trabajó", horas_extra,"horas extra.\nSu salario total es de $",salario_total)
else:
    salario_total=horas*salario
    print("Su salario es de $", salario_total)

#Ejercicio 19
print("BIENVENIDO\n¡7% de descuento en compras de 1000 (mil) unidades o más!\nCosto por unidad (sin descuento) $60")
lapices=int(input("Ingrese la cantidad de lapices que desea comprar: "))

if lapices>=1000:
    costo=lapices*60
    descuento=7*costo/100
    costo_final=costo-descuento
    print("El valor final de su compra es de $", costo_final)
else:
    costo_final=lapices*60
    print("El valor final de su compra es de $", costo_final)
    
#Ejercicio 20
nota1=float(input("Ingrese la primer nota: "))
nota2=float(input("Ingrese la segunda nota: "))
nota3=float(input("Ingrese la tercer nota: "))
nota4=float(input("Ingrese la cuarta nota: "))

if nota1<=0 or nota1>10 or nota2<=0 or nota2>10 or nota3<=0 or nota3>10 or nota4<=0 or nota4>10:
    print("ERROR, hay una o más notas con valores inálidos\nIngrese solo valores positivos, entre 1 y 10")
else:
    promedio=(nota1+nota2+nota3+nota4)/4
    if promedio>=6:
        print("Su promedio es de", promedio)
        print("APROBADO")
    else:
        print("Su promedio es de", promedio)
        print("DESAPROBADO")