from app.components import WordpressComponent
from app.drivers import selenium_driver

driver = selenium_driver()

class GeoLayout:
    def __init__(self, options):
        self.website_name = options["websiteName"]
        self.webpage_title = options["webpageTitle"]
        self.service = options["service"]
        self.city = options["location"]["city"]
        self.state = options["location"]["state"]
        self.map_url = options["mapUrl"]
        self.wordpress_components = WordpressComponent(driver)


    def buildLayout(self):
        self.wordpress_components.HEADER_PRINCIPAL_DE_PAGINAS()
        self.wordpress_components.IMAGEN_PARRAFO()
        self.wordpress_components.AREA_DE_SERVICIOS()
        self.wordpress_components.LLAMADO_DE_ACCION_1()
        self.wordpress_components.PARRAFO_BENEFICIOS()
        self.wordpress_components.GALERIA_VIDEOS()
        self.wordpress_components.LLAMADO_DE_ACCION_2()
        self.wordpress_components.PARRAFO_CIUDAD_MAPA_NO_GEO()
        self.wordpress_components.RECURSOS()
        self.wordpress_components.PARRAFO_CONCLUSION()
        self.wordpress_components.ZIP_CODE_SIN_GEO()
        self.wordpress_components.GEOLOCALIZACION()


