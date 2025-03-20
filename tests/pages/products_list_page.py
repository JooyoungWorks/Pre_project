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
    DETAIL_ICON_XPATH = "//*[@id='viewType']/li[1]/div/ul/li[1]/button"
    BLANK_ICON_SELECTOR = ".ic_dt.m_blank button"
    CART_ICON_SELECTOR = ".ic_dt.m_cart.active"
    WISH_ICON_SELECTOR = ".ic_dt.m_wish"
   
    def __init__(self, driver: WebDriver):
        self.driver = driver

    
    def open(self):
        self.driver.get(self.URL)


    def image_hover_icons(self):
        product_image = ws(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.PRODUCT_IMAGE_SELECTOR)))

        self.driver.execute_script("arguments[0].scrollIntoView();", product_image)
        
        actions = ActionChains(self.driver)
        actions.move_to_element(product_image).perform()


    def detail_icon_click(self):
        detail_icon_button = self.driver.find_element(By.XPATH, self.DETAIL_ICON_XPATH)
        detail_icon_button.click()


    def blank_icon_click(self):
        blank_icon_button = self.driver.find_element(By.CSS_SELECTOR, self.BLANK_ICON_SELECTOR)
        blank_icon_button.click()


    def cart_icon_click(self):
        cart_icon_button = self.driver.find_element(By.CSS_SELECTOR, self.CART_ICON_SELECTOR)
        cart_icon_button.click()


    def wish_icon_click(self):
        wish_icon_button = self.driver.find_element(By.CSS_SELECTOR, self.WISH_ICON_SELECTOR)
        wish_icon_button.click()