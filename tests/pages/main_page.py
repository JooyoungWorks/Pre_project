# 메인 페이지

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class MainPage:
    URL = "https://mall.ejeju.net/main/index.do"    # 이제주몰 메인 페이지 URL

    # 초기 준비 작업
    def __init__(self, driver:WebDriver):
        self.driver = driver    # 각 객체에서 사용할 드라이버 정의 (Chrome)
    
    # 이제주몰 메인 페이지 Open 메서드
    def open(self):
        self.driver.get(self.URL)

    # 배너 버튼 클릭 메서드
    def banner_btn_click(self, banner_btn_class):   # 배너 버튼 클래스명 받아와서 실행
        banner_btn = self.driver.find_element(By.CLASS_NAME, banner_btn_class)  # 받아온 클래스명으로 클릭할 버튼 탐색
        banner_btn.click()