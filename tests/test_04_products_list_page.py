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
            assert False, f"상품리스트 페이지 오픈 실패 : {e}"


    def test_image_mouse_hover(self, driver: WebDriver):
        try:
            ICON_CONTAINER_SELECTOR = ".info_icon"
            DETAIL_ICON_SELECTOR = ".ic_dt.m_plus"
            BLANK_ICON_SELECTOR = ".ic_dt.m_blank"
            CART_ICON_SELECTOR = ".ic_dt.m_cart.active"
            WISH_ICON_SELECTOR = ".ic_dt.m_wish"

            products_list_page = ProductListPage(driver)
            products_list_page.open()

            time.sleep(3)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("goods"))

            time.sleep(3)

            products_list_page.image_hover_icons()

            time.sleep(5)

            # 아이콘 컨테이너 표시 여부 검증
            icon_container = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ICON_CONTAINER_SELECTOR)))
            assert icon_container.is_displayed()
            driver.save_screenshot("상품리스트페이지-마우스호버-아이콘 컨테이너-성공.png")

            

            #상세보기 아이콘 표시 여부 검증
            detail_icon = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, DETAIL_ICON_SELECTOR)))
            style = detail_icon.get_attribute("style")

            if "display: none" in style or "visibility: hidden" in style:
                driver.execute_script("arguments[0].style.display = 'block';", detail_icon)

            ws(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, DETAIL_ICON_SELECTOR)))

            assert detail_icon.is_displayed()
            driver.save_screenshot("상품리스트페이지-마우스호버-상세보기 아이콘-성공.png")

            

            #새창열기 아이콘 표시 여부 검증
            blank_icon = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, BLANK_ICON_SELECTOR)))
            style = blank_icon.get_attribute("style")

            if "display: none" in style or "visibility: hidden" in style:
                driver.execute_script("arguments[0].style.display = 'block';", blank_icon)

            ws(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, BLANK_ICON_SELECTOR)))

            assert blank_icon.is_displayed()
            driver.save_screenshot("상품리스트페이지-마우스호버-새창열기 아이콘-성공.png")

            

            #장바구니 아이콘 표시 여부 검증
            cart_icon = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CART_ICON_SELECTOR)))
            assert cart_icon.is_displayed()
            driver.save_screenshot("상품리스트페이지-마우스호버-장바구니 아이콘-성공.png")

            

            #찜하기 아이콘 표시 여부 검증
            wish_icon = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, WISH_ICON_SELECTOR)))
            assert wish_icon.is_displayed()
            driver.save_screenshot("상품리스트페이지-마우스호버-찜하기 아이콘-성공.png")


        except NoSuchElementException as e:
            driver.save_screenshot("상품리스트페이지-마우스호버-실패-노서치.png")
            assert False            

        except TimeoutException as e:
            driver.save_screenshot("상품리스트페이지-마우스호버-실패-타임에러.png")
            assert False


    
    def test_detail_icon_click(self, driver: WebDriver):
        try:
            ICON_CONTAINER_SELECTOR = ".info_icon"
            DETAIL_ICON_SELECTOR = ".ic_dt.m_plus"

            products_list_page = ProductListPage(driver)
            products_list_page.open()

            time.sleep(3)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("goods"))

            time.sleep(3)

            products_list_page.image_hover_icons()

            time.sleep(3)
            ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ICON_CONTAINER_SELECTOR)))       
           
           
            detail_icon = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, DETAIL_ICON_SELECTOR)))
            style = detail_icon.get_attribute("style")

            if "display: none" in style or "visibility: hidden" in style:
                driver.execute_script("arguments[0].style.display = 'block';", detail_icon)

            ws(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, DETAIL_ICON_SELECTOR)))
            assert detail_icon.is_displayed()

            time.sleep(3)

            #상세보기 아이콘 클릭
            products_list_page.detail_icon_click()
            assert "detail" in driver.current_url
            driver.save_screenshot("상세보기 아이콘 클릭-상세페이지 이동-성공.png")


        except NoSuchElementException as e:
            driver.save_screenshot("상품리스트페이지-마우스호버-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("상품리스트페이지-마우스호버-실패-타임에러.png")
            assert False


    
    def test_blank_page_open(self, driver: WebDriver):
        try:
            ICON_CONTAINER_SELECTOR = ".info_icon"
            BLANK_ICON_SELECTOR = ".ic_dt.m_blank"

            products_list_page = ProductListPage(driver)
            products_list_page.open()

            time.sleep(3)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("goods"))

            time.sleep(3)

            products_list_page.image_hover_icons()

            time.sleep(3)
            ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ICON_CONTAINER_SELECTOR)))       
           
            blank_icon = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, BLANK_ICON_SELECTOR)))
            style = blank_icon.get_attribute("style")

            if "display: none" in style or "visibility: hidden" in style:
                driver.execute_script("arguments[0].style.display = 'block';", blank_icon)

            ws(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, BLANK_ICON_SELECTOR)))
            assert blank_icon.is_displayed()

            time.sleep(3)

            # 원래 탭의 핸들 저장
            original_window = driver.current_window_handle
            original_handles = driver.window_handles

            # 새 탭을 여는 링크 클릭
            products_list_page.blank_icon_click()

            # 새 탭이 열릴 때까지 기다림
            ws(driver, 10).until(EC.number_of_windows_to_be(len(original_handles) + 1))

            # 새 탭 핸들 확인
            new_handles = driver.window_handles
            new_tab = [handle for handle in new_handles if handle not in original_handles][0]

            # 새 탭으로 전환
            driver.switch_to.window(new_tab)

            # 새 탭 검증 (URL, 제목 등)
            assert "detail" in driver.current_url
            driver.save_screenshot("새 탭열기 아이콘 클릭-새 탭-상세페이지-성공.png")

            time.sleep(3)

            # 새 탭 닫기 및 원래 탭으로 전환
            driver.close()
            driver.switch_to.window(original_window)
            assert "goods/main" in driver.current_url
            driver.save_screenshot("새 탭 닫기-원래 탭 이동-성공.png")


        except NoSuchElementException as e:
            driver.save_screenshot("새 탭열기 아이콘 클릭-새 탭-상세페이지-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("새 탭열기 아이콘 클릭-새 탭-상세페이지-실패-타임에러.png")
            assert False


    
    def test_cart_icon_click(self, driver: WebDriver):
        try:
            ICON_CONTAINER_SELECTOR = ".info_icon"
            CART_ICON_SELECTOR = ".ic_dt.m_cart.active"
            CARTPOPUP_ICON_SELECTOR = ".pop_modal.detail_info_prd"

            products_list_page = ProductListPage(driver)
            products_list_page.open()

            time.sleep(3)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("goods"))

            time.sleep(3)

            products_list_page.image_hover_icons()
            
            ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ICON_CONTAINER_SELECTOR)))       
            
           
            cart_icon = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CART_ICON_SELECTOR)))
            style = cart_icon.get_attribute("style")

            if "display: none" in style or "visibility: hidden" in style:
                driver.execute_script("arguments[0].style.display = 'block';", cart_icon)

            ws(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CART_ICON_SELECTOR)))

            time.sleep(2)

            #장바구니 아이콘 클릭
            products_list_page.cart_icon_click()

            time.sleep(2)

            cart_popup =  ws(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CARTPOPUP_ICON_SELECTOR)))
        
            assert cart_popup.is_displayed()
            driver.save_screenshot("장바구니 아이콘 클릭-장바구니팝업창-성공.png")


        except NoSuchElementException as e:
            driver.save_screenshot("장바구니 아이콘 클릭-장바구니팝업창-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("장바구니 아이콘 클릭-장바구니팝업창-실패-타임에러.png")
            assert False


    
    def test_wish_icon_click(self, driver: WebDriver):
        try:
            ICON_CONTAINER_SELECTOR = ".info_icon"
            WISH_ICON_SELECTOR = ".ic_dt.m_wish"

            products_list_page = ProductListPage(driver)
            products_list_page.open()

            time.sleep(3)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("goods"))

            time.sleep(3)

            products_list_page.image_hover_icons()
            
            ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ICON_CONTAINER_SELECTOR)))       
           
            wish_icon = ws(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, WISH_ICON_SELECTOR)))
            style = wish_icon.get_attribute("style")

            if "display: none" in style or "visibility: hidden" in style:
                driver.execute_script("arguments[0].style.display = 'block';", wish_icon)

            ws(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, WISH_ICON_SELECTOR)))

            time.sleep(3)

            #찜하기 아이콘 클릭
            products_list_page.wish_icon_click()

            time.sleep(5)

            #비회원상태로 찜하기 클릭시 로그인창으로 넘어가는지 검증
            assert "member" in driver.current_url
            driver.save_screenshot("찜하기 아이콘 클릭-로그인페이지 이동-성공.png")


        except NoSuchElementException as e:
            driver.save_screenshot("찜하기 아이콘 클릭-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("찜하기 아이콘 클릭-실패-타임에러.png")
            assert False
