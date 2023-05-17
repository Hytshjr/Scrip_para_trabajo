import tkinter as tk
from tkinter import filedialog
from image_cut import Editor


def run():
    # Crear la ventana
    window = tk.Tk()
    window.title("Visor de Imágenes")

    # Crear una etiqueta para mostrar la imagen
    label = tk.Label(window)
    label.pack()

    # Crear el botón para abrir la imagen
    button = tk.Button(window, text="Recorte de imagen", command=Editor(label=label).cut_image)
    button.pack(pady=10)

    # Iniciar el bucle de la aplicación
    window.mainloop()

if __name__ == "__main__":
    run()



