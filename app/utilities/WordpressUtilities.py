from app.utilities import wait_and_click, wait_and_insert_item, wait_and_send_keys, scroll_down, By, Keys
import time
import os

def insert_shortcode(driver, shortcode):
    wait_and_insert_item(
        driver, 'Shortcode', 'components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode', False)
    wait_and_send_keys(driver, By.CLASS_NAME,
                       'block-editor-plain-text.blocks-shortcode__textarea', shortcode)

def insert_HTML(driver, html):
    wait_and_insert_item(
        driver, 'Custom HTML', 'components-button.block-editor-block-types-list__item.editor-block-list-item-html', False)
    wait_and_send_keys(driver, By.CLASS_NAME, 'block-editor-plain-text', html)

def insert_mapa(driver, mapa):
    mapaHTML = f'<iframe src="{mapa}" width="640" height="300"></iframe>'
    insert_HTML(driver, mapaHTML)

def insert_image(driver, url, col, cover):
    time.sleep(2)

    wait_and_insert_item(
        driver, 'Image', 'components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-image', col)

    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.block-editor-media-placeholder__button.is-tertiary')
    wait_and_send_keys(driver, By.CLASS_NAME,
                       'block-editor-media-placeholder__url-input-field', url)
    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.block-editor-media-placeholder__url-input-submit-button.has-icon')

    if cover:
        image_cover(driver)
    else:
        wait_and_click(driver, By.CLASS_NAME,
                       'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
        Btns = driver.find_elements(
            By.CSS_SELECTOR, '.components-menu-group button')
        last_Btn = Btns[0]
        last_Btn.click()

def insert_video(driver, url, col):
    time.sleep(2)

    wait_and_insert_item(
        driver, 'Video', 'components-button.block-editor-block-types-list__item.editor-block-list-item-video', col)

    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.block-editor-media-placeholder__button.is-tertiary')
    wait_and_send_keys(driver, By.CLASS_NAME,
                       'block-editor-media-placeholder__url-input-field', url)
    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.block-editor-media-placeholder__url-input-submit-button.has-icon')

    wait_and_click(driver, By.CLASS_NAME,
                   'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(
        By.CSS_SELECTOR, '.components-menu-group button')
    last_Btn = Btns[0]
    last_Btn.click()

def image_cover(driver):
    time.sleep(2)
    # Vuelve el tiem una imagen
    wait_and_click(driver, By.CLASS_NAME,
                   'components-dropdown.components-dropdown-menu.block-editor-block-switcher')
    time.sleep(1)
    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.components-menu-item__button.editor-block-list-item-image')
    time.sleep(2)
    # Le da la propiedad cover
    wait_and_click(driver, By.CLASS_NAME,
                   'components-dropdown.components-dropdown-menu.block-editor-block-switcher')
    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.components-menu-item__button.editor-block-list-item-cover')
    time.sleep(2)
    # Selecciona el coneedor dentro de la imagen
    wait_and_click(driver, By.CLASS_NAME,
                   'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.has-text-align-center.has-large-font-size.wp-block-paragraph.rich-text')
    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.components-dropdown-menu__toggle.has-icon')
    time.sleep(2)
    # Elimina el contenido
    wait_and_click(driver, By.CLASS_NAME,
                   'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(
        By.CSS_SELECTOR, '.components-menu-group button')
    last_Btn = Btns[-1]
    last_Btn.click()
    # Elimina el contenedor
    wait_and_click(driver, By.CLASS_NAME,
                   'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(
        By.CSS_SELECTOR, '.components-menu-group button')
    last_Btn = Btns[-1]
    last_Btn.click()

def insert_title(driver, title, size, col):
    wait_and_insert_item(
        driver, "Heading", "components-button.block-editor-block-types-list__item.editor-block-list-item-heading", col)
    time.sleep(1)
    # cambia el texto del interior
    wait_and_send_keys(driver, By.CLASS_NAME,
                       'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-heading.rich-text', title)
    wait_and_send_keys(driver, By.CLASS_NAME,
                       'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-heading.rich-text', Keys.ESCAPE)
    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.block-selection-button_select-button')
    time.sleep(2)
    # Selecciona el icono para cambiar los botones
    wait_and_click(driver, By.XPATH, '//button[@aria-label="Change level"]')
    time.sleep(2)
    # Recupera todo el listado de opciones disponibles y Selecciona la segun el tamaño
    btns = driver.find_elements(
        By.XPATH, '//div[@aria-label="Change level"]//button')
    btn = btns[size]
    aria_checked = btn.get_attribute('aria-checked')

    if aria_checked == 'true':
        print("El boton no se puede seleccionar")
    else:
        btn.click()

    # Selecciona el icono para alinear el texto
    wait_and_click(driver, By.XPATH, '//button[@aria-label="Align text"]')
    time.sleep(2)
    # Recupera todo el listado de opciones disponibles y elige el numero 2
    align = driver.find_elements(
        By.XPATH, '//div[@aria-label="Align text"]//button')
    center = align[1]
    center.click()

    time.sleep(1)
    # Selecciona el primer icono de da opciones generales
    wait_and_click(driver, By.CLASS_NAME,
                   'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(
        By.CSS_SELECTOR, '.components-menu-group button')
    last_Btn = Btns[0]
    last_Btn.click()

def insert_paragraph(driver, text, col):

    wait_and_insert_item(
        driver, 'Paragraph', 'components-button.block-editor-block-types-list__item.editor-block-list-item-paragraph', col)
    wait_and_send_keys(driver, By.CLASS_NAME,
                       'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-paragraph.rich-text', text)
    wait_and_send_keys(driver, By.CLASS_NAME,
                       'block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-paragraph.rich-text', Keys.ESCAPE)
    scroll_down(driver)
    time.sleep(2)
    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.block-selection-button_select-button')
    wait_and_click(driver, By.CLASS_NAME,
                   'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
    Btns = driver.find_elements(
        By.CSS_SELECTOR, '.components-menu-group button')
    last_Btn = Btns[0]
    last_Btn.click()

def insert_button(driver, text, url, align, col):
    wait_and_insert_item(
        driver, "Buttons", "components-button.block-editor-block-types-list__item.editor-block-list-item-buttons", col)
    time.sleep(1)

    # cambia el texto del interior
    divs = driver.find_elements(
        By.CLASS_NAME, 'block-editor-rich-text__editable.wp-block-button__link.wp-element-button.rich-text')

    # Ingresa el texto al ultimo boton creado
    divs[-1].send_keys(text)
    divs[-1].send_keys(Keys.ESCAPE)

    wait_and_click(driver, By.CLASS_NAME,
                   'components-button.block-selection-button_select-button')
    time.sleep(2)
    wait_and_click(driver, By.XPATH,
                   '//button[@aria-label="Change items justification"]')

    # #Recupera todo el listado de opciones disponibles y Selecciona la segun el tamaño
    btns = driver.find_elements(
        By.XPATH, '//div[@aria-label="Change items justification"]//button')
    btn = btns[align]
    btn.click()
    time.sleep(2)

    wait_and_click(driver, By.XPATH, '//button[@aria-label="Link"]')
    time.sleep(1)

    # Ingresa la url
    wait_and_send_keys(driver, By.CLASS_NAME,
                       'block-editor-url-input__input', url)
    wait_and_send_keys(driver, By.CLASS_NAME,
                       'block-editor-url-input__input', Keys.ENTER)

    # Selecciona el primer icono de da opciones generales
    for _ in range(2):
        wait_and_click(driver, By.CLASS_NAME,
                       'components-dropdown.components-dropdown-menu.block-editor-block-settings-menu')
        Btns = driver.find_elements(
            By.CSS_SELECTOR, '.components-menu-group button')
        last_Btn = Btns[0]
        last_Btn.click()

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

def login(driver,USERNAME,PASSWORD):
    time.sleep(2)
    wait_and_send_keys(driver, By.ID, 'user_login', USERNAME)
    wait_and_send_keys(driver, By.ID, 'user_pass', PASSWORD)
    wait_and_click(driver, By.ID, 'wp-submit')

def navigate_to_pages_section(driver):
    wait_and_click(driver, By.ID, 'menu-pages')
    wait_and_click(driver, By.CLASS_NAME, 'page-title-action')