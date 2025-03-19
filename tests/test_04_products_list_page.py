import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from tests.pages.products_list_page import ProductListPage


@pytest.mark.usefixtures("driver")
class TestProductsListPage:

    @pytest.mark.skip(reason="테스트 성공해서 계속 할 필요 없음")
    def test_open_products_list_page(self, driver: WebDriver):
        try:
            products_list_page = ProductListPage(driver)
            products_list_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("goods"))
            assert "goods" in driver.current_url
            driver.save_screenshot("상품리스트페이지-오픈-성공.png")

        
        except NoSuchElementException as e:
            assert False

    
    def test_image_mouse_hover(self, driver: WebDriver):
        try:
            ICON_CONTAINER_SELECTOR = ".info_icon"
            CART_ICON_SELECTOR = ".ic_dt.m_cart.active"

            products_list_page = ProductListPage(driver)
            products_list_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("goods"))
            assert "goods" in driver.current_url

            time.sleep(3)

            products_list_page.image_hover_icons()

            time.sleep(7)

            # 아이콘 컨테이너 표시 여부 검증
            icon_container = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ICON_CONTAINER_SELECTOR)))
        
            assert icon_container.is_displayed()
            driver.save_screenshot("상품리스트페이지-마우스호버-아이콘-성공.png")

            time.sleep(3)

            # 장바구니 아이콘 표시 여부 검증
            cart_icon = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CART_ICON_SELECTOR)))
            assert cart_icon.is_displayed()
            driver.save_screenshot("상품리스트페이지-마우스호버-장바구니 아이콘-성공.png")


        except NoSuchElementException as e:
            driver.save_screenshot("상품리스트페이지-마우스호버-상세보기-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("상품리스트페이지-마우스호버-상세보기-실패-타임에러.png")
            assert False