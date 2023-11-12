from app.utilities.WordpressUtilities import container_father, insert_image, insert_title, insert_button, insert_paragraph, insert_shortcode, insert_video, insert_mapa, login, navigate_to_pages_section
from app.utilities.SelleniumUtilities import wait_and_insert_item, navigate_to_website


class WordpressComponent:
    def __init__(self, driver):
        self.driver = driver
        navigate_to_website(self.driver, url="vozavoz.live-website.com")
        login(self.driver,'VozaVoz_Admin','Voz23#20Azteca')
        navigate_to_pages_section(self.driver)

    def HEADER_PRINCIPAL_DE_PAGINAS(self):
        container_father(self.driver, 0, False)

        insert_image(
            self.driver, 'https://aztecavisual.com/wp-content/uploads/2023/09/maestros-espirituales-amuletos-preparados-1024x536.jpg', False, True)

        insert_title(self.driver, '#1 EN BRUJOS EN CHICAGO IL', 0, False)
        insert_title(self.driver, '+1 872-314-5247', 1, False)
        insert_title(
            self.driver, 'BRUJO PODEROSOS EN HECHICERÍA Y MAGIA NEGRA CON VUDÚ Y AMARRE DE PAREJAS, AMOR Y DINERO.', 1, False)
        insert_button(self.driver, '¡LLAMA HOY +1 872-314-5247!',
                      'tel:1111111', 1, False)
        insert_button(
            self.driver, 'TRABAJOS A DISTANCIA 100% GARANTIZADOS', 'tel:1111111', 1, False)

    def IMAGEN_PARRAFO(self):
        container_father(self.driver, 0, False)

        insert_title(self.driver, 'Añade aquí tu texto de cabecera', 1, False)

        container_father(self.driver, 1, False)

        insert_image(
            'https://aztecavisual.com/wp-content/uploads/2023/09/maestros-espirituales-amuletos-preparados-1024x536.jpg', False, False)
        insert_paragraph(
            self.driver, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam', False)

    def AREA_DE_SERVICIOS(self):
        for _ in range(2):
            container_father(self.driver, 3, False)

            for _ in range(4):
                insert_image('https://imgs.search.brave.com/YTY9SurNAwLvr1qDnR8Hn9mn2vH5ITPfZe26jpeFEQs/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudGhlbm91bnBy/b2plY3QuY29tL3Bu/Zy8xMTE5NTAyLTIw/MC5wbmc', False, False)
                insert_title(self.driver, 'AMARRES DE AMOR', 2, True)

        container_father(self.driver, 0, False)

        wait_and_insert_item(self.driver, 'Shortcode',
                             'components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode', False)

    def LLAMADO_DE_ACCION_1(self):
        container_father(self.driver, 0, False)

        insert_title(self.driver, 'Añade aquí tu texto de cabecera', 1, False)
        insert_paragraph(
            self.driver, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ', False)
        insert_paragraph(self.driver, 'Llámame al : 872-314-5247 ', False)

        insert_button(self.driver, 'AMARRES DE AMOR DALLAS TX',
                      'tel:1111111', 1, False)

    def PARRAFO_BENEFICIOS(self):
        container_father(self.driver, 1, False)

        insert_title(
            self.driver, '¿Cómo trabajamos en la Botanica del Amor?', 1, False)
        insert_paragraph(self.driver, 'En Gorillas Gym Bogotá ofrecemos una variedad de servicios para satisfacer todas tus necesidades de entrenamiento físico. Contamos con instalaciones de alta calidad y equipos modernos que te ayudarán a alcanzar tus metas de acondicionamiento físico.\n\nNuestro equipo de entrenadores altamente capacitados está disponible para brindarte asesoramiento personalizado y diseñar un plan de entrenamiento adaptado a tus necesidades y objetivos específicos.\n\nAdemás, ofrecemos una amplia variedad de clases grupales, como spinning, yoga, pilates y entrenamiento de fuerza, que te permitirán diversificar tus rutinas de ejercicio y mantenerte motivado.\n\nEn Gorillas Gym Bogotá también tenemos un servicio exclusivo de nutrición y asesoramiento dietético, para que puedas complementar tu entrenamiento con una alimentación balanceada y obtener resultados aún más satisfactorios.\n\nNo importa si eres un principiante o un atleta experimentado, en Gorillas Gym Bogotá encontrarás el ambiente perfecto para entrenar y alcanzar tus metas de fitness. ¡Ven y únete a nuestra comunidad fitness hoy! ', True)

        insert_shortcode(self.driver, '[wpforms id="7"]')

    def GALERIA_VIDEOS(self):
        container_father(self.driver, 0, False)

        insert_title(
            self.driver, 'Ayudas espirituales y Brujeria del amor en Chicago', 1, False)

        container_father(self.driver, 1, False)

        insert_title(
            self.driver, 'Ayudas espirituales y Brujeria del amor en Chicago', 1, False)
        insert_paragraph(
            self.driver, 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', True)

        insert_video('https://youtu.be/BEQ_HMJaxS0', False)

        container_father(self.driver, 1, False)

        insert_video('https://youtu.be/BEQ_HMJaxS0', False)

        insert_title(
            self.driver, 'Ayudas espirituales y Brujeria del amor en Chicago', 2, False)
        insert_paragraph(
            self.driver, 'Excepteur sint occaecat cupidatat non proident', True)
        insert_paragraph(self.driver, 'Llamanos al :+1 872-314-5247', True)

        insert_button(self.driver, 'CONTACTANOS',
                      'http://+18723145247/', 1, False)

    def LLAMADO_DE_ACCION_2(self):
        container_father(self.driver, 0, False)

        insert_title(self.driver, 'Añade aquí tu texto de cabecera', 1, False)
        insert_paragraph(
            self.driver, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ', False)
        insert_paragraph(self.driver, 'Llámame al : 872-314-5247 ', False)

        insert_button(self.driver, 'AMARRES DE AMOR DALLAS TX',
                      'tel:1111111', 1, False)

    def PARRAFO_CIUDAD_MAPA_NO_GEO(self):
        container_father(self.driver, 1, False)

        insert_title(self.driver, 'Añade aquí tu texto de cabecera', 1, False)
        insert_paragraph(
            self.driver, 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', True)

        wait_and_insert_item(self.driver, 'Shortcode',
                             'components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode', False)

    def RECURSOS(self):
        container_father(self.driver, 2, False)

        for _ in range(3):
            insert_image(
                'https://botanicadelamor.com/wp-content/uploads/2023/04/botanica-del-amor-amarres-de-amor-chicago-illinois-768x768.jpg', False, False)
            insert_title(self.driver, 'GUBERNAMENTAL', 2, True)
            insert_title(self.driver, 'Texto por hiper enlace', 3, True)
            insert_title(self.driver, 'Texto por hiper enlace', 3, True)
            insert_title(self.driver, 'Texto por hiper enlace', 3, True)

    def PARRAFO_CONCLUSION(self):
        container_father(self.driver, 0, False)

        insert_title(self.driver, 'GUBERNAMENTAL', 1, False)
        insert_paragraph(self.driver, 'Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.', False)

    def ZIP_CODE_SIN_GEO(self):
        container_father(self.driver, 0, False)

        insert_title(self.driver, 'Párrafo Conclusión', 1, False)

        container_father(self.driver, 3, False)

        for _ in range(3):
            insert_paragraph(self.driver, '4411', False)
            for _ in range(12):
                insert_paragraph(self.driver, '4411', True)

    def GEOLOCALIZACION(self):
        container_father(self.driver, 0, False)

        insert_title(self.driver, 'UBICACION', 1, False)
        insert_paragraph(
            self.driver, 'istrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.', False)

        container_father(self.driver, 2, False)

        for _ in range(3):
            insert_image('https://imgs.search.brave.com/YTY9SurNAwLvr1qDnR8Hn9mn2vH5ITPfZe26jpeFEQs/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudGhlbm91bnBy/b2plY3QuY29tL3Bu/Zy8xMTE5NTAyLTIw/MC5wbmc', False, False)

        container_father(self.driver, 0, False)

        insert_title(
            self.driver, 'Como llegar a nuestra Botánica Del Amor', 1, False)

        container_father(self.driver, 0, False)

        insert_paragraph(self.driver, 'Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.Lorem fistrum por la gloria de mi madre esse jarl aliqua llevame al sircoo. De la pradera ullamco qué dise usteer está la cosa muy malar.', False)

        container_father(self.driver, 2, False)

        for _ in range(3):
            insert_mapa(
                self.driver, 'https://www./google.com/maps/d/viewer?mid=1TRQM_J3hY2-zUevr8KYhG8Mi-AsIYOE&ll=41.830121660387796%2C-87.69220170000001&z=13')

        container_father(self.driver, 1, False)

        wait_and_insert_item(self.driver, 'Shortcode',
                             'components-button.block-editor-block-types-list__item.editor-block-list-item-shortcode', False)
        insert_video('https://youtu.be/BEQ_HMJaxS0', False)
