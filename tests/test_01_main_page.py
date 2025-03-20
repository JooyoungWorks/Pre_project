# 메인 페이지 테스트

import pytest
import datetime # 스크린샷 파일명에 날짜와 시간 정보 기록을 위해 import

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from pages.main_page import MainPage

@pytest.mark.usefixtures("driver")
class TestMainPage:
    # 배너 관련 변수들
    banner_CLASS = "bx-viewport"    # 배너 영역 class 값
    banner_pager_CLASS = "bx-pager-item"   # 배너 페이저 항목들

    # 배너 버튼 클릭 테스트
    def test_main_banner_btn(self, driver:WebDriver):
        print(f"드라이버는 > {driver}")
        try:
            # 메인 페이지 열기
            mainPage = MainPage(driver)
            mainPage.open()

            # 메인 페이지 제대로 접근했는지 확인
            assert "mall.ejeju.net" in driver.current_url, "❌ 메인 페이지에 접근되지 않았습니다."

            # 배너 영역 나올때까지 최대 10초 대기
            WW(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, self.banner_CLASS)))

            # 배너 정상 제공 시 메시지 출력 및 스크린샷 저장
            print("✅ 배너가 정상 출력되었습니다.")
            driver.save_screenshot(f"메인 페이지 - 배너 정상 제공_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            
            # 배너 리스트 추출
            banners = driver.find_elements(By.CLASS_NAME, self.banner_CLASS)    # 배너 추출
            banners_li = [element for element in banners if element.tag_name == "li"]   # 배너 코드 안에서 li 태그만 추출

            # 현재 배너 페이지 값 추출
            bn_current_active = driver.find_element(By.CSS_SELECTOR, "a.bx-pager-link.active")  # 페이지 현재 활성화 상태인 것 찾기
            bn_current_index = int(bn_current_active.get_attribute("data-slide-index")) # 현재 활성화 된 페이지 index 값 추출

            # 가장 처음 위치 활성화 상태였을 경우 비교할 index 값 변경
            if bn_current_index == 0:
                bn_current_index = 5

            # 페이저 active 상태 변경 대기
            WW(driver, 15).until(lambda d: int(d.find_element(By.CSS_SELECTOR, "a.bx-pager-link.active").get_attribute("data-slide-index")) != bn_current_index)

            # 변경 감지 후 버튼 클릭 실행
            bn_new_active = driver.find_element(By.CSS_SELECTOR, "a.bx-pager-link.active")  # 신규 활성화 페이저 확인
            bn_new_index = int(bn_new_active.get_attribute("data-slide-index")) # 신규 활성화 페이저의 index 값

            if bn_new_index != bn_current_index:  # 변경 확인
                mainPage.banner_btn_click("bx-prev")  # 이전 버튼 클릭
                print("✅ 이전 버튼을 클릭했습니다.")
            else:
                print("❌ 페이저 상태가 변경되지 않았습니다.")

            # 페이저 변경되었는지 index 값으로 확인
            assert bn_new_index == bn_current_index-1, "❌ 이전 배너로 이동하지 못했습니다."
            
            # 이동된 배너와 현재 페이지 위치 동일한지 확인
            current_banner = banners_li[bn_new_index]  # 페이저 활성화 된 index 순서와 같은 배너 추출
            cb_zindex = current_banner.value_of_css_property("z-index")    # 현재 배너의 z-index 값 가져오기
            assert cb_zindex != 0, "❌ 현재 페이지와 다른 배너가 제공되고 있습니다."   # z-index 값이 동적으로 바뀌고 있어 0이 아닌지 검증

        except TimeoutException as e:
            print("❌ 타임아웃 에러 발생")
            driver.save_screenshot(f"타임아웃 에러_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            assert False

        except NoSuchElementException as e:
            print(f"❌ 항목 검색 실패\n오류 상세 : {e}")
            driver.save_screenshot(f"항목 검색 실패_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            assert False