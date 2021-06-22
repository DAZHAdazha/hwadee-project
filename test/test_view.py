# Generated by Selenium IDE
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

class TestView():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_view(self):
    self.driver.get("http://localhost/")
    self.driver.set_window_size(1936, 1056)
    self.driver.execute_script("window.scrollTo(0,69)")
    self.driver.find_element(By.ID, "echarts_trend").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#echarts_trend canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "#echarts_trend canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "#echarts_trend canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "#echarts_trend canvas").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > .boxall:nth-child(2)").click()
    self.driver.execute_script("window.scrollTo(0,326)")
    self.driver.find_element(By.CSS_SELECTOR, "#echarts_ticketOffice canvas").click()
  