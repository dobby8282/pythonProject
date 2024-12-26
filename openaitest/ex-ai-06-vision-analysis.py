'''
GPT-4 Vision API - 이미지 인식과 분석
   이미지를 이해하고 분석하여 자연어로 설명하는 기술
   다양한 분석 작업 수행 가능 (객체 인식, 텍스트 인식, 장면 설명 등)

주요 매개변수
   1. model
       - "gpt-4-vision-preview": OpenAI의 이미지 분석 모델
       - 높은 수준의 이미지 이해 및 자연어 설명 생성

   2. messages 구성
       - role: 사용자의 역할
       - content: 텍스트와 이미지 정보를 포함하는 리스트
           - text: 이미지에 대한 질문/요청
           - image_url: base64로 인코딩된 이미지 데이터

   3. 이미지 요구사항
       - 지원 형식: png, jpeg, gif, webp
       - 최대 파일 크기: 20MB
       - base64 인코딩 필요

주요 기능
   1. 이미지 설명
       - 장면의 전반적인 내용 설명
       - 객체, 행동, 상황 등 인식

   2. 특정 분석
       - 특정 객체나 활동 식별
       - 세부적인 특징 분석

   3. 텍스트 인식 (OCR)
       - 이미지 내 텍스트 읽기
       - 다양한 언어의 텍스트 인식
'''

# GPT-4 Vision을 사용한 이미지 분석 예제
from openai import OpenAI
import base64

client = OpenAI()


def analyze_image(image_path, prompt):
    """
    이미지를 분석하고 설명하는 GPT-4 Vision 모델을 사용합니다.

    Parameters:
        image_path (str): 분석할 이미지 파일 경로
        prompt (str): 이미지에 대해 물어볼 질문이나 요청사항

    Returns:
        str: 이미지 분석 결과 또는 에러 메시지

    지원 파일 형식:
        - png, jpeg, gif, webp
        - 최대 파일 크기: 20MB
    """
    try:
        # 이미지를 base64로 인코딩
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        # GPT-4 Vision 모델로 이미지 분석 요청
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing image: {str(e)}"


# 사용 예시
if __name__ == "__main__":
    # 예시 1: 기본 이미지 설명
    result1 = analyze_image(
        "scene.jpg",
        "이 이미지에서 보이는 것을 자세히 설명해주세요."
    )
    print("기본 설명:", result1)

    # 예시 2: 특정 객체 찾기
    result2 = analyze_image(
        "people.jpg",
        "이 이미지에서 사람들은 어떤 활동을 하고 있나요?"
    )
    print("활동 분석:", result2)

    # 예시 3: 텍스트 읽기
    result3 = analyze_image(
        "document.jpg",
        "이 이미지에 있는 모든 텍스트를 읽어주세요."
    )
    print("텍스트 내용:", result3)