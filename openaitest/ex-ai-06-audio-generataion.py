'''
OpenAI Multimodal API - 텍스트와 음성 동시 생성
   하나의 API 호출로 텍스트 응답과 음성 응답을 동시에 생성
   GPT-4의 텍스트 생성 능력과 TTS의 음성 합성 기능을 통합

주요 매개변수
   1. model
       - "gpt-4o-audio-preview": 텍스트와 음성을 동시 생성하는 모델

   2. modalities
       - 응답 형식을 지정하는 리스트
       - "text": 텍스트 응답 생성
       - "audio": 음성 응답 생성

   3. audio
       - voice: 음성의 특성 선택
           - alloy: 중성적이고 균형 잡힌 톤
           - echo: 깊고 차분한 톤
           - fable: 부드럽고 따뜻한 톤
           - onyx: 강력하고 단호한 톤
           - nova: 전문적이고 집중된 톤
           - shimmer: 밝고 긍정적인 톤
       - format: 오디오 파일 형식 (wav, mp3 등)

응답 처리
   1. 텍스트 응답
       - choices[0].message.content에서 텍스트 확인

   2. 음성 응답
       - choices[0].message.audio.data에서 base64 인코딩된 음성 데이터
       - base64 디코딩 후 파일로 저장

활용 분야
   - 음성 안내 시스템
   - 교육용 콘텐츠
   - 다국어 서비스
   - 접근성 향상
'''

import base64
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "wav"},
    messages=[
        {
            "role": "user",
            "content": "세종대왕 업적 5개 나열해줘?"
        }
    ]
)

print(completion.choices[0])

wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open("kingsejong.wav", "wb") as f:
    f.write(wav_bytes)