'''
파일명: Ex02-8-dict.py
딕셔너리(Dictionary):
   - key:value 쌍으로 이루어진 자료구조
   - key는 중복 불가, 순서 없음
   - 실제 데이터를 구조화하는데 유용
'''

# 1. 딕셔너리 생성과 접근
pokemon = {
   "name": "피카츄",
   "type": "전기",
   "level": 25,
   "moves": ["전기충격", "아이언테일"]
}
print('포켓몬 정보:', pokemon)
print('이름:', pokemon["name"])          # 대괄호로 접근
print('타입:', pokemon.get("type"))      # get()으로 접근

# 2. 딕셔너리 수정
print('수정 전:', pokemon)
pokemon["level"] = 30                    # 값 수정
pokemon.update({"ability": "정전기"})      # 새 항목 추가
print('수정 후:', pokemon)

# 3. 딕셔너리 삭제 메서드
trainer = {
   "name": "지우",
   "age": 10,
   "badges": 8,
   "region": "관동"
}
print('트레이너 정보:', trainer)

removed_value = trainer.pop("age")       # 특정 키 삭제
print(f'삭제된 정보: {removed_value}')

last_item = trainer.popitem()            # 마지막 항목 삭제
print('마지막 삭제 항목:', last_item)

# 4. 딕셔너리 메서드
print('모든 키:', trainer.keys())         # 키 목록
print('모든 값:', trainer.values())       # 값 목록
print('모든 쌍:', trainer.items())        # (키, 값) 쌍