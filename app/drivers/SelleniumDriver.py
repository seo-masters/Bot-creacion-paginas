from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

def selenium_driver():
    # Carga la ruta del driver desde una variable de entorno
    DRIVER_PATH = os.getenv('DRIVER_PATH')

    # Configura las opciones de Chrome
    options = webdriver.ChromeOptions()
    options.service_args = ['--executable_path=' + DRIVER_PATH]

    # Inicializa y devuelve el driver de Chrome
    driver = webdriver.Chrome(options=options)
    return driver