# OpenAI Whisper를 사용한 음성 번역 예제
from openai import OpenAI
import os

client = OpenAI()

def translate_audio(audio_file_path, output_text_path=None):
    """
    오디오 파일의 음성을 영어로 번역합니다.

    Parameters:
        audio_file_path (str): 번역할 오디오 파일 경로
        output_text_path (str): 번역 결과를 저장할 텍스트 파일 경로 (선택사항)

    Returns:
        str: 영어로 번역된 텍스트 또는 에러 메시지

    지원되는 파일 형식:
        - mp3, mp4, mpeg, mpga, m4a, wav, webm
        - 최대 파일 크기: 25MB
    """
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = client.audio.translations.create(
                model="whisper-1",  # OpenAI의 음성 번역 모델
                file=audio_file,
                response_format="text"  # 다른 옵션: "json", "srt", "verbose_json", "vtt"
            )

        # 결과를 파일로 저장 (선택사항)
        if output_text_path:
            with open(output_text_path, 'w', encoding='utf-8') as f:
                f.write(transcript.text)
            return f"Translation saved to {output_text_path}: {transcript.text}"
        
        return transcript.text

    except Exception as e:
        return f"Error translating audio: {str(e)}"

def batch_translate_audio(audio_directory, output_directory):
    """
    디렉토리 내의 모든 오디오 파일을 번역합니다.

    Parameters:
        audio_directory (str): 오디오 파일들이 있는 디렉토리 경로
        output_directory (str): 번역 결과를 저장할 디렉토리 경로

    Returns:
        dict: 각 파일의 번역 결과 또는 에러 메시지
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    results = {}
    for filename in os.listdir(audio_directory):
        if filename.lower().endswith(('.mp3', '.mp4', '.mpeg', '.mpga', '.m4a', '.wav', '.webm')):
            audio_path = os.path.join(audio_directory, filename)
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_translated.txt")
            
            results[filename] = translate_audio(audio_path, output_path)
    
    return results

# 사용 예시
if __name__ == "__main__":
    # 예시 1: 단일 오디오 파일 번역
    result1 = translate_audio(
        "korean_speech.mp3",
        "korean_speech_translated.txt"
    )
    print("단일 파일 번역 결과:")
    print(result1)
    print("-" * 50)

    # 예시 2: 응답 형식을 지정하지 않고 번역
    result2 = translate_audio("japanese_speech.mp3")
    print("직접 번역 결과:")
    print(result2)
    print("-" * 50)

    # 예시 3: 여러 오디오 파일 일괄 번역
    results = batch_translate_audio(
        "audio_files",
        "translated_texts"
    )
    print("일괄 번역 결과:")
    for filename, result in results.items():
        print(f"\n{filename}:")
        print(result)
