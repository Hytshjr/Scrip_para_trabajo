from Fazil.gui_app import Frame
from image_cut import Editor
import tkinter as tk


def run():
    # Crear la ventana
    window = tk.Tk()
    window.title("Fazil")
    window.config(bg='#808080')

    # Cargar el archivo de imagen desde el disco.
    icono = tk.PhotoImage(file="IMG/icon/fazil.png")
    # Establecerlo como ícono de la ventana.
    window.iconphoto(True, icono)

    edit = Editor(root = window) 
    app = Frame(root = window, clase = edit)

    # Iniciar el bucle de la aplicación
    app.mainloop()

if __name__ == "__main__":
    run()



