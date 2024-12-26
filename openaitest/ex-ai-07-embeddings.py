# OpenAI 임베딩 생성 및 유사도 계산 예제
from openai import OpenAI
import numpy as np

client = OpenAI()

def generate_embedding(text):
    """
    텍스트의 의미를 벡터로 변환합니다.
    
    Parameters:
        text (str): 벡터로 변환할 텍스트

    Returns:
        list: 1536 차원의 벡터 또는 에러 메시지
        
    특징:
        - 반환되는 벡터는 1536 차원
        - 텍스트의 의미적 특성을 수치화하여 표현
        - 유사도 계산, 검색, 분류 등에 활용 가능
    """
    try:
        response = client.embeddings.create(
            model="text-embedding-ada-002",  # OpenAI의 텍스트 임베딩 모델
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        return f"Error generating embedding: {str(e)}"

def calculate_similarity(embedding1, embedding2):
    """
    두 임베딩 벡터 간의 코사인 유사도를 계산합니다.

    Parameters:
        embedding1, embedding2 (list): 비교할 두 임베딩 벡터

    Returns:
        float: 코사인 유사도 (-1 ~ 1 사이의 값)
               1에 가까울수록 유사도가 높음
    """
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))

def find_most_similar(target_text, text_list):
    """
    주어진 텍스트와 가장 유사한 텍스트를 찾습니다.

    Parameters:
        target_text (str): 기준이 되는 텍스트
        text_list (list): 비교할 텍스트 리스트

    Returns:
        tuple: (가장 유사한 텍스트, 유사도 점수)
    """
    target_embedding = generate_embedding(target_text)
    similarities = []
    
    for text in text_list:
        current_embedding = generate_embedding(text)
        similarity = calculate_similarity(target_embedding, current_embedding)
        similarities.append((text, similarity))
    
    return max(similarities, key=lambda x: x[1])

# 사용 예시
if __name__ == "__main__":
    # 예시 1: 두 문장의 유사도 비교
    text1 = "오늘 날씨가 좋네요"
    text2 = "날씨가 정말 화창하네요"
    text3 = "어제 영화를 봤어요"

    emb1 = generate_embedding(text1)
    emb2 = generate_embedding(text2)
    emb3 = generate_embedding(text3)

    similarity1 = calculate_similarity(emb1, emb2)
    similarity2 = calculate_similarity(emb1, emb3)

    print(f"'{text1}'와 '{text2}'의 유사도: {similarity1}")
    print(f"'{text1}'와 '{text3}'의 유사도: {similarity2}")

    # 예시 2: 여러 문장 중 가장 유사한 것 찾기
    target = "맛있는 저녁 식사"
    candidates = [
        "오늘 저녁 뭐 먹지?",
        "내일 아침 날씨",
        "맛집 추천해주세요",
        "운동하는 방법"
    ]

    most_similar_text, similarity_score = find_most_similar(target, candidates)
    print(f"\n'{target}'와 가장 유사한 문장: '{most_similar_text}'")
    print(f"유사도 점수: {similarity_score}")
