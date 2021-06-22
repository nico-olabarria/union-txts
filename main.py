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

df_rows = pd.read_csv(rutas[0], sep=';', skiprows = 31, nrows = 139, usecols = range(1, 14), names = df_titles.columns)
dict_dtypes ={}
for i in range(0, len(df_rows.columns)):
    dict_dtypes[df_rows.columns[i]] = df_rows.iloc[:,i].dtype

for i in range(1, len(rutas)):
    with open(rutas[1],'r') as file:
        num = len(file.readlines())
    df_rows = df_rows.append(pd.read_csv(rutas[1], sep=';', skiprows = 31, nrows = num -32, usecols = range(1, 14),
                                         names = df_titles.columns, dtype = dict_dtypes),
                             ignore_index = True)

# Pasar a CSV

csv_route = input("Introduzca el nombre del archivo al que quiere exportar el .csv")

df_rows.to_csv(csv_route + ".csv", sep = ',')

print(df_rows)