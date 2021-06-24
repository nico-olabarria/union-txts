# Importación librerías

import os

def guardado_rutas():

    i = 0 

    # Introducción de la ruta que se quiere listar

    ruta = input("Introduce la ruta donde estén los archivos que quieres listar: ")
    
    # Creación de una lista vacía para rellenar con los nombres de los ficheros que contienen las rutas
    route_list = []

    while True:

        # Definición del título del archivo de rutas

        if i = 0:
            title = "Rutas.txt"
        else:
            title = "Rutas" + str(i) + ".txt"

        route_list.append(title)

        with open(title,'w+') as file:
            for i in range(0,len(os.listdir(ruta))):
                file.writelines(ruta + '\\' + os.listdir(ruta)[i] + '\n')

        option = input("¿Quiere seguir introduciendo ficheros?[y/n]: ")
        while option.upper != 'Y' and option.upper != 'N':
            print("Opción no válida inténtelo de nuevo.")
            option = input("¿Quiere seguir introduciendo ficheros?[y/n]: ")
        
        if option.upper == 'N':
            break
        
        i += 1

    return route_list   