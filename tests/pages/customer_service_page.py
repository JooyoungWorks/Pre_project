import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class CustomerServicePage():
    URL = "https://mall.ejeju.net/board/list.do?board=notice"
    MESSAGE_BOARD_CLASSNAME = "//tr[@class='bg'][1]/td[@class='title']/strong/a"

   
    def __init__(self, driver: WebDriver):
        self.driver = driver

    
    def open(self):
        self.driver.get(self.URL)

    def message_board(self):
        first_post = self.driver.find_element(By.XPATH, self.MESSAGE_BOARD_CLASSNAME)
        first_post.click()