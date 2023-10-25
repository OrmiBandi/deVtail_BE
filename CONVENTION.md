# COMMIT 컨벤션
## 태그
|이모지|태그 이름        |           설명           |
|-----|----------------|--------------------------|
|✨   |Feat            | 새로운 기능을 추가할 경우  |
|🐛   |Fix             | 버그를 고친 경우            |
|💄   |Design          | CSS 등 사용자 UI 디자인 변경|
|🎨   |Style           | 코드 포맷 변경, 세미 콜론 누락, 코드 수정이 없는 경우|
|♻️    |Refactor        | 프로덕션 코드 리팩토링|
|💡   |Comment         | 필요한 주석 추가 및 변경|
|📝   |Docs            | 문서를 수정한 경우|
|🧪   |Test            | 테스트 추가, 테스트 리팩토링(프로덕션 코드 변경 X)|
|👷   |Chore           | 빌드 태스트 업데이트, 패키지 매니저를 설정하는 경우(프로덕션 코드 변경 X)|
|🚚   |Rename          | 파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우|
|🔥   |Remove          | 파일을 삭제하는 작업만 수행한 경우|
|👽️   |!BREAKING CHANGE| 커다란 API 변경의 경우|
|🐛   |!HOTFIX         | 급하게 치명적인 버그를 고쳐야하는 경우|


## Commit 예시(Feat)
```
(커밋 이모지)Feat: 제목(추가한 기능 / 변경한 기능) (# 이슈번호)
✨Feat: Login 기능 개발 (#13)

### 수정 파일
main.py
index.py

### 추가한 기능
Login 기능 추가

(필요한 경우) ## 비고
```
## Commit 예시(Fix)
```
Fix 변경한 기능 (#이슈번호)
🐛Fix: type_message_and_enter (#3)

### 수정 파일
main.py
index.py

### 원인
스터디 멤버들 호출 시 @'이름'에서 'tab'이 안눌림

### 수정
호출 인원이 많을 시 디스코드 반응이 늦어지는 것이 원인으로, sleep(0.1)을 sleep(0.3)으로 수정. 이후 또 안되면 0.5로 수정
```


# 코드 컨벤션
 ## Python 코드
  - 전체적인 컨벤션 기준은 [PEP 8](https://peps.python.org/pep-0008/)로 한다.

  ### 공통
   - 탭 간격 들여쓰기 4칸
   - 기본적으로 문자형은 '' 사용
   - 주석 위치: def, class 다음 라인에 ''' '''
   - import * 지양 (개별적으로 import)
   - 라인별 최대 길이는 72(왠만하면 가독성있는 방향)
   
  ### 변수
   - 네이밍: 스네이크(예시 hello_world)
   - 'l'(소문자 엘), 'O'(대문자 오) 또는 'I'(대문자 아이) 문자를 단일 문자 변수 이름으로 사용 금지(예시 I, l, O <- 이렇게 사용 X)

  ### 함수
1.
board update
board create
2.
create board
update board

[Django 컨벤션](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)

 ### 변수, 함수, 클래스 네이밍
- 함수, 변수, 속성 : losercase_underscore
- protected 인스턴스 속성 : _leading_underscore
- private 인스턴스 속성 : __double_leading_underscore
- 클래스 및 예외 : CapitalizeWord
- 모듈 수준 상수 : ALL_CAPS
- 클래스의 인스턴스 메서드에서는 첫번째 파라미터 (해당 객체 참조)의 이름을 self로 지정
- 클래스 메서드에서는 첫번째 파라미터(해당 클래스 참조)의 이름을 cls로 지정

 ## HTML/CSS 
 1. 유효하고 읽을 수 있는 DOM 작성
   - 모든 태그는 lowercase
   - 들여쓰기 2칸
   - HTML에서 주석 사용은 지양하기
 2. 인라인 스타일과 스크립트 사용 지양
   - 인라인 크리티컬 CSS : 중요한 CSS의 경우 맨 위에 배치
 3. script 태그는 맨 아래 배치
   - 본문과 스크립트의 로딩 순서의 문제로 오류 발생 가능
   - script를 아래 두고도 해결이 안되면 defer 태그 추가
 4. 이미지에 alt 태그 사용
   - 로드, 경로 문제 등으로 이미지가 나오지 않을 때 텍스트가 표시되도록
 5. 하나의 페이지에는 하나의 h1
   - h1~h5 순서대로 나올 수 있도록. 글자 크기가 마음에 안 들 경우 CSS에서 수정
 6. 제목 및 메타 태그 사용
 7. 페이지 완성 시 HTML 유효성 확인
   - https://validator.w3.org/

 ## JavaScript
 
# 문서 컨벤션