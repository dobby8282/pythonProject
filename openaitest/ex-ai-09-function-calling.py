'''
OpenAI Function Calling - AI와 함수 연동하기
   AI가 사용자의 요청을 분석하여 적절한 함수를 호출하고 결과를 반환하는 시스템
   자연어 입력을 프로그래밍 함수 호출로 변환

주요 구성요소
   1. 함수 정의 (tools)
       - name: 함수 이름
       - description: 함수 설명
       - parameters: 매개변수 정의
           - type: 데이터 타입
           - properties: 속성 목록
           - required: 필수 매개변수

   2. 서비스 클래스
       - 실제 기능을 수행하는 클래스
       - 외부 API 연동 등을 처리
       - 예: WeatherService, CalendarService

   3. 처리 과정
       - 사용자 입력 분석
       - 적절한 함수 선택
       - 함수 실행 및 결과 획득
       - 결과를 자연어로 변환

활용 사례
   - 날씨 정보 조회
   - 일정 관리
   - 예약 시스템
   - 데이터베이스 조작
   - 외부 API 연동
'''

# OpenAI Function Calling 예제
from openai import OpenAI
import json
import datetime
import requests

client = OpenAI()

class WeatherService:
    """날씨 정보를 제공하는 서비스 클래스"""
    
    def get_weather(self, location):
        """실제 구현시에는 날씨 API를 호출해야 합니다"""
        # 예시 데이터 반환
        return {
            "temperature": 20,
            "condition": "맑음",
            "humidity": 60,
            "wind_speed": 5
        }

class CalendarService:
    """일정 관리 서비스 클래스"""
    
    def add_event(self, title, date, time):
        """실제 구현시에는 캘린더 API를 호출해야 합니다"""
        return {
            "status": "success",
            "event": {
                "title": title,
                "datetime": f"{date} {time}"
            }
        }

def handle_function_calling(user_input):
    """
    사용자 입력을 분석하여 적절한 함수를 호출하고 결과를 반환합니다.

    Parameters:
        user_input (str): 사용자의 질문이나 요청

    Returns:
        str: AI의 응답 또는 에러 메시지
    """
    try:
        # 사용 가능한 함수들 정의
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "특정 지역의 현재 날씨 정보를 조회합니다",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "날씨를 조회할 도시 이름"
                            }
                        },
                        "required": ["location"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "add_event",
                    "description": "캘린더에 새로운 일정을 추가합니다",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "일정 제목"
                            },
                            "date": {
                                "type": "string",
                                "description": "일정 날짜 (YYYY-MM-DD 형식)"
                            },
                            "time": {
                                "type": "string",
                                "description": "일정 시간 (HH:MM 형식)"
                            }
                        },
                        "required": ["title", "date", "time"]
                    }
                }
            }
        ]

        # 서비스 인스턴스 생성
        weather_service = WeatherService()
        calendar_service = CalendarService()

        messages = [{"role": "user", "content": user_input}]

        # AI에게 메시지 전송
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        response_message = response.choices[0].message

        print(f'response_message: {response_message}')
        
        # 함수 호출이 필요한 경우
        if response_message.tool_calls:
            tool_call = response_message.tool_calls[0]
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            # 적절한 함수 호출
            if function_name == "get_weather":
                result = weather_service.get_weather(function_args["location"])
            elif function_name == "add_event":
                result = calendar_service.add_event(
                    function_args["title"],
                    function_args["date"],
                    function_args["time"]
                )
            
            # 함수 실행 결과를 AI에게 전달
            messages.append(response_message)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": json.dumps(result)
            })
            
            # 최종 응답 생성
            final_response = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=messages
            )
            return final_response.choices[0].message.content
        
        return response_message.content

    except Exception as e:
        return f"Error in function calling: {str(e)}"

# 사용 예시
if __name__ == "__main__":
    # 예시 1: 날씨 정보 요청
    weather_query = "서울의 오늘 날씨는 어때?"
    print("질문:", weather_query)
    print("응답:", handle_function_calling(weather_query))
    print("-" * 50)

    # 예시 2: 일정 추가 요청
    calendar_query = "다음 주 월요일 오후 2시에 팀 미팅 일정을 추가해줘"
    print("질문:", calendar_query)
    print("응답:", handle_function_calling(calendar_query))
    print("-" * 50)

    # 예시 3: 복합 요청
    complex_query = "내일 오전 9시에 병원 예약이 있는데, 그 때 날씨가 어떨지 알려줘"
    print("질문:", complex_query)
    print("응답:", handle_function_calling(complex_query))