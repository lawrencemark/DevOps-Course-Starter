
import os,sys,inspect, pytest 
from datetime import datetime
sys.path.append('/srv/www/')
import utils.classfunct 

#import selenim and configuration for docker image :selenium/standalone-chrome
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # example
driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)


class TestClass():
    def setup_class(self):
        pass

    def teardown_class(self):
        pass


    def setup_method(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")

    def teardown_method(self):
        pass # we will add some fancy webhooks and emails here passed on the status of the tests later
    
    def test_enedtoendCapture(self):

    # Test end-to-end application and screenshot output
        driver.get('http://app-dev:5000')
        filename = (f'capture{self.current_time}.png')
        screenshot = driver.save_screenshot(filename)
        driver.quit()

