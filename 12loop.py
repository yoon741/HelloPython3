# while 문
# 조건을 만족할 때까지 반복 수행 - 반복횟수는 모름

# 변수 = 초기값
# while 조건식:
#     반복할문장
#     변수증가/감소

# 1 ~ 10 까지 정수 출력
# for i in range(1, 10+1):
#     print(i, end=' ')
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1

# 1 ~ 50 사이 정수 중 홀수만 출력

i = 1
while i <= 50:
    print(i, end=' ')
    i += 2  # 2개씩 증가하여 실행하므로 25번만 실행하면 됨

i = 1
while i <= 50:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1  # 1개씩 증가하여 하나씩 대조하므로 50번 실행하면 됨

# 1 ~ 50 사이 정수 중 9의 배수만 출력
i = 1
while i <= 50:
    if i % 9 == 0:
        print(i, end=' ')
    i += 1

# 반복문 내 실행 중지 : break
# for, while 문 내에서 반복흐름을 벗어나기 위해 사용

# 1 ~ 10000사이 정수의 합을 출력
# 단, 정수의 합이 123456578보다 크면 계산을 중지

# for
sum = 1

for i in range(1, 10000 + 1):
    if sum > 12345678: break
    sum += i

print(sum, i)

# while
i = 1
sum = 0
while i < 10000 + 1:
    if sum > 12345678: break
    sum += i
    i += 1

print(sum, i)

# 1 ~ 100사이 정수중에서
# 3과 8의 공배수와 최소 공배수를 출력
# while로 작성
result = ''

for i in range(1, 100+1):
    if i % 3 == 0 and i % 8 ==0:
        result += f'{i} '

print(result, f'[{3 * 8}]')


# 삼각형 너비 계산하기
limitArea = 150   # 반복 중단 삼각형 너비
width = 2
heigth = 3
i = 1

while True:
    area = ((width * i) * (heigth * i)) / 2
    if area > limitArea: break
    print(f'삼각형 너비 : {width * i} / {heigth * i} = {area}')
    i += 1



# 값 in str(문자열)
# '3' in str(36)
# '6' in str(36)
# '9' in str(12)

# 369게임 369가 들어갈 경우 갯수만큼 짝! 같이 출력 1 ~ 99
# 숫자 범위에 따라서 나누기
# while로 작성
i = 1
while i < 100:
    jjak = ''
    if '3' in str(i): jjak += ' 짝!'
    if '6' in str(i): jjak += ' 짝!'
    if '9' in str(i): jjak += ' 짝!'
    if i == 33 or i == 66 or i == 99 : jjak += ' 짝!'
    print(i, jjak)
    i += 1


# 한빛역에서 동시에 9시에 6시까지
# 운행하는 열차들이 교차하는 시간을 구해 열차 충돌 막기
trainA = 10
trainB = 25
trainC = 30
mins = 1


while mins < 541:
    if mins % 5 == 0:

        if mins % trainA == 0 and mins % trainB == 0:
            print(f'{9 + mins // 60:02d}시 {mins % 60:02d}분 : A - B 교차!')

        elif mins % trainB == 0 and mins % trainC == 0:
            print(f'{9 + mins // 60:02d}시 {mins % 60:02d}분 : B - C 교차!')

        elif mins % trainC == 0 and mins % trainA == 0:
            print(f'{9 + mins // 60:02d}시 {mins % 60:02d}분 : C - A 교차!')

        elif mins % trainA == 0 and mins % trainB == 0 and mins % trainC == 0:
            print(f'{9 + mins // 60:02d}시 {mins % 60:02d}분 : A - B - C 교차!')

    mins += 1

# 로그인 기능 만들기
cntLogin = 1
while True:
    passwd = input('관리자 암호를 입력하세요. ')

    if passwd == 'hanbitca':
        print('로그인 되었습니다.')
        break
    else:
        print('암호를 다시 확인하세요.')

    if cntLogin < 5: cntLogin += 1
    else:
        print('로그인 실패! 횟수 초과!')
        break


# 반복문 내 건너뛰기 : continue
# for, while문 내에서 반복흐름을 일시적으로 넘기기 위해 사용

# 1 ~ 10 사이 정수 중 홀수의 합 출력
sum = 0

for i in range(1, 10+1):
    if i % 2 == 0: continue
    sum += i

print(sum)


# 1 ~ 100 사이 정수의 합을 출력
# 단, 3의 배수나 7의 배수는 제외
# for문으로
sum = 0

for i in range(1, 100+1):
    if i % 3 == 0 or i % 7 == 0: continue
    sum += i

print(sum)



# while문으로
sum = 0
i = 0

while i < 101:
    i += 1
    if i % 3 == 0 or i % 7 == 0: continue
    sum += i

print(sum)

