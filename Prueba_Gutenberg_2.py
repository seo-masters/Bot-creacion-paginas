from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Elementos:
def insert_image(driver):
    time.sleep(2)
    input = driver.find_element(By.CLASS_NAME, 'components-search-control__input')
    input.send_keys('Image')
    time.sleep(2)
    btn = driver.find_element(By.CLASS_NAME, 'components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-image')
    btn.click()

def default_case():
    print("Caso por defecto")

#Funciones 
def wait_and_click(driver, by, value):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
    element.click()

def wait_and_send_keys(driver, by, value, keys):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))
    element.send_keys(keys)

def wait_and_insert_item(driver,value,iconClass):
    wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-inserter__toggle.has-icon')
    wait_and_send_keys(driver, By.CLASS_NAME, 'components-search-control__input', value)
    wait_and_click(driver, By.CLASS_NAME, iconClass)

def wait_and_insert_item_column(driver,func):
    time.sleep(2)
    btn = driver.find_element(By.CLASS_NAME, 'components-button.block-editor-button-block-appender')
    btn.click()
    time.sleep(2)
    func(driver)

def container_columns(driver,index):
    time.sleep(2)
    icon = driver.find_element( By.CLASS_NAME, 'components-button.block-editor-inserter__toggle.has-icon')
    icon.click()
    time.sleep(2)
    input = driver.find_element( By.CLASS_NAME, 'components-search-control__input')
    input.send_keys('container')
    time.sleep(2)
    btn = driver.find_element(By.CLASS_NAME, 'components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-container')
    btn.click()
    # wait_and_insert_item(driver,"container", 'components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-container')
    time.sleep(2)
    buttons = driver.find_elements(By.CLASS_NAME, 'components-button.block-editor-block-variation-picker__variation.is-secondary.has-icon')
    # Seleccionar el botón en una posición específica (por ejemplo, el segundo botón)
    if 0 <= index < len(buttons):
        print(buttons[index])
        buttons[index].click()
    else:
        print("La posición está fuera de rango")

options = webdriver.ChromeOptions()
options.service_args = ['--executable_path=C:\driver_chrome\chromedriver.exe']

driver = webdriver.Chrome(options=options)
driver.get("https://vozavoz.live-website.com/wp-admin")
driver.maximize_window()

# Iniciar sesión
wait_and_send_keys(driver, By.ID, 'user_login', 'VozaVoz_Admin')
wait_and_send_keys(driver, By.ID, 'user_pass', 'Voz23#20Azteca')
wait_and_click(driver, By.ID, 'wp-submit')

# Navegar a la sección de páginas
wait_and_click(driver, By.ID, 'menu-pages')
wait_and_click(driver, By.CLASS_NAME, 'page-title-action')

time.sleep(10)

container_columns(driver,0)

wait_and_insert_item_column(driver,insert_image)

# # Insertar imagen - sigue el mismo patrón
# wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-media-placeholder__button.is-tertiary')
# wait_and_send_keys(driver, By.CLASS_NAME, 'block-editor-media-placeholder__url-input-field', 'https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg')
# wait_and_click(driver, By.CLASS_NAME, 'components-button.edit-post-header-toolbar__document-overview-toggle.has-icon')

# # Insertar título - sigue el mismo patrón
# wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-block-types-list__item.editor-block-list-item-post-title')
# wait_and_send_keys(driver, By.CLASS_NAME, 'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-post-title.rich-text', 'Hola Mundo')

# # Insertar párrafo - sigue el mismo patrón
# wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-block-types-list__item.editor-block-list-item-paragraph')
# wait_and_send_keys(driver, By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[3]/div[3]/div/div[2]/div[2]/div/div/div/div/p', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.')

# Continuar con el flujo del script
# ...

# Cerrar el navegador al finalizar
time.sleep(60)
driver.quit()