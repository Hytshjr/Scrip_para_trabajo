from tkinter import *

def mostrar_mensaje(nombre):
    mensaje = "¡Hola, " + nombre + "! Has presionado el botón."
    print(mensaje)

root = Tk()

nombre = "Juan"

boton = Button(root, text="Presionar", command=lambda: mostrar_mensaje(nombre))
fun = lambda x, y: x**y 
print(fun(3,4))
boton.pack()

root.mainloop()
