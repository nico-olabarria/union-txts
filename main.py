# Importación de librerías
import pandas as pd

# Lectura de las rutas de los archivos de texto
with open("Rutas.txt","r") as route_file:
    rutas = route_file.readlines()

i = 0
for ruta in rutas:
    rutas[i] = ruta.replace("\n", "")
    i += 1

# Lectura de los archivos de texto

df_titles = pd.read_csv(rutas[0],sep = ';', skiprows = 29, nrows = 0, usecols = range(1, 14))
df_rows = pd.read_csv(rutas[0],names = df_titles.columns,sep = ';', skiprows = 31, nrows = 140, usecols = range(1, 14))
print(df_titles)
print(df_rows)