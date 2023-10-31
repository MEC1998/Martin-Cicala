#Ejercicio 1
#Definición de la clase Person
class Person:
    #Constructor de la clase con tres atributos: nombre, edad y DNI
    def __init__(self, name="", age="", dni=""):
        self.name=name
        self.age=age
        self.dni=dni

    #Método para validar que el nombre no esté vacío
    def validate_name(self):
        if len(self.name)==0:
            print("¡ERROR! El nombre no puede estar vacío")
            return False
        else:
            return True
    
    #Método para validar que la edad sea mayor o igual a 0
    def validate_age(self):
        if self.age<0:
            print("¡ERROR! La edad no puede ser menor que 0 (cero)")
            return False
        else:
            return True
    
    #Método para validar que el DNI tenga 8 dígitos
    def validate_dni(self):
        if len(self.dni)!=8:
            print("¡ERROR! El DNI debe tener 8 (ocho) dígitos")
            return False
        else:
            return True
    
    #Método para verificar si la persona es mayor de edad (mayor o igual a 18 años)
    def is_of_age(self, age):
        if self.age<18:
            return False
        else:
            return True

#Ejercicio 2
#Definición de la clase Account
class Account:
    #Constructor de la clase con dos atributos: titular y amount
    def __init__(self, titular="", amount=0):
        self.titular=titular
        self.amount=amount

    #Método para validar si el titular de la cuenta no está vacío
    def validate_titular(self):
        if len(self.titular)==0:
            print("¡ERROR! El nombre del titular no puede estar vacío")
            return False
        else:
            return True
    
    #Método para realizar un depósito en la cuenta
    def deposit(self, num):
        if num<=0:
            print("¡ERROR! El monto del depósito debe ser mayor que 0")
        else:
            self.amount+=num
            print("Depósito exitoso.")
            return self.amount
        
    # Método para consultar el saldo actual de la cuenta
    def get_balance(self):
        return self.amount
    
    #Método para realizar un retiro de la cuenta
    def extraction(self, num):
        if num<=0:
            print("¡ERROR! El monto del retiro debe ser mayor que 0")
        elif self.amount<num:
            print("¡ATENCION! Usted está retirando sin saldo a favor")
            self.amount-=num
            return self.amount
        else:
            self.amount-=num
            print("Retiro exitoso.")
            return self.amount
    
    #Método para mostrar el titular y el saldo de la cuenta
    def query_data(self):
        print(f"Titular: {self.titular}\nSaldo en cuenta: {self.amount}")
       
#Ejercicio 3
#Definición de la clase Triangle con atributos side_1, side_2 y side_3
class Triangle:
    #Constructor de la clase con los tres lados del triángulo como parámetros
    def __init__(self, side_1=0, side_2=0, side_3=0):
        self.side_1=side_1  # Inicialización del primer lado
        self.side_2=side_2  # Inicialización del segundo lado
        self.side_3=side_3  # Inicialización del tercer lado

    #Método para determinar el lado más largo del triángulo
    def max_side(self):
        #Utiliza la función max() para encontrar el lado de mayor longitud
        return max(self.side_1, self.side_2, self.side_3)

    #Método para determinar el tipo de triángulo basado en las longitudes de los lados
    def triangle_type(self):
        #Si los tres lados son iguales, el triángulo es equilátero
        if self.side_1==self.side_2==self.side_3:
            return "Equilátero"
        #Si al menos dos lados son iguales, el triángulo es isósceles
        elif self.side_1==self.side_2 or self.side_1==self.side_3 or self.side_2==self.side_3:
            return "Isósceles"
        #En todos los demás casos, el triángulo es escaleno
        else:
            return "Escaleno"
       
#Ejercicio 4
class Contact:
    def __init__(self, name, phone, email):
        # Constructor para la clase Contact, inicializa los atributos name, phone y email.
        self.name = name
        self.phone = phone
        self.email = email

class Agenda:
    def __init__(self):
        # Constructor para la clase Agenda, inicializa una lista vacía para almacenar contactos.
        self.contacts = []

    def add_contact(self, name, phone, email):
        try:
            # Intenta crear un nuevo objeto Contact y añadirlo a la lista de contactos.
            new_contact = Contact(name, phone, email)
            self.contacts.append(new_contact)
            print(f"Contacto {name} añadido exitosamente.")
        except ValueError:
            # Maneja un ValueError si se ingresan datos inválidos.
            print("Error: Por favor, ingrese datos válidos.")

    def list_contacts(self):
        # Muestra la lista de contactos en la agenda.
        print("Lista de contactos:")
        for contact in self.contacts:
            print(f"Nombre: {contact.name}, Teléfono: {contact.phone}, Correo: {contact.email}")

    def search_contact(self, name):
        found = False
        # Busca un contacto por nombre y muestra sus detalles si se encuentra.
        for contact in self.contacts:
            if contact.name == name:
                print(f"Nombre: {contact.name}, Teléfono: {contact.phone}, Correo: {contact.email}")
                found = True
                break
        if not found:
            print(f"Contacto {name} no encontrado.")

    def edit_contact(self, name, new_phone, new_email):
        found = False
        # Busca un contacto por nombre y actualiza su teléfono y correo si se encuentra.
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                print(f"Contacto {name} editado exitosamente.")
                found = True
                break
        if not found:
            print(f"Contacto {name} no encontrado.")

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Agregar contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            option = input("Seleccione una opción: ")

            if option == "1":
                name = input("Ingrese el nombre del contacto: ")
                phone = input("Ingrese el teléfono del contacto: ")
                email = input("Ingrese el correo del contacto: ")
                self.add_contact(name, phone, email)
            elif option == "2":
                self.list_contacts()
            elif option == "3":
                name = input("Ingrese el nombre del contacto a buscar: ")
                self.search_contact(name)
            elif option == "4":
                name = input("Ingrese el nombre del contacto a editar: ")
                new_phone = input("Ingrese el nuevo teléfono del contacto: ")
                new_email = input("Ingrese el nuevo correo del contacto: ")
                self.edit_contact(name, new_phone, new_email)
            elif option == "5":
                print("Agenda cerrada. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida del menú.")
