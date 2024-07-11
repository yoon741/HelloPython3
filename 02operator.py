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
sales = int(input('1분기 매출 : '))
buys = int(input('1분기 매입 : '))
profit = sales - buys
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

# 할당 연산자

# 논리 연산자

# 논리 연산자 단축식 평가

# 삼항 연산자
# 조건문을 한 줄로 표현할 수 있는 연산자
# 조건식이 참일 때의 값 if 조건식 else 거짓일 때의 값

myScore = 75
result = '합격!' if myScore >= 90 else '불합격!'

print(result)

# 복리 계산기
# 일년에 500만원씩 5년간, 연 5%
money = 5_000_000
rate = 0.05
money = money + (money * rate)
money = money + (money * rate)
money = money + (money * rate)
money = money + (money * rate)
money = money + (money * rate)
print(f'5년 후 총 수령액 : {int(money):,} 원')

# -------다른 방식
money = 5000000
interestRate = 0.05
years = 5
total = int(money * (interestRate + 1) ** years)
print(f'5년 후 총 수령액 : {total} 원')

# 범퍼카 탑승
#if문으로 작성
child = int(input('어린이의 신장을 입력하세요.'))
isRide = 'True' if (child >= 120) else 'False'
print(result)
# isRide로 작성
child = int(input('어린이의 신장을 입력하세요.'))
isRide = (child >= 120)
print(f'{isRide}')

# 범퍼카 탑승 가능 판별
#if문으로 작성
height = int(input('어린이의 신장을 입력하세요.'))
result = 'True' if (height >= 120) and (height <= 150) else 'False'
print(result)
# isRide로 작성
child = int(input('어린이의 신장을 입력하세요.'))
isRide = (child >= 120) & (child < 170)
print(f'{isRide}')

# 적자/흑자 판별
income = int(input('수입을 입력하세요: '))
outcome = int(input('지출을 입력하세요: '))
result = '흑자' if (income > outcome) else '적자'  #조건식은 괄호로 묶는 것이 보기 좋음
print(result)
