import unittest
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time


class RikBot(unittest.TestCase):
    """Parses relevant information from a text file consisting of
    RIK links."""
    def setUp(self):
        """Setup bot for Rik URL."""
        self.rik_url = "https://www.rik.ee/"

        self.options = Options()
        self.driver = webdriver.Chrome(r"C:\browserdriver\chromedriver.exe")
        self.driver.get(self.rik_url)



    def test_ariregister_opens(self):
        value = "e-äriregister"
        print("klikin lingil "+value)
        self.driver.get(self.rik_url)
        link = self.driver.find_element_by_xpath(u'//a[text()="' + value + '"]')
        link.click()
        time.sleep(3)
        site_result = self.driver.find_element_by_class_name('node-title').text
        print('site_result='+site_result)
        assert value in site_result

    def test_euroopa_ariregister_opens(self):
        value = 'Euroopa äriregister'
        print("klikin lingil "+value)
        self.driver.get(self.rik_url)
        link = self.driver.find_element_by_xpath(u'//a[text()="' + value + '"]')
        link.click()
        time.sleep(3)
        site_result = self.driver.find_element_by_class_name('node-title').text
        print('site_result='+site_result)
        assert value in site_result

    def test_ettevotjaportaal_opens(self):
        value = 'Ettevõtjaportaal'
        print("klikin lingil "+value)
        self.driver.get(self.rik_url)
        link = self.driver.find_element_by_xpath(u'//a[text()="' + value + '"]')
        link.click()
        time.sleep(3)
        site_result = self.driver.find_element_by_class_name('node-title').text
        print('site_result='+site_result)
        assert value in site_result

    def test_kinnistuportaal_opens(self):
        value = 'Kinnistuportaal'
        print("klikin lingil "+value)
        self.driver.get(self.rik_url)
        link = self.driver.find_element_by_xpath(u'//a[text()="' + value + '"]')
        link.click()
        time.sleep(3)
        site_result = self.driver.find_element_by_class_name('node-title').text
        print('site_result='+site_result)
        assert value in site_result


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
