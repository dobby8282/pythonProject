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