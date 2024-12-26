# GPT-4 Vision URL 분석 예제
from openai import OpenAI
import json

client = OpenAI()

def analyze_image_from_url(image_url, prompt, max_tokens=300):
    """
    온라인 이미지 URL을 통해 이미지를 분석합니다.

    Parameters:
        image_url (str): 분석할 이미지의 URL
        prompt (str): 이미지에 대해 물어볼 질문이나 요청사항
        max_tokens (int): 응답의 최대 길이

    Returns:
        str: 이미지 분석 결과 또는 에러 메시지

    지원 형식:
        - 대부분의 이미지 형식 (jpg, png, webp 등)
        - 공개적으로 접근 가능한 URL이어야 함
        - 이미지 크기 제한: 20MB
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": image_url,
                        }
                    ]
                }
            ],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing image: {str(e)}"

def batch_analyze_images(image_urls, prompt):
    """
    여러 이미지 URL을 일괄 분석합니다.

    Parameters:
        image_urls (list): 분석할 이미지 URL 리스트
        prompt (str): 각 이미지에 대해 물어볼 동일한 질문

    Returns:
        dict: 각 URL에 대한 분석 결과
    """
    results = {}
    for url in image_urls:
        results[url] = analyze_image_from_url(url, prompt)
    return results

def analyze_image_with_multiple_questions(image_url, questions):
    """
    하나의 이미지에 대해 여러 질문을 분석합니다.

    Parameters:
        image_url (str): 분석할 이미지 URL
        questions (list): 이미지에 대한 질문 리스트

    Returns:
        dict: 각 질문에 대한 분석 결과
    """
    results = {}
    for question in questions:
        results[question] = analyze_image_from_url(image_url, question)
    return results

# 사용 예시
if __name__ == "__main__":
    # 예시 1: 단일 이미지 기본 분석
    # image_url1 = "https://example.com/sample_image.jpg"
    image_url1 = "https://imgnews.pstatic.net/image/119/2024/12/26/0002907944_001_20241226113111421.jpeg"
    basic_prompt = "이 이미지에서 보이는 것을 자세히 설명해주세요."
    
    print("기본 이미지 분석:")
    result1 = analyze_image_from_url(image_url1, basic_prompt)
    print(result1)
    print("-" * 50)

    # 예시 2: 여러 이미지 일괄 분석
    # image_urls = [
    #     "https://example.com/image1.jpg",
    #     "https://example.com/image2.jpg",
    #     "https://example.com/image3.jpg"
    # ]
    #
    # print("여러 이미지 일괄 분석:")
    # results2 = batch_analyze_images(image_urls, "이미지의 주요 객체를 나열해주세요.")
    # for url, result in results2.items():
    #     print(f"\nURL: {url}")
    #     print(f"분석 결과: {result}")
    # print("-" * 50)

    # 예시 3: 하나의 이미지에 대한 다양한 질문
    detailed_questions = [
        "이미지에서 보이는 사람들의 표정과 감정을 설명해주세요.",
        "이미지의 전반적인 분위기는 어떠한가요?",
        "이미지에서 눈에 띄는 색상들을 설명해주세요.",
        "이미지의 구도와 촬영 기법에 대해 설명해주세요."
    ]
    
    print("다각도 이미지 분석:")
    results3 = analyze_image_with_multiple_questions(image_url1, detailed_questions)
    for question, answer in results3.items():
        print(f"\n질문: {question}")
        print(f"답변: {answer}")
