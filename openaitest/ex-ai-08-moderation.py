# OpenAI 콘텐츠 중재 API 사용 예제
from openai import OpenAI

client = OpenAI()


def check_content(text):
    """
    텍스트 콘텐츠의 안전성을 검사합니다.

    Parameters:
        text (str): 검사할 텍스트

    Returns:
        dict: 다음 카테고리별 위험도 점수
            - hate: 혐오 발언
            - hate/threatening: 위협적인 혐오 발언
            - self-harm: 자해 관련
            - sexual: 성적인 내용
            - sexual/minors: 미성년자 관련 성적 내용
            - violence: 폭력적인 내용
            - violence/graphic: 심각한 폭력적 내용

    점수 해석:
        - 0에 가까울수록 안전
        - 1에 가까울수록 위험
    """
    try:
        response = client.moderations.create(
            input=text
        )
        return response.results[0]
    except Exception as e:
        return f"Error checking content: {str(e)}"


def format_moderation_result(result):
    """
    중재 결과를 읽기 쉽게 포맷팅합니다.

    Parameters:
        result: 중재 API 응답 결과

    Returns:
        str: 포맷팅된 결과 문자열
    """
    if isinstance(result, str):
        return result

    formatted_result = "콘텐츠 분석 결과:\n"
    formatted_result += f"위험 여부: {'위험' if result.flagged else '안전'}\n\n"

    formatted_result += "카테고리별 점수:\n"
    # 직접 속성에 접근
    formatted_result += f"- hate: {result.category_scores.hate:.4f}\n"
    formatted_result += f"- hate/threatening: {result.category_scores.hate_threatening:.4f}\n"
    formatted_result += f"- self-harm: {result.category_scores.self_harm:.4f}\n"
    formatted_result += f"- sexual: {result.category_scores.sexual:.4f}\n"
    formatted_result += f"- sexual/minors: {result.category_scores.sexual_minors:.4f}\n"
    formatted_result += f"- violence: {result.category_scores.violence:.4f}\n"
    formatted_result += f"- violence/graphic: {result.category_scores.violence_graphic:.4f}\n"

    return formatted_result


# 사용 예시
if __name__ == "__main__":
    # 예시 1: 안전한 텍스트 검사
    safe_text = "오늘은 날씨가 정말 좋네요. 공원에서 산책하고 싶어요."
    result1 = check_content(safe_text)
    print("안전한 텍스트 분석:")
    print(format_moderation_result(result1))
    print("-" * 50)

    # 예시 2: 잠재적 위험 텍스트 검사
    risky_text = "I hate everyone and everything!"
    result2 = check_content(risky_text)
    print("잠재적 위험 텍스트 분석:")
    print(format_moderation_result(result2))
    print("-" * 50)

    # 예시 3: 여러 문장 동시 검사
    mixed_text = """
    First sentence: Hello, how are you?
    Second sentence: I will hurt you.
    Third sentence: Let's have coffee.
    """
    result3 = check_content(mixed_text)
    print("복합 텍스트 분석:")
    print(format_moderation_result(result3))