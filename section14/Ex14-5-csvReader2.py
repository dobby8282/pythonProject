'''
파일명: Ex14-5-csvReader2.py

회원명단.csv
"회원명",수강과목,등록일
"강나라",필라테스,25일
"나유라",수영,25일
"이상기",헬스,15일
'''
member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"')
        member[2] = member[2].strip('\n')

        member_list.append(member)

print(member_list)





