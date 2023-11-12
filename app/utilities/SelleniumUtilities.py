from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def wait_and_click(driver, by, value):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, value)))
    element.click()


def wait_and_send_keys(driver, by, value, keys):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, value)))
    element.send_keys(keys)


def wait_and_insert_item(driver, value, iconClass, col):
    scroll_down(driver)
    time.sleep(1)
    if col:
        try:
            wait_and_click(
                driver, By.CLASS_NAME, 'components-button.block-editor-inserter__toggle.has-icon')
        except Exception as e:
            print(e)
    else:
        try:
            wait_and_click(driver, By.CLASS_NAME,
                           'components-button.block-editor-button-block-appender')
        except:
            wait_and_click(
                driver, By.CLASS_NAME, 'components-button.block-editor-inserter__toggle.has-icon')

    wait_and_send_keys(driver, By.CLASS_NAME,
                       'components-search-control__input', value)
    time.sleep(1)
    wait_and_click(driver, By.CLASS_NAME, iconClass)


def scroll_down(driver):
    try:
        # interface-navigable-region interface-interface-skeleton__content
        contenedor_scroll = driver.find_element(
            By.CLASS_NAME, "editor-styles-wrapper.block-editor-writing-flow.ast-stacked-title-visibility")

        # Desplazar el contenedor hasta el final
        contenedor_scroll.send_keys(Keys.END)

    except Exception as e:
        print("No hay scroll", e)


def navigate_to_website(driver,url):
    driver.get(f"https://{url}/wp-admin")
    driver.maximize_window()