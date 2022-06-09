import requests as _req
from bs4 import BeautifulSoup as _bs

# taking the url from the different stores

DIA_URL = _req.get("https://www.dia.es/compra-online/despensa/pan/picos-de-pan/p/59304")
JAMON_URL = _req.get(
    "https://www.supermercadoseljamon.com/detalle/-/Producto/picos-finos-integrales-250g/23025302"
)
CARREFOUR_URL = _req.get(
    "https://www.carrefour.es/supermercado/colines-integrales-carrefour-250-g/R-prod970952/p"
)
