import openai

def analyze_image(image_path):
    try:
        # 이미지 파일 열기
        with open(image_path, "rb") as image_file:
            # OpenAI API 호출 (이미지 분석)
            response = openai.Image.create(
                file=image_file,
                model="gpt-4-vision-preview"
            )

        # 분석 결과 반환
        return response

    except Exception as e:
        return {"error": str(e)}


# 테스트: 로컬 이미지 파일 분석
if __name__ == "__main__":
    image_path = "example_image.jpg"  # 분석할 이미지 파일 경로 설정
    result = analyze_image(image_path)
    print(result)
