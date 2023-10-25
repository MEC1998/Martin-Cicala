class Motorcycle:

    status="Nueva"
    motor=False

    def __init__(self, color, enrollment, fuel_liters, number_wheels, mark, model, manuf_date, max_speed, weight):
        self.color=color
        self. enrollment=enrollment
        self.fuel_liters=fuel_liters
        self.number_wheels=number_wheels
        self.mark=mark
        self.model=model
        self.manuf_date=manuf_date
        self.max_speed=max_speed
        self.weight=weight

    def start_up (self):
        if self.motor==False:
            self.motor=True
            print("El motor ha arrancado")
        else:
            print("El motor ya se encuentra en marcha")

    def stop (self):
        if self.motor==True:
            self.motor=False
            print("El motor se ha detenido")
        else:
            print("El motor ya se encuentra detenido")

    def check_prize(self):
        if self.prize!=None:
            return self.prize
        else:
            return "El precio aun no está definido"
        
