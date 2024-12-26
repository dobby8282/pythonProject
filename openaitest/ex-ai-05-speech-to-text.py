'''
OpenAI Whisper API - 음성을 텍스트로 변환(STT)
   음성 파일을 텍스트로 변환(Speech-To-Text)하는 기술
   다양한 언어를 자동으로 감지하고 높은 정확도로 변환

주요 매개변수
   1. model
       - "whisper-1": OpenAI의 음성 인식 모델
       - 다국어 지원 및 높은 인식률

   2. file (필수)
       - 변환할 오디오 파일
       - 지원 형식: mp3, mp4, mpeg, mpga, m4a, wav, webm
       - 최대 파일 크기: 25 MB

   3. language (선택)
       - 오디오의 언어 코드 지정
       - 예: "ko"(한국어), "en"(영어), "ja"(일본어)
       - 미지정시 자동 언어 감지

특징
   1. 파일 처리
       - with open() 구문으로 안전한 파일 읽기
       - 바이너리 모드("rb")로 파일 열기

   2. 다국어 지원
       - 다양한 언어의 자동 감지 및 변환
       - 특정 언어 지정으로 정확도 향상

   3. 에러 처리
       - 파일 형식, 크기 제한 등 고려
       - try-except로 안전한 예외 처리
'''

# OpenAI Whisper를 사용한 음성-텍스트 변환 예제
from openai import OpenAI
import os

client = OpenAI()


def transcribe_audio(audio_file_path, language="ko"):
    """
    오디오 파일의 내용을 텍스트로 변환합니다.

    Parameters:
        audio_file_path (str): 변환할 오디오 파일 경로
        language (str): 오디오의 언어 코드 (예: "ko", "en", "ja")
                       지정하지 않으면 자동으로 감지합니다.

    Returns:
        str: 변환된 텍스트 또는 에러 메시지

    지원 파일 형식:
        - mp3, mp4, mpeg, mpga, m4a, wav, webm
        - 최대 파일 크기: 25 MB
    """
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",  # OpenAI의 음성 인식 모델
                file=audio_file,
                language=language  # 특정 언어 지정 (선택사항)
            )
        return transcript.text
    except Exception as e:
        return f"Error transcribing audio: {str(e)}"


# 사용 예시
if __name__ == "__main__":
    # 예시 1: 한국어 음성 파일 변환
    result1 = transcribe_audio("greeting_alloy_ko.mp3", language="ko")
    print("한국어 변환 결과:", result1)

    # 예시 2: 영어 음성 파일 변환
    result2 = transcribe_audio("greeting_alloy_en.mp3", language="en")
    print("영어 변환 결과:", result2)

    # 예시 3: 자동 언어 감지로 변환
    result3 = transcribe_audio("greeting_alloy_en.mp3")
    print("자동 감지 변환 결과:", result3)