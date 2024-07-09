# 변수 variable
# 어떤 값을 저장하는 장소(메모리)를 기억하기 쉽게 문자로 나타낸 것
# 변수에 값이 저장되는 공간을 메모리라고 함
# 변수에 값을 넣어라고 선언하면,
# 시스템 상의 메모리 어딘가에 공간을 확보하고,
# 그 공간의 실제주소와 이름을 연관mappiing함

# 이름과 나이를 저장하는 변수 선언
# 변수명 = 값
a = '홍길동'
b = 99

name = '홍길동'     # 의미있는 단어로 변수 선언
age = 99

Name = '일지매'     # 변수명은 대소문자 구분

# 변수에 저장된 값을 출력하려면 print 함수 사용
# print(변수명, 변수명, ...)   < 바로출력 (자바는 한가지 씩만, 파이썬은 여러가지 출력 가능)
print(name, age)

a = 'Hong gil dong'
b = 'Computer'

myName = 'Hong gil dong'
myMajor = 'Computer'

print(myName, myMajor)
print(a, b)


# 변수 선언 후 값 변경
intro = 'Hello, python'    # < 표현식
print(intro)               # < 명령문

intro = '안녕하세요, 파이썬'
print(intro)


# 변수명 작성 규칙
# 데이터의 의미를 쉽게 파악가능하게
# 소문자로
# 두개 이상의 단어를 조합할 경우 낙타표기법으로
# 특수문자는 _이외에 사용할 수 없
# 첫글자는 숫자를 사용할 수 없고 나머지 자리에서만 사용
# 예약어는 변수명으로 사용할 수 없음
# 파이썬 예약어 확인
import keyword
print(keyword.kwlist)


# 자료형 datatype
# 정적 static 자료형
# 변수선언시 자료형도 함께 지정
# 변수의 자료형은 컴파일 시간에 결정 - 오류발생 적음
# string name = '홍길동'
#        name = 123 (오류발생! - 선언시 자료형과 대입시 값의 자료형이 다름)

# 동적 dynamic 자료형
# 변수선언시 자료형은 생략 가능, 추론기능으로 자동할당
# 변수의 자료형은 실행 시간에 결정 - 오류발생 여지 존재
# 변수에 대입하는 값에 따라 자료형이 바뀔수도 있음
# name = '홍길동'
# name = 123   (문제없음! - 변수의 자료명은 자동으로 바뀜)

# ex) 회원정보 저장용 변수 선언
# 아이디, 비번, 이름, 나이, 이메일
# 결혼여부, 보유금액, 등록일
userid = 'abc123'
passwd = '987xyz'
name = '홍길동'
age = 99
email = 'abc123@987xyz.co.kr'
maried = True    # < 꼭 대문자로
money = 10000
reDate = '2024-07-09 12:15:35'


# 파이썬에서 제공하는 자료형 - 정수integer, 실수float, 문자string, 블리언boolean
# primitive data type - 메모리에 데이터(값) 그 자체를 저장

# 문자형
# 파이썬에서 문자char와 문자열string을 문자형로 취급
# 문자형은 ''나 ""를 이용해서 정의 - ''를 편리해서 추천!
# 여러줄 문자열text을 작성할 때에는 ''' '''를 사용
str1 = 'Hello, World!!'
str2 = "Hello, World!!"
str3 = "insert into member \
values ('', '', '')"
str4 = "Hello, \nWorld!!"    # \n : 내려쓰기
str5 = '''Hello,
World!!'''
print(str1, str2, str3, str4, str5)

# 정수형 - 소수점 이하의 값이 없는 숫자
int1 = 123
int2 = 1234561234567 # 큰 정수도 표현가능
int3 = 0b00001000  # 0b : 2진수
int4 = 0x0000FFFF  # 0x : 16진수

print(int1, int2, int3, int4, hex(65535), bin(65535))
                            # 함수 hex(값) : 16진수 /  bin(값) : 2진수

# 실수형 - 소수점 이하의 값이 있는 숫자
# 부동소수점floating point 실수 : 국제표준에 따라 실수를 표기하는 방식
# 즉, 실수를 정수부와 정수의 곱으로 된 지수로 표현하는 것을 의미
# 123.456 = 123456 x 10^-3 (소수점이 뒤로간 만큼 10^-3 곱함)
# 단, 파이썬에서는 유효숫자 e지수를 이요해서 지수부를 표현
# 123.456 = 123456 x e-3

float1 = 3.141213
float2 = 123.456
float3 = 123456e-3

print(float1, float2, float3)

# 부동소수점과 오차
# 컴퓨터에서는 숫자는 2진수 기반으로  표현하기 때문에
# 실수는 정확하게 나타내기 어려움! - 단지, 근사값으로만 표현
# 0.1 + 0.2 == 0.3

print(0.1 + 0.2, 0.3)
print(round(0.1 + 0.2, 5), round(0.3, 5))

# 논리형
# 논리적인 값으르 표현할 때 사용 - 참True(1), 거짓False(0)
# 논리연산(조건식), 조건문, 상태를 표시하는 플래그 변수
bool1 = True
bool2 = False

print(bool1, bool2, bool1 == 1, bool2 == 0)

# 리터럴

# type 함수 : 리터럴이나 변수의 자료형 출력
print(type(str1), type(int1), type(float1), type(bool1))
print(type('Hello'), type(123), type(3.14), type(True))

# 자료형 변환(type conversion / casting)
# 어떤 자료형에서 다른 자료형으로 변환하는 것
# 암시적implicit 변환 - 자동으로 컴파일러가 변환
# 명시적explicit 변환 - 개발자가 직접 변환(int, str, float, bool)
result1 = 5 + 3.14152
print(result1, type(result1))  # 정수 + 실수 = 실수 타입으로 변환 (float type)

result2 = True + 1    # 블리언 + 정수 = 정수 타입으로 변환 (int type)
print(result2, type(result2))

result3 = 3 == 4  # 정수 == 정수 (정수끼리 비교했을 때 float로 자동형 변환됨)
print(result3, type(result3))

print(type(int1), str(int1), type(str(int1)))
# print(type(str1), int(str1))  # 실행불가

str6 = '3.14152'
# print(type(str6), int(str6), type(int(str6)))  # 실행불가
print(type(str6), float(str6), type(float(str6)))

print(bool(''), bool('abc123'))  # 문자를 bool로 변환시

# 사용자로부터 값을 입력받아 변수 초기화
# 변수명 = input(메세지)
# 주의! - input함수로 입력받은 값은 무조건 문자로 취급됨
# 입력받은 값을 산술식으로 사용할 것이라면 int를 입력해 정수로 적용

# 이름과 나이를 입력받아서 출력
name = input('이름은?')
age = input('나이는?')

print(name, age)

# 환율 계산프로그램 작성
# 달러를 입력하면 원화로 계산해서 출력 (1$ -> 1382.12원)
dollar = input('달러는?')
won = int(dollar) * 1382.12
print(dollar, won)


# 문자열 템플릿
# 파이썬에서 문자열 속에 변수를 포함시켜 출력할때 유용하게 사용하는 방법
# f-string : python 3.6부터 도입
# f'문자열 {변수명:포맷팅}'

lang = 'python'
print('Hello,', lang, '!!')
print(f'Hello, {lang} !!')   # f-string으로 문자열 속 변수를 넣어 출력 가능

# 날씨예보 프로그램
riseSun = '오전 6시 30분'
dowmSun = '오후 7시 20분'

print(f'일출시간은 {riseSun}이고, 일몰시간은{dowmSun}입니다.')

