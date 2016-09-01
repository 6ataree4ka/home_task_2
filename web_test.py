import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_google_engine(self):
        driver = self.driver
        driver.get('https://www.google.com')
        self.assertIn('Google', driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys('Selenium')
        elem.send_keys(Keys.RETURN)
        assert 'Not results found.' not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
