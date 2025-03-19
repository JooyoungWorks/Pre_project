# 메인 페이지 테스트

import pytest
import datetime # 스크린샷 파일명에 날짜와 시간 정보 기록을 위해 import

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from pages.main_page import MainPage

@pytest.mark.usefixtures("driver")
class TestMainPage:
    # 배너 관련 변수들
    banner_CLASS = "bx-viewport" # 배너 XPATH값
    banner_pager_CLASS = "bx-pager-item"   # 배너 페이저 항목들

    # 배너 버튼 클릭 테스트
    def test_main_banner_btn(self, driver:WebDriver):
        try:
            # 메인 페이지 열기
            mainPage = MainPage(driver)
            mainPage.open()

            # 메인 페이지 제대로 접근했는지 확인
            assert "mall.ejeju.net" in driver.current_url, "❌ 메인 페이지에 접근되지 않았습니다."

            # 배너 영역 나올때까지 최대 10초 대기
            WW(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, self.banner_CLASS)))

            # 배너 정상 제공 시 메시지 출력 및 스크린샷 저장
            print("✅ 배너가 정상 출력되었습니다.")
            driver.save_screenshot(f"메인 페이지 - 배너 정상 제공_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

            # 배너 리스트 추출
            banners = driver.find_element(By.CLASS_NAME,self.banner_CLASS).find_elements(By.TAG_NAME,"li")

            # 현재 배너 페이지 값 추출
            bn_current_active = driver.find_element(By.CSS_SELECTOR, "a.bx-pager-link.active")  # 페이지 현재 활성화 상태인 것 찾기
            bn_current_index = int(bn_current_active.get_attribute("data-slide-index")) # 현재 활성화 된 페이지 index 값 추출

            # 가장 처음 위치 활성화 상태였을 경우 비교할 index 값 변경
            if bn_current_index == 0:
                bn_current_index = 5

            # (여기부터 작업 이어서) 현재 노출중인 배너와 index 동일한지 확인
            current_banner = ""

            # 배너 이전 버튼 선택
            MainPage.banner_btn_click("bx-prev")
            print("✅ 이전 버튼을 클릭했습니다.")

            # 페이저 active 상태 변경 대기
            WW(driver, 10).until(lambda d: int(d.find_element(By.CSS_SELECTOR, "a.bx-pager-link.active").get_attribute("data-slide-index")) != bn_current_index)
            bn_new_active = driver.find_element(By.CSS_SELECTOR, "a.bx-pager-link.active")
            bn_new_index = int(bn_new_active.get_attribute("data-slide-index"))

            assert bn_new_index == bn_current_index-1, "❌ 이전 배너로 이동하지 못했습니다."

        except TimeoutException as e:
            print(e)
            # 스크린샷 추가 예정
        except NoSuchElementException as e:
            print(e)
            # 스크린샷 추가 예정정

    @pytest.skip("구현 중")
    def test_main_banner_hover(self, driver:WebDriver):
        try:
            print("구현 중")
        except NoSuchElementException:
            print("구현 중")