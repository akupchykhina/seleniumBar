import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_ie(self):
        self.driver.get("https://www.pys.com/customer/account/login")
        self.driver.find_element(By.XPATH, "//input[@type= 'email']").send_keys('toninka@inbox.ru')
        self.driver.find_element(By.XPATH, "//input[@type= 'password']").send_keys('Plushka123')
        self.driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()