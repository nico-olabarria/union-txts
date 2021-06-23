

def time_coordination(df):
    import pandas as pd
    ref_route = input("Introduzca la ruta del excel que quiere utilizar como referencia: ")

    ref_df = pd.read_csv(ref_route, sep = ',')

    for i in range(0, len(ref_df), 2):
        pd.to_datetime(ref_df.iloc[:, i])

    print(ref_df.dtypes)

