import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestMe(unittest.TestCase):

    def test_example(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.set_window_size(1024, 768)

        driver.get("https://www.google.com/")

        driver.close()


if __name__ == "__main__":
    unittest.main()