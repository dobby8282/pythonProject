import openai
import base64
from mimetypes import guess_type

def local_image_to_data_url(image_path):
    """
    이미지 파일을 base64 데이터 URL로 변환하는 함수
    :param image_path: 변환할 이미지 파일의 경로
    :return: base64로 인코딩된 데이터 URL
    """
    # MIME 타입 추정
    mime_type, _ = guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # MIME 타입이 없을 경우 기본값 설정

    # 이미지 파일 읽기 및 base64 인코딩
    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # 데이터 URL 생성
    return f"data:{mime_type};base64,{base64_encoded_data}"

def analyze_image_with_gpt(image_path):
    """
    GPT-4 Turbo with Vision API를 호출하여 이미지를 분석하는 함수
    :param image_path: 분석할 이미지 파일의 경로
    :return: 이미지 분석 결과 텍스트
    """
    try:
        # 이미지를 Base64 데이터 URL로 변환
        image_data_url = local_image_to_data_url(image_path)

        # OpenAI GPT-4 Turbo API 호출
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo-2024-04-09",
            messages=[
                {"role": "system", "content": "You are a helpful assistant and you should respond in Korean."},
                {"role": "user", "content": [
                    {"type": "text", "text": "이 사진을 설명해주세요:"},
                    {"type": "image_url", "image_url": {"url": image_data_url}}
                ]}
            ],
            max_tokens=100  # 응답 토큰 최대 개수 설정
        )

        # 분석 결과 텍스트 반환
        return response['choices'][0]['message']['content']

    except Exception as e:
        # 에러 발생 시 에러 메시지 반환
        return {"error": str(e)}

# 테스트: 이미지 파일 분석
if __name__ == "__main__":
    image_path = "example_image.jpg"  # 분석할 이미지 파일 경로
    result = analyze_image_with_gpt(image_path)  # 분석 함수 호출
    print(result)  # 분석 결과 출력
