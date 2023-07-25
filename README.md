# 파이썬 모듈 구성 및 실행
### 조건
- clj처럼 쓸 수 있으면 됨
  - 개발 중에는 빠른 피드백을 지원하고
  - 개발 후에도 코드 변경 없이 멀쩡히 서로 호출하고
  - 가능한 코드 파일 안에 같이 있는 코드로 테스트할 수 있음 (`__main__` ?)

### 해답
파일 구조
- root/
  - proj/동일-디렉토리-구조, 모든 디렉토리에 `__init__.py` 포함
  - tests/동일-디렉토리-구조, 모든 디렉토리에 `__init__.py` 포함
- proj/ 아래에 util/을 둬야 함. 
- proj/ 아래 main.py를 둬야 함. 그 외 실험용 스크립트도 둘 수 있음

import
- proj/를 기준으로 절대 import를 하면 됨(vim의 경우 cwd를 proj로 하면 편함)

실행 방식
- 반드시 proj/ 바로 아래에 존재하는 (탑레벨) 스크립트만 실행해야 함
  - proj 디렉토리에서 `python main.py` 이런 식으로 실행(부모를 더 붙여도 실행은 됨)
  - 개별 소스 위치에서 실행은 안 됨(clj와 차이점)
- `pytest`를 하면 알아서 실행 됨
  - `$ pytest`로 유닛 테스트(개발용)
  - 필요하면 통합 테스트 추가할 것
