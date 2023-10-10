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

def insert_shortcode(driver,shortcode):
    wait_and_insert_item(driver,'Shortcode','components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode',False)
    wait_and_send_keys(driver,By.CLASS_NAME,'block-editor-plain-text.blocks-shortcode__textarea', shortcode)

def insert_HTML(driver,html):
    wait_and_insert_item(driver,'Custom HTML','components-button.block-editor-block-types-list__item.editor-block-list-item-html',False)
    wait_and_send_keys(driver,By.CLASS_NAME,'block-editor-plain-text', html)

def insert_mapa(driver,mapa):

    mapaHTML = f'<iframe src="{mapa}" width="640" height="300"></iframe>'
    insert_HTML(driver,mapaHTML)

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

def insert_video(url,col):
    time.sleep(2)
   
    wait_and_insert_item(driver,'Video','components-button.block-editor-block-types-list__item.editor-block-list-item-video',col)

    wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-media-placeholder__button.is-tertiary')
    wait_and_send_keys(driver, By.CLASS_NAME, 'block-editor-media-placeholder__url-input-field', url)
    wait_and_click(driver, By.CLASS_NAME, 'components-button.block-editor-media-placeholder__url-input-submit-button.has-icon')

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
    scroll_down(driver)
    time.sleep(2)
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

# Componentes
def HEADER_PRINCIPAL_DE_PAGINAS(driver):
    container_father(driver,0,False)

    insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg',False,True)

    insert_title(driver,'#1 EN BRUJOS EN CHICAGO IL', 0, False)
    insert_title(driver,'+1 872-314-5247', 1,False)
    insert_title(driver,'BRUJO PODEROSOS EN HECHICERÍA Y MAGIA NEGRA CON VUDÚ Y AMARRE DE PAREJAS, AMOR Y DINERO.', 1,False)
    insert_button(driver,'¡LLAMA HOY +1 872-314-5247!','tel:1111111',1,False)
    insert_button(driver,'TRABAJOS A DISTANCIA 100% GARANTIZADOS','tel:1111111',1,False)

def IMAGEN_PARRAFO (driver):
    container_father(driver,0,False)

    insert_title(driver,'Añade aquí tu texto de cabecera', 1,False)

    container_father(driver,1,False)

    insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg',False,False)
    insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',False)

def AREA_DE_SERVICIOS(driver):
    for _ in range(2):
        container_father(driver,3,False)

        for _ in range(4):
            insert_image('https://imgs.search.brave.com/YTY9SurNAwLvr1qDnR8Hn9mn2vH5ITPfZe26jpeFEQs/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudGhlbm91bnBy/b2plY3QuY29tL3Bu/Zy8xMTE5NTAyLTIw/MC5wbmc',False,False)
            insert_title(driver,'AMARRES DE AMOR', 2,True)


    container_father(driver,0,False)

    wait_and_insert_item(driver,'Shortcode','components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode',False)

def LLAMADO_DE_ACCION_1(driver):
    container_father(driver,0,False)
    
    insert_title(driver,'Añade aquí tu texto de cabecera', 1,False)
    insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ',False)
    insert_paragraph(driver,'Llámame al : 872-314-5247 ',False)

    insert_button(driver,'AMARRES DE AMOR DALLAS TX','tel:1111111',1,False)

def PARRAFO_BENEFICIOS(driver):
    container_father(driver,1,False)

    insert_title(driver,'¿Cómo trabajamos en la Botanica del Amor?', 1,False)
    insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ',True)

    insert_shortcode(driver,'[wpforms id="7"]')

def GALERIA_VIDEOS(driver):
    container_father(driver,0,False)

    insert_title(driver,'Ayudas espirituales y Brujeria del amor en Chicago', 1,False)

    container_father(driver,1,False)

    insert_title(driver,'Ayudas espirituales y Brujeria del amor en Chicago', 1,False)
    insert_paragraph(driver,'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',True)

    insert_video('https://youtu.be/BEQ_HMJaxS0',False)

    container_father(driver,1,False)

    insert_video('https://youtu.be/BEQ_HMJaxS0',False)

    insert_title(driver,'Ayudas espirituales y Brujeria del amor en Chicago', 2,False)
    insert_paragraph(driver,'Excepteur sint occaecat cupidatat non proident',True)
    insert_paragraph(driver,'Llamanos al :+1 872-314-5247',True)

    insert_button(driver,'CONTACTANOS','http://+18723145247/',1,False)

def LLAMADO_DE_ACCION_2(driver):
    container_father(driver,0,False)
    
    insert_title(driver,'Añade aquí tu texto de cabecera', 1,False)
    insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ',False)
    insert_paragraph(driver,'Llámame al : 872-314-5247 ',False)

    insert_button(driver,'AMARRES DE AMOR DALLAS TX','tel:1111111',1,False)

def PARRAFO_CIUDAD_MAPA_NO_GEO(driver):
    container_father(driver,1,False)

    insert_title(driver,'Añade aquí tu texto de cabecera', 1,False)
    insert_paragraph(driver,'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',True)

    wait_and_insert_item(driver,'Shortcode','components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode',False)

def RECURSOS(driver):
    container_father(driver,2,False)

    for _ in range(3):
        insert_image('https://botanicadelamor.com/wp-content/uploads/2023/04/botanica-del-amor-amarres-de-amor-chicago-illinois-768x768.jpg',False,False)
        insert_title(driver,'GUBERNAMENTAL', 2,True)
        insert_title(driver,'Texto por hiper enlace', 3,True)
        insert_title(driver,'Texto por hiper enlace', 3,True)
        insert_title(driver,'Texto por hiper enlace', 3,True)

def PARRAFO_CONCLUSION(driver):
    container_father(driver,0,False)

    insert_title(driver,'GUBERNAMENTAL', 1,False)
    insert_paragraph(driver,'Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.',False)

def ZIP_CODE_SIN_GEO(driver):
    container_father(driver,0,False)

    insert_title(driver,'Párrafo Conclusión', 1,False)

    container_father(driver,3,False)

    for _ in range(3):
        insert_paragraph(driver,'4411',False)
        for _ in range(12):
            insert_paragraph(driver,'4411',True)

def GEOLOCALIZACION(driver):
    container_father(driver,0,False)

    insert_title(driver,'UBICACION', 1,False)
    insert_paragraph(driver,'istrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.',False)

    container_father(driver,2,False)

    for _ in range(3):
        insert_image('https://imgs.search.brave.com/YTY9SurNAwLvr1qDnR8Hn9mn2vH5ITPfZe26jpeFEQs/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudGhlbm91bnBy/b2plY3QuY29tL3Bu/Zy8xMTE5NTAyLTIw/MC5wbmc',False,False)

    container_father(driver,0,False)

    insert_title(driver,'Como llegar a nuestra Botánica Del Amor', 1,False)

    container_father(driver,0,False)

    insert_paragraph(driver,'Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.',False)

    container_father(driver,2,False)

    for _ in range(3):
        wait_and_insert_item(driver,'Shortcode','components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode',False)

    container_father(driver,1,False)

    wait_and_insert_item(driver,'Shortcode','components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode',False)
    insert_video('https://youtu.be/BEQ_HMJaxS0',False)

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


# HEADER_PRINCIPAL_DE_PAGINAS(driver)

# IMAGEN_PARRAFO (driver)

# AREA_DE_SERVICIOS(driver)

# LLAMADO_DE_ACCION_1(driver)


# PARRAFO_BENEFICIOS(driver)


# GALERIA_VIDEOS(driver)


# LLAMADO_DE_ACCION_2(driver)


# PARRAFO_CIUDAD_MAPA_NO_GEO(driver)


# RECURSOS(driver)


# PARRAFO_CONCLUSION(driver)


# ZIP_CODE_SIN_GEO(driver)


# GEOLOCALIZACION(driver)

insert_mapa(driver,'https://www.google.com/maps/d/viewer?mid=1TRQM_J3hY2-zUevr8KYhG8Mi-AsIYOE&ll=41.830121660387796%2C-87.69220170000001&z=13')

time.sleep(60)
driver.quit()