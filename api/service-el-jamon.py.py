from selenium import webdriver


webdriver = webdriver.Firefox()
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
print(
    webdriver.find_element(
        "xpath", "/html/body/div[4]/div[2]/div[2]/div[2]/div/div/div/div/div/form/h1"
    ).__getattribute__("text")
)
print(
    webdriver.find_element(
        "xpath",
        "/html/body/div[4]/div[2]/div[2]/div[2]/div/div/div/div/div/form/div[4]/div/span",
    ).__getattribute__("text")
)
print(
    webdriver.find_element(
        "xpath",
        "/html/body/div[4]/div[2]/div[2]/div[2]/div/div/div/div/div/form/div[4]/div/div",
    ).__getattribute__("text")
)
