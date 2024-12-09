'''
파일명: Ex12-8-time.py
time 모듈의 주요 기능 예제
    - 현재 시간 조회
    - 시간 형식 변환
    - 시스템 일시 정지
'''
import time

# 유닉스 타임스탬프 반환 (1970년 1월 1일 00:00:00 UTC 기준)
print(time.time())

# 타임스탬프를 읽기 쉬운 문자열로 변환
print(time.ctime(time.time()))

# strftime()으로 날짜/시간을 지정된 형식의 문자열로 변환
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y년 %m월 %d일 %H:%M:%S'))

# 1초 동안 프로그램 실행 중지
time.sleep(1)

# 1초 간격으로 카운트하여 10초 후 종료
sec = 1
while True:
    print(sec)
    if sec == 10:
        break
    time.sleep(1)
    sec += 1
