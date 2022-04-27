#importar librerías utilizadas en el proyecto
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Opciones de navegador
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--disable_extensions')
#Estas opciones me solucionaron problema de no cargar la pagina en el webdriver
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

#Declarar variables utilizadas para buscar vuelos (Destino se puede cambiar)
url = 'https://www.vivaaerobus.com/es-mx/?msclkid=9582af72554d1d9f397ecd15ce61e757&utm_source=bing&utm_medium=cpc&utm_campaign=ma-sem_brand_do&utm_term=vivaaerobus&utm_content=Viva%20aerobus';
destino = "Guadalajara";
delay = 10;

#Introducir demora
#try:
     #Introducir demora inteligente
     #except

#Arrancar navegador con el path del ejecutable del driver
driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe', options=options)

#Ingresar a la url del sitio VivaAerobus
driver.get (url)

#Aceptar cookies
boton_cookies = driver.find_element(By.CLASS_NAME,'viva-btn.quick-add').click()