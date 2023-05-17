# def mouse_track(event,x,y,flags,param):
#     global pxl_save
#     global rect_pts
#     global size_img
#     global img_pos
#     global count


#     if event == cv2.EVENT_MBUTTONDOWN:
#         img_pos -= 50  # Ajusta la cantidad de desplazamiento Arriba

        
#     if event == cv2.EVENT_MOUSEWHEEL:
#         if flags < 0:
#             img_pos += 50     # Ajusta la cantidad de desplazamiento 


#     if count == 0:
#         if event == cv2.EVENT_LBUTTONDOWN:
#             rect_pts = [(x, y)]  

#             rect_pts.append((size_img[1],0))  #Estos son el ancho "size_img[1]" y el 0 es el top(la primera altura de la imagen)
#             rect_pts[0] = (0,rect_pts[0][1]+img_pos) #Estos son el inicio lateral de la imagen y la parte mas baja que seleccionamos

#             cv2.rectangle(imagen, rect_pts[0], rect_pts[1], (0, 255, 0))
 
#             pxl_save.append((0,rect_pts[0][1]))

#             count += 1 
               
        
#     else:
#         if event == cv2.EVENT_LBUTTONDOWN:
#             bottom_size = rect_pts[0][1] #Esto guarda la altura de la linea anterior y lo usa como tope para esta
#             rect_pts[1] = (size_img[1],bottom_size)

#             rect_pts[0] = (x, y)
#             rect_pts[0] = (0,rect_pts[0][1]+img_pos)
#             rect_pts[1] = (size_img[1],bottom_size)

#             cv2.rectangle(imagen, rect_pts[0], rect_pts[1], (0, 255, 0))
            
#             pxl_save.append((bottom_size,rect_pts[0][1]))
            
#             count += 1 
        
#     cv2.imshow("Imagen", imagen[img_pos:img_pos+window_height, :])

# import cv2
# import numpy as np

# file_path = 'test_image/cha-app_test.png'
# imagen = cv2.imread(file_path)
# copy_image = imagen.copy()
# size_img = imagen.shape
# pxl_save = []

# imagen_alto = size_img[0]
# window_height = 1080
# rect_pts = []
# img_pos = 0
# count = 0

# cv2.namedWindow('Imagen')
# cv2.setMouseCallback('Imagen',mouse_track)

# cv2.imshow('Imagen',imagen[:window_height, :])



# while True:
#     k = cv2.waitKey(10) & 0xFF

#     if k == ord('l'): # Limpiar el contenido de la imagen
#         imagen = cv2.imread(file_path)
#         rect_pts = []
#         count = 0

#     elif k == ord('f'):
#         if len(rect_pts)==0:
#             print('No tienes seleccion')
#             break
#         break

# size_cut = len(pxl_save)
# count_cut = 0
# imageOut = []

# try:
#     while count_cut < size_cut:

#         top = pxl_save[count_cut][0] #Define o indica la altura del corte
#         right = size_img[1] #Define el ancho de la imagen
#         bottom = pxl_save[count_cut][1] #Define el pixel que hemos seleccionado con el mouse para hacer el corte

#         print(f'top: {top}, right: {right}, bottom: {bottom}')

#         imageOut.append(copy_image[top:bottom, 0:right])

#         count_cut += 1

# except ValueError as e:
#     print(e)

# print(len(imageOut))


# for i in range(len(imageOut)):
#     while True:
#         cv2.imshow('Imagen de salida',imageOut[i])

#         b = cv2.waitKey(1) & 0xFF

#         if b == 27:
#             break
        
#         elif b == ord('a'):

#             name = f'cha-app_test_{i}__.png'

#             cv2.imwrite(name, imageOut[i])
#             cv2.destroyAllWindows()
#             break

# # _-------------------------------

import os
import cv2

# Ruta de la carpeta que deseas crear
ruta_carpeta = "/ruta/de/la/carpeta"

# Verificar si la carpeta no existe y crearla
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)
    print("Carpeta creada:", ruta_carpeta)
else:
    print("La carpeta ya existe:", ruta_carpeta)

# Ejemplo de guardar una imagen en la carpeta
imagen = cv2.imread("ruta/a/tu/imagen.jpg")
ruta_imagen_guardada = os.path.join(ruta_carpeta, "nombre_imagen.jpg")
cv2.imwrite(ruta_imagen_guardada, imagen)
print("Imagen guardada:", ruta_imagen_guardada)
