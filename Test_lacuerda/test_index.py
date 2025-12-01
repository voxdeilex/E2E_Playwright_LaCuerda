from playwright.sync_api import Page, expect
import pytest
import allure

############# TITLE & LOGO ################    
@allure.feature("Página principal")
@allure.story("Validar título y logo")
def test_title(browser_page):
    with allure.step("Navegar a lacuerda.net"):
        browser_page.goto("https://www.lacuerda.net/")

    with allure.step("Validar que el logo sea visible"):
        logo = browser_page.locator("img[src*='lacuerda-big']")
        expect(logo).to_be_visible()

    with allure.step("Validar título de la página"):
        assert browser_page.title() == "Letras y Acordes de Guitarra, Piano y Ukulele"

    # Captura de pantalla
    allure.attach(
        browser_page.screenshot(),
        name="Pantalla principal",
        attachment_type=allure.attachment_type.PNG
    )

############# HEADER ################ 
@allure.feature("Header")
@allure.story("Validar enlaces del header")
def test_header(browser_page):

    browser_page.goto("https://www.lacuerda.net/")

    header_links = browser_page.locator("#mTopCont a")
    total = header_links.count()

    allure.attach(str(total), "Total de enlaces en el header")

    for i in range(total):

        header_links = browser_page.locator("#mTopCont a")
        link = header_links.nth(i)
        text = link.inner_text()

        with allure.step(f"Clic en enlace #{i+1}: {text}"):
            link.click()
            browser_page.wait_for_load_state("domcontentloaded")

            # Screenshot
            allure.attach(
                browser_page.screenshot(),
                name=f"Enlace {i+1} - {text}",
                attachment_type=allure.attachment_type.PNG
            )

        browser_page.goto("https://www.lacuerda.net/")
        browser_page.wait_for_load_state("domcontentloaded")

############# SEARCHING BAR ################ 
@allure.feature("Buscador")
@allure.story("Validar funcionamiento de barra de búsqueda")
def test_searcher(browser_page):

    with allure.step("Hacer clic en la barra de búsqueda"):
        browser_page.locator("//*[@id='sExp']").click()

    with allure.step("Buscar 'Jose Jose'"):
        browser_page.locator("//*[@id='sExp']").fill("Jose Jose")

    with allure.step("Buscar 'Luis Miguel'"):
        browser_page.locator("//*[@id='sExp']").clear()
        browser_page.locator("//*[@id='sExp']").fill("Luis Miguel")

    with allure.step("Clic en botón Buscar"):
        browser_page.get_by_text("Buscar").click()

    # Captura de pantalla final
    allure.attach(
        browser_page.screenshot(),
        name="Resultado de búsqueda",
        attachment_type=allure.attachment_type.PNG
    )


#RUN WITH: pytest --alluredir=allure-results ; allure serve allure-results
