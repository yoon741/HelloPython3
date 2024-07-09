# 실전예제 1
# 비밀번호 메일 발송 프로그램
name = '홍길동'
email = 'gildong@abc.com'
id = 'gildong'
passwd = 1234

print(f'''To. {email} \n▶ 아이디 및 비밀번호 확인 \n  {name} 고객님 안녕하세요. \n  {name} 고객님의 아이디와 비밀번호는 아래와 같습니다. \n  아이디 : {id} \n  비밀번호 : {passwd}''')

# 위에 방식으로 가능하지만 밑에 처럼해도 가능
print(f'''To. {email} 
▶ 아이디 및 비밀번호 확인
  {name} 고객님 안녕하세요. 
  {name} 고객님의 아이디와 비밀번호는 아래와 같습니다. 
  아이디 : {id} 
  비밀번호 : {passwd}''')


# 실전예제 2
# 날씨 예보 프로그램
day = input('요일은?')
date = input('날짜(월일)은?')
minTemp = input('최저 기온은?')
maxTemp = input('최고 기온은?')
rainy = input('비올확률은?')
dusty = input('미세먼지는?')
riseSun = input('일출시간은?')
dowmSun = input('일몰시간은?')
southWave = input('남해 물결높이는?')
eastWave = input('동해 물결 높이는?')
westWave = input('서해 물결 높이는?')

day = '월'
date = '3월 30일'
minTemp = -1
maxTemp = 10
rainy = 45
dusty = '좋음'
riseSun = '오전 6시 30분'
dowmSun = '오후 7시 20분'
southWave = 0.5
eastWave = 1.5
westWave =0.5

print(f'''내일 날씨 예보입니다.
{day}요일인 {date}의 아침 최저 기온은 {minTemp}도, 낮 최고 기온은 {maxTemp}도로 예보됐습니다.
비올 확률은 {rainy}%이고, 미세먼지는 {dusty} 수준일 것으로 예상됩니다.
일출 시간은 {riseSun}이고, 일몰 시간은 {dowmSun}입니다.
바다의 물결은 남해 앞바다 {southWave}m, 동해 앞바다 {eastWave}m, 서해 앞바다 {westWave}m 높이로 일겠습니다.
지금까지 {date} {day}요일 날씨 예보였습니다.''')

#영수증예제
rstrName = '음식나라'
menu1 = '소주'
menu2 = '너나치킨'
m1price = 3000
m2price = 12000
money = 50000
date = '2014. 07. 07 14:35:24'

print([ rstrName ])
print('----------------------')
print(menu1, '   ', 2, '     ', m1price * 2)
print(menu2, '', 1, '     ', m2price * 1)
print('----------------------')
print('과세합계', '        ', round((m1price * 2 + m2price * 1) / 10 * 9))
print('부가세', '          ', round((m1price * 2 + m2price * 1) / 10))
print('----------------------')
print('총합계', '          ', round(m1price * 2 + m2price * 1))
print('받은금액', '        ', money)
print('받은금액', '        ', money - (m1price * 2 + m2price * 1))
print('----------------------')
print(date)

# 3
# 다음중 파이썬 변수로 사용 가능한 것은 무엇인지 서술하여라.
# rete1, 1stPlayer, myprogram.java, long, TimeLimit, numberOfWindows
# 답 : rete1, long, TimeLimit, numberOfWindows


# 11
# 이름과 몸무게, 나이를 변수로 선언하고 자신의 것을 값으로 초기화하는 프로그램을 작성
# MyInfo

name = '홍길동'
weight = 15.5
age = 99

name = input('이름은?')
weight = input('몸무게는?')
age = input('나이는?')

print(name, weight, age)

# 12
# 생년월일을 이용해서 나이를 계산하는 프로그램을 작성하여라.
# MyAge
# 년나이 계산 : 현재년도 - 태어난년도
# 만나이 : 현재년도 - 태어난년도, 생일안지남(-1) (민법상, 2023-06 부터)
# 한국식 나이 : 현재년도 - 태어난년도 + 1

birthYear = int(input('생일의 년도는?'))
currentYear = int(input('현재년도는?'))

# 연나이
MyAge = currentYear - birthYear
print(f'''현재년도는 {currentYear}이고, 생일의 년도가 {birthYear}일때, 
나이는 {MyAge} 입니다. ''')

#한국식 나이
MyAge2 = currentYear - birthYear + 1
print(f'''현재년도는 {currentYear}이고, 생일의 년도가 {birthYear}일때, 
나이는 {MyAge2} 입니다. ''')

# 13
# 구구단 중 7단을 출력하는 프로그램을 작성하여라
# GuGu7Dan

# 단순한 방법...
#print('7 * 1 = ', 7 * 1,'\n7 * 2 = ', 7 * 2, '\n7 * 3 = ', 7 *3,'\n7 * 4 = ', 28,
#'\n7 * 5 = ', 7 * 5, '\n7 * 6 = ', 7 * 6, '\n7 * 7 = ', 7 * 7,'\n7 * 8 = ', 7 * 7,
#'\n7 * 9 = ', 7 * 9)

#print('''7 x 1 = 7
#7 x 2 = 14
#7 x 3 = 21
#7 x 4 = 28
#7 x 5 = 35
#7 x 6 = 42
#7 x 7 = 49
#7 x 8 = 56
#7 x 9 = 63''')

dan = 7
print(f'''
{dan} x 1 = {dan * 1}
{dan} x 2 = {dan * 2}
{dan} x 3 = {dan * 3}
{dan} x 4 = {dan * 4}
{dan} x 5 = {dan * 5}
{dan} x 6 = {dan * 6}
{dan} x 7 = {dan * 7}
{dan} x 8 = {dan * 8}
{dan} x 9 = {dan * 9}''')





# gpt...
def print_gugudan(dan):
      for i in range(1, 10):
            print(f"{dan} * {i} = {dan * i}")
# 7단 출력
print_gugudan(7)
print_gugudan(3)
