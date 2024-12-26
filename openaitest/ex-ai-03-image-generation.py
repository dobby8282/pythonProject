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
        n (int): 생성할 이미지 수 (최대 1)

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
