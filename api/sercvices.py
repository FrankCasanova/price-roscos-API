import os

import requests as _req
from bs4 import BeautifulSoup as _bs
from selenium import webdriver as _webdriver
from selenium.webdriver.common.keys import Keys as _Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

headers = {"User-Agent": "Mozilla/5.0"}
headers_chrome = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
}

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

MAS_URL = _req.get(
    "https://www.supermercadosmas.com/panaderia-bolleria-pasteleria/colines-integrales-mas-250g",
    headers=headers,
)


def scraping_el_jamon():
    """
    Function to scrape the El Jamon website
    this function returns a dictionary with the title, price and price_kg
    it use selenium to open the browser and scrape the website
    instructions in:
    https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/
    """
    options = _webdriver.FirefoxOptions()
    # options.log.level = "trace"
    # options.add_argument("-remote-debugging-port=9224")
    options.add_argument("-headless")
    options.add_argument("-disable-gpu")
    options.add_argument("-no-sandbox")

    binary = FirefoxBinary(os.environ.get("FIREFOX_BIN"))

    webdriver = _webdriver.Firefox(
        options=options,
        firefox_binary=binary,
        executable_path=os.environ.get("GECKODRIVER_PATH"),
    )
    # chrome_options = _webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")

    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    # webdriver = _webdriver.Chrome(options=chrome_options)

    webdriver.get(
        "https://www.supermercadoseljamon.com/detalle/-/Producto/picos-finos-integrales-250g/23025302"
    )

    # webdriver.add_cookie({'c': '694a67a7-4cda-4642-b539-60d58e5be025'})
    webdriver.implicitly_wait(2)
    # webdriver.find_element("id", "aceptar").click()

    webdriver.find_element(
        "xpath", '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]'
    ).click()

    webdriver.find_element("xpath", '//*[@id="button"]').click()
    webdriver.find_element("xpath", '//*[@id="seleccionarCp"]').send_keys("21004")
    webdriver.find_element("xpath", '//*[@id="seleccionarCp"]').send_keys(_Keys.ENTER)
    webdriver.find_element("xpath", '//*[@id="seleccionarCp"]').send_keys(_Keys.ENTER)
    # webdriver.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/div/div/fieldset/div[3]/div[2]/input[3]').click()
    # select = _select(webdriver.find_element("xpath", '//*[@id="_SeleccionarCodPostalFoodPortlet_WAR_comerzziaportletsfood_tiendaRecogida_1020"]'))
    # select.select_by_visible_text("Huelva, Huelva 130 - Artesanos, 12 (21005)").click()

    # webdriver.execute_script("window.scrollTo(0, 1300);")

    # webdriver.find_element("id", "aceptarPorCp").click()
    # webdriver.find_element("xpath", '//*[@id="aceptarPorCp"]').click()
    # webdriver.find_element("xpath", '//*[@id="aceptarPorCp"]').send_keys(_Keys.ENTER)

    # webdriver.implicitly_wait(10)

    title = webdriver.find_element(
        "xpath",
        '//*[@id="_DetalleProductoFoodPortlet_WAR_comerzziaportletsfood_frmDatos"]/h1',
    ).__getattribute__("text")
    webdriver.get_screenshot_as_file("screenshot.png")
    price = webdriver.find_element(
        "xpath",
        '//*[@id="_DetalleProductoFoodPortlet_WAR_comerzziaportletsfood_frmDatos"]/div[4]/div/span',
    ).__getattribute__("text")
    price_kg = webdriver.find_element(
        "xpath",
        '//*[@id="_DetalleProductoFoodPortlet_WAR_comerzziaportletsfood_frmDatos"]/div[4]/div/div',
    ).__getattribute__("text")
    webdriver.quit()

    return {"title": title, "price": price, "price_kg": price_kg}


def scraping_dia():
    """
    function to scrape the DIA website
    returns a dictionary with the title, price and price_kg
    """
    dia_soup = _bs(DIA_URL.content, "html.parser")
    title = dia_soup.find("h1").text
    price = dia_soup.find("span", class_="big-price").text.replace("\xa0", "")
    price_kg = (
        dia_soup.find("span", class_="average-price")
        .text.replace("\r\n\t\t\t\t\t", "")
        .replace("\xa0", "")
    )

    return {"title": title, "price": price, "price_kg": price_kg}


def scraping_carrefour():
    """
    function to scrape the Carrefour website
    returns a dictionary with the title, price and price_kg
    """
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

    return {"title": title, "price": price, "price_kg": price_kg}


def scraping_mas():
    """
    function to scrape the Mas website
    returns a dictionary with the title, price and price_kg
    """
    mas_soup = _bs(MAS_URL.content, "html.parser")
    title = mas_soup.find("span", class_="base").text
    price = mas_soup.find("span", class_="price").text.replace("\xa0", "")
    price_kg = mas_soup.find("span", class_="unit").text

    return {"title": title, "price": price, "price_kg": price_kg}
