from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC


class GNB_Page:
    MAIN_URL = "https://mall.ejeju.net/main/index.do"
    GNB_XPATH = "//ul[@class='gnb_main']"
    EXHIBITION_XPATH = "//ul[@class='gnb_main']//li[@class='top_menu']//a[contains(text(), '축산물 기획전')]"

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