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
