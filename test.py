import fileinput

# Lista con las direcciones de las imágenes
image_urls = [
    "https://image.corp.fazil-app.com/lib/fe3911727564047d731776/m/23/4f12cae9-4f92-4234-88e2-9fe1c2369f6c.png",
    "https://image.corp.fazil-app.com/lib/fe3911727564047d731776/m/23/910052d9-5309-4209-91ac-2fcd7eaea218.png",
    "https://image.corp.fazil-app.com/lib/fe3911727564047d731776/m/23/ec6b7ede-610e-49a6-aa80-085d13c99db5.png"
]

# Abrir el archivo en modo de lectura y escritura
with fileinput.FileInput("guia.html", inplace=True, backup=".bak") as file:
    # Recorrer cada línea del archivo
    for line in file:
        # Buscar la posición donde se encuentra la etiqueta <!--/Legal/-->
        if "<!--/Legal/-->" in line:
            # Agregar el código antes de la etiqueta
            print(f'''
              <a target="_blank"> 
                <table align="center" border="0" bgcolor="#1fc0bd" cellpadding="0" cellspacing="0" class="banner" width="600">
                  <tr>
                    <td>
                      <table border="0" cellpadding="0" cellspacing="0" width="100%">
                        <tr>
                          <td class="mobileBanner" height="100%" width="100%">
                            <img border="0" class="banner" src="{image_urls[0]}" style="display:block;" width="100%">
                          </td>
                        </tr>
                      </table>
                    </td> 
                  </tr>
                </table>
              </a>
              ''')
        # Imprimir la línea actual
        print(line, end='')

