import pandas as pd

def time_coordination(df):

    ref_route = input("Introduzca la ruta del excel que quiere utilizar como referencia: ")

    ref_df = pd.read_csv(ref_route, sep = ',')
    

