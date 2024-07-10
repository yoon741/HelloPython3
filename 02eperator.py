# 수식 expression
# 숫자, 변수, 연산자를 이요해서 수학적 관계를 나타내는 것
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 -> 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 산술연산자 : 변수나 상수에 적용하여 계산을 수행하고,
#                           그 결과를 다른 변수에 할당하거나 출력
# 자료형 승격 promotion

# <예제>
# 매출액 입력시 총합 출력
sale1 = int(input('1월 매출 : '))
sale2 = int(input('2월 매출 : '))
sale3 = int(input('3월 매출 : '))
totalSale = sale1 + sale2 + sale3
print(f'1분기 전체 매출 : {totalSale}')

# 1분기 수익 계산
Sales = int(input('1분기 매출 : '))
buys = int(input('1분기 매입 : '))
profit = Sales - buys
print(f'1분기 수익 : {profit} 원')

# 방의 넓이 구하기
width = int(input('가로길이는? '))
height = int(input('세로길이는? '))
area = width * height
print(f'넓이 : {area}cm²')

# 신체질량지수BMI 구하기
weight = float(input('몸무게는?'))
height = float(input('키는?'))
bmi = weight / (height * height)
print(int(bmi))

# 홀짝 게임
coins = int(input('손안에 동전수를 입력하세요!'))
if coins % 2 == 0:
    print(1)
else:
    print(0)
#다른 방법
coins = int(input('손안에 동전수를 입력하세요!'))
result = coins % 2

print(f'{result}')
print(f'{coins % 2}')

# 빵 나누기
breads = 97
divsor = 33
studs = 97 // 3
mods = 97 % 3
print(f'''
빵을 나누어 줄수 있는 학생 수 : {studs}
남는 빵 갯수 : {mods}''')

# 전염병 예상 감염자 구하기
infectors = 2 ** 30

print(f'전염병 예상 감염자 수 : {infectors}')