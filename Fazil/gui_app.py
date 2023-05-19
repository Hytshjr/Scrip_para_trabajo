import tkinter as tk
from image_cut import Editor
from tkinter import messagebox as MessageBox

class Frame(tk.Frame):
    def __init__(self, root = None, clase = None):
        super().__init__(root)

        self.clase = clase
        self.root = root
        self.pack()
        self.config(width= 480, height= 320, bg='#808080')
        self.campos_rellenar()

    def campos_rellenar(self):
        # Lista de cada campo
        self.label_nombre = tk.Label(self, text = 'Introduce la Api: ')
        self.label_nombre.config(font = ('aakar',12), bg='#808080')
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        # Entrys
        with open("key_api.txt", "r") as file:
            key = file.read()

        self.compres_api = tk.StringVar() #Guarda lo que ingresa en el primer campo
        self.compres_api.set(key)

        self.entry_api = tk.Entry(self, textvariable = self.compres_api)
        self.entry_api.config(width=50, bg='#808080', border=0)
        self.entry_api.grid(row=0, column=1)

        # Botones

        #Este primer boton guarda el api
        self.boton_save = tk.Button(self, text='Guardar Api', command=self.guardar_api)
        self.boton_save.config(width=20, border=0, fg='black', bg='#DCDCDC')
        self.boton_save.grid(row=1, column=0, pady=3)

        #Este segundo boton remplaza el api
        self.boton_replpace = tk.Button(self, text='Reemplazar Api', command=self.replace_api)
        self.boton_replpace.config(width=20, border=0, fg='black', bg='#DCDCDC')
        self.boton_replpace.grid(row=1, column=1, pady=3)

        #Este boton recorte la imagen
        self.boton_replpace = tk.Button(self, text='Recortar imagen', command=self.clase.cut_image)
        self.boton_replpace.config(width=40, border=0, fg='black', bg='#DCDCDC')
        self.boton_replpace.grid(row=2, column=0, pady=3, columnspan=2)

        #Este boton comprime las imagenes
        self.boton_replpace = tk.Button(self, text='Comprimir imagenes', command=self.clase.compress)
        self.boton_replpace.config(width=40, border=0, fg='black', bg='#DCDCDC')
        self.boton_replpace.grid(row=3, column=0, pady=3, columnspan=2)

        #Este boton hace el proceso de corte y compresion
        self.boton_replpace = tk.Button(self, text='Corte y compresion de imagen', command=self.cut_compress)
        self.boton_replpace.config(width=40, border=0, fg='black', bg='#DCDCDC')
        self.boton_replpace.grid(row=4, column=0, pady=3, columnspan=2)
    
    def guardar_api(self):
        self.entry_api.config(state='disable')
        key = self.compres_api.get()

        with open("key_api.txt", "w") as file:
            file.write(key)
    
    def replace_api(self):
        self.compres_api.set('')
        self.entry_api.config(state='normal')

    def cut_compress(self):
        self.clase.cut_image()
        self.clase.compress(continuar = False)


        