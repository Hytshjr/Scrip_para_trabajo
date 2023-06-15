# from tkinter import *

# def mostrar_mensaje(nombre):
#     mensaje = "¡Hola, " + nombre + "! Has presionado el botón."
#     print(mensaje)

# root = Tk()

# nombre = "Juan"

# boton = Button(root, text="Presionar", command=lambda: mostrar_mensaje(nombre))
# fun = lambda x, y: x**y 
# print(fun(3,4))
# boton.pack()

# root.mainloop()
import tkinter as tk

# Función que se ejecuta al presionar el botón en la nueva ventana
def hacer_algo():
    print("Se presionó el botón en la nueva ventana")

# Función para abrir la nueva ventana
def abrir_ventana():
    # Crear una nueva ventana usando Toplevel
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nueva Ventana")

    # Crear un botón en la nueva ventana utilizando grid
    boton = tk.Button(nueva_ventana, text="Presionar", command=hacer_algo)
    boton.grid(row=0, column=0, padx=10, pady=10)

# Crear la ventana principal
root = tk.Tk()

# Agregar contenido a la ventana principal
button = tk.Button(root, text="Abrir ventana", command=abrir_ventana)
button.pack()

# Iniciar el bucle principal de la aplicación
root.mainloop()
