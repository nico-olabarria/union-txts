import pandas as pd

with open("Rutas.txt","r") as route_file:
    rutas = route_file.readlines()

i = 0
for ruta in rutas:
    rutas[i] = ruta.replace("\n", "")
    i += 1
    
print(rutas)