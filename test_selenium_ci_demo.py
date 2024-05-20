import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as edgeservice
from selenium.webdriver.edge.options import Options as edgeoptions
from selenium.webdriver.chrome.options import Options as chromeoptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Test_Selenium_CI:
    
    def test_getpython_homepage_title_edge(self):

        options = edgeoptions()
        options.add_argument('-headless')
        options.add_argument('--guest')
        
        # driver = webdriver.Edge(service=edgeservice(EdgeChromiumDriverManager().install()), options=options)

        driver = webdriver.Remote('192.168.1.171:4444', options=options)
        
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get('https://www.python.org')
        assert 'Python' in driver.title

        time.sleep(10)

        driver.quit()

    def test_getpython_homepage_title_chrome(self):

        options = chromeoptions()
        options.add_argument('-headless')
        options.add_argument('--guest')
        
        # driver = webdriver.Edge(service=edgeservice(EdgeChromiumDriverManager().install()), options=options)

        driver = webdriver.Remote('192.168.1.171:4444', options=options)
        
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get('https://www.python.org')
        assert 'Python' in driver.title

        time.sleep(10)

        driver.quit()