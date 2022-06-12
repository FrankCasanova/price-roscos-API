import requests as _req
from bs4 import BeautifulSoup as _bs
from selenium import webdriver as _webdriver

headers = {"User-Agent": "Mozilla/5.0"}

# taking the url from the different stores

DIA_URL = _req.get(
    "https://www.dia.es/compra-online/despensa/pan/picos-de-pan/p/59304",
    headers=headers,
)
JAMON_URL = _req.get(
    "https://www.supermercadoseljamon.com/detalle/-/Producto/picos-finos-integrales-250g/23025302",
    headers=headers,
)
CARREFOUR_URL = _req.get(
    "https://www.carrefour.es/supermercado/colines-integrales-carrefour-250-g/R-prod970952/p",
    headers=headers,
)


def scraping_el_jamon():
    webdriver = _webdriver.Firefox()
    webdriver.get(
        "https://www.supermercadoseljamon.com/detalle/-/Producto/picos-finos-integrales-250g/23025302"
    )
    webdriver.implicitly_wait(5)
    webdriver.find_element("id", "aceptar").click()
    webdriver.find_element(
        "xpath", '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]'
    ).click()
    webdriver.find_element("xpath", '//*[@id="button"]').click()
    webdriver.find_element("xpath", '//*[@id="seleccionarCp"]').send_keys("21004")
    webdriver.find_element("xpath", '//*[@id="aceptarPorCp"]').click()
    title = webdriver.find_element(
        "xpath", "/html/body/div[4]/div[2]/div[2]/div[2]/div/div/div/div/div/form/h1"
    ).__getattribute__("text")
    price = webdriver.find_element(
        "xpath",
        "/html/body/div[4]/div[2]/div[2]/div[2]/div/div/div/div/div/form/div[4]/div/span",
    ).__getattribute__("text")
    price_kg = webdriver.find_element(
        "xpath",
        "/html/body/div[4]/div[2]/div[2]/div[2]/div/div/div/div/div/form/div[4]/div/div",
    ).__getattribute__("text")
    webdriver.quit()

    return print({"title": title, "price": price, "price_kg": price_kg})


def scraping_dia():
    dia_soup = _bs(DIA_URL.content, "html.parser")
    title = dia_soup.find("h1").text
    price = dia_soup.find("span", class_="big-price").text.replace("\xa0", "")
    price_kg = (
        dia_soup.find("span", class_="average-price")
        .text.replace("\r\n\t\t\t\t\t", "")
        .replace("\xa0", "")
    )

    return print({"title": title, "price": price, "price_kg": price_kg})


def scraping_carrefour():
    carrefour_soup = _bs(CARREFOUR_URL.content, "html.parser")
    title = (
        carrefour_soup.find("h1", class_="product-header__name")
        .text.replace("\n", "")
        .strip()
    )
    price = carrefour_soup.find("span", class_="buybox__price").text.strip()
    price_kg = (
        carrefour_soup.find("div", class_="buybox__price-per-unit")
        .text.strip()
        .replace("\n", "")
    )

    return print({"title": title, "price": price, "price_kg": price_kg})


print("-----------------------------------------------")
print("El jamon")
scraping_el_jamon()
print("-----------------------------------------------")
print("Carrefour")
scraping_carrefour()
print("-----------------------------------------------")
print("Dia")
scraping_dia()
