# 이제주몰 기능 테스트 프로젝트
- Selenium과 Pytest를 활용하여 이제주몰의 페이지별 기능을 테스트하는 프로젝트입니다.
- 팀원: 김주영(조장), 신은영, 양송이, 이수빈
- 테스트 할 사이트: <https://mall.ejeju.net/main/index.do>

<br>

### [페이지: 기능] 분석
1. 메인: 페이지 오픈, 배너 변경 체크, 스크롤
2. 로그인: 회원가입, 로그인
3. 고객센터: 게시판 선택, 게시물 확인
4. 상품 리스트 페이지 중 1: 페이지 오픈, 특정 상품에 마우스 호버했을 때 뜨는 4개 버튼 클릭
5. 상품 상세 페이지: 옵션 변경, 장바구니 담기
6. 장바구니: 수량 변경, 상품 삭제 (최대수량 제한 없음)
7. 검색: 검색어 입력, 상품 정렬
8. 네비게이션바: 각 메뉴 페이지 오픈, 맨 밑 페이지 넘기기

<br>

### 담당 페이지
난이도 하, 난이도 상으로 나누어 각 1개씩 맡았습니다.
- 주영 8, 6 (네비, 장바구니)
- 은영 3, 4 (고객, 상품리스트)
- 송이 1, 2 (메인, 로그인)
- 수빈 7, 5 (검색, 상품상세)

<br>

### 규칙
- dev 밑으로 ‘feature/이름’ branch 만들고, 개인 branch에서 수정하여 dev branch로 PR 날리기
  - 팀원 중 한 명이 확인 후 comment 남겨주면, 스스로 개인 branch에서 dev로 merge
  - 모든 작업 완료 후 마지막에 조장이 dev에서 main으로 merge
- 테스트 파일 이름 형식: test_번호_페이지이름_page.py
  - 테스트 파일은 tests 폴더 안에 저장
- 페이지(기능 구현) 파일 이름 형식: 페이지이름_page.py
  - 페이지 파일은 tests 폴더 안의 pages 폴더 안에 저장