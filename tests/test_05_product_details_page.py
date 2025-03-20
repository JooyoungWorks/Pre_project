from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
import time


# 크롬 드라이버 실행
driver = webdriver.Chrome()

driver.get("https://mall.ejeju.net/main/index.do")
driver.maximize_window()

# 페이지가 완전히 로딩될 때까지 대기
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("✅ 페이지 로드 완료")

#메인 중앙 첫번째 상품 클릭
driver.find_element(By.XPATH, '//*[@id="wrap_container"]/div[1]/section[1]/ul/li[1]').click()
print("✅ 상품 클릭")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("✅ 상품 상세페이지 로드 완료")


def scroll_to_element(xpath=None, css=None):
    try:
        element = None
        if xpath:
            element = driver.find_element(By.XPATH, xpath)
        elif css:
            element = driver.find_element(By.CSS_SELECTOR, css)

        if element:
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})", element)
            time.sleep(2)
    except NoSuchElementException:
        print(f"⚠️ 스크롤 실패: 요소 없음 - {xpath if xpath else css}")

def verify_element(xpath=None, css=None, description=""):
    try:
        scroll_to_element(xpath, css)  # 요소가 화면에 나타날 수 있도록 스크롤 이동
        wait = WebDriverWait(driver, 20)  # 최대 20초 대기
        element = None

        # XPATH로 먼저 찾고, 실패하면 CSS Selector로 찾기
        if xpath:
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        if not element and css:
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
        
        assert element.is_displayed(), f"❌ 요소가 보이지 않습니다: {description}"
        print(f"✅ 요소 확인 성공: {description}")
    except NoSuchElementException:
        print(f"❌ 요소 없음: {description}")
        driver.save_screenshot(f"{description.replace(' ', '_')}_error.png")  # 오류 시 스크린샷 저장
    except Exception as e:
        print(f"⚠️ 오류 발생: {description} - {e}")

# 요소 리스트 (XPATH & CSS Selector)
elements_to_check = [

    {"xpath": '//*[@id="goodsBigImage"]', "css": "#frm > div.item_content > div.item_content_left > div > span", "description": "상품 메인 이미지"},
    {"xpath": '//*[@id="frm"]/div[3]/div[2]', "css": "#frm > div.item_content > div.item_content_right}", "description": "상품 정보 요소"},
    {"xpath": '//*[@id="cartPop"]', "css": "#cartPop", "description": "장바구니 요소"},
    {"xpath": '//*[@id="frm"]/div[3]/div[2]/div[5]/div[1]/button[3]', "css": "#frm > div.item_content > div.item_content_right > div.item_content_right_order > div.btn_choice_box > button.btn_buy_order.fc5", "description": "바로구매 버튼"},
    {"xpath": '//*[@id="frm"]/section[1]', "css": "#frm > section:nth-child(14)", "description": "관련추천상품 요소"},
    {"xpath": '//*[@id="frm"]/section[2]', "css": "#frm > section:nth-child(15)", "description": "묶음배송상품 요소"},
    {"xpath": '//*[@id="content"]/div', "css": "#content > div", "description": "상품 상세설명 요소"},
    {"xpath": '//*[@id="pc_prdDetailView"]/button', "css": "#pc_prdDetailView > button", "description": "상품 상세설명 더보기 버튼"},
    {"xpath": '//*[@id="tab-1"]/div/div/div[3]', "css": "#tab-1 > div > div > div:nth-child(3)", "description": "고객상담센터 요소"},

]

# 모든 요소 검증 실행
for element in elements_to_check:
    verify_element(xpath=element["xpath"], css=element["css"], description=element["description"])



def scroll_to_top():
    """
    페이지 상단으로 이동하는 함수.
    특정 버튼 클릭 방식으로 실행됨.
    """
    try:
        # "맨 위로 가기" 버튼 찾기
        top_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wrap_main"]/div[1]/a[2]'))
        )
        top_button.click()
        print("✅ 페이지 상단으로 이동 완료")
    except Exception as e:
        print(f"❌ 페이지 상단 이동 실패: {e}")

time.sleep(3)

# ✅ 상품 수량 조절 (증가/감소 버튼 클릭)
def adjust_quantity():
    try:
        # + 버튼 클릭
        plus_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="frm"]/div[3]/div[2]/div[4]/div[1]/div[2]/span/span/button[2]'))
        )
        plus_button.click()
        print("✅ 상품 수량 증가!")

        # - 버튼 클릭
        minus_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="frm"]/div[3]/div[2]/div[4]/div[1]/div[2]/span/span/button[1]'))
        )
        minus_button.click()
        print("✅ 상품 수량 감소!")
    except Exception as e:
        print(f"❌ 상품 수량 조절 실패: {e}")

time.sleep(5)


# ✅ 장바구니에 추가
def add_to_cart():
    try:
        # ✅ 장바구니 버튼 클릭
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cartPop"]'))
        )
        cart_button.click()
        print("✅ 장바구니 추가 성공!")

        # ✅ 알럿(팝업) 감지 및 닫기
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())  # 최대 5초 동안 알럿이 뜰 때까지 기다림
            alert = Alert(driver)  # 알럿 객체 생성
            print(f"⚠️ 알럿 감지: {alert.text}")  # 알럿 메시지 출력 (필요하면)
            alert.accept()  # 알럿 닫기 (확인 버튼 클릭)
            print("✅ 알럿 닫기 완료")
        except Exception:
            print("ℹ️ 알럿이 없습니다.")

        time.sleep(2)  # 추가 대기 (선택 사항)
    except Exception as e:
        print(f"❌ 장바구니 추가 실패: {e}")

time.sleep(5)

# ✅ 바로구매 버튼 클릭 후 구매 페이지 이동 확인
def buy_now():
    try:
        buy_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="frm"]/div[3]/div[2]/div[5]/div[1]/button[3]'))
        )
        buy_button.click()
        print("✅ 바로구매 버튼 클릭 성공!")

        # ✅ 구매 페이지가 로딩될 때까지 기다림 (URL 변경 확인)
        WebDriverWait(driver, 10).until(EC.url_contains("order"))
        print("✅ 구매 페이지 이동 확인 완료!")
    except Exception as e:
        print(f"❌ 구매 페이지 이동 실패: {e}")






# ✅ 기능 테스트 실행
scroll_to_top()    # 페이지 상단으로 이동
adjust_quantity()  # 상품 수량 조절
add_to_cart()      # 장바구니 추가
buy_now()          # 바로구매
time.sleep(3)


#비로그인 테스트로 로그인 페이지 진입 후 다시 상세페이지로 이동
driver.back()  
time.sleep(3)

# 브라우저 종료
driver.quit()
print("✅ 브라우저 종료")
print("✅ 테스트 종료")
