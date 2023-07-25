# 파이썬 모듈 구성 및 실행
## 조건
- clj처럼 쓸 수 있으면 됨
  - 개발 중에는 빠른 피드백을 지원하고
  - 개발 후에도 코드 변경 없이 멀쩡히 서로 호출하고
  - 가능한 코드 파일 안에 같이 있는 코드로 테스트할 수 있음 (`__main__` ?)

## 해답
구조
- 프로젝트 루트 디렉토리 아래 탑 패키지 `PROJ`(프로젝트 이름), `tests`를 둠
- 패키지가 되는 모든 디렉토리에 `__init__.py`를 넣어야 함

코드
- pyproject.toml에 다음을 넣어야 `pytest` 명령이 작동함 
  - `[tool.pytest.ini_options]` <br> `pythonpath = "PROJ"`
- 탑 패키지 PROJ는 import 경로에 넣지 않음
  - `root/PROJ/p1/p2/m.py` -> `from p1.p2 import m`

실행
- `python PROJ/xx.py` 오직 탑 패키지 `PROJ` 바로 아래 모듈만 실행 가능
- `pytest`로 `tests` 아래 임의의 코드 실행 가능

## 응용
실행 방법
- 프로젝트 루트 디렉토리(`root`)에서 실행
  - `python PROJ/xx.py` 오직 탑 패키지 `PROJ` 바로 아래 모듈만 실행 가능
  - `pytest`로 유닛 테스트(개발용), 필요하면 통합 테스트 추가할 것

개발 사이클
- 빠른 피드백: 탑 패키지 아래 임시 코드 `python PROJ/xx.py`로 피드백
- 모듈 쪼개기: 임시코드를 테스트 코드로, 임시 모듈을 나뉘어진 모듈로.
- 유닛/통합 테스팅: `pytest` 실행(`tests` 아래 임의의 코드 실행)
