import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class TestClass():
    def setup_class(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)


    def teardown_class(self):
        pass


    def setup_method(self):
        pass

    def teardown_method(self):
        pass # we will add some fancy webhooks and emails here passed on the status of the tests later
    
    def test_enedtoendCapture(self):

        self.driver.get("http://localhost:5000/")
        self.driver.set_window_size(1935, 1332)
        self.driver.find_element(By.ID, "tname").click()
        self.driver.find_element(By.ID, "tname").send_keys("Selenium End to End Test")
        self.driver.find_element(By.ID, "tdesc").click()
        self.driver.find_element(By.ID, "tdesc").send_keys("This is an automated end to end test")
        self.driver.find_element(By.ID, "tstatus").click()
        dropdown = self.driver.find_element(By.ID, "tstatus")
        dropdown.find_element(By.XPATH, "//option[. = 'Completed']").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(13)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(13)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(13)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(13)").click()
        self.driver.close()