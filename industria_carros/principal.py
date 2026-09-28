from carro import Carro
from carro_electrico import CarroElectrico
from carro_taxi import CarroTaxi
from carro_todoterreno import CarroTodoterreno

obj_carro_electrico = CarroElectrico("Sedan electrico", "azul", "electrico", 4, 5)
obj_carro_taxi = CarroTaxi("Taxi urbano", "amarillo", "1.6", 4, 5)
obj_carro_todoterreno = CarroTodoterreno("Campero 4x4", "verde", "3.2", 4, 5)

print(obj_carro_electrico.arrancar())
print(obj_carro_electrico.acelerar_y_frenar("acelerar", 80))
print(obj_carro_electrico.acelerar_y_frenar("frenar", 30))
print(obj_carro_electrico.apagar())
print(obj_carro_electrico.sistema_direccion("asistida"))
print(obj_carro_electrico.climatizacion("encendida"))
print(obj_carro_electrico.tipo_seguridad())
print(obj_carro_electrico.luces("encendidas"))
print(obj_carro_electrico.sistema_ventanas("abiertas"))
print(obj_carro_electrico.sistema_espejo("ajustados"))

print(obj_carro_taxi.arrancar())
print(obj_carro_taxi.sistema_ventanas("cerradas"))
print(obj_carro_taxi.tipo_seguridad())

print(obj_carro_todoterreno.arrancar())
print(obj_carro_todoterreno.sistema_espejo("ajustados"))
print(obj_carro_todoterreno.sistema_direccion("asistida"))
