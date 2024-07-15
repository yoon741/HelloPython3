# 반복문
# 특정 문장 / 코드를 지정한 횟수/조건에 반복 실행하는 문장

# 간단한 메세지 한번 출력
print('Hello, Pytion!!')

# 간단한 메세지 여러번 출력
print('Hello, Pytion!!')
print('Hello, Pytion!!')
print('Hello, Pytion!!')

# 메세지를 수정한다면? - 번거로움
print('Hello, Cloud!!')
print('Hello, Cloud!!')
print('Hello, Cloud!!')

# 만약, 반복문을 사용한다면?
# 반복의 용이성과 수정의 편리함을 제공

#파이썬의 반복문
# for     :  지정한 횟수만큼 반복 수행
# while   :  지정한 조건에 의해 반복 수행

# 횟수에 따른 반복 - for
# 반복횟수는 range() 함수로 유추가능 : 종료값-1 - 시작값
# for 카운트변수 in range(시작값, 종료값-1, 간격):
#      반복할 문장

# range 함수
# 시작값과 종료값-1 사이의 연속된 정수 반환
print(1,2,3,4,5,6,7,8,9,10)

print(list(range(1,10+1)))
print(list(range(1,10+1, 2)))

# for 사용예시
# for i in [1,2,3,4,5,6,7,8,9,10]:
for i in range(1,10+1):
    print(i)

for i in range(1,3+1):   # start ~ end-1
    print(f'Hello, World!! {i}')

for i in range(3):      # 0 ~ end-1
    print(f'Hello, World!! {i}')

for _ in range(3):      # count변수 생략
    print('Hello, World!!')

# 1 ~ 100 사이 모든 정수의 합 구하여 출력
sum = 0
for i in range(1, 100+1):
    sum = sum + i
print(sum)

# 1 ~ 100 사이 모든 짝수의 합 구하여 출력
sum = 0
for i in range(2, 100+1,2):
    sum = sum + i
print(sum)

# 메일발송
count = int(input('메일 발송 횟수를 입력하세요.'))

for _ in range(count):
    print('메일발송!')


# for문을 이용해 1~10 사이의 정수를 출력,
# 단, 정수가 3의 배수라면 '3의 배수!' 출력
result = ''

for i in range(1, 10+1):
    result += f'num = {i}\n'
    if i % 3 == 0:
        result += f'3의 배수!!\n'

print(result)


# 1~10까지 정수의 합 구하기
sum = 0
for i in range(1, 10+1):
    sum = sum + i
print(sum)

# 5단 출력
num = 5
for i in range(1, 9+1, 1):
    result = num * i
    print(result)


dan = 7
result = ''
for i in range(1, 9+1):
    result += f'{dan} x {i} = {dan * i}\n'
print(result)

# 출력할 때 줄바꿈 없이 출력하기 (end='')
# 1~10까지
result = ''

for i in range(1,10+1):
    # print(i, end=' ')
    result += f'{i} '

print(result)

# range 함수
for i in range(-10, 0, 1):
    print(i, end=' ')

print(list(range(-10,0+1, 1)))
print(list(range(10,0, -1)))

# 문자열을 for문에 사용하기
str = 'Hello, World!!'

for c in str:
    print(c, end='')

# 50보다 작은 7의 배수
result = ''
for i in range(50, 0):
    result += 5            # 끝까지 하지 않음 나중에 이어서


# 369게임 369가 들어갈 경우 갯수만큼 짝! 같이 출력 1 ~ 99
# 숫자 범위에 따라서 나누기
for i in range(1,100+1):
    if i < 10:
        if i % 3 == 0:
            print(f'{i} 짝!')
        else:
            print(i)
    else:
        clap = ''
        fnum = i // 10
        lnum = i % 10          # 숫자를 뽑아 낼 수 있다.
        if fnum % 3 == 0: clap += '짝! '
        if lnum % 3 == 0 and lnum != 0: clap += '짝! '
        print(f' {i} {clap}')


# 1 ~ 100사이 정수중에서 3과 7의
# 공배수와 최소 공배수를 출력
result = ''
for i in range(1, 100+1):
    if (i % 3 == 0) and (i % 7 ==0):
        result += f'{i} '

print(result, f'[{3 * 7}]')

# 한빛역에서 동시에 9시에 6시까지
# 운행하는 열차들이 교차하는 시간을 구해 열차 충돌 막기
trainA = 10
trainB = 25
trainC = 30

result = ''
for min in range(0, 540+1):
    if min % trainA == 0 and min % trainB == 0:   # 50분 간격
        hour = 9 + min // 60
        min  = min % 60
        print(f'{hour}시 {min}분 : A - B 교차!')

    elif min % trainB == 0 and min % trainC == 0:
        hour = 9 + min // 60
        min  = min % 60
        print(f'{hour}시 {min}분 : B - C 교차!')

    elif min % trainC == 0 and min % trainA == 0:   # 30분 간격
        hour = 9 + min // 60
        min  = min % 60
        print(f'{hour}시 {min}분 : C - A 교차!')

# -----모두 한번에 출동하는 시각-----
trainA = 10
trainB = 25
trainC = 30

for min in range(0, 540+1):
    if min % trainA == 0 and min % trainB == 0 and min % trainC == 0:
        hour = 9 + min // 60
        min  = min % 60
        print(f'{hour}시 {min}분 : 교차!')




# 로그인 기능 만들기
isLogin = False

for i in range(5):
    # if isLogin == False:
    if not isLogin:
        passwd = input('관리자 암호를 입력하세요. ')

        if passwd == 'hanbitca':
            isLogin = True
            print('로그인 되었습니다.')
        else:
            print('암호를 다시 확인하세요.')

if not isLogin: print('로그인 실패! 횟수 초과!')