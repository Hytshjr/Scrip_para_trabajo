from tkinter import messagebox as MessageBox
from Fazil.gui_app import Frame as fr
from tkinter import filedialog
import tkinter as tk
import numpy as np
import fileinput
import tinify
import glob
import time
import cv2
import os


def get_path(archivo = True):
    if archivo == True:
        file_path = filedialog.askopenfilename()
        return file_path
    
    elif archivo == False:
        file_path = filedialog.askdirectory()
        return file_path

    
def dist_maker(file_path, dist_name, ruta_herencia = True):
    if ruta_herencia == True:
        posicion_ultima_barra = file_path.rfind("/")
        directorio = file_path[:posicion_ultima_barra]
        name_image = file_path[posicion_ultima_barra + 1:]
        ruta_carpeta = directorio+'/'+dist_name

        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
            return ruta_carpeta
        
        else:
            return ruta_carpeta

    else:
        if not os.path.exists(file_path+'/'+dist_name):
            os.makedirs(file_path+'/'+dist_name)
            return file_path+'/'+dist_name
        
        elif os.path.exists(file_path+'/'+dist_name):
            return file_path+'/'+dist_name


def descomprimir(path):
    extention = path[path.rfind('.'):]
    carpeta = path[:path.rfind('/')]
    nombre = path[path.rfind('/')+1:-4]
    
    if extention == '.zip':
        import zipfile
        import os

        nombre_space = nombre.replace('_',' ')
        nombre_space = nombre_space.replace('-',' ')
        nopmbre_split = nombre_space.split()

        with zipfile.ZipFile(path,'r') as zf:
            zf.extractall(path=carpeta)
            os.remove(path)

        archivos = os.listdir(carpeta)
        images_count = 0

        for archivo in archivos:
            if archivo[archivo.rfind('.'):] == '.png' or archivo[archivo.rfind('.'):] == '.jpg':
                images_count += 1

        if images_count != 1:
            MessageBox.showwarning("Error",
                "Existe màs de una imagen en el comprimido, usa seleccion manual")
            
            file_path = get_path()
            return file_path
        
        elif images_count == 1:
            for archivo in archivos:
                name_validation = 0

                for word in nopmbre_split:
                    if word in archivo:
                        name_validation += 1
                    
                if name_validation >= len(nopmbre_split)-2 and archivo[archivo.rfind('.'):] == '.png' or archivo[archivo.rfind('.'):] == '.jpg':
                    return carpeta+'/'+archivo 


    elif extention == '.rar':
        import rarfile

        with rarfile.RarFile(path) as rf:
            rf.extractall(path=(carpeta))
            os.remove(path)

        archivos = os.listdir(carpeta)
        images_count = 0

        for archivo in archivos:
            if archivo[archivo.rfind('.'):] == '.png' or archivo[archivo.rfind('.'):] == '.jpg':
                images_count += 1

        if images_count != 1:
            MessageBox.showwarning("Error",
                "Existe màs de una imagen en el comprimido, usa seleccion manual")
            
            file_path = get_path()
            return file_path
        
        elif images_count == 1:
            for archivo in archivos:
                name_validation = 0

                for word in nopmbre_split:
                    if word in archivo:
                        name_validation += 1
                    
                if name_validation >= len(nopmbre_split)-2 and archivo[archivo.rfind('.'):] == '.png' or archivo[archivo.rfind('.'):] == '.jpg':
                    return carpeta+'/'+archivo    

    else:
        return path


def buscador(archivo, etiqueta, final_content = -2):
    import fileinput

    with fileinput.FileInput(archivo, inplace=False) as file:
                for line in file:
                    if etiqueta in line:
                        key = line[line.rfind('=')+2:final_content]
    
    return key



class Editor:
    def __init__(self, root = None, path = None):
        
        self.root = root
        self.path = path
    

    def cut_image(self):
        def mouse_track(event,x,y,flags,param):
            nonlocal size_img
            nonlocal pxl_save
            nonlocal img_pos
            global rect_pts
            nonlocal count


            if event == cv2.EVENT_MBUTTONDOWN:
                img_pos -= 50  # Ajusta la cantidad de desplazamiento Arriba

                
            if event == cv2.EVENT_MOUSEWHEEL:
                if flags < 0:
                    img_pos += 50     # Ajusta la cantidad de desplazamiento 


            if count == 0:
                if event == cv2.EVENT_LBUTTONDOWN:
                    rect_pts = [(x, y)]  

                    rect_pts.append((size_img[1],0))  #Estos son el ancho "size_img[1]" y el 0 es el top(la primera altura de la imagen)
                    rect_pts[0] = (0,rect_pts[0][1]+img_pos) #Estos son el inicio lateral de la imagen y la parte mas baja que seleccionamos

                    cv2.rectangle(imagen, rect_pts[0], rect_pts[1], (0, 255, 0))
        
                    pxl_save.append((0,rect_pts[0][1]))

                    count += 1 
                    
                
            else:
                if event == cv2.EVENT_LBUTTONDOWN:
                    bottom_size = rect_pts[0][1] #Esto guarda la altura de la linea anterior y lo usa como tope para esta
                    rect_pts[1] = (size_img[1],bottom_size)

                    rect_pts[0] = (x, y)
                    rect_pts[0] = (0,rect_pts[0][1]+img_pos)
                    rect_pts[1] = (size_img[1],bottom_size)

                    cv2.rectangle(imagen, rect_pts[0], rect_pts[1], (0, 255, 0))
                    
                    pxl_save.append((bottom_size,rect_pts[0][1]))
                    
                    count += 1 
                
            cv2.imshow("Imagen", imagen[img_pos:img_pos+window_height, :])

        try:
            # Declaramos las variables de guia e iniciamos la funcion para el mouse
            file_path = get_path()
            file_path = descomprimir(file_path)
            imagen = cv2.imread(file_path)

            copy_image = imagen.copy()
            size_img = imagen.shape

            if size_img != None:
                MessageBox.showwarning("Tamaño", 
                f"La altura es de: {size_img[0]} y el ancho es de {size_img[1]}")

            pxl_save = []

            window_height = 1080
            img_pos = 0
            count = 0
            cerrar = False

            # cv2.namedWindow('Imagen')
            cv2.imshow('Imagen', imagen)
            cv2.setMouseCallback('Imagen',mouse_track)  


            # Esto guarda y limpia la mesa de trabajo
            while True:
                k = cv2.waitKey(1)

                if k == ord('l'): # Limpiar el contenido de la imagen
                    imagen = cv2.imread(file_path)
                    pxl_save = []
                    count = 0
                
                elif k == 27: # Limpiar el contenido de la imagen
                    cerrar = True
                    cv2.destroyAllWindows()
                    break

                elif k == ord('s'):
                    cv2.destroyAllWindows()
                    break
                
            size_cut = len(pxl_save)
    
            count_cut = 0
            imageOut = []

            if cerrar == True:
                pass

            elif cerrar == False:
                while count_cut < size_cut:

                    top = pxl_save[count_cut][0] #Define o indica la altura del corte
                    right = size_img[1] #Define el ancho de la imagen
                    bottom = pxl_save[count_cut][1] #Define el pixel que hemos seleccionado con el mouse para hacer el corte

                    imageOut.append(copy_image[top:bottom, 0:right])

                    count_cut += 1
                
                with fileinput.FileInput('info.txt', inplace=False) as file:
                    for line in file:
                        if 'last' in line:
                            last = line[line.rfind('=')+2:-2]

                if last == 'True':
                    imageOut.append(copy_image[bottom:size_img[0], 0:right])

                posicion_ultima_barra = file_path.rfind("/")
                directorio = file_path[:posicion_ultima_barra]
                name_image = file_path[posicion_ultima_barra + 1:-4]
                ruta_carpeta = directorio+'/images'

                self.path = ruta_carpeta

                for index in range(len(imageOut)):

                    list_int = index+1

                    if not os.path.exists(ruta_carpeta):
                        os.makedirs(ruta_carpeta)

                        name = f'{ruta_carpeta}/{name_image}_{list_int}.png'

                        cv2.imwrite(name, imageOut[index])

                    else:
                        name = f'{ruta_carpeta}/{name_image}_{list_int}.png'

                        cv2.imwrite(name, imageOut[index])
                
                self.index = list_int

                cv2.destroyAllWindows()
                
                # Esto muestra las imagens cortadas
                for i in range(len(imageOut)):
                    condicion = True
                    if i+1 == len(imageOut):
                        MessageBox.showwarning("Final", 
                "Terminaron las imagenes")

                    while condicion == True:
                        cv2.imshow('Imagen de salida',imageOut[i])

                        b = cv2.waitKey(1) & 0xFF

                        if b == ord('a'):
                            break

                        if b == 27:
                            condicion = False  # Actualiza la variable de control del ciclo while


                        if i+1 == len(imageOut):
                            if b == 27:
                                break

                    if condicion != True:
                        cv2.destroyAllWindows()
                        break

        except NameError as e:
            print(e)
    

    def compress(self, continuar = True):
        import fileinput

        try:
            with fileinput.FileInput('info.txt', inplace=False) as file:
                for line in file:
                    if 'key' in line:
                        key = line[line.rfind('=')+2:-2]

            if key == None or key == '':
                
                MessageBox.showwarning("Alerta", 
                "No has agregado la api")
            
            elif continuar == True:            
                directorio_path = get_path(archivo = False)

                # Obtener la lista de archivos en la carpeta
                archivos = os.listdir(directorio_path)
                directorio_path_save = get_path(archivo = False)
                compress_save = dist_maker(directorio_path_save,'compress', False)

                # Imprimir los nombres de los archivos
                for archivo in archivos:
                    
                    position = archivo.rfind(".")
                    extension = archivo[position:]
                    
                    if extension == '.png' or extension == '.jpg':
                        
                        ruta_guardado = compress_save

                        tinify.key = key
                        source = tinify.from_file(directorio_path+'/'+archivo)
                        source.to_file(compress_save+'/'+archivo)

            elif continuar  == False:
                archivos = glob.glob(self.path + '/*')
                compress_save = dist_maker(self.path,'compress')

                # Imprimir los nombres de los archivos
                for archivo in archivos:
                    position = archivo.rfind("/")
                    name_file = archivo[position + 1:]

                    ruta_guardado = compress_save+'/'+name_file

                    tinify.key = key
                    source = tinify.from_file(archivo)
                    source.to_file(ruta_guardado)
        except NameError as e:
            print(e)
            
    
    def make_html(self, head_png=None, head_link=None, body_png=None, body_link=None, legal_content=None, footer_png=None, footer_link=None, title=['Nuevo mail'], continue_value = False, colors = ['#fff']):
        def make_a(path,list_png, list_link, position, inicio = False, Legal = False, guia = 'guia.html', color = False):
                import fileinput

                comparacion = "<!--/"+position+"/-->"
                path_file = path+"/"+title[0]+".html"


                if color == True:
                    with fileinput.FileInput(path_file, inplace=True, backup=False) as file:
                                # Recorrer cada línea del archivo de entrada
                                count=0
                                for line in file:
                                    count -=1
                                    
                                    
                                    # Buscar la etiqueta <!--/Legal/-->
                                    if comparacion in line:
                                        count=3
                                        for link_png in list_png:
                                        # Agregar el código después de la etiqueta
                                            print(f'''
            <table align="center" bgcolor="{link_png}" border="0" cellpadding="0" cellspacing="0" class="banner" width="600">
                <tr>
                    <td
                        style="font-family:'Trebuchet MS', Arial, Helvetica, sans-serif; color:#fff; font-size:12px; padding:14px 20px 20px 20px; text-align:justify;">''')
                                    
                                    elif count < 0:
                                        print(line,end='')

                elif inicio  == False and Legal == False:
                    

                    for link in list_link:

                        if link == '':

                            with fileinput.FileInput(path_file, inplace=True, backup=False) as file:
                                # Recorrer cada línea del archivo de entrada
                                for line in file:
                                    print(line,end='')
                                    
                                    # Buscar la etiqueta <!--/Legal/-->
                                    if comparacion in line:

                                        for link_png in list_png:
                                        # Agregar el código después de la etiqueta
                                            print(f'''
                <a target="_blank"> 
                    <table align="center" border="0" bgcolor="#1fc0bd" cellpadding="0" cellspacing="0" class="banner" width="600">
                        <tr>
                            <td>
                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                <td class="mobileBanner" height="100%" width="100%">
                                    <img border="0" class="banner" src="{link_png}" style="display:block;" width="100%">
                                </td>
                                </tr>
                            </table>
                            </td> 
                        </tr>
                    </table>
                </a>                
                                
''')
                                                        
                        else:
                            with fileinput.FileInput(path_file, inplace=True,backup=False) as file:
                                # Recorrer cada línea del archivo de entrada
                                for line in file:
                                    print(line,end='')
                                
                                    # Buscar la etiqueta <!--/Legal/-->
                                    if comparacion in line:
                            
                                        for index,link_png  in enumerate(list_png):
                                        # Agregar el código después de la etiqueta
                                            print(f'''
                <a href="{list_link[index]}" target="_blank"> 
                    <table align="center" border="0" bgcolor="#1fc0bd" cellpadding="0" cellspacing="0" class="banner" width="600">
                        <tr>
                            <td>
                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                <td class="mobileBanner" height="100%" width="100%">
                                    <img border="0" class="banner" src="{link_png}" style="display:block;" width="100%">
                                </td>
                                </tr>
                            </table>
                            </td> 
                        </tr>
                    </table>
                </a>

''')
                                        
                elif Legal == True and inicio == False:
                    import fileinput

                    with fileinput.FileInput(path_file, inplace=True) as file:
                        # Recorrer cada línea del archivo de entrada
                        for line in file:
                            print(line,end='')
                        
                            # Buscar la etiqueta <!--/Legal/-->
                            if position in line:
                    
                                for link_png  in range(len(list_png)):

                                    if len(list_png) == 1:
                                        print(f'''                              {list_png[link_png]}''')

                                    else:
                                        if link_png == 0:
                                            position_1 = position

                                            # Agregar el código después de la etiqueta
                                            print(f'''                             {list_png[link_png]}''')
                                            print(f'''                            {position_1[0]+'/'+position_1[1:]} \n''')
                                                
                                        else:
                                            position_1 = position
                                            print(f'''                             {position_1} \n''', end='')
                                            print(f'''                              {list_png[link_png]} \n''' ,end='')
                            
                elif inicio == True:
                    with open((path+"/"+title[0]+".html"), "w") as output_file:
                                with open(guia, "r") as input_file:
                                    
                                    # Recorrer cada línea del archivo de entrada
                                    for line in input_file:
                                        # Escribir la línea en el archivo de salida
                                        output_file.write(line)

                                        if comparacion in line:
                                            for index, link_png in enumerate(list_png):
                                                if list_link[index] == '':
                                                    
                                                    output_file.write(f'''
                <a target="_blank"> 
                    <table align="center" border="0" bgcolor="#1fc0bd" cellpadding="0" cellspacing="0" class="banner" width="600">
                        <tr>
                            <td>
                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                <td class="mobileBanner" height="100%" width="100%">
                                    <img border="0" class="banner" src="{link_png}" style="display:block;" width="100%">
                                </td>
                                </tr>
                            </table>  
                            </td> 
                        </tr>
                    </table>
                </a>
                                
''')

                                                        
                                                else:

                                                    # Agregar el código después de la etiqueta
                                                    output_file.write(f'''
                <a href="{list_link[index]}" target="_blank"> 
                    <table align="center" border="0" bgcolor="#1fc0bd" cellpadding="0" cellspacing="0" class="banner" width="600">
                        <tr>
                            <td>
                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                <td class="mobileBanner" height="100%" width="100%">
                                    <img border="0" class="banner" src="{link_png}" style="display:block;" width="100%">
                                </td>
                                </tr>
                            </table>
                            </td> 
                        </tr>
                    </table>
                </a>

''')
                                            

        if continue_value == False:
            path = get_path(False)

            make_a(path, head_png, head_link, 'Head',inicio=True)
            make_a(path, body_png, body_link, 'Contenido')
            make_a(path,footer_png, footer_link, 'Footer')
            make_a(path= path,position='<p>',list_png= legal_content,list_link= head_link, Legal=True, inicio=False)
            make_a(path, title, head_link,'<title>', Legal=True, inicio=False)

        elif continue_value == True:
            path = get_path(False)
            make_a(path, head_png, head_link, 'Contenido',inicio=True, guia='guia_aut.html')
            make_a(path= path,position='<p>',list_png= legal_content,list_link= head_link, Legal=True, inicio=False, guia='guia_aut.html')
            make_a(path, title, head_link,'<title>', Legal=True, inicio=False, guia='guia_aut.html')
            bool = buscador('info.txt', 'color')

            if bool == 'True' and '#FFF' in colors and '#fff' in colors and '' in colors:
                make_a(path, colors, head_link,'Footer', Legal=True, inicio=False, guia='guia_aut.html', color = True)
    

    def html_heredado(self):
        return self.index


    def create_navegador(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options

        def loop(loops):
            while loops:
                time.sleep(1)

        # Ruta al controlador de Chrome
        PATH = 'drivers_chrome/chromedriver'

        # Opciones del navegador Chrome
        options = Options()

        # Inicializar el servicio del controlador
        service = Service(PATH)

        # Inicializar el driver de Chrome
        self.driver = webdriver.Chrome(service=service, options=options)
    

    def verify_log(self):
        
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        

        link = 'https://mcrtlgjr-g-gwpsc952zwcc7q2vy.login.exacttarget.com/hub-cas/login?wl=Niw2MDAwMTAzOCxmZTZk0&service=https%3a%2f%2fmc.s6.exacttarget.com%2fcloud%2flogin.html%3fhash%3dOrEn1bG9nZ2VkLWluSXc9PQ2'

        

        
        # options.add_argument("--start-maximized")  # Iniciar maximizado (opcional)

        

        

        driver.get(link)
        time.sleep(2)

        content = driver.find_element(By.XPATH,'//form[@id="LoginForm"]')

        if 'Nombre de usuario' in content.text or 'Recordarme' in content.text:
            print('not login')
            
            username = driver.find_element(By.XPATH,'//input[@id="username"]')
            user = buscador('info.txt', 'user')
            username.send_keys(user)

            submit_name = driver.find_element(By.XPATH,'//input[@id="submit-btn"]')
            submit_name.click()

            time.sleep(2)

            password_form = driver.find_element(By.XPATH,'//input[@id="password"]')
            password = buscador('info.txt', 'Pass')
            password_form.send_keys(password)

            submit_pass = driver.find_element(By.XPATH,'//input[@id="submit-btn"]')
            submit_pass.click()
        
        navegador = True

        while navegador == True:
            time.sleep(1)
            navegador = navegador_boolean()
    






