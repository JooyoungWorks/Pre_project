# conftest.py: pytest의 공용 설정을 관리하는 파일
# 테스트 코드에서 공통적으로 사용할 fixture(고정된 테스트 설정)를 정의하는 데 사용됨
# 여러 개의 테스트 파일에서 중복되는 설정 코드나 초기화 코드를 관리할 수 있음
import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
]

# 매 테스트 함수(function) 실행마다 새로운 driver 인스턴스를 생성
# 새로운 driver 인스턴스는 열면 각 테스트가 독립적으로 실행되고,
# 오류나 상태 변경이 다른 테스트에 영향주지 않음 (테스트 간 간섭 없음)
# 그리고 테스트가 끝날 때마다 브라우저가 닫혀서 리소스가 정리되는 효과도 있음
# 병렬 테스트 실행도 가능
@pytest.fixture(scope="function")
def driver():

    user_agent = random.choice(user_agents)
    # 크롬 실행 옵션 설정
    # 자동화 크롤링을 막아둔 사이트에 접근하려면 많은 옵션 수정이 필요함
    chrome_options = Options()

    # 옵션 수정을 안 하면 메인 페이지에서 이동이 안 된다.
    # 다른 서버의 ip를 가져와서 우회하는 proxy 방법이 있다. (뚫어서 크롤링하다가 걸리면 내 ip를 차단해서 사이트에 들어갈 수 없게 됨. 이때 우회 사용)
    # 1)을 통해서 "나는 자동화 브라우저가 아닌 firefox에서 온 일반 유저야" 하고 속이는 것
    # 1) User-Agent 변경
    chrome_options.add_argument(f'user-agent={user_agent}')

    # 2) SSL 인증서 에러 무시
    # 일부 웹사이트는 Selenium 감지를 위해 SSL 인증서를 검사함
    # 인증서 에러를 무시하여 브라우저가 정상적으로 실행되도록 설정
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")

    # 자동화된 브라우저가 아니라는 설정값
    # 4) Selenium이 automation된 브라우저임을 숨기는 몇 가지 설정
    #    - (disable-blink-features=AutomationControlled) 제거 -> 내가 자동화 프로그램을 쓰고 있다는 표시를 삭제함
    #    - excludeSwitches, useAutomationExtension
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # 혹은 다음 방식으로 Blink 특징을 비활성화할 수도 있으나
    # "AutomationControlled" 자체가 표기되지 않도록 한다.
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # 5) 디버그 로깅 줄이기 (선택)
    # chrome_options.add_argument("--log-level=3") 

    # 나 샌드박스 아니다.
    # 6) Sandbox나 DevShm 사이즈 문제(공유 메모리 사용으로 메모리 부족) 우회 (리눅스 환경에서 발생 가능)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # 추가
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-popup-blocking')
    
    # 드라이버 객체 생성
    # Service()는 안 넣으면 기본값이 들어가서 상관은 없지만, 넣음
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    #추가
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # cdp(Chrome DevTools Protocol) 명령어로 HTTP 요청 헤더 수정
    # 헤더를 ejeju.net로 설정하여 내부에서 온 트래픽처럼 위장
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"Referer": "https://mall.ejeju.net/main/index.do"}})
    driver.execute_cdp_cmd("Network.clearBrowserCache", {})

    # Scrape using Stealth
# enable stealth mode
# 추가
    stealth(driver,
        languages=["ko-KR", "ko"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    driver.delete_all_cookies()

# 이제 사이트 동작 가능

    # 대기시간 설정
    driver.implicitly_wait(5)

    # yield 전은 setUp, 후는 teardown. 데이터 준비와 정리의 분기점
    # driver를 공용으로 쓸 거라 yield에 드라이버를 집어 넣었다.
    yield driver

    # 테스트가 끝나면 드라이버 종료
    driver.quit()