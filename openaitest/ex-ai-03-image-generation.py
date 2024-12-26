'''
DALL-E 3 API - 이미지 생성하기
   OpenAI의 DALL-E 3 모델을 사용하여 텍스트 설명(프롬프트)으로 이미지를 생성

주요 매개변수
   1. model
       - "dall-e-3": DALL-E의 최신 모델
       - 고품질의 사실적인 이미지 생성 가능

   2. prompt (필수)
       - 생성할 이미지에 대한 자세한 텍스트 설명
       - 구체적이고 명확한 설명일수록 원하는 결과 얻기 쉬움

   3. size (선택)
       - "1024x1024": 정사각형 (기본값)
       - "1024x1792": 세로형
       - "1792x1024": 가로형

   4. quality (선택)
       - "standard": 일반 품질 (기본값)
       - "hd": 고품질 (비용 증가)

   5. n (선택)
       - 생성할 이미지 수
       - DALL-E 3는 현재 n=1만 지원

반환값
   - 생성된 이미지의 URL
   - 에러 발생시 에러 메시지 반환

주의사항
   - API 사용량에 따른 비용 발생
   - 이미지 품질과 크기에 따라 비용 차이
   - 적절한 프롬프트 작성이 중요
'''

# DALL-E를 사용한 이미지 생성 예제
from openai import OpenAI
import base64

client = OpenAI()


def generate_image(prompt, size="1024x1024", quality="standard", n=1):
    """
    DALL-E 3 모델을 사용하여 텍스트 설명을 바탕으로 이미지를 생성합니다.

    Parameters:
        prompt (str): 생성할 이미지에 대한 상세한 설명
        size (str): 이미지 크기 ("1024x1024", "1024x1792", "1792x1024")
        quality (str): 이미지 품질 ("standard" 또는 "hd")
        n (int): 생성할 이미지 수 (DALL-E 3 최대 1 DALL-E 2 최대 10)

    Returns:
        str: 생성된 이미지의 URL 또는 에러 메시지
    """
    try:
        response = client.images.generate(
            model="dall-e-3",  # DALL-E의 최신 모델
            prompt=prompt,
            size=size,
            quality=quality,  # 고품질 이미지는 "hd" 사용
            n=n  # DALL-E 3는 현재 n=1만 지원
        )
        return response.data[0].url
    except Exception as e:
        return f"Error generating image: {str(e)}"


# 사용 예시
if __name__ == "__main__":
    # 예시 1: 기본 이미지 생성
    prompt1 = "한국의 전통 한옥과 현대적 고층 빌딩이 조화롭게 어우러진 도시 풍경"
    result1 = generate_image(prompt1)
    print(f"기본 이미지 생성 결과: {result1}")

    # 예시 2: 고품질 세로 이미지 생성
    prompt2 = "벚꽃이 만발한 경복궁의 봄 풍경"
    result2 = generate_image(
        prompt2,
        size="1024x1792",
        quality="hd"
    )
    print(f"고품질 세로 이미지 생성 결과: {result2}")

    # 예시 3: 가로 이미지 생성
    prompt3 = "제주도의 푸른 바다와 오름이 있는 자연 풍경"
    result3 = generate_image(
        prompt3,
        size="1792x1024",
        quality="standard"
    )
    print(f"가로 이미지 생성 결과: {result3}")