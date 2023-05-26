from tkinter import messagebox as MessageBox
from tkinter import filedialog
import tkinter as tk
import numpy as np
import tinify
import glob
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
        if not os.path.exists(file_path+'/'+dist_name):
            os.makedirs(file_path+'/'+dist_name)
            return file_path+'/'+dist_name

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

            imagen = cv2.imread(file_path)

            copy_image = imagen.copy()

            size_img = imagen.shape

            if size_img != None:
                MessageBox.showwarning("Tamaño", 
                f"La altura es de: {size_img[0]} y el ancho es de {size_img[1]}")

            pxl_save = []

            imagen_alto = size_img[0]
            window_height = 1080
            rect_pts = []
            img_pos = 0
            count = 0

            cv2.namedWindow('Imagen')
            cv2.setMouseCallback('Imagen',mouse_track)
        
        except NameError as e:
            print(e, 'Error en la parte de seleccion de archivo')

        try:
            while True:
                k = cv2.waitKey(10) & 0xFF

                if k == ord('l'): # Limpiar el contenido de la imagen
                    imagen = cv2.imread(file_path)
                    rect_pts = []
                    pxl_save = []
                    count = 0

                elif k == ord('f'):
                    if len(rect_pts)==0 and len(pxl_save)==0:
                        print('No tienes seleccion')
                        break
                    break

                elif k == ord('s'):
                    cv2.destroyAllWindows()
                    break

            size_cut = len(pxl_save)
        
        except NameError as e:
            print(e)

        count_cut = 0
        imageOut = []

        try:
            while count_cut < size_cut:

                top = pxl_save[count_cut][0] #Define o indica la altura del corte
                right = size_img[1] #Define el ancho de la imagen
                bottom = pxl_save[count_cut][1] #Define el pixel que hemos seleccionado con el mouse para hacer el corte

                imageOut.append(copy_image[top:bottom, 0:right])

                count_cut += 1

        except ValueError as e:
            print(e)

        imageOut.append(copy_image[bottom:size_img[0], 0:right])

        posicion_ultima_barra = file_path.rfind("/")
        directorio = file_path[:posicion_ultima_barra]
        name_image = file_path[posicion_ultima_barra + 1:-4]
        ruta_carpeta = directorio+'/images'

        self.path = ruta_carpeta

        for index in range(len(imageOut)):

            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)

                name = f'{ruta_carpeta}/{name_image}_{index}.png'

                cv2.imwrite(name, imageOut[index])

            else:
                name = f'{ruta_carpeta}/{name_image}_{index}.png'

                cv2.imwrite(name, imageOut[index])
        
        cv2.destroyAllWindows()
        

        for i in range(len(imageOut)):
            condicion = True

            while condicion:
                cv2.imshow('Imagen de salida',imageOut[i])

                b = cv2.waitKey(1) & 0xFF

                if b == ord('a'):
                    break

                if b == 27:
                    condicion = False  # Actualiza la variable de control del ciclo while
                    break  # Rompe el ciclo while

            
            if not condicion:
                cv2.destroyAllWindows()
                break

    def compress(self, continuar = True):

        with open("key_api.txt", "r") as file:
            key = file.read()

        if key == None or key == '':
            
            MessageBox.showwarning("Alerta", 
            "No has agregado la api")
        
        elif continuar == True:            
            directorio_path = get_path(archivo = False)

            # Obtener la lista de archivos en la carpeta
            archivos = glob.glob(directorio_path + '/*')
            directorio_path_save = get_path(archivo = False)
            compress_save = dist_maker(directorio_path_save,'compress', False)

            # Imprimir los nombres de los archivos
            for archivo in archivos:
                
                position = archivo.rfind("/")
                name_file = archivo[position + 1:]

                ruta_guardado = compress_save+'/'+name_file

                tinify.key = key
                source = tinify.from_file(archivo)
                source.to_file(ruta_guardado)

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

    def campos_rellenar_html(self):
        #Este primer espacio para poner el link de la imagen
        self.count_head = tk.StringVar() #Guarda lo que ingresa en el campo
        self.count_head.set('')

        self.entry_head = tk.Entry(self.frame, textvariable = self.count_head)
        self.entry_head.config(width=50, bg='#DCDCDC', border=0)
        self.entry_head.grid(row=1, column=0, padx=5, pady=5)
        
        #Este Segundo espacio para poner el link de la imagen
        self.count_body = tk.StringVar() #Guarda lo que ingresa en el campo
        self.count_body.set('')

        self.entry_body = tk.Entry(self.frame, textvariable = self.count_body)
        self.entry_body.config(width=50, bg='#DCDCDC', border=0)
        self.entry_body.grid(row=1, column=1, padx=5, pady=5)

        #Este Segundo espacio para poner el link de la imagen
        self.count_legal = tk.StringVar() #Guarda lo que ingresa en el campo
        self.count_legal.set('')

        self.entry_legal = tk.Entry(self.frame, textvariable = self.count_legal)
        self.entry_legal.config(width=50, bg='#DCDCDC', border=0)
        self.entry_legal.grid(row=1, column=2, padx=5, pady=5)

        # Boton para obtener las cantidades
        self.boton_save = tk.Button(self.frame, text='Cantidades', command=self.get_valor)
        self.boton_save.config(width=50, border=0, fg='black', bg='#DCDCDC')
        self.boton_save.grid(row=2, column=1)

        # Boton para obtener las cantidades
        self.boton_save = tk.Button(self.frame, text='Terminar', command=self.clean_frame)
        self.boton_save.config(width=50, border=0, fg='black', bg='#DCDCDC')
        self.boton_save.grid(row=2, column=0)

    def get_valor(self):
        head = self.entry_head.get()
        body = self.entry_body.get()
        legal = self.entry_legal.get()

        for i in range(int(head)):
            #Este primer espacio para poner el link de la imagen
            self.count_head = tk.StringVar() #Guarda lo que ingresa en el campo
            self.count_head.set('')

            self.entry_head = tk.Entry(self.frame, textvariable = self.count_head)
            self.entry_head.config(width=50, bg='#DCDCDC', border=0)
            self.entry_head.grid(row=i+3, column=0, padx=5, pady=5)
            self.entry_head.bind('<Return>', self.obtener_contenido)



    def clean_frame(self):
        self.frame.destroy()

    def obtener_contenido(self,event):
        contenido = self.entry_head.get()
        print(contenido)
    




