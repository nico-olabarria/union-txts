import os
import pandas as pd
import pandas.errors


def union_txt(title):
    # Lectura de las rutas de los archivos de texto

    import pandas as pd
    title = "Rutas24.txt"

    with open(title, "r") as route_file:
        rutas = route_file.readlines()

    i = 0

    for ruta in rutas:
        rutas[i] = ruta.replace("\n", "")
        i += 1

    # Lectura de los valores de los archivos

    df_rows = pd.read_csv(rutas[0], sep=';', skiprows=29, low_memory = False)

    df_rows = df_rows.drop(columns=df_rows.columns[0])
    df_rows = df_rows.drop([0])
    df_rows = df_rows.drop(df_rows.tail(1).index)

    # Unificación de los dtypes

    dict_dtypes = {}
    for i in range(0, len(df_rows.columns)):
        dict_dtypes[df_rows.columns[i]] = df_rows.iloc[:, i].dtype

    # Creación de un dataFrame auxiliar

    for i in range(1, len(rutas)):
        try:
            aux_df = pd.read_csv(rutas[i], sep=';', skiprows=29, dtype=dict_dtypes, engine = 'python')
            aux_df = aux_df.drop(columns=aux_df.columns[0])
            aux_df = aux_df.drop([0])
            aux_df = aux_df.drop(aux_df.tail(1).index)
            df_rows = df_rows.append(aux_df, ignore_index=True)
        except pd.errors.EmptyDataError:
            print("Archivo ", rutas[i])

    # Pasar a .csv

    csv_path = input("Introduzca el nombre del producto:") + ".csv"
    df_rows.to_csv(csv_path)
