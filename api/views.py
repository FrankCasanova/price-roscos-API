from .sercvices import scraping_carrefour
from .sercvices import scraping_dia
from .sercvices import scraping_el_jamon
from .sercvices import scraping_mas


def index():
    return {
        "welcome": "Welcome to the API",
        "instructions": "Use the following endpoints: /prices",
    }


def get_prices():
    el_jamon = scraping_el_jamon()
    dia = scraping_dia()
    carrefour = scraping_carrefour()
    mas = scraping_mas()

    return {"el_jamon": el_jamon, "dia": dia, "carrefour": carrefour, "mas": mas}
