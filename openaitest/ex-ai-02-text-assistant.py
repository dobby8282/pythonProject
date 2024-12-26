'''
OpenAI API - 대화형 AI 구현하기
   이전 대화 내용을 기억하고 문맥을 이해하여 대화를 이어나가는 방법

대화 기록 관리
   1. messages 리스트
       - 대화의 전체 흐름을 저장하는 리스트
       - 각 메시지는 role과 content를 가진 딕셔너리 형태
       - 시스템 메시지, 사용자 질문, AI 응답이 순차적으로 저장

   2. 대화 구성요소
       - system: AI의 역할 정의 (최초 1회 설정)
       - user: 사용자의 질문/입력 내용
       - assistant: AI의 응답 내용

대화 진행 과정
   1. 초기 질문과 응답
       - 첫 번째 질문을 포함한 messages로 API 호출
       - 받은 응답을 messages에 추가하여 대화 기록 유지

   2. 후속 질문과 응답
       - 이전 대화 기록이 포함된 messages에 새 질문 추가
       - 문맥을 파악하여 적절한 응답 생성

특징
   - 이전 대화 내용을 기반으로 맥락 이해 가능
   - 자연스러운 대화 흐름 구현
   - messages가 길어질수록 API 호출 비용 증가
'''

from openai import OpenAI
import os

client = OpenAI()

# 대화 기록을 저장할 messages 리스트
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "이순신의 업적 5가지"},
]

# 첫 번째 API 호출
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

# 첫 번째 응답 저장
first_response = completion.choices[0].message.content
print("첫 번째 응답:", first_response)

# assistant의 응답을 messages에 추가
messages.append({"role": "assistant", "content": first_response})

# 두 번째 질문 추가
messages.append({"role": "user", "content": "그 중에서 가장 위대한 업적은 뭐야?"})

# 두 번째 API 호출
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

# 두 번째 응답 출력
print("\n두 번째 응답:", completion.choices[0].message.content)