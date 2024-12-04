'''
파일명: time_datetime_examples.py

time 모듈: 
   - 기본적인 시간 처리 기능 제공
   - timestamp, 시간 포맷팅, sleep 등 지원

datetime 모듈:
   - 날짜와 시간을 더 직관적으로 다루는 기능 제공 
   - 날짜/시간 연산, 비교, 포맷팅 등이 가능

timedelta:
   - datetime 모듈의 시간 연산을 위한 클래스
   - 날짜/시간의 차이를 계산하거나 더하고 뺄 때 사용
'''
import time
from datetime import datetime, timedelta

# time.time(): Unix timestamp 반환 (1970년 1월 1일부터의 초)
print('=== time 모듈 ===')
print(f'현재 timestamp: {time.time()}')
print(f'현재 시간: {time.strftime("%Y-%m-%d %H:%M:%S")}')
print(f'현재 시간(한글): {time.strftime("%Y년 %m월 %d일 %H:%M:%S")}')

# datetime.now(): 현재 날짜와 시간을 datetime 객체로 반환
print('\n=== datetime 모듈 ===')
now = datetime.now()
print(f'현재 날짜/시간: {now}')
print(f'포맷팅: {now.strftime("%Y년 %m월 %d일 %H:%M:%S")}')

# timedelta: 날짜/시간 연산 (일, 시, 분, 초 단위 지원)
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print(f'\n내일: {tomorrow.strftime("%Y-%m-%d")}')
print(f'어제: {yesterday.strftime("%Y-%m-%d")}')

# datetime 객체 간의 차이 계산
date1 = datetime(2023, 6, 11)
date2 = datetime(2023, 12, 25)
diff = date2 - date1
print(f'\n날짜 차이: {diff.days}일')
