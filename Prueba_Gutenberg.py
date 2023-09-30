from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Elementos:
def insert_image(url):
    time.sleep(2)
   
    wait_and_insert_item(driver,'Image','components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-image')

    wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-media-placeholder__button.is-tertiary')
    wait_and_send_keys(driver, By.CLASS_NAME, 'block-editor-media-placeholder__url-input-field', url)
    wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-media-placeholder__url-input-submit-button.has-icon')

def image_cover(driver):
    time.sleep(2)
    #Vuelve el tiem una imagen
    wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-switcher')
    wait_and_click(driver,By.CLASS_NAME,'components-button.components-menu-item__button.editor-block-list-item-image')
    time.sleep(2)
    #Le da la propiedad cover
    wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-switcher')
    wait_and_click(driver,By.CLASS_NAME,'components-button.components-menu-item__button.editor-block-list-item-cover')
    time.sleep(2)
    #Selecciona el coneedor dentro de la imagen
    wait_and_click(driver,By.CLASS_NAME,'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.has-text-align-center.has-large-font-size.wp-block-paragraph.rich-text')
    wait_and_click(driver,By.CLASS_NAME,'components-button.components-dropdown-menu__toggle.has-icon')
    time.sleep(2)
    #Elimina el contenido
    wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(By.CSS_SELECTOR,'.components-menu-group button')
    last_Btn = Btns[-1]
    last_Btn.click()
    #Elimina el contenedor
    wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(By.CSS_SELECTOR,'.components-menu-group button')
    last_Btn = Btns[-1]
    last_Btn.click()

def insert_title(driver,title,size):
    wait_and_insert_item(driver,"Heading","components-button.block-editor-block-types-list__item.editor-block-list-item-heading")
    time.sleep(1)
    #cambia el texto del interior
    wait_and_send_keys(driver,By.CLASS_NAME,'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-heading.rich-text', title)
    wait_and_send_keys(driver,By.CLASS_NAME,'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-heading.rich-text', Keys.ESCAPE)
    wait_and_click(driver,By.CLASS_NAME,'components-button.block-selection-button_select-button')
    time.sleep(2)
    #Selecciona el icono para cambiar los botones 
    wait_and_click(driver,By.XPATH,'//button[@aria-label="Change level"]')
    time.sleep(2)
    #Recupera todo el listado de opciones disponibles y Selecciona la segun el tamaño
    btns = driver.find_elements(By.XPATH,'//div[@aria-label="Change level"]//button')
    btn = btns[size]
    aria_checked = btn.get_attribute('aria-checked')
    
    if aria_checked == 'true':
        print("El boton no se puede seleccionar")
    else:
        btn.click()

    #Selecciona el icono para alinear el texto
    wait_and_click(driver,By.XPATH,'//button[@aria-label="Align text"]')
    time.sleep(2)
    #Recupera todo el listado de opciones disponibles y elige el numero 2
    align = driver.find_elements(By.XPATH,'//div[@aria-label="Align text"]//button')
    center = align[1]
    center.click()
    # Selecciona el primer icono de da opciones generales
    wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(By.CSS_SELECTOR,'.components-menu-group button')
    last_Btn = Btns[0]
    last_Btn.click()

def insert_button(driver,text,url,align):
    wait_and_insert_item(driver,"Buttons","components-button.block-editor-block-types-list__item.editor-block-list-item-buttons")
    time.sleep(1)

    #cambia el texto del interior
    divs = driver.find_elements(By.CLASS_NAME,'block-editor-rich-text__editable.wp-block-button__link.wp-element-button.rich-text')

    # Ingresa el texto al ultimo boton creado
    divs[-1].send_keys(text)
    divs[-1].send_keys(Keys.ESCAPE)

    wait_and_click(driver,By.CLASS_NAME,'components-button.block-selection-button_select-button')
    time.sleep(2)
    wait_and_click(driver,By.XPATH,'//button[@aria-label="Change items justification"]')

    # #Recupera todo el listado de opciones disponibles y Selecciona la segun el tamaño
    btns = driver.find_elements(By.XPATH,'//div[@aria-label="Change items justification"]//button')
    btn = btns[align]
    btn.click()
    time.sleep(2)

    wait_and_click(driver,By.XPATH,'//button[@aria-label="Link"]')
    time.sleep(1)

    #Ingresa la url 
    wait_and_send_keys(driver,By.CLASS_NAME,'block-editor-url-input__input',url)
    wait_and_send_keys(driver,By.CLASS_NAME,'block-editor-url-input__input',Keys.ENTER)

    # Selecciona el primer icono de da opciones generales
    for _ in range(2): 
        wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
        Btns = driver.find_elements(By.CSS_SELECTOR,'.components-menu-group button')
        last_Btn = Btns[0]
        last_Btn.click()

def wait_and_click(driver, by, value):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
    element.click()

def wait_and_send_keys(driver, by, value, keys):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))
    element.send_keys(keys)

def wait_and_insert_item(driver,value,iconClass):
    try:
        wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-button-block-appender')
    except:    
        wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-inserter__toggle.has-icon')
    
    wait_and_send_keys(driver, By.CLASS_NAME, 'components-search-control__input', value)
    wait_and_click(driver, By.CLASS_NAME, iconClass)

def container_columns(driver,index):

    try:
        wait_and_click(driver,By.XPATH,'//ul[@class="block-editor-block-breadcrumb"]//button[text()="Page"]')
    except:
        print("Es primer contenedor")

    wait_and_insert_item(driver,"container", 'components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-container')
    buttons = driver.find_elements(By.XPATH, '//ul[@class="block-editor-block-variation-picker__variations"]/li/button')
    # Seleccionar el botón en una posición específica (por ejemplo, el segundo botón)
    if 0 <= index < len(buttons):
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

#creacion del contenedor
container_columns(driver,0)

#Insertar la imagen
insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg')

#Vuelve la imagen insertada en cover
image_cover(driver)

# Inserta un titulo de Tamaño H1
insert_title(driver,'Este es un titulo de ejemplo', 0)
insert_title(driver,'Este es un H2', 1)

#Inserta un boton
insert_button(driver,'Contactanos','tel: 111111111',1)

#creacion del contenedor
container_columns(driver,0)

insert_title(driver,'Este es un H2', 1)

time.sleep(60)
driver.quit()


# # Insertar párrafo - sigue el mismo patrón
# wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-block-types-list__item.editor-block-list-item-paragraph')
# wait_and_send_keys(driver, By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[3]/div[3]/div/div[2]/div[2]/div/div/div/div/p', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.')

# Continuar con el flujo del script
# ...

# Cerrar el navegador al finalizar
 
# components-button block-editor-media-placeholder__button is-tertiary