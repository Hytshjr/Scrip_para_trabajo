import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

import numpy as np
import cv2
import os

def get_path():
    file_path = filedialog.askopenfilename()
    return file_path

class Editor:
    def __init__(self, label):
        self.label = label

    
    def cut_image(self):
        def mouse_track(event,x,y,flags,param):
            nonlocal pxl_save
            global rect_pts
            nonlocal size_img
            nonlocal img_pos
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

        file_path = get_path()

        imagen = cv2.imread(file_path)
        copy_image = imagen.copy()
        size_img = imagen.shape
        pxl_save = []

        imagen_alto = size_img[0]
        window_height = 1080
        rect_pts = []
        img_pos = 0
        count = 0

        cv2.namedWindow('Imagen')
        cv2.setMouseCallback('Imagen',mouse_track)

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

        size_cut = len(pxl_save)
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

        for index in range(len(imageOut)):

            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)

                name = f'{ruta_carpeta}/{name_image}_{index}__.png'

                cv2.imwrite(name, imageOut[index])

            else:
                name = f'{ruta_carpeta}/{name_image}_{index}__.png'

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

