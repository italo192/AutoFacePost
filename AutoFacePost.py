# bot de postagem no facebook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR','--window-size= 800,600','--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
        
    chrome_options.add_experimental_option('prefs', {
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    #inicializando o webdriver
    driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    return driver
# navegar ate um site
driver = iniciar_driver()
driver.get('https://www.facebook.com')
sleep(30)

email = driver.find_element(By.XPATH,'//input[@id="email"]')
email.click()
sleep(2)
email.send_keys('martinhoitalo@hotmail.com')
sleep(3)
senha = driver.find_element(By.XPATH,'//input[@id="pass"]')
senha.click()
sleep(2)
senha.send_keys('28112001')
sleep(3)
entrar = driver.find_element(By.XPATH,'//button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]')
entrar.click()
sleep(10)
driver.execute_script("window.scrollTo(0, 500);")
sleep(2)
para_escrever = driver.find_element(By.XPATH,'//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]')
para_escrever.click()
sleep(10)
digitar = driver.find_element(By.XPATH,'//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
digitar.send_keys('boa tarde')
sleep(2)
publicar = driver.find_element(By.XPATH,'//div[@class="x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67"]')
publicar.click()
sleep(30)

input('')
