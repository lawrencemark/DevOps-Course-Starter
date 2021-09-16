import pytest 
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAddTask():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('/usr/local/bin/chromedriver') 
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addTask(self):
    self.driver.get("http://localhost:5000/")
    self.driver.set_window_size(1440, 838)
    self.driver.find_element(By.NAME, "addTo").click()
    self.driver.find_element(By.NAME, "addTo").send_keys("Selenium Test Task")
    self.driver.find_element(By.NAME, "description").send_keys("This is a task to be put in a WIP state")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
  