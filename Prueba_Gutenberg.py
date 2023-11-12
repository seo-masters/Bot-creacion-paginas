from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#
# Componentes
# def HEADER_PRINCIPAL_DE_PAGINAS(driver):
#     container_father(driver,0,False)

#     insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg',False,True)

#     insert_title(driver,'#1 EN BRUJOS EN CHICAGO IL', 0, False)
#     insert_title(driver,'+1 872-314-5247', 1,False)
#     insert_title(driver,'BRUJO PODEROSOS EN HECHICERÍA Y MAGIA NEGRA CON VUDÚ Y AMARRE DE PAREJAS, AMOR Y DINERO.', 1,False)
#     insert_button(driver,'¡LLAMA HOY +1 872-314-5247!','tel:1111111',1,False)
#     insert_button(driver,'TRABAJOS A DISTANCIA 100% GARANTIZADOS','tel:1111111',1,False)

# def IMAGEN_PARRAFO (driver):
#     container_father(driver,0,False)

#     insert_title(driver,'Añade aquí tu texto de cabecera', 1,False)

#     container_father(driver,1,False)

#     insert_image('https://magianegrachicago.com/wp-content/uploads/2023/07/amarres-en-chicago-efectivos-amarres-de-amor-chicago.jpg',False,False)
#     insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',False)

# def AREA_DE_SERVICIOS(driver):
#     for _ in range(2):
#         container_father(driver,3,False)

#         for _ in range(4):
#             insert_image('https://imgs.search.brave.com/YTY9SurNAwLvr1qDnR8Hn9mn2vH5ITPfZe26jpeFEQs/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudGhlbm91bnBy/b2plY3QuY29tL3Bu/Zy8xMTE5NTAyLTIw/MC5wbmc',False,False)
#             insert_title(driver,'AMARRES DE AMOR', 2,True)


#     container_father(driver,0,False)

#     wait_and_insert_item(driver,'Shortcode','components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode',False)

# def LLAMADO_DE_ACCION_1(driver):
#     container_father(driver,0,False)
    
#     insert_title(driver,'Añade aquí tu texto de cabecera', 1,False)
#     insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ',False)
#     insert_paragraph(driver,'Llámame al : 872-314-5247 ',False)

#     insert_button(driver,'AMARRES DE AMOR DALLAS TX','tel:1111111',1,False)

# def PARRAFO_BENEFICIOS(driver):
#     container_father(driver,1,False)

#     insert_title(driver,'¿Cómo trabajamos en la Botanica del Amor?', 1,False)
#     insert_paragraph(driver,'En Gorillas Gym Bogotá ofrecemos una variedad de servicios para satisfacer todas tus necesidades de entrenamiento físico. Contamos con instalaciones de alta calidad y equipos modernos que te ayudarán a alcanzar tus metas de acondicionamiento físico.\n\nNuestro equipo de entrenadores altamente capacitados está disponible para brindarte asesoramiento personalizado y diseñar un plan de entrenamiento adaptado a tus necesidades y objetivos específicos.\n\nAdemás, ofrecemos una amplia variedad de clases grupales, como spinning, yoga, pilates y entrenamiento de fuerza, que te permitirán diversificar tus rutinas de ejercicio y mantenerte motivado.\n\nEn Gorillas Gym Bogotá también tenemos un servicio exclusivo de nutrición y asesoramiento dietético, para que puedas complementar tu entrenamiento con una alimentación balanceada y obtener resultados aún más satisfactorios.\n\nNo importa si eres un principiante o un atleta experimentado, en Gorillas Gym Bogotá encontrarás el ambiente perfecto para entrenar y alcanzar tus metas de fitness. ¡Ven y únete a nuestra comunidad fitness hoy! ',True)

#     insert_shortcode(driver,'[wpforms id="7"]')

# def GALERIA_VIDEOS(driver):
#     container_father(driver,0,False)

#     insert_title(driver,'Ayudas espirituales y Brujeria del amor en Chicago', 1,False)

#     container_father(driver,1,False)

#     insert_title(driver,'Ayudas espirituales y Brujeria del amor en Chicago', 1,False)
#     insert_paragraph(driver,'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',True)

#     insert_video('https://youtu.be/BEQ_HMJaxS0',False)

#     container_father(driver,1,False)

#     insert_video('https://youtu.be/BEQ_HMJaxS0',False)

#     insert_title(driver,'Ayudas espirituales y Brujeria del amor en Chicago', 2,False)
#     insert_paragraph(driver,'Excepteur sint occaecat cupidatat non proident',True)
#     insert_paragraph(driver,'Llamanos al :+1 872-314-5247',True)

#     insert_button(driver,'CONTACTANOS','http://+18723145247/',1,False)

# def LLAMADO_DE_ACCION_2(driver):
#     container_father(driver,0,False)
    
#     insert_title(driver,'Añade aquí tu texto de cabecera', 1,False)
#     insert_paragraph(driver,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ',False)
#     insert_paragraph(driver,'Llámame al : 872-314-5247 ',False)

#     insert_button(driver,'AMARRES DE AMOR DALLAS TX','tel:1111111',1,False)

# def PARRAFO_CIUDAD_MAPA_NO_GEO(driver):
#     container_father(driver,1,False)

#     insert_title(driver,'Añade aquí tu texto de cabecera', 1,False)
#     insert_paragraph(driver,'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',True)

#     wait_and_insert_item(driver,'Shortcode','components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode',False)

# def RECURSOS(driver):
#     container_father(driver,2,False)

#     for _ in range(3):
#         insert_image('https://botanicadelamor.com/wp-content/uploads/2023/04/botanica-del-amor-amarres-de-amor-chicago-illinois-768x768.jpg',False,False)
#         insert_title(driver,'GUBERNAMENTAL', 2,True)
#         insert_title(driver,'Texto por hiper enlace', 3,True)
#         insert_title(driver,'Texto por hiper enlace', 3,True)
#         insert_title(driver,'Texto por hiper enlace', 3,True)

# def PARRAFO_CONCLUSION(driver):
#     container_father(driver,0,False)

#     insert_title(driver,'GUBERNAMENTAL', 1,False)
#     insert_paragraph(driver,'Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.',False)

# def ZIP_CODE_SIN_GEO(driver):
#     container_father(driver,0,False)

#     insert_title(driver,'Párrafo Conclusión', 1,False)

#     container_father(driver,3,False)

#     for _ in range(3):
#         insert_paragraph(driver,'4411',False)
#         for _ in range(12):
#             insert_paragraph(driver,'4411',True)

# def GEOLOCALIZACION(driver):
#     container_father(driver,0,False)

#     insert_title(driver,'UBICACION', 1,False)
#     insert_paragraph(driver,'istrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.',False)

#     container_father(driver,2,False)

#     for _ in range(3):
#         insert_image('https://imgs.search.brave.com/YTY9SurNAwLvr1qDnR8Hn9mn2vH5ITPfZe26jpeFEQs/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudGhlbm91bnBy/b2plY3QuY29tL3Bu/Zy8xMTE5NTAyLTIw/MC5wbmc',False,False)

#     container_father(driver,0,False)

#     insert_title(driver,'Como llegar a nuestra Botánica Del Amor', 1,False)

#     container_father(driver,0,False)

#     insert_paragraph(driver,'Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.',False)

#     container_father(driver,2,False)

#     for _ in range(3):
#         insert_mapa(driver,'https://www./google.com/maps/d/viewer?mid=1TRQM_J3hY2-zUevr8KYhG8Mi-AsIYOE&ll=41.830121660387796%2C-87.69220170000001&z=13')

#     container_father(driver,1,False)

#     wait_and_insert_item(driver,'Shortcode','components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode',False)
#     insert_video('https://youtu.be/BEQ_HMJaxS0',False)

options = webdriver.ChromeOptions()
options.service_args = ['--executable_path=C:\driver_chrome\chromedriver.exe']

driver = webdriver.Chrome(options=options)
# driver.get("https://vozavoz.live-website.com/wp-admin")
# driver.maximize_window()

# # Iniciar sesión
# wait_and_send_keys(driver, By.ID, 'user_login', 'VozaVoz_Admin')
# wait_and_send_keys(driver, By.ID, 'user_pass', 'Voz23#20Azteca')
# wait_and_click(driver, By.ID, 'wp-submit')

# Navegar a la sección de páginas
# wait_and_click(driver, By.ID, 'menu-pages')
# wait_and_click(driver, By.CLASS_NAME, 'page-title-action')


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

time.sleep(60)
driver.quit()