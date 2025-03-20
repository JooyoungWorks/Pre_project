import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC


class GNB_Page:
    MAIN_URL = "https://mall.ejeju.net/main/index.do"
    GNB_XPATH = "//ul[@class='gnb_main']"
    EXHIBITION_XPATH = "//ul[@class='gnb_main']//li[@class='top_menu']//a[contains(text(), '축산물 기획전')]"
    EXHIBITION_URL = "https://mall.ejeju.net/goods/main.do?cate=31160"


    # __init__에서 driver를 한 번 받아 Class 내부에서 저장하면,
    # 이후 메서드에서 self.driver로 쉽게 driver 사용 가능
    def __init__(self, driver: WebDriver):
        self.driver = driver
    

    # 이제주몰 메인 페이지 열기
    def open_main(self):
        self.driver.get(self.MAIN_URL)


    # 메인에서 네비게이션바의 '축산품 기획전' 페이지 열기 
    def open_exhibition(self):
        self.driver.get(self.MAIN_URL)

        # 요소 나타날 때까지 10초 기다리기
        exhibition_tab = ws(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, self.EXHIBITION_XPATH))
        )

        # '축산품 기획전' 클릭
        exhibition_tab.click()

    def scroll_exhibition(self):
        # '축산품 기획전' 페이지 열기
        self.driver.get(self.EXHIBITION_URL)
        
        time.sleep(3)

        # 페이지 버튼 요소까지 스크롤 내리기
        element_to_scroll = self.driver.find_element(By.XPATH, "//div[@class='pagination']//strong[text()='1']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll)

    def click_next_page_btn(self):
        try:
            next_page_button = ws(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='pagination']//a[@class='direction next']"))
            )

            # '다음 페이지' 버튼 클릭
            next_page_button.click()
        except:
            # '다음 페이지' 버튼이 없으면 안내 메시지 출력
            print("현재 페이지가 마지막 페이지입니다.")