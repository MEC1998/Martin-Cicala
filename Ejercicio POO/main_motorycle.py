from motorcycle import Motorcycle

moto1=Motorcycle(
    color="Verde",
    enrollment="LML666",
    fuel_liters=10,
    number_wheels=2,
    mark="Kawasaki",
    model="Z400",
    manuf_date="2023-24-10",
    max_speed=180,
    weight=167
)
moto2=Motorcycle(
    color="Negro",
    enrollment="UWU420",
    fuel_liters=10,
    number_wheels=2,
    mark="Yamaha",
    model="FZ16",
    manuf_date="2023-24-10",
    max_speed=130,
    weight=135
)
#Prueba de los métodos de arranque y detención con ambas motocicletas
moto1.start_up()
moto1.start_up()
moto1.stop()
moto1.stop()

#Añadir el atributo "precio" desde fuera de la clase para una de las motocicletas
moto1.prize=1200500
moto2.prize= None
print(f"Precio de moto1: {moto1.prize}")


print(f"Precio moto1= {moto1.check_prize()}")
print(f"Precio moto2= {moto2.check_prize()}")

print(f"El precio de la moto {moto1.mark} {moto1.model} es de {moto1.check_prize()}")

#Repondiendo a la pregunda del trabajo, la moto uno se había definido un precio y largo el precio con el metodo, en cambio la moto2 está vacio, es decir, el precio todavía no está definido.
