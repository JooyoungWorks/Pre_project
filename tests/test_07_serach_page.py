from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# 크롬 드라이버 실행
driver = webdriver.Chrome()

driver.get("https://mall.ejeju.net/main/index.do")
driver.maximize_window()

# 페이지가 완전히 로딩될 때까지 대기
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("✅ 페이지 로드 완료")

def scroll_to_element(xpath=None, css=None):
    """요소를 화면에 보이도록 스크롤 이동"""
    try:
        element = None
        if xpath:
            element = driver.find_element(By.XPATH, xpath)
        elif css:
            element = driver.find_element(By.CSS_SELECTOR, css)

        if element:
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})", element)
            time.sleep(1)
    except NoSuchElementException:
        print(f"⚠️ 스크롤 실패: 요소 없음 - {xpath if xpath else css}")

def verify_element(xpath=None, css=None, description=""):
    """하나의 요소를 검증하는 함수"""
    try:
        scroll_to_element(xpath, css)  # 요소가 화면에 나타날 수 있도록 스크롤 이동
        wait = WebDriverWait(driver, 10)  # 최대 10초 대기
        element = None

        # XPath로 찾기
        if xpath:
            try:
                element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            except:
                pass

        # XPath로 못 찾았으면 CSS Selector 시도
        if not element and css:
            try:
                element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
            except:
                pass

        # 최종 검증
        assert element and element.is_displayed(), f"❌ 요소가 보이지 않습니다: {description}"
        print(f"✅ 요소 확인 성공: {description}")

    except NoSuchElementException:
        print(f"❌ 요소 없음: {description}")
        driver.save_screenshot(f"{description.replace(' ', '_')}_error.png")  # 오류 시 스크린샷 저장
    except Exception as e:
        print(f"⚠️ 오류 발생: {description} - {e}")

def verify_elements_on_page(elements):
    """지정된 요소 리스트를 검증하는 함수"""
    for element in elements:
        verify_element(xpath=element.get("xpath"), css=element.get("css"), description=element["description"])

# ✅ **초기 페이지 요소 검증**
initial_elements = [
    {"xpath": '//*[@id="gnb"]/ul[2]/li[2]/div/span[2]/a', "css": "#gnb > ul.gnb_main > li.utill > div > span.srch > a", "description": "검색버튼 요소"},
 
]
# 초기페이지 요소검증 함수 실행
verify_elements_on_page(initial_elements)

# ✅ **검색 버튼 클릭**
driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[2]/div/span[2]/a').click()
print("✅ 검색버튼 클릭")

# ✅ **검색어 입력**
search_box = driver.find_element(By.XPATH, '//*[@id="search-box"]')
search_box.send_keys("감귤")
search_box.submit()  # 검색 실행
print("✅ 감귤 검색 실행")

# ✅ **새로운 페이지가 로드될 때까지 대기**
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("✅ 새로운 페이지 로드 완료")

# ✅ **새로운 페이지에서 검증할 요소 리스트**
new_page_elements = [
    {"xpath": '//*[@id="wrap_container"]/div[1]/div[1]/h3', "css": "#wrap_container > div.wrap_content > div.con_title > h3", "description": "검색결과 요소"},
    {"xpath": '//*[@id="wrap_container"]/div[1]/div[2]/div/form/div[1]/div/span/input', "css": "#wrap_container > div.wrap_content > div.contents > div > form > div.bgcont_box.mt10 > div > span > input[type=text]", "description": "검색바 요소"},
]

# ✅ **새로운 페이지에서 요소 검증 실행**
verify_elements_on_page(new_page_elements)

time.sleep(3)
driver.quit()