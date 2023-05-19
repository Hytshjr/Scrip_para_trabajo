import os

def dist_maker(file_path, dist_name):
    posicion_ultima_barra = file_path.rfind("/")
    directorio = file_path[:posicion_ultima_barra]
    name_image = file_path[posicion_ultima_barra + 1:]
    ruta_carpeta = directorio+'/'+dist_name

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

file_path = '/home/hytsh/Documentos/App_fazil/test_image'

dist_maker(file_path,'compress')

