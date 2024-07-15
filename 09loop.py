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

# for문을 이용해 구구단 5단 출력하기
num = 5

for i in range(1,10,1):
    result = num * i
    print(f'{num} x {i} = {result}')

# for문을 이용해 1~10 사이의 정수를 출력,
# 단, 정수가 3의 배수라면 '3의 배수!' 출력

#p.16 풀다 맘 if else문 사용 가능