import time
import fileinput
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

        # Leyendo o buscando la API        
        with fileinput.FileInput('info.txt', inplace=False) as file:
            for line in file:
                if 'key' in line:
                    key = line[line.rfind('=')+2:-3]

        # Entrys
        self.compres_api = tk.StringVar() #Guarda lo que ingresa en el primer campo
        self.compres_api.set(key)

        self.entry_api = tk.Entry(self, textvariable = self.compres_api)
        self.entry_api.config(width=20, bg='#808080', state='disable')
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

        #Este boton crea el nuevo frame para hacer el html
        self.boton_replpace = tk.Button(self, text='Hacer el html', command=self.create_html)
        self.boton_replpace.config(width=40, border=0)
        self.boton_replpace.grid(row=4, column=0, pady=3, columnspan=2)

        #Este boton hace el proceso de corte y compresion
        self.boton_replpace = tk.Button(self, text='Corte y compresion de imagen', command=self.just_cut)
        self.boton_replpace.config(width=40, border=0, fg='black', bg='#DCDCDC')
        self.boton_replpace.grid(row=5, column=0, pady=3, columnspan=2)

        #Este boton hace el proceso de corte y compresion
        self.boton_replpace = tk.Button(self, text='Corte y hacer HTML', command=self.cut_compress)
        self.boton_replpace.config(width=40, border=0, fg='black', bg='#DCDCDC')
        self.boton_replpace.grid(row=6, column=0, pady=3, columnspan=2)

        # Crear el checkbox y asociarlo a la variable
        checkbox_var_color = tk.BooleanVar()

        # Lee el archivo para setearlo en True o False
        with fileinput.FileInput('info.txt', inplace=False) as file:
                for line in file:
                    if 'color' in line:
                        color = line[line.rfind('=')+2:-2]            
        if color == 'False':
            checkbox_var_color.set(False)
        elif color == 'True':
            checkbox_var_color.set(True)       
        checkbox_color = tk.Checkbutton(self, text="Cambiar color", variable=checkbox_var_color, command=lambda: self.las_cut('color', checkbox_var_color))
        checkbox_color.grid(row=7, column=1)

        # Crear el checkbox y asociarlo a la variable
        checkbox_var = tk.BooleanVar()

        # Lee el archivo para setearlo en True o False
        with fileinput.FileInput('info.txt', inplace=False) as file:
                for line in file:
                    if 'last' in line:
                        last = line[line.rfind('=')+2:-2]            
        if last == 'False':
            checkbox_var.set(False)
        elif last == 'True':
            checkbox_var.set(True)       
        checkbox = tk.Checkbutton(self, text="Licor en exceso", variable=checkbox_var, command=lambda: self.las_cut('last', checkbox_var))
        checkbox.grid(row=7, column=0)


    def new_windows(self, name = 'Nueva ventana'):
        window = tk.Toplevel(self)
        window.title(name)
        window.config(bg='#808080')

        return window


    def create_html(self):
        ventana = self.new_windows(name='Hacer HTML')

        # Esto genera los cuadros de entrada y la variable que los guarda
        #Este primer espacio para poner la cantidad de headers
        count_head = tk.StringVar() #Guarda lo que ingresa en el campo
        count_head.set('')

        entry_head = tk.Entry(ventana, textvariable = count_head)
        entry_head.config(width=20, bg='#DCDCDC', border=0)
        entry_head.grid(row=1, column=0, padx=10, pady=10)

        #Este Segundo espacio para poner la cantidad de bodys
        count_body = tk.StringVar() 
        count_body.set('')

        entry_body = tk.Entry(ventana, textvariable = count_body)
        entry_body.config(width=20, bg='#DCDCDC', border=0)
        entry_body.grid(row=1, column=1, padx=5, pady=5)

        #Este Tercer espacio para poner la cantidad de footer
        count_footer = tk.StringVar() 
        count_footer.set('')

        entry_footer = tk.Entry(ventana, textvariable = count_footer)
        entry_footer.config(width=20, bg='#DCDCDC', border=0)
        entry_footer.grid(row=1, column=2, padx=5, pady=5)

        #Este Cuarto espacio para poner la cantidad de legales
        count_legal = tk.StringVar() 
        count_legal.set('')

        entry_legal = tk.Entry(ventana, textvariable = count_legal)
        entry_legal.config(width=20, bg='#DCDCDC', border=0)
        entry_legal.grid(row=1, column=3, padx=5, pady=5)

        def obtener_contenido():
            # Extraemos las variables de afuera de la funcion
            nonlocal ventana
            nonlocal entry_head
            nonlocal entry_body
            nonlocal entry_footer
            nonlocal entry_legal

            # Usamos el metodo get de tk para obtener los valores
            head = entry_head.get()
            body = entry_body.get()
            footer = entry_footer.get()
            legal = entry_legal.get()

            # Aseguramos que sea un numero entero
            try:
                head = int(head)
                body = int(body)
                footer = int(footer)
                legal = int(legal)
                    
                head_png,head_link = self.crear_entrys(head,3, ventana)
                body_png,body_link = self.crear_entrys(body,(head+3+1+1), ventana)
                footer_png, footer_link = self.crear_entrys(footer,(head+body+3+3), ventana)
                legal_content = self.crear_entrys(legal,(head+body+11+1), ventana, False)
                title = self.crear_entrys(1,(head+body+11+7), ventana, False)

            
                # Boton para obtener las cantidades
                boton_save = tk.Button(ventana, text='Hacer HTML', command= lambda:self.clase.make_html(head_png,head_link,body_png,body_link,legal_content,footer_png,footer_link,title))
                boton_save.config(width=50, border=0, fg='black', bg='#DCDCDC')
                boton_save.grid(row=body+head+legal+footer+11+8, column=0, columnspan=3, pady=10)

            except:
                MessageBox.showwarning("Alerta", 
                    "Solo ingrese valores numericos")

        # BOTONES
        # Boton para obtener las cantidades
        boton_save = tk.Button(ventana, text='Mostrar', command=obtener_contenido)
        boton_save.config(width=20, border=0, fg='black', bg='#DCDCDC')
        boton_save.grid(row=2, column=2,columnspan=2)

        # Boton para cerrar la ventana
        boton_save = tk.Button(ventana, text='Cerrar', command = lambda : self.clean_frame(ventana)) #Agregar el comman para "Cerrar"
        boton_save.config(width=20, border=0, fg='black', bg='#DCDCDC')
        boton_save.grid(row=2, column=1, columnspan=1)


    def crear_entrys(self,count, position, ventana, link = True):

        link_png = []
        link_app = []

        # En una iteracion crea los entrys que le pida, le paso la columna como atributo
        def crear_inputs(count, position, columna = 0):
            # count: La cantidad de entrys debe de haber
            # position: a partir de que empieza a crear los entrys

            list_entry = []

            for box_content in range(count):

                count_varia = tk.StringVar() #Guarda lo que ingresa en el campo
                position_row = position+(box_content+1)

                count_get = tk.Entry(ventana, textvariable = count_varia)
                count_get.config(width=20, bg='#DCDCDC', border=0)
                count_get.grid(row=position_row, column=columna, padx=5, pady=5)

                list_entry.append(count_get)

            return list_entry
            
        def get_text( content_png, content_link = False):

            nonlocal link_png
            nonlocal link_app


            if link == False and content_link == False:
                for content_get in content_png:
                    # link_png = []
                    link_png.append(content_get.get())


            elif link == True:
                for content_get in content_png:
                    # link_png = []
                    link_png.append(content_get.get())

                for content_get in content_link:
                    # link_app = []
                    link_app.append(content_get.get())


        # La condicion de si viene con link o no
        if link == True:
            
            link_png = []
            link_app = []

            entry_content_png = []
            entry_content_link = []

            entry_content_png = crear_inputs(count, position)
            entry_content_link = crear_inputs(count, position, columna=1)

            # Boton para obtener el contenido de las lineas
            boton_entry = tk.Button(ventana, text='Guardar valores', command= lambda: get_text(entry_content_png, entry_content_link)) 
            boton_entry.config(width=20, border=0, fg='black', bg='#DCDCDC')
            boton_entry.grid(row=position+count+1, column=0,columnspan=3)


            return link_png, link_app 


        elif link == False:
            entry_content_png = []
            entry_content_png = crear_inputs(count, position)

            # Boton para obtener el contenido de las lineas
            boton_entry = tk.Button(ventana, text='Guardar valores', command= lambda: get_text(content_png = entry_content_png)) 
            boton_entry.config(width=20, border=0, fg='black', bg='#DCDCDC')
            boton_entry.grid(row=position+count+1, column=0,columnspan=3)

            return link_png 
        

    def guardar_api(self):
        import fileinput

        self.entry_api.config(state='disable')
        key = self.compres_api.get()

        with fileinput.FileInput('info.txt', inplace=True) as file:
                # Recorrer cada línea del archivo de entrada
                for line in file:   
                              
                    # Buscar la etiqueta <!--/Legal/-->
                    if 'key' in line:
                      print(f'''key = {key},''')
                    
                    else:
                      print(line,end='')  


    def replace_api(self):
        self.compres_api.set('')
        self.entry_api.config(state='normal')


    def just_cut(self):

        self.clase.cut_image()
        self.clase.compress(continuar = False)   


        ventana = self.new_windows('Hacer html')
        ventana.config(width=100)

        #Este primer espacio para poner la cantidad de legales
        count_legal = tk.StringVar() #Guarda lo que ingresa en el campo
        count_legal.set('')

        entry_legal = tk.Entry(ventana, textvariable = count_legal)
        entry_legal.config(width=20, bg='#DCDCDC', border=0)
        entry_legal.grid(row=0, column=0, padx=10, pady=10)

        # Boton para obtener las cantidades
        boton_save = tk.Button(ventana, text='Cantidad de Legales', command=obtener_contenido)
        boton_save.config(width=20, border=0, fg='black', bg='#DCDCDC')
        boton_save.grid(row=0, column=1,columnspan=2)

        # num_imagenes es una variable que se hereda de las imagenes recortadas
        num_imagenes = self.clase.html_heredado()


    def cut_compress(self):
        try:
            self.clase.cut_image()
            self.clase.compress(continuar = False)
            
            def obtener_contenido():
                nonlocal count_legal
                nonlocal num_imagenes
                nonlocal ventana

                # Claridad de legales
                legal = count_legal.get()
                legal = int(legal)

                # Crear los nuevos inputs
                link_png, link_app = self.crear_entrys(num_imagenes,1,ventana)
                legal_content =self.crear_entrys(legal, (num_imagenes+2), ventana, link=False)
                title = self.crear_entrys(1,(num_imagenes+legal+4), ventana, link=False)
                
                with fileinput.FileInput('info.txt', inplace=False) as file:
                    for line in file:
                        if 'color' in line:
                            color = line[line.rfind('=')+2:-2]  

                if color == 'True':
                    color = self.crear_entrys(1,(num_imagenes+legal+6), ventana, link=False)

                else:
                    color = ['#fff']

                # Boton para hacer el html
                boton_save = tk.Button(ventana, text='Hacer HTML', command= lambda:self.clase.make_html(head_png = link_png, head_link = link_app,legal_content = legal_content,title=title, continue_value= True, colors=color))
                boton_save.config(width=50, border=0, fg='black', bg='#DCDCDC')
                boton_save.grid(row=num_imagenes+legal+9, column=0, columnspan=3, pady=10)   


            ventana = self.new_windows('Hacer html')
            ventana.config(width=100)

            #Este primer espacio para poner la cantidad de legales
            count_legal = tk.StringVar() #Guarda lo que ingresa en el campo
            count_legal.set('')

            entry_legal = tk.Entry(ventana, textvariable = count_legal)
            entry_legal.config(width=20, bg='#DCDCDC', border=0)
            entry_legal.grid(row=0, column=0, padx=10, pady=10)

            # Boton para obtener las cantidades
            boton_save = tk.Button(ventana, text='Cantidad de Legales', command=obtener_contenido)
            boton_save.config(width=20, border=0, fg='black', bg='#DCDCDC')
            boton_save.grid(row=0, column=1,columnspan=2)

            # num_imagenes es una variable que se hereda de las imagenes recortadas
            num_imagenes = self.clase.html_heredado()

        
        except NameError as e:
            print(e)
        

    def las_cut(self, cambio, check_box):
        
        import fileinput

        bool = check_box.get()

        with fileinput.FileInput('info.txt', inplace=True) as file:
                # Recorrer cada línea del archivo de entrada
                for line in file:   
                              
                    # Buscar la etiqueta <!--/Legal/-->
                    if cambio in line:
                      print(f'''{cambio} = {bool},''')
                    
                    else:
                      print(line,end='')  


    def clean_frame(self, ventana):
        ventana.destroy()
        self.create_html()



        