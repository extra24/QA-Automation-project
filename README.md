# 테스트 자동화 프로젝트

> 이 프로젝트는 Python, Selenium을 활용하여 웹 어플리케이션의 주요 기능을 자동화 테스트하는 예제 프로젝트입니다.

### 가상 테스트 시나리오 목록

1. **가상 로그인 테스트(`test_login.py`)** : 로그인 기능을 자동화하여 올바른 사용자 정보 테스트
2. **구글 검색 테스트 (`test_search.py`):** 구글 홈페이지에서 검색 기능을 테스트하고, 검색 결과 페이지가 올바르게 로드되었는지 검증
3. **위키백과 페이지 이동 및 내용 검증 테스트 (`test_wikipedia.py`):** 위키백과 대문에서 특정 링크를 클릭하여 페이지를 이동하고, 이동한 페이지의 내용이 올바른지 검증

## 1. 사전 준비

### • Python 설치 확인, Selenium 라이브러리 설치

```bash
# 파이썬 설치 확인
python

# requirements.txt에 있는 Selenium 설치
pip install -r requirements.txt
```

## 2. 실행 방법

### • 최상위 디렉토리에서 아래 명령어를 통해서 테스트 실행

```bash
python -m unittest tests.test_login
python -m unittest tests.test_search
python -m unittest tests.test_wikipedia
```

### • `unittest` 를 사용하여 모든 테스트 실행

```bash
python -m unittest discover tests
```

## 3. 프로젝트 구조

```
/qa-automation-project
├── tests/
│   ├── __init__.py         # 파이썬 패키지임을 알리는 빈 파일
│   ├── test_login.py       # 가상 로그인 테스트 코드
│   ├── test_search.py      # 구글 검색 기능 테스트 코드
│   └── test_wikipedia.py   # 위키백과 페이지 이동 및 내용 검증 테스트 코드
├── .gitignore              # Git에 올리지 않을 파일 목록
├── requirements.txt        # 프로젝트에 필요한 라이브러리 목록
└── README.md               # 프로젝트 설명 및 사용법
```
