import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


class Cart_Page:
    MAIN_URL = "https://mall.ejeju.net/main/index.do"
    CART_URL = "https://mall.ejeju.net/order/cart.do"

    # __init__에서 driver를 한 번 받아 Class 내부에서 저장하면,
    # 이후 메서드에서 self.driver로 쉽게 driver 사용 가능
    def __init__(self, driver: WebDriver):
        self.driver = driver
    

    # 이제주몰 메인 페이지 열기
    def open_main(self):
        self.driver.get(self.MAIN_URL)
    

    # 메인 페이지 첫 번째 상품까지 스크롤
    def scroll_to_product(self):
        product = self.driver.find_element(By.XPATH, "//div[@class='images ']//img[@src='https://mall.ejeju.net/data/base/goods/big/banner_03_0_2.jpg']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)


    # 메인 페이지 첫 번째 상품에 마우스 호버
    def hover_product(self):
        # ActionChains로 마우스 호버할 요소를 찾음
        hover_product_xpath = "//div[@class='images ']//img[@src='https://mall.ejeju.net/data/base/goods/big/banner_03_0_2.jpg']"
        hover_product = self.driver.find_element(By.XPATH, hover_product_xpath)

        # 마우스를 해당 요소로 이동시킴
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_product).perform()
    

    # 장바구니에 추가 버튼 클릭
    def add_to_cart(self):
        add_btn = ws(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='ic_dt m_cart ']//button[@id='cartPop']"))
        )
        add_btn.click()


    # 장바구니 추가 팝업 확인 버튼 클릭
    def confirm_add_to_cart(self):
        confirm_btn = ws(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='bd_btn_area center']//a[text()='확인"))
        )
        confirm_btn.click()

    
    # 장바구니로 이동
    def go_to_cart(self):
        cart_view_btn = ws(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='utill']//a[text()='장바구니']"))
        )
        cart_view_btn.click()

    
    # 장바구니 페이지 열기
    def open_cart(self):
        self.driver.get(self.CART_URL)


    # 상품 수량 추가 버튼 클릭
    def click_increase_product_btn(self):
        increase_button = ws(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='up']"))
        )
        increase_button.click()

    
    # 상품 삭제 버튼 클릭
    def click_delete_product_btn(self):
        delete_button = ws(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='삭제']"))
        )
        delete_button.click()


    # 상품 삭제 팝업 확인 버튼 클릭
    def confirm_delete_alert(self):
        try:
            alert = ws(self.driver, 10).until(EC.alert_is_present())
            alert.accept()  # 확인 버튼 클릭
        except Exception as e:
            print(f"❌ Alert 감지되지 않음: {e}")

    