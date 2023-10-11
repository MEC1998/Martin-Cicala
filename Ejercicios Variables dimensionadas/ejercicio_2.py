#Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual 
#contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
#*(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, ‘Calle 2 – 741’)+
#Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y 
#retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente 
#puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que 
#contenga cada domicilio una sola vez.

my_clients = [("cliente1", "5", "1234.5", "calle1"),("cliente1", "6", "12.5", "calle1"), ("cliente2", "5", "134.5", "calle2"), ("cliente3", "6", "12300", "calle3") ]
def return_adress(clients):
    adresses = []
    for client in clients:
        adresses.append(client[3])
    adresses = list(set(adresses))
    for adress in adresses:
        print(adress)
return_adress(my_clients)
