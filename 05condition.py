# 조건문
# 주어진 상황에 따라 적절한 명령문을 수행하는 문장
# 프로그래밍에서 조건을 판단하여
# 해당 조건에 맞는 상황을 수행하는데 사용됨
# 파이썬에서 조건문 작성시 반드시 들여쓰기를 사용함을 명심

# 파이썬의 코드 블록
# 특정한 동작을 위해 관련된 코드를 한곳에 모아둔 것
# 이런한 코드들은 반드시 같은 들여쓰기 내에 존재해야 함

# if 문
# if 조건식:
#    조건이 참일때 수행할 문장(들)

# 속도위반 경고하기

# 짝수 판별하기
num = int(input('숫자는? '))

# :기호가 있다면 다음줄은 꼭 들여쓰기(tap)를 해야함
# 같은 코드로 인식을 못함
if num % 2 == 0:
    print('짝수입니다')

# 코드 간략화 (짧을 때만) 한줄에 쓰거나 들여쓰기 필수
if num % 2 == 0: print('짝수입니다')

# if ~ else
# if문은 조건이 참일 경우에만 지정한 코드를 실행하는데 비해
# if ~ else문은 조건이 참일때와 거짓일때 각각 지정한 코드를
# 실행한다는 것이 다름
# if 조건식:
#       수행할문장1
# else:
#       수행할문장2

# 짝수/홀수 출력프로그램
num = int(input('숫자는? '))

if num % 2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다')

# pass
# 조건문/반복문/함수/클래스이나 다른 문 등에서
# 실행문이 정해지지 않은 경우 임시로 작성하는 명령문
if num % 2 == 0:
    pass
else:
    pass


# 마일리지 사용하기
mileage = 1200

# 판별과 동시에 출력을 하기 때문에 기능이 애매모호 하다.
# if mileage >= 1000:
#     print('마일리지 사용가능!')
# else:
#     print('마일리지 사용불가!')

# print는 비용이 듦으로 나눠 짜는 것이 좋다.
# result = ''
# if mileage >= 1000:
#     result = '마일리지 사용가능!'
# else:
#     result = '마일리지 사용불가!'

# result를 비우지 않고 조건에 맞지 않는
# 문구를 넣어서 하면 더 간략히 가능하다.
result = '마일리지 사용불가!'
if mileage >= 1000:
    result = '마일리지 사용가능!'

print(result)

# 중첩 if 문
# if 문 속에 또 다른 if 문을 포함시켜 작성하는 조건문
# 조건문을 중첩할때는 들여쓰기에 유의해야 함
# 다양한 조건에 따라 결과를 처리하고 싶을 때 사용 - 복잡함

# 평균점수에 따라 ABCDF 학점을
# 처리하는 조건문 작성 (중첩 if문 사용)
avg = 73.5

grade = 'F'
if avg >= 90:
    grade = 'A'
else:
    if avg >= 80:
        grade = 'B'
    else:
        if avg >= 70:
            grade = 'C'
        else:
            if avg >= 60:
                grade = 'D'

print(grade)

# 다중 if문
# 중첨 if문을 작성하는 경우, 조건이 많으면 다소 복잡함
# 이러한 중첨 if문을 단순하게 작성할 수 있는 조건문
# if 조건1:
#     실행할 코드1
# elif 조건2:
#     실행할 코드2
# elif 조건3:
#     실행할 코드3
# elif:
#     실행할 코드4

# 평균점수에 따라 ABCDF 학점을
# 처리하는 조건문 작성(다중 if문 사용)

avg = 85.5

grade = 'F'
if avg >= 90:
    grade = 'A'
elif avg >= 80:
      grade = 'B'
elif avg >= 70:
      grade = 'C'
elif avg >= 60:
      grade = 'D'

print(grade)

# if 조건문 대체 1 - switch 모방
# 조건이 많아 지는 경우, 다중 조건문은 역시 복잡해 짐
# 이럴 경우, dict 자료구조를 이용하면 간단하게 작성 가능

# if 조건문 대체 2
# python 3.10부터 switch와 비슷한 match ~ case 문 도입
# match 값:
#   case 값범위1: 실행문1
#   case 값범위2: 실행문2
#   default: 실행문2

# 주민번호 성별코드에 따른 성별 출력
# 1: 남자 (2000년 이전 출생)
# 2: 여자 (2000년 이전 출생)
# 3: 남자 (2000년 이후 출생)
# 4: 여자 (2000년 이후 출생)

code = int(input('성별코드는?'))

result = ''
match code:
    case 1: result = '남자 (2000년 이전 출생)'
    case 2: result = '여자 (2000년 이후 출생)'
    case 3: result = '남자 (2000년 이전 출생)'
    case 4: result = '여자 (2000년 이후 출생)'
    case _: result = '외국인이군요!'

print(result)


# 다중 if 문으로 작성한 학점계산 코드를
# match case로 바꿔 작성해보세요
avg = 85.5

match int(avg/10):
    case 10 | 9: grade = 'A'
    case 8: grade = 'B'
    case 7: grade = 'C'
    case 6: grade = 'D'
    case _: grade = 'F'

print(grade)


# ---예제---
# 속도 위반 경고
# 자동 온도 조절 장치
# 자동 주문 시스템

# 국가재난지원금 수령액 조회하기
count = int(input('인원수를 입력하세요.'))

result = ''
match count:
    case 1: result = '400,000원 지원'
    case 2: result = '600,000원 지원'
    case 3: result = '800,000원 지원'
    case _: result = '1,000,000원 지원'

print(result)

# 개선 된 BMI 지수 출력
# 버스 전용차로 단속
# 마스크 구매 가능 요일 출력

# 차량 2부제
# 생존율 출력
# 전기 요금 계산기