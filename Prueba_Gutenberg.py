from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Elementos:
def scroll_down(driver):
    try:
        # interface-navigable-region interface-interface-skeleton__content
        contenedor_scroll = driver.find_element(By.CLASS_NAME,"editor-styles-wrapper.block-editor-writing-flow.ast-stacked-title-visibility")

        # Desplazar el contenedor hasta el final
        contenedor_scroll.send_keys(Keys.END)

    except Exception as e:
        print("No hay scroll", e)

def insert_image(url,col,cover):
    time.sleep(2)
   
    wait_and_insert_item(driver,'Image','components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-image',col)

    wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-media-placeholder__button.is-tertiary')
    wait_and_send_keys(driver, By.CLASS_NAME, 'block-editor-media-placeholder__url-input-field', url)
    wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-media-placeholder__url-input-submit-button.has-icon')

    if cover:
        image_cover(driver)
    else:
        wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
        Btns = driver.find_elements(By.CSS_SELECTOR,'.components-menu-group button')
        last_Btn = Btns[0]
        last_Btn.click()

def image_cover(driver):
    time.sleep(2)
    #Vuelve el tiem una imagen
    wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-switcher')
    time.sleep(1)
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

def insert_title(driver,title,size,col):
    wait_and_insert_item(driver,"Heading","components-button.block-editor-block-types-list__item.editor-block-list-item-heading",col)
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

    time.sleep(1)
    # Selecciona el primer icono de da opciones generales
    wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(By.CSS_SELECTOR,'.components-menu-group button')
    last_Btn = Btns[0]
    last_Btn.click()

def insert_paragraph(driver,text,col):

    wait_and_insert_item(driver,'Paragraph','components-button.block-editor-block-types-list__item.editor-block-list-item-paragraph',col)
    wait_and_send_keys(driver,By.CLASS_NAME,'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-paragraph.rich-text',text)
    wait_and_send_keys(driver,By.CLASS_NAME,'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-paragraph.rich-text',Keys.ESCAPE)
    wait_and_click(driver,By.CLASS_NAME,'components-button.block-selection-button_select-button')
    wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(By.CSS_SELECTOR,'.components-menu-group button')
    last_Btn = Btns[0]
    last_Btn.click()

def insert_button(driver,text,url,align,col):
    wait_and_insert_item(driver,"Buttons","components-button.block-editor-block-types-list__item.editor-block-list-item-buttons",col)
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

def wait_and_insert_item(driver,value,iconClass,col):

    scroll_down(driver)

    time.sleep(1)

    if col:
        try:

            wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-inserter__toggle.has-icon')
        except Exception as e:    
            print(e)
    else:
        try:
            wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-button-block-appender')
        except:    
            wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-inserter__toggle.has-icon')
        
    wait_and_send_keys(driver, By.CLASS_NAME, 'components-search-control__input', value)
    time.sleep(1)
    wait_and_click(driver, By.CLASS_NAME, iconClass)

def container_father(driver,index,col):
   

    try:
        wait_and_click(driver,By.XPATH,'//ul[@class="block-editor-block-breadcrumb"]//button[text()="Page"]')
        scroll_down(driver)
    except:
        print('Primer contenedior')

    wait_and_insert_item(driver,"container", 'components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-container',col)
    buttons = driver.find_elements(By.XPATH, '//ul[@class="block-editor-block-variation-picker__variations"]/li/button')
    # Seleccionar el botón en una posición específica (por ejemplo, el segundo botón)
    if 0 <= index < len(buttons):
        buttons[index].click()
    else:
        print("La posición está fuera de rango")

    buttons = driver.find_elements(By.XPATH, '//ul[@class="block-editor-block-variation-picker__variations"]/li/button')
    # Seleccionar el botón en una posición específica (por ejemplo, el segundo botón)
    if 0 <= index < len(buttons):
        buttons[index].click()
    else:
        print("La posición está fuera de rango")

def add_column(driver,col):
    for _ in range(2):
        #Elimina el contenido
        wait_and_click(driver,By.CLASS_NAME,'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
        Btns = driver.find_elements(By.CSS_SELECTOR,'.components-menu-group button')
        last_Btn = Btns[0]
        last_Btn.click()

    wait_and_insert_item(driver,"container", 'components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-container',col)

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


# Seccion 1

container_father(driver,0,False)

insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg',False,True)

insert_title(driver,'Titulo para la demostracion', 0, False)
insert_title(driver,'Este es un H2', 1,False)
insert_button(driver,'Boton','tel:1111111',1,False)

# Seccion 2

container_father(driver,0,False)

insert_title(driver,'Este es un H2', 1,False)
insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',False)

# Seccion 3

container_father(driver,1,False)

insert_title(driver,'Este es un H2 DE OTRA SECCION', 1,False)
insert_button(driver,'anyway','tel:1111111',1,True)

insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg',False,False)

# Seccion 4

container_father(driver,0,False)

insert_title(driver,'Este es un llamado de accion', 1,False)
insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',False)
insert_button(driver,'Boton','tel:1111111',1,False)

# Seccion 5

container_father(driver,0,False)
insert_title(driver,'Servicios', 1,False)

try:
    for _ in range(2):
        container_father(driver,2,False)

        for _ in range(3):
            insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg',False,False)
            time.sleep(1)
            insert_title(driver,'Este es un H2 DE OTRA SECCION', 1,True)
            time.sleep(1)
            insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',True)
except:
    print('error')

# Seccion 6

container_father(driver,0,False)

insert_title(driver,'Reseñas', 1,False)
insert_paragraph(driver,'Lorem ipsum dolor sit amet.',True)

# # Seccion 7

container_father(driver,1,False)

insert_title(driver,'Titulo muy ataractivo a la lectura', 1,False)
insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',True)

insert_title(driver,'Esto es un video', 1,False)

# Seccion 8 

container_father(driver,1,False)

insert_title(driver,'Titulo para segundo llamado de accion', 1,False)

insert_title(driver,'Titulo muy ataractivo a la lectura', 1,False)
insert_button(driver,'Llamame','tel:1111111',1, True)

# Seccion 9

container_father(driver,1,False)

insert_title(driver,'[Shortcode]', 1,False)

insert_title(driver,'Otros servicios que ofrezco', 1,False)
insert_title(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 1,False)
insert_button(driver,'Boton','tel:1111111',1,True)

# Seccion 10

container_father(driver,0,False)

insert_title(driver,'Este es un llamado de accion', 1,False)
insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',False)
insert_button(driver,'Boton','tel:1111111',1,False)

#Seccion 11

container_father(driver,0,False)

insert_title(driver,'Mapa', 1,False)
insert_title(driver,'Mapa shortcode', 1,False)

# Seccion 12

container_father(driver,1,False)
insert_title(driver,'Nuestros clientes satisfechos', 1,False)

try:
   
    container_father(driver,2,False)

    for _ in range(3):
        insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg',False,False)
        time.sleep(1)
        insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',True)
        time.sleep(1)
        insert_title(driver,'Personas nombre', 1,True)
except:
    print('error')


# Seccion 13

container_father(driver,1,False)
insert_title(driver,'Mas recursos', 1,False)

try:
   
    container_father(driver,2,False)

    for _ in range(3):
        insert_title(driver,'Titulo recursos', 1,True)
        time.sleep(1)
        insert_button(driver,'Boton','tel:1111111',1,True)
        time.sleep(1)
        insert_button(driver,'Boton','tel:1111111',1,True)
        time.sleep(1)
        insert_button(driver,'Boton','tel:1111111',1,True)
        
except:
    print('error')

# Seccion 14

try:
   
    container_father(driver,3,False)

    insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg',False,False)
    time.sleep(1)
    
    insert_title(driver,'Servicios', 1,False)
    insert_paragraph(driver,'Lorem ipsum dolor sit amet',True)
    insert_paragraph(driver,'Lorem ipsum dolor sit amet',True)

    insert_title(driver,'Adress', 1,False)
    insert_paragraph(driver,'Lorem ipsum dolor sit amet',True)

    insert_title(driver,'Phone', 1,False)
    insert_paragraph(driver,'+1 6565465465',True)

except:
    print('error')



time.sleep(600)
driver.quit()
