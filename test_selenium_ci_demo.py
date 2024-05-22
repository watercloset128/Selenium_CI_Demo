import time
import pytest

from selenium import webdriver
from selenium.webdriver.edge.service import Service as edgeservice
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.edge.options import Options as edgeoptions
from selenium.webdriver.chrome.options import Options as chromeoptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Test_Selenium_CI:
    
    def test_getpython_homepage_title_edge(self, request):

        seleniumhub_ip = request.config.getoption('--seleniumhub')

        options = edgeoptions()
        options.add_argument('-headless')
        options.add_argument('--guest')
        
        if seleniumhub_ip == None:
            driver = webdriver.Edge(service=edgeservice(EdgeChromiumDriverManager().install()), options=options)
        else:
            driver = webdriver.Remote(seleniumhub_ip, options=options)
        
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get('https://www.python.org')
        assert 'Python' in driver.title

        time.sleep(10)

        driver.quit()

    def test_getpython_homepage_title_chrome(self, request):

        seleniumhub_ip = request.config.getoption('--seleniumhub')

        options = chromeoptions()
        options.add_argument('-headless')
        options.add_argument('--guest')
        
        if seleniumhub_ip == None:
            pytest.skip('WebDriver_Manager issue leads to not being able to load webdriver locally')
            # driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()), options=options)
        else:
            driver = webdriver.Remote(seleniumhub_ip, options=options)
        
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get('https://www.python.org')
        assert 'Python' in driver.title

        time.sleep(10)

        driver.quit()