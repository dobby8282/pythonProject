'''
OpenAI API 사용하기
   OpenAI에서 제공하는 AI 모델을 파이썬에서 활용하는 방법

주요 구성요소
   1. OpenAI 객체 생성
       - OpenAI 클래스의 인스턴스를 생성하여 API 통신 준비
       - API 키가 필요 (환경변수 OPENAI_API_KEY 사용)

   2. Chat Completion
       - AI 모델과 대화를 수행하는 API
       - model: 사용할 AI 모델 지정 (ex: gpt-4, gpt-3.5-turbo)
       - messages: 대화 내용을 담는 리스트
           - role: system(AI 지시), user(사용자), assistant(AI 응답)
           - content: 실제 대화 내용

   3. 응답 처리
       - completion.choices[0].message.content로 AI 응답 내용 접근
       - choices: 여러 개의 응답을 받을 수 있음 (기본값: 1개)

주의사항
   - API 키는 보안을 위해 코드에 직접 입력하지 않고 환경변수 사용
   - API 사용량에 따라 비용 발생
   - 응답 시간은 모델과 요청 내용에 따라 다름
'''

from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "이순신의 업적 5가지"
        }
    ]
)

print(completion.choices[0].message.content)