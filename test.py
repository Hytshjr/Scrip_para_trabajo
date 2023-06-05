import time

class Editor:
    def __init__(self, root = None, path = None):
        
        self.root = root
        self.path = path

    def tiempo(self, value):
        try:
            while value == True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Programa interrumpido. Cerrando el navegador...")
            # Código para cerrar el navegador Selenium
   

    # Crea el navegador de senelium
    def create_navegador(self):
        
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options

        # Ruta al controlador de Chrome
        PATH = 'drivers_chrome/chromedriver'

        # Opciones del navegador Chrome
        options = Options()

        # Inicializar el servicio del controlador
        service = Service(PATH)

        # Inicializar el driver de Chrome
        self.driver = webdriver.Chrome(service=service, options=options)

        self.tiempo(False)
     

    def get_link(self):
        self.create_navegador()
        self.driver.get('https://www.facebook.com/')
    
Editor().get_link()
