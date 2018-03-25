import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.log import logger
from utils.config import Config, CHROME_DRIVER, DATA_PATH
from utils.file_reader import JsonReader


class TestBaidu(unittest.TestCase):
    URL = Config().get('URL')
    json_data = DATA_PATH + "/test_data.json"

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        datas = JsonReader(self.json_data).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search_content'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    unittest.main()
