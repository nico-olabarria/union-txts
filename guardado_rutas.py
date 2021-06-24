# Importación librerías

import os
import shutil
import pandas as pd

def ordenado_ficheros():
    """
    Esta función crea un directorio donde copia todos los archivos de un mismo producto
    :return:
        No devuelve nada
    """

    option = input("¿Quiere ordenar los archivos en carpetas?[y/n]: ")

    while option.upper() != 'Y' and option.upper() != 'N':
        print("Opción no válida inténtelo de nuevo.")
        option = input("¿Quiere ordenar los archivos en carpetas?[y/n]: ")

    if option.upper() == 'Y':
        ruta = input("Introduzca la ruta de los archivos a ordenar: ")

        # Chequeo de que la ruta exista

        while os.path.exists(ruta) == False:
            print("Ruta no válida, inténtalo de nuevo.")
            ruta = input("Introduzca la ruta de los archivos a ordenar: ")

        # Listado de los archivos en el directorio

        file_list = pd.Series(os.listdir(ruta))
        print("Los archivos en el directorio son: \n %s" % file_list)

        # Copiado de archivos

        nombre_archivo = input("Introduzca el nombre del producto que quiere copiar al directorio: ")

        i = 0

        archivos_a_copiar = []

        for archivo in file_list:
            result = file_list.str.contains(nombre_archivo)
            if result[i] == True:
                print(nombre_archivo, " encontrado en el archivo ", archivo)
                archivos_a_copiar.append(archivo)
            i += 1
        # Creacion del directorio donde guardar los archivos

        try:
            directorio = input("Introduzca la carpeta donde quiere crear el directorio: ")
            directorio = directorio + '\\' + nombre_archivo
            os.mkdir(directorio)
        except OSError:
            print("No se pudo crear el directorio")
        else:
            print("Creado correctamente en: ", directorio)

        for archivo in archivos_a_copiar:
            archivo = ruta + "\\" + archivo
            shutil.copy(archivo,directorio)

def guardado_rutas():
    """
    Esta función coge los archivos de un directorio y los lista en un archivo de texto. Además, devuelve una lista con
    los títulos de los archivos que ha listado.
    :return:
        route_list : lista con los nombres de los archivos del directorio.
    """

    i = 0 

    # Introducción de la ruta que se quiere listar

    ruta = input("Introduce la ruta donde estén los archivos que quieres listar: ")
    
    # Creación de una lista vacía para rellenar con los nombres de los ficheros que contienen las rutas
    route_list = []

    while True:

        # Definición del título del archivo de rutas

        if i == 0:
            title = "Rutas.txt"
        else:
            title = "Rutas" + str(i) + ".txt"

        route_list.append(title)

        with open(title,'w+') as file:
            for i in range(0,len(os.listdir(ruta))):
                file.writelines(ruta + '\\' + os.listdir(ruta)[i] + '\n')

        option = input("¿Quiere seguir introduciendo ficheros?[y/n]: ")
        while option.upper() != 'Y' and option.upper() != 'N':
            print("Opción no válida inténtelo de nuevo.")
            option = input("¿Quiere seguir introduciendo ficheros?[y/n]: ")

        if option.upper() == 'N':
            break
        elif option.upper() == 'Y':
            ruta = input("Introduce la ruta donde estén los archivos que quieres listar: ")
            i += 1
        


    return route_list