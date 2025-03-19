import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


class ProductListPage():
    URL = "https://mall.ejeju.net/goods/main.do?cate=1"
    MESSAGE_BOARD_CLASSNAME = "//tr[@class='bg'][1]/td[@class='title']/strong/a"
    PRODUCT_IMAGE_SELECTOR = ".thum"
   
    def __init__(self, driver: WebDriver):
        self.driver = driver

    
    def open(self):
        self.driver.get(self.URL)

    def image_hover_icons(self):
        product_image = self.driver.find_element(By.CSS_SELECTOR, self.PRODUCT_IMAGE_SELECTOR)
        
        actions = ActionChains(self.driver)
        actions.move_to_element(product_image).perform()