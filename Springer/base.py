from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestSearchBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://link.springer.com/")

        assert 'Home - Springer' in driver.title

    def testSearchHappyPath(self):
        driver = self.driver

        search_field = driver.find_element(By.NAME, 'query')
        search_field.send_keys('foo')
        search_field.submit()

        results_list = driver.find_elements_by_xpath(
            "//ol[@id='results-list']/li[@class='no-access']")
        assert len(results_list) > 0

    def testSearchUnhappyPath(self):
        driver = self.driver

        search_field = driver.find_element(By.NAME, 'query')
        search_field.send_keys('qwertyasdfg')
        search_field.submit()

        no_results_msg = driver.find_elements_by_xpath(
            ".//*[@id='no-results-message']")

        assert no_results_msg

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
