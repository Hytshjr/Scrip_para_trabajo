from image_cut import get_path

def make_a(path,html_name,list_image):
    with open((path+"/"+html_name), "w") as output_file:
      with open("guia.html", "r") as input_file:
          
          # Recorrer cada línea del archivo de entrada
          for line in input_file:
              # Escribir la línea en el archivo de salida
              output_file.write(line)
              
              # Buscar la etiqueta <!--/Legal/-->
              if "<!--/Contenido/-->" in line:

                  for link_png in list_image:
                  # Agregar el código después de la etiqueta
                    output_file.write(f'''
                      <a target="_blank"> 
                        <table align="center" border="0" bgcolor="#1fc0bd" cellpadding="0" cellspacing="0" class="banner" width="600">
                          <tr>
                            <td>
                              <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                  <td class="mobileBanner" height="100%" width="100%">
                                    <img border="0" class="banner" src="{link_png}" style="display:block;" width="100%">
                                  </td>
                                </tr>
                              </table>
                            </td> 
                          </tr>
                        </table>
                      </a>

''')

# Lista con las direcciones de las imágenes
image_urls = [
    "https://image.corp.fazil-app.com/lib/fe3911727564047d731776/m/23/4f12cae9-4f92-4234-88e2-9fe1c2369f6c.png",
    "https://image.corp.fazil-app.com/lib/fe3911727564047d731776/m/23/910052d9-5309-4209-91ac-2fcd7eaea218.png",
    "https://image.corp.fazil-app.com/lib/fe3911727564047d731776/m/23/ec6b7ede-610e-49a6-aa80-085d13c99db5.png"
]

path = get_path(False)

make_a(path,'nuevo_mail', image_urls)

