# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장, 조회, 수정, 삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리
# 대량의 데이터를 처리할때 속도를 높이고, 메모리를 절약할 수 있음

# 리스트
# 다른 프로그래밍 언어에서 배열array과 유사
# 동일한 유형의 데이터를 1차원형태로 순차적으로 저장하는 자료구조
# 선언방법은 []에 값들을 하나씩 정의
# 리스트의 각 요소를 참조하려면 변수명[위치값] 형식을 사용

# 과일 데이터 저장
fruits = ['사과','포도','수박','참외','복숭아']
print(fruits)

# 점심 메뉴를 리스트로 선언
menus = ['라면', '돈까스', '냉면', '햄버거', '정식']
print(menus)

# 리스트에서 요소elements, item별로 출력
# 첫번째 요소의 위치값index은 0부터 시작
print(menus[0], menus[1], menus[4])
print(menus[5])    # index 범위 벗어남 - 오류발생

# 동적으로 리스트 추가하기
menus = []

# 리스트에 요소를 추가하려면 append(값) 함수 사용
# 추가된 요소는 리스트 맨뒤에 부착 - LIFO
menus.append('라면')
menus.append('돈까스')
menus.append('우동')
menus.append('햄버거')
menus.append('정식')
print(menus)

# 리스트에는 다른 유형의 데이터도 저장 가능 (비추!)
complexs = [1, 10.1, 'a', 'abc123', True]
print(complexs)

# 리스트 요소 수정 : 변수명[위치] = 새로운값
print(menus)
menus[2] = '탕수육'  # 탕수육으로 변경

# 리스트 요소 삭제 : remove(값) - 값으로 삭제
menus.remove(('탕수육'))
print(menus)

# 리스트 요소 삭제 : pop(위치) - 위치로 삭제
menus.pop(1)
print(menus)

# len() 함수 - 리스트의 요소 갯수 또는 문자열 길이 출력
print(len(menus))
print(len('Hello,World!!'))

# 입력받은 글자 수 확인
msg = input('메세지를 입력하세요 : ')
print(f'입력받은 메세지 길이 : {len(msg)}')


# -----------------------
# 합격여부 판정프로그램
exam = [55, 35, 40, 70, 65, 30]

# 과락여부
cntFail = 0
for i in range(6):
    if exam[i] < 40: cntFail += True

# 평균
sum = 0
for i in range(6):
    sum += exam[i]
avg = sum / 6

# 합격여부
passed = '아쉽습니다. 불합격하셨습니다.'
if cntFail < 1 and avg >= 60:
    passed = '축하합니다!. 합격하셨습니다.'

# 평가
print(f'''
40점 미만 과목수 : {cntFail}
평균 점수 : {avg:.1f}
결과 : {passed}
''')


# -----------------------
# 혈액 보관 시스템
bloods = []
cntblood = [0,0,0,0]
msg = '''헌혈해 주셔서 감사합니다. 헌혈하신 혈액형은?
(A, B, AB, O) : '''

for i in range(10):
    bloods.append(input(msg))

for i in range(10):
    if bloods[i] == 'A': cntblood[0] += 1
    elif bloods[i] == 'B': cntblood[1] += 1
    elif bloods[i] == 'AB': cntblood[2] += 1
    elif bloods[i] == 'O': cntblood[3] += 1


line = '-' * 20
# result = f'''
# {line}
# 혈액형 : 개수
# {line}
# A형 : {cntblood[0]}
# B형 : {cntblood[1]}
# AB형 : {cntblood[2]}
# O형 : {cntblood[3]}
# {line}
# '''
result = f'''
{line}
혈액형 : 개수
{line}
A형 : {bloods.count('A')}
B형 : {bloods.count('B')}
AB형 : {bloods.count('AB')}
O형 : {bloods.count('O')}
{line}
'''
print(result)


# -----------------------
