import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.set_window_size(1280, 720)

    def test_chrome(self):
        self.driver.get("https://www.pys.com/customer/account/login")
        self.driver.find_element(By.XPATH, "//input[@type= 'email']").send_keys('toninka@inbox.ru')
        self.driver.find_element(By.XPATH, "//input[@type= 'password']").send_keys('Plushka123')
        self.driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
