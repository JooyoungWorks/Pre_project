import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.pages.cart_page import Cart_Page
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


@pytest.mark.usefixtures("driver")  # driver를 달아줘야 conftest의 드라이버 여기서 사용 가능
class TestCartPage:

    @pytest.mark.skip
    def test_open_main(self, driver: WebDriver):
        try:
            # 메인 페이지 열기
            main_page = Cart_Page(driver)
            main_page.open_main()

            assert "ejeju.net" in driver.current_url
        except NoSuchElementException as e:
            assert False
    
    @pytest.mark.skip
    def test_hover_product(self, driver: WebDriver):
        try:
            # 메인 페이지 열기
            main_page = Cart_Page(driver)
            main_page.open_main()
            
            # 상품에 마우스 호버
            main_page.scroll_to_product()
            main_page.hover_product()

            
            # 호버 후, 장바구니 추가 버튼 나타나는지 확인
            add_to_cart_btn = ws(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//li[@class='ic_dt m_cart ']//button[@id='cartPop']"))
            )
            
            assert add_to_cart_btn.is_displayed()
        except NoSuchElementException as e:
            assert False
        except TimeoutException as e:
            assert False

    @pytest.mark.skip
    def test_add_to_cart(self, driver: WebDriver):
        try:
            # 메인 페이지 열기
            main_page = Cart_Page(driver)
            main_page.open_main()
            
            # 상품에 마우스 호버
            main_page.scroll_to_product()
            main_page.hover_product()

            # 장바구니에 추가 버튼 클릭
            main_page.add_to_cart()
            
            cart_popup = driver.find_element(By.XPATH, "//div[@class='pop_modal detail_info_prd']")
            assert cart_popup.is_displayed(), "❌ 장바구니 추가 팝업이 나타나지 않습니다!"
        except Exception as e:
            assert False

    def test_confrim_add_to_cart(self, driver: WebDriver):
        try:
            main_page = Cart_Page(driver)
            main_page.open_main()

            main_page.scroll_to_product()
            main_page.hover_product()
            main_page.add_to_cart()
            
            #장바구니 추가 팝업 확인 처리
            main_page.confirm_add_to_cart()

            ws(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='gnb_main']")))

            assert "main" in driver.current_url
        except Exception as e:
            assert False

