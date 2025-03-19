import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.pages.customer_service_page import CustomerServicePage


@pytest.mark.usefixtures("driver")
class TestCustomerServicePage:
    def test_open_customer_service_page(self, driver: WebDriver):
        try:
            customer_service_page = CustomerServicePage(driver)
            customer_service_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("board"))
            assert "board" in driver.current_url
            driver.save_screenshot("고객센터페이지-오픈-성공.png")
        
        except NoSuchElementException as e:
            assert False


    def test_message_board(self, driver: WebDriver):
        try:
            customer_service_page = CustomerServicePage(driver)
            customer_service_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("board"))
            assert "board" in driver.current_url

            time.sleep(2)

            customer_service_page.message_board()

            wait = ws(driver, 10)
            wait.until(EC.url_contains("boardContent"))
            assert "boardContent" in driver.current_url
            driver.save_screenshot("고객센터페이지-첫번째 게시물-성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot("고객센터페이지-첫번째 게시물-실패-노서치.png")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("고객센터페이지-첫번째 게시물-실패-타임에러.png")
            assert False