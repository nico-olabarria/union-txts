# Importación de librerías

import pandas as pd
import numpy as np
import guardado_rutas as gr
import union_txt as ut

# Listado de las rutas en cada directorio

#route_list = gr.guardado_rutas()

# Unión de todos los archivos en cada directorio

route_list = ["Rutas.txt", "Rutas7.txt", "Rutas11.txt", "Rutas24.txt"]

for archivo in route_list:
    ut.union_txt(archivo)
