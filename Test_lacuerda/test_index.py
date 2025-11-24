from playwright.sync_api import Page, expect
import pytest
from playwright.sync_api import Browser, Page, sync_playwright

import os

def test_title(browser_page):
    browser_page.goto("https://www.lacuerda.net/")
    

############# LOGO ################    
    
    logo = browser_page.locator("img[src*='lacuerda-big']")
    expect(logo).to_be_visible()
    #browser_page.wait_for_timeout(2000)
    browser_page.locator("text =Tablaturas y Acordes en Español")
    assert browser_page.title() == "Letras y Acordes de Guitarra, Piano y Ukulele"
    
    
############# HEADER ################ 

def test_header(browser_page):

    browser_page.goto("https://www.lacuerda.net/")

    # Localizar todos los enlaces dentro del header
    header_links = browser_page.locator("#mTopCont a")
    total = header_links.count()
    print("\nTotal de opciones en el header:", total)

    for i in range(total):

        # 👇 Re-seleccionar los links en cada vuelta porque la página cambia
        header_links = browser_page.locator("#mTopCont a")

        link = header_links.nth(i)
        text = link.inner_text()
        print(f"Opción #{i+1}: {text}")

        # Clic en el enlace
        link.click()

        # Espera a que cargue
        browser_page.wait_for_load_state("domcontentloaded")

        # Volver al home
        browser_page.goto("https://www.lacuerda.net/")
        browser_page.wait_for_load_state("domcontentloaded")

############# SIGN IN ################

def test_signin(browser_page): 
    browser_page.locator("#mReg").click()
    browser_page.locator("input[name='apodo']").fill("RandomUser")
    browser_page.wait_for_timeout(5000)
    browser_page.locator("#registro > div > div:nth-child(4) > input").fill("correo@test.com")
    browser_page.wait_for_timeout(5000)
    browser_page.locator("input[name='usr_clave']").fill("12345ABCd")
    browser_page.wait_for_timeout(3000)
    browser_page.locator("input[name='usr_clave2']").fill("12345ABCd")
    browser_page.wait_for_timeout(3000)
    browser_page.locator("input[name='acepto']").click()  
    browser_page.wait_for_timeout(5000)
    browser_page.locator(".btnmain").click()
    browser_page.wait_for_timeout(5000)
    browser_page.locator("text =¡Estás a un paso de completar tu inscripción!")
    
    # Volver al home
    browser_page.goto("https://www.lacuerda.net/")
    browser_page.wait_for_load_state("domcontentloaded")
      
############# SEARCHING BAR TESTING AND COUNT THE SONG################ 
def test_searcher(browser_page):
    browser_page.locator("//*[@id='sExp']").click()
    browser_page.wait_for_timeout(5000)
    browser_page.locator("//*[@id='sExp']").fill("Jose Jose" )
    browser_page.wait_for_timeout(5000)
    browser_page.locator("//*[@id='sExp']").clear()
    browser_page.wait_for_timeout(5000)
    browser_page.locator("//*[@id='sExp']").fill("Luis Miguel" )
    browser_page.wait_for_timeout(5000) 
    browser_page.get_by_text("Buscar").click()      
    browser_page.wait_for_timeout(5000)     

### Run with: pytest --headed

