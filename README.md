# wanted_pre_onboarding
## 백엔드 과정 선발과제

### 과제설명
본 서비스는 크라우드 펀딩 기능을 제공합니다. 게시자는 크라우드 펀딩을 받기위한 상품(=게시물)을 등록합니다.
유저는 해당 게시물의 펀딩하기 버튼을 클릭하여 해당 상품 ‘1회펀딩금액’ 만큼 펀딩합니다.


과제 구현 세부 구성요소는 아래와 같습니다.

### 구성 요소
- **사용자(User)**
  - django abstractuser
- **상품(Product)**
  - publisher : 게시자
  - title : 제목
  - description : 상세설명
  - target_amount : 목표금액
  - total_amount : 총펀딩금액
  - one_time_funding_amount : 1회펀딩금액
  - deadline : 마감기한
  - created_at : 생성시간

### 기능
**상품을 등록합니다 : POST /api/products**
- 제목, 게시자명, 상품설명, 목표금액, 펀딩종료일, 1회펀딩금액로 구성

**상품을 수정합니다 : PUT /api/products/:pk**
- 모든 내용이 수정 가능하나 '목표금액'은 수정이 불가능합니다.
- 목표금액의 수정불가는 request body의 target_amount값이 기존에 저장되어 있던값과 다를시에 에러를 반환합니다.

**상품을 삭제합니다 : DELETE /api/products/:pk**
- pk 값에 해당하는 상품이 DB에서 삭제됩니다.

**상품 목록을 가져옵니다 : GET /api/products**
- 제목, 게시자명, 총펀딩금액, 달성률 및 D-day로 구성
- 상품 검색 기능 구현 : GET /api/products?search=~~
- 상품 정렬 기능 구현 : GET /api/products?order_by=생성일 or 총펀딩금액

**상품 상세 페이지를 가져옵니다 : GET /api/products/:pk**
- 제목, 게시자명, 총펀딩금액, 달성률, D-day(펀딩 종료일까지), 상품설명, 목표금액 및 참여자 수로 구성

**펀딩 : POST /api/products/:pk/funding**
- pk 값에 해당하는 상품의 1회 펀딩금액 만큼 후원합니다.

### 구현
- 기본적인 CRUD는 ModelViewset을 활용하여 구현
- 펀딩의 경우 따로 모델을 분리하였고 signal 기능을 이용하여 Sponsor 객체가 생성되었을때 1회 펀딩금액만큼 늘어나도록 설정함
- 후원자수, 달성률, D_day은 @property를 활용하여 구현 