# OpenAI Assistant API 사용 예제
from openai import OpenAI
import time
import json

client = OpenAI()

class MathTutor:
    """
    수학 튜터 어시스턴트를 생성하고 관리하는 클래스
    """
    def __init__(self):
        self.assistant = None
        self.thread = None
        
    def create_assistant(self):
        """
        수학 튜터 어시스턴트를 생성합니다.
        """
        self.assistant = client.beta.assistants.create(
            name="Math Tutor",
            instructions="""
            당신은 수학 튜터입니다. 다음과 같은 방식으로 학생들을 도와주세요:
            1. 문제를 단계별로 자세히 설명
            2. 핵심 개념 설명 포함
            3. 유사한 예제 제공
            4. 학생이 이해하기 쉽게 설명
            """,
            model="gpt-4-turbo-preview",
            tools=[{"type": "code_interpreter"}]  # 수식 계산을 위한 코드 인터프리터 활성화
        )
        self.thread = client.beta.threads.create()
        return self.assistant

    def ask_question(self, question):
        """
        어시스턴트에게 질문을 하고 응답을 받습니다.

        Parameters:
            question (str): 수학 관련 질문

        Returns:
            str: 어시스턴트의 응답 또는 에러 메시지
        """
        try:
            # 스레드에 메시지 추가
            message = client.beta.threads.messages.create(
                thread_id=self.thread.id,
                role="user",
                content=question
            )

            # 어시스턴트 실행
            run = client.beta.threads.runs.create(
                thread_id=self.thread.id,
                assistant_id=self.assistant.id
            )

            # 완료될 때까지 대기
            while True:
                run = client.beta.threads.runs.retrieve(
                    thread_id=self.thread.id,
                    run_id=run.id
                )
                if run.status == 'completed':
                    break
                elif run.status == 'failed':
                    return "죄송합니다. 응답 생성에 실패했습니다."
                time.sleep(1)

            # 응답 메시지 가져오기
            messages = client.beta.threads.messages.list(
                thread_id=self.thread.id
            )
            return messages.data[0].content[0].text.value

        except Exception as e:
            return f"Error: {str(e)}"

def format_math_response(response):
    """
    수학 문제 응답을 보기 좋게 포맷팅합니다.
    """
    formatted = "-" * 50 + "\n"
    formatted += "수학 튜터 응답:\n"
    formatted += "-" * 50 + "\n"
    formatted += response + "\n"
    formatted += "-" * 50
    return formatted

# 사용 예시
if __name__ == "__main__":
    # 수학 튜터 초기화
    tutor = MathTutor()
    tutor.create_assistant()

    # 예시 1: 2차 방정식 풀이
    question1 = "x² + 5x + 6 = 0 방정식을 풀어주세요."
    response1 = tutor.ask_question(question1)
    print(format_math_response(response1))

    # 예시 2: 삼각함수 개념 설명
    question2 = "사인, 코사인, 탄젠트의 기본 개념을 설명해주세요."
    response2 = tutor.ask_question(question2)
    print(format_math_response(response2))

    # 예시 3: 적분 문제
    question3 = "∫x²dx의 계산 과정을 설명해주세요."
    response3 = tutor.ask_question(question3)
    print(format_math_response(response3))
