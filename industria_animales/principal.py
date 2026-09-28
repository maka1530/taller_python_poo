from animal import Animal
from perro import Perro
from tortuga import Tortuga
from aguila import Aguila

from conejo import Conejo
from tiburon import Tiburon
obj_perro = Perro("Perro", 4, "mediano", "dorado")
obj_tortuga = Tortuga("Tortuga", 12, "pequena", "verde")
obj_aguila = Aguila("Aguila", 6, "grande", "cafe")
obj_conejo = Conejo("Conejo", 2, "pequeno", "blanco")
obj_tiburon = Tiburon("Tiburon", 9, "grande", "gris")

print(obj_perro.moverse())
print(obj_perro.comunicacion())
print(obj_perro.reproduccion())
print(obj_perro.alimentarse())
print(obj_perro.adaptacion())
print(obj_perro.instintos())
print(obj_perro.descanso())
print(obj_perro.sueno())
print(obj_perro.interaccion_social())

print(obj_tortuga.moverse())
print(obj_tortuga.adaptacion())

print(obj_aguila.moverse())
print(obj_aguila.instintos())

print(obj_conejo.moverse())
print(obj_conejo.comunicacion())

print(obj_tiburon.moverse())
print(obj_tiburon.adaptacion())
