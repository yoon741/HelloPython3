# 4 수학식을 파이썬 표현식으로 변경
# 한줄에 넣어서 실행 가능 ; 붙여서
x = 1; y = 2; z = 3
s0 = 1; v0 = 2; t = 3; g = 9.8

# 3*x
a = 3 * x
# 3*x+y
b = 3 * x + y
# x+y/7
c = (x + y) / 7
# 3x+y/z+2
d = (3 * x + y) / (z + 2)
# 등가속도 공식
e = s0 + v0 * t + 1 / 3 * g * t ** 2

# 12
# 생년월일을 이용해서 나이를 계산하는 프로그램을 작성
# 만나이 : 현재년도 - 태어난년도, 생일안지남 (-1) (민법상, 2023-06부터)
currentYear = int(input('현재년도는?'))
birthYear = int(input('생일의 년도는?'))
isPass = bool(input('생일 지남 여부는? (True/False)'))

myAge = currentYear - birthYear
# myAge = myAge if (isPass == True) else (myAge - 1)
myAge = myAge if isPass else (myAge - 1)

print(f'''현재년도는 {currentYear}이고, 
생일의 년도가 {birthYear}일때, 
나이는 {myAge} 입니다. ''')

# 14
# TimeTime
day = 86400   # 하루 - 초
hour = 3600   # 시간 - 초
minute = 60   # 분 - 초

days = 1234567890 / day
hour = 98765 / hour
minute = 12345 / minute

print(f'''
{int(days):,} 일
{int(hour):,} 시간
{int(minute):,} 분
''')

#---입력 가능한 형식
days = int(input('몇초?'))
day = 86400
print(f'{int(days / day):,} 일')

hours = int(input('몇초?'))
hour = 3600
print(f'{int(hours / hour):,} 시간')

minute = int(input('몇초?'))
minutes = 60
print(f'{int(minutes / minute):,} 분')

# 16
# 고객에게 돌려줘야 하는잔돈을 화폐단위로 계산 하는 프로그램 작성
# 잔돈charge 계산
price = int(input('계산할 돈을 입력하세요.'))
paid = int(input('받은 돈을 입력하세요.'))
charge = paid - price

# w50000 = charge / 50000       # 결과 float
# w50000 = int(charge / 50000)  # 결과 정수형으로 변환
w50000 = charge // 50000      # 파이썬의 몫 연산
# charge = charge - (10000 * w10000)
# charge = charge % 10000
# charge %= 10000
w10000 = charge // 10000
charge %= 10000
w5000 = charge // 5000
charge %= 5000
w1000 = charge // 1000
charge %= 1000
w500 = charge // 500
charge %= 500
w100 = charge // 100
charge %= 100
w50 = charge // 50
charge %= 50
w10 = charge // 10
charge %= 10

print(f'''
금액 : {price:,} 원
지불금액 : {paid:,} 원 
잔돈 : {paid - price:,} 원
------------------------
50000원 : {w50000} 장
10000원 : {w10000} 장
5000원 : {w5000} 장
1000원 : {w1000} 장
500원 : {w500} 장
100원 : {w100} 장
50원 : {w50} 장
10원 : {w10} 장
''')
