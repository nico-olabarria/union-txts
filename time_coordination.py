

def time_coordination(df):
    import pandas as pd
    ref_route = input("Introduzca la ruta del excel que quiere utilizar como referencia: ")
    variable = input("Introduzca el nombre de la variable tiempo: ")
    ref_df = pd.read_csv(ref_route, sep = ',', parse_dates = [variable])
    print(ref_df.dtypes)
    
