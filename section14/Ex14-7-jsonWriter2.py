'''
파일명: Ex14-7-jsonWriter2.py
'''
import json

dict_list = [
    {
        'name': 'james',
        'age':20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name': '홍길동',
        'age':21,
        'spec': [
            168.5,
            60.5
        ]
    }
]
# indent 들여쓰기, ensure_ascii=False 한글읽기
json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)
with open('dictList.json', 'w', encoding='UTF-8') as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다.')












