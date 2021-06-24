
import pandas as pd

def time_coordination(df, title):

    ref_route = input("Introduzca la ruta del excel que quiere utilizar como referencia: ")
    variable = input("Introduzca el nombre de la variable tiempo: ")

    ref_df = pd.read_csv(ref_route, sep = ',', parse_dates = [variable], usecols = [0])
    df[title] = df[title].astype('datetime64[s]')
    print(df)
    print(df[title].dtype)
    new_df = pd.DataFrame()

    #list = df.iloc[:, 0].isin(ref_df.iloc[:, 0])
    #print(list)

    #for i in range(0, len(df.index)):
    #    if df.iloc[i, 0].isin(ref_df):
    #        print("La línea " + i + " está dentro")
    #        new_df = new_df.append(df.iloc[i, :])

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

column = variables[0] + "_" + variables[1]

print(column)

df_titles = pd.read_csv(rutas[0],sep = ';', skiprows = 29, nrows = 0, usecols = range(1, 14))

df_rows = pd.read_csv(rutas[0], sep=';', skiprows = 31, nrows = 139, usecols = range(1, 14), names = df_titles.columns,
                      parse_dates = [[variables[0], variables[1]]])

time_coordination(df_rows, column)