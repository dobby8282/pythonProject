# OpenAI TTS(Text-to-Speech) 예제
from openai import OpenAI
import os

client = OpenAI()

def generate_speech(text, voice="alloy", output_file="speech.mp3"):
    """
    텍스트를 자연스러운 음성으로 변환하여 오디오 파일로 저장합니다.

    Parameters:
        text (str): 음성으로 변환할 텍스트
        voice (str): 사용할 음성 모델
            - alloy: 중성적이고 균형 잡힌 톤
            - echo: 깊고 차분한 톤
            - fable: 부드럽고 따뜻한 톤
            - onyx: 강력하고 단호한 톤
            - nova: 전문적이고 집중된 톤
            - shimmer: 밝고 긍정적인 톤
        output_file (str): 저장할 오디오 파일 경로

    Returns:
        str: 성공/실패 메시지
    """
    try:
        response = client.audio.speech.create(
            model="tts-1",  # OpenAI의 텍스트 음성 변환 모델
            voice=voice,
            input=text
        )
        response.stream_to_file(output_file)
        return f"Speech saved to {output_file}"
    except Exception as e:
        return f"Error generating speech: {str(e)}"

# 사용 예시
if __name__ == "__main__":
    # 예시 1: 기본 음성 생성 (alloy voice)
    text1 = "안녕하세요. 오늘도 좋은 하루 보내세요."
    result1 = generate_speech(text1, output_file="greeting_alloy_ko.mp3")
    print(result1)

    text1 = "Hello, Have a nice day!"
    result1 = generate_speech(text1, output_file="greeting_alloy_en.mp3")
    print(result1)

    # 예시 2: 전문적인 톤의 음성 생성 (nova voice)
    text2 = "이번 프로젝트의 주요 목표는 고객 만족도 향상입니다."
    result2 = generate_speech(
        text2,
        voice="nova",
        output_file="business_nova.mp3"
    )
    print(result2)

    # 예시 3: 따뜻한 톤의 음성 생성 (fable voice)
    text3 = "이야기 들려줄게요. 옛날 옛적에..."
    result3 = generate_speech(
        text3,
        voice="fable",
        output_file="story_fable.mp3"
    )
    print(result3)
