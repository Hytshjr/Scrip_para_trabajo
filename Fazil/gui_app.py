import time
import tkinter as tk
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
        self.label_nombre.grid(row=0, column=0, padx=10, pady=15)

        # Entrys
        with open("key_api.txt", "r") as file:
            key = file.read()

        self.compres_api = tk.StringVar() #Guarda lo que ingresa en el primer campo
        self.compres_api.set(key)

        self.entry_api = tk.Entry(self, textvariable = self.compres_api)
        self.entry_api.config(width=20, bg='#808080')
        self.entry_api.grid(row=0, column=1)

        # Botones

        #Este primer boton guarda el api
        self.boton_save = tk.Button(self, text='Guardar Api', command=self.guardar_api)
        self.boton_save.config(width=20, border=0, fg='black', bg='#DCDCDC')
        self.boton_save.grid(row=1, column=0, pady=2)

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

        #Este boton crea el nuevo frame para hacer el html
        self.boton_replpace = tk.Button(self, text='Hacer el html', command=self.clase.new_windows)
        self.boton_replpace.config(width=40, border=0)
        self.boton_replpace.grid(row=5, column=0, pady=3, columnspan=2)

    def create_html(ventana):
    
        #Este primer espacio para poner el link de la imagen
        count_head = tk.StringVar() #Guarda lo que ingresa en el campo
        count_head.set('')

        entry_head = tk.Entry(ventana, textvariable = count_head)
        entry_head.config(width=20, bg='#DCDCDC', border=0)
        entry_head.grid(row=1, column=0, padx=5, pady=5)

        #Este Segundo espacio para poner el link de la imagen
        count_body = tk.StringVar() #Guarda lo que ingresa en el campo
        count_body.set('')

        entry_body = tk.Entry(ventana, textvariable = count_body)
        entry_body.config(width=20, bg='#DCDCDC', border=0)
        entry_body.grid(row=1, column=1, padx=5, pady=5)

        #Este Segundo espacio para poner el link de la imagen
        count_legal = tk.StringVar() #Guarda lo que ingresa en el campo
        count_legal.set('')

        entry_legal = tk.Entry(ventana, textvariable = count_legal)
        entry_legal.config(width=20, bg='#DCDCDC', border=0)
        entry_legal.grid(row=1, column=2, padx=5, pady=5)

        def obtener_contenido():
            nonlocal ventana
            nonlocal entry_head
            nonlocal entry_body
            nonlocal entry_legal

            head = entry_head.get()
            body = entry_body.get()
            legal = entry_legal.get()

            try:
                head = int(head)
                body = int(body)
                legal = int(legal)

                int_pass = True
            
            except:
                int_pass = False

            if int_pass == False:
                MessageBox.showwarning("Alerta", 
                "Solo ingrese valore numericos")

            else:

                def create_get_content(count, position, link = True):

                    link_png = []
                    link_app = []

                    def get_text():
                            nonlocal entry_content_png
                            nonlocal entry_content_link

                            nonlocal link_png
                            nonlocal link_app

                            try:
                                for content_get in entry_content_png:
                                    # print(content_get.get())
                                    link_png.append(content_get.get())
                            except:
                                pass

                            try:
                                for content_get in entry_content_link:
                                    # print(content_get.get())
                                    link_app.append(content_get.get())
                            except:
                                pass





                    if link == True:

                        entry_content_png = []
                        entry_content_link = []
                        # position_row = position+1

                        for box_content in range(count):

                            count_varia = tk.StringVar() #Guarda lo que ingresa en el campo

                            position_row = position+(box_content+1)

                            count_get = tk.Entry(ventana, textvariable = count_varia)
                            count_get.config(width=20, bg='#DCDCDC', border=0)
                            count_get.grid(row=position_row, column=0, padx=5, pady=5,columnspan=2)

                            entry_content_png.append(count_get)

                        # --------------------------------------------------------------

                        for box_content in range(count):

                            count_varia = tk.StringVar() #Guarda lo que ingresa en el campo

                            position_row = position+(box_content+1)

                            count_get = tk.Entry(ventana, textvariable = count_varia)
                            count_get.config(width=20, bg='#DCDCDC', border=0)
                            count_get.grid(row=position_row, column=1, padx=5, pady=5,columnspan=2)

                            entry_content_link.append(count_get)
                        
                        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                        # Boton para obtener el contenido de las lineas
                        boton_entry = tk.Button(ventana, text='Guardar valores', command=get_text)
                        boton_entry.config(width=20, border=0, fg='black', bg='#DCDCDC')
                        boton_entry.grid(row=position_row+1, column=1,columnspan=2)

                        return link_png, link_app

                    elif link == False:
                        entry_content_png = []

                        for box_content in range(count):
                            count_varia = tk.StringVar() #Guarda lo que ingresa en el campo

                            position_row = position+(box_content+1)

                            count_get = tk.Entry(ventana, textvariable = count_varia)
                            count_get.config(width=20, bg='#DCDCDC', border=0)
                            count_get.grid(row=position_row, column=1, padx=5, pady=5)

                            entry_content_png.append(count_get)

                        boton_entry = tk.Button(ventana, text='Guardar valores', command=get_text)
                        boton_entry.config(width=20, border=0, fg='black', bg='#DCDCDC')
                        boton_entry.grid(row=position_row+1, column=1,columnspan=2)

                        return link_png
                
                def test():

                    import sys
                    sys.path.append('../')
                    from image_cut import Editor
                    # print('jojojo')

                    edit = Editor()

                    nonlocal head_png
                    nonlocal head_link
                    nonlocal body_png
                    nonlocal body_link
                    nonlocal legal_content

                    edit.create_html(head_png=head_png, head_link=head_link, body_png=body_png, body_link=body_link, legal_content=legal_content)
                    

                    pass
                    

                head_png,head_link = create_get_content(head,3)
                body_png,body_link = create_get_content(body,(head+3+1+1))
                legal_content = create_get_content(legal,(head+body+3+3), False)

                # Boton para obtener las cantidades
                boton_save = tk.Button(ventana, text='Hacer HTML', command=test)
                boton_save.config(width=50, border=0, fg='black', bg='#DCDCDC')
                boton_save.grid(row=body+head+legal+9, column=0, columnspan=3, pady=10)

        def close():
            ventana.destroy()

        # BOTONES

        # Boton para obtener las cantidades
        boton_save = tk.Button(ventana, text='Cantidades', command=obtener_contenido)
        boton_save.config(width=20, border=0, fg='black', bg='#DCDCDC')
        boton_save.grid(row=2, column=1,columnspan=2)

        # Boton para obtener las cantidades
        boton_save = tk.Button(ventana, text='Cerrar', command=close)
        boton_save.config(width=20, border=0, fg='black', bg='#DCDCDC')
        boton_save.grid(row=2, column=0, columnspan=1)
        
        
    
    # def obtener_contenido(self,event):
    #     contenido = event.get()
    #     print(contenido)
    #     return contenido

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

    def clean_frame(self):
        self.frame.destroy()



        