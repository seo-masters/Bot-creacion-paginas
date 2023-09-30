from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.service_args = ['--executable_path=C:\driver_chrome\chromedriver.exe']

driver = webdriver.Chrome(options=options)
driver.get("https://vozavoz.live-website.com/wp-admin")
driver.maximize_window()

def seleccionarWidget(nombreElemento):

    time.sleep(2)

    btnAdd = driver.find_element(By.CLASS_NAME,"components-button.block-editor-inserter__toggle.has-icon")
    btnAdd.click()

    time.sleep(2)

    inputSearch = driver.find_element(By.CLASS_NAME,"components-search-control__input")
    inputSearch.send_keys(nombreElemento)

    time.sleep(2)

    # widget = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/button")
    
def seleccionarwidget_central(nombreElemento1):
    time.sleep(2)
    sect1_2_3 = driver.find_element(By.CLASS_NAME, "components-button.block-editor-button-block-appender")
    sect1_2_3.click()
    time.sleep(2)
    sendtext_sect1 = driver.find_element(By.ID, "components-search-control-1")
    sendtext_sect1.send_keys(nombreElemento1)

def intafter():
    inputTitle = driver.find_element(By.CLASS_NAME,"components-button.edit-post-header-toolbar__document-overview-toggle.has-icon")
    print("Hola mundo")
    inputTitle.click()

    time.sleep(2)

    elementos = driver.find_elements(By.CLASS_NAME, "components-button.block-editor-list-view-block__menu.components-dropdown-menu__toggle.has-icon")
    ultimo_elemento = elementos[-1]
    ultimo_elemento.click()

    time.sleep(2)

    btnAfter = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div/button[5]")
    btnAfter.click()

def intafter_2():
    elementos = driver.find_elements(By.CLASS_NAME, "components-button.block-editor-list-view-block__menu.components-dropdown-menu__toggle.has-icon")
    ultimo_elemento = elementos[-1]
    ultimo_elemento.click()

    time.sleep(2)

    btnAfter = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div/button[5]")
    btnAfter.click()

inputUser = driver.find_element(By.ID,'user_login')
inputUser.send_keys('VozaVoz_Admin')

inputPass = driver.find_element(By.ID,'user_pass')
inputPass.send_keys('Voz23#20Azteca')

inputPass = driver.find_element(By.ID,'wp-submit')
inputPass.send_keys(Keys.ENTER)

time.sleep(1)

button=driver.find_element(By.ID, "menu-pages")
button.click()
time.sleep(1)

button=driver.find_element(By.CLASS_NAME, "page-title-action")
button.click()
time.sleep(2)

seleccionarWidget("container")

time.sleep(2)

# components-button edit-post-header-toolbar__document-overview-toggle has-icon
# elementos = driver.find_elements(By.CLASS_NAME, "components-button.block-editor-list-view-block__menu.components-dropdown-menu__toggle.has-icon")
#     ultimo_elemento = elementos[-1]
#     ultimo_elemento.click()

# components-button edit-post-header-toolbar__document-overview-toggle is-pressed has-icon

sect1 = driver.find_element(By.CLASS_NAME, "components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-container")
sect1.click()

time.sleep(2)

sect1_2 = driver.find_element(By.CLASS_NAME, "components-button.block-editor-block-variation-picker__variation.is-secondary.has-icon")
sect1_2.click()

time.sleep(2)

seleccionarwidget_central("image")

time.sleep(2)

sect1_2_3 = driver.find_element(By.CLASS_NAME, "components-button.block-editor-block-types-list__item.editor-block-list-item-image")
sect1_2_3.click()
time.sleep(2)

image_url = driver.find_element(By.CLASS_NAME, "components-button.block-editor-media-placeholder__button.is-tertiary")
image_url.click()
time.sleep(2)

inputUrl = driver.find_element(By.CLASS_NAME,"block-editor-media-placeholder__url-input-field")
inputUrl.send_keys("https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg")
inputUrl.send_keys(Keys.ENTER)
time.sleep(2)

intafter()

seleccionarWidget("Title")

insertTitle = driver.find_element(By.CLASS_NAME, "components-button.block-editor-block-types-list__item.editor-block-list-item-post-title")
insertTitle.click()

time.sleep(2)
title_1 = driver.find_element(By.CLASS_NAME, "block-editor-rich-text__editable.block-editor-block-list__block.wp-block.is-selected.wp-block-post-title.rich-text")
title_1.send_keys("Hola Mundo")

intafter_2()

seleccionarWidget("paragraph")

time.sleep(2)

btnObject = driver.find_element(By.CLASS_NAME,'components-button.block-editor-block-types-list__item.editor-block-list-item-paragraph')
btnObject.click()

time.sleep(2)

parragrafo = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[3]/div[3]/div/div[2]/div[2]/div/div/div/div/p")
parragrafo.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
time.sleep(2)

#-------------------------------------------------------------------------------------------------------------------------------------


newContent = driver.find_element(By.CLASS_NAME, "components-button.block-editor-block-breadcrumb__button.is-tertiary")
newContent.send_keys(Keys.ENTER)

time.sleep(3)

driver.execute_script('document.querySelector("#editor > div > div.edit-post-layout.is-mode-visual.has-metaboxes.interface-interface-skeleton.has-footer > div.interface-interface-skeleton__editor > div.interface-interface-skeleton__body > div.interface-navigable-region.interface-interface-skeleton__content > div.edit-post-visual-editor > div.edit-post-visual-editor__content-area > div > div.editor-styles-wrapper.block-editor-writing-flow.ast-stacked-title-visibility > div.is-root-container.is-layout-flow.wp-block-post-content-is-layout-flow.wp-block-post-content.block-editor-block-list__layout > div.block-list-appender.wp-block > div > div > button").click()')
time.sleep(5)

sendtext_sect1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div/div/input")
sendtext_sect1.send_keys("container")
time.sleep(5)
newcontainer = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/button")
newcontainer.click()
time.sleep(5)
newcontainer2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/fieldset/ul/li[2]/button")
newcontainer2.click()
time.sleep(5)
newcontainer2_1 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[3]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/button")
newcontainer2_1.click()

newcontainer2_1_1 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div/div/input")
newcontainer2_1_1.send_keys("image")

newcontainer2_1_1_1 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[3]/button")
newcontainer2_1_1_1.click()

#time.sleep(2)
#driver.execute_script('document.querySelector("#id-9o4huq-6").click()')
#time.sleep(2)
#driver.execute_script('document.querySelector("#editor > div > div.edit-post-layout.is-mode-visual.has-metaboxes.interface-interface-skeleton.has-footer > div.interface-interface-skeleton__editor > div.interface-interface-skeleton__body > div.interface-navigable-region.interface-interface-skeleton__content > div.edit-post-visual-editor > div.edit-post-visual-editor__content-area > div > div.editor-styles-wrapper.block-editor-writing-flow.ast-stacked-title-visibility > div.is-root-container.is-layout-flow.wp-block-post-content-is-layout-flow.wp-block-post-content.block-editor-block-list__layout > div.uagb-container-variation-picker > div > fieldset > ul > li:nth-child(2) > button").click()')
#time.sleep(2)

#close = driver.find_element(By.CLASS_NAME,"components-button.edit-post-editor__document-overview-panel__close-button.has-icon")
#close.click()

#newContent2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div/button")
#time.sleep(5)
#newContent2.click()

#time.sleep(10)

#sect1 = driver.find_element(By.CLASS_NAME, "components-button.block-editor-block-types-list__item.editor-block-list-item-uagb-container")
#sect1.click()

time.sleep(300)

#intafter_2()

#seleccionarWidget("container")

#time.sleep(5)

