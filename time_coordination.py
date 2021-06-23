
import pandas as pd

def time_coordination(df):

    ref_route = input("Introduzca la ruta del excel que quiere utilizar como referencia: ")
    variable = input("Introduzca el nombre de la variable tiempo: ")

    ref_df = pd.read_csv(ref_route, sep = ',', parse_dates = [variable])

    print(df.dtypes)

# Simulacion del main

with open("Rutas.txt","r") as route_file:
    rutas = route_file.readlines()

i = 0
for ruta in rutas:
    rutas[i] = ruta.replace("\n", "")
    i += 1

# Lectura de los archivos de texto


with open("Variables.txt", "r") as file:
    variables = file.readlines()

for i in range(0, len(variables)):
    variables[i] = variables[i].replace("\n", "")

df_titles = pd.read_csv(rutas[0],sep = ';', skiprows = 29, nrows = 0, usecols = range(1, 14))

df_rows = pd.read_csv(rutas[0], sep=';', skiprows = 31, nrows = 139, usecols = range(1, 14), names = df_titles.columns,
                      parse_dates = [[variables[0], variables[1]]])

time_coordination(df_rows)