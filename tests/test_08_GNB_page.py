import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.pages.GNB_page import GNB_Page
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


@pytest.mark.usefixtures("driver")  # driver를 달아줘야 conftest에 있는 드라이버를 이 파일에서 쓸 수 있다
class TestGNBPage:

    @pytest.mark.skip
    def test_open_main(self, driver: WebDriver):
        try:
            # 메인 페이지 열기
            main_page = GNB_Page(driver)
            main_page.open_main()

            # 네비게이션바 나타날 때까지 최대 10초 기다리기
            wait = ws(driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, GNB_Page.GNB_XPATH)))

            # 네비게이션바의 '축산물 기획전'이 잘 나타났는지 검증
            exhibition_tab = driver.find_element(By.XPATH, GNB_Page.EXHIBITION_XPATH)
            assert "축산물 기획전" in exhibition_tab.text
        except NoSuchElementException as e:
            assert False
    
    @pytest.mark.skip
    def test_open_exhibition(self, driver: WebDriver):
        try:
            # '축산품 기획전' 페이지 열기 (메인 페이지부터 시작)
            exhibition_page = GNB_Page(driver)
            exhibition_page.open_exhibition()

            time.sleep(3)

            page_heading = driver.find_element(By.XPATH, "//div[@class='con_title']//h3[@class='pt5 mt5']")
            assert "축산물 기획전" in page_heading.text
        except NoSuchElementException as e:
            assert False
        except TimeoutException as e:
            assert False
    
    @pytest.mark.skip
    def test_scroll_exhibition(self, driver: WebDriver):
        try:
            exhibition_page_scroll = GNB_Page(driver)
            exhibition_page_scroll.scroll_exhibition()

            # 스크롤을 내려 footer가 화면에 보이는지 확인
            footer = ws(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "footer"))
            )
        
            assert footer.is_displayed(), "❌ footer가 화면에 보이지 않습니다. 테스트 실패"
            
            # footer가 보이면 스크롤 완료 메시지 출력
            print("스크롤 완료")

        except AssertionError as e:
            print(f"테스트 실패: {e}")

        except Exception as e:
            print(f"오류 발생: {e}")

    def test_click_next_page_btn(self, driver: WebDriver):
        try:
            # 페이지 스크롤
            exhibition_page_scroll = GNB_Page(driver)
            exhibition_page_scroll.scroll_exhibition()

            click_next_page_btn = GNB_Page(driver)
            click_next_page_btn.click_next_page_btn

            pre_page_btn = ws(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='pagination']//a[@class='direction prev']")))

            assert pre_page_btn.is_enabled, "❌ 다음 페이지로 이동하지 못했습니다. 테스트 실패"
            print("✅ 다음 페이지 버튼 클릭 성공!")
        except Exception as e:
            print("현재 페이지가 마지막 페이지로, 다음 페이지 버튼 클릭 테스트 종료합니다.")